"""Per-chapter / per-question retrieval over a subject's resource bundle.

The bundle is pooled by resources.py into one corpus of up to MAX_CORPUS_CHARS (400k). Before
this module, both consumers took a HEAD SLICE of that corpus and shipped it to every job:

  flashcards.py    corpus[:80_000] -> the same opening 80k for all ~30 chapters
  model_answers.py corpus[:15_000] -> the same opening 15k copied into every question's job

That is wrong twice over. Chapters whose material sits past the slice never saw their own source
text, so the model fell back on general knowledge — the exact failure the resource bundle exists
to prevent. And because the keyless worker path flattens the prompt to a plain string on disk
(the `cache_control` prefix in model_answers is dead code — nothing caches), the same slice was
duplicated into every job file: ~12M chars of corpus for an 800-question subject.

This module replaces the head slice with a relevance query, so each job gets a SMALLER context
that actually concerns its topic. Retrieval is BM25 over character-windowed chunks: pure Python,
no dependencies, no model calls, index built once per subject per process.

    import retrieval
    retrieval.search("chemistry", "Stoichiometry", budget_chars=10_000)
"""
from __future__ import annotations
import math
import re
from functools import lru_cache

from config import (RETRIEVAL_CHUNK_CHARS, RETRIEVAL_CHUNK_OVERLAP,
                    RETRIEVAL_MIN_SCORE, RETRIEVAL_SECTION_RE)

# Deliberately small: exam material is dense with short content words we want to keep.
_STOP = frozenset("""
the and for are but not you all any can her was one our out has had his she him its who how why
that this with from they what which their there when been were where would could should into
than then them these those upon each other some such only very more most much many also about
""".split())

_K1 = 1.5                    # BM25 term-frequency saturation
_B = 0.75                    # BM25 length normalisation
_WORD_RE = re.compile(r"[a-z0-9]+")


def _tokens(s: str) -> list[str]:
    return [w for w in _WORD_RE.findall((s or "").lower())
            if len(w) >= 3 and w not in _STOP]


def _sections(corpus: str) -> list[tuple[str, str]]:
    """Split the pooled corpus back into (label, text) at the markers resources.py writes."""
    marks = list(RETRIEVAL_SECTION_RE.finditer(corpus))
    if not marks:
        return [("bundle", corpus)]
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(corpus)
        out.append((m.group(1).strip(), corpus[m.end():end]))
    return out


def _chunk(corpus: str) -> list[dict]:
    """Character windows with overlap, tagged with the source file they came from. Overlap keeps
    a definition that straddles a window boundary retrievable from at least one whole chunk."""
    step = max(1, RETRIEVAL_CHUNK_CHARS - RETRIEVAL_CHUNK_OVERLAP)
    chunks, order = [], 0
    for label, text in _sections(corpus):
        text = text.strip()
        if not text:
            continue
        for start in range(0, len(text), step):
            body = text[start:start + RETRIEVAL_CHUNK_CHARS]
            if len(body.strip()) < 40:               # skip scraps
                continue
            chunks.append({"label": label, "text": body, "order": order})
            order += 1
            if start + RETRIEVAL_CHUNK_CHARS >= len(text):
                break
    return chunks


@lru_cache(maxsize=8)
def _index(subject: str):
    """(chunks, term-frequency per chunk, document frequency, average length). Cached per subject
    for the life of the process — prepare() retrieves once per chapter/question in a single run."""
    import resources
    corpus = resources.corpus(subject)
    chunks = _chunk(corpus)
    tfs, df = [], {}
    for c in chunks:
        tf: dict[str, int] = {}
        for w in _tokens(c["text"]):
            tf[w] = tf.get(w, 0) + 1
        tfs.append(tf)
        for w in tf:
            df[w] = df.get(w, 0) + 1
    lens = [sum(tf.values()) for tf in tfs]
    avg = (sum(lens) / len(lens)) if lens else 0.0
    return chunks, tfs, df, lens, avg


def _score(query_terms: list[str], tf: dict[str, int], length: int,
           df: dict[str, int], n_docs: int, avg_len: float) -> float:
    if not length or not avg_len:
        return 0.0
    total = 0.0
    for t in query_terms:
        f = tf.get(t, 0)
        if not f:
            continue
        idf = math.log(1 + (n_docs - df.get(t, 0) + 0.5) / (df.get(t, 0) + 0.5))
        total += idf * (f * (_K1 + 1)) / (f + _K1 * (1 - _B + _B * length / avg_len))
    return total


def has_corpus(subject: str) -> bool:
    return bool(_index(subject)[0])


def search(subject: str, query: str, budget_chars: int, extra: str = "") -> tuple[str, float]:
    """Best-matching corpus passages for `query`, concatenated up to `budget_chars`.

    Returns (text, top_score). `extra` adds query terms without weighting them differently —
    model_answers passes the question text so an answer retrieves material about that question.
    Selected chunks are re-sorted into corpus order so the excerpt still reads top-to-bottom.
    A top_score of 0 means nothing matched: the caller should say so rather than pretend the
    excerpt is on-topic.
    """
    chunks, tfs, df, lens, avg = _index(subject)
    if not chunks:
        return "", 0.0
    terms = _tokens(query) + _tokens(extra)
    if not terms:
        return "", 0.0
    n = len(chunks)
    scored = [(_score(terms, tfs[i], lens[i], df, n, avg), i) for i in range(n)]
    scored.sort(key=lambda x: (-x[0], x[1]))
    top = scored[0][0] if scored else 0.0

    picked, used = [], 0
    for s, i in scored:
        if s <= RETRIEVAL_MIN_SCORE:
            break
        body = chunks[i]["text"]
        if used + len(body) > budget_chars:
            if used:                                  # budget spent — stop at a whole chunk
                break
            body = body[:budget_chars]                # first chunk alone exceeds it: truncate
        picked.append((chunks[i]["order"], chunks[i]["label"], body))
        used += len(body)
        if used >= budget_chars:
            break
    if not picked:
        return "", top

    picked.sort()
    out, last_label = [], None
    for _order, label, body in picked:
        if label != last_label:
            out.append(f"\n--- from {label} ---")
            last_label = label
        out.append(body)
    return "\n".join(out).strip(), top


def excerpt(subject: str, query: str, budget_chars: int, extra: str = "",
            what: str = "") -> str:
    """search() plus a one-line note when the bundle had nothing relevant, so a thin result is
    visible in the run log instead of silently degrading into the model's general knowledge."""
    text, top = search(subject, query, budget_chars, extra)
    if not text:
        print(f"[retrieval] no bundle material matched {what or query!r} — "
              f"that topic may be missing from {subject}'s resource bundle")
    elif top < 1.0:
        print(f"[retrieval] weak match for {what or query!r} (score {top:.2f}) — "
              f"check the bundle covers this topic")
    return text


def select_text_chunks(corpus: str, queries: list[str], budget_chars: int,
                       per_query: int = 2) -> str:
    """Retrieve small windows from an arbitrary text without a model call.

    Unlike ``search`` this serves many independent queries (e.g. every part in one exam paper):
    each query gets a chance to select its own best scheme window, then duplicate windows are
    removed and restored to source order. This avoids both head truncation and repeating a full
    100k-character marking scheme in every job.
    """
    chunks = _chunk(corpus)
    if not chunks or not queries or budget_chars <= 0:
        return ""
    tfs, df = [], {}
    for chunk in chunks:
        tf: dict[str, int] = {}
        for word in _tokens(chunk["text"]):
            tf[word] = tf.get(word, 0) + 1
        tfs.append(tf)
        for word in tf:
            df[word] = df.get(word, 0) + 1
    lens = [sum(tf.values()) for tf in tfs]
    avg = sum(lens) / len(lens) if lens else 0.0
    rankings, coverage_terms = [], {}
    for query in queries:
        terms = _tokens(query)
        ranked = sorted(((_score(terms, tfs[i], lens[i], df, len(chunks), avg), i)
                         for i in range(len(chunks))), key=lambda pair: (-pair[0], pair[1]))
        ranked = [(score, i) for score, i in ranked[:per_query]
                  if score > RETRIEVAL_MIN_SCORE]
        rankings.append(ranked)
        if ranked:
            coverage_terms.setdefault(ranked[0][1], []).extend(terms)

    # First reserve the best window for EVERY query. If those windows exceed the whole budget,
    # fairly focus each around its matching words instead of letting early scheme pages consume
    # the budget and silently cutting off Section C again.
    primary = set(coverage_terms)
    if not primary:
        return ""

    def focused(body: str, terms: list[str], limit: int) -> str:
        if len(body) <= limit:
            return body
        low = body.lower()
        positions = [low.find(term) for term in terms if low.find(term) >= 0]
        centre = min(positions) if positions else len(body) // 2
        start = max(0, min(len(body) - limit, centre - limit // 3))
        return body[start:start + limit]

    bodies: dict[int, str] = {}
    primary_chars = sum(len(chunks[i]["text"]) for i in primary)
    if primary_chars > budget_chars:
        share = max(80, budget_chars // len(primary))
        for i in primary:
            bodies[i] = focused(chunks[i]["text"], coverage_terms[i], share)
    else:
        bodies = {i: chunks[i]["text"] for i in primary}
        used = primary_chars
        # Spend remaining budget on second-choice neighbouring/relevant windows by rank, but only
        # after every question already has coverage.
        for rank in range(1, per_query):
            for ranked in rankings:
                if len(ranked) <= rank:
                    continue
                i = ranked[rank][1]
                if i in bodies:
                    continue
                body = chunks[i]["text"]
                if used + len(body) > budget_chars:
                    continue
                bodies[i] = body
                used += len(body)

    out, used, last_label = [], 0, None
    for i in sorted(bodies, key=lambda j: chunks[j]["order"]):
        body = bodies[i]
        if used + len(body) > budget_chars:
            remaining = budget_chars - used
            if remaining < 80:
                break
            body = body[:remaining]
        label = chunks[i]["label"]
        if label != last_label:
            out.append(f"\n--- from {label} ---")
            last_label = label
        out.append(body)
        used += len(body)
        if used >= budget_chars:
            break
    return "\n".join(out).strip()
