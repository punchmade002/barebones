"""Stage 1 — ACQUIRE. Download every paper + marking scheme PDF, build a manifest.

The SEC archive at https://www.examinations.ie/exammaterialarchive/ is a form:
    Papers vs Marking Scheme -> year -> exam (LC/JC) -> subject -> level -> language
The resulting PDFs live at predictable archive paths once you observe the pattern.

Two strategies (pick one):
  (A) FORM-DRIVEN  — drive the form with Playwright, capture the PDF URLs it produces,
      download them. Robust to markup changes. Best first run to *discover* the codes.
  (B) DIRECT PATH  — once you know the code pattern, enumerate URLs directly (fast).

This file implements (B) with a discovery hook for (A). Fill SUBJECTS[...]["code"] in
config.py from a single form run, then this enumerates everything.

Idempotent: a PDF already on disk is skipped. Manifest is the source of truth for stage 2.
"""
from __future__ import annotations
import csv
import time
import urllib.request
from pathlib import Path

from config import RAW, REPORTS, YEARS, LEVELS, SUBJECTS, USER_AGENT, REQUEST_DELAY_S

ARCHIVE = "https://www.examinations.ie/archive"
MANIFEST = REPORTS / "manifest.csv"


def archive_url(kind: str, year: int, code: str, level: str, paper: int) -> str:
    """Build a candidate PDF URL. `kind` is 'exampapers' or 'markingschemes'.

    NOTE: the real filename encodes exam/subject/level/paper/language. Replace the
    f-string below with the exact pattern you observe in the archive's network tab.
    Keeping it in one function means you fix the pattern once.
    """
    fname = f"LC{code}{level}P{paper}00EV.pdf"          # <-- adjust to observed pattern
    return f"{ARCHIVE}/{kind}/{year}/{fname}"


def download(url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        return True                                    # cached — idempotent
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status != 200 or "pdf" not in r.headers.get("Content-Type", ""):
                return False
            dest.write_bytes(r.read())
        time.sleep(REQUEST_DELAY_S)                    # be polite to the archive
        return True
    except Exception as e:                             # noqa: BLE001 — log and move on
        print(f"  miss {url} ({e})")
        return False


def run(subjects: list[str] | None = None) -> None:
    subjects = subjects or list(SUBJECTS)
    rows: list[dict] = []
    for subj in subjects:
        cfg = SUBJECTS[subj]
        if "?" in cfg["code"]:
            print(f"[skip] {subj}: set its SEC code in config.py first")
            continue
        for year in YEARS:
            for level in LEVELS:
                for paper in range(1, cfg["papers"] + 1):
                    for kind in ("exampapers", "markingschemes"):
                        url = archive_url(kind, year, cfg["code"], level, paper)
                        dest = RAW / subj / f"{year}-{level}-P{paper}-{kind}.pdf"
                        ok = download(url, dest)
                        print(f"[{'ok ' if ok else '-- '}] {dest.name}")
                        rows.append({
                            "subject": subj, "year": year, "level": level,
                            "paper": paper, "kind": kind,
                            "path": str(dest), "downloaded": ok,
                        })
    with MANIFEST.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else
                           ["subject", "year", "level", "paper", "kind", "path", "downloaded"])
        w.writeheader()
        w.writerows(rows)
    got = sum(r["downloaded"] for r in rows)
    print(f"\nManifest: {MANIFEST}  ({got}/{len(rows)} PDFs on disk)")


if __name__ == "__main__":
    import sys
    run(sys.argv[1:] or None)
