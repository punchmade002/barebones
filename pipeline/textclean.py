"""Deterministic text repair for PDF-derived exam content — no model calls, no token cost.

Three defect families slipped past every stage of the Home Economics run and were only found by
reading the merged output. All three are mechanical, so all three are fixed here in plain Python
rather than by asking a worker to try harder:

  1. SCHEME MARKUP.  SEC marking schemes from some eras lead with a mark allocation
     ("4 points @ 6 marks each", "Breakfast = 6 marks"). Copied faithfully out of the scheme —
     as schemes.py asks the worker to do — it lands in the student-facing answer.
  2. LABEL BLEED.  PDF table extraction appends the *next* part's label to the previous cell, so
     an answer to (b) ends "...etc.\n\n(c)".
  3. GLYPH JUNK.  Symbol/Wingdings-encoded bullets and ticks extract as private-use codepoints
     (U+F0B7, U+F0FC). They render as tofu boxes in the browser and waste worker prompt tokens.

Plus the cosmetic consequence of all three: PDF hard-wrapping preserved as literal newlines
mid-sentence, which is what makes an old scheme answer read as a dump rather than as prose.

WHY IT LIVES IN ONE MODULE: `clean_*` (the repair) and `artifacts` (the detection validate.py
reports) are driven by the SAME regexes. A validator with its own copy of the patterns drifts
from the cleaner and then either cries wolf forever or goes quiet while the defect returns.

Wired in at three edges, each of which is free:
    digest.extract_pages / extract.extract_pdf  -> normalize_glyphs   (once, at PDF ingestion)
    schemes.parse_result                        -> clean_scheme_answer (as answers arrive)
    validate.part_defects                       -> artifacts           (so the gate can see it)

And offered as a backfill for stores built before this module existed:

    python3 textclean.py home-economics            # report only, changes nothing
    python3 textclean.py home-economics --apply    # repair canonical + re-render the app JS
"""
from __future__ import annotations
import json
import re
import sys

# ── 1. glyph normalisation ────────────────────────────────────────────────────
# PDF producers embed Symbol/Wingdings text by mapping each glyph into the private use area at
# U+F000 + its font byte. PyMuPDF hands those codepoints back verbatim. The table below covers
# what SEC papers actually use; anything else in the PUA becomes a space (see normalize_glyphs),
# because a tofu box in a question is worse than a missing ornament.
#
# Keyed by codepoint, not by literal character: these glyphs are invisible in an editor and
# several are indistinguishable from one another, so a literal table would be unreviewable, would
# not survive a diff, and would silently corrupt on the next edit.
_PUA_CODES = {
    0xF0B7: "\u2022", 0xF0A7: "\u25aa", 0xF0D8: "\u203a",       # bullets
    0xF0FC: "\u2713", 0xF0FB: "\u2717", 0xF071: "\u25a1",       # ticks / boxes
    0xF02D: "-", 0xF02A: "*", 0xF03D: "=", 0xF02B: "+",
    0xF0E0: "\u2192", 0xF0AE: "\u2192", 0xF0AC: "\u2190", 0xF0AB: "\u2194",
    0xF0B0: "\u00b0", 0xF0B1: "\u00b1", 0xF0B4: "\u00d7", 0xF0B8: "\u00f7",
    0xF0A3: "\u2264", 0xF0B3: "\u2265", 0xF0B9: "\u2260", 0xF0BB: "\u2248",
    # Symbol-font Greek: U+F000 + the Latin letter's byte. Chemistry/biology lean on these.
    0xF061: "\u03b1", 0xF062: "\u03b2", 0xF067: "\u03b3", 0xF064: "\u03b4",
    0xF065: "\u03b5", 0xF06B: "\u03ba", 0xF06C: "\u03bb", 0xF06D: "\u03bc",
    0xF070: "\u03c0", 0xF072: "\u03c1", 0xF073: "\u03c3", 0xF074: "\u03c4",
    0xF077: "\u03c9", 0xF044: "\u0394", 0xF057: "\u03a9", 0xF053: "\u03a3",
}

# Ligatures aren't PUA, but they break substring matching in retrieval just as badly.
_LIGATURES = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}

PUA_MAP = {chr(code): repl for code, repl in _PUA_CODES.items()} | _LIGATURES

PUA_RE = re.compile("[%s-%s]" % (chr(0xE000), chr(0xF8FF)))


def normalize_glyphs(text: str) -> str:
    """Map font-encoded private-use codepoints to real characters. Unknown PUA becomes a space.

    Idempotent, and effectively free on clean text: a normal paper contains no PUA at all, so
    this costs one regex scan and nothing else.
    """
    if not text:
        return text
    for bad, good in PUA_MAP.items():
        if bad in text:
            text = text.replace(bad, good)
    if PUA_RE.search(text):
        # Space, not deletion: an unmapped glyph sitting between two words must not silently weld
        # them together. Any doubled space is collapsed by the whitespace pass in reflow/clean.
        text = PUA_RE.sub(" ", text)
    return text


def count_pua(text: str) -> int:
    """How many private-use codepoints remain. Used by the validator and the backfill report."""
    return len(PUA_RE.findall(text or ""))


# ── 2. marking-scheme markup ──────────────────────────────────────────────────
# A mark allocation always pairs a number with the word "mark(s)" through an allocator: "@", "=",
# "x"/"×", or a trailing "each". Requiring that allocator is what keeps this off ordinary prose —
# an answer may well say "marks" (stretch marks, watermarks) but never "3 @ 2 marks". An optional
# leading stem ("Name:", "Breakfast =") is absorbed so the whole fragment goes at once.
_STEM = r"[A-Za-z][A-Za-z'/ -]{0,24}?\s*[:=]\s*"      # "Name:", "Breakfast ="
_ALLOC = rf"""
  (?:
      (?:{_STEM})?                                   # optional stem
      \d+\s*
      (?:[a-z]{{2,14}}s?\s+){{0,4}}?                  # unit: "points", "example of each class"
      (?:\([^)\n]{{0,40}}\)\s*)?                      # aside: "(one for each food)"
      [@x×=]\s*
      \d+\s*(?:marks?|m)\b
      (?:\s*each)?
      (?:\s*=\s*\d+\s*(?:marks?)?)?                   # "... each = 6 marks", "... each =4"
      (?:\s*\(\d+\))?                                 # "... (8)"
    |                                                 # or the stemmed form with one number:
      {_STEM}\d+\s*marks?\b(?:\s*each)?               # "Breakfast = 6 marks"
  )
"""
ALLOC_RE = re.compile(_ALLOC, re.I | re.X)

# The bare "N marks each" / "N points" form, only where it stands alone as its own line — without
# that anchor this would eat legitimate sentences that mention a mark total.
ALLOC_LINE_RE = re.compile(
    r"^[ \t]*(?:[A-Za-z][A-Za-z'/ -]{0,24}?[:=]\s*)?"
    r"\d+\s*(?:[a-z]{3,12}s?\s*)?marks?(?:\s*each)?[ \t]*$", re.I | re.M)

# A part label alone at the very end: "(c)", "(c) (i)", "2(a)(iii)", or a lone "(ii)".
#
# Two deliberate restrictions, both learned from real damage:
#   * it must follow a NEWLINE (or be the entire string). Every genuine bleed is a table cell the
#     PDF appended on its own line. Without this the rule ate trailing chemistry notation on the
#     same line — "potassium (K)" became "potassium", and state symbols like "H2O (l)" were next.
#   * lowercase only, no re.I. "(K)" is an element, "(III)" is an oxidation state; SEC part labels
#     are always lowercase.
_LABEL = r"\(?\d{0,2}\s*\(\s*[a-z]\s*\)(?:\s*\(\s*[ivx]{1,4}\s*\))?|\(\s*[ivx]{1,4}\s*\)"
LABEL_BLEED_RE = re.compile(rf"(?:\n\s*(?:{_LABEL})|^\s*(?:{_LABEL}))\s*$")

# Stripping an allocation out of the middle of a line leaves its separators behind: "1 method @ 6
# marks, 1 point @ 6 marks \nCash: ..." would otherwise start ", \nCash:". These patterns clear
# what the removal orphaned — never anything that was load-bearing on its own.
# NOTE: there is deliberately no general "strip stranded =" rule. One was tried and it destroyed
# real content in chemistry — "Kc = [HI]2/([H2][I2])" lost its "=", and "8.9 / 890 = 0.01 mol"
# became "890 .01 mol". The allocation pattern above now swallows its own trailing "= N" instead,
# so the only "=" ever removed is one that was part of a matched allocation.
DEBRIS_BRACKETS_RE = re.compile(r"\(\s*[;,:.=\s]*\)")        # "( ; ; ; )" once its content is gone
# Any letter or digit at all means there is still an answer. A stricter "two consecutive letters"
# rule deleted legitimate short answers: "0.06 g / l" and "25%" are complete answers in chemistry
# and history respectively.
HAS_CONTENT_RE = re.compile(r"[A-Za-z0-9]")


def _tidy_debris(text: str) -> str:
    """Clear punctuation orphaned by markup removal; return "" if nothing but debris remains."""
    text = DEBRIS_BRACKETS_RE.sub(" ", text)
    text = re.sub(r"\s*([,;:])(?=\s*[,;:])", "", text)       # ";  ;  ;" -> ";"
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"(?m)^[ \t]*[,;:.=]+[ \t]*", "", text)      # line-leading orphans
    # Only "=" trails as debris. A line-final ";" or "," is the separator of a semicolon-delimited
    # scheme list — stripping those made reflow's list detection disagree with the validator's.
    text = re.sub(r"(?m)[ \t=]+$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text if HAS_CONTENT_RE.search(text) else ""

# The narrow artefact schemes.py already handled: a bare next question number on its own trailing
# line ("... etc.\n\n7."). Folded in here so there is one cleaning path rather than two.
TRAILING_QNUM_RE = re.compile(r"\n\s*(?:\[\d+\]\s*)?\d{1,2}\.\s*$")


def strip_scheme_markup(text: str) -> str:
    """Remove mark-allocation bookkeeping. The credit-bearing content itself is left alone."""
    if not text:
        return text
    text = ALLOC_LINE_RE.sub("", text)
    return ALLOC_RE.sub(" ", text)


def strip_label_bleed(text: str) -> str:
    """Remove a trailing part label / question number left behind by PDF table extraction."""
    if not text:
        return text
    prev = None
    # Loop: extraction sometimes leaves both a label and a number ("... (c)\n8."), and each
    # pattern only strips the outermost one.
    while prev != text:
        prev = text
        text = TRAILING_QNUM_RE.sub("", text).rstrip()
        text = LABEL_BLEED_RE.sub("", text).rstrip()
    return text


# ── 3. hard-wrap reflow ───────────────────────────────────────────────────────
# Rejoin a line break the PDF put mid-sentence. The test is deliberately two-sided: the text
# before must NOT end a sentence, and the text after must start lowercase (or with an opening
# bracket). Genuine paragraph breaks in authored answers end with "." and resume with a capital,
# so they survive untouched — which matters, because the ai-h1 answers are already well-formed
# multi-paragraph prose and must not be flattened into a wall.
_BULLET = "•▪›"
_KEEP = "\x00"                                   # sentinel: a newline that must survive reflow

HARDWRAP_RE = re.compile(r"(?<=[^.?!:;\n" + _BULLET + r"\-])[ \t]*\n[ \t\n]*(?=[a-z(])")
BULLET_KEEP_RE = re.compile(r"[ \t]*\n[ \t]*(?=[" + _BULLET + r"])")


def reflow(text: str) -> str:
    """Undo PDF hard-wrapping and tidy whitespace, preserving bullets and real paragraph breaks."""
    if not text:
        return text
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace(_KEEP, "")
    # Protect bullet line starts before the general rejoin, so a bullet that happens to follow a
    # lowercase word is not pulled up into the previous line.
    text = BULLET_KEEP_RE.sub(_KEEP, text)
    text = HARDWRAP_RE.sub(" ", text)
    text = text.replace(_KEEP, "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"[ \t]+\n", "\n", text)      # trailing spaces only; indentation is content
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ── the public cleaners ───────────────────────────────────────────────────────
def clean_scheme_answer(text: str) -> str:
    """Full repair for one marking-scheme answer. Order matters: markup and labels are stripped
    while the original line structure still marks their boundaries, then the remainder is
    reflowed into prose.

    May legitimately return "" — an "answer" that was nothing but a stray label never was one.
    Callers must treat that as unanswered rather than as an empty answer (see schemes.collect).
    """
    if not text:
        return ""
    text = normalize_glyphs(text)
    text = strip_scheme_markup(text)
    text = strip_label_bleed(text)
    text = reflow(text)
    text = _tidy_debris(text)
    return strip_label_bleed(text).strip()


def clean_question(text: str) -> str:
    """Questions come from the paper, not the scheme, so they need glyph and whitespace repair
    only — never markup stripping, which would eat a question that states its own mark total."""
    if not text:
        return ""
    text = normalize_glyphs(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# ── detection, for validate.py ────────────────────────────────────────────────
# Long enough that a genuinely terse scheme answer ("True; False; True.") cannot trip the wrap
# heuristic on one unlucky line break.
_WRAP_MIN_CHARS = 160
_WRAP_MIN_HITS = 2


def artifacts(part: dict) -> list[str]:
    """Defect names for one part's text. Same regexes as the cleaners, so a clean part is silent
    and a dirty one stays flagged until it is actually repaired."""
    out = []
    answer = (part.get("model") or "").strip()
    question = (part.get("question") or "").strip()
    if answer:
        if ALLOC_RE.search(answer) or ALLOC_LINE_RE.search(answer):
            out.append("scheme_markup")
        if LABEL_BLEED_RE.search(answer) or TRAILING_QNUM_RE.search(answer):
            out.append("label_bleed")
        # Only PDF-derived text can be hard-wrapped. An ai-h1 answer was authored as prose, so its
        # line breaks are deliberate and clean_question rightly leaves them alone — flagging those
        # produced a warning no tool would ever clear, which is how a gate learns to be ignored.
        if (part.get("model_source") != "ai-h1"
                and len(answer) >= _WRAP_MIN_CHARS
                and len(HARDWRAP_RE.findall(answer)) >= _WRAP_MIN_HITS):
            out.append("raw_wrap")
    if count_pua(answer) or count_pua(question):
        out.append("glyph_junk")
    return out


# ── backfill for stores built before this module ──────────────────────────────
def backfill(subject: str, apply: bool = False) -> dict:
    """Repair an existing canonical store in place. Pure Python: repairing a whole subject costs
    nothing, where re-running the schemes stage would re-send every paper to a worker.

    Returns a summary. With apply=False nothing is written — run that first and read the numbers.
    """
    from config import CANONICAL
    path = CANONICAL / f"{subject}.json"
    if not path.exists():
        raise SystemExit(f"no canonical store for {subject}")
    canonical = json.loads(path.read_text())

    stats = {"subject": subject, "parts": 0, "answers_changed": 0, "questions_changed": 0,
             "emptied": 0, "pua_removed": 0, "before": {}, "after": {}, "emptied_ids": []}
    for q in canonical:
        for i, p in enumerate(q.get("parts", [])):
            stats["parts"] += 1
            for d in artifacts(p):
                stats["before"][d] = stats["before"].get(d, 0) + 1

            question = p.get("question") or ""
            new_q = clean_question(question)
            if new_q != question:
                stats["pua_removed"] += count_pua(question)
                p["question"] = new_q
                stats["questions_changed"] += 1

            answer = p.get("model") or ""
            if answer:
                # Only scheme-sourced text carries the markup; ai-h1 answers were authored as
                # prose and must not go through markup stripping on the off chance a sentence
                # happens to resemble an allocation.
                new_a = (clean_scheme_answer(answer) if p.get("model_source") == "scheme"
                         else clean_question(answer))
                if new_a != answer:
                    stats["pua_removed"] += count_pua(answer)
                    stats["answers_changed"] += 1
                    if not new_a:
                        # Was pure markup/label. Clearing model_source hands the part back to
                        # model_answers.py, which authors a real answer on the next run.
                        p.pop("model_source", None)
                        p["model"] = ""
                        stats["emptied"] += 1
                        stats["emptied_ids"].append(f"{q.get('id')}#{i}")
                    else:
                        p["model"] = new_a

            for d in artifacts(p):
                stats["after"][d] = stats["after"].get(d, 0) + 1

    if apply:
        path.write_text(json.dumps(canonical, ensure_ascii=False, indent=2))
        import segment
        stats["rendered"] = segment.render_js(subject, canonical).name
        _backfill_flashcards(subject, stats)
    return stats


def _backfill_flashcards(subject: str, stats: dict) -> None:
    """Flashcards are authored from retrieved course text, so they only ever need glyph repair."""
    from config import CANONICAL
    path = CANONICAL / f"flashcards.{subject}.json"
    if not path.exists():
        return
    by_chapter = json.loads(path.read_text())
    changed = 0
    for cards in by_chapter.values():
        for c in cards:
            for field in ("term", "definition"):
                before = c.get(field) or ""
                after = clean_question(before)
                if after != before:
                    c[field] = after
                    changed += 1
    if changed:
        path.write_text(json.dumps(by_chapter, ensure_ascii=False, indent=2))
        import flashcards
        flashcards.render_js(subject, by_chapter)
    stats["flashcard_fields_changed"] = changed


def _report(stats: dict) -> None:
    print(f"\n=== textclean: {stats['subject']} ===")
    print(f"{stats['parts']} part(s) scanned")
    keys = sorted(set(stats["before"]) | set(stats["after"]))
    if not keys:
        print("  no text defects found")
    for k in keys:
        print(f"  {k:<14} {stats['before'].get(k, 0):>5} -> {stats['after'].get(k, 0)}")
    print(f"  answers rewritten   {stats['answers_changed']}")
    print(f"  questions rewritten {stats['questions_changed']}")
    print(f"  PUA glyphs removed  {stats['pua_removed']}")
    if stats["emptied"]:
        print(f"  {stats['emptied']} answer(s) were pure markup -> cleared for re-authoring:")
        for x in stats["emptied_ids"][:10]:
            print(f"      {x}")
    if "rendered" in stats:
        print(f"  rendered {stats['rendered']}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subj = next((a for a in args if not a.startswith("-")), "home-economics")
    result = backfill(subj, apply="--apply" in args)
    _report(result)
    if "--apply" not in args:
        print("\n(dry run — nothing written. re-run with --apply)")
