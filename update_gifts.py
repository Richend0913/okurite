import json
import urllib.parse
import urllib.request
import time
import os

AFF_ID = "522e40a0.f2dc4208.522e40a1.385f875e"
AMAZON_TAG = "okuritegift-22"

# 楽天API設定 - 環境変数 or 直接入力
APP_ID = os.environ.get("RAKUTEN_APP_ID", "")
ACCESS_KEY = os.environ.get("RAKUTEN_ACCESS_KEY", "")

API_URL = "https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20220601"

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


def search_rakuten(keyword, hits=3):
    """楽天APIで商品を検索し、最初のヒットを返す"""
    params = urllib.parse.urlencode({
        "applicationId": APP_ID,
        "accessKey": ACCESS_KEY,
        "keyword": keyword,
        "hits": hits,
        "imageFlag": 1,
        "sort": "-reviewCount",
        "formatVersion": 2,
    })
    url = f"{API_URL}?{params}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "OkuriteUpdater/1.0",
        "Origin": "https://richend0913.github.io",
        "Referer": "https://richend0913.github.io/",
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        items = data.get("Items", [])
        if items:
            return items[0]
    except Exception as e:
        print(f"  API error for '{keyword}': {e}")
    return None


def make_affiliate_url(item_url):
    """商品URLをアフィリエイトURLに変換"""
    encoded = urllib.parse.quote(item_url, safe="")
    return f"https://hb.afl.rakuten.co.jp/ichiba/{AFF_ID}/?pc={encoded}&link_type=hybrid_url"


def upgrade_image(img_url):
    """画像URLを128x128→256x256にアップグレード"""
    return img_url.replace("128x128", "256x256").replace("?_ex=128x128", "?_ex=256x256")


with open("gifts.json", "r", encoding="utf-8") as f:
    gifts = json.load(f)

if not APP_ID or not ACCESS_KEY:
    print("ERROR: 楽天APIキーが未設定")
    print("環境変数を設定してください:")
    print("  export RAKUTEN_APP_ID='your-app-id'")
    print("  export RAKUTEN_ACCESS_KEY='your-access-key'")
    exit(1)

updated = 0
failed = 0
skipped = 0

for i, g in enumerate(gifts):
    name = g["name"]
    print(f"[{i+1}/{len(gifts)}] {name}...", end=" ", flush=True)

    item = search_rakuten(name)

    if item:
        # 画像取得
        img_urls = item.get("mediumImageUrls", [])
        if img_urls:
            img = img_urls[0] if isinstance(img_urls[0], str) else img_urls[0].get("imageUrl", "")
            g["img"] = upgrade_image(img) if img else CATEGORY_IMAGES.get(g.get("category", ""), "")
        else:
            g["img"] = CATEGORY_IMAGES.get(g.get("category", ""), "")

        # 個別商品URL → アフィリエイトURL
        item_url = item.get("itemUrl", "")
        if item_url:
            g["rakutenUrl"] = make_affiliate_url(item_url)

        updated += 1
        print("OK")
    else:
        # API失敗時はカテゴリ画像をフォールバック
        if not g.get("img"):
            g["img"] = CATEGORY_IMAGES.get(g.get("category", ""), "")
        # 検索URLのままアフィリエイト化
        current_url = g.get("rakutenUrl", "")
        if current_url and "hb.afl.rakuten.co.jp" not in current_url:
            g["rakutenUrl"] = make_affiliate_url(current_url)
        failed += 1
        print("FAILED (fallback)")

    # レートリミット対策: 1リクエスト/秒
    time.sleep(1)

with open("gifts.json", "w", encoding="utf-8") as f:
    json.dump(gifts, f, ensure_ascii=False, indent=1)

print(f"\n=== 完了 ===")
print(f"更新成功: {updated}/{len(gifts)}")
print(f"失敗(フォールバック): {failed}")
unique_imgs = len(set(g.get("img", "") for g in gifts))
print(f"ユニーク画像数: {unique_imgs}")
print(f"Sample: {gifts[0]['name']}")
print(f"  img: {gifts[0]['img'][:80]}...")
print(f"  url: {gifts[0]['rakutenUrl'][:80]}...")
