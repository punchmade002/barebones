"""Segmentation: the golden paper, plus the shaping rules to_canonical is responsible for.

The golden fixture is the real 2022 Higher history paper — 48 questions drawn from just 4
distinct labels (Q1–Q4, each reused once per topic). Under the old id scheme those 48 rows
collapsed to 4 ids. It is the sharpest available test of the fix.
"""
import json
from pathlib import Path

import segment
from run_tests import golden, FIXTURES

FX = json.loads((FIXTURES / "segment-input-history-2022-HL.json").read_text())


def test_golden_2022_higher_paper():
    rows = segment.to_canonical("history", FX["digest"], FX["questions"])
    golden("segment-expected-history-2022-HL.json", rows)


def test_golden_paper_really_does_reuse_labels():
    """Guards the fixture itself: if this stops being true the golden test proves nothing."""
    labels = [q["label"] for q in FX["questions"]]
    assert len(labels) == 48 and len(set(labels)) == 4, (len(labels), len(set(labels)))


def test_every_question_in_the_golden_paper_gets_its_own_id():
    rows = segment.to_canonical("history", FX["digest"], FX["questions"])
    assert len({r["id"] for r in rows}) == len(rows) == 48


def test_no_collision_across_papers_via_taken():
    first = segment.to_canonical("history", FX["digest"], FX["questions"])
    second = segment.to_canonical("history", FX["digest"], FX["questions"],
                                  taken={r["id"] for r in first})
    assert not ({r["id"] for r in first} & {r["id"] for r in second})


def test_source_line_uses_the_display_name_not_capitalize():
    d = {"year": 2019, "level": "higher", "status": "on-course"}
    q = [{"label": "Q1", "sectionId": "s", "chapterId": "c", "parts": [{"question": "x", "marks": 1}]}]
    row = segment.to_canonical("home-economics", d, q)[0]
    assert row["source"] == "LC Home Economics Higher 2019 — Q1", row["source"]
    assert "Home-economics" not in row["source"]


def test_reference_papers_keep_their_suffix():
    d = {"year": 2005, "level": "ordinary", "status": "reference"}
    q = [{"label": "A1", "sectionId": "s", "chapterId": "c", "parts": [{"question": "x", "marks": 1}]}]
    row = segment.to_canonical("history", d, q)[0]
    assert row["source"].endswith("[REFERENCE — pre-current-syllabus]"), row["source"]


def test_level_and_label_are_stored_not_sniffed():
    """images.py used to recover the level by looking for 'Higher' in the source string."""
    d = {"year": 2019, "level": "ordinary", "status": "on-course"}
    q = [{"label": "Q7", "sectionId": "s", "chapterId": "c", "parts": [{"question": "x", "marks": 1}]}]
    row = segment.to_canonical("history", d, q)[0]
    assert row["level"] == "ordinary" and row["label"] == "Q7"
    assert segment.level_of(row) == "ordinary"


def test_level_of_falls_back_for_legacy_rows():
    """A store written before `level` existed must still read correctly."""
    assert segment.level_of({"source": "LC History Higher 2022 — Q1"}) == "higher"
    assert segment.level_of({"source": "LC History Ordinary 2022 — Q1"}) == "ordinary"


def test_non_dict_parts_are_dropped():
    d = {"year": 2019, "level": "higher", "status": "on-course"}
    q = [{"label": "Q1", "sectionId": "s", "chapterId": "c",
          "parts": [{"question": "ok", "marks": 1}, "garbage", None]}]
    row = segment.to_canonical("history", d, q)[0]
    assert len(row["parts"]) == 1


def test_missing_label_falls_back_to_position():
    d = {"year": 2019, "level": "higher", "status": "on-course"}
    q = [{"sectionId": "s", "chapterId": "c", "parts": [{"question": "x", "marks": 1}]}]
    row = segment.to_canonical("history", d, q)[0]
    assert row["label"] == "q1"


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
