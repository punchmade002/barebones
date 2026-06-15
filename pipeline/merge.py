"""Stage 8 — MERGE generated content into the live app.

Copies the generated, additive JS for a subject to the repo root and wires it into app.html so
the subject is immediately playable. It only ever ADDS additive globals
(`window.EXAM_QUESTIONS_DB.concat(...)`, `Object.assign(window.FLASHCARDS_DB, ...)`) loaded as
their own <script> tags — it never edits hand-curated files like exam-questions-db.js or the
*-content.js packs. Diagram PNGs are already under exam-images/<subject>/ from images.py.

Idempotent: re-running overwrites the two generated root files in place and never adds a
duplicate <script> tag.

    python3 merge.py chemistry
"""
from __future__ import annotations
import shutil
import sys
from pathlib import Path

from config import ROOT, CANONICAL

APP_HTML = ROOT / "app.html"
APP_TAG = "./app.js"                                   # new tags go immediately before this one


def _copy(subject: str) -> list[tuple[str, str]]:
    """Copy generated files to root as <subject>-*.js. Return [(root_filename, label)]."""
    plan = [
        (CANONICAL / f"exam-questions-db.{subject}.generated.js", f"{subject}-exam-questions.js", "exam questions"),
        (CANONICAL / f"flashcards-{subject}.generated.js",        f"{subject}-flashcards.js",     "flashcards"),
    ]
    done = []
    for src, dest_name, label in plan:
        if not src.exists():
            print(f"[merge] skip {label}: {src.name} not generated yet")
            continue
        shutil.copyfile(src, ROOT / dest_name)
        print(f"[merge] {src.name} -> {dest_name}")
        done.append((dest_name, label))
    return done


def _wire(files: list[tuple[str, str]]) -> int:
    if not APP_HTML.exists():
        print(f"[merge] no {APP_HTML.name}; copied files but did not wire script tags")
        return 0
    html = APP_HTML.read_text()
    added = 0
    for dest_name, _label in files:
        if f"./{dest_name}" in html:                  # matches with or without a ?v= query string
            continue                                  # already wired
        tag = f'    <script src="./{dest_name}?v=1"></script>\n'
        idx = html.find(f'<script src="{APP_TAG}')
        if idx == -1:
            html = html.rstrip() + "\n" + tag         # fallback: append at end
        else:
            line_start = html.rfind("\n", 0, idx) + 1
            html = html[:line_start] + tag + html[line_start:]
        added += 1
        print(f"[merge] wired <script> for {dest_name}")
    if added:
        APP_HTML.write_text(html)
    return added


def run(subject: str) -> None:
    files = _copy(subject)
    if not files:
        print("[merge] nothing to merge — run segment/flashcards first.")
        return
    added = _wire(files)
    print(f"\nMerged {subject}: {len(files)} file(s) at repo root, {added} new <script> tag(s) in app.html.")
    print("Open app.html and check the subject's exam + flashcards.")


if __name__ == "__main__":
    subj = next((a for a in sys.argv[1:] if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 merge.py <subject>")
    run(subj)
