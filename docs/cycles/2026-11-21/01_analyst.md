# 01. アナリスト所見(2026-11-23)

インプット: docs/metrics/digest.md(11/23 朝に再生成済み)、gsc_queries.json・gsc_pages.json・gsc_index.json(Search Console 10/23〜11/20)、ga4_clicks.json(10/24〜11/23)、src/posts/*.md の本文 grep。前回比較は docs/cycles/2026-11-14.md「01. アナリスト所見」。
注意: Search Console は28日の移動期間で、前回(10/14〜11/11)と約3週間重なっている。週ごとの差は独立した変化ではない。

## データの状態
- 投稿台帳 199件(199投稿)/ Xメトリクス 808件・61投稿(最終取得 2026-11-23 05:12)/ ピンメトリクス 3898件・143投稿(同 05:12)/ GA4 `affiliate_click` あり / Search Console 31(2026-11-20 まで)
- ⚠ digest の注記: 「リンククリック(GA4)が取れていない間は、計測済み件数が目安に達しても型の優劣は結論しない」「表示100回未満の記事どうしの比較は『データ不足』」「サイトへの流入(セッション)とリンククリックは流入元を問わずGA4由来のため、現時点では比較できない」
- ⚠ digest の記事単位ファネル表は、GA4 データがあるのにリンククリック欄が「0」と「未取得」が混在している(前回からの持ち越し)。セッション列も無い
- GA4(ga4_clicks.json そのまま): セッション合計31(うち20はトップページへの直接訪問)、affiliate_click 0。記事ページの最大は couples-different-sleep-temperatures-dual-zone-bed の4セッション(直接3・Google 1)
- 検索: 表示515・クリック1(28日)。検索語の内訳が分かるのは515回のうち358回分(140語)。掲載 29/35記事
- X の自動投稿は停止中(X の新しい数字は今後増えない前提)
- 月初の確定報酬の突き合わせ: 今回は月初の回ではないため対象外。10月分の Amazon 確定報酬レポートは、今回確認した範囲(website フォルダと1つ上の階層)では見当たらなかった

## 比較の判定
- ピン・X投稿の型の比較: データ不足。thread_root n=15/20。thread_reply は37/20で件数は足りるが、リンククリックが投稿単位で取れていないため保留。Pinterest は143ピンで表示64・サイトへの遷移1(デザイン別の件数は目安未満)。従来方針を維持
- 記事の比較: データ不足(記事ページのセッション最大 n=4/100)。従来方針を維持
- 検索の比較: データ不足(記事単位で表示100以上は white-noise-machines-vs-sound-machines-light-sleepers の115だけ。検索語単位では最大21/100)。以下(a)(b)(c)は優劣の判断ではなく、マーケターへの観測材料として渡す

## 今週のサマリー
データ不足のため該当なし(affiliate_click が全記事0、セッションも全記事100未満)

## ファネル診断
- サイト全体: affiliate_click 0・記事ページのセッション合計11。詰まっている段階は「そもそも記事に人が来ていない」(表示→クリック)。検索の表示515に対しクリック1(クリック率0.19%)。記事ごとの「読まれるがリンクに進まない」の診断は、来訪が少なすぎて診断不可
- Pinterest: 143ピンで表示64・遷移1。「インプレッションが少ない」段階で止まっている(配信の段階)。型・デザインの優劣はデータ不足
- 個別記事のファネル診断は、記事のセッションがすべて100未満のため書かない

## マーケター向け: 次の記事候補への示唆(検索)

### 先に共有したい事実: 表示の多くは関係の薄い「◯◯ vs white noise machine」型の検索語
- white-noise-machines-vs-sound-machines-light-sleepers の内訳が分かる表示112回のうち、約99回(44語)は「wok vs white noise machine」「chainsaw vs …」「dac vs …」「lazy susan vs …」のように、白色雑音機と無関係な物との比較語(どれも表示1〜6回、順位1〜20位)
- red-light-therapy-vs-massage-gun(表示21回分)も「massage gun vs ring light」「laser pointer vs massage gun」「chandelier vs massage gun」など同じ形が大半
- 推測: 実在の購入検討者による検索とは考えにくい(自動生成された問い合わせの可能性)。この記事の「平均10.5位・表示115」は、狙っている検索語での強さを示していない。本来狙う語の実績は `best white noise machine for light sleepers` 1回・11位、`how to choose the right white-noise or sound-sleep machine …` 2回・10位、`white noise machine vs fan` 1回・60位、`how to choose a noise machine` 1回・100位だけ

### (a) すでに表示されている検索語のうち、既存記事が十分に答えていないもの(新記事の種。すべて表示100回未満=データ不足)
| 検索語 | 表示 | 平均順位 | 表示された記事 | 本文 grep の結果(事実) |
|---|---:|---:|---|---|
| do i need orion intelligence if i already have an oura or whoop? | 14 | 8.2 | oura-ring-vs-whoop-sleep-tracking | 「Orion」は全記事で0件。Orion Intelligence が何の製品かは未確認(推測で書かないこと。まず実在と内容の確認が必要) |
| back massagers for corporate headquarters / best back massagers for employee benefits / best back massagers for employee wellness / back massager chairs for train stations | 13 / 4 / 4 / 4 | 26.4 / 68.2 / 13.5 / 34.2 | shiatsu-back-massager-office-chair-desk-workers | 「employee」は全記事で0件。会社・福利厚生として買う向けの内容は無い。推測: 個人の購入検討とは意図が違う可能性があり、上の「vs」型と同様に不自然な語の可能性もある |
| best mattress pad for dual heating and cooling | 6 | 25.3 | best-bedding-couples-different-temperatures-hot-sleeper | 表示された記事は「暑がり側だけ冷やす」内容で、温め・冷やしの両用は扱っていない。couples-different-sleep-temperatures-dual-zone-bed は両方向の選択肢として BedJet 3(送風)と温めるだけのパッドを扱うが、「1枚で温冷両用・左右別のマットレスパッド」そのものの比較は無い |
| best heating pad for couples | 2 | 5 | best-bedding-couples-different-temperatures-hot-sleeper(冷やす記事) | 答えは couples-different-sleep-temperatures-dual-zone-bed の「Dual-Control Heated Mattress Pads」節にあるが、Google は別の記事を出している(前回の申し送り4「取り合い」と同じ問題) |
| how can i use a heated seat massager to relieve back tension effectively? | 4 | 37.8 | shiatsu-back-massager-office-chair-desk-workers | 「heated seat」を扱うのは下書きのまま見送った heated-seat-massager-for-back だけ(公開記事には無い) |
| intimacy pillow for menopause | 7 | 58.6 | best-cooling-pillow-for-menopause-night-sweats | 「intimacy」は0件。冷感枕とは別の意図(推測)。サイトの方針に合うかは編集長判断 |
| sunrise alarm vs regular alarm | 2 | 84.5 | sunrise-alarm-clocks-wake-up-light-comparison | 本文は携帯アラームの不快さに触れるが、普通の目覚ましとの比較を見出しで扱っていない(前回から持ち越し) |
| sleep bar alternative | 1 | 47 | トップページ | 「Sleep Bar」は0件(何の製品かは未確認) |

### (b) 「伸ばす候補」(平均8〜30位)の記事と同じテーマの周辺
- shiatsu-back-massager-office-chair-desk-workers(27.5位・表示93): 記事の主題どおりの語が上位に近い。`what back massage cushion works well on an office chair?` 13回・9.5位(+「in 2026」付き1回・9位)、`seated back massager` 4回・18.2位。一方 `back massagers for first responders` 15回・28.3位はこの記事に来ているが、専用記事 back-massager-for-first-responders-after-shift は未掲載(→c)。`shiatsu for back pain` 4回・52.5位は痛み目的で、医療の線引きに注意が必要
- couples-different-sleep-temperatures-dual-zone-bed(17.4位・表示11・クリック1)と best-bedding-couples-different-temperatures-hot-sleeper(17.5位・表示11): 周辺語は `best mattress pad for dual heating and cooling` 6回・25.3位、`best heating pad for couples` 2回・5位、`best cooling topper … couple who sleep at different temperatures` 1回・9位、`dual zone comforter` 1回・37位。温める語が冷やす記事に出ている。どちらの記事でどの語を狙うかを決めないと、周辺記事を足しても取り合いが増える
- oura-ring-vs-whoop-sleep-tracking(30.0位・表示21): 表示の大半(14回)は上の Orion の語。`whoop vs oura` 系は計7回・45〜92位と低い。周辺の apple-watch-vs-oura-ring-sleep-tracking は `oura ring 4 vs apple watch` 5回・24.4位(本文に Ring 4・Series 11・Ultra の記述あり)
- white-noise-machines-vs-sound-machines-light-sleepers(10.5位・表示115): 上記のとおり大半が無関係語。参考として、同じ白色雑音機テーマで実際の購入語に近いのは portable-white-noise-machine-athletes-hotel(候補の条件外=6.7位だが表示55): `best white noise machine for athletes` 21回・6位、`best noise machine for athletes` 14回・5位、`white noise machine for athletes` 5回・5.2位。runners / cyclists / fitness enthusiasts の言い換えも各1回・1〜7位。11/19 にタイトル等を改善済み(2026-11-14-2)で、まだ効果判定できる期間ではない
- best-recovery-and-sleep-gifts-2026(26.5位・表示10): 内訳が分かる語は `i want a sleep gift with great durability.` 1回・89位だけ。周辺テーマを示す材料なし(データ不足)

### (c) 検索結果に未掲載の記事(内部リンクで支える対象)
gsc_index.json(11/23 確認)で未掲載は6本。うち5本は「Google が存在を知っているが一度も巡回していない」状態。
| 記事 | 状態 | 公開日 | 他の公開記事からのリンク数(本文 grep) |
|---|---|---|---:|
| white-noise-machine-for-apartment-noise | Google が URL を知らない | 11/19 | 2(white-noise-vs-sound、11/25予約の day-sleepers) |
| white-noise-machine-without-light | 存在は知っているが未巡回 | 11/06 | 4(white-noise-vs-sound・apartment-noise・本日公開の sleep-mask・11/25予約) |
| back-massager-for-first-responders-after-shift | 同上 | 11/02 | 3(shiatsu-back・heated-foot・compression-boots。下書きの heated-seat は除く) |
| what-to-buy-on-sale-recovery-sleep | 同上 | 10/30 | 4 |
| quiet-space-heaters-bedroom-light-sleepers | 同上 | 10/13 | 9 |
| heated-foot-massagers-nurses-standing-workers | 同上 | 10/11 | 5 |
- 事実: quiet-space-heaters は他記事から9本のリンクがあっても未巡回のまま。推測: リンク本数だけでは巡回が進んでいない。リンク元の多くも検索の表示が少ない記事で、URL 検査からの登録リクエストを併用する方が確実と考える
- `back massagers for first responders`(15回・28.3位)は、専用記事が未掲載のため shiatsu の記事が代わりに表示されている。未掲載記事のうち、検索語の実績がある唯一の記事
- 本日11/23公開の sleep-mask-for-side-sleepers と 11/25公開予定の white-noise-machine-for-day-sleepers は、他記事からのリンク0本。11/17公開の foot-warmer-for-bed も0本、11/15公開の compression-boots-for-nurses-full-leg-vs-calf は1本(ギフトガイドから)だけ(この2本は掲載済みだが表示0)

## アーキテクト向け: 構成改善の示唆
- データ不足のため、構成・見せ方の優劣に関する示唆は書かない(affiliate_click 0、記事セッション最大4)
- 事実のみ: best-cooling-pillow-for-menopause-night-sweats から cooling-mattress-pad-for-hot-flashes へのリンクはまだ入っていない(前回の申し送り2の後半)。white-noise-vs-sound → without-light のリンクは入った

## 前回(11/14)からの変化(期間が約3週間重なるため、傾向とは呼ばない)
| 項目 | 前回 | 今回 |
|---|---|---|
| 検索の表示 | 412 | 515 |
| 検索のクリック | 1(couples-dual-zone) | 1(同じ記事。28日の期間内に残っている同じ1件の可能性あり) |
| 掲載記事 | 24/32 | 29/35 |
| 未掲載 | 8本 | 6本(cooling-mattress-pad・no-drill-blackout・red-light-therapy-devices-for-home が掲載。apartment-noise が新たに追加) |
| white-noise-vs-sound | 17.4位・表示91 | 10.5位・表示115(増加分の多くは上記の無関係語) |
| back massagers for first responders | 15回・28.3位 | 15回・28.3位(変化なし) |
| GA4 セッション | 42(10/15〜11/14) | 31(10/24〜11/23) |
| affiliate_click | 0 | 0 |
- 11/14 の改善3件(white-noise-vs-sound、athletes、gift-guide-by-recipient)は 11/19 に反映済み(improvement_log.json に記録あり。前回の「記録が11/01で止まっている」は11/14分については解消。11/03 の blackout・赤色光の変更が記録されたかは今回未確認)。Search Console のデータは11/20までなので、効果はまだ判定できない

## 人間への申し送り(アナリストより)
1. 未掲載6本の URL 検査からの登録リクエスト。優先は back-massager-for-first-responders-after-shift(検索語の実績あり)→ white-noise-machine-for-apartment-noise(Google が URL 自体を知らない)→ 残り4本
2. 「◯◯ vs white noise machine」「◯◯ vs massage gun」型の不自然な検索語が white-noise-vs-sound と red-light-vs-massage-gun の表示の大半を占める。digest の「伸ばす候補」と順位はこれに引っ張られている。digest の集計でこの種の語を分けて表示するか判断してほしい
3. `best bedding for couples with different temperatures` 周辺の取り合いが4週目。温める語(heating pad for couples / dual heating and cooling)が冷やす記事に出ている。どちらの記事で狙うか決めてほしい
4. 本日公開の sleep-mask-for-side-sleepers、11/25公開の white-noise-machine-for-day-sleepers、11/17公開の foot-warmer-for-bed は他記事からのリンクが0本
5. 下書きのまま見送った heated-seat-massager-for-back に合う検索語(heated seat massager … back tension 4回・37.8位)が出ている。表示4回でデータ不足のため、公開判断の根拠にはならない。記録として共有
6. digest の「0」と「未取得」の混在が継続。10月分の Amazon 確定報酬レポートも今回の確認範囲では見当たらない(12月初回の突き合わせに必要)
