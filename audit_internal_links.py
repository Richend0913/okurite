# -*- coding: utf-8 -*-
"""内部リンク404監査: 各記事の相対/内部リンクが実在ファイルを指しているか検証。"""
import os, re, glob
from collections import Counter

ROOT = os.path.dirname(__file__)
BLOG = os.path.join(ROOT, "blog")
href_re = re.compile(r'href="([^"]*)"')

def resolve(base_dir, href):
    # strip anchors/query
    h = href.split("#")[0].split("?")[0]
    if not h:
        return None
    if h.startswith("http") or h.startswith("mailto:") or h.startswith("//"):
        return None  # external handled elsewhere
    # absolute path on the site (GitHub Pages serves under /okurite/)
    if h.startswith("/okurite/"):
        target = os.path.join(ROOT, h[len("/okurite/"):])
    elif h.startswith("/"):
        target = os.path.join(ROOT, h.lstrip("/"))
    else:
        target = os.path.normpath(os.path.join(base_dir, h))
    # directory -> index.html
    if h.endswith("/"):
        target = os.path.join(target, "index.html")
    return target

issues = []
checked = 0
for path in sorted(glob.glob(os.path.join(BLOG, "*.html"))) + [os.path.join(ROOT, "index.html")]:
    name = os.path.relpath(path, ROOT)
    base = os.path.dirname(path)
    with open(path, encoding="utf-8") as f:
        html = f.read()
    for h in href_re.findall(html):
        t = resolve(base, h)
        if t is None:
            continue
        checked += 1
        if not os.path.exists(t):
            issues.append((name, h, os.path.relpath(t, ROOT)))

print(f"checked internal links: {checked}")
print(f"BROKEN: {len(issues)}")
by_target = Counter(i[2] for i in issues)
print("\n=== broken targets (most common) ===")
for tgt, cnt in by_target.most_common(30):
    print(f"  {cnt:3d}x -> {tgt}")
print("\n=== samples (first 20) ===")
for name, h, tgt in issues[:20]:
    print(f"  {name}: href={h} -> {tgt}")
