#!/usr/bin/env python3
"""
Post a tweet to X via API v2 (OAuth 1.0a user context) using tweepy.

Note: X API has no free tier as of 2026 -- pay-per-usage
($0.015/post, $0.20/post if it contains a link). This script enforces
MAX_POSTS_PER_RUN from .env as a simple cost-control safety limit.

Usage:
  python3 post_to_twitter.py --text "Does a weighted blanket actually help with sleep? ..." [--dry-run]
"""
import argparse
import os
import sys
from datetime import date
import tweepy
from dotenv import load_dotenv

load_dotenv()

STATE_FILE = os.path.join(os.path.dirname(__file__), ".post_count_state")


def _posts_made_today():
    """Returns today's post count. State file format is "YYYY-MM-DD:count";
    if the stored date isn't today, the count is treated as 0 (daily reset).
    This fixes a bug where the counter previously persisted forever across
    runs (via git commit), permanently blocking all future posts once the
    cap was reached a single time."""
    if not os.path.exists(STATE_FILE):
        return 0
    with open(STATE_FILE) as f:
        raw = f.read().strip()
    if not raw:
        return 0
    if ":" in raw:
        stored_date, count = raw.split(":", 1)
        if stored_date != str(date.today()):
            return 0
        return int(count or 0)
    # Legacy format (no date prefix) -- treat as stale, reset to 0.
    return 0


def _record_post():
    count = _posts_made_today() + 1
    with open(STATE_FILE, "w") as f:
        f.write(f"{date.today()}:{count}")
    return count


def post_tweet(text, dry_run=False):
    max_per_run = int(os.environ.get("MAX_POSTS_PER_RUN", "6"))
    current = _posts_made_today()
    if current >= max_per_run:
        raise RuntimeError(
            f"Refusing to post: MAX_POSTS_PER_RUN ({max_per_run}) already reached today. "
            f"Resets automatically tomorrow, or edit scripts/.post_count_state to override."
        )

    if dry_run:
        print("[DRY RUN] Would post tweet:")
        print(" ", text)
        return {"dry_run": True}

    api_key = os.environ.get("X_API_KEY")
    api_secret = os.environ.get("X_API_SECRET")
    access_token = os.environ.get("X_ACCESS_TOKEN")
    access_secret = os.environ.get("X_ACCESS_TOKEN_SECRET")
    if not all([api_key, api_secret, access_token, access_secret]):
        raise RuntimeError("X API credentials missing in .env (X_API_KEY / X_API_SECRET / X_ACCESS_TOKEN / X_ACCESS_TOKEN_SECRET)")

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret,
    )
    resp = client.create_tweet(text=text[:280])
    _record_post()
    return resp.data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    try:
        result = post_tweet(args.text, args.dry_run)
        print(result)
    except tweepy.TweepyException as e:
        print(f"X API error: {e}", file=sys.stderr)
        sys.exit(1)
