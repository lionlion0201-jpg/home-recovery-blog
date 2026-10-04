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
import re
import sys
from datetime import datetime, timezone

import requests

sys.path.insert(0, os.path.dirname(__file__))
from run_promotion import run as run_promotion  # noqa: E402

CYCLES_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "cycles")
POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "posts")


def article_url(manifest):
    """マニフェスト内の最初の記事URL(/posts/<slug>/)を返す。"""
    text = json.dumps(manifest, ensure_ascii=False)
    m = re.search(r'https?://[^"\s]+/posts/[^/"\s]+/', text)
    return m.group(0) if m else None


def publish_at(slug):
    """記事のフロントマターから公開予定時刻を返す。下書きなら None、判定できなければ datetime.min。"""
    path = os.path.join(POSTS_DIR, f"{slug}.md")
    if not os.path.exists(path):
        return datetime.min.replace(tzinfo=timezone.utc)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    if re.search(r"^published:\s*false", fm, re.M):
        return None
    m = re.search(r'^publishAt:\s*"?([^"\n]+)"?', fm, re.M)
    if m:
        return datetime.fromisoformat(m.group(1).strip())
    m = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", fm, re.M)
    if m:
        return datetime.fromisoformat(m.group(1) + "T09:00:00+09:00")
    return datetime.min.replace(tzinfo=timezone.utc)


def is_live(url):
    try:
        return requests.head(url, timeout=15, allow_redirects=True).status_code == 200
    except requests.RequestException:
        return False


def not_ready_reason(manifest):
    """記事がまだ読めない状態なら理由を返す。読めるなら None。

    2026-10-04: 週末レビューの承認(マニフェストのpush)と同時にツイートが流れ、
    公開日が翌日以降の3記事へのリンクが404のまま投稿された。9/25の回も同じだった。
    公開日を過ぎていて、かつ実際にページが200を返すまでは投稿しない。
    """
    url = article_url(manifest)
    if not url:
        return None
    slug = url.rstrip("/").rsplit("/", 1)[-1]
    when = publish_at(slug)
    if when is None:
        return f"{slug} は下書きのまま"
    if when > datetime.now(timezone.utc):
        return f"{slug} の公開予定は {when.isoformat()}"
    if not is_live(url):
        return f"{url} がまだ開けない(デプロイ待ち)"
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--skip-pins", action="store_true",
        help=("Post tweets only. Pin posting is owned by post_pin_backlog.py, "
              "which paces pins a few per day; letting this script post pins too "
              "would double-post them and defeat that pacing."))
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

        with open(manifest_path, encoding="utf-8") as f:
            reason = not_ready_reason(json.load(f))
        if reason:
            # .posted を付けないので、次回以降の実行で記事が読めるようになったら投稿される
            print(f"Waiting {os.path.basename(manifest_path)}: {reason}")
            continue

        print(f"Processing {os.path.basename(manifest_path)}"
              f"{' (tweets only)' if args.skip_pins else ''}...")
        report = run_promotion(manifest_path, args.dry_run, skip_pins=args.skip_pins)
        print(json.dumps(report, indent=2, ensure_ascii=False))

        if not args.dry_run:
            with open(marker_path, "w") as f:
                json.dump({"processed": True}, f)
        any_processed = True

    if not any_processed:
        print("Nothing new to process.")


if __name__ == "__main__":
    main()
