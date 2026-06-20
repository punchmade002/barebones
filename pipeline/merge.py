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
import json
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


def gate(subject: str) -> list[str]:
    """Auto-publish-if-clean pre-flight. Returns human-readable failure reasons (empty == clean):
      * any placeholder/empty part still in the store (segment should have dropped these),
      * more than 40% of answers being ai-h1 (a symptom of upstream segmentation failure),
      * any question attributed to a year no paper was acquired for (fabricated years)."""
    import validate
    cpath = CANONICAL / f"{subject}.json"
    if not cpath.exists():
        return [f"no canonical store ({cpath.name}) — run segment first"]
    canon = json.loads(cpath.read_text())
    parts = [(q, p) for q in canon for p in q.get("parts", [])]
    bad = [(q["id"], validate.part_problems(p)) for q, p in parts if validate.part_problems(p)]
    ai = sum(1 for _, p in parts if p.get("model_source") == "ai-h1") / max(len(parts), 1)
    fab_years = sorted({q.get("year") for q in canon
                        if not validate.year_is_real(subject, q.get("year"))})
    fails = []
    if bad:
        eg = f" (e.g. {bad[0][0]}: {','.join(bad[0][1])})"
        fails.append(f"{len(bad)} placeholder/empty part(s){eg}")
    if ai > 0.40:
        fails.append(f"{ai:.0%} of answers are ai-h1 (>40% cap)")
    if fab_years:
        fails.append(f"questions from non-acquired year(s): {fab_years}")
    return fails


def run(subject: str, force: bool = False) -> bool:
    """Merge generated content into the app. Returns True iff it actually published. A failing
    gate blocks publishing unless force=True (the deliberate human override)."""
    fails = gate(subject)
    if fails:
        head = "[merge] gate failures OVERRIDDEN by --force:" if force else \
               "[merge] BLOCKED — fix these or re-run with --force:"
        print(head)
        for f in fails:
            print(f"  - {f}")
        if not force:
            return False
    files = _copy(subject)
    if not files:
        print("[merge] nothing to merge — run segment/flashcards first.")
        return False
    added = _wire(files)
    print(f"\nMerged {subject}: {len(files)} file(s) at repo root, {added} new <script> tag(s) in app.html.")
    print("Open app.html and check the subject's exam + flashcards.")
    return True


if __name__ == "__main__":
    subj = next((a for a in sys.argv[1:] if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 merge.py <subject> [--force]")
    run(subj, force=("--force" in sys.argv[1:]))
