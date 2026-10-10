#!/usr/bin/env python3
"""
下書き記事の Amazon リンクを一覧にする(Amazon 確認の作業リスト)。

なぜ必要か
----------
ファクトチェッカーは WebFetch で Amazon を開けない(503 で拒否される)ため、
「リンク先に狙った商品が出るか」は人間の確認として残っていた。
2026-10-10 に、デスクトップアプリの内蔵ブラウザなら Amazon の検索結果を
読めることを確認したので、パイプラインがこの一覧を使って1本ずつ開いて確かめる。
手順は docs/agents/fact_checker.md の「Amazon 確認」。

同じ検索URLは記事内で何度も出てくるので、URL単位にまとめる。

Usage:
  python3 scripts/list_amazon_links.py                  # 下書き(published: false)すべて
  python3 scripts/list_amazon_links.py slug1 slug2      # 記事を指定
"""
import glob
import html
import json
import os
import re
import sys
from urllib.parse import parse_qs, urlparse

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
POSTS = os.path.join(ROOT, "src", "posts")
LINK = re.compile(r'<a\s+[^>]*href="(https://www\.amazon\.com/[^"]+)"[^>]*>(.*?)</a>', re.S)


def is_draft(text):
    head = text.split("---", 2)[1] if text.startswith("---") else ""
    return re.search(r"^published:\s*false\s*$", head, re.M) is not None


def links_in(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    found = {}
    for m in LINK.finditer(text):
        url = html.unescape(m.group(1))
        line = text.count("\n", 0, m.start()) + 1
        label = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        query = parse_qs(urlparse(url).query)
        entry = found.setdefault(url, {
            "url": url,
            "search": (query.get("k") or [""])[0],
            "tag_ok": query.get("tag") == ["quietrecover-20"],
            "lines": [],
            "labels": [],
        })
        entry["lines"].append(line)
        if label and label not in entry["labels"]:
            entry["labels"].append(label)
    return list(found.values())


def main():
    slugs = sys.argv[1:]
    paths = ([os.path.join(POSTS, f"{s}.md") for s in slugs] if slugs
             else sorted(glob.glob(os.path.join(POSTS, "*.md"))))
    out = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            if not slugs and not is_draft(f.read()):
                continue
        out.append({"slug": os.path.basename(p)[:-3], "links": links_in(p)})
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
