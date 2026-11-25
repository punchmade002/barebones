"""Merge and check Crunch Mode prerequisite drafts for one subject (see CRUNCH_MODE.md).

    python3 scripts/crunch_prereqs.py biology          # merge drafts/crunch/<subject>/prereqs-*.json
    python3 scripts/crunch_prereqs.py biology --check  # check content/crunch/<subject>-prerequisites.json only

Writes content/crunch/<subject>-prerequisites.json (not content/<subject>/, which
build_notes.py reads as subsections) and drafts/crunch/<subject>/review.md.
"""
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def subsections(subject):
    from crunch_points import items
    return set(items(subject))


def problems(links, ids):
    errs = []
    for sid in ids - links.keys():
        errs.append(f"missing subsection {sid}")
    for sid, needs in links.items():
        if sid not in ids:
            errs.append(f"unknown subsection {sid}")
        seen = set()
        for link in needs:
            n = link.get("needs")
            if n not in ids:
                errs.append(f"{sid} needs unknown {n}")
            if n == sid:
                errs.append(f"{sid} needs itself")
            if n in seen:
                errs.append(f"{sid} needs {n} twice")
            seen.add(n)
            if link.get("strength") not in ("essential", "helpful"):
                errs.append(f"{sid}->{n} bad strength {link.get('strength')}")
            if link.get("confidence") not in ("high", "low"):
                errs.append(f"{sid}->{n} bad confidence {link.get('confidence')}")
            if not link.get("why"):
                errs.append(f"{sid}->{n} has no reason")
    return errs


def cycles(links):
    """Return each cycle once, as a list of ids. Cycles break 'downstream' scoring, so a human picks which link to drop."""
    found, state, stack = [], {}, []

    def visit(node):
        state[node] = 1
        stack.append(node)
        for link in links.get(node, []):
            nxt = link["needs"]
            if state.get(nxt) == 1:
                found.append(stack[stack.index(nxt):] + [nxt])
            elif nxt not in state:
                visit(nxt)
        stack.pop()
        state[node] = 2

    for node in sorted(links):
        if node not in state:
            visit(node)
    return found


def review(subject, links, cyc):
    rows = [(s, l) for s, needs in links.items() for l in needs]
    low = [r for r in rows if r[1]["confidence"] == "low"]
    rng = random.Random(0)
    sample = rng.sample([r for r in rows if r[1]["confidence"] == "high"], min(30, len(rows) - len(low)))
    line = lambda s, l: f"- [ ] `{s}` needs `{l['needs']}` ({l['strength']}): {l['why']}"
    out = [f"# {subject} prerequisite review", "", "Tick to keep; write a note on any you'd change or drop.", ""]
    if cyc:
        out += ["## Cycles (drop at least one link in each)", ""]
        for c in cyc:
            out += [f"**{' → '.join(c)}**", ""]
            out += [line(a, l) for a, b in zip(c, c[1:]) for l in links[a] if l["needs"] == b] + [""]
    out += [f"## Low confidence ({len(low)})", ""] + [line(*r) for r in sorted(low, key=lambda r: (r[0], r[1]["needs"]))]
    out += ["", f"## Random sample of high confidence ({len(sample)})", ""] + [line(*r) for r in sorted(sample, key=lambda r: (r[0], r[1]["needs"]))]
    return "\n".join(out) + "\n"


def main():
    subject, check = sys.argv[1], "--check" in sys.argv
    target = ROOT / "content" / "crunch" / f"{subject}-prerequisites.json"
    ids = subsections(subject)
    if check:
        links = json.loads(target.read_text())
    else:
        links = {}
        for p in sorted((ROOT / "drafts" / "crunch" / subject).glob("prereqs-*.json")):
            links.update(json.loads(p.read_text()))
    errs = problems(links, ids)
    cyc = cycles({s: [l for l in v if l.get("needs") in ids] for s, v in links.items()})
    n = sum(len(v) for v in links.values())
    print(f"{len(links)} subsections, {n} links, {len(cyc)} cycles, {len(errs)} problems")
    for e in errs:
        print(" ", e)
    if errs or check:
        return 1 if errs else 0
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(dict(sorted(links.items())), indent=1, ensure_ascii=False) + "\n")
    (ROOT / "drafts" / "crunch" / subject / "review.md").write_text(review(subject, links, cyc))
    print(f"wrote {target.relative_to(ROOT)} and drafts/crunch/{subject}/review.md")
    return 0


if __name__ == "__main__":
    # self-check: a 2-cycle and a bad link are caught
    t = {"a": [{"needs": "b", "strength": "essential", "why": "x", "confidence": "high"}],
         "b": [{"needs": "a", "strength": "helpful", "why": "y", "confidence": "low"}, {"needs": "z", "strength": "?", "why": "", "confidence": "high"}]}
    assert cycles(t) == [["a", "b", "a"]], cycles(t)
    assert len(problems(t, {"a", "b"})) == 3, problems(t, {"a", "b"})
    sys.exit(main())
