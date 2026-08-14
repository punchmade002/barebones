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
                    SUPPLIED_FIGURE_RE, SCAN_ALL_PARTS_FOR_FIGURES)
import ids
import textclean
import validate

BLOCK, WARN, INFO = "BLOCK", "WARN", "INFO"

# Quality thresholds. These shape WARN output; only AI_SHARE_MAX and the regression limits block.
AI_SHARE_MAX = 0.40             # share of answers that may be ai-h1 before it means segmentation failed
CARD_DUP_RATE_MAX = 0.05        # normalised-duplicate share of a subject's whole deck
CARDS_PER_CHAPTER = (12, 45)    # soft band; outside it is a report line, never a block
REGRESSION_BLOCK = 0.10         # >10% content loss vs baseline blocks
REGRESSION_WARN = 0.02          # >2% is worth saying out loud
TEXT_ARTIFACT_BLOCK = 0.25      # >25% of parts carrying raw PDF/scheme text is not publishable


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
        self.exam_info = self._json(Path(__file__).parent / "exam-info" / f"{subject}.json")
        figure_raw = self._json(REPORTS / f"figures-{subject}.json")
        self.figure_report_exists = figure_raw is not None
        self.figures = ((figure_raw or {}).get("entries", {})
                        if isinstance(figure_raw, dict) and "id_scheme_version" in figure_raw
                        else (figure_raw or {}))
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
    bad = []
    for q in c.canon:
        # Several SEC short questions print two separately marked prompts with no (a)/(b)
        # labels. Repeated empty labels faithfully represent the paper and are not a split smell.
        labels = [p.get("label") for p in q.get("parts", []) if (p.get("label") or "").strip()]
        if len(set(labels)) != len(labels):
            bad.append(q["id"])
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
    # Split papers/sections carry an explicit component between year and label (e.g. Paper A,
    # Paper BC). It is part of the canonical source identity, not malformed display text.
    pat = re.compile(rf"^LC {re.escape(want)} (Higher|Ordinary) \d{{4}}(?: Paper [A-Za-z0-9]+)? — ")
    bad = [q["id"] for q in c.canon if not pat.match(q.get("source", ""))]
    if bad:
        sample = next((q["source"] for q in c.canon if q["id"] == bad[0]), "")
        yield Finding("sources", BLOCK,
                      f"{len(bad)} malformed source label(s); expected 'LC {want} …', "
                      f"got {sample!r}", bad[:50])


def check_exam_info(c: Ctx):
    """Exam Info is a required pipeline artifact; incomplete shells must never publish."""
    import exam_info
    errors = exam_info.validate(getattr(c, "exam_info", None), c.subject)
    if errors:
        yield Finding("exam-info", BLOCK,
                      f"exam info is missing/incomplete: {'; '.join(errors[:4])}", errors)


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


def check_figure_audit(c: Ctx):
    """Reconcile canonical parts, exhaustive inspection state, and supplied-visual wording."""
    figures = getattr(c, "figures", {}) or {}
    report_exists = getattr(c, "figure_report_exists", bool(figures))
    if SCAN_ALL_PARTS_FOR_FIGURES and c.parts and not report_exists:
        yield Finding("figure-audit", BLOCK,
                      "no exhaustive figure-inspection report — run the images stages")
        return
    expected = {f"{q['id']}#{i}" for q in c.canon for i, _p in enumerate(q.get("parts", []))}
    missing = sorted(expected - set(figures))
    if missing:
        yield Finding("figure-audit", BLOCK,
                      f"{len(missing)} part(s) were never visually inspected for supplied figures",
                      missing[:50])
    unresolved = sorted(k for k, v in figures.items()
                        if isinstance(v, dict) and (v.get("pending_crop") or v.get("needs_review")
                                                   or v.get("reason") == "page-not-located"))
    if unresolved:
        yield Finding("figure-audit", BLOCK,
                      f"{len(unresolved)} figure inspection(s) remain unresolved/reviewable",
                      unresolved[:50])
    weak_qa = sorted(k for k, v in figures.items() if isinstance(v, dict)
                     and v.get("has_figure") is True and v.get("diagram")
                     and not (v.get("qa_version", 0) >= 2 and v.get("relevant") is True
                              and v.get("complete") is True and v.get("tight") is True
                              and v.get("context_compared") is True))
    if weak_qa:
        yield Finding("figure-audit", BLOCK,
                      f"{len(weak_qa)} diagram crop(s) lack context-aware relevance, completeness and tightness QA",
                      weak_qa[:50])
    supplied_missing = []
    for q, p in c.parts:
        if SUPPLIED_FIGURE_RE.search(p.get("question", "")) and not (p.get("diagram") or "").strip():
            supplied_missing.append(q["id"])
    if supplied_missing:
        yield Finding("figure-audit", BLOCK,
                      f"{len(supplied_missing)} part(s) explicitly reference a supplied visual but have no diagram",
                      supplied_missing[:50])


def check_text_artifacts(c: Ctx):
    """Marking-scheme markup, bled part labels, PDF hard-wrapping and font-encoded glyphs.

    Home Economics shipped 720 raw scheme dumps and 155 tofu glyphs past a gate that reported
    CLEAN, because the only answer-quality check exempted scheme-sourced text — 94% of the store.
    These are WARN rather than BLOCK while they are a minority, since `textclean.py <subject>
    --apply` clears them for free; past TEXT_ARTIFACT_BLOCK the subject is mostly raw PDF and
    should not reach students at all.
    """
    counts = Counter()
    for _q, p in c.parts:
        for defect in textclean.artifacts(p):
            counts[defect] += 1
    if not counts:
        return
    worst = max(counts.values())
    total = max(1, len(c.parts))
    share = worst / total
    detail = ", ".join(f"{k} {v}" for k, v in counts.most_common())
    sev = BLOCK if share > TEXT_ARTIFACT_BLOCK else WARN
    yield Finding("text-artifacts", sev,
                  f"{worst} part(s) ({share:.1%}) carry raw PDF/marking-scheme text — {detail}. "
                  f"Repair with: python3 textclean.py {c.subject} --apply",
                  dict(counts))


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
    """Duplicates ACROSS chapters — the per-chapter dedup in flashcards.py cannot see these."""
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
        sev = WARN if rate <= CARD_DUP_RATE_MAX else BLOCK
        eg = ", ".join(sorted(dup_groups)[:3])
        yield Finding("card-duplicates", sev,
                      f"{len(dup_groups)} term(s) duplicated across chapters covering "
                      f"{dup_cards} redundant card(s) ({rate:.1%} of the deck) — e.g. {eg}",
                      {"rate": round(rate, 4), "groups": len(dup_groups)})


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
          check_ai_share, check_years, check_sources, check_exam_info, check_diagrams, check_figure_audit, check_flashcards,
          check_flashcard_duplicates, check_card_budgets, check_coverage, check_regression,
          check_text_artifacts]


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
