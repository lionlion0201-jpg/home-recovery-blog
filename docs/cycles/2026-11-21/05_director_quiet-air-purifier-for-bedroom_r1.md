# 05. ディレクター判定: quiet-air-purifier-for-bedroom(r1、2026-11-23)

## 照合した共通ルールの見出し(rule of foreign affiliate.md)
- チーム全員が守ること
- サイトの声(文体・一人称・価値観)
- 絶対NG表現
- 訴求の優先順位
- セール記事・価格の書き方(2026-09-29決定)(守ること 1〜6/自動チェック)
- 読者への姿勢
- 各エージェントの境界
- 運用改善ルール

あわせて照合: docs/agents/director.md(チェックリスト)、docs/agents/reviewer.md(執筆ルール)、03 設計図、04 ファクトチェック結果。

## 判定: 承認

(ディレクターの判定はチェックリスト照合まで。公開の最終承認は人間が行う。)

### チェックリスト照合結果
| 項目 | 結果 | 根拠 |
|---|---|---|
| 共通ルール(ジャンル・文体・NG表現・読者への姿勢) | OK | 寝室の空気清浄機=睡眠ウェルネスの範囲。一人称は "we" で統一。誇大語(always / guaranteed / cures / everyone)なし |
| 設計図の見出し構成 | OK(軽微な差1点、下記) | H2 1〜12 の構成・各 Pick の型(What it's for → 本文 → Who it may not suit → CTA)は設計図どおり。タイトルは設計図の短縮案系統で許容範囲 |
| 医療効果の断定 | OK | L212 は EPA の "possibly" と「大きな改善が常に出るわけではない/すべての症状ではない」の範囲内(ファクトチェック #36 で修正済み)。「よく眠れる」とは書いていない(L17, L214)。喘息・重いアレルギーは医師へ(L221, L262) |
| 虚偽の一人称体験 | OK | 冒頭で "We have not used these products ourselves." と明記。"we tested / we used" 等なし。"when we checked" は公式情報の確認行為の記述 |
| 向いていない人 | OK | 各 Pick に "Who it may not suit"、独立 H2 "Who a Quiet Bedroom Air Purifier Isn't Right For"(L218-225) |
| FTC 開示・医療免責 | OK | 冒頭 L13 に affiliate disclosure + Not medical advice、末尾 L262 に医療免責 |
| rel="nofollow sponsored" | OK | Amazon リンク10本すべてに付与(L23, 101-103, 132, 158, 179, 257-259) |
| tag=quietrecover-20 | OK | `list_amazon_links.py` で3種類・10本すべて tag_ok: true。プレースホルダーなし |
| CTA ボックス形式 | OK | すべて `<div class="cta-box">` 。導入直後・比較表直後・各 Pick 末尾・まとめの配置は設計図どおり。Also Looked At にリンクなし |
| 内部リンクの記法・公開状態 | OK | 4本すべて `{{ '/posts/xxx/' \| url }}` 形式。リンク先は publishAt 2026-11-06 / 10-13 / 09-27、humidifiers は 08-29 公開済み。未公開記事へのリンクなし |
| 未設定 ASP のプレースホルダー | OK | YOURTAG 等なし。Amazon 以外のリンクなし |
| タイトル・説明文の重複 | OK | 既存記事に air purifier のタイトルなし |
| フロントマター | OK | layout / title / description / date / tags あり。published: false / permalink: false / eleventyExcludeFromCollections: true を確認 |
| 手書きの価格・値引き・セール名・クーポン・送料無料・Amazon画像 | OK | `check_amazon_policy()`(lang=en)の結果は指摘0件。"$" 表記・Black Friday 等なし。比較表の "Price tier / Filter cost tier" は budget / mid-range / premium の相対表現 |
| ファクトチェックの未確認記述 | OK(1点は人間確認) | #15 ENERGY STAR は削除済み、#16「3機種で最小」は "compact" に弱化済み。#31(L167 Blueair 公式ページ同士の数字の食い違い)は設計図の取得記録に基づく記述で、数字は書いていない。今回再確認できていないため人間確認へ |
| 狙う検索語 | OK(補助語は見出しになし) | 主語 "quiet air purifier for bedroom" はタイトル・説明文・H2(L89, L218, L249)に自然に入っている。補助語 "air purifier for light sleepers" は本文 L17 に1回、説明文は "for light sleepers" の形 |
| 語数 | 許容 | 本文(表を除く)約3,060語、CTA 文言も除くと約2,850語。上限 2,800語程度をやや超えるが大幅超過ではない |

### 差し戻しにしない軽微な所見(次回以降・人間の判断用)
- 設計図は補助語 "air purifier for light sleepers" を H2 に1か所入れる指定だったが、見出しには入っていない。本文と説明文には自然に入っているため差し戻し理由にはしない。入れるなら H2 "What Makes an Air Purifier Hard to Sleep Next To" を "...for Light Sleepers" 系に変える程度(人間判断)。
- 語数は上限をやや超過(約1割)。削るなら "Air Purifiers We Looked At but Didn't Pick" か FAQ が候補。
- L147 "When we checked Coway's U.S. online store on November 23, 2026" は設計図の当日記録で、ファクトチェックでは再確認できていない(429)。

### 承認の場合
- プロモーターへ引き渡し可能(ただし下記の人間確認の後に公開判断)

### 人間確認として残す項目
1. Amazon(3週連続で AI のアクセス拒否のため未実施): 3本の検索リンクで狙った商品(Levoit Core 300S-P / Coway AP-1512HH / Blueair 311i Max)が出るか、取り扱い・新品在庫・評価・レビュー数、記事の説明とずれがないか
2. Coway AP-1512HH が今も新品で買えるか(L147 の日付つき記述の再確認)
3. Blueair 311i Max の公式ページで CADR・部屋の広さ・フィルター寿命の数字が実際に食い違っているか(L167)。食い違っていなければ L167 の該当文を差し替える
4. Blueair 311i Max の Night mode でランプがどこまで暗くなるか/イオン機能を切れるか
5. タイトルの最終決定(現タイトルは設計図の短縮案系統)と、公開日(publishAt)の設定
