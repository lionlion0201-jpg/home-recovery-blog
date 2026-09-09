#!/usr/bin/env python3
"""
Refresh an expired Pinterest access_token using the stored refresh_token,
and write the new access_token straight into both .env files (scripts/.env
and the project-root .env), so no token value needs to be typed or shown
anywhere else.

Why this exists: PINTEREST_ACCESS_TOKEN started returning
"401 Authentication failed" on 2026-09-09 (both reads and pin creation),
which means the access token itself expired -- Pinterest access tokens are
short-lived and need periodic refreshing via the refresh_token, which the
project already stores in .env but had no script to actually use.

You will be prompted for the Pinterest app's Client ID and Client Secret
(the same two values used for the original OAuth setup). They are only
used in-memory for this one request and are never written anywhere.

Usage (run this from your own terminal -- api.pinterest.com is not
reachable from the Cowork sandbox):
  cd scripts
  python3 refresh_pinterest_token.py
"""
import os
import re
import sys

import requests
from dotenv import load_dotenv

SCRIPT_DIR = os.path.dirname(__file__)
ENV_PATHS = [
    os.path.join(SCRIPT_DIR, ".env"),
    os.path.join(SCRIPT_DIR, "..", ".env"),
]

load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

TOKEN_URL = "https://api.pinterest.com/v5/oauth/token"


def _update_env_file(path, updates):
    if not os.path.exists(path):
        print(f"  (skip: {path} does not exist)")
        return
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    found_keys = set()
    new_lines = []
    for line in lines:
        m = re.match(r"^([A-Z_]+)=", line)
        if m and m.group(1) in updates:
            key = m.group(1)
            new_lines.append(f"{key}={updates[key]}\n")
            found_keys.add(key)
        else:
            new_lines.append(line)

    for key, value in updates.items():
        if key not in found_keys:
            new_lines.append(f"{key}={value}\n")

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"  updated: {path}")


def main():
    refresh_token = os.environ.get("PINTEREST_REFRESH_TOKEN")
    if not refresh_token:
        print("PINTEREST_REFRESH_TOKEN not found in scripts/.env -- cannot refresh.", file=sys.stderr)
        sys.exit(1)

    client_id = input("Pinterest app Client ID: ").strip()
    client_secret = input("Pinterest app Client Secret: ").strip()
    print(f"  (using Client ID: {client_id!r}, Client Secret length: {len(client_secret)})")

    resp = requests.post(
        TOKEN_URL,
        auth=(client_id, client_secret),
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )

    if resp.status_code >= 300:
        print(f"Refresh failed: {resp.status_code} {resp.text}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    new_access_token = data.get("access_token")
    new_refresh_token = data.get("refresh_token", refresh_token)

    if not new_access_token:
        print(f"No access_token in response: {data}", file=sys.stderr)
        sys.exit(1)

    print("Refresh succeeded. Updating .env files...")
    updates = {
        "PINTEREST_ACCESS_TOKEN": new_access_token,
        "PINTEREST_REFRESH_TOKEN": new_refresh_token,
    }
    for path in ENV_PATHS:
        _update_env_file(path, updates)

    print("\nDone. Next steps:")
    print("1. Update the PINTEREST_ACCESS_TOKEN secret on GitHub (Settings > Secrets and variables > Actions)")
    print("   with the new value now saved in your .env file.")
    print("2. If the refresh_token also changed, no action needed there -- GitHub Actions doesn't use it directly.")


if __name__ == "__main__":
    main()
