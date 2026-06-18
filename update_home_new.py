# -*- coding: utf-8 -*-
"""トップページ(index.html)の「新着記事」セクションを、blog/index.html の最新記事で自動再生成する。
原因: auto_publish は blog/index.html だけ更新し、トップの新着ウィジェット(ハードコード)を放置していた。
→ 公開のたびにこれを呼べばトップの新着も最新に保たれる。"""
import re
from pathlib import Path

HERE = Path(__file__).parent
BLOG = HERE / "blog" / "index.html"
ROOT = HERE / "index.html"
N = 10            # 表示件数
NEW_BADGE = 3     # 先頭何件にNEWバッジ

CAL_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
           '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>'
           '<line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/>'
           '<line x1="3" y1="10" x2="21" y2="10"/></svg>')

def parse_cards(html):
    """blog/index.html を上から順に解析。(slug,img,title,date,cat) のリストを返す。"""
    cards = []
    for m in re.finditer(r'<div class="blog-card"[^>]*>(.*?)<span class="blog-card-date">([^<]+)</span>',
                         html, re.S):
        block, date = m.group(1), m.group(2).strip()
        href = re.search(r'href="([^"]+\.html)"', block)
        img = re.search(r'<img src="([^"]+)"', block)
        title = re.search(r'class="blog-card-title">([^<]+)</', block)
        tag = re.search(r'class="blog-card-tag">([^<]+)</', block)
        if not (href and title):
            continue
        slug = href.group(1)
        # サムネは小さめサイズに(144x96)
        src = img.group(1) if img else "https://images.unsplash.com/photo-1513885535751-8b9238bd345a?w=144&h=96&fit=crop"
        src = re.sub(r'w=\d+&h=\d+', 'w=144&h=96', src)
        cards.append({
            "slug": slug, "img": src,
            "title": title.group(1).strip(),
            "date": date,
            "cat": tag.group(1).strip() if tag else "ギフト",
        })
    return cards

def build_li(c, badge=False):
    b = '\n      <span class="new-badge">NEW</span>' if badge else ''
    return (f'    <li><a href="blog/{c["slug"]}">\n'
            f'      <img class="new-article-thumb" src="{c["img"]}" alt="" loading="lazy">\n'
            f'      <div class="new-article-info">\n'
            f'        <div class="new-article-title">{c["title"]}</div>\n'
            f'        <div class="new-article-meta"><span class="new-article-date">{CAL_SVG}{c["date"]}</span>'
            f'<span>{c["cat"]}</span></div>\n'
            f'      </div>{b}\n'
            f'    </a></li>')

def main():
    cards = parse_cards(BLOG.read_text(encoding="utf-8"))[:N]
    if not cards:
        print("カード0件。中断。"); return
    lis = "\n".join(build_li(c, i < NEW_BADGE) for i, c in enumerate(cards))
    new_ul = f'<ul class="new-articles-list">\n{lis}\n  </ul>'
    root = ROOT.read_text(encoding="utf-8")
    new_root, n = re.subn(r'<ul class="new-articles-list">.*?</ul>', new_ul, root, count=1, flags=re.S)
    if n == 0:
        print("新着ULが見つからない。中断。"); return
    ROOT.write_text(new_root, encoding="utf-8")
    print(f"トップ新着を更新: {len(cards)}件 (先頭: {cards[0]['date']} {cards[0]['title'][:24]})")

if __name__ == "__main__":
    main()
