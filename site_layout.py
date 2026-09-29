# -*- coding: utf-8 -*-
"""Okurite 共通レイアウト（ヘッダー / フッター / head / ナビJS）の唯一の定義元。

全ページのデザインは css/style.css だけで決まる。各ページに <style> を直書きすると
デザインがページごとにばらけるため、このモジュールの normalize_* で除去・統一する。

  python site_layout.py          # 全ページ(記事・一覧・規約)を現行レイアウトへ統一（冪等）
  python site_layout.py FILE...  # 指定ページだけ統一

記事生成(gen_article_ai.py)・自動公開(auto_publish.py)からも呼ばれる。
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
BLOG = HERE / "blog"
CSS_VER = "4"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600'
         '&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&display=swap" rel="stylesheet">')

LOGO_MARK = ('<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true">'
             '<rect x="3" y="10" width="26" height="19" rx="5" fill="#1f4d45"/>'
             '<path d="M16 10v19M3 17h26" stroke="#faf7f2" stroke-width="2.4"/>'
             '<path d="M16 10c-1.6-4.6-7.5-6-7.5-2.6S12.6 10 16 10zm0 0c1.6-4.6 7.5-6 7.5-2.6S19.4 10 16 10z" fill="#c8711f"/>'
             '</svg>')

LOGO = (f'<a href="{{root}}" class="logo" aria-label="Okurite（おくりて）トップへ">{LOGO_MARK}'
        '<span class="logo-text"><span class="logo-word">Okurite</span><span class="logo-kana">おくりて</span></span></a>')

ICON_MENU = ('<svg class="i-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
             '<path d="M4 7h16M4 12h16M4 17h16"/></svg>'
             '<svg class="i-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
             '<path d="M6 6l12 12M18 6L6 18"/></svg>')

NAV_JS_MARK = "okurite-nav"
NAV_JS = f"""<script>/* {NAV_JS_MARK} */
(function(){{var b=document.getElementById('hamburger'),n=document.getElementById('nav');if(!b||!n)return;
b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');b.setAttribute('aria-label',o?'メニューを閉じる':'メニューを開く');}});
n.addEventListener('click',function(e){{if(e.target.closest('a')){{n.classList.remove('open');b.setAttribute('aria-expanded','false');}}}});}})();
</script>"""

AD_NOTE_MARK = 'class="ad-note"'
AD_NOTE = '<p class="ad-note">※本記事にはアフィリエイト広告（Amazon・楽天市場へのリンク）が含まれます。</p>'

# フッターのリンク群。(表示名, blog内のslug)
FOOT_SCENE = [("母の日", "mothers-day-2026"), ("父の日", "fathers-day-2026"), ("誕生日", "birthday-gift-women"),
              ("結婚祝い", "wedding-gift-guide"), ("出産祝い", "baby-shower-gift"), ("敬老の日", "keirou-no-hi-2026"),
              ("クリスマス", "christmas-gift-2026"), ("お歳暮", "oseibo-2026")]
FOOT_BUDGET = [("500円", "budget-500-gift"), ("1,000円", "gift-exchange-1000"), ("2,000円", "budget-2000-gift"),
               ("3,000円", "gift-budget-3000"), ("5,000円", "budget-5000-gift"), ("10,000円", "budget-10000-gift")]
FOOT_TARGET = [("彼氏", "gift-for-boyfriend"), ("彼女", "gift-for-girlfriend"), ("妻", "gift-for-wife-birthday"),
               ("夫", "gift-for-husband"), ("上司", "gift-for-boss"), ("祖父母", "gift-for-grandparents"),
               ("子ども", "gift-for-kids-birthday")]


def _prefixes(depth):
    """depth=0: サイト直下のページ / depth=1: blog/ 配下のページ"""
    root = "../" if depth else "./"
    blog = "./" if depth else "blog/"
    return root, blog


def header_html(depth, current="", seasonal_label=None):
    """current: 'blog' ならコラムを現在地表示。seasonal_label: トップ専用の季節特集リンク(#seasonal)"""
    root, blog = _prefixes(depth)
    home = "" if depth == 0 and seasonal_label is not None else root
    items = []
    if seasonal_label is not None:
        items.append(f'<li><a href="#seasonal">{seasonal_label}</a></li>')
    items.append(f'<li><a href="{home}#diagnosis">ギフト診断</a></li>')
    cur = ' aria-current="page"' if current == "blog" else ""
    items.append(f'<li><a href="{blog}"{cur}>コラム</a></li>')
    items.append(f'<li class="nav-cta"><a href="{home}#gifts">ギフトを探す</a></li>')
    return (f'<header class="header" id="site-header">\n'
            f'  <div class="header-inner">\n'
            f'    {LOGO.format(root=root)}\n'
            f'    <nav aria-label="メインメニュー"><ul class="nav" id="nav">\n      '
            + "\n      ".join(items) +
            f'\n    </ul></nav>\n'
            f'    <button class="hamburger" id="hamburger" type="button" aria-label="メニューを開く" aria-expanded="false" aria-controls="nav">{ICON_MENU}</button>\n'
            f'  </div>\n'
            f'</header>')


def footer_html(depth):
    root, blog = _prefixes(depth)

    def col(title, rows):
        lis = "".join(f'<li><a href="{blog}{slug}.html">{name}</a></li>' for name, slug in rows
                      if (BLOG / f"{slug}.html").exists())
        return f'<div class="footer-col"><h4>{title}</h4><ul>{lis}</ul></div>'

    return (f'<footer class="footer">\n'
            f'  <div class="footer-inner">\n'
            f'    <div class="footer-grid">\n'
            f'      <div class="footer-brand">{LOGO.format(root=root)}'
            f'<p>シーン・予算・相手から、贈って喜ばれるギフトを探せるギフト選びのメディアです。'
            f'商品はAmazon・楽天市場で購入できます。</p></div>\n'
            f'      {col("シーン別", FOOT_SCENE)}\n'
            f'      {col("予算別", FOOT_BUDGET)}\n'
            f'      {col("相手別", FOOT_TARGET)}\n'
            f'    </div>\n'
            f'    <div class="footer-bottom">\n'
            f'      <div class="footer-links"><a href="{blog}">コラム一覧</a><a href="{root}privacy.html">プライバシーポリシー</a>'
            f'<a href="{root}terms.html">利用規約</a><a href="{root}contact.html">お問い合わせ</a></div>\n'
            f'      <p>当サイトはAmazonアソシエイト・プログラム、楽天アフィリエイトに参加しており、紹介リンクから収益を得ることがあります。</p>\n'
            f'      <p>&copy; 2026 Okurite</p>\n'
            f'    </div>\n'
            f'  </div>\n'
            f'</footer>')


def head_links(depth):
    root, _ = _prefixes(depth)
    return (f'<!-- okurite-head -->\n  {FONTS}\n'
            f'  <link rel="icon" href="{root}images/favicon.svg" type="image/svg+xml">\n'
            f'  <link rel="stylesheet" href="{root}css/style.css?v={CSS_VER}">\n'
            f'  <!-- /okurite-head -->')


# ---------------------------------------------------------------- blog categories
# コラム一覧の絞り込みカテゴリ。(data-cat値, 表示名)。auto_publish の新記事もここで分類する。
BLOG_CATS = [("parents-day", "母の日・父の日"), ("birthday", "誕生日"), ("celebration", "お祝い"),
             ("anniversary", "記念日"), ("season", "季節の贈り物"), ("business", "職場・お礼"),
             ("budget", "予算別"), ("other", "その他")]

_CAT_RULES = [
    ("budget", r"budget|gift-exchange-1000|thank-you-gift-casual"),
    ("parents-day", r"mothers-day|fathers-day|father-in-law|mother-in-law"),
    ("anniversary", r"anniversary"),
    ("season", r"ochugen|oseibo|obon|christmas|valentine|white-day|keirou|summer|natsu|shochu|new-school-term"),
    ("business", r"boss|coworker-(?!wedding)|farewell|job-transfer|teacher|retirement"),
    ("birthday", r"birthday|gift-for-(?:girlfriend|boyfriend|husband|teens|friend)"),
    ("celebration", r"congratulations|entrance|graduation|university|socialite|promotion|moving|hikkoshi|housewarming|"
                    r"wedding|baby|birth|kanreki|coming-of-age|academic|new-car|new-life|alone-living|newlyweds|"
                    r"new-dad|inner-blessing|grandparents|job"),
]


def blog_category(slug):
    for cat, pat in _CAT_RULES:
        if re.search(pat, slug):
            return cat
    return "other"


# ---------------------------------------------------------------- normalize

def _replace_block(html, tag, new):
    """最初の <tag ...>...</tag> を new に置換（無ければ None）。"""
    m = re.search(rf"<{tag}\b[^>]*>.*?</{tag}>", html, re.S)
    if not m:
        return None
    return html[:m.start()] + new + html[m.end():]


def _normalize_head(html, depth):
    # 旧 head 部品を除去: ページ内<style>、Google Fonts、旧CSSリンク、旧統一ブロック
    html = re.sub(r"\s*<!-- okurite-head -->.*?<!-- /okurite-head -->", "", html, flags=re.S)
    html = re.sub(r"\s*<style[^>]*>.*?</style>", "", html, flags=re.S)
    html = re.sub(r'\s*<link rel="preconnect"[^>]*>', "", html)
    html = re.sub(r'\s*<link[^>]*fonts\.googleapis\.com/css2[^>]*>', "", html)
    html = re.sub(r'\s*<link rel="stylesheet" href="[^"]*css/style\.css[^"]*">', "", html)
    html = re.sub(r'\s*<link rel="icon"[^>]*>', "", html)
    return html.replace("</head>", "  " + head_links(depth) + "\n</head>", 1)


def _chrome(html, depth, current="", seasonal_label=None):
    h = _replace_block(html, "header", header_html(depth, current, seasonal_label))
    if h is None:
        h = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + "\n" + header_html(depth, current, seasonal_label), html, count=1)
    html = h
    f = _replace_block(html, "footer", footer_html(depth))
    if f is None:
        f = html.replace("</body>", footer_html(depth) + "\n</body>", 1)
    html = f
    if NAV_JS_MARK not in html:
        html = html.replace("</body>", NAV_JS + "\n</body>", 1)
    return html


PICKUP_RE = re.compile(
    r'<div class="pickup-box" style="[^"]*">\s*<div style="[^"]*">結論：迷ったらこれ</div>\s*'
    r'<div style="[^"]*">(.*?)</div>\s*<div class="gift-card-buttons" style="[^"]*">', re.S)
BANNER_RE = re.compile(
    r'\s*<div style="display:flex;align-items:center;gap:10px;background:linear-gradient\(135deg,#(?:c62828|2e7d32)[^"]*">'
    r'.*?</span>\s*</div>', re.S)
PICK_RE = re.compile(r'<div style="background:linear-gradient\(135deg,#fff8f0,#fff0e0\);border:2px solid #c49b1a;[^"]*">(.*?)\n    </div>', re.S)


def _editor_pick(m):
    inner = m.group(1)
    ps = iter(["ep-label", "ep-title"])
    inner = re.sub(r'<p style="[^"]*">', lambda _m: f'<p class="{next(ps, "ep-text")}">', inner)
    inner = re.sub(r'<a ([^>]*?) style="[^"]*">', r'<a \1 class="btn btn-primary">', inner)
    inner = inner.replace('rel="noopener" class="btn', 'rel="noopener sponsored" class="btn')
    return f'<div class="editor-pick">{inner}\n    </div>'


def normalize_article(html):
    html = _normalize_head(html, 1)
    html = _chrome(html, 1)
    html = html.replace('<div style="height:60px;"></div>', "")
    # 結論ボックス: インラインstyle → クラス
    html = PICKUP_RE.sub(lambda m: ('<div class="pickup-box">\n      <div class="pickup-label">結論：迷ったらこれ</div>\n'
                                    f'      <div class="pickup-name">{m.group(1)}</div>\n      <div class="gift-card-buttons">'), html)
    # 期限切れの季節の告知バナー（父の日6/21・母の日・お中元の「今週がラスト」等）を除去
    html = BANNER_RE.sub("", html)
    html = PICK_RE.sub(_editor_pick, html)
    # urgent-box 内の色直書きを除去
    html = re.sub(r'(<div class="(?:urgent-box|label|ttl)") style="[^"]*"', r"\1", html)
    # 広告表記（ステマ規制対応）: メタ行の直後に1回だけ
    if AD_NOTE_MARK not in html:
        html = re.sub(r'(<div class="article-meta">.*?</div>)', lambda m: m.group(1) + "\n    " + AD_NOTE, html, count=1, flags=re.S)
    return html


def normalize_doc(html):
    """privacy / terms / contact"""
    html = _normalize_head(html, 0)
    html = _chrome(html, 0)
    html = html.replace("<main>", '<main class="doc-page">', 1)
    base = "https://richend0913.github.io/okurite/"
    html = re.sub(r'(<div class="breadcrumb">)<a href="' + re.escape(base) + r'">', r'\1<a href="./">', html)
    return html


def normalize_blog_index(html):
    html = _normalize_head(html, 1)
    return _chrome(html, 1, current="blog")


def normalize_home(html, seasonal_label):
    html = _normalize_head(html, 0)
    return _chrome(html, 0, seasonal_label=seasonal_label)


def normalize_file(path):
    p = Path(path)
    html = p.read_text(encoding="utf-8")
    if p.parent.name == "blog":
        new = normalize_blog_index(html) if p.name == "index.html" else normalize_article(html)
    elif p.name in ("privacy.html", "terms.html", "contact.html"):
        new = normalize_doc(html)
    elif p.name == "index.html":
        m = re.search(r'<a href="#seasonal">([^<]*)</a>', html)
        new = normalize_home(html, m.group(1) if m else "季節の特集")
    else:
        return False
    if new != html:
        p.write_text(new, encoding="utf-8")
        return True
    return False


def all_pages():
    pages = sorted(BLOG.glob("*.html"))
    pages += [HERE / n for n in ("index.html", "privacy.html", "terms.html", "contact.html")]
    return [p for p in pages if p.exists()]


if __name__ == "__main__":
    targets = [Path(a) for a in sys.argv[1:]] or all_pages()
    changed = sum(normalize_file(t) for t in targets)
    print(f"layout: {changed}/{len(targets)} ページを更新")
