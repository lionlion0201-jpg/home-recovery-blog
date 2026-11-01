#!/usr/bin/env python3
"""
公開済みの既存記事に、新しいピン(新しい切り口の文面+別デザインの画像)を足すための補助スクリプト。
2026-11-01 追加。

なぜ:
  Pinterest は新しい画像のピンを優遇する。新記事は週3本・各4枚なので、9月からの投稿待ちが
  無くなると毎日の投稿が途切れがちになる。既存記事にも週に数枚ずつ新しいピンを足して、
  毎日3〜4枚の投稿を続ける。投稿そのものは今までどおり post_pin_backlog.py(1日4枚まで)が行う。

流れ(US の週次パイプラインが実行する):
  1. python3 scripts/pin_refresh.py candidates   ピンを足す記事の候補(最後にピンを出してから日が経った順)
  2. 候補の記事を読み、これまでのピンと違う切り口の文面を作り、
     docs/cycles/cycle_manifest_YYYY-MM-DD_refresh_<記事スラッグ>.json に保存する
     (記事は公開済みなので pending ではなく docs/cycles/ に直接置く)
  3. python3 scripts/pin_refresh.py check        保存したマニフェストを機械的に確認する(error が0になるまで直す)

マニフェストの形は通常と同じ。各ピンに "style": "overlay" | "card" | "bold" を付けて、
同じ記事のピンが同じ見た目に偏らないようにする(generate_pin_image.py の説明を参照)。
"""
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(__file__))
from run_new_promotions import publish_at, is_live  # noqa: E402
from generate_pin_image import STYLES  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
POSTS_DIR = os.path.join(ROOT, "src", "posts")
CYCLES_DIR = os.path.join(ROOT, "docs", "cycles")
LEDGER = os.path.join(ROOT, "docs", "metrics", "posted_assets.json")
SITE = "https://quietrecover.com"

PRICE = re.compile(r"\$\s?[0-9]")
OFF = re.compile(r"[0-9]+\s*%\s*off", re.I)


def published_slugs():
    now = datetime.now(timezone.utc)
    out = []
    for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
        slug = os.path.basename(path)[:-3]
        when = publish_at(slug)
        if when is not None and when <= now:
            out.append(slug)
    return out


def manifest_pins_by_slug():
    """記事ごとの、マニフェストにあるピン(投稿済み・投稿待ちの両方)。"""
    pins = {}
    for path in glob.glob(os.path.join(CYCLES_DIR, "cycle_manifest_*.json*")):
        if path.endswith(".posted") and os.path.exists(path[:-len(".posted")]):
            continue
        try:
            manifest = json.load(open(path, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for p in manifest.get("pins", []):
            m = re.search(r"/posts/([^/?#]+)/?", p.get("link", ""))
            if m:
                pins.setdefault(m.group(1), []).append(p)
    return pins


def cmd_candidates(limit=8):
    ledger = json.load(open(LEDGER, encoding="utf-8")) if os.path.exists(LEDGER) else []
    last = {}
    for a in ledger:
        if a.get("platform") == "pinterest" and a.get("article"):
            last[a["article"]] = max(last.get(a["article"], ""), a.get("posted_at", ""))
    pins = manifest_pins_by_slug()
    rows = sorted(published_slugs(), key=lambda s: last.get(s, ""))
    print(f"公開済みの記事 {len(rows)} 本。最後にピンを投稿した日が古い順に {limit} 本:")
    for slug in rows[:limit]:
        titles = [p["title"] for p in pins.get(slug, [])]
        print(f"\n- {slug}  最後の投稿: {last.get(slug, 'なし')[:10]}  既存ピン {len(titles)} 枚")
        for t in titles:
            print(f"    既存: {t}")


def cmd_check():
    errors = warns = 0
    paths = sorted(glob.glob(os.path.join(CYCLES_DIR, "cycle_manifest_*_refresh_*.json")))
    existing = {p["title"].strip().lower()
                for path in glob.glob(os.path.join(CYCLES_DIR, "cycle_manifest_*.json*"))
                if "_refresh_" not in path
                for p in json.load(open(path, encoding="utf-8")).get("pins", [])}
    published = set(published_slugs())
    for path in paths:
        name = os.path.basename(path)
        manifest = json.load(open(path, encoding="utf-8"))
        for i, p in enumerate(manifest.get("pins", [])):
            where = f"{name}#{i}"
            problems = []
            m = re.search(r"/posts/([^/?#]+)/$", p.get("link", ""))
            if not p.get("link", "").startswith(SITE + "/posts/") or not m:
                problems.append(("error", "link が https://quietrecover.com/posts/<スラッグ>/ の形ではない"))
            elif m.group(1) not in published:
                problems.append(("error", f"{m.group(1)} は公開済みの記事ではない"))
            elif not is_live(p["link"]):
                problems.append(("error", f"{p['link']} が開けない"))
            text = " ".join(str(p.get(k, "")) for k in ("title", "subtitle", "description", "cta"))
            if PRICE.search(text) or OFF.search(text):
                problems.append(("error", "価格や割引率を書いている(US の Amazon 規約で禁止)"))
            if not p.get("title") or len(p["title"]) > 100:
                problems.append(("error", "title が空か100文字を超えている"))
            if len(p.get("description", "")) > 500:
                problems.append(("error", "description が500文字を超えている"))
            if p.get("style") not in STYLES:
                problems.append(("warn", f"style が {'/'.join(STYLES)} のどれでもない(タイトルから自動で選ばれる)"))
            if p.get("title", "").strip().lower() in existing:
                problems.append(("error", "既存のピンと同じタイトル(Pinterest で重複扱いになる)"))
            for level, msg in problems:
                print(f"[{level}] {where}: {msg}")
                errors += level == "error"
                warns += level == "warn"
    print(f"\n確認したマニフェスト {len(paths)} 件 / error {errors} / warn {warns}")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "candidates":
        cmd_candidates(int(sys.argv[2]) if len(sys.argv) > 2 else 8)
    elif cmd == "check":
        cmd_check()
    else:
        sys.exit("使い方: pin_refresh.py candidates [件数] | check")
