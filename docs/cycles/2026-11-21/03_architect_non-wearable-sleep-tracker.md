# 03. アーキテクト設計図: non-wearable-sleep-tracker(2026-11-23)

インプット: docs/agents/architect.md、共通ルール(rule of foreign affiliate.md)、02_marketer.md「提案2」、既存トラッカー3記事(oura-vs-whoop / apple-watch-vs-oura / smart-ring-no-subscription)、構成見本 white-noise-machine-for-apartment-noise、src/_data/categories.json(`non-wearable-sleep-tracker` は sleep-tracking-aids に登録済み)、lib/publishing.js

- スラッグ: `non-wearable-sleep-tracker` / カテゴリ: sleep-tracking-aids(front matter は `category: Wearables` でも可。categories.json の posts で解決済み)
- 本文は書かない。以下は設計のみ

---

## 0. 調査で分かった前提(ライターが最初に読むこと)

1. **Withings の公式サイト(withings.com・support.withings.com)はページ本体の取得が 403 で読めなかった。** Withings の仕様は「公式ページの検索結果抜粋」で確認したもの。数値・文言は公開前に人間が公式ページで目視確認すること(下の「人間確認」一覧)。
2. **米国で売られている Withings の一般向けモデルの名前は「Withings Sleep」(米国外は「Sleep Analyzer」)。** 米国版は公式サポートで「医療機器ではない」と明記され、測るのは「breathing disturbances(呼吸の乱れ)」。**睡眠時無呼吸の検出機能は米国版には無い**(EU 等の Sleep Analyzer にある機能)。
3. **FDA 510(k) クリアランスを受けているのは別製品「Withings Sleep Rx」(K231667、2024-09-06、閉塞性睡眠時無呼吸の診断補助)。** 米国では医療機関向けで、一般の小売品ではない。記事では「市販の Withings Sleep とは別物」と書き分ける。市販品に FDA の話を結びつけない。
4. **Google Nest Hub (2nd gen) は Google Store(米国)で全4色「Out of stock」(2026-11-23 時点、ページのソースで確認)。** 販売終了の告知は見当たらないが、Sleep Sensing は今も「preview(追加料金なし)」扱いで、データ表示先の Google Fit は Google Health へ移行中(報道ベース。Google の公式発表で日付は未確認)。→ 推奨に入れるが条件つき(下記)。
5. **Amazon Halo Rise は販売終了・サービス終了**(Amazon 公式 2023-04-26 発表、2023-08-01 以降は動作しない)。記事に入れない。FAQ で「昔の枕元型は?」に短く触れる程度は可。
6. **SleepScore Max** は現行で買えるか公式で確認できなかった(会社は Sleep.ai に移行、公式ページに購入導線なし)。記事に入れない。

---

## 商品候補スコアリング(比較記事の場合)

**採点は暫定。** 「レビュー」は Amazon を開けないため推測で、人間確認後に確定する。「紹介料」は Amazon の価格帯からの相対的な推測。

| 商品 | 種類 | 検索意図 | 紹介料 | レビュー(暫定) | 伝えやすさ | 比較軸 | 合計 |
|---|---|---|---|---|---|---|---|
| Withings Sleep(米国版、ベッド下パッド) | ベッド下 | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Google Nest Hub (2nd gen) + Sleep Sensing | 枕元・レーダー | 2 | 1 | 2 | 2 | 2 | **9/10**(在庫条件つき) |
| Sleepal AI Lamp | 枕元・レーダー(ランプ型) | 2 | 2 | 0 | 2 | 2 | **8/10** |
| Eight Sleep Pod | マットレスカバー型(温度調整が主) | 1 | 2 | 1 | 1 | 1 | 6/10 |
| Emfit QS | ベッド下 | 1 | 2 | 0 | 1 | 1 | 5/10 |
| Sleepme Sleep Tracker | ベッド下 | 1 | 1 | 0 | 1 | 1 | 4/10 |
| Sleep Number スマートベッド | ベッドそのもの | 0 | 2 | 1 | 0 | 1 | 4/10 |
| Garmin Index Sleep Monitor | 上腕バンド(身に着ける) | 0 | 1 | 1 | 1 | 1 | 4/10 |
| SleepScore Max | 枕元 | — | — | — | — | — | 対象外(現行販売を確認できず) |
| Amazon Halo Rise | 枕元 | — | — | — | — | — | 対象外(販売・サービス終了) |

採点の理由(要点):
- Withings: 「着けない」「ベッド下に敷くだけ」に直結。核の機能はサブスク不要。レビュー数は不明なので暫定1。
- Nest Hub: 枕元に置くだけ・カメラなし・budget。長く売られており Amazon のレビューは厚い可能性が高い(推測)。ただし公式ストア在庫切れと preview 扱いがリスク。
- Sleepal: 2026年発売の新製品(CES 2026)。基本機能は無料。Amazon での扱い・レビューは判断材料なし → 0。
- Eight Sleep: 着けずに測れるが本題は温度調整。公式ヘルプで Autopilot(有料)が最初の12か月必須、トラッキングも有料機能側。
- Emfit: 公式でアプリは Web のみの記載、直販中心、HRV 重視の上級者向け。
- Sleepme: トラッカーが会員プランとセット(公式)、アプリは iPhone のみ(App Store 表記)。

### 採用(7点以上の上位3件)
1. **Withings Sleep** — 「ベッド下パッド型」の代表
2. **Google Nest Hub (2nd gen) Sleep Sensing** — 「枕元・budget」枠。**条件:** 人間確認で Amazon(または Google Store)に新品の在庫が無ければ Also Looked At に下げ、推奨は2点(Withings / Sleepal)で構成する。7点以上の代替が無いため、無理に3点目を足さない
3. **Sleepal AI Lamp** — 「枕元・premium・ライト兼用」枠。**条件:** Amazon で取り扱いが無ければ、CTA は Amazon 検索リンクを置かず、公式サイトへの言及のみ(アフィリエイトなし)にするか、Also Looked At に下げるかを人間が判断

Also Looked At(短く1〜2文ずつ): Eight Sleep Pod / Emfit QS / Sleepme Sleep Tracker / Sleep Number / Garmin Index Sleep Monitor(「指輪・腕は嫌だが腕に巻くのは平気な人向けの別解。ただし身に着ける」)

---

## 公式で確認できた仕様(出典つき)

### Withings Sleep(米国版)
| 項目 | 内容 | 出典 |
|---|---|---|
| 呼び名 | 米国は「Sleep」、米国外は「Sleep Analyzer」 | https://www.withings.com/en-us/products/sleep(検索抜粋) |
| 置き方 | マットレスの下(またはマットレスとトッパーの間)。違和感があればマットレスとベッドフレームの間へ | https://support.withings.com/hc/en-us/articles/4411156111761-Sleep-U-S-Bed-and-Mattress-Compatibility(検索抜粋) |
| ベッドの制約 | スプリング・ラテックス・フォーム・メモリーフォームに対応。厚さ 4〜15インチで試験。**ウォーターベッド・エアベッドは非推奨**。振動するマットレスは非推奨。すのこ状フレームは平らな板(段ボール等)を挟む場合あり | 同上 |
| 何人 | 1枚で1人。2人なら2枚(1人1枚) | 同上 |
| 電源 | 電池なし。付属アダプタでコンセントにつなぎっぱなし | Withings 製品ページ/製品ガイド(検索抜粋) https://media.withings.com/kits/guides/2023/sleep-analyzer/AW_PRODUCT_GUIDE_WSM02_INT_A.pdf(※国際版ガイド) |
| 通信 | Wi-Fi と Bluetooth(BLE)。設定に Wi-Fi が必要 | 同上/US Compatibility(検索抜粋) |
| 対応OS | iOS 16 以降 / Android 12.0 以降 | https://support.withings.com/hc/en-us/articles/4411183431313-Sleep-U-S-Compatibility(検索抜粋) |
| 測るもの | 睡眠の段階・Sleep Score(100点満点)・睡眠中の心拍・いびき(回数と時間)・breathing disturbances | Sleep (U.S.) の各サポート記事(検索抜粋) https://support.withings.com/hc/en-us/articles/4411186106641-Sleep-U-S-What-is-the-Sleep-Score / https://support.withings.com/hc/en-us/articles/4411186310801-Sleep-U-S-Tracking-my-snoring |
| breathing disturbances の条件 | 5時間以上の睡眠と、音センサーをオンにすることが必要 | https://support.withings.com/hc/en-us/articles/360018780534-Sleep-U-S-Tracking-my-breathing-disturbances(検索抜粋) |
| 医療機器か | 米国版は「医療機器ではなく、診断・治療・予防に使うものではない」 | https://support.withings.com/hc/en-us/articles/360019269474-Sleep-U-S-Frequently-asked-questions-about-breathing-disturbances(検索抜粋) |
| CPAP | 米国版は CPAP 使用中の動作を未検証 | 同上 |
| サブスク | Withings+ は任意。睡眠の履歴と傾向はサブスクなしで見られる(公式の表現) | 製品ページ(検索抜粋) |
| Apple Health | 睡眠中の心拍は Apple Health に同期しない(サポート記載、検索抜粋) | 人間確認 |
| スマートホーム | IFTTT 連携は古い製品シート・EU 版の記載のみ → **記事では触れない**(米国現行で未確認) | — |

### Google Nest Hub (2nd gen) — Sleep Sensing
| 項目 | 内容 | 出典 |
|---|---|---|
| 仕組み | Motion Sense(低出力レーダー)で動きと呼吸、マイク等で音、部屋の光と温度も | https://support.google.com/googlenest/answer/10357290 / https://store.google.com/us/product/nest_hub_sleep_sensing |
| 測るもの | 就寝・起床時刻、睡眠時間、呼吸数、せき・いびきなどの睡眠の乱れ | 同上 |
| カメラ | 無し(公式 FAQ) | Google Store ページ |
| 人数 | 1人(ディスプレイに一番近い人)。2人なら2台 | 同上 |
| 費用 | 「preview」として追加料金なし。将来 Fitbit / Google Health Premium に組み込む可能性に言及、日付なし | 同上 |
| 必要なもの | Nest Hub (2nd gen) のみ(1st gen・Hub Max は不可)、Google Home アプリ、Google Fit アプリ、個人の Google アカウント(Workspace 不可)。国・言語によっては使えない | support.google.com |
| 置き方 | ベッドの近くに置き、寝る位置に合わせて調整(キャリブレーション) | 同上 |
| 医療 | "not intended to diagnose, cure, mitigate, prevent, or treat any disease or condition" | support.google.com |
| 在庫 | Google Store(米国)で全4色 Out of stock(2026-11-23 確認) | https://store.google.com/us/config/nest_hub_2nd_gen |
| 今後 | Google Fit → Google Health への移行が報道されている(Android Authority 2026-07-31、9to5Google)。Google 公式の日付は未確認 | 報道。記事では「表示アプリが変わる可能性」程度に留める |

### Sleepal AI Lamp
| 項目 | 内容 | 出典 |
|---|---|---|
| 仕組み | レーダーと赤外線(サーマル)センサーで動きと呼吸。カメラなし | https://sleepal.ai/home |
| プライバシー | センサーを回路ごと切るボタンあり | 同上 |
| 通信 | Wi-Fi 2.4GHz/5GHz | 同上 |
| 対応OS | iOS 16.4 以降 / Android 7.0 以降(Android は「APK」表記あり → Google Play での配布かは人間確認) | 同上 |
| サブスク | 「works without a subscription」。上位の AI+ は任意、購入時に1年分付属の表記 | 同上 |
| 機能 | 寝つくまでの時間・睡眠段階・寝姿勢といびき・寝室環境(温湿度・音・光)、ランプの減光・光と音で起こすアラーム、Apple Health / Google Health Connect 連携、Matter で Apple Home / Google Home | 同上 |
| 医療 | 医療機器かどうかの記載を見つけられず → **医療的な言い回しを一切使わない**。公式の精度パーセント表示は自社値なので引用しない | — |
| 電源 | 国別の電源アダプタ同梱(公式 FAQ の検索抜粋)。FAQ 本体は 403 | 人間確認 |
| 販売中のセール表示 | 公式にセール表示あり → **記事では一切触れない**(規約) | — |

### Also Looked At の根拠
- Eight Sleep Pod: Autopilot が最初の12か月必須、未加入だと温度調整の一部のみ(公式ヘルプ/規約の検索抜粋) https://help.eightsleep.com/en_us/can-i-buy-the-pod-without-autopilot-S1BzQo5rn / https://www.eightsleep.com/terms-of-service/
- Emfit QS: 購入に3年分のクラウドサービス込み、以降は年単位で任意更新。Web アプリ、2.4GHz Wi-Fi 必須 https://emfit.com/subscribe-emfit-qs-for-personal-use/
- Sleepme Sleep Tracker: 会員プラン(sleepme+)にトラッカーが含まれる形 https://sleep.me/sleepmeplus-pricing 、アプリは iPhone のみ(App Store)
- Garmin Index Sleep Monitor: 上腕に着けるバンド https://www.garmin.com/en-US/p/1650098/
- Withings Sleep Rx(FDA 510(k) K231667) https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K231667
- Amazon Halo 終了 https://www.aboutamazon.com/news/company-news/amazon-halo-discontinued

**金額は一切書かない(サブスク料金も)。** 「optional paid tier」「included for the first year」「required for the first 12 months」のような表現に留める。

---

## 記事設計: タイトル案

1. **Non-Wearable Sleep Tracker: Under-Mattress Pad or Bedside Sensor?**(65字・推奨)
2. Non-Wearable Sleep Trackers: 3 Picks If You Hate Sleeping in a Ring
3. Non-Wearable Sleep Tracker Guide: Under-Mattress vs. Bedside Picks

- ターゲットキーワード: `non wearable sleep tracker`(主)/ `under mattress sleep tracker`(補助。H2 1か所と本文で自然に使う。タイトルには入れない)
- メタディスクリプション案(約150字):
  "Want sleep data without a ring or watch? We compare non-wearable sleep trackers—an under-mattress pad and two bedside sensors—by bed fit, phone, power, and subscription."
- 想定文字数: 2,200〜2,800語
- 冒頭の開示文: 見本記事と同じ型(アフィリエイト開示+Not medical advice+「メーカー仕様と公開情報に基づく。実際には使っていない」)

---

## 見出し構成(H2/H3)

1. **導入(H2なし、120〜180語)**
   - 悩み: 指輪や腕時計を着けて寝ると気になる/夜中に外してしまう/充電を忘れる。でも睡眠の記録は取りたい
   - 答え方: 「着けない型」は2種類(ベッド下・枕元)。何を置くかはベッドと寝室の状況で決まる、と予告
   - 既存記事への導線: 着けてもよいなら [smart ring without subscription] へ1本だけリンク

2. **H2: What a Non-Wearable Sleep Tracker Can and Can't Tell You**
   - H3: How They Measure Without Touching You — ベッド下は体の動き・心拍・呼吸をマットレス越しに、枕元はレーダーで動きと呼吸を拾う(各社公式の説明の範囲で)
   - H3: What You Give Up Compared With a Ring or Watch — 昼間の活動・外出先の昼寝は測れない/寝ている場所が固定/2人で寝ると影響を受ける。
   - H3: These Are Not Medical Devices — Withings Sleep(米国版)と Nest Hub は公式に「診断用ではない」。数値は傾向を見るもの。**断定しない。**

3. **H2: Under-Mattress Sleep Tracker or Bedside Sensor: Which Fits Your Bed?**(補助KWを含むH2)
   - 判断表(Pinterest 切り出し用・その1): 行=状況、列=Under-mattress pad / Bedside sensor
     - 行例: ウォーターベッド・エアベッド / パートナーと同じベッド / ペットや子どもが一緒に寝る / ベッド脇にコンセントが無い / 枕元の画面・光が気になる / 家の Wi-Fi・スマホの種類 / 旅行先でも測りたい
   - H3: If You Share the Bed — Withings は1人1枚、Nest Hub は一番近い1人、他の人やペットでデータが乱れることがある(公式記載)
   - H3: If You Have an Airbed, Waterbed, or Adjustable Base — Withings はウォーターベッド・エアベッド非推奨。可動式ベッドは公式記載を確認できず → 「メーカーに確認を」とだけ書く
   - H3: If Bedside Light or a Screen Bothers You — Nest Hub は画面、Sleepal はランプ。明るさの具体値は書かない

4. **H2: Non-Wearable Sleep Trackers Compared**(比較表・メイン。Pinterest 切り出し用・その2)
   - 表の列: **Product / Type / Where it goes / What the maker says it tracks / Subscription for core tracking / Phone & app / Power / People per device / Bed or room limits / Price tier / Best for / May not suit**
   - 価格帯(相対): Withings Sleep = mid-range / Nest Hub (2nd gen) = budget / Sleepal AI Lamp = premium
   - 表の直後に CTA ボックス(3商品まとめ)

5. **H2: The 3 Picks**(各 H3 は見本記事と同じ型: 「What it's for」→ 説明 → 「Who it may not suit」箇条書き → CTA)
   - **H3: Withings Sleep — An Under-Mattress Pad You Set Up Once**
     - 置き方・対応マットレス・コンセント常時接続・iOS 16+/Android 12+・1人1枚
     - 測るもの(Sleep Score・心拍・いびき・breathing disturbances)と、その条件(5時間・音センサー)
     - 医療の書き分け(重要): 米国版は医療機器ではない/睡眠時無呼吸の検出は米国版に無い(他地域の Sleep Analyzer の機能)/FDA クリアランスを受けたのは医療機関向けの別製品 Withings Sleep Rx。「市販品で無呼吸がわかる」と読める文を作らない
     - サブスク: Withings+ は任意、履歴と傾向は無料(公式の表現)
     - May not suit: エアベッド・ウォーターベッド/2人とも測りたいが1枚で済ませたい人/コンセントが遠い/旅行で持ち歩きたい/CPAP 使用中(未検証)
   - **H3: Google Nest Hub (2nd gen) — Bedside Radar, No Camera**
     - 冒頭に在庫と状態の注意を1段落: 公式ストアで在庫切れの時期がある/Sleep Sensing は今も preview(追加料金なし)で、将来の有料化に Google が言及/表示アプリが Google Fit から Google Health に変わる途中との報道。「買う前に販売ページで新品・2nd gen・Sleep Sensing 対応を確認」
     - 測るもの・カメラ無し・1人・キャリブレーション・必要なアカウント(個人 Google アカウント、Workspace 不可)
     - 医療: Google の "not intended to diagnose..." を言い換えで
     - May not suit: Google アカウントを使いたくない人/枕元に画面を置きたくない人/2人とも測りたい人/将来の条件変更を避けたい人/1st gen や Hub Max を持っている人(非対応)
   - **H3: Sleepal AI Lamp — A Bedside Lamp That Tracks Sleep**
     - レーダー+赤外線、カメラ無し、物理プライバシーボタン、Wi-Fi 2.4/5GHz、iOS 16.4+/Android 7.0+
     - ランプ・光と音の目覚まし・寝室環境の記録・Matter 連携
     - サブスク: 基本は不要、AI+ は任意(購入時に一定期間付属の公式表記。期間は公開前に再確認)
     - 新製品なので長期の評判が少ない、と率直に書く。公式の精度パーセントは書かない
     - May not suit: Android で Google Play 以外の入手に抵抗がある人(人間確認の結果次第で削除)/枕元に光源を置きたくない人/実績の長い製品を選びたい人/最も安い選択肢を探す人
   - 各 H3 末尾に個別 CTA

6. **H2: Others We Looked At**(各1〜2文)
   - Eight Sleep Pod: 着けずに測れるが主目的は温度調整、最初の12か月は有料プランが必須(公式)。トラッキング目的だけなら過剰 → 内部リンク: couples-different-sleep-temperatures-dual-zone-bed
   - Emfit QS: ベッド下型、HRV 重視。Web アプリ中心・直販中心
   - Sleepme Sleep Tracker: 会員プランとセット、アプリは iPhone のみ
   - Sleep Number: ベッド自体の買い替えになる
   - Garmin Index Sleep Monitor: 上腕に巻くバンド。「指や手首が嫌なだけ」の人の別解だが、身に着けるタイプ
   - 対象外の明記: Amazon Halo Rise(2023年に販売・サービス終了。中古でも動かない)

7. **H2: Before You Buy: A 6-Point Checklist**(チェックボックス形式。切り出し用・その3)
   - ベッドの種類と厚さ/一緒に寝る人・ペット/ベッド脇のコンセント/スマホの OS バージョン/家の Wi-Fi/サブスクなしで何が見られるか(各社の現行条件を確認)

8. **H2: Who a Non-Wearable Sleep Tracker Isn't For**(必須節)
   - 昼間の活動や運動も1台で記録したい人 → 既存のリング/腕時計記事へ
   - 出張・旅行先でも毎晩測りたい人
   - 寝る場所が毎晩変わる人、交代勤務で仮眠場所が違う人
   - 睡眠時無呼吸などが心配で「診断」を求めている人 → 医師へ(家庭用トラッカーは代わりにならない)
   - 数字を見ると不安で眠れなくなる人 → 測らない選択肢もある(weighted blankets 記事へ軽く)

9. **H2: FAQ**(5〜6問)
   - Can an under-mattress sleep tracker detect sleep apnea? → 米国の市販 Withings Sleep は医療機器ではなく、無呼吸の検出機能は無い。別の医療機関向け製品が FDA クリアランスを受けている事実だけ書き、「心配なら医師へ」
   - Do non-wearable sleep trackers work for couples? → 多くは1人用。2台必要/パートナーやペットで乱れる
   - Do I need a subscription? → 3商品の現行条件(金額なし)
   - Are non-wearable trackers as accurate as a ring or watch? → 比較できる公開データが限られる。断定しない。数字より傾向を
   - Does the Nest Hub have a camera? → 無し(公式)
   - What happened to the Amazon Halo Rise? → 2023年に終了

10. **H2: A Note on Health and Accuracy**(医療免責の本体)
    - 「情報提供であり医療アドバイスではない」
    - 大きないびき、寝ている間に呼吸が止まると言われた、日中の強い眠気、数週間続く不眠 → 医師に相談
    - トラッカーの数値で薬や治療を変えない

11. **H2: Which Non-Wearable Sleep Tracker Fits You?**(まとめ・状況別の一行ずつ)+最終 CTA ボックス
    - 末尾にイタリックの免責(見本記事の型)

---

## アフィリエイトリンク配置ポイント

すべて Amazon Associates US の検索リンク(`rel="nofollow sponsored" target="_blank"`)。金額・セール名・値引き・送料無料に触れない。

| 商品 | Amazon 検索リンク |
|---|---|
| Withings Sleep | https://www.amazon.com/s?k=Withings+Sleep+Tracking+Pad+under+mattress&tag=quietrecover-20 |
| Google Nest Hub (2nd gen) | https://www.amazon.com/s?k=Google+Nest+Hub+2nd+Gen&tag=quietrecover-20 |
| Sleepal AI Lamp | https://www.amazon.com/s?k=Sleepal+AI+Lamp&tag=quietrecover-20 (Amazon に無ければ削除) |

置き場所:
1. 比較表の直後: 3商品まとめの CTA ボックス
2. 各 H3(The 3 Picks)の末尾: 個別 CTA
3. まとめ節の後: 最終 CTA ボックス
- Others We Looked At にはリンクを置かない(推奨しない商品への誘導を避ける)
- Withings・Sleepal 直販のアフィリエイト(Impact/Awin 等)は**未登録・未承認なので使わない**。プレースホルダーも置かない

---

## 内部リンク候補(すべて公開済みを確認。記法は `{{ '/posts/xxx/' | url }}`)

| 記事 | 公開状況 | 置く場所 |
|---|---|---|
| smart-ring-no-subscription-oura-alternative | publishAt 2026-11-04(過去) | 導入・Who it isn't for |
| oura-ring-vs-whoop-sleep-tracking | date 2026-07-27(publishAt なし=公開済み) | 「リングと比べて失うもの」 |
| apple-watch-vs-oura-ring-sleep-tracking | date 2026-09-19(公開済み) | 同上/Who it isn't for |
| weighted-blankets-sleep-anxiety | date 2026-07-25(公開済み) | Who it isn't for(数字が不安になる人) |
| sleep-earbuds-vs-earplugs-snoring-partner | publishAt 2026-10-15(過去) | 「If You Share the Bed」(いびきのパートナー) |
| couples-different-sleep-temperatures-dual-zone-bed | publishAt 2026-10-05(過去) | Others We Looked At(Eight Sleep) |
| sunrise-alarm-clocks-wake-up-light-comparison | publishAt 2026-10-07(過去) | Sleepal の光の目覚まし |

使わない: white-noise-machine-for-day-sleepers(publishAt 11-25 で未公開)、quiet-massage-gun-for-apartments・heated-seat-massager-for-back(published: false)

---

## 人間確認(公開前に必須)

1. **Amazon**: 3商品それぞれの取り扱い有無・新品在庫・評価・レビュー数(→スコアの「レビュー」を確定)。特に Nest Hub が **2nd gen の新品**で買えるか、Sleepal が Amazon にあるか
2. **Nest Hub の扱い**: 新品在庫が無ければ Also Looked At へ下げ、推奨2点構成に変更
3. **Withings 公式ページの目視**(取得が 403): 米国での販売継続、iOS 16+/Android 12+、マットレス 4〜15インチ、Withings+ の「履歴と傾向は無料」の文言、心拍が Apple Health に同期しない件
4. **Withings の EU 終了サポート一覧(2026-04-23版)に「Sleep Trackers」という分類名がある**。旧製品(Aura 等)を指すと思われるが、現行 Sleep / Sleep Analyzer が含まれないことを確認
5. **Sleepal**: Android アプリが Google Play にあるか(公式に「APK」表記)、AI+ の付属期間、電源アダプタ、医療機器扱いでないこと
6. **Google**: Sleep Sensing の preview が継続中か、Google Fit → Google Health 移行の公式発表の有無
7. 合格基準の採点は暫定。上記確認後にアーキテクトまたはディレクターが確定する
