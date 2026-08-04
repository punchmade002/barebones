"""Global cross-chapter flashcard consolidation.

Two properties matter more than any individual case here:

  * IDEMPOTENCE — `merge_exact` run on its own output must change nothing. Without it,
    the stage cannot be re-run safely, and a pipeline whose stages can't be re-run gets
    re-run anyway and quietly erodes the deck.
  * NEVER LOSE A CARD ON SILENCE — `apply_decisions` keeps every card unless the worker
    explicitly said "merge". A consolidation pass that deleted content whenever the model
    returned nothing useful would be the same class of defect as the lossy id index.
"""
import consolidate


def card(term, answer="an answer long enough to be real", prompt="", type_="concept"):
    c = {"term": term, "answer": answer, "type": type_}
    if prompt:
        c["prompt"] = prompt
    return c


ORDER = ["ch1", "ch2", "ch3"]


# ── exact merge ───────────────────────────────────────────────────────────────
def test_cross_chapter_duplicate_is_merged():
    store = {"ch1": [card("Acid")], "ch2": [card("acid")]}
    merged, report = consolidate.merge_exact(store, ORDER)
    assert sum(len(v) for v in merged.values()) == 1
    assert report[0]["term"] == "Acid" and report[0]["home"] == "ch1"


def test_home_chapter_is_the_first_in_scaffold_order():
    """Not the chapter with the best content — syllabus order, so the result is stable."""
    store = {"ch3": [card("Acid", "a much much longer and richer answer here")],
             "ch1": [card("Acid", "short one")]}
    merged, _ = consolidate.merge_exact(store, ORDER)
    assert merged["ch1"] and not merged["ch3"]


def test_merged_card_keeps_the_best_of_every_field():
    store = {"ch1": [card("Acid", "short", type_="concept")],
             "ch2": [card("Acid", "a considerably longer and better answer",
                          prompt="What is an acid?", type_="substance")]}
    merged, _ = consolidate.merge_exact(store, ORDER)
    got = merged["ch1"][0]
    assert got["answer"] == "a considerably longer and better answer"
    assert got["prompt"] == "What is an acid?"
    assert got["type"] == "substance"        # a specific type beats the 'concept' catch-all


def test_unknown_type_is_not_promoted_over_concept():
    store = {"ch1": [card("Acid", type_="concept")],
             "ch2": [card("Acid", type_="wingding")]}
    merged, _ = consolidate.merge_exact(store, ORDER, {"concept", "substance"})
    assert merged["ch1"][0]["type"] == "concept"


def test_distinct_terms_are_untouched():
    store = {"ch1": [card("Acid"), card("Base")], "ch2": [card("Salt")]}
    merged, report = consolidate.merge_exact(store, ORDER)
    assert sum(len(v) for v in merged.values()) == 3 and report == []


def test_within_chapter_duplicates_also_collapse():
    store = {"ch1": [card("Acid"), card("ACID")]}
    merged, _ = consolidate.merge_exact(store, ORDER)
    assert len(merged["ch1"]) == 1


def test_card_order_within_a_chapter_is_preserved():
    store = {"ch1": [card("Alpha"), card("Beta"), card("Gamma")]}
    merged, _ = consolidate.merge_exact(store, ORDER)
    assert [c["term"] for c in merged["ch1"]] == ["Alpha", "Beta", "Gamma"]


def test_merge_is_idempotent():
    """Re-running the stage must be a no-op, or the deck erodes on every pipeline run."""
    store = {"ch1": [card("Acid"), card("Base")], "ch2": [card("acid"), card("Salt")]}
    once, _ = consolidate.merge_exact(store, ORDER)
    twice, report = consolidate.merge_exact(once, ORDER)
    assert once == twice and report == []


def test_chapters_absent_from_the_scaffold_still_rank_stably():
    store = {"zzz": [card("Acid")], "ch1": [card("acid")]}
    merged, _ = consolidate.merge_exact(store, ORDER)
    assert merged["ch1"] and not merged["zzz"]      # scaffold chapters outrank unknown ones


def test_blank_terms_are_dropped_not_merged_together():
    store = {"ch1": [card(""), card("  ")], "ch2": [card("Acid")]}
    merged, _ = consolidate.merge_exact(store, ORDER)
    assert sum(len(v) for v in merged.values()) == 1


# ── near-duplicate clustering ─────────────────────────────────────────────────
def test_plural_variants_cluster():
    store = {"ch1": [card("Gas law")], "ch2": [card("Gas laws")]}
    clusters = consolidate.near_duplicate_clusters(store, ORDER)
    assert len(clusters) == 1 and len(clusters[0]["members"]) == 2


def test_close_spellings_cluster():
    store = {"ch1": [card("Covalent bond")], "ch2": [card("Covalent bonding")]}
    assert len(consolidate.near_duplicate_clusters(store, ORDER)) == 1


def test_unrelated_terms_do_not_cluster():
    store = {"ch1": [card("Photosynthesis")], "ch2": [card("Titration")]}
    assert consolidate.near_duplicate_clusters(store, ORDER) == []


def test_opposites_sharing_a_token_are_not_forced_together():
    """'Endothermic reaction' vs 'Exothermic reaction' may cluster, but must never be
    merged without a decision — which is exactly why clustering feeds a model, not a delete."""
    store = {"ch1": [card("Endothermic reaction")], "ch2": [card("Exothermic reaction")]}
    merged, report = consolidate.merge_exact(store, ORDER)
    assert sum(len(v) for v in merged.values()) == 2 and report == []


def test_singletons_are_not_clusters():
    store = {"ch1": [card("Acid")], "ch2": [card("Enthalpy")]}
    assert consolidate.near_duplicate_clusters(store, ORDER) == []


def test_clustering_is_deterministic():
    store = {"ch1": [card("Gas law"), card("Acid")], "ch2": [card("Gas laws"), card("acid rain")]}
    a = consolidate.near_duplicate_clusters(store, ORDER)
    b = consolidate.near_duplicate_clusters(store, ORDER)
    assert a == b


# ── applying decisions ────────────────────────────────────────────────────────
def _cluster_store():
    store = {"ch1": [card("Covalent bond", "bond answer")],
             "ch2": [card("Covalent bonding", "bonding answer")]}
    return store, consolidate.near_duplicate_clusters(store, ORDER)


def test_merge_decision_collapses_the_cluster():
    store, clusters = _cluster_store()
    d = {clusters[0]["cluster_id"]: {"action": "merge", "term": "Covalent bonding",
                                     "prompt": "What is covalent bonding?",
                                     "answer": "Sharing of electron pairs between atoms.",
                                     "type": "concept"}}
    out, applied = consolidate.apply_decisions(store, clusters, d)
    assert sum(len(v) for v in out.values()) == 1 and len(applied) == 1
    assert out["ch1"][0]["prompt"] == "What is covalent bonding?"


def test_keep_separate_changes_nothing():
    store, clusters = _cluster_store()
    d = {clusters[0]["cluster_id"]: {"action": "keep-separate"}}
    out, applied = consolidate.apply_decisions(store, clusters, d)
    assert sum(len(v) for v in out.values()) == 2 and applied == []


def test_missing_decision_keeps_every_card():
    """Silence must never delete content."""
    store, clusters = _cluster_store()
    out, applied = consolidate.apply_decisions(store, clusters, {})
    assert sum(len(v) for v in out.values()) == 2 and applied == []


def test_merge_with_a_blank_answer_is_refused():
    store, clusters = _cluster_store()
    d = {clusters[0]["cluster_id"]: {"action": "merge", "term": "X", "answer": "  "}}
    out, applied = consolidate.apply_decisions(store, clusters, d)
    assert sum(len(v) for v in out.values()) == 2 and applied == []


def test_merge_with_an_unknown_type_falls_back_to_concept():
    store, clusters = _cluster_store()
    d = {clusters[0]["cluster_id"]: {"action": "merge", "term": "X",
                                     "answer": "a real answer that is long enough",
                                     "type": "not-a-real-type"}}
    out, _ = consolidate.apply_decisions(store, clusters, d, {"concept", "substance"})
    assert [c for deck in out.values() for c in deck][0]["type"] == "concept"


TESTS = [(n[5:], f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
