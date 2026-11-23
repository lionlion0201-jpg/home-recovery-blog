# 05. ディレクター判定: non-wearable-sleep-tracker(r1 / 2026-11-23)

対象: src/posts/non-wearable-sleep-tracker.md(ファクトチェック修正後の版)
照合資料: docs/agents/director.md、docs/agents/reviewer.md、03_architect 設計図、04_factcheck 表、共通ルール

## 照合した共通ルールの見出し
- チーム全員が守ること
- サイトの声(文体・一人称・価値観)
- 絶対NG表現
- 訴求の優先順位
- セール記事・価格の書き方(2026-09-29決定)(守ること 1〜6 / 自動チェック)
- 読者への姿勢
- 各エージェントの境界
- 運用改善ルール

## 判定: 差し戻し

修正は小さく3点のみ(本文の数文)。それ以外のチェック項目はすべて合格。

### 差し戻しの場合
- 指摘事項1: [L41 H3「These Are Not Medical Devices」] → 見出しを「医療機器ではない」と断定しない形に変更(例: "Wellness Trackers, Not Diagnostic Tools")。
  理由: ファクトチェック #8 で「Withings U.S. 版は医療機器ではない」は未確認とされ、本文(L43)は "wellness device" に弱めてある。Sleepal については本文自身が「どちらとも書いていない」としている。見出しだけが未確認の内容を断定で残しており、本文と食い違う。設計図の見出し名からは外れるが、設計図の前提(「公式サポートで医療機器ではないと明記」)がファクトチェックで崩れたための変更として認める。
- 指摘事項2: [L254 末尾の免責 "Consumer sleep trackers are not medical devices and can't diagnose sleep disorders."] → 同じ理由で断定を外す(例: "The consumer trackers in this guide are sold for wellness tracking and aren't meant to diagnose sleep disorders.")。L234 の言い回しに揃えればよい。
- 指摘事項3: [L193 チェックリスト "each device tracks one person"] → Sleepal は1台で何人を測れるか未確認(比較表 L80 でも "Check with the maker")。記事内で食い違っているので、"Withings and the Nest Hub track one person per device; check Sleepal's specs." のように確認済みの範囲に限定する。
→ 差し戻し先: レビュワー(該当3文のみ修正。見出し構成・リンク・CTA は変えない)

## チェックリスト照合結果
- [x] 共通ルールとの整合: ジャンル内、"we" 統一、buyer's guide 口調。冒頭に「実際には使っていない」と明記
- [△] 設計図からの逸脱: H2「The 3 Picks」→「The Picks」、Nest Hub を3番目の条件付き枠に移動・CTA ボックスなし(本文中のテキストリンク1本)。オーケストレーター方針(在庫切れのため条件付き)どおりで可。指摘事項1の見出し変更のみ要対応
- [x] 絶対NG表現: 誇大な断定・健康効果の断定・一人称の虚偽体験なし。"may help" 等の言い回し
- [x] 「向いていない人」: 各商品の "Who it may not suit" と H2「Who a Non-Wearable Sleep Tracker Isn't For」
- [x] rel="nofollow sponsored": Amazon リンク7本すべてに付与
- [x] tag=quietrecover-20: 7本すべて(list_amazon_links.py で tag_ok=true、検索語3種)
- [x] 内部リンク形式: 7本すべて `{{ '/posts/xxx/' | url }}`。リンク先7記事はすべて公開済み(date/publishAt が今日以前、draft なし)
- [x] 未設定 ASP のプレースホルダー: なし
- [x] タイトル・説明文の重複: 既存記事と重複なし
- [x] フロントマター: layout/title/description/date/tags/category あり。published: false / permalink: false / eleventyExcludeFromCollections: true を確認。カテゴリは categories.json で sleep-tracking-aids に登録済み
- [x] 価格: 手書きの金額・値引き率・クーポン・送料無料・セール名なし。価格帯は budget / mid-range / premium のみ。サブスクも金額なし(期間のみ)。review_lib の check_amazon_policy と check_article は指摘ゼロ
- [x] CTA ボックス: `<div class="cta-box">` 形式で4か所(比較表後・Withings・Sleepal・まとめ)
- [x] FTC 開示: 冒頭イタリックで開示
- [x] 医療免責: 冒頭・H2「A Note on Health and Accuracy」・末尾の3か所
- [x] 「気になる症状は医師へ」: L112、L203、L210、L236、L245、L254
- [x] 睡眠時無呼吸・FDA の書き分け: 市販の Withings Sleep(U.S.)は無呼吸検出なし、FDA 510(k) は医療機関向けの別製品 Sleep Rx(K231667、ファクトチェック #36 確認済み)と明確に分離。市販品で無呼吸がわかると読める文なし
- [x] 検索語: "Non-Wearable Sleep Tracker" がタイトル・H2(4か所)・説明文に、"Under-Mattress Sleep Tracker" が H2 と FAQ に自然に入っている
- [△] ファクトチェックの未確認項目: #2・#3・#18・#23・#28・#40 は修正済み。#8 は本文 L43/L108/L210 は弱めてあるが、見出し L41 と免責 L254 に断定が残る(指摘事項1・2)

## 人間確認として残す項目(差し戻しの理由にはしない)
1. Amazon での取り扱い・新品在庫・評価・レビュー数(Withings Sleep / Sleepal AI Lamp / Nest Hub 2nd Gen の検索リンク3種)。AI のアクセス拒否で3週連続未実施。Sleepal が Amazon に無ければ CTA の扱いを人間が判断(設計図どおり)
2. Google 米国ストアで Nest Hub (2nd gen) が全色在庫切れか(L83・L160「執筆時点」)
3. Withings 公式ページの目視(403 のため): U.S. 版の対応 OS、マットレス 4〜15インチ(出典は Sleep Analyzer 版 FAQ)、Withings+ なしで履歴・傾向が見られる文言、医療機器かどうかの文言
4. Sleepal: 購入に含まれる「1 Year Subscription」の対象プラン、電源アダプタ、1台で測れる人数
5. Sleep Sensing の preview 継続状況
6. 公開日(publishAt)の設定と公開フラグの切り替えは人間が行う

## 運用改善メモ
Amazon 確認が3週連続で人間確認に回っている。共通ルール「運用改善ルール」(同じ指摘が3サイクル連続)に該当するため、Amazon 確認を人間の定常作業として手順化することを提案する。
