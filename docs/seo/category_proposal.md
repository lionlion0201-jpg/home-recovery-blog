# Topic (category) proposal — QuietRecover

ブランチ `seo/clusters`。如月さんの承認待ち。

## 目的
- 記事末尾の関連記事(Related Reading)が全記事(22本)へのリンクになっていて、テーマのまとまりが Google に伝わらない。
- テーマ別のまとめページ(/category/<スラッグ>/)を作り、関連記事を同じテーマの記事(最大6本)に絞る。

## 仕組み
- テーマの定義と「記事スラッグ → テーマ」の対応は `src/_data/categories.json` に置く。記事フロントマターの `category` は書き換えていない(表の「旧category」)。表示・まとめページ・パンくずは categories.json の結果を使う。
- **新しい記事を作ったら、`categories.json` の `posts` に `"記事スラッグ": "テーマのスラッグ"` を1行足す。**
  足し忘れた場合は、フロントマターの `category` をテーマの slug・表示名・aliases(旧カテゴリ名)と照合する。`Sleep` → Bedroom Sleep Environment、`Recovery` → Recovery & Massage、`Wearables` → Sleep Tracking & Sleep Aids、`Gift Guide` → Gift Guides。どれにも当たらなければ「テーマなし」(まとめページに出ない、パンくずは Home > 記事、関連記事は新しい順4本)で、ビルド時に警告が出る。
- まとめページ・関連記事には公開済みの記事だけが出る。公開中が0本のテーマはページを作らない。
- 関連記事:同じテーマの公開記事を新しい順に最大6本。同テーマが4本未満なら、ほかのテーマの新しい記事で4本まで補う。

## 見直しの内容
- 旧 Sleep(12本)を「寝室の環境(温度・音・光)」と「睡眠の計測・サポート用品」に分割。
- 旧 Wearables(2本)は「睡眠の計測・サポート用品」に統合。
- 旧 Gift Guide(2本)は4本未満だが、年末商戦(ブラックフライデー告知期間 11/27〜)の入口として独立させた。統合する場合は Recovery & Massage へ。

## 決めてほしいこと
1. Gift Guides を2本のまま独立させるか。
2. 下の表の「迷った理由」がある記事の振り分け。

## テーマ一覧

| 表示名 | スラッグ(URL) | 公開中 | 全体(予約・下書き含む) | 導入文 |
|---|---|---|---|---|
| Recovery & Massage | /category/recovery/ | 9 | 10 | Guides to at-home recovery tools — red light therapy, cold plunges, sauna blankets, massage guns, compression boots and shiatsu massagers — compared on cost, space and everyday practicality. We explain what each tool is designed to do and say plainly where the evidence is still thin. This is general information, not medical advice: if you have an injury, a heart condition, are pregnant, or live with ongoing pain, talk to your doctor before using heat, cold or massage devices. |
| Bedroom Sleep Environment | /category/sleep-environment/ | 8 | 10 | Comparisons of the gear that shapes your bedroom at night: temperature (cooling pillows, dual-zone bedding, quiet heaters, humidifiers), noise (sound machines, sleep earbuds) and light (blackout curtains, sunrise alarms). Each guide focuses on fit for a specific situation — hot sleepers, couples, light sleepers and day sleepers. If poor sleep persists, see a doctor; ongoing insomnia, loud snoring or night sweats can have medical causes worth checking. |
| Sleep Tracking & Sleep Aids | /category/sleep-tracking-aids/ | 4 | 4 | Honest comparisons of sleep trackers such as the Oura Ring, Whoop and Apple Watch, plus popular sleep aids like weighted blankets and magnesium supplements. We cover what these products measure or claim and where the research is limited. Wearables are not medical devices for diagnosing sleep disorders, and supplements can interact with medications — check with your doctor or pharmacist before starting one. |
| Gift Guides | /category/gift-guides/ | 2 | 2 | Gift ideas for people who care about recovery and sleep, organized by budget and by recipient. Each pick links back to our full comparison guides so you can check the details before buying. Prices and availability change often, so confirm them at the retailer. |

公開中 23 本 / 全 26 本(2026-10-17 時点の判定)。公開中の記事が0本のテーマはページを作らない。

## 記事 → テーマの対応表

迷った記事は「迷った理由」欄に、ほかの候補と決め手を書いています。

### Recovery & Massage(recovery)

| 記事タイトル | スラッグ | 状態 | 旧category | 迷った理由 |
|---|---|---|---|---|
| Cold Plunge vs. Red Light Therapy: Which Recovery Tool Should You Buy First for Sore Muscles? | cold-plunge-vs-red-light-therapy | 公開中 | Recovery |  |
| Cold Plunge vs. Sauna Blanket: Which Should You Buy First for Recovery? | cold-plunge-vs-sauna-blanket | 公開中 | Recovery |  |
| Heated Foot Massagers for Nurses and On-Your-Feet Workers: Shiatsu vs. Air Compression | heated-foot-massagers-nurses-standing-workers | 公開中 | Recovery | 運動後の回復というより日常の疲れ向け。マッサージ機器をまとめるため Recovery & Massage に |
| Massage Gun vs. Compression Boots: Which Actually Cuts Post-Workout Soreness at Home? | massage-gun-vs-compression-boots-recovery | 公開中 | Recovery |  |
| Red-Eye Flight Recovery Kit: What to Pack to Sleep on a Plane and Land More Comfortably | red-eye-flight-recovery-kit-carry-on | 公開中 | Recovery | 睡眠(機内で眠る)も候補。商品がネックピローと小型マッサージャーなので、旧カテゴリどおり Recovery & Massage に |
| Best Red Light Therapy Devices for Home Use: A Buyer's Guide by Budget | red-light-therapy-devices-for-home | 公開中 | Recovery |  |
| Red Light Therapy vs Massage Gun: Which Recovery Tool Should You Buy First? | red-light-therapy-vs-massage-gun | 公開中 | Recovery |  |
| Infrared Sauna Blanket vs. Home Sauna: Which Is Worth It in a Small Space? | sauna-blanket-vs-home-sauna | 公開中 | Recovery |  |
| Shiatsu Neck & Shoulder Massagers for Desk-Related Tension: A Buyer's Guide | shiatsu-neck-shoulder-massager-desk-tension | 公開中 | Recovery |  |
| Shiatsu Back Massager for Office Chair: 3 Heated Cushion Types Compared for Desk Workers | shiatsu-back-massager-office-chair-desk-workers | 予約(2026-10-22) | Recovery |  |

### Bedroom Sleep Environment(sleep-environment)

| 記事タイトル | スラッグ | 状態 | 旧category | 迷った理由 |
|---|---|---|---|---|
| Best Cooling Pillows & Pads for Menopause Night Sweats and Hot Flashes: 3 Picks for Sleeping Cooler | best-cooling-pillow-for-menopause-night-sweats | 公開中 | Sleep |  |
| Best Quiet Bedroom Humidifiers for Fall: Stop Waking Up With a Dry Throat | best-quiet-bedroom-humidifiers-for-fall | 公開中 | Sleep | 寝室の空気(乾燥)の話なので Bedroom Sleep Environment に |
| Blackout Curtains vs. Sleep Masks for Day Sleepers: Which Actually Blocks More Light? | blackout-curtains-sleep-masks-for-day-sleepers | 公開中 | Sleep |  |
| Couples With Different Sleep Temperatures: Dual-Zone Bed Options Compared (Two Comforters, Heated Pads & BedJet) | couples-different-sleep-temperatures-dual-zone-bed | 公開中 | Sleep |  |
| Quiet Space Heaters for Bedrooms: Oil-Filled vs. Ceramic for Light Sleepers (Clicks, Hum & Glow Compared) | quiet-space-heaters-bedroom-light-sleepers | 公開中 | Sleep |  |
| Sleep Earbuds vs. Earplugs for a Snoring Partner: What Works for Side Sleepers | sleep-earbuds-vs-earplugs-snoring-partner | 公開中 | Sleep |  |
| Sunrise Alarm Clocks Compared: Which Wake-Up Light Fits Your Bedroom? | sunrise-alarm-clocks-wake-up-light-comparison | 公開中 | Sleep |  |
| Best Noise Machines for Light Sleepers: White Noise vs. Fan vs. Smart Sound Machines Compared | white-noise-machines-vs-sound-machines-light-sleepers | 公開中 | Sleep |  |
| Best Bedding for Couples With Different Temperatures: Cooling Options for the Hot Sleeper's Side | best-bedding-couples-different-temperatures-hot-sleeper | 予約(2026-10-18) | Sleep |  |
| White Noise Machine for Athletes: 3 Portable Picks for Hotel Rooms on Away Trips | portable-white-noise-machine-athletes-hotel | 予約(2026-10-20) | Sleep |  |

### Sleep Tracking & Sleep Aids(sleep-tracking-aids)

| 記事タイトル | スラッグ | 状態 | 旧category | 迷った理由 |
|---|---|---|---|---|
| Apple Watch vs. Oura Ring for Sleep: Do You Need Both If You Already Own an Apple Watch? | apple-watch-vs-oura-ring-sleep-tracking | 公開中 | Wearables | 旧 Wearables(2本のみ)。睡眠計測として Sleep Tracking & Sleep Aids に統合 |
| Magnesium Glycinate for Sleep: A Shift Worker's Subscription Comparison Guide | magnesium-glycinate-sleep-shift-workers | 公開中 | Sleep | 旧 Sleep。サプリメントなので寝室の環境ではなく睡眠サポート用品に |
| Oura Ring vs Whoop for Sleep Tracking: Which Smart Ring Actually Fits Your Recovery Goals? | oura-ring-vs-whoop-sleep-tracking | 公開中 | Wearables | 旧 Wearables(2本のみ)。睡眠計測として Sleep Tracking & Sleep Aids に統合 |
| Do Weighted Blankets Actually Help With Sleep and Anxiety? | weighted-blankets-sleep-anxiety | 公開中 | Sleep | 旧 Sleep。寝具なので Bedroom Sleep Environment も候補。「睡眠・不安に効くのか」が主題なので睡眠サポート用品側に(このテーマの公開数を4本にする意味もある) |

### Gift Guides(gift-guides)

| 記事タイトル | スラッグ | 状態 | 旧category | 迷った理由 |
|---|---|---|---|---|
| 2026 Recovery & Sleep Gift Guide: Best Picks by Who You're Buying For (Him, Her, Athletes, Tired Parents) | 2026-recovery-sleep-gift-guide-by-recipient | 公開中 | Gift Guide | 同上 |
| Best Home Recovery & Sleep Gifts 2026: The Ultimate Guide by Budget, From Stocking Stuffers to Splurges | best-recovery-and-sleep-gifts-2026 | 公開中 | Gift Guide | ギフトガイドは2本のみ。年末商戦の入口として独立テーマにした。別案: Recovery & Massage に統合 |
