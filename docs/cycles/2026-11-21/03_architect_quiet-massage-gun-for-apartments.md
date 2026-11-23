# 03. アーキテクト設計図: quiet-massage-gun-for-apartments(2026-11-23)

インプット: docs/agents/architect.md、共通ルール(rule of foreign affiliate.md)、02_marketer.md 提案1、既存記事 white-noise-machine-for-apartment-noise(承認済みの型)/ massage-gun-vs-compression-boots-recovery / red-light-therapy-vs-massage-gun / 2026-recovery-sleep-gift-guide-by-recipient、メーカー公式ページ(下記の出典)

- スラッグ: `quiet-massage-gun-for-apartments`
- カテゴリ: front matter `category: Recovery`(categories.json の recovery に解決される)。※ categories.json の `posts` に1行追加が必要かはライター/ディレクター側で確認
- 狙う検索語: `quiet massage gun`(主)/ `quietest massage gun for apartment`(補)

---

## 0. 重要な前提(ライターへの申し送り)

1. **Amazon は確認できていない。** 取り扱い・評価・レビュー数・価格帯はすべて「人間確認」。下の採点の「レビュー」欄は全商品とも暫定 1 点。
2. **デシベル値はメーカー公式ページで本文として確認できたものだけ使う。** 今回それに当たるのは Ekrin の2機種だけ(下の「仕様の確認結果」)。他社の数値(第三者レビューの計測値、検索結果に出たが公式ページ本文で確認できなかった数値)は **記事に書かない**。
3. **dB は各社の測り方が違い、比べられない。** Ekrin も測定条件(距離・速度・負荷の有無)を公表していない。記事では「メーカーが公表している範囲」と書き、「最も静か」「◯dB だから寝ている人は起きない」とは書かない。
4. **「the quietest」と断定しない。** 主検索語に答えつつ、「どれが一番静かかは公表値からは決められない。だから音の数字・音の伝わり方・使い方で選ぶ」という切り口にする(タイトルに "quietest" を入れる場合は疑問形)。
5. **効能を書かない。** 痛みが取れる・回復が早まる・よく眠れる、は使わない。比べるのは「音(公表の有無と値)・重さ・電池・アタッチメント・振り幅(amplitude)・保証」だけ。
6. **価格は書かない。** budget / mid-range / premium の相対表現のみ。値引き率・セール名・送料に触れない(Ekrin 公式に Early Black Friday の表示があったが記事には一切書かない)。
7. 一人称は "we"。実際に使っていないので「使ってみた」「静かだった」と書かない。冒頭の開示文は white-noise-machine-for-apartment-noise と同じ型(アフィリエイト開示+医療免責+「メーカー仕様と公開情報に基づく/自分たちでは使っていない」)。

---

## 仕様の確認結果(メーカー公式)

| 商品 | 音(公式の表現) | 重さ | 電池 | 速度 | アタッチメント | その他 | 出典 |
|---|---|---|---|---|---|---|---|
| Ekrin B37 | **35–55 dB**("As quiet as rainfall") | 2.2 lbs | Up to 8 Hours / Fast USB-C PD | 5 speeds, up to 3200 RPM | 4(flat, bullet, round, fork) | Lifetime Warranty / 10 Min. Intelligent Stop / Travel Case / 15° angled handle | https://www.ekrin.com/pages/compare-models |
| Ekrin Bantam | **35–58 dB**("As quiet as a conversation") | 1.1 lbs | Up to 6 Hours / USB-C | 3 speeds, up to 3200 RPM | 4(flat, bullet, round, fork) | Lifetime Warranty / 10 Min. Intelligent Stop / Travel Case | https://www.ekrin.com/pages/compare-models |
| Theragun Relief | **dB 値の公表なし**。"Whisper-quiet for a distraction-free treatment" | 1.37 lbs | Around 120 minutes / USB-C | 3 speeds(low/medium/high、1ボタン) | 3(Standard Ball, Dampener, Thumb) | 10mm amplitude("Comfortable 10mm") | https://tw.therabody.com/en/blogs/theragun-faq/relief (Therabody 公式FAQ、英語版)。US 商品ページ https://www.therabody.com/us/en-us/theragun-relief.html は 429 で本文取得できず |
| Hypervolt Go 2(Also Looked At) | **dB 値の公表なし**。QuietGlide™ technology | 1.5 lbs | Up to 3 hours | 3 speeds | 2(flat, bullet) | 40W brushless motor / TSA carry-on 承認 / 1 year warranty | https://get.hyperice.com/compare-page |
| Bob and Brad Q2 Mini(Also Looked At) | **dB 値は公式ページ本文で確認できず**。"noise reduction technology keeps it ultra-quiet even at max speed" | 1.5lbs(公式ページの記載) | 記載なし | 5 speeds(1800–3000/min) | 5 | 2年保証 / USB-C / 10-minute auto-off | https://www.bobandbrad.com/products/bob-and-brad-q2-mini-massage-gun |
| Theragun Mini 3rd Gen(Also Looked At・既存記事で採用済み) | **dB 値の公表なし**。"30% smaller, lighter and quieter than the original Theragun Mini (1st Gen)" | 0.45 kg(FAQ)/ 0.4 kg(US 商品ページの検索要約)で食い違い | Around 120 minutes(FAQ)/ 150 minutes(US の検索要約)で食い違い | 3 speeds | 3(Dampener, Standard Ball, Thumb)+ soft travel case | QuietForce Solution(異音時の注油)同梱 | https://tw.therabody.com/en/blogs/theragun-faq/mini-3rd-generation |

### 確認できなかった/使わない数値
- **Bob and Brad Q2 Mini の 40–50 dB**: 検索結果の要約には出たが、公式ページを取得した本文には無い(画像内の可能性)。人間確認まで記事に書かない。
- **Renpho Power Massage Gun の ≤45dB**: 公式ページが 429 で取得できず。検索要約では同じページ内で 45dB と 55dB が食い違う。今回は不採用。
- **Lifepro(Sonic Lite Mini 40–50 dB、DynaMini 45 / 45–55 dB)**: 公式ページが 403。検索要約でも食い違いあり。不採用。
- **Theragun Prime / Hypervolt 2 などの第三者計測値(65–75 dB など)**: メーカー値ではないので書かない。
- Theragun Relief の Bluetooth/アプリ対応: 公式FAQ は "not Bluetooth enabled"、US ページは連携ありとの検索要約で食い違い → 記事では触れない。

---

## 商品候補スコアリング(暫定:Amazon 未確認)

レビュー欄は Amazon の評価・件数を見られないため全商品「暫定1」。紹介料は公式の価格帯から相対的に推定(人間確認)。

| 商品 | 検索意図 | 紹介料 | レビュー | 伝えやすさ | 比較軸 | 合計 |
|---|---|---|---|---|---|---|
| Ekrin B37 | 2(公式に dB 範囲・フルサイズ) | 2 | 1(暫定) | 2 | 2 | **9/10** |
| Ekrin Bantam | 2(公式に dB 範囲・1.1 lbs) | 1 | 1(暫定) | 2 | 2 | **8/10** |
| Theragun Relief | 1(静音をうたうが数値なし) | 1 | 1(暫定) | 2 | 2(10mm・1ボタン・軽さ) | **7/10** |
| Hypervolt Go 2 | 1(QuietGlide、数値なし) | 1 | 1(暫定) | 2 | 1(アタッチメント2個で軸が少ない) | 6/10 |
| Bob and Brad Q2 Mini | 1(静音をうたうが数値未確認) | 0 | 1(暫定) | 2 | 2 | 6/10 |
| Theragun Mini 3rd Gen | 1(1st Gen 比で静か、数値なし) | 1 | 1(暫定) | 2 | 1 | 6/10 |
| Theragun Prime | 0(静音の数値なし・フルサイズで重い) | 2 | 1(暫定) | 1 | 2 | 6/10 |
| Renpho Power | 1(公式数値が食い違い・未取得) | 0 | 1(暫定) | 1 | 2 | 5/10 |

採用(7点以上の上位3件): **Ekrin B37 / Ekrin Bantam / Theragun Relief**
- Relief は 7 点で Hypervolt Go 2 と僅差。Relief を採るのは「振り幅 10mm=打つ強さが控えめ」「1ボタン」という“音以外で夜向き”の軸を出せるため。Go 2 は Also Looked At へ。
- Ekrin が2機種になる理由を本文で明記する:「今回確認した中で、自社ページに dB の範囲を載せていたのは Ekrin だけ。フルサイズとコンパクトで比べる」
- **人間確認で点が動く可能性**: Amazon の評価4.0以上かつ100件以上なら各+1。Ekrin が Amazon で扱われていない/評価が低い場合は、Hypervolt Go 2 を3枠目に繰り上げ(その場合 Bantam か B37 を Also Looked At へ)。

### Also Looked At(本文に短く。各2〜3文)
- **Hypervolt Go 2** — QuietGlide をうたい 1.5 lbs・up to 3 hours。dB の公表は見つからず、ヘッドは2つ。※ 2026-recovery-sleep-gift-guide-by-recipient で採用済み → 「ギフト」ではなく「音の数値が無い・ヘッドが少ない」という別の切り口で書く。
- **Bob and Brad Q2 Mini** — budget 帯の候補。公式は "ultra-quiet even at max speed" と書くが、ページ本文で dB を確認できなかった。
- **Theragun Mini 3rd Gen** — 公式は 1st Gen 比で "quieter" とするが数値なし。※ red-light-therapy-vs-massage-gun で採用済み → 「予算/旅行」ではなく「静かさの比較の基準が自社の旧型」という別の切り口で。
- **Theragun Prime** — 既存2記事で採用済み。本文で「既存記事で扱った機種は静音の数値を公表していない」と一言触れる程度(リンクで既存記事へ)。

---

## 記事設計

### タイトル案
1. **Quiet Massage Gun for Apartments: 3 Picks Compared by Noise, Weight, and Battery**(推奨・約78字→長い場合は下)
2. **Quiet Massage Gun for Apartments: What the Noise Specs Actually Tell You**(約70字)
3. **Quietest Massage Gun for Apartments? 3 Low-Noise Picks Compared**(約63字・補助語も含む)

→ 推奨は 3(60字前後、主検索語 "quiet massage gun" と補助語を自然に含み、"quietest" は疑問形で断定を避ける)。マーケター案の "Won't Wake the Household" は効果の断定に近いので使わない。

### メタディスクリプション案
"Looking for a quiet massage gun for an apartment? We compare three low-noise picks by published decibel ranges, weight, battery, and attachments, and explain what dB specs leave out."(約150字)

### 想定語数
2,300〜2,700 語

### H1 直下(導入・約150語)
- 場面: 夜10時、隣室で家族が寝ている/薄い壁の向こうに隣人。マッサージガンの「ドドド」という音と、床や壁に伝わる振動が気になる。
- この記事でわかること: (1) マッサージガンの音は「空気を通る音」と「床・壁・ベッドを伝わる振動」の2種類、(2) 公表 dB の読み方と限界、(3) 3機種の比較、(4) 置き場所・速度・ヘッドで音を抑える工夫。
- 開示文(アフィリエイト+医療免責+メーカー仕様に基づく・未使用)を冒頭に。

## 見出し構成(H2/H3)

1. **H2: Why Massage Guns Are Loud in an Apartment**(なぜうるさく感じるか)
   - H3: Two Kinds of Noise: The Buzz You Hear and the Thump That Travels(空気音と、床・壁・ベッドを伝わる振動)
     - 振動は「固体を伝わる音」で、足音と同じく壁や床を通って届きやすい、という一般論に留める。white-noise-machine-for-apartment-noise の Footsteps 節へ内部リンク
   - H3: What Changes the Sound: Speed, Pressure, Attachment, and Surface(速度・押し付け・ヘッド・下にある物で音が変わる)
     - 断定せず "may" で。数値は出さない
2. **H2: How to Read a Massage Gun's Decibel Rating**(dB 表示の読み方)
   - H3: Few Brands Publish a Number(数値を載せている会社は少ない:今回確認した中では Ekrin のみ。Therabody・Hyperice は "whisper-quiet" "QuietGlide" 等の表現のみ)
   - H3: Why a Range Like "35–55 dB" Isn't a Promise(範囲の下限は低速時の可能性が高いが、測定条件は非公開。他社と比べられない。家の環境で同じ音になるとは限らない)
   - ※ ここに Pinterest 化しやすい「Spec checklist」(箇条書き5項目: published dB? / weight / battery / soft attachment included? / amplitude)を置く
3. **H2: Quiet Massage Guns Compared**(比較表 ← ここで明示)
   - 比較表の列: | Model | Noise claim (as published) | Weight | Battery (as published) | Speeds | Attachments | Amplitude (if published) | Warranty | Price tier | Best for | May not suit |
   - 行: Ekrin B37 / Ekrin Bantam / Theragun Relief(Also Looked At は表に入れない)
   - 表の下に注記: 「Noise claim は各社の表現をそのまま。dB は Ekrin の公表範囲で、測定条件は非公開。数値が無い機種が静かでないという意味ではない」
   - 価格帯(暫定・人間確認): B37 = mid-range(上側。premium 寄りなら修正)/ Bantam = mid-range / Relief = mid-range
   - CTA ボックス(3機種まとめ)を表の直後に
4. **H2: The 3 Picks**
   - H3: **Ekrin B37 — A Full-Size Gun With a Published Noise Range**
     - What it's for / 35–55 dB(公表範囲・条件非公開)/ 2.2 lbs で3機種中いちばん重い / up to 8 hours / 5 speeds / 4 heads / Lifetime Warranty / 10 Min. Intelligent Stop
     - Who it may not suit(箇条書き3〜4): 重さが気になる人、ソフトなクッション型ヘッドがほしい人(B37 の公式比較表では cushion なし)、数値の測定条件を知りたい人、上の階・薄い床で振動が心配な人
     - CTA
   - H3: **Ekrin Bantam — Compact, Light, Also With a Published Range**
     - 35–58 dB(上限は B37 より高い表記)/ 1.1 lbs / up to 6 hours / 3 speeds / 4 heads / Lifetime Warranty / travel case
     - Who it may not suit: 細かく速度を変えたい人(3段階)、上限値の数字を気にする人、大きい筋肉群を長時間当てたい人(断定せず「フルサイズを好む人」)
     - CTA
   - H3: **Theragun Relief — Gentler 10mm Stroke and One-Button Control**
     - Therabody は dB を公表せず "Whisper-quiet" とうたう、と正直に書く / 10mm amplitude(公式 "Comfortable 10mm")/ 1.37 lbs / around 120 minutes / 3 speeds / 3 heads(Dampener 含む)/ USB-C
     - 振り幅が小さい=打つ動きが控えめ、までに留める(静かさとの因果は断定しない)
     - Who it may not suit: 公表値で比べたい人、強い刺激を求める人(断定せず "people who prefer a stronger stroke")、長い電池が必要な人(3機種中最短)
     - CTA
5. **H2: Also Looked At**(Hypervolt Go 2 / Bob and Brad Q2 Mini / Theragun Mini 3rd Gen、各2〜3文。外した理由=公式で dB を確認できなかった、など。Theragun Prime は既存記事へのリンクで一言)
6. **H2: How to Keep the Noise Down at Night**(使い方で音を抑える工夫・効果は断定しない)
   - H3: Start on the Lowest Speed and a Soft Attachment
   - H3: Mind What's Underneath You(ベッドフレーム・ヘッドボード・硬い床・共有壁に体を預けない。ラグやヨガマットの上、共有壁から離れた場所)
   - H3: Pick Your Timing and Tell the Household(寝入りばなを避ける/家族・同居人と時間を決める。集合住宅の quiet hours は建物ごとに違うので確認を、程度)
   - H3: If the Sound Still Bothers Someone(相手側の対策として white-noise-machine-for-apartment-noise、sleep-earbuds-vs-earplugs-snoring-partner へリンク)
7. **H2: Who a Quiet Massage Gun Isn't For**(向いていない人)
   - 完全な無音が必要な人(公表値でも無音ではない)
   - 上の階に住んでいて床への振動が一番の心配な人(静音モデルでも振動は伝わる可能性)
   - 強い刺激・深い圧を最優先する人
   - 痛み・ケガ・持病がある人 → 医師に相談(下の安全節へ)
   - 手で持つのが負担な人(重さ・握り)→ shiatsu-back-massager-office-chair-desk-workers へ(座って使う別の選択肢として)
8. **H2: Safety Notes**(短く・医療免責)
   - 「情報提供であり医療アドバイスではない」/ メーカーの注意書きに従う / 骨・関節・首の前側・ケガや腫れのある所に当てない旨はメーカー取説の一般的注意として "check the manual" 形式で / 妊娠中・血栓・心臓の持病・ペースメーカー等がある人は使う前に医師へ(categories.json の recovery intro と表現を揃える)
   - 断定語(always / never / guaranteed)を使わない
9. **H2: FAQ**(5問、各2〜4文)
   - What is the quietest massage gun?(公表値の条件が違うので一つに決められない。今回見た中で公表範囲を出しているのは Ekrin、と事実のみ)
   - Is 55 dB quiet enough to use while someone is sleeping?(dB の一般的な目安と、部屋・距離・振動で変わること。「起きない」とは書かない)
   - Are mini massage guns quieter than full-size ones?(公表値からは一概に言えない。Bantam の上限は B37 より高い表記、という事実で答える)
   - Can neighbors hear a massage gun through the wall or floor?(振動として伝わる可能性。工夫の節へ)
   - Why does my massage gun get louder over time?(Therabody FAQ に「音が大きくなったら QuietForce Solution を軸に1滴」という手入れ記載あり → 各社取説の手入れに従う、と一般化)
10. **H2: Which Quiet Massage Gun Fits Your Home?**(まとめ/次のアクション)
    - 数字で比べたい+フルサイズ → B37 / 軽さ・持ち運び+数字 → Bantam / 打つ強さ控えめ・操作が簡単 → Relief
    - 最後の CTA ボックス(3機種)

## アフィリエイトリンク配置ポイント
- ASP: Amazon Associates US のみ(tag=quietrecover-20)。Therabody・Hyperice・Ekrin の直販プログラムは未承認なので使わない(承認後に検討)
- CTA の位置: (1) 比較表の直後(3機種まとめ)、(2) 各 Pick の H3 末尾(1つずつ)、(3) まとめ節の末尾(3機種)。Also Looked At は CTA ボックスにせず本文中のテキストリンクに留める(任意)
- リンク属性: `rel="nofollow sponsored" target="_blank"`、文言は "Check ... on Amazon"(価格を示唆する "Check Price" は既存記事にあるが、今回は "See/Check [商品名] on Amazon" に統一)
- Amazon 検索リンク(検索語):
  - Ekrin B37: `https://www.amazon.com/s?k=Ekrin+B37+massage+gun&tag=quietrecover-20`
  - Ekrin Bantam: `https://www.amazon.com/s?k=Ekrin+Bantam+massage+gun&tag=quietrecover-20`
  - Theragun Relief: `https://www.amazon.com/s?k=Theragun+Relief&tag=quietrecover-20`
  - (Also Looked At)Hypervolt Go 2: `https://www.amazon.com/s?k=Hypervolt+Go+2&tag=quietrecover-20`
  - (Also Looked At)Bob and Brad Q2 Mini: `https://www.amazon.com/s?k=Bob+and+Brad+Q2+Mini+massage+gun&tag=quietrecover-20`
  - (Also Looked At)Theragun Mini 3rd Gen: `https://www.amazon.com/s?k=Theragun+Mini+3rd+Gen&tag=quietrecover-20`
- 公式ページへの出典リンク(dB・仕様の根拠)は本文中に通常リンクで置いてよい(アフィリエイトではないので sponsored 不要)

## 内部リンク候補(すべて公開済みを確認: publishAt または date が 2026-11-23 より前)
記法は必ず `{{ '/posts/xxx/' | url }}`。
- `white-noise-machine-for-apartment-noise`(2026-11-19 公開)— 「振動・足音は伝わりやすい」節、と「音が気になる側の対策」節から
- `massage-gun-vs-compression-boots-recovery`(2026-08-08)— Also Looked At の Theragun Prime から/マッサージガンとは何か
- `red-light-therapy-vs-massage-gun`(2026-09-05)— Theragun Mini の言及から
- `2026-recovery-sleep-gift-guide-by-recipient`(2026-09-19)— Hypervolt Go 2 の言及から(任意)
- `sleep-earbuds-vs-earplugs-snoring-partner`(2026-10-15)— 寝ている側の対策(任意)
- `shiatsu-back-massager-office-chair-desk-workers`(2026-10-22)— 「向いていない人」:手で持たない選択肢(任意)
- 使わない: `heated-seat-massager-for-back`(下書き・見送り中)

## 人間確認リスト(公開前に必須)
1. Amazon で Ekrin B37 / Ekrin Bantam / Theragun Relief が扱われているか、評価(4.0以上か)とレビュー件数(100件以上か)→ 採点の確定
2. 3機種の Amazon 上の価格帯 → budget / mid-range / premium の割り当て確定(B37 を premium にするか)
3. Theragun Relief の US 公式ページ(https://www.therabody.com/us/en-us/theragun-relief.html)で重さ 1.37 lbs・電池 around 120 minutes・"Whisper-quiet" の記載を確認(今回は 429 で本文を取れず、Therabody の英語版FAQで確認)
4. Ekrin の dB 範囲が個別商品ページ(B37 は 429 で取得不可)でも同じか
5. Bob and Brad Q2 Mini の 40–50 dB が公式ページ上にあるか(画像内の可能性)。確認できれば Also Looked At で「公表値」として書いてよい
6. Theragun Mini 3rd Gen の重さ・電池(0.4kg/150分 と 0.45kg/120分の食い違い)— Also Looked At で数値を出すなら確認、出さないなら不要
7. categories.json の `posts` に本記事を追加するか

## 判断基準の自己チェック
- 1記事1メインキーワード: quiet massage gun(補助語はタイトルとH2/FAQで自然に)✓
- 画像化しやすい要素: 比較表+ "Spec checklist" ✓
- 見出しで効能を断定しない: "Why ... Loud" "How to Read" "Isn't For" 型のみ ✓
- 向いていない人・医療免責・FAQ ✓
- 金額・セール名・値引き・送料なし ✓
