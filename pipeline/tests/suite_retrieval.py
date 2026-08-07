"""Retrieval + corpus-cache behaviour.

These cover the two failures that made the resource bundle much less useful than it looked:
a head slice of the corpus (so deep material was unreachable), and an mtime-based cache that
could serve a partial corpus indefinitely.
"""
import json
from unittest.mock import patch

import resources
import retrieval


def _corpus(*sections: tuple[str, str]) -> str:
    return "\n".join(f"\n===== GUIDE: {name} =====\n{body}" for name, body in sections)


def _search(corpus: str, query: str, budget: int = 2_000):
    retrieval._index.cache_clear()
    try:
        with patch.object(resources, "corpus", return_value=corpus):
            return retrieval.search("test-subject", query, budget)
    finally:
        retrieval._index.cache_clear()


# The bug this replaced: flashcards passed corpus[:80_000] to every chapter, so a chapter whose
# material sat past that point saw none of its own source text. Depth must not matter.
def test_material_deep_in_the_corpus_is_still_found():
    filler = ("General administrative notes about timetabling and classroom procedure. " * 400)
    corpus = _corpus(("front.md", filler),
                     ("deep.md", "Electrolysis drives a redox reaction using electrical energy. "
                                 "The anode is the site of oxidation."))
    assert len(corpus) > 25_000, "fixture must bury the target well past a head slice"
    text, score = _search(corpus, "electrolysis anode oxidation")
    assert score > 0
    assert "Electrolysis" in text, "material late in the corpus was not retrieved"
    assert "timetabling" not in text


def test_budget_is_respected():
    body = " ".join(f"Enzyme catalysis fact number {i} about active sites." for i in range(600))
    text, _ = _search(_corpus(("g.md", body)), "enzyme catalysis active sites", budget=1_500)
    assert 0 < len(text) <= 1_500 + 200, len(text)   # allow the source-label lines


def test_no_match_returns_empty_not_arbitrary_text():
    corpus = _corpus(("g.md", "Shareholders supply capital and receive dividends from profit."))
    text, score = _search(corpus, "photosynthesis chloroplast thylakoid")
    assert score == 0 and text == "", "an unrelated query must not return filler as if on-topic"


def test_excerpt_of_an_empty_bundle_is_empty():
    assert _search("", "anything") == ("", 0.0)


# The cache served ~5% of every bundle because a corpus written just after its sources looked
# fresh forever. Identity must come from the inputs, not from mtime ordering.
def test_fingerprint_changes_when_a_source_changes(tmpdir=None):
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        sub = root / "zz-fp"
        sub.mkdir()
        f = sub / "guide-a.md"
        f.write_text("alpha")
        old = resources.RESOURCES
        try:
            resources.RESOURCES = root
            fp1 = resources._fingerprint("zz-fp", [f])
            f.write_text("alpha beta gamma")            # different size
            fp2 = resources._fingerprint("zz-fp", [f])
            assert fp1 != fp2, "editing a source must change the fingerprint"
            assert resources._fingerprint("zz-fp", [f]) == fp2, "fingerprint must be stable"
        finally:
            resources.RESOURCES = old


def test_ingest_version_is_part_of_the_fingerprint():
    from pathlib import Path
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        root = Path(d); sub = root / "zz-v"; sub.mkdir()
        f = sub / "guide-a.md"; f.write_text("alpha")
        old_root, old_v = resources.RESOURCES, resources.INGEST_VERSION
        try:
            resources.RESOURCES = root
            fp1 = resources._fingerprint("zz-v", [f])
            resources.INGEST_VERSION = old_v + 1
            assert resources._fingerprint("zz-v", [f]) != fp1, \
                "bumping INGEST_VERSION must force every subject to re-ingest"
        finally:
            resources.RESOURCES, resources.INGEST_VERSION = old_root, old_v


TESTS = [(n[5:].replace("_", " "), f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
