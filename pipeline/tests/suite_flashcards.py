"""Flashcard dedup, the authored-question standard, and cross-chapter consolidation.

Three standards are enforced here, each of which shipped broken once:

  * every card carries a real question, so the app shows "What is mitosis?" and not "Mitosis";
  * `dedup` collapses repeats WITHIN a chapter;
  * `consolidate` removes repeats BETWEEN chapters — the gap that let 75 duplicate groups ship
    in Home Economics. dedup still cannot see across chapters by construction, so the
    consolidation pass is what makes the "no duplicates between chapters" rule true, and
    gate.check_flashcard_duplicates is the backstop that blocks if it ever regresses.
"""
import flashcards
import gate


def card(term, definition="d", type_="concept", question=None):
    return {"term": term, "question": question if question is not None else f"What is {term}?",
            "definition": definition, "type": type_}


# ── questions ─────────────────────────────────────────────────────────────────
def test_card_without_a_question_is_dropped():
    out = flashcards.dedup([{"term": "Mitosis", "definition": "d", "type": "concept"}])
    assert out == []


def test_term_with_a_question_mark_is_not_a_question():
    """The exact degradation the requirement exists to stop: "Mitosis?" is not a prompt."""
    assert not flashcards.is_usable_question("Mitosis?", "Mitosis")
    assert flashcards.dedup([card("Mitosis", question="Mitosis?")]) == []


def test_real_questions_are_accepted():
    for q, term in [("What is mitosis?", "Mitosis"),
                    ("Who was Rosa Parks?", "Rosa Parks"),
                    ("What was Catholic Emancipation?", "Catholic Emancipation")]:
        assert flashcards.is_usable_question(q, term), q


def test_question_survives_dedup():
    out = flashcards.dedup([card("Mitosis", question="What is mitosis?")])
    assert out[0]["question"] == "What is mitosis?"


def test_validate_output_requeues_a_deck_missing_questions():
    answer = [_ToolUse([{"term": "A", "definition": "d"}, {"term": "B", "definition": "d"}])]
    assert not flashcards.validate_output(answer)


def test_validate_output_accepts_a_good_deck():
    answer = [_ToolUse([card("A"), card("B"), card("C")])]
    assert flashcards.validate_output(answer)


class _ToolUse:
    """Minimal stand-in for the SDK's tool_use block, which parse_result reads."""
    type = "tool_use"
    name = "emit_flashcards"

    def __init__(self, cards):
        self.input = {"cards": cards}


# ── dedup within a chapter ────────────────────────────────────────────────────
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
    out = flashcards.dedup([card(""), card("   "), card("Real")])
    assert [c["term"] for c in out] == ["Real"]


def test_type_defaults_to_concept():
    out = flashcards.dedup([{"term": "X", "question": "What is X?", "definition": "d"}])
    assert out[0]["type"] == "concept"


def test_distinct_terms_are_kept():
    assert len(flashcards.dedup([card("A"), card("B"), card("C")])) == 3


# ── consolidation across chapters ─────────────────────────────────────────────
def test_dedup_cannot_see_across_chapters():
    """Documents the boundary: dedup is per chapter by construction."""
    a = flashcards.dedup([card("Home Rule")])
    b = flashcards.dedup([card("Home Rule")])
    assert len(a) == len(b) == 1              # each chapter self-consistent, duplicate survives


def test_consolidate_removes_the_cross_chapter_duplicate():
    out, removed = flashcards.consolidate({"ch1": [card("Home Rule")], "ch2": [card("Home Rule")]})
    assert removed == 1
    assert sum(len(v) for v in out.values()) == 1


def test_consolidate_keeps_the_fullest_definition():
    out, _ = flashcards.consolidate({
        "ch1": [card("Home Rule", "short")],
        "ch2": [card("Home Rule", "a considerably longer and fuller definition")],
    })
    assert out["ch1"] == []
    assert out["ch2"][0]["definition"].startswith("a considerably longer")


def test_consolidate_leaves_distinct_terms_alone():
    decks = {"ch1": [card("A"), card("B")], "ch2": [card("C")]}
    out, removed = flashcards.consolidate(decks)
    assert removed == 0
    assert sum(len(v) for v in out.values()) == 3


def test_consolidated_output_passes_the_gate():
    """End to end: what consolidate returns must not trip the duplicate blocker."""
    out, _ = flashcards.consolidate({"ch1": [card("Home Rule")], "ch2": [card("Home Rule")]})
    c = gate.Ctx.__new__(gate.Ctx)
    c.subject, c.canon, c.parts, c.scaffold, c.baseline = "history", [], [], {}, None
    c.cards = out
    assert not list(gate.check_flashcard_duplicates(c))


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
