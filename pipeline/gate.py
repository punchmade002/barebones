"""The publication gate — every check that must pass before a subject reaches the app.

The original gate gave three answers (placeholders, ai-h1 share, fabricated years) and nothing
about flashcards, ids, source labels, diagrams or coverage — so a subject could publish 939
cards, 158 of them duplicates, with source lines reading "LC Home-economics", and the gate
would call it clean.

Two deliberate design choices:

  * BLOCK vs WARN. A gate that blocks on everything gets bypassed with --force on the first
    run and then permanently. Only defects that make published content *wrong* block; quality
    signals report. Card-count budgets in particular are WARN by design — a hard cap on a
    model-generated deck is an instruction to discard content to hit a number, which is the
    failure it is meant to prevent.

  * Regression over absolutes. `check_regression` compares against a recorded baseline, so
    "this run produces 40% fewer answered parts than what is already live" is caught even when
    every absolute threshold passes. That is the check that actually protects existing content.

    python3 gate.py history              # human-readable report
    python3 gate.py history --snapshot   # record the current store as the baseline
"""
from __future__ import annotations
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from config import (CANONICAL, REPORTS, EXAM_IMAGES, ROOT, display_name,
                    SYLLABUS_COVERAGE_MIN, SYLLABUS_COVERAGE_GOOD)
import ids
import validate

BLOCK, WARN, INFO = "BLOCK", "WARN", "INFO"

# Quality thresholds. These shape WARN output; only AI_SHARE_MAX and the regression limits block.
AI_SHARE_MAX = 0.40             # share of answers that may be ai-h1 before it means segmentation failed
CARD_DUP_RATE_MAX = 0.05        # normalised-duplicate share of a subject's whole deck
CARDS_PER_CHAPTER = (12, 45)    # soft band; outside it is a report line, never a block
REGRESSION_BLOCK = 0.10         # >10% content loss vs baseline blocks
REGRESSION_WARN = 0.02          # >2% is worth saying out loud


class Finding:
    __slots__ = ("check", "severity", "message", "detail")

    def __init__(self, check: str, severity: str, message: str, detail=None):
        self.check, self.severity, self.message, self.detail = check, severity, message, detail

    def __repr__(self):
        return f"<{self.severity} {self.check}: {self.message}>"


class Ctx:
    """Everything the checks read, loaded once."""

    def __init__(self, subject: str):
        self.subject = subject
        self.canon = self._json(CANONICAL / f"{subject}.json") or []
        self.cards = self._json(CANONICAL / f"flashcards.{subject}.json") or {}
        self.scaffold = self._json(Path(__file__).parent / "scaffold" / f"{subject}.json") or {}
        self.baseline = self._json(REPORTS / f"baseline-{subject}.json")
        self.parts = [(q, p) for q in self.canon for p in q.get("parts", [])]

    @staticmethod
    def _json(p: Path):
        return json.loads(p.read_text()) if p.exists() else None


# ── checks ────────────────────────────────────────────────────────────────────
def check_store_exists(c: Ctx):
    if not c.canon:
        yield Finding("store", BLOCK, f"no canonical store for {c.subject} — run segment first")


def check_question_ids(c: Ctx):
    dups = ids.duplicate_ids(c.canon)
    if dups:
        eg = ", ".join(f"{k}×{v}" for k, v in list(dups.items())[:3])
        yield Finding("question-ids", BLOCK,
                      f"{len(dups)} duplicate question id(s) covering {sum(dups.values())} row(s) "
                      f"— e.g. {eg}; run `python3 migrate_ids.py {c.subject}`", dups)


def check_part_labels(c: Ctx):
    """Repeated part labels inside one question are a segmentation smell, not a fatal defect:
    the app addresses parts positionally, so nothing breaks — but it usually means the model
    merged or split parts wrongly."""
    bad = [q["id"] for q in c.canon
           if len({p.get("label") for p in q.get("parts", [])}) != len(q.get("parts", []))]
    if bad:
        yield Finding("part-labels", WARN,
                      f"{len(bad)} question(s) repeat a part label — e.g. {', '.join(bad[:3])}", bad)


def check_parts(c: Ctx):
    bad = [(q["id"], validate.part_problems(p)) for q, p in c.parts if validate.part_problems(p)]
    if bad:
        eg = f"{bad[0][0]}: {','.join(bad[0][1])}"
        yield Finding("parts", BLOCK, f"{len(bad)} placeholder/empty part(s) (e.g. {eg})",
                      [{"id": i, "problems": p} for i, p in bad[:50]])


def check_ai_share(c: Ctx):
    if not c.parts:
        return
    ai = sum(1 for _, p in c.parts if p.get("model_source") == "ai-h1") / len(c.parts)
    if ai > AI_SHARE_MAX:
        yield Finding("ai-share", BLOCK,
                      f"{ai:.0%} of answers are ai-h1 (>{AI_SHARE_MAX:.0%} cap) — usually a "
                      f"symptom of upstream segmentation failure", round(ai, 3))


def check_years(c: Ctx):
    fab = sorted({q.get("year") for q in c.canon
                  if not validate.year_is_real(c.subject, q.get("year"))})
    if fab:
        yield Finding("years", BLOCK, f"questions from non-acquired year(s): {fab}", fab)


def check_sources(c: Ctx):
    """Every source line must read 'LC <Display Name> <Level> <Year> — <label>'. This is what
    catches `.capitalize()` mangling ('LC Home-economics') and a stale display name."""
    want = display_name(c.subject)
    pat = re.compile(rf"^LC {re.escape(want)} (Higher|Ordinary) \d{{4}} — ")
    bad = [q["id"] for q in c.canon if not pat.match(q.get("source", ""))]
    if bad:
        sample = next((q["source"] for q in c.canon if q["id"] == bad[0]), "")
        yield Finding("sources", BLOCK,
                      f"{len(bad)} malformed source label(s); expected 'LC {want} …', "
                      f"got {sample!r}", bad[:50])


def check_diagrams(c: Ctx):
    missing = []
    for q, p in c.parts:
        rel = (p.get("diagram") or "").strip()
        if rel and not (ROOT / rel).exists():
            missing.append((q["id"], rel))
    if missing:
        yield Finding("diagrams", BLOCK,
                      f"{len(missing)} part(s) reference a diagram file that does not exist "
                      f"— e.g. {missing[0][1]}", [{"id": i, "path": r} for i, r in missing[:50]])
    total = sum(1 for _, p in c.parts if (p.get("diagram") or "").strip())
    if total:
        yield Finding("diagrams", INFO, f"{total} part(s) carry a diagram")


def check_flashcards(c: Ctx):
    if not c.cards:
        yield Finding("flashcards", WARN, "no flashcard store — run the flashcards stage")
        return
    empty = [(cid, i) for cid, deck in c.cards.items() for i, card in enumerate(deck)
             if not (card.get("term") or "").strip() or not (card.get("definition") or "").strip()]
    if empty:
        yield Finding("flashcards", BLOCK,
                      f"{len(empty)} flashcard(s) with an empty term or definition "
                      f"— e.g. {empty[0][0]}[{empty[0][1]}]", empty[:50])


def check_flashcard_duplicates(c: Ctx):
    """Duplicates ACROSS chapters. `flashcards.consolidate()` now removes these outright, so any
    survivor means that pass didn't run or didn't work — hence BLOCK rather than a tolerated rate.
    The requirement is zero duplicates between chapters, and a threshold cannot express zero."""
    if not c.cards:
        return
    norm = defaultdict(list)
    for cid, deck in c.cards.items():
        for card in deck:
            key = re.sub(r"\s+", " ", (card.get("term") or "").strip().lower())
            if key:
                norm[key].append(cid)
    total = sum(len(v) for v in norm.values())
    dup_groups = {k: v for k, v in norm.items() if len(v) > 1}
    dup_cards = sum(len(v) for v in dup_groups.values()) - len(dup_groups)
    rate = dup_cards / total if total else 0
    if dup_groups:
        eg = ", ".join(sorted(dup_groups)[:3])
        yield Finding("card-duplicates", BLOCK,
                      f"{len(dup_groups)} term(s) duplicated across chapters covering "
                      f"{dup_cards} redundant card(s) ({rate:.1%} of the deck) — e.g. {eg}. "
                      f"Re-run the flashcards stage; consolidate() should leave none.",
                      {"rate": round(rate, 4), "groups": len(dup_groups)})


def check_card_questions(c: Ctx):
    """Every flashcard must ask a real question. A card that shows the bare term ("Mitosis")
    is the defect this check exists for — the student sees a label, not a prompt."""
    if not c.cards:
        return
    import flashcards
    bad = [(cid, card.get("term", ""))
           for cid, deck in c.cards.items() for card in deck
           if not flashcards.is_usable_question(card.get("question", ""), card.get("term", ""))]
    total = sum(len(d) for d in c.cards.values())
    if bad:
        eg = "; ".join(f"{cid}:{term}" for cid, term in bad[:3])
        yield Finding("card-questions", BLOCK,
                      f"{len(bad)} of {total} flashcard(s) have no usable question — e.g. {eg}",
                      {"count": len(bad), "total": total})


def check_syllabus_coverage(c: Ctx):
    """Does the deck cover the course? Measured against the guide's own topic taxonomy, which is
    independent of whatever the generator chose to write about."""
    if not c.cards:
        return
    import syllabus
    cov = syllabus.coverage(c.subject, c.cards)
    if not cov["verifiable"]:
        yield Finding("syllabus-coverage", WARN,
                      f"no topic taxonomy in {c.subject}'s guide — flashcard coverage of the "
                      f"course could not be verified")
        return
    rate, missing = cov["rate"], cov["missing"]
    detail = {"rate": rate, "covered": cov["covered"], "total": cov["total"],
              "missing": missing[:40]}
    if rate < SYLLABUS_COVERAGE_MIN:
        eg = "; ".join(missing[:5]) + (" …" if len(missing) > 5 else "")
        yield Finding("syllabus-coverage", BLOCK,
                      f"flashcards cover only {cov['covered']}/{cov['total']} syllabus topics "
                      f"({rate:.0%}, floor {SYLLABUS_COVERAGE_MIN:.0%}) — missing e.g. {eg}", detail)
    elif rate < SYLLABUS_COVERAGE_GOOD:
        yield Finding("syllabus-coverage", WARN,
                      f"{len(missing)} syllabus topic(s) have no flashcard "
                      f"({cov['covered']}/{cov['total']} covered, {rate:.0%})", detail)
    else:
        yield Finding("syllabus-coverage", INFO,
                      f"flashcards cover {cov['covered']}/{cov['total']} syllabus topics ({rate:.0%})")


def check_question_timing(c: Ctx):
    """Every question should carry how long it ought to take. Missing timing means either
    exam_info never ran for this subject, or the parts have no marks to derive it from."""
    timed = [p for _q, p in c.parts if p.get("time_minutes")]
    if not c.parts:
        return
    from config import exam_info
    if not exam_info(c.subject):
        yield Finding("timing", WARN,
                      f"no exam-info store for {c.subject} — questions carry no time labels and "
                      f"answers were sized without a time budget; run the exam-info stage")
        return
    missing = len(c.parts) - len(timed)
    if missing:
        yield Finding("timing", WARN,
                      f"{missing} of {len(c.parts)} part(s) have no time label (usually missing "
                      f"marks)", {"missing": missing, "total": len(c.parts)})
    else:
        yield Finding("timing", INFO, f"all {len(c.parts)} part(s) carry a time label")


def check_card_budgets(c: Ctx):
    """Reports only. A hard cap would push the generator to drop content to hit a number."""
    if not c.cards:
        return
    lo, hi = CARDS_PER_CHAPTER
    out = [(cid, len(deck)) for cid, deck in sorted(c.cards.items()) if not lo <= len(deck) <= hi]
    total = sum(len(v) for v in c.cards.values())
    yield Finding("card-budget", INFO,
                  f"{total} cards across {len(c.cards)} chapters "
                  f"(mean {total / max(len(c.cards), 1):.0f})")
    if out:
        eg = ", ".join(f"{cid}={n}" for cid, n in out[:4])
        yield Finding("card-budget", WARN,
                      f"{len(out)} chapter(s) outside the {lo}-{hi} card band — {eg}", out)


def check_coverage(c: Ctx):
    """Every scaffold chapter should have questions and cards; an empty one means either the
    scaffold is wrong or segmentation missed a topic."""
    chapters = [ch["id"] for ch in c.scaffold.get("chapters", [])]
    if not chapters:
        return
    q_by_chapter = Counter(q.get("chapterId") for q in c.canon)
    no_q = [ch for ch in chapters if not q_by_chapter.get(ch)]
    if no_q:
        yield Finding("coverage", WARN,
                      f"{len(no_q)}/{len(chapters)} chapter(s) have no questions: "
                      f"{', '.join(no_q[:5])}", no_q)
    if c.cards:
        no_c = [ch for ch in chapters if not c.cards.get(ch)]
        if no_c:
            yield Finding("coverage", WARN,
                          f"{len(no_c)}/{len(chapters)} chapter(s) have no flashcards: "
                          f"{', '.join(no_c[:5])}", no_c)
    off = sorted({q.get("chapterId") for q in c.canon} - set(chapters) - {None, ""})
    if off:
        yield Finding("coverage", WARN,
                      f"{len(off)} question(s) tagged to chapter id(s) not in the scaffold: "
                      f"{', '.join(off[:5])}", off)


def _counts(c: Ctx) -> dict:
    return {
        "questions": len(c.canon),
        "parts": len(c.parts),
        "answered_parts": sum(1 for _, p in c.parts if (p.get("model") or "").strip()),
        "cards": sum(len(v) for v in c.cards.values()) if c.cards else 0,
        "diagrams": sum(1 for _, p in c.parts if (p.get("diagram") or "").strip()),
    }


def check_regression(c: Ctx):
    """Compare against the recorded baseline. This is the check that protects live content:
    absolute thresholds all pass happily while a run quietly halves the deck."""
    if not c.baseline:
        yield Finding("regression", INFO,
                      f"no baseline recorded — `python3 gate.py {c.subject} --snapshot` to set one")
        return
    now, was = _counts(c), c.baseline.get("counts", {})
    for field, current in now.items():
        before = was.get(field)
        if not before:                       # nothing to compare against, or grew from zero
            continue
        drop = (before - current) / before
        if drop > REGRESSION_BLOCK:
            yield Finding("regression", BLOCK,
                          f"{field}: {before} -> {current} ({drop:.0%} loss vs baseline "
                          f"of {c.baseline.get('recorded', 'unknown date')})",
                          {"field": field, "before": before, "after": current})
        elif drop > REGRESSION_WARN:
            yield Finding("regression", WARN,
                          f"{field}: {before} -> {current} ({drop:.0%} lower than baseline)",
                          {"field": field, "before": before, "after": current})


CHECKS = [check_store_exists, check_question_ids, check_part_labels, check_parts,
          check_ai_share, check_years, check_sources, check_diagrams, check_flashcards,
          check_flashcard_duplicates, check_card_questions, check_syllabus_coverage,
          check_card_budgets, check_coverage, check_question_timing, check_regression]


# ── api ───────────────────────────────────────────────────────────────────────
def run(subject: str) -> list[Finding]:
    c = Ctx(subject)
    if not c.canon:                                   # nothing else can run meaningfully
        return list(check_store_exists(c))
    out: list[Finding] = []
    for check in CHECKS:
        out += list(check(c))
    order = {BLOCK: 0, WARN: 1, INFO: 2}
    return sorted(out, key=lambda f: order[f.severity])


def blockers(subject: str) -> list[str]:
    """The merge gate's answer: human-readable reasons publishing must not proceed."""
    return [f.message for f in run(subject) if f.severity == BLOCK]


def snapshot(subject: str) -> dict:
    """Record the current store as the baseline future runs are compared against."""
    import datetime
    c = Ctx(subject)
    if not c.canon:
        raise SystemExit(f"no canonical store for {subject} — nothing to snapshot")
    data = {"subject": subject,
            "recorded": datetime.date.today().isoformat(),
            "id_scheme_version": ids.ID_SCHEME_VERSION,
            "counts": _counts(c)}
    (REPORTS / f"baseline-{subject}.json").write_text(json.dumps(data, indent=2))
    return data


def report(subject: str) -> str:
    findings = run(subject)
    c = Ctx(subject)
    n = _counts(c)
    lines = [f"=== gate: {subject} ===",
             f"{n['questions']} questions · {n['parts']} parts · {n['answered_parts']} answered "
             f"· {n['cards']} cards · {n['diagrams']} diagrams", ""]
    for sev in (BLOCK, WARN, INFO):
        group = [f for f in findings if f.severity == sev]
        if not group:
            continue
        lines.append(f"{sev} ({len(group)})")
        lines += [f"  [{f.check}] {f.message}" for f in group]
        lines.append("")
    verdict = "BLOCKED" if any(f.severity == BLOCK for f in findings) else "CLEAN — safe to merge"
    lines.append(verdict)
    return "\n".join(lines)


if __name__ == "__main__":
    args = sys.argv[1:]
    subj = next((a for a in args if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 gate.py <subject> [--snapshot] [--json]")
    if "--snapshot" in args:
        d = snapshot(subj)
        print(f"baseline recorded for {subj}: {d['counts']}")
    elif "--json" in args:
        print(json.dumps([{"check": f.check, "severity": f.severity, "message": f.message,
                           "detail": f.detail} for f in run(subj)], indent=2))
    else:
        print(report(subj))
        raise SystemExit(1 if blockers(subj) else 0)
