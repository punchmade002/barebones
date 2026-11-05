#!/usr/bin/env python3
"""Validate authored subsection notes and compile them into a script the app loads.

Content agents write one JSON file per subsection to content/<subject>/<loId>.json, in the
format set out in course-outlines/NOTES_STANDARD.md. This script checks every file against the
standard and writes <subject>-notes.js, which attaches the notes, key terms, fact cards and any
practice questions to the matching learning outcome in COURSE_DATA.

    python3 scripts/build_notes.py geography          # validate + build
    python3 scripts/build_notes.py geography --check  # validate only

Tests pass --content DIR and --out FILE to build from fixtures without touching the app.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BANNED_PHRASES = (
    "these ideas should be used together",
    "it is important to note",
    "in conclusion",
    "this topic is frequently examined",
    "a complete answer should",
    "question focus:",
    "model content:",
)
MARKDOWN = re.compile(r"\*\*|__|^#|\n|`|\$(?!\d)|\$.*\$")  # the app renders $...$ as KaTeX maths; a lone $2.15 is fine
# Internal ids (chapter and outcome ids) mean nothing to students; refer to notes by name.
INTERNAL_IDS: set[str] = set()
# Ids look like geo-rivers-s2 or bio19-s2, so a token may contain digits before its first hyphen.
ID_TOKEN = re.compile(r"\b[a-z][a-z0-9]*(?:-[a-z0-9]+)+\b")
# Subjects whose chapter review outcome still carries the old hand-written notes and
# flashcards, mapped to that outcome's id suffix (biology <chapter>-1; PE <chapter>-core, built
# by pe-pipeline-content.js). When a chapter's authored notes arrive, those are cleared so the
# old content (which predates the current syllabus or outline) doesn't sit beside the new notes.
# The review outcome keeps its test questions.
RETIRE_REVIEW_NOTES = {"biology": "-1", "pe": "-core"}


def outcome_ids(subject: str) -> dict[str, str]:
    """Map each learning-outcome id in data.js for the subject to its chapter id."""
    text = (ROOT / "data.js").read_text()
    ids: dict[str, str] = {}
    chapter = None
    for line in text.splitlines():
        if f'subject: "{subject}"' in line:
            chapter = re.search(r'id: "([^"]+)"', line).group(1)
            continue
        if chapter and re.search(r'subject: "', line):
            chapter = None
        if chapter:
            for lo in re.findall(r'\{ id: "([^"]+)", code:', line):
                ids[lo] = chapter
    return ids


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def plain(value, where: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{where}: must be non-empty text")
        return
    if MARKDOWN.search(value):
        errors.append(f"{where}: contains markdown or a line break")
    for token in ID_TOKEN.findall(value):
        if token in INTERNAL_IDS:
            errors.append(f"{where}: contains the internal id {token!r}; name the notes instead")
    low = value.lower()
    for phrase in BANNED_PHRASES:
        # Whole phrases only: "in conclusions" (in the spec's definition of evaluate) isn't filler.
        if re.search(re.escape(phrase) + r"(?!\w)", low):
            errors.append(f'{where}: contains filler "{phrase}"')


def validate(path: Path, los: dict[str, str]) -> tuple[dict | None, list[str]]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        return None, [f"{path.name}: invalid JSON ({exc})"]
    lo_id = data.get("loId")
    if lo_id != path.stem:
        errors.append(f"{path.name}: loId must equal the file name ({path.stem})")
    if lo_id not in los:
        errors.append(f"{path.name}: loId {lo_id!r} is not a learning outcome in data.js")
    elif not re.search(r"-s\d+$", lo_id):
        errors.append(f"{path.name}: write notes for subsections (-s1, -s2, ...), not the chapter review outcome")
    if lo_id in los and data.get("chapterId") != los[lo_id]:
        errors.append(f"{path.name}: chapterId must be {los.get(lo_id)!r}")

    notes = data.get("notes")
    if not isinstance(notes, list) or not notes:
        errors.append(f"{path.name}: notes must be a non-empty list")
        notes = []
    seen: dict[str, str] = {}
    for i, block in enumerate(notes):
        where = f"{path.name} notes[{i}]"
        if not isinstance(block, dict):
            errors.append(f"{where}: must be an object")
            continue
        plain(block.get("h"), f"{where}.h", errors)
        points = block.get("points", [])
        if "b" in block:
            plain(block["b"], f"{where}.b", errors)
        if not isinstance(points, list):
            errors.append(f"{where}.points: must be a list")
            points = []
        if not block.get("b") and not points:
            errors.append(f"{where}: needs a lead (b) or points")
        for j, point in enumerate(points):
            plain(point, f"{where}.points[{j}]", errors)
            if isinstance(point, str):
                key = norm(point)
                if key in seen:
                    errors.append(f"{where}.points[{j}]: repeats {seen[key]}")
                seen[key] = f"notes[{i}].points[{j}]"

    terms = data.get("keyTerms", [])
    if not isinstance(terms, list) or not terms:
        errors.append(f"{path.name}: keyTerms must be a non-empty list")
        terms = []
    for i, term in enumerate(terms):
        where = f"{path.name} keyTerms[{i}]"
        if not isinstance(term, dict):
            errors.append(f"{where}: must be an object")
            continue
        plain(term.get("term"), f"{where}.term", errors)
        plain(term.get("definition"), f"{where}.definition", errors)

    # Fact cards (optional) test case-study facts, formation stages and named examples. They
    # are shown after the key terms, so existing flashcard ids and progress stay put.
    fronts = {norm(t["term"]) for t in terms if isinstance(t, dict) and isinstance(t.get("term"), str)}
    facts = data.get("factCards", [])
    if not isinstance(facts, list):
        errors.append(f"{path.name}: factCards must be a list")
        facts = []
    for i, card in enumerate(facts):
        where = f"{path.name} factCards[{i}]"
        if not isinstance(card, dict):
            errors.append(f"{where}: must be an object")
            continue
        plain(card.get("term"), f"{where}.term", errors)
        plain(card.get("definition"), f"{where}.definition", errors)
        if isinstance(card.get("term"), str):
            key = norm(card["term"])
            if key in fronts:
                errors.append(f"{where}.term: repeats another card ({card['term']!r})")
            fronts.add(key)

    for i, question in enumerate(data.get("questions", [])):
        where = f"{path.name} questions[{i}]"
        if not isinstance(question, dict):
            errors.append(f"{where}: must be an object")
            continue
        if not isinstance(question.get("marks"), int) or question["marks"] <= 0:
            errors.append(f"{where}.marks: must be a positive integer")
        plain(question.get("prompt"), f"{where}.prompt", errors)
        plain(question.get("model"), f"{where}.model", errors)

    return data, errors


def build(subject: str, check_only: bool, folder: Path | None = None, out: Path | None = None) -> int:
    los = outcome_ids(subject)
    if not los:
        print(f"No learning outcomes found for subject {subject!r} in data.js")
        return 1
    INTERNAL_IDS.update(los)
    INTERNAL_IDS.update(los.values())
    folder = folder or ROOT / "content" / subject
    files = sorted(folder.glob("*.json")) if folder.is_dir() else []
    entries: dict[str, dict] = {}
    errors: list[str] = []
    for path in files:
        data, file_errors = validate(path, los)
        errors.extend(file_errors)
        if data is not None and not file_errors:
            entries[data["loId"]] = {
                "notes": data["notes"],
                "keyTerms": [
                    {"term": t["term"], "definition": t["definition"]}
                    for t in data["keyTerms"] + data.get("factCards", [])
                ],
                "questions": [
                    {"type": "short", "marks": q["marks"], "prompt": q["prompt"], "model": q["model"]}
                    for q in data.get("questions", [])
                ],
            }

    # A chapter switches from the generated notes to authored notes as a whole, so warn
    # about chapters where only some subsections have been written.
    by_chapter: dict[str, list[str]] = {}
    for lo, chapter in los.items():
        if re.search(r"-s\d+$", lo):
            by_chapter.setdefault(chapter, []).append(lo)
    warnings = []
    for chapter, subsections in by_chapter.items():
        done = [lo for lo in subsections if lo in entries]
        if done and len(done) < len(subsections):
            missing = ", ".join(lo for lo in subsections if lo not in entries)
            warnings.append(f"{chapter}: {len(done)}/{len(subsections)} subsections written (missing {missing})")

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")
    complete = sum(
        1 for subs in by_chapter.values() if subs and all(lo in entries for lo in subs)
    )
    print(
        f"{subject}: {len(entries)}/{len(files)} file(s) valid; "
        f"{len(entries)}/{sum(len(s) for s in by_chapter.values())} subsections written; "
        f"{complete}/{len(by_chapter)} chapters complete"
    )
    if errors:
        return 1
    if check_only:
        return 0

    payload = json.dumps(entries, ensure_ascii=False, indent=1, sort_keys=True)
    out = out or ROOT / f"{subject}-notes.js"
    out.write_text(
        f"// Generated by scripts/build_notes.py from content/{subject}/*.json. Do not edit by hand.\n"
        "// Attaches authored subsection notes, key terms and practice questions to COURSE_DATA.\n"
        "(function () {\n"
        '  if (typeof COURSE_DATA === "undefined") return;\n'
        f"  var NOTES = {payload};\n"
        "  COURSE_DATA.chapters.forEach(function (chapter) {\n"
        "    (chapter.learningOutcomes || []).forEach(function (outcome) {\n"
        "      var entry = NOTES[outcome.id];\n"
        "      if (!entry) return;\n"
        "      outcome.notes = entry.notes;\n"
        "      outcome.keyTerms = entry.keyTerms.map(function (term) {\n"
        "        return { term: term.term, definition: term.definition, section: outcome.title };\n"
        "      });\n"
        "      outcome.questions = (outcome.questions || []).concat(entry.questions);\n"
        "      outcome.authored = true;\n"
        "    });\n"
        + (
            "    var review = (chapter.learningOutcomes || []).find(function (outcome) {\n"
            f"      return outcome.id === chapter.id + \"{RETIRE_REVIEW_NOTES.get(subject, '')}\";\n"
            "    });\n"
            "    if (review && (chapter.learningOutcomes || []).some(function (outcome) { return outcome.authored; })) {\n"
            "      review.notes = [];\n"
            "      review.keyTerms = [];\n"
            "    }\n"
            if subject in RETIRE_REVIEW_NOTES else ""
        )
        + "  });\n"
        "})();\n"
    )
    print(f"wrote {out}")
    return 0


def option(name: str) -> Path | None:
    if name in sys.argv:
        return Path(sys.argv[sys.argv.index(name) + 1]).resolve()
    return None


if __name__ == "__main__":
    argv = sys.argv[1:]
    args = [a for i, a in enumerate(argv) if not a.startswith("-") and (i == 0 or argv[i - 1] not in ("--content", "--out"))]
    if len(args) != 1:
        raise SystemExit("usage: python3 scripts/build_notes.py <subject> [--check] [--content DIR] [--out FILE]")
    sys.exit(build(args[0], "--check" in argv, option("--content"), option("--out")))
