#!/usr/bin/env python3
"""
Create a Pin on Pinterest via API v5.

Requires PINTEREST_ACCESS_TOKEN (and a board id) in .env.
Image is sent as base64 (image_base64) so no external image hosting is needed.

Usage:
  python3 post_to_pinterest.py \
    --title "Best Red Light Therapy Devices for Home Use" \
    --description "A no-hype buyer's guide... #homewellness #recoverytools" \
    --link "https://example.com/posts/red-light-therapy-devices-for-home/" \
    --image /path/to/pin.png \
    [--board-id BOARD_ID] [--dry-run]
"""
import argparse
import base64
import os
import re
import sys
import mimetypes
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE = "https://api.pinterest.com/v5"

# Pinterest board IDs are always numeric strings. Manifests sometimes carry a
# human-readable board *name* (from the original 5-board plan in
# docs/pinterest_sns_plan.md) instead of the board's real numeric ID -- this
# happens for boards that haven't actually been created on Pinterest yet.
# Map known board names to their real IDs here as boards get created; any
# name not listed (or any non-numeric value) falls back to the default board
# instead of failing the whole pin.
BOARD_NAME_TO_ID = {
    "Red Light Therapy at Home": "904449606356442643",
}


def _resolve_board_id(board_id):
    default_id = os.environ.get("PINTEREST_DEFAULT_BOARD_ID")
    if not board_id:
        return default_id
    if re.fullmatch(r"\d+", str(board_id)):
        return board_id
    if board_id in BOARD_NAME_TO_ID:
        return BOARD_NAME_TO_ID[board_id]
    print(
        f"Warning: board '{board_id}' is not a known numeric Pinterest board ID "
        f"(not yet created / not in BOARD_NAME_TO_ID) -- falling back to default board.",
        file=sys.stderr,
    )
    return default_id


def create_pin(title, description, link, image_path, board_id, dry_run=False):
    token = os.environ.get("PINTEREST_ACCESS_TOKEN")
    board_id = _resolve_board_id(board_id)

    if not board_id and not dry_run:
        raise RuntimeError("No board_id provided and PINTEREST_DEFAULT_BOARD_ID not set in .env")

    with open(image_path, "rb") as f:
        image_bytes = f.read()
    content_type = mimetypes.guess_type(image_path)[0] or "image/png"
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    payload = {
        "board_id": board_id,
        "title": title[:100],
        "description": description[:800],
        "link": link,
        "media_source": {
            "source_type": "image_base64",
            "content_type": content_type,
            "data": image_b64,
        },
    }

    if dry_run:
        print("[DRY RUN] Would POST to", f"{API_BASE}/pins")
        print("  board_id:", board_id)
        print("  title:", title)
        print("  link:", link)
        print("  image bytes:", len(image_bytes))
        return {"dry_run": True}

    if not token:
        raise RuntimeError("PINTEREST_ACCESS_TOKEN not set in .env")

    resp = requests.post(
        f"{API_BASE}/pins",
        headers={"Authorization": f"Bearer {token}"},
        json=payload,
        timeout=30,
    )
    if resp.status_code >= 300:
        print(f"Pinterest API error {resp.status_code}: {resp.text}", file=sys.stderr)
        resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--link", required=True)
    parser.add_argument("--image", required=True)
    parser.add_argument("--board-id", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    result = create_pin(args.title, args.description, args.link, args.image, args.board_id, args.dry_run)
    print(result)
