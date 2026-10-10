#!/usr/bin/env python3
"""
投稿済みツイートのインプレッション・エンゲージメントを取得し、
docs/metrics/x_metrics.json に追記する。

なぜ必要か
----------
配信の指標(インプレッション)だけでは売上の判断はできないが、
「そもそも配信されていないのか、配信はされているが刺さっていないのか」を
切り分けるには要る。判断の主軸はあくまで GA4 の affiliate_click。
設計の背景は アフィリエイト/共通/計測設計.md を参照。

コストの抑え方(JP側の同名スクリプトと同じ方針)
------------------------------------------------
- 任意のIDを指定する GET /2/tweets は $0.005/件
- 自分の投稿一覧 GET /2/users/{id}/tweets は "Owned Reads" 扱いで $0.001/件
後者だけを使う。ユーザーIDは環境変数 X_USER_ID があればそれを使い、
無ければ一度だけ GET /2/users/me を呼んでローカルにキャッシュする。

台帳の穴埋めについて
--------------------
docs/metrics/posted_assets.json は 2026-09-20 に導入したので、それ以前に
投稿したツイートのIDは記録されていない。このスクリプトは取得した自分の
ツイート本文を docs/cycles/ のマニフェストと突き合わせ、一致したものを
台帳に遡って登録する(--no-backfill で無効化できる)。

JP サイトと同じ X アカウントを使っていることについて
------------------------------------------------------
自分の投稿一覧には JP(シニアペット)の日本語ツイートも混ざって返ってくる。
2026-10-10 の点検で、記事・型が「不明」だった72件のうち55件が JP の投稿だった
(JP 側は自分の docs/engagement_log.json に記録している)。US の数字に混ぜると
インプレッションの合計も型の比較も歪むので、日本語を含むツイートは記録しない。

Usage:
  python3 fetch_tweet_metrics.py [--dry-run] [--max-results 50] [--no-backfill]
"""
import argparse
import glob
import html
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone

import tweepy
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from asset_ledger import record_safe, article_slug  # noqa: E402

load_dotenv()

JST = timezone(timedelta(hours=9))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_ID_CACHE = os.path.join(SCRIPT_DIR, ".x_user_id_cache")
LEDGER_FILE = os.path.join(SCRIPT_DIR, "..", "docs", "metrics", "posted_assets.json")
METRICS_FILE = os.path.join(SCRIPT_DIR, "..", "docs", "metrics", "x_metrics.json")
CYCLES_DIR = os.path.join(SCRIPT_DIR, "..", "docs", "cycles")


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


def get_client():
    keys = ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    vals = [os.environ.get(k) for k in keys]
    if not all(vals):
        raise SystemExit(f"X API credentials missing ({', '.join(keys)})")
    return tweepy.Client(
        consumer_key=vals[0],
        consumer_secret=vals[1],
        access_token=vals[2],
        access_token_secret=vals[3],
    )


def get_own_user_id(client, dry_run=False):
    env_id = os.environ.get("X_USER_ID", "").strip()
    if env_id:
        return env_id
    if os.path.exists(USER_ID_CACHE):
        with open(USER_ID_CACHE) as f:
            cached = f.read().strip()
            if cached:
                return cached
    if dry_run:
        print("[DRY RUN] Would call GET /2/users/me (one-time ~$0.01)")
        return "DRY_RUN_USER_ID"
    # user_auth=True が無いと tweepy はベアラートークンで認証しようとする。
    # ベアラートークンは渡していないので 401 Unauthorized になる(2026-09-20〜30 の全失敗の原因)。
    user_id = str(client.get_me(user_auth=True).data.id)
    with open(USER_ID_CACHE, "w") as f:
        f.write(user_id)
    return user_id


_JAPANESE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")


def is_other_site(text):
    """JP サイトの投稿か(ひらがな・カタカナ・漢字を含むか)。US の投稿は英語のみ。"""
    return bool(_JAPANESE.search(text or ""))


def normalize(text):
    """本文の突き合わせ用に表記ゆれを消す。

    X の API が返す本文は、URL が t.co の短縮URLに置き換わり、& などが
    HTMLエスケープされている。マニフェストの原文とそのまま比べると、リンク付きの
    CTA投稿や & を含む投稿が一致せず「記事不明」になっていた。
    """
    text = html.unescape(text or "")
    text = re.sub(r"https?://\S+", "<url>", text)
    return " ".join(text.split()).lower()


def manifest_index():
    """マニフェストのツイート本文(正規化済み) -> (記事スラッグ, マニフェスト名, 型) の対応表。

    台帳導入前に投稿したツイートを、本文の一致で記事に紐づけ直すために使う。
    型は run_promotion.py と同じく、スレッドの1件目を thread_root、それ以降を thread_reply とする。
    """
    index = {}
    for path in sorted(glob.glob(os.path.join(CYCLES_DIR, "cycle_manifest_*.json"))):
        try:
            with open(path, encoding="utf-8") as f:
                manifest = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        slug = article_slug(path, manifest)
        for i, tweet in enumerate(manifest.get("tweets", [])):
            text = normalize(tweet.get("text"))
            if text:
                index[text] = (slug, os.path.basename(path),
                               "thread_root" if i == 0 else "thread_reply")
    return index


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-results", type=int, default=50,
                        help="直近何件の自分のツイートを対象にするか(5〜100)")
    parser.add_argument("--no-backfill", action="store_true",
                        help="台帳に無いツイートをマニフェストと突き合わせて登録する処理を行わない")
    args = parser.parse_args()

    ledger = load_json(LEDGER_FILE, [])
    known = {str(r["id"]): r for r in ledger if r.get("platform") == "x"}

    client = get_client()
    user_id = get_own_user_id(client, dry_run=args.dry_run)

    if args.dry_run:
        print(f"[DRY RUN] Would call GET /2/users/{user_id}/tweets "
              f"(Owned Reads, $0.001/post), max_results={args.max_results}")
        print(f"[DRY RUN] Ledger currently knows {len(known)} X post(s).")
        return

    try:
        resp = client.get_users_tweets(
            id=user_id,
            max_results=max(5, min(args.max_results, 100)),
            tweet_fields=["public_metrics", "created_at"],
            user_auth=True,  # get_own_user_id と同じ理由
        )
    except tweepy.TweepyException as e:
        print(f"X API error: {e}", file=sys.stderr)
        print("残高不足の可能性があります。https://console.x.com を確認してください。", file=sys.stderr)
        sys.exit(1)

    if not resp.data:
        print("No tweets returned for this account.")
        return

    by_text = {} if args.no_backfill else manifest_index()
    log = load_json(METRICS_FILE, [])
    checked_at = datetime.now(JST).isoformat()
    logged = backfilled = skipped = 0

    for tweet in resp.data:
        tid = str(tweet.id)
        entry = known.get(tid)

        if entry is None and is_other_site(tweet.text):
            skipped += 1
            continue

        if entry is None and by_text:
            # 台帳導入前の投稿。本文が一致するマニフェストがあれば記事に紐づけ直す。
            hit = by_text.get(normalize(tweet.text))
            if hit:
                slug, source, ctype = hit
                if record_safe(platform="x", asset_id=tid, article=slug,
                               content_type=ctype, text=tweet.text, source=source):
                    backfilled += 1
                entry = {"article": slug, "type": ctype}

        m = tweet.public_metrics or {}
        log.append({
            "checked_at": checked_at,
            "tweet_id": tid,
            "article": (entry or {}).get("article"),
            "type": (entry or {}).get("type"),
            "created_at": tweet.created_at.isoformat() if tweet.created_at else None,
            "impression_count": m.get("impression_count"),
            "like_count": m.get("like_count"),
            "retweet_count": m.get("retweet_count"),
            "reply_count": m.get("reply_count"),
            "quote_count": m.get("quote_count"),
        })
        logged += 1

    save_json(METRICS_FILE, log)
    print(f"Logged metrics for {logged} tweet(s) to {os.path.basename(METRICS_FILE)}. "
          f"Backfilled {backfilled} ledger entry(ies). "
          f"Skipped {skipped} JP-site tweet(s).")


if __name__ == "__main__":
    main()
