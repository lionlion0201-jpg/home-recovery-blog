# 04. ファクトチェック結果(2回目): light-therapy-lamp-vs-sunrise-alarm-clock(2026-11-28)

インプット: docs/agents/fact_checker.md、src/posts/light-therapy-lamp-vs-sunrise-alarm-clock.md、docs/cycles/2026-11-28/03_architect_2.md
Amazon は開いていない(手順どおり)。行番号は記事ファイルの行番号(修正は1行内の書き換えのみで、行番号は修正前後で同じ)。

アクセスできなかったもの(回避していない):
- mayoclinic.org: WebFetch が 403。mayoclinic.org に限定した検索結果の抜粋で確認した
- verilux.com: WebFetch が 429。verilux.com に限定した検索結果の抜粋で確認した
- carex.com: 設計段階で 429。今回は carex.com に限定した検索結果の抜粋で確認した(直接取得は試していない)

## 主な情報源(本文を確認したもの)
- NIMH「Seasonal Affective Disorder」(本文確認): https://www.nimh.nih.gov/health/publications/seasonal-affective-disorder
- Verilux HappyLight Luxe(VT43)説明書 PDF(VT43_MAN_Rev3、2019年、PDF をテキスト化して英語部分を全ページ確認): https://library.douglascollege.ca/sites/default/files/2024-07/vt43_man_rev3_web.pdf
- Alaska Northern Lights NorthStar 10,000 製品ページ(本文確認): https://www.alaskanorthernlights.com/product/north-star-10000/
- NorthStar 10,000 ユーザーガイド PDF(テキスト化して全ページ確認): https://www.alaskanorthernlights.com/wp-content/uploads/pdfs/User-Guide-ANL-North-Star.pdf
- Philips HF3520/60 リーフレット PDF(発行 2026-01-15、テキスト化して全ページ確認): https://www.documents.philips.com/assets/20211230/35c554f242184d17a874ae0e00cf8684.pdf
- Philips HF3520 取扱説明書(検索抜粋。ボタン操作・タップでスヌーズ・日の出の長さ): https://www.documents.philips.com/assets/20211006/db16df37402d4246a018adb900f241c4.pdf
- 検索抜粋のみ: Mayo Clinic https://www.mayoclinic.org/diseases-conditions/seasonal-affective-disorder/in-depth/seasonal-affective-disorder-treatment/art-20048298 / Carex https://carex.com/products/carex-day-light-classic-plus-light-therapy-sun-lamp / Verilux Luxe https://verilux.com/products/happylight-luxe / Verilux Lumi Plus https://verilux.com/products/happylight-lumi-plus / Lumie Vitamin L https://www.lumie.com/en-us/products/vitamin-l-us / Philips goLITE BLU https://www.usa.philips.com/c-p/HF3431_60/golite-blu-energy-light

## ファクトチェック結果: light-therapy-lamp-vs-sunrise-alarm-clock

| # | 行 | 主張(要約) | 判定 | 根拠URL | 対応 |
|---|---|---|---|---|---|
| 1 | L17, L28, L38, L61, L165, L209 | Philips HF3520 は最大 300 lux | 確認済み | Philips リーフレット(Light intensity: 300 Lux) | なし |
| 2 | L52, L74 | Philips は 300 lux に距離を書いていない | 確認済み | Philips リーフレット | なし |
| 3 | L38, L74, L165 | 日の出は 20〜40分で選べる、赤→橙→黄 | 確認済み(製品ページ本文は「30分」とだけ書くが、リーフレット仕様と説明書は 20〜40分) | Philips リーフレット / 取扱説明書 | なし |
| 4 | L165, L74 | 20段階の明るさ、自然音5種+FMラジオ、アラーム2つ、タップでスヌーズ9分 | 確認済み | Philips リーフレット | なし |
| 5 | L165 | アプリなし、本体のボタンで操作 | 確認済み(Controlled by App: No/説明書にアラーム1・2、+/−、Select ボタン) | Philips リーフレット / 取扱説明書 | なし |
| 6 | L74 | 高さ約 7.6 インチ | 確認済み(19.2cm) | Philips リーフレット | なし |
| 7 | L22, L71, L103 | Carex Classic Plus: 10,000 lux at 12–14"、5,000 lux の task 設定 | 確認済み(検索抜粋) | carex.com 製品ページ | なし |
| 8 | L22, L71, L103 | 画面 16"×13"、高さ約22〜31"・角度調整、4000K、UV-filtered、9.35 lbs | 確認済み(検索抜粋。UV は公式内で 100% と 99.3% が食い違うため % は書かない現状のままでよい) | carex.com 製品ページ・コレクションページ | なし |
| 9 | L71, L105 | Carex のタイマー・光源は確認できなかった、公式説明書は入手できなかった | 確認済み(確認できなかった、という記述として正しい) | — | なし |
| 10 | L42 | Verilux 説明書: やや正面から外して置き、直接見ない | 確認済み("slightly off-center"、"Do not look directly into the lamp") | Verilux 説明書 p.8 | なし |
| 11 | L72, L122 | Verilux: 4段階(2,500〜10,000 lux)、3色温度(3,500K/4,250K/5,000K)、タイマー(ワンタッチ1時間・5分刻み) | 確認済み | Verilux 説明書 p.6–7 | なし |
| 12 | L72, L122 | Verilux: 11.7"×7.5"、厚さ約0.5"、2 lbs、スタンド着脱・壁掛け可、UV-free | 確認済み(寸法・重さ・UV は verilux.com 検索抜粋、壁掛けは説明書 p.9) | verilux.com 製品ページ / 説明書 p.9 | なし |
| 13 | L122 | 説明書に ETL Listed(米国・カナダ) | 確認済み | Verilux 説明書 p.11 | なし |
| 14 | L72, L90, L124 | 10,000 lux は 6 インチでの値。説明書は顔から 6〜24 インチに置くよう説明 | 確認済み("10,000 lux (photopic measurement) at 6""/"as close as 6 inches but within 24 inches") | Verilux 説明書 p.8・10 | なし |
| 15 | L126 | 説明書の注意: 薬(抗うつ薬の例)・精神疾患で光に敏感になり、不快感・"overactivity"・軽躁 | 誤り(一部ずれ: 説明書は "hyperactivity") | Verilux 説明書 p.3・9 | "hyperactivity" に修正 |
| 16 | L126 | 眼の持病・黄斑変性のリスク→医療者へ/初回は約18インチで約10分、不快なら医師へ/調光器・タイマー・人感センサーにつながない | 確認済み | Verilux 説明書 p.3・9 | なし |
| 17 | L93 | Verilux 説明書: 低い設定から始めて上げていける | 確認済み | Verilux 説明書 p.6 | なし |
| 18 | L200 | 頭痛や眼の不快があれば中止(Verilux 説明書の助言として) | 誤り(一部ずれ: 説明書は「何らかの不快があれば中止」。頭痛・眼の不快という限定は説明書に無い) | Verilux 説明書 p.3・9 | 「The light makes you uncomfortable. Stop using it, as the Verilux manual advises; its first-use pretest says to see a doctor…」に修正(説明書の範囲に合わせた) |
| 19 | L50, L73, L90, L139, L143 | NorthStar: 10,000 lux at 24"、約40インチで約2,500 lux | 確認済み | NorthStar 製品ページ / ガイド p.5・9 | なし |
| 20 | L143 | ガイドの使い始め: 最初の週は約40インチ・15分、1週間かけて24インチ・30分へ | 確認済み | NorthStar ガイド p.9 | なし |
| 21 | L73, L143 | NorthStar: 製品ページに明るさ段階・タイマーの記載なし | 確認済み | NorthStar 製品ページ | なし |
| 22 | L73, L145 | 蛍光管2本(broad-spectrum)、4100K、UV-free、3年で電球交換を勧める、約2フィート幅・10 lbs、縦置き・横置き・壁掛け | 確認済み | NorthStar 製品ページ / ガイド p.5・11 | なし |
| 23 | L147, L190, L221 | ガイド: 眼の病気・家族歴→眼科医へ/日光を避ける薬→薬剤師か医師に確認/夜遅い使用は睡眠に影響しうる | 確認済み | NorthStar ガイド p.11 | なし |
| 24 | L147 | 「The brand mainly sells direct」 | 未確認(製品ページは自社サイトでの販売を示すが、「主に直販」と言える情報は無い) | NorthStar 製品ページ | 「Alaska Northern Lights sells it on its own site」に弱めた |
| 25 | L90 | Alaska Northern Lights は距離の書かれていない 10,000 lux 表示に注意を促している | 確認済み("Only buy a light unit that specifies a distance for 10,000 Lux!") | NorthStar 製品ページ | なし |
| 26 | L44, L190, L221 | NIMH: 冬型 SAD の光療法は 10,000 lux の light box の前に毎日約30〜45分、多くは朝起きてすぐ、秋から春まで | 確認済み | NIMH | なし |
| 27 | L92 | NIMH: SAD 用の light box は UV を除いている/皮膚用ランプは別の機器 | 確認済み(前半 NIMH 本文、後半は Mayo 検索抜粋「皮膚の病気用のランプは主に UV を出す」) | NIMH / Mayo Clinic | なし |
| 28 | L196 | NIMH は治療の利点とリスクを医療者と話すよう勧める | 確認済み(治療の節の冒頭) | NIMH | なし |
| 29 | L196, L225 | Mayo Clinic: 医療者の指導のもとで使うのがよい/処方なしで買える | 確認済み(検索抜粋のみ。403 で本文未目視) | Mayo Clinic | なし |
| 30 | L197 | 眼の病気の例「glaucoma, cataracts, retinal disease, macular degeneration」、出典は NIMH・Verilux・NorthStar | 誤り(一部ずれ: 「retinal disease」はどの出典にも無い。緑内障・白内障・糖尿病による眼の障害は Mayo、黄斑変性は Verilux。NIMH は「certain eye diseases」) | Mayo Clinic(抜粋)/ Verilux 説明書 p.3 / NIMH / NorthStar ガイド | 「retinal disease」を「eye damage from diabetes」に置き換え、出典に Mayo Clinic を加えた |
| 31 | L198 | 光に敏感になる薬→医師・薬剤師へ(NIMH・Verilux・NorthStar) | 確認済み | NIMH / Verilux 説明書 p.3 / NorthStar ガイド p.11 | なし |
| 32 | L199 | 双極性障害: Mayo は注意を促す/Verilux は軽躁の可能性に触れる | 確認済み(Mayo は検索抜粋のみ。NIMH の光療法の節には双極性障害の記載なし=記事も NIMH の言葉にしていない) | Mayo Clinic(抜粋)/ Verilux 説明書 p.3 | なし |
| 33 | L213 | Mayo: 距離はメーカーの指示に従う | 確認済み(検索抜粋のみ) | Mayo Clinic | なし |
| 34 | L221 | NIMH と Mayo は朝の使用として説明 | 確認済み(Mayo は「起床後1時間以内」検索抜粋) | NIMH / Mayo Clinic | なし |
| 35 | L181 | Lumie Vitamin L: 10,000 lux at 20cm、5,000 at 30cm、2,500 at 50cm、明るさ固定 | 確認済み(検索抜粋) | lumie.com | なし |
| 36 | L182 | Verilux Lumi Plus: 明るさ3段階・タイマー・色の調整なし | 誤り(一部ずれ: 3段階・タイマーは確認。「色の調整なし」は公式に書かれておらず、色温度の記載が無いだけ) | verilux.com Lumi Plus(検索抜粋) | 「with no color setting listed」に修正 |
| 37 | L182 | Verilux の公式サイトで在庫切れ表示のことがある | 確認済み(検索抜粋で "Sold Out / Notify Me When Available"。直接取得は 429) | verilux.com Lumi Plus | なし |
| 38 | L183 | Philips goLITE BLU は米国サイトで販売終了表示 | 確認済み(HF3431/60 が Discontinued、HF3429/60 も生産終了の表示。検索抜粋) | usa.philips.com | なし |

照合対象外としたもの: lux が距離で下がるという一般論(L48)、比較表1の「Check with a doctor first if…」の目覚まし側の欄(L65。商品・機関の主張ではない一般的な注意)、「24 inches is a little beyond arm's length」(L91。一般的な説明)。

健康面の表現: 「治る」「気分が良くなる」「眠りが良くなる」などの断定は無い。メーカーの宣伝文句(Philips の clinically proven・improves your mood、NorthStar ガイドの completely safe・Doctor Recommended・Medical Grade、Verilux の lift spirits・feel an improvement in your mood)はどれも記事に入っていない。FDA の記述も無い。NIMH の 30〜45分は「NIMH describes」の形で、読者への指示になっていない。

集計: 確認済み 33 / 一部のモデルのみ 0 / 未確認 1 / 誤り 4(いずれも一部の言い回しのずれ) / 修正 5 箇所(L126・L147・L182・L197・L200)

## 人間確認として残すもの
- Amazon 確認(サイクルログのリスト参照。下の「Amazon 確認リスト」と同じ内容)
- Mayo Clinic の本文目視(403 のため検索抜粋のみ): 医療者の指導・処方なしで買える(L196・L225)、眼の病気の例(L197)、双極性障害(L199)、距離はメーカーの指示に従う(L213)、朝の使用(L221)、皮膚用ランプと UV(L92)
- Carex の公式説明書(タイマーの有無・光源・注意事項)。carex.com は検索抜粋のみ
- Verilux Luxe の現行説明書が今回読んだ版(VT43_MAN_Rev3、2019年)と同じか

## Amazon 確認リスト(人間用)

`python3 scripts/list_amazon_links.py` の出力から作成(4本すべて tag_ok: true)。

| 商品 | 検索リンク | 記事で前提にしていること(形・方式・機能) | 見つからない・ずれのときの対応 |
|---|---|---|---|
| Carex Day-Light Classic Plus(CCFDL93011) | https://www.amazon.com/s?k=Carex+Day-Light+Classic+Plus+light+therapy+lamp&tag=quietrecover-20 | 据え置きの大画面ランプ。画面 16"×13"、高さ・角度調整。10,000 lux at 12–14"、5,000 lux の2段階、4000K。出品名に "Classic Plus" と型番 CCFDL93011 があること | 1番目: Lumie Vitamin L に差し替え(条件: Amazon US に現行品があり、評価4.0以上かつレビュー100件以上)。満たさなければ差し替えず、ランプ2つにする。Day-Light Sky・Elite・SunLite など名前の似た別モデルに置き換えない |
| Verilux HappyLight Luxe(VT43) | https://www.amazon.com/s?k=Verilux+HappyLight+Luxe&tag=quietrecover-20 | 薄型の卓上・壁掛けランプ。4段階(2,500〜10,000 lux)、3色温度、タイマー(1時間・5分刻み)。10,000 lux は 6" での値。出品名に "Luxe" と型番 VT43(色違い VT43WW3・VT43MB3・VT43CG3)があること | 1番目: Verilux HappyLight Lumi Plus(条件: 同上+在庫あり。比較表の色温度は「設定なし」、タイマーは15分刻みに直す)。2番目: Lumie Vitamin L(同条件)。Lumi / Lucent / Touch / Alba / Halo など似た名前の別モデルに注意 |
| Alaska Northern Lights NorthStar 10,000 | https://www.amazon.com/s?k=Alaska+Northern+Lights+NorthStar+10000&tag=quietrecover-20 | 大型のボックス型ランプ(蛍光管2本、4100K)。10,000 lux at 24"。明るさ段階・タイマーなし。約2フィート幅・10 lbs。メーカー直販が中心で Amazon にあるか不明 | 差し替えず、ランプ2つにする(Also Looked At に1文で残し、リンクは外す)。外した場合、「距離」の節は Verilux と Carex の2つで書く |
| Philips SmartSleep Wake-up Light(HF3520/60) | https://www.amazon.com/s?k=Philips+SmartSleep+Wake-up+Light+HF3520&tag=quietrecover-20 | 光目覚まし。最大 300 lux、20段階、日の出 20〜40分、音5種+FM、アプリなし(本体ボタン)、タップでスヌーズ。出品名に HF3520 があること | 1番目: 既存 sunrise 記事と同じ検索リンク https://www.amazon.com/s?k=Philips+SmartSleep+Wake-up+Light&tag=quietrecover-20 に戻し、300 lux・20段階など HF3520 固有の数字を外す。2番目: 目覚まし側の商品を置かず、sunrise 記事へのリンクだけにする。HF3505・HF3650(Somneo)など型番違いは仕様が違うので注意 |
