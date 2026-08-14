"""Exam Info is complete, validated, and rendered without a model call."""
import json

import exam_info


def complete():
    return {
        "subject": "test-subject", "totalMarks": 100, "totalMinutes": 60,
        "sections": [{
            "id": "test-a", "name": "Section A", "marks": 100, "color": "#000000",
            "tips": {"timing": "One hour.", "structure": "Answer clearly.",
                     "reminders": ["Read the question"]},
        }],
    }


def test_complete_record_passes():
    assert not exam_info.validate(complete(), "test-subject")


def test_old_empty_shell_is_rejected():
    data = complete()
    data["sections"][0].pop("marks")
    data["sections"][0].pop("tips")
    errors = exam_info.validate(data, "test-subject")
    assert any("marks" in x for x in errors) and any("tips" in x for x in errors)


def test_home_economics_record_is_publishable():
    data = exam_info.load("home-economics")
    assert not exam_info.validate(data, "home-economics")
    assert data["totalMinutes"] == 150
    assert [s["marks"] for s in data["sections"]] == [60, 180, 80]


TESTS = [(n[5:].replace("_", " "), f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
