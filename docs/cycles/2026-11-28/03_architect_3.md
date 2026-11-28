# 03. アーキテクト設計図: microwavable-neck-wrap-vs-electric-heating-pad(2026-11-28)

インプット: docs/agents/architect.md、共通ルール(rule of foreign affiliate.md)、02_marketer.md「3」、見本 03_architect_1.md、内部リンク候補 shiatsu-neck-shoulder-massager-desk-tension / shiatsu-back-massager-office-chair-desk-workers(中身確認)、重複確認用の下書き heated-seat-massager-for-back / heated-mattress-pad-vs-electric-blanket(どちらも published: false。リンクしない)

- スラッグ: `microwavable-neck-wrap-vs-electric-heating-pad` / テーマ: recovery(front matter は `category: Recovery`。**categories.json の posts には未登録** → 公開作業時に `"microwavable-neck-wrap-vs-electric-heating-pad": "recovery"` を1行追加。アーキテクトは編集しない)
- 読者: デスクワークの後、首・肩が冷えてこわばる感じがある人。**マッサージ器を買う前に「まず温めるだけ」で足りるかを決めたい人**。揉む機能が欲しい人は shiatsu-neck 記事へ送る
- 本文は書かない。リポジトリのファイルはこの設計図以外変更していない

---

## 0. 調査で分かった前提(ライターが最初に読むこと)

1. **Amazon は開いていない。** 取り扱い・評価・レビュー数・現在の出品名はすべて人間確認。スコアの「レビュー」は全商品「仮に1点」。
2. **メーカー公式サイトの多くが自動取得を拒否した。**
   - sunbeam.com: 403。仕様は **sunbeam.com に限定した検索の抜粋**と、Sunbeam の商品情報配信ページ(sites.salsify.com、本文確認)で確認。sunbeam.ca(カナダ公式)の類似品ページは本文確認。
   - comfytemp.com・carex.com(Bed Buddy の製造元)・pureenrichment.com: Shopify の 429(アクセス過多)が続き、本文は読めなかった。仕様は**各公式ドメインに限定した検索の抜粋**で確認。Comfytemp の商品一覧と説明書ページの本文、K9015 の商品データ(.json)は1回だけ取得できた。
   - warmies.com: Cloudflare の確認画面で止まる(ボット判定)。回避していない。
   - huggaroo.com: SSL エラーで接続できず。
   → **「検索抜粋」で確認した値は、ライターが本文に書く前に人間がメーカーページを目視で照合する**(下の「人間確認」1〜3)。
3. **電子レンジの加熱時間は商品ごとに違う。** Bed Buddy だけでも「ラップ(2個組)」「ネックピロー」「首と手のラップ」「ボディラップ」で時間が全部違う。**記事には採用品の公式の値だけを書き、ほかの商品へ流用しない。** 読者には「手元の商品のラベル・説明書の時間に従う」と必ず添える。
4. **「寝ている間に使わない」は電気パッドについて公的機関とメーカーの両方で確認できた**(CPSC・FDA・Sunbeam)。電子レンジのラップについて「寝ながら使ってよい/だめ」を明記した公式の一文は**見つからなかった** → 記事では「ラップの説明書には睡眠中の記載を確認できなかった。時間とともに冷めるが、最初は熱い。眠くなる場面では使わない」程度に留め、断定しない。
5. **効能の言い回し:** メーカーの商品名・説明には "pain relief" "deep penetrating relief" などが多い。**記事では引用しない。**「温める」「心地よい」「こわばった感じ」の範囲で書く。商品名に含まれる場合も見出しには入れない(例: Sunbeam のカテゴリ名 "Heating Pads for Neck & Shoulder Pain" はアンカーにも使わない)。
6. **Comfytemp の電気パッド(K9015)は公式データで「131°F〜140°F の9段階」「自動オフ 11 通り」**。小売店の掲載では「0.5〜9時間」。温度の下限が他社(110°F など)より高く、タイマーが最長9時間と長い。**睡眠中の使用についての記載は確認できず、説明書 PDF も開けなかった** → 推奨から外し、Also Looked At にも温度・時間の数字は書かない。

---

## 商品候補スコアリング(比較記事の場合)

**採点は暫定。** 「レビュー」は Amazon を見られないため全商品「仮に1点」。「紹介料」は価格帯からの相対的な推測(電子レンジのラップは budget 帯で低め。金額は書かない)。

| 商品 | 種類 | 検索意図 | 紹介料 | レビュー(仮) | 伝えやすさ | 比較軸 | 合計 |
|---|---|---|---|---|---|---|---|
| Sunbeam Neck Renue Heat Wrap(model 700-825-001 / Material 2137638) | 電気(首肩用の形) | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Pure Enrichment PureRelief Neck & Shoulder Heating Pad | 電気(首肩用の形) | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Comfytemp Microwavable Neck & Shoulder Heating Pad(K9306) | 電子レンジ | 2 | 0 | 1 | 2 | 2 | **7/10** |
| Bed Buddy Hot & Cold Wrap(Carex) | 電子レンジ(冷凍も可) | 2 | 0 | 1 | 2 | 2 | **7/10** |
| Sunbeam Renue Heat Wrap(Material 2102255) | 電気(首肩用の形) | 2 | 1 | 1 | 2 | 1 | **7/10** |
| Comfytemp Weighted Neck & Shoulder Heating Pad(K9015) | 電気(加重) | 1 | 1 | 1 | 2 | 2 | **7/10**(推奨しない。理由は下) |
| Warmies Microwavable Neck Wrap | 電子レンジ | 2 | 0 | 1 | 2 | 1 | 6/10 |
| Huggaroo Neck Wrap | 電子レンジ | 2 | 0 | 1 | 2 | 1 | 6/10 |
| Bed Buddy Neck & Hand Wrap | 電子レンジ | 1 | 0 | 1 | 1 | 1 | 4/10 |
| Sharper Image Heated Aromatherapy Neck and Shoulder Wrap(#204232) | 不明(レンジ式と読める) | 1 | 0 | 1 | 1 | 1 | 4/10 |

採点の理由(要点):
- **Sunbeam Neck Renue:** 4段階・2時間で自動オフ・9フィート(108インチ)コード・22×19インチ・後頭部まで覆う高い襟・磁石の留め具と重りつきの端・洗濯機可(コントローラーを外す、冷水・弱水流、完全に乾くまでつながない)・75W。首肩専用の形で「デスクの後」に一番合う。比較軸(段階数・自動オフ・コード・洗濯・形)が全部そろう。
- **PureRelief Neck & Shoulder:** 4段階(110〜140°F)・自動オフ 120分・9フィートコード・14×22インチ・1.6ポンド・磁石の留め具・コントローラーを外して洗濯機可・55W。仕様は Sunbeam と近い → **差し替え先の1番目**。
- **Comfytemp K9306(電子レンジ):** 亜麻仁(linseed)+クレイビーズ(バリエーションによっては小豆も)・2.8ポンドの加重タイプ・**800W で3〜4分/1200W で2〜3分/最大5分を超えない/W数が分からなければ2分から始め、温め直しは前回の半分**・温かさは15〜20分程度(メーカー説明)・冷蔵庫で冷やせる(冷凍の記載なし)・**洗濯不可**(湿らせた布で拭く。水に浸けない・洗濯機不可)。「重みのあるラップ」で電気パッドとの差が分かりやすい。
- **Bed Buddy Hot & Cold Wrap:** 天然の穀物・ハーブ・花の詰め物・**600W 1分15秒/900W 50秒/1200W 37秒、温めた後1分置く**(2個組の公式ページの値)・冷凍庫で数時間冷やせる・拭き取りのみ。「温冷両用・軽い」でもう一方のラップと役割が分かれる。
- **Sunbeam Renue Heat Wrap(旧型):** 4段階・2時間・9フィート・22×14インチ・スプレーで湿らせて moist heat 可(salsify 本文)。ただし sunbeam.com で **Out of Stock** 表示 → 比較軸1、差し替え先2番目。
- **Comfytemp K9015:** 9段階・自動オフ11通り・ガラスビーズで2.6ポンド・コントローラーを外して洗濯機可(.json 本文)。**温度の下限が高く、タイマーが最長9時間(小売店掲載)と「短時間で切る」公的機関の注意と合いにくい。説明書未読** → 検索意図を1点に下げ、推奨しない。
- **Warmies / Huggaroo:** 公式サイトに接続できず、加熱時間は小売店・ブログの情報だけ → 比較軸1。推奨しない。
- **Bed Buddy Neck & Hand Wrap:** 「90秒から始めて20秒ずつ」(公式抜粋)。W数別の時間が無く、手まで伸びる形でデスク後の首肩とは少しずれる → 4点。
- **Sharper Image #204232:** 公式ページの抜粋では加熱方法が読み取れない(電気か電子レンジか公式で確定できない) → 4点。

### 採用(7点以上の上位3件)
1. **Sunbeam Neck Renue Heat Wrap** — 電気パッド枠「コンセントにつないで、段階を選んで、2時間で切れる」(mid-range)
2. **Comfytemp Microwavable Neck & Shoulder Heating Pad(K9306)** — 電子レンジ枠「コードなし・重みで肩に沿う」(budget)
3. **Bed Buddy Hot & Cold Wrap** — 電子レンジ枠「軽い・冷凍して冷やしても使える」(budget)

※ 電気1・ラップ2の構成。理由: 電気の2候補(Sunbeam と PureRelief)は仕様がほぼ同じで比較にならず、ラップ2つは「重い/軽い」「冷蔵/冷凍」で役割が分かれるため。電気側を厚くしたい場合は **PureRelief を4件目に足してよい**(語数上限 2,800 を超えない範囲。ライター判断)。

### 差し替え先(Amazon で見つからない・型番がずれる場合)
| 採用商品 | 1番目の差し替え先 | 2番目 | 判断のしかた |
|---|---|---|---|
| Sunbeam Neck Renue Heat Wrap | **Pure Enrichment PureRelief Neck & Shoulder Heating Pad**(8点) | Sunbeam Renue Heat Wrap(7点。22×14インチの旧型。sunbeam.com では在庫切れ表示) | 検索で「Neck Renue」が出ず「Renue Heat Wrap」「Massaging XL Renue」だけ出る場合も差し替え。**マッサージ(振動)つきの Renue は別商品なので使わない**(揉む・振動は shiatsu-neck 記事の領域) |
| Comfytemp K9306 | **構成を「ラップ1(Bed Buddy)+電気2(Sunbeam+PureRelief)」に変える** | Warmies Microwavable Neck Wrap(6点。**人間がパッケージか公式ページで加熱時間を目視できた場合だけ**。小売店の「60秒/90秒」は使わない) | Comfytemp の 33×4インチの細いラップ(K9305)や 12×23インチの平らなパッド(K9304)は**別商品**。時間も違う(K9304 は3〜5分)ので取り違えない |
| Bed Buddy Hot & Cold Wrap | **構成を「ラップ1(Comfytemp)+電気2(Sunbeam+PureRelief)」に変える** | Bed Buddy Neck & Hand Wrap(4点。7点未満なので**採用はせず**、使うなら Also Looked At に1文だけ) | Amazon で1個売りと2個組のどちらが出ても同じ商品として扱ってよいかは**人間確認**。加熱時間は2個組の公式ページの値。1個売りのページ本文は未読 |

### Also Looked At(本文では短く1〜2文ずつ。確認できた事実だけ。リンクは付けない)
- **Pure Enrichment PureRelief Neck & Shoulder Heating Pad** — 4段階・120分で自動オフ・9フィートコード・コントローラーを外して洗濯機可。Sunbeam と近い仕様の代わりの候補(4件目に採用しない場合のみここに置く)
- **Comfytemp Weighted Neck & Shoulder Heating Pad** — ガラスビーズの重みつきの電気パッド。タイマーを長く設定できるが、説明書を確認できなかったため推奨から外した、と正直に(温度・時間の数字は書かない)
- **Warmies / Huggaroo のレンジ式ラップ** — 人気があるが、メーカーの公式ページで加熱時間を確認できなかったので外した、と1文で

---

## 公式で確認できた仕様(出典つき)

### Sunbeam Neck Renue Heat Wrap
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | sunbeam.com に製品ページあり。在庫は未確認(同じシリーズの Renue Heat Wrap と Renue XL は Out of Stock 表示) | https://www.sunbeam.com/pain-relief/neck-and-shoulder-pain/sunbeam-neck-renue-heat-wrap/SP_615336.html(検索抜粋。直接取得は 403) |
| 加熱方法 | 電気(コンセント) | 同上 |
| 温度段階 | 4段階(押しボタン、LED 表示) | 同上 / https://sites.salsify.com/41c9c255-1884-40e0-bc05-ad8dd5617744/c662aea6-b860-4545-ab16-2118694bf473/en-US/product/SAP_2137638/Sunbeam(r)-Neck-Renue(r)-Heat-Wrap/(本文確認) |
| 自動オフ | 2時間 | 同上(両方) |
| コードの長さ | 9フィート(仕様表では 108インチ) | 同上(両方) |
| 形・大きさ | 22×19インチ、後頭部まで覆う高い襟、磁石の留め具、重りつきの端 | sunbeam.com(検索抜粋)/ salsify(襟の高さ以外は本文確認) |
| 洗えるか | 洗濯機可。コントローラーを外す・冷水・弱水流・完全に乾くまでつながない・漂白剤とドライクリーニング不可 | sunbeam.com(検索抜粋) |
| 中身の素材 | 表地 Micromink。中身(発熱線以外)は**未確認** | sunbeam.com(検索抜粋) |
| 冷やして使えるか | **不可(電気製品のため冷却の記載なし)**。記事では「冷やす用途には使えない」とだけ書く | — |
| 湿らせて使うか(moist heat) | **未確認**(旧型 Renue Heat Wrap は「生地に水をスプレー」の記載あり。Neck Renue では未確認 → 書かない) | salsify SAP_2102255(本文確認、旧型) |
| 説明書 | **未入手**。Sunbeam の他の電気パッドの説明書・FAQ には「寝ている間は使わない」「乳児・動物に使わない」「感覚が鈍い・血行が悪い人は使わない」「糖尿病の人に使わない」とある(下の安全の節) | — |

### Comfytemp Microwavable Neck & Shoulder Heating Pad(K9306)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | comfytemp.com に製品ページあり。商品一覧(本文確認)にも掲載 | https://comfytemp.com/products/comfytemp-neck-shoulder-microwavable-heating-pad(検索抜粋。直接取得は 429)/ 一覧 https://www.comfytemp.com/(本文確認) |
| 加熱方法・時間 | 電子レンジ。**800W: 3〜4分/1200W: 2〜3分/最大5分を超えない/初回や W数不明なら2分から、温め直しは前回の半分の時間** | 同上(検索抜粋)。**本文に書く前に人間が目視照合** |
| 温かさの続く時間 | 15〜20分程度(メーカー説明)。水を吹きかける・タオルで包むと長くなる、とメーカーは書いている → 後者は書かない(効果の誇張になりうる) | 同上 |
| 中身の素材 | 亜麻仁(linseed)とクレイビーズ。バリエーションによっては小豆も | 同上 |
| 重さ | 2.8ポンド(加重タイプ) | 同上 |
| 洗えるか | **洗えない。** 湿らせた布で表面を拭く。手洗い・水に浸ける・洗濯機は不可(FAQ) | 同上 |
| 冷やして使えるか | 冷蔵庫で冷やすと「ひんやり感」(FAQ)。**冷凍は記載なし → 「冷凍」とは書かない** | 同上 |
| 温度段階・自動オフ・コード | 該当なし(電子レンジ式) | — |
| 加熱前の注意(メーカー) | 繰り返し加熱で傷むのを防ぐため、表面に 1〜2ml の水をスプレー(メーカー説明)。→ 書くなら「メーカーの説明どおりに」と添えて1文 | 同上 |

### Bed Buddy Hot & Cold Wrap(Carex)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | carex.com に製品ページあり(1個: bed-buddy-microwaveable-neck-wrap、2個組: bed-buddy-hot-cold-wrap-two-pack)。在庫は未確認 | https://carex.com/products/bed-buddy-microwaveable-neck-wrap(検索結果に表示のみ)/ https://carex.com/products/bed-buddy-hot-cold-wrap-two-pack(検索抜粋。直接取得は 429) |
| 加熱方法・時間 | 電子レンジ。**600W: 1分15秒/900W: 50秒/1200W: 37秒。加熱後1分置く**(moist heat 用の時間として掲載) | 2個組のページ(検索抜粋)。**1個売りページでも同じ値か人間が目視照合** |
| 中身の素材 | 天然の穀物・ハーブ・花(100% natural grains, herbs, and flowers) | 同上 |
| 冷やして使えるか | 冷凍庫で数時間冷やす。温め・冷凍を繰り返せる、とメーカー説明 | 同上 |
| 洗えるか | 湿らせた布で拭く(洗わない) | carex.com(検索抜粋)/ Bed Buddy 説明書(ボディラップ用、下記) |
| 使える部位 | 首・腕・脚・背中(メーカー説明) | 同上 |
| 大きさ・重さ | **未確認** | — |
| 温度段階・自動オフ・コード | 該当なし | — |

### Bed Buddy の説明書(ボディラップ BBF2000 用。PDF 本文確認)
出典: https://cdn.shopify.com/s/files/1/0240/6504/8681/files/BB_BodyWrap_Instructions.pdf(Bed Buddy の説明書 PDF。**このファイルが置かれた Shopify ストアが Carex のものかは照合できていない**。採用品のラップ専用の説明書ではない → 記事では「Bed Buddy's instruction sheet for its body wrap」と書く)
- 加熱時間は商品で違う、過熱しない/**電子レンジのオーブン(convection)機能は使わない**
- 清潔で空の、電子レンジ対応の皿にのせ、平らにして中身を均等に広げる
- **使う前に必ず中身を動かして熱い所がないか触って確かめる**
- もっと温めたい場合は15秒ずつ(※ボディラップの記載。採用品の時間とは別 → 記事では数字を流用しない)
- **食べ物や液体で汚れると過熱し、やけどの原因になる**
- 使っている間は位置を変え続ける/温めたものを目の上にのせない
- 洗わない。湿らせた布で拭いてよく乾かす
- **神経障害・血行の問題・敏感な肌・傷のある肌の人、自分で外せない人(乳児・子ども・一部の高齢者)に使わない**
- 妊娠中・持病がある場合は使う前に医師に相談
- **温めている間、目を離さない**(ボディラップは「合計2分を超えない」とある → 数字は流用しない)

### Comfytemp の安全ページ(電子レンジ式全般)
出典: https://comfytemp.com/blogs/news/how-to-safely-use-microwavable-heating-pad(検索抜粋)
- 手首の内側で温度を確かめる/使うのは15〜20分程度/**焦げたにおいがしたらすぐ取り出す**/温め直す前に室温近くまで冷ます
- → 記事では「メーカーの安全ページの説明」として、においの件と冷ましてから温め直す件を使う

---

## 安全面の公式情報(根拠URLつき)

| 内容 | 出典 | 確認方法 |
|---|---|---|
| **ヒーティングパッドは寝る前に必ず切る。比較的低い設定でも重いやけどの恐れ** | CPSC Publication 701「Safety for Older Consumers – Home Safety Checklist」 https://www.cpsc.gov/s3fs-public/701.pdf | **PDF 本文確認(今回も文字を抽出して確認)**。高齢者向けチェックリスト |
| 電気パッドの使い方: **つけたまま寝ない/1回 15〜20分/最初は一番低い設定/肌との間にタオル/パッドの上に座ったり寝たりしない・自分と椅子やソファ・ベッド・枕の間に挟まない/ほつれ・穴・破れがあれば使わない/火花が出たら使わない** | FDA Safety Communication「Do Not Use Certain Mighty Bliss Electric Heating Pads Due to Risk of Injury」 https://fda.gov/medical-devices/safety-communications/do-not-use-certain-mighty-bliss-electric-heating-pads-due-risk-injury-fda-safety-communication | **検索抜粋のみ**(本文は 404。ページが移動した可能性)→ 人間確認4 |
| **折りたたんで使うと折れた部分の電力密度が上がり、過熱を検知できず熱くなりすぎる**(Navajo Manufacturing の首肩用パッド、Class I リコール、2026-03 発表、重いけが4件) | FDA「Heating Pad Recall: Navajo Manufacturing Company Removes Handy Solutions Neck & Shoulders Heating Pad」 http://www.fda.gov/medical-devices/medical-device-recalls-and-early-alerts/heating-pad-recall-navajo-manufacturing-company-removes-handy-solutions-neck-shoulders-heating-pad | **本文確認**。foot-warmer 記事でも触れている → 本記事では「首肩用の形の電気パッドでも折りたたまない」の根拠として1文だけ。ブランド名は出さなくてよい |
| **電子レンジで温める首用ラップ(スカーフ)の中身が過熱し、火災・やけどの危険**でリコール(Telebrands Therma Scarf、2010-03-10、約98,500台) | CPSC https://www.cpsc.gov/Recalls/2010/telebrands-recalls-scarves-with-microwaveable-heat-packs-due-to-fire-and-burn-hazards | **検索抜粋のみ**(本文は 403)。古いリコールなので「電子レンジ式でも過熱すれば発火しうる、と公的に記録がある」という一般的な根拠に留め、商品名は出さない |
| ヒーティングパッドは同じ場所に長く当てると数時間でやけどしうる/寝落ちが原因になる/高齢者が最もリスクが高い/乳児には使わない/麻痺のある人は熱さに気づけない/折りたたむ・巻き付けるのは危険 | University of Utah Health(熱傷センターの看護管理者)「Heating Pads Can Cause Second-Degree Burns」 https://healthcare.utah.edu/the-scope/health-library/all/2018/11/heating-pads-can-cause-second-degree-burns | **本文確認**(2018-11-23 再掲、初出 2014) |
| Sunbeam の電気パッドの注意: **感覚の鈍い肌・血行が悪い人に使わない/乳児・動物に使わない/眠っている人・意識のない人・糖尿病の人に使わない/パッドの上に寝ない** | Sunbeam ヘルプ・FAQ https://help.sunbeam.com/s/article/CA-Pain-Relief-Buying-Guide?language=en_CA / https://sunbeam.com/service-and-support/product-support/product-faqs/pain-relief/heat-wraps/heating-pads-heat-wraps-faq.html | **検索抜粋のみ**。採用モデル専用の説明書ではない → 「Sunbeam's heating pad safety guidance」と書き、手元の説明書を優先するよう添える |
| Bed Buddy 説明書の注意(上記) | Bed Buddy ボディラップ説明書 PDF | PDF 本文確認 |

使わない情報:
- Cedars-Sinai の記事(本文確認)は「寒い環境ならタオルを挟めば寝ながらでも」と読める箇所があり、CPSC・FDA と食い違う → **使わない**
- MedlinePlus: 該当するページを取得できなかった(Magazine の熱傷の PDF は火・熱い飲み物の話のみ)→ **使わない**。糖尿病の詳しい話は foot-warmer 記事(NIDDK・CDC・MedlinePlus を使用済み)へリンクで送る
- 「低温やけど(low-temperature burn)」という語は公的な出典の文言としては確認できていない → 見出しには使わない。本文で使うなら「長く同じ場所を温めるとやけどしうる(University of Utah Health)」という形で、出典の言い方に合わせる
- 公式ページの「pain relief」「deep penetrating」「promote relaxation」などの効能表現・温度の数字(°F)は記事に書かない

---

## 記事設計

### タイトル案
1. **Microwavable Neck Wrap vs. Electric Heating Pad for Desk Workers**(推奨。64字。主キーワードが先頭、補助語の desk workers も入る)
2. Microwavable Neck Wrap vs. Electric Heating Pad: Which to Choose?(65字)
3. Microwavable Neck Wrap vs. Heating Pad: Warmth After a Desk Day(63字。"Electric" が抜けて主キーワードと完全一致しない)

→ 推奨は 1。最終判断はディレクター/人間。

- ターゲットキーワード: `microwavable neck wrap vs electric heating pad`(主)/ `heated neck wrap for desk workers`(補。導入1回+H2 1か所+FAQ 1問。詰め込まない)
- メタディスクリプション案(約150字):
  "Microwavable neck wrap vs. electric heating pad after a desk day: we compare heating, timers, washing, and what the manuals say about safe use."
- 想定語数: **2,200〜2,800 語**
- front matter: `layout: post.njk` / `tags: post` / `category: Recovery` / `publishAt` は人間が決定
- 冒頭の開示文(foot-warmer・下書きと同じ形):
  "*Disclosure: This post contains affiliate links. If you purchase through one of them, we may earn a commission at no extra cost to you. Not medical advice: this article is for general informational purposes only and is not a substitute for advice from a doctor. Our picks are based on manufacturer websites, manuals, and published product information. We have not used these products ourselves. Your product's manual and safety warnings take priority over anything in this article.*"

### 見出し構成(H2/H3)

1. **導入**(約150語)
   - 場面: 夕方、デスクから立つと首と肩が冷えてこわばった感じがする。部屋の暖房を上げるほどではない。マッサージ器を買う前に「まず温めるだけ」で足りるか試したい
   - 結論を先に: 「電子レンジのラップはコードなしで動ける代わりに温かさが短く、時間は自分で守る。電気パッドは温度を選べて一定に保てる代わりにコンセントの近くで使い、寝る前には切る」
   - この記事の範囲: 温めるだけの道具。揉む機能が欲しい人は shiatsu-neck 記事へ(1文でリンク)
   - 「In a hurry?」CTA ボックス(Sunbeam Neck Renue 1本)

2. **H2: Microwavable Neck Wrap vs. Electric Heating Pad: The Short Answer**(約200語)
   - 3行の早見(箇条書き):
     - 席を立って動き回りたい・コードが邪魔 → 電子レンジのラップ
     - 段階を選びたい・温度をしばらく一定にしたい・洗濯機で洗いたい → 電気パッド
     - 冷やしても使いたい → 冷凍できるラップ(Bed Buddy)。電気パッドは冷やせない
   - 「どちらも温めるための道具で、こわばりの原因を治すものではない」と1文(断定しない言い回し: "Neither is a treatment")

3. **H2: How Each One Heats, and What That Means at Your Desk**(約350語)
   - H3: **A microwavable neck wrap: heat that fades on its own** — 穀物・亜麻仁・クレイビーズなどを温める。加熱時間は商品とレンジの W数で違う(Comfytemp と Bed Buddy の公式の値を例に、**桁が違うほど差がある**ことを示す: Bed Buddy は1分前後、Comfytemp は数分)。温かさは時間とともに下がる(Comfytemp は15〜20分程度と説明)。コードがない
   - H3: **An electric heating pad: steady heat, a cord, and an auto-off** — 段階を選ぶ。採用品は2時間で自動オフ。コンセントの近く・コードの取り回し(9フィート)。デスクで使うなら、椅子の背もたれと自分の間に挟まない(FDA の「自分と椅子の間に置かない」)
   - H3: **Weight and fit on your shoulders** — Comfytemp は2.8ポンドの加重、Sunbeam は重りつきの端と磁石の留め具。Bed Buddy の重さは未確認なので比べない。「重みが心地よいか」は好みとして書く(効果を書かない)

4. **H2: Microwavable Neck Wrap vs. Electric Heating Pad, Compared**(比較表。**必須・Pinterest 化する要素**)
   - 表1(種類の比較。5〜7行):
     | | Microwavable neck wrap | Electric heating pad |
     |---|---|---|
     | How it heats | Microwave, for the time on its label | Plugs into an outlet |
     | Heat over time | Starts warm, cools down on its own | Stays at the setting you pick until auto-off |
     | Settings | None — you control it with heating time | Several heat settings(採用品は4段階) |
     | Cord | None | Yes(採用品は9フィート) |
     | Cold use | Some can go in the fridge or freezer — check the label | No |
     | Washing | Usually wipe clean only(採用2品) | Some are machine washable with the controller removed |
     | Biggest safety habit | Follow the label time, check for hot spots, don't leave it heating unattended | Start low, keep sessions short, turn it off before you sleep |
   - 表2(3商品の仕様):
     - 列: Product / Type / Heating / Heat settings / Auto-off / Fill / Cold use / Washing / Cord / Price tier / Best for / May not suit
     - Sunbeam Neck Renue / electric / outlet / 4 / 2 hours / — / No / Machine wash, controller removed / 9 ft / mid-range / 一定の温かさ・後頭部まで / コードなしで動きたい人
     - Comfytemp K9306 / microwavable / 3–4 min at 800W, 2–3 min at 1200W(max 5 min) / — / — / Flaxseed and clay beads / Fridge(per maker) / Wipe clean only / None / budget / 重みのあるラップが好き / 洗濯機で洗いたい人
     - Bed Buddy Hot & Cold Wrap / microwavable / 1:15 at 600W, 0:50 at 900W, 0:37 at 1200W, then rest 1 min / — / — / Natural grains, herbs, flowers / Freezer / Wipe clean only / None / budget / 温冷どちらも・軽い / 長く温かさを保ちたい人
   - 表の下に注記: 加熱時間はメーカーの公表値。**手元の商品のラベルの時間を優先**。価格帯は相対表現。出品ページで型番を確認
   - 表の直後に CTA ボックス(3商品まとめ)
   - ※ 表2の加熱時間は「人間確認 2・3」で目視照合が取れた値だけ残す。取れなければ「See the label」に置き換える

5. **H2: Heated Neck Wrap for Desk Workers: Using One Safely at Your Desk**(約350語。補助キーワードの H2)
   - **書き方の原則: 説明書と公的機関に書いてあることだけ。推測で「安全」と言わない**
   - H3: **Microwave wraps: time, hot spots, and not walking away** — ラベルの時間どおり/W数の確認(Carex はレンジの W数はドアの内側・背面のラベルか説明書にあると案内)/オーブン機能は使わない/空で清潔な皿/温めている間は目を離さない/取り出したら中身を動かして熱い所を確かめる/食べ物や液体で汚れたものは過熱しうる(以上 Bed Buddy の説明書)/焦げたにおいがしたらすぐ出す・冷めてから温め直す(Comfytemp)/過熱した電子レンジ式の首用ラップが火災・やけどの危険でリコールされた例がある(CPSC、2010。商品名は出さない)
   - H3: **Electric pads: start low, keep it short, keep it off the chair back** — 一番低い設定から/1回 15〜20分/肌との間に布/自分と椅子・ソファの間に挟まない/傷んでいたら使わない(FDA)/折りたたまない(FDA の首肩用パッドのリコール)/自動オフは2時間だが、それまで使い続けてよいという意味ではない(下書き heated-seat の言い回しと重ならないよう表現を変える)
   - H3: **Don't use either one to fall asleep** — 電気パッドは寝る前に必ず切る(CPSC)・つけたまま寝ない(FDA)。電子レンジのラップは説明書に睡眠中の記載を確認できなかった。ただし Bed Buddy は自分で外せない人に使わないとしている → 「眠くなりそうなら使わない」
   - 小さな表にしてもよい: Product / What the maker says about time / Auto-off

6. **H2: The 3 Picks**(各 約250〜300語)
   - 各商品の型(foot-warmer と同じ): **What it's for:** 1行 → 本文 → **Who it may not suit:** 箇条書き3〜4 → CTA ボックス
   - H3: **Sunbeam Neck Renue Heat Wrap — Steady Heat With a Tall Collar**
     - 書くこと: 4段階/2時間の自動オフ/9フィートのコード/22×19インチ・後頭部まで覆う襟/磁石の留め具と重りつきの端/洗濯機可の手順(コントローラーを外す・冷水・弱水流・完全に乾くまでつながない)/説明書は入手できなかったので、注意は Sunbeam のヘルプページの記載として書く
     - 向かない: 席を離れて動きたい人/冷やす用途にも使いたい人/寝る前にベッドで使いたい人(CPSC・FDA)/「向いていない人」節の該当者
     - **"Pain" を含む Sunbeam のカテゴリ名・宣伝文句は引用しない**
   - H3: **Comfytemp Microwavable Neck & Shoulder Heating Pad — A Weighted Wrap With No Cord**
     - 書くこと: 亜麻仁とクレイビーズ/2.8ポンド/800W・1200W 別の時間と最大5分/W数不明なら2分から・温め直しは半分/温かさは15〜20分程度とメーカー説明/冷蔵庫で冷やせる(冷凍とは書かない)/洗えない(拭くだけ)
     - 向かない: 洗濯機で洗いたい人/肩に重さがのるのが苦手な人/職場の電子レンジを使う人(W数が分からない・待つ間に目を離せない、という実用上の注意。説明書の「目を離さない」に結びつける)
   - H3: **Bed Buddy Hot & Cold Wrap — Light, and It Can Go in the Freezer**
     - 書くこと: 天然の穀物・ハーブ・花/600W・900W・1200W 別の時間と1分置く/冷凍庫で数時間/拭くだけ/首・腕・脚・背中に使える(メーカー説明)/大きさ・重さは未確認と正直に
     - 向かない: 温かさを長く保ちたい人(時間は未確認 → 「温め直しが前提」程度に留める)/香りが苦手な人(**ハーブ・花の詰め物と公式にあるが「香り」の有無は未確認** → 書くなら「ハーブと花が入っている」までにして香りの断定はしない)/洗いたい人

7. **H2: Neck Wraps and Heating Pads We Looked At but Didn't Pick**(約120語)— Also Looked At を各1〜2文。リンクなし

8. **H2: Before You Heat It: A Neck Warmth Checklist**(約200語。チェックリスト=画像化しやすい要素2つ目)
   - [ ] ラベルの加熱時間とレンジの W数を確認(Carex・Comfytemp)
   - [ ] オーブン機能を使わない・空で清潔な皿(Bed Buddy)
   - [ ] 温めている間は目を離さない(Bed Buddy)
   - [ ] 使う前に中身を動かして熱い所がないか触って確かめる(Bed Buddy)
   - [ ] 焦げたにおいがしたらすぐ取り出す(Comfytemp)
   - [ ] 電気パッドは一番低い設定から・1回 15〜20分・肌との間に布(FDA)
   - [ ] 電気パッドを折りたたまない・椅子の背もたれとの間に挟まない(FDA)
   - [ ] 眠くなりそうなら使わない。電気パッドは寝る前に切る(CPSC)
   - [ ] cpsc.gov/Recalls でブランドと型番を確認
   - heated-seat 下書きの「Heat Safety」節・shiatsu-back の「Heat Settings」節と項目は一部重なるが、**電子レンジ側の項目(W数・オーブン機能・皿・においの確認)が本記事の独自部分**。電気側の項目は短く

9. **H2: Who Shouldn't Use a Neck Wrap or Heating Pad**(約200語。**必須の「向いていない人」節**)
   - Bed Buddy 説明書: 神経障害・血行の問題・敏感な肌・傷のある肌の人/自分で外せない人(乳児・子ども・一部の高齢者)には使わない/妊娠中・持病がある人は使う前に医師に相談
   - Sunbeam のヘルプ: 感覚が鈍い・血行が悪い人、乳児、眠っている人、糖尿病の人には使わない
   - University of Utah Health: 高齢者はやけどのリスクが最も高い/麻痺のある人は熱さに気づけない
   - 糖尿病で冷えを感じる人は foot-warmer 記事の該当節へリンク(NIDDK・CDC の記載を重ねて書かない)
   - 首を痛めた直後・手術後・強い痛みやしびれがある → 温める前に医師へ(shiatsu-neck の「Who Should Check With a Doctor First」と同じ方向。断定しない)
   - **こういう人には別の道具**(短い箇条書き。下書き heated-seat の "isn't right for" 節と言い回しを変える):
     - 揉む感じが欲しい → shiatsu-neck 記事
     - 肩甲骨の間や腰までこわばる・椅子で使いたい → shiatsu-back 記事
     - 部屋そのものが寒い → quiet space heaters 記事
     - 足だけ冷える → foot-warmer 記事

10. **H2: FAQ**(H3 か太字で4〜5問)
    - **How long should you microwave a neck wrap?** — 商品ごとに違う。採用2品の公式の値を例に出し、ラベルを優先、と書く(推測の「目安」は書かない)
    - **Can you sleep with a heated neck wrap on?** — 電気パッドは寝る前に切る(CPSC)・つけたまま寝ない(FDA)。電子レンジのラップは説明書で睡眠中の記載を確認できなかった。眠くなりそうなら使わない
    - **Is a heated neck wrap good for desk workers?** — 補助キーワード用。「温めると心地よいと感じる人がいる」程度。治療ではない。こわばりが続く・痛みが強いなら医師へ。揉む機能が欲しいなら shiatsu-neck 記事へ
    - **Can you use a microwavable neck wrap cold?** — Bed Buddy は冷凍可、Comfytemp は冷蔵庫(メーカー説明)。電気パッドは不可
    - **Can you wash a microwavable neck wrap?** — 採用2品は洗えず拭くだけ。洗いたいなら洗濯機可の電気パッド(Sunbeam)

11. **H2: Microwavable Neck Wrap or Electric Heating Pad: Which Fits Your Day?**(まとめ、約150語)
    - 3〜4行の早見(導入の早見と言い回しを変える)
    - 「温めても物足りない、揉む感じが欲しい」→ shiatsu-neck 記事へ送る導線(**ここが本記事の出口**。1文+リンク)
    - 最後の CTA ボックス(3商品)
    - 医療免責(本文末尾にも1文):"*This article is for general informational purposes only and is not medical advice. If you have diabetes, reduced feeling in your skin, a circulation condition, a recent neck injury, or are pregnant, talk to your doctor before using heat. Follow your product's label, manual, and safety warnings.*"

### 健康・表現のルール(この記事固有)
- 見出しに "Relief" "Relieves" "Soothes" "Cures" "Fix" "Pain" を使わない。"vs." "Which…?" "What the Manuals Say" 型
- 「こりが取れる」「痛みが消える」「血行がよくなる」「筋肉がほぐれる」を書かない。「温める」「心地よく感じる人がいる」「こわばった感じ」まで
- メーカーの効能表現(pain relief、deep penetrating、promote relaxation、moist heat therapy の効果)を引用しない。"moist heat" は機能名としても使わない(採用品で Neck Renue の可否が未確認のため)
- 温度の数字(°F)は書かない(各社の値の測り方が分からず、比較を誤らせる)
- 加熱時間は採用品の公式の値だけ。ほかの商品・一般論の「目安」を作らない
- 「使った」「テストした」は書かない。レビュー数・評価も書かない
- 価格・割引・送料無料・Black Friday などのセール名は書かない

---

## アフィリエイトリンク配置ポイント
すべて Amazon Associates US(tag=quietrecover-20)、`rel="nofollow sponsored" target="_blank"`、文言は "Check … on Amazon" / "See … on Amazon"。CTA は `<div class="cta-box">...</div>`(foot-warmer と同じ形)。

| 位置 | 商品 | 検索リンク |
|---|---|---|
| 導入直後「In a hurry?」 | Sunbeam Neck Renue | https://www.amazon.com/s?k=Sunbeam+Neck+Renue+Heat+Wrap&tag=quietrecover-20 |
| 比較表2の直後(3商品まとめ) | 3点 | 下の3本 |
| Pick 1 の末尾 | Sunbeam Neck Renue | https://www.amazon.com/s?k=Sunbeam+Neck+Renue+Heat+Wrap&tag=quietrecover-20 |
| Pick 2 の末尾 | Comfytemp K9306 | https://www.amazon.com/s?k=Comfytemp+Microwavable+Neck+Shoulder+Heating+Pad&tag=quietrecover-20 |
| Pick 3 の末尾 | Bed Buddy Hot & Cold Wrap | https://www.amazon.com/s?k=Bed+Buddy+Hot+Cold+Wrap&tag=quietrecover-20 |
| まとめ | 3点(短い一言つき) | 同上 |

差し替え時のリンク(使う場合だけ):
- PureRelief: https://www.amazon.com/s?k=Pure+Enrichment+PureRelief+Neck+Shoulder+Heating+Pad&tag=quietrecover-20
- Sunbeam Renue Heat Wrap: https://www.amazon.com/s?k=Sunbeam+Renue+Heat+Wrap&tag=quietrecover-20
- Warmies(人間確認が取れた場合のみ): https://www.amazon.com/s?k=Warmies+Microwavable+Neck+Wrap&tag=quietrecover-20

- 比較表の中にはリンクを入れない(表を画像化するため)
- Also Looked At にはリンクを付けない
- ブランド直販・他 ASP は未承認のため使わない
- `{% if campaign.phase %}` のセールブロックは入れない

## 内部リンク候補(すべて公開済みを確認: publishAt が 2026-11-28 より過去、または publishAt 無し)
| リンク先 | 公開日 | 置く場所 | アンカー例 |
|---|---|---|---|
| `/posts/shiatsu-neck-shoulder-massager-desk-tension/` | 2026-09-26 | 導入(範囲)、FAQ「desk workers」、向いていない人、**まとめ(出口の導線)** | our guide to shiatsu neck massagers for desk workers |
| `/posts/shiatsu-back-massager-office-chair-desk-workers/` | 2026-10-22 | 向いていない人(肩甲骨の間・腰) | shiatsu back massagers for office chairs |
| `/posts/foot-warmer-for-bed/` | 2026-11-17 | 向いていない人(糖尿病の詳しい話・足の冷え) | our foot warmer for bed guide |
| `/posts/quiet-space-heaters-bedroom-light-sleepers/` | 2026-10-13 | 向いていない人(部屋が寒い) | quiet space heaters |
| `/posts/red-light-therapy-devices-for-home/` | 2026-07-25(publishAt 無し・公開済み) | **任意**。まとめの後に1文(夜の習慣に別の道具を足す人向け。shiatsu-neck のまとめと同じ扱い)。語数が厳しければ省く | red light therapy devices for home |

- 記法は必ず `{{ '/posts/xxx/' | url }}`(例: `[our guide to shiatsu neck massagers for desk workers]({{ '/posts/shiatsu-neck-shoulder-massager-desk-tension/' | url }})`)
- **リンクしない:** `heated-seat-massager-for-back`・`heated-mattress-pad-vs-electric-blanket`(どちらも published: false)。公開後に相互リンクを足すなら `{% whenPublished "slug" %}...{% endwhenPublished %}` で囲む(.eleventy.js に定義あり)。今回は入れない
- 重複を避けるための線引き:
  - **shiatsu-neck:** 揉む機能・RENPHO/Naipo/Breo の比較はあちら。本記事は**揉まない・温めるだけ**の道具に限定し、マッサージ器は扱わない。shiatsu-neck の「Who Should Check With a Doctor First」と同じ内容を長く繰り返さない
  - **shiatsu-back:** 椅子に付けるクッション・タイマーの話はあちら。本記事で「椅子の背もたれとの間に挟まない」は FDA の注意として1文だけ
  - **heated-seat(下書き):** 座面・ソファ・車のクッション。HoMedics/Sharper Image のクッションは扱わない。「Heat Safety」節の言い回し(auto shut-off is a backup など)をそのまま使わない
  - **heated-mattress-pad(下書き):** ベッド全面の電気寝具。本記事はベッドで使う話をしない(「寝る前に切る」だけ)
  - **foot-warmer:** 足元・糖尿病の詳しい出典はあちら。FDA の折りたたみリコールはあちらでも触れているので、本記事では1文に留める
- 逆方向(shiatsu-neck の導入や「Which One Should You Buy?」から本記事へ「まず温めるだけで試したい人は」)のリンク追加は公開後の別作業

---

## 人間確認(公開前)
1. **Amazon:** 3商品の取り扱い・現行の出品名・評価・レビュー数(スコアの「レビュー」欄を確定)。特に
   - 「Sunbeam Neck Renue Heat Wrap」で出るか。マッサージつきの Renue や旧型(22×14)と混ざっていないか
   - Comfytemp は K9306(首肩用、亜麻仁+クレイ)が出るか。K9305(33×4 の細長い型)・K9304(12×23 の平ら型)と取り違えない
   - Bed Buddy Hot & Cold Wrap が1個売りか2個組か
2. **Comfytemp(comfytemp.com を目視):** K9306 の加熱時間(800W 3〜4分/1200W 2〜3分/最大5分/2分から・半分)、冷蔵庫の記載、洗えない記載、2.8ポンド。**取れなければ表2・FAQ の加熱時間を「See the label」に置き換える**
3. **Bed Buddy(carex.com を目視):** 1個売りページの加熱時間が 2個組と同じか(600W 1:15/900W 0:50/1200W 0:37/1分置く)、冷凍の記載、大きさ・重さ。採用品専用の説明書があれば、睡眠中の使用・対象外の人の記載
4. **FDA の Mighty Bliss 安全情報:** ページが 404。移動先を探し、「Never sleep with the heating pad on」「15-20 mins」などの文言が今も載っているか確認。見つからなければ、その項目は CPSC 701 と University of Utah Health だけで書く(「15〜20分」は削る)
5. **Sunbeam(sunbeam.com を目視):** Neck Renue の洗濯手順・22×19インチ・在庫。個別の説明書 PDF が取れるなら、睡眠中・対象外の人の記載が FAQ と同じか
6. タイトル案の最終決定
7. 採点は暫定。人間確認の結果で 7点を割る商品があれば差し替え表に沿って入れ替える
8. categories.json の posts に `"microwavable-neck-wrap-vs-electric-heating-pad": "recovery"` を追加(公開作業時)

## 出典一覧
- Sunbeam Neck Renue Heat Wrap(sunbeam.com): https://www.sunbeam.com/pain-relief/neck-and-shoulder-pain/sunbeam-neck-renue-heat-wrap/SP_615336.html(検索抜粋。直接取得は 403)
- Sunbeam Neck Renue(Sunbeam の商品情報配信ページ): https://sites.salsify.com/41c9c255-1884-40e0-bc05-ad8dd5617744/c662aea6-b860-4545-ab16-2118694bf473/en-US/product/SAP_2137638/Sunbeam(r)-Neck-Renue(r)-Heat-Wrap/(本文確認)
- Sunbeam Renue Heat Wrap(旧型): https://sites.salsify.com/41c9c255-1884-40e0-bc05-ad8dd5617744/c662aea6-b860-4545-ab16-2118694bf473/en-US/product/SAP_2102255/Sunbeam(r)-Renue(r)-Heat-Wrap/(本文確認)/ https://www.sunbeam.com/pain-relief/neck-and-shoulder-pain/renue-heat-wrap/SAP_2102255.html(検索結果で Out of Stock 表示)
- Sunbeam Renue Neck & Shoulder Wrap(カナダ公式、類似品): https://www.sunbeam.ca/en_CA/new/renue-neck-and-shoulder-wrap/2102241.html(本文確認)
- Sunbeam ヘルプ・FAQ: https://help.sunbeam.com/s/article/CA-Pain-Relief-Buying-Guide?language=en_CA / https://sunbeam.com/service-and-support/product-support/product-faqs/pain-relief/heat-wraps/heating-pads-heat-wraps-faq.html(検索抜粋)
- Pure Enrichment PureRelief Neck & Shoulder: https://pureenrichment.com/products/purerelief-neck-shoulder-heating-pad(検索抜粋。直接取得は 429)
- Comfytemp K9306: https://comfytemp.com/products/comfytemp-neck-shoulder-microwavable-heating-pad(検索抜粋。直接取得は 429)
- Comfytemp 安全ページ: https://comfytemp.com/blogs/news/how-to-safely-use-microwavable-heating-pad(検索抜粋)
- Comfytemp K9015: https://comfytemp.com/products/wyj-weighted-heating-pad-for-neck-and-shoulders(商品データ .json を本文確認)
- Comfytemp 商品一覧・説明書ページ: https://www.comfytemp.com/ / https://comfytemp.com/pages/product-instruction(本文確認。PDF リンクは無し)
- Bed Buddy Hot & Cold Wrap: https://carex.com/products/bed-buddy-microwaveable-neck-wrap(検索結果に表示のみ)/ 2個組 https://carex.com/products/bed-buddy-hot-cold-wrap-two-pack(検索抜粋)
- Bed Buddy Neck & Hand Wrap: https://carex.com/products/bed-buddy-neck-hand-wrap(検索抜粋)
- Bed Buddy ボディラップ説明書: https://cdn.shopify.com/s/files/1/0240/6504/8681/files/BB_BodyWrap_Instructions.pdf(PDF 本文確認)
- CPSC Publication 701: https://www.cpsc.gov/s3fs-public/701.pdf(PDF 本文確認)
- FDA Mighty Bliss 安全情報: https://fda.gov/medical-devices/safety-communications/do-not-use-certain-mighty-bliss-electric-heating-pads-due-risk-injury-fda-safety-communication(検索抜粋。本文は 404)
- FDA Navajo 首肩用パッドのリコール: http://www.fda.gov/medical-devices/medical-device-recalls-and-early-alerts/heating-pad-recall-navajo-manufacturing-company-removes-handy-solutions-neck-shoulders-heating-pad(本文確認)
- CPSC Telebrands Therma Scarf リコール(2010): https://www.cpsc.gov/Recalls/2010/telebrands-recalls-scarves-with-microwaveable-heat-packs-due-to-fire-and-burn-hazards(検索抜粋。本文は 403)
- University of Utah Health: https://healthcare.utah.edu/the-scope/health-library/all/2018/11/heating-pads-can-cause-second-degree-burns(本文確認)
- 使わなかった: Cedars-Sinai https://www.cedars-sinai.org/stories-and-insights/healthy-living/how-to-use-a-heating-pad-to-heal-and-ease-pain-from-muscle-injuries(本文確認。睡眠中の扱いが CPSC・FDA と食い違うため)/ NIH MedlinePlus Magazine 熱傷 PDF(該当記載なし)
