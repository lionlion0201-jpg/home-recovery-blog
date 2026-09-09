#!/usr/bin/env python3
"""
Local, git-committed record of tweet text / pin titles that have actually
been posted for real (not dry-run). This is the duplicate-prevention safety
net for post_to_twitter.py and post_to_pinterest.py.

Why a local file instead of asking the API "have I already posted this?":
that was the previous approach (querying client.get_users_tweets() / the
Pinterest board's existing pins) and it failed silently on 2026-09-09 --
both read endpoints returned 401 Unauthorized under the account's current
API access tier, the check treated "couldn't check" as "safe to post", and
the account ended up with a dozen duplicate tweets as a result. A local log
that we write ourselves right after every real, successful post has no such
dependency: it doesn't need read access to any external API, and it's
committed to git in the same step that commits the *.posted markers, so it
persists across workflow runs just like they do.

This does mean the log can only know about posts made by this codebase
(not, say, a tweet posted manually from the X app) -- that's an accepted
limitation, not a gap that matters for this pipeline's use case.

Usage:
    from posted_content_log import PostedContentLog
    log = PostedContentLog()
    if log.has_tweet(text):
        ...skip...
    else:
        ...post it...
        log.add_tweet(text)  # saves to disk immediately
"""
import json
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), "posted_content_log.json")


def _normalize(text):
    """Loose normalization so near-identical text (whitespace/case
    differences) still counts as the same content for duplicate detection."""
    return " ".join((text or "").split()).strip().lower()


class PostedContentLog:
    def __init__(self, path=LOG_PATH):
        self.path = path
        self._data = self._load()

    def _load(self):
        if not os.path.exists(self.path):
            return {"tweets": [], "pins": []}
        try:
            with open(self.path, encoding="utf-8") as f:
                data = json.load(f)
            data.setdefault("tweets", [])
            data.setdefault("pins", [])
            return data
        except Exception as e:
            # A corrupt/unreadable log is treated as empty rather than
            # blocking every post -- but this is logged loudly since it
            # means duplicate protection is effectively reset.
            print(f"Warning: posted_content_log.json unreadable ({e}); starting a fresh log.")
            return {"tweets": [], "pins": []}

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2, ensure_ascii=False)

    def has_tweet(self, text):
        return _normalize(text) in self._data["tweets"]

    def add_tweet(self, text):
        norm = _normalize(text)
        if norm not in self._data["tweets"]:
            self._data["tweets"].append(norm)
            self._save()

    def has_pin(self, title):
        return _normalize(title) in self._data["pins"]

    def add_pin(self, title):
        norm = _normalize(title)
        if norm not in self._data["pins"]:
            self._data["pins"].append(norm)
            self._save()
