# Pinterest & SNS 運用プラン

## ニッチ戦略まとめ

- **ニッチ**: Home Recovery & Sleep Wellness(自宅リカバリー・睡眠ウェルネス機器)
- **狙い**: 単価が高く($100〜$2,000)、需要が一時的なブームでなく緩やかに伸び続けている、Pinterest/SEOと相性が良い、Amazon Associatesを軸に複数のASPで収益源を分散できる
- **将来的な拡張**: サブスク型サプリ・会員制コンテンツのアフィリエイトを組み込めば、リカーリングコミッション(継続報酬)化も狙える

## Pinterestボード構成(まず5つ)

1. **Red Light Therapy at Home** — 記事1(red-light-therapy-devices-for-home)からのピン
2. **Home Sauna & Sweat Recovery** — 記事2(sauna-blanket-vs-home-sauna)からのピン
3. **Better Sleep Tools** — 記事3(weighted-blankets-sleep-anxiety)からのピン
4. **Recovery Room Inspiration**(汎用・画像中心、SEO記事に紐付かなくてもOK。世界観作り用)
5. **Budget Wellness Finds**(価格帯別のまとめピン。複数記事を横断)

## ピン3型フレームワーク(記事ごとに必ずA/B/C揃える)

同じ記事から作るピンは、切り口を変えた3タイプを基本セットにする(詳細は`agents/promoter.md`)。

- **A. 悩み解決型** — 悩みをそのまま言葉にする
- **B. 比較型** — 選択肢を並べて記事で答えを知りたくなる入口を作る
- **C. 使用場面型** — 商品名でなく使用後の場面・状態を見せる

**記事1: Red Light Therapy**
- [A]「Best Red Light Therapy Devices for Home Use (By Budget)」
- [B]「Handheld vs Full-Body Red Light Panel: Which Do You Need?」
- [C]「5 Things to Check Before Buying a Red Light Therapy Panel」

**記事2: Sauna Blanket vs Home Sauna**
- [A]「Sauna Blanket vs Home Sauna: Which Fits a Small Apartment?」
- [B]「Budget-Friendly Way to Get Sauna Benefits at Home」
- [C]「A Weeknight Sweat Routine for a Small Apartment」

**記事3: Weighted Blankets**
- [A]「Do Weighted Blankets Actually Work? What Research Says」
- [B]「How to Pick the Right Weighted Blanket Weight (Chart Inside)」
- [C]「A Calmer Bedtime Routine, One Blanket at a Time」

画像内テキストは2行以内・アクセントカラー1色を目安に、`scripts/generate_pin_image.py`で生成する(Canva等の手作業ツールは使わず、自動生成で統一する)。

## ピン説明文の型

```
[フック文で悩みを提示] + [記事が解決すること] + [キーワード自然に含める] + [CTA]

例:
Not sure if a red light therapy panel is worth it? Here's a no-hype
buyer's guide comparing handheld vs full-body panels by budget —
plus what actually matters (wavelength, irradiance, warranty).
Read the full guide → [link]
#redlighttherapy #homewellness #recoverytools
```

ハッシュタグは2〜8個、説明文末尾に配置。

## 運用ペース(週5時間未満で回す場合)

- 新規ピン画像は週5〜10枚を目安。週次の自動パイプライン(`run_promotion.py`)がA/B/C3枚を毎サイクル生成・投稿するので、手動でのテンプレート作業は基本不要
- 新記事を書いたら、その記事から最低3種類(A/B/C)のピンを作る

## SNS(X / Instagram)への転用テンプレート

ブログ記事1本から、SNS投稿を3〜4個切り出す。

1. **フック投稿**: 記事の核心的な問いを1文で(例: 「Weighted blankets: placebo or does the research actually back this up?」)
2. **リスト投稿**: 記事内の表や比較ポイントを箇条書きで再構成
3. **Before/After的投稿**: 「よくある間違い→正しい選び方」の対比
4. **リンク付き投稿**: 記事へのCTA、ピンと同じ説明文の短縮版

Instagramの場合は上記をカルーセル画像(1枚目=フック、2〜4枚目=要点、最終枚=CTA)にすると相性が良い。

## 次に記事を追加するときの選定基準

- 単価が高い、または継続課金型の商品を含められるか
- Pinterestで視覚的に見せられる(製品写真・図解・比較表が作れる)か
- 一時的なトレンドではなく、検索需要が年間を通して安定しているか(Googleトレンドで確認推奨)

候補: cold plunge tubs, massage guns, smart sleep trackers(Oura等), magnesium/sleep supplement subscriptions(リカーリング狙い), percussion recovery devices
