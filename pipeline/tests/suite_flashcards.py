"""Flashcard dedup — and an explicit record of what it cannot do.

flashcards.dedup runs per chapter, so it cannot see a term repeated in a different chapter.
That limitation is why 75 duplicate groups shipped in Home Economics, and it is the reason the
cross-chapter check lives in gate.py instead. `test_dedup_cannot_see_across_chapters` documents
the boundary deliberately: if someone later makes dedup global, that test should fail loudly
rather than the gap being rediscovered from published output.
"""
import flashcards
import gate


def card(term, definition="d", type_="concept"):
    return {"term": term, "definition": definition, "type": type_}


def test_exact_duplicates_collapse():
    out = flashcards.dedup([card("Home Rule"), card("Home Rule")])
    assert len(out) == 1


def test_case_and_whitespace_variants_collapse():
    out = flashcards.dedup([card("Home Rule"), card("home rule"), card("  Home Rule  ")])
    assert len(out) == 1


def test_longest_definition_wins():
    out = flashcards.dedup([card("X", "short"), card("X", "a much longer definition")])
    assert out[0]["definition"] == "a much longer definition"


def test_empty_terms_are_dropped():
    assert flashcards.dedup([card(""), card("   "), card("Real")]) == \
        [{"term": "Real", "definition": "d", "type": "concept"}]


def test_type_defaults_to_concept():
    out = flashcards.dedup([{"term": "X", "definition": "d"}])
    assert out[0]["type"] == "concept"


def test_empty_worker_deck_fails_validation():
    assert not flashcards.validate_output({"cards": []})


def test_question_term_fails_worker_validation():
    assert not flashcards.validate_output({"cards": [
        card("Explain pasteurisation", "A heat treatment.", "process")
    ]})


def test_distinct_terms_are_kept():
    assert len(flashcards.dedup([card("A"), card("B"), card("C")])) == 3


def test_dedup_cannot_see_across_chapters():
    """Documents the boundary: dedup is per chapter by construction."""
    a = flashcards.dedup([card("Home Rule")])
    b = flashcards.dedup([card("Home Rule")])
    assert len(a) == len(b) == 1              # each chapter self-consistent, duplicate survives

    # the gate is what catches it
    c = gate.Ctx.__new__(gate.Ctx)
    c.subject, c.canon, c.parts, c.scaffold, c.baseline = "history", [], [], {}, None
    c.cards = {"ch1": a, "ch2": b}
    assert list(gate.check_flashcard_duplicates(c)), "gate missed a cross-chapter duplicate"


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
