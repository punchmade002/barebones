#!/usr/bin/env python3
"""List names and numbers in authored notes that their information package doesn't contain.

The writing model may only use facts from its package (course-outlines/packages/). This is a
review aid, not a gate: capitalised sentence openers show up too, so read the list by eye.
A trailing * means the word appears in some other package of the subject.

    python3 scripts/check_package_names.py geography [loId ...]
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = re.compile(r"\b[A-Z][a-zà-ž'’]+(?:[ -](?:[A-Z][a-zà-ž'’]+|de|del|of|du))*\b")
NUMBER = re.compile(r"\b\d[\d,.]*\b")


def main(subject: str, only: list[str]) -> None:
    packages = ROOT / "course-outlines" / "packages" / subject
    every = " ".join(p.read_text().lower() for p in packages.glob("*.md"))
    for path in sorted((ROOT / "content" / subject).glob("*.json")):
        if only and path.stem not in only:
            continue
        package = packages / f"{path.stem}.md"
        if not package.exists():
            print(f"{path.stem}: no package")
            continue
        own = package.read_text().lower()
        data = json.loads(path.read_text())
        text = " ".join(
            [block.get("b", "") + " " + " ".join(block.get("points", [])) for block in data["notes"]]
            + [q["model"] for q in data.get("questions", [])]
        )
        found = {re.sub(r"^(The|A|An) ", "", w) for w in NAME.findall(text)} | set(NUMBER.findall(text))
        found = {re.sub(r"['’]s$", "", w) for w in found}
        missing = sorted(w for w in found if len(w) > 2 and w.lower() not in own)
        listed = ", ".join(w + ("*" if w.lower() in every else "") for w in missing)
        print(f"{path.stem}: {listed or 'ok'}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: python3 scripts/check_package_names.py <subject> [loId ...]")
    main(sys.argv[1], sys.argv[2:])
