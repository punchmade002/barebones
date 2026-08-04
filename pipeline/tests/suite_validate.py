"""Content validation — the distinction the re-queue and the merge gate both depend on.

An empty answer is NORMAL at segment time (model_answers.py fills it later) but a real defect
at the merge gate. Collapsing those two would either re-queue every paper forever or publish
unanswered questions.
"""
import validate


def part(**kw):
    p = {"label": "(a)", "question": "A question of entirely adequate length.", "marks": 10,
         "model": "An answer."}
    p.update(kw)
    return p


def test_good_part_has_no_problems():
    assert validate.part_problems(part()) == []


def test_placeholder_question_is_an_extraction_failure():
    assert "placeholder-question" in validate.part_problems(part(question="Part (a)"))
    assert "placeholder-question" in validate.extraction_problems(part(question="Part (a)"))


def test_short_question_is_an_extraction_failure():
    assert "question-too-short" in validate.extraction_problems(part(question="Why?"))


def test_empty_answer_is_a_gate_problem_but_not_an_extraction_failure():
    p = part(model="")
    assert "empty-answer" in validate.part_problems(p)
    assert validate.extraction_problems(p) == []


def test_answer_to_nothing_is_caught():
    p = part(question="Part (a)", model="Generic prose.", model_source="ai-h1")
    assert "answer-to-nothing" in validate.part_problems(p)


def test_validate_output_requeues_a_mostly_broken_paper():
    bad = {"questions": [{"parts": [part(question="Part (a)") for _ in range(5)]}]}
    assert validate.validate_output(bad) is False


def test_validate_output_tolerates_a_little_noise():
    parts = [part() for _ in range(19)] + [part(question="Part (a)")]
    assert validate.validate_output({"questions": [{"parts": parts}]}) is True


def test_validate_output_rejects_empty():
    assert validate.validate_output({"questions": []}) is False
    assert validate.validate_output("not a dict") is False


def test_empty_answers_alone_do_not_requeue():
    """Otherwise every paper re-queues forever, since answers arrive in a later stage."""
    parts = [part(model="") for _ in range(10)]
    assert validate.validate_output({"questions": [{"parts": parts}]}) is True


def test_scan_canonical_locates_bad_parts():
    canon = [{"id": "q1", "parts": [part(), part(model="")]}]
    found = validate.scan_canonical(canon)
    assert len(found) == 1 and found[0]["problems"] == ["empty-answer"]


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
