"""ID construction and indexing invariants.

These lock in the fix for the defect that made two thirds of the history store unreachable:
a question id built from `{subject}-pp-{year}-{LV}-{label}` collides whenever a paper reuses a
label, and every subject reuses labels.
"""
import ids


def _row(**kw):
    base = {"subject": "history", "year": 2022, "level": "higher",
            "sectionId": "hist-section3", "chapterId": "hist-eur2", "label": "Q1"}
    base.update(kw)
    return base


def test_unique_when_every_field_collides():
    rows = [_row() for _ in range(3)]
    ids.assign_unique_ids(rows)
    assert len({r["id"] for r in rows}) == 3, [r["id"] for r in rows]
    assert rows[0]["id"].endswith("-Q1")          # first keeps the bare base
    assert rows[1]["id"].endswith("-Q1-2")
    assert rows[2]["id"].endswith("-Q1-3")


def test_ids_are_stable_across_reruns():
    """Same input in the same order must yield the same ids, or every re-run churns the store."""
    a = [_row(chapterId=c) for c in ("hist-eur1", "hist-eur2", "hist-eur2")]
    b = [_row(chapterId=c) for c in ("hist-eur1", "hist-eur2", "hist-eur2")]
    ids.assign_unique_ids(a)
    ids.assign_unique_ids(b)
    assert [r["id"] for r in a] == [r["id"] for r in b]


def test_taken_reserves_ids_from_earlier_papers():
    rows = [_row()]
    ids.assign_unique_ids(rows, taken={"history-pp-2022-HI-section3-eur2-Q1"})
    assert rows[0]["id"] == "history-pp-2022-HI-section3-eur2-Q1-2"


def test_chapter_distinguishes_same_label_in_same_section():
    """History's real shape: one Q1 per topic, all inside section 3."""
    rows = [_row(chapterId=f"hist-eur{i}") for i in range(1, 7)]
    ids.assign_unique_ids(rows)
    assert len({r["id"] for r in rows}) == 6
    assert not any(r["id"].endswith(("-2", "-3")) for r in rows)   # no suffixes needed


def test_shared_prefix_folded_only_when_shared():
    assert ids.question_base("history", 2022, "higher", "hist-section3", "hist-eur1", "Q1") == \
        "history-pp-2022-HI-section3-eur1-Q1"
    # different stems must NOT be folded, or two chapters could blur together
    assert ids.question_base("x", 2022, "higher", "alpha-s1", "beta-c1", "Q1") == \
        "x-pp-2022-HI-alphas1-betac1-Q1"
    # no hyphen to fold on
    assert ids.question_base("x", 2022, "higher", "s1", "c1", "Q1") == "x-pp-2022-HI-s1-c1-Q1"


def test_label_is_sanitised_not_trusted():
    r = [_row(label="Q 1 (a)/(b)")]
    ids.assign_unique_ids(r)
    assert r[0]["id"] == "history-pp-2022-HI-section3-eur2-Q1ab"


def test_missing_label_still_yields_an_id():
    r = [_row(label="")]
    ids.assign_unique_ids(r)
    assert r[0]["id"].endswith("-q")


def test_index_by_id_refuses_a_lossy_index():
    """The regression that mattered: a plain dict comprehension silently keeps the last row."""
    rows = [{"id": "a", "n": 1}, {"id": "a", "n": 2}, {"id": "b", "n": 3}]
    try:
        ids.index_by_id(rows, where="test")
    except ValueError as e:
        assert "duplicate" in str(e) and "test" in str(e)
    else:
        raise AssertionError("index_by_id accepted a store with duplicate ids")


def test_index_by_id_accepts_a_sound_store():
    rows = [{"id": "a"}, {"id": "b"}]
    idx = ids.index_by_id(rows)
    assert len(idx) == 2 and idx["a"] is rows[0]


def test_duplicate_ids_reports_counts():
    rows = [{"id": "a"}, {"id": "a"}, {"id": "a"}, {"id": "b"}]
    assert ids.duplicate_ids(rows) == {"a": 3}


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
