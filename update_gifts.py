import json
import urllib.parse

AFF_ID = "522e40a0.f2dc4208.522e40a1.385f875e"

CATEGORY_IMAGES = {
    "コスメ":         "https://tshop.r10s.jp/skindesign/cabinet/cosme/thesaem/perfumedhandcream/main5_00.jpg",
    "スイーツ":       "https://tshop.r10s.jp/buriruby/cabinet/12797424/41429072_1.jpg",
    "フラワー":       "https://tshop.r10s.jp/jmei3rd/cabinet/eat01/b/se_10-01.jpg",
    "お酒":           "https://tshop.r10s.jp/isekadoyabeer/cabinet/biiino/item/s-image-3/imgrc0084774386.jpg",
    "グルメ":         "https://tshop.r10s.jp/yamaichi-himono/cabinet/04735669/sab1nis1kam2koa3.jpg",
    "食品":           "https://tshop.r10s.jp/hokkaido-gourmation/cabinet/syouhin/cbell/26cbell_sg001rt.jpg",
    "タオル":         "https://tshop.r10s.jp/balloon-cube/cabinet/item/towel/kk/kk79100.jpg",
    "カタログ":       "https://tshop.r10s.jp/giftman/cabinet/new_catalogue/harmonick-v/3740.jpg",
    "アクセサリー":   "https://tshop.r10s.jp/alevel/cabinet/tommy/12766-bds.jpg",
    "ガジェット":     "https://tshop.r10s.jp/gift-bmcjapan/cabinet/toothcase/thntb3.jpg",
    "バッグ":         "https://tshop.r10s.jp/lapiz/cabinet/original/lpmg/lpmg-s1_2.jpg",
    "ファッション":   "https://tshop.r10s.jp/erikaland/cabinet/07746014/08564067/09631264/erem4756-1.jpg",
    "ベビー":         "https://tshop.r10s.jp/omutsufactory/cabinet/11013756/imgrc0096174926.jpg",
    "ペア":           "https://tshop.r10s.jp/fika/cabinet/08062032/holder_wood_001/set002_re/set002_re.jpg",
    "リラクゼーション": "https://tshop.r10s.jp/howmoreliving/cabinet/06943964/olor/olor-027.jpg",
    "おもちゃ":       "https://tshop.r10s.jp/k999/cabinet/item/05992753/360011-sam202112.jpg",
    "体験":           "https://tshop.r10s.jp/toolandmeal/cabinet/item/12592352/concierge_card_th_02.jpg",
    "健康":           "https://tshop.r10s.jp/hisarekomafu/cabinet/compass1689051895.jpg",
    "子供ファッション": "https://tshop.r10s.jp/lucky13/cabinet/main03/sfkidswatch.jpg",
    "文具":           "https://tshop.r10s.jp/backyard/cabinet/main07/softpencase5.jpg",
    "旅行":           "https://tshop.r10s.jp/rambbit/cabinet/ikou_20100223/c001.jpg",
    "知育":           "https://tshop.r10s.jp/houjou-kyouzai/cabinet/reku/uno1.jpg",
    "菓子":           "https://tshop.r10s.jp/matsukazeya-ec/cabinet/foucher/amanderois/ar-10_0304u.jpg",
    "趣味":           "https://tshop.r10s.jp/imobuta/cabinet/11151275/11151277/imgrc0102419392.jpg",
    "飲料":           "https://tshop.r10s.jp/arumama/cabinet/shohin/sake/beer/gu-330-1.jpg",
}

with open("gifts.json", "r", encoding="utf-8") as f:
    gifts = json.load(f)

for g in gifts:
    # Set image from category if missing
    if not g.get("img"):
        g["img"] = CATEGORY_IMAGES.get(g.get("category", ""), "")

    # Convert rakutenUrl to affiliate format
    current_url = g.get("rakutenUrl", "")
    if current_url and "hb.afl.rakuten.co.jp" not in current_url:
        encoded = urllib.parse.quote(current_url, safe="")
        g["rakutenUrl"] = f"https://hb.afl.rakuten.co.jp/ichiba/{AFF_ID}/?pc={encoded}&link_type=hybrid_url"

with open("gifts.json", "w", encoding="utf-8") as f:
    json.dump(gifts, f, ensure_ascii=False, indent=1)

print(f"Updated {len(gifts)} products")
print(f"Products with images: {sum(1 for g in gifts if g.get('img'))}")
print(f"Sample rakutenUrl: {gifts[0]['rakutenUrl'][:90]}")
