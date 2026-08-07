"""Syllabus taxonomy parsing and flashcard coverage verification.

"Flashcards should cover all examinable knowledge within a chapter" is only a testable claim if
something outside the generator says what the examinable knowledge is. The bundle's
`guide-simplestudy.md` does: a `## Unit and topic structure` section listing every unit and its
topics. These tests cover the parse (including the wrapped-line and non-content-unit cases that
real guides contain) and the coverage scoring the gate blocks on.

The guide is written to a temp directory and `syllabus.RESOURCES` is pointed at it, so no real
subject bundle is touched.
"""
import tempfile
from pathlib import Path

import syllabus

GUIDE = """# Test research guide

## Source

- Provider: SimpleStudy.

## Unit and topic structure

1. **Cell Biology** — Cell Structure; Enzymes; Respiration.
2. **Genetics and Inheritance** — DNA Replication; Genetic Inheritance; Mutations and
   Genetic Screening.
3. **Assessment** — Written Exam; Coursework.

## Pipeline guidance

- Generate original prose.
"""


def _with_guide(fn, text=GUIDE, subject="zz-test"):
    original = syllabus.RESOURCES
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp) / subject
        d.mkdir(parents=True)
        (d / "guide-simplestudy.md").write_text(text)
        syllabus.RESOURCES = Path(tmp)
        try:
            return fn(subject)
        finally:
            syllabus.RESOURCES = original


def card(term, definition=""):
    return {"term": term, "question": f"What is {term}?", "definition": definition}


# ── parsing ───────────────────────────────────────────────────────────────────
def test_units_and_topics_are_parsed():
    units = _with_guide(syllabus.units)
    assert [u["unit"] for u in units] == ["Cell Biology", "Genetics and Inheritance"]
    assert units[0]["topics"] == ["Cell Structure", "Enzymes", "Respiration"]


def test_a_topic_list_wrapped_over_two_lines_is_not_truncated():
    units = _with_guide(syllabus.units)
    assert units[1]["topics"][-1] == "Mutations and Genetic Screening"


def test_assessment_units_are_excluded():
    """Assessment describes how the subject is examined, not what must be learned — counting it
    would cap coverage below 100% forever and train everyone to ignore the number."""
    assert "Written Exam" not in _with_guide(syllabus.topics)


def test_a_subject_with_no_guide_yields_nothing():
    assert syllabus.units("zz-does-not-exist-at-all") == []


def test_topics_for_selects_the_matching_unit():
    got = _with_guide(lambda s: syllabus.topics_for(s, "Genetics and Inheritance"))
    assert "Genetic Inheritance" in got
    assert "Enzymes" not in got


# ── coverage ──────────────────────────────────────────────────────────────────
def test_full_coverage_is_recognised():
    decks = {"c1": [card("Cell Structure"), card("Enzymes"), card("Respiration")],
             "c2": [card("DNA Replication"), card("Genetic Inheritance"),
                    card("Mutations and Genetic Screening")]}
    rep = _with_guide(lambda s: syllabus.coverage(s, decks))
    assert rep["verifiable"] and rep["rate"] == 1.0 and rep["missing"] == []


def test_missing_topics_are_named():
    decks = {"c1": [card("Cell Structure")]}
    rep = _with_guide(lambda s: syllabus.coverage(s, decks))
    assert "Enzymes" in rep["missing"]
    assert rep["rate"] < 1.0


def test_a_partial_term_match_still_counts():
    """A card titled "Enzyme" covers the topic "Enzymes" — demanding the literal wording would
    report false misses and make the whole check noise."""
    rep = _with_guide(lambda s: syllabus.coverage(s, {"c1": [card("Enzyme")]}))
    assert "Enzymes" not in rep["missing"]


def test_the_definition_can_carry_the_match():
    decks = {"c1": [card("Krebs cycle", "the second stage of cellular respiration")]}
    rep = _with_guide(lambda s: syllabus.coverage(s, decks))
    assert "Respiration" not in rep["missing"]


def test_words_scattered_across_different_cards_are_not_coverage():
    """A single card must carry the topic; spreading its words over the deck is not coverage."""
    decks = {"c1": [card("Mutations"), card("Genetic"), card("Screening")]}
    rep = _with_guide(lambda s: syllabus.coverage(s, decks))
    assert "Mutations and Genetic Screening" in rep["missing"]


def test_unverifiable_when_there_is_no_guide():
    """Absent a taxonomy the report must say so, never report perfect coverage."""
    rep = syllabus.coverage("zz-does-not-exist-at-all", {"c1": [card("Anything")]})
    assert rep["verifiable"] is False and rep["rate"] == 0.0


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
