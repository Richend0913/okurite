import json, urllib.parse

gifts = []
c = 0

def a(name, price, budget, desc, td, reason, stars, targets, scenes, cat):
    global c; c += 1
    gifts.append({
        "id": c, "name": name, "price": price, "budget": budget,
        "desc": desc, "target_detail": td, "reason": reason, "stars": stars,
        "targets": targets, "scenes": scenes, "img": "", "category": cat,
        "rakutenUrl": "https://search.rakuten.co.jp/search/mall/" + urllib.parse.quote(name) + "/",
        "amazonUrl": "https://www.amazon.co.jp/s?k=" + urllib.parse.quote(name) + "&tag=okuritegift-22"
    })

# ===== 女性コスメ (15) =====
a("SK-II フェイシャルトリートメントエッセンス","¥11,990","10k+","世界中で愛される美容液。90%以上天然成分ピテラ配合。","30代以上のスキンケアにこだわる女性へ","使うたびに透明感が増すと評判のロングセラー",{"practical":5,"surprise":3,"looks":4},["female","parents"],["mothers-day","birthday","christmas"],"コスメ")
a("ジルスチュアート ブルーミィレイヤード フレグランス ハンドクリーム","¥2,750","3k5k","上品なフローラルの香りと保湿力が人気。ジルスチュアートらしいかわいいパッケージ。","甘いものが好きなおしゃれ女性へ","プレゼントにぴったりなギフトボックス入り",{"practical":4,"surprise":3,"looks":5},["female"],["mothers-day","birthday","valentines","christmas"],"コスメ")
a("ロクシタン シア バター ハンドクリーム","¥2,530","3k5k","南フランス発。シアバター20%配合で手をしっかり保湿。香りも選べる。","手荒れが気になる女性・主婦へ","定番中の定番。外れなしのギフト",{"practical":5,"surprise":2,"looks":4},["female","parents"],["mothers-day","birthday","christmas","thanks"],"コスメ")
a("THREE バランシング スチーム オーバーローション","¥7,700","5k10k","天然・オーガニック成分95%以上。肌のバランスを整える化粧水。","自然派・オーガニック好きな女性へ","スタイリッシュなパッケージで見た目も◎",{"practical":5,"surprise":3,"looks":5},["female"],["birthday","christmas","mothers-day"],"コスメ")
a("イソップ レインウォーター バランシング トナー","¥7,480","5k10k","人気ブランドAesopの化粧水。シンプルで上質なスキンケア。","センスのある女性・美容好きへ","もらって嬉しいブランド力と実力を兼備",{"practical":4,"surprise":4,"looks":5},["female"],["birthday","christmas","mothers-day"],"コスメ")
a("SABON ボディスクラブ ジャスミン&コーデュロイ","¥4,290","3k5k","イスラエル発の人気ブランド。海塩スクラブで肌をつるつるに。","ボディケアが好きな女性へ","芳醇な香りとザラメ感が気持ちいい",{"practical":4,"surprise":4,"looks":5},["female"],["birthday","christmas","mothers-day","valentines"],"コスメ")
a("シロ ホワイトリリー オードパルファン","¥9,350","5k10k","日本発ブランドSIROの人気香水。清楚なホワイトリリーの香り。","清楚系・和モダン好きな女性へ","洗練されたボトルデザインも贈り物映え",{"practical":3,"surprise":5,"looks":5},["female"],["birthday","christmas","valentines"],"コスメ")
a("ディオール アディクト リップ グロウ","¥5,280","5k10k","唇の色を引き出す魔法のリップバーム。Diorの定番人気コスメ。","メイク好きの女性全般へ","高級感ありつつ使いやすい万能コスメ",{"practical":5,"surprise":3,"looks":5},["female"],["birthday","valentines","christmas"],"コスメ")
a("ランコム ジェニフィック アドバンスト N","¥19,800","10k+","肌の輝きを引き出す美容液。世界でNo.1の売上実績。","本格美容に興味のある女性へ","プレゼントとしての格が違う高級美容液",{"practical":5,"surprise":4,"looks":4},["female","parents"],["birthday","christmas","mothers-day"],"コスメ")
a("クリニーク モイスチャー サージ 100H","¥6,270","5k10k","72時間保湿が続く人気の保湿クリーム。敏感肌にも使いやすい。","忙しくてスキンケアに時間がとれない女性へ","クリニークの看板商品で安定した人気",{"practical":5,"surprise":2,"looks":3},["female"],["birthday","christmas","mothers-day"],"コスメ")
a("雪肌精 クリームN","¥7,150","5k10k","日本の伝統美容・漢方の知恵を活かしたオールインワンクリーム。","和コスメが好きな女性・お母さんへ","香りが上品で年齢問わず喜ばれる",{"practical":5,"surprise":3,"looks":4},["female","parents"],["mothers-day","birthday","christmas","thanks"],"コスメ")
a("ポーラ BA ローション L","¥22,000","10k+","最先端技術の化粧水。肌の奥から美しさを引き出す。","美容に投資する意識の高い女性へ","高級感と効果を両立した至高の一本",{"practical":5,"surprise":4,"looks":4},["female"],["birthday","christmas","mothers-day"],"コスメ")
a("ルナソル スキンモデリングアイズ","¥6,050","5k10k","上品な発色と使いやすさで人気のアイシャドウパレット。","メイクが好きな女性・コスメマニアへ","デパコスならではの高級感",{"practical":4,"surprise":3,"looks":5},["female"],["birthday","valentines","christmas"],"コスメ")
a("RMK ベーシック リクイドファンデーション","¥7,040","5k10k","自然なツヤとカバー力が人気のリキッドファンデーション。","ナチュラルメイクが好きな女性へ","肌がきれいに見えると口コミ多数",{"practical":5,"surprise":2,"looks":4},["female"],["birthday","christmas"],"コスメ")
a("SUQQU ディファイニング アイズ","¥8,800","5k10k","日本発高級コスメSUQQUの人気アイシャドウ。繊細な色みが特徴。","上品・知的な女性へ","年齢を問わず使えるニュアンスカラー",{"practical":4,"surprise":4,"looks":5},["female"],["birthday","christmas","mothers-day"],"コスメ")

# ===== 女性アクセ (8) =====
a("ティファニー ラブ バンドリング リング","¥39,600","10k+","世界中で愛されるティファニーのシンプルなバンドリング。","大切な女性・パートナーへ","プロポーズや記念日に最適な定番ジュエリー",{"practical":2,"surprise":5,"looks":5},["female"],["birthday","christmas","valentines","anniversary"],"アクセサリー")
a("4℃ ダイヤモンド ネックレス","¥19,800","10k+","日本女性に人気の4℃のダイヤモンドネックレス。シンプルで上品。","彼女・妻・娘へ","日常使いできるシンプルさが魅力",{"practical":3,"surprise":5,"looks":5},["female"],["birthday","christmas","valentines","anniversary"],"アクセサリー")
a("agete シルバー リング","¥14,300","10k+","繊細なデザインが人気のageteのシルバーリング。","センスのある女性・アクセサリー好きへ","日常使いできる上品さが◎",{"practical":3,"surprise":4,"looks":5},["female"],["birthday","christmas","valentines"],"アクセサリー")
a("スワロフスキー クリスタル ピアス","¥6,600","5k10k","スワロフスキーのクリスタルピアス。華やかで上品な輝き。","輝きが好きな女性全般へ","コスパよく高級感を演出",{"practical":3,"surprise":4,"looks":5},["female"],["birthday","christmas","valentines"],"アクセサリー")
a("ete ゴールド チャーム ブレスレット","¥12,100","10k+","人気ブランドeteのチャームブレスレット。重ね付けにも◎。","トレンドに敏感な女性へ","さりげないおしゃれを楽しめる",{"practical":3,"surprise":4,"looks":5},["female"],["birthday","valentines","christmas"],"アクセサリー")
a("Canal4℃ パール ネックレス","¥8,800","5k10k","清楚なパールのネックレス。フォーマルにもカジュアルにも合う。","上品さを大切にする女性へ","年齢問わず使えるパールの定番",{"practical":3,"surprise":3,"looks":5},["female"],["birthday","christmas","graduation","mothers-day"],"アクセサリー")
a("AHKAH ダイヤモンド ピアス","¥16,500","10k+","繊細なダイヤモンドピアス。つけるだけで洗練された印象に。","上質なものが好きな女性へ","特別な日のプレゼントに最適",{"practical":3,"surprise":5,"looks":5},["female"],["birthday","christmas","valentines","anniversary"],"アクセサリー")
a("ヴァンドーム青山 シルバー バングル","¥9,900","5k10k","シンプルなシルバーバングル。どんなコーデにも合わせやすい。","ミニマリスト・シンプル好きな女性へ","使いやすいシンプルデザイン",{"practical":4,"surprise":3,"looks":5},["female"],["birthday","christmas","valentines"],"アクセサリー")

# ===== 女性スイーツ (12) =====
a("ゴディバ ゴールドコレクション 15粒","¥4,320","3k5k","ベルギー王室御用達。厳選されたプラリネ15粒の豪華ボックス。","チョコレート好きな女性全般へ","高級感があり見た目も美しい定番ギフト",{"practical":4,"surprise":3,"looks":5},["female","parents"],["birthday","christmas","valentines","thanks","mothers-day"],"スイーツ")
a("ピエールエルメ マカロン ギフトボックス","¥3,780","3k5k","パリの人気パティシエのマカロン。繊細な味わいと美しい色合い。","スイーツ好きのおしゃれ女性へ","インスタ映えする美しさ",{"practical":3,"surprise":5,"looks":5},["female"],["birthday","christmas","valentines","mothers-day"],"スイーツ")
a("千疋屋 フルーツゼリー詰め合わせ","¥5,940","5k10k","老舗果物店の贅沢フルーツゼリー。果肉たっぷりで上品な甘さ。","フルーツ好きな方・年配の方へ","日本の老舗ブランドの安心感",{"practical":4,"surprise":3,"looks":4},["female","parents"],["mothers-day","thanks","birthday","mid-year","year-end"],"スイーツ")
a("ヨックモック シガール","¥3,240","3k5k","サクサクのバター風味が人気のシガール。東京土産の定番。","幅広い年代の女性へ","万人受けする定番スイーツ",{"practical":4,"surprise":2,"looks":3},["female","parents"],["thanks","birthday","christmas","mothers-day"],"スイーツ")
a("バウムクーヘン ギフトセット","¥4,500","3k5k","しっとりふわふわのバウムクーヘン。個包装で配りやすい。","職場・グループへの贈り物にも","日持ちするので送りやすい定番ギフト",{"practical":5,"surprise":2,"looks":3},["female","parents"],["thanks","birthday","christmas","mid-year","year-end"],"スイーツ")
a("ダロワイヨ マカロン ギフト","¥3,456","3k5k","パリの老舗パティスリーのマカロン詰め合わせ。","おしゃれな女性・スイーツ通へ","フランス菓子ならではの上品さ",{"practical":3,"surprise":4,"looks":5},["female"],["birthday","valentines","christmas"],"スイーツ")
a("キハチ スイーツ ギフトセット","¥4,104","3k5k","洋菓子の名店キハチの人気菓子詰め合わせ。","幅広い年代の方へ","種類豊富で選ぶ楽しみも",{"practical":4,"surprise":3,"looks":4},["female","parents"],["birthday","thanks","mothers-day"],"スイーツ")
a("モロゾフ クッキー詰め合わせ","¥2,916","1k3k","神戸の老舗モロゾフの人気クッキー。サクサクの食感と上品な味。","幅広い年代に人気","缶のデザインがかわいく再利用できる",{"practical":4,"surprise":2,"looks":4},["female","parents"],["birthday","thanks","christmas","mothers-day"],"スイーツ")
a("ユーハイム バウム ギフトセット","¥3,888","3k5k","バウムクーヘン発祥の老舗ユーハイムのギフト。","年代問わず愛される","日持ちするのでいつでも贈りやすい",{"practical":5,"surprise":2,"looks":3},["female","parents"],["birthday","thanks","mid-year","year-end","mothers-day"],"スイーツ")
a("アンリ・シャルパンティエ フィナンシェ","¥4,320","3k5k","バターの香り豊かなフィナンシェ。しっとり濃厚な味わい。","お菓子好きの女性へ","高級感あるパッケージで贈り物に最適",{"practical":4,"surprise":3,"looks":4},["female","parents"],["birthday","christmas","mothers-day","thanks"],"スイーツ")
a("リンツ リンドール チョコレート","¥3,240","3k5k","スイスの高級チョコレート。なめらかな口溶けが人気。","チョコレート好きな方へ","カラフルなボールが見た目も可愛い",{"practical":4,"surprise":3,"looks":5},["female","parents"],["valentines","christmas","birthday","thanks"],"スイーツ")
a("堂島ロール ロールケーキ","¥2,700","1k3k","大阪土産の定番。ふわふわのスポンジとミルククリームが絶品。","スイーツ好き全般へ","要冷蔵なので直接渡す際に◎",{"practical":4,"surprise":3,"looks":4},["female","parents"],["birthday","thanks","mothers-day"],"スイーツ")

# ===== 女性フラワー (5) =====
a("プリザーブドフラワー アレンジメント ボックス","¥6,000","5k10k","枯れない花をおしゃれにアレンジ。長期間飾れる。","花が好きな女性・インテリアにこだわる方へ","お手入れ不要で場所を選ばない",{"practical":3,"surprise":5,"looks":5},["female","parents"],["mothers-day","birthday","anniversary","christmas"],"フラワー")
a("ハーバリウム ボトル ギフト","¥4,000","3k5k","植物をオイルに漬け込んだインテリア雑貨。幻想的な見た目。","インテリア好き・おしゃれな女性へ","飾るだけでお部屋が華やぐ",{"practical":2,"surprise":5,"looks":5},["female"],["birthday","christmas","mothers-day"],"フラワー")
a("生花 アレンジメント フラワーギフト","¥5,000","3k5k","プロが作る季節の花のアレンジメント。そのまま飾れる。","花が好きな女性全般へ","贈られた瞬間の感動が大きい",{"practical":2,"surprise":5,"looks":5},["female","parents"],["mothers-day","birthday","anniversary","thanks"],"フラワー")
a("ドライフラワー リース","¥4,500","3k5k","ナチュラルなドライフラワーのリース。玄関やリビングに映える。","ナチュラルインテリア好きな女性へ","長く楽しめるサスティナブルなギフト",{"practical":3,"surprise":4,"looks":5},["female"],["birthday","christmas","mothers-day"],"フラワー")
a("ソープフラワー ギフトボックス","¥3,500","3k5k","石鹸でできた花のアレンジ。見た目は本物そっくりで長持ち。","枯れない花を贈りたい方へ","香りも楽しめるおしゃれなギフト",{"practical":2,"surprise":5,"looks":5},["female","parents"],["mothers-day","birthday","anniversary"],"フラワー")

# ===== 女性バッグ (5) =====
a("ケイトスペード トートバッグ","¥28,600","10k+","ニューヨーク発の人気ブランド。機能的でおしゃれなトートバッグ。","働く女性・アクティブな女性へ","実用的かつブランド感があり喜ばれる",{"practical":5,"surprise":4,"looks":5},["female"],["birthday","christmas","anniversary"],"バッグ")
a("コーチ シグネチャー ショルダーバッグ","¥33,000","10k+","アメリカの老舗レザーブランド。耐久性とデザイン性を兼備。","ファッション好きな女性へ","長く使えるブランドバッグ",{"practical":5,"surprise":4,"looks":5},["female"],["birthday","christmas","anniversary","graduation"],"バッグ")
a("フルラ ポップ ミニバッグ","¥27,500","10k+","イタリアのフルラのカラフルなミニバッグ。コンパクトで使いやすい。","おしゃれ好きな女性へ","鮮やかなカラーが気分を上げる",{"practical":4,"surprise":5,"looks":5},["female"],["birthday","christmas","valentines"],"バッグ")
a("マイケルコース クロスボディバッグ","¥22,000","10k+","人気ブランドの使いやすいクロスボディバッグ。","幅広い年代の女性へ","おしゃれと機能性を両立",{"practical":5,"surprise":3,"looks":5},["female"],["birthday","christmas"],"バッグ")
a("ロンシャン プリアージュ トートバッグ","¥18,700","10k+","フランスのロンシャンの折りたたみトートバッグ。軽くて使いやすい。","旅行好き・アクティブな女性へ","軽量で普段使いに最適",{"practical":5,"surprise":3,"looks":4},["female"],["birthday","christmas","mothers-day"],"バッグ")

# ===== 女性リラクゼーション (6) =====
a("ロクシタン バスソルト セット","¥4,400","3k5k","南フランスのハーブを使ったバスソルト。癒しのバスタイムに。","バスタイムを大切にする女性へ","香りと保湿効果でリラックスできる",{"practical":5,"surprise":3,"looks":4},["female","parents"],["birthday","christmas","mothers-day","thanks"],"リラクゼーション")
a("ディプティック アロマキャンドル","¥8,800","5k10k","パリの人気ブランドのアロマキャンドル。上品な香りが部屋を包む。","インテリアや香りにこだわる女性へ","プレゼントとしての格が高いキャンドル",{"practical":3,"surprise":5,"looks":5},["female"],["birthday","christmas","valentines"],"リラクゼーション")
a("ヴェレダ アルニカ マッサージオイル","¥2,860","1k3k","スイスの自然派ブランド。疲れた体をほぐすマッサージオイル。","忙しく働く女性・スポーツする女性へ","天然成分で肌にも優しい",{"practical":5,"surprise":3,"looks":3},["female","parents"],["birthday","mothers-day","thanks"],"リラクゼーション")
a("バスボム ギフトセット","¥3,000","1k3k","入浴剤のバスボムセット。カラフルで見た目もかわいい。","お風呂好きな女性全般へ","手軽に特別なバスタイムを演出",{"practical":4,"surprise":4,"looks":5},["female"],["birthday","christmas","valentines","mothers-day"],"リラクゼーション")
a("ジョーマローン ルームスプレー","¥9,350","5k10k","英国の人気ブランドのルームフレグランス。上品な香りで空間を彩る。","インテリアにこだわる女性へ","香りのプレゼントは記憶に残る",{"practical":3,"surprise":5,"looks":5},["female"],["birthday","christmas","valentines"],"リラクゼーション")
a("バスクリン 薬用入浴剤 ギフトセット","¥3,240","1k3k","日本の老舗ブランドの入浴剤セット。様々な香りが楽しめる。","幅広い年代の女性・親御さんへ","日常的に使える実用的なギフト",{"practical":5,"surprise":2,"looks":3},["female","parents"],["mothers-day","thanks","birthday","mid-year","year-end"],"リラクゼーション")

# ===== 女性体験 (4) =====
a("エステ ギフト券 スパトリートメント","¥10,000","10k+","有名エステサロンのトリートメントギフト券。非日常の体験を贈る。","頑張っている女性・自分へのご褒美に","体験型ギフトは特別な思い出になる",{"practical":3,"surprise":5,"looks":3},["female"],["birthday","mothers-day","anniversary","christmas"],"体験")
a("スパ＆温泉 ギフト券","¥15,000","10k+","高級温泉旅館・スパ施設のギフト券。心身のリフレッシュに。","疲れている方・ご夫婦へ","日頃の疲れを癒す最高のプレゼント",{"practical":4,"surprise":5,"looks":3},["female","parents"],["birthday","mothers-day","anniversary"],"体験")
a("アフタヌーンティー ペアチケット","¥8,000","5k10k","高級ホテルのアフタヌーンティーペアチケット。優雅なひとときを。","お茶好きな女性・特別な記念日に","一緒に楽しめる思い出になるギフト",{"practical":3,"surprise":5,"looks":4},["female","parents"],["birthday","mothers-day","anniversary","valentines"],"体験")
a("ヨガ体験レッスン ギフト券","¥6,000","5k10k","人気ヨガスタジオの体験レッスンギフト券。健康的なライフスタイルを応援。","健康志向の女性・初心者でも安心","心とカラダのバランスを整える体験",{"practical":4,"surprise":4,"looks":3},["female"],["birthday","christmas","mothers-day"],"体験")

# ===== 女性ファッション (5) =====
a("エルメス カシミヤストール","¥66,000","10k+","最高級カシミヤのストール。肌触り抜群で上品な印象に。","特別な女性・記念日の贈り物に","一生使える高品質ストール",{"practical":5,"surprise":5,"looks":5},["female"],["birthday","christmas","anniversary"],"ファッション")
a("シルクスカーフ ブランドギフト","¥12,100","10k+","100%シルクのスカーフ。様々な巻き方で楽しめる。","おしゃれが好きな女性へ","コーデのアクセントになる万能アイテム",{"practical":4,"surprise":4,"looks":5},["female","parents"],["birthday","christmas","mothers-day"],"ファッション")
a("UVカット 帽子 レディース","¥5,500","3k5k","紫外線対策に最適なおしゃれな帽子。折りたたみ可能で持ち運び楽。","アウトドア好き・日焼けが気になる女性へ","実用的で喜ばれるファッションアイテム",{"practical":5,"surprise":2,"looks":4},["female","parents"],["birthday","mothers-day","christmas"],"ファッション")
a("シルク ルームウェア ギフトセット","¥8,800","5k10k","肌触りの良いシルクのルームウェア。上質な時間を過ごせる。","自分の時間を大切にする女性へ","着た瞬間の気持ちよさが伝わる",{"practical":5,"surprise":4,"looks":4},["female"],["birthday","christmas","mothers-day"],"ファッション")
a("レディース パジャマ 上質コットン","¥6,600","5k10k","肌触り抜群のコットンパジャマ。睡眠の質を上げる贈り物。","睡眠を大切にする女性へ","毎日使うものだから実用性も高い",{"practical":5,"surprise":3,"looks":4},["female","parents"],["birthday","christmas","mothers-day"],"ファッション")

# ===== 男性お酒 (10) =====
a("ザ・プレミアム・モルツ ビールギフト","¥3,888","3k5k","サントリーの高級ビール。すっきりした飲み口と豊かなコク。","ビール好きな男性へ","缶のデザインも高級感があり贈り物向き",{"practical":5,"surprise":2,"looks":3},["male","parents"],["fathers-day","birthday","thanks","mid-year","year-end","christmas"],"お酒")
a("獺祭 純米大吟醸 45","¥2,200","1k3k","山口県の人気地酒。フルーティーで飲みやすい大吟醸。","日本酒好きな男性・お父さんへ","知名度が高く確実に喜ばれる",{"practical":4,"surprise":3,"looks":4},["male","parents"],["fathers-day","birthday","thanks","mid-year","year-end"],"お酒")
a("久保田 千寿 純米吟醸","¥1,870","1k3k","新潟の老舗酒蔵の人気銘柄。すっきりとした辛口の日本酒。","日本酒が好きな年配の方へ","辛口好きに外れなしの一本",{"practical":4,"surprise":3,"looks":3},["male","parents"],["fathers-day","birthday","mid-year","year-end","thanks"],"お酒")
a("山崎 シングルモルト ウイスキー","¥8,000","5k10k","サントリーの国産ウイスキー。世界的評価の高い逸品。","ウイスキー好きな男性へ","大人の男性へのプレミアムギフト",{"practical":4,"surprise":5,"looks":4},["male"],["birthday","christmas","fathers-day","thanks"],"お酒")
a("響 ブレンデッドウイスキー","¥12,000","10k+","日本のウイスキー文化を代表する逸品。繊細で複雑な味わい。","ウイスキー通・上司へ","日本が誇るウイスキーの最高峰",{"practical":4,"surprise":5,"looks":5},["male"],["birthday","christmas","fathers-day","thanks"],"お酒")
a("バランタイン 17年 スコッチウイスキー","¥7,000","5k10k","世界的に人気のスコッチウイスキー。まろやかで飲みやすい。","洋酒好きな男性へ","コスパが良く喜ばれる洋酒ギフト",{"practical":4,"surprise":4,"looks":4},["male"],["birthday","christmas","fathers-day"],"お酒")
a("クラフトビール 飲み比べセット","¥5,000","3k5k","国内外の個性豊かなクラフトビール詰め合わせ。","ビール好き・新しい味を試したい方へ","飲み比べが楽しい体験型ギフト",{"practical":4,"surprise":5,"looks":4},["male","parents"],["fathers-day","birthday","christmas","thanks"],"お酒")
a("ボルドー ワイン ギフトセット","¥6,000","5k10k","フランス・ボルドーの厳選赤ワインセット。","ワイン好きなカップル・夫婦へ","食事とともに楽しめるギフト",{"practical":4,"surprise":4,"looks":4},["male","female"],["anniversary","birthday","christmas","thanks"],"お酒")
a("モエ・エ・シャンドン ブリュット","¥6,600","5k10k","世界で最も有名なシャンパン。お祝いの席を華やかに。","お祝い事全般に","泡が上がる瞬間の特別感が◎",{"practical":3,"surprise":5,"looks":5},["male","female","parents"],["birthday","anniversary","christmas","graduation","wedding"],"お酒")
a("ジャック ダニエル テネシー ウイスキー","¥2,970","1k3k","アメリカの定番ウイスキー。甘くてまろやかな飲み口。","ウイスキー入門者・普段飲みに","知名度が高く気軽に贈れる",{"practical":4,"surprise":2,"looks":3},["male"],["birthday","christmas","fathers-day"],"お酒")

# ===== 男性グルメ (10) =====
a("松阪牛 すき焼き用 ギフト","¥19,800","10k+","日本三大和牛の一つ。霜降りが美しいA5ランクの松阪牛。","肉好きな男性・特別なお礼に","最高級の牛肉で感謝を伝える",{"practical":5,"surprise":5,"looks":4},["male","parents"],["fathers-day","birthday","thanks","mid-year","year-end"],"グルメ")
a("うなぎ 国産 蒲焼き ギフト","¥8,000","5k10k","国産うなぎの蒲焼きセット。ふっくらした身と香ばしいタレが絶品。","うなぎが好きな方・年配の方へ","土用の丑以外でも喜ばれる逸品",{"practical":5,"surprise":4,"looks":3},["male","parents"],["fathers-day","birthday","mid-year","year-end","thanks"],"グルメ")
a("ズワイガニ 姿 冷凍 ギフト","¥12,000","10k+","ふんわりとした身がたっぷりのズワイガニ。豪快に食べる喜びを。","海鮮好きな方・豪華な贈り物に","食卓が一気に豪華になる",{"practical":5,"surprise":5,"looks":4},["male","parents"],["birthday","mid-year","year-end","fathers-day","thanks"],"グルメ")
a("神戸牛 ステーキ ギフトセット","¥22,000","10k+","世界に誇る神戸牛のステーキ用セット。","肉好きな男性・記念日の贈り物に","高級レストランの味を自宅で",{"practical":5,"surprise":5,"looks":4},["male","parents"],["birthday","fathers-day","anniversary","thanks"],"グルメ")
a("カレー 高級 レトルト ギフトセット","¥4,500","3k5k","有名シェフ監修の高級レトルトカレー詰め合わせ。","カレー好きな男性へ","本格的な味を手軽に楽しめる",{"practical":4,"surprise":3,"looks":3},["male","parents"],["birthday","fathers-day","thanks","mid-year"],"グルメ")
a("燻製 ギフトセット","¥5,500","3k5k","職人が作る本格燻製セット。チーズ・ナッツ・肉など詰め合わせ。","お酒好き・グルメな男性へ","おつまみにぴったりな大人のギフト",{"practical":4,"surprise":4,"looks":4},["male"],["birthday","christmas","fathers-day","thanks"],"グルメ")
a("ジャーキー ギフトボックス","¥3,500","3k5k","国産・輸入の高級ジャーキー詰め合わせ。","肉好き・おつまみ好きな男性へ","おつまみにぴったりのギフト",{"practical":4,"surprise":3,"looks":3},["male"],["birthday","christmas","fathers-day","thanks"],"グルメ")
a("佐賀牛 しゃぶしゃぶ用 ギフト","¥13,200","10k+","九州が誇る佐賀牛のしゃぶしゃぶセット。","肉好きな家族・グループへ","家族で楽しめる豪華ギフト",{"practical":5,"surprise":4,"looks":4},["male","parents"],["birthday","fathers-day","anniversary","thanks"],"グルメ")
a("ローストビーフ ギフトセット","¥6,600","5k10k","本格的なローストビーフのギフト。パーティーやお祝いにも。","肉好きな方・ホームパーティーに","食卓が華やかになる豪華グルメ",{"practical":4,"surprise":4,"looks":4},["male","female","parents"],["birthday","christmas","anniversary","thanks"],"グルメ")
a("高級ハム ギフトセット","¥5,400","3k5k","国産豚使用の高級ハムセット。やわらかくジューシーな味わい。","幅広い年代の方へ","定番中の定番お歳暮ギフト",{"practical":5,"surprise":2,"looks":3},["male","parents"],["mid-year","year-end","thanks","fathers-day","birthday"],"グルメ")

# ===== 男性ファッション (8) =====
a("ポーター タンカー ウォレット","¥22,000","10k+","日本が誇る吉田カバンのポーターの人気財布。","ビジネスマン・こだわりのある男性へ","Made in Japanの高品質が伝わる",{"practical":5,"surprise":4,"looks":4},["male"],["birthday","fathers-day","christmas","graduation"],"ファッション")
a("タケオキクチ レザー 名刺入れ","¥8,800","5k10k","日本のブランドTAKEO KIKUCHIのスマートな名刺入れ。","社会人・ビジネスマンへ","社会人になった息子・後輩への贈り物に",{"practical":5,"surprise":3,"looks":4},["male"],["birthday","graduation","fathers-day","christmas"],"ファッション")
a("ポールスミス マルチストライプ 財布","¥25,300","10k+","英国ブランドのカラフルなストライプが特徴の財布。","おしゃれに敏感な男性へ","使うたびに気分が上がるユニークデザイン",{"practical":5,"surprise":4,"looks":5},["male"],["birthday","christmas","graduation"],"ファッション")
a("バーバリー マフラー チェック柄","¥44,000","10k+","英国の老舗ブランドのシグネチャーチェックマフラー。","上品な男性・格式のある贈り物に","一生もののブランドマフラー",{"practical":5,"surprise":5,"looks":5},["male"],["birthday","christmas","anniversary"],"ファッション")
a("カルバンクライン ボクサーパンツ ギフトセット","¥5,500","3k5k","人気ブランドのボクサーパンツ3枚セット。","パートナー・夫へのカジュアルギフト","毎日使う実用的なプレゼント",{"practical":5,"surprise":2,"looks":3},["male"],["birthday","christmas","fathers-day"],"ファッション")
a("ダンヒル カードケース","¥16,500","10k+","英国の紳士ブランドのスマートなカードケース。","ビジネスマン・重役の方へ","シンプルで格調高いギフト",{"practical":5,"surprise":3,"looks":4},["male"],["birthday","fathers-day","christmas","thanks"],"ファッション")
a("本革 ベルト メンズ ギフト","¥9,900","5k10k","イタリアンレザーを使用した高級ベルト。","ビジネスマン・スーツを着る男性へ","毎日使える実用的な高級品",{"practical":5,"surprise":3,"looks":4},["male"],["birthday","fathers-day","christmas","graduation"],"ファッション")
a("ラルフローレン ポロシャツ","¥11,000","10k+","アメリカの定番ブランドの上質なポロシャツ。","アクティブなシニア・ゴルフ好きへ","長く着られるクラシックなデザイン",{"practical":5,"surprise":3,"looks":4},["male","parents"],["fathers-day","birthday","christmas"],"ファッション")

# ===== 男性ガジェット (7) =====
a("AirPods Pro 第2世代","¥39,800","10k+","Appleの最新完全ワイヤレスイヤホン。アクティブノイズキャンセリング搭載。","スマホユーザー・音楽好きな方へ","持っていない人へのサプライズに最適",{"practical":5,"surprise":5,"looks":5},["male","female"],["birthday","christmas","graduation","anniversary"],"ガジェット")
a("Anker PowerCore 大容量 モバイルバッテリー","¥4,999","3k5k","世界で人気のAnkerのモバイルバッテリー。大容量で安心。","スマホをよく使う方へ","実用的すぎて確実に喜ばれる",{"practical":5,"surprise":2,"looks":3},["male","female"],["birthday","christmas","graduation","fathers-day"],"ガジェット")
a("ワイヤレス充電器 Qi対応","¥3,500","1k3k","置くだけで充電できるワイヤレスチャージャー。","スマホ好きな男性へ","デスク周りがすっきりする便利グッズ",{"practical":5,"surprise":3,"looks":3},["male","female"],["birthday","christmas","fathers-day"],"ガジェット")
a("Garmin スマートウォッチ","¥44,000","10k+","高性能GPSスマートウォッチ。ランニング・アウトドアに最適。","スポーツ好き・アウトドア好きな男性へ","健康管理も楽しくなるウェアラブル",{"practical":5,"surprise":5,"looks":4},["male"],["birthday","christmas","fathers-day"],"ガジェット")
a("ソニー ノイズキャンセリングヘッドホン WH-1000XM5","¥49,500","10k+","世界トップクラスのノイズキャンセリング性能。","音楽好き・テレワーク中の方へ","集中力を高める最高の相棒",{"practical":5,"surprise":5,"looks":4},["male","female"],["birthday","christmas","graduation"],"ガジェット")
a("iPad mini 第6世代","¥78,800","10k+","Appleのコンパクトタブレット。電子書籍・動画・仕事に使える。","デジタル好き・読書家へ","一台あると生活が変わる万能ガジェット",{"practical":5,"surprise":5,"looks":5},["male","female"],["birthday","christmas","graduation"],"ガジェット")
a("Amazon Echo Dot 第5世代","¥5,980","3k5k","スマートスピーカーの定番。音声操作で生活が便利に。","スマートホームに興味がある方へ","ちょっとした贈り物に最適なガジェット",{"practical":4,"surprise":4,"looks":3},["male","female","parents"],["birthday","christmas","fathers-day"],"ガジェット")

# ===== 男性趣味 (7) =====
a("タイトリスト プロV1 ゴルフボール","¥7,200","5k10k","プロも愛用するゴルフボールの最高峰。","ゴルフ好きな男性・上司へ","ゴルファーへの鉄板ギフト",{"practical":5,"surprise":3,"looks":3},["male"],["birthday","fathers-day","christmas","thanks"],"趣味")
a("ダイワ 釣り竿 入門セット","¥12,000","10k+","国産釣り具ブランドダイワの入門セット。","釣り好きな男性へ","趣味を応援する気持ちが伝わる",{"practical":5,"surprise":4,"looks":3},["male"],["birthday","fathers-day","christmas"],"趣味")
a("コールマン ツーリングドームテント","¥29,800","10k+","定番アウトドアブランドのキャンプテント。","キャンプ好きな方・アウトドア派へ","キャンプの楽しさが広がるギフト",{"practical":5,"surprise":5,"looks":4},["male"],["birthday","fathers-day","christmas"],"趣味")
a("デロンギ コーヒーミル カッティングセット","¥8,800","5k10k","イタリアのデロンギ製コーヒーミル。豆から挽いた本格的なコーヒーを。","コーヒー好きな男性へ","毎朝のコーヒータイムが特別になる",{"practical":5,"surprise":4,"looks":4},["male","female"],["birthday","christmas","fathers-day"],"趣味")
a("アシックス ランニングシューズ ゲルカヤノ","¥17,600","10k+","日本が誇るアシックスの高性能ランニングシューズ。","ランニングが趣味の男性へ","毎日走りたくなる相棒シューズ",{"practical":5,"surprise":3,"looks":4},["male"],["birthday","christmas","fathers-day"],"趣味")
a("ヨネックス バドミントンラケット","¥9,900","5k10k","日本のスポーツブランドヨネックスの人気ラケット。","バドミントン・テニス好きな方へ","スポーツの楽しさを応援するギフト",{"practical":5,"surprise":3,"looks":3},["male"],["birthday","fathers-day","christmas"],"趣味")
a("サウナハット & サウナグッズセット","¥5,500","3k5k","サウナブームに乗ったサウナグッズセット。","サウナ好き・健康意識の高い男性へ","ととのう体験をサポートするギフト",{"practical":5,"surprise":4,"looks":4},["male"],["birthday","fathers-day","christmas","thanks"],"趣味")

# ===== 子供おもちゃ (8) =====
a("レゴ クラシック 黄色のアイデアボックス スペシャル","¥7,678","5k10k","何でも作れるレゴのクラシックセット。創造力を育む。","3歳〜12歳の子供へ","何時間でも遊べる知育おもちゃの定番",{"practical":4,"surprise":4,"looks":4},["kids"],["birthday","christmas","baby-shower"],"おもちゃ")
a("プラレール 新幹線 はやぶさセット","¥6,600","5k10k","人気の新幹線おもちゃ。線路をつないでコースを作れる。","電車好きの男の子（2〜8歳）へ","子供の目が輝く定番おもちゃ",{"practical":3,"surprise":5,"looks":4},["kids"],["birthday","christmas"],"おもちゃ")
a("シルバニアファミリー はじめてのシルバニア","¥4,500","3k5k","かわいい小さな動物たちのリアルなミニチュアセット。","女の子（3〜10歳）へ","女の子が絶対喜ぶ定番おもちゃ",{"practical":3,"surprise":5,"looks":5},["kids"],["birthday","christmas"],"おもちゃ")
a("木製 ままごとキッチン","¥15,800","10k+","おしゃれな木製ままごとキッチンセット。","2〜6歳の女の子へ","知育効果もあるおしゃれなおもちゃ",{"practical":4,"surprise":5,"looks":5},["kids"],["birthday","christmas","baby-shower"],"おもちゃ")
a("トミカ 人気車種 5台セット","¥3,500","1k3k","子供に大人気のトミカのミニカー詰め合わせ。","2〜8歳の男の子へ","集めるほど楽しいミニカー",{"practical":3,"surprise":4,"looks":3},["kids"],["birthday","christmas"],"おもちゃ")
a("磁気ブロック マグネットタイル","¥5,500","3k5k","磁石でくっつく知育ブロック。3D造形が楽しい。","3〜10歳の子供へ","創造力と空間認識力を育む",{"practical":4,"surprise":4,"looks":4},["kids"],["birthday","christmas"],"おもちゃ")
a("キネティックサンド 砂遊びセット","¥3,300","1k3k","室内で楽しめる不思議な砂。べとつかず片付け簡単。","3〜8歳の子供へ","雨の日でも楽しめる室内砂遊び",{"practical":4,"surprise":5,"looks":4},["kids"],["birthday","christmas"],"おもちゃ")
a("カタン ボードゲーム","¥5,500","3k5k","世界的人気のボードゲーム。家族みんなで楽しめる。","8歳以上の子供〜大人まで","家族時間が豊かになるボードゲーム",{"practical":4,"surprise":4,"looks":3},["kids","parents"],["birthday","christmas"],"おもちゃ")

# ===== 子供知育 (7) =====
a("学研 よくわかる図鑑 科学ボックスセット","¥9,900","5k10k","子供の「なぜ？」に答える科学系図鑑セット。","好奇心旺盛な子供（6〜12歳）へ","本物の興味を引き出す良質な図鑑",{"practical":5,"surprise":3,"looks":3},["kids"],["birthday","christmas"],"知育")
a("くもん 思考力パズル","¥1,980","1k3k","KUMONの人気知育パズル。論理的思考力を養う。","3〜10歳の子供へ","脳の発達に良い知育玩具",{"practical":5,"surprise":3,"looks":3},["kids"],["birthday","christmas"],"知育")
a("スクラッチ プログラミング 入門キット","¥5,500","3k5k","子供向けプログラミング入門セット。楽しみながら学べる。","8〜12歳の子供へ","未来のスキルを楽しく学べる",{"practical":5,"surprise":4,"looks":3},["kids"],["birthday","christmas"],"知育")
a("地球儀 知育 おもちゃ 子供用","¥7,700","5k10k","子供が楽しく学べるインタラクティブ地球儀。","5〜12歳の子供へ","世界への興味を育む知育グッズ",{"practical":5,"surprise":4,"looks":4},["kids"],["birthday","christmas"],"知育")
a("顕微鏡 子供用 科学実験セット","¥5,500","3k5k","本格的な子供用顕微鏡。身近なものを観察できる。","理科好きの子供（8〜14歳）へ","科学者の芽を育てるプレゼント",{"practical":5,"surprise":5,"looks":3},["kids"],["birthday","christmas"],"知育")
a("こどもチャレンジ 英語絵本セット","¥3,960","1k3k","楽しく英語が学べる絵本と教材のセット。","幼児〜小学生へ","英語を遊びながら自然に学べる",{"practical":5,"surprise":3,"looks":4},["kids"],["birthday","christmas"],"知育")
a("モンテッソーリ 木製教具セット","¥8,800","5k10k","モンテッソーリ教育に基づいた木製教具。自主性と集中力を育む。","0〜6歳の幼児へ","世界的に認められた知育メソッド",{"practical":5,"surprise":3,"looks":4},["kids"],["birthday","christmas","baby-shower"],"知育")

# ===== 子供ベビー (8) =====
a("おむつケーキ 豪華3段セット","¥9,800","5k10k","おむつをケーキのように重ねたギフト。実用的で見た目も華やか。","出産祝いに","見た目のインパクトと実用性が両立",{"practical":5,"surprise":5,"looks":5},["kids"],["baby-shower"],"ベビー")
a("ミキハウス ベビー ロンパース","¥6,600","5k10k","日本の子供服ブランドミキハウスの上質なロンパース。","0〜1歳の赤ちゃんへ","ブランド力で確実に喜ばれる",{"practical":5,"surprise":3,"looks":5},["kids"],["baby-shower","birthday"],"ベビー")
a("ベビー食器セット ギフト","¥5,500","3k5k","離乳食に使える安心素材のベビー食器セット。","離乳食が始まる赤ちゃんへ","成長に合わせて長く使える",{"practical":5,"surprise":3,"looks":4},["kids"],["baby-shower","birthday"],"ベビー")
a("今治タオル ベビー ガーゼケット","¥5,500","3k5k","やわらかい今治タオルのベビー用ガーゼケット。","新生児〜1歳の赤ちゃんへ","肌に優しい日本製の安心品質",{"practical":5,"surprise":3,"looks":4},["kids"],["baby-shower"],"ベビー")
a("スタイ（よだれかけ）セット オーガニック","¥3,300","1k3k","オーガニックコットンのおしゃれなスタイセット。","0〜1歳の赤ちゃんへ","おしゃれで実用的な出産祝い",{"practical":5,"surprise":3,"looks":5},["kids"],["baby-shower"],"ベビー")
a("タカラトミー メリー ベビートイ","¥5,500","3k5k","赤ちゃんの視覚と聴覚を刺激するメリー。","0〜6ヶ月の赤ちゃんへ","赤ちゃんが喜ぶ定番ベビーグッズ",{"practical":4,"surprise":4,"looks":4},["kids"],["baby-shower"],"ベビー")
a("ベビーリング 出産祝い ギフト","¥8,800","5k10k","赤ちゃんの誕生を祝うシルバーのベビーリング。","誕生した赤ちゃんへ","一生の記念になる特別なギフト",{"practical":2,"surprise":5,"looks":5},["kids"],["baby-shower"],"ベビー")
a("手形足形 アート ギフトセット","¥4,400","3k5k","赤ちゃんの手形・足形を残せるアートキット。","0〜1歳の赤ちゃんの親御さんへ","成長の記念として一生残せる",{"practical":4,"surprise":5,"looks":5},["kids"],["baby-shower","birthday"],"ベビー")

# ===== 子供ファッション (5) =====
a("ニューバランス 990 キッズスニーカー","¥11,000","10k+","人気ブランドのキッズ用高品質スニーカー。","3〜12歳の子供へ","ブランドものは親御さんも喜ぶ",{"practical":5,"surprise":4,"looks":5},["kids"],["birthday","christmas"],"子供ファッション")
a("ファミリア 子供服 セット","¥8,800","5k10k","日本の子供服ブランドFamiliarの上質な子供服。","0〜6歳の子供へ","質の良い子供服は親御さんに喜ばれる",{"practical":5,"surprise":3,"looks":5},["kids"],["birthday","christmas","baby-shower"],"子供ファッション")
a("キッズ レインコート ポンチョ","¥3,500","1k3k","かわいいデザインのキッズ用レインコート。","幼児〜小学生へ","雨の日が楽しくなるおしゃれなレインコート",{"practical":5,"surprise":3,"looks":5},["kids"],["birthday","christmas"],"子供ファッション")
a("キッズ リュックサック 通学用","¥5,500","3k5k","丈夫で軽いキッズ用リュック。通園・通学に最適。","幼稚園〜小学生へ","毎日使える実用的なプレゼント",{"practical":5,"surprise":3,"looks":4},["kids"],["birthday","christmas","graduation"],"子供ファッション")
a("お名前シール セット 防水","¥1,500","under1k","防水・耐久性があるお名前シール大量セット。","入園・入学の子供へ","地味だけど親御さんが本当に助かる",{"practical":5,"surprise":2,"looks":2},["kids"],["graduation"],"子供ファッション")

# ===== 両親カタログ (4) =====
a("リンベル プレシャスチョイス カタログギフト","¥10,000","10k+","人気のカタログギフト。全国の名産品・体験から選べる。","相手の好みがわからない時に","好きなものを選ぶ楽しみがある",{"practical":5,"surprise":3,"looks":4},["parents"],["mid-year","year-end","birthday","mothers-day","fathers-day","thanks"],"カタログ")
a("ハーモニック グルメカタログ テイスト オブ プレミアム","¥7,000","5k10k","全国の厳選グルメが選べるカタログギフト。","食べることが好きな方へ","外れなしの実用的なカタログギフト",{"practical":5,"surprise":3,"looks":3},["parents"],["mid-year","year-end","birthday","mothers-day","fathers-day","thanks"],"カタログ")
a("ベルメゾン カタログギフト おとどけもの","¥5,000","3k5k","日常使いできる生活用品が豊富なカタログギフト。","実用志向の両親へ","生活の役に立つカタログギフト",{"practical":5,"surprise":2,"looks":3},["parents"],["mid-year","year-end","birthday","thanks"],"カタログ")
a("ANA セレクション カタログギフト","¥15,000","10k+","ANAのカタログギフト。旅行・グルメ・体験まで幅広い。","旅行好きな両親へ","旅行の夢が広がるプレミアムカタログ",{"practical":5,"surprise":4,"looks":4},["parents"],["birthday","anniversary","mothers-day","fathers-day"],"カタログ")

# ===== 両親旅行 (3) =====
a("JTB 国内旅行ギフト券","¥30,000","10k+","大手旅行会社JTBの旅行ギフト券。全国どこでも使える。","旅行好きな両親・カップルへ","行きたい場所に自由に使えるギフト",{"practical":5,"surprise":4,"looks":3},["parents"],["birthday","anniversary","mothers-day","fathers-day"],"旅行")
a("全国 温泉旅館 ギフト券","¥20,000","10k+","全国の人気温泉旅館で使えるギフト券。","温泉好きな方・ゆっくりしたい方へ","日頃の疲れを癒す最高のプレゼント",{"practical":5,"surprise":5,"looks":3},["parents"],["birthday","anniversary","mothers-day","fathers-day","thanks"],"旅行")
a("じゃらん ギフトカード","¥10,000","10k+","人気旅行サイトじゃらんのギフトカード。宿の選択肢が豊富。","旅行好きな方へ","いつでも使える便利な旅行ギフト",{"practical":5,"surprise":3,"looks":3},["parents"],["birthday","mothers-day","fathers-day"],"旅行")

# ===== 両親食品 (8) =====
a("新潟 コシヒカリ 特選米 5kg","¥4,500","3k5k","日本を代表するブランド米。ふっくら甘いコシヒカリ。","米好きな年配の方へ","毎日食べるものだから喜ばれる",{"practical":5,"surprise":2,"looks":3},["parents"],["mid-year","year-end","thanks","birthday","mothers-day","fathers-day"],"食品")
a("北海道産 ズワイガニ ギフト","¥13,000","10k+","北海道直送の新鮮なズワイガニ。","海鮮好きな両親へ","豪華な食卓を演出する贈り物",{"practical":5,"surprise":5,"looks":4},["parents"],["mid-year","year-end","birthday","mothers-day","fathers-day"],"食品")
a("近江牛 すき焼き用 ギフト","¥15,000","10k+","滋賀が誇る近江牛のすき焼きセット。","肉好きな両親・記念日に","日本三大和牛の贅沢な味わい",{"practical":5,"surprise":5,"looks":4},["parents"],["birthday","anniversary","mothers-day","fathers-day","thanks"],"食品")
a("贈答用 フルーツセット 旬の厳選品","¥8,000","5k10k","旬の果物を厳選した贈答用フルーツセット。","果物好きな方・年配の方へ","見た目も美しい贈り物",{"practical":5,"surprise":4,"looks":5},["parents"],["mid-year","year-end","birthday","mothers-day","fathers-day","thanks"],"食品")
a("伊勢海老 ギフトセット","¥18,000","10k+","高級食材の伊勢海老。お祝いの席を豪華に彩る。","特別なお祝いの贈り物に","縁起のいい贈り物",{"practical":4,"surprise":5,"looks":5},["parents"],["birthday","anniversary","mothers-day","fathers-day"],"食品")
a("辛子明太子 高級 ギフト","¥5,400","3k5k","博多の名産・上質な辛子明太子のギフト。","幅広い年代に","ご飯のお供に最高の贈り物",{"practical":5,"surprise":3,"looks":3},["parents"],["mid-year","year-end","thanks","birthday"],"食品")
a("高級お茶漬け セット","¥4,500","3k5k","京都の老舗の高級お茶漬けセット。","年配の方・お茶漬け好きへ","シンプルだけど確かに美味しい",{"practical":4,"surprise":3,"looks":3},["parents"],["mid-year","year-end","thanks","birthday"],"食品")
a("静岡産 最高級緑茶 深蒸し茶","¥3,500","1k3k","静岡の名産・コクのある深蒸し緑茶。","お茶好きな年配の方へ","毎日飲むお茶だから喜ばれる",{"practical":5,"surprise":2,"looks":3},["parents"],["mid-year","year-end","thanks","birthday","mothers-day","fathers-day"],"食品")

# ===== 両親健康 (6) =====
a("ファーレスト マッサージクッション","¥8,800","5k10k","首・肩・腰に使えるマッサージクッション。","体の疲れが気になる年配の方へ","毎日気軽にマッサージが楽しめる",{"practical":5,"surprise":4,"looks":3},["parents"],["birthday","mothers-day","fathers-day","christmas","thanks"],"健康")
a("オムロン 電子血圧計 上腕式","¥7,700","5k10k","信頼のオムロンの上腕式血圧計。健康管理に欠かせない。","健康が気になる年配の方へ","毎日使える健康管理ギフト",{"practical":5,"surprise":3,"looks":3},["parents"],["birthday","mothers-day","fathers-day","thanks"],"健康")
a("国産 黒豆茶 健康茶セット","¥3,600","1k3k","健康に良い黒豆茶のギフトセット。","健康志向の年配の方へ","毎日飲める美味しい健康茶",{"practical":5,"surprise":2,"looks":3},["parents"],["mid-year","year-end","birthday","thanks","mothers-day","fathers-day"],"健康")
a("ネイチャーメイド サプリメント ギフトセット","¥4,400","3k5k","人気サプリブランドのギフトセット。健康をサポート。","健康意識が高い方へ","長く使える健康サポートギフト",{"practical":5,"surprise":2,"looks":3},["parents"],["birthday","mothers-day","fathers-day","thanks"],"健康")
a("フットマッサージャー 足裏マッサージ機","¥9,900","5k10k","足裏を刺激するフットマッサージャー。疲れた足をほぐす。","立ち仕事・足の疲れが気になる方へ","帰宅後の至福のリラックスタイム",{"practical":5,"surprise":4,"looks":3},["parents"],["birthday","mothers-day","fathers-day","christmas","thanks"],"健康")
a("テンピュール 枕 ネックピロー","¥12,100","10k+","高反発で睡眠の質を上げるテンピュールの枕。","快眠を求める年配の方へ","毎晩の睡眠が変わる体感できるギフト",{"practical":5,"surprise":4,"looks":3},["parents"],["birthday","mothers-day","fathers-day","christmas"],"健康")

# ===== 両親ペア (5) =====
a("波佐見焼 ペアマグカップ","¥5,500","3k5k","長崎の伝統工芸・波佐見焼のペアマグカップ。","夫婦・カップルへ","毎日使えるおしゃれなペアグッズ",{"practical":5,"surprise":3,"looks":5},["parents"],["anniversary","birthday","mothers-day","fathers-day"],"ペア")
a("今治タオル ペアパジャマ","¥9,900","5k10k","吸湿性抜群の今治タオル素材のペアパジャマ。","夫婦・カップルへ","一緒に使えるほっこりペアギフト",{"practical":5,"surprise":3,"looks":4},["parents"],["anniversary","birthday","christmas"],"ペア")
a("バカラ ペアグラス","¥22,000","10k+","フランスの高級クリスタルブランドのペアグラス。","特別な夫婦・記念日に","特別な夜を演出するプレミアムペアグラス",{"practical":4,"surprise":5,"looks":5},["parents"],["anniversary","birthday","wedding"],"ペア")
a("箸 ペアセット 職人手作り","¥8,800","5k10k","職人が一本一本手作りしたペアの箸。","和食が好きな夫婦・両親へ","日本の職人技が光る贈り物",{"practical":5,"surprise":4,"looks":5},["parents"],["anniversary","birthday","mothers-day","fathers-day"],"ペア")
a("有田焼 ペア湯呑み","¥4,400","3k5k","有田焼の伝統的なペア湯呑みセット。","お茶が好きな両親・夫婦へ","毎日お茶の時間が楽しくなる",{"practical":5,"surprise":3,"looks":5},["parents"],["anniversary","birthday","mothers-day","fathers-day"],"ペア")

# ===== 上司・目上菓子 (10) =====
a("とらや 羊羹 詰め合わせ","¥5,400","3k5k","室町時代から続く老舗とらやの羊羹。","格式を重んじる上司・目上の方へ","日本の和菓子文化の最高峰",{"practical":4,"surprise":3,"looks":4},["boss"],["thanks","mid-year","year-end","birthday"],"菓子")
a("虎屋 和菓子 詰め合わせ","¥6,480","5k10k","伝統ある虎屋の季節の和菓子詰め合わせ。","和菓子が好きな上司へ","老舗ブランドの安心感と品格",{"practical":4,"surprise":3,"looks":4},["boss"],["thanks","mid-year","year-end","birthday"],"菓子")
a("千疋屋 フルーツゼリー 高級セット","¥8,640","5k10k","高級フルーツ店千疋屋の贅沢ゼリーセット。","フルーツが好きな上司へ","上品な甘さで喜ばれる",{"practical":4,"surprise":4,"looks":5},["boss"],["thanks","birthday","mid-year","year-end"],"菓子")
a("帝国ホテル クッキー缶","¥5,184","3k5k","帝国ホテルの上質なクッキー缶。贈り物に最適。","上品なものが好きな方へ","ホテルブランドの格調が伝わる",{"practical":4,"surprise":3,"looks":5},["boss"],["thanks","birthday","mid-year","year-end"],"菓子")
a("クルミッ子 鎌倉紅谷","¥3,780","1k3k","鎌倉の人気菓子クルミッ子。バターとクルミの絶妙な味わい。","お菓子好きな方へ","地方銘菓の希少感で喜ばれる",{"practical":4,"surprise":4,"looks":4},["boss"],["thanks","birthday","mid-year","year-end"],"菓子")
a("東京ばな奈 ギフトセット","¥2,916","1k3k","東京土産の定番。ふわふわのバナナクリームがたまらない。","幅広い年代に人気の定番","万人受けする親しみやすい菓子",{"practical":4,"surprise":2,"looks":3},["boss"],["thanks","birthday","mid-year","year-end"],"菓子")
a("六花亭 バターサンド 詰め合わせ","¥3,240","1k3k","北海道の名菓六花亭のバターサンド詰め合わせ。","北海道土産・バター菓子好きへ","濃厚なバタークリームが絶品",{"practical":4,"surprise":3,"looks":4},["boss"],["thanks","birthday","mid-year","year-end"],"菓子")
a("シュガーバターの木 ギフトボックス","¥3,240","1k3k","サクサクの食感が人気のシュガーバター系焼き菓子。","洋菓子好きな方へ","軽い食感で食べやすい人気菓子",{"practical":4,"surprise":3,"looks":4},["boss"],["thanks","birthday","mid-year","year-end"],"菓子")
a("ガレー チョコレート アソートメント","¥5,400","3k5k","高品質なチョコレートの詰め合わせ。上品な甘さ。","チョコレート好きな方へ","上品なパッケージで贈り物向き",{"practical":4,"surprise":3,"looks":5},["boss"],["thanks","birthday","christmas"],"菓子")
a("ラデュレ マカロン ギフト","¥4,860","3k5k","パリの老舗ラデュレのマカロン。上品で華やか。","おしゃれな女性上司・お世話になった方へ","フランス菓子の格調高さが伝わる",{"practical":3,"surprise":5,"looks":5},["boss"],["thanks","birthday","christmas"],"菓子")

# ===== 上司飲料 (6) =====
a("スターバックス コーヒー ギフトカード","¥5,000","3k5k","スタバのギフトカード。好きな飲み物を選べる。","コーヒー好きな方・幅広い年代に","外れなしの定番コーヒーギフト",{"practical":5,"surprise":2,"looks":3},["boss"],["thanks","birthday","christmas"],"飲料")
a("ネスプレッソ カプセルコーヒー ギフト","¥5,500","3k5k","自宅でカフェの味が楽しめるネスプレッソカプセル詰め合わせ。","コーヒー好きな方へ","様々な種類が楽しめるコーヒーギフト",{"practical":5,"surprise":3,"looks":4},["boss"],["birthday","christmas","thanks"],"飲料")
a("TWG ティー コレクション","¥6,600","5k10k","シンガポール発の高級紅茶ブランドTWGのギフト。","紅茶好きな方・女性上司へ","パッケージも美しい高級感あふれる紅茶",{"practical":4,"surprise":4,"looks":5},["boss"],["birthday","christmas","thanks"],"飲料")
a("ルピシア 紅茶 緑茶 詰め合わせ","¥4,320","3k5k","世界のお茶が楽しめるルピシアのギフトセット。","お茶好きな方へ","種類豊富で選ぶ楽しみがある",{"practical":4,"surprise":3,"looks":4},["boss","parents"],["birthday","christmas","thanks","mid-year","year-end"],"飲料")
a("八女茶 高級 煎茶 ギフト","¥4,000","3k5k","福岡八女産の最高級煎茶。深い味わいと豊かな香り。","日本茶が好きな年配の方へ","本物の日本茶の美味しさを贈る",{"practical":5,"surprise":3,"looks":4},["boss","parents"],["mid-year","year-end","birthday","thanks"],"飲料")
a("伊藤園 お茶ギフト セット","¥3,240","1k3k","老舗ブランド伊藤園の高品質日本茶詰め合わせ。","幅広い年代に人気の定番","手頃な価格で確実に喜ばれる",{"practical":5,"surprise":2,"looks":3},["boss","parents"],["mid-year","year-end","thanks","birthday"],"飲料")

# ===== 上司文具 (5) =====
a("パーカー ボールペン IM プレミアム","¥7,700","5k10k","英国の老舗筆記具ブランドパーカーの高級ボールペン。","ビジネスマン・上司へ","格調高い筆記具は長く使われる",{"practical":5,"surprise":4,"looks":5},["boss"],["birthday","thanks","graduation"],"文具")
a("モンブラン ボールペン マイスターシュテュック","¥49,500","10k+","筆記具の最高峰モンブランのボールペン。","特別な上司・重役の方へ","最高のビジネスギフト",{"practical":5,"surprise":5,"looks":5},["boss"],["birthday","thanks","retirement"],"文具")
a("伊東屋 レザー ノートカバー","¥8,800","5k10k","銀座の老舗文具店伊東屋の本革ノートカバー。","ビジネスマン・手帳好きへ","上質な革の風合いが長く楽しめる",{"practical":5,"surprise":4,"looks":5},["boss"],["birthday","thanks","graduation"],"文具")
a("ペリカン スーベレーン 万年筆","¥38,500","10k+","ドイツの名門ペリカンの高級万年筆。","万年筆好き・文字を大切にする方へ","書く喜びを伝える究極のギフト",{"practical":4,"surprise":5,"looks":5},["boss"],["birthday","thanks","retirement"],"文具")
a("ロルバーン ノート デラックス セット","¥2,200","1k3k","人気のロルバーンノートとペンのセット。","ビジネスマン・学生へ","シンプルながら使いやすい定番文具",{"practical":5,"surprise":2,"looks":4},["boss"],["birthday","thanks","graduation"],"文具")

# ===== 上司タオル (4) =====
a("今治タオル 高級 フェイスタオル セット","¥5,500","3k5k","日本が誇る今治タオルの高級フェイスタオルセット。","幅広い年代・目上の方へ","毎日使えて品質が伝わる定番ギフト",{"practical":5,"surprise":2,"looks":4},["boss","parents"],["thanks","mid-year","year-end","birthday","mothers-day","fathers-day"],"タオル")
a("Hipopotamus ヒポポタマス バスタオル","¥8,800","5k10k","エジプトコットン使用の高級バスタオル。","質にこだわる方へ","使った瞬間の質の高さが伝わる",{"practical":5,"surprise":3,"looks":4},["boss","parents"],["birthday","thanks","mid-year","year-end"],"タオル")
a("フェイラー タオルハンカチ ギフトセット","¥4,400","3k5k","ドイツのブランドフェイラーの人気タオルハンカチ。","女性・目上の方へ","かわいいデザインと高品質が両立",{"practical":5,"surprise":3,"looks":5},["boss","parents","female"],["birthday","thanks","mothers-day","mid-year","year-end"],"タオル")
a("白鷹 越中ふんどし・和タオル ギフト","¥3,300","1k3k","日本の伝統的な和タオルのギフトセット。","和のものが好きな方・年配の方へ","日本の伝統工芸品の贈り物",{"practical":4,"surprise":3,"looks":4},["boss","parents"],["thanks","mid-year","year-end","birthday"],"タオル")

# ===== 追加商品 (20) =====
# 女性追加
a("ケアプロスト まつ毛美容液","¥3,300","1k3k","まつ毛を長く美しく育てる人気の美容液。","まつ毛が気になる女性へ","継続使用で効果実感",{"practical":5,"surprise":3,"looks":3},["female"],["birthday","mothers-day","christmas"],"コスメ")
a("ドクターシーラボ VC100 エッセンスローション","¥6,050","5k10k","ビタミンCを高配合した美容化粧水。毛穴や美白ケアに。","スキンケアに力を入れている女性へ","効果を実感しやすい医師監修コスメ",{"practical":5,"surprise":3,"looks":4},["female"],["birthday","mothers-day","christmas"],"コスメ")
a("ホワイトニング 歯磨きセット","¥3,500","1k3k","歯科医院でも使われる高品質ホワイトニングセット。","美しい歯を保ちたい方へ","実用的だけど喜ばれる美容ギフト",{"practical":5,"surprise":2,"looks":3},["female","male"],["birthday","christmas"],"コスメ")

# 男性追加
a("キャプテンスタッグ BBQセット","¥8,800","5k10k","アウトドア料理が楽しめるBBQセット。","アウトドア好き・家族が多い方へ","夏のアウトドアが盛り上がる",{"practical":5,"surprise":4,"looks":3},["male"],["fathers-day","birthday","christmas"],"趣味")
a("デロンギ エスプレッソメーカー","¥24,200","10k+","本格エスプレッソが自宅で楽しめるデロンギのマシン。","コーヒー好きな男性へ","カフェ気分を毎日味わえる",{"practical":5,"surprise":5,"looks":5},["male","female"],["birthday","christmas","fathers-day"],"趣味")
a("バルミューダ トースター","¥33,000","10k+","料理を美味しくするバルミューダのスチームトースター。","料理好き・パン好きな方へ","一度使ったら戻れない感動的なトースト",{"practical":5,"surprise":5,"looks":5},["male","female","parents"],["birthday","christmas","anniversary","wedding"],"ガジェット")
a("ニトリル グローブ 作業手袋","¥2,200","1k3k","頑丈で使いやすい作業手袋セット。","DIY・アウトドア好きな男性へ","実用的で確実に使われる",{"practical":5,"surprise":1,"looks":2},["male"],["fathers-day","birthday","thanks"],"趣味")
a("アディダス ランニングソックス 5足セット","¥3,300","1k3k","スポーツ用の高品質ランニングソックス。","ランニング・スポーツ好きな男性へ","地味に嬉しい実用的ギフト",{"practical":5,"surprise":2,"looks":2},["male"],["birthday","fathers-day","christmas"],"ファッション")

# 子供追加
a("スイッチライト 任天堂","¥22,980","10k+","子供に大人気のポータブルゲーム機。","8歳以上のゲーム好きな子供へ","今どきの子供への最高プレゼント",{"practical":4,"surprise":5,"looks":5},["kids"],["birthday","christmas"],"おもちゃ")
a("ポケモンカード スターターセット","¥1,760","under1k","世界中で人気のポケモンカードゲーム入門セット。","6〜15歳のポケモン好きな子供へ","友達と一緒に楽しめるカードゲーム",{"practical":3,"surprise":5,"looks":4},["kids"],["birthday","christmas"],"おもちゃ")
a("アンパンマン よくばりボックス","¥4,400","3k5k","アンパンマンの知育玩具がたくさん詰まったボックス。","1〜3歳の幼児へ","幼児の発達を促す定番おもちゃ",{"practical":4,"surprise":4,"looks":4},["kids"],["birthday","christmas","baby-shower"],"おもちゃ")

# 両親追加
a("高野豆腐 精進料理 セット","¥3,800","1k3k","健康的な精進料理食材のギフトセット。","健康志向の年配の方へ","体に優しい和の食材セット",{"practical":5,"surprise":3,"looks":3},["parents"],["mid-year","year-end","birthday","thanks"],"食品")
a("南部鉄器 急須 ギフト","¥8,800","5k10k","岩手の伝統工芸・南部鉄器の急須。一生使える日本の名品。","お茶好きな両親・年配の方へ","使うほど味が出る日本の宝",{"practical":5,"surprise":4,"looks":5},["parents"],["birthday","mothers-day","fathers-day","anniversary"],"ペア")
a("北海道 乳製品 詰め合わせ","¥5,500","3k5k","北海道産バター・チーズ・ヨーグルトの詰め合わせ。","乳製品が好きな方へ","北海道の豊かな大地の恵み",{"practical":5,"surprise":3,"looks":3},["parents"],["mid-year","year-end","birthday","thanks"],"食品")

# 上司追加
a("ネクタイ 高級 シルク ブランド","¥12,100","10k+","イタリア製シルクの高級ネクタイ。","スーツを着る男性上司へ","毎日使えるプレミアムアイテム",{"practical":5,"surprise":3,"looks":5},["boss"],["birthday","thanks","fathers-day"],"ファッション")
a("ゴディバ チョコレート ギフト 缶","¥6,480","5k10k","ゴディバの高級チョコレートが入った特別な缶。","甘いものが好きな上司へ","見た目も豪華なプレミアムチョコ",{"practical":4,"surprise":4,"looks":5},["boss"],["birthday","christmas","thanks","valentines"],"菓子")
a("一保堂 抹茶 煎茶 ギフトセット","¥5,400","3k5k","京都の老舗茶舗・一保堂の高級茶詰め合わせ。","お茶好きな上司・目上の方へ","京都の老舗が誇る本物のお茶",{"practical":4,"surprise":4,"looks":5},["boss"],["thanks","mid-year","year-end","birthday"],"飲料")
a("マリアージュ フレール 紅茶 缶","¥4,860","3k5k","パリの高級紅茶ブランドのシグネチャー缶入り紅茶。","紅茶好きな女性上司へ","フランスの高級紅茶で特別感を演出",{"practical":4,"surprise":5,"looks":5},["boss"],["birthday","christmas","thanks"],"飲料")
a("手ぬぐい 注染 高級 ギフトセット","¥3,300","1k3k","職人が染めた本格注染の手ぬぐいセット。","和のものが好きな上司・年配の方へ","日本の伝統工芸品の粋な贈り物",{"practical":4,"surprise":3,"looks":5},["boss","parents"],["thanks","mid-year","year-end","birthday"],"タオル")
a("フルーツギフト 初夏の彩り セット","¥12,000","10k+","旬の初夏フルーツ・マンゴー・さくらんぼの贈答セット。","高級フルーツが好きな上司へ","季節を感じる贅沢なフルーツギフト",{"practical":5,"surprise":5,"looks":5},["boss","parents"],["mid-year","birthday","mothers-day","thanks"],"菓子")

with open("gifts.json", "w", encoding="utf-8") as f:
    json.dump(gifts, f, ensure_ascii=False, indent=1)
print(f"Generated {len(gifts)} products")
