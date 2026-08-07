"""The exam-information stage — filling the app's exam breakdown from the specification.

`normalise` is where a model's answer is made safe to publish. Two things must hold: section ids
have to be real scaffold ids (the app matches each question's sectionId against them, so an
invented id renders nothing), and colours have to be assigned here rather than by the model, so a
regenerated breakdown doesn't reshuffle the palette under a returning student.

`validate_output` is the re-queue hook: an answer without both totals cannot drive the timing
model, so it is sent back to the worker rather than accepted and silently degraded.
"""
import exam_info


SECTIONS = [{"id": "bio-sectionA", "title": "Section A"},
            {"id": "bio-sectionB", "title": "Section B"},
            {"id": "bio-sectionC", "title": "Section C"}]


def _answer(**over):
    data = {
        "totalMarks": 400,
        "totalMinutes": 180,
        "sections": [{
            "id": "bio-sectionB", "name": "Section B – Medium", "marks": 60,
            "minutesPerQuestion": 15,
            "tips": {"timing": "t", "structure": "s", "reminders": ["r1", "r2"]},
            "chapterIds": ["bio1"],
        }, {
            "id": "bio-sectionA", "name": "Section A – Short", "marks": 100,
            "tips": {"timing": "t", "structure": "s", "reminders": []},
            "chapterIds": [],
        }],
    }
    data.update(over)
    return data


class _ToolUse:
    type = "tool_use"
    name = "emit_exam_info"

    def __init__(self, data):
        self.input = data


# ── normalise ─────────────────────────────────────────────────────────────────
def test_totals_are_carried_through():
    e = exam_info.normalise("biology", _answer(), SECTIONS)
    assert e["totalMarks"] == 400 and e["totalMinutes"] == 180
    assert e["subject"] == "biology"


def test_sections_are_reordered_to_scaffold_order():
    """The model returned B before A; the panel must follow the paper."""
    e = exam_info.normalise("biology", _answer(), SECTIONS)
    assert [s["id"] for s in e["sections"]] == ["bio-sectionA", "bio-sectionB"]


def test_an_invented_section_id_is_dropped():
    bad = _answer()
    bad["sections"].append({"id": "not-a-real-section", "name": "Ghost", "marks": 10,
                            "tips": {"timing": "t", "structure": "s", "reminders": []}})
    e = exam_info.normalise("biology", bad, SECTIONS)
    assert all(s["id"] in {"bio-sectionA", "bio-sectionB"} for s in e["sections"])


def test_colours_are_assigned_here_and_are_stable():
    first = exam_info.normalise("biology", _answer(), SECTIONS)
    second = exam_info.normalise("biology", _answer(), SECTIONS)
    assert [s["color"] for s in first["sections"]] == [s["color"] for s in second["sections"]]
    assert first["sections"][0]["color"] == exam_info.PALETTE[0]


def test_a_section_the_model_omitted_does_not_shift_the_others_colours():
    """Colour comes from scaffold position, so dropping section C can't recolour A and B."""
    e = exam_info.normalise("biology", _answer(), SECTIONS)
    by_id = {s["id"]: s["color"] for s in e["sections"]}
    assert by_id["bio-sectionA"] == exam_info.PALETTE[0]
    assert by_id["bio-sectionB"] == exam_info.PALETTE[1]


def test_tips_are_always_present_even_when_thin():
    e = exam_info.normalise("biology", _answer(), SECTIONS)
    for s in e["sections"]:
        assert set(s["tips"]) == {"timing", "structure", "reminders"}
        assert isinstance(s["tips"]["reminders"], list)


def test_optional_fields_appear_only_when_set():
    plain = exam_info.normalise("biology", _answer(), SECTIONS)
    assert "notice" not in plain and "timingNote" not in plain
    noted = exam_info.normalise("biology", _answer(timingNote="Two papers"), SECTIONS)
    assert noted["timingNote"] == "Two papers"


def test_a_new_specification_with_no_paper_yet_is_representable():
    e = exam_info.normalise("biology", _answer(sections=[], notice="No paper sat yet."), SECTIONS)
    assert e["sections"] == [] and e["notice"] == "No paper sat yet."


# ── validate_output ───────────────────────────────────────────────────────────
def test_missing_totals_are_requeued():
    assert not exam_info.validate_output([_ToolUse({"sections": [], "totalMarks": 400})])


def test_no_sections_and_no_notice_is_requeued():
    assert not exam_info.validate_output(
        [_ToolUse({"totalMarks": 400, "totalMinutes": 180, "sections": []})])


def test_a_complete_answer_passes():
    assert exam_info.validate_output([_ToolUse(_answer())])


def test_an_empty_breakdown_passes_when_explained():
    assert exam_info.validate_output(
        [_ToolUse({"totalMarks": 400, "totalMinutes": 180, "sections": [],
                   "notice": "Specification is new."})])


# ── rendered JS ───────────────────────────────────────────────────────────────
def test_render_js_is_additive():
    """It must assign into window.EXAM_BREAKDOWN, not replace it — the hand-written entries in
    exam-breakdown.js have to survive alongside it."""
    out = exam_info.render_js("biology", exam_info.normalise("biology", _answer(), SECTIONS))
    text = out.read_text()
    out.unlink(missing_ok=True)
    assert "window.EXAM_BREAKDOWN = window.EXAM_BREAKDOWN || {}" in text
    assert 'window.EXAM_BREAKDOWN["biology"]' in text


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
