"""Diagram completeness: every part is inspected and source-page metadata beats fuzzy matching."""
import images


def _row(question="Explain how starch changes when heated in water.", source_page=3):
    return [{
        "id": "home-economics-pp-2024-HI-hom-food-Q1",
        "year": 2024,
        "level": "higher",
        "source": "LC Home Economics Higher 2024 — Q1",
        "parts": [{"label": "(a)", "question": question, "source_page": source_page,
                   "diagram": ""}],
    }]


def test_uncued_parts_are_still_visually_inspected():
    pages = {(2024, "higher"): [("paper.pdf", 2, "unrelated extracted text", "")]}
    cands = images._candidates(_row(), pages, {}, False)
    assert len(cands) == 1 and cands[0]["page"] == 2


def test_source_page_wins_over_fuzzy_text_location():
    pages = {(2024, "higher"): [
        ("paper.pdf", 0, "Explain how starch changes when heated in water.", ""),
        ("paper.pdf", 2, "page holding the actual supplied figure", ""),
    ]}
    cands = images._candidates(_row(), pages, {}, False)
    assert cands[0]["page"] == 2


def test_malformed_figure_worker_output_is_requeued():
    assert images.validate_output({"results": [{"key": "q#0", "has_figure": False}]})
    assert images.validate_output({"results": [{"key": "q#0", "has_figure": True,
                                                  "bbox": [0.1, 0.2, 0.8, 0.9]}]})
    assert not images.validate_output({"results": [{"key": "q#0", "has_figure": True}]})
    assert not images.validate_output({"results": []})


TESTS = [(n[5:].replace("_", " "), f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
