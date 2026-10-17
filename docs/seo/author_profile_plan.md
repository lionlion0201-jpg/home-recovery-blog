# 運営者プロフィール(E-E-A-T)構成案と質問案 — QuietRecover(US)

作成: 2026-10-17。構成案と質問リストのみ。プロフィール本文は含まない。本文は如月さんの実体験の回答をもとに作る(事実を創作しない)。サイトは英語なので、最終的なページは英語で書く。この文書は日本語。

## (a) 現状の不足点

現在の About(`src/about/index.md`)は4段落。書いてあるのは「実用的な調査型の買い方ガイド」「トレンドを追わない」「商品スペック・メーカー資料・公開レビューから調査」「健康の話題は断定せず専門家への相談を促す」「質問はプライバシーポリシーの連絡先へ」。

| # | 不足 | 影響 |
|---|---|---|
| 1 | 誰が運営しているか無い。著者は "QuietRecover Team"(Organization) | 睡眠・健康は経験/信頼性が重く見られる分野。個人の顔が見えない |
| 2 | 睡眠・リカバリーに関する運営者の実体験が無い | Experience が評価できない |
| 3 | 連絡先が About に無い(プライバシーポリシーに lionlion0201@gmail.com が書かれており、Aboutはそこへ誘導) | 一応の導線はあるが、About から直接見えない。サイト用の専用アドレスにするかも検討 |
| 4 | 記事の作り方が説明されていない。AI を使った下書きと人間のレビュー、ファクトチェックの工程が About に書かれていない(US の docs/agents/fact_checker.md では公式情報との照合を行う運用がある) | 透明性不足。AI利用の明示が無い(JP は書いている) |
| 5 | 商品を実際に使ったかどうかの区別が無い。記事内に "None of these are personal endorsements" の類の記述はあるが、サイト方針として明文化されていない | 誤解を避けつつ、「調査に基づくガイド」であることを誠実に示せる |
| 6 | 医療情報の扱いは1文のみ。監修者の有無、運営者が医療者でないことが明記されていない | YMYL(健康)に近い。線引きの明文化が必要 |
| 7 | 更新方針が無い(価格・在庫・製品の世代交代、訂正の手順) | 鮮度の担保が見えない。更新日表示は今回実装済み |
| 8 | 収益構造は affiliate-disclosure にあるが About から触れていない | 導線の補強 |
| 9 | 記事末尾に著者表示が無い | 記事単位の帰属が無い |
| 10 | 外部プロフィール(X: @quietrecover は site.json にあるが About からリンクが無い) | 実在性の補強 |

## (b) 推奨する About ページの構成(見出し案)

1. What this site is(目的と読者。2〜3文)
2. Who runs it(名前/ハンドル名、顔出しは任意。事実のみの一言)
3. Why I care about sleep and recovery(実体験。[回答から])
4. How articles are made(下記の骨子)
5. How we choose and compare products(基準。使った物と調べた物の区別)
6. Health information(医療者ではないこと、監修の有無、受診を促す方針)
7. Updates and corrections(更新日の表示、価格変動、訂正の連絡先)
8. How the site earns money(アフィリエイト、affiliate-disclosure へのリンク)
9. Contact(連絡先)
10. Links(X など。任意)

### 記事の作り方の説明案(誠実に書く場合の骨子。事実と違う部分は直す)

現状の運用(docs/agents/ と fact_checker.md より): マーケター → アーキテクト → レビュワー(AIによる本文執筆)→ ファクトチェッカー(商品の機能・仕様・機関の勧告・数字を、メーカー公式・政府機関の公式ページと照合。裏が取れない主張は弱めるか削る。Amazon の取扱いも確認)→ ディレクター(公開可否)→ 人間の週末レビュー → 公開。

- "Drafts are written with the help of AI tools. Before publishing, product claims (features, specs, safety guidance) are checked against manufacturer pages and official sources, and an editor reviews each article." — ファクトチェック工程が実際に全記事で動いている場合のみこの形。動き始めた日以降の記事に限るなら、そう書く(「2026年10月以降の記事は」など)
- "We research products from specs, manufacturer documentation, and public reviews. We have not tested every product ourselves; where we have, we say so." — 実際に使った物が無い間は、前半だけ書く
- 書かないこと: "expert-reviewed", "lab-tested", "we tested" (根拠が無い限り), 医療者を思わせる肩書き

## (c) 如月さんへの質問リスト(全部で15問)

すべて、答えたくなければ「無回答」で構いません。個人が特定される情報は出さず、ハンドル名と "an independent writer" のような書き方にすることも可能です。

**A. 実体験(最重要)**
1. 睡眠やリカバリーで、実際に自分で使ったことがある物(マットレス、枕、寝具、ウェアラブル、レッドライト、サウナ関連、マッサージ機 など)。商品名またはカテゴリ、使った期間
2. 使ってみて良かった点・不便だった点・やめた物とその理由
3. 睡眠で悩んだ経験(寝つき、暑さ、いびき、など。話せる範囲で)と、試して変わったこと/変わらなかったこと
4. 運動・トレーニング習慣やリカバリーの習慣(あれば。週何回、何をしているか)
5. 記事で扱ったカテゴリのうち、実際に買って使った物はどれか(あれば記事名を教えてください。記事に「使った」と明記できます)

**B. 運営者について**
6. 表示したい名前(本名/ハンドル名/チーム名のまま)と顔出しの可否(任意)
7. 本業・経歴のうち公開してよく、関係するもの(任意)
8. 睡眠・健康・栄養・スポーツに関する資格や専門的な学習歴(あれば。無ければ「無し」。その場合、専門家とは書かない)
9. サイトを始めたきっかけ(一言)

**C. 運営方針**
10. 公開してよい連絡先。現在は lionlion0201@gmail.com がプライバシーポリシーに載っている。サイト専用のアドレスに変えたいか
11. 米国の読者向けサイトを日本から運営していることを書くか(書かない選択も可。書くと誠実さは増すが、書かなくても虚偽にはならない。**米国在住などと書かないこと**)
12. 医療者や専門家による監修を依頼する予定はあるか(無いなら、無いと明記する方針で良いか)
13. ファクトチェックの手順を About に書いて良いか(上記の骨子で事実と合っているか確認)
14. 訂正の連絡を受けたときの対応(確認→修正→更新日を変更、で良いか)
15. 公開してよい外部アカウント(X: @quietrecover など)

## (d) 記事末尾の著者紹介テンプレート(中身は空欄)

```
<aside class="author-box">
  Written by [name / handle]. [1-2 sentences on the relevant background: only facts.]
  [If the author has used this product category: "I have used ___ for ___."  Otherwise delete this line.]
  Articles are researched from manufacturer documentation and official sources. This is general information, not medical advice.
  [Link to About]
</aside>
```

注意: 使っていない商品に "I tested" と書かない。資格や監修者が無いなら肩書きは書かない。

## 実装メモ(コードは今回変えていない)

- 公開日・更新日の表示と dateModified は実装済み(同じブランチ)。Aboutの内容確定後に、JSON-LD の author を Person に変える・著者ボックスを post.njk に足す、が次の作業
- 予約公開の publishAt はすべて 09:00 JST で書かれている。US の読者から見ると前日の夕方〜夜(米東部で前日20時)にあたるが、表示は書かれた日付(JST)のまま。米国の日付とずれて気になる場合は publishAt の扱いを決める必要がある
