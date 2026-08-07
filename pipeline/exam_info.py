"""Stage 2.6 — the EXAM INFORMATION section, derived from the syllabus/specification bundle.

The app's exam-breakdown panel (window.EXAM_BREAKDOWN) tells a student how the paper is built:
total marks, total time, what each section is worth, how long to spend, and how to attack it.
Every subject's entry used to be hand-written, which meant a pipeline-built subject shipped with
no exam guidance at all — and it is also the source of the per-question timing label, so its
absence silently disabled that too.

This stage fills it from the same authoritative pool everything else uses: the NCCA specification
and course guide in `pipeline/resources/<subject>/`. ONE model call per subject.

Two things are deliberately NOT asked of the model:

  * `color` — assigned here from a fixed palette, so section colours stay stable across re-runs
    instead of drifting every time the stage regenerates.
  * `questionIdPattern` — a regex over generated question ids. The app never reads it (only the
    hand-written entries carry one), and a guessed regex that silently matches nothing is worse
    than an absent field.

    python3 exam_info.py biology            # queue the job
    python3 exam_info.py biology collect     # write the store + app JS

Output:
    _data/canonical/exam-info.<subject>.json          consumed by config.recommended_minutes()
    _data/canonical/exam-breakdown-<subject>.generated.js   window.EXAM_BREAKDOWN.<subject>
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

from config import CANONICAL, display_name

SPEC_CTX_CHARS = 14_000            # assessment sections of a spec are short; this is generous
MAX_TOKENS = 8_000                 # tips for every section add up

# Section colours, in order. Fixed so a regenerated breakdown doesn't reshuffle the app's palette.
PALETTE = ["#F97316", "#10B981", "#6366F1", "#EC4899", "#0EA5E9", "#EAB308", "#8B5CF6", "#14B8A6"]

EMIT_TOOL = {
    "name": "emit_exam_info",
    "description": "Return the exam structure for this subject, from its official specification.",
    "input_schema": {
        "type": "object",
        "properties": {
            "totalMarks": {"type": "integer", "description": "total marks available on the paper(s)"},
            "totalMinutes": {"type": "integer", "description": "total writing time in minutes"},
            "timingNote": {
                "type": "string",
                "description": ("optional one-line note when the time is not a single sitting, "
                                "e.g. 'Paper 1: 2h 30m, Paper 2: 2h 30m'. Omit if not needed."),
            },
            "notice": {
                "type": "string",
                "description": ("Set ONLY when the specification is new and no exam paper has been "
                                "sat under it yet, so no section breakdown can be given. When set, "
                                "sections may be empty."),
            },
            "sections": {
                "type": "array",
                "description": "the paper's top-level divisions, in the order a student meets them",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "MUST be one of the scaffold section ids given in the prompt"},
                        "name": {"type": "string", "description": "student-facing name, e.g. 'Section A – Short Questions'"},
                        "marks": {"type": "integer", "description": "marks available in this section"},
                        "minutesPerQuestion": {"type": "integer", "description": "recommended minutes per question in this section"},
                        "tips": {
                            "type": "object",
                            "properties": {
                                "timing": {"type": "string", "description": "how to budget time here, incl. how many questions to answer"},
                                "structure": {"type": "string", "description": "what a full-marks answer looks like in this section"},
                                "reminders": {
                                    "type": "array",
                                    "description": "3-6 short, concrete exam-technique reminders",
                                    "items": {"type": "string"},
                                },
                            },
                            "required": ["timing", "structure", "reminders"],
                        },
                        "chapterIds": {
                            "type": "array",
                            "description": "scaffold chapter ids examinable in this section (from the prompt's list)",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["id", "name", "marks", "tips"],
                },
            },
        },
        "required": ["totalMarks", "totalMinutes", "sections"],
    },
}


def build_prompt(subject: str, spec: str, sections: list[dict], chapters: list[dict]) -> str:
    sec_lines = "\n".join(f"  - {s['id']}: {s['title']}" for s in sections) or "  (none)"
    ch_lines = "\n".join(f"  - {c['id']}: {c['title']}" for c in chapters) or "  (none)"
    return f"""You are documenting how the Leaving Certificate {display_name(subject)} exam is
structured, for a study app's "exam breakdown" panel. A student reads this before sitting a mock
to understand what the paper asks of them and how to spend the time.

Work ONLY from the official specification / course material below. Do not guess a structure from
memory, and do not describe a version of the exam the material does not support.

- `totalMarks` and `totalMinutes` are for the whole examination. If the subject has two papers,
  sum both and explain the split in `timingNote`.
- `sections` must use the scaffold section ids EXACTLY as listed below — the app matches each
  question's sectionId against them, so an invented id shows the student nothing. Omit any
  scaffold section the specification does not describe as part of the written exam.
- `marks` per section must be what the specification allocates. `minutesPerQuestion` should be a
  realistic budget for one question there, consistent with the section's share of the total time.
- `tips.timing` says how many questions to answer and how long to spend. `tips.structure` says
  what a full-marks answer looks like HERE specifically (not generic exam advice).
  `tips.reminders` are 3-6 short, concrete, subject-specific instructions.
- `chapterIds` lists which of the scaffold chapters below can be examined in that section. Use
  the ids verbatim. If a section can draw on the whole course, list them all.
- If the specification is so new that no exam has been sat under it, set `notice` explaining that
  and return an empty `sections` array rather than inventing a breakdown.
- Return ONLY via the emit_exam_info tool.

SCAFFOLD SECTIONS (use these ids):
{sec_lines}

SCAFFOLD CHAPTERS (use these ids):
{ch_lines}

=== OFFICIAL SPECIFICATION / COURSE MATERIAL ===
{spec}
"""


def parse_result(content) -> dict | None:
    for block in content:
        if getattr(block, "type", None) == "tool_use" and block.name == "emit_exam_info":
            return block.input if isinstance(block.input, dict) else None
    return None


def _stage(subject: str) -> str:
    return f"exam-info-{subject}"


_TASK = ("Describe how this subject's exam is structured, from the official specification in "
         "`prompt`. Return the object exactly as `schema` describes, reusing the scaffold "
         "section/chapter ids verbatim.")


def store_path(subject: str) -> Path:
    return CANONICAL / f"exam-info.{subject}.json"


def validate_output(answer) -> bool:
    """Re-queue an answer that can't drive the app: the timing model needs BOTH totals, and a
    breakdown with no sections is only acceptable when the model explained why via `notice`."""
    data = parse_result(answer)
    if not data:
        return False
    if not (data.get("totalMarks") and data.get("totalMinutes")):
        return False
    return bool(data.get("sections") or data.get("notice"))


def normalise(subject: str, data: dict, sections: list[dict]) -> dict:
    """Shape the model's answer into the app's EXAM_BREAKDOWN entry.

    Sections are filtered to real scaffold ids and re-ordered to scaffold order, so a model that
    invents an id or shuffles the paper can't desynchronise the panel from the question data.
    """
    valid = {s["id"]: i for i, s in enumerate(sections)}
    out_sections = []
    for s in data.get("sections") or []:
        sid = (s.get("id") or "").strip()
        if sid not in valid:
            print(f"[exam-info] dropping section with unknown id {sid!r}")
            continue
        tips = s.get("tips") or {}
        out_sections.append({
            "id": sid,
            "name": (s.get("name") or "").strip() or sid,
            "marks": s.get("marks") or 0,
            "color": PALETTE[valid[sid] % len(PALETTE)],
            "minutesPerQuestion": s.get("minutesPerQuestion"),
            "tips": {
                "timing": (tips.get("timing") or "").strip(),
                "structure": (tips.get("structure") or "").strip(),
                "reminders": [r.strip() for r in (tips.get("reminders") or []) if r.strip()],
            },
            "chapterIds": [c for c in (s.get("chapterIds") or []) if c],
        })
    out_sections.sort(key=lambda s: valid[s["id"]])
    entry = {
        "subject": subject,
        "totalMarks": data.get("totalMarks"),
        "totalMinutes": data.get("totalMinutes"),
        "sections": out_sections,
    }
    for optional in ("timingNote", "notice"):
        if (data.get(optional) or "").strip():
            entry[optional] = data[optional].strip()
    return entry


def render_js(subject: str, entry: dict) -> Path:
    out = CANONICAL / f"exam-breakdown-{subject}.generated.js"
    out.write_text(
        "window.EXAM_BREAKDOWN = window.EXAM_BREAKDOWN || {};\n\n"
        f"window.EXAM_BREAKDOWN[{json.dumps(subject)}] =\n"
        + json.dumps(entry, indent=2, ensure_ascii=False) + ";\n")
    return out


def prepare(subject: str, regen: bool = False) -> int:
    """Queue the single exam-structure job. Returns 0 when the store already exists."""
    import agent_bridge as bridge
    import resources
    import retrieval
    from segment import load_scaffold
    if store_path(subject).exists() and not regen:
        return 0
    if not resources.corpus(subject).strip():
        print(f"[exam-info] no resource bundle for {subject} — cannot describe the exam without "
              f"the specification; skipping (per-question timing will be unavailable)")
        return 0
    scaffold = load_scaffold(subject)
    spec = retrieval.excerpt(
        subject,
        "assessment structure examination paper sections marks duration time allocation "
        "weighting written examination format",
        SPEC_CTX_CHARS, what="exam structure / assessment")
    if not spec.strip():
        print(f"[exam-info] bundle has no assessment material for {subject} — skipping")
        return 0
    job = {"custom_id": "exam-info",
           "prompt": build_prompt(subject, spec, scaffold.get("sections", []),
                                  scaffold.get("chapters", [])),
           "tool": EMIT_TOOL}
    bridge.prepare(_stage(subject), [job], task=_TASK)
    print("[exam-info] queued 1 job for the worker")
    return 1


def collect(subject: str) -> None:
    """Write the exam-info store (drives per-question timing) and the app's breakdown JS."""
    import agent_bridge as bridge
    from segment import load_scaffold
    outs = bridge.outputs(_stage(subject))
    content = outs.get("exam-info")
    data = parse_result(content) if content else None
    if not data:
        print(f"[exam-info] worker returned nothing usable for {subject} — "
              f"per-question timing will be unavailable")
        return
    entry = normalise(subject, data, load_scaffold(subject).get("sections", []))
    store_path(subject).write_text(json.dumps(entry, ensure_ascii=False, indent=2))
    js = render_js(subject, entry)
    mins, marks = entry.get("totalMinutes"), entry.get("totalMarks")
    print(f"[exam-info] {marks} marks / {mins} min, {len(entry['sections'])} section(s) -> {js.name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subj = next((a for a in args if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 exam_info.py <subject> [collect] [--regen]")
    if "collect" in args:
        collect(subj)
    else:
        n = prepare(subj, regen=("--regen" in args))
        print("exam info already exists" if not n else "1 job ready — spawn the pipeline-worker")
