"""Canonical question IDs — construction and safe indexing.

A question ID must be UNIQUE across a subject's whole canonical store, because three later
stages look questions up by it (model_answers.collect, images.collect, and the app's
EXAM_QUESTIONS_INDEX). The original scheme was `{subject}-pp-{year}-{LV}-{label}`, which is
not unique for any subject that reuses question labels — and every subject does:

  * History repeats "Q1" once per topic per section (12 rows shared one ID in 2022 HL alone),
  * Home Economics repeats "Q1" across Sections A, B and C.

The model-supplied `label` can't be trusted for uniqueness even *within* one chapter: the 2005
OL history paper has two different questions both labelled "D4". So uniqueness here is
guaranteed by construction (a deterministic `-2`, `-3`… suffix on any repeated base), never
assumed from the inputs.

`index_by_id` exists because a plain `{q["id"]: q for q in rows}` silently keeps only the last
row per ID — that is how misrouting stays invisible. It raises instead.
"""
from __future__ import annotations
import re
from collections import Counter, defaultdict

# Bumped whenever the ID scheme changes. Anything keyed by question ID (e.g. the images
# sidecar, reports/figures-<subject>.json) must be invalidated when this changes.
ID_SCHEME_VERSION = 2


def level_tag(level: str) -> str:
    """'higher' -> 'HI', 'ordinary' -> 'OR'. Matches the pre-existing scheme."""
    return (level or "")[:2].upper()


def _clean(s) -> str:
    """One ID component: no spaces or separators that would blur the component boundaries."""
    return re.sub(r"[^A-Za-z0-9]+", "", str(s or ""))


def _topic(section: str, chapter: str) -> list[str]:
    """The section+chapter discriminator, with a shared leading token folded away.

    Scaffold ids repeat the subject stem ('hist-section3' + 'hist-eur1'), which would make every
    ID carry it twice. Strip it only when BOTH ids share the same leading token, so the fold is
    deterministic and can't merge two distinct chapters that merely end alike.
    """
    sec, chap = (section or "").strip(), (chapter or "").strip()
    s_head, _, s_tail = sec.partition("-")
    c_head, _, c_tail = chap.partition("-")
    if s_tail and c_tail and s_head == c_head:
        sec, chap = s_tail, c_tail
    return [p for p in (_clean(sec), _clean(chap)) if p]


def question_base(subject: str, year, level: str, section: str, chapter: str, label: str) -> str:
    """The ID a question wants, before uniqueness is enforced. Not guaranteed unique on its own."""
    parts = [_clean(subject), "pp", _clean(year), level_tag(level)]
    parts += _topic(section, chapter)
    parts.append(_clean(label) or "q")
    return "-".join(parts)


def assign_unique_ids(rows: list[dict], taken: set[str] | None = None) -> list[dict]:
    """Set `id` on every row, guaranteeing uniqueness within `rows` (and against `taken`).

    Rows are processed in order, so IDs are stable across re-runs of the same input: the first
    row keeps the bare base, later collisions get '-2', '-3', … `taken` lets a caller reserve
    IDs already committed to the store by an earlier paper.
    """
    used = set(taken or ())
    for r in rows:
        base = question_base(r.get("subject", ""), r.get("year"), r.get("level", ""),
                             r.get("sectionId", ""), r.get("chapterId", ""), r.get("label", ""))
        rid, n = base, 2
        while rid in used:
            rid = f"{base}-{n}"
            n += 1
        used.add(rid)
        r["id"] = rid
    return rows


def duplicate_ids(rows: list[dict]) -> dict[str, int]:
    """{id: count} for every id appearing more than once. Empty == the store is sound."""
    c = Counter(r.get("id") for r in rows)
    return {k: v for k, v in c.items() if k and v > 1}


def index_by_id(rows: list[dict], where: str = "") -> dict[str, dict]:
    """{id: row}, refusing to build a lossy index.

    `{q["id"]: q for q in rows}` keeps only the LAST row per duplicate id, so every lookup for
    that id returns the wrong question and the other rows become unreachable — answers and
    diagram crops then attach to whichever row happened to be last. Fail loudly instead.
    """
    dups = duplicate_ids(rows)
    if dups:
        top = ", ".join(f"{k}×{v}" for k, v in list(dups.items())[:5])
        raise ValueError(
            f"{where or 'index_by_id'}: {len(dups)} duplicate question id(s) in a store of "
            f"{len(rows)} rows ({sum(dups.values())} rows affected): {top}"
            f"{' …' if len(dups) > 5 else ''}\n"
            f"Indexing would silently drop all but the last row per id and misroute answers/"
            f"diagrams. Run `python3 migrate_ids.py <subject>` to re-issue unique ids."
        )
    return {r["id"]: r for r in rows}


def group_by_id(rows: list[dict]) -> dict[str, list[dict]]:
    """Non-raising variant for read-only reporting over a store that may still be broken."""
    out: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        out[r.get("id")].append(r)
    return dict(out)
