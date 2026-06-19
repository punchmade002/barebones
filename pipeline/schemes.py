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
import sys

from config import CANONICAL
from segment import load_scaffold, render_js
from model_answers import load_scheme_context, q_level

PID_SEP = "@@"                      # part id = "<question id>@@<part index>"
MAX_SCHEME_CHARS = 60_000          # cap scheme text per paper to keep the call bounded

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


def _paper_key(q: dict) -> str:
    return f"{q.get('year')}-{q_level(q)}"


def _empty_parts(q: dict):
    """(part_index, part) for parts that still need an answer."""
    return [(i, p) for i, p in enumerate(q["parts"]) if not (p.get("model") or "").strip()]


def build_prompt(subject: str, scheme: str, lines: list[str]) -> str:
    return f"""You are reading the official State Examinations Commission MARKING SCHEME for one
Leaving Certificate {subject} paper. Below it is the list of question PARTS already extracted from
that paper's question paper. For each part, copy the corresponding model/expected answer out of
the marking scheme.

Rules:
- Match each part to the scheme by its label and question wording.
- Copy the scheme's answer faithfully; you may tidy obvious OCR artefacts. Keep it concise.
- If the scheme gives only marking *criteria* (points/keywords, not a usable answer) or does not
  cover a part, return "" for that pid — a later stage will author a full answer.
- Echo every `pid` exactly as given. Do NOT invent content that isn't in the scheme.
- Return ONLY via the emit_scheme_answers tool.

=== MARKING SCHEME ===
{scheme[:MAX_SCHEME_CHARS]}

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
                    out.append({"pid": str(a["pid"]).strip(),
                                "answer": (a.get("answer") or "").strip()})
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
    canonical = json.loads((CANONICAL / f"{subject}.json").read_text())
    by_id = {q["id"]: q for q in canonical}
    outs = bridge.outputs(_stage(subject))
    filled = 0
    for _cid, content in outs.items():
        for a in parse_result(content):
            pid, ans = a["pid"], a["answer"]
            if not ans or PID_SEP not in pid:
                continue
            qid, _, idx = pid.rpartition(PID_SEP)
            q = by_id.get(qid)
            if not q or not idx.isdigit():
                continue
            i = int(idx)
            if i < len(q["parts"]) and not (q["parts"][i].get("model") or "").strip():
                q["parts"][i]["model"] = ans
                q["parts"][i]["model_source"] = "scheme"
                filled += 1
    (CANONICAL / f"{subject}.json").write_text(json.dumps(canonical, ensure_ascii=False, indent=2))
    js = render_js(subject, canonical)
    print(f"\n[schemes] filled {filled} official answer(s) from marking schemes. Rendered: {js.name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject)
        print("nothing to do" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
