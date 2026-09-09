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


def _normalize(text):
    """Loose normalization so near-identical text (whitespace/case/truncation
    differences) still counts as the same tweet for duplicate detection."""
    return " ".join(text.split()).strip().lower()[:280]


def _recent_posted_texts(client, max_results=100):
    """Fetch the account's own recent tweet texts, so we can refuse to post
    something that's already out there. This is a safety net independent of
    the .posted marker files in docs/cycles/ -- those markers are only as
    reliable as the git commit that saves them (a push race or a mid-run
    crash can leave a manifest "unmarked" even though it already posted),
    which is exactly how the same tweets ended up posted multiple times on
    2026-08-07. Checking the account's actual timeline before posting means
    a repeat run can't duplicate content even if the marker file is wrong."""
    try:
        me = client.get_me()
        user_id = me.data.id
        resp = client.get_users_tweets(
            id=user_id,
            max_results=min(max_results, 100),
            tweet_fields=["text"],
            exclude=["retweets"],
        )
        if not resp.data:
            return set()
        return {_normalize(t.text) for t in resp.data}
    except Exception as e:
        # If we can't check (rate limit, permissions, etc.), don't block
        # posting on it -- just note that the safety net is unavailable.
        print(f"Warning: could not fetch recent tweets for duplicate check: {e}", file=sys.stderr)
        return None


def post_tweet(text, dry_run=False, in_reply_to_tweet_id=None):
    """Post a tweet. If in_reply_to_tweet_id is given, this tweet is posted
    as a reply to that tweet ID, which is how a thread is built: post the
    root tweet first (in_reply_to_tweet_id=None), then pass the returned
    tweet's id as in_reply_to_tweet_id for each following tweet in sequence."""
    max_per_run = int(os.environ.get("MAX_POSTS_PER_RUN", "6"))
    current = _posts_made_today()
    if current >= max_per_run:
        raise RuntimeError(
            f"Refusing to post: MAX_POSTS_PER_RUN ({max_per_run}) already reached today. "
            f"Resets automatically tomorrow, or edit scripts/.post_count_state to override."
        )

    if dry_run:
        print("[DRY RUN] Would post tweet:")
        if in_reply_to_tweet_id:
            print(f"  (as reply to tweet id {in_reply_to_tweet_id})")
        print(" ", text)
        # Fake id so a dry-run can still simulate chaining downstream.
        return {"dry_run": True, "id": f"dryrun-{abs(hash(text)) % 100000}"}

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

    recent = _recent_posted_texts(client)
    if recent is not None and _normalize(text) in recent:
        print(f"Skipping duplicate tweet (already on the timeline): {text[:60]}...")
        return {"skipped_duplicate": True, "id": None}

    kwargs = {"text": text[:280]}
    if in_reply_to_tweet_id:
        kwargs["in_reply_to_tweet_id"] = in_reply_to_tweet_id
    resp = client.create_tweet(**kwargs)
    _record_post()
    return resp.data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--in-reply-to", default=None, help="Tweet ID to post this as a reply to (for threads)")
    args = parser.parse_args()

    try:
        result = post_tweet(args.text, args.dry_run, in_reply_to_tweet_id=args.in_reply_to)
        print(result)
    except tweepy.TweepyException as e:
        print(f"X API error: {e}", file=sys.stderr)
        sys.exit(1)
