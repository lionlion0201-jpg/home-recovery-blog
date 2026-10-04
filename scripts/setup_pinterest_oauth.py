#!/usr/bin/env python3
"""
Pinterest の認可をやり直し、1年有効のリフレッシュトークンを GitHub Secrets に登録する。

これを1回やっておけば、Actions(投稿・計測)が実行のたびにアクセストークンを作り直すので
(scripts/pinterest_auth.py)、トークン切れで止まることがなくなる。

やること:
  1. Client ID / Client Secret を入力してもらう(Secret は画面に表示しない)
  2. 認可URLを表示 → ブラウザで「許可」→ 移動先のURL(localhost/callback?code=...)を貼ってもらう
  3. コードをトークンに交換し、scope に pins:read と pins:write が入っているか確認する
  4. GitHub Secrets に PINTEREST_REFRESH_TOKEN / PINTEREST_CLIENT_ID / PINTEREST_CLIENT_SECRET を登録する
     (gh CLI に標準入力で渡すので、値は画面にもファイルにも残らない)
  5. scripts/.env の PINTEREST_REFRESH_TOKEN も更新する(ローカルでの手動実行用。.env は git 管理外)

Usage(自分のターミナルで):
  python3 scripts/setup_pinterest_oauth.py
"""
import getpass
import os
import re
import subprocess
import sys
import urllib.parse

import requests

REPO = "lionlion0201-jpg/home-recovery-blog"
GH = os.path.expanduser("~/.local/bin/gh")
SCOPES = "boards:read,boards:write,pins:read,pins:write"
ENV_FILE = os.path.join(os.path.dirname(__file__), ".env")


def set_secret(name, value):
    subprocess.run([GH, "secret", "set", name, "-R", REPO], input=value, text=True, check=True,
                   stdout=subprocess.DEVNULL)
    print(f"  GitHub Secrets に {name} を登録しました")


def update_env(key, value):
    lines = open(ENV_FILE, encoding="utf-8").read().splitlines() if os.path.exists(ENV_FILE) else []
    out, found = [], False
    for line in lines:
        if line.startswith(key + "="):
            out.append(f"{key}={value}")
            found = True
        else:
            out.append(line)
    if not found:
        out.append(f"{key}={value}")
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


def main():
    print("Pinterest Developer Portal(https://developers.pinterest.com → My apps → App ID 1594065)の値を入力してください。")
    client_id = input("Client ID(App ID): ").strip()
    client_secret = getpass.getpass("Client Secret(入力しても表示されません): ").strip()
    redirect = input("Redirect URI(そのまま Enter で https://localhost/callback): ").strip() or "https://localhost/callback"

    url = "https://www.pinterest.com/oauth/?" + urllib.parse.urlencode({
        "client_id": client_id, "redirect_uri": redirect, "response_type": "code",
        "scope": SCOPES, "state": "setup",
    })
    print("\n次の URL をブラウザで開き、「許可する」を押してください:\n")
    print(url)
    print("\n許可すると、表示できないページ(localhost)に移動します。それで正常です。")
    pasted = input("そのときのアドレスバーの URL をまるごと貼って Enter: ").strip()
    m = re.search(r"[?&]code=([^&]+)", pasted)
    if not m:
        sys.exit("URL に code= が見つかりませんでした。最初からやり直してください。")

    resp = requests.post(
        "https://api.pinterest.com/v5/oauth/token",
        auth=(client_id, client_secret),
        data={"grant_type": "authorization_code", "code": m.group(1), "redirect_uri": redirect},
        timeout=30,
    )
    if resp.status_code >= 300:
        sys.exit(f"トークンの取得に失敗しました: HTTP {resp.status_code} {resp.text[:200]}\n"
                 "コードは数分で失効するので、最初からやり直してください。")
    data = resp.json()
    scope = data.get("scope", "")
    missing = [s for s in ("pins:read", "pins:write", "boards:read") if s not in scope]
    if missing:
        sys.exit(f"権限が足りません({', '.join(missing)} が無い)。許可画面で全ての権限を許可してやり直してください。")
    refresh = data.get("refresh_token")
    if not refresh:
        sys.exit("リフレッシュトークンが返ってきませんでした。")

    print(f"\n取得できました(権限: {scope})。GitHub に登録します。")
    set_secret("PINTEREST_REFRESH_TOKEN", refresh)
    set_secret("PINTEREST_CLIENT_ID", client_id)
    set_secret("PINTEREST_CLIENT_SECRET", client_secret)
    update_env("PINTEREST_REFRESH_TOKEN", refresh)
    update_env("PINTEREST_ACCESS_TOKEN", data["access_token"])
    print("  scripts/.env も更新しました")
    print("\n完了です。Claude に「Pinterest の登録が終わった」と伝えてください。")


if __name__ == "__main__":
    main()
