"""Crunch point packages for big subjects: a grid of target chunks x candidate groups, each about BUDGET bytes.

    python3 drafts/crunch/geography/parts.py build   # -> drafts/crunch/geography/packs/<sid>.t<T>g<G>.txt + packs.json
    python3 drafts/crunch/geography/parts.py join    # point-links/<sid>.t*g*.json -> point-links/<sid>.json (then crunch_points.py merge)

Geography packages built the Biology way are ~3x bigger (median 92 KB, max 272 KB), past what agents read reliably.
So each target chunk (<= CHUNK items) is paired with candidate groups packed up to BUDGET: group 1 holds the
target's own subsection and rates cost + links; later groups add links only. Join unions the links.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from crunch_points import items  # noqa: E402

SUBJECT = HERE.name
BUDGET = 75_000
CHUNK = 200


def lines(rows):
    return [f"[{i}] {t}" for i, t, _ in rows]


def build(keep=()):
    """keep: subsection ids whose packages are already out with agents; their files and index entries are left as they are."""
    all_items = items(SUBJECT)
    prereqs = json.loads((ROOT / "content" / "crunch" / f"{SUBJECT}-prerequisites.json").read_text())
    out = HERE / "packs"
    out.mkdir(exist_ok=True)
    old = json.loads((HERE / "packs.json").read_text()) if (HERE / "packs.json").exists() else {}
    index = {k: v for k, v in old.items() if v["sid"] in keep}
    for f in out.glob("*.txt"):
        if f.name.split(".t")[0] not in keep:
            f.unlink()
    for sid, (title, rows) in all_items.items():
        if sid in keep:
            continue
        n = -(-len(rows) // CHUNK)
        size = -(-len(rows) // n)  # even chunks, so no 1-item leftover part
        chunks = [rows[i:i + size] for i in range(0, len(rows), size)]
        # candidate sections: the rest of this subsection first, then each needed subsection, split if one is too big
        sections = []
        for n in [sid] + [l["needs"] for l in prereqs.get(sid, [])]:
            t, rs = all_items[n]
            for k in range(0, len(rs), CHUNK):
                sections.append((n, t, rs[k:k + CHUNK]))
        for ti, chunk in enumerate(chunks, 1):
            own = {i for i, _, _ in chunk}
            head = [f"TARGET {sid}" + (f" (part {ti} of {len(chunks)})" if len(chunks) > 1 else "") + f": {title}"] + lines(chunk)
            size0 = len("\n".join(head).encode())
            groups, cur, size = [], [], size0
            for n, t, rs in sections:
                rs = [r for r in rs if r[0] not in own]
                if not rs:
                    continue
                block = ["", f"CANDIDATES {n}: {t}"] + lines(rs)
                b = len("\n".join(block).encode())
                if cur and size + b > BUDGET:
                    groups.append(cur)
                    cur, size = [], size0
                cur += block
                size += b
            groups.append(cur)
            for gi, g in enumerate(groups, 1):
                mode = "MODE: cost and links" if gi == 1 else "MODE: links only (another package rates cost)"
                name = f"{sid}.t{ti}g{gi}"
                (out / f"{name}.txt").write_text("\n".join([mode] + head + g) + "\n")
                index[name] = {"sid": sid, "cost": gi == 1, "targets": [i for i, _, _ in chunk]}
    (HERE / "packs.json").write_text(json.dumps(index, indent=0))
    sizes = sorted((p.stat().st_size for p in out.glob("*.txt")))
    print(f"{len(sizes)} packages for {len(all_items)} subsections, median {sizes[len(sizes) // 2] // 1000} KB, "
          f"max {sizes[-1] // 1000} KB, {sum(sizes) / 1e6:.1f} MB total, cost-rating packages {sum(v['cost'] for v in index.values())}")


def join():
    index = json.loads((HERE / "packs.json").read_text())
    src = HERE / "point-links"
    by_sid = {}
    for name, v in index.items():
        by_sid.setdefault(v["sid"], []).append(name)
    done = 0
    for sid, names in sorted(by_sid.items()):
        missing = [n for n in names if not (src / f"{n}.json").exists()]
        if missing:
            continue
        merged = {}
        for n in sorted(names, key=lambda n: not index[n]["cost"]):  # cost-rating packages first
            res = json.loads((src / f"{n}.json").read_text())
            for i in index[n]["targets"]:
                r = res.get(i, {})
                m = merged.setdefault(i, {"cost": None, "needs": []})
                if index[n]["cost"]:
                    m["cost"] = r.get("cost")
                seen = {l["id"] for l in m["needs"]}
                m["needs"] += [l for l in r.get("needs", []) if l.get("id") not in seen]
        (src / f"{sid}.json").write_text(json.dumps(merged, indent=0, ensure_ascii=False))
        done += 1
    print(f"joined {done} of {len(by_sid)} subsections")


def check_pack(name, res, index, pack_ids):
    """Problems with one package's output (crunch_points.check covers the joined file)."""
    v = index[name]
    errs = [f"missing {i}" for i in v["targets"] if i not in res]
    errs += [f"extra {i}" for i in res if i not in v["targets"]]
    for i, r in res.items():
        if v["cost"] and r.get("cost") not in (1, 2):
            errs.append(f"{i} bad cost")
        for l in r.get("needs", []):
            if l.get("id") not in pack_ids or l.get("id") == i:
                errs.append(f"{i} bad link {l.get('id')}")
    return errs


def check():
    """Validate every finished package output, then flag odd cost-rating packages (like biology/audit.py)."""
    import re
    import statistics
    index = json.loads((HERE / "packs.json").read_text())
    src = HERE / "point-links"
    bad, stats, done = {}, [], 0
    for name, v in index.items():
        f = src / f"{name}.json"
        if not f.exists():
            continue
        done += 1
        ids = set(re.findall(r"^\[([^\]]+)\]", (HERE / "packs" / f"{name}.txt").read_text(), re.M))
        try:
            res = json.loads(f.read_text())
        except ValueError as e:
            bad[name] = [f"does not parse: {e}"]
            continue
        errs = check_pack(name, res, index, ids)
        if errs:
            bad[name] = errs
        elif v["cost"]:
            n = len(res)
            stats.append((name, n, sum(r.get("cost") == 2 for r in res.values()) / n, sum(len(r.get("needs", [])) for r in res.values()) / n))
    print(f"{done} of {len(index)} packages done, {len(bad)} with problems")
    for k, e in bad.items():
        print(f"  {k}: {e[:3]}{' …' if len(e) > 3 else ''}")
    if len(stats) > 4:
        for col, label in ((2, "cost-2 rate"), (3, "links/item")):
            vals = [s[col] for s in stats]
            lo = statistics.mean(vals) - 2 * statistics.pstdev(vals)
            print(f"{label}: mean {statistics.mean(vals):.2f}; low (< {lo:.2f}):", [s[0] for s in stats if s[col] < lo])


if __name__ == "__main__":
    t = {"x": {"sid": "s", "cost": False, "targets": ["a"]}}
    assert check_pack("x", {"a": {"needs": [{"id": "b"}]}}, t, {"a", "b"}) == []
    assert len(check_pack("x", {"a": {"needs": [{"id": "z"}]}, "q": {}}, t, {"a", "b"})) == 2
    if sys.argv[1] == "build":
        build(keep=set(sys.argv[2:]))
    else:
        join()
