#!/usr/bin/env python3
"""
Orchestrator: reads a cycle's promotion manifest (JSON) and posts pins to
Pinterest + posts to X. Falls back to a clear "credentials missing, here is
what would have been posted" report instead of crashing, so the weekly
scheduled pipeline can still complete and hand a usable summary to the user
even before API keys are configured.

Manifest format (see manifest.example.json):
{
  "pins": [
    {"title": "...", "description": "...", "link": "...", "board_id": "optional"}
  ],
  "tweets": [
    {"text": "..."}
  ]
}

The "tweets" list is posted as a single thread, in order: the first tweet
is the root post, and each following tweet is posted as a reply to the one
before it (so the whole list reads as one connected thread rather than
several separate, unrelated posts). If an earlier tweet in the list fails
to post, the next one is still attempted as a reply to the last
successfully-posted tweet, so one failure doesn't break the rest of the
thread.

Usage:
  python3 run_promotion.py --manifest cycle_manifest.json [--dry-run]
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from generate_pin_image import generate as generate_pin_image  # noqa: E402
from post_to_pinterest import create_pin  # noqa: E402
from post_to_twitter import post_tweet  # noqa: E402

from dotenv import load_dotenv
load_dotenv()


def has_pinterest_creds():
    return bool(os.environ.get("PINTEREST_ACCESS_TOKEN"))


def has_x_creds():
    return all(
        os.environ.get(k)
        for k in ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    )


def run(manifest_path, dry_run):
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    report = {"pins": [], "tweets": []}

    pinterest_ready = has_pinterest_creds()
    x_ready = has_x_creds()

    for i, pin in enumerate(manifest.get("pins", [])):
        image_path = os.path.join(
            os.path.dirname(manifest_path), f"_generated_pin_{i}.png"
        )
        generate_pin_image(
            title=pin["title"],
            subtitle=pin.get("subtitle", ""),
            brand=pin.get("brand", "QuietRecover"),
            out_path=image_path,
            cta=pin.get("cta", "Read the full guide"),
        )
        if pinterest_ready or dry_run:
            try:
                result = create_pin(
                    title=pin["title"],
                    description=pin["description"],
                    link=pin["link"],
                    image_path=image_path,
                    board_id=pin.get("board_id"),
                    dry_run=dry_run or not pinterest_ready,
                )
                report["pins"].append({"title": pin["title"], "status": "ok", "result": result})
            except Exception as e:
                report["pins"].append({"title": pin["title"], "status": "error", "error": str(e)})
        else:
            report["pins"].append({
                "title": pin["title"],
                "status": "skipped_no_credentials",
                "note": "Pinterest credentials not set in .env -- image generated but not posted. See docs/social_api_setup.md",
                "image_path": image_path,
            })

    # Tweets are posted as one thread: each tweet replies to the previous
    # one, starting from the root (no reply target) for the first tweet.
    previous_tweet_id = None
    for tweet in manifest.get("tweets", []):
        if x_ready or dry_run:
            try:
                result = post_tweet(
                    tweet["text"],
                    dry_run=dry_run or not x_ready,
                    in_reply_to_tweet_id=previous_tweet_id,
                )
                report["tweets"].append({
                    "text": tweet["text"],
                    "status": "ok",
                    "result": result,
                    "in_reply_to": previous_tweet_id,
                })
                new_id = result.get("id") if isinstance(result, dict) else getattr(result, "id", None)
                if new_id:
                    previous_tweet_id = new_id
            except Exception as e:
                # Keep previous_tweet_id as-is so the next tweet still
                # attaches to the last tweet that actually posted, instead
                # of breaking the thread chain because of one failure.
                report["tweets"].append({"text": tweet["text"], "status": "error", "error": str(e)})
        else:
            report["tweets"].append({
                "text": tweet["text"],
                "status": "skipped_no_credentials",
                "note": "X credentials not set in .env. See docs/social_api_setup.md",
            })

    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    report = run(args.manifest, args.dry_run)
    print(json.dumps(report, indent=2, ensure_ascii=False))
