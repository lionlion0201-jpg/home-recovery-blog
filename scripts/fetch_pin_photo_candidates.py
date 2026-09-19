#!/usr/bin/env python3
"""
Fetch candidate background photos from Pexels and build an offline review page.

Why a human review step: the Pexels search API exposes only query / orientation
/ size / color / locale / page / per_page -- there is no "exclude people" or
"exclude logos" filter. Our rule for these pins is no identifiable people and no
visible brands/products (both to stay clear of personality-rights and trademark
issues, and to avoid implying a real product is pictured in a review pin). That
rule cannot be enforced automatically, so candidates get eyeballed once and only
approved photos enter the pool.

Run this locally (the Cowork sandbox cannot reach api.pexels.com). Needs
PEXELS_API_KEY in scripts/.env.

  python3 fetch_pin_photo_candidates.py [--per-query 8] [--out ../assets/pin-candidates]

Then open the generated photo_review.html, approve what passes, and save the
exported JSON as approved.json in the same folder. Finally:

  python3 apply_photo_approvals.py
"""
import argparse
import base64
import io
import json
import os
import sys
import urllib.parse

import requests
from PIL import Image
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

API = "https://api.pexels.com/v1/search"

# Scene-led queries: interiors, light, textures. Deliberately avoids anything
# that would surface people ("woman sleeping") or branded gear ("smartwatch").
DEFAULT_QUERIES = [
    "minimal bedroom interior",
    "morning light bedroom",
    "linen bedding texture",
    "calm bathroom interior",
    "wooden sauna interior",
    "neutral living room corner",
    "soft blanket texture",
    "candle warm interior",
    "houseplant minimal shelf",
    "dark moody bedroom",
    "towels folded spa",
    "window curtain daylight",
]

CHECKLIST = [
    "人物が識別できる形で写っていない",
    "ロゴ・ブランド名・商品名が写り込んでいない",
    "レビュー対象の商品そのものと誤認される恐れがない",
    "上部にテキストを載せても読める明るさ・情報量である",
]


# Pexels sits behind Cloudflare, which rejects the default Python-urllib
# User-Agent with a 403. A normal browser UA gets through.
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def _get(url, api_key):
    resp = requests.get(url, headers={"Authorization": api_key, "User-Agent": UA},
                        timeout=30)
    resp.raise_for_status()
    return resp.json()


def _download(url, timeout=60):
    resp = requests.get(url, headers={"User-Agent": UA}, timeout=timeout)
    resp.raise_for_status()
    return resp.content


def _thumb_data_uri(image_bytes, width=480):
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert("RGB")
    ratio = width / img.width
    img = img.resize((width, max(int(img.height * ratio), 1)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=72)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("ascii")


def build_review_html(candidates, out_path):
    checklist_html = "".join(f"<li>{item}</li>" for item in CHECKLIST)
    cards = []
    for idx, c in enumerate(candidates):
        cards.append(f"""
      <article class="card" id="card-{idx}" data-file="{c['filename']}">
        <img src="{c['thumb']}" alt="">
        <div class="meta">
          <span class="num">{idx + 1} / {len(candidates)}</span>
          <span class="q">検索語: {c['query']}</span>
          <a href="{c['pexels_url']}" target="_blank" rel="noopener">Pexelsで原本を見る</a>
          <span class="by">撮影: {c['photographer']}</span>
        </div>
        <ul class="checklist">{checklist_html}</ul>
        <div class="actions">
          <button class="approve" data-idx="{idx}">承認 (A)</button>
          <button class="reject" data-idx="{idx}">見送り (R)</button>
        </div>
        <div class="verdict"></div>
      </article>""")

    html = f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<title>ピン背景写真レビュー</title>
<style>
  :root {{ color-scheme: light; }}
  body {{ font-family: -apple-system, "Hiragino Sans", sans-serif; margin: 0;
         background: #faf8f5; color: #1f2937; }}
  header {{ position: sticky; top: 0; background: #2f6f4f; color: #fff;
            padding: 14px 24px; display: flex; gap: 20px; align-items: center;
            justify-content: space-between; z-index: 10; }}
  header h1 {{ font-size: 17px; margin: 0; font-weight: 600; }}
  header .counts {{ font-size: 14px; }}
  header button {{ background: #fff; color: #2f6f4f; border: 0; border-radius: 6px;
                   padding: 9px 16px; font-weight: 700; cursor: pointer; }}
  .hint {{ padding: 12px 24px; font-size: 13px; color: #6b7280; }}
  main {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
          gap: 20px; padding: 0 24px 60px; }}
  .card {{ background: #fff; border-radius: 12px; overflow: hidden;
           box-shadow: 0 1px 3px rgba(0,0,0,.09); display: flex; flex-direction: column; }}
  .card.focused {{ outline: 3px solid #2f6f4f; }}
  .card.approved {{ opacity: .55; }}
  .card.rejected {{ opacity: .3; }}
  .card img {{ width: 100%; display: block; aspect-ratio: 2/3; object-fit: cover; }}
  .meta {{ padding: 10px 14px 0; font-size: 12px; color: #6b7280;
           display: flex; flex-direction: column; gap: 2px; }}
  .checklist {{ margin: 10px 14px; padding-left: 18px; font-size: 12.5px;
                line-height: 1.75; color: #374151; }}
  .actions {{ display: flex; gap: 8px; padding: 0 14px 14px; margin-top: auto; }}
  .actions button {{ flex: 1; padding: 9px; border-radius: 7px; border: 0;
                     cursor: pointer; font-weight: 700; font-size: 13px; }}
  .approve {{ background: #2f6f4f; color: #fff; }}
  .reject {{ background: #e5e7eb; color: #374151; }}
  .verdict {{ padding: 0 14px 12px; font-size: 12px; font-weight: 700; min-height: 16px; }}
  .verdict.ok {{ color: #2f6f4f; }}
  .verdict.ng {{ color: #b91c1c; }}
</style></head><body>
<header>
  <h1>ピン背景写真レビュー</h1>
  <span class="counts"><span id="done">0</span> / {len(candidates)} 判定済み・承認 <span id="okc">0</span> 枚</span>
  <button id="export">承認リストを書き出す</button>
</header>
<p class="hint">各写真のチェック項目をすべて満たす場合のみ承認してください。カーソルキー(←→)で移動、A で承認、R で見送りができます。すべて判定したら右上のボタンでJSONを書き出し、<code>approved.json</code> という名前でこのフォルダに保存してください。</p>
<main>{''.join(cards)}</main>
<script>
const verdicts = {{}};
const cards = [...document.querySelectorAll('.card')];
let cur = 0;
function focus(i) {{
  cards.forEach(c => c.classList.remove('focused'));
  if (!cards[i]) return;
  cur = i; cards[i].classList.add('focused');
  cards[i].scrollIntoView({{ block: 'center', behavior: 'smooth' }});
}}
function setVerdict(i, ok) {{
  const card = cards[i]; if (!card) return;
  verdicts[card.dataset.file] = ok;
  card.classList.toggle('approved', ok);
  card.classList.toggle('rejected', !ok);
  const v = card.querySelector('.verdict');
  v.textContent = ok ? '承認' : '見送り';
  v.className = 'verdict ' + (ok ? 'ok' : 'ng');
  const vals = Object.values(verdicts);
  document.getElementById('done').textContent = vals.length;
  document.getElementById('okc').textContent = vals.filter(Boolean).length;
  if (i + 1 < cards.length) focus(i + 1);
}}
document.querySelectorAll('.approve').forEach(b =>
  b.onclick = () => setVerdict(+b.dataset.idx, true));
document.querySelectorAll('.reject').forEach(b =>
  b.onclick = () => setVerdict(+b.dataset.idx, false));
document.addEventListener('keydown', e => {{
  const k = e.key.toLowerCase();
  if (k === 'a') setVerdict(cur, true);
  else if (k === 'r') setVerdict(cur, false);
  else if (e.key === 'ArrowRight') focus(cur + 1);
  else if (e.key === 'ArrowLeft') focus(cur - 1);
}});
document.getElementById('export').onclick = () => {{
  const approved = Object.entries(verdicts).filter(([, v]) => v).map(([f]) => f);
  const blob = new Blob([JSON.stringify({{ approved }}, null, 2)],
                        {{ type: 'application/json' }});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'approved.json'; a.click();
}};
focus(0);
</script></body></html>"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-query", type=int, default=8)
    parser.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "assets", "pin-candidates"))
    args = parser.parse_args()

    api_key = os.environ.get("PEXELS_API_KEY")
    if not api_key:
        raise SystemExit("PEXELS_API_KEY not set in scripts/.env")

    out_dir = os.path.abspath(args.out)
    os.makedirs(out_dir, exist_ok=True)

    candidates, seen = [], set()
    for query in DEFAULT_QUERIES:
        url = (f"{API}?query={urllib.parse.quote(query)}"
               f"&orientation=portrait&size=medium&per_page={args.per_query}")
        try:
            data = _get(url, api_key)
        except Exception as e:
            print(f"[{query}] search failed: {e}", file=sys.stderr)
            continue

        for photo in data.get("photos", []):
            pid = photo["id"]
            if pid in seen:
                continue
            seen.add(pid)
            filename = f"pexels-{pid}.jpg"
            try:
                full = _download(photo["src"]["large2x"])
                with open(os.path.join(out_dir, filename), "wb") as f:
                    f.write(full)
                thumb = _thumb_data_uri(full)
            except Exception as e:
                print(f"[{query}] download failed for {pid}: {e}", file=sys.stderr)
                continue

            candidates.append({
                "id": pid,
                "filename": filename,
                "query": query,
                "photographer": photo.get("photographer", ""),
                "pexels_url": photo.get("url", ""),
                "thumb": thumb,
            })
            print(f"fetched {filename} ({query})")

    if not candidates:
        raise SystemExit("No candidates fetched.")

    with open(os.path.join(out_dir, "candidates.json"), "w", encoding="utf-8") as f:
        json.dump([{k: v for k, v in c.items() if k != "thumb"} for c in candidates],
                  f, indent=2, ensure_ascii=False)

    review_path = os.path.join(out_dir, "photo_review.html")
    build_review_html(candidates, review_path)
    print(f"\n{len(candidates)} candidate(s) saved to {out_dir}")
    print(f"Open this in a browser to review: {review_path}")


if __name__ == "__main__":
    main()
