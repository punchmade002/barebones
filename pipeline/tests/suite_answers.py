"""H1 answer jobs address parts by stable id, including when labels repeat."""
import model_answers


def _question():
    return {
        "id": "homeeconomics-test-Q1",
        "parts": [
            {"label": "(i)", "question": "First prompt", "marks": 4, "model": ""},
            {"label": "(i)", "question": "Second prompt", "marks": 4, "model": ""},
        ],
    }


def test_prompt_uses_stable_part_ids_for_repeated_labels():
    prompt = model_answers.variable_suffix("home-economics", _question(), "Test")
    assert "[homeeconomics-test-Q1@@0]" in prompt
    assert "[homeeconomics-test-Q1@@1]" in prompt


def test_apply_maps_repeated_labels_by_pid():
    q = _question()
    filled = model_answers._apply(q, [
        {"pid": "homeeconomics-test-Q1@@0", "label": "(i)", "answer": "First answer"},
        {"pid": "homeeconomics-test-Q1@@1", "label": "(i)", "answer": "Second answer"},
    ])
    assert filled == 2
    assert [p["model"] for p in q["parts"]] == ["First answer", "Second answer"]


def test_output_must_cover_expected_pids_in_order():
    job = {"prompt": "[q@@0] first\n[q@@1] second\n"}
    good = {"answers": [
        {"pid": "q@@0", "answer": "First"},
        {"pid": "q@@1", "answer": "Second"},
    ]}
    assert model_answers.validate_output(good, job)
    assert not model_answers.validate_output({"answers": list(reversed(good["answers"]))}, job)


def test_curated_level_abbreviations_are_recognised():
    assert model_answers.q_level({"source": "LC Biology HL 2018 — Q7"}) == "higher"
    assert model_answers.q_level({"source": "LC Biology OL 2018 — Q7"}) == "ordinary"
    assert model_answers.q_level({"level": "higher", "source": "legacy"}) == "higher"


TESTS = [
    ("prompt uses stable ids for repeated labels", test_prompt_uses_stable_part_ids_for_repeated_labels),
    ("apply maps repeated labels by pid", test_apply_maps_repeated_labels_by_pid),
    ("output covers expected pids in order", test_output_must_cover_expected_pids_in_order),
    ("curated level abbreviations are recognised", test_curated_level_abbreviations_are_recognised),
]
