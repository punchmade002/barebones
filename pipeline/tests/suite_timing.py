"""Timing: turning marks into "how long should this take", and capping answers at what a
student can actually write.

Two rules are under test. A part's time is its share of the paper's marks scaled to the paper's
duration. An answer's length target is then capped at that time × WRITING_WPM — so a 4-mark part
on a 400-mark/180-minute paper gets ~2 minutes and therefore ~70 words, no matter how many points
the marking scheme rewards. Without the cap the pipeline authored exemplars nobody could write in
the time, which is the defect these tests exist to prevent.

The exam-info store is written to a temp path and config's cache is cleared around each case, so
these run without any real subject data.
"""
import json

import config
import timing
import validate

SUBJECT = "zz-timing-test"


def _with_exam_info(total_marks, total_minutes, fn):
    """Install a temporary exam-info store for SUBJECT, run fn, then remove it."""
    path = config.CANONICAL / f"exam-info.{SUBJECT}.json"
    path.write_text(json.dumps({"subject": SUBJECT, "totalMarks": total_marks,
                                "totalMinutes": total_minutes, "sections": []}))
    config._EXAM_INFO_CACHE.pop(SUBJECT, None)
    try:
        return fn()
    finally:
        path.unlink(missing_ok=True)
        config._EXAM_INFO_CACHE.pop(SUBJECT, None)


# ── minutes from marks ────────────────────────────────────────────────────────
def test_minutes_are_the_share_of_the_paper():
    # 40 of 400 marks on a 180-minute paper = a tenth of the time.
    assert _with_exam_info(400, 180, lambda: config.recommended_minutes(SUBJECT, 40)) == 18


def test_minutes_are_none_without_exam_info():
    config._EXAM_INFO_CACHE.pop(SUBJECT, None)
    assert config.recommended_minutes(SUBJECT, 40) is None


def test_minutes_are_none_without_marks():
    assert _with_exam_info(400, 180, lambda: config.recommended_minutes(SUBJECT, 0)) is None


def test_a_tiny_part_still_gets_a_minute():
    """Rounding must never produce a 0-minute label."""
    assert _with_exam_info(400, 180, lambda: config.recommended_minutes(SUBJECT, 1)) == 1


# ── words from minutes ────────────────────────────────────────────────────────
def test_writable_words_uses_the_writing_speed():
    assert config.writable_words(10) == 10 * config.WRITING_WPM


def test_time_caps_a_scheme_heavy_target():
    """12 scheme points wants ~420 words, but a 2-minute part allows only 70."""
    def check():
        capped = config.recommended_words(SUBJECT, marks=4, points=12)
        assert capped == config.writable_words(config.recommended_minutes(SUBJECT, 4)), capped
        assert capped < 420
    _with_exam_info(400, 180, check)


def test_a_generous_time_budget_does_not_inflate_the_target():
    """The cap only ever shortens. A part with plenty of time keeps its scheme-derived length."""
    def check():
        uncapped = 3 * config.WORDS_PER_POINT                    # ~105
        got = config.recommended_words(SUBJECT, marks=100, points=3)
        assert got <= max(15, round(uncapped / 10) * 10)
    _with_exam_info(400, 180, check)


def test_without_exam_info_the_old_behaviour_stands():
    config._EXAM_INFO_CACHE.pop(SUBJECT, None)
    assert config.recommended_words(SUBJECT, marks=0, points=10) == 350


# ── stamping the records ──────────────────────────────────────────────────────
def _rows():
    return [{"id": "q1", "parts": [{"label": "(a)", "marks": 40, "question": "x"},
                                   {"label": "(b)", "marks": 20, "question": "y"}]}]


def test_stamp_writes_part_and_question_totals():
    def check():
        rows = _rows()
        rep = timing.stamp(SUBJECT, rows)
        assert [p["time_minutes"] for p in rows[0]["parts"]] == [18, 9]
        assert rows[0]["time_minutes"] == 27
        assert rep["stamped"] == 2 and rep["missing"] == 0
    _with_exam_info(400, 180, check)


def test_stamp_omits_labels_it_cannot_derive():
    """No exam-info means no label at all — an invented duration would be worse than none."""
    config._EXAM_INFO_CACHE.pop(SUBJECT, None)
    rows = _rows()
    rep = timing.stamp(SUBJECT, rows)
    assert all("time_minutes" not in p for p in rows[0]["parts"])
    assert "time_minutes" not in rows[0]
    assert rep["missing"] == 2


def test_stamp_is_idempotent_and_self_correcting():
    def check():
        rows = _rows()
        timing.stamp(SUBJECT, rows)
        rows[0]["parts"][0]["marks"] = 20          # a corrected mark
        timing.stamp(SUBJECT, rows)
        assert rows[0]["parts"][0]["time_minutes"] == 9
        assert rows[0]["time_minutes"] == 18
    _with_exam_info(400, 180, check)


# ── the validator ─────────────────────────────────────────────────────────────
def test_an_overlong_answer_is_flagged_as_unwritable():
    part = {"question": "A real question here", "marks": 4, "time_minutes": 2,
            "model": " ".join(["word"] * 300)}          # 2 min allows ~70 words
    assert "not_writable_in_time" in validate.part_defects(SUBJECT, part)


def test_an_answer_inside_the_budget_is_not_flagged():
    part = {"question": "A real question here", "marks": 4, "time_minutes": 2,
            "model": " ".join(["word"] * 70)}
    assert "not_writable_in_time" not in validate.part_defects(SUBJECT, part)


def test_untimed_parts_are_not_flagged():
    """No time label means the check has nothing to judge against — it must stay silent."""
    part = {"question": "A real question here", "marks": 4,
            "model": " ".join(["word"] * 3000)}
    assert "not_writable_in_time" not in validate.part_defects(SUBJECT, part)


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
