from __future__ import annotations

import json
import tempfile
from pathlib import Path

import resources


def test_all_configured_subjects_meet_resource_contract():
    from config import SUBJECTS
    failures = {subject: resources.validate_bundle(subject) for subject in SUBJECTS}
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
                "sources": {
                    "research": {"provider": "Another site"},
                    "syllabus": {"authority": "NCCA"},
                },
            }))
            assert "research provider must be SimpleStudy" in resources.validate_bundle(subject)
        finally:
            resources.RESOURCES = old


TESTS = [
    ("all configured subjects meet the same resource contract",
     test_all_configured_subjects_meet_resource_contract),
    ("mixed research sources are rejected", test_contract_rejects_mixed_research_sources),
]
