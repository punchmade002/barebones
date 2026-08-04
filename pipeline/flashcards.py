"""Stage 6 — FLASHCARDS, deduplicated per topic, batched on Claude Haiku.

Runs AFTER segment.py. Reads the canonical store (questions + marking-scheme model answers,
already tagged to a chapter) and makes ONE model call PER CHAPTER — not per paper. Because
the model sees every year's content for a topic at once and is told to return a single
unique set, the same term can't be generated twenty times. A final normalise pass removes
any case/whitespace near-duplicates that slip through, and `collect` then runs the global
cross-chapter merge (consolidate.merge_exact), which is the only pass that can see a term
repeated in a DIFFERENT chapter.

A card is {term, prompt, answer, type}. `term` is an index label; `prompt` is the authored
question the student actually sees. Before `prompt` existed the app rendered the bare term as
the question — "Q1: Food Pyramid" — which is unanswerable as an exam prompt. The type
vocabulary is per subject (config.CARD_TYPES); it used to be History's for everyone.

    export ANTHROPIC_API_KEY=sk-ant-...
    python3 flashcards.py history            # batch (unattended)
    python3 flashcards.py history --sync      # immediate, concurrent
    python3 flashcards.py history --chapter hist-ire1   # one chapter only (test)

Output:
    _data/canonical/flashcards.<subject>.json          {chapterId: [{term,definition}]}
    _data/canonical/flashcards-<subject>.generated.js  window.FLASHCARDS_DB, mergeable into app
"""
from __future__ import annotations
import json
import os
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from config import CANONICAL, card_types, display_name
from segment import _retry, MODEL, MAX_TOKENS, load_scaffold   # reuse the hardened helpers

MAX_CHAPTER_CHARS = 80_000          # cap pooled text per chapter to keep cost predictable

def emit_tool(subject: str) -> dict:
    """The emit schema, built per subject.

    Two things used to be hard-coded here and both were wrong for every subject but History:
    the type enum (see config.CARD_TYPES), and the card shape — a card was {term, definition},
    and the app rendered the bare `term` as the question, so students were shown "Food Pyramid"
    and asked to answer it. A card now carries an authored `prompt`.
    """
    types = card_types(subject)
    return {
        "name": "emit_flashcards",
        "description": "Return a single deduplicated set of study flashcards for this topic.",
        "input_schema": {
            "type": "object",
            "properties": {
                "cards": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "term": {
                                "type": "string",
                                "description": "the concept being tested, 1-5 words — an index "
                                               "label, NOT the question",
                            },
                            "prompt": {
                                "type": "string",
                                "description": "the exam-style question a student is asked. Must "
                                               "be answerable on its own, with no reference to a "
                                               "paper, diagram or passage.",
                            },
                            "answer": {
                                "type": "string",
                                "description": "the full answer to `prompt` — exam-relevant, "
                                               "1-3 sentences",
                            },
                            "type": {
                                "type": "string",
                                "enum": sorted(types),
                                "description": "Classify the term: "
                                               + ", ".join(f"{k}={v}" for k, v in sorted(types.items())),
                            },
                        },
                        "required": ["term", "prompt", "answer", "type"],
                    },
                }
            },
            "required": ["cards"],
        },
    }


def pool_by_chapter(canonical: list[dict]) -> dict[str, str]:
    """Concatenate question text + marking-scheme model answers per chapterId, across years."""
    buckets: dict[str, list[str]] = defaultdict(list)
    for q in canonical:
        cid = q.get("chapterId") or "untagged"
        for p in q.get("parts", []):
            if p.get("question"):
                buckets[cid].append(p["question"])
            if p.get("model"):
                buckets[cid].append(p["model"])
    return {cid: "\n".join(parts)[:MAX_CHAPTER_CHARS] for cid, parts in buckets.items()}


def build_prompt(subject: str, chapter_title: str, pooled: str) -> str:
    types = card_types(subject)
    type_lines = "\n".join(f"  - {k}: {v}" for k, v in sorted(types.items()))
    return f"""You are building a DEDUPLICATED set of study flashcards for one topic of
Leaving Certificate {display_name(subject)}.

TOPIC: {chapter_title}

Below is the pooled content for this topic from ~20 years of exam questions and their
marking schemes. Produce ONE clean set of atomic flashcards covering the key examinable
concepts, people, events and terms.

Each card has FOUR fields, and the difference between `term` and `prompt` matters:
- `term` — a 1-5 word label for the concept. It is an index entry, never shown as a question.
- `prompt` — the actual question the student is asked. It must be a real question
  ("What is …?", "Why did …?") or an exam instruction ("Explain …", "Describe …").
  It must stand alone: never write "the diagram above", "the passage", or "in this question",
  because the student sees only this card.
- `answer` — the answer to `prompt`, 1-3 sentences, exam-relevant.
- `type` — one of:
{type_lines}

Rules:
- NEVER make the prompt a restatement of the term. "Food Pyramid" is not a question;
  "What does the food pyramid show about a balanced diet?" is.
- A student must be able to answer `prompt` from `answer` alone.
- No duplicates. If the same concept appears many times, make ONE card and merge the best
  detail. Treat variants of the same term as one card.
- Prefer concepts a student must know to answer this topic; skip trivia and exam chrome.
- Return ONLY via the emit_flashcards tool.

=== POOLED CONTENT ===
{pooled}
"""


def parse_result(content) -> list[dict]:
    for block in content:
        if getattr(block, "type", None) == "tool_use" and block.name == "emit_flashcards":
            return block.input.get("cards", [])
    return []


def normalise_card(c: dict, types: set | None = None) -> dict:
    """One card in canonical shape: {term, prompt, answer, type}.

    Accepts legacy `{term, definition}` cards so an old store can be read, re-merged and
    re-rendered without a migration step; `prompt` is simply absent on those, and both the
    gate and the app treat a missing prompt as "fall back to the term".
    """
    out = {
        "term": (c.get("term") or "").strip(),
        "prompt": (c.get("prompt") or "").strip(),
        "answer": (c.get("answer") or c.get("definition") or "").strip(),
        "type": (c.get("type") or "concept").strip() or "concept",
    }
    if types is not None and out["type"] not in types:
        out["type"] = "concept"
    if not out["prompt"]:
        del out["prompt"]
    return out


def dedup(cards: list[dict], types: set | None = None) -> list[dict]:
    """Per-chapter safety net: collapse case/whitespace-identical terms, keeping the best
    copy of each field. Cross-chapter duplicates are invisible here by construction — that is
    what consolidate.merge_exact is for."""
    best: dict[str, dict] = {}
    for c in cards:
        card = normalise_card(c, types)
        if not card["term"]:
            continue
        key = card["term"].lower()
        prev = best.get(key)
        if prev is None:
            best[key] = card
            continue
        if len(card["answer"]) > len(prev["answer"]):
            prev["answer"], prev["term"] = card["answer"], card["term"]
        if len(card.get("prompt", "")) > len(prev.get("prompt", "")):
            prev["prompt"] = card["prompt"]
        if prev["type"] == "concept" and card["type"] != "concept":
            prev["type"] = card["type"]
    return list(best.values())


def _chapters(subject: str, only: str | None):
    canonical = json.loads((CANONICAL / f"{subject}.json").read_text())
    pooled = pool_by_chapter(canonical)
    titles = {c["id"]: c["title"] for c in load_scaffold(subject)["chapters"]}
    # only build decks for real scaffold topics; off-scaffold tags (e.g. <UNKNOWN>) are
    # left for the segmentation review queue, not turned into a junk flashcard set.
    skipped = [cid for cid in pooled if cid not in titles]
    if skipped:
        print(f"skipping {len(skipped)} off-scaffold tag bucket(s): {', '.join(skipped)}")
    items = [(cid, titles[cid], txt) for cid, txt in pooled.items() if cid in titles and txt.strip()]
    if only:
        items = [it for it in items if it[0] == only]
    if not items:
        raise SystemExit(f"Nothing to do — is {CANONICAL / (subject + '.json')} populated? "
                         f"Run `python3 segment.py {subject}` first.")
    return items


def _stage(subject: str) -> str:
    return f"flashcards-{subject}"


_TASK = ("Build a deduplicated set of study flashcards for each topic. Each job's `prompt` "
         "pools ~20 years of exam content for one topic; return ONE clean set of atomic cards "
         "as `schema` describes (term, definition, type), no duplicates.")


def render_js(subject: str, by_chapter: dict[str, list]) -> Path:
    # The app's keyTerm shape is {term, definition, section, type}; `definition` stays the
    # answer field so every existing render path keeps working, and `prompt` is added on top.
    # The app shows `prompt || term`, so a legacy card without one degrades to the old
    # behaviour instead of rendering an empty question.
    db = {}
    for cid, cards in by_chapter.items():
        deck = []
        for c in cards:
            answer = (c.get("answer") or c.get("definition") or "").strip()
            item = {"term": c["term"], "definition": answer, "section": cid,
                    "type": c.get("type", "concept")}
            if (c.get("prompt") or "").strip():
                item["prompt"] = c["prompt"].strip()
            deck.append(item)
        db[cid] = deck
    out = CANONICAL / f"flashcards-{subject}.generated.js"
    out.write_text("window.FLASHCARDS_DB = Object.assign(window.FLASHCARDS_DB || {},\n"
                   + json.dumps(db, indent=2, ensure_ascii=False) + "\n);\n")
    return out


def prepare(subject: str, only: str | None = None) -> int:
    """One job per topic (chapter). chapterIds may contain stray chars, so jobs use index ids
    c0,c1,… and carry the real chapterId in `meta`. Returns the job count (0 = nothing to do)."""
    import agent_bridge as bridge
    items = _chapters(subject, only)
    tool = emit_tool(subject)
    jobs = [{
        "custom_id": f"c{i}",
        "prompt": build_prompt(subject, title, txt),
        "tool": tool,
        "meta": {"chapterId": cid},
    } for i, (cid, title, txt) in enumerate(items)]
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[flashcards] {len(jobs)} topic(s) queued for the worker")
    return len(jobs)


def collect(subject: str) -> None:
    """Read the worker's per-topic cards, dedup per chapter, merge globally, write the store.

    The global pass runs here rather than being left to a later stage because a per-chapter
    dedup structurally cannot see a term repeated in another chapter — that blind spot is how
    Chemistry published 34 duplicated terms with every per-chapter check passing.
    """
    import agent_bridge as bridge
    import consolidate
    stage = _stage(subject)
    types = set(card_types(subject))
    ins, outs = bridge.inputs(stage), bridge.outputs(stage)
    by_chapter: dict[str, list] = {}
    for cid_key, content in outs.items():
        chapter = ins.get(cid_key, {}).get("meta", {}).get("chapterId", cid_key)
        cards = dedup(parse_result(content), types)
        print(f"[fc] {chapter}: {len(cards)} cards")
        by_chapter[chapter] = cards

    per_chapter_total = sum(len(v) for v in by_chapter.values())
    order = [c["id"] for c in load_scaffold(subject).get("chapters", [])]
    by_chapter, merges = consolidate.merge_exact(by_chapter, order, types)
    total = sum(len(v) for v in by_chapter.values())
    if merges:
        print(f"[fc] global merge: {len(merges)} term(s) duplicated across chapters, "
              f"{per_chapter_total - total} card(s) removed")

    (CANONICAL / f"flashcards.{subject}.json").write_text(
        json.dumps(by_chapter, ensure_ascii=False, indent=2))
    js = render_js(subject, by_chapter)
    print(f"\n{total} unique flashcards across {len(by_chapter)} chapters -> {js.name}")
    clusters = consolidate.near_duplicate_clusters(by_chapter, order)
    if clusters:
        print(f"{len(clusters)} near-duplicate cluster(s) need a judgement call — "
              f"`python3 consolidate.py {subject} --clusters`")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    only = args[args.index("--chapter") + 1] if "--chapter" in args else None
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject, only=only)
        print("nothing to do" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
