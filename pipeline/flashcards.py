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

from config import CANONICAL, FLASHCARD_CTX_CHARS
from segment import _retry, MODEL, MAX_TOKENS, load_scaffold   # reuse the hardened helpers

MAX_CHAPTER_CHARS = 80_000          # cap for the no-bundle fallback (pooled past-paper text)

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
                        "term": {"type": "string", "description": "the concept/term itself (a noun phrase) — NEVER a question or instruction"},
                        "question": {
                            "type": "string",
                            "description": (
                                "the question a student is asked, which this card's definition "
                                "answers. A natural, specific question ending in '?' — e.g. "
                                "'What was Catholic Emancipation?', 'What is mitosis?', "
                                "'Who was Rosa Parks?'"
                            ),
                        },
                        "definition": {"type": "string", "description": "concise, exam-relevant explanation of the term — must answer the question"},
                        "type": {
                            "type": "string",
                            "description": (
                                "a short, subject-appropriate category — e.g. concept, term, "
                                "process, person, example, definition. Default 'concept'."
                            ),
                        },
                    },
                    "required": ["term", "question", "definition", "type"],
                },
            }
        },
        "required": ["cards"],
    },
}


def pool_by_chapter(canonical: list[dict]) -> dict[str, str]:
    """FALLBACK only (no resource bundle): pool question text + scheme answers per chapter. This
    is the old, weaker source — terms drift toward question fragments, so the prompt forbids that."""
    buckets: dict[str, list[str]] = defaultdict(list)
    for q in canonical:
        cid = q.get("chapterId") or "untagged"
        for p in q.get("parts", []):
            if p.get("question"):
                buckets[cid].append(p["question"])
            if p.get("model"):
                buckets[cid].append(p["model"])
    return {cid: "\n".join(parts)[:MAX_CHAPTER_CHARS] for cid, parts in buckets.items()}


def build_prompt(subject: str, chapter_title: str, material: str, from_guide: bool,
                 topics: list[str] | None = None) -> str:
    src = ("the COURSE MATERIAL (guide / summary / spec) below" if from_guide
           else "the pooled past-paper text below (no course guide was supplied)")
    # The syllabus topics belonging to this chapter are named explicitly so the deck aims at
    # full course coverage instead of at whatever the retrieved excerpt happened to emphasise.
    # gate.py then verifies the result against this same taxonomy.
    checklist = ""
    if topics:
        listed = "\n".join(f"  - {t}" for t in topics)
        checklist = (f"\nSYLLABUS TOPICS THIS CHAPTER MUST COVER — produce at least one card for "
                     f"each of these that the material supports:\n{listed}\n")
    return f"""You are building a clean set of study flashcards for ONE topic of Leaving
Certificate {subject}, from {src}.

TOPIC: {chapter_title}
{checklist}
Produce the atomic concepts a student MUST know for this topic. Each card is a question, the
concept it is about, and the answer — exactly the shape the app already uses for other subjects.

Rules:
- `term` is the CONCEPT ITSELF — a noun phrase (e.g. "Recommended Daily Allowance", "Pasteurisation",
  "High biological value protein"). It is NEVER a question or an instruction. Do NOT produce terms
  like "Define the following", "Using the table, comment on…", or anything ending in "?".
- `question` is what the student is actually asked, and MUST end in "?". Write the question a
  teacher would ask to elicit this card's definition, phrased naturally for what the term IS:
    * a concept or process -> "What is mitosis?", "What happens during pasteurisation?"
    * a person             -> "Who was Rosa Parks?"
    * an event or policy   -> "What was Catholic Emancipation?"
    * a cause/effect point -> "Why did the Dublin Lockout of 1913 begin?"
  Make it specific enough that the definition is the obvious answer — never a generic stem like
  "What is this?" and never just the term with a question mark bolted on.
- `definition` answers that question concisely and accurately, grounded in the material.
- `type`: a short subject-appropriate category (concept, term, process, person, example…); default "concept".
- One card per concept — no duplicates; merge variants of the same concept.
- Cover the topic's key examinable concepts; skip trivia, exam rubric, and page chrome.
- Stay strictly on the Leaving Certificate {subject} course. Do not invent facts.
- Return ONLY via the emit_flashcards tool.

=== {'COURSE MATERIAL' if from_guide else 'POOLED PAST-PAPER TEXT'} ===
{material}
"""


def parse_result(content) -> list[dict]:
    for block in content:
        if getattr(block, "type", None) == "tool_use" and block.name == "emit_flashcards":
            return block.input.get("cards", [])
    return []


import re as _re
# Reject "terms" that are really question stems / instructions (the old bug).
_QUESTION_TERM_RE = _re.compile(
    r"^\s*(define|describe|explain|outline|list|name|state|give|comment|using|discuss|"
    r"identify|evaluate|account for|distinguish|what|why|how|when|where|who)\b", _re.I)


def is_question_like(term: str) -> bool:
    t = (term or "").strip()
    return t.endswith("?") or bool(_QUESTION_TERM_RE.match(t)) or len(t.split()) > 9


def is_usable_question(question: str, term: str = "") -> bool:
    """A card's question must actually prompt the answer. Rejects the two ways this degrades:
    no question at all, and the term with a "?" stapled on ("Mitosis?"), which is what the app
    used to render and what the requirement exists to stop."""
    q = (question or "").strip()
    if not q.endswith("?") or len(q.split()) < 3:
        return False
    bare = q.rstrip("?").strip().lower()
    return bare != (term or "").strip().lower()


def dedup(cards: list[dict]) -> list[dict]:
    """Final safety net within one chapter: drop question-stem 'terms' and cards with no usable
    question, then collapse case/whitespace-identical terms (keeping the longest definition)."""
    best: dict[str, dict] = {}
    dropped = no_question = 0
    for c in cards:
        term = (c.get("term") or "").strip()
        if not term or is_question_like(term):          # not a concept — discard
            dropped += 1 if term else 0
            continue
        if not is_usable_question(c.get("question", ""), term):
            no_question += 1
            continue
        key = term.lower()
        if key not in best or len(c.get("definition", "")) > len(best[key].get("definition", "")):
            best[key] = {
                "term": term,
                "question": (c.get("question") or "").strip(),
                "definition": (c.get("definition") or "").strip(),
                "type": c.get("type") or "concept",
            }
    if dropped:
        print(f"    dropped {dropped} question-like 'term(s)'")
    if no_question:
        print(f"    dropped {no_question} card(s) with no usable question")
    return list(best.values())


def consolidate(by_chapter: dict[str, list]) -> tuple[dict[str, list], int]:
    """Eliminate duplicate cards ACROSS chapters — the requirement is zero, not few.

    `dedup` only ever sees one chapter, so a concept the course touches in three places came back
    three times. Each duplicated term is kept exactly once, in the chapter whose card carries the
    fullest definition (ties broken by chapter order, so the outcome is deterministic and a re-run
    doesn't move cards around). Returns the pruned decks and how many cards were removed.
    """
    winner: dict[str, tuple[str, int]] = {}            # term -> (chapterId, definition length)
    for cid, deck in by_chapter.items():
        for card in deck:
            key = _re.sub(r"\s+", " ", (card.get("term") or "").strip().lower())
            if not key:
                continue
            length = len(card.get("definition") or "")
            held = winner.get(key)
            if held is None or length > held[1]:
                winner[key] = (cid, length)
    out: dict[str, list] = {}
    removed = 0
    for cid, deck in by_chapter.items():
        kept = []
        for card in deck:
            key = _re.sub(r"\s+", " ", (card.get("term") or "").strip().lower())
            if key and winner.get(key, (cid, 0))[0] != cid:
                removed += 1
                continue
            kept.append(card)
        out[cid] = kept
    if removed:
        print(f"[flashcards] removed {removed} cross-chapter duplicate card(s)")
    return out, removed


def validate_output(answer) -> bool:
    """Re-queue a worker answer whose cards are missing usable questions.

    Requirement: every generated flashcard comes with a question. Silently dropping the offenders
    in `dedup` would shrink the deck instead of fixing it, so a job that mostly failed is sent
    back to the worker (agent_bridge caps the retries, then reports it for a human)."""
    cards = parse_result(answer)
    if not cards:
        return False
    ok = sum(1 for c in cards if is_usable_question(c.get("question", ""), c.get("term", "")))
    return ok >= max(1, int(len(cards) * 0.9))


def _chapters(subject: str, only: str | None):
    """Return [(chapterId, title, material, from_guide, topics)] — one deck source per chapter.

    PRIMARY source is the resource bundle (course guide/summary/spec): concepts come from what the
    course says must be learned, NOT from past-paper question text. Each chapter sees the corpus
    (capped) and is told to pull just its topic's concepts. Only if there's no bundle do we fall
    back to pooling past-paper text per chapter.

    `topics` is the chapter's slice of the guide's own syllabus taxonomy, passed to the prompt so
    coverage is aimed at the course rather than at whatever the retrieved excerpt emphasised."""
    import resources
    import retrieval
    import syllabus
    chapters = load_scaffold(subject)["chapters"]
    corpus = resources.corpus(subject)
    if corpus.strip():
        # Each chapter retrieves ITS OWN passages. Handing every chapter the same corpus[:80k]
        # meant chapters whose material sat past that point never saw their source text at all.
        print(f"[flashcards] sourcing concepts from the resource bundle ({len(corpus)} chars, "
              f"retrieving up to {FLASHCARD_CTX_CHARS} chars per chapter)")
        taxonomy = syllabus.topics(subject)
        if taxonomy:
            print(f"[flashcards] steering coverage with {len(taxonomy)} syllabus topic(s) "
                  f"from the guide")
        items = []
        for c in chapters:
            material = retrieval.excerpt(subject, c["title"], FLASHCARD_CTX_CHARS,
                                         what=f"chapter '{c['title']}'")
            if material.strip():
                items.append((c["id"], c["title"], material, True,
                              syllabus.topics_for(subject, c["title"])))
        if not items:
            print("[flashcards] bundle matched no chapter — check it covers this subject")
    else:
        print(f"[flashcards] no resource bundle — falling back to past-paper text "
              f"(weaker; drop course material in {resources.subject_dir(subject)})")
        canonical = json.loads((CANONICAL / f"{subject}.json").read_text())
        pooled = pool_by_chapter(canonical)
        titles = {c["id"]: c["title"] for c in chapters}
        skipped = [cid for cid in pooled if cid not in titles]
        if skipped:
            print(f"skipping {len(skipped)} off-scaffold tag bucket(s): {', '.join(skipped)}")
        items = [(cid, titles[cid], txt, False, []) for cid, txt in pooled.items()
                 if cid in titles and txt.strip()]
    if only:
        items = [it for it in items if it[0] == only]
    if not items:
        raise SystemExit(f"Nothing to do for {subject} — add a resource bundle at "
                         f"pipeline/resources/{subject}/ or populate canonical first.")
    return items


def _stage(subject: str) -> str:
    return f"flashcards-{subject}"


_TASK = ("Build a clean set of study flashcards for each topic. Each job's `prompt` gives one "
         "topic and the course material to draw from; return atomic cards as `schema` describes. "
         "EVERY card needs all four fields: `term` (the concept itself — never a question), "
         "`question` (what the student is asked, ending in '?', e.g. 'What is mitosis?'), "
         "`definition` (the answer to that question), and `type`. A card without a real question "
         "is rejected and re-queued. No duplicates.")


def render_js(subject: str, by_chapter: dict[str, list]) -> Path:
    # shape matches the app's keyTerm: {term, question, definition, section, type}
    db = {cid: [{"term": c["term"], "question": c.get("question", ""),
                 "definition": c["definition"], "section": cid,
                 "type": c.get("type", "concept")} for c in cards]
          for cid, cards in by_chapter.items()}
    out = CANONICAL / f"flashcards-{subject}.generated.js"
    out.write_text("window.FLASHCARDS_DB = Object.assign(window.FLASHCARDS_DB || {},\n"
                   + json.dumps(db, indent=2, ensure_ascii=False) + "\n);\n")
    return out


def prepare(subject: str, only: str | None = None) -> int:
    """One job per topic (chapter). chapterIds may contain stray chars, so jobs use index ids
    c0,c1,… and carry the real chapterId in `meta`. Returns the job count (0 = nothing to do)."""
    import agent_bridge as bridge
    items = _chapters(subject, only)
    jobs = [{
        "custom_id": f"c{i}",
        "prompt": build_prompt(subject, title, material, from_guide, topics),
        "tool": EMIT_TOOL,
        "meta": {"chapterId": cid},
    } for i, (cid, title, material, from_guide, topics) in enumerate(items)]
    bridge.prepare(_stage(subject), jobs, task=_TASK)
    print(f"[flashcards] {len(jobs)} topic(s) queued for the worker")
    return len(jobs)


def collect(subject: str) -> None:
    """Read the worker's per-topic cards, dedup within and across chapters, verify the deck
    against the syllabus taxonomy, then write the flashcards store + app JS."""
    import agent_bridge as bridge
    import syllabus
    stage = _stage(subject)
    ins, outs = bridge.inputs(stage), bridge.outputs(stage)
    by_chapter: dict[str, list] = {}
    for cid_key, content in outs.items():
        chapter = ins.get(cid_key, {}).get("meta", {}).get("chapterId", cid_key)
        cards = dedup(parse_result(content))
        print(f"[fc] {chapter}: {len(cards)} cards")
        by_chapter[chapter] = cards
    by_chapter, _removed = consolidate(by_chapter)
    (CANONICAL / f"flashcards.{subject}.json").write_text(
        json.dumps(by_chapter, ensure_ascii=False, indent=2))
    js = render_js(subject, by_chapter)
    total = sum(len(v) for v in by_chapter.values())
    print(f"\n{total} unique flashcards across {len(by_chapter)} chapters -> {js.name}")
    # Verify coverage here as well as at the gate: the run log is where you find out WHICH
    # topics were missed while the material is still in front of you.
    cov = syllabus.coverage(subject, by_chapter)
    if not cov["verifiable"]:
        print("[flashcards] no guide taxonomy — coverage could not be verified")
        return
    print(f"[flashcards] syllabus coverage {cov['covered']}/{cov['total']} topics "
          f"({cov['rate']:.0%})")
    if cov["missing"]:
        shown = "; ".join(cov["missing"][:8]) + (" …" if len(cov["missing"]) > 8 else "")
        print(f"[flashcards] {len(cov['missing'])} topic(s) with no card: {shown}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    only = args[args.index("--chapter") + 1] if "--chapter" in args else None
    if "collect" in args:
        collect(subject)
    else:
        n = prepare(subject, only=only)
        print("nothing to do" if not n else f"{n} job(s) ready — spawn the pipeline-worker")
