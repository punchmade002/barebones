"""Split big Crunch point packages into parts, and join the parts' agent outputs.

    python3 drafts/crunch/geography/parts.py split   # points/<sid>.txt over LIMIT items -> points/<sid>.partN.txt
    python3 drafts/crunch/geography/parts.py join    # point-links/<sid>.partN.json -> point-links/<sid>.json

Each part keeps the whole package's candidates, and the subsection's other items become candidates too,
so links inside the subsection are still possible. Parts break at block boundaries.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIMIT = 250


def split():
    made = []
    for f in sorted((HERE / "points").glob("*.txt")):
        if ".part" in f.name:
            continue
        head, _, rest = f.read_text().partition("\n\n")
        lines = head.splitlines()
        target, items = lines[0], lines[1:]
        if len(items) <= LIMIT:
            continue
        sid = f.stem
        blocks = {}
        for line in items:
            blocks.setdefault(re.match(r"\[[^.]+\.(\d+)\.", line).group(1), []).append(line)
        parts, cur = [], []
        for b in blocks.values():
            if cur and len(cur) + len(b) > LIMIT:
                parts.append(cur)
                cur = []
            cur += b
        parts.append(cur)
        for n, part in enumerate(parts, 1):
            others = [l for l in items if l not in part]
            text = [target.replace(f"TARGET {sid}:", f"TARGET {sid} (part {n} of {len(parts)}):")] + part
            text += ["", f"CANDIDATES {sid} (the rest of this subsection):"] + others
            (HERE / "points" / f"{sid}.part{n}.txt").write_text("\n".join(text) + ("\n\n" + rest if rest else "\n"))
        f.rename(f.with_suffix(".whole"))
        made.append((sid, len(items), len(parts)))
    for m in made:
        print("split %s: %d items into %d parts" % m)


def join():
    src = HERE / "point-links"
    groups = {}
    for f in src.glob("*.part*.json"):
        groups.setdefault(f.name.split(".part")[0], []).append(f)
    for sid, fs in sorted(groups.items()):
        expected = len(list((HERE / "points").glob(f"{sid}.part*.txt")))
        if len(fs) < expected:
            print(f"{sid}: {len(fs)} of {expected} parts done")
            continue
        merged = {}
        for f in sorted(fs, key=lambda p: int(p.name.split(".part")[1].split(".")[0])):
            merged.update(json.loads(f.read_text()))
        (src / f"{sid}.json").write_text(json.dumps(merged, indent=0, ensure_ascii=False))
        print(f"joined {sid}: {len(merged)} items from {len(fs)} parts")


if __name__ == "__main__":
    {"split": split, "join": join}[sys.argv[1]]()
