"""
Pinterest のアクセストークンを、実行のたびにリフレッシュトークンから作り直す。

背景(2026-10-04):
- Developer Portal の「アクセストークンを生成する」で作ったトークンは約1日で失効し、
  計測用の PINTEREST_READ_TOKEN が 10/1 から 401 になっていた
- OAuth で取ったアクセストークンも30日で切れる。投稿用の PINTEREST_ACCESS_TOKEN は
  9/9 登録なので 10/9 ごろに切れる見込みだった
- リフレッシュトークンは1年有効。これと Client ID / Secret を Secrets に置いておけば、
  毎回の実行で新しいアクセストークンを作れるので、手で差し替える必要がなくなる

必要な環境変数(GitHub Secrets):
  PINTEREST_REFRESH_TOKEN, PINTEREST_CLIENT_ID, PINTEREST_CLIENT_SECRET
未設定の場合は、従来どおり固定のトークン(fallback_env で指定した環境変数)を使う。
"""
import os
import sys

import requests

TOKEN_URL = "https://api.pinterest.com/v5/oauth/token"
_cache = {}


def access_token(fallback_env="PINTEREST_ACCESS_TOKEN"):
    refresh = os.environ.get("PINTEREST_REFRESH_TOKEN", "").strip()
    client_id = os.environ.get("PINTEREST_CLIENT_ID", "").strip()
    secret = os.environ.get("PINTEREST_CLIENT_SECRET", "").strip()
    if not (refresh and client_id and secret):
        return os.environ.get(fallback_env)

    if "token" in _cache:
        return _cache["token"]
    resp = requests.post(
        TOKEN_URL,
        auth=(client_id, secret),
        data={"grant_type": "refresh_token", "refresh_token": refresh},
        timeout=30,
    )
    if resp.status_code >= 300:
        # 応答本文にトークンは含まれないが、念のため先頭だけ出す
        print(f"Pinterest トークンの更新に失敗: HTTP {resp.status_code} {resp.text[:150]}", file=sys.stderr)
        return os.environ.get(fallback_env)
    data = resp.json()
    _cache["token"] = data["access_token"]
    if "scope" in data:
        _cache["scope"] = data["scope"]
    return _cache["token"]


def has_credentials(fallback_env="PINTEREST_ACCESS_TOKEN"):
    return bool(os.environ.get("PINTEREST_REFRESH_TOKEN") or os.environ.get(fallback_env))
