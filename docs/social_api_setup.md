# Pinterest / X 自動投稿セットアップガイド

## 現在の申請状況(2026-09-19更新)

- Pinterest Standard access: **2026-09-17に承認済み**(App ID 1594065)。本番投稿が可能な状態になった。以前の`403 Apps with Trial access may not create Pins in production`は解消しており、サイクル実行時に審査状況を確認したり申請を促したりする必要はない
  - 承認後の運用については `pipeline_runbook.md` の「Pinterest投稿の運用」を参照すること。ピン投稿は週次パイプラインではなく `pinterest-backlog.yml`(毎日10:00 JST、1日4枚のドリップ)が担当する
  - 以下は承認に至るまでの経緯(記録として残す)
  - 2026-09-16: 審査が9日経過しても進捗がないため、Pinterest Help Center経由でサポートチケットを提出済み(カテゴリ: Pinterest API and Developer Tools → API Access → Application Status)。Pinterest Business Community(公式フォーラム)は運営が新規スレッドをKNOWN ISSUEスレッドにクローズ/マージする運用になっており、かつApp ID等の投稿が規約違反になるため、フォーラムへの投稿は行わずサポートチケットのみとした
  - 2026-09-16(続報): サポート担当Teriから返信あり。初回申請(2026-09-07)は実際には**却下されていた**(保留ではなかった)。却下理由はデモ動画がOAuth認可フロー全体とAPI呼び出しの両方を1本の連続録画で示せていなかったため。要求されたデモ内容: ①OAuth認可URLを開いてユーザーが許可する画面 → ②リダイレクトで認可コードを受け取る → ③コードをアクセストークンに交換 → ④そのトークンで実際にAPI呼び出し(ピンまたはボード作成)を行い成功レスポンスを得る、までを画面を切り替えても構わないので一度も録画を止めずに撮ること
  - 2026-09-17: 上記要件を満たす形でOAuthフロー(Sandbox環境、`api-sandbox.pinterest.com`)を実際に動かして動画を再撮影し、Developer PortalのApp ID 1594065 Configureページ「アクセスをアップグレードする」から再申請完了。Teriのサポートチケットにも再申請済みである旨を返信済み。次サイクル以降は再申請の審査結果(承認/却下)を確認すること
  - 補足(技術メモ): Sandbox環境でOAuthトークンを取得する際は、通常の`https://api.pinterest.com/v5/oauth/token`ではなく**`https://api-sandbox.pinterest.com/v5/oauth/token`**を使う必要がある(本番用トークンではSandbox APIの認証が通らず`{"code":2,"message":"Authentication failed."}`になる)。また、curlでBasic認証ヘッダーを手動base64エンコードすると入力ミスが起きやすいため、`-u "{client_id}:{client_secret}"`オプションを使う方が確実。デモ用にSandboxボードを作成する際は、同名ボードが既に存在すると`{"code":58,"message":"Try a different name..."}`になるため、毎回ユニークな名前(日付入りなど)にすること。動作確認だけしたい場合はOAuthフローを経由せず、Developer Portal → Configure → 「Generate Access Token」からSandboxトークンをワンクリックで発行することも可能(ただしStandard access審査用の動画としてはOAuthフロー自体を見せる必要があるため、審査提出用の動画ではこのショートカットは使えない)
- X (Twitter) API: 認証情報設定済み・投稿実績あり(2026-09-05、2026-09-12サイクルで実際に投稿成功)

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
