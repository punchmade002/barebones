"""Targeted chapter retagging without re-transcribing exam questions.

Use this after expanding or correcting a subject scaffold. Question IDs, wording, marks,
source pages, answers, and diagrams stay untouched; only chapterId/tag_confidence change.
The worker sees every question and the complete current chapter list.
"""
from __future__ import annotations

import json
import sys
from collections import Counter

import agent_bridge as bridge
import ids
from config import CANONICAL, REPORTS
from segment import load_scaffold, render_js

BATCH_SIZE = 35

EMIT_TOOL = {
    "name": "emit_tags",
    "description": "Assign every supplied exam question to one current scaffold chapter.",
    "input_schema": {
        "type": "object",
        "properties": {
            "assignments": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "chapterId": {"type": "string"},
                        "confidence": {"type": "number"},
                    },
                    "required": ["id", "chapterId", "confidence"],
                },
            },
        },
        "required": ["assignments"],
    },
}

_TASK = ("Retag every supplied canonical exam question against the complete current chapter "
         "scaffold. Preserve IDs and return exactly one assignment for every listed question.")


def _stage(subject: str, review: bool = False) -> str:
    return f"retag{'-review' if review else ''}-{subject}"


def validate_output(obj) -> bool:
    if not isinstance(obj, dict) or not isinstance(obj.get("assignments"), list):
        return False
    return all(
        isinstance(a, dict)
        and isinstance(a.get("id"), str)
        and isinstance(a.get("chapterId"), str)
        and isinstance(a.get("confidence"), (int, float))
        for a in obj["assignments"]
    )


def _parse(content) -> list[dict]:
    for block in content:
        if getattr(block, "type", None) == "tool_use" and block.name == "emit_tags":
            obj = block.input if isinstance(block.input, dict) else {}
            return obj.get("assignments", []) if isinstance(obj.get("assignments"), list) else []
    return []


def _prompt(chapters: list[dict], rows: list[dict]) -> str:
    chapter_text = "\n".join(f"- {c['id']}: {c['title']}" for c in chapters)
    questions = []
    for q in rows:
        wording = "\n".join(p.get("question", "") for p in q.get("parts", []))
        questions.append(
            f"ID: {q['id']}\nCURRENT: {q.get('chapterId', '')}\n"
            f"SOURCE: {q.get('source', '')}\nQUESTION:\n{wording[:6000]}"
        )
    return f"""Retag these Leaving Certificate exam questions against the COMPLETE Home Economics
chapter taxonomy below. The taxonomy combines the course-information database with the official
NCCA syllabus and includes core plus all three electives.

Rules:
- Return exactly one assignment for EVERY ID, in the same order.
- Use only chapterId values from the list.
- Choose the chapter containing the principal knowledge needed to answer the whole exam question.
- Do not let the old CURRENT tag bias you; it may be wrong because the former taxonomy omitted
  family, social studies, education, work, unemployment, and poverty.
- confidence is 0–1 and measures how clearly the question belongs to that chapter.

CHAPTERS:
{chapter_text}

QUESTIONS:
{"\n\n=====\n\n".join(questions)}
"""


def prepare(subject: str, batch_size: int = BATCH_SIZE, review: bool = False) -> int:
    path = CANONICAL / f"{subject}.json"
    if not path.exists():
        raise SystemExit(f"No canonical store {path}")
    rows = json.loads(path.read_text())
    if review:
        rows = [q for q in rows if q.get("tag_confidence", 0) < 0.6]
    chapters = load_scaffold(subject)["chapters"]
    jobs = []
    for start in range(0, len(rows), batch_size):
        batch = rows[start:start + batch_size]
        jobs.append({
            "custom_id": f"batch_{start // batch_size:03d}",
            "prompt": _prompt(chapters, batch),
            "tool": EMIT_TOOL,
            "meta": {"ids": [q["id"] for q in batch]},
        })
    bridge.prepare(_stage(subject, review), jobs, task=_TASK)
    label = "retag-review" if review else "retag"
    print(f"[{label}] {len(rows)} question(s) queued in {len(jobs)} batch job(s)")
    return len(jobs)


def collect(subject: str, review: bool = False) -> dict:
    path = CANONICAL / f"{subject}.json"
    rows = json.loads(path.read_text())
    by_id = ids.index_by_id(rows, where="retag.collect")
    allowed = {c["id"] for c in load_scaffold(subject)["chapters"]}
    ins, outs = bridge.inputs(_stage(subject, review)), bridge.outputs(_stage(subject, review))
    changed = invalid = 0
    missing: list[str] = []
    transitions = Counter()
    for cid, content in outs.items():
        expected = ins.get(cid, {}).get("meta", {}).get("ids", [])
        returned = {a.get("id"): a for a in _parse(content) if isinstance(a, dict)}
        for qid in expected:
            a = returned.get(qid)
            if not a:
                missing.append(qid)
                continue
            chapter = a.get("chapterId")
            confidence = a.get("confidence")
            if chapter not in allowed or not isinstance(confidence, (int, float)):
                invalid += 1
                continue
            q = by_id.get(qid)
            if not q:
                invalid += 1
                continue
            old = q.get("chapterId", "")
            if old != chapter:
                transitions[(old, chapter)] += 1
                changed += 1
            q["chapterId"] = chapter
            q["tag_confidence"] = max(0.0, min(1.0, float(confidence)))

    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    render_js(subject, rows)
    report = {
        "subject": subject, "questions": len(rows), "changed": changed,
        "missing": missing, "invalid": invalid,
        "low_confidence": [q["id"] for q in rows if q.get("tag_confidence", 0) < 0.6],
        "transitions": [
            {"from": old, "to": new, "count": count}
            for (old, new), count in transitions.most_common()
        ],
    }
    report_name = f"retag{'-review' if review else ''}-{subject}.json"
    (REPORTS / report_name).write_text(json.dumps(report, indent=2))
    label = "retag-review" if review else "retag"
    print(f"[{label}] changed {changed}/{len(rows)} question(s); "
          f"missing={len(missing)}, invalid={invalid}, "
          f"low-confidence={len(report['low_confidence'])}")
    return report


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "home-economics")
    if "collect" in args:
        collect(subject, review=("--review" in args))
    else:
        prepare(subject, review=("--review" in args))
