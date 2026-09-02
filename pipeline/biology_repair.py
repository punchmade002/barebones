"""Surgical backfill for the hand-curated Biology exam bank.

The ordinary pipeline intentionally never edits ``exam-questions-db.js``.  Biology predates the
generated pipeline, however, so its 24 curated questions had no canonical store and could not
reach the scheme/answer stages.  This adapter imports just those rows, adds four question pages
verified against the official PDFs, canonicalises their source-page images, and exports the
backfilled answers into the same curated block.

It never runs segmentation, image detection, flashcards, validation cleanup, or additive merge.

    python3 biology_repair.py import
    python3 schemes.py biology              # worker, then collect
    python3 model_answers.py biology         # only remaining blanks
    python3 biology_repair.py export
    python3 biology_repair.py archive-images
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

from config import CANONICAL, DIGEST, EXAM_IMAGES, REPORTS, ROOT

SUBJECT = "biology"
DB_PATH = ROOT / "exam-questions-db.js"
SCAFFOLD_PATH = ROOT / "pipeline" / "scaffold" / "biology.json"
IMAGE_DIR = EXAM_IMAGES / SUBJECT
ARCHIVE_DIR = ROOT / "pipeline" / "_data" / "archive" / "biology-images-legacy"
CURATED_BASELINE = ROOT / "pipeline" / "_data" / "archive" / "biology-curated-baseline.json"
DUPLICATE_REPORT = REPORTS / "biology-duplicate-audit.json"


ORPHAN_QUESTIONS = [
    {
        "id": "biology-pp-2015-A-q6",
        "subject": SUBJECT,
        "chapterId": "bio21",
        "sectionId": "bio-sectionA",
        "source": "LC Biology Higher 2015 — A — Q6 [LEGACY — pre-2027 syllabus]",
        "year": 2015,
        "level": "higher",
        "paper": "",
        "legacy_image": "2015-A-Q1.png",
        "parts": [
            {"label": "(a)", "question": "The diagram shows a vertical section through human skin. Place an X on the adipose tissue.", "marks": 8, "model": "", "diagram": ""},
            {"label": "(b)", "question": "The diagram shows a vertical section through human skin. Name A and B.", "marks": 7, "model": "", "diagram": ""},
            {"label": "(c)", "question": "Define each of the following words and explain how each process keeps the human body warm.\n(i) Piloerection.\n(ii) Vasoconstriction.", "marks": 5, "model": "", "diagram": ""},
        ],
    },
    {
        "id": "biology-pp-2015-C-q11",
        "subject": SUBJECT,
        "chapterId": "bio27",
        "sectionId": "bio-sectionC",
        "source": "LC Biology Higher 2015 — C — Q11 [LEGACY — pre-2027 syllabus]",
        "year": 2015,
        "level": "higher",
        "paper": "",
        "legacy_image": "2015-A-Q2.png",
        "parts": [
            {"label": "(a)", "question": "(i) Humans are heterotrophic and omnivorous. Explain each of these terms.\n(ii) What is meant by a balanced diet?", "marks": 9, "model": "", "diagram": ""},
            {"label": "(b)", "question": "(i) Draw a large diagram of the human alimentary canal and its associated glands. On your diagram label all of the following:\n1. Two associated glands. Name each gland labelled and put the letter G in brackets after each name to indicate it is a gland.\n2. Two parts of the small intestine. Name each part labelled and put the letter S in brackets after each name to indicate it is part of the small intestine.\n3. Two parts of the large intestine. Name each part labelled and put the letter L in brackets after each name to indicate it is part of the large intestine.\n(ii) Answer the following questions in relation to lipase.\n1. What is lipase?\n2. Give one part of the alimentary canal that secretes lipase.\n3. What is the approximate pH at the site of lipase action?", "marks": 27, "model": "", "diagram": ""},
            {"label": "(c)", "question": "(i) 1. Write the dental formula for an adult human with a full set of teeth.\n2. Give one difference between that dental formula and the tooth arrangement of the mammal in the photograph.\n3. What type of food do you think is mainly consumed by the mammal in the photograph? Explain your answer.\n(ii) Give two functions of the large intestine.\n(iii) Outline two beneficial functions of the bacteria that live in the digestive tract.", "marks": 24, "model": "", "diagram": ""},
        ],
    },
    {
        "id": "biology-pp-2016-C-q15",
        "subject": SUBJECT,
        "chapterId": "bio29",
        "sectionId": "bio-sectionC",
        "source": "LC Biology Higher 2016 — C — Q15 [LEGACY — pre-2027 syllabus]",
        "year": 2016,
        "level": "higher",
        "paper": "",
        "legacy_image": "2016-A-Q1.png",
        "parts": [
            {"label": "(a)", "question": "(i) Draw a labelled diagram of a transverse section and a labelled diagram of a longitudinal section through a human vein to show its structure.\n(ii) In each case name a vein which fits the description.\n1. Transports blood out of the muscle of the heart.\n2. Brings blood away from the kidneys.\n3. Carries very little carbon dioxide.\n4. Brings blood into the right atrium.\n5. Has capillaries at both ends.\n(iii) Briefly describe how blood is moved through veins.", "marks": 30, "model": "", "diagram": ""},
            {"label": "(b)", "question": "Answer the following questions in relation to the typical human female menstrual cycle.\n(i) State one change that occurs, and the approximate day(s) of the cycle on which it occurs, in: 1. the endometrium; 2. the ovary.\n(ii) FSH and LH each plays a role in the cycle. Where in the body are these hormones produced?\n(iii) State one role of each of these hormones in the cycle.\n(iv) Name two other hormones that play a role in the cycle.\n(v) Stating clearly which hormone you have chosen from (iv), give a function of that hormone in the cycle.", "marks": 30, "model": "", "diagram": ""},
            {"label": "(c)", "question": "(i) Long bones contain both yellow marrow and red marrow. Give one function of each type of marrow.\n(ii) Diseases in humans occur for a number of different reasons. In each case explain how the presence of a named disease may be recognised.\n1. A dietary deficiency of a named water-soluble vitamin.\n2. A genetically sex-linked disease, other than haemophilia.\n3. Excessive secretion of a named hormone.\n4. Caused by a virus.\n(iii) Explain the biological basis of each of the following.\n1. The use of micro-organisms in waste management.\n2. Vaccination.\n3. The artificial propagation of flowering plants.\n4. Increasing the amount of wholegrain foods in the diet.", "marks": 30, "model": "", "diagram": ""},
        ],
    },
    {
        "id": "biology-pp-2017-B-q8",
        "subject": SUBJECT,
        "chapterId": "bio13",
        "sectionId": "bio-sectionB",
        "source": "LC Biology Higher 2017 — B — Q8 [LEGACY — pre-2027 syllabus]",
        "year": 2017,
        "level": "higher",
        "paper": "",
        "legacy_image": "2017-A-Q1.png",
        "parts": [
            {"label": "(a)", "question": "Answer the following in relation to enzymes.\n(i) Give a factor, other than pH, which affects enzyme activity.\n(ii) Explain the term optimum activity.", "marks": 6, "model": "", "diagram": ""},
            {"label": "(b)", "question": "Answer the following in relation to an investigation you carried out into the effect of pH on the rate of enzyme activity.\n(i) Name the enzyme that you used in this investigation.\n(ii) State: 1. The source of this enzyme. 2. The substrate of this enzyme.\n(iii) Explain why changing the pH would have an effect on enzyme activity.\n(iv) How did you measure the rate of enzyme activity?\n(v) Label the axes and sketch a graph to show the effect of pH on enzyme activity.", "marks": 24, "model": "", "diagram": ""},
        ],
    },
]


def _block_bounds(text: str) -> tuple[int, int]:
    start = text.index("  // ── BIOLOGY")
    # Biology used to be followed by PE, but curated subjects can move out to additive files.
    # Bound it by the next subject divider instead of coupling this adapter to one neighbour.
    next_divider = re.search(r"(?m)^  // ── (?!BIOLOGY)[^\n]+$", text[start + 1:])
    if next_divider:
        end = start + 1 + next_divider.start()
    else:
        end = text.index("\n\n];", start)
    return start, end


def _object_literals(block: str) -> list[str]:
    out: list[str] = []
    start = None
    depth = 0
    quote = None
    escaped = False
    for i, ch in enumerate(block):
        if quote:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}" and depth:
            depth -= 1
            if depth == 0 and start is not None:
                out.append(block[start:i + 1])
                start = None
    return out


def _parse_literal(raw: str) -> dict:
    quoted = re.sub(r"(?m)^(\s*)([A-Za-z_$][\w$]*)(\s*:)", r'\1"\2"\3', raw)
    quoted = re.sub(r",\s*([}\]])", r"\1", quoted)
    return json.loads(quoted)


def load_curated() -> list[dict]:
    text = DB_PATH.read_text()
    start, end = _block_bounds(text)
    rows = [_parse_literal(raw) for raw in _object_literals(text[start:end])]
    return [q for q in rows if q.get("subject") == SUBJECT]


def _normalise_source(source: str) -> str:
    source = re.sub(r"^LC Biology HL\b", "LC Biology Higher", source)
    source = source.replace(" [⚠ may not match current course]", "")
    return source + (" [LEGACY — pre-2027 syllabus]" if "[LEGACY" not in source else "")


def _question_number(q: dict) -> int | None:
    """Return the printed exam question number, independent of PDF component/section.

    The archive calls the post-2018 Sections A/B booklet ``paper A`` even though the printed
    question numbers continue into the separately stored Section C paper.  Year + level + printed
    number is therefore the stable exam identity; the archive component is not.
    """
    label = str(q.get("label") or "").strip()
    labelled = re.match(r"(?i)^(?:question|q)?\s*(\d{1,2})(?:\D.*)?$", label)
    if labelled:
        return int(labelled.group(1))
    for value in (q.get("source"), q.get("id")):
        matches = re.findall(r"(?i)(?:^|[^a-z0-9])q\s*(\d{1,2})(?:[^0-9]|$)", str(value or ""))
        if matches:
            return int(matches[-1])
    return None


def _level(q: dict) -> str:
    explicit = str(q.get("level") or "").strip().lower()
    if explicit in {"higher", "ordinary"}:
        return explicit
    source = str(q.get("source") or "").lower()
    if "higher" in source or re.search(r"\bhl\b", source):
        return "higher"
    if "ordinary" in source or re.search(r"\bol\b", source):
        return "ordinary"
    return ""


def exam_identity(q: dict) -> tuple[int, str, int] | None:
    number = _question_number(q)
    try:
        year = int(q.get("year"))
    except (TypeError, ValueError):
        return None
    level = _level(q)
    return (year, level, number) if level and number is not None else None


def _question_text(q: dict) -> str:
    return "\n".join(str(p.get("question") or "") for p in q.get("parts", []))


def _text_signature(q: dict) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", _question_text(q).lower())).strip()


def _row_quality(q: dict) -> tuple[int, int, int]:
    parts = q.get("parts", [])
    return (sum(bool(str(p.get("question") or "").strip()) for p in parts),
            sum(len(str(p.get("question") or "")) for p in parts),
            sum(int(p.get("marks") or 0) > 0 for p in parts))


def reconcile_rows(generated: list[dict], curated_rows: list[dict]) -> tuple[list[dict], dict]:
    """Keep curated exam identities and return a duplicate-free additive expansion bank."""
    curated_identities = {identity for q in curated_rows if (identity := exam_identity(q))}
    curated_signatures = {sig for q in curated_rows if (sig := _text_signature(q))}
    missing_identity = [q.get("id", "") for q in generated if not exam_identity(q)]
    if missing_identity:
        raise ValueError(f"{len(missing_identity)} generated Biology row(s) have no exam identity: "
                         f"{missing_identity[:5]}")

    identity_groups: dict[tuple[int, str, int], list[dict]] = defaultdict(list)
    dropped_curated_identity = 0
    dropped_curated_text = 0
    for q in generated:
        q["source"] = _normalise_source(str(q.get("source") or ""))
        identity = exam_identity(q)
        signature = _text_signature(q)
        if identity in curated_identities:
            dropped_curated_identity += 1
            continue
        if signature and signature in curated_signatures:
            dropped_curated_text += 1
            continue
        identity_groups[identity].append(q)

    identity_collisions = {str(k): [q.get("id", "") for q in v]
                           for k, v in identity_groups.items() if len(v) > 1}
    selected = [max(group, key=_row_quality) for group in identity_groups.values()]

    # Exact whole-question repeats add no practice value.  Curated rows already won above; among
    # generated rows retain the richer extraction, with Higher Level as the deterministic tie-break.
    text_groups: dict[str, list[dict]] = defaultdict(list)
    for q in selected:
        text_groups[_text_signature(q)].append(q)
    exact_groups = {sig: rows for sig, rows in text_groups.items() if sig and len(rows) > 1}
    exact_dropped = 0
    kept: list[dict] = []
    for signature, rows in text_groups.items():
        if not signature:
            kept.extend(rows)
            continue
        winner = max(rows, key=lambda q: (_row_quality(q), _level(q) == "higher", int(q["year"])))
        kept.append(winner)
        exact_dropped += len(rows) - 1

    kept.sort(key=lambda q: (int(q["year"]), _level(q), _question_number(q) or 0))
    report = {
        "generated_before": len(generated),
        "curated_questions": len(curated_rows),
        "dropped_curated_identity": dropped_curated_identity,
        "dropped_curated_text": dropped_curated_text,
        "generated_identity_collisions": identity_collisions,
        "dropped_generated_identity_duplicates": sum(len(v) - 1 for v in identity_groups.values()),
        "dropped_generated_exact_text_duplicates": exact_dropped,
        "generated_after": len(kept),
    }
    return kept, report


def audit_rows(rows: list[dict], near_threshold: float = 0.965) -> dict:
    """Audit true identity/ID duplicates and exact or very-near whole-question repeats."""
    by_id: dict[str, list[dict]] = defaultdict(list)
    by_identity: dict[tuple, list[dict]] = defaultdict(list)
    by_text: dict[str, list[dict]] = defaultdict(list)
    for q in rows:
        by_id[str(q.get("id") or "")].append(q)
        by_identity[exam_identity(q)].append(q)
        by_text[_text_signature(q)].append(q)
    id_duplicates = {k: [q.get("source", "") for q in v] for k, v in by_id.items()
                     if k and len(v) > 1}
    identity_duplicates = {str(k): [q.get("id", "") for q in v]
                           for k, v in by_identity.items() if k and len(v) > 1}
    exact_duplicates = {sig[:160]: [q.get("id", "") for q in v]
                        for sig, v in by_text.items() if sig and len(v) > 1}

    # Keep the fuzzy check conservative and whole-question only.  Short definitions naturally
    # recur between levels; requiring 100 normalized characters avoids noisy false positives.
    candidates = [(q, _text_signature(q)) for q in rows if len(_text_signature(q)) >= 100]
    near = []
    for i, (left, ltext) in enumerate(candidates):
        for right, rtext in candidates[i + 1:]:
            if exam_identity(left) == exam_identity(right):
                continue
            if abs(len(ltext) - len(rtext)) > max(len(ltext), len(rtext)) * 0.12:
                continue
            ratio = SequenceMatcher(None, ltext, rtext, autojunk=False).ratio()
            if ratio >= near_threshold:
                near.append({"left": left.get("id", ""), "right": right.get("id", ""),
                             "similarity": round(ratio, 4)})
    return {
        "questions": len(rows),
        "parts": sum(len(q.get("parts", [])) for q in rows),
        "duplicate_ids": id_duplicates,
        "duplicate_exam_identities": identity_duplicates,
        "exact_whole_question_duplicates": exact_duplicates,
        "near_whole_question_duplicates": near,
        "clean": not id_duplicates and not identity_duplicates and not exact_duplicates and not near,
    }


def _canonical_image(q: dict, legacy_name: str) -> str:
    source = IMAGE_DIR / legacy_name
    if not source.exists():
        raise SystemExit(f"Missing Biology source image: {source}")
    dest = IMAGE_DIR / f"{q['id']}.png"
    if not dest.exists():
        shutil.copy2(source, dest)
    elif hashlib.sha256(dest.read_bytes()).digest() != hashlib.sha256(source.read_bytes()).digest():
        raise SystemExit(f"Refusing to overwrite non-identical canonical image: {dest}")
    return f"exam-images/biology/{dest.name}"


def _build_scaffold(rows: list[dict]) -> None:
    data = (ROOT / "data.js").read_text()
    chapters = [
        {"id": cid, "title": title}
        for cid, title in re.findall(
            r'id:\s*"(bio\d+)",\s*number:\s*\d+,\s*subject:\s*"biology",\s*title:\s*"([^"]+)"',
            data,
        )
    ]
    known = {c["id"] for c in chapters}
    for q in rows:
        if q["chapterId"] not in known:
            chapters.append({"id": q["chapterId"], "title": q["chapterId"].replace("bio-", "").replace("-", " ").title()})
            known.add(q["chapterId"])
    scaffold = {
        "subject": SUBJECT,
        "field": "Leaving Certificate Biology — Higher Level",
        "note": "Built deterministically from the app's existing Biology chapters for curated answer backfill.",
        "sections": [
            {"id": "bio-sectionA", "title": "Section A"},
            {"id": "bio-sectionB", "title": "Section B"},
            {"id": "bio-sectionC", "title": "Section C"},
        ],
        "chapters": chapters,
    }
    SCAFFOLD_PATH.write_text(json.dumps(scaffold, ensure_ascii=False, indent=2) + "\n")


def import_curated() -> list[dict]:
    rows = load_curated()
    if len(rows) not in {24, 28}:
        raise SystemExit(f"Expected 24 pre-repair or 28 repaired Biology rows, found {len(rows)}")
    by_id = {q["id"]: q for q in rows}
    for orphan in ORPHAN_QUESTIONS:
        if orphan["id"] not in by_id:
            q = json.loads(json.dumps(orphan, ensure_ascii=False))
            rows.append(q)
            by_id[q["id"]] = q
    for q in rows:
        q["level"] = "higher"
        q.setdefault("paper", "")
        q["source"] = _normalise_source(q["source"])
        legacy = q.pop("legacy_image", None)
        if not legacy:
            legacy = next((Path(p.get("diagram", "")).name for p in q["parts"] if p.get("diagram")), None)
        if not legacy:
            raise SystemExit(f"No source-page image recorded for {q['id']}")
        path = _canonical_image(q, legacy)
        attached = False
        for part in q["parts"]:
            if part.get("diagram") and not attached:
                part["diagram"] = path
                attached = True
            elif part.get("diagram"):
                part["diagram"] = ""
        if not attached:
            q["parts"][0]["diagram"] = path
    rows.sort(key=lambda q: (q["year"], q["id"]))
    if len({q["id"] for q in rows}) != len(rows):
        raise SystemExit("Duplicate Biology question id after import")
    CANONICAL.mkdir(parents=True, exist_ok=True)
    cpath = CANONICAL / "biology.json"
    cpath.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    _build_scaffold(rows)
    parts = sum(len(q["parts"]) for q in rows)
    print(f"Imported {len(rows)} verified Biology questions / {parts} parts -> {cpath}")
    print(f"Canonical source images: {len(rows)}")
    return rows


def _js_string(value: str) -> str:
    return json.dumps(value or "", ensure_ascii=False)


def _format_question(q: dict) -> str:
    lines = ["  {",
             f"    id:        {_js_string(q['id'])},",
             f"    subject:   {_js_string(q['subject'])},",
             f"    chapterId: {_js_string(q['chapterId'])},",
             f"    sectionId: {_js_string(q['sectionId'])},",
             f"    source:    {_js_string(q['source'])},",
             f"    year:      {int(q['year'])},",
             "    parts: ["]
    for p in q["parts"]:
        lines += ["      {",
                  f"        label:    {_js_string(p.get('label', ''))},",
                  f"        question: {_js_string(p.get('question', ''))},",
                  f"        marks:    {int(p.get('marks', 0) or 0)},",
                  f"        model:    {_js_string(p.get('model', ''))},"]
        if p.get("model_source"):
            lines.append(f"        model_source: {_js_string(p['model_source'])},")
        lines += [f"        diagram:  {_js_string(p.get('diagram', ''))}", "      },"]
    lines += ["    ],", "  },"]
    return "\n".join(lines)


def export_curated() -> None:
    cpath = CANONICAL / "biology.json"
    rows = json.loads(cpath.read_text())
    empty = [(q["id"], p.get("label", "")) for q in rows for p in q["parts"] if not (p.get("model") or "").strip()]
    if empty:
        raise SystemExit(f"Refusing to export with {len(empty)} unanswered part(s); first: {empty[:3]}")
    text = DB_PATH.read_text()
    start, end = _block_bounds(text)
    block = "  // ── BIOLOGY ({} questions) ───────────────────────────────────────\n\n{}\n\n\n".format(
        len(rows), "\n\n".join(_format_question(q) for q in rows))
    DB_PATH.write_text(text[:start] + block + text[end:])
    print(f"Exported {len(rows)} Biology questions / {sum(len(q['parts']) for q in rows)} answered parts -> {DB_PATH}")


def snapshot_curated() -> None:
    """Save the verified bank before the generated canonical store is replaced for expansion."""
    rows = load_curated()
    if len(rows) != 28:
        raise SystemExit(f"Refusing expansion snapshot: expected 28 curated Biology rows, got {len(rows)}")
    if any(not (p.get("model") or "").strip() for q in rows for p in q.get("parts", [])):
        raise SystemExit("Refusing expansion snapshot: the curated Biology bank has unanswered parts")
    CURATED_BASELINE.parent.mkdir(parents=True, exist_ok=True)
    CURATED_BASELINE.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    print(f"Snapshotted {len(rows)} curated Biology questions -> {CURATED_BASELINE}")


def reconcile_expansion() -> dict:
    """Reconcile a fully segmented canonical store against the verified curated layer."""
    import segment
    cpath = CANONICAL / "biology.json"
    generated = json.loads(cpath.read_text())
    curated_rows = load_curated()
    kept, report = reconcile_rows(generated, curated_rows)
    cpath.write_text(json.dumps(kept, ensure_ascii=False, indent=2) + "\n")
    segment.render_js(SUBJECT, kept)
    REPORTS.mkdir(parents=True, exist_ok=True)
    DUPLICATE_REPORT.write_text(json.dumps({"phase": "post-segment-reconcile", **report},
                                           ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return report


def audit_expansion() -> dict:
    """Audit the live curated layer plus the generated additive canonical layer."""
    generated_path = CANONICAL / "biology.json"
    generated = json.loads(generated_path.read_text()) if generated_path.exists() else []
    rows = load_curated() + generated
    report = audit_rows(rows)
    previous = {}
    if DUPLICATE_REPORT.exists():
        try:
            previous = json.loads(DUPLICATE_REPORT.read_text())
        except Exception:
            previous = {}
    DUPLICATE_REPORT.write_text(json.dumps({**previous, "final_audit": report},
                                           ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return report


def archive_images() -> None:
    cpath = CANONICAL / "biology.json"
    rows = json.loads(cpath.read_text())
    keep = {Path(p["diagram"]).name for q in rows for p in q["parts"] if p.get("diagram")}
    if len(keep) != len(rows):
        raise SystemExit(f"Expected one distinct canonical page per question; got {len(keep)} for {len(rows)}")
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    moved = 0
    for source in sorted(IMAGE_DIR.glob("*.png")):
        if source.name in keep:
            continue
        dest = ARCHIVE_DIR / source.name
        if dest.exists():
            if hashlib.sha256(dest.read_bytes()).digest() != hashlib.sha256(source.read_bytes()).digest():
                raise SystemExit(f"Archive collision with different bytes: {dest}")
            source.unlink()
        else:
            shutil.move(str(source), dest)
        moved += 1
    report = {
        "subject": SUBJECT,
        "active_images": len(list(IMAGE_DIR.glob("*.png"))),
        "distinct_active_hashes": len({hashlib.sha256(p.read_bytes()).hexdigest() for p in IMAGE_DIR.glob("*.png")}),
        "archived_legacy_files": moved,
        "archive": str(ARCHIVE_DIR),
        "verified_orphans": [q["id"] for q in ORPHAN_QUESTIONS],
    }
    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / "biology-image-repair.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


def main() -> None:
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action == "import":
        import_curated()
    elif action == "export":
        export_curated()
    elif action == "archive-images":
        archive_images()
    elif action == "snapshot":
        snapshot_curated()
    elif action == "reconcile-expansion":
        reconcile_expansion()
    elif action == "audit-expansion":
        audit_expansion()
    else:
        raise SystemExit("usage: python3 biology_repair.py "
                         "import|export|archive-images|snapshot|reconcile-expansion|audit-expansion")


if __name__ == "__main__":
    main()
