#!/usr/bin/env python3
"""
Post the backlog of Pinterest pins, a few at a time.

Why this exists: between 2026-07 and 2026-09 the weekly pipeline generated pin
material in docs/cycles/cycle_manifest_*.json, but every pin POST failed (the
app only had Trial access, plus a board_id bug). run_new_promotions.py writes a
`.posted` marker per manifest regardless of whether individual pins succeeded,
so all that pin material was marked done without a single pin going live.

Pinterest Standard access was granted 2026-09-17, so the backlog is postable
now. This script works at pin granularity (not manifest granularity) and keeps
its own state, so it is independent of the `.posted` markers and can safely
resume. It never touches X/Twitter.

New accounts that dump 30 pins at once risk being flagged as spam, so the
default is a small daily drip rather than one big burst.

State file: docs/cycles/.pins_posted.json
  {"posted": ["cycle_manifest_2026-07-25.json#0", ...]}

Usage:
  python3 post_pin_backlog.py [--max-pins 4] [--dry-run]
"""
import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from generate_pin_image import generate as generate_pin_image  # noqa: E402
from asset_ledger import record_safe, article_slug  # noqa: E402
from post_to_pinterest import create_pin  # noqa: E402

from dotenv import load_dotenv  # noqa: E402
load_dotenv()

CYCLES_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "cycles")
STATE_FILE = os.path.join(CYCLES_DIR, ".pins_posted.json")


def _load_state():
    if not os.path.exists(STATE_FILE):
        return set()
    try:
        with open(STATE_FILE, encoding="utf-8") as f:
            return set(json.load(f).get("posted", []))
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: could not read state file ({e}); treating as empty.", file=sys.stderr)
        return set()


def _save_state(posted):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({"posted": sorted(posted)}, f, indent=2, ensure_ascii=False)


def _iter_backlog_pins(posted):
    """Yields (key, manifest_basename, index, pin_dict) for every pin not yet posted."""
    for manifest_path in sorted(glob.glob(os.path.join(CYCLES_DIR, "cycle_manifest_*.json"))):
        basename = os.path.basename(manifest_path)
        try:
            with open(manifest_path, encoding="utf-8") as f:
                manifest = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Skipping {basename}: cannot parse ({e})", file=sys.stderr)
            continue
        for i, pin in enumerate(manifest.get("pins", [])):
            key = f"{basename}#{i}"
            if key not in posted:
                yield key, basename, i, pin


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-pins", type=int, default=4,
                        help="How many pins to post in this run (default: 4).")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    posted = _load_state()
    backlog = list(_iter_backlog_pins(posted))

    if not backlog:
        print("No pins left in the backlog. Nothing to do.")
        return

    print(f"Backlog: {len(backlog)} pin(s) not yet posted. "
          f"Posting up to {args.max_pins} this run.")

    results = []
    newly_posted = 0

    for key, basename, i, pin in backlog:
        if newly_posted >= args.max_pins:
            break

        image_path = os.path.join(CYCLES_DIR, f"_backlog_pin_{basename}_{i}.png")
        try:
            generate_pin_image(
                title=pin["title"],
                subtitle=pin.get("subtitle", ""),
                brand=pin.get("brand", "QuietRecover"),
                out_path=image_path,
                cta=pin.get("cta", "Read the full guide"),
            )
        except Exception as e:
            print(f"[{key}] image generation failed: {e}", file=sys.stderr)
            results.append({"key": key, "title": pin.get("title"), "status": "image_error", "error": str(e)})
            continue

        try:
            result = create_pin(
                title=pin["title"],
                description=pin["description"],
                link=pin["link"],
                image_path=image_path,
                board_id=pin.get("board_id"),
                dry_run=args.dry_run,
            )
            is_duplicate = isinstance(result, dict) and result.get("skipped_duplicate")
            status = "skipped_duplicate" if is_duplicate else "ok"
            results.append({"key": key, "title": pin["title"], "status": status, "result": result})

            # 発行されたピンIDを台帳に残す(Pinterest Analyticsで保存数・
            # クリック数を引くのに必要)。manifest本体は読み込み済みなので
            # ファイル名からスラッグを割り出す。
            pin_id = result.get("id") if isinstance(result, dict) else None
            record_safe(
                platform="pinterest",
                asset_id=pin_id,
                # 2026-09-12以前のマニフェストはファイル名に記事スラッグを含まないため、
                # ピン単体を渡してリンクURLから拾わせる(渡さないと article が None になる)。
                article=article_slug(os.path.join(CYCLES_DIR, basename), {"pins": [pin]}),
                content_type="pin",
                link=pin.get("link"),
                text=pin["title"],
                source=basename,
            )

            # A duplicate means Pinterest already has it -- count it as done so we
            # stop retrying it, but don't count it against the posting quota.
            if not args.dry_run:
                posted.add(key)
                _save_state(posted)
            if status == "ok":
                newly_posted += 1
        except Exception as e:
            # Leave the key out of the state file so it is retried next run.
            print(f"[{key}] pin POST failed: {e}", file=sys.stderr)
            results.append({"key": key, "title": pin.get("title"), "status": "error", "error": str(e)})

        # Clean up the generated image; it has already been uploaded as base64.
        try:
            os.remove(image_path)
        except OSError:
            pass

    print(json.dumps({"results": results}, indent=2, ensure_ascii=False))

    ok = sum(1 for r in results if r["status"] == "ok")
    dup = sum(1 for r in results if r["status"] == "skipped_duplicate")
    err = sum(1 for r in results if r["status"] in ("error", "image_error"))
    remaining = len(backlog) - ok - dup
    print(f"\nSummary: posted {ok}, duplicates {dup}, errors {err}. "
          f"Roughly {max(remaining, 0)} pin(s) still in the backlog.")


if __name__ == "__main__":
    main()
