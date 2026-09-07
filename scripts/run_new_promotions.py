#!/usr/bin/env python3
"""
Wrapper for run_promotion.py: finds cycle manifests that haven't been
promoted yet, runs run_promotion.py on each, and marks them done.

Why this exists: the weekly Cowork pipeline generates docs/cycles/cycle_manifest_*.json
but cannot actually reach api.twitter.com / api.pinterest.com from its sandbox
(outbound requests are blocked there). This script is meant to run instead from
GitHub Actions, which has normal internet access, on a schedule shortly after
each weekly deploy. It commits nothing itself -- the calling workflow is
responsible for committing the *.posted marker files it creates.

Usage:
  python3 run_new_promotions.py [--dry-run]
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

    any_processed = False
    for manifest_path in manifests:
        marker_path = manifest_path + ".posted"
        if os.path.exists(marker_path):
            print(f"Skipping {os.path.basename(manifest_path)} (already posted)")
            continue

        print(f"Processing {os.path.basename(manifest_path)}...")
        report = run_promotion(manifest_path, args.dry_run)
        print(json.dumps(report, indent=2, ensure_ascii=False))

        if not args.dry_run:
            with open(marker_path, "w") as f:
                json.dump({"processed": True}, f)
        any_processed = True

    if not any_processed:
        print("Nothing new to process.")


if __name__ == "__main__":
    main()
