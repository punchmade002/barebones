"""Stage 6b — H1 MODEL ANSWERS. Fill empty `model` fields with full-marks sample answers.

Runs AFTER segment.py. Many essay questions have no official model answer (the marking
scheme gives marking *criteria*, not a sample essay). This step writes a high-quality,
H1-standard answer for each such question with an economy-tier worker, instructed to satisfy the
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

from config import (CANONICAL, DIGEST, REPORTS, ANSWER_CTX_CHARS, SCHEME_ANSWER_CTX_CHARS,
                    ANSWER_BATCH_SIZE, recommended_words)
from segment import _retry, MODEL, load_scaffold
import ids
import validate

ANSWER_TOKENS = 5_000           # room for a full essay per question
SCHEME_CTX_CHARS = SCHEME_ANSWER_CTX_CHARS
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
                        "pid": {"type": "string", "description": "the stable part id, echoed back exactly"},
                        "label": {"type": "string", "description": "the part label, echoed back"},
                        "answer": {"type": "string", "description": "the H1 sample answer"},
                    },
                    "required": ["pid", "answer"],
                },
            }
        },
        "required": ["answers"],
    },
}

PID_SEP = "@@"


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
            paper = str(dg.get("paper_no", "") or "")
            per[f"{dg['year']}-{dg['level']}{'-P' + paper if paper else ''}"] = txt
            pool.append(txt)
    fallback = "\n\n".join(pool)[:FALLBACK_CHARS]
    return per, fallback


def q_level(q: dict) -> str:
    """Return the canonical level, tolerating curated ``HL``/``OL`` source labels.

    Generated rows carry an explicit ``level`` field, while the older hand-curated bank only
    encoded the abbreviation in ``source``.  Treating ``HL`` as unknown prevents an otherwise
    valid marking scheme from ever being paired to the question.
    """
    explicit = (q.get("level") or "").strip().lower()
    if explicit in {"higher", "ordinary"}:
        return explicit
    s = (q.get("source") or "").lower()
    if "higher" in s or re.search(r"\bhl\b", s):
        return "higher"
    if "ordinary" in s or re.search(r"\bol\b", s):
        return "ordinary"
    return ""


def is_documents_q(q: dict) -> bool:
    return any(DOC_RE.search(p.get("question", "")) for p in q["parts"])


def needs_fill(q: dict) -> list[dict]:
    """Parts with no model answer AND a real question to answer. A placeholder question
    (e.g. 'Part (a)') is skipped — AI-filling it just manufactures a convincing answer to
    nothing; the coverage/validator flags the missing question instead."""
    return [p for p in q["parts"]
            if not (p.get("model") or "").strip() and not validate.is_placeholder(p)]


CORPUS_CTX_CHARS = 15_000       # legacy cap, kept for the API path's cached_prefix()


def _part_line(subject: str, qid: str, idx: int, p: dict) -> str:
    marks = p.get("marks", 0)
    points = p.get("scheme_points")
    words = recommended_words(subject, marks, points)
    bits = []
    if points:
        bits.append(f"~{points} scheme points")
    if words:
        bits.append(f"AT LEAST {words} words")
    target = f" [{'; '.join(bits)}]" if bits else ""
    return (f"[{qid}{PID_SEP}{idx}] (label: {p.get('label') or 'part'}; "
            f"{marks} marks{target}) {p['question']}")


def cached_prefix(subject: str, scheme_ctx: str, used_fallback: bool,
                  material: str | None = None) -> str:
    """The scheme + instruction block. `material` is the course material to ground answers in;
    pass the retrieved, question-specific excerpt (what the keyless worker path does). When it is
    None this falls back to a head slice of the corpus, which is only right for the API path
    below, where a byte-identical prefix across questions is the point of the cache."""
    import resources
    note = ("NOTE: this year's marking scheme wasn't available, so the criteria below are "
            "pooled from other years of the same subject — use them to infer the standard.\n\n"
            if used_fallback else "")
    scheme = scheme_ctx[:SCHEME_CTX_CHARS] if scheme_ctx.strip() else \
        f"(use standard {subject} marking conventions)"
    if material is None:
        material = resources.corpus(subject)[:CORPUS_CTX_CHARS]
    course = (f"\n\n=== COURSE MATERIAL (ground every answer in THIS; it is the authoritative "
              f"source for the course) ===\n{material}" if material.strip() else "")
    return f"""You are a State Examinations Commission examiner AND a top H1 candidate for
Leaving Certificate {subject}. Write sample answers that would score FULL MARKS.

{note}Each part states a length as "~N scheme points" and/or "AT LEAST N words". MEET OR EXCEED
it — develop EVERY scheme point fully with specific, accurate detail. Do not stop short; a
full-marks exemplar is thorough, not terse. No padding or waffle, but cover every creditable point.

    Match what the marking scheme rewards: sustained relevance to the question, accurate
specific evidence (names, dates, events, statistics), clear structure, developed analysis,
and a reasoned judgement.

STAY ON COURSE: ground answers in the COURSE MATERIAL below and the marking scheme. Use ONLY
material on the Leaving Certificate {subject} syllabus for the stated topic. Do not bring in
facts outside the course. Do not invent facts. Return ONLY via the emit_answers tool, echoing each pid.

=== MARKING SCHEME / CRITERIA ===
{scheme}{course}"""


def variable_suffix(subject: str, q: dict, title: str) -> str:
    """The small, per-question part."""
    parts = "\n".join(_part_line(subject, q["id"], i, p)
                      for i, p in enumerate(q["parts"])
                      if not (p.get("model") or "").strip() and not validate.is_placeholder(p))
    return f"TOPIC: {title}\n\nQUESTION PART(S) TO ANSWER:\n{parts}"


def content_blocks(subject: str, q: dict, scheme_ctx: str, used_fallback: bool, title: str) -> list:
    """User content as two blocks: a cached scheme/instruction prefix + the question."""
    return [
        {"type": "text", "text": cached_prefix(subject, scheme_ctx, used_fallback),
         "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": variable_suffix(subject, q, title)},
    ]


def parse_result(content):
    """Normalise the tool output to a list of {label, answer}. Workers sometimes return the
    answers as bare strings or with missing labels — tolerate every shape."""
    for b in content:
        if getattr(b, "type", None) == "tool_use" and b.name == "emit_answers":
            raw = b.input.get("answers", []) if isinstance(b.input, dict) else []
            out = []
            for a in raw:
                if isinstance(a, dict):
                    out.append({"pid": str(a.get("pid", "")).strip(),
                                "label": str(a.get("label", "")).strip(),
                                "answer": (a.get("answer") or a.get("text") or "").strip()})
                elif isinstance(a, str):
                    out.append({"pid": "", "label": "", "answer": a.strip()})
            return out
    return []


def validate_output(obj, job=None) -> bool:
    """Require a complete, exactly addressed set of non-empty answers for one question job."""
    if not isinstance(obj, dict) or not isinstance(obj.get("answers"), list) or not obj["answers"]:
        return False
    pids = []
    for answer in obj["answers"]:
        if not isinstance(answer, dict) or not isinstance(answer.get("pid"), str):
            return False
        if not isinstance(answer.get("answer"), str) or not answer["answer"].strip():
            return False
        pids.append(answer["pid"])
    if len(set(pids)) != len(pids):
        return False
    if isinstance(job, dict):
        expected = re.findall(r"^\[([^\]]+@@\d+)\]", job.get("prompt", ""), re.MULTILINE)
        if expected and pids != expected:
            return False
    return True


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
        paper = str(q.get("paper", "") or "")
        key = f"{q['year']}-{q_level(q)}{'-P' + paper if paper else ''}"
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
    """Match each empty part by stable id; tolerate old label/position outputs for old queues."""
    empties = [(i, p) for i, p in enumerate(q["parts"])
               if not (p.get("model") or "").strip() and not validate.is_placeholder(p)]
    by_pid = {a["pid"]: a["answer"] for a in answers if a.get("pid")}
    by_label = {a["label"].lower(): a["answer"] for a in answers if a.get("label")}
    filled = 0
    for pos, (idx, p) in enumerate(empties):
        ans = by_pid.get(f"{q['id']}{PID_SEP}{idx}")
        if not ans:
            ans = by_label.get((p.get("label") or "").lower())
        if not ans:                                    # positional / single-answer fallback
            if pos < len(answers):
                ans = answers[pos]["answer"]
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
    """Tag official answers, queue small batches of questions needing H1 answers. The
    `model_source` tagging done by _targets is persisted now so it survives. Returns job count."""
    import agent_bridge as bridge
    canonical, jobs = _targets(subject, limit)
    (CANONICAL / f"{subject}.json").write_text(json.dumps(canonical, ensure_ascii=False, indent=2))
    if not jobs:
        return 0
    # group questions that share a marking scheme (stable prefix) for tidy, comparable prompts
    jobs.sort(key=lambda j: (j["fallback"], j["q"].get("year", 0), q_level(j["q"])))
    # Ground each question in the passages that concern IT. Nothing caches on the keyless path
    # (prepare flattens the prompt to a string on disk), so the old shared corpus[:15k] was
    # simply copied into every job file — the largest avoidable cost in the pipeline.
    import retrieval
    prepared = []
    for job in jobs:
        q = job["q"]
        asked = " ".join((p.get("question") or "") for p in needs_fill(q))
        material = retrieval.excerpt(subject, job["title"], ANSWER_CTX_CHARS, extra=asked,
                                     what=f"{q['id']} ({job['title']})")
        scheme = retrieval.select_text_chunks(job["ctx"], [asked], SCHEME_ANSWER_CTX_CHARS,
                                               per_query=3)
        scheme = scheme or job["ctx"][:SCHEME_ANSWER_CTX_CHARS]
        prepared.append({**job, "material": material, "scheme": scheme})

    out = []
    for i in range(0, len(prepared), ANSWER_BATCH_SIZE):
        batch = prepared[i:i + ANSWER_BATCH_SIZE]
        sections = []
        for job in batch:
            q = job["q"]
            fallback_note = ("This paper has no local scheme; the excerpt is pooled from other "
                             "years.\n" if job["fallback"] else "")
            sections.append(
                f"=== ITEM {q['id']} ===\n{fallback_note}"
                f"MARKING SCHEME / CRITERIA:\n{job['scheme'] or '(use standard marking conventions)'}\n\n"
                f"AUTHORITATIVE COURSE MATERIAL:\n{job['material'] or '(no matching bundle passage)'}\n\n"
                f"{variable_suffix(subject, q, job['title'])}")
        prompt = f"""You are a State Examinations Commission examiner and top H1 candidate for
Leaving Certificate {subject}. Write a full-marks sample answer for EVERY pid below. Meet or
exceed stated point/word targets; develop each creditable point with accurate course detail.
Ground answers in the item-specific authoritative course material and marking criteria. Do not
invent facts or import content from outside the course. Echo every pid in its listed order and
return only via emit_answers.

{chr(10).join(sections)}"""
        qids = [job["q"]["id"] for job in batch]
        out.append({"custom_id": f"batch_{i // ANSWER_BATCH_SIZE:04d}", "prompt": prompt,
                    "tool": EMIT_TOOL, "meta": {"qids": qids}})
    bridge.prepare(_stage(subject), out, task=_TASK)
    print(f"[model-answers] {len(prepared)} question(s) queued in {len(out)} batch job(s)")
    return len(out)


def collect(subject: str) -> None:
    """Read the worker's answers, fill empty `model` fields (tagged ai-h1), re-render the JS."""
    import agent_bridge as bridge
    canonical = json.loads((CANONICAL / f"{subject}.json").read_text())
    # raises on duplicate ids: a lossy index here writes every colliding question's answer onto
    # whichever row happened to be last, and leaves the rest unanswered
    by_id = ids.index_by_id(canonical, where="model_answers.collect")
    stage = _stage(subject)
    ins, outs = bridge.inputs(stage), bridge.outputs(stage)
    for cid, content in outs.items():
        meta = ins.get(cid, {}).get("meta", {})
        qids = meta.get("qids") or ([meta["qid"]] if meta.get("qid") else [])
        answers = parse_result(content)
        for qid in qids:
            q = by_id.get(qid)
            if not q:
                continue
            own = [a for a in answers if a.get("pid", "").startswith(f"{qid}{PID_SEP}")]
            n = _apply(q, own)
            print(f"[ans] {qid}: {n} part(s) filled" + ("" if n else "  ← EMPTY"))
    (CANONICAL / f"{subject}.json").write_text(json.dumps(canonical, ensure_ascii=False, indent=2))
    import segment
    js = segment.render_js(subject, canonical)
    filled = sum(1 for q in canonical for p in q["parts"] if p.get("model_source") == "ai-h1")
    have = sum(1 for q in canonical for p in q["parts"] if (p.get("model") or "").strip())
    total = sum(len(q["parts"]) for q in canonical)

    # Track the ai-h1 share (a high one is the symptom of upstream segmentation failure) so the
    # merge gate can cap it and a human can see where the AI answers cluster by year.
    by_year: dict = defaultdict(lambda: [0, 0])             # year -> [ai_h1, total]
    for q in canonical:
        for p in q["parts"]:
            by_year[q["year"]][1] += 1
            if p.get("model_source") == "ai-h1":
                by_year[q["year"]][0] += 1
    ratio = filled / max(1, total)
    rep = {"subject": subject, "ai_h1_filled": filled, "answered_parts": have,
           "parts_total": total, "ai_h1_ratio": round(ratio, 3),
           "by_year": {str(y): {"ai_h1": a, "total": t, "ratio": round(a / max(1, t), 3)}
                       for y, (a, t) in sorted(by_year.items())}}
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / f"answers-{subject}.json").write_text(json.dumps(rep, indent=2))

    print(f"\nFilled {filled} H1 answers. Coverage now {have}/{total} parts "
          f"({100*have//max(1,total)}%). ai-h1 ratio {ratio:.0%}. Rendered: {js.name}")
    if ratio > 0.40:
        print("⚠ ai-h1 ratio exceeds the 40% cap — the merge gate will block publishing "
              "unless segmentation is improved or --force is used.")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject, limit=limit)
        print("nothing to fill" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
