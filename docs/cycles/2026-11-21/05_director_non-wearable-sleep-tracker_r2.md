# 05. ディレクター判定: non-wearable-sleep-tracker(r2 / 2026-11-23、2回目)

対象: src/posts/non-wearable-sleep-tracker.md(r1 差し戻し3点の修正後)
照合資料: 共通ルール(再読)、docs/agents/director.md、docs/agents/reviewer.md、03_architect 設計図、04_factcheck(末尾「差し戻し後の再確認」節を含む)

## 照合した共通ルールの見出し
- チーム全員が守ること
- サイトの声(文体・一人称・価値観)
- 絶対NG表現
- 訴求の優先順位
- セール記事・価格の書き方(2026-09-29決定)(守ること / 既存記事の棚卸し / 自動チェック)
- 読者への姿勢
- 各エージェントの境界
- 運用改善ルール

## 判定: 承認

### r1 指摘の解消
- 指摘事項1(L41 見出し): "Wellness Trackers, Not Diagnostic Tools" に変更済み。本文 L43 と一致。再確認 R1 で確認済み
- 指摘事項2(L254 末尾免責): "made for wellness tracking; their numbers are estimates, and they can't diagnose sleep disorders" に変更済み。L234 と一致。再確認 R2 で確認済み
- 指摘事項3(L192): "A Withings pad and a Nest Hub each track one person." に限定済み。比較表(Sleepal は "Check with the maker")と矛盾なし。再確認 R3 で確認済み
- 上の3か所以外に新しい事実の主張は加わっていない(ファクトチェッカーが差分で確認、ディレクターも全文を再読)

### 承認の場合
- プロモーターへ引き渡し可能(ただし最終的な公開承認は人間が行う。下の人間確認を先に済ませること)

## チェックリスト照合結果(全体を再判定)
- [x] 共通ルールとの整合: ジャンル内、"we" で統一、ハイプのない buyer's guide 口調。冒頭で「実際には使っていない」と明記
- [x] 設計図からの逸脱: 「The 3 Picks」→「The Picks」、Nest Hub を条件付きの3番目に移動(オーケストレーターの方針どおり)。L41 見出しの変更はファクトチェック結果に基づくもので可
- [x] 絶対NG表現: 誇大な断定・医療効果の断定・一人称の虚偽体験・根拠のない数字なし(Sleepal の自社精度値は引用しないと明記)
- [x] 「向いていない人」: 各商品の "Who it may not suit" と H2「Who a Non-Wearable Sleep Tracker Isn't For」
- [x] rel="nofollow sponsored": Amazon リンク7本すべて
- [x] tag=quietrecover-20: 7本すべて(list_amazon_links.py で検索語3種とも tag_ok=true)
- [x] 内部リンク形式: 7本すべて `{{ '/posts/xxx/' | url }}`。リンク先7記事はすべて公開済み
- [x] 未設定 ASP のプレースホルダー: なし
- [x] タイトル・説明文の重複: 既存記事と重複なし
- [x] フロントマター: layout/title/description/date/tags/category あり。published: false / permalink: false / eleventyExcludeFromCollections: true
- [x] 価格: 手書きの金額・値引き率・クーポン・送料無料・セール名なし。価格は budget / mid-range / premium のみ。サブスクは金額なし。review_lib の check_article・check_amazon_policy とも指摘ゼロ
- [x] CTA ボックス: `<div class="cta-box">` 形式で4か所
- [x] FTC 開示: 冒頭
- [x] 医療免責: 冒頭・H2「A Note on Health and Accuracy」・末尾
- [x] 「気になる症状は医師へ」: L112・L203・L210・L236・L245・L254
- [x] 睡眠時無呼吸・FDA の書き分け: 市販の Withings Sleep(U.S.)は無呼吸検出なし、FDA 510(k) は医療機関向けの別製品 Sleep Rx と分けて書かれている
- [x] 検索語: "non-wearable sleep tracker" はタイトル・H2・説明文に、"under-mattress sleep tracker" は H2・FAQ に自然に入っている
- [x] ファクトチェックの未確認項目: 断定のまま残っているものはない。未確認のものは「at the time of writing」「check the current terms」等の言い回しで残すか、人間確認に回されている

## 人間確認として残す項目(公開前に人間が行う)
1. Amazon での取り扱い・新品在庫・評価・レビュー数(Withings Sleep / Sleepal AI Lamp / Nest Hub 2nd Gen の3つの検索リンク)。AI のアクセスが拒否されたため3週連続で未実施。Sleepal が Amazon に無い場合の CTA の扱いは人間が判断
2. Google 米国ストアで Nest Hub (2nd gen) が全色在庫切れかどうか(L83・L160 の「執筆時点」の記述)
3. Withings 公式ページの目視(403 で読めなかった): U.S. 版の対応 OS、マットレス 4〜15インチ(出典は Sleep Analyzer 版 FAQ)、Withings+ なしで履歴・傾向が見られる文言、1枚で1人(公式の記載は未発見で、小売ページで確認)
4. Sleepal: 購入に含まれる「1 Year Subscription」の対象プラン、電源アダプタ
5. Sleep Sensing の preview が続いているか
6. 公開日(publishAt)の設定と公開フラグの切り替え

## 運用改善メモ
Amazon 確認が3週連続で人間確認に回っている。共通ルールの「運用改善ルール」(同じ指摘が3サイクル連続したらルール化)に該当する。Amazon 確認を人間の定常作業として手順にすることを提案する。
