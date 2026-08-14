"""Stage 5b — OFFICIAL ANSWERS, matched out of the marking scheme (reform A).

Runs AFTER segment.py (which now reads the exam PAPER only) and BEFORE model_answers.py.
Segment no longer reads the marking scheme at all — that separation is what stops the model
mistaking the scheme's mark-allocation skeleton for the question wording. This stage closes the
loop: for each paper it reads the marking SCHEME only, alongside the list of parts segment
already extracted, and copies each part's official model answer out of the scheme.

One model call per paper. For each part it returns the scheme's answer (faithful, concise) or
"" when the scheme gives only marking criteria / doesn't cover that part — model_answers.py then
writes a full H1 answer for whatever is left. Answers placed here are tagged
`model_source: "scheme"` (official SEC material), distinct from the later `"ai-h1"`.

    python3 schemes.py home-economics prepare    # queue one job per paper with a scheme
    python3 schemes.py home-economics collect     # fold the worker's answers into canonical
"""
from __future__ import annotations
import json
import re
import sys

import textclean
from config import CANONICAL, SCHEME_MATCH_CTX_CHARS
from segment import load_scaffold, render_js
from model_answers import load_scheme_context, q_level

PID_SEP = "@@"                      # part id = "<question id>@@<part index>"

EMIT_TOOL = {
    "name": "emit_scheme_answers",
    "description": "Return the official marking-scheme answer for each requested exam part.",
    "input_schema": {
        "type": "object",
        "properties": {
            "answers": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "pid": {"type": "string", "description": "the part id, echoed back exactly"},
                        "answer": {"type": "string", "description": "the model answer copied from the marking scheme; '' if the scheme has none"},
                        "points": {"type": "integer", "description": "how many DISTINCT marking points/credits the scheme rewards for this part (0 if unclear)"},
                    },
                    "required": ["pid", "answer"],
                },
            }
        },
        "required": ["answers"],
    },
}


def _stage(subject: str) -> str:
    return f"schemes-{subject}"


_TASK = ("Copy the official answer for each exam part out of the MARKING SCHEME in `prompt`. "
         "Each part is listed with a `pid`, its label, marks, and question text; return one entry "
         "per pid (echoed exactly) with the scheme's answer, or '' when the scheme only gives "
         "marking criteria / doesn't cover that part. Be faithful to the scheme; invent nothing.")


def validate_output(obj, job=None) -> bool:
    """Reject placeholder files and obviously wrong scheme assets before collection.

    A real written-paper marking scheme covers most listed parts. An all-empty answer list was
    previously accepted when the archive supplied a practical-coursework rubric instead.
    """
    if not isinstance(obj, dict) or not isinstance(obj.get("answers"), list) or not obj["answers"]:
        return False
    pids = []
    useful = 0
    for answer in obj["answers"]:
        if not isinstance(answer, dict) or not isinstance(answer.get("pid"), str) \
                or not isinstance(answer.get("answer", ""), str):
            return False
        pids.append(answer["pid"])
        points = answer.get("points", 0)
        useful += bool(answer.get("answer", "").strip()) or (isinstance(points, int) and points > 0)
    if len(set(pids)) != len(pids):
        return False
    # A lone table row/column number is an OCR/layout artefact, not an official answer.  These
    # used to pass because the surrounding paper had enough valid answers to clear the coarse
    # coverage threshold.
    trivial = {str(n) for n in range(1, 21)} | {f"{n}." for n in range(1, 21)}
    if any(a.get("answer", "").strip() in trivial for a in obj["answers"]):
        return False
    if isinstance(job, dict):
        expected = re.findall(r"^\[([^\]]+@@\d+)\]", job.get("prompt", ""), re.MULTILINE)
        if expected and pids != expected:
            return False
    return useful / len(obj["answers"]) >= 0.5


def _paper_key(q: dict) -> str:
    paper = str(q.get("paper", "") or "")
    return f"{q.get('year')}-{q_level(q)}{'-P' + paper if paper else ''}"


def _empty_parts(q: dict):
    """(part_index, part) for parts that still need an answer."""
    return [(i, p) for i, p in enumerate(q["parts"]) if not (p.get("model") or "").strip()]


def build_prompt(subject: str, scheme: str, lines: list[str]) -> str:
    import retrieval
    excerpt = retrieval.select_text_chunks(scheme, lines, SCHEME_MATCH_CTX_CHARS, per_query=2)
    # A text-only/scanned scheme can have no retrievable tokens. Retain a bounded fallback, never
    # the historical 140k-character repeat.
    excerpt = excerpt or scheme[:SCHEME_MATCH_CTX_CHARS]
    return f"""You are reading the official State Examinations Commission MARKING SCHEME for one
Leaving Certificate {subject} paper. Below it is the list of question PARTS already extracted from
that paper's question paper. For each part, copy the corresponding model/expected answer out of
the marking scheme.

Rules:
- Match each part to the scheme by its label and question wording.
- Copy the scheme's answer faithfully; you may tidy obvious OCR artefacts. Keep it concise.
- Copy the ANSWER only. Leave out mark allocations ("4 points @ 6 marks each", "= 6 marks") and
  any part label belonging to the NEXT part — that is the scheme's bookkeeping, not the answer.
- If the scheme gives only marking *criteria* (points/keywords, not a usable answer) or does not
  cover a part, return "" for that pid — a later stage will author a full answer.
- `points`: count how many DISTINCT marking points/credits the scheme rewards for the part (e.g.
  "any 3 × 2 marks" -> 3; a 6-mark part credited as 3 points -> 3). Use 0 only if truly unclear.
- Echo every `pid` exactly as given. Do NOT invent content that isn't in the scheme.
- Return ONLY via the emit_scheme_answers tool.

=== MARKING SCHEME ===
{excerpt}

=== QUESTION PARTS (answer each pid) ===
{chr(10).join(lines)}
"""


def parse_result(content) -> list[dict]:
    for b in content:
        if getattr(b, "type", None) == "tool_use" and b.name == "emit_scheme_answers":
            raw = b.input.get("answers", []) if isinstance(b.input, dict) else []
            out = []
            for a in raw:
                if isinstance(a, dict) and a.get("pid"):
                    pts = a.get("points")
                    # Deterministic repair, not a re-prompt: schemes from some eras lead with a
                    # mark allocation ("4 points @ 6 marks each") and PDF tables append the next
                    # part's label to the previous cell. Both are mechanical, so they are stripped
                    # in Python for free rather than by spending tokens asking the worker again.
                    # May return "" — see collect(), which then leaves the part unanswered.
                    answer = textclean.clean_scheme_answer(a.get("answer") or "")
                    out.append({"pid": str(a["pid"]).strip(),
                                "answer": answer,
                                "points": int(pts) if isinstance(pts, int) or (isinstance(pts, str) and pts.isdigit()) else 0})
            return out
    return []


def prepare(subject: str) -> int:
    """One job per paper that has a marking scheme on disk and parts still needing an answer."""
    import agent_bridge as bridge
    canonical = json.loads((CANONICAL / f"{subject}.json").read_text())
    per, _fallback = load_scheme_context(subject)
    if not per:
        print("[schemes] no marking schemes on disk — model_answers.py will author all answers")
        return 0

    # group questions by paper, collect the parts that still need an answer
    by_paper: dict[str, list[tuple[str, dict, int, dict]]] = {}
    for q in canonical:
        key = _paper_key(q)
        if key not in per:
            continue                                  # no scheme for this paper — skip
        for idx, p in _empty_parts(q):
            by_paper.setdefault(key, []).append((q["id"], q, idx, p))

    jobs = []
    for i, (key, items) in enumerate(sorted(by_paper.items())):
        if not items:
            continue
        lines = []
        for qid, q, idx, p in items:
            pid = f"{qid}{PID_SEP}{idx}"
            qtext = (p.get("question") or "").replace("\n", " ")[:600]
            lines.append(f"[{pid}] ({p.get('label') or 'part'}, {p.get('marks', 0)} marks) {qtext}")
        jobs.append({"custom_id": f"p{i}", "prompt": build_prompt(subject, per[key], lines),
                     "tool": EMIT_TOOL, "meta": {"paper": key}})
    if not jobs:
        print("[schemes] every part already has an answer — nothing to match")
        return 0
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[schemes] {len(jobs)} paper(s) queued for the worker")
    return len(jobs)


def collect(subject: str) -> None:
    """Fold the worker's scheme answers into canonical (tagged 'scheme'), re-render the app JS."""
    import agent_bridge as bridge
    import ids
    canonical = json.loads((CANONICAL / f"{subject}.json").read_text())
    # raises on duplicate ids: a plain {q["id"]: q} keeps only the LAST row per id, so official
    # marking-scheme answers would land on the wrong question (or vanish) without a word
    by_id = ids.index_by_id(canonical, where="schemes.collect")
    outs = bridge.outputs(_stage(subject))
    filled = markup_only = 0
    for _cid, content in outs.items():
        for a in parse_result(content):
            pid, ans, pts = a["pid"], a["answer"], a.get("points", 0)
            if not ans:
                markup_only += 1              # nothing survived cleaning -> model_answers fills it
            if PID_SEP not in pid:
                continue
            qid, _, idx = pid.rpartition(PID_SEP)
            q = by_id.get(qid)
            if not q or not idx.isdigit():
                continue
            i = int(idx)
            if i >= len(q["parts"]):
                continue
            if pts:                                     # length target, kept regardless of answer
                q["parts"][i]["scheme_points"] = pts
            if ans and not (q["parts"][i].get("model") or "").strip():
                q["parts"][i]["model"] = ans
                q["parts"][i]["model_source"] = "scheme"
                filled += 1
    (CANONICAL / f"{subject}.json").write_text(json.dumps(canonical, ensure_ascii=False, indent=2))
    js = render_js(subject, canonical)
    print(f"\n[schemes] filled {filled} official answer(s) from marking schemes. Rendered: {js.name}")
    if markup_only:
        print(f"[schemes] {markup_only} scheme entr(ies) were mark allocation only — left unanswered "
              f"for model_answers.py rather than published as bookkeeping")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject)
        print("nothing to do" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
