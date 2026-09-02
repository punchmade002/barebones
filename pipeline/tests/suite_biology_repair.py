"""Curated Biology import/export invariants."""
import biology_repair


def test_parser_reads_the_curated_biology_bank():
    rows = biology_repair.load_curated()
    assert len(rows) in {24, 28}
    assert sum(len(q["parts"]) for q in rows) in {55, 66}
    assert all(q["subject"] == "biology" for q in rows)


def test_verified_orphans_have_unique_ids_and_images():
    rows = biology_repair.ORPHAN_QUESTIONS
    assert len(rows) == 4
    assert len({q["id"] for q in rows}) == 4
    assert len({q["legacy_image"] for q in rows}) == 4
    assert sum(len(q["parts"]) for q in rows) == 11


def _row(qid, year, level, label, text, source=""):
    return {"id": qid, "subject": "biology", "year": year, "level": level,
            "label": label, "source": source or f"LC Biology {level.title()} {year} — {label}",
            "parts": [{"label": "(a)", "question": text, "marks": 5, "model": ""}]}


def test_expansion_reconcile_preserves_curated_identity_and_deduplicates_generated_rows():
    curated = [_row("curated-q1", 2020, "higher", "Q1", "Name the organelle shown.")]
    generated = [
        _row("generated-curated-q1", 2020, "higher", "Q1", "Name the organelle shown."),
        _row("generated-q2-short", 2020, "higher", "Q2", "Define osmosis."),
        {**_row("generated-q2-rich", 2020, "higher", "Q2", "Define osmosis precisely."),
         "parts": [{"label": "(a)", "question": "Define osmosis precisely.", "marks": 5},
                   {"label": "(b)", "question": "Give one example.", "marks": 5}]},
        _row("generated-q3", 2020, "ordinary", "Q3", "State one function of the nucleus."),
    ]
    kept, report = biology_repair.reconcile_rows(generated, curated)
    assert [q["id"] for q in kept] == ["generated-q2-rich", "generated-q3"]
    assert report["dropped_curated_identity"] == 1
    assert report["dropped_generated_identity_duplicates"] == 1
    assert all("[LEGACY — pre-2027 syllabus]" in q["source"] for q in kept)
    numeric = _row("numeric-label", 2024, "ordinary", "10.", "State one function.")
    assert biology_repair.exam_identity(numeric) == (2024, "ordinary", 10)


def test_duplicate_audit_checks_ids_exam_identity_exact_and_near_whole_questions():
    repeated = "Explain how water moves across a selectively permeable membrane down a water potential gradient."
    rows = [
        _row("same-id", 2020, "higher", "Q1", repeated),
        _row("same-id", 2020, "higher", "Q1", repeated),
        _row("different-id", 2021, "higher", "Q2", repeated),
    ]
    report = biology_repair.audit_rows(rows)
    assert report["duplicate_ids"]
    assert report["duplicate_exam_identities"]
    assert report["exact_whole_question_duplicates"]
    assert not report["clean"]


TESTS = [
    ("parser reads curated Biology bank", test_parser_reads_the_curated_biology_bank),
    ("verified Biology orphans are unique", test_verified_orphans_have_unique_ids_and_images),
    ("Biology expansion reconciliation is preservation-first", test_expansion_reconcile_preserves_curated_identity_and_deduplicates_generated_rows),
    ("Biology duplicate audit catches every duplicate class", test_duplicate_audit_checks_ids_exam_identity_exact_and_near_whole_questions),
]
