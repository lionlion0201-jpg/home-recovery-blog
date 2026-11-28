# 05. ディレクター判定(1回目): heated-mattress-pad-vs-electric-blanket(2026-11-28)

インプット(すべて Read 済み): 共通ルール `rule of foreign affiliate.md`、`docs/agents/director.md`、`docs/cycles/2026-11-28/03_architect_1.md`、`docs/cycles/2026-11-28/04_factcheck_1.md`、`src/posts/heated-mattress-pad-vs-electric-blanket.md`(全251行)、`src/posts/*.md` の title/description。
Amazon・ブラウザ・git は使っていない。Amazon 確認は人間の週末レビューの手順(2026-11-23 変更)なので判定材料にしていない。行番号はファクトチェック修正後の現在の記事。

照合した共通ルールの見出し:
- チーム全員が守ること
- サイトの声(文体・一人称・価値観)
- 絶対NG表現
- 訴求の優先順位
- セール記事・価格の書き方(2026-09-29決定)/ 守ること / 自動チェック
- 読者への姿勢
- 各エージェントの境界
- 運用改善ルール

## 判定: 承認

### 承認の場合
- プロモーターへ引き渡し可能(最終的な公開承認は人間が行う)

## チェックリスト(director.md)

| # | 項目 | 結果 | 根拠 |
|---|---|---|---|
| 1 | 共通ルール(ジャンル・文体・NG表現・読者への姿勢)と矛盾していないか | OK | ジャンル=睡眠環境の寝具。一人称は "we" のみ(L13, L88, L97, L103, L159)。"I" は FAQ 見出しの読者の質問(L223, L231)だけ。比較表2つ(L60-75)と「向いていない人」(L117-122, L139-144, L161-166, L191-209)あり |
| 2 | 設計図の見出し構成から逸脱していないか | OK | 導入(L15-24)→ Short Answer(L26)→ Where the Heat Comes From + H3×3(L34-54)→ Compared(表2つ+CTA、L56-84)→ Can You Sleep…(L86-103)→ The 3 Picks + H3×3(L105-171)→ Looked At but Didn't Pick(L173)→ Checklist(L179)→ Who Shouldn't(L191)→ FAQ 5問(L213-233)→ まとめ(L235-251)。設計図の 1〜11 と一致。タイトルは設計図の短縮案4(L3) |
| 3 | 絶対NG表現がないか | OK | 誇大な断定("always" "guaranteed" "cures" "everyone should")なし。"Best" は表の列名 "Best for"(L71)のみ。睡眠効果・健康効果の記述なし(EMF の話も無し)。虚偽の一人称体験なし(L13 "We have not used these products ourselves")。cloaking・クーポンなし |
| 4 | 「向いていない人」への言及があるか | OK | 専用 H2(L191-209)+各商品の "Who it may not suit"(L117, L139, L161)+まとめ(L240) |
| 5 | アフィリエイトリンクに rel="nofollow sponsored" | OK | Amazon リンク10本すべて `rel="nofollow sponsored" target="_blank"`(L23, L81-83, L126, L148, L170, L246-248)。nofollow sponsored の無い `<a>` は0件 |
| 6 | Amazon タグが quietrecover-20 か | OK | 10本すべて `tag=quietrecover-20`。プレースホルダー無し |
| 7 | 内部リンクが `{{ '/posts/xxx/' \| url }}` 形式か | OK | 7箇所すべてこの形式(L15, L19, L101, L209×2, L211, L233)。素の `/posts/` は0件 |
| 8 | 未設定 ASP のプレースホルダーが残っていないか | OK | `YOURTAG` 等なし。他 ASP リンクなし |
| 9 | タイトル・メタディスクリプションの重複 | OK | `src/posts/*.md` の title・description に完全一致の重複なし。類似の foot-warmer(L3-4)・couples(L4)とも文言が異なる |
| 10 | フロントマター(layout, title, description, date, tags)の形式 | OK | L2-7 に layout: post.njk / title / description / date: 2026-11-28 / tags: post / category: Sleep |

## 追加確認

| 項目 | 結果 | 根拠 |
|---|---|---|
| 手書きの価格・価格帯の金額・割引率・セール名・クーポン・送料無料 | なし | `grep -n '\$[0-9]'` 0件。percent / off / Black Friday / Prime / deal / sale / coupon / free shipping / Cyber も0件。価格は列 "Price tier" の相対表現(L73-75, L77)。`campaign` ブロックなし |
| 自動チェック `scripts/review_lib.py` | 指摘0件 | `check_article()` → []、`check_amazon_policy()` → [](読み取りのみで実行) |
| フロントマターの非公開設定 | OK | `published: false`(L8)/ `permalink: false`(L9)/ `eleventyExcludeFromCollections: true`(L10) |
| 内部リンク先が公開済みか | OK | quiet-space-heaters(publishAt 2026-10-13)、couples-dual-zone(2026-10-05)、foot-warmer(2026-11-17)、humidifiers(2026-08-29、publishAt 無し)。4本とも `published: false` / `permalink: false` / `eleventyExcludeFromCollections` なし |
| 冒頭のアフィリエイト開示 | OK | L13(開示+Not medical advice+未使用の明記+説明書優先) |
| 末尾の医療免責 | OK | L251 |
| ファクトチェックの「誤り」「未確認」が本文に残っていないか | 残っていない | #4-6 UL は "before you go to sleep" に修正済み(L99, L103, L217)/#10 後半「毛布は広げて…」は削除済み(L32)/#19 "still damp"・clothesline か shower rod・commercial or laundromat dryers(L115, L229)/#27 予熱は "Not confirmed"・"couldn't confirm"(L74, L133)/#28-29 "wash label"・リコール品に限定(L137, L182)/#32 ライセンス・卸の断定なし(L155)/#35 LoftTec の段階数食い違いの記述なし(L176)/#8 UL の対象(L202、下の軽い指摘1を参照) |
| 安全上の注意が出典の範囲を超えていないか | 超えていない | CPSC 701(L17, L46, L63-64, L99, L101, L135, L143, L184, L225)、Sunbeam 説明書(L29, L40, L52, L66, L92-95, L111-115, L121, L142, L183-189, L193-207, L221, L229)、UL(L52, L99, L103, L155, L181, L202, L217)はファクトチェック表の確認済み項目と一致。「寝ながら使って安全」とは書いておらず、一晩使用を勧めも禁止もしていない(L103)。タイマーについても "It doesn't make the blanket safer by itself."(L155) と保証を避けている |

## 差し戻しにしない軽い指摘

1. **L202 UL の対象者:** ファクトチェック #8 は「一部ずれ(UL は麻痺のある人・安全な操作方法を理解できない人)」とし、修正後も "infants, young children," が残っている。UL 記事に乳幼児の記載があるかは 04 の記録だけでは読み取れない。人間の週末レビューで UL 記事を見て、無ければ "infants, young children," を削る(Sunbeam 説明書側 L195 で乳幼児は既にカバーされているので、削っても内容は欠けない)。
2. **語数:** 本文は表を含めて約3,100語(URL・HTML を除いた概算)で、設計図の上限 2,800 語を超えている。見出し構成は設計どおりで内容の重複も少ないため差し戻さない。削るなら Short Answer(L26-32)とまとめ(L235-242)の言い回しの重なり。
3. **Sunbeam 比較ページへの言及が2回(L32, L95):** 設計図は「引用は1回」。どちらも言い換えで直接引用ではないため問題は小さい。ページ本文は 403 で検索抜粋のみ確認なので、人間確認(sunbeam.com 目視)で文言を確かめる。
4. **L92 "some models let you turn it off":** "it" が製品本体か自動オフか分かりにくい。"some models let you disable the auto-off" とすると L95 と揃う。
5. **公開作業時の残り:** `src/_data/categories.json` への `"heated-mattress-pad-vs-electric-blanket": "sleep-environment"` 追加、`publishAt` の決定(設計図「人間確認」6・front matter 指示)。
6. **director.md の参照先:** インプットの `../setup_guide.md` は存在せず、L26 の `director_house_rules.md` も共通ルールのファイル名と違う。今回の判定には影響なし(共通ルールを優先して照合した)。director.md の参照先の書き直しを別作業で検討。
