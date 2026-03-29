#!/usr/bin/env python3
"""
generate_products.py - Okuriteギフトサイト 実商品データ生成スクリプト

楽天市場から収集した実際の商品データをもとに、index.html の gift-grid セクションを生成します。
Amazon アソシエイトタグ: okuritegift-22

使い方:
  python generate_products.py        # product_cards.html を生成
  python generate_products.py --json # products.json を生成
"""

import json
import sys
from urllib.parse import quote

AMAZON_TAG = "okuritegift-22"

# ================================================================
# 実商品データベース（楽天市場スクレイピング + Amazon検索リンク）
# ================================================================
PRODUCTS = {
    "haha": {
        "scene_name": "母の日",
        "scene_id": "haha",
        "icon": "🌸",
        "subtitle": "5月第2日曜日 — 日頃の感謝を花と贈り物に込めて",
        "items": [
            {
                "title": "高麗橋吉兆 栗ぜんざいギフト 4個入",
                "price": "¥3,754（送料無料）",
                "description": "老舗料亭・高麗橋吉兆の本格的な栗ぜんざい4個入。上品な甘さと高級感で日頃の感謝を伝えます。",
                "emoji": "🍡",
                "budget": "3k5k",
                "target": "female parents",
                "tags": ["女性向け", "両親へ"],
                "amazon_kw": "高麗橋吉兆 栗ぜんざい ギフト",
                "rakuten_url": "https://item.rakuten.co.jp/buriruby/xzvbbxrdxputkmepoy57noo3ke/",
            },
            {
                "title": "カーネーション花鉢＋ヴィタメール焼き菓子セット",
                "price": "¥7,300（送料無料）",
                "description": "生花のカーネーション鉢とベルギー王室御用達ヴィタメールの焼き菓子5個入。花とスイーツの豪華セット。",
                "emoji": "🌸",
                "budget": "5k10k",
                "target": "female parents",
                "tags": ["女性向け", "両親へ"],
                "amazon_kw": "母の日 カーネーション スイーツ セット",
                "rakuten_url": "https://item.rakuten.co.jp/jmei3rd/fgift-389/",
            },
            {
                "title": "THE SAEM 選べるハンドクリーム 5個セット",
                "price": "¥2,000（送料無料）",
                "description": "25種類から好きな香りを選べる人気コスメブランドSAEMのハンドクリーム5個セット。",
                "emoji": "💆",
                "budget": "under3k",
                "target": "female",
                "tags": ["女性向け"],
                "amazon_kw": "THE SAEM ハンドクリーム ギフトセット",
                "rakuten_url": "https://item.rakuten.co.jp/skindesign/perfumed-hand-cream5set/",
            },
            {
                "title": "日本製 ガーゼハンカチ＋ハンドクリームセット",
                "price": "¥2,000（送料無料）",
                "description": "上品なガーゼハンカチとホワイトティーの香りのハンドクリームの日本製ギフトセット。",
                "emoji": "🌿",
                "budget": "under3k",
                "target": "female parents",
                "tags": ["女性向け", "両親へ"],
                "amazon_kw": "ハンカチ ハンドクリーム ギフトセット 日本製",
                "rakuten_url": "https://item.rakuten.co.jp/bridgehappy/kj03/",
            },
            {
                "title": "金木犀 ハンドクリーム プチギフト 日本製",
                "price": "¥2,000（送料無料）",
                "description": "上品な金木犀の香りの日本製ハンドクリーム。ラッピング無料で手軽に贈れる人気ギフト。",
                "emoji": "🌼",
                "budget": "under3k",
                "target": "female",
                "tags": ["女性向け"],
                "amazon_kw": "ハンドクリーム 金木犀 ギフト 日本製",
                "rakuten_url": "https://item.rakuten.co.jp/bridgehappy/cl0018/",
            },
        ],
    },
    "chichi": {
        "scene_name": "父の日",
        "scene_id": "chichi",
        "icon": "👔",
        "subtitle": "6月第3日曜日 — お父さんの好きなものをプレゼント",
        "items": [
            {
                "title": "伊勢角屋麦酒 クラフトビール ペールエール 瓶セット",
                "price": "¥1,835〜（価格+送料）",
                "description": "三重・伊勢の老舗クラフトビール醸造所のペールエール瓶セット。フルーティーな香りが特徴。",
                "emoji": "🍺",
                "budget": "under3k",
                "target": "male parents",
                "tags": ["男性向け", "両親へ"],
                "amazon_kw": "伊勢角屋麦酒 クラフトビール セット",
                "rakuten_url": "https://item.rakuten.co.jp/isekadoyabeer/paleale-b-1p/",
            },
            {
                "title": "城崎温泉 地ビール ギフトセット（330ml）",
                "price": "¥2,090（価格+送料）",
                "description": "温泉地・城崎の地元直送クラフトビール。産地直送の新鮮さが自慢のギフトセット。",
                "emoji": "🍻",
                "budget": "under3k",
                "target": "male parents",
                "tags": ["男性向け", "両親へ"],
                "amazon_kw": "城崎温泉 地ビール ギフト",
                "rakuten_url": "https://item.rakuten.co.jp/arumama/gu-330-1/",
            },
            {
                "title": "国産旬彩 干物セット（サバ・ニシン等）",
                "price": "¥3,000（送料無料）",
                "description": "職人が丁寧に仕上げた国産魚の旬彩干物セット。お酒好きのお父さんへ本格的な贈り物。",
                "emoji": "🐟",
                "budget": "3k5k",
                "target": "male parents",
                "tags": ["男性向け", "両親へ"],
                "amazon_kw": "国産 干物セット ギフト 父の日",
                "rakuten_url": "https://item.rakuten.co.jp/yamaichi-himono/s-himono-1/",
            },
            {
                "title": "北海道 カウベルアイスクリーム 詰め合わせ 12個",
                "price": "¥3,180（送料無料）",
                "description": "北海道産の濃厚アイスクリーム12個詰め合わせ。夏の父の日にぴったりの冷たいギフト。",
                "emoji": "🍦",
                "budget": "3k5k",
                "target": "male female parents",
                "tags": ["男性向け", "女性向け", "両親へ"],
                "amazon_kw": "北海道 アイスクリーム 詰め合わせ ギフト",
                "rakuten_url": "https://item.rakuten.co.jp/hokkaido-gourmation/fax-089-ice12/",
            },
            {
                "title": "仙台牛 低温調理ユッケ 2個セット",
                "price": "¥3,945〜（価格+送料）",
                "description": "最高級A5仙台牛の低温調理ユッケ2個セット。特別な日にふさわしい高級感ある肉ギフト。",
                "emoji": "🥩",
                "budget": "3k5k",
                "target": "male parents",
                "tags": ["男性向け", "両親へ"],
                "amazon_kw": "仙台牛 ユッケ 高級 ギフト",
                "rakuten_url": "https://item.rakuten.co.jp/hisarekomafu/compass1640161685/",
            },
        ],
    },
    "tanjobi": {
        "scene_name": "誕生日",
        "scene_id": "tanjobi",
        "icon": "🎂",
        "subtitle": "年に一度の特別な日に、心に残る贈り物を",
        "items": [
            {
                "title": "チーズファクトリー 厳選スイーツセット",
                "price": "¥2,000（送料無料）",
                "description": "チーズを使った濃厚スイーツの詰め合わせ。誕生日の贈り物に喜ばれるお菓子ギフト。",
                "emoji": "🧀",
                "budget": "under3k",
                "target": "female",
                "tags": ["女性向け"],
                "amazon_kw": "誕生日 スイーツ ギフトセット チーズ",
                "rakuten_url": "https://item.rakuten.co.jp/monmiya/70005926/",
            },
            {
                "title": "ジュレパフェ 6個セット フルーツゼリー",
                "price": "¥2,200（送料無料）",
                "description": "見た目も華やかなフルーツゼリーのジュレパフェ6個セット。誕生日に華を添える洋菓子ギフト。",
                "emoji": "🍮",
                "budget": "under3k",
                "target": "female male",
                "tags": ["女性向け", "男性向け"],
                "amazon_kw": "フルーツゼリー ギフトセット 誕生日",
                "rakuten_url": "https://item.rakuten.co.jp/watch-me/t-11-035/",
            },
            {
                "title": "誕生日 アクセサリー（ネックレス・ピアス）",
                "price": "¥5,000〜¥10,000",
                "description": "シンプルで使いやすいシルバー・ゴールドのネックレス。誕生日に定番の人気ジュエリーギフト。",
                "emoji": "💎",
                "budget": "5k10k",
                "target": "female",
                "tags": ["女性向け"],
                "amazon_kw": "誕生日 ネックレス ギフト シンプル",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E8%AA%95%E7%94%9F%E6%97%A5+%E3%83%8D%E3%83%83%E3%82%AF%E3%83%AC%E3%82%B9+%E3%82%AE%E3%83%95%E3%83%88/",
            },
            {
                "title": "ブランド財布 誕生日プレゼント",
                "price": "¥8,000〜¥15,000",
                "description": "長財布・二つ折り財布。実用的で毎日使えるため男女問わず喜ばれる定番ギフト。",
                "emoji": "👛",
                "budget": "over10k",
                "target": "male female",
                "tags": ["男性向け", "女性向け"],
                "amazon_kw": "誕生日 財布 ギフト ブランド",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E8%AA%95%E7%94%9F%E6%97%A5+%E8%B2%A1%E5%B8%83+%E3%82%AE%E3%83%95%E3%83%88/",
            },
            {
                "title": "体験ギフト（グルメ・アクティビティ・スパ）",
                "price": "¥8,000〜¥15,000",
                "description": "旅行・グルメ・スパなど体験型プレゼント。モノより思い出の特別感ある誕生日ギフト。",
                "emoji": "🎫",
                "budget": "over10k",
                "target": "male female",
                "tags": ["全員向け"],
                "amazon_kw": "体験ギフト 誕生日 プレゼント",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E4%BD%93%E9%A8%93%E3%82%AE%E3%83%95%E3%83%88+%E8%AA%95%E7%94%9F%E6%97%A5/",
            },
        ],
    },
    "kekkon": {
        "scene_name": "結婚祝い",
        "scene_id": "kekkon",
        "icon": "💍",
        "subtitle": "新しい門出を祝う、二人への特別な贈り物",
        "items": [
            {
                "title": "カタログギフト 3,740円コース（ネコポス便）",
                "price": "¥3,000（送料無料）",
                "description": "グルメ・旅行・日用品など豊富なラインナップから選べるカタログギフト。結婚祝いの定番。",
                "emoji": "📋",
                "budget": "3k5k",
                "target": "female male",
                "tags": ["ペアで"],
                "amazon_kw": "結婚祝い カタログギフト 3000円",
                "rakuten_url": "https://item.rakuten.co.jp/giftman/neko-sh-be/",
            },
            {
                "title": "グランチョイスギフト カタログ 2,900円コース",
                "price": "¥3,000（送料無料）",
                "description": "楽天評価★4.75の高評価カタログギフト。豊富なジャンルから二人で選んでもらえる人気商品。",
                "emoji": "🎁",
                "budget": "3k5k",
                "target": "female male",
                "tags": ["ペアで"],
                "amazon_kw": "結婚祝い カタログギフト 人気",
                "rakuten_url": "https://item.rakuten.co.jp/rambbit/649933/",
            },
            {
                "title": "ハートフルセレクション カタログギフト（カードタイプ）",
                "price": "¥3,080〜（送料無料）",
                "description": "コンシェルジュ対応のカードタイプカタログギフト。WEB選択可でスマートに贈れる。",
                "emoji": "💝",
                "budget": "3k5k",
                "target": "female male",
                "tags": ["ペアで"],
                "amazon_kw": "カタログギフト カードタイプ 結婚祝い",
                "rakuten_url": "https://item.rakuten.co.jp/toolandmeal/105069450/",
            },
            {
                "title": "山崎実業 tower WEBカタログギフト",
                "price": "¥3,630〜（価格+送料）",
                "description": "人気ブランド山崎実業「タワー」のインテリア雑貨などが選べるウェブカタログギフト。",
                "emoji": "🏠",
                "budget": "3k5k",
                "target": "female male",
                "tags": ["ペアで", "実用的"],
                "amazon_kw": "山崎実業 タワー ギフト 結婚祝い",
                "rakuten_url": "https://item.rakuten.co.jp/bellevie-harima/cat-tower-003/",
            },
            {
                "title": "結婚祝い 今治タオルセット",
                "price": "¥5,000〜¥8,000",
                "description": "日本が誇る今治タオルの高級セット。新生活に実用的で縁起の良い贈り物。",
                "emoji": "🛁",
                "budget": "5k10k",
                "target": "female male",
                "tags": ["ペアで", "実用的"],
                "amazon_kw": "結婚祝い 今治タオル ギフトセット",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E7%B5%90%E5%A9%9A%E7%A5%9D%E3%81%84+%E4%BB%8A%E6%B2%BB%E3%82%BF%E3%82%AA%E3%83%AB/",
            },
        ],
    },
    "shussan": {
        "scene_name": "出産祝い",
        "scene_id": "shussan",
        "icon": "👶",
        "subtitle": "新しい命の誕生を祝う、ママ・赤ちゃんへの贈り物",
        "items": [
            {
                "title": "名入れ 乳歯ケース 木製 記念品",
                "price": "¥3,000（送料無料）",
                "description": "子供の大切な乳歯を保管できる木製の名入れ乳歯ケース。出産祝いの記念品として人気。",
                "emoji": "🌟",
                "budget": "3k5k",
                "target": "child female",
                "tags": ["子供へ", "記念品"],
                "amazon_kw": "出産祝い 乳歯ケース 名入れ",
                "rakuten_url": "https://item.rakuten.co.jp/gift-bmcjapan/o20211030/",
            },
            {
                "title": "fika 木製 歯固め＋ホルダーセット",
                "price": "¥3,325（価格+送料）",
                "description": "厚生労働省認定機関検査合格のオーガニック素材。赤ちゃんに安心な木製歯固めとホルダーセット。",
                "emoji": "👶",
                "budget": "3k5k",
                "target": "child female",
                "tags": ["子供へ", "安心素材"],
                "amazon_kw": "出産祝い 歯固め 木製 セット",
                "rakuten_url": "https://item.rakuten.co.jp/fika/set002/",
            },
            {
                "title": "ネオママイズム 柄おくるみ オーガニックコットン",
                "price": "¥3,080（送料無料）",
                "description": "コットン100%のふんわりモスリンおくるみ。出産祝いの定番として人気のベビーブランケット。",
                "emoji": "👕",
                "budget": "3k5k",
                "target": "child female",
                "tags": ["子供へ", "実用的"],
                "amazon_kw": "出産祝い おくるみ オーガニック",
                "rakuten_url": "https://item.rakuten.co.jp/neomamaism/nm21swd001/",
            },
            {
                "title": "今治タオル コンテックス ビブ（スタイ）セット",
                "price": "¥3,850（価格+送料）",
                "description": "日本が誇る今治タオルブランドのビブ（よだれかけ）セット。肌触り抜群で実用的な出産祝い。",
                "emoji": "🌸",
                "budget": "3k5k",
                "target": "child female",
                "tags": ["子供へ", "実用的"],
                "amazon_kw": "出産祝い 今治タオル スタイ",
                "rakuten_url": "https://item.rakuten.co.jp/omutsufactory/kontex-buraburabib/",
            },
            {
                "title": "出産祝い おむつケーキ 人気",
                "price": "¥5,000〜¥8,000",
                "description": "おむつをケーキ型に飾り付けた人気ギフト。実用的でインスタ映えする出産祝いの定番アイテム。",
                "emoji": "🎂",
                "budget": "5k10k",
                "target": "child female",
                "tags": ["子供へ", "見た目◎"],
                "amazon_kw": "出産祝い おむつケーキ 人気",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E5%87%BA%E7%94%A3%E7%A5%9D%E3%81%84+%E3%81%8A%E3%82%80%E3%81%A4%E3%82%B1%E3%83%BC%E3%82%AD+%E4%BA%BA%E6%B0%97/",
            },
        ],
    },
    "christmas": {
        "scene_name": "クリスマス",
        "scene_id": "christmas",
        "icon": "🎄",
        "subtitle": "12月25日 — ワクワクする特別な贈り物を",
        "items": [
            {
                "title": "子供用 お医者さん・大工ごっこ 知育おもちゃ",
                "price": "¥2,180（送料無料）",
                "description": "ごっこ遊びができる知育おもちゃセット。男の子も女の子も楽しめるクリスマスプレゼント。",
                "emoji": "🎮",
                "budget": "under3k",
                "target": "child",
                "tags": ["子供へ"],
                "amazon_kw": "子供 クリスマスプレゼント 知育おもちゃ",
                "rakuten_url": "https://item.rakuten.co.jp/k999/360011/",
            },
            {
                "title": "バランスボード ゆらゆら 子供 体幹トレーニング",
                "price": "¥2,180〜（送料無料）",
                "description": "遊びながら体幹を鍛えられるバランスボード。楽天40冠達成の人気クリスマスプレゼント。",
                "emoji": "🏄",
                "budget": "under3k",
                "target": "child",
                "tags": ["子供へ", "運動"],
                "amazon_kw": "バランスボード 子供 クリスマス",
                "rakuten_url": "https://item.rakuten.co.jp/lifetips/life-30114/",
            },
            {
                "title": "クリスマス 高級チョコ・焼き菓子 詰め合わせ",
                "price": "¥1,500〜¥3,000",
                "description": "クリスマス限定パッケージの高級チョコレートや焼き菓子のセット。大人にも子供にも人気。",
                "emoji": "🍫",
                "budget": "under3k",
                "target": "female male child",
                "tags": ["全員向け", "子供へ"],
                "amazon_kw": "クリスマス お菓子 ギフトセット",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%9E%E3%82%B9+%E3%81%8A%E8%8F%93%E5%AD%90+%E3%82%AE%E3%83%95%E3%83%88/",
            },
            {
                "title": "アロマ・キャンドルセット クリスマスギフト",
                "price": "¥3,000〜¥5,000",
                "description": "冬の夜にぴったりのアロマキャンドルセット。インテリアにもなるおしゃれな大人へのギフト。",
                "emoji": "🕯️",
                "budget": "3k5k",
                "target": "female",
                "tags": ["女性向け"],
                "amazon_kw": "クリスマス アロマキャンドル ギフト",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%9E%E3%82%B9+%E3%82%A2%E3%83%AD%E3%83%9E%E3%82%AE%E3%83%95%E3%83%88/",
            },
        ],
    },
    "nyugaku": {
        "scene_name": "入学祝い",
        "scene_id": "nyugaku",
        "icon": "🎒",
        "subtitle": "新しいスタートを応援する贈り物",
        "items": [
            {
                "title": "両面 ソフトペンケース 小学生 入学準備",
                "price": "¥2,026（送料無料）",
                "description": "かわいいデザインの両面両開きソフトペンケース。小学校入学準備の定番プレゼント。",
                "emoji": "✏️",
                "budget": "under3k",
                "target": "child",
                "tags": ["子供へ", "実用的"],
                "amazon_kw": "入学祝い ペンケース 小学生 かわいい",
                "rakuten_url": "https://item.rakuten.co.jp/backyard/softpencase5/",
            },
            {
                "title": "子供用 アナログ腕時計 入学祝い",
                "price": "¥2,129（送料無料）",
                "description": "男の子・女の子両対応のおしゃれなアナログ腕時計。入学祝いに時間の管理を学べる贈り物。",
                "emoji": "⌚",
                "budget": "under3k",
                "target": "child",
                "tags": ["子供へ", "実用的"],
                "amazon_kw": "入学祝い 子供 腕時計 キッズ",
                "rakuten_url": "https://item.rakuten.co.jp/lucky13/sfkidswatch/",
            },
            {
                "title": "入学祝い 学習図鑑・辞典セット",
                "price": "¥3,000〜¥5,000",
                "description": "学習意欲を育てる人気の図鑑や辞典セット。長く使えて知育にもなる喜ばれる贈り物。",
                "emoji": "📚",
                "budget": "3k5k",
                "target": "child",
                "tags": ["子供へ", "知育"],
                "amazon_kw": "入学祝い 図鑑 子供 人気",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E5%85%A5%E5%AD%A6%E7%A5%9D%E3%81%84+%E5%9B%B3%E9%91%91+%E5%B0%8F%E5%AD%A6%E7%94%9F/",
            },
            {
                "title": "入学祝い 知育ボードゲーム・パズル",
                "price": "¥5,000〜¥8,000",
                "description": "思考力・コミュニケーション力を育てるボードゲームやパズル。家族で楽しめる知育玩具。",
                "emoji": "🎲",
                "budget": "5k10k",
                "target": "child",
                "tags": ["子供へ", "知育"],
                "amazon_kw": "入学祝い 知育玩具 ボードゲーム",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E5%85%A5%E5%AD%A6%E7%A5%9D%E3%81%84+%E7%9F%A5%E8%82%B2%E7%8E%A9%E5%85%B7/",
            },
        ],
    },
    "ochugen": {
        "scene_name": "お中元・お歳暮",
        "scene_id": "ochugen",
        "icon": "🍱",
        "subtitle": "日頃の感謝を伝える、格式あるギフト",
        "items": [
            {
                "title": "千葉県産 いも豚 3点ハムセット",
                "price": "¥2,140〜（送料無料）",
                "description": "千葉県産のいも豚を使った本格ハムの詰め合わせ3点セット。おつまみにもなる贈り物。",
                "emoji": "🥩",
                "budget": "under3k",
                "target": "parents boss",
                "tags": ["両親へ", "上司へ"],
                "amazon_kw": "お中元 ハムギフトセット 国産",
                "rakuten_url": "https://item.rakuten.co.jp/imobuta/0041/",
            },
            {
                "title": "Hitotoe ジュレパフェ 6個セット フルーツゼリー",
                "price": "¥2,200（送料無料）",
                "description": "中島大祥堂のブランド「Hitotoe」のフルーツゼリーパフェ6個詰め合わせ。見た目も美しい。",
                "emoji": "🍮",
                "budget": "under3k",
                "target": "parents boss female",
                "tags": ["両親へ", "上司へ"],
                "amazon_kw": "お中元 ゼリー ギフトセット",
                "rakuten_url": "https://item.rakuten.co.jp/watch-me/t-11-035/",
            },
            {
                "title": "お中元・お歳暮 ビール・お酒 詰め合わせ",
                "price": "¥3,000〜¥5,000",
                "description": "定番のビールセットや日本酒・焼酎の詰め合わせ。幅広い年代に喜ばれる王道ギフト。",
                "emoji": "🍺",
                "budget": "3k5k",
                "target": "parents boss",
                "tags": ["両親へ", "上司へ"],
                "amazon_kw": "お中元 ビール ギフト 人気",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E3%81%8A%E4%B8%AD%E5%85%83+%E3%83%93%E3%83%BC%E3%83%AB%E3%82%AE%E3%83%95%E3%83%88/",
            },
            {
                "title": "高級グルメセット お中元・お歳暮",
                "price": "¥5,000〜¥10,000",
                "description": "産地直送の海産物・肉・惣菜のグルメセット。目上の方への格式ある贈り物。",
                "emoji": "🫒",
                "budget": "5k10k",
                "target": "parents boss",
                "tags": ["両親へ", "上司へ"],
                "amazon_kw": "お中元 グルメ ギフト 高級",
                "rakuten_url": "https://search.rakuten.co.jp/search/mall/%E3%81%8A%E4%B8%AD%E5%85%83+%E3%82%B0%E3%83%AB%E3%83%A1%E3%82%AE%E3%83%95%E3%83%88/",
            },
        ],
    },
}


def make_amazon_url(keyword: str) -> str:
    """Amazon検索URLをアフィリエイトタグ付きで生成"""
    return f"https://www.amazon.co.jp/s?k={quote(keyword)}&tag={AMAZON_TAG}"


def render_gift_card(item: dict) -> str:
    """商品カードのHTMLを生成"""
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in item["tags"])
    amazon_url = make_amazon_url(item["amazon_kw"])
    rakuten_url = item["rakuten_url"]
    return f"""        <div class="gift-card" data-budget="{item['budget']}" data-target="{item['target']}">
          <div class="gift-image">{item['emoji']}</div>
          <div class="gift-body">
            <h3>{item['title']}</h3>
            <p class="price">{item['price']}</p>
            <p class="description">{item['description']}</p>
            <div class="tag-row">{tags_html}</div>
            <div class="affiliate-links">
              <a href="{amazon_url}" target="_blank" rel="noopener" class="btn-amazon">Amazonで見る</a>
              <a href="{rakuten_url}" target="_blank" rel="noopener" class="btn-rakuten">楽天で見る</a>
            </div>
          </div>
        </div>"""


def render_scene_section(scene: dict) -> str:
    """シーンセクション全体のHTMLを生成"""
    cards_html = "\n".join(render_gift_card(item) for item in scene["items"])
    return f"""    <!-- {scene['scene_name']} -->
    <section class="scene-section" data-scene="{scene['scene_id']}" id="{scene['scene_id']}">
      <div class="scene-header">
        <div class="scene-icon">{scene['icon']}</div>
        <div>
          <h2>{scene['scene_name']}のギフト</h2>
          <p>{scene['subtitle']}</p>
        </div>
      </div>
      <div class="gift-grid">
{cards_html}
      </div>
    </section>"""


def main():
    if "--json" in sys.argv:
        # JSON出力モード
        output = []
        for scene_id, scene in PRODUCTS.items():
            for item in scene["items"]:
                output.append({
                    "scene": scene_id,
                    "scene_name": scene["scene_name"],
                    "title": item["title"],
                    "price": item["price"],
                    "description": item["description"],
                    "budget": item["budget"],
                    "target": item["target"],
                    "amazon_url": make_amazon_url(item["amazon_kw"]),
                    "rakuten_url": item["rakuten_url"],
                })
        with open("products.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"products.json に {len(output)} 件の商品データを出力しました。")
    else:
        # HTMLカード出力モード
        sections = "\n\n".join(render_scene_section(s) for s in PRODUCTS.values())
        with open("product_cards.html", "w", encoding="utf-8") as f:
            f.write(sections)
        total = sum(len(s["items"]) for s in PRODUCTS.values())
        print(f"product_cards.html に {total} 件の商品カードを出力しました。")
        print("シーン別内訳:")
        for scene_id, scene in PRODUCTS.items():
            print(f"  {scene['scene_name']}: {len(scene['items'])} 件")


if __name__ == "__main__":
    main()
