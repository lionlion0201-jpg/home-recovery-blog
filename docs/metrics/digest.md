# ファネル表(US)

生成日: 2026-11-23 / 生成: `scripts/build_digest.py`(手で編集しない)

読み方は `docs/agents/analyst.md` の「読み方のルール」に従う。**インプレッションは売上の指標ではない。**判断の主軸はアフィリエイトリンクのクリック(GA4 `affiliate_click`)。

## データの状態

| ソース | レコード数 | 対象投稿数 | 最終取得 |
|---|---:|---:|---|
| docs/metrics/posted_assets.json(投稿台帳) | 199 | 199 | - |
| docs/metrics/x_metrics.json(Xメトリクス) | 808 | 61 | 2026-11-23 05:12 |
| docs/metrics/pin_metrics.json(ピンメトリクス) | 3898 | 143 | 2026-11-23 05:12 |
| GA4 `affiliate_click` | あり | - | - |
| Search Console | 31 | - | 2026-11-20 まで |


## X投稿の型の比較(hook / cta など)

| 型 | 比較対象の投稿数 | うち計測済み | 目安 | 判定 |
|---|---:|---:|---:|---|
| thread_reply | 37 | 37 | 20 | 判断可(ただしクリック未取得なら保留) |
| thread_root | 15 | 15 | 20 | **データ不足**(従来方針を維持) |
| 不明 | 9 | 9 | 20 | 比較対象外(型が記録されていない) |

リンククリック(GA4)が取れていない間は、計測済み件数が目安に達しても型の優劣は結論しない(インプレッション単体で型を評価しない)。

## 検索(Search Console)

期間: 2026-10-23〜2026-11-20(Search Console は2〜3日遅れて確定する)/ 表示 515回 / クリック 1回
検索結果に載っている記事: 29 / 35(サイトマップの記事URLを URL 検査 API で確認)

表示が少ない記事の順位は日々大きく動く。表示100回未満の記事どうしの比較は「データ不足」とする。

| 記事 | 公開日 | 掲載 | 表示 | クリック | クリック率 | 平均順位 | 表示の多い検索語(順位) |
|---|---|---|---:|---:|---:|---:|---|
| Best Noise Machines for Light Sleepers:  | 2026-09-27 | ○ | 115 | 0 | 0.00% | 10.5 | futon vs white noise machine(9.5) |
| Shiatsu Back Massager for Office Chairs: | 2026-10-22 | ○ | 93 | 0 | 0.00% | 27.5 | back massagers for first respo(28.3) |
| Best White Noise Machine for Athletes: 3 | 2026-10-20 | ○ | 55 | 0 | 0.00% | 6.7 | best white noise machine for a(6) |
| Best Cooling Pillows & Pads for Menopaus | 2026-09-12 | ○ | 44 | 0 | 0.00% | 66 | intimacy pillow for menopause(58.6) |
| Red Light Therapy vs Massage Gun: Which  | 2026-09-05 | ○ | 33 | 0 | 0.00% | 7.7 | massage gun vs ring light(5.5) |
| Oura Ring vs Apple Watch for Sleep: Do Y | 2026-09-19 | ○ | 23 | 0 | 0.00% | 43.5 | oura ring 4 vs apple watch(24.4) |
| Whoop vs. Oura Ring for Sleep Tracking:  | 2026-07-27 | ○ | 21 | 0 | 0.00% | 30 | do i need orion intelligence i(8.2) |
| Sunrise Alarm Clocks: Hatch vs. Lumie vs | 2026-10-07 | ○ | 18 | 0 | 0.00% | 45.7 | philips smartsleep vs hatch(82.7) |
| Blackout Curtains vs. Sleep Masks for Da | 2026-09-25 | ○ | 16 | 0 | 0.00% | 6.7 | - |
| Best Bedding for Couples With Different  | 2026-10-18 | ○ | 11 | 0 | 0.00% | 17.5 | best mattress pad for dual hea(25.3) |
| Bedding for Couples When One Sleeps Hot: | 2026-10-05 | ○ | 11 | 1 | 9.09% | 17.4 | dual zone comforter(37) |
| Best Home Recovery & Sleep Gifts 2026, b | 2026-08-15 | ○ | 10 | 0 | 0.00% | 26.5 | i want a sleep gift with great(89) |
| Cooling Mattress Pad for Hot Flashes: 3  | 2026-10-26 | ○ | 7 | 0 | 0.00% | 56.3 | chilipad for night sweats(67) |
| Infrared Sauna Blanket vs. Home Sauna fo | 2026-07-25 | ○ | 7 | 0 | 0.00% | 80 | sauna blanket vs sauna(74.2) |
| Massage Gun vs. Compression Boots for Po | 2026-08-08 | ○ | 6 | 0 | 0.00% | 28.2 | normatec vs theragun(29.5) |
| Do Weighted Blankets Actually Help With  | 2026-07-25 | ○ | 5 | 0 | 0.00% | 12.2 | - |
| 2026 Recovery & Sleep Gift Guide: Picks  | 2026-09-19 | ○ | 4 | 0 | 0.00% | 7.8 | - |
| Smart Ring, No Subscription: Oura Ring A | 2026-11-04 | ○ | 4 | 0 | 0.00% | 79.5 | oura alternative without track(95) |
| Sleep Earbuds vs. Earplugs for a Snoring | 2026-10-15 | ○ | 3 | 0 | 0.00% | 8 | - |
| Best Quiet Bedroom Humidifiers for Fall  | 2026-08-29 | ○ | 1 | 0 | 0.00% | 4 | - |
| Sauna Blanket vs. Cold Plunge: Which to  | 2026-08-01 | ○ | 1 | 0 | 0.00% | 2 | - |
| Blackout Curtains for Renters, No Drill: | 2026-10-28 | ○ | 1 | 0 | 0.00% | 64 | renter friendly blackout curta(64) |
| Best Neck Massagers for Desk Workers: Sh | 2026-09-26 | ○ | 1 | 0 | 0.00% | 76 | - |
| Back Massager for First Responders: 3 Af | 2026-11-02 | × | 0 | 0 | 未取得 | - | - |
| Cold Plunge vs. Red Light Therapy: Which | 2026-09-19 | ○ | 0 | 0 | 未取得 | - | - |
| Compression Boots for Nurses: Full-Leg B | 2026-11-15 | ○ | 0 | 0 | 未取得 | - | - |
| Foot Warmer for Bed: Under-Sheet Warmer, | 2026-11-17 | ○ | 0 | 0 | 未取得 | - | - |
| Heated Foot Massagers for Nurses: Shiats | 2026-10-11 | × | 0 | 0 | 未取得 | - | - |
| Magnesium Glycinate for Sleep: Shift Wor | 2026-07-25 | ○ | 0 | 0 | 未取得 | - | - |
| Quiet Space Heaters for Bedrooms: Oil-Fi | 2026-10-13 | × | 0 | 0 | 未取得 | - | - |
| Red-Eye Flight Recovery Kit: What to Pac | 2026-10-06 | ○ | 0 | 0 | 未取得 | - | - |
| Best Red Light Therapy Devices for Home: | 2026-07-25 | ○ | 0 | 0 | 未取得 | - | - |
| What to Buy on Sale for Recovery and Sle | 2026-10-30 | × | 0 | 0 | 未取得 | - | - |
| White Noise Machine for Apartment Noise: | 2026-11-19 | × | 0 | 0 | 未取得 | - | - |
| White Noise Machine Without Light: 3 Sou | 2026-11-06 | × | 0 | 0 | 未取得 | - | - |

**伸ばす候補**(平均8〜30位・表示10回以上。1ページ目の下〜2ページ目にいて、タイトル・説明文・内部リンク・内容の補強で上位を狙える): `white-noise-machines-vs-sound-machines-light-sleepers`(10.5位)、`couples-different-sleep-temperatures-dual-zone-bed`(17.4位)、`best-bedding-couples-different-temperatures-hot-sleeper`(17.5位)、`best-recovery-and-sleep-gifts-2026`(26.5位)、`shiatsu-back-massager-office-chair-desk-workers`(27.5位)、`oura-ring-vs-whoop-sleep-tracking`(30.0位)

**検索結果に未掲載**: `back-massager-for-first-responders-after-shift`、`heated-foot-massagers-nurses-standing-workers`、`quiet-space-heaters-bedroom-light-sleepers`、`what-to-buy-on-sale-recovery-sleep`、`white-noise-machine-for-apartment-noise`、`white-noise-machine-without-light`(Search Console の URL 検査からインデックス登録をリクエストできる)

## 記事単位のファネル

記事の比較はセッション100以上が目安。セッションもGA4由来のため現時点では未取得。

| 記事 | 公開日 | 投稿数 | 配信(imp) | ピン→サイト遷移 | リンククリック | クリック到達率 |
|---|---|---:|---:|---:|---|---|
| White Noise Machine for Apartment Noise: | 2026-11-19 | 4 | 未取得 | 未取得 | 未取得 | 未取得 |
| Foot Warmer for Bed: Under-Sheet Warmer, | 2026-11-17 | 4 | 0 | 0 | 未取得 | 未取得 |
| Compression Boots for Nurses: Full-Leg B | 2026-11-15 | 4 | 0 | 0 | 未取得 | 未取得 |
| White Noise Machine Without Light: 3 Sou | 2026-11-06 | 4 | 0 | 0 | 未取得 | 未取得 |
| Smart Ring, No Subscription: Oura Ring A | 2026-11-04 | 4 | 6 | 0 | 未取得 | 未取得 |
| Back Massager for First Responders: 3 Af | 2026-11-02 | 4 | 0 | 0 | 0 | 未取得 |
| What to Buy on Sale for Recovery and Sle | 2026-10-30 | 4 | 0 | 0 | 未取得 | 未取得 |
| Blackout Curtains for Renters, No Drill: | 2026-10-28 | 4 | 0 | 0 | 未取得 | 未取得 |
| Cooling Mattress Pad for Hot Flashes: 3  | 2026-10-26 | 4 | 0 | 0 | 未取得 | 未取得 |
| Shiatsu Back Massager for Office Chairs: | 2026-10-22 | 4 | 0 | 0 | 未取得 | 未取得 |
| Best White Noise Machine for Athletes: 3 | 2026-10-20 | 4 | 1 | 0 | 未取得 | 未取得 |
| Best Bedding for Couples With Different  | 2026-10-18 | 4 | 8 | 0 | 未取得 | 未取得 |
| Sleep Earbuds vs. Earplugs for a Snoring | 2026-10-15 | 8 | 4 | 0 | 未取得 | 未取得 |
| Quiet Space Heaters for Bedrooms: Oil-Fi | 2026-10-13 | 8 | 8 | 0 | 未取得 | 未取得 |
| Heated Foot Massagers for Nurses: Shiats | 2026-10-11 | 8 | 0 | 0 | 未取得 | 未取得 |
| Sunrise Alarm Clocks: Hatch vs. Lumie vs | 2026-10-07 | 8 | 5 | 0 | 0 | 0.00% |
| Red-Eye Flight Recovery Kit: What to Pac | 2026-10-06 | 8 | 51 | 0 | 未取得 | 未取得 |
| Bedding for Couples When One Sleeps Hot: | 2026-10-05 | 8 | 11 | 0 | 0 | 0.00% |
| Best Noise Machines for Light Sleepers:  | 2026-09-27 | 8 | 5 | 0 | 未取得 | 未取得 |
| Best Neck Massagers for Desk Workers: Sh | 2026-09-26 | 8 | 147 | 0 | 未取得 | 未取得 |
| Blackout Curtains vs. Sleep Masks for Da | 2026-09-25 | 7 | 7 | 0 | 未取得 | 未取得 |
| Cold Plunge vs. Red Light Therapy: Which | 2026-09-19 | 3 | 10 | 未取得 | 0 | 0.00% |
| Oura Ring vs Apple Watch for Sleep: Do Y | 2026-09-19 | 3 | 14 | 未取得 | 未取得 | 未取得 |
| 2026 Recovery & Sleep Gift Guide: Picks  | 2026-09-19 | 3 | 2 | 未取得 | 未取得 | 未取得 |
| Best Cooling Pillows & Pads for Menopaus | 2026-09-12 | 9 | 16 | 1 | 0 | 0.00% |
| Red Light Therapy vs Massage Gun: Which  | 2026-09-05 | 5 | 0 | 0 | 未取得 | 未取得 |
| Best Quiet Bedroom Humidifiers for Fall  | 2026-08-29 | 7 | 9 | 0 | 未取得 | 未取得 |
| Best Home Recovery & Sleep Gifts 2026, b | 2026-08-15 | 7 | 10 | 0 | 未取得 | 未取得 |
| Massage Gun vs. Compression Boots for Po | 2026-08-08 | 4 | 0 | 0 | 未取得 | 未取得 |
| Sauna Blanket vs. Cold Plunge: Which to  | 2026-08-01 | 4 | 11 | 0 | 未取得 | 未取得 |
| Whoop vs. Oura Ring for Sleep Tracking:  | 2026-07-27 | 3 | 1 | 0 | 未取得 | 未取得 |
| refresh_magnesium-glycinate-sleep-shift- | ? | 3 | 1 | 0 | 未取得 | 未取得 |
| refresh_red-light-therapy-devices-for-ho | ? | 3 | 2 | 0 | 未取得 | 未取得 |
| refresh_sauna-blanket-vs-home-sauna | ? | 3 | 0 | 0 | 未取得 | 未取得 |
| refresh_weighted-blankets-sleep-anxiety | ? | 3 | 0 | 0 | 未取得 | 未取得 |
| refresh_2026-recovery-sleep-gift-guide-b | ? | 3 | 0 | 0 | 未取得 | 未取得 |
| refresh_best-recovery-and-sleep-gifts-20 | ? | 2 | 0 | 0 | 未取得 | 未取得 |
| refresh_cold-plunge-vs-red-light-therapy | ? | 2 | 0 | 0 | 未取得 | 未取得 |
| refresh_massage-gun-vs-compression-boots | ? | 3 | 0 | 0 | 未取得 | 未取得 |
| refresh_blackout-curtains-sleep-masks-fo | ? | 2 | 0 | 0 | 未取得 | 未取得 |
| refresh_cold-plunge-vs-sauna-blanket | ? | 2 | 0 | 0 | 未取得 | 未取得 |
| refresh_oura-ring-vs-whoop-sleep-trackin | ? | 3 | 0 | 0 | 未取得 | 未取得 |
| refresh_red-light-therapy-vs-massage-gun | ? | 3 | 0 | 0 | 未取得 | 未取得 |
| (記事不明) | ? | 9 | 190 | 未取得 | 未取得 | 未取得 |

## 集計軸

### テーマ・商品カテゴリ別

| テーマ | 投稿数 | 計測済み | 配信(imp) | ピン→サイト遷移 | リンククリック(GA4) | クリック到達率 |
|---|---:|---:|---:|---:|---|---|
| Bedroom Sleep Environment | 95 | 91 | 74 | 1 | 未取得 | 未取得 |
| Gift Guides | 10 | 10 | 12 | 0 | 未取得 | 未取得 |
| Recovery & Massage | 52 | 52 | 219 | 0 | 未取得 | 未取得 |
| Sleep Tracking & Sleep Aids | 10 | 10 | 21 | 0 | 未取得 | 未取得 |
| 未設定 | 41 | 41 | 193 | 0 | 未取得 | 未取得 |

### 投稿の型別

| チャネル / 型 | 投稿数 | 計測済み | 配信(imp) | ピン→サイト遷移 | リンククリック(GA4) | クリック到達率 |
|---|---:|---:|---:|---:|---|---|
| Pinterest / pin | 147 | 143 | 64 | 1 | 未取得 | 未取得 |
| X / thread_reply | 37 | 37 | 148 | 未取得 | 未取得 | 未取得 |
| X / thread_root | 15 | 15 | 117 | 未取得 | 未取得 | 未取得 |
| X / 不明 | 9 | 9 | 190 | 未取得 | 未取得 | 未取得 |

### 曜日・時間帯別(JST、投稿時刻)

| 曜日 時間帯 | 投稿数 | 計測済み | 配信(imp) | ピン→サイト遷移 | リンククリック(GA4) | クリック到達率 |
|---|---:|---:|---:|---:|---|---|
| 土 10時台 | 2 | 2 | 3 | 未取得 | 未取得 | 未取得 |
| 土 11時台 | 6 | 6 | 12 | 未取得 | 未取得 | 未取得 |
| 土 14時台 | 4 | 4 | 7 | 1 | 未取得 | 未取得 |
| 土 15時台 | 15 | 15 | 151 | 0 | 未取得 | 未取得 |
| 土 16時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 日 13時台 | 12 | 12 | 60 | 未取得 | 未取得 | 未取得 |
| 日 14時台 | 16 | 16 | 20 | 0 | 未取得 | 未取得 |
| 日 15時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 日 16時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 月 11時台 | 2 | 2 | 24 | 未取得 | 未取得 | 未取得 |
| 月 14時台 | 8 | 8 | 2 | 0 | 未取得 | 未取得 |
| 月 15時台 | 8 | 8 | 5 | 0 | 未取得 | 未取得 |
| 月 16時台 | 8 | 8 | 0 | 0 | 未取得 | 未取得 |
| 木 13時台 | 4 | 4 | 0 | 未取得 | 未取得 | 未取得 |
| 木 14時台 | 12 | 12 | 4 | 0 | 未取得 | 未取得 |
| 木 15時台 | 4 | 4 | 2 | 0 | 未取得 | 未取得 |
| 木 16時台 | 4 | 4 | 2 | 0 | 未取得 | 未取得 |
| 木 17時台 | 4 | 0 | 未取得 | 未取得 | 未取得 | 未取得 |
| 水 14時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 水 15時台 | 11 | 11 | 6 | 0 | 未取得 | 未取得 |
| 水 16時台 | 15 | 15 | 45 | 0 | 未取得 | 未取得 |
| 水 17時台 | 6 | 6 | 59 | 0 | 未取得 | 未取得 |
| 水 21時台 | 3 | 3 | 107 | 未取得 | 未取得 | 未取得 |
| 火 14時台 | 8 | 8 | 1 | 0 | 未取得 | 未取得 |
| 火 15時台 | 8 | 8 | 0 | 0 | 未取得 | 未取得 |
| 火 16時台 | 12 | 12 | 9 | 0 | 未取得 | 未取得 |
| 火 17時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 火 19時台 | 4 | 4 | 0 | 未取得 | 未取得 | 未取得 |
| 金 14時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 金 15時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 金 16時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |

### 流入元別

| 流入元 | 投稿数 | 計測済み | 配信(imp) | ピン→サイト遷移 | リンククリック(GA4) | クリック到達率 |
|---|---:|---:|---:|---:|---|---|
| Pinterest | 147 | 143 | 64 | 1 | 未取得 | 未取得 |
| X | 61 | 61 | 455 | 未取得 | 未取得 | 未取得 |
| 検索 | - | - | 上の「検索(Search Console)」を参照 | - | - | - |

サイトへの流入(セッション)とリンククリックは流入元を問わずGA4由来のため、現時点では比較できない。

