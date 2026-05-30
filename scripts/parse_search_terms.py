#!/usr/bin/env python3
"""Parse Search Terms CSVs and output candidate negative keywords.

Simple heuristics used:
- Terms with clicks == 0 and impressions >= 2 and containing informational trigger words ('how', 'can', 'why', 'tutorial', 'diy', 'cheap', 'free') are flagged.
- Terms containing obvious DIY phrases ("how to", "pour hot water", "diy") are flagged.

Usage:
  python3 scripts/parse_search_terms.py path/to/Searches.csv

Outputs a `reports/candidate_negatives.txt` file with one candidate per line.
"""
import csv
import sys
from pathlib import Path

INFO_TRIGGERS = ["how", "how to", "can", "why", "tutorial", "diy", "cheap", "free", "pour hot water", "easiest way", "how do i"]


def suggest_negatives(csv_path: Path, out_path: Path):
    candidates = set()
    with csv_path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            term = row.get('Search', row.get('Search term', '')).strip().lower()
            try:
                clicks = float(row.get('Clicks', '0').replace(',', '').strip() or 0)
                impressions = float(row.get('Impressions', '0').replace(',', '').strip() or 0)
            except Exception:
                clicks = 0
                impressions = 0

            if clicks == 0 and impressions >= 2:
                for trig in INFO_TRIGGERS:
                    if trig in term:
                        candidates.add(term)
                        break

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('w', encoding='utf-8') as f:
        for c in sorted(candidates):
            f.write(c + '\n')

    print(f"Wrote {len(candidates)} candidate negatives to {out_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/parse_search_terms.py path/to/Searches.csv")
        sys.exit(2)
    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        sys.exit(2)
    out_path = Path('services/google-ads/reports/candidate_negatives.txt')
    suggest_negatives(csv_path, out_path)


if __name__ == '__main__':
    main()
