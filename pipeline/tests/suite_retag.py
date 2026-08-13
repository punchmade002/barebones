"""Retag worker-output validation."""
import retag


def test_valid_assignments_pass():
    assert retag.validate_output({"assignments": [
        {"id": "q1", "chapterId": "hom-family-society", "confidence": 0.9}
    ]})


def test_malformed_assignments_fail():
    assert not retag.validate_output({"assignments": [{"id": "q1", "confidence": 0.9}]})
    assert not retag.validate_output({"assignments": "not-a-list"})


TESTS = [("valid assignments pass", test_valid_assignments_pass),
         ("malformed assignments fail", test_malformed_assignments_fail)]
