# 05. ディレクター判定(2回目): light-therapy-lamp-vs-sunrise-alarm-clock(2026-11-28)

インプット(すべて Read 済み): rule of foreign affiliate.md / docs/agents/director.md / 03_architect_2.md / 04_factcheck_2.md / src/posts/light-therapy-lamp-vs-sunrise-alarm-clock.md(全245行)/ src/posts/*.md の title・description・公開状態
Amazon・ブラウザ・git は使っていない。行番号は記事ファイルの行番号。

照合した共通ルールの見出し: 「チーム全員が守ること」「サイトの声(文体・一人称・価値観)」「絶対NG表現」「訴求の優先順位」「セール記事・価格の書き方(2026-09-29決定)」(守ること 1〜6)「読者への姿勢」「各エージェントの境界」「運用改善ルール」

## 判定: 承認

(公開前の人間確認として、Mayo Clinic の本文目視を必須条件にする。下の「健康面」参照)

### 承認の場合
- プロモーターへ引き渡し可能(最終的な公開承認は人間が行う)

## チェックリスト

| # | 項目 | 判定 | 根拠(行) |
|---|---|---|---|
| 1 | 共通ルール(ジャンル・文体・NG表現・読者への姿勢)と矛盾しない | OK | 睡眠・自宅の光環境でジャンル内。一人称は「we」で統一(L13・L42・L52・L105・L188)。比較表(L56〜74)・向き不向き(各 Pick の「Who it may not suit」L107・L128・L149・L169、L194〜203)あり |
| 2 | 設計図の見出し構成から逸脱しない | OK | H2 11本が設計 1〜11 と同順(L26・34・54・86・97・179・186・194・205・227)。H3 も一致(L36・40・46・99・118・139・161)。sunrise 記事へのリンクは3回(L28・L167・L192)で上限内。設計 0-6 の FDA の1文は入っていないが、Mayo 抜粋のみの記述を減らす方向なので問題なし |
| 3 | 絶対NG表現が無い | OK | 下の「表現」「健康面」参照 |
| 4 | 「向いていない人」がある | OK | L194〜203 の節+各 Pick の L107・L128・L149・L169 |
| 5 | アフィリエイトリンクに rel="nofollow sponsored" | OK | Amazon リンク13本すべてに付いている(L23・80〜83・115・136・158・176・239〜242) |
| 6 | Amazon タグが quietrecover-20 | OK | 13本すべて tag=quietrecover-20。tag 無しの amazon.com リンクは0 |
| 7 | 内部リンクが `{{ '/posts/x/' | url }}` 形式で、公開済み | OK | L28・L167・L192(sunrise、publishAt 2026-10-07)、L95(red-light、2026-07-25・publishAt 無し)、L201(blackout、2026-09-25/white-noise-day-sleepers、2026-11-25)。いずれも published: false 無し。素の `](/posts/...)` は0 |
| 8 | 未設定 ASP のプレースホルダーが無い | OK | YOURTAG 等 0件 |
| 9 | タイトル・ディスクリプションが既存記事と重複しない | OK | 下の「重複確認」参照 |
| 10 | フロントマターの形式 | OK | L2〜10: layout / title / description / date / tags / category に加え、published: false・permalink: false・eleventyExcludeFromCollections: true の3点あり |

### 追加確認
- 手書きの価格・金額・割引率・セール名: 無し。`$`・`%`・Black Friday・Prime・deal・coupon・free shipping・sale を検索して0件。価格は「budget / mid-range / premium」の相対表現のみ(L71〜74、注記 L76)
- 冒頭の開示: L13(アフィリエイト開示+Not medical advice+「使っていない」の明記)。末尾の医療免責: L245
- 一人称の虚偽テスト表現: 無し。「the manual we read」(L42・L122)は資料を読んだ事実の記述で、使用体験ではない。L13 で "We have not used these products ourselves" と明記
- 誇大表現: always / guaranteed / cures / everyone should / proven / boost 等は0件。メーカーの宣伝文句(clinically proven、completely safe、Doctor Recommended、lift spirits 等)も入っていない

### 健康面
- **効果の断定: 無し。** 冬季うつ(SAD)は NIMH の説明として「describes」で紹介(L44)し、「not a routine we're suggesting」と線を引いている。気分・睡眠が良くなるという記述は無く、L188「We're not saying the pair will make mornings easier」、L52「We're not claiming one works better」、L19「compares tools, not treatments」で効果の比較を避けている。L209 も明るさと使う場面の違いだけで、効果の比較をしていない
- **NIMH・説明書・ガイド(本文を読めた出典)の範囲:** L44・L92・L190・L196 前半(NIMH)、L42・L93・L124・L126・L200(Verilux 説明書)、L143・L147・L190・L221 後半(NorthStar ガイド)は、04_factcheck_2 の #10〜#28・#31 で本文と照合済み。範囲を超えた記述は無い
- **Mayo Clinic だけを根拠にした記述(403 で本文を読めていない):**
  - L92: 現在の文は「NIMH notes that light boxes for SAD filter out UV light」+「Lamps made for skin conditions are a different kind of device」。UV の部分は NIMH(本文確認)。後半は Mayo の名前を出さず、UV が出る・眼を傷めるといった健康上の主張もしていない一般的な区別なので問題なし
  - L196: 「health sources such as Mayo Clinic suggest using a light box with a provider's guidance」— 医師に相談する方向の記述で、同じ文の NIMH(本文確認)とも同じ趣旨。断定的ではない
  - L197: 例の「glaucoma, cataracts, eye damage from diabetes」は Mayo の抜粋だけが根拠(黄斑変性は Verilux 説明書、「眼の病気がある人は相談」自体は NIMH・Verilux・NorthStar の本文で確認済み)。ただしこれは設計図の健康面の表(03_architect_2 L161・L269)で「要目視」付きで認められていた内容に戻したもので、使うことは決まっていた。中身も「使う前に眼科医に相談」という慎重な方向なので、効果を断定する記述にはあたらない
  - L199: 「Mayo Clinic advises caution」— 「注意を促している」とだけ書き、具体的な躁症状の説明は Mayo の言葉として書いていない。軽躁については Verilux 説明書(本文確認)で裏付けがある
  - L213: 「Mayo Clinic advises following the manufacturer's instructions」— 一般的な数字を勧めず説明書に従うよう促すだけで、健康効果の主張ではない
  - L221: 朝に使うという点は NIMH(本文確認)と同じ趣旨。Mayo は付け足し
  - L225: 処方の要否は「sold directly to consumers」という事実で答え、Mayo は医療者の指導という慎重側の一文だけ
  - **結論: どれも医師に相談する・注意するという慎重な方向の記述で、効果の断定や読者への使用指示は無い。差し戻しにはしない。** ただし出典を名指しして書いている以上、本文を読めていない状態のまま公開するのは「正確性が最優先」に反する。**公開前の人間確認で Mayo Clinic の本文目視を必須にする**(04_factcheck_2「人間確認として残すもの」の2点目)。確認できなかった場合や表現が違った場合は、公開作業のときに次のとおり直す(どれも1行内の書き換え):
    - L196: 「, and health sources such as Mayo Clinic suggest using a light box with a provider's guidance」を削除
    - L197: 「(such as glaucoma, cataracts, eye damage from diabetes, or macular degeneration)」→「(the Verilux manual mentions macular degeneration)」にし、「NIMH, Mayo Clinic, the Verilux manual, and the NorthStar guide all raise this」→「NIMH, the Verilux manual, and the NorthStar guide all raise this」
    - L199: 「Mayo Clinic advises caution, and the Verilux manual mentions possible hypomania」→「The Verilux manual mentions possible hypomania with some mental health conditions」
    - L213: 「Mayo Clinic advises following the manufacturer's instructions, so use your manual's distance」→「Use the distance in your lamp's manual」
    - L221: 「NIMH and Mayo Clinic describe it」→「NIMH describes it」
    - L225: 「Health sources such as Mayo Clinic still suggest using one with a provider's guidance」→「NIMH encourages talking with a provider about treatment options first」

### 重複確認
- sunrise-alarm-clocks-wake-up-light-comparison: title「Sunrise Alarm Clocks: Hatch vs. Lumie vs. Philips Compared」/description は「起こし方・音・スマホなしで使えるか・パートナー」が軸。本記事は「ランプか目覚ましか」と「10,000 lux の距離」が軸で、目覚まし側は Philips HF3520 の1台だけ(L161〜177)。Hatch・Lumie・パートナーの話は sunrise 記事に送っている(L167・L184・L192)。タイトル・ディスクリプションとも言葉の重なりは「sunrise alarm」程度で、重複しすぎていない
- red-light-therapy-devices-for-home・white-noise-machine-for-day-sleepers(wake-up light に触れる)・blackout-curtains とも、タイトル・ディスクリプションの軸が別。ほかの既存記事とも重複なし

## 差し戻しにしない軽い指摘
1. **Mayo Clinic の本文目視を公開の条件にする**(上記)。人間確認リストの中で、Amazon 確認と同じ重さで扱うこと
2. L192: 「section on alarms that won't wake your partner」というアンカー文なのに、リンク先は sunrise 記事の冒頭。見出しへのアンカー(該当見出しは sunrise 記事 L126)が使えるなら付けると親切。使えなければ文言を「our sunrise alarm comparison also covers alarms that won't wake your partner」程度にする
3. L15: 「Search for a fix」の "fix" は設計図の「見出しに Fix を使わない」に直接は当たらない(本文・検索行動の描写)が、治す道具を探す印象をわずかに残す。「Search for help」などにしてもよい
4. L65: 比較表の目覚まし側「Check with a doctor first if… You're sensitive to light or have an eye condition」は出典の無い一般的な注意(ファクトチェックも対象外とした)。慎重側なので残してよい
5. 公開作業時の残り(設計図「人間確認」7): categories.json の posts に `"light-therapy-lamp-vs-sunrise-alarm-clock": "sleep-environment"` を追加、publishAt の決定、published: false などの3点の解除
6. Carex の公式説明書、Verilux Luxe の現行説明書の版の確認(04_factcheck_2 の人間確認)は残っている。本文は「確認できなかった」(L105)と正直に書いているので、確認できなくても公開の妨げにはならない
