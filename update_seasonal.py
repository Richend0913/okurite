# -*- coding: utf-8 -*-
"""ホームページの季節特集を“今日の日付”に合わせて自律更新する。
日付駆動カレンダーで直近の贈り物イベントを判定し、index.html の
title/meta/heroバッジ/navラベル/カウントダウン(見出し・sub・JS目標日)・特集リンクを差し替える。
リンクは実在する記事のみ採用(壊れリンク防止)。完全自動・人手不要。
"""
import re
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
INDEX = HERE / "index.html"
BLOG = HERE / "blog"
GIFT_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 12v10H4V12"/><path d="M2 7h20v5H2z"/><path d="M12 22V7"/><path d="M12 7H7.5a2.5 2.5 0 010-5C11 2 12 7 12 7z"/></svg>'

# 年間ギフトイベント暦 (月日, 名称, 見出し用jp, SEOタイトル, meta, sub, 候補リンク[(slug,text,sub)])
CAL = [
    ("02-14", "バレンタイン", "2026年2月14日（土）", "バレンタインギフト特集 2026｜本命・義理・友チョコ",
     "バレンタイン2026特集。本命・義理・自分用までシーン別におすすめチョコ・ギフトを厳選。",
     "大切な人へのバレンタイン。チョコ以外の実用ギフトも人気です。",
     [("valentine-gift", "バレンタインギフト", "本命・義理別"), ("gift-for-boyfriend", "彼氏へのギフト", "年代別おすすめ")]),
    ("03-14", "ホワイトデー", "2026年3月14日（土）", "ホワイトデーお返し特集 2026｜relations別おすすめ",
     "ホワイトデー2026特集。お返しの相場・人気ギフトをシーン別に厳選。",
     "もらって嬉しいホワイトデーのお返しを厳選しました。",
     [("white-day-gift", "ホワイトデーお返し", "相場とおすすめ"), ("gift-for-girlfriend", "彼女へのギフト", "年代別おすすめ")]),
    ("05-10", "母の日", "2026年5月10日（日）", "母の日ギフト特集 2026 シーン別プレゼント検索",
     "母の日2026特集。コスメ・スイーツ・体験ギフトなど人気商品を厳選。",
     "お母さんへの感謝を伝える母の日プレゼントを厳選しました。",
     [("mothers-day-2026", "母の日プレゼント15選", "予算別おすすめ"),
      ("mothers-day-not-flowers", "花以外のプレゼント10選", "実用的なギフト"),
      ("mothers-day-from-husband", "妻へ贈る母の日", "夫からのギフト")]),
    ("06-21", "父の日", "2026年6月21日（日）", "父の日ギフト特集 2026｜お父さんが本当に喜ぶプレゼント",
     "父の日2026特集。お父さんが本当に喜ぶプレゼントを予算別・相手別に厳選。Amazon・楽天の人気商品を比較。",
     "お父さんへ感謝を伝える父の日。実用的で喜ばれるギフトを厳選しました。",
     [("fathers-day-2026", "父の日プレゼント特集", "予算別おすすめ"),
      ("gift-for-father-in-law", "義父への父の日ギフト", "失敗しない選び方"),
      ("gift-for-new-dad", "新米パパへのギフト", "初めての父の日に")]),
    ("07-15", "お中元", "2026年7月15日（水）", "お中元特集 2026｜相場・マナーと人気ギフト",
     "お中元2026特集。相場・時期・マナーと、本当に喜ばれる夏の贈り物を厳選。",
     "日頃の感謝を伝える夏のご挨拶。お中元の人気ギフトを厳選しました。",
     [("ochugen-2026", "お中元おすすめギフト", "相場とマナー"), ("natsu-matsuri-sashiire", "夏の差し入れ", "喜ばれる選び方")]),
    ("12-25", "クリスマス", "2026年12月25日（金）", "クリスマスギフト特集 2026｜彼氏・彼女・友達別",
     "クリスマス2026特集。彼氏・彼女・友達・家族別に本当に喜ばれるプレゼントを厳選。",
     "大切な人と過ごすクリスマス。心に残るプレゼントを厳選しました。",
     [("christmas-gift-2026", "クリスマスプレゼント15選", "相手別ガイド"), ("gift-for-boyfriend", "彼氏へのギフト", "年代別おすすめ")]),
]


import urllib.parse
def lf(kw, w, h, seed):
    k = urllib.parse.quote((kw or "gift").strip().replace(" ", ","))
    return f"https://loremflickr.com/{w}/{h}/{k}?lock={abs(hash(str(seed))) % 100000}"

# 季節ごとの「人気記事」筆頭スポット(slug, tag, card_title, card_desc, 画像kw)。既存featuredと被らない記事を選ぶ
SPOT = {
    "父の日": ("gift-for-father-in-law", "父の日", "義父も喜ぶ父の日ギフト｜失敗しない選び方", "目上の方にも安心の上質ギフトを予算別に厳選", "fathers day gift"),
    "お中元": ("ochugen-2026", "お中元", "【2026】お中元おすすめギフト｜相場とマナー", "夏のご挨拶に喜ばれる贈り物を厳選", "summer gift box"),
    "クリスマス": ("christmas-gift-2026", "クリスマス", "【2026】クリスマスプレゼント15選｜相手別", "彼氏・彼女・友達別の本命ギフトを厳選", "christmas gift"),
    "母の日": ("mothers-day-2026", "母の日", "【2026】母の日に本当に喜ばれるプレゼント15選", "予算別にお母さんが喜ぶギフトを厳選", "mothers day flowers"),
    "バレンタイン": ("valentine-gift", "バレンタイン", "本命・義理別バレンタインギフト", "チョコ以外も喜ばれる選び方", "valentine chocolate"),
    "ホワイトデー": ("white-day-gift", "ホワイトデー", "ホワイトデーお返し特集｜相場とおすすめ", "もらって嬉しいお返しを厳選", "white day gift"),
}


def pick(today):
    md = today.strftime("%m-%d")
    future = [e for e in CAL if e[0] >= md]
    return future[0] if future else CAL[0]  # 無ければ翌年の最初(バレンタイン)


def links_html(cands):
    rows = []
    for slug, text, sub in cands:
        if (BLOG / f"{slug}.html").exists():
            rows.append(f'''      <a href="blog/{slug}.html" class="countdown-link">
        <div class="countdown-link-icon">{GIFT_SVG}</div>
        <div><div class="countdown-link-text">{text}</div><div class="countdown-link-sub">{sub}</div></div>
      </a>''')
    if not rows:  # 全滅なら一般リンク
        rows.append('''      <a href="#gifts" class="countdown-link">
        <div class="countdown-link-icon">''' + GIFT_SVG + '''</div>
        <div><div class="countdown-link-text">ギフトを探す</div><div class="countdown-link-sub">シーン・予算で検索</div></div>
      </a>''')
    return "\n".join(rows)


def main():
    today = date.today()
    md_, name, jp, title, desc, sub, cands = pick(today)
    iso = f"2026-{md_}" if md_ >= today.strftime("%m-%d") else f"2027-{md_}"
    html = INDEX.read_text(encoding="utf-8")
    orig = html

    html = re.sub(r"<title>[^<]*</title>", f"<title>Okurite（おくりて）| {title}</title>", html, count=1)
    html = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1)+desc+m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1)+f"Okurite（おくりて）| {title}"+m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1)+desc+m.group(2), html, count=1)
    # heroバッジ等の「○○ギフト特集 2026」
    html = re.sub(r"[一-龯ぁ-んァ-ヶ]+ギフト特集 2026", f"{name}ギフト特集 2026", html)
    # navラベル
    html = re.sub(r'(<a href="#mothers-day">)[^<]*(</a>)', lambda m: m.group(1)+f"{name}特集"+m.group(2), html, count=1)
    # カウントダウン見出し
    html = re.sub(r'(<div class="countdown-header">[\s\S]*?<h2>)[^<]*(</h2>)', lambda m: m.group(1)+f"{name} {jp}"+m.group(2), html, count=1)
    # カウントダウンsub
    html = re.sub(r'(<p class="countdown-sub">)[^<]*(</p>)', lambda m: m.group(1)+sub+m.group(2), html, count=1)
    # カウントダウンJS目標日
    html = re.sub(r"new Date\('[^']*'\)", f"new Date('{iso}T00:00:00+09:00')", html, count=1)
    # 特集リンク群
    html = re.sub(r'(<div class="countdown-links">)[\s\S]*?(\n    </div>)',
                  lambda m: m.group(1)+"\n"+links_html(cands)+m.group(2), html, count=1)

    # 「人気記事」の筆頭カードを季節スポットに差し替え(トップ商品が季節と不一致な問題の解消)
    sp = SPOT.get(name)
    if sp and (BLOG / f"{sp[0]}.html").exists():
        slug, tag, ct, cd, kw = sp
        import gen_article_ai as G
        rel = G.get_image(kw, "seasonal", slug)
        img_src = ("blog/" + rel) if rel else G.FALLBACK_IMG
        card = (f'<a href="blog/{slug}.html" class="featured-card">\n'
                f'      <img class="featured-card-img" src="{img_src}" alt="{ct}" loading="lazy">\n'
                f'      <div class="featured-card-body">\n'
                f'        <span class="featured-card-tag">{tag}</span>\n'
                f'        <div class="featured-card-title">{ct}</div>\n'
                f'        <p class="featured-card-desc">{cd}</p>\n'
                f'      </div>\n    </a>')
        html = re.sub(r'(<div class="featured-grid">\s*)<a href="[^"]*" class="featured-card">[\s\S]*?</a>',
                      lambda m: m.group(1)+card, html, count=1)

    if html != orig:
        INDEX.write_text(html, encoding="utf-8")
        print(f"季節更新: {name} ({jp}) / 目標日{iso} / リンク{links_html(cands).count('countdown-link')}")
    else:
        print("変更なし")


if __name__ == "__main__":
    main()
