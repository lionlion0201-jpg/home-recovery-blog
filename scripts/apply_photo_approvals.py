#!/usr/bin/env python3
"""
Move human-approved candidate photos into the pin background pool.

Reads assets/pin-candidates/approved.json (exported from photo_review.html),
copies those files into assets/pin-backgrounds/, and records attribution in
assets/pin-backgrounds/credits.json.

Pexels does not require attribution, but keeping the photographer and source URL
makes it straightforward to show provenance if the licensing of a pin is ever
questioned.

  python3 apply_photo_approvals.py
"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CANDIDATES_DIR = os.path.join(HERE, "..", "assets", "pin-candidates")
POOL_DIR = os.path.join(HERE, "..", "assets", "pin-backgrounds")
CREDITS_PATH = os.path.join(POOL_DIR, "credits.json")


def main():
    approved_path = os.path.join(CANDIDATES_DIR, "approved.json")
    candidates_path = os.path.join(CANDIDATES_DIR, "candidates.json")

    if not os.path.exists(approved_path):
        raise SystemExit(
            f"approved.json not found in {os.path.abspath(CANDIDATES_DIR)}.\n"
            "Open photo_review.html, review the candidates, then save the exported "
            "file there as approved.json."
        )

    with open(approved_path, encoding="utf-8") as f:
        approved = json.load(f).get("approved", [])
    if not approved:
        raise SystemExit("approved.json contains no approved photos.")

    with open(candidates_path, encoding="utf-8") as f:
        meta_by_file = {c["filename"]: c for c in json.load(f)}

    os.makedirs(POOL_DIR, exist_ok=True)

    credits = {}
    if os.path.exists(CREDITS_PATH):
        with open(CREDITS_PATH, encoding="utf-8") as f:
            credits = json.load(f)

    moved = 0
    for filename in approved:
        src = os.path.join(CANDIDATES_DIR, filename)
        if not os.path.exists(src):
            print(f"skip {filename}: not found in candidates", file=sys.stderr)
            continue
        shutil.copy2(src, os.path.join(POOL_DIR, filename))
        meta = meta_by_file.get(filename, {})
        credits[filename] = {
            "source": "Pexels",
            "photographer": meta.get("photographer", ""),
            "url": meta.get("pexels_url", ""),
            "query": meta.get("query", ""),
        }
        moved += 1

    with open(CREDITS_PATH, "w", encoding="utf-8") as f:
        json.dump(credits, f, indent=2, ensure_ascii=False)

    pool_size = len([n for n in os.listdir(POOL_DIR) if n.lower().endswith((".jpg", ".jpeg", ".png"))])
    print(f"Added {moved} photo(s). Background pool now holds {pool_size}.")
    print(f"Pool: {os.path.abspath(POOL_DIR)}")
    print("\nassets/pin-candidates/ は作業用なのでコミット不要です"
          "(.gitignore 済み)。assets/pin-backgrounds/ をコミットしてください。")


if __name__ == "__main__":
    main()
