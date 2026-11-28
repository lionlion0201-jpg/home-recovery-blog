# 03. アーキテクト設計図: light-therapy-lamp-vs-sunrise-alarm-clock(2026-11-28)

インプット: docs/agents/architect.md、共通ルール(rule of foreign affiliate.md)、02_marketer.md「2」、見本 03_architect_1.md、内部リンク候補 sunrise-alarm-clocks-wake-up-light-comparison(全文)/ blackout-curtains-sleep-masks-for-day-sleepers / magnesium-glycinate-sleep-shift-workers / white-noise-machine-for-day-sleepers、src/_data/categories.json

- スラッグ: `light-therapy-lamp-vs-sunrise-alarm-clock` / テーマ: sleep-environment(front matter は `category: Sleep`。**categories.json の posts には未登録** → 公開作業時に1行追加。アーキテクトは編集しない)
- 読者: 冬、起きる時間にまだ外が暗い人。「光療法ランプ(light box)」と「光で起こす目覚まし」のどちらを買うべきか迷っている人。**病気の治療を探している人向けの記事にはしない**(その人は医師へ、と明記)
- 記事の軸: **「明るさの桁が違う、別の道具」**。目覚まし=起きる瞬間の光(Philips 公表 最大 300 lux)/ランプ=起きた後に座って浴びる強い光(10,000 lux、ただし「何インチで」かが製品ごとに違う)。ランプは「朝の明るさの環境づくり」として扱う
- 本文は書かない。リポジトリのファイルはこの設計図以外変更していない

---

## 0. 調査で分かった前提(ライターが最初に読むこと)

1. **Amazon は開いていない。** 取り扱い・評価・レビュー数・現行の出品名はすべて人間確認。スコアの「レビュー」は全商品「仮に1点」。
2. **verilux.com・carex.com・lumie.com は自動取得が 429(アクセス制限)で本文を読めなかった。** 製品ページの仕様は**そのドメインに限定した検索結果の抜粋**で確認した。代わりに以下は本文を確認できた:
   - **Verilux HappyLight Luxe(VT43)の説明書 PDF**(Douglas College 図書館が置いている Verilux 発行の版。2019年作成、英仏併記)→ 注意事項・明るさ段階・色温度・タイマー・距離を本文で確認
   - **Alaska Northern Lights の製品ページと NorthStar 10,000 ユーザーガイド PDF**(公式ドメイン)
   - **Philips HF3520/60 の公式リーフレット PDF**(documents.philips.com、発行日 2026-01-15)と usa.philips.com の製品ページ
   - **NIMH の SAD ページ**(本文確認)
3. **Mayo Clinic は 403 で本文を読めなかった。** 使う記述はすべて mayoclinic.org の検索抜粋。**ファクトチェックで本文を目視確認すること**(下の「健康面の出典」に要確認として印を付けた)。
4. **「10,000 lux」は距離とセットでないと比べられない(この記事の核)。** 確認できた値:
   - Verilux Luxe: **10,000 lux は 6 インチ(約15cm)での値**(説明書「photopic measurement at 6"」)。説明書の使い方は「顔から 6〜24 インチ」。明るさは 2,500 / 5,000 / 7,500 / 10,000 lux の4段階
   - Carex Day-Light Classic Plus: **10,000 lux at 12–14"**(carex.com 抜粋)
   - Alaska Northern Lights NorthStar 10,000: **10,000 lux at 24"**(公式ページ本文)。ガイドは「最初の週は約40インチ(2,500 lux)で15分から」
   - Philips 目覚まし HF3520: **最大 300 lux**(距離の記載なし)
   - → 同じ「10,000 lux」でも、Verilux は顔のすぐ近く、NorthStar は約60cm離れた位置の値。Alaska Northern Lights も「距離を書いていない 10,000 lux 表示に注意」と書いている(メーカーの主張として扱う)
5. **メーカーの効能・安全の宣伝文句は使わない。** 見つかったもの: Verilux「lift spirits」「feel an improvement in your mood」、Alaska Northern Lights「completely safe」「Doctor Recommended」「Medical Grade」「Proven Light Therapy Aid」、Philips「clinically proven」「improves your mood」、Carex「improving mood」。**一切引用しない・言い換えもしない。**
6. **FDA について:** 「FDA 承認の医療機器ではない」と言い切れる公式情報(FDA 自身の文書)は**確認できなかった**。書けるのは次の2つだけ:
   - Mayo Clinic(検索抜粋・要目視): light box は SAD の治療用として FDA の規制を受けていない
   - Alaska Northern Lights の製品ページ: 自社製品は FDA の評価を受けておらず、一般的なウェルネス用途であり病気の診断・治療を目的としない(メーカー自身の免責)
   → 記事では「Mayo Clinic notes that light boxes aren't regulated by the FDA for SAD treatment」を1回(出典つき)。**「FDA-approved ではない」「FDA cleared」等の言い方は使わない**
7. **Philips の光療法ランプ(goLITE BLU)は usa.philips.com で各型番が「Discontinued」表示。** 候補から外した。Philips は目覚まし側(SmartSleep)だけ扱う
8. **既存記事との重複:** sunrise-alarm-clocks 記事は Hatch Restore・Philips SmartSleep・Lumie Bodyclock を「起こし方」「パートナー」「アプリの有無」で比較済み。white-noise-for-day-sleepers 記事は Hatch Restore 3 を推奨済み。→ **本記事の目覚まし側は Philips HF3520 を1つだけ、明るさ(300 lux)とボタン操作の事実だけ書き、他の比較は sunrise 記事へ送る。** Hatch・Lumie Bodyclock は本文で比較しない(1文で「他の目覚ましはこちら」とリンク)

---

## 商品候補スコアリング(比較記事の場合)

**採点は暫定。** 「レビュー」は Amazon を見られないため全商品「仮に1点」。「紹介料」は価格帯からの相対的な推測(金額は書かない)。

| 商品 | 種類 | 検索意図 | 紹介料 | レビュー(仮) | 伝えやすさ | 比較軸 | 合計 |
|---|---|---|---|---|---|---|---|
| Carex Day-Light Classic Plus(CCFDL93011) | ランプ(据え置き・大画面) | 2 | 2 | 1 | 2 | 2 | **9/10** |
| Verilux HappyLight Luxe(VT43) | ランプ(薄型・卓上/壁掛け) | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Alaska Northern Lights NorthStar 10,000 | ランプ(大型ボックス) | 2 | 2 | 1 | 1 | 2 | **8/10** |
| Philips SmartSleep Wake-up Light(HF3520/60) | 光目覚まし | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Lumie Vitamin L | ランプ(小型) | 2 | 1 | 1 | 1 | 1 | 6/10 |
| Verilux HappyLight Lumi Plus | ランプ(小型) | 2 | 0 | 1 | 2 | 1 | 6/10 |
| Northern Light Technologies Boxelite | ランプ | 2 | 2 | 1 | 1 | 0 | 6/10 |
| Hatch Restore 3 | 光目覚まし(アプリ) | 1 | 2 | 1 | 1 | 1 | 6/10 |
| Lumie Bodyclock Shine 300 | 光目覚まし | 1 | 1 | 1 | 1 | 1 | 5/10 |
| Philips goLITE BLU | ランプ(小型) | — | — | — | — | — | 対象外(公式で Discontinued) |

採点の理由(要点):
- **Carex Classic Plus:** 公式抜粋で 10,000 lux at 12–14"/10,000 lux(therapy)と 5,000 lux(task)の2段階/4000K・CRI 85/画面 16"×13"/高さ 22〜31" 調整・角度調整/9.35 lbs。「上から斜めに当てる大きな画面」で画像にしやすい。価格帯が高めで紹介料2
- **Verilux Luxe:** 説明書で4段階(2,500〜10,000 lux)・3色温度(3,500K / 4,250K / 5,000K)・タイマー(ワンタッチ1時間、5分刻み)・壁掛け可・ETL Listed(米国・カナダ)。軸が最も多い。ただし 10,000 lux は 6" の値
- **NorthStar 10,000:** 公式で 10,000 lux at 24"(採用3つで最も遠い)/蛍光管2本・4100K・CRI 84/10 lbs/12.5"H×22.5"L×4.5"W/明るさ段階・タイマーの記載なし/電球は3年で交換を勧める(ガイド)。「離れて座れる」が独自の軸。見た目が箱で変化を伝えにくい → 伝えやすさ1。**直販中心で Amazon に出ているか不明**
- **Philips HF3520:** 公式リーフレットで最大 300 lux・20段階・日の出 20〜40分で調整・赤→橙→黄・音5種+FMラジオ・アプリ操作なし(本体ボタン)・タップでスヌーズ(9分)・UV-free。ランプとの「桁の違い」を示す比較相手として最適
- **Lumie Vitamin L:** 公式抜粋で 10,000 lux at 20cm(5,000 at 30cm / 2,500 at 50cm)・UV-free LED・明るさ固定・小型(28×20×8cm、0.83kg)。英国・EU の医療機器認証の記載あり(米国の話ではないので記事では使わない)。調整できる軸が少ない → 比較軸1。米国 Amazon での流通は不明
- **Verilux Lumi Plus:** 公式抜粋で3段階・タイマー(15分刻み、最大1時間)・色調整なし・9"×5.6"。公式で「入荷通知」表示=在庫切れの可能性。低価格帯
- **Boxelite:** 10,000 lux の距離が販売店ごとに 14"/17"/18" と食い違い、公式仕様を確認できず → 比較軸0
- **Hatch Restore 3:** 既存2記事で推奨済み。アプリ前提で「暗い朝の明るさ」比較の軸が弱い。明るさ(lux)未確認
- **Lumie Bodyclock Shine 300:** 公式で日の出 15〜90分・明るさ1〜20段階。**lux 値は公式で確認できず**(名前の 300 を lux として書かない)

### 採用(7点以上)
1. **Carex Day-Light Classic Plus** — ランプ枠「机で、上から斜めに当てる大きな画面」(mid-range〜premium、人間判断)
2. **Verilux HappyLight Luxe** — ランプ枠「薄くて置き場所を選ばない。明るさ4段階・色3種・タイマー」(budget〜mid-range、人間判断)。**条件:** 10,000 lux は 6" の値である点を必ず書く
3. **Alaska Northern Lights NorthStar 10,000** — ランプ枠「24" 離れて 10,000 lux。朝食や身支度をしながら」(premium)。**条件:** Amazon で現行品が見つからなければ下の差し替え先へ
4. **Philips SmartSleep Wake-up Light(HF3520)** — 目覚まし枠を1つだけ「起きる瞬間の光。最大 300 lux」(mid-range)。詳しい比較は sunrise 記事へ

※ ランプ3+目覚まし1。語数が上限 2,800 を超えそうなら、**NorthStar を Also Looked At に下げてランプ2つにしてよい**(ライター判断)。

### 差し替え先(Amazon で見つからない・型番がずれる場合)
7点以上の残りが無いため、差し替え先は「Amazon のレビューが評価4.0以上かつ100件以上ならレビュー2点 → 7点に上がる商品」を条件付きで指定する。条件を満たさなければ**差し替えずに商品数を減らす**。

| 採用商品 | 1番目の差し替え先 | 2番目 | 判断のしかた |
|---|---|---|---|
| Carex Day-Light Classic Plus | **Lumie Vitamin L**(条件: Amazon US で現行品+レビュー条件を満たす) | 差し替えず、ランプ2つにする | Carex は Classic Plus のほか Day-Light Sky・Elite・SunLite などが並ぶ。**名前が似た別モデルに置き換えない**(仕様を確認していない)。出品名に "Classic Plus" と型番 CCFDL93011 があるか確認 |
| Verilux HappyLight Luxe | **Verilux HappyLight Lumi Plus**(条件: 同上+在庫あり。比較表の色温度は「調整なし」、タイマーは15分刻み) | Lumie Vitamin L(同条件) | Verilux は Lumi / Lucent / Touch / Alba / Halo など似た名前が多い。出品名に "Luxe" と型番 VT43(色違い VT43WW3・VT43MB3・VT43CG3)があるか確認 |
| Alaska Northern Lights NorthStar 10,000 | **差し替えず、ランプ2つにする**(Also Looked At に1文で残す。リンクなし) | — | Boxelite は「離れて使える」軸の代わりになりそうだが、距離の公式値を確認できていないので使わない。NorthStar を外したら H2「距離」の節は Verilux と Carex の2つで書く |
| Philips SmartSleep HF3520 | **既存 sunrise 記事と同じ Philips SmartSleep Wake-up Light 系の検索リンク**に戻す(300 lux・20段階など HF3520 固有の数字は書かない) | 目覚まし側の商品を置かず、sunrise 記事へのリンクだけにする | Philips は HF3505・HF3650(Somneo)など型番が多く仕様が違う。出品名に HF3520 があるか確認 |

### Also Looked At(本文では1〜2文ずつ。確認できた事実だけ。リンクは付けない)
- **Lumie Vitamin L** — 小型。公式で 10,000 lux は 20cm での値、30cm で 5,000、50cm で 2,500。明るさは固定(差し替えに使わない場合のみ)
- **Verilux HappyLight Lumi Plus** — 小型で明るさ3段階とタイマー。色の調整はない。公式で在庫切れ表示のことがある
- **Philips goLITE BLU** — Philips の米国サイトで販売終了の表示。中古・在庫品に注意、とまでは書かない(推測になる)。「Philips's US site lists it as discontinued」だけ
- **Hatch Restore 3 / Lumie Bodyclock** — 目覚まし側。sunrise 記事で比較済み、の1文でリンク(ここだけ内部リンク可)

---

## 公式で確認できた仕様(出典つき)

### Carex Day-Light Classic Plus(CCFDL93011)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | carex.com に製品ページあり。在庫は未確認 | https://carex.com/products/carex-day-light-classic-plus-light-therapy-sun-lamp(検索抜粋のみ。直接取得は 429) |
| lux と距離 | 10,000 lux at 12–14" | 同上 |
| 明るさ段階 | 2段階(10,000 lux therapy / 5,000 lux task) | 同上 |
| UV | 公式内で食い違い(「UV Protection: 100%」と「blocks 99.3% of UV」)→ **記事は「Carex says it's UV-filtered」まで。% は書かない** | 同上・コレクションページ抜粋 |
| 色温度 | 4000K(CRI 85) | 同上 |
| タイマー | **未確認**(公式抜粋に記載なし。記事では「Carex doesn't list a timer」と書かず「we couldn't confirm a timer」) | — |
| 画面・サイズ・重さ | 画面 16"×13"/本体 31.12"×15.75"×12"/高さ 22〜31" 調整/角度 15〜180°/9.35 lbs | 同上 |
| 光源 | **未確認**(LED と書く資料と蛍光管と書く資料がある。書かない) | — |
| 使い方の注意 | **公式の説明書は入手できず。** manuals.plus に「Carex 説明書」とする PDF があり、眼の病気(緑内障・白内障・網膜の病気)、皮膚の病気、光に敏感になる薬(一部の抗うつ薬・抗精神病薬・抗生物質)の人は使用前に医療者へ、とある。**ただし第三者サイトが作成した文書(作成日 2026-11-26)で、Carex 発行か確認できない → 記事では使わない** | https://manuals.plus/asin/B00PCN4UVU(参考のみ) |

### Verilux HappyLight Luxe(VT43)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | verilux.com に製品ページあり(色違い: White・Marble・Champagne Gold)。在庫は未確認 | https://verilux.com/products/happylight-luxe(検索抜粋のみ。直接取得は 429) |
| lux と距離 | 最大 10,000 lux。**「10,000 lux (photopic measurement) at 6"」** | 説明書 p.10 |
| 置く距離(説明書) | 顔から 6〜24 インチ、やや正面から外して置く。直接光を見ない。色付き眼鏡は届く光を減らす | 説明書 p.8 |
| 明るさ段階 | 4段階(2,500 / 5,000 / 7,500 / 10,000 lux) | 説明書 p.6 |
| 色温度 | 3段階: warm white 3,500K / medium white 4,250K / daylight 5,000K | 説明書 p.6 |
| タイマー | ワンタッチで1時間、または5分刻みで設定。一時停止中は1時間で自動消灯 | 説明書 p.6–7 |
| UV | UV-free(製品ページ抜粋) | 製品ページ |
| サイズ・重さ | 11.7"H×7.5"W×0.5"D、2 lbs。スタンド着脱・壁掛け可 | 製品ページ抜粋/説明書 p.4・9 |
| 認証 | ETL Listed in Canada and the USA | 説明書 p.11 |
| 使い方の注意(説明書本文) | 「一部の薬(例: 抗うつ薬)や診断された精神疾患で光に敏感になり、不快感・過活動・軽躁(hypomania)が起こることがある。使用前に医療者に相談」/「眼の持病がある、または加齢黄斑変性などのリスクがある人は使用前に医療者に相談」/「不快を感じたら中止」/初回は約18インチで10分の「プレテスト」、不快なら中止して医師へ/使用中は覆わない・上に物を置かない/調光器・タイマー・人感センサーにつながない | 説明書 p.3・4・9 |
| 出典 | https://library.douglascollege.ca/sites/default/files/2024-07/vt43_man_rev3_web.pdf(PDF 本文確認。Verilux 発行の VT43 説明書を大学図書館が掲載したもの。**改訂版がある可能性 → 「the Luxe manual we read」と書く**) | |

### Alaska Northern Lights NorthStar 10,000
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | 公式に製品ページあり・カート表示あり。**直販中心。Amazon にあるかは人間確認** | https://www.alaskanorthernlights.com/product/north-star-10000/(本文確認) |
| lux と距離 | 10,000 lux at 24" | 同上 |
| 使い始め(ガイド) | 最初の週は約40インチ(2,500 lux)で朝15分、起床から2時間以内。1週間かけて24インチ・30分へ | ユーザーガイド p.9 |
| 明るさ段階・タイマー | **記載なし**(記事では「NorthStar doesn't list brightness settings or a timer」= 公式ページに無い、と書いてよい。距離で調整する道具と説明) | 同上 |
| 光源・色温度 | 蛍光管(broad-spectrum)2本、4100K、CRI 84。電球は3年使ったら交換を勧める(ガイド) | 製品ページ/ガイド FAQ |
| UV | UV-free(公式) | 同上 |
| サイズ・重さ | 12.5"H×22.5"L×4.5"W、10 lbs(ガイドでは 13"×24"×4" と食い違い → **サイズは「about 2 feet wide」程度に留める**)。縦置き・横置き・壁掛け | 製品ページ |
| 使い方の注意(ガイド本文) | 眼の病気がある・家族歴がある人は使用前に眼科医へ/一時的な眼の不調があれば治まるまで使わない/日光を避ける薬を飲んでいる人は薬剤師か医師に確認/夜遅い使用は睡眠に影響しうる/上に物を置かない/電球は熱くなる。※ ガイドの「completely safe」は**使わない** | https://www.alaskanorthernlights.com/wp-content/uploads/pdfs/User-Guide-ANL-North-Star.pdf(PDF 本文確認) |
| FDA の記載 | 製品ページ: FDA の評価を受けていない・一般的なウェルネス用途・診断や治療を目的としない(メーカーの免責) | 製品ページ |
| 双極性障害 | **ガイドに記載なし** | — |

### Philips SmartSleep Wake-up Light(HF3520/60)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | usa.philips.com に販売ページあり(2026年のレビューあり)。在庫は未確認 | https://www.usa.philips.com/c-p/HF3520_60/smartsleep(本文確認) |
| 明るさ | 最大 300 lux、20段階。**距離の記載なし** | 公式リーフレット(発行 2026-01-15)https://www.documents.philips.com/assets/20211230/35c554f242184d17a874ae0e00cf8684.pdf(PDF 本文確認) |
| 日の出 | 20〜40分で調整。赤→橙→黄 | 同上 |
| 夕暮れ(sunset) | あり | 同上 |
| 音 | 自然音5種+FMラジオ。音は約1分半かけて大きくなる | 同上 |
| 操作 | アプリ操作なし(Controlled by App: No)。本体のボタン。タップでスヌーズ(9分)。アラーム2つ | 同上 |
| 表示 | 部屋の明るさで自動調光、4段階 | 同上 |
| UV | UV-free | 同上 |
| サイズ・重さ | 高さ 19.2cm × 直径 19.9cm × 奥行 14.6cm、730g | 同上 |
| 使わない表現 | 「clinically proven」「improves your mood」「Sunset simulation is a light therapy」→ **書かない** | — |

---

## 健康面で使う出典(この記事で使ってよいのはここまで)

| 書いてよいこと | 出典 | 確認状態 |
|---|---|---|
| NIMH は、冬型の SAD に対する光療法を「毎日 10,000 lux の light box の前に約30〜45分、多くは朝起きてすぐ、秋から春まで」と説明している | NIMH「Seasonal Affective Disorder」https://www.nimh.nih.gov/health/publications/seasonal-affective-disorder(Revised 2023, NIH Pub. No. 23-MH-8138) | 本文確認 |
| NIMH: light box は UV を除いている | 同上 | 本文確認 |
| NIMH: 特定の眼の病気がある人、日光への感受性を高める薬を飲んでいる人は、別の治療を使うか医療者の管理下で使う必要があるかもしれない | 同上 | 本文確認 |
| NIMH: 治療の選択肢の利点とリスクを医療者と話すように | 同上 | 本文確認 |
| Mayo Clinic: light box は SAD の治療用として FDA の規制を受けていない/処方なしで買えるが医療者の指導のもとで使うのがよい | https://www.mayoclinic.org/diseases-conditions/seasonal-affective-disorder/in-depth/seasonal-affective-disorder-treatment/art-20048298 | **検索抜粋のみ(403)。要目視** |
| Mayo Clinic: SAD と双極性障害の両方がある人は、使うかどうか・時間帯を医療者とよく相談。急に増やす・長く使いすぎると躁症状を起こすことがある | 同上 | **検索抜粋のみ。要目視** |
| Mayo Clinic: 緑内障・白内障・糖尿病による眼の障害など眼の問題がある人は始める前に眼科医に相談 | 同上 | **検索抜粋のみ。要目視** |
| Mayo Clinic: 皮膚の病気用のランプは主に UV を出し眼を傷めうる。SAD 用は UV をほぼ全て除くもの | 同上 | **検索抜粋のみ。要目視** |
| Mayo Clinic: 一般に 10,000 lux、起床後1時間以内に20〜30分(具体的な距離はメーカーの指示に従う) | 同上 | **検索抜粋のみ。要目視** |
| Verilux 説明書の注意(上表)/NorthStar ガイドの注意(上表) | 各 PDF | 本文確認 |

**双極性障害の注意は「Mayo Clinic(要目視)」と「Verilux 説明書の hypomania の注意」の2つで書く。** NIMH の光療法の節には双極性障害の記載が無いので、NIMH の言葉として書かない。

**書かないこと:**
- 光療法ランプ・光目覚ましが SAD を「治す」「防ぐ」「気分を良くする」「元気が出る」「眠りが良くなる」「体内時計を整える」
- 目覚ましの 300 lux とランプの 10,000 lux を比べて「目覚ましは効かない」「ランプのほうが効く」(効果の比較になる)。**書くのは明るさの数字と使い方の違いだけ**
- NIMH の「30〜45分」「秋から春」を読者への使用指示として書く(「NIMH describes…」と出典の説明として書く。「You should use it for 30 minutes」は不可)
- 「FDA-approved ではない」「FDA cleared」/メーカーの「clinically proven」「completely safe」「Doctor Recommended」「Medical Grade」
- Lumie の英国・EU 医療機器認証(米国読者に誤解を与える)
- 頭痛・眼精疲労の発生率など、二次情報の数字

---

## 記事設計

### タイトル案
1. **Light Therapy Lamp vs. Sunrise Alarm Clock for Dark Mornings**(推奨。60字。主キーワードが先頭)
2. Light Therapy Lamp vs. Sunrise Alarm Clock: Which Do You Need?(62字)
3. Light Therapy Lamp vs. Sunrise Alarm Clock for Dark Winter Mornings(67字。補助語を含むが長め)

→ 推奨は 1。最終判断はディレクター/人間。

- ターゲットキーワード: `light therapy lamp vs sunrise alarm clock`(主)/ `light therapy lamp for dark winter mornings`(補。H2 1か所+導入で自然に1回。詰め込まない)
- メタディスクリプション案(155字):
  "Light therapy lamp vs. sunrise alarm clock for dark winter mornings: brightness, the distance behind 10,000 lux, timers, and who should ask a doctor first."
- 想定語数: **2,200〜2,800 語**
- front matter: `layout: post.njk` / `tags: post` / `category: Sleep` / `publishAt` は人間が決定
- 冒頭の開示文(タイトル直下、導入より前。見本と同じ形):
  "*Disclosure: This post contains affiliate links. If you purchase through one of them, we may earn a commission at no extra cost to you. Not medical advice: this article is for general informational purposes only and is not a substitute for advice from a doctor. Light therapy lamps and sunrise alarm clocks aren't a substitute for medical care. Our picks are based on manufacturer websites, manuals, and published product information. We have not used these products ourselves.*"

### 見出し構成(H2/H3)

1. **導入**(約150語)
   - 場面: 11〜2月、目覚ましが鳴る時間にまだ外が真っ暗。電気をつけても部屋が薄暗く感じる。「光療法ランプ」と「光で起こす目覚まし」が検索で並んで出てくるが、何が違うのか分からない
   - 結論を先に: 「目覚ましは**起きる瞬間**の光(Philips が公表する最大 300 lux)。ランプは**起きた後に座って浴びる**強い光(10,000 lux、ただし何インチの値かは製品ごとに違う)。役割が違うので、両方使う人もいる」
   - 範囲: この記事は道具の違いを比べるもの。気分の落ち込みや眠りの問題が続くなら医師へ(1文。「向いていない人」節へ誘導)
   - 「In a hurry?」CTA ボックス(Carex 1本)

2. **H2: Light Therapy Lamp vs. Sunrise Alarm Clock: The Short Answer**(約200語)
   - 3行の早見(箇条書き):
     - 暗い中で大きな音に起こされるのがつらい → 光目覚まし(Philips HF3520。他は sunrise 記事へ)
     - 起きた後、朝食や机仕事の間に明るい光の前に座る時間を作りたい → 光療法ランプ
     - 両方 → 目覚ましで起きて、ランプを机に置く。**ただし両方必要とは言わない**
   - 「10,000 lux と 300 lux は同じ種類の数字ではない」と1文で予告(次の H2 へ)

3. **H2: What's Actually Different: Brightness, Timing, and Where You Sit**(約400語)
   - H3: **A sunrise alarm brightens the room before you wake** — 日の出は 20〜40分(HF3520)、最大 300 lux、音が後から。寝ている間・起きる瞬間に使うもの。sunrise 記事で詳しく比べている(リンク1回目)
   - H3: **A light therapy lamp is something you sit in front of after you're up** — 目を開けて、光が顔に届く位置に座る。直接見つめない(Verilux 説明書・Carex 公式)。NIMH が説明する SAD の光療法で使われるのはこの種類(NIMH の説明を「describes」で1回。30〜45分・朝・秋から春)
   - H3: **Why the two numbers aren't comparable** — lux は距離で大きく変わる。Lumie の例(20cm で 10,000、50cm で 2,500)は Also Looked At と重なるので、ここでは Verilux の段階表示(2,500〜10,000)か NorthStar の「40インチで 2,500 / 24インチで 10,000」を例に使う。Philips の 300 lux は距離の記載がない、と正直に
   - ※ 効果の比較はしない。「明るさの数字と使う場面が違う」だけ

4. **H2: Light Therapy Lamp vs. Sunrise Alarm Clock, Compared**(比較表。**必須・Pinterest 化する要素**)
   - 表1(種類の比較。5〜6行):
     | | Sunrise alarm clock | Light therapy lamp |
     |---|---|---|
     | When you use it | Before and as you wake up | After you're up, while sitting nearby |
     | How bright (our picks) | Up to 300 lux (Philips HF3520) | 10,000 lux at a stated distance (6" to 24" depending on the model) |
     | Where it sits | Nightstand | Desk, table, or kitchen counter |
     | Wakes you up? | Yes: light, then sound | No alarm |
     | Main thing to check | Sunrise length, sound, buttons vs. app | The distance behind "10,000 lux," size, timer |
     | Check with a doctor first if… | You're light-sensitive or have an eye condition(sunrise 記事と同じ線) | You have an eye condition, take light-sensitizing medication, or have bipolar disorder(NIMH・Mayo・説明書) |
   - 表2(4商品の仕様):
     - 列: Product / Type / 10,000 lux at / Brightness settings / Color temperature / Timer / Size / Price tier / Best for / May not suit
     - Carex Day-Light Classic Plus / lamp / 12–14" / 2 (10,000 and 5,000 lux) / 4000K / Not confirmed / Large: 16"×13" screen, height-adjustable / mid-range〜premium / 机で上から当てたい / 置き場所が狭い人
     - Verilux HappyLight Luxe / lamp / 6" / 4 (2,500–10,000 lux) / 3 settings (3,500K–5,000K) / Yes (1 hour, or 5-minute steps) / Slim: 11.7"×7.5", 2 lbs / budget〜mid-range / 狭い机・壁掛け / 顔から離して使いたい人(離れると暗くなる)
     - Alaska Northern Lights NorthStar 10,000 / lamp / 24" / Not listed (adjust by distance) / 4100K / Not listed / About 2 feet wide, 10 lbs / premium / 離れて座りたい・身支度しながら / 小さいものが欲しい人、電球交換が面倒な人
     - Philips SmartSleep HF3520 / sunrise alarm / — (up to 300 lux; distance not stated) / 20 / Red→orange→yellow sunrise / Sunrise 20–40 min / Bedside: about 7.6" tall / mid-range / 暗い朝に音だけで起きたくない / 起きた後の明るさを求める人
   - 表の下に注記: 価格帯は相対表現/仕様はメーカー公表情報(または説明書)で、出品ページで型番を確認すること/lux は距離で変わる
   - 表の直後に CTA ボックス(4商品まとめ)
   - **比較表の中にはリンクを入れない**

5. **H2: "10,000 Lux" at What Distance? Reading a Light Therapy Lamp Listing**(約300語。補助キーワードを自然に入れる H2 候補: "…for Dark Winter Mornings" を H3 か本文に)
   - チェックリスト形式(画像化しやすい要素2つ目):
     - [ ] 10,000 lux が**何インチでの値か**書いてあるか(Alaska Northern Lights も距離の明記を求めている。メーカーの主張として紹介)
     - [ ] その距離に座れる置き場所があるか(6" は顔のすぐ近く、24" は腕を伸ばしたより少し先)
     - [ ] UV を除いていると書いてあるか(NIMH・Mayo: SAD 用の light box は UV を除く。Mayo: 皮膚病用のランプは別物で UV を出す)
     - [ ] 明るさの段階・タイマーがあるか(段階があれば弱く始められる。Verilux 説明書は弱い設定から始めて上げてよいと説明)
     - [ ] 説明書の注意事項(眼・薬・精神疾患)が書いてあるか、買う前に読めるか
     - [ ] 赤色光パネル(red light therapy)と混同していないか → [red light therapy devices]({{ '/posts/red-light-therapy-devices-for-home/' | url }}) は別の目的の機器、と1文(**既存の赤色光記事にリンクするなら「別物」として。光療法ランプの代わりとして紹介しない**)

6. **H2: The Picks**(各 約220〜280語。目覚ましは約150語)
   - 各商品の型(見本と同じ): **What it's for:** 1行 → 本文 → **Who it may not suit:** 箇条書き2〜4 → CTA ボックス
   - H3: **Carex Day-Light Classic Plus — A Large Screen That Angles Down Over Your Desk**
     - 書くこと: 10,000 lux at 12–14"/2段階(5,000 lux の task 設定)/16"×13" の画面、高さ 22〜31"・角度調整/4000K/タイマーは確認できなかった/UV は「Carex says it's UV-filtered」(% は書かない)/説明書は入手できなかったので、届いたら注意事項を読む
     - 向かない: 机が狭い・持ち運びたい人/タイマーで自動消灯したい人(未確認)/「向いていない人」節の該当者
   - H3: **Verilux HappyLight Luxe — Slim, Adjustable, and Rated Up Close**
     - 書くこと: 4段階(2,500〜10,000)/3色温度/タイマー(1時間・5分刻み)/壁掛け可/ETL Listed/**10,000 lux は 6" での値、説明書は 6〜24" に置くよう説明 → 離れると明るさは下がる**/説明書の注意(薬・精神疾患で光に敏感になり軽躁がありうる → 医療者に相談/眼の持病・黄斑変性のリスク → 医療者に相談/初回は18インチで10分のプレテスト)
     - 向かない: 顔から離して大きな面で当てたい人/調光器やタイマー付きコンセントにつなぎたい人(説明書で不可)
   - H3: **Alaska Northern Lights NorthStar 10,000 — Rated at 24 Inches, for Sitting Farther Back**
     - 書くこと: 10,000 lux at 24"/明るさ段階・タイマーの記載なし(距離で調整する道具)/ガイドの使い始め(40インチ・15分から1週間かけて)は「メーカーのガイドではこう書いている」と紹介。**読者への指示にしない**/蛍光管2本、3年で交換を勧める/約2フィート幅、10 lbs/ガイドの眼の注意・薬の注意/直販中心で Amazon の出品は型番を確認
     - 向かない: 置き場所が小さい人/タイマーや明るさ切り替えが欲しい人/電球交換をしたくない人
   - H3: **Philips SmartSleep Wake-up Light (HF3520) — If What You Want Is a Gentler Wake-Up**(約150語)
     - 書くこと: 最大 300 lux・20段階・日の出 20〜40分・音5種+FM・本体ボタン(アプリなし)・タップでスヌーズ/ランプの代わりではなく「起こし方を変える道具」/他の目覚まし(Hatch・Lumie)とパートナーへの配慮は sunrise 記事で比較(リンク2回目)
     - 向かない: 起きた後の明るい光の時間を作りたい人(それはランプの役割)/アプリで細かく設定したい人(→ sunrise 記事の Hatch)

7. **H2: Light Therapy Lamps We Looked At but Didn't Pick**(約120語)— Also Looked At を各1〜2文。リンクなし(Hatch・Lumie Bodyclock の1文だけ sunrise 記事へのリンク可。ただし sunrise 記事へのリンクは本文全体で最大3回)

8. **H2: Using Both: A Simple Dark-Morning Setup**(約150語)
   - 例: 目覚ましは寝室のナイトスタンド、ランプは朝食のテーブルか机。**「この組み合わせで朝が楽になる」と書かない。** 「置き場所と使う時間が違うので重ならない」という整理だけ
   - 夜遅い時間の使用は睡眠に影響しうる(NorthStar ガイド)。NIMH・Mayo も朝の使用として説明している → 「ランプは朝のもの、と各資料が説明している」
   - ナイトスタンドに置くなら sunrise 記事の「パートナーへの光漏れ」節へ(リンク3回目でも可。3回を超えない)

9. **H2: Who Shouldn't Buy a Light Therapy Lamp (or Should Ask a Doctor First)**(約250語。**必須の「向いていない人」節**)
   - **気分の落ち込みが続く・SAD かもしれないと思う人** → まず医師へ。ランプは診断や治療の代わりではない(NIMH: 治療の選択肢を医療者と話す/Mayo: 医療者の指導のもとで使うのがよい・要目視)
   - **眼の病気がある・リスクがある人**(緑内障・白内障・網膜の病気・糖尿病による眼の障害・黄斑変性のリスク) → 使う前に眼科医・医療者へ(NIMH・Mayo・Verilux 説明書・NorthStar ガイド)
   - **光に敏感になる薬を飲んでいる人** → 使う前に医師・薬剤師へ(NIMH・Verilux 説明書・NorthStar ガイド)
   - **双極性障害の人** → 使うかどうか・時間帯を医療者と相談(Mayo・要目視)。Verilux 説明書も精神疾患による軽躁の可能性に触れている
   - **使って頭痛・眼の不快を感じた人** → 中止(Verilux 説明書「不快なら中止」、プレテストで不快なら医師へ)
   - **夜勤・日中に寝る人** → この記事の「冬の朝」の使い方は当てはまらない。昼に眠る環境づくりは [blackout curtains vs. sleep masks]({{ '/posts/blackout-curtains-sleep-masks-for-day-sleepers/' | url }}) と [white noise machines for day sleepers]({{ '/posts/white-noise-machine-for-day-sleepers/' | url }})。シフト勤務で光を使う時間を決めるのは医療者と(断定しない)
   - **朝、座っている時間がない人** → ランプは前に座る時間が要る。目覚ましだけのほうが合うかもしれない
   - **すでに朝の部屋が明るい人** → 違いは小さいかもしれない

10. **H2: FAQ**(4〜5問)
    - **Can a sunrise alarm clock replace a light therapy lamp?** — 明るさの数字が違う(300 lux 対 10,000 lux at a stated distance)、使う場面も違う。NIMH が説明する SAD の光療法は light box を使うもの。効果の比較はしない。症状があれば医師へ
    - **How far should a light therapy lamp be from your face?** — 製品ごとに違う。Verilux 6〜24"、Carex 12–14"、NorthStar 24"。Mayo は「メーカーの指示に従う」(要目視)。**一般的な数字を勧めない**
    - **Is a light therapy lamp the same as a red light therapy panel?** — 別物。Mayo: 皮膚用のランプは UV を出す(要目視)。赤色光パネルは別の目的(赤色光記事へ。効果は書かない)
    - **When do people use a light therapy lamp?** — NIMH・Mayo は朝の使用として説明。NorthStar ガイドは夜遅い使用が睡眠に影響しうるとしている
    - **Do light therapy lamps need a prescription?** — Mayo: 処方なしで買えるが医療者の指導のもとで使うのがよい/SAD 治療用としての FDA の規制はない(要目視)

11. **H2: Lamp, Sunrise Alarm, or Both?**(まとめ、約150語)
    - 3〜4行の早見(導入の早見と言い回しを変える)
    - 最後の CTA ボックス(4商品)
    - 医療免責(本文末尾):"*This article is for general informational purposes only and is not medical advice. Light therapy lamps and sunrise alarm clocks are not intended to diagnose or treat any condition. If you have ongoing low mood, sleep problems, an eye condition, bipolar disorder, or take medication that increases light sensitivity, talk with a doctor before using a light therapy lamp, and follow your device's manual.*"

### 健康・表現のルール(この記事固有)
- 見出しに "Beat the Winter Blues" "Boost Your Mood" "Fix" "Cure" "Better Mornings" を使わない。"vs." "What's Different" "at What Distance?" "Who Should Ask a Doctor First" 型
- SAD という語は NIMH・Mayo の説明として出すときだけ。「SAD lamp」は検索語として1回使ってよい(商品カテゴリ名として)が、「SAD を治すランプ」の意味にしない
- メーカーの宣伝文句(0-5)は引用・言い換えともに不可
- 「使った」「テストした」は書かない。レビュー数・評価も書かない
- 価格・割引・送料無料・Black Friday などのセール名は書かない(各公式サイトが今セール中だが本文に入れない)。`{% if campaign.phase %}` ブロックも入れない
- 引用は15語未満を1記事で1つまで(NIMH の一文を使うならそれ1つ)。他は言い換え

---

## アフィリエイトリンク配置ポイント
すべて Amazon Associates US(tag=quietrecover-20)、`rel="nofollow sponsored" target="_blank"`、文言は "Check … on Amazon" / "See … on Amazon"。CTA は `<div class="cta-box">...</div>`(既存記事と同じ形)。

| 位置 | 商品 | 検索リンク |
|---|---|---|
| 導入直後「In a hurry?」 | Carex Day-Light Classic Plus | https://www.amazon.com/s?k=Carex+Day-Light+Classic+Plus+light+therapy+lamp&tag=quietrecover-20 |
| 比較表2の直後(4商品まとめ) | 4点 | 下の4本 |
| Pick: Carex の末尾 | Carex Day-Light Classic Plus | https://www.amazon.com/s?k=Carex+Day-Light+Classic+Plus+light+therapy+lamp&tag=quietrecover-20 |
| Pick: Verilux の末尾 | Verilux HappyLight Luxe | https://www.amazon.com/s?k=Verilux+HappyLight+Luxe&tag=quietrecover-20 |
| Pick: NorthStar の末尾 | Alaska Northern Lights NorthStar 10,000 | https://www.amazon.com/s?k=Alaska+Northern+Lights+NorthStar+10000&tag=quietrecover-20 |
| Pick: Philips の末尾 | Philips SmartSleep HF3520 | https://www.amazon.com/s?k=Philips+SmartSleep+Wake-up+Light+HF3520&tag=quietrecover-20 |
| まとめ | 4点(短い一言つき) | 同上 |

差し替え時のリンク(使う場合だけ):
- Lumie Vitamin L: https://www.amazon.com/s?k=Lumie+Vitamin+L+light+therapy+lamp&tag=quietrecover-20
- Verilux HappyLight Lumi Plus: https://www.amazon.com/s?k=Verilux+HappyLight+Lumi+Plus&tag=quietrecover-20
- Philips(HF3520 が出ない場合。既存 sunrise 記事と同じ): https://www.amazon.com/s?k=Philips+SmartSleep+Wake-up+Light&tag=quietrecover-20

- 比較表・チェックリスト・Also Looked At にはリンクを入れない
- ブランド直販(Alaska Northern Lights 直販など)・他 ASP は未承認のため使わない

## 内部リンク候補(すべて公開済みを確認: publishAt が 2026-11-28 より過去、または publishAt 無し)
| リンク先 | 公開日 | 置く場所 | アンカー例 |
|---|---|---|---|
| `/posts/sunrise-alarm-clocks-wake-up-light-comparison/` | 2026-10-07 | H2 3(目覚まし側の説明)、Philips の Pick、Also Looked At or H2 8(パートナーへの光)。**最大3回** | our sunrise alarm clock comparison |
| `/posts/blackout-curtains-sleep-masks-for-day-sleepers/` | 2026-09-25 | 向いていない人(日中に寝る人) | blackout curtains vs. sleep masks for day sleepers |
| `/posts/white-noise-machine-for-day-sleepers/` | 2026-11-25 | 向いていない人(日中に寝る人) | white noise machines for day sleepers |
| `/posts/red-light-therapy-devices-for-home/` | 2026-07-25(publishAt 無し) | H2 5 チェックリスト or FAQ「赤色光とは別物」 | red light therapy devices |
| `/posts/magnesium-glycinate-sleep-shift-workers/` | 2026-07-25(publishAt 無し) | **入れなくてよい**(下の注記)。入れるなら向いていない人(シフト勤務)に1文 | — |

- 記法は必ず `{{ '/posts/xxx/' | url }}`(例: `[our sunrise alarm clock comparison]({{ '/posts/sunrise-alarm-clocks-wake-up-light-comparison/' | url }})`)
- 重複を避けるための線引き:
  - **sunrise-alarm-clocks:** Hatch・Philips・Lumie の機種比較、アプリ/サブスク、パートナーへの配慮、光目覚ましの「向いていない人」はあちら。本記事の目覚まし側は Philips HF3520 の明るさとボタン操作だけ
  - **white-noise-for-day-sleepers:** Hatch Restore 3 はあちらで推奨済み。本記事では推奨しない
  - **blackout-curtains:** 日中に暗くする話はあちら。本記事は冬の朝に明るくする話
- **気づいた点(別作業・人間判断):** magnesium 記事の77行目は「光を時間を決めて浴びる(timed light exposure)」の説明として**赤色光記事**にリンクしている。赤色光パネルは本記事の光療法ランプとは別物なので、公開後にリンク先を本記事へ差し替えるか検討を(アーキテクトは編集しない)
- 逆方向(sunrise 記事の「What We're Not Claiming」付近からこの記事へ)のリンク追加は公開後の別作業

---

## 人間確認(公開前)
1. **Amazon:** 4商品の取り扱い・現行型番・評価・レビュー数(スコアの「レビュー」欄を確定)。特に NorthStar 10,000 が Amazon にあるか(直販中心)、Carex は "Classic Plus"(CCFDL93011)で出るか、Verilux は "Luxe"(VT43)で出るか、Philips は HF3520 で出るか
2. **Mayo Clinic の本文目視:** FDA の規制・双極性障害・眼の病気・皮膚用ランプと UV・時間帯の5点(すべて検索抜粋で確認しただけ)
3. **Carex:** 公式の説明書(注意事項・タイマーの有無・光源が LED か蛍光管か)。確認できなければ本文は「確認できなかった」のまま。manuals.plus の文書は使わない
4. **Verilux:** 現行の Luxe 説明書が今回読んだ版(2019年)と同じ注意事項か
5. タイトル案の最終決定
6. 採点は暫定。人間確認の結果で 7点を割る商品があれば差し替え表に沿って入れ替える(差し替え先は条件付き。満たさなければ商品数を減らす)
7. categories.json の posts に `"light-therapy-lamp-vs-sunrise-alarm-clock": "sleep-environment"` を追加(公開作業時)

## 出典一覧
- NIMH「Seasonal Affective Disorder」: https://www.nimh.nih.gov/health/publications/seasonal-affective-disorder(本文確認、Revised 2023)
- Mayo Clinic「Seasonal affective disorder treatment: Choosing a light box」: https://www.mayoclinic.org/diseases-conditions/seasonal-affective-disorder/in-depth/seasonal-affective-disorder-treatment/art-20048298(検索抜粋のみ。直接取得は 403)
- Verilux HappyLight Luxe 製品ページ: https://verilux.com/products/happylight-luxe(検索抜粋のみ。直接取得は 429)
- Verilux VT43 説明書: https://library.douglascollege.ca/sites/default/files/2024-07/vt43_man_rev3_web.pdf(PDF 本文確認)
- Verilux HappyLight Lumi Plus: https://verilux.com/products/happylight-lumi-plus(検索抜粋のみ)
- Carex Day-Light Classic Plus: https://carex.com/products/carex-day-light-classic-plus-light-therapy-sun-lamp(検索抜粋のみ。直接取得は 429)
- Alaska Northern Lights NorthStar 10,000: https://www.alaskanorthernlights.com/product/north-star-10000/(本文確認)
- NorthStar ユーザーガイド: https://www.alaskanorthernlights.com/wp-content/uploads/pdfs/User-Guide-ANL-North-Star.pdf(PDF 本文確認)
- Philips HF3520/60 製品ページ: https://www.usa.philips.com/c-p/HF3520_60/smartsleep(本文確認)
- Philips HF3520/60 リーフレット: https://www.documents.philips.com/assets/20211230/35c554f242184d17a874ae0e00cf8684.pdf(PDF 本文確認、発行 2026-01-15)
- Philips goLITE BLU(販売終了表示): https://www.usa.philips.com/c-p/HF3431_60/golite-blu-energy-light(検索抜粋)
- Lumie Vitamin L(US): https://www.lumie.com/en-us/products/vitamin-l-us(検索抜粋のみ)
- Lumie Bodyclock Shine 300(US): https://www.lumie.com/en-us/products/bodyclock-shine-300-us(検索抜粋のみ)
- 参考のみ・記事で使わない: manuals.plus の Carex 文書 https://manuals.plus/asin/B00PCN4UVU
