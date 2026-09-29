# -*- coding: utf-8 -*-
"""NVIDIA無料AIでOkuriteのアフィリ記事を生成。
本文・商品推薦をLLM(meta/llama-3.3-70b)で生成し、キーワードからアフィリリンク(Amazon okuritegift-22 /
楽天アフィID)を構築、既存テンプレでHTML化して blog/ に保存。コストゼロ。
使い方: python gen_article_ai.py "還暦祝い 父 母" kanreki-gift
"""
import sys
import json
import re
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import site_layout as L

HERE = Path(__file__).parent
AMAZON_TAG = "okuritegift-22"
RAKUTEN_AFF = "522e40a0.f2dc4208.522e40a1.385f875e"
NV_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
HERO = "https://images.unsplash.com/photo-1513885535751-8b9238bd345a?w=800&h=400&fit=crop"
CARD_IMGS = [
    "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=400&h=250&fit=crop",
    "https://images.unsplash.com/photo-1607344645866-009c320b63e0?w=400&h=250&fit=crop",
    "https://images.unsplash.com/photo-1513885535751-8b9238bd345a?w=400&h=250&fit=crop",
    "https://images.unsplash.com/photo-1481437156560-3205f6a55735?w=400&h=250&fit=crop",
    "https://images.unsplash.com/photo-1556742393-d75f468bfcb0?w=400&h=250&fit=crop",
]


def nv_key():
    for cand in [HERE.parent / "short-video-maker" / ".env", HERE / ".env"]:
        if cand.exists():
            for line in cand.read_text(encoding="utf-8").splitlines():
                if line.startswith("NVIDIA_API_KEY="):
                    return line.split("=", 1)[1].strip()
    raise SystemExit("NVIDIA_API_KEY not found")


def llm(prompt, key, max_tokens=2200, retries=6):
    """NVIDIA無料枠は間欠的にタイムアウトする。リトライで空振り公開を防ぐ。"""
    body = {"model": "meta/llama-3.3-70b-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7, "max_tokens": max_tokens}
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(NV_URL, data=json.dumps(body).encode(),
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.load(r)["choices"][0]["message"]["content"]
        except Exception as e:
            last = e
            wait = 5 * (attempt + 1)
            print(f"  llm retry {attempt+1}/{retries} ({type(e).__name__}); {wait}s待機")
            try:
                import time; time.sleep(wait)
            except Exception:
                pass
    raise last


IMGDIR = HERE / "blog" / "img"
FALLBACK_IMG = "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=600&h=400&fit=crop"


def _env(name):
    for cand in [HERE / ".env", HERE.parent / "short-video-maker" / ".env"]:
        if cand.exists():
            for line in cand.read_text(encoding="utf-8").splitlines():
                if line.startswith(name + "="):
                    return line.split("=", 1)[1].strip()
    return ""


def _save(url, dest):
    try:
        data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20).read()
        if len(data) > 2500:
            dest.write_bytes(data)
            return True
    except Exception:
        pass
    return False


def _rakuten_image(kw_ja, dest):
    """楽天商品検索APIで“実際の商品写真”を取得(applicationId要)。商品サイトなので一致率が高い。"""
    appid = _env("RAKUTEN_APP_ID")
    if not appid or not kw_ja:
        return False
    try:
        u = ("https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"
             f"?applicationId={appid}&keyword={urllib.parse.quote(kw_ja)}&hits=5&imageFlag=1&sort=standard")
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "okurite/1.0"}), timeout=20))
        for it in d.get("Items", []):
            item = it.get("Item", {})
            for im in (item.get("mediumImageUrls") or []):
                url = im.get("imageUrl") if isinstance(im, dict) else im
                if url:
                    url = re.sub(r"\?_ex=\d+x\d+", "?_ex=500x500", url)
                    if _save(url, dest):
                        return True
    except Exception:
        pass
    return False


def _openverse_image(kw_en, dest):
    try:
        u = f"https://api.openverse.org/v1/images/?q={urllib.parse.quote(kw_en or 'gift')}&page_size=5&mature=false"
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "okurite/1.0"}), timeout=20))
        for r in d.get("results", []):
            src = r.get("url") or r.get("thumbnail")
            if src and src.startswith("http") and _save(src, dest):
                return True
    except Exception:
        pass
    return False


def get_image(kw_ja, kw_en, slug, idx):
    """商品画像を取得しローカル保存→相対パス。優先: 楽天“実商品写真”(一致率高)→ Openverse。失敗時None。"""
    IMGDIR.mkdir(parents=True, exist_ok=True)
    name = f"{slug}_{idx}.jpg"
    dest = IMGDIR / name
    # 楽天の実商品写真(一致率高)のみ採用。Openverse(CC検索)は「ビール→猫」等の無関係画像を返すので使わない。
    if _rakuten_image(kw_ja, dest):
        return f"img/{name}"
    # 楽天APIキーが無い/失敗時は、無関係画像を出すより category別の中立なギフト画像にフォールバック(呼び出し側)
    return None


def amazon(kw):
    return f"https://www.amazon.co.jp/s?k={urllib.parse.quote(kw)}&tag={AMAZON_TAG}"


def rakuten(kw):
    pc = urllib.parse.quote(f"https://search.rakuten.co.jp/search/mall/{kw}/", safe="")
    return f"https://hb.afl.rakuten.co.jp/ichiba/{RAKUTEN_AFF}/?pc={pc}&link_type=hybrid_url"


def gen_json(theme, key):
    prompt = f"""あなたは日本のギフト専門メディアのプロ編集者。テーマ「{theme}」のSEOブログ記事を作る。
必ず次のJSONだけを出力(前後に説明文やmarkdownは一切不要):
{{
 "title": "SEOタイトル。形式:【2026年】{theme}に喜ばれるプレゼント5選｜<相手>別おすすめ のように年・数・相手を含め35字以内",
 "desc": "検索意図に応える120字程度のメタディスクリプション",
 "keywords": "カンマ区切り6-7語",
 "intro": ["相手の気持ちに寄り添う導入(100-130字)", "記事で何が分かるかを示す導入(100-130字)"],
 "sections": [
   {{"h2":"選び方のポイント等の見出し","paras":["具体的で実用的な本文(各100-160字)","本文"]}},
   {{"h2":"見出し","paras":["本文"]}}
 ],
 "gifts": [
   {{"name":"具体的な商品名(必ず実在ブランド例を括弧で。例:名入れタンブラー(サーモス・スタンレー))","price":"¥3,000〜¥8,000","desc":"なぜその相手に喜ばれるか具体的根拠で130字","keyword":"購入につながる具体的な日本語検索キーワード","img":"商品写真用の英語キーワード1-2語(例:tumbler, wristwatch, whiskey, leather wallet)"}}
 ],
 "hero_kw": "記事トップ画像用の英語キーワード(例: fathers day gift)",
 "matome": ["まとめ段落1(100字)","背中を押すまとめ段落2(100字)"]
}}
厳守要件:
- giftsは必ず5個。各 name には**実在ブランド名の例を括弧で**入れる(汎用語『家電』『本』『旅行券』だけは禁止、必ず具体化)。
- sectionsは3〜4個。titleは必ず【2026年】と数字と相手を含む。
- 日本語。具体的で本当に役立つ内容。誇大・嘘は禁止。
- 景表法・優良誤認に配慮し、裏付けのない断定や実績主張は禁止。「実際に贈って喜ばれた」「必ず喜ばれる」「絶対に喜ばれる」「累計◯人が活用」等の体験・実績・統計の断定は使わず、「ギフトに向く」「喜ばれやすい」等の中立表現にする。"""
    raw = llm(prompt, key)
    raw = re.sub(r"^```(json)?|```$", "", raw.strip(), flags=re.M).strip()
    m = re.search(r"\{.*\}", raw, re.S)
    return json.loads(m.group(0))





def render(d, slug):
    url = f"https://richend0913.github.io/okurite/blog/{slug}.html"
    hero_img = get_image(None, d.get("hero_kw", "gift present"), slug, "hero") or FALLBACK_IMG
    toc = "\n".join(f'      <a href="#s{i}">{i+1}. {s["h2"]}</a>' for i, s in enumerate(d["sections"]))
    secs = []
    for i, s in enumerate(d["sections"]):
        ps = "\n".join(f"    <p>{p}</p>" for p in s["paras"])
        secs.append(f'    <h2 id="s{i}">{s["h2"]}</h2>\n{ps}')
    cards = []
    for j, g in enumerate(d["gifts"]):
        kw = g["keyword"]
        card_img = get_image(g['name'], g.get('img') or g['name'], slug, j) or FALLBACK_IMG
        cards.append(f'''    <div class="gift-card">
      <img class="gift-card-img" src="{card_img}" alt="{g['name']}" loading="lazy">
      <div class="gift-card-title">{j+1}. {g['name']}</div>
      <div class="gift-card-price">{g['price']}</div>
      <div class="gift-card-desc">{g['desc']}</div>
      <div class="gift-card-buttons">
        <a href="{amazon(kw)}" target="_blank" rel="noopener sponsored" class="gift-card-link">Amazonで探す</a>
        <a href="{rakuten(kw)}" target="_blank" rel="noopener sponsored" class="gift-card-link rakuten">楽天で探す</a>
      </div>
    </div>''')
    # giftカードは最初のsectionの後に差し込む
    body_secs = secs[0] + "\n" + "\n".join(cards) + "\n" + "\n".join(secs[1:])
    intro = "\n".join(f"    <p>{p}</p>" for p in d["intro"])
    matome = "\n".join(f"    <p>{p}</p>" for p in d["matome"])
    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-63VB4HT3T2"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-63VB4HT3T2');</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['title']} - Okurite</title>
  <meta name="description" content="{d['desc']}">
  <meta name="keywords" content="{d['keywords']}">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{d['title']}">
  <meta property="og:description" content="{d['desc']}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{hero_img}">
</head>
<body>
  <header></header>
  <article class="article">
    <div class="breadcrumb"><a href="../">TOP</a> &gt; <a href="./">コラム</a> &gt; {d['title']}</div>
    <h1>{d['title']}</h1>
    <div class="article-meta">{date.today().year}年{date.today().month}月{date.today().day}日 公開｜ギフト特集</div>
    <img class="article-hero" src="{hero_img}" alt="{d['title']}">
{intro}
    <div class="toc"><div class="toc-title">この記事の目次</div>
{toc}
    </div>
{body_secs}
    <div class="cta-box"><p>「結局どれにしよう」と迷ったら。<br>相手・予算・シーンを選ぶだけで、ギフトに向く商品を絞り込めます。</p>
      <a href="../#gifts" class="cta-btn">相手に合うギフトを見つける</a></div>
    <h2>まとめ</h2>
{matome}
  </article>
  <footer></footer>
</body>
</html>'''
    # ヘッダー/フッター/head/CSS は site_layout で全ページ共通のものに差し替える
    return L.normalize_article(html)


def main():
    theme = sys.argv[1] if len(sys.argv) > 1 else "還暦祝い 父 母 60歳"
    slug = sys.argv[2] if len(sys.argv) > 2 else "kanreki-gift"
    key = nv_key()
    print(f"生成中: {theme} -> blog/{slug}.html (NVIDIA llama-3.3)...")
    d = gen_json(theme, key)
    html = render(d, slug)
    out = HERE / "blog" / f"{slug}.html"
    out.write_text(html, encoding="utf-8")
    print(f"OK: {out}  ({len(html)}字)  title='{d['title']}'  gifts={len(d['gifts'])} sections={len(d['sections'])}")


if __name__ == "__main__":
    main()
