"""Crunch Mode point-level packages (see CRUNCH_MODE.md).

Every note item gets a stable id: <subsection>.<block>.<point>, with "b" for the
block's explanation paragraph (e.g. bio13-s3.2.b, bio13-s3.2.4). Exam tips are not
items; they follow their block.

    python3 scripts/crunch_points.py biology         # write drafts/crunch/<subject>/points/<sid>.txt
    python3 scripts/crunch_points.py biology merge   # check agent output, write content/crunch/<subject>-points.json

Each package holds one subsection's items (to link and rate) plus the items of the
subsections it needs in content/crunch/<subject>-prerequisites.json (link candidates).
shortcut: a point can only link to its own subsection or a linked subsection, so a
missed subsection link hides point links; fix the subsection graph and re-run.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def items(subject):
    """{subsection: (title, [(item_id, text, hash)])} in note order."""
    out = {}
    for p in sorted((ROOT / "content" / subject).glob("*.json")):
        if "acronyms" in p.stem:
            continue
        d = json.loads(p.read_text())
        rows = []
        for i, block in enumerate(d["notes"]):
            texts = [("b", block.get("b", ""))] + list(enumerate(block.get("points", [])))
            for j, text in texts:
                if text.strip():
                    rows.append((f"{p.stem}.{i}.{j}", text, hashlib.sha1(text.encode()).hexdigest()[:8]))
        out[p.stem] = (d["subsection"], rows)
    return out


def package(sid, all_items, prereqs):
    title, own = all_items[sid]
    lines = [f"TARGET {sid}: {title}"] + [f"[{i}] {t}" for i, t, _ in own]
    for link in prereqs.get(sid, []):
        n = link["needs"]
        lines += ["", f"CANDIDATES {n}: {all_items[n][0]}"] + [f"[{i}] {t}" for i, t, _ in all_items[n][1]]
    return "\n".join(lines) + "\n"


def main():
    subject = sys.argv[1]
    all_items = items(subject)
    prereqs = json.loads((ROOT / "content" / "crunch" / f"{subject}-prerequisites.json").read_text())
    out = ROOT / "drafts" / "crunch" / subject / "points"
    out.mkdir(parents=True, exist_ok=True)
    sizes = []
    for sid in all_items:
        text = package(sid, all_items, prereqs)
        (out / f"{sid}.txt").write_text(text)
        sizes.append((len(text.encode()), sid))
    # index of every item's hash, so ratings/links can be checked for stale text later
    index = {i: h for _, rows in all_items.values() for i, _, h in rows}
    (out / "index.json").write_text(json.dumps(index, indent=0))
    sizes.sort()
    total = sum(s for s, _ in sizes)
    print(f"{len(index)} items in {len(sizes)} packages, {total // 1000} KB total, "
          f"median {sizes[len(sizes) // 2][0] // 1000} KB, largest {sizes[-1][0] // 1000} KB ({sizes[-1][1]})")
    print("over 60 KB:", [sid for s, sid in sizes if s > 60_000])


def check(own, package_ids, result):
    """Problems with one package's agent output."""
    errs = [f"missing {i}" for i in own if i not in result]
    errs += [f"extra {i}" for i in result if i not in own]
    for i, r in result.items():
        if r.get("cost") not in (1, 2):
            errs.append(f"{i} bad cost {r.get('cost')}")
        for l in r.get("needs", []):
            if l.get("id") not in package_ids or l.get("id") == i:
                errs.append(f"{i} bad link {l.get('id')}")
            if l.get("strength") not in ("essential", "helpful") or l.get("confidence") not in ("high", "low"):
                errs.append(f"{i}->{l.get('id')} bad strength/confidence")
    return errs


def merge(subject):
    """Check drafts/crunch/<subject>/point-links/*.json and write content/crunch/<subject>-points.json."""
    from crunch_prereqs import cycles
    all_items = items(subject)
    prereqs = json.loads((ROOT / "content" / "crunch" / f"{subject}-prerequisites.json").read_text())
    src = ROOT / "drafts" / "crunch" / subject / "point-links"
    merged, todo, bad = {}, [], {}
    for sid, (_, rows) in all_items.items():
        f = src / f"{sid}.json"
        if not f.exists():
            todo.append(sid)
            continue
        own = [i for i, _, _ in rows]
        pkg = set(own) | {i for l in prereqs.get(sid, []) for i, _, _ in all_items[l["needs"]][1]}
        result = json.loads(f.read_text())
        errs = check(own, pkg, result)
        if errs:
            bad[sid] = errs
            continue
        for i, _, h in rows:
            merged[i] = {"hash": h, **result[i]}
    print(f"{len(merged)} items merged, {len(todo)} packages not done, {len(bad)} packages with problems")
    for sid, errs in bad.items():
        print(f"  {sid}: {errs[:3]}{' …' if len(errs) > 3 else ''}")
    (ROOT / "drafts" / "crunch" / subject / "redo.txt").write_text("\n".join(todo + list(bad)) + "\n")
    links = {i: [{"needs": l["id"]} for l in r["needs"]] for i, r in merged.items()}
    cyc = cycles(links)
    n = sum(len(r["needs"]) for r in merged.values())
    print(f"{n} links, {sum(1 for r in merged.values() if r['cost'] == 2)} cost-2 items, {len(cyc)} cycles")
    target = ROOT / "content" / "crunch" / f"{subject}-points.json"
    target.write_text(json.dumps(merged, indent=0, ensure_ascii=False) + "\n")
    (ROOT / "drafts" / "crunch" / subject / "point-cycles.json").write_text(json.dumps(cyc, indent=0))
    return 1 if bad else 0


if __name__ == "__main__":
    block = {"b": "body", "points": ["p0", "  ", "p2"]}
    texts = [("b", block["b"])] + list(enumerate(block["points"]))
    ids = [f"x.0.{j}" for j, s in texts if s.strip()]
    assert ids == ["x.0.b", "x.0.0", "x.0.2"], ids
    ok = {"cost": 1, "needs": [{"id": "y", "strength": "helpful", "confidence": "low", "why": "w"}]}
    assert check(["x"], {"x", "y"}, {"x": ok}) == []
    assert len(check(["x", "z"], {"x"}, {"x": ok})) == 2  # missing z, bad link y
    sys.exit(merge(sys.argv[1]) if "merge" in sys.argv else main())
