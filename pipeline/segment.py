"""Stages 3-5 — SEGMENT + TAG, from the EXAM PAPER ONLY (reform A).

Reads the digests produced by run.py/digest.py and, with one model call per paper, turns each
into structured records: questions split into parts (with marks), and a topic tag
(chapterId/sectionId from scaffold/<subject>.json) plus a confidence score. Output is the
canonical store + the rendered EXAM_QUESTIONS_DB JS.

Crucially it is given ONLY the exam paper — never the marking scheme. The old combined call
asked one model to read both documents at once and routinely emitted the scheme's
mark-allocation skeleton ("Part (a) … 4 marks") as the question wording, losing ~20% of the
real question text. Official answers are matched separately afterwards by schemes.py (scheme
only); H1 answers for the rest by model_answers.py. Flashcards are a later per-chapter step.

Keyless: the model work is done by a spawned `pipeline-worker` subagent via agent_bridge.py
(no ANTHROPIC_API_KEY). run.py recommends the `opus` model for this stage — exact question
text and marks are the foundation everything downstream depends on.

    python3 segment.py history prepare    # queue one job per paper for the worker
    python3 segment.py history collect      # fold the worker's answers into canonical
    python3 segment.py history --limit 2 prepare   # only 2 papers (cheap smoke test)
"""
from __future__ import annotations
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from config import DIGEST, CANONICAL, REPORTS, ROOT

MODEL = "claude-haiku-4-5-20251001"
SCAFFOLD_DIR = ROOT / "pipeline" / "scaffold"
MAX_SCHEME_CHARS = 60_000          # cap marking-scheme text to keep cost predictable
MAX_TOKENS = 16_000                # output cap; a full paper's questions+answers can be large
MAX_QUESTIONS_PER_PAPER = 200      # above this, the paper is malformed (usually bad OCR) -> skip

# ── structured-output tool: forces clean JSON back from the model ─────────────
# PAPER-ONLY (reform A). This stage reads the EXAM PAPER alone — never the marking
# scheme — so the model can't mistake the scheme's mark-allocation skeleton for the
# question wording (the old combined call lost ~20% of question text that way).
# Official model answers are matched out of the scheme later, by schemes.py.
EMIT_TOOL = {
    "name": "emit_questions",
    "description": "Return the exam questions extracted and tagged from this exam paper.",
    "input_schema": {
        "type": "object",
        "properties": {
            "questions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "label": {"type": "string", "description": "e.g. 'Q1'"},
                        "sectionId": {"type": "string"},
                        "chapterId": {"type": "string"},
                        "tag_confidence": {"type": "number", "description": "0-1"},
                        "parts": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "label": {"type": "string", "description": "sub-part label, e.g. '(a)'"},
                                    "question": {"type": "string", "description": "the FULL question wording as printed on the paper — never just a label like 'Part (a)'"},
                                    "marks": {"type": "integer", "description": "marks for this part; MUST be > 0 (use the section's marking rule if not printed beside the part)"},
                                },
                                "required": ["label", "question", "marks"],
                            },
                        },
                    },
                    "required": ["label", "sectionId", "chapterId", "parts"],
                },
            }
        },
        "required": ["questions"],
    },
}


def _retry(fn, *args, attempts: int = 6, **kwargs):
    """Call fn with exponential backoff on transient API errors (502/503/529/connection).
    Anthropic's gateway occasionally returns a 502; an unattended run should ride it out."""
    import anthropic
    transient = (anthropic.InternalServerError, anthropic.APIConnectionError,
                 anthropic.RateLimitError)
    for i in range(attempts):
        try:
            return fn(*args, **kwargs)
        except transient as e:
            if i == attempts - 1:
                raise
            wait = min(60, 2 ** i)
            print(f"  transient API error ({type(e).__name__}); retry {i+1}/{attempts-1} in {wait}s…")
            time.sleep(wait)


def load_scaffold(subject: str) -> dict:
    f = SCAFFOLD_DIR / f"{subject}.json"
    if not f.exists():
        raise SystemExit(f"No scaffold/{subject}.json — create the section+chapter list first.")
    return json.loads(f.read_text())


def pages_text(block: dict | None) -> str:
    if not block:
        return ""
    return "\n".join(p["text"] for p in block["pages"] if p.get("text"))


def build_prompt(subject: str, digest: dict, scaffold: dict) -> str:
    sections = "\n".join(f"  {s['id']}: {s['title']}" for s in scaffold["sections"])
    chapters = "\n".join(f"  {c['id']}: {c['title']}" for c in scaffold["chapters"])
    paper = pages_text(digest.get("paper"))
    return f"""You are extracting Leaving Certificate {subject} exam questions for a study app.
You are given ONLY the exam paper (no marking scheme). Transcribe what the paper actually asks.

YEAR {digest['year']} · {digest['level'].upper()} LEVEL · status: {digest['status']}

Assign every question to exactly one sectionId and one chapterId from these lists:
SECTIONS:
{sections}
CHAPTERS:
{chapters}

Rules:
- Split each exam question into its parts (a), (b), (i), (ii)… as the paper prints them.
- `question` MUST contain the FULL wording of what that part asks, exactly as printed.
  NEVER output a bare label like "Part (a)" or "(i)" as the question — that is wrong;
  put the label in `label` and the real question text in `question`. If a part has
  sub-points, join them with \\n into the one `question` string.
- `marks`: an integer GREATER THAN ZERO for every part. If marks aren't printed beside
  the part, derive them from the section's marking rule stated in the paper's instructions
  (e.g. "Section A: each question carries 6 marks", "Question 1 is worth 80 marks") and
  split sensibly across the sub-parts so they sum to the question's total. Do not output 0.
- Strip page numbers, booklet titles, "write your answers here", and other chrome.
- Set tag_confidence 0-1 (1 = the paper labels the topic explicitly).
- Return ONLY via the emit_questions tool.

=== EXAM PAPER ===
{paper}
"""


def parse_result(content) -> list[dict]:
    """Return the questions list, defensively. Garbled OCR can make the model emit a string
    or junk instead of a list of question objects — keep only well-formed dict items."""
    for block in content:
        if getattr(block, "type", None) == "tool_use" and block.name == "emit_questions":
            qs = block.input.get("questions") if isinstance(block.input, dict) else None
            if not isinstance(qs, list):
                return []
            return [q for q in qs if isinstance(q, dict)]
    return []


def to_canonical(subject: str, digest: dict, questions: list[dict]) -> list[dict]:
    out = []
    yr, lvl = digest["year"], digest["level"]
    for i, q in enumerate(questions, 1):
        parts = [p for p in q.get("parts", []) if isinstance(p, dict)]
        out.append({
            "id": f"{subject}-pp-{yr}-{lvl[:2].upper()}-{q.get('label','q'+str(i))}".replace(" ", ""),
            "subject": subject,
            "chapterId": q.get("chapterId", ""),
            "sectionId": q.get("sectionId", ""),
            "source": f"LC {subject.capitalize()} {lvl.capitalize()} {yr} — {q.get('label','')}"
                      + (" [REFERENCE — pre-current-syllabus]" if digest["status"] == "reference" else ""),
            "year": yr,
            "tag_confidence": q.get("tag_confidence", 0),
            # `model` starts empty — schemes.py fills official answers from the marking
            # scheme, then model_answers.py writes H1 answers for whatever's left.
            "parts": [{"label": p.get("label", ""), "question": p.get("question", ""),
                       "marks": p.get("marks", 0), "model": "", "diagram": ""}
                      for p in parts],
        })
    return out


# ── runners ───────────────────────────────────────────────────────────────────
def _paper_chars(dg: dict) -> int:
    p = dg.get("paper")
    return sum(len(x.get("text", "")) for x in p["pages"]) if p else 0


def _digests(subject: str, limit: int | None, year: int | None = None) -> list[dict]:
    d = DIGEST / subject
    # newest first, so a --limit quick test hits recent (complete, digital-text) papers
    files = sorted((f for f in d.glob("*.json") if f.name != "_index.json"), reverse=True)
    if year:
        files = [f for f in files if f.name.startswith(str(year))]
    if not files:
        raise SystemExit(f"No digests in {d} — run `python run.py {subject}` first.")
    digests = [json.loads(f.read_text()) for f in files]
    # skip year/levels with no usable exam paper (only a marking scheme, or a scan) —
    # they can't yield questions; report them instead of silently emitting 0.
    usable, skipped = [], []
    for dg in digests:
        (usable if _paper_chars(dg) >= 200 else skipped).append(dg)
    if skipped:
        names = ", ".join(f"{d['year']}-{d['level']}" for d in skipped)
        print(f"skipping {len(skipped)} set(s) with no usable exam paper (missing/scan): {names}")
    if limit:
        usable = usable[:limit]
    if not usable:
        raise SystemExit("No digests with a usable exam paper. Re-run acquire to fill gaps:\n"
                         f"  python3 run.py {subject}")
    return usable


def _diag(msg) -> str:
    """One-line summary of a response: stop reason + block types (+ text snippet if any)."""
    blocks = [getattr(b, "type", "?") for b in msg.content]
    text = " ".join(getattr(b, "text", "") for b in msg.content if getattr(b, "type", None) == "text")
    extra = f" text='{text[:160]}'" if text else ""
    return f"stop={msg.stop_reason} blocks={blocks}{extra}"


def _save(subject, rows):
    (CANONICAL / f"{subject}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))


def _stage(subject: str) -> str:
    return f"segment-{subject}"


_TASK = ("Extract the exam questions from each paper. Every job's `prompt` contains one exam "
         "paper + its marking scheme and the list of topics to tag against. Return the questions "
         "object exactly as `schema` describes — split into parts with marks, the model answer "
         "copied from the scheme, and a sectionId/chapterId for each question.")


def render_js(subject: str, canonical: list[dict]) -> Path:
    db = [{k: q[k] for k in ("id", "subject", "chapterId", "sectionId", "source", "year", "parts")}
          for q in canonical]
    out = REPORTS.parent / "canonical" / f"exam-questions-db.{subject}.generated.js"
    out.write_text("window.EXAM_QUESTIONS_DB = (window.EXAM_QUESTIONS_DB || []).concat(\n"
                   + json.dumps(db, indent=2, ensure_ascii=False) + "\n);\n")
    return out


def prepare(subject: str, limit: int | None = None, year: int | None = None,
            force: bool = False) -> int:
    """Write one job per paper that still needs segmenting. Returns the job count (0 = done)."""
    import agent_bridge as bridge
    scaffold = load_scaffold(subject)
    digests = _digests(subject, limit, year)

    # RESUME: skip papers already in the canonical store so re-runs never redo work.
    cpath = CANONICAL / f"{subject}.json"
    existing = json.loads(cpath.read_text()) if cpath.exists() else []
    if existing and not force:
        done = {(q["year"], "higher" if "Higher" in q.get("source", "") else "ordinary")
                for q in existing}
        before = len(digests)
        digests = [d for d in digests if (d["year"], d["level"]) not in done]
        print(f"resuming: {before - len(digests)} paper(s) already done, {len(digests)} to do")
    if not digests:
        return 0
    jobs = [{
        "custom_id": f"{dg['year']}_{dg['level']}_{dg['status']}",
        "prompt": build_prompt(subject, dg, scaffold),
        "tool": EMIT_TOOL,
        "meta": {"year": dg["year"], "level": dg["level"], "status": dg["status"]},
    } for dg in digests]
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[segment] {len(jobs)} paper(s) queued for the worker")
    return len(jobs)


def collect(subject: str, force: bool = False, review_threshold: float = 0.6) -> None:
    """Read the worker's answers, merge into the canonical store, render the app JS + report."""
    import agent_bridge as bridge
    cpath = CANONICAL / f"{subject}.json"
    existing = json.loads(cpath.read_text()) if cpath.exists() else []
    stage = _stage(subject)
    ins, outs = bridge.inputs(stage), bridge.outputs(stage)
    base = [] if force else existing
    new: list[dict] = []
    for cid, content in outs.items():
        meta = ins.get(cid, {}).get("meta", {})
        qs = parse_result(content)
        if len(qs) > MAX_QUESTIONS_PER_PAPER:
            print(f"[skip] {cid}: {len(qs)} items — malformed (likely scanned/OCR)")
            continue
        print(f"[seg] {cid}: {len(qs)} questions")
        new += to_canonical(subject, meta, qs)
        _save(subject, base + new)                          # durable as each lands
    canonical = base + new
    cpath.write_text(json.dumps(canonical, ensure_ascii=False, indent=2))
    js = render_js(subject, canonical)

    # coverage + review queue
    review = [q["id"] for q in canonical if q.get("tag_confidence", 0) < review_threshold]
    cov: dict[str, int] = {}
    for q in canonical:
        cov[q["chapterId"]] = cov.get(q["chapterId"], 0) + 1
    rep = {"subject": subject, "questions": len(canonical),
           "coverage_by_chapter": cov, "review_queue_low_confidence": review}
    (REPORTS / f"segment-{subject}.json").write_text(json.dumps(rep, indent=2))
    print(f"\n{len(canonical)} questions -> {cpath}")
    print(f"Rendered: {js.name} | review queue (<{review_threshold}): {len(review)}")


if __name__ == "__main__":
    # Manual per-stage use: `python3 segment.py <subject> prepare|collect`
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    year = int(args[args.index("--year") + 1]) if "--year" in args else None
    if "collect" in args:
        collect(subject, force=("--force" in args))
    else:
        n = prepare(subject, limit=limit, year=year, force=("--force" in args))
        print("nothing to do" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
