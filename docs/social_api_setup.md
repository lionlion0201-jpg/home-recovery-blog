# Pinterest / X 自動投稿セットアップガイド

## 前提として知っておくべきこと(重要)

### Pinterest API
- **費用は無料**(Trial・Standardいずれも無料)
- ただし **Trial access だけだと投稿したピンは自分にしか見えない(Sandbox扱い)**。一般公開するには **Standard access** への昇格申請が必要
- Standard access申請には、実際にOAuth認証フローを完了して1件アクションを起こす様子を録画した動画の提出が必要(審査は営業日ベースで数日程度)
- つまり「Trial登録→動作確認→動画撮影→Standard申請→承認」まで完了して、初めて本番の自動投稿が機能する

### X (Twitter) API
- **2026年2月以降、新規デベロッパー向けの無料枠は廃止**。現在は従量課金(pay-per-usage)のみ
- 投稿コストは **リンクなし投稿: $0.015/件、リンクあり投稿: $0.20/件**、閲覧は $0.005/件
- 今回の運用(週1回、リンク付き投稿を3〜4件)を想定すると、月あたり目安 **$3〜4程度**(1回のサイクルで$0.80前後 × 月4回)。高額ではないが、無料ではない点は把握しておくこと
- Basic/Proプランへの新規申込みは終了しており、個人開発者は従量課金プランのみ選択可能

---

## Pinterest セットアップ手順

1. Pinterestビジネスアカウントを用意する(個人アカウントの場合は無料でビジネスアカウントに切り替え可能)
2. https://developers.pinterest.com にアクセスし、開発者アカウント登録
3. 「Connect app」から新しいアプリを作成。リダイレクトURI等は初期はローカル(例: `https://localhost/callback`)でOK
4. 作成したアプリで **Trial access** が自動的に付与される
5. OAuth認可フローを実行し、`pins:write` `boards:read` `boards:write` スコープを含むアクセストークンを取得する(Pinterestの公式ドキュメント「Getting started」の手順に従う。ブラウザでの認可画面→リダイレクトで認可コード取得→トークン交換、という一般的なOAuth2フロー)
6. 取得したアクセストークン・リフレッシュトークンを本プロジェクトの `.env` に保存する(下記参照)
7. ボードを1つ以上作成し、そのボードIDを控える(`GET /v5/boards` で取得可能)
8. ここまでできたら、実際に1件テスト投稿(Sandbox内)を行い、その様子を画面録画する
9. 録画をもとにPinterest Developer Portalから **Standard access** を申請する
10. 承認が下りたら、以降の投稿が一般公開される状態になる

## X (Twitter) セットアップ手順

1. https://developer.twitter.com でデベロッパーアカウントを作成
2. 新しいProject/Appを作成し、**OAuth 1.0a** の "Read and Write" 権限を有効にする(投稿にはWrite権限が必須)
3. 従量課金(pay-per-usage)プランに登録し、支払い方法を設定する
4. アプリの以下4つの認証情報を取得する:
   - API Key (Consumer Key)
   - API Key Secret (Consumer Secret)
   - Access Token
   - Access Token Secret
5. 取得した4つを `.env` に保存する

## `.env` の設定

プロジェクトルート(`website/`)に `.env.example` を用意した。これをコピーして `.env` を作り、値を埋めること。

```
cp .env.example .env
```

`.env` は `.gitignore` に含めてあるので、Gitにコミットされることはない。

## 重要な注意

- API資格情報(トークン・キー)は絶対に公開リポジトリにコミットしないこと
- Pinterestのアクセストークンには有効期限があり、リフレッシュトークンでの更新が必要になる場合がある(Pinterestの公式ドキュメント「Refresh a token」を参照し、定期的に更新すること)
- Xの従量課金は使った分だけ請求されるため、想定外の大量投稿がないよう `scripts/` 内のスクリプトは1回の実行で投稿する件数の上限を明示的にチェックする実装にしてある
