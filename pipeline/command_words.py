"""Count the instruction words ("Examine", "Describe and explain", "Name"…) each exam section uses,
from the past-paper PDFs in exam-papers/<subject>/, and store the most common in
pipeline/exam-info/<subject>.json as sections[].commandWords = {higher|ordinary: [[word, count], …]}.

    python3 pipeline/command_words.py geography          # write
    python3 pipeline/command_words.py geography --dry    # print only

Then re-render the app file:  python3 pipeline/command_words.py geography --render
A word counts once per question part, and only where it starts an instruction (line or sentence start),
so "Examine the OS map…" (an instruction to look, not to answer) is skipped.

shortcut: only Geography's paper layout is described in LAYOUTS; add a subject's sections there to extend.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YEARS = range(2017, 2027)
TOP = 6

# Longest first, so "Describe and explain" wins over "Describe"
WORDS = [
    "Describe and explain", "Examine how", "Account for", "With the aid of", "Distinguish between",
    "Examine", "Describe", "Explain", "Discuss", "Compare", "Contrast", "Assess", "Evaluate", "Analyse",
    "Outline", "Name", "Identify", "Calculate", "Draw", "State", "Explain briefly", "Give", "Suggest",
    "Locate", "Indicate", "Match", "Complete", "Classify", "Label", "Circle", "Tick", "Measure",
]
WORDS.sort(key=len, reverse=True)
# "Examine the OS map / photograph / figure…" is an instruction to look, not an answer task
LOOK_AT = re.compile(r"^Examine\b.{0,40}\b(map|photograph|figure|fig\.|chart|graph|table|diagram|image|data|legend|satellite|source)", re.I)
NUMBERING = re.compile(r"^(?:\d{1,2}[A-C]?\.|\([a-z]+\)|[a-z]\))\s+")  # "13.", "1B.", "(ii)", "a)" before the task
START = re.compile(r"(?:^|(?<=[.:?]\s))\s*(" + "|".join(re.escape(w) for w in WORDS) + r")\b", re.M)

# Per subject: section id → (paper part, question numbers or None for the whole part)
LAYOUTS = {
    "geography": {
        "geo-part1": ("one", None),
        "geo-section1": ("two", range(1, 4)),
        "geo-section2": ("two", range(4, 7)),
        "geo-section3": ("two", range(7, 13)),
        "geo-section4": ("two", range(13, 25)),
    },
}


def text(pdf: Path) -> str:
    return subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout


def parts(subject: str, year: int, level: str) -> dict[str, str]:
    """Part One and Part Two text of one paper, from split files (2020+) or one combined file."""
    d = ROOT / "exam-papers" / subject
    one, two = d / f"{year}-{level}-part-one.pdf", d / f"{year}-{level}-part-two.pdf"
    if one.exists() and two.exists():
        return {"one": text(one), "two": text(two)}
    whole = d / f"{year}-{level}-exam-paper.pdf"
    if not whole.exists():
        return {}
    t = text(whole)
    cut = re.search(r"PART TWO", t)
    return {"one": t[:cut.start()], "two": t[cut.start():]} if cut else {}


def questions(part_two: str) -> dict[int, str]:
    """Split Part Two on "Question N" headings, or "N.   " for the Options (13–24), keeping numbers increasing."""
    heads, last = [], 0
    for m in re.finditer(r"^\s*(?:Question\s+(\d+)\b|(\d{1,2})\.\s{2,})", part_two, re.M):
        n = int(m.group(1) or m.group(2))
        if n > last:
            heads.append((n, m))
            last = n
    return {n: part_two[m.end():(heads[i + 1][1].start() if i + 1 < len(heads) else len(part_two))]
            for i, (n, m) in enumerate(heads)}


def count(block: str) -> Counter:
    found = Counter()
    for line in block.splitlines():
        line = NUMBERING.sub("", line.strip())
        if LOOK_AT.match(line):
            continue
        for m in START.finditer(line):
            word = m.group(1)
            found["Examine" if word == "Examine how" else word] += 1
    return found


def collect(subject: str) -> dict[str, dict[str, Counter]]:
    """section id → level → word counts. Levels apart: Ordinary's short "Name…" parts would bury Higher's essays."""
    layout = LAYOUTS[subject]
    totals = {sid: {"higher": Counter(), "ordinary": Counter()} for sid in layout}
    for year in YEARS:
        for level in ("higher", "ordinary"):
            p = parts(subject, year, level)
            if not p:
                continue
            qs = questions(p["two"])
            for sid, (part, numbers) in layout.items():
                if part == "one":
                    totals[sid][level] += count(p["one"])
                else:
                    totals[sid][level] += sum((count(qs[n]) for n in numbers if n in qs), Counter())
    return totals


def main() -> None:
    subject = next((a for a in sys.argv[1:] if not a.startswith("-")), None)
    if subject not in LAYOUTS:
        raise SystemExit(f"usage: python3 pipeline/command_words.py <{'|'.join(LAYOUTS)}> [--dry] [--render]")
    path = ROOT / "pipeline" / "exam-info" / f"{subject}.json"
    data = json.loads(path.read_text())
    totals = collect(subject)
    for section in data["sections"]:
        words = totals.get(section["id"])
        if words is None:
            continue
        section["commandWords"] = {lvl: [[w, n] for w, n in c.most_common(TOP)] for lvl, c in words.items() if c}
        print(section["id"], section["commandWords"])
    data["commandWordYears"] = f"{YEARS[0]}–{YEARS[-1]}"
    if "--dry" in sys.argv:
        return
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    if "--render" in sys.argv:
        out = ROOT / f"{subject}-exam-info.js"
        out.write_text(
            "// Generated by pipeline/exam_info.py — edit pipeline/exam-info/"
            f"{subject}.json, not this file.\n"
            "window.EXAM_BREAKDOWN = window.EXAM_BREAKDOWN || {};\n"
            f"window.EXAM_BREAKDOWN[{json.dumps(subject)}] = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
        )
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
