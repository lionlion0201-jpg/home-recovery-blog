#!/usr/bin/env python3
"""
One-time catch-up: re-run every cycle manifest (pins + tweets), ignoring the
docs/cycles/*.posted marker files, relying entirely on the content-based
duplicate checks in post_to_pinterest.py / post_to_twitter.py to make this
safe to run even for manifests that already partially or fully posted.

Why this exists (2026-09-08 status):
  - Pinterest: none of the 6 manifests so far have ever actually posted a pin
    (PINTEREST_ACCESS_TOKEN wasn't set when they were marked "posted"). This
    re-attempts all of them. Note Pinterest Trial access cannot create Pins
    in production -- until Standard access is approved, these will report
    status "error" with a 403, which is expected and harmless (nothing is
    created, nothing is charged).
  - X: two manifests (2026-08-08, 2026-08-15) partially posted using the old
    non-threaded format before the reply-chain feature existed, so a few of
    their tweets are missing. Two others (2026-08-29, 2026-09-05) never
    posted to X at all. Two more (2026-07-25, 2026-08-01) already posted in
    full -- in fact were accidentally posted 3x each back on 2026-08-07 due
    to a since-fixed marker-commit race, so this run must NOT repeat them.
    The duplicate-tweet check (by exact text match against the account's
    recent timeline) is what makes it safe to include them in this same
    batch run rather than hand-picking which manifests to touch.

After this runs successfully, .posted markers are (re)written for every
manifest, so the normal weekly run_new_promotions.py goes back to skipping
them as usual.

Usage:
  python3 catchup_all_manifests.py [--dry-run]
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
        print(f"\n=== {name} ===")
        report = run_promotion(manifest_path, args.dry_run)
        all_reports[name] = report
        for pin in report["pins"]:
            print(f"  [pin:{pin['status']}] {pin['title']}")
        for tweet in report["tweets"]:
            print(f"  [tweet:{tweet['status']}] {tweet['text'][:60]}...")

        if not args.dry_run:
            marker_path = manifest_path + ".posted"
            with open(marker_path, "w") as f:
                json.dump({"processed": True, "via": "catchup_all_manifests.py"}, f)

    print("\n=== Full report ===")
    print(json.dumps(all_reports, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
