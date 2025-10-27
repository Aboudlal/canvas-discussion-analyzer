#!/usr/bin/env python3
"""
parse_discussion_minimal.py

"""

import argparse
import re
import csv
from pathlib import Path

# The ONLY labels we want in the CSV
LABELS = [
    ("name",       r"Your\s+preferred\s+name\s*:"),
    ("activity_1",   r"Your\s+preferred\s+activity\s*1\s*:"),
    ("activity_2",   r"Your\s+preferred\s+activity\s*2\s*:"),
    ("activity_3",   r"Your\s+preferred\s+activity\s*3\s*:"),
    ("tool_not_now", r"Tool\s+YOU\s+don'?t\s+want\s+to\s+learn\s+now\s*:"),
]

# Anchor to detect each "block" (start of a post)
BLOCK_ANCHOR = re.compile(r"Your\s+preferred\s+name\s*:", re.IGNORECASE)

# --------- Cleanup of raw text BEFORE parsing ---------
def clean_raw_text(raw: str) -> str:
    txt = raw

    #1) Remove "Reply to post..." / "Mark as Unread..." (noise lines)
    txt = re.sub(r"(?im)^\s*(Reply to post.*|Mark as Unread.*)\s*$", "", txt)

    #2) Remove "Why does this tool appeal..." + answer
    txt = re.sub(
        r"Why\s+does\s+this\s+tool\s+appeal\s+to\s+YOU\s+for\s+business\s+intelligence\s*:.*?(?=(?:Your\s+preferred\s+name\s*:|Tool\s+YOU\s+don'?t\s+want\s+to\s+learn\s+now\s*:|$))",
        "",
        txt,
        flags=re.IGNORECASE | re.DOTALL,
    )

    #3) Remove "Why does this tool not seem..." + answer
    txt = re.sub(
        r"Why\s+does\s+this\s+tool\s+not\s+seem\s+as\s+important\s+for\s+YOU\s+to\s+learn\s+right\s+now\s*:.*?(?=(?:Your\s+preferred\s+name\s*:|Tool\s+YOU\s+don'?t\s+want\s+to\s+learn\s+now\s*:|$))",
        "",
        txt,
        flags=re.IGNORECASE | re.DOTALL,
    )

    #4) Delete "Tool YOU want to learn:" + answer until the next useful label
    txt = re.sub(
        r"Tool\s+YOU\s+want\s+to\s+learn\s*:.*?(?=(?:Tool\s+YOU\s+don'?t\s+want\s+to\s+learn\s+now\s*:|Your\s+preferred\s+name\s*:|$))",
        "",
        txt,
        flags=re.IGNORECASE | re.DOTALL,
    )

    #5) Compress multiple empty lines
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()

def _compile_label_patterns():
    return [(key, re.compile(pat, re.IGNORECASE)) for key, pat in LABELS]

def format_name(raw_name: str) -> str:

    parts = raw_name.strip().split()
    if len(parts) >= 2:
        return f"{parts[0]} {parts[1][0].upper()}"
    return parts[0] if parts else ""

def _extract_fields_from_block(text, label_patterns):
    results = {key: "" for key, _ in label_patterns}
    # Find the labels PRESENT in this block
    occurrences = []
    for key, rx in label_patterns:
        m = rx.search(text)
        if m:
            occurrences.append((m.start(), m.end(), key))
    occurrences.sort(key=lambda x: x[0])

    # Extract the value between this label and the next detected label
    for i, (start, end, key) in enumerate(occurrences):
        val_start = end
        val_end = occurrences[i+1][0] if i + 1 < len(occurrences) else len(text)
        val = text[val_start:val_end]
        val = re.sub(r"[ \t]+", " ", val.strip().strip("-").strip())
        if key == "prenom":
            val = format_name(val)
        results[key] = val
    return results

def parse_discussion_text(raw_text: str):
    cleaned = clean_raw_text(raw_text)
    label_patterns = _compile_label_patterns()

    anchors = list(BLOCK_ANCHOR.finditer(cleaned))
    if not anchors:
        return []

    blocks = []
    for i, m in enumerate(anchors):
        start = m.start()
        end = anchors[i+1].start() if i+1 < len(anchors) else len(cleaned)
        blocks.append(cleaned[start:end].strip())

    rows = [_extract_fields_from_block(b, label_patterns) for b in blocks]
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in",  dest="infile", required=True, help="Canvas discussion text file")
    ap.add_argument("--out", dest="outfile", required=True, help="CSV output file")
    args = ap.parse_args()

    raw = Path(args.infile).read_text(encoding="utf-8", errors="ignore")
    rows = parse_discussion_text(raw)

    fieldnames = [k for k, _ in LABELS]
    with open(args.outfile, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    print(f"Wrote {len(rows)} rows to {args.outfile}")

if __name__ == "__main__":
    main()
