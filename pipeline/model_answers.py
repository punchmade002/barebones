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


def _apply(q, answers: list) -> int:
    """Match each empty part to an answer by label, else by position. Returns count filled."""
    empties = needs_fill(q)
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


def _stage(subject: str) -> str:
    return f"answers-{subject}"


_TASK = ("Write an H1 (full-marks) sample answer for each exam question part in `prompt`, "
         "satisfying the marking scheme/criteria it quotes. Return them as `schema` describes, "
         "echoing each part label. Stay strictly on the Leaving Cert course; invent nothing.")


def prepare(subject: str, limit: int | None = None) -> int:
    """Tag official answers, queue one job per question that still needs an H1 answer. The
    `model_source` tagging done by _targets is persisted now so it survives. Returns job count."""
    import agent_bridge as bridge
    canonical, jobs = _targets(subject, limit)
    (CANONICAL / f"{subject}.json").write_text(json.dumps(canonical, ensure_ascii=False, indent=2))
    if not jobs:
        return 0
    # group questions that share a marking scheme (stable prefix) for tidy, comparable prompts
    jobs.sort(key=lambda j: (j["fallback"], j["q"].get("year", 0), q_level(j["q"])))
    out = []
    for i, job in enumerate(jobs):
        prompt = (cached_prefix(subject, job["ctx"], job["fallback"]) + "\n\n"
                  + variable_suffix(subject, job["q"], job["title"]))
        out.append({"custom_id": f"q{i}", "prompt": prompt, "tool": EMIT_TOOL,
                    "meta": {"qid": job["q"]["id"]}})
    bridge.prepare(_stage(subject), out, task=_TASK)
    print(f"[model-answers] {len(out)} question(s) queued for the worker")
    return len(out)


def collect(subject: str) -> None:
    """Read the worker's answers, fill empty `model` fields (tagged ai-h1), re-render the JS."""
    import agent_bridge as bridge
    canonical = json.loads((CANONICAL / f"{subject}.json").read_text())
    by_id = {q["id"]: q for q in canonical}
    stage = _stage(subject)
    ins, outs = bridge.inputs(stage), bridge.outputs(stage)
    for cid, content in outs.items():
        qid = ins.get(cid, {}).get("meta", {}).get("qid")
        q = by_id.get(qid)
        if not q:
            continue
        n = _apply(q, parse_result(content))
        print(f"[ans] {qid}: {n} part(s) filled" + ("" if n else "  ← EMPTY"))
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
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject, limit=limit)
        print("nothing to fill" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
