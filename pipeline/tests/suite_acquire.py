"""Acquisition manifest invariants."""
from acquire_form import _merge_rows


def _row(*, paper: str, path: str, size: int = 100) -> dict:
    return {
        "subject": "home-economics", "year": "2024", "level": "higher",
        "paper": paper, "version": "EV", "kind": "papers", "status": "on-course",
        "bytes": str(size), "path": path,
    }


def test_component_rows_supersede_old_alias():
    rows = _merge_rows(
        [_row(paper="", path="old-section-a.pdf")],
        [_row(paper="A", path="section-a.pdf"), _row(paper="BC", path="section-bc.pdf")],
    )
    assert [(r["paper"], r["path"]) for r in rows] == [
        ("A", "section-a.pdf"), ("BC", "section-bc.pdf")
    ]


def test_one_component_does_not_hide_existing_whole_paper():
    rows = _merge_rows(
        [_row(paper="", path="whole.pdf")],
        [_row(paper="A", path="section-a.pdf")],
    )
    assert {r["paper"] for r in rows} == {"", "A"}


def test_larger_retry_replaces_prior_manifest_row():
    rows = _merge_rows(
        [_row(paper="A", path="short.pdf", size=10)],
        [_row(paper="A", path="complete.pdf", size=100)],
    )
    assert len(rows) == 1
    assert rows[0]["path"] == "complete.pdf"


def test_successful_smaller_forced_result_replaces_wrong_cached_asset():
    rows = _merge_rows(
        [_row(paper="A", path="wrong-large.pdf", size=1000)],
        [_row(paper="A", path="correct-smaller.pdf", size=100)],
    )
    assert len(rows) == 1
    assert rows[0]["path"] == "correct-smaller.pdf"


TESTS = [
    ("component rows supersede old alias", test_component_rows_supersede_old_alias),
    ("single component keeps whole paper", test_one_component_does_not_hide_existing_whole_paper),
    ("larger retry replaces prior row", test_larger_retry_replaces_prior_manifest_row),
    ("successful smaller force replaces wrong asset", test_successful_smaller_forced_result_replaces_wrong_cached_asset),
]
