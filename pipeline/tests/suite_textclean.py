"""Deterministic text repair — the cleaner and the detector must never disagree.

These defects reached the live app once already: 720 marking-scheme dumps, 410 bled labels and
155 tofu glyphs shipped in Home Economics while the gate reported CLEAN. The invariant that keeps
that from recurring is the last test here — anything `artifacts` flags, `clean_scheme_answer` must
actually fix, or the gate warns forever about something no one can clear.

The negative controls matter as much as the positives: an over-eager cleaner that eats real
answer text is worse than the markup it removes, because nothing downstream can detect the loss.
"""
import textclean as tc


# ── glyphs ────────────────────────────────────────────────────────────────────
# Built with chr(), never pasted as literal characters: these codepoints are invisible in an
# editor, so a literal test would be unreadable and would not survive a copy/paste or a diff.
BULLET = chr(0xF0B7)          # Symbol-font bullet
TICK = chr(0xF0FC)            # Wingdings tick
ALPHA, BETA = chr(0xF061), chr(0xF062)
UNMAPPED = chr(0xE123)        # in the PUA, deliberately absent from the table


def test_symbol_font_bullets_become_real_bullets():
    got = tc.normalize_glyphs(f"Describe:\n{BULLET} cis\n{BULLET} trans")
    assert got == "Describe:\n\u2022 cis\n\u2022 trans"


def test_wingdings_tick_becomes_a_tick():
    assert tc.normalize_glyphs(f"tick ({TICK})") == "tick (\u2713)"


def test_symbol_greek_survives_for_science_subjects():
    got = tc.normalize_glyphs(f"{ALPHA}-glucose and {BETA}-amylase")
    assert got == "\u03b1-glucose and \u03b2-amylase"


def test_unmapped_private_use_becomes_a_space_not_a_deletion():
    """Deleting would weld two words together and there would be no trace of the damage."""
    assert tc.normalize_glyphs(f"word{UNMAPPED}word") == "word word"
    assert tc.count_pua(tc.normalize_glyphs(f"word{UNMAPPED}")) == 0


def test_clean_text_is_untouched_by_normalisation():
    plain = "Ordinary text with no font tricks at all."
    assert tc.normalize_glyphs(plain) == plain


# ── marking-scheme markup ─────────────────────────────────────────────────────
def test_leading_mark_allocation_is_stripped():
    got = tc.clean_scheme_answer("4 points @ 4 marks each \n\nEnergy intake greater than output.")
    assert got == "Energy intake greater than output."


def test_stemmed_allocation_is_stripped():
    assert tc.clean_scheme_answer("Breakfast = 6 marks Fruit and Fibre cereal") \
        == "Fruit and Fibre cereal"


def test_run_of_allocations_is_stripped():
    got = tc.clean_scheme_answer(
        "3 classes @ 2 marks each = 6 marks 1 example of each class = 3 marks Monosaccharide")
    assert got == "Monosaccharide"


def test_allocation_with_a_parenthetical_aside_is_stripped():
    assert tc.clean_scheme_answer("2 reasons (one for each food) @ 3 marks each Yoghurt adds flavour") \
        == "Yoghurt adds flavour"


def test_an_answer_that_is_only_allocation_becomes_empty():
    """Better unanswered — model_answers.py then authors one — than published as bookkeeping."""
    assert tc.clean_scheme_answer(
        "(Name = 4 marks; 2 sources @ 2 marks each; 2 symptoms @ 3 marks each)") == ""


# ── label bleed ───────────────────────────────────────────────────────────────
def test_trailing_next_part_label_is_removed():
    assert tc.clean_scheme_answer("Reduces LDL cholesterol. \n\n(c)") == "Reduces LDL cholesterol."


def test_trailing_compound_label_is_removed():
    assert tc.clean_scheme_answer("Calcium varies; etc.\n\n(c) (i)") == "Calcium varies; etc."


def test_trailing_question_number_is_removed():
    assert tc.clean_scheme_answer("Vitamin C aids absorption.\n\n7.") == "Vitamin C aids absorption."


def test_an_enumerating_answer_keeps_its_internal_labels():
    """(i)/(ii) followed by content are the answer's own structure, not a bleed."""
    text = "(i) bread, cakes, biscuits (ii) pastries, pizzas, pies"
    assert tc.clean_scheme_answer(text) == text


# ── reflow ────────────────────────────────────────────────────────────────────
def test_pdf_hardwrap_is_rejoined():
    got = tc.clean_scheme_answer("money that has to be spent on \n\nnecessities; it can be fixed.")
    assert got == "money that has to be spent on necessities; it can be fixed."


def test_authored_paragraphs_survive_reflow():
    """The ai-h1 answers are already good multi-paragraph prose; flattening them is a regression."""
    text = ("Low sugar was the strongest motivation at 66%. Consumers may choose fruit.\n\n"
            "Low fat ranked next at 56%. A lower-fat snack reduces energy density.")
    assert tc.clean_scheme_answer(text) == text


def test_bullet_lines_keep_their_line_breaks():
    text = "Factors:\n• culture\n• religion\n• budget"
    assert tc.clean_scheme_answer(text) == text


def test_semicolon_list_items_stay_on_their_own_lines():
    text = "(i) strong; durable;\nodourless;\n(ii) easy to store; recyclable;"
    assert "\n" in tc.clean_scheme_answer(text)


# ── negative controls: real answer text must never be touched ─────────────────
def test_prose_mentioning_marks_is_not_treated_as_an_allocation():
    for text in ("Stretch marks may appear on the skin during rapid growth.",
                 "The garment was pressed at 3 stages during construction.",
                 "Grill the fish for 5 minutes on each side until it flakes."):
        assert tc.clean_scheme_answer(text) == text


def test_short_official_answers_are_left_alone():
    for text in ("True; True; False.", "It aids digestion.", "Do not bleach. Dry flat."):
        assert tc.clean_scheme_answer(text) == text


def test_questions_keep_their_own_mark_totals():
    """clean_question must not strip markup — a question may legitimately state its marks."""
    text = "Name three sources of protein and give 2 marks worth of detail on each."
    assert tc.clean_question(text) == text


# ── content the cleaner destroyed before these tests existed ──────────────────
# Every case here is real text from the chemistry or history store that an earlier, more
# aggressive version of this module damaged. They are the reason the "=" sweep was removed and
# the label rule was narrowed.
def test_chemistry_equations_keep_their_equals_sign():
    for text in ("Kc = [HI]2/([H2][I2])",
                 "76-77%. Calculation: 8.9 / 890 = 0.01 mol; 0.03 x 306 = 9.18 g soap",
                 "CuO (mass of oxygen = 0.32 g; moles Cu = 0.02; empirical formula = CuO)",
                 "pH = 7 at equivalence"):
        assert tc.clean_scheme_answer(text) == text


def test_short_numeric_answers_are_not_wiped():
    """"0.06 g / l" and "25%" are complete answers; a "must contain a word" guard deleted them."""
    for text in ("0.06 g / l", "25%", "12"):
        assert tc.clean_scheme_answer(text) == text


def test_trailing_chemical_notation_is_not_mistaken_for_a_part_label():
    """"potassium (K)" lost its symbol once. State symbols would have been next."""
    for text in ("potassium (K)", "iron (III) oxide", "the product is H2O (l)",
                 "sodium chloride (s)"):
        assert tc.clean_scheme_answer(text) == text


def test_structural_formula_indentation_is_preserved():
    """Leading spaces carry the bond layout in an ASCII structural formula."""
    text = "CH3\n |\nCH3-C-CH3"
    assert tc.clean_scheme_answer(text) == text


def test_authored_answers_are_never_flagged_as_hard_wrapped():
    """ai-h1 answers are prose; clean_question does not reflow them, so flagging them would be a
    warning nothing could ever clear."""
    authored = ("Moles of HCl: n = M x V / 1000 = 0.1 mol\n\n"
                "(ii) Heat produced per mole: 5.71 / 0.1 = 57.1 kJ\n\n"
                "(iii) The heat of reaction is negative because the process is exothermic.")
    assert tc.artifacts({"question": "A question of adequate length.",
                         "model": authored, "model_source": "ai-h1"}) == []


# ── the invariants that keep this from silently rotting ───────────────────────
def test_cleaning_is_idempotent():
    for text in ("4 points @ 4 marks each \nEnergy in excess of output. \n\n(c)",
                 "Factors:\n• culture\n• religion",
                 "money spent on \n\nnecessities."):
        once = tc.clean_scheme_answer(text)
        assert tc.clean_scheme_answer(once) == once


def test_everything_the_detector_flags_the_cleaner_can_fix():
    """The drift guard. A defect the gate reports but no tool clears is a permanent false alarm."""
    dirty = [
        "4 points @ 6 marks each \nExpect reference to four food shelves. \n\n(b)",
        "Cannot be manufactured by the body; must be \nsupplied by the diet; etc. \n\n(c)",
        f"Sources of {BULLET} iron\n{BULLET} red meat; {BULLET} offal; etc.",
        "Name: 3 @ 2 marks Reasons: 2 @ 4 marks Frozen - cakes, fingers.",
    ]
    for text in dirty:
        assert tc.artifacts({"question": "A question of adequate length.", "model": text}), \
            f"detector missed a known-dirty answer: {text!r}"
        cleaned = tc.clean_scheme_answer(text)
        assert tc.artifacts({"question": "A question of adequate length.", "model": cleaned}) == [], \
            f"cleaner left something the detector still flags: {cleaned!r}"


def test_clean_answers_are_never_flagged():
    for text in ("Sensory preferences such as colour and flavour; culture; religion.",
                 "True; False; True.",
                 "Factors:\n• culture\n• religion\n• budget"):
        assert tc.artifacts({"question": "A question of adequate length.", "model": text}) == []


def test_glyph_junk_is_detected_in_the_question_too():
    """A tofu box in the question is as visible to a student as one in the answer."""
    part = {"question": f"Describe:{BULLET} cis fats", "model": "An answer."}
    assert "glyph_junk" in tc.artifacts(part)


# ── the pipeline stage ────────────────────────────────────────────────────────
def _store(tmp, rows):
    import json
    (tmp / "sub.json").write_text(json.dumps(rows))


def _with_store(rows, fn):
    """Run fn() with config.CANONICAL pointed at a throwaway store containing `rows`."""
    import json, shutil, tempfile
    from pathlib import Path
    import config
    tmp = Path(tempfile.mkdtemp())
    (tmp / "sub.json").write_text(json.dumps(rows))
    original = config.CANONICAL
    config.CANONICAL = tmp
    try:
        return fn()
    finally:
        config.CANONICAL = original
        shutil.rmtree(tmp)


def _row(model, source="scheme", question="A question of entirely adequate length."):
    return {"id": "sub-q1", "parts": [{"label": "(a)", "question": question, "marks": 10,
                                       "model": model, "model_source": source}]}


def test_backfill_counts_defects_before_and_after():
    rows = [_row("4 points @ 6 marks each \nEnergy in excess of output. \n\n(c)")]
    stats = _with_store(rows, lambda: tc.backfill("sub"))
    assert stats["before"]["scheme_markup"] == 1
    assert stats["after"] == {}, "the repair must clear what it counted"
    assert stats["answers_changed"] == 1


def test_backfill_clears_a_bookkeeping_only_answer_for_reauthoring():
    """model_source must go too, or model_answers.py will not pick the part up."""
    rows = [_row("(Name = 4 marks; 2 sources @ 2 marks each)")]
    stats = _with_store(rows, lambda: tc.backfill("sub"))
    assert stats["emptied"] == 1 and stats["emptied_ids"] == ["sub-q1#0"]


def test_backfill_does_not_strip_markup_from_authored_answers():
    """An ai-h1 answer gets whitespace repair only — never the marking-scheme rules."""
    text = "The scheme awards 3 marks for each named source of dietary iron."
    rows = [_row(text, source="ai-h1")]
    stats = _with_store(rows, lambda: tc.backfill("sub"))
    assert stats["answers_changed"] == 0


def test_backfill_on_a_missing_store_is_not_an_error():
    """run.py calls repair() unconditionally, before it knows whether anything was segmented."""
    assert tc.backfill("no-such-subject") == {}
    assert tc.repair("no-such-subject") == {}


def test_a_clean_store_needs_no_repair():
    rows = [_row("Sensory preferences such as colour and flavour; culture; religion.")]
    stats = _with_store(rows, lambda: tc.backfill("sub"))
    assert stats["before"] == {} and stats["answers_changed"] == 0


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
