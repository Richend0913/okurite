# -*- coding: utf-8 -*-
"""アフィリリンク健全性監査: 全記事のAmazon/楽天リンクのタグ欠落・素URL・空リンクを検出。"""
import os, re, glob

BLOG = os.path.join(os.path.dirname(__file__), "blog")
AMZ_TAG = "tag=okuritegift-22"
RAK_AFL = "hb.afl.rakuten.co.jp/ichiba/522e40a0.f2dc4208.522e40a1.385f875e"

href_re = re.compile(r'href="([^"]*)"')

issues = []
totals = {"files": 0, "amazon": 0, "rakuten": 0,
          "amz_no_tag": 0, "rak_raw": 0, "empty": 0}

for path in sorted(glob.glob(os.path.join(BLOG, "*.html"))):
    name = os.path.basename(path)
    if name == "index.html":
        continue
    totals["files"] += 1
    with open(path, encoding="utf-8") as f:
        html = f.read()
    for h in href_re.findall(html):
        hl = h.lower()
        # empty / placeholder links
        if h.strip() in ("", "#") or h.strip().startswith("javascript:"):
            totals["empty"] += 1
            issues.append((name, "EMPTY", h))
            continue
        if "amazon." in hl:
            totals["amazon"] += 1
            if AMZ_TAG not in h:
                totals["amz_no_tag"] += 1
                issues.append((name, "AMZ_NO_TAG", h))
        if "rakuten.co.jp" in hl:
            totals["rakuten"] += 1
            # 楽天リンクはアフィリ経由(hb.afl)でなければコミッションゼロ
            if "hb.afl.rakuten.co.jp" in hl:
                if RAK_AFL not in h:
                    totals["rak_raw"] += 1
                    issues.append((name, "RAK_WRONG_ID", h))
            else:
                # search.rakuten.co.jp等の素URL = アフィリ未経由
                totals["rak_raw"] += 1
                issues.append((name, "RAK_RAW", h))

print("=== SUMMARY ===")
for k, v in totals.items():
    print(f"  {k}: {v}")
print(f"\n=== ISSUES ({len(issues)}) ===")
from collections import Counter
by_type = Counter(i[1] for i in issues)
print("by type:", dict(by_type))
by_file = Counter(i[0] for i in issues)
print(f"affected files: {len(by_file)}")
for name, cnt in by_file.most_common(20):
    print(f"  {name}: {cnt}")
print("\n=== SAMPLES (first 15) ===")
for name, t, h in issues[:15]:
    print(f"  [{t}] {name}: {h[:120]}")
