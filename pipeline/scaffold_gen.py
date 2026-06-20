"""Auto-derive a topic scaffold (section + chapter list) when one doesn't exist yet.

`segment.py`/`flashcards.py` tag every question to a `sectionId`/`chapterId` from
`scaffold/<subject>.json`. That file used to be hand-written, so a brand-new subject couldn't
run end-to-end. This stage closes that gap: from a handful of recently-digested papers it asks
the model for the same shape `scaffold/history.json` already uses, and writes it.

It runs as ONE cheap model call and is idempotent — if the scaffold already exists it is reused
untouched (pass regen=True / `--regen-scaffold` to rebuild). The result is a starting point: it's
plain JSON you can hand-edit and then re-segment.

    export ANTHROPIC_API_KEY=sk-ant-...
    python3 scaffold_gen.py biology            # write scaffold/biology.json if missing
    python3 scaffold_gen.py biology --regen     # rebuild it from scratch
"""
from __future__ import annotations
import json
import os
import sys
from pathlib import Path

from segment import SCAFFOLD_DIR, MODEL, _retry, _digests, pages_text

MAX_SCAFFOLD_DIGESTS = 10          # how many recent papers to read when deriving topics from papers
MAX_POOL_CHARS = 80_000            # cap pooled paper text to keep the single call cheap
MAX_SPEC_CHARS = 120_000           # cap official-spec text (reform F)
MAX_TOKENS = 4_000                 # a section+chapter list is small

EMIT_TOOL = {
    "name": "emit_scaffold",
    "description": "Return the section + chapter topic list a tagger will assign exam questions to.",
    "input_schema": {
        "type": "object",
        "properties": {
            "subject": {"type": "string"},
            "field": {"type": "string", "description": "short description of the subject's scope"},
            "note": {"type": "string", "description": "one-line guidance for the tagger"},
            "sections": {
                "type": "array",
                "description": "the paper's top-level divisions (e.g. 'Section A — Plants')",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "kebab id, subject-prefixed, e.g. bio-section1"},
                        "title": {"type": "string"},
                    },
                    "required": ["id", "title"],
                },
            },
            "chapters": {
                "type": "array",
                "description": "the examinable topics, finer-grained than sections",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "kebab id, subject-prefixed, e.g. bio-cell"},
                        "title": {"type": "string"},
                    },
                    "required": ["id", "title"],
                },
            },
        },
        "required": ["subject", "sections", "chapters"],
    },
}


def _exists(subject: str) -> Path:
    return SCAFFOLD_DIR / f"{subject}.json"


def _spec_path(subject: str) -> Path:
    """Optional official syllabus/specification text. If present it is the AUTHORITATIVE source
    for the topic list (reform F) — drop the subject's spec here as plain text and re-run."""
    return SCAFFOLD_DIR / f"{subject}.spec.txt"


def build_prompt(subject: str, pooled: str, spec: str = "") -> str:
    if spec.strip():
        source = (f"Below is the OFFICIAL syllabus/specification for {subject}. Derive the topic "
                  f"list from it — it is authoritative and defines what is on the course. The exam "
                  f"papers that follow are only to help you name the paper's top-level sections.\n\n"
                  f"=== OFFICIAL SPECIFICATION ===\n{spec}\n\n"
                  f"=== RECENT EXAM PAPERS (for section names only) ===\n{pooled}")
    else:
        source = (f"No official specification was provided, so infer the syllabus structure from "
                  f"the exam papers below — cover the WHOLE course, not only what these papers "
                  f"happened to ask.\n\n=== RECENT EXAM PAPERS ===\n{pooled}")
    return f"""You are designing the topic scaffold for a Leaving Certificate {subject} study app.
A downstream tagger will assign every past-paper question to exactly one sectionId and one
chapterId from the lists you return, so the lists must COVER the whole course and be mutually
distinct.

- `sections`: the paper's top-level divisions (the way the exam itself is split into parts).
- `chapters`: the examinable topics — finer-grained than sections; aim for 8-20 that span the
  whole subject. When an official specification is given, mirror ITS topic structure.
- Give every entry a kebab-case `id` with a short subject prefix (e.g. "{subject[:3]}-section1",
  "{subject[:3]}-cell"). Titles should read like a syllabus topic, not a question.
- Also return a short `field` (the subject's scope) and a one-line `note` for the tagger.
- Return ONLY via the emit_scaffold tool.

{source}
"""


def _client():
    try:
        import anthropic
    except ImportError:
        raise SystemExit("pip install anthropic --break-system-packages")
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY in your environment first.")
    return anthropic.Anthropic(max_retries=6)


def _parse(content) -> dict | None:
    for block in content:
        if getattr(block, "type", None) == "tool_use" and block.name == "emit_scaffold":
            return block.input if isinstance(block.input, dict) else None
    return None


_STAGE = "scaffold"
_TASK = ("Design the topic scaffold (section + chapter list) for this subject from the pooled "
         "exam-paper text in `prompt`. Return the object exactly as `schema` describes.")


def _stage(subject: str) -> str:
    return f"scaffold-{subject}"


def prepare(subject: str, regen: bool = False) -> int:
    """Queue one job to derive the scaffold, unless one already exists. Returns 0 if nothing to do."""
    import agent_bridge as bridge
    if _exists(subject).exists() and not regen:
        return 0
    digests = _digests(subject, limit=MAX_SCAFFOLD_DIGESTS)
    pooled = "\n\n".join(pages_text(dg.get("paper")) for dg in digests)[:MAX_POOL_CHARS]
    if not pooled.strip():
        raise SystemExit(f"No usable paper text for {subject} — run `python3 run.py {subject}` first.")
    # Source priority for the topic list: resource bundle (authoritative) > spec.txt > papers.
    import resources
    spec = resources.corpus(subject)[:MAX_SPEC_CHARS]
    if spec.strip():
        print(f"[scaffold] deriving topics from the resource bundle ({len(spec)} chars)")
    else:
        sp = _spec_path(subject)
        spec = sp.read_text()[:MAX_SPEC_CHARS] if sp.exists() else ""
        print(f"[scaffold] using official spec {sp.name}" if spec
              else f"[scaffold] no resource bundle/spec — inferring topics from papers "
                   f"(drop course material in {resources.subject_dir(subject)} for accuracy)")
    job = {"custom_id": "scaffold", "prompt": build_prompt(subject, pooled, spec), "tool": EMIT_TOOL}
    bridge.prepare(_stage(subject), [job], task=_TASK)
    print(f"[scaffold] queued 1 job for the worker")
    return 1


def collect(subject: str) -> Path:
    """Read the worker's scaffold answer and write scaffold/<subject>.json."""
    import agent_bridge as bridge
    outs = bridge.outputs(_stage(subject))
    content = outs.get("scaffold")
    data = _parse(content) if content else None
    if not data or not data.get("sections") or not data.get("chapters"):
        raise SystemExit(f"Worker returned no usable scaffold for {subject}.")
    data.setdefault("subject", subject)
    data.setdefault("field", "")
    data.setdefault("note", "Auto-generated scaffold — review and hand-edit, then re-segment.")
    path = _exists(subject)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"[scaffold] wrote {path.name}: {len(data['sections'])} sections, "
          f"{len(data['chapters'])} chapters")
    return path


if __name__ == "__main__":
    args = sys.argv[1:]
    subj = next((a for a in args if not a.startswith("-")), None)
    if not subj:
        raise SystemExit("usage: python3 scaffold_gen.py <subject> prepare|collect [--regen]")
    if "collect" in args:
        print(collect(subj).read_text())
    else:
        n = prepare(subj, regen=("--regen" in args))
        print("scaffold already exists" if not n else "1 job ready — spawn the pipeline-worker")
