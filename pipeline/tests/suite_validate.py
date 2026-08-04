"""Content validation — the distinction the re-queue and the merge gate both depend on.

An empty answer is NORMAL at segment time (model_answers.py fills it later) but a real defect
at the merge gate. Collapsing those two would either re-queue every paper forever or publish
unanswered questions.
"""
import validate


def part(**kw):
    p = {"label": "(a)", "question": "A question of entirely adequate length.", "marks": 10,
         "model": "An answer."}
    p.update(kw)
    return p


def test_good_part_has_no_problems():
    assert validate.part_problems(part()) == []


def test_placeholder_question_is_an_extraction_failure():
    assert "placeholder-question" in validate.part_problems(part(question="Part (a)"))
    assert "placeholder-question" in validate.extraction_problems(part(question="Part (a)"))


def test_short_question_is_an_extraction_failure():
    assert "question-too-short" in validate.extraction_problems(part(question="Why?"))


def test_empty_answer_is_a_gate_problem_but_not_an_extraction_failure():
    p = part(model="")
    assert "empty-answer" in validate.part_problems(p)
    assert validate.extraction_problems(p) == []


def test_answer_to_nothing_is_caught():
    p = part(question="Part (a)", model="Generic prose.", model_source="ai-h1")
    assert "answer-to-nothing" in validate.part_problems(p)


def test_validate_output_requeues_a_mostly_broken_paper():
    bad = {"questions": [{"parts": [part(question="Part (a)") for _ in range(5)]}]}
    assert validate.validate_output(bad) is False


def test_validate_output_tolerates_a_little_noise():
    parts = [part() for _ in range(19)] + [part(question="Part (a)")]
    assert validate.validate_output({"questions": [{"parts": parts}]}) is True


def test_validate_output_rejects_empty():
    assert validate.validate_output({"questions": []}) is False
    assert validate.validate_output("not a dict") is False


def test_empty_answers_alone_do_not_requeue():
    """Otherwise every paper re-queues forever, since answers arrive in a later stage."""
    parts = [part(model="") for _ in range(10)]
    assert validate.validate_output({"questions": [{"parts": parts}]}) is True


def test_scan_canonical_locates_bad_parts():
    canon = [{"id": "q1", "parts": [part(), part(model="")]}]
    found = validate.scan_canonical(canon)
    assert len(found) == 1 and found[0]["problems"] == ["empty-answer"]


# ── flashcards ────────────────────────────────────────────────────────────────
def fcard(**kw):
    c = {"term": "Food Pyramid", "prompt": "What does the food pyramid show?",
         "answer": "It shows the proportions of each food group in a balanced diet.",
         "type": "concept"}
    c.update(kw)
    return c


def test_good_card_has_no_problems():
    assert validate.card_problems(fcard()) == []


def test_a_prompt_that_is_just_the_term_is_caught():
    """The exact defect the prompt field exists to fix: 'Q1: Food Pyramid'."""
    assert "prompt-is-term" in validate.card_problems(fcard(prompt="Food Pyramid"))


def test_a_prompt_that_is_the_term_with_a_question_mark_is_still_caught():
    assert "prompt-is-term" in validate.card_problems(fcard(prompt="Food Pyramid?"))


def test_a_legacy_card_reports_no_prompt():
    c = {"term": "Food Pyramid", "definition": "It shows a balanced diet's proportions."}
    assert "no-prompt" in validate.card_problems(c)


def test_a_statement_is_not_a_question():
    assert "prompt-not-a-question" in validate.card_problems(
        fcard(prompt="The food pyramid is a dietary guide."))


def test_an_imperative_exam_instruction_is_a_valid_prompt():
    for stem in ("Explain the role of the food pyramid.",
                 "Describe how the food pyramid is used.",
                 "Distinguish between the two food groups shown here."):
        assert "prompt-not-a-question" not in validate.card_problems(fcard(prompt=stem)), stem


def test_a_prompt_referring_to_the_paper_is_not_self_contained():
    """A flashcard carries no diagram, so this prompt is unanswerable."""
    assert "prompt-not-self-contained" in validate.card_problems(
        fcard(prompt="Explain the process shown in the diagram above."))


def test_empty_term_and_answer_are_caught():
    probs = validate.card_problems(fcard(term="", answer=""))
    assert "empty-term" in probs and "empty-answer" in probs


def test_legacy_definition_counts_as_the_answer():
    c = {"term": "X", "prompt": "What is X?", "definition": "A sufficiently long answer here."}
    assert "empty-answer" not in validate.card_problems(c)


def test_bad_type_only_reported_when_a_vocabulary_is_given():
    assert "bad-type" not in validate.card_problems(fcard(type="wingding"))
    assert "bad-type" in validate.card_problems(fcard(type="wingding"), {"concept"})


def test_scan_cards_locates_the_bad_card():
    store = {"ch1": [fcard(), fcard(term="Bad", prompt="Bad")]}
    found = validate.scan_cards(store)
    assert len(found) == 1 and found[0]["term"] == "Bad" and found[0]["chapter"] == "ch1"


# ── term keys ─────────────────────────────────────────────────────────────────
def test_normalise_term_folds_only_case_and_whitespace():
    """It drives a merge that DELETES cards, so it must stay conservative."""
    assert validate.normalise_term("  Food   Pyramid ") == validate.normalise_term("food pyramid")
    assert validate.normalise_term("Gas law") != validate.normalise_term("Gas laws")


def test_variant_key_folds_plurals_articles_and_punctuation():
    v = validate.variant_key
    assert v("Gas laws") == v("gas law")
    assert v("The Food Pyramid") == v("food pyramid")
    assert v("food-pyramid") == v("Food Pyramid")


def test_variant_key_catches_the_dash_variant():
    """A hyphen vs an en-dash is invisible on screen and survives the strict key."""
    assert validate.variant_key("Berlin Wall (1961-1989)") == \
        validate.variant_key("Berlin Wall (1961–1989)")


def test_variant_key_keeps_genuinely_different_terms_apart():
    v = validate.variant_key
    assert v("Endothermic reaction") != v("Exothermic reaction")
    assert v("Acid") != v("Base")


def test_variant_key_does_not_mangle_short_or_latin_plurals():
    v = validate.variant_key
    assert v("gas") == "gas" and v("basis") == "basis" and v("nucleus") == "nucleus"


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
