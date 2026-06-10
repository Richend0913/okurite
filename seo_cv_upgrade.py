# -*- coding: utf-8 -*-
"""Okurite 収益化改善バッチ(冪等)。URLは一切変更しない。
各記事に: ①画像lazy ②ボタン「見る」統一 ③冒頭「結論:迷ったらこれ」ボックス
④アフィリンクGA4クリック計測 ⑤関連記事3本 ⑥JSON-LD(Article+Breadcrumb, Q&AはFAQPage)。
別途: sitemap全ページ再生成 / index等metaの「母の日」整合修正。
使い方: python seo_cv_upgrade.py [--apply]   (無指定はdry-run集計)
"""
import re
import sys
import json
import html as _html
from pathlib import Path
from datetime import date

HERE = Path(__file__).parent
BLOG = HERE / "blog"
BASE = "https://richend0913.github.io/okurite"
TRACK_MARK = "okurite-aff-track"

CLICK_JS = f"""<script>/* {TRACK_MARK} */
document.addEventListener('click',function(e){{
  var a=e.target.closest&&e.target.closest('a'); if(!a||!a.href) return;
  var h=a.href, t=(a.textContent||''), d=null;
  if(h.indexOf('amazon.co.jp')>-1||h.indexOf('amzn')>-1) d='amazon';
  else if(h.indexOf('rakuten.co.jp')>-1||h.indexOf('hb.afl.rakuten')>-1) d='rakuten';
  else if(h.indexOf('moshimo')>-1||h.indexOf('a8.net')>-1||h.indexOf('valuecommerce')>-1)
    d = t.indexOf('楽天')>-1?'rakuten':(t.indexOf('Amazon')>-1?'amazon':'affiliate');
  if(d&&typeof gtag==='function') gtag('event','affiliate_click',{{affiliate:d,link_url:h,page:location.pathname}});
}},true);
</script>"""


def meta_of(htmls):
    def g(pat, d=""):
        m = re.search(pat, htmls, re.S)
        return m.group(1).strip() if m else d
    title = g(r"<title>([^<]*)</title>").replace(" - Okurite", "").replace(" | Okurite", "")
    desc = g(r'<meta name="description" content="([^"]*)"')
    h1 = g(r"<h1>(.*?)</h1>")
    h1 = re.sub(r"<[^>]+>", "", h1)
    crumb = g(r'<div class="breadcrumb">.*?コラム</a>\s*&gt;\s*([^<]+)</div>')
    return {"title": title or h1, "desc": desc, "h1": h1 or title, "crumb": crumb.strip()}


def first_product(htmls):
    """最初のgift-cardの 商品名 と ボタンリンク2つ を取得(amazon/楽天/もしも 等ドメイン非依存)。"""
    name = re.search(r'<div class="gift-card-title">\s*(?:\d+\.\s*)?([^<]+)</div>', htmls)
    links = re.findall(r'<a href="([^"]+)"[^>]*class="gift-card-link[^"]*"', htmls)
    if not name or not links:
        return None
    a = links[0]
    r = links[1] if len(links) > 1 else links[0]
    return name.group(1).strip(), a, r


def pickup_box(name, amazon, rak):
    return (
        '\n    <div class="pickup-box" style="background:linear-gradient(135deg,#fff8f0,#fdeede);'
        'border:1px solid rgba(198,40,40,.18);border-radius:14px;padding:20px 22px;margin:0 0 30px;">\n'
        '      <div style="font-size:.78rem;font-weight:700;color:#c62828;letter-spacing:.04em;margin-bottom:6px;">結論：迷ったらこれ</div>\n'
        f'      <div style="font-size:1.05rem;font-weight:700;color:#2d2a26;line-height:1.6;margin-bottom:12px;">{name}</div>\n'
        '      <div class="gift-card-buttons" style="display:flex;gap:10px;flex-wrap:wrap;">\n'
        f'        <a href="{amazon}" target="_blank" rel="noopener sponsored" class="gift-card-link">Amazonで見る</a>\n'
        f'        <a href="{rak}" target="_blank" rel="noopener sponsored" class="gift-card-link rakuten">楽天で見る</a>\n'
        '      </div>\n    </div>\n')


def jsonld_article(m, url):
    art = {"@context": "https://schema.org", "@type": "Article",
           "headline": m["h1"][:110], "description": m["desc"],
           "datePublished": "2026-01-01", "dateModified": str(date.today()),
           "author": {"@type": "Organization", "name": "Okurite"},
           "publisher": {"@type": "Organization", "name": "Okurite"},
           "mainEntityOfPage": url}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "TOP", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "コラム", "item": BASE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": m["crumb"] or m["h1"][:40], "item": url}]}
    return ('<script type="application/ld+json">' + json.dumps(art, ensure_ascii=False) + '</script>\n'
            '<script type="application/ld+json">' + json.dumps(bc, ensure_ascii=False) + '</script>\n')


def related_block(slug, registry):
    same = [(s, t) for s, t, c in registry if s != slug]
    # 同カテゴリ優先
    cat = next((c for s, t, c in registry if s == slug), "")
    pri = [(s, t) for s, t, c in registry if c == cat and s != slug]
    pick = (pri + same)[:3]
    lis = "".join(f'<li><a href="{s}.html">{t}</a></li>' for s, t in pick)
    return f'\n    <div class="related-articles"><h3>関連記事</h3><ul>{lis}</ul></div>\n'


def build_registry():
    reg = []
    for f in sorted(BLOG.glob("*.html")):
        if f.name == "index.html":
            continue
        h = f.read_text(encoding="utf-8", errors="ignore")
        m = meta_of(h)
        reg.append((f.stem, m["h1"][:48] or f.stem, m["crumb"]))
    return reg


def process(f, registry, apply):
    h = f.read_text(encoding="utf-8", errors="ignore")
    orig = h
    changes = []
    # ① lazy
    def addlazy(mm):
        tag = mm.group(0)
        return tag if "loading=" in tag else tag[:-1] + ' loading="lazy">'
    h2 = re.sub(r"<img [^>]*>", addlazy, h)
    if h2 != h: changes.append("lazy"); h = h2
    # ② ボタン「見る」統一
    if "で探す</a>" in h:
        h = h.replace("Amazonで探す", "Amazonで見る").replace("楽天で探す", "楽天で見る")
        changes.append("btn")
    # ③ 結論ボックス(無ければhero直後)
    if "pickup-box" not in h:
        prod = first_product(h)
        if prod:
            box = pickup_box(*prod)
            h, n = re.subn(r'(<img class="article-hero"[^>]*>)', lambda mm: mm.group(1) + box, h, count=1)
            if n: changes.append("pickup")
    # ④ クリック計測
    if TRACK_MARK not in h:
        h = h.replace("</body>", CLICK_JS + "\n</body>", 1)
        changes.append("track")
    # ⑤ 関連記事(無ければ</article>直前)
    if "related-articles" not in h and "</article>" in h:
        h = h.replace("</article>", related_block(f.stem, registry) + "  </article>", 1)
        changes.append("related")
    # ⑥ JSON-LD(Articleが無ければ補完)
    if '"@type": "Article"' not in h and '"@type":"Article"' not in h:
        m = meta_of(h); url = f"{BASE}/blog/{f.name}"
        h = h.replace("</head>", jsonld_article(m, url) + "</head>", 1)
        changes.append("jsonld")
    if apply and h != orig:
        f.write_text(h, encoding="utf-8")
    return changes


def main():
    apply = "--apply" in sys.argv
    reg = build_registry()
    print(f"{'APPLY' if apply else 'DRY-RUN'}: {len(reg)}記事処理")
    agg = {}
    for f in sorted(BLOG.glob("*.html")):
        if f.name == "index.html":
            continue
        ch = process(f, reg, apply)
        for c in ch: agg[c] = agg.get(c, 0) + 1
    print("変更集計:", agg)


if __name__ == "__main__":
    main()
