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
import re
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
        # The exam-breakdown entry is additive too: it assigns into window.EXAM_BREAKDOWN rather
        # than replacing it, so it sits alongside the hand-written entries in exam-breakdown.js.
        (CANONICAL / f"exam-breakdown-{subject}.generated.js",    f"{subject}-exam-breakdown.js", "exam breakdown"),
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
        # Already wired: the FILE was just overwritten, so the ?v= must move or every returning
        # user keeps the cached previous build. Bump it rather than skipping.
        existing = re.search(rf'(\./{re.escape(dest_name)})\?v=(\d+)', html)
        if existing:
            html = html.replace(existing.group(0), f"{existing.group(1)}?v={int(existing.group(2)) + 1}")
            APP_HTML.write_text(html)
            print(f"[merge] {dest_name} cache-buster -> v={int(existing.group(2)) + 1}")
            continue
        if f"./{dest_name}" in html:                  # wired, but with no ?v= to bump
            continue
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
    """Auto-publish-if-clean pre-flight. Returns human-readable failure reasons (empty == clean).

    The checks themselves live in gate.py, which also reports WARN/INFO findings a human should
    read but which must not block publishing. `python3 gate.py <subject>` prints the full report.
    """
    import gate as gate_mod
    return gate_mod.blockers(subject)


def run(subject: str, force: bool = False) -> bool:
    """Merge generated content into the app. Returns True iff it actually published. A failing
    gate blocks publishing unless force=True (the deliberate human override)."""
    import gate as gate_mod
    findings = gate_mod.run(subject)
    fails = [f.message for f in findings if f.severity == gate_mod.BLOCK]
    # WARN findings never block, but publishing without showing them is how 158 duplicate
    # flashcards shipped unnoticed — print them either way.
    warns = [f.message for f in findings if f.severity == gate_mod.WARN]
    if warns:
        print(f"[merge] {len(warns)} warning(s) — not blocking:")
        for w in warns:
            print(f"  ! {w}")
    if fails:
        head = "[merge] gate failures OVERRIDDEN by --force:" if force else \
               "[merge] BLOCKED — fix these or re-run with --force:"
        print(head)
        for f in fails:
            print(f"  - {f}")
        print(f"  (full report: python3 gate.py {subject})")
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
