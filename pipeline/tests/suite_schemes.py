"""Official marking-scheme output validation."""
import schemes
from types import SimpleNamespace


def test_real_scheme_coverage_passes():
    assert schemes.validate_output({"answers": [
        {"pid": "q1@@0", "answer": "Accepted point", "points": 1},
        {"pid": "q2@@0", "answer": "", "points": 2},
        {"pid": "q3@@0", "answer": "", "points": 0},
    ]})


def test_all_empty_placeholder_fails():
    assert not schemes.validate_output({"answers": [
        {"pid": "q1@@0", "answer": "", "points": 0},
        {"pid": "q2@@0", "answer": "", "points": 0},
    ]})


def test_duplicate_pid_fails():
    assert not schemes.validate_output({"answers": [
        {"pid": "q1@@0", "answer": "a", "points": 1},
        {"pid": "q1@@0", "answer": "b", "points": 1},
    ]})


def test_job_pid_coverage_and_order_are_exact():
    job = {"prompt": "[q1@@0] first\n[q2@@0] second\n"}
    assert schemes.validate_output({"answers": [
        {"pid": "q1@@0", "answer": "a", "points": 1},
        {"pid": "q2@@0", "answer": "b", "points": 1},
    ]}, job)
    assert not schemes.validate_output({"answers": [
        {"pid": "q2@@0", "answer": "b", "points": 1},
        {"pid": "q1@@0", "answer": "a", "points": 1},
    ]}, job)


def test_table_number_artifact_fails():
    assert not schemes.validate_output({"answers": [
        {"pid": "q1@@0", "answer": "2.", "points": 0},
        {"pid": "q2@@0", "answer": "real answer", "points": 1},
    ]})


def test_prompt_keeps_scheme_text_beyond_old_60k_cutoff():
    marker = "FINAL_SECTION_C_OFFICIAL_ANSWER"
    scheme = "x" * 70_000 + marker
    prompt = schemes.build_prompt("home-economics", scheme, ["[q@@0] question"])
    assert marker in prompt


def test_parse_strips_trailing_next_question_number():
    content = [SimpleNamespace(type="tool_use", name="emit_scheme_answers", input={"answers": [
        {"pid": "q@@0", "answer": "Official marking points.\n\n7.", "points": 1}
    ]})]
    assert schemes.parse_result(content)[0]["answer"] == "Official marking points."


TESTS = [("real scheme coverage passes", test_real_scheme_coverage_passes),
         ("all-empty placeholder fails", test_all_empty_placeholder_fails),
         ("duplicate pid fails", test_duplicate_pid_fails),
         ("job pid coverage and order are exact", test_job_pid_coverage_and_order_are_exact),
         ("table number artifact fails", test_table_number_artifact_fails),
         ("prompt retains full scheme", test_prompt_keeps_scheme_text_beyond_old_60k_cutoff),
         ("parse strips trailing next question number", test_parse_strips_trailing_next_question_number)]
