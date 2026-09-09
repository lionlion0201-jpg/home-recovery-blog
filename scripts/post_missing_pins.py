#!/usr/bin/env python3
"""
Catch-up script: post the Pinterest pins for every cycle manifest, regardless
of whether docs/cycles/*.posted already exists.

Why this exists: the six manifests processed so far (2026-07-25 through
2026-09-05) were all marked "posted" by run_new_promotions.py before
PINTEREST_ACCESS_TOKEN was ever set in GitHub Secrets, so every one of their
pins was silently skipped with status "skipped_no_credentials" -- no pin has
actually gone out. The .posted marker means "don't re-run this manifest
automatically," which is now wrong for Pinterest specifically (it's still
right for X, since those tweets already posted for several of these
manifests). So this script:

  - Ignores the .posted marker files entirely (by design -- this is the one
    approved exception to that skip logic).
  - Only touches pins (--pins-only under the hood). Tweets are never posted
    by this script, so there is no risk of re-sending/duplicating any X
    content that already went out for these manifests.
  - Still benefits from the duplicate-pin safety net added to
    post_to_pinterest.py (checks the board's existing pins by title before
    creating one), so re-running this script after a partial success is
    safe.

Usage:
  python3 post_missing_pins.py [--dry-run]

Requires PINTEREST_ACCESS_TOKEN (Standard access, not Trial -- Trial access
cannot create Pins in production) and PINTEREST_DEFAULT_BOARD_ID in .env.
"""
import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from run_promotion import run as run_promotion  # noqa: E402

CYCLES_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "cycles")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    manifests = sorted(glob.glob(os.path.join(CYCLES_DIR, "cycle_manifest_*.json")))
    if not manifests:
        print("No cycle manifests found.")
        return

    all_reports = {}
    for manifest_path in manifests:
        name = os.path.basename(manifest_path)
        print(f"\n=== {name} (pins only, tweets skipped) ===")
        report = run_promotion(manifest_path, args.dry_run, skip_tweets=True)
        all_reports[name] = report["pins"]
        for pin in report["pins"]:
            print(f"  [{pin['status']}] {pin['title']}")

    print("\n=== Summary ===")
    print(json.dumps(all_reports, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
