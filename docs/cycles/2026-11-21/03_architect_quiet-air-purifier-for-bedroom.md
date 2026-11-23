# 03. アーキテクト設計図: quiet-air-purifier-for-bedroom(2026-11-23)

インプット: docs/agents/architect.md、共通ルール(rule of foreign affiliate.md)、02_marketer.md「提案3」(依頼文では「テーマ3」)、関連既存記事4本(humidifiers / quiet space heaters / white-noise-without-light / noise machines vs sound machines)、構成見本 white-noise-machine-for-apartment-noise、src/_data/categories.json(`quiet-air-purifier-for-bedroom` は sleep-environment に登録済み)、lib/publishing.js

- スラッグ: `quiet-air-purifier-for-bedroom` / カテゴリ: sleep-environment(front matter は `category: Sleep` で可。categories.json の posts で解決済み)
- 本文は書かない。以下は設計のみ
- リポジトリのファイルは変更していない

---

## 0. 調査で分かった前提(ライターが最初に読むこと)

1. **メーカーの製品ページ(levoit.com / cowaymega.com / blueair.com)は自動取得が 429(アクセス制限)で本文を読めなかった。** 代わりに次の方法で確認した:
   - **Levoit Core 300S-P:** 公式サイトに置かれた **米国版取扱説明書 PDF を直接取得して本文を確認**(下表の多くはここから)。CADR・部屋の広さは公式ページの検索結果抜粋。
   - **Coway AP-1512HH:** cowaymega.com の製品ページ本文と、そこからリンクされた **米国版取扱説明書 PDF(2025-11-13版)を取得して確認**。※ cowaymega.com のフッターは「Copyright © 2026 DigiFist」。Coway の米国向けオンラインストアとして運営されているが、運営会社名が Coway ではない点は人間確認。
   - **Blueair Blue Pure 311i Max:** 公式ページは検索結果の抜粋のみ。説明書は第三者サイト(manuals.plus 等)の抜粋のみ。**公式の数字同士が食い違っている(下記)ので、311i Max の CADR は記事で使わない。**
2. **EPA と CARB は公式ページを取得して確認済み**(下の「公的機関の一般論」)。
3. **CARB(カリフォルニア州大気資源局)の認証リストで、候補の型番を確認した**(2026-11-23 取得)。重要な発見:
   - Coway AP-1512HH は **「Electronic」(電子式)** として認証(2016-01-04、G-16-011)。イオン発生機能(Coway の呼び名は "bipolar device" / 説明書では "IONIZER" ボタン)があるため
   - Blueair Blue Pure 311i Max も **「Electronic」**(2023-03-09、G-23-050)
   - Levoit Core 300S は **「Mechanical」(機械式=フィルターのみ)**(2021-05-13、G-21-183)。※ 「Core 300S-P」という表記での登録は見つからず。300S-P が同じ認証の範囲かは人間確認
   - CARB 認証は「オゾン排出 0.050 ppm 以下」を満たした、という意味。**「オゾンゼロ」ではない**。Electronic を悪く書かず、「イオン機能を切れるか」を比較軸にする
4. **Coway には新型「Airmega Mighty2(AP-1512N)」「Mighty2 Mini」が 2026 年に出ている**(CARB 2026-03/2026-09 認証、cowaymega.com に "NEW" 表示)。AP-1512HH は同サイトで現在も販売中(黒は購入可、白は "SOLD OUT OR UNAVAILABLE"、2026-11-23 時点)。旧型扱いになりつつあるので、公開前に Amazon で新品が買えるか人間確認。
5. **Levoit は「Core 300S」の現行表記が「Core 300S-P」**(公式の商品名・説明書とも 300S-P / Core 300S series)。記事では「Core 300S-P」と書く。旧「Core 300S」の中古・在庫品と混同しないよう注記する。
6. **Coway AP-1512HH の「Sleep mode」は公式の中で食い違う。** 製品ページの宣伝文は "In sleep mode, the Airmega Mighty is quiet as a whisper" だが、**仕様欄と米国版説明書の運転モードは「Auto・1・2・3・Eco」のみで Sleep mode が無い**。→ 記事では「Sleep mode がある」と書かない。「最も弱い風量(speed 1)」と書く。
7. **Amazon は開けないため、取り扱い・評価・レビュー数はすべて人間確認。下のスコアの「レビュー」は暫定。**

---

## 商品候補スコアリング(比較記事の場合)

**採点は暫定。** 「レビュー」は Amazon を開けないため推測。「紹介料」は価格帯からの相対的な推測(金額は書かない)。

| 商品 | 検索意図 | 紹介料 | レビュー(暫定) | 伝えやすさ | 比較軸 | 合計 |
|---|---|---|---|---|---|---|
| Levoit Core 300S-P | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Coway Airmega Mighty AP-1512HH | 2 | 1 | 2 | 2 | 2 | **9/10** |
| Blueair Blue Pure 311i Max | 2 | 2 | 1 | 2 | 1 | **8/10** |
| Coway Airmega Mighty2 Mini | 1 | 1 | 0 | 2 | 2 | 6/10 |
| Coway Airmega Mighty2(AP-1512N) | 1 | 2 | 0 | 1 | 1 | 5/10 |
| Winix 5500-2 | 1 | 1 | 1 | 1 | 1 | 5/10 |
| Dyson Purifier Cool 系 | 1 | 2 | 1 | 1 | 1 | 6/10 |
| Levoit Core 200S | 1 | 0 | 1 | 1 | 1 | 4/10 |
| Levoit Core Mini(Night Light 付き) | 0 | 0 | 1 | 1 | 1 | 3/10 |

採点の理由(要点):
- **Levoit Core 300S-P:** 説明書に「Display Off ボタン」と「Sleep Mode(3秒後に表示を消す)」が明記。暗い寝室という検索意図に直結。CARB は Mechanical(Core 300S として)。小さめの寝室向け。budget〜mid-range。レビューは不明なので暫定1。
- **Coway AP-1512HH:** 長く売られている定番で、Amazon のレビューは厚い可能性が高い(推測)。説明書に「IONIZER ボタンでイオン機能を切れる」「IONIZER を3秒長押しで空気質ランプを消せる」。CADR 3種と部屋の広さが公式に揃う。弱点は Sleep mode が説明書に無いこと、新型 Mighty2 への置き換わり。
- **Blueair 311i Max:** Night mode(最弱+ランプ完全減光)が一押しで済む、明るさ調整あり(説明書抜粋・人間確認)。premium 寄りで紹介料は高め。ただし **公式の CADR 表記が 250 / 283-314-365 / 153-159-174 と食い違う**、イオン機能を切れるか公式で未確認 → 比較軸は1。
- **Mighty2 Mini:** 公式で 19.2〜49 dB・Quiet Mark・CADR 143/150.6/173.7・Night Sensor。ただし「暗い部屋を感知して表示を暗くし、柔らかい光(soft glow)を出す」=ランプを完全に消したい読者には逆効果の可能性。2026年発売でレビュー薄い → Also Looked At。
- **Mighty2(AP-1512N):** 新型。公式仕様を今回確認できず → Also Looked At(1文、仕様の数字は書かない)。
- **Winix 5500-2:** CARB Electronic(PlasmaWave)。ランプ・イオン機能の公式仕様を今回確認できず → Also Looked At(仕様の数字は書かない)。
- **Dyson:** ファン兼用で premium。今回公式未確認 → Also Looked At に入れるなら「確認できた事実のみ」。入れなくてもよい。
- **Core 200S / Core Mini:** Core Mini は名前の通りナイトライト付き(CARB 表記 "Core Mini Air Purifier with Night Light")。「光を消したい」意図と合わない例として「選ばなかった理由」に1文。

### 採用(7点以上の上位3件)
1. **Levoit Core 300S-P** — 「表示を完全に消せる・小さめの寝室」枠(budget〜mid-range)
2. **Coway Airmega Mighty AP-1512HH** — 「やや広い寝室・イオン機能を切れる」枠(mid-range)。**条件:** 人間確認で Amazon に新品在庫が無い/旧型在庫のみなら Also Looked At に下げ、推奨2点で構成(7点以上の代替が無いため無理に足さない)
3. **Blueair Blue Pure 311i Max** — 「ボタン1つで最弱+消灯の Night mode」枠(premium)。**条件:** CADR は書かない(部屋の広さはメーカーの推奨値として「Blueair lists…」の形で1つだけ。人間が公式ページで目視した値を使う)

### Also Looked At(本文では短く1〜2文ずつ。確認できた事実だけ)
- **Coway Airmega Mighty2 Mini** — 公式で最小 19.2 dB(Sleep mode)・Quiet Mark 認証。ただし Night Sensor が暗い部屋で「soft glow」を出すと公式説明 → 真っ暗にしたい人は消せるか確認を
- **Coway Airmega Mighty2(AP-1512N)** — AP-1512HH の新型。今回は公式仕様を確認しきれず推奨から外した、とだけ書く
- **Winix 5500-2** — PlasmaWave(CARB では Electronic として認証)。イオン機能・ランプの切り方は公式の説明書で確認を、とだけ書く
- **Levoit Core Mini(Night Light 付き)** — 名前の通りナイトライト機能付き。光を足したくない寝室には向かない例として

---

## 公式で確認できた仕様(出典つき)

### Levoit Core 300S-P
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | 公式サイトに製品ページ・説明書・交換フィルターあり。旧「Core 300S」の後継表記 | https://levoit.com/products/core-300s-p-smart-air-purifier(検索抜粋)/ 説明書 |
| 運転音 | **22–54.5 dB**(説明書の仕様欄。**測定条件の記載なし → 他社と比較不可**)。製品ページは「22–50dB」「as low as 22dB」と表記が異なる → 記事では説明書の値を使い、測定条件不明と書く | 説明書 PDF: https://levoit.com/cdn/shop/files/HEAPAPLVSUS0073A_Core_300S-P_Smart_Air_Purifier_manual_US_A2-240918_4855d907-1d27-4231-ad1c-82899f56e370.pdf |
| Sleep Mode | 「fan speed 1 より遅い風量で静かに運転」「ほかのボタンを押さなければ 3 秒後に表示を消す」 | 同上 |
| 表示を消す | **Display Off ボタン**:ボタンのランプと表示ランプを消す(**ただし Check Filter Indicator=フィルター確認ランプは除く**)。ボタンを押すと3秒だけ点く | 同上 |
| フィルター確認ランプ | 交換時期には表示オフでも点灯したまま。目安「6–8 か月で点灯」 | 同上 |
| フィルター | 3層の Original Filter(交換品 Core 300-P-RF)。別売で Pet Allergy(Core 300-RF-PA)/ Toxin Absorber(Core 300-RF-TX)。プレフィルターは 2–4 週ごとに掃除、本体フィルターは 6–8 か月で交換目安 | 同上 |
| オートモード | レーザー式ほこりセンサー(AirSight Plus)で風量を自動調整。※寝ている間にオートだと風量が上がり得る → 寝室では Sleep Mode を使う、という設計上の注意に使える | 同上 |
| アプリ | VeSync アプリ(タイマー・スケジュール等)。アプリから Display Off 等を操作可 | 同上 |
| CADR | 141 CFM(240 m³/h)。Levoit ブログで「AHAM Verified」と記載。**AHAM 公式ディレクトリでは未確認 → 人間確認** | 製品ページ・ブログ(検索抜粋)https://levoit.com/blogs/levoit-blog/air-purifier-for-different-room-sizes |
| 部屋の広さ | 219 sq ft(4.8 回換気/時)/ 1,051 sq ft(1 回換気/時)。記事では 219 sq ft(4.8 ACH)を使う | 製品ページ(検索抜粋) |
| オゾン | 製品ページに「Ozone Free」(検索抜粋)。CARB リストでは「Core 300S」が Mechanical(G-21-183) | CARB リスト |
| 電源・大きさ | AC 120V、39W、8.7 × 8.7 × 14.2 in、7.48 lb | 説明書 |
| ENERGY STAR | 説明書に ENERGY STAR 認証モデルの記載 | 説明書 |

### Coway Airmega Mighty AP-1512HH
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | cowaymega.com で販売中(黒は購入可、白は売り切れ表示、2026-11-23)。新型 Mighty2 も併売 | https://cowaymega.com/products/mighty-ap-1512hh |
| 運転音 | **24 ~ 53 dB(A)**(製品ページ仕様欄。**測定条件の記載なし → 比較不可**)。説明書の仕様欄には dB 記載なし | 同上 |
| 運転モード | Auto・1・2・3・Eco の5段階(仕様欄・説明書)。**Sleep mode は説明書に無い**(宣伝文にはある → 記事では使わない) | 同上 / 説明書 PDF: https://cdn.shopify.com/s/files/1/0351/1864/5383/files/9240281_AP-1512HH__Manual_US__25.11.13.pdf |
| Eco mode | 30分汚れを感知しないとファンが止まり、汚れを感知すると再始動。※夜中にファンが止まる/動き出す=音の変化がある点は「light sleeper には注意」として書ける(推測ではなく仕組みの説明) | 説明書 |
| ランプを消す | 説明書「Press and hold the IONIZER button for 3 seconds to turn on or off the air quality indicating light.」→ **空気質ランプは消せる**。ボタン類・フィルター交換ランプまで消えるかは記載なし → 人間確認 | 説明書 |
| イオン機能 | 「Ionizer On/Off: Use this button to turn the ionizer on or off.」→ **切れる** | 説明書 |
| オゾン | 説明書「complies with the maximum allowable concentration of ozone of 0.050 ppmv」。CARB リストでは Electronic(G-16-011) | 説明書 / CARB |
| CADR | 233(Smoke)/ 246(Dust)/ 240(Pollen)。ENERGY STAR の認証製品リストも同じ値(AHAM AC-1 試験に基づく)。**AHAM Verifide の掲載は未確認 → 「AHAM 認証済み」とは書かない。「Coway lists a CADR of…」と書く** | 製品ページ仕様欄 / https://downloads.energystar.gov/bi/qplist/Room_Air_Cleaners_Qualified_Product_List.pdf(検索抜粋) |
| 部屋の広さ | 361 ft²(4.8 回換気/時)、874 ft²(2 回)、1,748 ft²(1 回) | 製品ページ・説明書 |
| フィルター | プレフィルター(水洗い可、2–4 週ごと)+脱臭フィルター(6 か月で交換)+HEPA(1 年で交換)。「最大風量で1日8時間使用」が前提と注記 | 説明書 |
| タイマー | 1・4・8 時間 | 説明書 |
| 電源・大きさ | 120V、77W、16.8 × 18.3 × 9.6 in、12.3 lb | 説明書 |

### Blueair Blue Pure 311i Max
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | 公式サイトに製品ページあり(検索結果で確認)。在庫状況は未確認 → 人間確認 | https://www.blueair.com/products/blue-pure-311i-max |
| 運転音 | 23–50 dB(公式の仕様表記、検索抜粋)。**測定条件不明 → 比較不可** | 同上(検索抜粋) |
| Night mode | 風量ボタンの選択肢が 1・2・3・AUTO・NIGHT。「最弱の風量+ランプを完全に暗くする」(311i+ Max の公式説明書 PDF の抜粋、311i Max は第三者サイトの説明書抜粋)→ **人間確認** | https://www.blueair.com/us/troubleshooting-blue.html(検索抜粋)ほか |
| 明るさ調整 | 風量ボタンと電源ボタンの同時長押しで表示の明るさを変えられる(第三者サイトの説明書抜粋)→ **人間確認。確認できなければ記事に書かない** | manuals.plus 等 |
| イオン機能 | CARB リストで Electronic(G-23-050)。イオン機能を切れるかは公式で未確認(第三者サイトに「切れない」との記載あり)→ **人間確認。記事では「切れるかは公式で確認できなかった」と書く** | CARB |
| CADR | **公式ページ間で 250 / 283・314・365 / 153・159・174 と食い違う → 記事で使わない** | blueair.com 各ページ(検索抜粋) |
| 部屋の広さ | 387 ft² / 439 ft² の両方の表記あり → 人間が公式ページで目視した1つだけ使う | 同上 |
| フィルター | 交換目安は「最大9か月」と「6か月」の表記が混在 → 人間確認。記事では「メーカーの目安を確認」程度に | 同上 |

### 公的機関の一般論(取得して確認済み)
EPA「Guide to Air Cleaners in the Home」 https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home
- 粒子を取るなら、**部屋の広さに足りる CADR** の機種を選ぶ。CADR が高いほど広い部屋に使える。**CADR はふつう最大風量で測る**(→ 静かな最弱運転では表示どおりの能力は出ない、という本記事の核心に使える)
- 目安表(天井 8 フィート想定): 100 sq ft→65 cfm、200→130、300→195、400→260、500→325、600→390
- **CADR は粒子だけの指標**。ガス(におい等)を取る性能の広く使われる評価方式は無い
- 風量を上げる・長く運転するほど、ろ過される空気は増える。低い風量では減る
- **騒音:** 一部の機種は騒音値を表示している。騒音は風量設定に左右される。騒音で使わなくなりそうなら公表騒音値の低い機種を検討。目安として約 50 dB は現代の冷蔵庫の運転音程度
- **オゾン:** 意図的にオゾンを出す空気清浄機は避ける(オゾンは肺への刺激物)。電気集じん・イオン発生・コーティング不十分な UV・プラズマ式は場合によりオゾンを出す可能性。CARB と AHAM が「オゾンをほとんど/全く出さない」機種のリストを持つ。オゾン発生器を人のいる空間で使うことを承認した連邦機関は無い
- **アレルギー・喘息:** 「Possibly(可能性はある)」。HEPA 空気清浄機の研究で一部の症状に改善が見られたが、大きな改善とは限らず、すべての症状ではない → **記事ではこの温度感を超えない**。「治る」「改善する」とは書かない
- 空気清浄機は汚染源の対策や換気の代わりにならない(同ページ)

CARB https://ww2.arb.ca.gov/list-carb-certified-air-cleaning-devices / https://ww2.arb.ca.gov/air-cleaner-information-consumers
- 2010 年以降、カリフォルニアで販売される室内用空気清浄機はオゾン排出 0.050 ppm 以下などの基準を満たす必要がある。認証リストは Mechanical / Electronic の区別つき

---

## 記事設計

### タイトル案
1. **Quiet Air Purifier for Bedroom: 3 Picks With Low Fan Noise and Lights You Can Turn Off**(推奨。84字で長め → SEO 上の表示で切れる可能性。前半に主語が入るので許容)
2. Quiet Air Purifier for Bedroom Use: Sleep Modes, Display Lights, and Fan Noise Compared(83字)
3. Quiet Air Purifier for Bedroom: Which Ones Go Dark and Stay Quiet at Night?(76字)
4. 60字前後に収める短縮案: **Quiet Air Purifier for Bedroom: Low Noise, Lights Off**(54字)

→ 推奨は 1(マーケター案)。60字前後を厳守するなら 4。最終判断はディレクター/人間。

- ターゲットキーワード: `quiet air purifier for bedroom`(主)/ `air purifier for light sleepers`(補。H2 1か所と本文1〜2回、詰め込まない)
- メタディスクリプション案(約150字):
  "Looking for a quiet air purifier for your bedroom? We compare sleep modes, display lights you can switch off, published noise levels, and filter upkeep."
- 想定語数: 2,200〜2,800 語
- front matter: `layout: post.njk` / `tags: post` / `category: Sleep` / `publishAt` は公開日(人間が決定)
- 冒頭の開示文: 見本と同じ形(affiliate disclosure + Not medical advice + "Our picks are based on manufacturer specifications and published product information. We have not used these products ourselves.")

### 見出し構成(H2/H3)

1. **導入**(約150語)
   - 冬は窓を閉めきる→寝室に空気清浄機を置きたい→でもファンの音・青いランプ・夜中に急に強くなる自動運転が気になる、という場面
   - この記事の見方:「音」「光」「部屋の広さ」「フィルターの手間」の4つだけで比べる。効能の話はしない
   - 内部リンク: 光の悩みの姉妹記事として [white noise machines without light] に1回
   - 「In a hurry?」CTA ボックス(Levoit Core 300S-P)

2. **H2: What Makes an Air Purifier Hard to Sleep Next To**(約300語)
   - H3: Fan noise, and why the change in sound matters more than the number — 一定の音より「急に強くなる/止まる」が気になる人がいる、という書き方。Auto mode と Coway の Eco mode(30分で停止→再始動)を例に。※ quiet space heaters 記事の「change in sound」の考え方に内部リンク
   - H3: Display lights, air-quality rings, and filter reminders — 光の出どころを4つに分ける(電源・空気質ランプ・フィルター交換ランプ・画面)。「dimmed」と「off」の違い
   - H3: A note on ionizers and ozone — EPA の一般論(意図的にオゾンを出す機種は避ける/イオン式などは出す可能性/CARB・AHAM のリスト)。**イオン機能付き=危険とは書かない**。「CARB 認証があるか」「イオン機能を切れるか」を確認しよう、まで

3. **H2: Quiet vs. Powerful: The Trade-Off on Every Purifier**(約250語)— 本記事の核
   - EPA:CADR はふつう最大風量で測る/低い風量ではろ過する空気が減る
   - だから「寝る時は最弱=静か」と「部屋に足りる能力」は両立しにくい → 対策は「部屋に対して余裕のある機種を選び、低めの風量で回す」「寝る前に強めで回して、寝るときに Sleep/Night に落とす」(運用の提案。効果の断定はしない)
   - H3: How to read a dB figure on a listing — 測定条件(距離・どの風量か)がメーカーごとに違うので、**別ブランドの dB は直接比べられない**。比較表の dB は「メーカー公表値・測定条件不明」と明記。EPA の「約50 dB ≈ 冷蔵庫」の目安を1回だけ
   - H3: Matching CADR to your bedroom size — EPA の目安表(100〜400 sq ft の4行だけ抜粋で表にする=Pinterest 化しやすい要素)、天井が高い部屋は余裕を

4. **H2: Bedroom Air Purifier Checklist: What to Look for on the Listing**(約200語、チェックリスト=画像化しやすい要素)
   - □ Sleep/Night mode があるか、それは何をするか(最弱になる?ランプも消える?)
   - □ 表示を「消せる」か「暗くできる」だけか/フィルター交換ランプは消えるか
   - □ Auto mode が夜中に風量を上げないか(寝室では手動か Sleep を推奨)
   - □ 公表 dB と、それがどの風量の値か
   - □ 部屋の広さに対する CADR(AHAM の数字か)
   - □ イオン機能の有無・切れるか・CARB 認証
   - □ 交換フィルターの目安と入手性

5. **H2: Quiet Bedroom Air Purifiers, Compared**(比較表)
   - 列: Product / Quietest setting(名前) / Published noise range(測定条件不明と脚注) / Display lights at night / Ionizer / Room size (maker's figure) / Filter change guide / Price tier / Filter cost tier / Best for / May not suit
   - 値(ライター用の下書き。確認済みのものだけ):
     - Levoit Core 300S-P / Sleep Mode / 22–54.5 dB(manual) / Display Off button; filter-check light stays on when due / None listed; CARB: Mechanical(Core 300S) / 219 sq ft(4.8 ACH) / Main filter 6–8 months / budget〜mid-range / budget / 小さめ寝室で暗さ重視 / 広い部屋
     - Coway AP-1512HH / Speed 1(Sleep mode なし)/ 24–53 dB(A) / Air-quality light can be switched off(他のランプは要確認)/ Yes, can be turned off; CARB: Electronic / 361 ft²(4.8 ACH) / Deodorization 6 months, HEPA 1 year / mid-range / mid-range / やや広い寝室・イオンを切りたい / 「Sleep mode」が欲しい人、Eco の停止・再始動が気になる人
     - Blueair 311i Max / Night mode / 23–50 dB / Night mode fully dims lights(人間確認後)/ CARB: Electronic; whether ionizer can be switched off not confirmed / (人間確認後の1値) / (人間確認後) / premium / mid-range〜premium(人間判断) / ワンボタンで最弱+消灯 / イオン機能を確実に切りたい人
   - 表の下に注記: dB は各社の公表値で測定条件が違うため比較できない/価格は書かない(budget / mid-range / premium の相対表現)
   - 表の直後に CTA ボックス(3商品まとめ)

6. **H2: The 3 Picks**(各 約300〜350語)
   - 各商品の型(見本どおり): **What it's for:** 1行 → 本文(音・光・広さ・フィルター・オゾン/イオン)→ **Who it may not suit:** 箇条書き3〜4 → CTA ボックス
   - H3: **Levoit Core 300S-P — Best for a Fully Dark Small Bedroom**
     - 書くこと: Display Off ボタン/Sleep Mode は speed 1 より弱く3秒で表示オフ/**フィルター確認ランプは交換時期には点灯する**(正直に)/219 sq ft(4.8 ACH)/Auto は夜に風量が上がり得る/VeSync アプリ
     - 向かない: 広いリビング兼寝室/アプリを使いたくない人(本体だけでも可と補足)/フィルター交換ランプも嫌な人
   - H3: **Coway Airmega Mighty AP-1512HH — Best for a Larger Bedroom (With an Ionizer You Can Switch Off)**
     - 書くこと: 361 ft²/CADR 233・246・240(Coway lists)/24–53 dB(A)/**Sleep mode は説明書に無い。最弱は speed 1**/IONIZER ボタンでイオン機能 on/off、3秒長押しで空気質ランプ on/off/Eco mode はファンが止まって再始動する=音の変化/フィルター目安/新型 Mighty2 の存在に一言
     - 向かない: 「Sleep」ボタンが欲しい人/音の変化に敏感で Eco を使えない人(Eco を使わなければよい、と補足)/ランプを全部消したい人(要確認)/小さな寝室で場所を取りたくない人(16.8 × 18.3 in)
   - H3: **Blueair Blue Pure 311i Max — Best for One-Press Night Mode**
     - 書くこと: Night mode = 最弱+ランプを完全に暗く(人間確認後に断定度を決める)/23–50 dB/CARB Electronic、イオン機能を切れるかは公式で確認できなかった/部屋の広さは人間確認値を1つ/CADR は書かない(理由:公式表記が食い違っていたため、と書いてよい)
     - 向かない: イオン機能を必ず切りたい人/フィルター代を抑えたい人/アプリ不要派(要確認)

7. **H2: Air Purifiers We Looked At but Didn't Pick**(約150語)— Also Looked At の4機種を各1〜2文

8. **H2: How to Run an Air Purifier in Your Bedroom Without It Waking You**(約250語)
   - H3: Run it on high before bed, then drop to sleep mode — EPA「風量・運転時間でろ過量は変わる」を根拠に運用案として。効果の断定はしない
   - H3: Placement — EPA「最も長く過ごす部屋に置く」。ベッドから少し離す、吹き出し口を顔に向けない(快適性の話として)、メーカーの設置間隔に従う
   - H3: Taming leftover glow — 黒いマスキングテープ等で覆うのはセンサーや吸排気口をふさがない範囲で/メーカー指示に反しないこと。white-noise-machine-without-light の「How to Cut the Glow」に内部リンク
   - H3: Keep the filter on schedule — プレフィルター掃除の周期(Levoit 2–4 週、Coway 2–4 週)

9. **H2: What an Air Purifier Can and Can't Do for Your Bedroom**(約200語)
   - EPA の温度感をそのまま:アレルギー・喘息の症状について「possibly」、研究で一部症状に改善が見られたが大きいとは限らない、すべての症状ではない/汚染源の対策・換気の代わりにはならない/CADR は粒子のみ、においやガスは別
   - 「よく眠れるようになる」とは書かない。この記事は「置いても眠りの邪魔になりにくい機種の選び方」であると再確認
   - 乾燥が気になるなら humidifier 記事へ、寒さなら quiet space heaters 記事へ(冬の寝室シリーズとして)

10. **H2: Who a Quiet Bedroom Air Purifier Isn't Right For**(約150語)
    - 完全な無音が必要な人(どの機種もファンの音はする)
    - 喘息・重いアレルギーがあり治療の代わりを探している人 → 医師へ
    - 原因がカビ・湿気の場合(EPA:空気清浄機はカビ問題を解決しない)
    - 広いワンルーム・天井の高い部屋で小型機1台に期待する人
    - フィルター交換の手間・費用を続けられない人
    - 小さな子ども・ペットがいてコードや転倒が心配な場合はメーカーの注意に従う(断定しない)

11. **H2: FAQ**(H3 で4〜5問)
    - Is a quiet air purifier quiet enough to sleep next to? — 公表値の比べ方の注意+感じ方は人による
    - Can I turn off the lights on an air purifier? — 機種による。Levoit=消せる(フィルター確認ランプ除く)/Coway=空気質ランプを消せる/Blueair=Night mode で暗く(確認後)
    - Do air purifiers with ionizers produce ozone? — EPA・CARB の一般論、CARB 0.050 ppm 基準、リストで確認
    - Should I leave my air purifier on all night? — メーカーの説明に従う/タイマー(Coway 1・4・8h、Levoit アプリ)/安全面はメーカー指示優先。断定しない
    - What size air purifier do I need for my bedroom? — EPA の目安表へ誘導
    - (候補) Is an air purifier the same as a humidifier? — 別物。humidifier 記事へリンク

12. **H2: Which Quiet Air Purifier Fits Your Bedroom?**(まとめ、約150語)
    - 3行の早見(暗さ最優先の小さめ寝室→Levoit/やや広い寝室でイオンを切りたい→Coway/ボタン1つで夜モード→Blueair)
    - 最後の CTA ボックス
    - 医療免責(本文末尾にも1文):"This article is for general informational purposes only and is not medical advice. If you have asthma, allergies, or another breathing condition, talk with your doctor about whether an air purifier makes sense for you."

### 健康・表現のルール(この記事固有)
- 見出しに "Relieves" "Cures" "Better Sleep" を使わない。"Does…?" "What…Can and Can't Do" 型
- ECARF・Quiet Mark・「Microplastic Removal」など、メーカーの認証・効能系の宣伝文句は引用しない(Mighty2 Mini の紹介でも「Quiet Mark 認証」だけに留める)
- 「AHAM 認証済み」は AHAM ディレクトリで確認できた機種にだけ書く。今回は全機種未確認 → 「the maker lists a CADR of…」の形
- dB はメーカー公表値・測定条件不明と必ず添える。機種間の「どちらが静か」の断定はしない
- 「使った」「テストした」は書かない

---

## アフィリエイトリンク配置ポイント
すべて Amazon Associates US(tag=quietrecover-20)、`rel="nofollow sponsored" target="_blank"`、文言は "Check … on Amazon"。価格・割引・送料無料・セール名は書かない(現在の Black Friday 時期でも記事本文には書かない)。

| 位置 | 商品 | 検索リンク |
|---|---|---|
| 導入直後「In a hurry?」 | Levoit Core 300S-P | https://www.amazon.com/s?k=Levoit+Core+300S-P+air+purifier&tag=quietrecover-20 |
| 比較表の直後(まとめ) | 3点 | 下の3本 |
| 各 Pick の末尾 | Levoit Core 300S-P | https://www.amazon.com/s?k=Levoit+Core+300S-P+air+purifier&tag=quietrecover-20 |
| 〃 | Coway AP-1512HH | https://www.amazon.com/s?k=Coway+Airmega+AP-1512HH+Mighty&tag=quietrecover-20 |
| 〃 | Blueair 311i Max | https://www.amazon.com/s?k=Blueair+Blue+Pure+311i+Max&tag=quietrecover-20 |
| まとめ | 3点(短い一言つき) | 同上 |

- 交換フィルターへのリンクは入れない(本記事の焦点がぶれる。入れるなら人間判断)
- Also Looked At にはリンクを付けない(推奨と誤解されないよう)
- ブランド直販(Impact 等)は未承認のため使わない

## 内部リンク候補(すべて公開済みを確認。publishAt が 2026-11-23 より過去、または publishAt 無しで published: false でもない)
| リンク先 | 公開日 | 置く場所 | アンカー例 |
|---|---|---|---|
| `/posts/white-noise-machine-without-light/` | 2026-11-06 | 導入、および「Taming leftover glow」 | our guide to white noise machines without light |
| `/posts/quiet-space-heaters-bedroom-light-sleepers/` | 2026-10-13 | 「Fan noise, and why the change in sound…」、まとめ前 | quiet space heaters for light sleepers |
| `/posts/best-quiet-bedroom-humidifiers-for-fall/` | 2026-08-29(publishAt 無し・公開済み) | 「Can and Can't Do」、FAQ(humidifier との違い) | quiet bedroom humidifiers |
| `/posts/white-noise-machines-vs-sound-machines-light-sleepers/` | 2026-09-27 | 「Who it isn't right for」(音を消したい人は別の対策) or FAQ1 | noise machines for light sleepers |

- 記法は必ず `{{ '/posts/xxx/' | url }}`
- 使わない: white-noise-machine-for-day-sleepers(publishAt 2026-11-25、未公開)、non-wearable-sleep-tracker・quiet-massage-gun-for-apartments(published: false)
- 逆方向(既存記事からこの記事へ)のリンク追加は公開後に別作業(既存記事の修正はアーキテクトの範囲外)

---

## 人間確認(公開前)
1. **Amazon:** 3商品の取り扱い・新品在庫・評価・レビュー数(スコアの「レビュー」欄を確定)。特に Coway AP-1512HH が旧型在庫だけになっていないか、Levoit の検索で「300S-P」が出るか
2. **Levoit Core 300S-P:** CADR 141 CFM と 219 sq ft を公式製品ページで目視/AHAM Verifide ディレクトリ掲載/CARB リストで 300S-P が対象か
3. **Coway AP-1512HH:** IONIZER 長押しで消えるのが「空気質ランプ」だけか、他のランプ(ボタン・フィルター交換)の扱い/AHAM Verifide 掲載/cowaymega.com が Coway 公式扱いでよいか(運営 DigiFist)
4. **Blueair 311i Max:** 公式説明書で Night mode の「ランプ完全減光」と明るさ調整の手順/イオン機能を切れるか/推奨の部屋の広さ(387 か 439 sq ft)/フィルター交換目安(6 か 9 か月)/在庫
5. タイトル案の最終決定(84字案か54字案か)
6. 採点は暫定。人間確認の結果で 7 点を割る商品があれば推奨2点構成に変更

## 出典一覧
- EPA Guide to Air Cleaners in the Home: https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home(取得・本文確認)
- CARB 認証リスト: https://ww2.arb.ca.gov/list-carb-certified-air-cleaning-devices(取得・型番確認)
- CARB 消費者向け情報: https://ww2.arb.ca.gov/air-cleaner-information-consumers(検索抜粋)
- Levoit Core 300S-P 説明書(米国版): https://levoit.com/cdn/shop/files/HEAPAPLVSUS0073A_Core_300S-P_Smart_Air_Purifier_manual_US_A2-240918_4855d907-1d27-4231-ad1c-82899f56e370.pdf(取得・本文確認)
- Levoit Core 300S-P 製品ページ: https://levoit.com/products/core-300s-p-smart-air-purifier(検索抜粋のみ)
- Coway AP-1512HH 製品ページ: https://cowaymega.com/products/mighty-ap-1512hh(本文確認)
- Coway AP-1512HH 説明書(米国版 2025-11-13): https://cdn.shopify.com/s/files/1/0351/1864/5383/files/9240281_AP-1512HH__Manual_US__25.11.13.pdf(取得・本文確認)
- Coway Mighty2 Mini: https://cowaymega.com/products/airmega-mighty2-mini(検索抜粋)
- Blueair 311i Max: https://www.blueair.com/products/blue-pure-311i-max(検索抜粋のみ)/ https://www.blueair.com/us/troubleshooting-blue.html(検索抜粋)
- ENERGY STAR Room Air Cleaners QPL: https://downloads.energystar.gov/bi/qplist/Room_Air_Cleaners_Qualified_Product_List.pdf(検索抜粋)
