"""Stage 6 — FLASHCARDS, deduplicated per topic, batched on Claude Haiku.

Runs AFTER segment.py. Reads the canonical store (questions + marking-scheme model answers,
already tagged to a chapter) and makes ONE model call PER CHAPTER — not per paper. Because
the model sees every year's content for a topic at once and is told to return a single
unique set, the same term can't be generated twenty times. A final normalise pass removes
any case/whitespace near-duplicates that slip through.

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

from config import CANONICAL
from segment import _retry, MODEL, MAX_TOKENS, load_scaffold   # reuse the hardened helpers

MAX_CHAPTER_CHARS = 80_000          # cap pooled text per chapter to keep cost predictable

EMIT_TOOL = {
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
                        "term": {"type": "string", "description": "a concept, person, event or term"},
                        "definition": {"type": "string", "description": "one-line, exam-relevant"},
                        "type": {
                            "type": "string",
                            "enum": ["person", "event", "movement", "policy", "law", "concept"],
                            "description": (
                                "Classify the term: "
                                "person=named individual, "
                                "event=dated/named occurrence (war, rising, crisis, famine), "
                                "movement=organised campaign or political/social movement, "
                                "policy=government strategy or doctrine (e.g. Containment, Appeasement), "
                                "law=legislation, act, treaty, or agreement, "
                                "concept=abstract idea, principle, or institution"
                            ),
                        },
                    },
                    "required": ["term", "definition", "type"],
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
    return f"""You are building a DEDUPLICATED set of study flashcards for one topic of
Leaving Certificate {subject}.

TOPIC: {chapter_title}

Below is the pooled content for this topic from ~20 years of exam questions and their
marking schemes. Produce ONE clean set of atomic flashcards covering the key examinable
concepts, people, events and terms.

Rules:
- No duplicates. If the same concept appears many times, make ONE card and merge the best
  detail. Treat variants of the same term as one card.
- Each card: a short `term`, a one-line exam-relevant `definition`, and a `type` classification.
- type values: person (named individual), event (war/rising/crisis/famine etc.), movement
  (organised campaign/party/association), policy (government strategy/doctrine), law
  (act/treaty/agreement/constitution), concept (abstract idea, institution, or anything else).
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


def dedup(cards: list[dict]) -> list[dict]:
    """Final safety net: drop case/whitespace-identical terms, keep the longest definition."""
    best: dict[str, dict] = {}
    for c in cards:
        term = (c.get("term") or "").strip()
        if not term:
            continue
        key = term.lower()
        if key not in best or len(c.get("definition", "")) > len(best[key].get("definition", "")):
            best[key] = {
                "term": term,
                "definition": (c.get("definition") or "").strip(),
                "type": c.get("type") or "concept",
            }
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


def run_sync(client, subject, items):
    out: dict[str, list] = {}
    def one(it):
        cid, title, txt = it
        msg = _retry(client.messages.create, model=MODEL, max_tokens=MAX_TOKENS, tools=[EMIT_TOOL],
                     tool_choice={"type": "tool", "name": "emit_flashcards"},
                     messages=[{"role": "user", "content": build_prompt(subject, title, txt)}])
        return cid, dedup(parse_result(msg.content))
    with ThreadPoolExecutor(max_workers=4) as ex:
        for cid, cards in ex.map(one, items):
            print(f"[fc] {cid}: {len(cards)} cards")
            out[cid] = cards
    return out


def run_batch(client, subject, items):
    # Batch custom_id must match ^[a-zA-Z0-9_-]{1,64}$, but chapterIds from tagging may
    # contain stray characters — use safe index ids and map back.
    id_for = {f"c{i}": cid for i, (cid, _t, _x) in enumerate(items)}
    reqs = [{
        "custom_id": f"c{i}",
        "params": {"model": MODEL, "max_tokens": MAX_TOKENS, "tools": [EMIT_TOOL],
                   "tool_choice": {"type": "tool", "name": "emit_flashcards"},
                   "messages": [{"role": "user", "content": build_prompt(subject, title, txt)}]},
    } for i, (cid, title, txt) in enumerate(items)]
    batch = _retry(client.messages.batches.create, requests=reqs)
    print(f"[batch] submitted {len(reqs)} chapters as {batch.id}; polling…")
    import time
    while True:
        b = _retry(client.messages.batches.retrieve, batch.id)
        if b.processing_status == "ended":
            break
        time.sleep(20)
    out: dict[str, list] = {}
    for r in client.messages.batches.results(batch.id):
        cid = id_for.get(r.custom_id, r.custom_id)
        if r.result.type == "succeeded":
            cards = dedup(parse_result(r.result.message.content))
            print(f"[fc] {cid}: {len(cards)} cards")
            out[cid] = cards
        else:
            print(f"[skip] {cid}: {getattr(r.result, 'type', '?')}")
    return out


def render_js(subject: str, by_chapter: dict[str, list]) -> Path:
    # shape matches the app's keyTerm: {term, definition, section, type}
    db = {cid: [{"term": c["term"], "definition": c["definition"], "section": cid,
                 "type": c.get("type", "concept")} for c in cards]
          for cid, cards in by_chapter.items()}
    out = CANONICAL / f"flashcards-{subject}.generated.js"
    out.write_text("window.FLASHCARDS_DB = Object.assign(window.FLASHCARDS_DB || {},\n"
                   + json.dumps(db, indent=2, ensure_ascii=False) + "\n);\n")
    return out


def run(subject: str, sync: bool, only: str | None = None) -> None:
    try:
        import anthropic
    except ImportError:
        raise SystemExit("pip install anthropic --break-system-packages")
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY in your environment first.")
    client = anthropic.Anthropic(max_retries=6)
    items = _chapters(subject, only)

    by_chapter = (run_sync if sync else run_batch)(client, subject, items)

    (CANONICAL / f"flashcards.{subject}.json").write_text(
        json.dumps(by_chapter, ensure_ascii=False, indent=2))
    js = render_js(subject, by_chapter)
    total = sum(len(v) for v in by_chapter.values())
    print(f"\n{total} unique flashcards across {len(by_chapter)} chapters")
    print(f"  -> {CANONICAL / ('flashcards.' + subject + '.json')}")
    print(f"  -> {js.name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    only = args[args.index("--chapter") + 1] if "--chapter" in args else None
    run(subject, sync=("--sync" in args), only=only)
