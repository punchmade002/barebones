"""The syllabus topic taxonomy — the yardstick flashcard coverage is measured against.

Requirement: "flashcards should cover all examinable knowledge within a chapter". That is only
checkable if something independent of the generator states what the examinable knowledge IS.
The resource bundle already carries it: `guide-simplestudy.md` has a `## Unit and topic structure`
section listing every unit and its topics, validated by `resources.require_bundle`.

This module parses that taxonomy and scores a generated deck against it. Two consumers:

  * `flashcards.py` — feeds each chapter its topic list so generation AIMS at full coverage.
  * `gate.py`       — measures what actually came back, and blocks a publish that skipped
                      too much of the course.

Coverage is deliberately measured by token overlap rather than an exact string match. A card
titled "Pasteurisation" covers the topic "Pasteurisation and Sterilisation"; demanding the
topic's literal wording would report that as a miss and make the whole check noise.

    python3 syllabus.py history            # print the parsed taxonomy
    python3 syllabus.py history --coverage # score the generated deck against it
"""
from __future__ import annotations
import json
import re
import sys

from config import CANONICAL, RESOURCES

# `1. **Unit Name** — topic; topic; topic.` — the unit line opens the entry; the topic list may
# wrap across indented continuation lines, so entries are joined before splitting.
_UNIT_RE = re.compile(r"^\s*\d+\.\s+\*\*(?P<unit>.+?)\*\*\s*(?:[—–-]\s*(?P<topics>.*))?$")
_SECTION_RE = re.compile(r"^##\s+Unit and topic structure\s*$", re.I)
_NEXT_SECTION_RE = re.compile(r"^##\s+")

# Units that describe how the subject is EXAMINED rather than what must be learned. They are
# real syllabus content but produce no flashcards, so counting them would permanently cap
# coverage below 100% and train everyone to ignore the number.
_NON_CONTENT_UNIT_RE = re.compile(r"^\s*(assessment|examination|exam structure|"
                                  r"coursework|practical assessment)\s*$", re.I)

# Words carrying no discriminating power when matching a topic to a card.
_STOPWORDS = frozenset("""
a an and the of in on to for with without from into as at by or nor but its their there here
is are was were be been being this that these those it he she they we you i not no
case study studies topic topics unit units section sessions introduction overview
""".split())

_TOKEN_RE = re.compile(r"[a-z0-9]+")

# Share of a topic's significant tokens that must appear in one card for it to count as covered.
MATCH_RATIO = 0.6


def guide_path(subject: str):
    return RESOURCES / subject / "guide-simplestudy.md"


def _entries(text: str) -> list[str]:
    """The raw `1. **Unit** — topics` entries of the taxonomy section, each rejoined to one line."""
    lines, inside, buf, out = text.splitlines(), False, [], []
    for line in lines:
        if _SECTION_RE.match(line):
            inside = True
            continue
        if inside and _NEXT_SECTION_RE.match(line):
            break
        if not inside:
            continue
        if _UNIT_RE.match(line):
            if buf:
                out.append(" ".join(buf))
            buf = [line.strip()]
        elif buf and line.strip():
            buf.append(line.strip())          # indented continuation of the current entry
        elif buf and not line.strip():
            out.append(" ".join(buf))
            buf = []
    if buf:
        out.append(" ".join(buf))
    return out


def units(subject: str) -> list[dict]:
    """[{unit, topics[]}] from the bundle's guide. [] when the subject has no guide — callers
    treat that as "cannot verify" and say so, rather than reporting perfect coverage."""
    path = guide_path(subject)
    if not path.exists():
        return []
    out = []
    for entry in _entries(path.read_text()):
        m = _UNIT_RE.match(entry)
        if not m:
            continue
        unit = m.group("unit").strip()
        if _NON_CONTENT_UNIT_RE.match(unit):
            continue
        raw = (m.group("topics") or "").strip().rstrip(".")
        topics = [t.strip() for t in raw.split(";") if t.strip()] or [unit]
        out.append({"unit": unit, "topics": topics})
    return out


def topics(subject: str) -> list[str]:
    """Every examinable topic, flat and de-duplicated, in syllabus order."""
    seen, out = set(), []
    for u in units(subject):
        for t in u["topics"]:
            key = t.lower()
            if key not in seen:
                seen.add(key)
                out.append(t)
    return out


def topics_for(subject: str, chapter_title: str, limit: int = 12) -> list[str]:
    """The topics most likely to belong to a scaffold chapter, best first.

    Chapters are generated from the same bundle but do not carry the guide's unit ids, so the
    link is made by name: a unit whose title overlaps the chapter's contributes all its topics,
    then individual topics are matched. Used to steer generation, never to score it.
    """
    want = _significant(chapter_title)
    if not want:
        return []
    scored: list[tuple[float, str]] = []
    for u in units(subject):
        unit_score = _overlap(want, _significant(u["unit"]))
        for t in u["topics"]:
            score = max(unit_score, _overlap(want, _significant(t)))
            if score > 0:
                scored.append((score, t))
    scored.sort(key=lambda s: -s[0])
    out, seen = [], set()
    for _score, t in scored:
        if t.lower() not in seen:
            seen.add(t.lower())
            out.append(t)
        if len(out) >= limit:
            break
    return out


def _stem(word: str) -> str:
    """Crude singular/plural fold so "Enzymes" matches "Enzyme"."""
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def _significant(text: str) -> set[str]:
    return {_stem(w) for w in _TOKEN_RE.findall((text or "").lower())
            if w not in _STOPWORDS and len(w) > 2}


def _overlap(want: set[str], have: set[str]) -> float:
    return len(want & have) / len(want) if want else 0.0


def _card_tokens(card: dict) -> set[str]:
    return _significant(f"{card.get('term', '')} {card.get('definition', '')}")


def coverage(subject: str, by_chapter: dict[str, list]) -> dict:
    """Score a generated deck against the guide's taxonomy.

    A topic counts as covered when a SINGLE card carries at least MATCH_RATIO of its
    significant tokens — spreading the words across the whole deck is not coverage of that
    topic. `verifiable` is False when the subject has no guide, so the gate can distinguish
    "nothing to check against" from "checked and complete".
    """
    all_topics = topics(subject)
    if not all_topics:
        return {"verifiable": False, "total": 0, "covered": 0, "missing": [], "rate": 0.0}
    card_sets = [_card_tokens(c) for deck in by_chapter.values() for c in deck]
    covered, missing = [], []
    for t in all_topics:
        want = _significant(t)
        if want and any(_overlap(want, have) >= MATCH_RATIO for have in card_sets):
            covered.append(t)
        else:
            missing.append(t)
    return {"verifiable": True, "total": len(all_topics), "covered": len(covered),
            "missing": missing, "rate": round(len(covered) / len(all_topics), 4)}


def _load_cards(subject: str) -> dict[str, list]:
    path = CANONICAL / f"flashcards.{subject}.json"
    return json.loads(path.read_text()) if path.exists() else {}


if __name__ == "__main__":
    args = sys.argv[1:]
    subj = next((a for a in args if not a.startswith("-")), "history")
    if "--coverage" in args:
        rep = coverage(subj, _load_cards(subj))
        if not rep["verifiable"]:
            raise SystemExit(f"no guide taxonomy for {subj} — cannot verify coverage")
        print(f"{subj}: {rep['covered']}/{rep['total']} topics covered ({rep['rate']:.0%})")
        for t in rep["missing"]:
            print(f"  MISSING  {t}")
    else:
        for u in units(subj):
            print(f"{u['unit']}")
            for t in u["topics"]:
                print(f"    - {t}")
