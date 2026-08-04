"""Publication-gate checks, each driven by a synthetic store built to trip exactly one of them.

The point of these is that every check has been seen to FIRE at least once. A gate whose
checks have only ever been observed passing is indistinguishable from a gate that does nothing.
"""
import gate


def ctx(canon=None, cards=None, scaffold=None, baseline=None):
    """A Ctx with no disk access, so a check can be exercised in isolation."""
    c = gate.Ctx.__new__(gate.Ctx)
    c.subject = "history"
    c.canon = canon if canon is not None else []
    c.cards = cards or {}
    c.scaffold = scaffold or {}
    c.baseline = baseline
    c.parts = [(q, p) for q in c.canon for p in q.get("parts", [])]
    return c


def row(qid="history-pp-2022-HI-section1-ire1-Q1", **kw):
    r = {"id": qid, "year": 2022, "level": "higher", "chapterId": "hist-ire1",
         "source": "LC History Higher 2022 — Q1",
         "parts": [{"label": "(a)", "question": "A real question of adequate length.",
                    "marks": 10, "model": "An answer."}]}
    r.update(kw)
    return r


def severities(findings, check):
    return [f.severity for f in findings if f.check == check]


# ── each check must fire on its own trigger ───────────────────────────────────
def test_duplicate_question_ids_block():
    f = list(gate.check_question_ids(ctx([row(), row()])))
    assert f and f[0].severity == gate.BLOCK and "duplicate" in f[0].message


def test_clean_ids_produce_no_finding():
    assert not list(gate.check_question_ids(ctx([row("a"), row("b")])))


def test_malformed_source_blocks():
    bad = row(source="LC Home-economics Higher 2022 — Q1")
    f = list(gate.check_sources(ctx([bad])))
    assert f and f[0].severity == gate.BLOCK and "malformed" in f[0].message


def test_wellformed_source_passes():
    assert not list(gate.check_sources(ctx([row()])))


def test_reference_suffix_does_not_trip_the_source_check():
    r = row(source="LC History Ordinary 2005 — A1 [REFERENCE — pre-current-syllabus]")
    assert not list(gate.check_sources(ctx([r])))


def test_placeholder_part_blocks():
    r = row(parts=[{"label": "", "question": "Part (a)", "marks": 0, "model": ""}])
    f = list(gate.check_parts(ctx([r])))
    assert f and f[0].severity == gate.BLOCK


def test_ai_share_over_cap_blocks():
    rows = [row(f"q{i}", parts=[{"label": "", "question": "A long enough question here.",
                                 "marks": 5, "model": "x", "model_source": "ai-h1"}])
            for i in range(6)]
    rows.append(row("q9"))
    f = list(gate.check_ai_share(ctx(rows)))
    assert f and f[0].severity == gate.BLOCK


def test_ai_share_under_cap_is_silent():
    rows = [row(f"q{i}") for i in range(9)]
    rows.append(row("qa", parts=[{"label": "", "question": "A long enough question here.",
                                  "marks": 5, "model": "x", "model_source": "ai-h1"}]))
    assert not list(gate.check_ai_share(ctx(rows)))


def test_missing_diagram_file_blocks():
    r = row(parts=[{"label": "", "question": "See the diagram shown below here.", "marks": 5,
                    "model": "x", "diagram": "exam-images/history/does-not-exist.png"}])
    f = [x for x in gate.check_diagrams(ctx([r])) if x.severity == gate.BLOCK]
    assert f and "does not exist" in f[0].message


def test_empty_flashcard_blocks():
    f = list(gate.check_flashcards(ctx([row()], cards={"hist-ire1": [{"term": "", "definition": "d"}]})))
    assert any(x.severity == gate.BLOCK for x in f), f


def test_a_card_whose_prompt_is_just_the_term_is_reported():
    """'Q1: Food Pyramid' — the defect the authored prompt replaces."""
    cards = {"hist-ire1": [{"term": "Home Rule", "prompt": "Home Rule",
                            "answer": "A campaign for Irish self-government within the UK."}]}
    f = list(gate.check_flashcards(ctx([row()], cards=cards)))
    assert any("prompt-is-term" in x.message for x in f), f


def test_an_unanswerable_prompt_blocks():
    """A flashcard carries no diagram, so a prompt pointing at one is broken content."""
    cards = {"hist-ire1": [{"term": "Home Rule",
                            "prompt": "Explain the process shown in the diagram above.",
                            "answer": "A campaign for Irish self-government within the UK."}]}
    f = list(gate.check_flashcards(ctx([row()], cards=cards)))
    assert any(x.severity == gate.BLOCK and "self-contained" in x.message for x in f), f


def test_a_legacy_deck_reports_but_does_not_block():
    """Cards with no prompt render as they always did — bad, but not newly broken, so a
    republish of existing content must not be blocked by the schema change alone."""
    cards = {"hist-ire1": [{"term": "Home Rule",
                            "definition": "A campaign for Irish self-government in the UK."}]}
    f = list(gate.check_flashcards(ctx([row()], cards=cards)))
    assert f and all(x.severity != gate.BLOCK for x in f), f


def test_prompt_coverage_is_reported():
    cards = {"hist-ire1": [{"term": "A", "definition": "x" * 30},
                           {"term": "B", "prompt": "What is B?", "answer": "y" * 30}]}
    f = list(gate.check_card_prompts(ctx([row()], cards=cards)))
    assert f and "1/2" in f[0].message and f[0].severity == gate.WARN


def test_full_prompt_coverage_is_not_a_warning():
    cards = {"hist-ire1": [{"term": "B", "prompt": "What is B?", "answer": "y" * 30}]}
    f = list(gate.check_card_prompts(ctx([row()], cards=cards)))
    assert f and f[0].severity == gate.INFO


def test_types_outside_the_subject_vocabulary_warn():
    cards = {"hist-ire1": [{"term": "A", "definition": "x" * 30, "type": "substance"}]}
    f = list(gate.check_card_types(ctx([row()], cards=cards)))
    assert any("outside the history vocabulary" in x.message for x in f), f


def test_a_deck_that_is_all_concept_warns_that_the_vocabulary_does_not_fit():
    """Chemistry's deck was 91% 'concept' under History's enum."""
    cards = {"hist-ire1": [{"term": f"t{i}", "definition": "x" * 30, "type": "concept"}
                           for i in range(10)]}
    f = list(gate.check_card_types(ctx([row()], cards=cards)))
    assert any("not fitting this subject" in x.message for x in f), f


def test_a_well_spread_type_distribution_is_only_informational():
    cards = {"hist-ire1": [{"term": f"p{i}", "definition": "x" * 30, "type": "person"}
                           for i in range(6)]
             + [{"term": f"c{i}", "definition": "x" * 30, "type": "concept"} for i in range(4)]}
    f = list(gate.check_card_types(ctx([row()], cards=cards)))
    assert f and all(x.severity == gate.INFO for x in f), f


def test_spelling_variants_are_reported():
    """A hyphen vs an en-dash survives the duplicate check but is still one card."""
    cards = {"hist-ire1": [{"term": "Berlin Wall (1961-1989)", "definition": "x" * 30}],
             "hist-eur1": [{"term": "Berlin Wall (1961–1989)", "definition": "x" * 30}]}
    f = list(gate.check_term_variants(ctx([row()], cards=cards)))
    assert f and f[0].severity == gate.WARN and "Berlin Wall" in f[0].message


def test_variants_never_block():
    """variant_key folds aggressively, so it informs a human — it never deletes or blocks."""
    cards = {"a": [{"term": f"gas law{'s' if i else ''}", "definition": "x" * 30}
                   for i in range(2)]}
    f = list(gate.check_term_variants(ctx([row()], cards=cards)))
    assert f and all(x.severity != gate.BLOCK for x in f)


def test_case_only_differences_are_left_to_the_duplicate_check():
    """Otherwise the same defect is reported twice under two names."""
    cards = {"a": [{"term": "Home Rule", "definition": "x" * 30}],
             "b": [{"term": "home rule", "definition": "x" * 30}]}
    assert not list(gate.check_term_variants(ctx([row()], cards=cards)))


def test_cross_chapter_duplicate_cards_are_found():
    """The defect per-chapter dedup structurally cannot see."""
    cards = {"hist-ire1": [{"term": "Home Rule", "definition": "a"}],
             "hist-ire2": [{"term": "home rule", "definition": "b"}]}
    f = list(gate.check_flashcard_duplicates(ctx([row()], cards=cards)))
    assert f and "duplicated across chapters" in f[0].message


def test_low_duplicate_rate_warns_rather_than_blocks():
    cards = {"a": [{"term": f"t{i}", "definition": "d"} for i in range(50)] + [{"term": "t0", "definition": "d"}]}
    f = list(gate.check_flashcard_duplicates(ctx([row()], cards=cards)))
    assert f and f[0].severity == gate.WARN, f


def test_high_duplicate_rate_blocks():
    cards = {"a": [{"term": "same", "definition": "d"} for _ in range(10)]}
    f = list(gate.check_flashcard_duplicates(ctx([row()], cards=cards)))
    assert f and f[0].severity == gate.BLOCK


def test_empty_chapter_coverage_warns():
    sc = {"chapters": [{"id": "hist-ire1"}, {"id": "hist-ire2"}]}
    f = list(gate.check_coverage(ctx([row()], scaffold=sc)))
    assert any("no questions" in x.message for x in f)


def test_offscaffold_chapter_tag_warns():
    sc = {"chapters": [{"id": "hist-ire1"}]}
    f = list(gate.check_coverage(ctx([row(chapterId="hist-nope")], scaffold=sc)))
    assert any("not in the scaffold" in x.message for x in f)


def test_card_budget_is_never_a_blocker():
    """A hard cap would make the generator drop content to hit a number."""
    cards = {"a": [{"term": f"t{i}", "definition": "d"} for i in range(500)]}
    f = list(gate.check_card_budgets(ctx([row()], cards=cards)))
    assert f and all(x.severity != gate.BLOCK for x in f)


def test_severe_regression_blocks():
    base = {"recorded": "2026-01-01", "counts": {"questions": 100, "parts": 100,
                                                 "answered_parts": 100, "cards": 100, "diagrams": 0}}
    f = list(gate.check_regression(ctx([row()], baseline=base)))
    assert any(x.severity == gate.BLOCK for x in f), f


def test_mild_regression_warns_only():
    base = {"recorded": "2026-01-01", "counts": {"questions": 100, "parts": 100,
                                                 "answered_parts": 100, "cards": 0, "diagrams": 0}}
    c = ctx([row(f"q{i}") for i in range(97)], baseline=base)
    f = list(gate.check_regression(c))
    assert f and all(x.severity == gate.WARN for x in f), f


def test_growth_is_not_a_regression():
    base = {"recorded": "2026-01-01", "counts": {"questions": 1, "parts": 1,
                                                 "answered_parts": 1, "cards": 0, "diagrams": 0}}
    c = ctx([row(f"q{i}") for i in range(50)], baseline=base)
    assert not [x for x in gate.check_regression(c) if x.severity in (gate.BLOCK, gate.WARN)]


def test_missing_store_blocks():
    assert [f.severity for f in gate.run("subject-that-does-not-exist")] == [gate.BLOCK]


def test_blockers_only_returns_block_severity():
    """merge.gate() delegates to this, so a WARN leaking in would stop publishing."""
    real = gate.run("history")
    assert set(gate.blockers("history")) == {f.message for f in real if f.severity == gate.BLOCK}


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
