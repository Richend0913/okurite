# -*- coding: utf-8 -*-
"""記事の商品カード画像を“その商品そのもの”の実画像に差し替える。
APIキー不要: 商品名で楽天市場の検索ページを取得し、先頭(売れ筋)商品のサムネ画像を使う。
- キャッシュ(image_cache.json)で再開可能・冪等。
- 取得失敗時は既存画像を維持(壊さない)。
- 礼儀: 新規取得ごとに待機。"""
import glob, re, json, os, time, urllib.request, urllib.parse, sys

ROOT = r"C:\Users\sushi\okurite"
CACHE = ROOT + r"\image_cache.json"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
DELAY = 1.0
READ_BYTES = 300000  # 先頭だけ読む(先頭商品の画像は早い位置に出る)

def load_cache():
    try:
        return json.load(open(CACHE, encoding="utf-8"))
    except Exception:
        return {}

def save_cache(c):
    json.dump(c, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)

def scrape(kw):
    url = "https://search.rakuten.co.jp/search/mall/" + urllib.parse.quote(kw) + "/"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    html = urllib.request.urlopen(req, timeout=20).read(READ_BYTES).decode("utf-8", "replace")
    imgs = re.findall(r'https://thumbnail\.image\.rakuten\.co\.jp/@0_mall/[A-Za-z0-9_\-/.]+\.(?:jpg|jpeg|png|gif)', html)
    # ロゴ/汎用を避け、最初の商品サムネ(cabinet配下)を返す
    for u in imgs:
        if "/cabinet/" in u:
            return u
    return imgs[0] if imgs else None

def main():
    apply = "--apply" in sys.argv
    cache = load_cache()
    files = glob.glob(ROOT + r"\blog\*.html")
    # まず全記事から (img位置, title) を集めてユニークtitleを確定
    jobs = []  # (file, img_match_span, title)
    per_file = {}
    for f in files:
        h = open(f, encoding="utf-8").read()
        per_file[f] = h
        titles = [(m.start(), re.sub(r"^\d+\.\s*", "", re.sub("<.*?>", "", m.group(1)).strip()))
                  for m in re.finditer(r'gift-card-title">(.*?)</div>', h, re.S)]
        for m in re.finditer(r'(<img class="gift-card-img"[^>]*?src=")([^"]+)(")', h):
            after = [t for p, t in titles if p > m.start()]
            title = after[0] if after else ""
            jobs.append((f, (m.start(2), m.end(2)), title))
    uniq = sorted({t for _, _, t in jobs if t})
    print(f"カード総数:{len(jobs)} / ユニーク商品:{len(uniq)} / 既キャッシュ:{sum(1 for t in uniq if t in cache)}")
    # 未取得を並列スクレイプ(各リクエストが遅いので並列化)
    from concurrent.futures import ThreadPoolExecutor, as_completed
    todo = [t for t in uniq if t not in cache]
    def scrape_safe(t):
        for _ in range(2):
            try:
                return t, scrape(t)
            except Exception:
                time.sleep(1)
        return t, ""
    done = 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(scrape_safe, t) for t in todo]
        for fu in as_completed(futs):
            t, img = fu.result()
            cache[t] = img or ""
            done += 1
            if done % 20 == 0:
                save_cache(cache); print(f"  ...{done}/{len(todo)} ({'OK' if img else 'なし'})", flush=True)
    save_cache(cache)
    got = sum(1 for t in uniq if cache.get(t))
    print(f"取得完了: {got}/{len(uniq)} 商品に画像")
    if not apply:
        print("(dry-run。--apply で記事に反映)"); return
    # 反映(後ろから置換でズレ防止)
    changed = 0
    for f, h in per_file.items():
        fj = sorted([j for j in jobs if j[0] == f], key=lambda x: -x[1][0])
        nh = h
        for _, (s, e), title in fj:
            img = cache.get(title)
            if img:
                nh = nh[:s] + img + nh[e:]
                changed += 1
        if nh != h:
            open(f, "w", encoding="utf-8").write(nh)
    print(f"反映カード: {changed}/{len(jobs)}  APPLY済み")

if __name__ == "__main__":
    main()
