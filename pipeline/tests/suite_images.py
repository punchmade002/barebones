"""Diagram completeness: every part is inspected and source-page metadata beats fuzzy matching."""
import images
import images_verify
import crop_cleanup


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


def test_crop_verifier_requires_relevance_completeness_and_tightness():
    result = {"key": "q#0", "relevant": True, "complete": True, "tight": True,
              "needs_recrop": False}
    good = {"results": [result]}
    assert images_verify.validate_output(good)
    for field in ("relevant", "complete", "tight"):
        bad_result = dict(result); bad_result.pop(field)
        assert not images_verify.validate_output({"results": [bad_result]})


def test_crop_verifier_requires_every_batched_key_in_order():
    results = [{"key": key, "relevant": True, "complete": True, "tight": True,
                "needs_recrop": False} for key in ("q#0", "q#1")]
    job = {"meta": {"keys": ["q#0", "q#1"]}}
    assert images_verify.validate_output({"results": results}, job)
    assert not images_verify.validate_output({"results": list(reversed(results))}, job)


def test_visual_evidence_filter_is_conservative():
    class Page:
        def __init__(self, images=(), drawings=(), blocks=()):
            self._images, self._drawings, self._blocks = images, drawings, blocks
        def get_images(self, full=True): return self._images
        def get_drawings(self): return self._drawings
        def get_text(self, kind): return {"blocks": list(self._blocks)}
    class Doc:
        def __init__(self, page): self.page = page
        def load_page(self, _index): return self.page
    old_open = images.fitz.open
    try:
        images.fitz.open = lambda _path: Doc(Page())
        assert not images._page_has_visual_evidence("p.pdf", 0, [{"cue": False}])
        assert images._page_has_visual_evidence("p.pdf", 0, [{"cue": True}])
        images.fitz.open = lambda _path: Doc(Page(images=[("img",)]))
        assert images._page_has_visual_evidence("p.pdf", 0, [{"cue": False}])
        images.fitz.open = lambda _path: Doc(Page(drawings=[{"rect": 1}]))
        assert images._page_has_visual_evidence("p.pdf", 0, [{"cue": False}])
    finally:
        images.fitz.open = old_open


def test_cleanup_distinguishes_question_instructions_from_chart_titles():
    q = {"the", "graph", "below", "shows", "housing", "sector", "changes"}
    assert crop_cleanup._looks_like_instruction(["The", "graph", "below", "shows"], q)
    assert not crop_cleanup._looks_like_instruction(
        ["Breakdown", "of", "the", "Housing", "Sector", "2000"], q)


TESTS = [(n[5:].replace("_", " "), f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
