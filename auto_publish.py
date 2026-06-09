# -*- coding: utf-8 -*-
"""完全自律 Okurite記事パブリッシャ。
AIが既存記事を見て未カバーの新テーマを自分で考案 → 各記事をNVIDIA無料AIで生成 →
blog/index.html(コラム一覧)とsitemap.xmlに自動追加 → git commit & push でGitHub Pages公開。
使い方: python auto_publish.py [新規記事数]
"""
import sys
import re
import json
import subprocess
import urllib.request
from datetime import date
from pathlib import Path
import gen_article_ai as G

HERE = Path(__file__).parent
BLOG = HERE / "blog"
INDEX = BLOG / "index.html"
SITEMAP = HERE / "sitemap.xml"
CARD_MARK = '      <div class="blog-card" data-cat='


def existing_titles():
    out = []
    for f in BLOG.glob("*.html"):
        if f.name == "index.html":
            continue
        m = re.search(r"<title>([^<]*)</title>", f.read_text(encoding="utf-8", errors="ignore"))
        out.append((f.stem, (m.group(1).replace(" - Okurite", "") if m else f.stem)))
    return out


def ai_topics(existing, n, key):
    titles = "\n".join(t for _, t in existing[:50])
    slugs = ", ".join(s for s, _ in existing)
    prompt = f"""日本のギフトメディア「Okurite」の編集長として、まだ無い新しい記事テーマを{n}個考えて。
【既存タイトル(一部)】
{titles}
【既存slug】{slugs}
要件: 検索需要があり収益化しやすいギフト/プレゼントのテーマ。既存と重複しない切り口(例:入学祝い,新築祝い,昇進祝い,定年退職,内祝い,ペット,推し活,一人暮らし応援 等)。
次のJSON配列だけ出力(説明不要):
[{{"theme":"記事生成用の日本語テーマ(相手や予算も含め具体的に)","slug":"english-kebab-case(既存と被らない)","tag":"短いカテゴリ名"}}]"""
    raw = G.llm(prompt, key, max_tokens=900)
    raw = re.sub(r"^```(json)?|```$", "", raw.strip(), flags=re.M).strip()
    arr = json.loads(re.search(r"\[.*\]", raw, re.S).group(0))
    have = {s for s, _ in existing}
    return [t for t in arr if t.get("slug") and t["slug"] not in have][:n]


def card_html(slug, title, tag, excerpt):
    img = G.CARD_IMGS[abs(hash(slug)) % len(G.CARD_IMGS)]
    d = date.today().strftime("%Y.%m.%d") if False else f"{date.today().year}.{date.today().month:02d}.{date.today().day:02d}"
    return f'''      <div class="blog-card" data-cat="ai">
        <a href="{slug}.html">
          <div class="blog-card-img-wrap"><img src="{img}" alt="{title}" loading="lazy"></div>
          <div class="blog-card-body">
            <span class="blog-card-tag">{tag}</span>
            <h2 class="blog-card-title">{title}</h2>
            <p class="blog-card-excerpt">{excerpt}</p>
            <span class="blog-card-date">{d}</span>
          </div>
        </a>
      </div>
'''


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    key = G.nv_key()
    existing = existing_titles()
    print(f"既存{len(existing)}記事。AIが新テーマ{n}個を考案中...")
    topics = ai_topics(existing, n, key)
    print("採用テーマ:", [t["slug"] for t in topics])

    cards, sitemap_lines, published = [], [], []
    for t in topics:
        try:
            if (BLOG / f"{t['slug']}.html").exists():
                print(f"  skip {t['slug']}: 既存記事のため上書きしない"); continue
            d = G.gen_json(t["theme"], key)
            (BLOG / f"{t['slug']}.html").write_text(G.render(d, t["slug"]), encoding="utf-8")
            cards.append(card_html(t["slug"], d["title"], t.get("tag", "ギフト"), d["desc"][:55]))
            sitemap_lines.append(
                f'  <url><loc>https://richend0913.github.io/okurite/blog/{t["slug"]}.html</loc>'
                f'<lastmod>{date.today()}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>')
            published.append((t["slug"], d["title"]))
            print(f"  OK {t['slug']}: {d['title']}")
        except Exception as e:
            print(f"  NG {t['slug']}: {e}")

    if not published:
        print("公開対象なし"); return

    # index.html に挿入(最初のblog-cardの前)
    idx = INDEX.read_text(encoding="utf-8")
    pos = idx.find(CARD_MARK)
    idx = idx[:pos] + "".join(cards) + idx[pos:]
    INDEX.write_text(idx, encoding="utf-8")
    # sitemap.xml に追記(</urlset>の前)
    sm = SITEMAP.read_text(encoding="utf-8")
    sm = sm.replace("</urlset>", "\n".join(sitemap_lines) + "\n</urlset>")
    SITEMAP.write_text(sm, encoding="utf-8")
    print(f"index/sitemap更新: {len(published)}記事")

    # git公開
    msg = f"feat: AI自律生成 {len(published)}記事公開 ({', '.join(s for s,_ in published)})"
    for cmd in [["git", "add", "-A"], ["git", "commit", "-m", msg], ["git", "push", "origin", "master"]]:
        r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
        print(f"$ {' '.join(cmd[:2])}: rc={r.returncode} {(r.stderr or r.stdout).strip()[:160]}")


if __name__ == "__main__":
    main()
