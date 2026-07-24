# セットアップガイド:デプロイ〜アフィリエイト登録

## このプロジェクトの中身

```
affiliate-site/
├── src/                    ← サイトの中身(記事はここに追加していく)
│   ├── posts/               ← ブログ記事(Markdown)
│   ├── _includes/           ← レイアウト(base.njk, post.njk)
│   ├── _data/site.json      ← サイト名・説明文などの共通設定
│   └── assets/style.css     ← デザイン
├── .github/workflows/deploy.yml  ← GitHub Pagesへの自動デプロイ設定(すでに完成)
├── docs/                    ← この運用ガイド類
└── package.json
```

## ステップ1: ローカルで確認する(任意・スキップ可)

これは公開前にパソコン上だけでサイトの見た目を確認したい場合のおまけの工程。急ぎでURLだけ必要な場合(Pinterest申請など)は、この工程は飛ばしてステップ2に進んでよい。

ターミナル(Mac右上の虫眼鏡で「ターミナル」と検索)を開き、以下を1行ずつ実行する。

```
cd "/Users/kisaragisaito/Library/Mobile Documents/iCloud~md~obsidian/Documents/アフィリエイト/海外/海外アフィ/website"
npm install
npx @11ty/eleventy --serve
```

ブラウザで `http://localhost:8080` を開けば、今作ったサイトがそのまま見られる。終了する時はターミナルで Control+C。

## ステップ2: GitHubアカウント・リポジトリ作成

1. https://github.com でアカウント作成(無料)
2. 右上「+」→「New repository」。リポジトリ名は何でも良い(例: `home-recovery-blog`)。Public推奨(GitHub Pages無料枠はPublicリポジトリが基本)
3. ローカルの `website` フォルダをそのリポジトリにpush

```
cd "/Users/kisaragisaito/Library/Mobile Documents/iCloud~md~obsidian/Documents/アフィリエイト/海外/海外アフィ/website"
git init
git add .
git commit -m "initial site"
git branch -M main
git remote add origin https://github.com/【あなたのユーザー名】/【リポジトリ名】.git
git push -u origin main
```

## ステップ3: GitHub Pagesを有効化

1. GitHub上でリポジトリの「Settings」→「Pages」
2. 「Build and deployment」の「Source」を **GitHub Actions** に設定
3. mainブランチにpushすると、`.github/workflows/deploy.yml` が自動でビルド&公開してくれる
4. 数分後、`https://【ユーザー名】.github.io/【リポジトリ名】/` でサイトが見られる

## ステップ4(後で): 独自ドメインに切り替える

無料運用に慣れて、収益が見えてきたら独自ドメイン(年1,000〜2,000円程度)を取得してGitHub Pagesに接続すると信頼性・SEOともに有利。ドメイン取得後、GitHubの「Pages」設定にある「Custom domain」欄に入力するだけで反映される。

**独自ドメインに変えたら**、`src/_data/site.json` の `url` を実際のドメインに書き換えること(現在は仮で `https://example.com` になっている)。

## ステップ5: アフィリエイトプログラムに登録する

### Amazon Associates(最優先・無料)
1. https://affiliate-program.amazon.com (US向けならこちら。日本のAmazonアソシエイトとは別プログラム)
2. サイトURL(GitHub Pagesで公開したURL)を登録
3. 承認後、発行される Associate ID(例: `yourtag-20`)を、記事中の `YOURTAG-20` プレースホルダーすべてに置き換える
4. 審査には「180日以内に一定数の適格販売」が必要な場合がある点に注意(Amazon側の規約は変更されることがあるので登録時に必ず最新の条件を確認)

### 個別ブランドの高単価プログラム(収益が育ってきたら)
以下のようなアフィリエイトネットワーク経由で、レッドライトセラピー・サウナブランケット・睡眠系ブランドの個別プログラムに申請できる場合がある。

- ShareASale
- CJ Affiliate (Commission Junction)
- Impact
- Awin

いずれも無料でアカウント作成でき、サイトが「実在するコンテンツを持つブログ」であることが承認の前提になることが多いため、まずは記事を数本〜十数本公開してから申請するのが通りやすい。

## ステップ6: サイトに新しい記事を追加する方法

`src/posts/` に新しい `.md` ファイルを作り、既存記事と同じフロントマター形式(`layout`, `title`, `description`, `date`, `tags: post`)をコピーして書き足すだけで、自動的にトップページと `sitemap.xml` に反映される。

## 運用上の注意点

- Amazon Associatesのリンクには `rel="nofollow sponsored"` を付ける(すでにテンプレートに組み込み済み)。これはGoogle・Amazon双方のガイドライン対応
- 医療・健康効果を断定する表現は避ける(「may help」「some research suggests」等、断定しない書き方に統一済み)
- 記事内のアフィリエイト開示(`/affiliate-disclosure/`)は必須。米FTC向けに用意済みだが、実際に公開する前に一度目を通すこと

## ステップ7: Pinterest/Xへの自動投稿を有効にする

`scripts/` にPinterest・X用の自動投稿スクリプトを用意してある。使うには:

```
cd scripts
pip install -r requirements.txt
cp ../.env.example ../.env
```

`.env` にPinterest/XのAPI認証情報を入力する手順は `docs/social_api_setup.md` を参照(Pinterestは無料だがStandard access昇格に動画審査が必要、Xは2026年以降従量課金制)。認証情報が未設定の間は、`run_promotion.py` がピン画像の生成だけ行い投稿はスキップする安全設計になっているので、途中の状態でも壊れることはない。
