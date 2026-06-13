"""Stage 6b — H1 MODEL ANSWERS. Fill empty `model` fields with full-marks sample answers.

Runs AFTER segment.py. Many essay questions have no official model answer (the marking
scheme gives marking *criteria*, not a sample essay). This step writes a high-quality,
H1-standard answer for each such question with Claude Haiku, instructed to satisfy the
marking scheme for FULL marks. It uses that year's marking scheme as the criteria; when a
year has no scheme on disk, it falls back to the pooled criteria from other years.

Every answer it writes is tagged `model_source: "ai-h1"` so the app can distinguish it from
official `"scheme"` answers — these are AI-authored study aids, not SEC material.

Documents-based questions that quote a specific source ("In document A, …") are skipped:
the source image isn't in our text, so an answer would be guesswork. They're tagged
`model_source: "needs-source"`.

    export ANTHROPIC_API_KEY=sk-ant-...
    python3 model_answers.py history            # batch (unattended)
    python3 model_answers.py history --sync --limit 3   # quick test
"""
from __future__ import annotations
import json
import os
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

from config import CANONICAL, DIGEST, recommended_words
from segment import _retry, MODEL, load_scaffold

ANSWER_TOKENS = 5_000           # room for a full essay per question
SCHEME_CTX_CHARS = 12_000       # cap marking-scheme context per request (cached, so reused cheaply)
FALLBACK_CHARS = 12_000         # cap pooled cross-year criteria
DOC_RE = re.compile(r"\bdocument\s+[A-Z]\b|in the (?:above|following) document", re.I)

EMIT_TOOL = {
    "name": "emit_answers",
    "description": "Return a full-marks H1 sample answer for each requested question part.",
    "input_schema": {
        "type": "object",
        "properties": {
            "answers": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "label": {"type": "string", "description": "the part label, echoed back"},
                        "answer": {"type": "string", "description": "the H1 sample answer"},
                    },
                    "required": ["label", "answer"],
                },
            }
        },
        "required": ["answers"],
    },
}


def _scheme_text(block) -> str:
    return "\n".join(p["text"] for p in block["pages"] if p.get("text")) if block else ""


def load_scheme_context(subject: str):
    """Return (per_year_level_scheme, fallback_corpus). Keys: 'YYYY-level'."""
    per, pool = {}, []
    d = DIGEST / subject
    for f in sorted(d.glob("*.json")):
        if f.name == "_index.json":
            continue
        dg = json.loads(f.read_text())
        txt = _scheme_text(dg.get("scheme"))
        if txt.strip():
            per[f"{dg['year']}-{dg['level']}"] = txt
            pool.append(txt)
    fallback = "\n\n".join(pool)[:FALLBACK_CHARS]
    return per, fallback


def q_level(q: dict) -> str:
    """Canonical questions don't store level explicitly — read it from `source`."""
    s = (q.get("source") or "").lower()
    return "higher" if "higher" in s else "ordinary" if "ordinary" in s else ""


def is_documents_q(q: dict) -> bool:
    return any(DOC_RE.search(p.get("question", "")) for p in q["parts"])


def needs_fill(q: dict) -> list[dict]:
    """Parts with no model answer that aren't document-dependent."""
    return [p for p in q["parts"] if not (p.get("model") or "").strip()]


def _part_line(subject: str, p: dict) -> str:
    marks = p.get("marks", 0)
    words = recommended_words(subject, marks)
    target = f", aim ~{words} words" if words else ""
    return f"[{p.get('label') or 'part'}] ({marks} marks{target}) {p['question']}"


def cached_prefix(subject: str, scheme_ctx: str, used_fallback: bool) -> str:
    """The big, STABLE part of the prompt — identical for every question that shares this
    marking scheme. Sent with cache_control so repeats cost ~10%."""
    note = ("NOTE: this year's marking scheme wasn't available, so the criteria below are "
            "pooled from other years of the same subject — use them to infer the standard.\n\n"
            if used_fallback else "")
    scheme = scheme_ctx[:SCHEME_CTX_CHARS] if scheme_ctx.strip() else \
        f"(use standard {subject} marking conventions)"
    return f"""You are a State Examinations Commission examiner AND a top H1 candidate for
Leaving Certificate {subject}. Write sample answers that would score FULL MARKS.

{note}Write each answer to the length given by the "aim ~N words" target on each part —
dense, fully relevant, no padding or waffle. A shorter answer that nails the marking
criteria beats a long one.

Match what the marking scheme rewards: sustained relevance to the question, accurate
specific evidence (names, dates, events, statistics), clear structure, developed analysis,
and a reasoned judgement.

STAY ON COURSE: use ONLY material on the Leaving Certificate {subject} syllabus for the
stated topic. Do not bring in facts, figures, examples, theories or events outside the
course. Do not invent facts. Return ONLY via the emit_answers tool, echoing each label.

=== MARKING SCHEME / CRITERIA ===
{scheme}"""


def variable_suffix(subject: str, q: dict, title: str) -> str:
    """The small, per-question part."""
    parts = "\n".join(_part_line(subject, p) for p in needs_fill(q))
    return f"TOPIC: {title}\n\nQUESTION PART(S) TO ANSWER:\n{parts}"


def content_blocks(subject: str, q: dict, scheme_ctx: str, used_fallback: bool, title: str) -> list:
    """User content as two blocks: a cached scheme/instruction prefix + the question."""
    return [
        {"type": "text", "text": cached_prefix(subject, scheme_ctx, used_fallback),
         "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": variable_suffix(subject, q, title)},
    ]


def parse_result(content):
    """Normalise the tool output to a list of {label, answer}. Haiku sometimes returns the
    answers as bare strings or with missing labels — tolerate every shape."""
    for b in content:
        if getattr(b, "type", None) == "tool_use" and b.name == "emit_answers":
            raw = b.input.get("answers", []) if isinstance(b.input, dict) else []
            out = []
            for a in raw:
                if isinstance(a, dict):
                    out.append({"label": str(a.get("label", "")).strip(),
                                "answer": (a.get("answer") or a.get("text") or "").strip()})
                elif isinstance(a, str):
                    out.append({"label": "", "answer": a.strip()})
            return out
    return []


def _targets(subject: str, limit: int | None):
    """Questions needing answers, with their scheme context attached."""
    canonical = json.loads((CANONICAL / f"{subject}.json").read_text())
    per, fallback = load_scheme_context(subject)
    titles = {c["id"]: c["title"] for c in load_scaffold(subject)["chapters"]}
    jobs, skipped_docs, tagged_scheme = [], 0, 0
    for q in canonical:
        empties = needs_fill(q)
        if not empties:
            for p in q["parts"]:                       # tag the official ones
                p.setdefault("model_source", "scheme"); tagged_scheme += 1
            continue
        if is_documents_q(q):                          # can't answer without the source doc
            for p in empties:
                p["model_source"] = "needs-source"
            skipped_docs += 1
            continue
        key = f"{q['year']}-{q_level(q)}"
        ctx = per.get(key, "")
        used_fallback = not ctx.strip()
        if used_fallback:
            ctx = fallback
        jobs.append({"q": q, "ctx": ctx, "fallback": used_fallback,
                     "title": titles.get(q.get("chapterId", ""), q.get("chapterId", ""))})
    if limit:
        jobs = jobs[:limit]
    print(f"{len(jobs)} question(s) to answer; {skipped_docs} documents-based skipped "
          f"(need source images)")
    return canonical, jobs


def _apply(job, answers: list) -> int:
    """Match each empty part to an answer by label, else by position. Returns count filled."""
    empties = needs_fill(job["q"])
    by_label = {a["label"].lower(): a["answer"] for a in answers if a.get("label")}
    filled = 0
    for i, p in enumerate(empties):
        ans = by_label.get((p.get("label") or "").lower())
        if not ans:                                    # positional / single-answer fallback
            if i < len(answers):
                ans = answers[i]["answer"]
            elif len(answers) == 1:
                ans = answers[0]["answer"]
        if ans and ans.strip():
            p["model"] = ans.strip()
            p["model_source"] = "ai-h1"
            filled += 1
    return filled


def run_sync(client, subject, jobs):
    def one(job):
        msg = _retry(client.messages.create, model=MODEL, max_tokens=ANSWER_TOKENS, tools=[EMIT_TOOL],
                     tool_choice={"type": "tool", "name": "emit_answers"},
                     messages=[{"role": "user",
                                "content": content_blocks(subject, job["q"], job["ctx"], job["fallback"], job["title"])}])
        return job, parse_result(msg.content)
    with ThreadPoolExecutor(max_workers=4) as ex:
        for job, answers in ex.map(one, jobs):
            n = _apply(job, answers)
            print(f"[ans] {job['q']['id']}: {n} part(s) filled" + ("" if n else "  ← EMPTY"))


def run_batch(client, subject, jobs):
    id_for = {f"q{i}": job for i, job in enumerate(jobs)}
    reqs = [{
        "custom_id": f"q{i}",
        "params": {"model": MODEL, "max_tokens": ANSWER_TOKENS, "tools": [EMIT_TOOL],
                   "tool_choice": {"type": "tool", "name": "emit_answers"},
                   "messages": [{"role": "user",
                                 "content": content_blocks(subject, job["q"], job["ctx"], job["fallback"], job["title"])}]},
    } for i, job in enumerate(jobs)]
    batch = _retry(client.messages.batches.create, requests=reqs)
    print(f"[batch] submitted {len(reqs)} answers as {batch.id}; polling…")
    while True:
        b = _retry(client.messages.batches.retrieve, batch.id)
        if b.processing_status == "ended":
            break
        time.sleep(20)
    for r in client.messages.batches.results(batch.id):
        job = id_for.get(r.custom_id)
        if job and r.result.type == "succeeded":
            _apply(job, parse_result(r.result.message.content))
        else:
            print(f"[skip] {r.custom_id}: {getattr(r.result,'type','?')}")


def run(subject: str, sync: bool, limit: int | None = None) -> None:
    try:
        import anthropic
    except ImportError:
        raise SystemExit("pip install anthropic --break-system-packages")
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY in your environment first.")
    client = anthropic.Anthropic(max_retries=6)
    canonical, jobs = _targets(subject, limit)
    if not jobs:
        print("Nothing to fill — run segment.py first, or all answers already present.")
        return

    # group questions that share a marking scheme (same year+level -> identical cached prefix)
    jobs.sort(key=lambda j: (j["fallback"], j["q"].get("year", 0), q_level(j["q"])))
    if not sync:
        print("Tip: batch mode (this) is ~50% cheaper than --sync, and the scheme context is "
              "prompt-cached across questions of the same year.")

    (run_sync if sync else run_batch)(client, subject, jobs)

    (CANONICAL / f"{subject}.json").write_text(json.dumps(canonical, ensure_ascii=False, indent=2))
    import segment
    js = segment.render_js(subject, canonical)
    filled = sum(1 for q in canonical for p in q["parts"] if p.get("model_source") == "ai-h1")
    have = sum(1 for q in canonical for p in q["parts"] if (p.get("model") or "").strip())
    total = sum(len(q["parts"]) for q in canonical)
    print(f"\nFilled {filled} H1 answers. Coverage now {have}/{total} parts "
          f"({100*have//max(1,total)}%). Rendered: {js.name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    run(subject, sync=("--sync" in args), limit=limit)
