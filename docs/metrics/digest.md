# ファネル表(US)

生成日: 2026-11-03 / 生成: `scripts/build_digest.py`(手で編集しない)

読み方は `docs/agents/analyst.md` の「読み方のルール」に従う。**インプレッションは売上の指標ではない。**判断の主軸はアフィリエイトリンクのクリック(GA4 `affiliate_click`)。

## データの状態

| ソース | レコード数 | 対象投稿数 | 最終取得 |
|---|---:|---:|---|
| docs/metrics/posted_assets.json(投稿台帳) | 147 | 147 | - |
| docs/metrics/x_metrics.json(Xメトリクス) | 568 | 61 | 2026-11-03 07:13 |
| docs/metrics/pin_metrics.json(ピンメトリクス) | 2209 | 91 | 2026-11-03 07:13 |
| GA4 `affiliate_click` | あり | - | - |
| Search Console | 25 | - | 2026-10-31 まで |


## X投稿の型の比較(hook / cta など)

| 型 | 比較対象の投稿数 | うち計測済み | 目安 | 判定 |
|---|---:|---:|---:|---|
| thread_reply | 37 | 37 | 20 | 判断可(ただしクリック未取得なら保留) |
| thread_root | 15 | 15 | 20 | **データ不足**(従来方針を維持) |
| 不明 | 9 | 9 | 20 | 比較対象外(型が記録されていない) |

リンククリック(GA4)が取れていない間は、計測済み件数が目安に達しても型の優劣は結論しない(インプレッション単体で型を評価しない)。

## 検索(Search Console)

期間: 2026-10-03〜2026-10-31(Search Console は2〜3日遅れて確定する)/ 表示 452回 / クリック 0回
検索結果に載っている記事: 23 / 30(サイトマップの記事URLを URL 検査 API で確認)

表示が少ない記事の順位は日々大きく動く。表示100回未満の記事どうしの比較は「データ不足」とする。

| 記事 | 公開日 | 掲載 | 表示 | クリック | クリック率 | 平均順位 | 表示の多い検索語(順位) |
|---|---|---|---:|---:|---:|---:|---|
| Best Noise Machines for Light Sleepers:  | 2026-09-27 | ○ | 93 | 0 | 0.00% | 16.7 | noise machine for light sleepe(8.1) |
| Best Cooling Pillows & Pads for Menopaus | 2026-09-12 | ○ | 66 | 0 | 0.00% | 37.8 | most effective cooling pads fo(6.9) |
| Bedding for Couples When One Sleeps Hot: | 2026-10-05 | ○ | 60 | 0 | 0.00% | 39.7 | what bedding keeps both partne(57) |
| Blackout Curtains vs. Sleep Masks for Da | 2026-09-25 | ○ | 49 | 0 | 0.00% | 8.1 | - |
| Do Weighted Blankets Actually Help With  | 2026-07-25 | ○ | 30 | 0 | 0.00% | 65.5 | anxiety and weighted blanket(63.7) |
| Red Light Therapy vs Massage Gun: Which  | 2026-09-05 | ○ | 29 | 0 | 0.00% | 6.7 | laser pointer vs massage gun(10) |
| Shiatsu Back Massager for Office Chairs: | 2026-10-22 | ○ | 24 | 0 | 0.00% | 33.1 | back massagers for first respo(29.8) |
| 2026 Recovery & Sleep Gift Guide: Picks  | 2026-09-19 | ○ | 14 | 0 | 0.00% | 6.5 | - |
| Massage Gun vs. Compression Boots for Po | 2026-08-08 | ○ | 13 | 0 | 0.00% | 18.7 | massage gun boots(76.5) |
| Whoop vs. Oura Ring for Sleep Tracking:  | 2026-07-27 | ○ | 13 | 0 | 0.00% | 35.9 | whoop versus oura ring(6.5) |
| Oura Ring vs Apple Watch for Sleep: Do Y | 2026-09-19 | ○ | 12 | 0 | 0.00% | 68.1 | oura ring vs apple watch(86.8) |
| Best Neck Massagers for Desk Workers: Sh | 2026-09-26 | ○ | 10 | 0 | 0.00% | 20.2 | best neck massagers for cowork(93) |
| Sunrise Alarm Clocks: Hatch vs. Lumie vs | 2026-10-07 | ○ | 9 | 0 | 0.00% | 48.2 | sunrise alarm vs regular alarm(78.5) |
| Best Home Recovery & Sleep Gifts 2026, b | 2026-08-15 | ○ | 7 | 0 | 0.00% | 7 | - |
| Magnesium Glycinate for Sleep: Shift Wor | 2026-07-25 | ○ | 7 | 0 | 0.00% | 9.6 | - |
| Sauna Blanket vs. Cold Plunge: Which to  | 2026-08-01 | ○ | 5 | 0 | 0.00% | 54 | sauna vs cold plunge(82.3) |
| Infrared Sauna Blanket vs. Home Sauna fo | 2026-07-25 | ○ | 3 | 0 | 0.00% | 43 | sauna blanket vs sauna(30) |
| Best Bedding for Couples With Different  | 2026-10-18 | ○ | 1 | 0 | 0.00% | 10 | - |
| Best Quiet Bedroom Humidifiers for Fall  | 2026-08-29 | ○ | 1 | 0 | 0.00% | 5 | - |
| Cold Plunge vs. Red Light Therapy: Which | 2026-09-19 | ○ | 1 | 0 | 0.00% | 1 | - |
| Red-Eye Flight Recovery Kit: What to Pac | 2026-10-06 | ○ | 1 | 0 | 0.00% | 12 | - |
| Back Massager for First Responders: 3 Af | 2026-11-02 | × | 0 | 0 | 未取得 | - | - |
| Cooling Mattress Pad for Hot Flashes: 3  | 2026-10-26 | × | 0 | 0 | 未取得 | - | - |
| Heated Foot Massagers for Nurses: Shiats | 2026-10-11 | × | 0 | 0 | 未取得 | - | - |
| Blackout Curtains for Renters, No Drill: | 2026-10-28 | × | 0 | 0 | 未取得 | - | - |
| White Noise Machine for Athletes: 3 Port | 2026-10-20 | ○ | 0 | 0 | 未取得 | - | - |
| Quiet Space Heaters for Bedrooms: Oil-Fi | 2026-10-13 | × | 0 | 0 | 未取得 | - | - |
| Best Red Light Therapy Devices for Home: | 2026-07-25 | × | 0 | 0 | 未取得 | - | - |
| Sleep Earbuds vs. Earplugs for a Snoring | 2026-10-15 | ○ | 0 | 0 | 未取得 | - | - |
| What to Buy on Sale for Recovery and Sle | 2026-10-30 | × | 0 | 0 | 未取得 | - | - |

**伸ばす候補**(平均8〜30位・表示10回以上。1ページ目の下〜2ページ目にいて、タイトル・説明文・内部リンク・内容の補強で上位を狙える): `blackout-curtains-sleep-masks-for-day-sleepers`(8.1位)、`white-noise-machines-vs-sound-machines-light-sleepers`(16.7位)、`massage-gun-vs-compression-boots-recovery`(18.7位)、`shiatsu-neck-shoulder-massager-desk-tension`(20.2位)

**検索結果に未掲載**: `back-massager-for-first-responders-after-shift`、`cooling-mattress-pad-for-hot-flashes`、`heated-foot-massagers-nurses-standing-workers`、`no-drill-blackout-for-renters`、`quiet-space-heaters-bedroom-light-sleepers`、`red-light-therapy-devices-for-home`、`what-to-buy-on-sale-recovery-sleep`(Search Console の URL 検査からインデックス登録をリクエストできる)

## 記事単位のファネル

記事の比較はセッション100以上が目安。セッションもGA4由来のため現時点では未取得。

| 記事 | 公開日 | 投稿数 | 配信(imp) | ピン→サイト遷移 | リンククリック | クリック到達率 |
|---|---|---:|---:|---:|---|---|
| Back Massager for First Responders: 3 Af | 2026-11-02 | 4 | 未取得 | 未取得 | 未取得 | 未取得 |
| What to Buy on Sale for Recovery and Sle | 2026-10-30 | 4 | 0 | 0 | 未取得 | 未取得 |
| Blackout Curtains for Renters, No Drill: | 2026-10-28 | 4 | 0 | 0 | 未取得 | 未取得 |
| Cooling Mattress Pad for Hot Flashes: 3  | 2026-10-26 | 4 | 0 | 0 | 未取得 | 未取得 |
| Shiatsu Back Massager for Office Chairs: | 2026-10-22 | 4 | 0 | 0 | 未取得 | 未取得 |
| White Noise Machine for Athletes: 3 Port | 2026-10-20 | 4 | 1 | 0 | 未取得 | 未取得 |
| Best Bedding for Couples With Different  | 2026-10-18 | 4 | 6 | 0 | 未取得 | 未取得 |
| Sleep Earbuds vs. Earplugs for a Snoring | 2026-10-15 | 8 | 12 | 0 | 0 | 0.00% |
| Quiet Space Heaters for Bedrooms: Oil-Fi | 2026-10-13 | 8 | 15 | 0 | 未取得 | 未取得 |
| Heated Foot Massagers for Nurses: Shiats | 2026-10-11 | 8 | 0 | 0 | 未取得 | 未取得 |
| Sunrise Alarm Clocks: Hatch vs. Lumie vs | 2026-10-07 | 8 | 14 | 0 | 未取得 | 未取得 |
| Red-Eye Flight Recovery Kit: What to Pac | 2026-10-06 | 8 | 59 | 0 | 未取得 | 未取得 |
| Bedding for Couples When One Sleeps Hot: | 2026-10-05 | 8 | 19 | 0 | 0 | 0.00% |
| Best Noise Machines for Light Sleepers:  | 2026-09-27 | 8 | 14 | 0 | 未取得 | 未取得 |
| Best Neck Massagers for Desk Workers: Sh | 2026-09-26 | 8 | 147 | 0 | 未取得 | 未取得 |
| Blackout Curtains vs. Sleep Masks for Da | 2026-09-25 | 7 | 17 | 0 | 未取得 | 未取得 |
| Cold Plunge vs. Red Light Therapy: Which | 2026-09-19 | 3 | 10 | 未取得 | 未取得 | 未取得 |
| Oura Ring vs Apple Watch for Sleep: Do Y | 2026-09-19 | 3 | 14 | 未取得 | 未取得 | 未取得 |
| 2026 Recovery & Sleep Gift Guide: Picks  | 2026-09-19 | 3 | 2 | 未取得 | 未取得 | 未取得 |
| Best Cooling Pillows & Pads for Menopaus | 2026-09-12 | 9 | 29 | 1 | 0 | 0.00% |
| Red Light Therapy vs Massage Gun: Which  | 2026-09-05 | 5 | 4 | 0 | 未取得 | 未取得 |
| Best Quiet Bedroom Humidifiers for Fall  | 2026-08-29 | 7 | 9 | 0 | 未取得 | 未取得 |
| Best Home Recovery & Sleep Gifts 2026, b | 2026-08-15 | 7 | 11 | 0 | 未取得 | 未取得 |
| Massage Gun vs. Compression Boots for Po | 2026-08-08 | 4 | 2 | 0 | 未取得 | 未取得 |
| Sauna Blanket vs. Cold Plunge: Which to  | 2026-08-01 | 4 | 13 | 0 | 未取得 | 未取得 |
| Whoop vs. Oura Ring for Sleep Tracking:  | 2026-07-27 | 3 | 2 | 0 | 未取得 | 未取得 |
| (記事不明) | ? | 9 | 190 | 未取得 | 未取得 | 未取得 |

## 集計軸

### テーマ・商品カテゴリ別

| テーマ | 投稿数 | 計測済み | 配信(imp) | ピン→サイト遷移 | リンククリック(GA4) | クリック到達率 |
|---|---:|---:|---:|---:|---|---|
| Bedroom Sleep Environment | 83 | 83 | 136 | 1 | 未取得 | 未取得 |
| Gift Guides | 10 | 10 | 13 | 0 | 未取得 | 未取得 |
| Recovery & Massage | 48 | 44 | 235 | 0 | 未取得 | 未取得 |
| Sleep Tracking & Sleep Aids | 6 | 6 | 16 | 0 | 未取得 | 未取得 |
| 未設定 | 9 | 9 | 190 | 未取得 | 未取得 | 未取得 |

### 投稿の型別

| チャネル / 型 | 投稿数 | 計測済み | 配信(imp) | ピン→サイト遷移 | リンククリック(GA4) | クリック到達率 |
|---|---:|---:|---:|---:|---|---|
| Pinterest / pin | 95 | 91 | 135 | 1 | 未取得 | 未取得 |
| X / thread_reply | 37 | 37 | 148 | 未取得 | 未取得 | 未取得 |
| X / thread_root | 15 | 15 | 117 | 未取得 | 未取得 | 未取得 |
| X / 不明 | 9 | 9 | 190 | 未取得 | 未取得 | 未取得 |

### 曜日・時間帯別(JST、投稿時刻)

| 曜日 時間帯 | 投稿数 | 計測済み | 配信(imp) | ピン→サイト遷移 | リンククリック(GA4) | クリック到達率 |
|---|---:|---:|---:|---:|---|---|
| 土 10時台 | 2 | 2 | 3 | 未取得 | 未取得 | 未取得 |
| 土 11時台 | 6 | 6 | 12 | 未取得 | 未取得 | 未取得 |
| 土 14時台 | 4 | 4 | 18 | 1 | 未取得 | 未取得 |
| 土 15時台 | 11 | 11 | 151 | 未取得 | 未取得 | 未取得 |
| 日 13時台 | 12 | 12 | 60 | 未取得 | 未取得 | 未取得 |
| 日 14時台 | 16 | 16 | 31 | 0 | 未取得 | 未取得 |
| 日 15時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 月 11時台 | 2 | 2 | 24 | 未取得 | 未取得 | 未取得 |
| 月 14時台 | 8 | 8 | 2 | 0 | 未取得 | 未取得 |
| 月 15時台 | 8 | 4 | 11 | 0 | 未取得 | 未取得 |
| 木 13時台 | 4 | 4 | 0 | 未取得 | 未取得 | 未取得 |
| 木 14時台 | 12 | 12 | 12 | 0 | 未取得 | 未取得 |
| 木 15時台 | 4 | 4 | 11 | 0 | 未取得 | 未取得 |
| 水 14時台 | 4 | 4 | 1 | 0 | 未取得 | 未取得 |
| 水 15時台 | 11 | 11 | 20 | 0 | 未取得 | 未取得 |
| 水 16時台 | 9 | 9 | 39 | 未取得 | 未取得 | 未取得 |
| 水 17時台 | 4 | 4 | 59 | 未取得 | 未取得 | 未取得 |
| 水 21時台 | 3 | 3 | 107 | 未取得 | 未取得 | 未取得 |
| 火 14時台 | 8 | 8 | 3 | 0 | 未取得 | 未取得 |
| 火 15時台 | 8 | 8 | 11 | 0 | 未取得 | 未取得 |
| 火 16時台 | 4 | 4 | 15 | 0 | 未取得 | 未取得 |
| 火 19時台 | 4 | 4 | 0 | 未取得 | 未取得 | 未取得 |
| 金 14時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |
| 金 15時台 | 4 | 4 | 0 | 0 | 未取得 | 未取得 |

### 流入元別

| 流入元 | 投稿数 | 計測済み | 配信(imp) | ピン→サイト遷移 | リンククリック(GA4) | クリック到達率 |
|---|---:|---:|---:|---:|---|---|
| Pinterest | 95 | 91 | 135 | 1 | 未取得 | 未取得 |
| X | 61 | 61 | 455 | 未取得 | 未取得 | 未取得 |
| 検索 | - | - | 上の「検索(Search Console)」を参照 | - | - | - |

サイトへの流入(セッション)とリンククリックは流入元を問わずGA4由来のため、現時点では比較できない。

