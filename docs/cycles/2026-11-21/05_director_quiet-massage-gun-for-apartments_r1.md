# 05. ディレクター判定: quiet-massage-gun-for-apartments(r1 / 2026-11-23)

対象: src/posts/quiet-massage-gun-for-apartments.md
照合資料: docs/agents/director.md、docs/agents/reviewer.md、共通ルール(rule of foreign affiliate.md)、03_architect 設計図、04_factcheck 結果表

## 照合した共通ルールの見出し
- チーム全員が守ること
- サイトの声(文体・一人称・価値観)
- 絶対NG表現
- 訴求の優先順位
- セール記事・価格の書き方(2026-09-29決定)(守ること 1〜6 / 自動チェック)
- 読者への姿勢
- 各エージェントの境界
- 運用改善ルール

## 判定: 承認

## チェックリスト照合

| 項目 | 結果 | 根拠 |
|---|---|---|
| 共通ルールとの整合(ジャンル・文体・we・NG・姿勢) | OK | 自宅リカバリー機器。一人称は "we" のみ、buyer's guide 口調 |
| 設計図の見出し構成 | OK | H2 10本・H3 構成が設計図 1〜10 と一致。タイトル・説明文は設計図の推奨案3とメタ案どおり |
| 誇大な断定 | OK | always / never / guaranteed / cures / best 等なし。"quietest" は疑問形タイトルと FAQ の問いのみで、FAQ は「一つに決められない」と回答 |
| 医療効果の断定 | OK | 効能の記述なし。L203 で「痛み・回復・睡眠への効果は主張しない」と明記 |
| 虚偽の一人称体験 | OK | L13 で "We have not used these products ourselves"。tested / tried 等なし |
| FTC 開示 | OK | L13 冒頭にアフィリエイト開示 |
| 医療免責 | OK | L13・L203・L245 の3か所 |
| 「向いていない人」 | OK | 各 Pick に "Who it may not suit"、H2 "Who a Quiet Massage Gun Isn't For"、比較表 "May not suit" 列 |
| rel="nofollow sponsored" | OK | Amazon リンク 12本すべてに付与 |
| tag=quietrecover-20 | OK | 12本すべて(list_amazon_links.py で tag_ok: true、プレースホルダーなし) |
| CTA ボックス形式 | OK | `<div class="cta-box">` を表直後・各 Pick 末尾・まとめ末尾の5か所。Also Looked At はテキストリンク(設計図どおり)。文言は "See/Check … on Amazon" で価格を示唆しない |
| 手書き価格・値引き・クーポン・送料・セール名 | OK | `$`・%off・coupon・free shipping・Black Friday 等なし("Prime" は Theragun Prime の商品名のみ)。価格は Mid-range / budget の相対表現。check_amazon_policy() の結果は指摘なし([]) |
| Amazon 商品画像 | OK | 画像なし |
| 内部リンク形式と公開状況 | OK | 6本すべて `{{ '/posts/xxx/' \| url }}` 形式。リンク先はいずれも 2026-11-23 より前に公開済み(最新は white-noise-machine-for-apartment-noise 11/19)。下書きの heated-seat-massager-for-back へのリンクなし |
| 未設定 ASP のプレースホルダー | OK | YOURTAG-IMPACT 等なし。Amazon のみ |
| タイトル・説明文の重複 | OK | 既存記事に同一・類似のタイトル/説明文なし |
| フロントマター | OK | layout / title / description / date / tags / category に加え、published: false・permalink: false・eleventyExcludeFromCollections: true を確認 |
| 狙う検索語 | OK | "quiet massage gun" は説明文冒頭・H2 3本(Compared / Isn't For / Fits Your Home?)・導入に自然に入る。"quietest massage gun for apartment(s)" はタイトル、"quietest massage gun" は FAQ 見出し |
| ファクトチェックの反映 | OK | 未確認7件("As quiet as rainfall/conversation"、B37 アタッチメント4種、10-minute Intelligent Stop、ケース・15°ハンドル、クッション型ヘッドなし、Ekrin の amplitude)はすべて削除または "check the listing" / "Not confirmed on the pages we could read" に置き換え済み。B37 USB-C は "current version" と旧型注記に修正済み。誤り1件(QuietForce)は "For some Theragun models…" に修正済み |

## 気づいた点(差し戻し理由にはしない)
- Bantam の振り幅は公式の検索抜粋に 10mm の記載があるが、本文は "Not confirmed" のまま。読者に不利な誤りではないため現状で可。個別ページで確認できたら追記を検討。
- categories.json の `posts` に本記事を追加するかは未決(設計図の人間確認7)。

## 人間確認として残す項目(公開前)
1. Amazon での取り扱い・評価(4.0以上か)・レビュー数(100件以上か): Ekrin B37 / Ekrin Bantam / Theragun Relief / Hypervolt Go 2 / Bob and Brad Q2 Mini / Theragun Mini 3rd Gen。Amazon が AI のアクセスを拒否しているため3週連続で未実施。Ekrin が扱われていない・評価が低い場合は設計図どおり Hypervolt Go 2 を3枠目に繰り上げる(その場合は差し戻し)
2. Amazon で売られている B37 が USB-C の現行版か
3. 価格帯の表記(表の Mid-range ×3、本文の Bob and Brad "budget")。B37 を premium にするか
4. Ekrin 個別商品ページ(429 で読めず)で dB 範囲・付属品・Intelligent Stop を確認できれば、削った記述を戻すか判断
5. Theragun Relief の US 公式商品ページ本文(1.37 lbs・around 120 minutes・"whisper-quiet")
6. categories.json への追加の要否
7. 最終的な公開承認(published / permalink / eleventyExcludeFromCollections の切り替え)

## 承認の場合
- プロモーターへ引き渡し可能(ただし公開は上記の人間確認と人間の最終承認の後)
