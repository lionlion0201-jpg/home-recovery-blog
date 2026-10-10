#!/usr/bin/env python3
"""
X(旧Twitter)の自動投稿用アクセストークンを、指定したアカウントで発行し直して
GitHub Secrets に登録する。

なぜ必要か
----------
2026-10-10 の点検で、US(QuietRecover)の英語の投稿が JP(シニアペット)のアカウント
(@95wDCuNebX41439、現 @2seniorpets)から出ていたことが分かった。8/7 に US 用のトークンを作ったとき、
JP のアカウントでログインしたまま発行したとみられる。X の開発者画面でトークンを
作ると、そのときログインしているアカウントの投稿権限になるため、取り違えやすい。

このスクリプトは、ブラウザで「どのアカウントで許可するか」を選ぶ方式(PIN方式)で
トークンを作り、最後に「どのアカウントのトークンか」を表示してから登録する。
違うアカウントだったら登録せずに止まる。

やること:
  1. 開発者アプリの API Key / API Key Secret を .env(git 管理外)に書いてもらい、そこから読む
  2. 認可URLを表示 → ブラウザで US のアカウントにログインして「許可」→ 表示された番号(PIN)を入力
  3. 発行されたトークンで「誰のトークンか」を確認し、@ユーザー名を表示する
  4. 想定のアカウントだと確認できたら、GitHub Secrets の X_API_KEY / X_API_SECRET /
     X_ACCESS_TOKEN / X_ACCESS_TOKEN_SECRET を上書きする
     (gh CLI に標準入力で渡すので、値は画面にもファイルにも残らない)

注意: 開発者アプリの権限が "Read and write" になっていないと投稿できない。
      アプリの権限を変えた場合は、変えた後に発行したトークンでないと反映されない。

Usage(自分のターミナルで):
  python3 scripts/setup_x_oauth.py
"""
import os
import re
import subprocess
import sys

import tweepy

REPO = "lionlion0201-jpg/home-recovery-blog"
GH = os.path.expanduser("~/.local/bin/gh")
# JP のアカウント(@2seniorpets、旧 @95wDCuNebX41439)。US 用にこれで許可してしまったら登録しない。
# ユーザー名は変えられるので、変わらない数字のIDで判定する
WRONG_ACCOUNT_ID = "1963740489590661120"


ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")


def read_env():
    """.env の値を読む(値は表示しない)。前後の空白や引用符は取り除く。"""
    values = {}
    if not os.path.exists(ENV_FILE):
        return values
    with open(ENV_FILE, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\s*([A-Z_]+)\s*=\s*(.*)$", line)
            if m:
                values[m.group(1)] = m.group(2).strip().strip('"').strip("'").strip()
    return values


def write_env(updates):
    """.env の指定キーだけ書き換える(手元で手動実行するとき用。.env は git 管理外)。"""
    with open(ENV_FILE, encoding="utf-8") as f:
        lines = f.read().splitlines()
    done = set()
    for i, line in enumerate(lines):
        m = re.match(r"\s*([A-Z_]+)\s*=", line)
        if m and m.group(1) in updates:
            lines[i] = f"{m.group(1)}={updates[m.group(1)]}"
            done.add(m.group(1))
    lines += [f"{k}={v}" for k, v in updates.items() if k not in done]
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def set_secret(name, value):
    subprocess.run([GH, "secret", "set", name, "-R", REPO], input=value.encode(), check=True)


def main():
    # API Key / Secret はターミナルに貼り付けず、.env に書いてもらって読む。
    # 2026-10-10: 画面に表示されない入力欄(getpass)への貼り付けが何度やっても通らなかったため
    env = read_env()
    api_key, api_secret = env.get("X_API_KEY", ""), env.get("X_API_SECRET", "")
    if not api_key or not api_secret:
        sys.exit(f"{ENV_FILE} の X_API_KEY= と X_API_SECRET= の後ろに値を貼り付けて保存してから、もう一度実行してください。")
    print(f".env から API Key({len(api_key)}文字)と API Key Secret({len(api_secret)}文字)を読み込みました。")

    auth = tweepy.OAuth1UserHandler(api_key, api_secret, callback="oob")
    try:
        url = auth.get_authorization_url()
    except tweepy.TweepyException as e:
        sys.exit(f"認可URLを作れませんでした。API Key / Secret を確認してください({e})")

    print()
    print("1. いま X にログインしているアカウントを、ブラウザで一度ログアウトしてください")
    print("   (または別のブラウザ/シークレットウィンドウを使う)")
    print("2. 下のURLを開き、**QuietRecover 用(US)のアカウント**でログインして「連携アプリを認証」を押す")
    print("3. 表示された番号(PIN)を、ここに入力する")
    print()
    print(url)
    print()
    pin = input("PIN: ").strip()

    try:
        token, token_secret = auth.get_access_token(pin)
    except tweepy.TweepyException as e:
        sys.exit(f"PIN からトークンを作れませんでした。もう一度最初からやり直してください({e})")

    client = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret,
                           access_token=token, access_token_secret=token_secret)
    try:
        me = client.get_me(user_auth=True).data
    except tweepy.TweepyException as e:
        sys.exit(f"トークンの持ち主を確認できませんでした({e})")

    print()
    print(f"このトークンのアカウント: @{me.username}({me.name})")
    if str(me.id) == WRONG_ACCOUNT_ID:
        sys.exit("これは JP(シニアペット)のアカウントです。登録せずに終了します。"
                 "US のアカウントでログインし直して、もう一度実行してください。")

    answer = input(f"@{me.username} を US サイト(QuietRecover)の投稿用として登録しますか? [y/N]: ").strip().lower()
    if answer != "y":
        sys.exit("登録しませんでした。")

    for name, value in [("X_API_KEY", api_key), ("X_API_SECRET", api_secret),
                        ("X_ACCESS_TOKEN", token), ("X_ACCESS_TOKEN_SECRET", token_secret)]:
        set_secret(name, value)
    write_env({"X_ACCESS_TOKEN": token, "X_ACCESS_TOKEN_SECRET": token_secret})
    print(f"{REPO} の Secrets に登録しました。次の投稿から @{me.username} で投稿されます。")
    print(f"アカウントID(メモ用): {me.id}")


if __name__ == "__main__":
    main()
