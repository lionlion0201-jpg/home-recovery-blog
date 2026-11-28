# 04. ファクトチェック結果(3回目): microwavable-neck-wrap-vs-electric-heating-pad(2026-11-28)

インプット: docs/agents/fact_checker.md、src/posts/microwavable-neck-wrap-vs-electric-heating-pad.md、docs/cycles/2026-11-28/03_architect_3.md
Amazon は開いていない(手順どおり)。行番号は記事ファイルの行番号(修正は1行内の書き換えのみで、行番号は修正前後で同じ)。

アクセスできなかったもの(回避していない):
- sunbeam.com: WebFetch が 403。sunbeam.com に限定した検索の抜粋で確認
- comfytemp.com・carex.com: WebFetch が 429。各ドメインに限定した検索の抜粋で確認
- pureenrichment.com・fda.gov の Mighty Bliss 安全情報: 今回は取得を試さず、ドメイン限定の検索抜粋で確認

## 主な情報源
本文を確認したもの:
- Sunbeam Neck Renue(Sunbeam の商品情報配信ページ、Material 2137638): https://sites.salsify.com/41c9c255-1884-40e0-bc05-ad8dd5617744/c662aea6-b860-4545-ab16-2118694bf473/en-US/product/SAP_2137638/Sunbeam(r)-Neck-Renue(r)-Heat-Wrap/ (4段階・2時間自動オフ・9フィート・高い襟・重りつきの端・磁石の留め具・Micromink。LED・寸法・洗濯はこのページに無い)
- CPSC Publication 701(PDF をテキスト化して確認。"Always turn off your heating pad before you go to sleep. It can cause serious burns even at relatively low settings."): https://www.cpsc.gov/s3fs-public/701.pdf
- FDA Navajo 首肩用パッドのリコール(Class I、2026-03-25。折った部分で電力密度が上がり、過熱を検知できない): https://www.fda.gov/medical-devices/medical-device-recalls-and-early-alerts/heating-pad-recall-navajo-manufacturing-company-removes-handy-solutions-neck-shoulders-heating-pad
- University of Utah Health: https://healthcare.utah.edu/the-scope/health-library/all/2018/11/heating-pads-can-cause-second-degree-burns (痛み・こり・血流への効果は書かれていない)
- Bed Buddy 説明書 PDF(Product # BBF2000。PDF をテキスト化して確認): https://cdn.shopify.com/s/files/1/0240/6504/8681/files/BB_BodyWrap_Instructions.pdf

検索抜粋のみ:
- Sunbeam Neck Renue(sunbeam.com): https://www.sunbeam.com/pain-relief/neck-and-shoulder-pain/neck-renue-heat-wrap/SAP_2137638.html (22×19インチ、LED 表示つき押しボタン、9フィート、洗濯機可・コントローラーを外す・cool water・gentle cycle・漂白剤とドライクリーニング不可・乾くまでつながない、model 700-825-001、75W)
- Comfytemp K9306: https://comfytemp.com/products/comfytemp-neck-shoulder-microwavable-heating-pad (800W 3〜4分/1200W 2〜3分/合計5分を超えない/W数不明なら2分から・温め直しは前回の半分/15〜20分温かい/2.8ポンド/linseed clay beads and adzuki beans)
- Comfytemp 電子レンジ式パッドのコレクションページ(FAQ。冷蔵庫でひんやり/外側を湿らせた布で拭く/洗濯機不可/天然の詰め物は浸けない): https://comfytemp.com/collections/microwave-heating-pad
- Comfytemp 安全ページ: https://comfytemp.com/blogs/news/how-to-safely-use-microwavable-heating-pad (「焦げたにおいは過熱」「温熱器具をつけたまま寝ない」の記載あり)
- Comfytemp K9015(電気・加重): https://comfytemp.com/products/wyj-weighted-heating-pad-for-neck-and-shoulders (micro-glass beads、2.6ポンド、9段階、自動オフ11通り)
- Bed Buddy Hot & Cold Wrap 2個組: https://carex.com/products/bed-buddy-hot-cold-wrap-two-pack (600W 1:15/900W 0:50/1200W 0:37・1分置く/natural grains, herbs, and flowers/冷凍庫で数時間/首・腕・脚・背中)
- Bed Buddy Hot & Cold Wrap 1個売り: https://carex.com/products/bed-buddy-microwaveable-neck-wrap (加熱時間は抜粋に出ず未確認。中身は「小麦50%・大豆50%・ラベンダー1%未満」と2個組と違う記載の可能性)
- Pure Enrichment PureRelief Neck & Shoulder: https://pureenrichment.com/products/purerelief-neck-shoulder-heating-pad (4段階・120分自動オフ・9フィート・コントローラーを外して洗濯機可)
- FDA Mighty Bliss 安全情報(一番低い設定から・15〜20分・つけたまま寝ない): https://fda.gov/medical-devices/safety-communications/do-not-use-certain-mighty-bliss-electric-heating-pads-due-risk-injury-fda-safety-communication

## ファクトチェック結果: microwavable-neck-wrap-vs-electric-heating-pad

| # | 行 | 主張(要約) | 判定 | 根拠URL | 対応 |
|---|---|---|---|---|---|
| 1 | L22, L46, L64, L74, L82, L132, L146 | Sunbeam Neck Renue: 電気式・4段階・2時間で自動オフ | 確認済み | salsify(本文)/ sunbeam.com(抜粋) | なし |
| 2 | L48, L65, L74, L132, L146 | Sunbeam のコードは 9 フィート | 確認済み | salsify(本文)/ sunbeam.com(抜粋) | なし |
| 3 | L132 | LED 表示、22×19インチ、後頭部まで覆う高い襟 | 確認済み(LED・寸法は sunbeam.com 抜粋のみ。襟は salsify 本文) | sunbeam.com / salsify | なし |
| 4 | L46, L54, L132 | 磁石の留め具と重りつきの端、表地 Micromink | 確認済み | salsify(本文) | なし |
| 5 | L134, L74, L252 | 洗濯機可: コントローラーを外す・冷水・弱水流・漂白剤とドライクリーニング不可・完全に乾くまでつながない | 誤り(一部ずれ: 公式は "cool water"。ほかは一致) | sunbeam.com(抜粋) | "cold water" → "cool water" |
| 6 | L136 | Sunbeam の説明書は入手できなかった/冷やして使えない | 確認済み(入手できなかった、という記述として正しい。冷却はカテゴリ一般の性質) | — | なし |
| 7 | L40, L75, L156, L236 | Comfytemp K9306: 800W 3〜4分/1200W 2〜3分/最大5分 | 確認済み(検索抜粋。設計時と今回の2回、同じ値) | comfytemp.com K9306(抜粋) | なし(人間の目視照合を残す) |
| 8 | L156 | 初回やW数不明なら2分から、温め直しは前回の半分 | 誤り(一部ずれ: 公式抜粋は「W数不明なら2分から」。「初回」の記載は確認できず) | comfytemp.com K9306(抜粋) | "For the first use, or" を削除 |
| 9 | L42, L123, L156 | Comfytemp は約15〜20分温かいと説明 | 確認済み | comfytemp.com K9306(抜粋) | なし |
| 10 | L54, L154 | Comfytemp は 2.8 ポンドの加重タイプ | 確認済み | comfytemp.com K9306(抜粋) | なし |
| 11 | L75, L154, L168 | 中身は亜麻仁(linseed)とクレイビーズ、一部に小豆(red beans) | 一部のモデルのみ(公式抜粋は "linseed clay beads and adzuki beans"。小豆がバリエーション限定かは未確認) | comfytemp.com K9306(抜粋) | なし(本文はすでに "some versions … check the listing" の形) |
| 12 | L75, L158, L248 | Comfytemp は冷蔵庫で冷やせる(冷凍の記載なし) | 一部のモデルのみ(冷蔵庫の記載は電子レンジ式パッド全般の FAQ。K9306 のページでは未確認) | comfytemp.com コレクション(抜粋) | L158 を「Comfytemp's FAQ for its microwavable pads says…」に修正 |
| 13 | L67, L75, L158, L252 | Comfytemp は洗えない(湿らせた布で拭く・浸けない・洗濯機不可) | 一部のモデルのみ(同上、電子レンジ式全般のケア説明。別の掲載で「手洗い」をすすめる記載があるとの抜粋もあり) | comfytemp.com コレクション(抜粋) | L158 を「care guidance for microwavable pads says… check the label on yours」に修正 |
| 14 | L40, L76, L178, L236 | Bed Buddy: 600W 1:15/900W 0:50/1200W 0:37、加熱後1分置く(2個組のページ) | 確認済み(2個組ページの抜粋。1個売りページの値は未確認。本文はすでに「two-pack's product page」と出典を明記) | carex.com 2個組(抜粋) | なし(人間の目視照合を残す) |
| 15 | L76, L176, L190 | Bed Buddy の中身は天然の穀物・ハーブ・花 | 一部のモデルのみ(2個組ページの記載。1個売り・別のネックラップの掲載は「小麦・大豆・ラベンダー」と読める) | carex.com 2個組 / 1個売り(抜粋) | L176 に「on the two-pack's product page … check the label」、L76 の表に「(two-pack page; check the label)」 |
| 16 | L76, L178, L248 | Bed Buddy は冷凍庫で数時間、温めと冷凍を切り替えられる | 確認済み | carex.com 2個組(抜粋) | なし |
| 17 | L180 | 首・腕・脚・背中に使える/湿らせた布で拭く・洗わない | 確認済み | carex.com 2個組(抜粋)/ Bed Buddy 説明書 PDF | なし |
| 18 | L176 | Bed Buddy は Carex 製 | 確認済み | carex.com | なし |
| 19 | L93–101, L203–205 | Bed Buddy 説明書(ボディラップ用): 過熱しない・オーブン機能を使わない・清潔で空の皿に平らに・目を離さない・中身を動かして熱い所を確かめる・食べ物や液体の汚れで過熱・位置を変え続ける・目の上にのせない | 確認済み | Bed Buddy 説明書 PDF(BBF2000、本文) | なし |
| 20 | L214–219 | Bed Buddy 説明書: 神経障害・血行の問題・敏感な肌・傷のある肌の人、自分で外せない人(乳児・子ども・一部の高齢者)に使わない/妊娠中・持病は医師に相談 | 確認済み(原文は "nerve damage"。"neuropathy" は原文に無い語) | Bed Buddy 説明書 PDF | "neuropathy (nerve damage)" → "nerve damage" |
| 21 | L118, L240 | 電子レンジのラップについて、メーカーの睡眠に関する記載は見つからなかった | 誤り(Comfytemp の安全ページに「温熱器具をつけたまま寝ない」とある、との検索抜粋) | comfytemp.com 安全ページ(抜粋) | 「見つからなかった」の文を削除。結論「眠りそうなら使わない」は残す |
| 22 | L116, L142, L209, L240 | CPSC: 寝る前にヒーティングパッドを切る。比較的低い設定でも重いやけど | 確認済み | CPSC 701(PDF 本文) | なし |
| 23 | L108, L208 | FDA の Class I リコール(首肩用パッド): 折ると電力が集中し、過熱を検知できない | 誤り(一部ずれ: 説明はリコール通知中の製造元の説明。「FDA explained」より「FDA の通知が説明」が正確) | FDA Navajo リコール(本文) | "An FDA Class I recall notice … explains that folding raises the power in the folded area, where the pad may not detect the extra heat." に修正 |
| 24 | L50 | University of Utah Health: 同じ場所に当て続けると数時間でやけどしうる | 確認済み | Utah Health(本文) | なし |
| 25 | L109 | University of Utah Health: 折る・巻き付けるのは危険 | 確認済み(折る・巻き付けると電気的な危険がある、という趣旨) | Utah Health(本文) | なし |
| 26 | L116, L221 | Utah Health: 寝落ちがやけどの原因/高齢者が最もリスクが高い/乳児に使わない/麻痺のある人は熱さに気づけない | 確認済み | Utah Health(本文) | なし |
| 27 | L107, L110 | 一番低い設定から・短時間/傷んでいたら使わない | 確認済み(FDA Mighty Bliss 安全情報の抜粋。本文には機関名を出していない) | FDA Mighty Bliss(抜粋) | なし |
| 28 | L196 | PureRelief: 4段階・120分で自動オフ・9フィート・コントローラーを外して洗濯機可 | 確認済み | pureenrichment.com(抜粋) | なし |
| 29 | L197 | Comfytemp の電気加重パッド: ガラスビーズ・「longer timer options」 | 誤り(一部ずれ: 公式は「自動オフ11通り」。「長い」は小売店の 0.5〜9時間に基づく比較で、公式では未確認) | comfytemp.com K9015(抜粋) | "several auto-off timer options" に修正 |
| 30 | L198 | Warmies・Huggaroo はメーカー公式で加熱時間を確認できなかった | 確認済み(調査の記述として正しい。設計図どおり) | — | なし |
| 31 | L32, L244, L15 ほか | 健康面: 治療ではない・心地よいと感じる人がいる、の範囲 | 確認済み(痛み・こり・血流への効果の断定なし。メーカーの効能表現の引用なし) | — | なし |

集計: 確認済み 22 / 一部のモデルのみ 4 / 未確認 0 / 誤り 5 / 修正 10 箇所

(#20 は内容は確認済みで、語を原文に合わせただけなので確認済みに数えた。誤りは #5・#8・#21・#23・#29。いずれも「一部ずれ」を含む)

### 電子レンジの加熱時間について
- 記事に残した数字は Comfytemp K9306(800W・1200W・最大5分・2分から)と Bed Buddy 2個組(600W・900W・1200W・1分置く)だけ。どちらもメーカー公式ドメインの検索抜粋で、設計時と今回で同じ値が出た。本文取得は 429 で不可(回避していない)
- Bed Buddy の1個売りページの時間は確認できていない。本文は「from the two-pack's product page」と出典を明記し、毎回「Follow the instructions for your microwave wattage on the label」を添えている
- 人間の目視照合で値が違えば、表2(L75・L76)・L156・L178・FAQ(L236)の数字を削り、"follow the heating time on the label for your microwave's wattage" の形にする

## 人間確認として残すもの
- Amazon 確認(サイクルログのリスト参照。下の「Amazon 確認リスト」)
- comfytemp.com の K9306 ページを目視: 加熱時間(800W 3〜4分/1200W 2〜3分/5分以内/2分から・半分)、2.8ポンド、冷蔵庫の記載、お手入れ(拭くだけか、手洗い可か)
- carex.com の Bed Buddy Hot & Cold Wrap 1個売りページを目視: 加熱時間が2個組と同じか、中身の記載(穀物・ハーブ・花か、小麦・大豆・ラベンダーか)
- sunbeam.com の Neck Renue ページを目視: 22×19インチ・LED・洗濯手順(sunbeam.com は 403 で抜粋のみ)

## Amazon 確認リスト(人間用)

記事: microwavable-neck-wrap-vs-electric-heating-pad(`python3 scripts/list_amazon_links.py` の結果。3本とも tag_ok: true)

| 商品 | 検索リンク | 記事で前提にしていること(形・方式・機能) | 見つからない・ずれのときの対応 |
|---|---|---|---|
| Sunbeam Neck Renue Heat Wrap(L23・L82・L147・L265) | https://www.amazon.com/s?k=Sunbeam+Neck+Renue+Heat+Wrap&tag=quietrecover-20 | 電気式(コンセント)の首肩用ラップ。4段階・2時間で自動オフ・9フィートのコード・22×19インチで後頭部まで覆う高い襟・磁石の留め具と重りつきの端・コントローラーを外して洗濯機可。**マッサージ(振動)機能なし**。旧型 Renue Heat Wrap(22×14)や Massaging Renue と混ざっていないか | 1番目: Pure Enrichment PureRelief Neck & Shoulder Heating Pad に差し替え(https://www.amazon.com/s?k=Pure+Enrichment+PureRelief+Neck+Shoulder+Heating+Pad&tag=quietrecover-20)。2番目: Sunbeam Renue Heat Wrap(旧型、22×14)。マッサージつきの Renue は使わない |
| Comfytemp Microwavable Neck & Shoulder Heating Pad(L83・L169・L266) | https://www.amazon.com/s?k=Comfytemp+Microwavable+Neck+Shoulder+Heating+Pad&tag=quietrecover-20 | 電子レンジ式・コードなし。首肩用の形(K9306)。亜麻仁とクレイビーズ(小豆入りもあり)・2.8ポンドの加重タイプ・洗えない(拭くだけ)。K9305(33×4の細長い型)・K9304(12×23の平ら型)や電気式の K9015 と取り違えない | 構成を「ラップ1(Bed Buddy)+電気2(Sunbeam+PureRelief)」に変える。2番目: Warmies Microwavable Neck Wrap(人間がパッケージか公式ページで加熱時間を目視できた場合だけ) |
| Bed Buddy Hot & Cold Wrap(L84・L191・L267) | https://www.amazon.com/s?k=Bed+Buddy+Hot+Cold+Wrap&tag=quietrecover-20 | 電子レンジ式・冷凍もできる・コードなし。Carex 製。洗えない(拭くだけ)。1個売りか2個組か(加熱時間は2個組の公式ページの値) | 構成を「ラップ1(Comfytemp)+電気2(Sunbeam+PureRelief)」に変える。Bed Buddy Neck & Hand Wrap は採用しない(使うなら Also Looked At に1文だけ) |

## 再確認(差し戻し後)

対象: 05_director_3.md の差し戻しを受けてレビュワーが書き換えた L40・L75・L76・L78・L156・L178・L184・L236 のみ。WebSearch は使っていない(上の照合結果と 03_architect_3.md の範囲で判断できたため)。Amazon・ブラウザは開いていない。行番号は修正前後で同じ(1行内の書き換えのみ。記事は270行のまま)。

| # | 行 | 書き換え後の主張(要約) | 判定 | 根拠 | 対応 |
|---|---|---|---|---|---|
| R1 | L40 | 加熱時間は商品と電子レンジのW数で大きく違い、同じブランド内でも違う。ラベルの時間に従う | 確認済み(抜粋) | 上の #7(K9306)と 03_architect_3 L66(K9304 は別の時間)。数字は書いていない | なし |
| R2 | L75 | 表2 Comfytemp の加熱欄: "Microwave; see the label for your wattage" | 確認済み(数字なし。ラベルに従う案内のみ) | — | なし |
| R3 | L76 | 表2 Bed Buddy の加熱欄: 同上。"rest 1 min" も削除済み | 確認済み(数字なし) | — | なし |
| R4 | L78 | 手元の商品のラベルのW数ごとの時間に従う | 確認済み(一般的な案内。新しい主張なし) | — | なし |
| R5 | L156 | Comfytemp は電子レンジのW数ごとに加熱時間を示している/約15〜20分温かい | 確認済み(抜粋) | 上の #7(K9306 ページに 800W・1200W 別の時間)、#9 | なし(15〜20分は 05 の軽い指摘2どおり残し、人間確認で照合) |
| R6 | L178 | Bed Buddy は電子レンジのW数ごとに加熱時間を示している/冷凍庫で数時間 | 一部のモデルのみ(W数別の時間は2個組ページの抜粋のみ。1個売りページは未確認=#14) | carex.com 2個組(抜粋)、#16 | "Bed Buddy gives…" → "Bed Buddy's two-pack page gives…" に修正 |
| R7 | L184 | 電子レンジ式は自然に冷めるので温め直しが前提 | 対象外(カテゴリ一般の性質) | — | なし |
| R8 | L236 | FAQ: 商品とW数で違う。別の商品の時間を流用せずラベルに従う | 確認済み(数字なし。新しい主張なし) | — | なし |

全体の確認:
- **加熱時間の数字: 残っていない。** 記事全体を「数字+min/minute/sec/second/W/watt」「1:15 形式」「half the previous」「rest … for」で検索。残る時間の数字は「温かさが続く約15〜20分」(L42・L123・L156)だけで、05 の軽い指摘2で残してよいとされたもの。加熱時間・W数の数字は0件
- **健康効果の断定・価格: 持ち込まれていない。** `$`・% off・deal・coupon・cures・pain relief 等は0件。書き換え8行に効能の表現なし
- 書き換え8行で、上の照合の範囲を超える新しい主張は無し(R6 は出典の範囲に合わせて表現を狭めた)

集計(再確認): 確認済み 6 / 一部のモデルのみ 1 / 未確認 0 / 誤り 0 / 対象外 1 / 修正 1 箇所(L178)

人間確認として残すもの: 上の「人間確認として残すもの」から変更なし(加熱時間の目視照合は、記事から数字を削ったので公開の条件からは外れる。15〜20分と1個売りページの記載は引き続き目視)
