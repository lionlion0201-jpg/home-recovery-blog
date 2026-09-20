#!/usr/bin/env python3
"""
投稿した資産(ツイート・ピン)のIDを残す台帳。

なぜ必要か
----------
`post_to_twitter.py` も `post_to_pinterest.py` も、投稿に成功すると発行された
ID を戻り値で返している。しかし呼び出し側(`run_promotion.py` /
`post_pin_backlog.py`)はそれを標準出力に出すだけで、どこにも保存していなかった。
IDが残っていないと、後からその投稿がどれだけ見られ・クリックされたかを
APIで問い合わせる手段がない。つまり「投稿はできるが効果は永久に分からない」
状態だった(2026-09-20 に発覚)。

この台帳は、あとからメトリクスを引くための最小限の情報だけを持つ:
どのプラットフォームの、どのIDの投稿が、どの記事に紐づくか。
実測値そのものはここには入れない(別ファイルに追記していく)。

参照: アフィリエイト/共通/計測設計.md
"""
import json
import os
import re
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=9))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LEDGER_FILE = os.path.join(SCRIPT_DIR, "..", "docs", "metrics", "posted_assets.json")


def _load():
    if not os.path.exists(LEDGER_FILE):
        return []
    try:
        with open(LEDGER_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # 壊れていても投稿処理そのものは止めない。台帳は補助的な記録なので、
        # ここで例外を投げると本来成功しているはずの投稿が失敗扱いになる。
        return []


def _save(rows):
    os.makedirs(os.path.dirname(LEDGER_FILE), exist_ok=True)
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


def article_slug(manifest_path, manifest=None):
    """記事スラッグを割り出す。

    新しいマニフェストはファイル名に記事スラッグを含む:
      cycle_manifest_2026-09-19_cold-plunge-vs-red-light-therapy.json
    2026-09-12以前のものは日付のみなので、ピンのリンクURLの末尾から拾う。
    """
    base = os.path.basename(manifest_path)
    m = re.match(r"cycle_manifest_\d{4}-\d{2}-\d{2}_(.+)\.json$", base)
    if m:
        return m.group(1)

    pins = (manifest or {}).get("pins") or []
    for pin in pins:
        link = pin.get("link", "")
        m = re.search(r"/posts/([a-z0-9-]+)/?", link)
        if m:
            return m.group(1)
    return None


def _is_real_id(asset_id):
    """dry-run の疑似IDや None を弾く。"""
    if not asset_id:
        return False
    return not str(asset_id).startswith("dryrun-")


def record(platform, asset_id, article=None, content_type=None, link=None,
           text=None, source=None):
    """1件を台帳に追記する。同じ (platform, id) は二重に入れない。

    戻り値: 追記したら True、スキップしたら False。
    """
    if not _is_real_id(asset_id):
        return False

    rows = _load()
    key = (platform, str(asset_id))
    if any((r.get("platform"), str(r.get("id"))) == key for r in rows):
        return False

    rows.append({
        "platform": platform,
        "id": str(asset_id),
        "article": article,
        "type": content_type,
        "link": link,
        "source": source,
        "posted_at": datetime.now(JST).isoformat(),
        "text_excerpt": (text or "")[:120] or None,
    })
    _save(rows)
    return True


def record_safe(*args, **kwargs):
    """記録に失敗しても呼び出し元を落とさない版。

    台帳への書き込みは投稿処理の副次的な作業であり、ここでの失敗を理由に
    投稿フロー全体を止めるべきではない(投稿済みなのにマーカーが残らない、
    という最悪のパターンを避ける)。
    """
    try:
        return record(*args, **kwargs)
    except Exception as e:  # noqa: BLE001
        print(f"Warning: could not write to asset ledger ({e})")
        return False
