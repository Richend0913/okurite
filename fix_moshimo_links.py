# -*- coding: utf-8 -*-
"""もしもアフィリ記事のボタン同一リンク問題を修正。
各商品(gift-card)と結論ボックスで、Amazonボタン→Amazon(okuritegift-22検索)、
楽天ボタン→楽天(hb.afl検索)に商品名キーワードで分離。サイト他59記事と同形式に統一。
検収: もしもリンク残0・ボタン文言↔遷移先が全商品一致。
"""
import re
from pathlib import Path
import gen_article_ai as G  # amazon(), rakuten()

BLOG = Path(__file__).parent / "blog"
MOSHI = r'href="https://af\.moshimo\.com[^"]*"'


def fix_block(block):
    """gift-card or pickup-box ブロック内のもしもボタンを商品名で分離。"""
    tm = re.search(r'(?:gift-card-title">\s*(?:\d+\.\s*)?|font-size:1\.05rem[^"]*">)([^<]+)</div>', block)
    if not tm:
        return block
    kw = tm.group(1).strip()
    # 楽天ボタン(class="gift-card-link rakuten")を先に
    block = re.sub(MOSHI + r'([^>]*class="gift-card-link rakuten")',
                   lambda m: f'href="{G.rakuten(kw)}"' + m.group(1), block)
    # Amazonボタン(class="gift-card-link")
    block = re.sub(MOSHI + r'([^>]*class="gift-card-link")',
                   lambda m: f'href="{G.amazon(kw)}"' + m.group(1), block)
    return block


def main():
    files = sorted(BLOG.glob("*.html"))
    fixed = []
    for f in files:
        h = f.read_text(encoding="utf-8", errors="ignore")
        if "af.moshimo.com" not in h:
            continue
        h2 = re.sub(r'<div class="pickup-box".*?</div>\s*</div>', lambda m: fix_block(m.group(0)), h, flags=re.S)
        h2 = re.sub(r'<div class="gift-card">.*?</div>\s*</div>', lambda m: fix_block(m.group(0)), h2, flags=re.S)
        remain = h2.count("af.moshimo.com")
        f.write_text(h2, encoding="utf-8")
        fixed.append((f.name, h.count("af.moshimo.com"), remain))
    print(f"処理: {len(fixed)}記事")
    for n, before, after in fixed:
        print(f"  {n}: もしも {before}→{after}")


if __name__ == "__main__":
    main()
