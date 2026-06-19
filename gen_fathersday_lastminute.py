# -*- coding: utf-8 -*-
"""Generate last-minute father's day article (today/next-day/digital gifts)."""
import urllib.parse, io, sys

AMZ_TAG = "okuritegift-22"
RKT_BASE = "https://hb.afl.rakuten.co.jp/ichiba/522e40a0.f2dc4208.522e40a1.385f875e/?pc="
RKT_SUFFIX = "&link_type=hybrid_url"

def amz(kw):
    return f"https://www.amazon.co.jp/s?k={urllib.parse.quote(kw)}&tag={AMZ_TAG}"

def rkt(kw):
    inner = "https://search.rakuten.co.jp/search/mall/" + urllib.parse.quote(kw) + "/"
    return RKT_BASE + urllib.parse.quote(inner, safe="") + RKT_SUFFIX

def card(num, title, price, desc, kw, img):
    return f'''    <div class="gift-card">
      <img class="gift-card-img" src="{img}" alt="{num}. {title}" loading="lazy">
      <div class="gift-card-title">{num}. {title}</div>
      <div class="gift-card-price">{price}</div>
      <div class="gift-card-desc">{desc}</div>
      <div class="gift-card-buttons">
        <a href="{amz(kw)}" target="_blank" rel="noopener sponsored" class="gift-card-link">Amazonで見る</a>
        <a href="{rkt(kw)}" target="_blank" rel="noopener sponsored" class="gift-card-link rakuten">楽天で見る</a>
      </div>
    </div>
'''

HERO = "https://images.unsplash.com/photo-1513885535751-8b9238bd345a?w=800&h=400&fit=crop"

# === Tier 1: メール・デジタルで今日届く ===
t1 = ""
t1 += card(1, "Amazonギフトカード Eメールタイプ（メッセージ入り）", "金額自由（1,000円〜）",
    "注文後すぐにお父さんのメールへ届く電子ギフト。配送ゼロなので父の日当日でも間に合います。メッセージとデザインを添えられ、お父さんは好きなものを自分で選べるのが利点。「何が欲しいか分からない」時の最終回答です。",
    "Amazonギフトカード Eメールタイプ 父の日", "https://m.media-amazon.com/images/I/41YQ2gqB5DL._AC_.jpg")
t1 += card(2, "スターバックス eGift（ドリンクチケット）", "¥500〜",
    "LINEやメールで今すぐ送れるスタバのデジタルギフト。受け取ったお父さんは近くの店舗でコーヒー1杯と交換できます。住所も配送も不要、スマホひとつで数分で贈れる手軽さが、直前の父の日にぴったりです。",
    "スターバックス eギフト チケット", "https://m.media-amazon.com/images/I/31m6cVKZ8RL._AC_.jpg")
t1 += card(3, "選べる体験ギフト（eギフト/カタログ）", "¥5,000前後",
    "温泉・食事・ものづくり体験などからお父さんが好きな体験を選べるカタログギフト。eギフト版ならメールで即日納品が可能。「モノは足りている」というお父さんに、思い出という特別な時間を贈れます。",
    "体験ギフト カタログ 父の日 eギフト", "https://m.media-amazon.com/images/I/51rXyVy0qPL._AC_.jpg")

# === Tier 2: あす楽・プライムで翌日に間に合う ===
t2 = ""
t2 += card(4, "プレミアムビール 飲み比べギフトセット", "¥3,000前後",
    "Amazonプライム・楽天あす楽対応なら、今日頼んで明日届く定番。よなよなエールやプレモルなど普段と違う一杯は、晩酌好きのお父さんの鉄板。父の日ギフト対応の熨斗・ラッピングも選べます。",
    "ビール 飲み比べ ギフト あす楽 父の日", "https://m.media-amazon.com/images/I/61gO0z3qVOL._AC_.jpg")
t2 += card(5, "国産うなぎ蒲焼き 化粧箱入り", "¥4,000〜6,000",
    "スタミナをつけてほしいお父さんへ。冷蔵・冷凍の最短発送便なら週末の食卓に間に合います。温めるだけで専門店の味、父の日のごちそうとして毎年人気の高い一品です。",
    "うなぎ 蒲焼き ギフト 父の日", "https://m.media-amazon.com/images/I/71Qe7Wc0qkL._AC_.jpg")
t2 += card(6, "コードレス筋膜リリースガン（マッサージガン）", "¥4,000前後",
    "肩・腰の疲れをほぐすハンディマッサージガン。プライム当日・翌日便で間に合うガジェット系の人気株。「体を気遣ってくれた」と気持ちが伝わり、毎日使ってもらえる実用ギフトです。",
    "マッサージガン 筋膜リリース 父の日", "https://m.media-amazon.com/images/I/61yj5q0H3pL._AC_.jpg")
t2 += card(7, "名入れタンブラー・グラス（即日対応ショップ）", "¥3,500前後",
    "名前やメッセージを刻める特別感のある一品。楽天の即日・翌日出荷対応ショップを選べば直前でも間に合います。世界に一つだけのグラスで晩酌が特別な時間に変わります。",
    "名入れ タンブラー グラス 父の日 即日", "https://m.media-amazon.com/images/I/61QF6m6kK9L._AC_.jpg")
t2 += card(8, "高級コーヒー ドリップバッグ アソート", "¥2,500前後",
    "猿田彦珈琲など専門店のドリップバッグ詰め合わせ。器具不要で毎朝の一杯がワンランク上に。常温配送で最短発送、コーヒー好きのお父さんへ確実に喜ばれる軽やかなギフトです。",
    "コーヒー ドリップ ギフト 父の日", "https://m.media-amazon.com/images/I/71Ypw8Q3o5L._AC_.jpg")

OUT = f'''<!DOCTYPE html>
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
  <title>今からでも間に合う父の日ギフト2026｜当日・即日に贈れる人気プレゼント8選 - Okurite</title>
  <meta name="description" content="父の日まであと少し！今からでも間に合う父の日ギフトを厳選。メールで今日届くデジタルギフトと、あす楽・プライムで翌日届く人気プレゼント8選を紹介します。">
  <meta name="keywords" content="父の日,間に合う,当日,即日,デジタルギフト,プレゼント,直前">
  <link rel="canonical" href="https://richend0913.github.io/okurite/blog/fathers-day-last-minute-2026.html">
  <meta property="og:title" content="今からでも間に合う父の日ギフト2026｜当日・即日に贈れる人気8選">
  <meta property="og:description" content="メールで今日届くデジタルギフトと、あす楽で翌日届く人気プレゼント8選。父の日直前でも間に合う。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://richend0913.github.io/okurite/blog/fathers-day-last-minute-2026.html">
  <meta property="og:image" content="{HERO}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{HERO}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
  <style>
        .article {{ max-width: 720px; margin: 0 auto; padding: 80px 24px 60px; }}
    .article h1 {{ font-size: 1.5rem; font-weight: 700; color: #2d2a26; line-height: 1.7; margin-bottom: 12px; }}
    .article-meta {{ font-size: .8rem; color: #999; margin-bottom: 28px; }}
    .article-hero {{ width: 100%; height: 320px; object-fit: cover; border-radius: 14px; margin-bottom: 32px; }}
    .article h2 {{ font-size: 1.2rem; font-weight: 700; color: #8b6914; margin: 40px 0 16px; padding-bottom: 10px; border-bottom: 2px solid rgba(139,105,20,.06); }}
    .article h3 {{ font-size: 1rem; font-weight: 700; color: #2d2a26; margin: 28px 0 12px; }}
    .article p {{ font-size: .9rem; line-height: 2; color: #555; margin-bottom: 16px; }}
    .article ul, .article ol {{ margin: 0 0 16px 24px; }}
    .article li {{ font-size: .9rem; line-height: 2; color: #555; margin-bottom: 4px; }}
    .gift-card {{ background: #fff; border: 1px solid rgba(180,160,120,.12); border-radius: 14px; padding: 24px; margin-bottom: 20px; transition: box-shadow .3s; }}
    .gift-card:hover {{ box-shadow: 0 2px 8px rgba(0,0,0,.04); }}
    .gift-card-img {{ width: 100%; height: 180px; object-fit: cover; border-radius: 8px; margin-bottom: 16px; }}
    .gift-card-title {{ font-size: 1rem; font-weight: 700; color: #2d2a26; margin-bottom: 4px; }}
    .gift-card-price {{ font-size: .9rem; color: #c62828; font-weight: 700; margin-bottom: 10px; }}
    .gift-card-desc {{ font-size: .85rem; color: #666; line-height: 1.8; margin-bottom: 16px; }}
    .gift-card-buttons {{ display: flex; gap: 10px; flex-wrap: wrap; }}
    .gift-card-link {{ display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 11px 24px; background: #ff9900; color: #fff; border-radius: 8px; font-size: .85rem; font-weight: 600; transition: all .2s; text-decoration: none; flex: 1; min-width: 140px; text-align: center; }}
    .gift-card-link:hover {{ opacity: .9; color: #fff; transform: translateY(-1px); }}
    .gift-card-link.rakuten {{ background: #bf0000; }}
    .gift-card-link.rakuten:hover {{ background: #a00; }}
    .toc {{ background: #faf8f5; border: 1px solid rgba(180,160,120,.15); border-radius: 14px; padding: 20px 24px; margin-bottom: 32px; }}
    .toc-title {{ font-size: .9rem; font-weight: 700; color: #8b6914; margin-bottom: 12px; }}
    .toc a {{ font-size: .85rem; color: #555; line-height: 2.2; display: block; padding-left: 16px; border-left: 2px solid transparent; transition: all .2s; }}
    .toc a:hover {{ color: #8b6914; border-left-color: #8b6914; padding-left: 20px; }}
    .breadcrumb {{ font-size: .8rem; color: #999; margin-bottom: 16px; }}
    .breadcrumb a {{ color: #8b6914; }}
    .cta-box {{ background: linear-gradient(135deg, #faf8f5, #f0ebe2); border: 1px solid rgba(180,160,120,.15); border-radius: 20px; padding: 32px; text-align: center; margin: 40px 0; }}
    .cta-box p {{ font-size: .95rem; color: #555; margin-bottom: 16px; }}
    .cta-btn {{ display: inline-block; padding: 14px 40px; background: linear-gradient(135deg, #c49b1a, #8b6914); color: #fff; border-radius: 999px; font-size: .95rem; font-weight: 600; transition: all .2s; text-decoration: none; }}
    .cta-btn:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(139,105,20,.25); color: #fff; }}
    .related-articles {{ background: #faf8f5; border: 1px solid rgba(180,160,120,.15); border-radius: 14px; padding: 24px; margin: 40px 0; }}
    .related-articles h3 {{ font-size: 1rem; font-weight: 700; color: #8b6914; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid rgba(180,160,120,.15); }}
    .related-articles ul {{ list-style: none; margin: 0; padding: 0; }}
    .related-articles li {{ padding: 10px 0; border-bottom: 1px solid rgba(180,160,120,.08); margin-bottom: 0; }}
    .related-articles li:last-child {{ border-bottom: none; }}
    .related-articles a {{ font-size: .88rem; color: #555; display: flex; align-items: center; gap: 8px; }}
    .related-articles a::before {{ content: ''; width: 6px; height: 6px; background: #c49b1a; border-radius: 50%; flex-shrink: 0; }}
    .related-articles a:hover {{ color: #8b6914; }}
    @media (max-width: 768px) {{ .article {{ padding: 72px 16px 48px; }} .article-hero {{ height: 200px; }} .gift-card-buttons {{ flex-direction: column; }} .gift-card-link {{ width: 100%; justify-content: center; }} }}
  </style>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "今からでも間に合う父の日ギフト2026｜当日・即日に贈れる人気8選",
    "datePublished": "2026-06-19",
    "dateModified": "2026-06-19",
    "author": {{"@type": "Organization", "name": "Okurite"}},
    "publisher": {{"@type": "Organization", "name": "Okurite"}},
    "description": "メールで今日届くデジタルギフトと、あす楽で翌日届く人気プレゼント8選。父の日直前でも間に合う。",
    "image": "{HERO}"
  }}
  </script>
<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "TOP", "item": "https://richend0913.github.io/okurite/"}},
      {{"@type": "ListItem", "position": 2, "name": "コラム", "item": "https://richend0913.github.io/okurite/blog/"}},
      {{"@type": "ListItem", "position": 3, "name": "今からでも間に合う父の日ギフト2026", "item": "https://richend0913.github.io/okurite/blog/fathers-day-last-minute-2026.html"}}
    ]
  }}
  </script>
</head>
<body>
  <header class="header">
    <div class="header-inner">
      <a href="../" class="logo" style="text-decoration:none;">Okurite</a>
      <button class="hamburger" onclick="document.querySelector('.nav').classList.toggle('open')">&#9776;</button>
      <ul class="nav">
        <li><a href="../">TOP</a></li>
        <li><a href="../#gifts">ギフト検索</a></li>
        <li><a href="./">コラム</a></li>
      </ul>
    </div>
  </header>

  <article class="article">
    <div class="breadcrumb"><a href="../">TOP</a> &gt; <a href="./">コラム</a> &gt; 今からでも間に合う父の日ギフト</div>

    <h1>今からでも間に合う父の日ギフト2026｜当日・即日に贈れる人気プレゼント8選</h1>
    <div class="article-meta">2026年6月19日 公開｜父の日特集</div>
    <div style="display:flex;align-items:center;gap:10px;background:linear-gradient(135deg,#c62828,#e53935);color:#fff;border-radius:12px;padding:13px 18px;margin:0 0 22px;font-weight:700;font-size:.9rem;line-height:1.55;box-shadow:0 4px 14px rgba(198,40,40,.25);">
      <span style="font-size:1.25rem;">⏰</span>
      <span>父の日は<strong>6/21（日）</strong>。まだ間に合います。<strong>メールで今日届くデジタルギフト</strong>、または<strong>あす楽・プライムの翌日便</strong>を選べば直前でもOK。</span>
    </div>

    <img class="article-hero" src="{HERO}" alt="今からでも間に合う父の日ギフト" loading="lazy">

    <p>「父の日、すっかり忘れてた…」「気づいたら明日が父の日」。そんな駆け込みでも、まだ諦めるのは早いです。今は<strong>メールやLINEで数分で贈れるデジタルギフト</strong>や、<strong>あす楽・プライム当日/翌日便で間に合う人気ギフト</strong>がたくさんあります。</p>
    <p>この記事では、<strong>「今からでも間に合う」を最優先</strong>に、お父さんが本当に喜ぶ父の日ギフトだけを厳選しました。「配送が間に合わないから」と諦めず、感謝の気持ちを今年も届けましょう。</p>

    <div class="toc">
      <div class="toc-title">この記事の目次</div>
      <a href="#today">1. メール・デジタルで今日届くギフト</a>
      <a href="#nextday">2. あす楽・プライムで翌日に間に合うギフト</a>
      <a href="#tips">3. 直前でも失敗しない選び方のコツ</a>
    </div>

    <h2 id="today">1. メール・デジタルで今日届くギフト</h2>
    <p>配送を待つ必要がゼロ。注文後すぐにお父さんのメールやLINEへ届くので、<strong>父の日当日でも確実に間に合います</strong>。「とにかく今日中に贈りたい」という方はここから選べば失敗しません。</p>
{t1}
    <h2 id="nextday">2. あす楽・プライムで翌日に間に合うギフト</h2>
    <p>「やっぱりモノを贈りたい」という方へ。Amazonプライムや楽天あす楽の対応商品なら、<strong>今日注文して明日届く</strong>ので父の日（6/21）に十分間に合います。注文時にお届け日を必ず確認しましょう。</p>
{t2}
    <h2 id="tips">3. 直前でも失敗しない選び方のコツ</h2>

    <h3>1. まずはお届け日を確認する</h3>
    <p>直前ギフトで最も大切なのは「いつ届くか」。Amazonは商品ページの「お届け日時」、楽天は「あす楽」マークを必ずチェックしましょう。デジタルギフトなら配送日を気にせず確実です。</p>

    <h3>2. 迷ったらデジタルギフト一択</h3>
    <p>「何が欲しいか分からない」「サイズや好みが不安」という時は、お父さんが自分で選べるギフトカードやeギフトが安全。配送ゼロで当日に間に合い、もらった側も嬉しい万能な選択肢です。</p>

    <h3>3. メッセージを一言添える</h3>
    <p>デジタルでもモノでも、「いつもありがとう」の一言を添えるだけで価値が何倍にもなります。照れくさい言葉も、メッセージカードやギフトのメッセージ欄なら自然に伝えられます。</p>

    <div class="cta-box">
      <p>Okuriteでは、贈る相手やシーンに合わせて<br>ぴったりのギフトを簡単に探せます。</p>
      <a href="../#gifts" class="cta-btn">ギフトを探す</a>
    </div>

    <h2>まとめ</h2>
    <p>父の日を忘れていても、今からでも間に合う選択肢はたくさんあります。<strong>当日に贈るならデジタルギフト、翌日に届けるならあす楽・プライム便</strong>。大切なのは金額やタイミングの完璧さより、「お父さんを思って贈る」気持ちです。</p>
    <p>2026年の父の日は<strong>6月21日（日）</strong>。間に合ううちに、お父さんに感謝を届けましょう。</p>

    <div class="related-articles"><h3>関連記事</h3><ul>
        <li><a href="fathers-day-2026.html">父の日プレゼント｜"何もいらない"と言う父が実際に使ったもの10選</a></li>
        <li><a href="gift-for-father-in-law.html">義父へのプレゼントおすすめ10選｜父の日・誕生日に失敗しない選び方</a></li>
        <li><a href="experience-gift.html">体験ギフトのおすすめ｜モノより思い出を贈る人気プレゼント</a></li>
        <li><a href="gift-budget-3000.html">予算3,000円のプレゼント特集｜気の利いたプチギフト</a></li>
        <li><a href="budget-5000-gift.html">予算5,000円で贈るセンスのいいプレゼント12選｜男女別おすすめ</a></li>
      </ul></div>
  </article>

    <footer class="footer">
    <div class="footer-inner">
      <div class="footer-grid">
        <div class="footer-brand">
          <span class="footer-logo">Okurite</span>
          <p>シーン別ギフト・プレゼント検索サービス。<br>あらゆるシーンのギフト選びをサポートします。</p>
        </div>
        <div class="footer-col">
          <h4>シーン別</h4>
          <ul>
            <li><a href="mothers-day-2026.html">母の日</a></li>
            <li><a href="fathers-day-2026.html">父の日</a></li>
            <li><a href="birthday-gift-women.html">誕生日</a></li>
            <li><a href="wedding-gift-guide.html">結婚祝い</a></li>
            <li><a href="baby-shower-gift.html">出産祝い</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>予算別</h4>
          <ul>
            <li><a href="budget-500-gift.html">500円以下</a></li>
            <li><a href="gift-exchange-1000.html">1,000円</a></li>
            <li><a href="gift-budget-3000.html">3,000円</a></li>
            <li><a href="budget-5000-gift.html">5,000円</a></li>
            <li><a href="budget-10000-gift.html">10,000円</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>当サイトはAmazonアソシエイトプログラム・楽天アフィリエイトプログラムに参加しています。</p>
        <p style="margin-top:8px;"><a href="../">TOP</a> | <a href="./">コラム</a></p>
        <p style="margin-top:8px;">&copy; 2026 Okurite. All rights reserved.</p>
      </div>
    </div>
  </footer>
<script>/* okurite-aff-track */
document.addEventListener('click',function(e){{
  var a=e.target.closest&&e.target.closest('a'); if(!a||!a.href) return;
  var h=a.href, t=(a.textContent||''), d=null;
  if(h.indexOf('amazon.co.jp')>-1||h.indexOf('amzn')>-1) d='amazon';
  else if(h.indexOf('rakuten.co.jp')>-1||h.indexOf('hb.afl.rakuten')>-1) d='rakuten';
  else if(h.indexOf('moshimo')>-1||h.indexOf('a8.net')>-1||h.indexOf('valuecommerce')>-1)
    d = t.indexOf('楽天')>-1?'rakuten':(t.indexOf('Amazon')>-1?'amazon':'affiliate');
  if(d&&typeof gtag==='function') gtag('event','affiliate_click',{{affiliate:d,link_url:h,page:location.pathname}});
}},true);
</script>
</body>
</html>
'''

with io.open("blog/fathers-day-last-minute-2026.html", "w", encoding="utf-8") as f:
    f.write(OUT)
print("WROTE blog/fathers-day-last-minute-2026.html", len(OUT), "bytes")
