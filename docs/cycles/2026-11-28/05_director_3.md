# 05. ディレクター判定(3回目): microwavable-neck-wrap-vs-electric-heating-pad(2026-11-28)

インプット(すべて Read 済み): rule of foreign affiliate.md / docs/agents/director.md / docs/agents/fact_checker.md(「修正のルール」ほか)/ 03_architect_3.md / 04_factcheck_3.md / src/posts/microwavable-neck-wrap-vs-electric-heating-pad.md(全270行)/ src/posts/*.md の title・description・公開状態(特に shiatsu-neck-shoulder-massager-desk-tension)
Amazon・ブラウザ・git は使っていない。行番号は記事ファイルの行番号。

照合した共通ルールの見出し: 「チーム全員が守ること」「サイトの声(文体・一人称・価値観)」「絶対NG表現」「訴求の優先順位」「セール記事・価格の書き方(2026-09-29決定)」(守ること 1〜6)「読者への姿勢」「各エージェントの境界」「運用改善ルール」

## 判定: 差し戻し

理由は1点だけ: **電子レンジの加熱時間の数字**(やけど・過熱に直結する数字が、本文を読めていない検索抜粋だけを根拠にしている)。それ以外のチェック項目はすべて OK。

### 差し戻しの場合
- 指摘事項1: 加熱時間の数字(L75・L76・L156・L178・L236、関連して L40・L78・L184)→ 数字を削り、"follow the heating time on the label for your microwave's wattage" の形に書き換える(具体的な書き換えは下の「書き換え指示」)
→ 差し戻し先: **レビュワー**(本文の書き換え。設計図の見出し構成は変えないので、アーキテクトへの差し戻しは不要)
→ 書き換え後: ファクトチェッカーは変更行だけ再確認(新しい数字・主張が入っていないか)→ ディレクター再判定

#### 判断の理由(加熱時間を残さない)
1. **fact_checker.md「修正のルール」**: 「数字は、公式の情報源で確認できたもの以外は削る」。Comfytemp・Bed Buddy の値は「メーカー公式ドメインに限定した検索の抜粋」で、ページ本文は 429 で一度も読めていない(04_factcheck_3 L8・L21・L25・L71)。抜粋は検索エンジンが切り出した断片で、どの型・どの売り方のページの、いつの時点の文かを本文で確かめられていない。これを「公式の情報源で確認できた」とは扱わない
2. **取り違えの余地が実際にある**: Comfytemp は K9304(3〜5分)・K9305 など型で時間が違い(03_architect_3 L66)、Bed Buddy は1個売りページの時間が未確認で、中身の記載も2個組と違う可能性がある(04_factcheck_3 L26・#14・#15)。記事の Amazon リンクは検索リンクなので、読者が手にする商品が2個組・K9306 とは限らない
3. **設計図が条件を付けていた**: 「検索抜粋で確認した値は、ライターが本文に書く前に人間がメーカーページを目視で照合する」(03_architect_3 L19)、「表2の加熱時間は人間確認 2・3 で目視照合が取れた値だけ残す。取れなければ See the label に置き換える」(同 L213・L333)。この照合はまだ済んでいない
4. **共通ルールの優先順位「正確性 > 実用性」**: 間違っていた場合の害が、重さ・寸法などと違ってやけど・過熱になる。一方、削っても読者が失うものは小さい(本文はすでに毎回「ラベルの時間に従う」と案内しており、正しい時間は手元の商品のラベルにある)
5. 人間の目視で値が確かめられた後に、更新として数字を戻すことは妨げない(その場合はファクトチェック→ディレクターを通す)

#### 書き換え指示(レビュワー向け。新しい主張は足さない)
- **L40**: "Bed Buddy lists around a minute or less; Comfytemp lists a few minutes for its heavier wrap. So we only quote each maker's numbers for its own product." を削る(抜粋の数字から作った要約のため)。残す形の例: "Heating times vary a lot by product and by microwave wattage, even between wraps from the same brand. Follow the heating time on the label for your microwave's wattage, not a time you read elsewhere."
- **L75(表2 Comfytemp の Heating 欄)**: 数字を削り "Microwave; follow the heating time on the label for your microwave's wattage"(表が長くなるなら "Microwave; see the label for your wattage")
- **L76(表2 Bed Buddy の Heating 欄)**: 同上。"then rest 1 min" も削る
- **L78**: "Heating times are the makers' published figures." を削り、"Follow the heating time on the label for your microwave's wattage on the product you actually have." の1文に
- **L156**: "3 to 4 minutes at 800W or 2 to 3 minutes at 1200W, never more than 5 minutes. If you don't know your wattage, start with 2 minutes; reheat for half the previous time." を削る。"Comfytemp gives heating times by microwave wattage; follow the heating time on the label for your microwave's wattage on the wrap you receive." の形に。"Comfytemp says it stays warm roughly 15 to 20 minutes." は残してよい(下の軽い指摘2)
- **L178**: "1 minute 15 seconds at 600W, 50 seconds at 900W, or 37 seconds at 1200W, then rest it for 1 minute." を削る。"Bed Buddy gives heating times by microwave wattage; follow the heating time on the label for your microwave's wattage on the wrap you receive." の形に。冷凍の文("freeze it for a few hours…")は確認済み(#16)なので残す
- **L184**: "With short heating times, plan on reheating." は削った数字が前提なので、"A microwavable wrap cools on its own, so plan on reheating." に
- **L236(FAQ)**: 2品の数字を削る。"It depends on the wrap and your microwave's wattage. Don't borrow one product's time for another; follow the heating time on the label for your microwave's wattage." の形に
- 見出し(L91 の H3 を含む)は消さない。チェックリスト L202 はすでに数字なしの形なので変更不要

## チェックリスト

| # | 項目 | 判定 | 根拠(行) |
|---|---|---|---|
| 1 | 共通ルール(ジャンル・文体・NG表現・読者への姿勢)と矛盾しない | OK(加熱時間を除く) | 首・肩を温める自宅・職場のリカバリー用品でジャンル内。一人称は「we」で統一(L13・L54・L89・L136・L158)。比較表2つ(L60〜68・L72〜76)、向き不向き(各 Pick の L138・L160・L182、L212〜230)あり。押し売りなし |
| 2 | 設計図の見出し構成から逸脱しない | OK | H2 10本+導入が設計 1〜11 と同順(L26・34・56・87・126・194・200・212・232・254)。H3 も一致(L36・44・52・91・105・114・128・150・172)。FAQ 5問も設計どおり(L234・238・242・246・250)。設計にあった「FDA の 15〜20 分」「Sunbeam ヘルプの対象外の人」は本文に入っていないが、抜粋のみ・入手できない資料を避ける方向なので問題なし |
| 3 | 絶対NG表現が無い | NG(1件) | 根拠の弱い数字(加熱時間)= 「根拠のない数字の提示」に近く、上の指摘事項1。誇大・効能・虚偽の一人称・ASP 規約・開示は OK(下の「追加確認」「健康面」) |
| 4 | 「向いていない人」がある | OK | L212〜230 の節+各 Pick の L138〜143・L160〜165・L182〜187、比較表の "May not suit" 列(L72〜76) |
| 5 | アフィリエイトリンクに rel="nofollow sponsored" | OK | Amazon リンク10本すべてに付いている(L23・L82〜84・L147・L169・L191・L265〜267) |
| 6 | Amazon タグが quietrecover-20 | OK | 10本すべて tag=quietrecover-20。tag なし・rel なしのリンクは0 |
| 7 | 内部リンクが `{{ '/posts/x/' | url }}` 形式で、公開済み | OK | shiatsu-neck(L19・L227・L244・L261、publishAt 2026-09-26)、shiatsu-back(L228、2026-10-22)、quiet-space-heaters(L229、2026-10-13)、foot-warmer(L223・L230、2026-11-17)。いずれも published: false なし・categories.json に登録あり。素の `](/posts/...)` は0。下書きの heated-seat・heated-mattress-pad へのリンクなし |
| 8 | 未設定 ASP のプレースホルダーが無い | OK | YOURTAG 等 0件 |
| 9 | タイトル・ディスクリプションが既存記事と重複しない | OK | title・description とも全記事で重複0。shiatsu-neck は "Best Neck Massagers for Desk Workers: Shiatsu Buyer's Guide"/揉む機能の比較で、本記事(温めるだけの道具)と語も切り口も別。下書き heated-seat・heated-mattress-pad とも別 |
| 10 | フロントマターの形式 | OK | L2〜10: layout / title / description / date / tags / category に加え、published: false・permalink: false・eleventyExcludeFromCollections: true の3点あり。publishAt なし(人間が決める) |

### 追加確認
- **手書きの価格・金額・割引率・セール名: 無し。** `$`・`% off`・Black Friday・Cyber・deal・coupon・free shipping を検索して0件。価格は「budget / mid-range」の相対表現のみ(L74〜76、注記 L78)。campaign ブロックなし
- **冒頭の開示**: L13(アフィリエイト開示+Not medical advice+"We have not used these products ourselves")。**末尾の医療免責**: L270(設計図の文と同一)
- **一人称の虚偽テスト表現: 無し。** tested / tried / used は0件。"We couldn't confirm"(L54・L124・L180)、"We couldn't get the manual"(L136)、"We couldn't read its manual"(L197)は調査の事実の記述
- **誇大表現: 無し。** always / guaranteed / cures / everyone should / proven は0件。メーカーの宣伝文句(pain relief、deep penetrating、therapy 等)の引用なし
- **「always」(CPSC の引用)について**: CPSC 701 の原文は "Always turn off your heating pad before you go to sleep."(04_factcheck_3 L14)だが、**記事本文に "always" は入っていない**。L116 は "CPSC's home safety checklist says to turn a heating pad off before you go to sleep" と言い換えており、L142・L209・L240 も同様。NG に当たる箇所は無し。なお、仮に原文どおり引用したとしても、機関名を示した安全上の指示の引用であって「誇大な断定」(効果や結果を言い切る表現)とは性質が違う。ただし NG 語リストとの機械照合で毎回議論になるので、今の言い換えのまま維持するのがよい

### 健康面
- **痛み・こり・血流への効果の断定: 無し。** L32 "Neither is a treatment. Both simply add warmth, which some people find comfortable"、L244 "It isn't a treatment"。「こりが取れる」「血行が良くなる」系の表現は0。重みについても L54 "Whether weight feels pleasant is personal" と好みに留めている
- **安全上の注意は出典の範囲内:**
  - Bed Buddy 説明書(本文確認): L93〜101・L203〜205・L214〜219(#19・#20)。L93 で「採用品と別の body wrap 用」と明記している点もよい
  - CPSC 701(本文確認): L116・L142・L209・L240(#22)
  - FDA Navajo リコール(本文確認): L108・L208(#23 の修正後の言い回しどおり)
  - University of Utah Health(本文確認): L50・L109・L116・L221(#24〜#26)
  - L107・L110 は FDA Mighty Bliss(抜粋のみ)由来だが、機関名を出さず「一番低い設定から・短く・傷んでいたら使わない」という一般的な注意に留め、時間は "check your manual for how long" で数字を出していない。問題なし
  - L118・L240 の「眠りそうなら使わない」は断定的な事実主張ではなく慎重側の助言。#21 の修正で「記載が見つからなかった」の文は削除済み
- **加熱時間**: 上の指摘事項1のとおり、これだけが正確性の基準を満たしていない

## 差し戻しにしない軽い指摘
1. **人間確認(公開前)は引き続き必須**: Amazon 確認(サイクルログのリスト)、comfytemp.com の K9306 ページ(2.8 ポンド・冷蔵庫の記載・お手入れ)、carex.com の Bed Buddy(1個売りと2個組の違い・中身の記載)、sunbeam.com(22×19 インチ・LED・洗濯手順)。加熱時間を削った後も、これらは検索抜粋のみなので目視照合を公開の条件にする
2. **L42・L123・L156「Comfytemp says it stays warm roughly 15 to 20 minutes」**も検索抜粋のみ。ただし「温かさが続く時間」で、外れても直接やけどにつながる数字ではないため、今回は残してよい。人間確認1で Comfytemp ページを見るときに一緒に照合し、違えば削る
3. **L196 PureRelief「a reasonable alternative if the Sunbeam isn't available」**: リンクなしなので問題はないが、Amazon 確認で Sunbeam が見つからず差し替えになった場合は、この文と Pick 1 を入れ替える(差し替え表どおり)
4. **タイトル**: 設計図の推奨案1 "…for Desk Workers" ではなく "…at Your Desk"(L3)。補助キーワード "heated neck wrap for desk workers" は L15・L87・L242 で拾えているので問題なし。最終決定は人間(設計図 人間確認6)
5. **公開作業時**: categories.json の posts に `"microwavable-neck-wrap-vs-electric-heating-pad": "recovery"` を1行追加(現在は未登録。設計図 人間確認8)
6. **運用改善ルールの観点**: 「検索抜粋だけで本文が読めない数字をどう扱うか」は今日の3本でも繰り返し出ている。fact_checker.md の判定に「確認済み(抜粋のみ)」を独立した区分として設け、安全に関わる数字(加熱時間・温度・使用時間)は抜粋のみなら削る、と明文化することを提案する(ルール変更は人間の承認事項)

最終的な公開承認は人間が行う。

## 2回目の判定

インプット(すべて Read 済み): rule of foreign affiliate.md / docs/agents/director.md / 本ファイルの1回目の判定 / 04_factcheck_3.md(末尾「再確認(差し戻し後)」を含む)/ src/posts/microwavable-neck-wrap-vs-electric-heating-pad.md(全270行を再読)。Amazon・ブラウザ・git は使っていない。

照合した共通ルールの見出し: 「チーム全員が守ること」「サイトの声(文体・一人称・価値観)」「絶対NG表現」「訴求の優先順位」「セール記事・価格の書き方(2026-09-29決定)」(守ること 1〜6)「読者への姿勢」「各エージェントの境界」「運用改善ルール」

## 判定: 承認

- プロモーターへ引き渡し可能(最終的な公開承認は人間が行う)

### 1回目の書き換え指示の反映
| 行 | 指示 | 結果 |
|---|---|---|
| L40 | 抜粋の数字から作った要約を削り、ラベルに従う文へ | 反映済み。指示どおりの2文 |
| L75 | 表2 Comfytemp の Heating 欄から数字を削る | 反映済み "Microwave; see the label for your wattage" |
| L76 | 表2 Bed Buddy の Heating 欄、"rest 1 min" も削る | 反映済み(同上) |
| L78 | "Heating times are the makers' published figures." を差し替え | 反映済み |
| L156 | W数別の時間・5分・2分・半分を削る | 反映済み。15〜20分(温かさが続く時間)は1回目の軽い指摘2どおり残存 |
| L178 | W数別の時間・1分置くを削る | 反映済み。ファクトチェック再確認 R6 で "Bed Buddy's two-pack page gives…" と出典を狭めた形。冷凍の文は残存 |
| L184 | "With short heating times…" を差し替え | 反映済み "A microwavable wrap cools on its own, so plan on reheating." |
| L236 | FAQ の2品の数字を削る | 反映済み |

- **加熱時間の数字: 残っていない。** 「数字+min/minute/sec/second/W/watt」「1:15 形式」「half the previous」「rest … for」で全文検索し、ヒットは温かさが続く「15〜20分」(L42・L123・L156)のみ。加熱時間・W数の数字は0件
- **書き換えによる新しい問題: 無し。** 新しい主張・断定・効能・価格は入っていない。表2(L72〜76)はヘッダー12列に対し L74・L75・L76 とも12セルで崩れなし。L91 の H3・L202 のチェックリストもそのまま。行数は270行で変わらず

### チェックリスト
| # | 項目 | 判定 | 根拠(行) |
|---|---|---|---|
| 1 | 共通ルール(ジャンル・文体・NG表現・読者への姿勢)と矛盾しない | OK | 首・肩を温める自宅・職場のリカバリー用品でジャンル内。一人称は「we」(L13・L54・L89・L136・L158)。比較表2つ(L60〜68・L72〜76)、向き不向き(L138〜143・L160〜165・L182〜187・L212〜230)。冒頭の開示と Not medical advice(L13)、末尾の医療免責(L270)。押し売りなし |
| 2 | 設計図の見出し構成から逸脱しない | OK | H2 10本(L26・34・56・87・126・194・200・212・232・254)、H3(L36・44・52・91・105・114・128・150・172)、FAQ 5問(L234・238・242・246・250)。1回目から変更なし |
| 3 | 絶対NG表現が無い | OK | 1回目の唯一のNG(加熱時間の数字)は解消。always / guaranteed / cures / tested / tried は0件("used" は L13 の "We have not used these products ourselves" のみ)。効能の断定なし(L32・L244)。手書きの価格・割引率・クーポン・送料無料・セール名は0件($・% off・deal・coupon・free shipping・Black Friday で検索)。価格は budget / mid-range の相対表現(L74〜76、注記 L78) |
| 4 | 「向いていない人」がある | OK | L212〜230 の節、各 Pick の "Who it may not suit"(L138・L160・L182)、表の "May not suit" 列(L72〜76) |
| 5 | アフィリエイトリンクに rel="nofollow sponsored" | OK | Amazon リンク10本すべて(L23・L82・L83・L84・L147・L169・L191・L265・L266・L267) |
| 6 | Amazon タグが quietrecover-20 | OK | 10本すべて tag=quietrecover-20。条件に合わないリンクは0 |
| 7 | 内部リンクが `{{ '/posts/x/' \| url }}` 形式 | OK | 8箇所(L19・L223・L227・L228・L229・L230・L244・L261)。素の `](/posts/...)` は0。リンク先は1回目に公開済みを確認済み、今回の書き換えで変更なし |
| 8 | 未設定 ASP のプレースホルダーが無い | OK | YOURTAG 等 0件 |
| 9 | タイトル・ディスクリプションが既存記事と重複しない | OK | L3・L4 は1回目から変更なし(1回目に全記事と照合済み) |
| 10 | フロントマターの形式 | OK | L2〜10: layout / title / description / date / tags / category、published: false(L8)・permalink: false(L9)・eleventyExcludeFromCollections: true(L10)。publishAt なし |

### 差し戻しにしない軽い指摘
1. **L42・L123・L156 の「約15〜20分温かい」**は検索抜粋のみ(04 #9)。やけどに直結する数字ではないので残してよいが、人間確認で comfytemp.com を見るときに照合し、違えば削る
2. **L156・L178「W数ごとに加熱時間を示している」**は時間の存在を言うだけで数字は無い。L178 は再確認 R6 で "two-pack page" に狭めた形になっており問題なし
3. 1回目の軽い指摘3〜6(PureRelief の差し替え文、タイトル案、categories.json への登録、抜粋のみの数字の扱いのルール化提案)は引き続き有効

### 公開前の人間確認
1. Amazon 確認(04_factcheck_3「Amazon 確認リスト」の3商品。型違い・マッサージつき・2個組/1個売りの取り違えがないか。差し替え時は表どおり。Sunbeam を差し替えたら L196 と Pick 1 を入れ替え)
2. comfytemp.com の K9306 ページを目視: 15〜20分温かい・2.8ポンド・冷蔵庫の記載・お手入れ(拭くだけか)
3. carex.com の Bed Buddy 1個売りページを目視: 中身の記載(穀物・ハーブ・花か、小麦・大豆・ラベンダーか)、冷凍・拭くだけの記載
4. sunbeam.com の Neck Renue ページを目視: 22×19インチ・LED・洗濯手順(cool water ほか)
5. タイトルの最終決定(設計図 人間確認6)
6. 公開作業時に categories.json の posts に `"microwavable-neck-wrap-vs-electric-heating-pad": "recovery"` を追加し、published: false・permalink: false・eleventyExcludeFromCollections: true を外して publishAt を決める
- 加熱時間は記事から削ったため、その目視照合は公開の条件から外れる(値を戻す場合はファクトチェック→ディレクターを再度通す)

最終的な公開承認は人間が行う。
