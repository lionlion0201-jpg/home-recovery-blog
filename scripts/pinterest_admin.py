#!/usr/bin/env python3
"""
Pinterest のボードとピンを、サイトのテーマ(src/_data/categories.json)に合わせて整える管理用スクリプト。
2026-10-17 追加。GitHub Actions の pinterest-admin.yml から手動で実行する(リフレッシュトークンが Actions にあるため)。

背景:
- 当初計画の5ボードのうち実際に作られていたのは1つだけで、作られていないボード宛てのピンは既定のボードに
  まとめて入っていた。テーマの違うピンが同じボードに混ざると、Pinterest がピンの内容を判断しにくい
- 投稿済みピンの約半分が旧 URL(lionlion0201-jpg.github.io/home-recovery-blog/...)にリンクしていた

コマンド:
  boards                       アカウントのボード一覧(ID・名前・ピン数)
  ensure-boards [--apply]      テーマごとのボードが無ければ作る。docs/pinterest_boards.json に テーマ→ボードID を書く
  fix-pins [--limit N] [--apply]
                               全ピンを一覧し、リンク先の記事のテーマに合うボードへ移し、旧 URL を新ドメインに直す。
                               --apply が無ければ何を変えるかの表示だけ(ドライラン)
"""
import argparse
import json
import os
import re
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(__file__))
from pinterest_auth import access_token  # noqa: E402

API = "https://api.pinterest.com/v5"
ROOT = os.path.join(os.path.dirname(__file__), "..")
CATEGORIES = os.path.join(ROOT, "src", "_data", "categories.json")
BOARDS_FILE = os.path.join(ROOT, "docs", "pinterest_boards.json")
OLD_PREFIX = "https://lionlion0201-jpg.github.io/home-recovery-blog/"
NEW_PREFIX = "https://quietrecover.com/"

# テーマ → Pinterest ボードの名前と説明。名前は Pinterest で検索されやすい言い方にする
BOARD_SPECS = {
    "recovery": ("Home Recovery & Massage Tools",
                 "Massage guns, shiatsu massagers, compression boots, red light therapy, cold plunges and sauna blankets "
                 "for muscle recovery at home. Practical comparisons to help you choose the right recovery tool."),
    "sleep-environment": ("Bedroom Sleep Environment Ideas",
                          "Ideas for a quieter, darker, cooler bedroom: white noise machines, blackout curtains, sleep masks, "
                          "cooling pillows, bedding for hot sleepers, humidifiers and quiet space heaters."),
    "sleep-tracking-aids": ("Sleep Trackers & Sleep Aids",
                            "Sleep tracking rings and wearables (Oura, Whoop, Apple Watch), weighted blankets, sunrise alarm "
                            "clocks and other sleep aids compared for light sleepers and shift workers."),
    "gift-guides": ("Recovery & Sleep Gift Ideas",
                    "Gift ideas for people who are always tired or sore: home recovery and sleep gifts by budget and by recipient."),
}

RENAME_EXISTING = {"recovery": "Red Light Therapy at Home"}


def headers():
    tok = access_token("PINTEREST_ACCESS_TOKEN")
    if not tok:
        sys.exit("Pinterest のトークンがありません(PINTEREST_REFRESH_TOKEN などの Secrets を確認)")
    return {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}


def paged(url, h, params=None):
    params = dict(params or {}, page_size=100)
    while True:
        r = requests.get(url, headers=h, params=params, timeout=30)
        r.raise_for_status()
        d = r.json()
        yield from d.get("items", [])
        if not d.get("bookmark"):
            return
        params["bookmark"] = d["bookmark"]


def theme_of(link, cats):
    m = re.search(r"/posts/([^/?#]+)/?", link or "")
    if not m:
        return None
    return cats["posts"].get(m.group(1))


def cmd_boards(h):
    for b in paged(f"{API}/boards", h):
        print(f"{b['id']}  {b['name']}  ピン数 {b.get('pin_count')}  公開 {b.get('privacy')}")


def cmd_ensure_boards(h, apply):
    existing = {b["name"]: b["id"] for b in paged(f"{API}/boards", h)}
    mapping = {}
    # 全ピンが入っている既存ボードは作り直さず、名前と説明を変えてリカバリー用に使う(保存やフォローを残すため)
    for theme, old_name in RENAME_EXISTING.items():
        name, desc = BOARD_SPECS[theme]
        if old_name in existing and name not in existing:
            if apply:
                r = requests.patch(f"{API}/boards/{existing[old_name]}", headers=h,
                                   json={"name": name, "description": desc}, timeout=30)
                if r.status_code >= 300:
                    sys.exit(f"ボード名の変更に失敗: {old_name}: HTTP {r.status_code} {r.text[:200]}")
                print(f"名前を変更: {old_name} -> {name} ({existing[old_name]})")
            else:
                print(f"(名前を変更予定) {old_name} -> {name}")
            existing[name] = existing.pop(old_name)
    for theme, (name, desc) in BOARD_SPECS.items():
        if name in existing:
            mapping[theme] = existing[name]
            print(f"既存: {name} -> {existing[name]}")
            continue
        if not apply:
            print(f"(作成予定) {name}")
            continue
        r = requests.post(f"{API}/boards", headers=h, json={"name": name, "description": desc, "privacy": "PUBLIC"}, timeout=30)
        if r.status_code >= 300:
            sys.exit(f"ボード作成に失敗: {name}: HTTP {r.status_code} {r.text[:200]}")
        mapping[theme] = r.json()["id"]
        print(f"作成: {name} -> {mapping[theme]}")
    if apply:
        with open(BOARDS_FILE, "w", encoding="utf-8") as f:
            json.dump(mapping, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"{BOARDS_FILE} に保存しました")


def cmd_fix_pins(h, limit, apply):
    cats = json.load(open(CATEGORIES, encoding="utf-8"))
    boards = json.load(open(BOARDS_FILE, encoding="utf-8")) if os.path.exists(BOARDS_FILE) else {}
    if not boards:
        sys.exit("docs/pinterest_boards.json がありません。先に ensure-boards --apply を実行してください")
    pins = list(paged(f"{API}/pins", h))
    print(f"アカウントのピン {len(pins)} 枚")
    done = skipped = failed = 0
    for p in pins:
        link = p.get("link") or ""
        body = {}
        new_link = link.replace(OLD_PREFIX, NEW_PREFIX) if link.startswith(OLD_PREFIX) else None
        if new_link:
            body["link"] = new_link
        theme = theme_of(new_link or link, cats)
        target = boards.get(theme) if theme else None
        if target and p.get("board_id") != target:
            body["board_id"] = target
        if not body:
            skipped += 1
            continue
        if limit is not None and done >= limit:
            break
        print(f"{p['id']} [{theme or '-'}] {(p.get('title') or '')[:50]} :: "
              + (f"ボード {p.get('board_id')} -> {body['board_id']} " if 'board_id' in body else "")
              + (f"リンク -> {body['link']}" if 'link' in body else ""))
        if apply:
            r = requests.patch(f"{API}/pins/{p['id']}", headers=h, json=body, timeout=30)
            if r.status_code >= 300:
                failed += 1
                print(f"   失敗: HTTP {r.status_code} {r.text[:200]}")
            time.sleep(0.5)  # レート制限に配慮
        done += 1
    print(f"{'変更' if apply else '変更予定'} {done} 枚 / 変更不要 {skipped} 枚 / 失敗 {failed} 枚")
    if failed:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["boards", "ensure-boards", "fix-pins"])
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    h = headers()
    if a.command == "boards":
        cmd_boards(h)
    elif a.command == "ensure-boards":
        cmd_ensure_boards(h, a.apply)
    else:
        cmd_fix_pins(h, a.limit, a.apply)


if __name__ == "__main__":
    main()
