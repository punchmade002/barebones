"""Per-chapter flashcard dedup, the card schema, and the per-subject type vocabulary.

`flashcards.dedup` runs per chapter, so it cannot see a term repeated in a different chapter.
That limitation is why 75 duplicate groups shipped in Home Economics.
`test_dedup_cannot_see_across_chapters` documents the boundary deliberately, and names the two
things that DO close it: consolidate.merge_exact at generation time, and the gate afterwards.

The schema tests exist because a card used to be {term, definition} and the app rendered the
bare term as the question — a student was shown "Q1: Food Pyramid" and asked to answer it.
"""
import json
import tempfile
from pathlib import Path

import consolidate
import flashcards
import gate
from config import card_types


def card(term, answer="d", type_="concept", prompt=""):
    c = {"term": term, "answer": answer, "type": type_}
    if prompt:
        c["prompt"] = prompt
    return c


# ── dedup ─────────────────────────────────────────────────────────────────────
def test_exact_duplicates_collapse():
    assert len(flashcards.dedup([card("Home Rule"), card("Home Rule")])) == 1


def test_case_and_whitespace_variants_collapse():
    out = flashcards.dedup([card("Home Rule"), card("home rule"), card("  Home Rule  ")])
    assert len(out) == 1


def test_longest_answer_wins():
    out = flashcards.dedup([card("X", "short"), card("X", "a much longer answer")])
    assert out[0]["answer"] == "a much longer answer"


def test_longest_prompt_wins():
    out = flashcards.dedup([card("X", prompt="What is X?"),
                            card("X", prompt="What is X and why does it matter?")])
    assert out[0]["prompt"] == "What is X and why does it matter?"


def test_empty_terms_are_dropped():
    assert flashcards.dedup([card(""), card("   "), card("Real")]) == \
        [{"term": "Real", "answer": "d", "type": "concept"}]


def test_type_defaults_to_concept():
    assert flashcards.dedup([{"term": "X", "answer": "d"}])[0]["type"] == "concept"


def test_specific_type_beats_the_catch_all():
    out = flashcards.dedup([card("X", type_="concept"), card("X", type_="person")])
    assert out[0]["type"] == "person"


def test_distinct_terms_are_kept():
    assert len(flashcards.dedup([card("A"), card("B"), card("C")])) == 3


# ── schema ────────────────────────────────────────────────────────────────────
def test_legacy_definition_is_read_as_the_answer():
    """An old {term, definition} store must survive being re-read and re-merged."""
    out = flashcards.normalise_card({"term": "X", "definition": "the old field"})
    assert out["answer"] == "the old field"


def test_a_card_without_a_prompt_omits_the_key():
    assert "prompt" not in flashcards.normalise_card({"term": "X", "answer": "a"})


def test_unknown_type_is_coerced_when_a_vocabulary_is_given():
    out = flashcards.normalise_card({"term": "X", "answer": "a", "type": "wingding"},
                                    {"concept", "person"})
    assert out["type"] == "concept"


def _rendered(by_chapter) -> dict:
    """Run render_js against a throwaway output dir and read back the emitted DB."""
    real = flashcards.CANONICAL
    with tempfile.TemporaryDirectory() as tmp:
        flashcards.CANONICAL = Path(tmp)
        try:
            out = flashcards.render_js("history", by_chapter)
            body = out.read_text()
        finally:
            flashcards.CANONICAL = real
    # the file is `window.FLASHCARDS_DB = Object.assign(window.FLASHCARDS_DB || {}, {...});`
    payload = body.split("|| {},", 1)[1]
    return json.loads(payload[:payload.rindex("}") + 1])


def test_render_js_keeps_definition_as_the_answer_field():
    """The app reads `definition`, so the answer must keep arriving under that name."""
    db = _rendered({"ch1": [card("X", "the answer")]})
    assert db["ch1"][0]["definition"] == "the answer"


def test_render_js_emits_the_prompt():
    db = _rendered({"ch1": [card("X", "a", prompt="What is X?")]})
    assert db["ch1"][0]["prompt"] == "What is X?"


def test_render_js_omits_prompt_for_legacy_cards():
    """A missing prompt must be absent, not empty — the app falls back to the term on absence."""
    db = _rendered({"ch1": [{"term": "X", "definition": "a"}]})
    assert "prompt" not in db["ch1"][0]


# ── per-subject type vocabulary ───────────────────────────────────────────────
def test_every_subject_vocabulary_has_a_catch_all():
    """Without 'concept' the model is forced to misclassify, and legacy cards become invalid."""
    from config import CARD_TYPES, DEFAULT_CARD_TYPES
    for subject, types in list(CARD_TYPES.items()) + [("<default>", DEFAULT_CARD_TYPES)]:
        assert "concept" in types, subject


def test_chemistry_does_not_inherit_historys_vocabulary():
    """The original enum was History's for every subject, so a titration could only be
    'concept'. 91% of Chemistry's deck collapsed to that one value."""
    chem = card_types("chemistry")
    assert "substance" in chem and "movement" not in chem


def test_unknown_subject_gets_the_generic_vocabulary_not_historys():
    types = card_types("basket-weaving")
    assert "movement" not in types and "concept" in types


def test_emit_tool_enum_matches_the_subject():
    tool = flashcards.emit_tool("chemistry")
    enum = tool["input_schema"]["properties"]["cards"]["items"]["properties"]["type"]["enum"]
    assert set(enum) == set(card_types("chemistry"))


def test_emit_tool_requires_an_authored_prompt():
    req = flashcards.emit_tool("history")["input_schema"]["properties"]["cards"]["items"]["required"]
    assert "prompt" in req and "answer" in req


def test_build_prompt_states_the_subjects_own_types():
    body = flashcards.build_prompt("chemistry", "Organic Chemistry", "pooled text")
    assert "substance" in body and "movement" not in body


def test_build_prompt_uses_the_display_name():
    """'home-economics' must never reach a student-facing prompt as 'Home Economics S & S'."""
    body = flashcards.build_prompt("home-economics", "Nutrition", "pooled")
    assert "Home Economics" in body and "S & S" not in body


# ── the boundary between dedup and consolidation ──────────────────────────────
def test_dedup_cannot_see_across_chapters():
    """Documents the boundary: dedup is per chapter by construction."""
    a = flashcards.dedup([card("Home Rule")])
    b = flashcards.dedup([card("Home Rule")])
    assert len(a) == len(b) == 1              # each chapter self-consistent, duplicate survives

    # the gate is what catches it after the fact
    c = gate.Ctx.__new__(gate.Ctx)
    c.subject, c.canon, c.parts, c.scaffold, c.baseline = "history", [], [], {}, None
    c.cards = {"ch1": a, "ch2": b}
    assert list(gate.check_flashcard_duplicates(c)), "gate missed a cross-chapter duplicate"

    # and consolidate is what stops it being published in the first place
    merged, report = consolidate.merge_exact({"ch1": a, "ch2": b}, ["ch1", "ch2"])
    assert sum(len(v) for v in merged.values()) == 1 and report


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
