#!/usr/bin/env python3
"""Rewrite existing subsection notes to course-outlines/NOTES_STANDARD.md, one agent per subsection.

    python3 scripts/notes_rewrite.py prep biology            # brief + one job file per subsection still to do
    python3 scripts/notes_rewrite.py check biology bio7-s2   # check <loId>.new.json; apply it if it has no errors
    python3 scripts/notes_rewrite.py report biology          # re-check every applied rewrite against its old notes

Work files live in drafts/notes-rewrite/<subject>/ (git-ignored): BRIEF.md (the parts of the standard a
rewrite needs), <loId>.job.md (old notes + package), <loId>.old.json (old notes, the baseline for checks)
and <loId>.new.json (the agent's new notes array). Only the notes array of content/<subject>/<loId>.json
is replaced; keyTerms, factCards and questions stay byte-identical.
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_notes  # noqa: E402

ROOT = build_notes.ROOT
STANDARD = ROOT / "course-outlines" / "NOTES_STANDARD.md"
BRIEF_SECTIONS = ("The goal", "Rules", "Block types to use", "Worked example (biology)",
                  "Rewriting existing notes", "Quality checks before finishing a subsection")
EXPLAIN = re.compile(r"\b(because|so|so that|therefore|which means|this means|this is why|that is why|as a result|in other words|"
                     r"in order to|due to|for example|such as|e\.g\.|for instance|this allows|allowing|which)\b", re.I)
META = re.compile(r"\b(this block|this section|these notes|described in|explained in|covered in|next block|as (mentioned|described) above|(?-i:see [A-Z]))", re.I)
EQUATION = re.compile(r"[^\s,;:()]+(?:\s*\+\s*[^\s,;:()]+)*\s*(?:→|⇌)\s*[^\s,;:()]+(?:\s*\+\s*[^\s,;:()]+)*")
NUMBER = re.compile(r"(?<![\w₀-₉⁰-⁹])\d+(?:\.\d+)?(?![₀-₉⁰-⁹])")


def work(subject: str) -> Path:
    return ROOT / "drafts" / "notes-rewrite" / subject


def sections(md: str) -> dict[str, str]:
    parts = re.split(r"^## ", md, flags=re.M)
    return {p.split("\n", 1)[0].strip(): "## " + p for p in parts[1:]}


def brief(subject: str) -> str:
    secs = sections(STANDARD.read_text())
    keep = [secs[s] for s in BRIEF_SECTIONS[:3]] + [secs[f"Subject notes: {subject}"]] + [secs[s] for s in BRIEF_SECTIONS[3:]]
    text = "\n".join(keep).replace(" Read one of them in full before writing.", "")
    return (
        "# Rewriting notes: the brief\n\n"
        "You are rewriting one subsection's notes. Your job file holds the old notes and the information package. "
        "Don't open other files: everything you need is here and in the job file.\n\n"
        "Write the new notes as a JSON array of blocks, each {\"h\", \"b\", \"points\", \"tip\"} (tip optional), "
        "to the path the job file gives, then run the check command it gives. The check applies your notes "
        "when there are no errors. Fix every error and re-run. Then deal with each warning: fix it, or leave it only "
        "if it is a false alarm (say which in your final reply).\n\n" + text
    )


def strip_package(md: str) -> str:
    md = re.sub(r"^## 5\. Practice questions.*", "", md, flags=re.M | re.S)
    return re.sub(r"^- \*\*Prepared by:\*\*.*?(?=^\S|^- |\Z)", "", md, flags=re.M | re.S).strip()


def is_done(notes: list) -> bool:
    return any(isinstance(n, dict) and n.get("tip") for n in notes)


def prep(subject: str) -> list[str]:
    out = work(subject)
    out.mkdir(parents=True, exist_ok=True)
    (out / "BRIEF.md").write_text(brief(subject))
    todo = []
    for path in sorted((ROOT / "content" / subject).glob("*.json")):
        data = json.loads(path.read_text())
        lo = data["loId"]
        package = ROOT / "course-outlines" / "packages" / subject / f"{lo}.md"
        if is_done(data["notes"]) or not package.exists():
            continue
        (out / f"{lo}.old.json").write_text(json.dumps(data["notes"], ensure_ascii=False, indent=1))
        old = "\n".join(json.dumps(n, ensure_ascii=False) for n in data["notes"])
        (out / f"{lo}.job.md").write_text(
            f"# Job: {lo} ({data.get('subsection', '')})\n\n"
            f"Write the new notes array to: drafts/notes-rewrite/{subject}/{lo}.new.json\n"
            f"Then run: python3 scripts/notes_rewrite.py check {subject} {lo}\n\n"
            f"## Old notes (one block per line)\n\n{old}\n\n"
            f"# Information package\n\n{strip_package(package.read_text())}\n"
        )
        todo.append(lo)
    return todo


def text_of(notes: list, tips: bool = True) -> str:
    parts = []
    for n in notes:
        parts += [n.get("h", ""), n.get("b", "")] + list(n.get("points", []))
        if tips:
            parts.append(n.get("tip", ""))
    return "\n".join(parts)


def prose_words(notes: list) -> int:
    """Words in leads and non-diagram points: what the old notes had, so the two compare fairly."""
    t = [n.get("b", "") for n in notes] + [p for n in notes for p in n.get("points", []) if not p.startswith("Diagram:")]
    return len(re.findall(r"\w+", " ".join(t)))


def squash(s: str) -> str:
    return re.sub(r"\s+", "", s)


def stem(w: str) -> str:
    return w.lower()[:6]


def checks(new: list, old: list, package: str, chapter: str = "", terms: tuple = ()) -> list[str]:
    """Warnings comparing the new notes with the old ones and the package (errors come from build_notes).

    chapter: text of the chapter's other notes, old and new, where an equation may already be written.
    terms: the subsection's key term and fact card names; dropping one from the notes is flagged.
    """
    warns = []
    new_text, old_text = text_of(new), text_of(old)
    ratio = prose_words(new) / max(1, prose_words(old))
    if ratio < 1.0:
        warns.append(f"the notes are shorter than before ({ratio:.2f}x the old words, leads and points only); "
                     "rewrites usually grow 20-50%, so a fact has probably been dropped or merged")
    sources = squash(old_text + package + chapter)
    for eq in sorted(set(EQUATION.findall(new_text))):
        if squash(eq) not in sources:
            warns.append(f"equation not found character for character in the old notes or package: {eq!r}")
    new_nums = set(NUMBER.findall(new_text))
    lost = sorted(set(NUMBER.findall(old_text)) - new_nums, key=lambda x: float(x))
    if lost:
        warns.append(f"numbers in the old notes that are missing now: {', '.join(lost)}")
    words = lambda s: {stem(w) for w in re.findall(r"[A-Za-z]{5,}", s)}
    old_stems, new_stems = words(old_text), words(new_text)
    dropped = sorted({t for t in terms if (words(t) & old_stems) - new_stems})
    if dropped:
        warns.append(f"key terms the old notes used that the new notes no longer mention: {'; '.join(dropped)}")
    old_diag = sum(p.startswith("Diagram:") for n in old for p in n.get("points", []))
    new_diag = sum(p.startswith("Diagram:") for n in new for p in n.get("points", []))
    if new_diag < old_diag:
        warns.append(f"{old_diag - new_diag} fewer Diagram: bullets than the old notes")
    hl = lambda ns: sum(n.get("h", "").endswith("(Higher Level only)") for n in ns)
    if hl(old) and not hl(new):
        warns.append("the old notes had Higher Level only blocks; the new notes have none")
    points = [p for n in new for p in n.get("points", []) if not p.startswith("Diagram:")]
    explained = sum(bool(EXPLAIN.search(p)) for p in points)
    if points and explained * 3 < len(points):
        warns.append(f"only {explained} of {len(points)} bullets give a reason or example (aim for a third)")
    for i, n in enumerate(new):
        where = f"block {i + 1} ({n.get('h', '')[:40]})"
        if not n.get("b"):
            warns.append(f"{where}: no lead (b)")
        elif len(re.findall(r"[.!?](\s|$)", n["b"])) > 3:
            warns.append(f"{where}: lead is over three sentences")
        if len(n.get("points", [])) > 9:
            warns.append(f"{where}: {len(n['points'])} points; split the block")
        for j, p in enumerate(n.get("points", [])):
            if len(p.split()) > 50:
                warns.append(f"{where} point {j + 1}: {len(p.split())} words; split it")
        for field in [n.get("b", ""), n.get("tip", "")] + list(n.get("points", [])):
            m = META.search(field)
            if m:
                warns.append(f"{where}: meta-text or hand-off {m.group(0)!r}; say the thing instead")
    return warns


def splice(path: Path, notes: list) -> str:
    orig = path.read_text()
    start, end = orig.index('"notes": ['), orig.index('"keyTerms"')
    body = json.dumps(notes, ensure_ascii=False, indent=2).replace("\n", "\n  ")
    out = orig[:start] + '"notes": ' + body + ",\n  " + orig[end:]
    a, b = json.loads(out), json.loads(orig)
    assert a["notes"] == notes and all(a[k] == b[k] for k in b if k != "notes"), "splice changed more than notes"
    return out


def check(subject: str, lo: str, apply: bool = True) -> int:
    w = work(subject)
    try:
        new = json.loads((w / f"{lo}.new.json").read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: can't read {lo}.new.json ({exc})")
        return 1
    if isinstance(new, dict):
        new = new.get("notes", new)
    if not isinstance(new, list):
        print("error: the file must hold a JSON array of blocks")
        return 1
    old = json.loads((w / f"{lo}.old.json").read_text())
    path = ROOT / "content" / subject / f"{lo}.json"
    merged = splice(path, new)
    los = build_notes.outcome_ids(subject)
    build_notes.INTERNAL_IDS.update(los, los.values())
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp) / path.name
        tmp_path.write_text(merged)
        _, errors = build_notes.validate(tmp_path, los)
    errors += [f"block {i + 1}: missing lead (b)" for i, n in enumerate(new) if isinstance(n, dict) and not n.get("b")]
    package = strip_package((ROOT / "course-outlines" / "packages" / subject / f"{lo}.md").read_text())
    chapter = lo.rsplit("-", 1)[0]
    others = [p for p in (ROOT / "content" / subject).glob(f"{chapter}-s*.json") if p != path]
    others += [p for p in w.glob(f"{chapter}-s*.old.json") if p.name != f"{lo}.old.json"]
    data = json.loads(path.read_text())
    terms = tuple(t["term"] for t in data.get("keyTerms", []) + data.get("factCards", []))
    warns = checks(new, old, package, "".join(p.read_text() for p in others), terms) if not errors else []
    for e in errors:
        print(f"error: {e}")
    for x in warns:
        print(f"warning: {x}")
    if errors:
        print(f"{lo}: {len(errors)} error(s); not applied")
        return 1
    if apply:
        path.write_text(merged)
    print(f"{lo}: {'applied' if apply else 'ok'}; {len(warns)} warning(s); "
          f"{prose_words(new)} words vs {prose_words(old)} before")
    return 0


def report(subject: str) -> int:
    for old in sorted(work(subject).glob("*.old.json")):
        lo = old.name.removesuffix(".old.json")
        if (work(subject) / f"{lo}.new.json").exists():
            check(subject, lo, apply=False)
        else:
            print(f"{lo}: not written")
    return 0


def self_test() -> None:
    old = [{"h": "A", "points": ["Water is split: 2H₂O → 4H⁺ + 4e⁻ + O₂, in 2 steps.", "Chlorophyll absorbs light."]}]
    good = [{"h": "A", "b": "Lead.", "points": ["Water is split: 2H₂O → 4H⁺ + 4e⁻ + O₂, in 2 steps, because light gives energy.",
                                                 "Chlorophyll absorbs light, so energy enters."]}]
    assert checks(good, old, "chlorophyll photolysis") == [], checks(good, old, "chlorophyll photolysis")
    bad = [{"h": "A", "b": "Lead.", "points": ["Water is split: H₂O → H⁺ + O₂."]}]
    msgs = " ".join(checks(bad, old, "chlorophyll", terms=("Chlorophyll",)))
    assert "equation not found" in msgs and "numbers" in msgs and "Chlorophyll" in msgs and "shorter" in msgs, msgs
    assert not checks(bad, old, "", "H₂O → H⁺ + O₂")[0].startswith("equation"), "chapter text counts as a source"
    assert not any("hand-off" in m for m in checks([dict(good[0], b="We see the cell.")], old, ""))
    assert strip_package("# P\n- **Prepared by:** x\n  y\n## 1. Must\nz\n## 5. Practice questions\nq") == "# P\n## 1. Must\nz"


if __name__ == "__main__":
    self_test()
    cmd, subject, *rest = sys.argv[1:] + [""] * (2 - len(sys.argv[1:]))
    if cmd == "prep":
        todo = prep(subject)
        print(f"{len(todo)} job(s) in {work(subject).relative_to(ROOT)}")
        print(json.dumps(todo))
    elif cmd == "check" and rest:
        sys.exit(check(subject, rest[0]))
    elif cmd == "report":
        sys.exit(report(subject))
    else:
        raise SystemExit(__doc__)
