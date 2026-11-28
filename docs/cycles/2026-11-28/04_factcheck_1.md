# 04. ファクトチェック結果(1回目): heated-mattress-pad-vs-electric-blanket(2026-11-28)

インプット: docs/agents/fact_checker.md、src/posts/heated-mattress-pad-vs-electric-blanket.md、docs/cycles/2026-11-28/03_architect_1.md
Amazon は開いていない(手順どおり)。sunbeam.com は WebFetch が 403(アクセス拒否)のため回避せず、sunbeam.com ドメインに限定した検索結果の抜粋と説明書 PDF で確認した。行番号は修正前の記事の行番号。

## 主な情報源(本文を確認したもの)
- Sunbeam 共通説明書(sunbeam.ca、P.N. 192633 Rev A、英語部分の本文をテキスト化して確認): https://www.sunbeam.ca/on/demandware.static/-/Sites-sunbeam-ca-Library/default/dwbe5fa15c/documents/instruction-manuals/Sunbeam-Heated-Mattress-Pads-EXTENDED-User-Manual.pdf
- CPSC「Safety for Older Consumers – Home Safety Checklist」(本文をテキスト化して確認): https://www.cpsc.gov/s3fs-public/701.pdf
- UL: https://ul.com/insights/electric-blankets-are-cozy-are-they-safe
- CPSC リコール Sunbeam 32810027: https://www.cpsc.gov/Recalls/2023/Sunbeam-Heated-Blankets-Recalled-Due-to-Burn-and-Fire-Hazards-Distributed-by-Star-Elite
- Olliix(Serta Plush): https://www.olliix.com/product/data/13954/st54-0091 / Beautyrest Cotton Blend: https://olliix.com/Product/Data/7363/BR55-0671 / Beautyrest Deep Pocket: https://www.olliix.com/product/data/11248/br55-0899 / 一覧: https://www.olliix.com/product?c=125
- Target(Serta Plush、補助): https://www.target.com/p/serta-full-plush-heated-blanket-teal/-/A-93487176

## ファクトチェック結果: heated-mattress-pad-vs-electric-blanket

| # | 行 | 主張(要約) | 判定 | 根拠URL | 対応 |
|---|---|---|---|---|---|
| 1 | L17, L46, L63, L184, L225 | CPSC: 使用中の電気毛布の上にほかの毛布・掛け布団・寝ているペットを乗せない/tuck in しない/端は垂らす/熱がこもり火災の恐れ。高齢者向けチェックリスト | 確認済み | https://www.cpsc.gov/s3fs-public/701.pdf | なし |
| 2 | L52 | CPSC と UL はどちらも使用中に折りたたまないよう言っている | 確認済み | CPSC 701 / https://ul.com/insights/electric-blankets-are-cozy-are-they-safe | なし |
| 3 | L101 | CPSC: ヒーティングパッドは寝る前に切る。低い設定でも重いやけどの恐れ | 確認済み | CPSC 701 | なし |
| 4 | L99 | UL: 先に温めて、ベッドに「入る前に」切る | 誤り(UL は "turn it off before you go to sleep") | UL 記事 | "before you go to sleep" に修正 |
| 5 | L103 | UL の方法=予熱して「下げるか」切る | 誤り(UL は切るとだけ書いている) | UL 記事 | "turn it off before you go to sleep" に修正 |
| 6 | L217 | 最も慎重な方法=予熱して下げるか切る | 誤り(#5 と同じ) | UL 記事 | "which UL recommends … switch it off before you go to sleep" に修正 |
| 7 | L181 | UL は国が認める試験機関の認証品を使うよう勧める | 確認済み | UL 記事 | なし |
| 8 | L202 | UL は乳児・幼い子ども・自分で操作できない人に勧めない | 一部ずれ(UL は「麻痺のある人・安全な操作方法を理解できない人」) | UL 記事 | UL の表現に合わせて修正 |
| 9 | L29 | Sunbeam 説明書: ひざ掛けなど一部の製品はロッキングチェア・リクライナーで使わない | 確認済み(対象は throw と back/body pad) | Sunbeam 説明書 注意13 | なし |
| 10 | L32 | Sunbeam 比較ページ: 敷きパッドは一か所にとどまり夜通し下から温める/毛布は広げて掛ける必要がある | 前半は確認済み(検索抜粋)/後半は未確認 | https://www.sunbeam.com/Heated-Mattress-Pad-vs-Heated-Blanket.html(403、検索抜粋のみ) | 後半「毛布は広げて…」を削除 |
| 11 | L40 | 説明書: ヒーティングパッドではないので平らだと熱く感じない | 確認済み | Sunbeam 説明書 FAQ | なし |
| 12 | L52, L142, L185 | 説明書: 折りたたみ・寄せ集めで過熱/発熱部を tuck in しない | 確認済み | Sunbeam 説明書 注意3・11 | なし |
| 13 | L66, L121, L183, L221 | 説明書: ほかの電気で温める製品と一緒に使わない | 確認済み | Sunbeam 説明書 注意15 | なし |
| 14 | L92, L95, L217 | 説明書: 自動オフは省エネ目的で連続10時間/使わないときは OFF/一部モデルは解除でき StayOn 表示/睡眠中の使用を禁じる・認める一文はない | 確認済み | Sunbeam 説明書 p.8 | なし |
| 15 | L111 | 説明書: 予熱は30分温めて元の設定に戻る | 確認済み(説明書では「selected models only」) | Sunbeam 説明書 p.8 | なし |
| 16 | L22, L73, L111, L125 | Premium Quilted pad: 10段階・10時間自動オフ・予熱 | 確認済み(sunbeam.com 検索抜粋) | https://www.sunbeam.com/on/demandware.store/Sites-sunbeam-Site/default/Product-Variation?pid=MRU5S-MASTER+PMP&dwvar_MRU5S-MASTER+PMP_size=Twin | なし |
| 17 | L111 | ThermoFine は温度の変化を感知して一定に保つ(メーカーの説明) | 確認済み(メーカーの説明として) | https://www.sunbeam.com/on/demandware.store/Sites-sunbeam-Site/default/Content-Show?cid=how-do-heated-blankets-work(検索抜粋) | なし |
| 18 | L113 | Twin は21インチまで/説明書の図で Twin はシングル、Full・Queen・King はデュアル | 確認済み(21インチは sunbeam.com 抜粋、図は説明書) | 上記 / 説明書 p.4-5 | なし |
| 19 | L115, L229 | 洗濯手順: 冷水・弱水流か手洗い、低温・デリケートで乾燥、「slightly damp」で取り出す、洗濯ばさみなしで干す、「coin-operated dryers」不可、完全に乾くまでつながない | 一部ずれ(説明書は "still damp"、"commercial dryers or the dryers at your local laundromat"、干す場所は clothesline か shower rod) | Sunbeam 説明書 p.11 | 説明書の表現に合わせて修正(L115・L229) |
| 20 | L115, L186 | コードをマットレスとボックススプリングの間に通さない/延長コード不可 | 確認済み | Sunbeam 説明書 注意4・9 | なし |
| 21 | L187 | 使用前に毎回点検 | 確認済み | Sunbeam 説明書 注意12 | なし |
| 22 | L188 | 電動リクライニングベッド・ウォーターベッド・二段ベッドで使わない | 確認済み("mechanically adjustable bed") | Sunbeam 説明書 注意14 | なし |
| 23 | L193-200 | 使ってはいけない人(乳児・子ども・動けない人・対麻痺/四肢麻痺・糖尿病・熱を感じにくい人・説明を理解できない/操作できない人) | 確認済み | Sunbeam 説明書 注意2・FAQ | なし |
| 24 | L206-207 | ペースメーカー等は医療者に確認/鎮痛クリーム・塗り薬と併用しない | 確認済み | Sunbeam 説明書 注意21・22 | なし |
| 25 | L229 | コントローラーは洗わない | 確認済み(説明書: コントローラー・コードを水に浸けない、外してから洗う) | Sunbeam 説明書 p.11 | なし |
| 26 | L74, L133, L147 | Quilted Fleece: 10段階・10時間・ポリエステル100%・洗濯機と乾燥機可 | 確認済み(sunbeam.com 検索抜粋) | https://sunbeam.com/heated-bedding/blankets/sunbeam-twin-quilted-fleece-heated-blanket-newport-blue/BRF9GTS-R595-13A44.html | なし |
| 27 | L74, L133 | Quilted Fleece の予熱は未確認 | 未確認(記事も「未確認」と書いている) | — | なし |
| 28 | L137 | 2023年 CPSC が Sunbeam Queen 電気毛布 32810027 のリコールを公表、別会社が流通 | 確認済み(2023-03-16、Star Elite Inc.) | CPSC リコールページ | 「care label」を CPSC の表記「wash label」に修正 |
| 29 | L182 | Sunbeam 製品は型番が care label にある | 一部のモデルのみ(CPSC が書いているのはリコール対象品の wash label だけ) | CPSC リコールページ | 「リコール対象の Sunbeam 毛布は wash label に型番、と CPSC」に修正 |
| 30 | L75, L155, L169 | Serta Plush: 10段階・1〜12時間の自動オフタイマー | 確認済み | https://www.olliix.com/product/data/13954/st54-0091 / Target | なし |
| 31 | L75, L157 | Serta Plush: Twin・Full はコントローラー1つ、Queen・King は2つ/洗濯機可、乾燥は未確認 | 確認済み(乾燥は Olliix に記載なし。Target には乾燥機可とあるが、新しい主張になるため書き足していない) | Olliix / Target | なし |
| 32 | L155 | Serta 電気寝具はライセンス品、Olliix はその卸元 | 未確認(Olliix のページにライセンス・卸の記載なし。Serta のサポートページは電気製品の窓口を JLA Home としている。Olliix のサイトには「Olliix · JLA Home」とある) | https://www.olliix.com/product?c=125 / https://forms.sertasimmons.com/241935101703952(検索抜粋) | 確認できた範囲(Serta は電気製品の窓口を JLA Home としている、仕様は Olliix(JLA Home)のページ)に修正 |
| 33 | L159 | 卸元の在庫表示が古い | 確認済み(「Out of Stock Pre-order」、01/19/2024) | Olliix | なし |
| 34 | L175 | Beautyrest Cotton Blend pad: 5段階・10時間・Twin/Twin XL/Full はコントローラー1つ | 確認済み | Olliix BR55-0671 | なし |
| 35 | L176 | Sunbeam LoftTec: 20段階・予熱。ページ内で段階数の表記が揃っていない | 前半は確認済み(sunbeam.com 抜粋)/後半は未確認(根拠はレビュー欄の指摘のみ) | https://www.sunbeam.com/heated-bedding/blankets/sunbeam-twin-lofttec-heated-blanket-garnet/BRL9STS-R310-16A44.html(検索抜粋) | 「本文を読めず他の仕様を確かめられなかったので外した」に修正 |
| 36 | L177 | Beautyrest Cotton Deep Pocket: 20段階・21インチまで | 確認済み | Olliix BR55-0899 | なし |
| 37 | L67, L162 | 自動オフ: Sunbeam 10時間/Serta 1〜12時間 | 確認済み | 説明書・sunbeam.com 抜粋・Olliix | なし |
| 38 | L233 | 確認した製品では Twin はシングル、Queen 以上でデュアルのものがある | 確認済み | 説明書・Olliix | なし |

集計: 確認済み 28 / 一部のモデルのみ 1 / 未確認 4(#10後半・#27・#32・#35後半)/ 誤り 5(#4・#5・#6、表現のずれ #8・#19 を含む)/ 修正 11 箇所

※ #10・#35 は1行の中に「確認済み」と「未確認」が混在するため、未確認に数えた。#8・#19 は情報源との表現のずれ(誤り扱い)。

## 修正した箇所(修正後の文)
1. L32: 比較ページの要約から未確認の「while a blanket has to be spread out over you」を削除
2. L99: UL の推奨を "switch the blanket off before you go to sleep" に
3. L103: "preheat the bed, then turn it off before you go to sleep"
4. L115: "remove while still damp" / "drape over a clothesline or shower rod without clothespins" / "No commercial or laundromat dryers"
5. L137: "care label" → "wash label"
6. L155: "Serta's support page lists JLA Home as the contact for its heated products; these specs come from the product page of Olliix (JLA Home)."
7. L176: LoftTec を外した理由を "we couldn't read the full product page to check the rest of the specs" に
8. L182: "For the recalled Sunbeam blanket, CPSC says the model number is on the wash label."
9. L202: UL の対象を "anyone who is paralyzed or can't understand how to operate them safely" に
10. L217: "The most cautious routine, which UL recommends, is to preheat, then switch it off before you go to sleep."
11. L229: "removing it while still damp"

フロントマター・アフィリエイトリンク(10本、URL・tag・rel)・CTA ボックスの構造・冒頭と末尾の免責・内部リンクは変更していない。

## 人間確認として残すもの
- Amazon 確認(サイクルログのリスト参照。下に同じ表を置く)
- sunbeam.com の製品ページ本文(403 のため検索抜粋のみ): Premium Quilted Twin のコントローラー数、Quilted Fleece の予熱の有無、比較ページの文言
- Serta Plush の説明書(睡眠中の使用、使ってはいけない人)。参考: Target の商品ページには乾燥機可・ETL 認証と記載あり(記事には書き足していない)

## Amazon 確認リスト(人間用)

### heated-mattress-pad-vs-electric-blanket
| 商品 | 検索リンク | 記事で前提にしていること(形・方式・機能) | 見つからない・ずれのときの対応 |
|---|---|---|---|
| Sunbeam Premium Quilted Heated Mattress Pad(Twin、MRU5S) | https://www.amazon.com/s?k=Sunbeam+Premium+Quilted+Heated+Mattress+Pad+Twin&tag=quietrecover-20 | 電気敷きパッド(マットレスとシーツの間)、10段階、10時間自動オフ、予熱あり、洗濯機・乾燥機可、Twin は21インチまで・コントローラー1つ | 1番目: Beautyrest Cotton Blend Heated Mattress Pad(https://www.amazon.com/s?k=Beautyrest+Cotton+Blend+Heated+Mattress+Pad+Twin&tag=quietrecover-20)。2番目: Sunbeam Water Resistant pad(公式で仕様を再確認できた場合のみ)。「Restful Quilted」など別名しか出ない場合も差し替え |
| Sunbeam Quilted Fleece Heated Blanket(Twin、BRF9) | https://www.amazon.com/s?k=Sunbeam+Quilted+Fleece+Heated+Blanket+Twin&tag=quietrecover-20 | 電気毛布(上に掛ける)、フリース・ポリエステル100%、10段階、10時間自動オフ、洗濯機・乾燥機可、Twin はコントローラー1つ | 1番目: Sunbeam LoftTec Heated Blanket(https://www.amazon.com/s?k=Sunbeam+LoftTec+Heated+Blanket+Twin&tag=quietrecover-20、段階数は人間が公式ページで目視した値を使う)。2番目: Sunbeam Channeled Microplush。リコール対象の Queen 型番 32810027 と取り違えない |
| Serta Plush Heated Blanket(Twin、ST54-0091 ほか) | https://www.amazon.com/s?k=Serta+Plush+Heated+Blanket+Twin&tag=quietrecover-20 | 電気毛布、10段階、自動オフタイマーを1〜12時間で選べる、Twin・Full はコントローラー1つ、洗濯機可 | 1番目: Serta Corded Plush Heated Blanket(https://www.amazon.com/s?k=Serta+Corded+Plush+Heated+Blanket+Twin&tag=quietrecover-20、自動オフ時間は「未確認、出品ページで確認を」と書く)。2番目: Beautyrest Electric Micro Fleece(olliix.com で再確認してから)。Serta を外す場合はタイマーの節を一般論に寄せる |
