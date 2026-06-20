# -*- coding: utf-8 -*-
"""法務ページ生成: privacy/terms/contact をブランドデザインで生成(自己完結CSS)。
サイトワイドのフッター404解消 + ステマ規制/アフィリ規約準拠。"""
import os, datetime

ROOT = os.path.dirname(__file__)
BASE = "https://richend0913.github.io/okurite"
TODAY = datetime.date.today().isoformat()
CONTACT_EMAIL = "next.growth0913@gmail.com"

SHELL = """<!DOCTYPE html>
<html lang="ja">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-63VB4HT3T2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-63VB4HT3T2');
</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Okurite</title>
  <link rel="canonical" href="{base}/{slug}.html">
  <meta name="description" content="{desc}">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="{title} | Okurite">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{base}/{slug}.html">
  <meta property="og:image" content="{base}/images/ogp.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">
  <style>
    :root{{--cream:#fdfaf6;--warm-white:#fff9f2;--blush-light:#fce8ef;--rose:#d4687a;--rose-dark:#b8506a;--gold:#b8922e;--text:#2d2320;--text-sub:#5a4e48;--text-muted:#9a8e88;--border:#e8ddd5;--radius:16px;}}
    *{{box-sizing:border-box;margin:0;padding:0;}}
    body{{font-family:'Noto Sans JP',sans-serif;color:var(--text);background:var(--cream);line-height:1.9;}}
    a{{color:var(--rose-dark);text-decoration:none;}}
    a:hover{{text-decoration:underline;}}
    .header{{background:var(--warm-white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:50;}}
    .header-inner{{max-width:1080px;margin:0 auto;padding:18px 24px;display:flex;align-items:center;justify-content:space-between;}}
    .logo{{font-family:'Noto Serif JP',serif;font-weight:700;font-size:1.5rem;color:var(--rose-dark);letter-spacing:.04em;}}
    .header-nav{{list-style:none;display:flex;gap:24px;}}
    .header-nav a{{color:var(--text-sub);font-size:.95rem;}}
    main{{max-width:760px;margin:0 auto;padding:56px 24px 40px;}}
    .breadcrumb{{font-size:.82rem;color:var(--text-muted);margin-bottom:24px;}}
    h1{{font-family:'Noto Serif JP',serif;font-size:2rem;color:var(--text);margin-bottom:8px;line-height:1.4;}}
    .updated{{color:var(--text-muted);font-size:.85rem;margin-bottom:36px;}}
    h2{{font-size:1.25rem;color:var(--rose-dark);margin:38px 0 14px;padding-left:14px;border-left:4px solid var(--gold);}}
    p{{margin-bottom:14px;color:var(--text-sub);}}
    ul.doc{{margin:0 0 16px 1.4em;color:var(--text-sub);}}
    ul.doc li{{margin-bottom:8px;}}
    .card{{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:24px 26px;margin:20px 0;box-shadow:0 4px 20px rgba(100,60,50,.06);}}
    .btn{{display:inline-block;background:var(--rose);color:#fff;padding:14px 30px;border-radius:999px;font-weight:700;margin-top:10px;}}
    .btn:hover{{background:var(--rose-dark);text-decoration:none;}}
    .footer{{background:var(--warm-white);border-top:1px solid var(--border);margin-top:48px;}}
    .footer-inner{{max-width:1080px;margin:0 auto;padding:36px 24px;text-align:center;}}
    .footer-bottom p{{font-size:.82rem;color:var(--text-muted);margin-bottom:8px;}}
  </style>
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="{base}/" class="logo">Okurite</a>
    <nav><ul class="header-nav">
      <li><a href="{base}/">トップ</a></li>
      <li><a href="{base}/blog/">コラム</a></li>
    </ul></nav>
  </div>
</header>
<main>
  <div class="breadcrumb"><a href="{base}/">ホーム</a> &rsaquo; {title}</div>
  <h1>{title}</h1>
  <p class="updated">最終更新日: {today}</p>
  {body}
</main>
<footer class="footer">
  <div class="footer-inner">
    <div class="footer-bottom">
      <p>当サイトはAmazonアソシエイト・楽天アフィリエイトプログラムに参加しています。</p>
      <p><a href="{base}/privacy.html">プライバシーポリシー</a> | <a href="{base}/terms.html">利用規約</a> | <a href="{base}/contact.html">お問い合わせ</a> | <a href="{base}/blog/">コラム一覧</a></p>
      <p>&copy; 2026 Okurite. All rights reserved.</p>
    </div>
  </div>
</footer>
</body>
</html>
"""

PRIVACY_BODY = """
  <p>Okurite（以下「当サイト」）は、ご利用いただく皆さまの個人情報・プライバシーを尊重し、適切に取り扱います。本ポリシーは、当サイトにおける情報の取得・利用・管理について定めたものです。</p>

  <h2>1. 運営者情報</h2>
  <p>当サイトはギフト選びを支援する個人運営のメディアです。お問い合わせは<a href="{base}/contact.html">お問い合わせページ</a>よりお願いいたします。</p>

  <h2>2. 取得する情報</h2>
  <ul class="doc">
    <li>アクセス解析ツール（Googleアナリティクス4）による閲覧情報（閲覧ページ、滞在時間、参照元、利用端末・ブラウザの種類など）</li>
    <li>Cookie（クッキー）等を通じて自動的に収集される匿名の利用データ</li>
  </ul>
  <p>これらの情報に氏名・住所・電話番号など個人を直接特定する情報は含まれません。</p>

  <h2>3. 利用目的</h2>
  <ul class="doc">
    <li>サイトの利用状況の把握とコンテンツ・利便性の改善</li>
    <li>より役立つギフト情報を提供するための分析</li>
  </ul>

  <h2>4. アクセス解析ツールについて</h2>
  <p>当サイトは、Googleによるアクセス解析ツール「Googleアナリティクス」を利用しています。Googleアナリティクスはトラフィックデータの収集のためにCookieを使用します。このデータは匿名で収集されており、個人を特定するものではありません。Cookieを無効にすることで収集を拒否することが可能です。詳しくは<a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">Googleのポリシー</a>をご確認ください。</p>

  <h2>5. アフィリエイトプログラムについて</h2>
  <p>当サイトは、Amazon.co.jpを宣伝しリンクすることによってサイトが紹介料を獲得できる手段を提供することを目的に設定されたアフィリエイトプログラムである「Amazonアソシエイト・プログラム」の参加者です。また「楽天アフィリエイト」にも参加しています。</p>
  <p>当サイト内の商品紹介リンクを経由して各サービスで商品をご購入された場合、当サイトが各プログラムの規定に基づく紹介料を受け取ることがあります。リンク先のAmazon・楽天市場等での購入・決済・個人情報の取り扱いは、各サービスの規約・プライバシーポリシーに従って行われます。商品価格・在庫・送料等は変動するため、必ずリンク先の最新情報をご確認ください。</p>

  <h2>6. 第三者配信事業者によるCookieの利用</h2>
  <p>第三者配信事業者（Amazon・楽天・Google等）は、Cookieを使用して、ユーザーが当サイトや他のサイトに過去にアクセスした際の情報に基づいて広告・リンクを表示することがあります。ユーザーはブラウザの設定によりCookieを無効化できます。</p>

  <h2>7. 免責事項</h2>
  <p>当サイトに掲載する情報は正確性に努めていますが、その完全性・有用性を保証するものではありません。当サイトの情報やリンク先サービスのご利用によって生じたいかなる損害についても、当サイトは責任を負いかねます。</p>

  <h2>8. 本ポリシーの変更</h2>
  <p>当サイトは、必要に応じて本ポリシーを改定することがあります。変更後の内容は本ページに掲載した時点で効力を生じるものとします。</p>
"""

TERMS_BODY = """
  <p>本利用規約（以下「本規約」）は、Okurite（以下「当サイト」）の利用条件を定めるものです。当サイトをご利用いただいた時点で、本規約に同意いただいたものとみなします。</p>

  <h2>1. コンテンツの著作権</h2>
  <p>当サイトに掲載されている文章・画像・構成等の著作権は、当サイトまたは正当な権利者に帰属します。引用の範囲を超える無断転載・複製・改変を禁止します。</p>

  <h2>2. 商品情報・価格について</h2>
  <p>当サイトで紹介する商品の価格・在庫・仕様・送料・販売状況等は、執筆時点の情報であり、リンク先（Amazon・楽天市場等）の都合により予告なく変更されることがあります。ご購入の際は、必ずリンク先の最新情報をご自身でご確認ください。</p>

  <h2>3. リンク先での取引について</h2>
  <p>当サイトはギフト選びの情報提供を目的としており、商品の販売主体ではありません。商品の購入・決済・配送・返品・お問い合わせ等は、すべてリンク先の各販売事業者（Amazon・楽天市場の各ショップ等）との間で、各サービスの規約に基づいて行われます。これらの取引に関するトラブルについて、当サイトは一切の責任を負いません。</p>

  <h2>4. 免責事項</h2>
  <ul class="doc">
    <li>当サイトの情報の正確性・完全性・最新性・有用性について保証するものではありません。</li>
    <li>当サイトの利用、または利用できなかったことにより生じた損害について、当サイトは責任を負いません。</li>
    <li>当サイトからリンクされた外部サイトの内容について、当サイトは責任を負いません。</li>
  </ul>

  <h2>5. 禁止事項</h2>
  <p>当サイトの利用にあたり、法令または公序良俗に反する行為、当サイトの運営を妨害する行為、その他当サイトが不適切と判断する行為を禁止します。</p>

  <h2>6. 本規約の変更</h2>
  <p>当サイトは、必要に応じて本規約を変更することがあります。変更後の本規約は、本ページに掲載した時点で効力を生じるものとします。</p>
"""

CONTACT_BODY = """
  <p>Okuriteをご覧いただきありがとうございます。記事内容に関するご指摘、掲載商品・リンクに関するお問い合わせ、その他ご意見・ご要望は、下記よりお気軽にご連絡ください。</p>

  <div class="card">
    <h2 style="margin-top:0;border:none;padding:0;">メールでのお問い合わせ</h2>
    <p>下記アドレス宛にメールをお送りください。内容を確認のうえ、順次対応いたします（個人運営のため、お返事までお時間をいただく場合があります）。</p>
    <p style="font-weight:700;color:var(--text);">{email}</p>
    <a class="btn" href="mailto:{email}?subject=Okurite%E3%81%B8%E3%81%AE%E3%81%8A%E5%95%8F%E3%81%84%E5%90%88%E3%82%8F%E3%81%9B">メールを作成する</a>
  </div>

  <h2>お問い合わせ前のご確認</h2>
  <ul class="doc">
    <li>商品の購入・配送・返品・在庫に関するお問い合わせは、当サイトではお答えできません。各販売店（Amazon・楽天市場の各ショップ等）へ直接お問い合わせください。</li>
    <li>掲載情報・価格は変動する場合があります。最新情報はリンク先にてご確認ください。</li>
    <li>個人情報の取り扱いについては<a href="{base}/privacy.html">プライバシーポリシー</a>をご覧ください。</li>
  </ul>

  <h2>掲載・提携について</h2>
  <p>記事への掲載・商品紹介・提携等のご相談も、上記メールアドレスより承っております。</p>
"""

PAGES = [
    ("privacy", "プライバシーポリシー",
     "Okuriteのプライバシーポリシー。アクセス解析・Cookie・Amazonアソシエイト/楽天アフィリエイトプログラムへの参加と情報の取り扱いについて。",
     PRIVACY_BODY),
    ("terms", "利用規約",
     "Okuriteの利用規約。コンテンツの著作権、商品情報・価格、リンク先での取引、免責事項について定めています。",
     TERMS_BODY),
    ("contact", "お問い合わせ",
     "Okuriteへのお問い合わせ窓口。記事・掲載・提携に関するご連絡はこちらから。",
     CONTACT_BODY),
]

for slug, title, desc, body in PAGES:
    body_filled = body.format(base=BASE, email=CONTACT_EMAIL)
    html = SHELL.format(title=title, slug=slug, desc=desc, base=BASE,
                        today=TODAY, body=body_filled)
    out = os.path.join(ROOT, f"{slug}.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {out} ({len(html)} bytes)")

print("done.")
