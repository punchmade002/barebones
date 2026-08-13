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
    c.figures = {}
    c.figure_report_exists = False
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


def test_split_paper_source_passes():
    r = row(source="LC Home Economics Higher 2024 Paper BC — Q1")
    c = ctx([r])
    c.subject = "home-economics"
    assert not list(gate.check_sources(c))


def test_reference_suffix_does_not_trip_the_source_check():
    r = row(source="LC History Ordinary 2005 — A1 [REFERENCE — pre-current-syllabus]")
    assert not list(gate.check_sources(ctx([r])))


def test_placeholder_part_blocks():
    r = row(parts=[{"label": "", "question": "Part (a)", "marks": 0, "model": ""}])
    f = list(gate.check_parts(ctx([r])))
    assert f and f[0].severity == gate.BLOCK


def test_repeated_empty_part_labels_are_allowed():
    r = row(parts=[
        {"label": "", "question": "First separately marked prompt.", "marks": 3, "model": "x"},
        {"label": "", "question": "Second separately marked prompt.", "marks": 3, "model": "y"},
    ])
    assert not list(gate.check_part_labels(ctx([r])))


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


def test_uninspected_parts_block_figure_audit():
    c = ctx([row()])
    c.figure_report_exists = True
    f = list(gate.check_figure_audit(c))
    assert f and f[0].severity == gate.BLOCK and "never visually inspected" in f[0].message


def test_explicit_supplied_visual_without_diagram_blocks():
    r = row(parts=[{"label": "", "question": "Study the following food label and answer.",
                    "marks": 5, "model": "x", "diagram": ""}])
    c = ctx([r])
    c.figure_report_exists = True
    c.figures = {f"{r['id']}#0": {"has_figure": False}}
    f = list(gate.check_figure_audit(c))
    assert any("explicitly reference" in x.message for x in f)


def test_student_created_sketch_is_not_a_supplied_visual():
    assert not gate.SUPPLIED_FIGURE_RE.search("Name one design principle shown on your sketch.")
    assert not gate.SUPPLIED_FIGURE_RE.search("Name three charges shown on a domestic electricity bill.")


def test_empty_flashcard_blocks():
    f = list(gate.check_flashcards(ctx([row()], cards={"hist-ire1": [{"term": "", "definition": "d"}]})))
    assert f and f[0].severity == gate.BLOCK


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
