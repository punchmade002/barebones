"""Curated Biology import/export invariants."""
import biology_repair


def test_parser_reads_the_curated_biology_bank():
    rows = biology_repair.load_curated()
    assert len(rows) in {24, 28}
    assert sum(len(q["parts"]) for q in rows) in {55, 66}
    assert all(q["subject"] == "biology" for q in rows)


def test_verified_orphans_have_unique_ids_and_images():
    rows = biology_repair.ORPHAN_QUESTIONS
    assert len(rows) == 4
    assert len({q["id"] for q in rows}) == 4
    assert len({q["legacy_image"] for q in rows}) == 4
    assert sum(len(q["parts"]) for q in rows) == 11


TESTS = [
    ("parser reads curated Biology bank", test_parser_reads_the_curated_biology_bank),
    ("verified Biology orphans are unique", test_verified_orphans_have_unique_ids_and_images),
]
