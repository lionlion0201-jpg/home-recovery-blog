#!/usr/bin/env python3
"""
投稿済みピンの効果を取得し、docs/metrics/pin_metrics.json に追記する。

なぜ Pinterest は「表示」より「クリック」を見るのか
--------------------------------------------------
Pinterestは発見型のメディアなので、インプレッションは母数が大きく出やすい。
売上に近いのは以下の2つ:

  OUTBOUND_CLICK  ピンからリンク先(自サイト)へ遷移した数 ← 最重要
  SAVE            ユーザーが自分のボードに保存した数(後から戻ってくる意向)

PIN_CLICK はピンを拡大しただけでも数えられるので、購買意向の指標としては弱い。
設計の背景は アフィリエイト/共通/計測設計.md を参照。

トークンを2本に分けている理由(重要)
------------------------------------
GET /v5/pins/{pin_id}/analytics には **boards:read と pins:read** が要る。
一方、投稿用の `PINTEREST_ACCESS_TOKEN` は `pins:write` `boards:read`
`boards:write` で発行されており pins:read を持たない。

そこで、Developer Portal の「アクセストークンを生成する」で発行できる
読み取り専用トークン(pins:read / boards:read / user_accounts:read /
ads:read / catalogs:read)を `PINTEREST_READ_TOKEN` として別に持たせ、
計測にはそちらだけを使う。

この分け方には2つ利点がある:
  1. 毎日動いているピン投稿(pinterest-backlog.yml)のトークンに一切触らない
  2. 計測処理に書き込み権限を渡さない(最小権限)

PINTEREST_READ_TOKEN が未設定の場合は PINTEREST_ACCESS_TOKEN に
フォールバックするが、その場合は pins:read が無いので403になる。
詳細は docs/social_api_setup.md を参照。

APIの制約
---------
- start_date は今日から90日前までしか遡れない
- end_date は start_date から90日以内

Usage:
  python3 fetch_pin_metrics.py [--dry-run] [--days 30]
"""
import argparse
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone

import requests
from dotenv import load_dotenv

load_dotenv()

JST = timezone(timedelta(hours=9))
API_BASE = "https://api.pinterest.com/v5"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LEDGER_FILE = os.path.join(SCRIPT_DIR, "..", "docs", "metrics", "posted_assets.json")
METRICS_FILE = os.path.join(SCRIPT_DIR, "..", "docs", "metrics", "pin_metrics.json")

METRIC_TYPES = "IMPRESSION,OUTBOUND_CLICK,PIN_CLICK,SAVE"


def load_json(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--days", type=int, default=30,
                        help="何日分を集計対象にするか(APIの上限は90)")
    args = parser.parse_args()

    ledger = load_json(LEDGER_FILE, [])
    pins = [r for r in ledger if r.get("platform") == "pinterest" and r.get("id")]
    if not pins:
        print("台帳にピンがまだ記録されていません。"
              "docs/metrics/posted_assets.json は 2026-09-20 に導入したので、"
              "以降に投稿したピンから順次たまります。")
        return

    # 読み取り専用トークンを優先する。投稿用トークンには pins:read が無いため、
    # フォールバックした場合は403になる(その旨は403ハンドラで案内する)。
    token = os.environ.get("PINTEREST_READ_TOKEN") or os.environ.get("PINTEREST_ACCESS_TOKEN")
    using_fallback = not os.environ.get("PINTEREST_READ_TOKEN")
    if not token and not args.dry_run:
        raise SystemExit("PINTEREST_READ_TOKEN(または PINTEREST_ACCESS_TOKEN)が設定されていません")
    if using_fallback and not args.dry_run:
        print("警告: PINTEREST_READ_TOKEN が未設定のため投稿用トークンを使います。"
              "pins:read が無いため403になる見込みです。", file=sys.stderr)

    days = max(1, min(args.days, 90))
    end = date.today()
    start = end - timedelta(days=days)

    if args.dry_run:
        print(f"[DRY RUN] {len(pins)}件のピンについて "
              f"GET {API_BASE}/pins/<pin_id>/analytics を呼び出します "
              f"({start} 〜 {end}, metric_types={METRIC_TYPES})")
        return

    log = load_json(METRICS_FILE, [])
    checked_at = datetime.now(JST).isoformat()
    ok = forbidden = failed = 0

    for pin in pins:
        try:
            resp = requests.get(
                f"{API_BASE}/pins/{pin['id']}/analytics",
                headers={"Authorization": f"Bearer {token}"},
                params={
                    "start_date": start.isoformat(),
                    "end_date": end.isoformat(),
                    "metric_types": METRIC_TYPES,
                },
                timeout=30,
            )
        except requests.RequestException as e:
            print(f"[{pin['id']}] リクエスト失敗: {e}", file=sys.stderr)
            failed += 1
            continue

        if resp.status_code == 403:
            # スコープ不足がほぼ確実。1件目で分かるので、全件叩かずに止める。
            print(f"[{pin['id']}] 403 Forbidden: {resp.text[:200]}", file=sys.stderr)
            print("トークンに pins:read が含まれていない可能性が高いです。"
                  "Developer Portal の「アクセストークンを生成する」(本番環境)で発行した"
                  "読み取り専用トークンを PINTEREST_READ_TOKEN に設定してください。"
                  "詳細は docs/social_api_setup.md を参照。", file=sys.stderr)
            forbidden += 1
            break
        if resp.status_code != 200:
            print(f"[{pin['id']}] HTTP {resp.status_code}: {resp.text[:200]}", file=sys.stderr)
            failed += 1
            continue

        data = resp.json()
        # レスポンスは split_field ごとのキーを持つ辞書。NO_SPLIT の場合は
        # 単一キーなので、最初のエントリの summary_metrics を採る。
        summary = {}
        for value in data.values():
            if isinstance(value, dict) and value.get("summary_metrics"):
                summary = value["summary_metrics"]
                break

        log.append({
            "checked_at": checked_at,
            "pin_id": pin["id"],
            "article": pin.get("article"),
            "period_start": start.isoformat(),
            "period_end": end.isoformat(),
            "impression": summary.get("IMPRESSION"),
            "outbound_click": summary.get("OUTBOUND_CLICK"),
            "pin_click": summary.get("PIN_CLICK"),
            "save": summary.get("SAVE"),
        })
        ok += 1

    if ok:
        save_json(METRICS_FILE, log)
    print(f"取得成功 {ok}件 / スコープ不足で中断 {forbidden}件 / その他失敗 {failed}件")
    if forbidden:
        sys.exit(2)


if __name__ == "__main__":
    main()
