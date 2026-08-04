"""Stage 6b — GLOBAL flashcard consolidation, across every chapter of a subject.

flashcards.py dedups inside one chapter because it makes one model call per chapter, and a
model that never sees chapter B cannot know it already wrote "acid" there. That is a
structural blind spot, not a tuning problem: Chemistry shipped 34 terms duplicated across
chapters (14.3% of the whole deck) with every per-chapter dedup passing.

This module closes it in two passes, and the split is the whole point:

  * EXACT (`merge_exact`) — same term after case/whitespace folding. Unarguably the same card,
    so it is merged in plain Python with no model call and no judgement. This is what removes
    the bulk of the duplication, deterministically and for free.

  * NEAR (`near_duplicate_clusters`) — "Le Chatelier's Principle" vs "Le Chatelier principle",
    "Acid Rain" vs "acid rain formation". Whether these are one card or two is a judgement
    call, so ONLY these reach a model. Clusters are found by shared-token bucketing plus
    difflib, so the model sees a handful of real decisions instead of the whole deck.

A merged card takes its HOME CHAPTER from the first chapter it appears in (syllabus order —
where the topic is introduced) and its CONTENT from the best copy of each field. Keeping those
two rules separate is why the merge is stable: re-running it on its own output is a no-op.

    python3 consolidate.py chemistry              # report only, changes nothing
    python3 consolidate.py chemistry --apply      # write the exact-merged store
    python3 consolidate.py chemistry --clusters   # queue near-duplicate clusters for the worker
    python3 consolidate.py chemistry collect      # apply the worker's merge decisions
"""
from __future__ import annotations
import json
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

from config import CANONICAL, REPORTS, card_types, display_name
from validate import normalise_term, variant_key

NEAR_RATIO = 0.87           # difflib ratio on normalised terms above which two cards cluster
MIN_TOKEN = 4               # tokens shorter than this are too common to bucket on
MAX_BUCKET = 400            # skip pathologically large buckets rather than go quadratic on them


# ── helpers ───────────────────────────────────────────────────────────────────
def _answer(card: dict) -> str:
    """Legacy decks store the text as `definition`; new ones as `answer`."""
    return (card.get("answer") or card.get("definition") or "").strip()


def _chapter_order(by_chapter: dict, scaffold_order: list | None) -> dict[str, int]:
    """Rank chapters so 'first chapter wins' is a defined, stable rule.

    Scaffold order is syllabus order, which is what we want a merged card to follow. Chapters
    absent from the scaffold keep a stable rank after it rather than being dropped.
    """
    rank = {cid: i for i, cid in enumerate(scaffold_order or [])}
    nxt = len(rank)
    for cid in by_chapter:                       # dict order is insertion order — deterministic
        if cid not in rank:
            rank[cid] = nxt
            nxt += 1
    return rank


def _best(cards: list[dict], types: set | None = None) -> dict:
    """One card built from the best of every field across duplicates.

    `cards` must arrive home-copy-first; every tie-break falls back to that order, which is
    what makes the result deterministic.

    Longest wins for prompt/answer (the fuller copy is the one worth keeping). The displayed
    `term` prefers a capitalised spelling over an all-lowercase one — merging "Acid" with
    "acid" should not publish the lowercase variant just because it sorts later. For `type`, a
    specific value beats the 'concept' catch-all, so a card correctly typed in one chapter
    isn't degraded by a lazier copy in another.
    """
    prompt = max(((c.get("prompt") or "").strip() for c in cards), key=len, default="")
    answer = max((_answer(c) for c in cards), key=len, default="")
    terms = [t for t in ((c.get("term") or "").strip() for c in cards) if t]
    term = min(terms, key=lambda t: (t.islower(), terms.index(t))) if terms else ""
    specific = [t for t in ((c.get("type") or "").strip() for c in cards)
                if t and t != "concept" and (types is None or t in types)]
    out = {"term": term, "prompt": prompt, "answer": answer,
           "type": specific[0] if specific else "concept"}
    if not prompt:
        out.pop("prompt")
    return out


# ── exact merge (no model) ────────────────────────────────────────────────────
def merge_exact(by_chapter: dict, scaffold_order: list | None = None,
                types: set | None = None) -> tuple[dict, list[dict]]:
    """Collapse cards sharing a `normalise_term` key across the WHOLE subject.

    Returns (merged_by_chapter, merges) where `merges` records every collapse for the report:
    {term, home, dropped_from:[chapter], copies:int}. Chapters keep their original card order,
    minus what moved out; the surviving card sits at the position of its first copy.
    """
    rank = _chapter_order(by_chapter, scaffold_order)
    groups: dict[str, list[tuple[int, int, str, dict]]] = defaultdict(list)
    for cid, deck in by_chapter.items():
        for i, card in enumerate(deck or []):
            key = normalise_term(card.get("term"))
            if key:
                groups[key].append((rank[cid], i, cid, card))

    keep: dict[str, dict[int, dict]] = {cid: {} for cid in by_chapter}
    merges: list[dict] = []
    for key, entries in groups.items():
        entries.sort(key=lambda e: (e[0], e[1]))          # home = earliest chapter, then position
        home_rank, home_idx, home_cid, _ = entries[0]
        card = _best([e[3] for e in entries], types)
        keep[home_cid][home_idx] = card
        if len(entries) > 1:
            others = sorted({e[2] for e in entries[1:]} - {home_cid})
            merges.append({"term": card["term"], "home": home_cid,
                           "dropped_from": others, "copies": len(entries)})

    merged = {cid: [keep[cid][i] for i in sorted(keep[cid])] for cid in by_chapter}
    merges.sort(key=lambda m: (-m["copies"], m["term"]))
    return merged, merges


# ── near-duplicate clustering (what the model is for) ─────────────────────────
class _Union:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def join(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def near_duplicate_clusters(by_chapter: dict, scaffold_order: list | None = None,
                            ratio: float = NEAR_RATIO) -> list[dict]:
    """Clusters of cards that are probably — but not certainly — the same card.

    Run this AFTER merge_exact, so anything left is a genuine judgement call. Pairs are only
    compared when they share a token of MIN_TOKEN+ characters or an exact `variant_key`, which
    keeps this near-linear instead of comparing all pairs of a 5,000-card deck.
    """
    rank = _chapter_order(by_chapter, scaffold_order)
    flat = [(rank[cid], cid, card) for cid, deck in by_chapter.items() for card in (deck or [])
            if (card.get("term") or "").strip()]
    flat.sort(key=lambda e: (e[0], normalise_term(e[2].get("term"))))
    if len(flat) < 2:
        return []

    keys = [normalise_term(c.get("term")) for _, _, c in flat]
    vkeys = [variant_key(c.get("term")) for _, _, c in flat]

    buckets: dict[str, list[int]] = defaultdict(list)
    for i, vk in enumerate(vkeys):
        buckets[f"v:{vk}"].append(i)                      # exact variant match: always compare
        for tok in {t for t in vk.split() if len(t) >= MIN_TOKEN}:
            buckets[f"t:{tok}"].append(i)

    uf = _Union(len(flat))
    for members in buckets.values():
        if len(members) < 2 or len(members) > MAX_BUCKET:
            continue
        for a_pos, a in enumerate(members):
            for b in members[a_pos + 1:]:
                if uf.find(a) == uf.find(b):
                    continue
                if vkeys[a] == vkeys[b] or SequenceMatcher(None, keys[a], keys[b]).ratio() >= ratio:
                    uf.join(a, b)

    grouped: dict[int, list[int]] = defaultdict(list)
    for i in range(len(flat)):
        grouped[uf.find(i)].append(i)

    clusters = []
    for root in sorted(grouped):
        idxs = grouped[root]
        if len(idxs) < 2:
            continue
        members = [{"chapter": flat[i][1], "term": (flat[i][2].get("term") or "").strip(),
                    "prompt": (flat[i][2].get("prompt") or "").strip(),
                    "answer": _answer(flat[i][2]), "type": flat[i][2].get("type") or "concept"}
                   for i in idxs]
        clusters.append({"cluster_id": f"k{len(clusters)}", "members": members})
    return clusters


# ── applying model decisions ──────────────────────────────────────────────────
def apply_decisions(by_chapter: dict, clusters: list[dict], decisions: dict,
                    types: set | None = None) -> tuple[dict, list[dict]]:
    """Fold the worker's merge/keep-separate verdicts back into the store.

    An absent or malformed decision means KEEP SEPARATE. A consolidation stage that silently
    deleted cards whenever the worker returned nothing useful would be the same class of bug
    as the lossy index this pipeline already had.
    """
    drop: dict[str, set] = defaultdict(set)
    replace: dict[tuple, dict] = {}
    applied: list[dict] = []

    for cl in clusters:
        d = decisions.get(cl["cluster_id"]) or {}
        if (d.get("action") or "").strip() != "merge":
            continue
        members = cl["members"]
        home = members[0]["chapter"]
        card = {"term": (d.get("term") or members[0]["term"]).strip(),
                "prompt": (d.get("prompt") or members[0].get("prompt") or "").strip(),
                "answer": (d.get("answer") or members[0]["answer"]).strip(),
                "type": d.get("type") or members[0].get("type") or "concept"}
        if types is not None and card["type"] not in types:
            card["type"] = "concept"
        if not card["term"] or not card["answer"]:
            continue                                      # refuse to trade real cards for a blank
        if not card["prompt"]:
            card.pop("prompt")
        for m in members[1:]:
            drop[m["chapter"]].add(normalise_term(m["term"]))
        replace[(home, normalise_term(members[0]["term"]))] = card
        applied.append({"term": card["term"], "home": home,
                        "absorbed": [m["term"] for m in members[1:]]})

    out: dict[str, list] = {}
    for cid, deck in by_chapter.items():
        kept = []
        for card in deck or []:
            key = normalise_term(card.get("term"))
            if (cid, key) in replace:
                kept.append(replace[(cid, key)])
            elif key in drop.get(cid, ()):
                continue
            else:
                kept.append(card)
        out[cid] = kept
    return out, applied


# ── agent stage ───────────────────────────────────────────────────────────────
def _stage(subject: str) -> str:
    return f"consolidate-{subject}"


EMIT_TOOL = {
    "name": "emit_merge_decision",
    "description": "Decide whether a cluster of similar flashcards is one card or several.",
    "input_schema": {
        "type": "object",
        "properties": {
            "action": {"type": "string", "enum": ["merge", "keep-separate"],
                       "description": "merge only if every listed card teaches the SAME thing"},
            "term": {"type": "string", "description": "the single best term (merge only)"},
            "prompt": {"type": "string",
                       "description": "one exam-style question for the merged card (merge only)"},
            "answer": {"type": "string", "description": "the merged answer (merge only)"},
            "type": {"type": "string", "description": "type value for the merged card"},
        },
        "required": ["action"],
    },
}

_TASK = ("Decide whether each cluster of similar flashcards is really ONE card. Merge only "
         "when every card in the cluster teaches the same thing; if they are genuinely "
         "different (e.g. a process vs the substance it acts on), keep them separate. "
         "When merging, return the best term, ONE exam-style question, and a merged answer.")


def build_prompt(subject: str, cluster: dict) -> str:
    listing = "\n\n".join(
        f"[{i + 1}] chapter: {m['chapter']}\n    term: {m['term']}\n"
        f"    question: {m['prompt'] or '(none)'}\n    answer: {m['answer']}"
        for i, m in enumerate(cluster["members"]))
    allowed = ", ".join(sorted(card_types(subject)))
    return f"""These Leaving Certificate {display_name(subject)} flashcards were written for
different topics but look like they may be the same card.

{listing}

Decide: is this ONE card or several?

- MERGE only if they all teach the same thing. Then return the clearest `term`, ONE
  `prompt` (a real exam-style question a student can answer without seeing anything else),
  an `answer` that keeps the best detail from every copy, and a `type`.
- KEEP-SEPARATE if they are genuinely different ideas that merely share wording — for
  example a process and the substance it acts on, or a general term and a specific case.

Allowed `type` values: {allowed}.
Return ONLY via the emit_merge_decision tool.
"""


def _load(subject: str) -> dict:
    p = CANONICAL / f"flashcards.{subject}.json"
    if not p.exists():
        raise SystemExit(f"no flashcard store at {p} — run `python3 flashcards.py {subject}` first")
    return json.loads(p.read_text())


def _scaffold_order(subject: str) -> list[str]:
    p = Path(__file__).parent / "scaffold" / f"{subject}.json"
    if not p.exists():
        return []
    return [c["id"] for c in json.loads(p.read_text()).get("chapters", [])]


def _save(subject: str, store: dict, before: int | None = None) -> None:
    import flashcards
    (CANONICAL / f"flashcards.{subject}.json").write_text(
        json.dumps(store, ensure_ascii=False, indent=2))
    flashcards.render_js(subject, store)
    if before:
        _warn_if_gate_will_see_a_regression(subject, before, sum(len(v) for v in store.values()))


def _warn_if_gate_will_see_a_regression(subject: str, before: int, after: int) -> None:
    """Consolidation removes cards on purpose, and the gate's regression check cannot tell a
    deliberate dedup from a run that quietly halved the deck — nor should it guess. Say so
    plainly, and leave re-snapshotting as an explicit human act, because a stage that
    re-baselined itself would disarm the one check that protects live content.
    """
    import gate
    base = REPORTS / f"baseline-{subject}.json"
    if not base.exists() or not before:
        return
    was = json.loads(base.read_text()).get("counts", {}).get("cards")
    if not was:
        return
    drop = (was - after) / was
    if drop > gate.REGRESSION_WARN:
        print(f"\nNOTE: the deck is now {after} cards vs a baseline of {was} ({drop:.0%} lower).\n"
              f"      That drop is the duplicate removal, but the gate cannot know that and "
              f"will {'BLOCK' if drop > gate.REGRESSION_BLOCK else 'warn'}.\n"
              f"      Check `python3 gate.py {subject}`, then re-baseline deliberately:\n"
              f"        python3 gate.py {subject} --snapshot")


def prepare(subject: str) -> int:
    """Queue one job per near-duplicate cluster — the only model spend this stage makes."""
    import agent_bridge as bridge
    store = _load(subject)
    order = _scaffold_order(subject)
    merged, _ = merge_exact(store, order, set(card_types(subject)))
    clusters = near_duplicate_clusters(merged, order)
    if not clusters:
        print("[consolidate] no near-duplicate clusters — nothing for the worker to decide")
        return 0
    (REPORTS / f"clusters-{subject}.json").write_text(json.dumps(clusters, indent=2))
    jobs = [{"custom_id": cl["cluster_id"], "prompt": build_prompt(subject, cl),
             "tool": EMIT_TOOL, "meta": {"cluster_id": cl["cluster_id"]}} for cl in clusters]
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[consolidate] {len(jobs)} near-duplicate cluster(s) queued for the worker")
    return len(jobs)


def collect(subject: str) -> None:
    """Apply the worker's decisions on top of the exact merge, then rewrite the store."""
    import agent_bridge as bridge
    store = _load(subject)
    order = _scaffold_order(subject)
    types = set(card_types(subject))
    merged, exact = merge_exact(store, order, types)

    cl_path = REPORTS / f"clusters-{subject}.json"
    clusters = json.loads(cl_path.read_text()) if cl_path.exists() else []
    decisions = {}
    for cid_key, content in bridge.outputs(_stage(subject)).items():
        for block in content:
            if getattr(block, "type", None) == "tool_use" and block.name == EMIT_TOOL["name"]:
                decisions[cid_key] = block.input
    final, applied = apply_decisions(merged, clusters, decisions, types)

    before = sum(len(v) for v in store.values())
    after = sum(len(v) for v in final.values())
    _save(subject, final, before)
    print(f"[consolidate] exact merges: {len(exact)} · model merges: {len(applied)} "
          f"· {before} -> {after} cards")


def report(subject: str) -> str:
    store = _load(subject)
    order = _scaffold_order(subject)
    merged, exact = merge_exact(store, order, set(card_types(subject)))
    clusters = near_duplicate_clusters(merged, order)
    before = sum(len(v) for v in store.values())
    after = sum(len(v) for v in merged.values())
    lines = [f"=== consolidate: {subject} ===",
             f"{before} cards -> {after} after exact merge ({before - after} removed)", ""]
    if exact:
        lines.append(f"exact duplicate terms ({len(exact)}):")
        lines += [f"  {m['term']} — kept in {m['home']}, dropped from "
                  f"{', '.join(m['dropped_from']) or '(same chapter)'}" for m in exact[:15]]
        if len(exact) > 15:
            lines.append(f"  … and {len(exact) - 15} more")
        lines.append("")
    if clusters:
        lines.append(f"near-duplicate clusters needing a decision ({len(clusters)}):")
        for cl in clusters[:10]:
            lines.append("  " + " | ".join(f"{m['term']} ({m['chapter']})" for m in cl["members"]))
        if len(clusters) > 10:
            lines.append(f"  … and {len(clusters) - 10} more")
        lines.append(f"\nrun `python3 consolidate.py {subject} --clusters` to queue these")
    else:
        lines.append("no near-duplicate clusters")
    return "\n".join(lines)


if __name__ == "__main__":
    args = sys.argv[1:]
    subj = next((a for a in args if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 consolidate.py <subject> "
                         "[--apply | --clusters | collect]")
    if "collect" in args:
        collect(subj)
    elif "--clusters" in args:
        n = prepare(subj)
        print("nothing to do" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
    elif "--apply" in args:
        s = _load(subj)
        before = sum(len(v) for v in s.values())
        m, ex = merge_exact(s, _scaffold_order(subj), set(card_types(subj)))
        _save(subj, m, before)
        print(f"applied {len(ex)} exact merge(s): "
              f"{before} -> {sum(len(v) for v in m.values())} cards")
    else:
        print(report(subj))
