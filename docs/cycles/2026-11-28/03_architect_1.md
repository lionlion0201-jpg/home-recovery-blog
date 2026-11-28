# 03. アーキテクト設計図: heated-mattress-pad-vs-electric-blanket(2026-11-28)

インプット: docs/agents/architect.md、共通ルール(rule of foreign affiliate.md)、02_marketer.md「1」、関連既存記事(foot-warmer-for-bed / couples-different-sleep-temperatures-dual-zone-bed / quiet-space-heaters-bedroom-light-sleepers / best-quiet-bedroom-humidifiers-for-fall)、構成見本 docs/cycles/2026-11-21/03_architect_quiet-air-purifier-for-bedroom.md、src/_data/categories.json

- スラッグ: `heated-mattress-pad-vs-electric-blanket` / テーマ: sleep-environment(front matter は `category: Sleep` で可。**categories.json の posts にはまだ未登録** → 公開作業時に1行追加が必要。アーキテクトは編集しない)
- 読者: **1人で寝る人**(または自分の側だけ温めたい人)。2人用・左右別設定の話は couples-dual-zone 記事へリンクで送る。本記事では dual control を「比較表の1列」と「1段落+リンク」以上に掘らない
- 本文は書かない。リポジトリのファイルはこの設計図以外変更していない

---

## 0. 調査で分かった前提(ライターが最初に読むこと)

1. **sunbeam.com は自動取得が 403(アクセス拒否)。** 製品ページの仕様は **sunbeam.com ドメインに限定した検索結果の抜粋**で確認した。本文は読めていない。
2. **Sunbeam の説明書は、sunbeam.ca(Sunbeam カナダ公式)に置かれた「Universal Heated Bedding User Manual - Extended Version」(P.N. 192633 Rev A、2019-07、英仏併記、電気毛布・敷きパッド・ひざ掛け共通)を PDF 取得して本文を確認した。** 米国の問い合わせ先(800-892-7684)と米国の保証元 Sunbeam Products, Inc. の記載があり北米共通版と読めるが、**採用する個別モデル(MRU5S・BRF9)専用の説明書ではない** → 記事では「Sunbeam's heated bedding manual we read」と書き、手元の説明書を優先するよう添える。
3. **Serta・Beautyrest の電気寝具はライセンス品で、製造・卸は Olliix(旧 JLA Home)。** 仕様は olliix.com(卸サイト)の製品ページ本文で確認した。**在庫表示は「Out of Stock Pre-order / 01/19/2024」という古い日付のまま** → 現行流通しているかは Amazon で人間確認が必須。Serta・Beautyrest の**説明書は入手できなかった**。
4. **Bedsure は公式サイト(bedsure.com)に接続できなかった(DNS エラー)。** 小売店の掲載情報は仕様が食い違う(6段階/10段階、自動オフ 8時間/3時間)。さらに **CPSC が 2023-03-09 に Bedsure の電気毛布・電気パッド約35万台のリコールを公表**(コントローラーの故障で火災・やけどの危険。2022年8〜11月販売の7型番。リコール番号 23-735)。現行品の安全性を否定する根拠ではないが、公式仕様を確認できないため推奨から外す。
5. **「つけたまま寝ていいか」について公式に確認できたこと(ここが記事の核):**
   - **Sunbeam 説明書:** 「寝ている間は使うな」という一文は**無い**。同時に「寝ている間も使ってよい」と明記した一文も**無い**。書かれているのは「Auto-Off は**省エネのため**、連続使用 **10時間**で電気毛布・敷きパッドを自動で切る(ひざ掛けは3時間)」「使わないときは必ず OFF」「一部モデルは Auto-Off Select で自動オフを解除でき、表示が StayOn になる」。→ 記事では「説明書は一晩使うことを禁じていないが、自動オフを安全装置としては説明していない(省エネ目的と書いている)」とだけ書く。**「寝ながら使って安全」とは書かない。**
   - **Sunbeam 公式の比較ページ(マーケティング記事):** 敷きパッドは「一か所にとどまり、夜通し(throughout the night)下から温める」と説明。→ メーカーが夜通しの使用を想定している根拠として**引用は1回、出典を明記**。安全性の保証としては扱わない。
   - **CPSC(米国消費者製品安全委員会)「Safety for Older Consumers – Home Safety Checklist」(Publication 701):** 電気毛布は**折りたたまない・ほかの物で覆わない・「tuck in(端をマットレスに挟み込む)」しない**/**ほかの毛布や掛け布団、寝ているペットも上に乗せない**/端はベッドの横と足元から自然に垂らす/電源コードを挟まない。**ヒーティングパッド(治療用の温熱パッド)は寝る前に必ず切る(低い設定でも重いやけどの恐れ)**。→ 重要: **電気毛布を掛け布団の下に入れて一晩使う、という多くの人のやり方は CPSC の注意と衝突する。** 記事の比較軸にする。またヒーティングパッドと電気敷きパッドは別物であることを明記(混同させない)。
   - **UL(安全認証機関)の記事:** UL など国が認める試験機関の認証がある毛布だけを使う/使うときは折りたたまない/**ベッドを先に温めて、入る前に切る**ことを推奨。→「寝る前に温めて切る」が最も保守的な使い方、という整理に使う。
   - **Serta:** 説明書未入手。**olliix.com の製品ページに「1〜12時間の自動オフタイマー」**とあるのみ。睡眠中の使用についての記載は未確認。
6. **リコール(公式・cpsc.gov):**
   - Sunbeam Queen Size Heated Blanket **型番 32810027**(2023-03-16、Star Elite Inc. がカナダで流通、約4.3万台米国、過熱で火災・やけどの恐れ、リコール番号 23-157)。**型番は洗濯表示ラベルに印字** → 「買った・持っているなら型番を確認」の一文に使える。採用モデル(MRU5S・BRF9)とは別型番。
   - Bedsure(上記 4)。
   - **Melinora 電気毛布**(2026-07-16 CPSC 警告 26-616、Amazon で 2025年2〜10月販売、内部の発熱線が過熱し生地を溶かす、メーカーはリコールに応じず)。
   - → 記事では「買う前・使う前に cpsc.gov/Recalls でブランドと型番を確認」と1か所で書く。特定ブランドを悪く書かない。
7. **Amazon は開いていない。** 取り扱い・評価・レビュー数・現在の型番の出方はすべて人間確認。下のスコアの「レビュー」は全商品「仮に1点」。

---

## 商品候補スコアリング(比較記事の場合)

**採点は暫定。** 「レビュー」は Amazon を見られないため全商品「仮に1点」。「紹介料」は価格帯からの相対的な推測(金額は書かない)。

| 商品 | 種類 | 検索意図 | 紹介料 | レビュー(仮) | 伝えやすさ | 比較軸 | 合計 |
|---|---|---|---|---|---|---|---|
| Sunbeam Premium Quilted Heated Mattress Pad(MRU5S) | 敷きパッド | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Sunbeam Quilted Fleece Heated Blanket(BRF9) | 電気毛布 | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Serta Plush Heated Blanket(ST54-0091 ほか) | 電気毛布 | 2 | 1 | 1 | 2 | 2 | **8/10** |
| Beautyrest Cotton Blend Heated Mattress Pad(BR55-0200 ほか) | 敷きパッド | 2 | 1 | 1 | 1 | 2 | **7/10** |
| Sunbeam LoftTec Heated Blanket(BRL9) | 電気毛布 | 2 | 1 | 1 | 2 | 1 | **7/10** |
| Beautyrest Cotton Deep Pocket Heated Mattress Pad(20段階) | 敷きパッド | 1 | 1 | 1 | 1 | 2 | 6/10 |
| Serta Corded Plush Heated Blanket(ST54-0291) | 電気毛布 | 2 | 1 | 1 | 2 | 1 | **7/10** |
| Sunbeam Water Resistant Heated Mattress Pad(MSU6S) | 敷きパッド | 1 | 1 | 1 | 1 | 1 | 5/10 |
| Serta Plush Heated Mattress Pad(ST55-0187) | 敷きパッド | 1 | 1 | 1 | 1 | 1 | 5/10 |
| Bedsure 電気毛布(フランネル各種) | 電気毛布 | 1 | 0 | 1 | 1 | 1 | 4/10 |

採点の理由(要点):
- **Sunbeam Premium Quilted pad:** 公式で 10段階・予熱(preheat)・10時間で自動オフ・洗濯機と乾燥機可・ツインはマットレス厚 21インチまで・5年保証。説明書でツインは「シングルコントロール」、Full/Queen/King は「デュアルコントロール」の設定図あり。1人寝の「下から温める」代表。
- **Sunbeam Quilted Fleece blanket:** 公式で 10段階・10時間自動オフ・ポリエステル100%・洗濯機と乾燥機可。同じ説明書(共通版)で注意事項を引ける=敷きパッドとの「同じメーカー内での比較」がきれいに作れる。
- **Serta Plush Heated Blanket:** olliix.com で 10段階・**1〜12時間で選べる自動オフタイマー**・Twin/Full はコントローラー1つ(Queen/King は2つ)・洗濯機可・5年保証。「寝る前だけ温めて短時間で切る」使い方と相性がよい=比較軸として独自。ただし説明書未入手・卸サイトの在庫表示が古い。
- **Beautyrest Cotton Blend pad:** olliix.com で 5段階・10時間自動オフ・Twin/Twin XL/Full はコントローラー1つ・洗濯機可・18インチまで・5年保証。「Secure Comfort technology で電磁界(EMF)を virtually eliminate」とあるが**健康効果に結びつく宣伝文句なので記事では使わない**。段階数が少なく画像で差が伝わりにくい → 伝えやすさ1。
- **Sunbeam LoftTec:** 公式で 20段階・予熱・10時間。ただし同じページ内で「10段階」の記載もある(検索抜粋のレビュー指摘)→ 段階数の食い違いで比較軸1。
- **Beautyrest Deep Pocket(20段階):** 20段階・10時間・21インチまで・Twin/Full はコントローラー1つ。厚いマットレス向けという限定的な意図 → 6点。
- **Serta Corded Plush:** 10段階・過熱保護・洗濯機可。自動オフの時間が製品ページに無い → 比較軸1。
- **Sunbeam Water Resistant pad / Serta Plush pad:** 公式で存在は確認したが仕様の詳細を読めていない → 5点。
- **Bedsure:** 公式サイトに接続できず仕様が食い違う。2023年に CPSC リコール(型番限定)。低価格帯で紹介料も低め → 4点。本文では扱わない(リコールの話で名前を出す必要もない。「cpsc.gov で確認を」で足りる)。

### 採用(7点以上の上位3件)
1. **Sunbeam Premium Quilted Heated Mattress Pad(Twin)** — 敷きパッド枠「寝床を下から、一晩中同じ場所で」(mid-range)
2. **Sunbeam Quilted Fleece Heated Blanket(Twin)** — 電気毛布枠「上から掛ける・ソファでも使える」(budget〜mid-range、人間判断)
3. **Serta Plush Heated Blanket(Twin)** — 電気毛布枠「自動オフを1〜12時間で短く設定できる」(mid-range)。**条件:** Amazon で現行品が見つからなければ下の差し替え先へ

※ 敷きパッド1・電気毛布2の構成。敷きパッドが1つだけになるのを避けたい場合は、**Beautyrest Cotton Blend pad(7点)を4件目として追加してよい**(語数上限 2,800 を超えない範囲で。ライター判断)。

### 差し替え先(Amazon で見つからない・型番がずれる場合)
| 採用商品 | 1番目の差し替え先 | 2番目 | 判断のしかた |
|---|---|---|---|
| Sunbeam Premium Quilted pad | **Beautyrest Cotton Blend Heated Mattress Pad**(7点) | Sunbeam Water Resistant pad(仕様を公式で再確認できた場合のみ) | 検索で「Premium Quilted」が出ず「Restful Quilted」などの別名だけ出る場合も差し替え。Restful は公式で確認できていない(小売店の掲載のみ・段階数と自動オフ時間が掲載ごとに違う) |
| Sunbeam Quilted Fleece blanket | **Sunbeam LoftTec Heated Blanket**(7点。段階数は「Sunbeam lists 20」とせず、人間が公式ページで目視した値を使う) | Sunbeam Channeled Microplush Heated Blanket(公式で 10段階・予熱・10時間。抜粋確認のみ) | 型番 32810027(2023年リコール対象の Queen)と取り違えない |
| Serta Plush Heated Blanket | **Serta Corded Plush Heated Blanket**(7点。自動オフ時間は「未確認、出品ページで確認を」と書く) | Beautyrest Electric Micro Fleece Heated Blanket(仕様未確認。差し替えるなら olliix.com で再確認してから) | Serta を外すと「タイマーを短くできる」比較軸が弱くなる → その場合は H2「タイマー」の節を一般論に寄せる |

### Also Looked At(本文では短く1〜2文ずつ。確認できた事実だけ。リンクは付けない)
- **Beautyrest Cotton Blend Heated Mattress Pad** — 5段階・10時間自動オフ・Twin〜Full はコントローラー1つ(Olliix の製品ページ)。段階を細かく選びたい人には少なめ(4件目に採用しない場合のみここに置く)
- **Sunbeam LoftTec Heated Blanket** — 公式ページで 20段階・予熱。ただし段階数の表記が揃っていなかったので推奨から外した、と正直に
- **Beautyrest Cotton Deep Pocket(20段階)** — 21インチまでの厚いマットレス向け

---

## 公式で確認できた仕様(出典つき)

### Sunbeam Premium Quilted Heated Mattress Pad(MRU5S)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | sunbeam.com に製品ページあり(Twin / Full / Queen / King)。在庫は未確認 | https://sunbeam.com/channeladvisor-us/sunbeam-premium-quilted-heated-mattress-pad-full/MRU5SFS-S000-12A44.html(検索抜粋)/ Twin: https://www.sunbeam.com/on/demandware.store/Sites-sunbeam-Site/default/Product-Variation?pid=MRU5S-MASTER%20PMP&dwvar_MRU5S-MASTER%20PMP_size=Twin(検索抜粋) |
| 温度段階 | 10段階 | 同上 |
| 自動オフ | 10時間 | 同上 |
| 予熱 | あり(preheat setting)。説明書では「予熱は30分ベッドを温め、元の設定に戻る」(予熱付きモデルの説明) | 製品ページ / 説明書 |
| 温度調整の仕組み | ThermoFine technology(温度の変化を感知して一定に保つ、とメーカー説明) | 製品ページ・https://www.sunbeam.com/on/demandware.store/Sites-sunbeam-Site/default/Content-Show?cid=how-do-heated-blankets-work(検索抜粋) |
| 洗濯 | 洗濯機・乾燥機可(製品ページ)。説明書: 冷水・弱水流で洗うか手洗い、乾燥は低温・デリケート、湿り気が残るうちに取り出して形を整え、物干しにかける(洗濯ばさみは使わない)、完全に乾くまで電源につながない。コインランドリーの乾燥機は使わない | 製品ページ / 説明書 |
| デュアルコントロール | Queen は左右別のデュアルコントロール(製品ページ)。**Twin のコントローラー数は製品ページで未確認**(説明書の設定図は「TWIN SINGLE CONTROL」「FULL/QUEEN/KING DUAL CONTROL」) | 製品ページ / 説明書 |
| 素材・厚み | Twin は綿50%・ポリエステル50%、21インチまで(ページ内で「綿100%」の記載もあり食い違い → 素材は書かない) | 製品ページ |
| 保証 | 5年限定保証(製品ページ)。※説明書(共通版)は3年保証と記載 → **保証年数は記事に書かない** | 製品ページ / 説明書 |
| UL/ETL 認証 | **未確認**(公式ページ本文を読めなかった) | — |

### Sunbeam Quilted Fleece Heated Blanket(BRF9、Twin)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | sunbeam.com に製品ページあり(Twin、Newport Blue ほか)。在庫は未確認 | https://sunbeam.com/heated-bedding/blankets/sunbeam-twin-quilted-fleece-heated-blanket-newport-blue/BRF9GTS-R595-13A44.html(検索抜粋) |
| 温度段階 | 10段階 | 同上 |
| 自動オフ | 10時間 | 同上 |
| 予熱 | **未確認** | — |
| 洗濯 | 洗濯機・乾燥機可、ポリエステル100% | 同上 |
| コントローラー | Twin はシングル(説明書の設定図)。製品ページでは未確認 | 説明書 |
| UL/ETL 認証 | **未確認** | — |

### Serta Plush Heated Blanket(ST54-0091 ほか、Twin)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | olliix.com(Serta 電気寝具の卸元)に製品ページあり。**在庫表示は「Out of Stock Pre-order / 予定 01/19/2024」で古い** → Amazon で人間確認 | https://www.olliix.com/product/data/13954/st54-0091 |
| 温度段階 | 10段階 | 同上 |
| 自動オフ | **1〜12時間で設定できる自動オフタイマー** | 同上 |
| コントローラー | Twin・Full は1つ、Queen・King は2つ | 同上 |
| 洗濯 | 洗濯機可。乾燥の可否は**未確認** | 同上 |
| 保証 | メーカー5年保証(記事には書かない) | 同上 |
| UL/ETL 認証 | **未確認**(小売店の別 Serta 製品に「ETL certified」の記載はあるが本品では未確認) | — |
| 説明書 | **未入手。睡眠中の使用・対象外の人の記載は未確認** | — |

### Beautyrest Cotton Blend Heated Mattress Pad(差し替え先1/4件目候補)
| 項目 | 内容 | 出典 |
|---|---|---|
| 現行品か | olliix.com に製品ページあり。在庫表示は古い(01/19/2024) | https://olliix.com/Product/Data/7363/BR55-0671 / 一覧 https://www.olliix.com/product?c=125(型番 BR55-0200) |
| 温度段階 | 5段階 | 同上 |
| 自動オフ | 10時間 | 同上 |
| コントローラー | Twin・Twin XL・Full は1つ、Queen・King・Cal King は2つ | 同上 |
| 洗濯 | 洗濯機可(乾燥は未確認) | 同上 |
| 厚み | 18インチまで | 同上 |
| 使わない表現 | 「Secure Comfort technology で EMF を virtually eliminate」→ 健康不安をあおる・効果を連想させるため**記事に書かない** | — |

### Sunbeam 説明書(共通版)で確認した注意事項(PDF 本文確認)
出典: https://www.sunbeam.ca/on/demandware.static/-/Sites-sunbeam-ca-Library/default/dwbe5fa15c/documents/instruction-manuals/Sunbeam-Heated-Mattress-Pads-EXTENDED-User-Manual.pdf
- **使ってはいけない人:** 乳児、子ども、体が不自由で動けない人、対麻痺・四肢麻痺の人、**糖尿病の人**、**血行が悪いなど熱を感じにくい人**、**説明を理解できない人・コントローラーを操作できない人**(注意事項2・FAQ)
- **折りたたむ・寄せ集める**と使用中に過熱することがある(11)/**tuck in しない**、挟まない(3)
- コードをマットレスとボックススプリングの間に通さない、挟まない、傷んだコードは使わない(4)/延長コード・発電機・インバーターで使わない(9)
- **ほかの電気で温める製品と一緒に使わない**(15)= 電気敷きパッドと電気毛布の**併用不可**(本記事で必ず書く。「両方買う」読者が出るため)
- ウォーターベッド・二段ベッド・電動リクライニングベッド・子ども用ベッドでは使わない(14)
- ピンなど金属を使わない(6)/濡れたら使わない(7)/使わないときは OFF か抜く(10)/使用前に毎回、本体・コード・コントローラーを点検(12)
- ペットを近づけない(19)/鎮痛クリーム・塗り薬と一緒に使わない(やけどの恐れ)(21)/**ペースメーカーなど医療機器を使っている人は使用前に医療者に確認**(22)
- 自動オフ: 「省エネのため」連続使用10時間で切れる(ひざ掛けは3時間)。デュアルはそれぞれ独立して10時間。一部モデルは解除可(StayOn)。停電後はタイマーがリセット
- 「ヒーティングパッドではないので、平らに敷いた状態では熱く感じない」(FAQ)= 期待値の調整に使える(「思ったより熱くない」は故障ではない、ただし説明書の点検手順に従う)

### 公的機関・認証機関の情報
- **CPSC Publication 701(Safety for Older Consumers – Home Safety Checklist)** PDF 本文確認: https://www.cpsc.gov/s3fs-public/701.pdf
  - 電気毛布は使用中、折りたたまない・ほかの物で覆わない・tuck in しない/電源コードをベッドや壁・床で挟まない・つぶさない/発熱部やコントローラーを覆う物は過熱の原因/**ほかの毛布・掛け布団・寝ているペットも上に乗せない**/tuck in は熱がこもり火災の原因になりうる/端はベッドの横と足元から自然に垂らす
  - ヒーティングパッドは寝る前に必ず切る。低い設定でも重いやけどの恐れ
  - ※高齢者向けチェックリストだが内容は一般的な使い方の注意。記事では「CPSC's home safety checklist」と書き、高齢者向けである旨を一言添えてもよい
- **UL「Electric blankets are cozy, but are they safe?」** https://ul.com/insights/electric-blankets-are-cozy-are-they-safe(本文確認): UL など国が認める試験機関の認証がある製品を使う/使用中に折りたたまない/ベッドを温めてから入る前に切る/傷んだ物は捨てる/乳児・幼い子ども・自分で操作できない人には勧めない/ペットを近づけない
- **CPSC リコール:** Sunbeam 32810027(https://www.cpsc.gov/Recalls/2023/Sunbeam-Heated-Blankets-Recalled-Due-to-Burn-and-Fire-Hazards-Distributed-by-Star-Elite、検索抜粋)/ Bedsure(https://www.cpsc.gov/Recalls/2023/Bedshe-International-Recalls-Bedsure-Electric-Heating-Blankets-and-Pads-Due-to-Fire-and-Thermal-Burn-Hazards-Recall-Alert、検索抜粋。本文取得は 403)/ Melinora 警告(https://www.cpsc.gov/Warnings/2026/CPSC-Warns-Consumers-to-Stop-Using-Melinora-Electric-Heated-Blankets-Immediately-Due-to-Risk-of-Serious-Injury-from-Burn-and-Fire-Hazards、本文確認)
- **UL 964(電気寝具の規格)** は存在のみ確認(規格本文・最新版は未確認)。記事では「UL 964」という番号を出さず「a UL or ETL mark」程度に留める
- **糖尿病で足の感覚が鈍い人の熱源使用:** NIDDK・CDC の記載は foot-warmer 記事で使用済み。本記事では Sunbeam 説明書の「糖尿病の人・熱を感じにくい人は使わない」を主に使い、重複を避けて foot-warmer 記事へリンクする

---

## 記事設計

### タイトル案
1. **Heated Mattress Pad vs. Electric Blanket: Which Warms a Cold Bed Better for One Sleeper?**(推奨。83字。長いが主キーワードが先頭)
2. Heated Mattress Pad vs. Electric Blanket: Heat From Below or Above?(66字)
3. Heated Mattress Pad vs. Electric Blanket for a Cold Bed: Timers, Washing, and What the Manuals Say(96字、長い)
4. 短縮案: **Heated Mattress Pad vs. Electric Blanket: Which to Choose?**(58字)

→ 推奨は 1。60字前後を厳守するなら 4。最終判断はディレクター/人間。
※ "Better" は「暖め方の向き不向き」の意味で健康効果ではないが、気になる場合は 2 か 4。

- ターゲットキーワード: `heated mattress pad vs electric blanket`(主)/ `can you sleep with a heated mattress pad on`(補。H2 1か所+FAQ 1問。詰め込まない)
- メタディスクリプション案(約150字):
  "Heated mattress pad vs. electric blanket for one sleeper: we compare where the heat comes from, timers, washing, and what the manuals say about using them overnight."
- 想定語数: **2,200〜2,800 語**(foot-warmer が 3,200 語超で長め。本記事は上限 2,800 を守る)
- front matter: `layout: post.njk` / `tags: post` / `category: Sleep` / `publishAt` は人間が決定
- 冒頭の開示文(foot-warmer と同じ形。アフィリエイト開示+医療免責+「We have not used these products ourselves」+「Your device's manual and safety warnings take priority」):
  "*Disclosure: This post contains affiliate links. If you purchase through one of them, we may earn a commission at no extra cost to you. Not medical advice: this article is for general informational purposes only and is not a substitute for advice from a doctor. Our picks are based on manufacturer websites, manuals, and published product information. We have not used these products ourselves. Your heated bedding's manual and safety warnings take priority over anything in this article.*"

### 見出し構成(H2/H3)

1. **導入**(約150語)
   - 場面: 1人で寝ている。部屋はそこまで寒くないのに、ベッドに入った瞬間のシーツが冷たい/夜中に冷えて目が覚める。暖房を一晩つけるのは避けたい(→ quiet space heaters 記事に1回リンク:部屋ごと温める選択肢)
   - 結論を先に: 「敷きパッドは下から・一晩同じ場所で。電気毛布は上から・ソファにも持っていける。ただし電気毛布の上には掛け布団を重ねないよう CPSC は注意している」
   - この記事の範囲: 1人で使う場合。2人で設定を分けたい人は couples-dual-zone 記事へ(1文でリンク)
   - 「In a hurry?」CTA ボックス(Sunbeam Premium Quilted pad 1本)

2. **H2: Heated Mattress Pad vs. Electric Blanket: The Short Answer**(約200語)
   - 3行の早見(箇条書き):
     - 冷たいシーツが一番の悩み・掛け布団はいつもどおり使いたい → 敷きパッド
     - ソファやリクライニングしない椅子でも使いたい・寝る前だけ温めたい → 電気毛布(Sunbeam 説明書はひざ掛け・ボディパッドについて、ロッキングチェア・リクライナーでの使用不可と書いている点に注意 → 「ソファで」までに留める)
     - 自分で温度を感じにくい・操作できない → どちらも使わない(「向いていない人」節へ)
   - Sunbeam 公式比較ページの要点を1回だけ引用:「違いは熱が来る向き」「敷きパッドは一か所にとどまる」「毛布は広げて使う必要がある」(引用は15語未満を1つだけ。他は言い換え)

3. **H2: Where the Heat Comes From, and Why It Matters**(約350語)
   - H3: A heated mattress pad warms you from below — マットレスとシーツの間。動かない。掛け布団は普段どおり。説明書: 平らに敷いた状態では「熱く感じない」のが正常(ヒーティングパッドとは違う)
   - H3: An electric blanket warms you from above — 上に掛ける。持ち運べる。ただし **CPSC: 使用中はほかの毛布・掛け布団を上に重ねない/tuck in しない/端は垂らす**。→ 寒い冬に「電気毛布+厚い掛け布団」にしたい人は、その使い方が注意と合わないことを知っておく(ここが比較の決め手になりうる、と書く。断定せず「worth knowing before you choose」)
   - H3: Folding, bunching, and tucking — 両方共通: 折りたたむ・寄せ集めると過熱しうる(Sunbeam 説明書・CPSC・UL)。寝返りでずれやすいのは上掛け(毛布)のほう、という整理は**推測なので書かない**。説明書の注意だけ書く

4. **H2: Heated Mattress Pad vs. Electric Blanket, Compared**(比較表。**必須・Pinterest 化する要素**)
   - 表1(種類の比較。4〜6行):
     | | Heated mattress pad | Electric blanket |
     |---|---|---|
     | Where it goes | Between mattress and fitted sheet | On top of you |
     | What can go on top | Your usual sheet and comforter(説明書の設置手順どおり) | CPSC: nothing on top while in use, including other blankets or comforters |
     | Tucking in | Don't tuck in the wired area(Sunbeam manual) | Don't tuck in; let edges hang(CPSC) |
     | Moves to the couch | No | Yes(ただし説明書の家具の注意に従う) |
     | Use with the other one | No — Sunbeam's manual says not to use with another electrically heated product | Same |
     | Typical auto-off(our picks) | 10 hours(Sunbeam) | 10 hours(Sunbeam)/ 1–12 hours, selectable(Serta) |
   - 表2(3商品の仕様。表1と分けて縦に長くしない):
     - 列: Product / Type / Heat settings / Auto-off / Preheat / Washing / Controllers(Twin) / Price tier / Best for / May not suit
     - Sunbeam Premium Quilted pad / pad / 10 / 10 hours / Yes / Machine wash and dry(follow the manual) / Single on Twin(manual diagram; confirm on listing) / mid-range / 冷たいシーツが悩み・掛け布団は普段どおり / 短い自動オフを選びたい人
     - Sunbeam Quilted Fleece blanket / blanket / 10 / 10 hours / Not confirmed / Machine wash and dry / Single on Twin(manual) / budget〜mid-range(人間判断) / ソファでも使いたい / 厚い掛け布団を重ねたい人
     - Serta Plush Heated Blanket / blanket / 10 / 1–12 hours, selectable / Not confirmed / Machine washable(drying not confirmed) / 1 on Twin and Full / mid-range / 寝る前だけ短時間 / 説明書を事前に読みたい人(未入手のため、出品ページで確認を)
   - 表の下に注記: 価格帯は相対表現/仕様はメーカー・卸元の公表情報で、出品ページで型番を確認すること
   - 表の直後に CTA ボックス(3商品まとめ)

5. **H2: Can You Sleep With a Heated Mattress Pad On? What the Manuals Say**(約350語。補助キーワードの H2)
   - **書き方の原則: 説明書と公的機関に書いてあることだけ。推測で「安全」「危険」と言わない**
   - Sunbeam: 説明書に「寝ている間は使わない」という一文は無い/自動オフは省エネ目的と説明、10時間/使わないときは OFF/一部モデルは自動オフを解除できる → 「説明書は一晩の使用を禁じていない。ただし自動オフを安全装置としては説明していない」。比較ページでは敷きパッドが夜通し温めると説明(1回だけ、出典明記)
   - Serta: 説明書を入手できなかった。製品ページで確認できたのは 1〜12時間のタイマーまで → 「手元の説明書を読んでから決めて」
   - 電気毛布: CPSC の「上に何も重ねない」。UL は「先に温めて、入る前に切る」を勧める
   - ヒーティングパッド(治療用)は別物: CPSC は寝る前に必ず切るよう言っている。**敷きパッドの代わりにヒーティングパッドをベッドに入れない**(foot-warmer 記事へのリンクはここで1回: 足元だけ冷える人向け)
   - 最も保守的な使い方として「予熱して、寝る前に下げるか切る」を提示(UL の推奨と一致)。**読者に一晩使用を勧めも禁止もしない。説明書に従うよう促す**
   - 小さな表にしてもよい(foot-warmer の「What the maker says about sleep」表と同じ形): Product / What the manual or maker says about overnight use / Auto-off

6. **H2: The 3 Picks**(各 約250〜300語)
   - 各商品の型(foot-warmer と同じ): **What it's for:** 1行 → 本文 → **Who it may not suit:** 箇条書き3〜4 → CTA ボックス
   - H3: **Sunbeam Premium Quilted Heated Mattress Pad — Warmth From Below, With a Preheat Setting**
     - 書くこと: 10段階/予熱(30分温めて元の設定に戻る=説明書の予熱機能の説明)/10時間自動オフ/洗濯機・乾燥機可だが手順は説明書どおり(低温、湿り気が残るうちに出す、完全に乾くまでつながない)/Twin は21インチまで/ThermoFine はメーカーの説明として1文/コントローラーとコードをマットレスとボックススプリングの間に通さない
     - 向かない: 自動オフを短く設定したい人(10時間固定、公式で確認できた範囲)/ソファでも使いたい人/電気毛布と併用したい人(説明書で不可)/「向いていない人」節の該当者
   - H3: **Sunbeam Quilted Fleece Heated Blanket — A Blanket You Can Also Use on the Couch**
     - 書くこと: 10段階/10時間/洗濯機・乾燥機可/Twin はシングルコントロール(説明書)/CPSC: 上に掛け布団を重ねない・tuck in しない/予熱は未確認なので書かない/型番 32810027(2023年リコールの Queen、別流通)と混同しないよう洗濯ラベルで確認、の一文はここか安全の節のどちらか1か所
     - 向かない: 厚い掛け布団を重ねて寝たい人/寝返りが多く毛布がまとまりやすい人(→「折りたたみ・寄せ集め」の注意に触れる。推測の断定はしない)/ペットと一緒に寝る人(CPSC: 寝ているペットも上に乗せない)
   - H3: **Serta Plush Heated Blanket — A Shut-Off Timer You Can Set Shorter**
     - 書くこと: 10段階/**1〜12時間のタイマー**(UL の「入る前に切る」に近い使い方をしやすい、という書き方。安全を保証しない)/Twin・Full はコントローラー1つ/洗濯機可、乾燥は未確認/説明書を確認できなかったことを正直に書く/電気寝具は Serta ブランドのライセンス品(Olliix が扱う)と1文入れてもよい(人間判断)
     - 向かない: 買う前に説明書を読みたい人(出品ページで確認を)/掛け布団を重ねたい人/予熱機能が欲しい人(未確認)

7. **H2: Electric Blankets and Heated Pads We Looked At but Didn't Pick**(約120語)— Also Looked At を各1〜2文。リンクなし

8. **H2: Before You Plug It In: A Heated Bedding Checklist**(約200語。チェックリスト=画像化しやすい要素2つ目)
   - foot-warmer の「Bedtime Checklist」と重ならないよう、**電気寝具全体(ベッド全面)向け**の項目にする:
   - [ ] UL か ETL の認証マークをラベルで確認(UL 記事)
   - [ ] cpsc.gov/Recalls でブランドと型番を確認(型番は洗濯ラベル。Sunbeam 32810027 の例)
   - [ ] 敷きパッドと電気毛布を同時に使わない(Sunbeam 説明書)
   - [ ] 電気毛布の上に掛け布団を重ねない・tuck in しない(CPSC)
   - [ ] 敷きパッドは平らに。折れ・寄りを毎回直す(説明書)
   - [ ] コードはマットレスとボックススプリングの間に通さない、延長コードを使わない(説明書)
   - [ ] 使う前に毎回、本体・コード・コントローラーを点検(説明書)
   - [ ] 電動リクライニングベッド・ウォーターベッド・二段ベッドでは使わない(説明書)
   - [ ] 洗ったら完全に乾くまでつながない(説明書)

9. **H2: Who Shouldn't Use a Heated Mattress Pad or Electric Blanket**(約200語。**必須の「向いていない人」節**)
   - Sunbeam 説明書の対象外リストをそのまま(乳児・子ども・動けない人・麻痺のある人・糖尿病の人・熱を感じにくい人・説明を理解できない/操作できない人)
   - ペースメーカーなど医療機器 → 使用前に医療者に確認(説明書)
   - 鎮痛クリーム・塗り薬を塗っている夜は使わない(説明書)
   - UL も乳児・幼い子ども・自分で操作できない人には勧めない
   - 糖尿病で足が冷える人は foot-warmer 記事の該当節へリンク(NIDDK・CDC の記載を重ねて書かない)
   - 2人で設定が合わない人 → この記事の対象外として couples-dual-zone 記事へ
   - 寒さの原因が分からない・急に冷えるようになった → 医師へ(断定しない言い回し)

10. **H2: FAQ**(H3 か太字で4〜5問)
    - **Can you sleep with a heated mattress pad on?** — 説明書の記載どおり(H2 5 の要約。Sunbeam は禁じていない/自動オフ10時間は省エネ目的/手元の説明書に従う)
    - **Is it safe to use a heated mattress pad and an electric blanket together?** — Sunbeam 説明書: ほかの電気で温める製品と一緒に使わない
    - **Can I put a comforter on top of an electric blanket?** — CPSC: 使用中はほかの毛布や掛け布団を上に乗せない
    - **Can you wash a heated mattress pad?** — 採用品は洗濯機可。説明書の手順(冷水・弱水流・低温乾燥・完全に乾くまでつながない・コントローラーは洗わない)
    - **Do I need a dual-control heated mattress pad if I sleep alone?** — Twin は多くがシングル(採用品で確認できた範囲)。Queen 以上でデュアルになるモデルもある。2人の話は couples 記事へ

11. **H2: Heated Mattress Pad or Electric Blanket: Which Fits Your Bed?**(まとめ、約150語)
    - 3〜4行の早見(導入の早見と言い回しを変える)
    - 最後の CTA ボックス(3商品)
    - 医療免責(本文末尾にも1文):"*This article is for general informational purposes only and is not medical advice. If you have diabetes, reduced feeling in your skin, a circulation condition, or a medical device, talk to your doctor before using heated bedding. Follow your product's manual and safety warnings.*"

### 健康・表現のルール(この記事固有)
- 見出しに "Better Sleep" "Relieves" "Soothes" "Improves Circulation" を使わない。"Which…?" "What the Manuals Say" 型
- 「温めると眠りやすくなる」「深い睡眠が増える」など睡眠効果を書かない(検索で見つかった「熱で睡眠段階が減る」系の話も根拠が二次情報なので書かない)
- EMF の話(Beautyrest の Secure Comfort、Serta の low EMF)は書かない。効能・不安訴求になる
- 「UL 認証済み」は採用品で確認できていない → 書かない。「ラベルで確認を」とだけ
- 保証年数は公式内で食い違う(5年/3年)→ 書かない
- 「使った」「テストした」は書かない。レビュー数・評価も書かない(sunbeam.com の評価 4.4/約330件は Amazon ではないので使わない)
- 価格・割引・送料無料・Black Friday などのセール名は書かない(今はセール時期だが本文には入れない)

---

## アフィリエイトリンク配置ポイント
すべて Amazon Associates US(tag=quietrecover-20)、`rel="nofollow sponsored" target="_blank"`、文言は "Check … on Amazon" / "See … on Amazon"。CTA は `<div class="cta-box">...</div>`(foot-warmer と同じ形)。

| 位置 | 商品 | 検索リンク |
|---|---|---|
| 導入直後「In a hurry?」 | Sunbeam Premium Quilted pad | https://www.amazon.com/s?k=Sunbeam+Premium+Quilted+Heated+Mattress+Pad+Twin&tag=quietrecover-20 |
| 比較表2の直後(3商品まとめ) | 3点 | 下の3本 |
| Pick 1 の末尾 | Sunbeam Premium Quilted pad | https://www.amazon.com/s?k=Sunbeam+Premium+Quilted+Heated+Mattress+Pad+Twin&tag=quietrecover-20 |
| Pick 2 の末尾 | Sunbeam Quilted Fleece blanket | https://www.amazon.com/s?k=Sunbeam+Quilted+Fleece+Heated+Blanket+Twin&tag=quietrecover-20 |
| Pick 3 の末尾 | Serta Plush Heated Blanket | https://www.amazon.com/s?k=Serta+Plush+Heated+Blanket+Twin&tag=quietrecover-20 |
| まとめ | 3点(短い一言つき) | 同上 |

差し替え時のリンク(使う場合だけ):
- Beautyrest Cotton Blend pad: https://www.amazon.com/s?k=Beautyrest+Cotton+Blend+Heated+Mattress+Pad+Twin&tag=quietrecover-20
- Sunbeam LoftTec: https://www.amazon.com/s?k=Sunbeam+LoftTec+Heated+Blanket+Twin&tag=quietrecover-20
- Serta Corded Plush: https://www.amazon.com/s?k=Serta+Corded+Plush+Heated+Blanket+Twin&tag=quietrecover-20

- 比較表の中にはリンクを入れない(表を画像化するため)
- Also Looked At にはリンクを付けない
- ブランド直販・他 ASP は未承認のため使わない
- `{% if campaign.phase %}` のセールブロックは入れない(記事の主旨と関係が薄い。入れるなら人間判断)

## 内部リンク候補(すべて公開済みを確認: publishAt が 2026-11-28 より過去、または publishAt 無し)
| リンク先 | 公開日 | 置く場所 | アンカー例 |
|---|---|---|---|
| `/posts/couples-different-sleep-temperatures-dual-zone-bed/` | 2026-10-05 | 導入(範囲の説明)、FAQ「dual-control」、向いていない人 | our guide to dual-zone options for couples |
| `/posts/foot-warmer-for-bed/` | 2026-11-17 | H2 5(ヒーティングパッドとの違い/足だけ冷える人)、向いていない人(糖尿病) | our guide to foot warmers for bed |
| `/posts/quiet-space-heaters-bedroom-light-sleepers/` | 2026-10-13 | 導入(部屋ごと温める選択肢) | quiet space heaters for the bedroom |
| `/posts/best-quiet-bedroom-humidifiers-for-fall/` | 2026-08-29(publishAt 無し・公開済み) | まとめ前 or 「向いていない人」の後に1文(冬の寝室の乾燥) | quiet bedroom humidifiers |

- 記法は必ず `{{ '/posts/xxx/' | url }}`(例: `[our guide to dual-zone options for couples]({{ '/posts/couples-different-sleep-temperatures-dual-zone-bed/' | url }})`)
- 重複を避けるための線引き:
  - **couples-dual-zone:** 「デュアルコントロール敷きパッドの仕組み・2人の安全上の注意」はあちらが詳しい。本記事では1段落とリンクだけ
  - **foot-warmer:** 「足元だけ」「NIDDK・CDC・糖尿病の詳細」「ヒーティングソックス」はあちら。本記事は**ベッド全面**の電気寝具に限定し、足元ウォーマーの商品は扱わない
  - **quiet space heaters:** 「部屋を温める」「CPSC の暖房器具の注意」はあちら。本記事は寝床を温める話
- 逆方向(foot-warmer の "You don't want a full heated mattress pad" 付近や space heaters の "Warm the bed rather than the room" からこの記事へ)のリンク追加は公開後の別作業

---

## 人間確認(公開前)
1. **Amazon:** 3商品の取り扱い・現行型番・評価・レビュー数(スコアの「レビュー」欄を確定)。特に Serta Plush Heated Blanket が現行で売られているか(卸サイトの在庫表示が 2024年のまま)。Sunbeam は「Premium Quilted」で出るか、「Restful Quilted」など別名でしか出ないか
2. **Sunbeam(sunbeam.com を目視):** Premium Quilted Twin のコントローラー数/Quilted Fleece の予熱の有無/UL・ETL 表示/製品ページから個別モデルの説明書 PDF が取れるなら、睡眠中の使用についての記載が共通版と同じか
3. **Serta:** 説明書(睡眠中の使用、使ってはいけない人、乾燥機の可否、UL/ETL)。確認できなければ本文は「確認できなかった」のまま
4. タイトル案の最終決定(83字案か58字案か)
5. 採点は暫定。人間確認の結果で 7点を割る商品があれば差し替え表に沿って入れ替える
6. categories.json の posts に `"heated-mattress-pad-vs-electric-blanket": "sleep-environment"` を追加(公開作業時)

## 出典一覧
- Sunbeam 共通説明書(sunbeam.ca、P.N. 192633 Rev A): https://www.sunbeam.ca/on/demandware.static/-/Sites-sunbeam-ca-Library/default/dwbe5fa15c/documents/instruction-manuals/Sunbeam-Heated-Mattress-Pads-EXTENDED-User-Manual.pdf(PDF 本文確認)
- Sunbeam Premium Quilted Heated Mattress Pad: https://sunbeam.com/channeladvisor-us/sunbeam-premium-quilted-heated-mattress-pad-full/MRU5SFS-S000-12A44.html(検索抜粋のみ。直接取得は 403)
- Sunbeam Quilted Fleece Heated Blanket: https://sunbeam.com/heated-bedding/blankets/sunbeam-twin-quilted-fleece-heated-blanket-newport-blue/BRF9GTS-R595-13A44.html(検索抜粋のみ)
- Sunbeam LoftTec: https://www.sunbeam.com/heated-bedding/blankets/sunbeam-twin-lofttec-heated-blanket-garnet/BRL9STS-R310-16A44.html(検索抜粋のみ)
- Sunbeam「Heated Mattress Pad vs. Heated Blanket」: https://www.sunbeam.com/Heated-Mattress-Pad-vs-Heated-Blanket.html(検索抜粋のみ)
- Sunbeam「How Do Heated Blankets Work?」: https://www.sunbeam.com/on/demandware.store/Sites-sunbeam-Site/default/Content-Show?cid=how-do-heated-blankets-work(検索抜粋のみ)
- Serta Plush Heated Blanket(Olliix): https://www.olliix.com/product/data/13954/st54-0091(本文確認)
- Serta Corded Plush Heated Blanket(Olliix): https://www.olliix.com/product/data/15552/st54-0291(本文確認)
- Beautyrest Cotton Blend Heated Mattress Pad(Olliix): https://olliix.com/Product/Data/7363/BR55-0671(本文確認)
- Beautyrest Cotton Deep Pocket(Olliix): https://www.olliix.com/product/data/11248/br55-0899(本文確認)
- Olliix 電気寝具一覧: https://www.olliix.com/product?c=125(本文確認)
- CPSC Publication 701: https://www.cpsc.gov/s3fs-public/701.pdf(PDF 本文確認)
- UL: https://ul.com/insights/electric-blankets-are-cozy-are-they-safe(本文確認)
- CPSC リコール Sunbeam 32810027: https://www.cpsc.gov/Recalls/2023/Sunbeam-Heated-Blankets-Recalled-Due-to-Burn-and-Fire-Hazards-Distributed-by-Star-Elite(検索抜粋)
- CPSC リコール Bedsure: https://www.cpsc.gov/Recalls/2023/Bedshe-International-Recalls-Bedsure-Electric-Heating-Blankets-and-Pads-Due-to-Fire-and-Thermal-Burn-Hazards-Recall-Alert(検索抜粋。直接取得は 403)
- CPSC 警告 Melinora: https://www.cpsc.gov/Warnings/2026/CPSC-Warns-Consumers-to-Stop-Using-Melinora-Electric-Heated-Blankets-Immediately-Due-to-Risk-of-Serious-Injury-from-Burn-and-Fire-Hazards(本文確認)
