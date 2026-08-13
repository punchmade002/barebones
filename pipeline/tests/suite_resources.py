from __future__ import annotations

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import resources


def test_all_supported_subjects_meet_resource_contract():
    failures = {subject: resources.validate_bundle(subject)
                for subject in resources.SUPPORTED_SUBJECTS}
    failures = {subject: errors for subject, errors in failures.items() if errors}
    assert not failures, failures


def test_contract_rejects_mixed_research_sources():
    with tempfile.TemporaryDirectory() as tmp:
        old = resources.RESOURCES
        resources.RESOURCES = Path(tmp)
        try:
            subject = "test-subject"
            folder = resources.RESOURCES / subject
            folder.mkdir()
            (folder / "spec-syllabus.pdf").write_bytes(b"%PDF-test")
            (folder / "guide-simplestudy.md").write_text(
                "## Source\n\n## Unit and topic structure\n\n## Pipeline guidance\n"
            )
            (folder / "worked-example-guidance.md").write_text(
                "## Source pattern\n\n## Required answer shape\n\n## Original model\n"
            )
            (folder / "manifest.json").write_text(json.dumps({
                "schemaVersion": 1,
                "subject": subject,
                "level": "Higher",
                "unitCount": 1,
                "topicCount": 1,
                "alignmentStatus": "aligned",
                "sources": {
                    "research": {"provider": "Another site"},
                    "syllabus": {"authority": "NCCA", "firstExamYear": 2025},
                },
            }))
            assert "research provider must be SimpleStudy" in resources.validate_bundle(subject)
        finally:
            resources.RESOURCES = old


def test_retrieval_returns_topic_specific_material():
    import retrieval
    corpus = """
===== GUIDE: first.md =====
Photosynthesis uses light energy in chloroplasts to make carbohydrate.
The rate can be investigated by controlling temperature and carbon dioxide.

===== GUIDE: second.md =====
Shareholders supply company capital and may receive dividends from profit.
Directors manage the company on their behalf.
"""
    retrieval._index.cache_clear()
    try:
        with patch.object(resources, "corpus", return_value=corpus):
            text, score = retrieval.search("test-retrieval", "photosynthesis chloroplasts", 900)
        assert score > 0
        assert "Photosynthesis" in text
        assert "Shareholders" not in text
    finally:
        retrieval._index.cache_clear()


def test_failed_extraction_marker_invalidates_cache():
    assert resources._cache_is_complete("a complete syllabus corpus")
    assert not resources._cache_is_complete("[skipped PDF: install pymupdf]")
    assert not resources._cache_is_complete("[unreadable PDF: damaged]")


TESTS = [
    ("all supported subjects meet the same resource contract",
     test_all_supported_subjects_meet_resource_contract),
    ("mixed research sources are rejected", test_contract_rejects_mixed_research_sources),
    ("resource retrieval returns topic-specific material",
     test_retrieval_returns_topic_specific_material),
    ("failed extraction marker invalidates cache",
     test_failed_extraction_marker_invalidates_cache),
]
