"""File-based bridge that lets a spawned Claude Code subagent stand in for the Anthropic API.

There is NO ANTHROPIC_API_KEY and no network call anywhere in the pipeline. Instead, each model
stage WRITES its work as plain files, a low-cost worker selected by the orchestrating agent READS
them and writes answers back as files, and the stage READS those answers. The answer JSON is
wrapped to look exactly like a tool_use response block, so every stage's existing
`parse_result(...)` / `to_canonical(...)` / crop code keeps working untouched.

Layout, per stage (e.g. stage="segment-chemistry"):
    _data/agent/<stage>/INSTRUCTIONS.md     what the worker must do (written by prepare)
    _data/agent/<stage>/in/<id>.json        one job: {custom_id, prompt, tool_name, schema, meta, image?}
    _data/agent/<stage>/in/<id>.png         optional image the worker should look at
    _data/agent/<stage>/out/<id>.json       the worker's answer: a JSON object matching `schema`
    _data/agent/<stage>/.collected          marker: this stage's answers were finalised

Protocol the worker follows: for each in/<id>.json with no out/<id>.json, read `prompt` (+ Read
the `image` PNG if present), produce a JSON object conforming to `schema`, write it to
out/<id>.json. That's it — no code, no keys.
"""
from __future__ import annotations
import json
import inspect
import hashlib
import shutil
from pathlib import Path
from types import SimpleNamespace

from config import DATA

AGENT = DATA / "agent"
AGENT_CACHE = DATA / "agent-cache-v1"

WORKER_PROTOCOL = """# Pipeline worker job

You are the low-cost worker for the bare-bones exam pipeline. Use the cheapest capable model
selected by the orchestrator. Do exactly this, then stop:

1. List every file in `in/` matching `*.json`.
2. For each one that does NOT already have a same-named file in `out/`:
   - Read it. It has: `prompt` (your task), `schema` (the JSON shape to return),
     `tool_name`, and sometimes `image` (a PNG filename in `in/`).
   - If `image` is set, Read that PNG (e.g. `in/<image>`) and look at it — your answer
     depends on what you see.
   - Think, then produce a single JSON object that conforms to `schema` and answers `prompt`.
   - Write that JSON object (and nothing else — no markdown fences, no commentary) to
     `out/<same-filename>.json`.
3. Skip any job whose `out/` file already exists (idempotent — never redo work).
4. When every job has an `out/` file, reply with one line: how many you wrote.

Rules: return ONLY the JSON the schema asks for. Be faithful to the source text. Do not invent
data. Keep going until all jobs are done.
"""


def _dirs(stage: str):
    base = AGENT / stage
    return base, base / "in", base / "out"


def reset(stage: str) -> None:
    base, _i, _o = _dirs(stage)
    if base.exists():
        shutil.rmtree(base)


def reset_all() -> None:
    if AGENT.exists():
        shutil.rmtree(AGENT)


def _cache_key(rec: dict, image_png: bytes | None = None) -> str:
    """Content address independent of stage/job ids and of the AI provider."""
    stable = {k: rec.get(k) for k in ("prompt", "tool_name", "schema", "meta")}
    h = hashlib.sha256(json.dumps(stable, ensure_ascii=False, sort_keys=True,
                                  separators=(",", ":")).encode())
    if image_png is not None:
        h.update(image_png)
    return h.hexdigest()


def _cache_path(key: str) -> Path:
    return AGENT_CACHE / key[:2] / f"{key}.json"


def _ensure_cache_key(input_path: Path) -> str:
    rec = json.loads(input_path.read_text())
    if rec.get("cache_key"):
        return rec["cache_key"]
    image = None
    if rec.get("image"):
        image_path = input_path.parent / rec["image"]
        image = image_path.read_bytes() if image_path.exists() else None
    rec["cache_key"] = _cache_key(rec, image)
    input_path.write_text(json.dumps(rec, ensure_ascii=False, indent=2))
    return rec["cache_key"]


def _promote_cache(input_path: Path, answer_path: Path) -> None:
    try:
        key = _ensure_cache_key(input_path)
        if not key or not answer_path.exists():
            return
        dest = _cache_path(key)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copy2(answer_path, dest)
    except Exception:
        pass


def cache_valid_outputs(stage: str, validate=None) -> int:
    """Seed the persistent cache from an old/collected queue before a restart deletes it."""
    _base, ind, outd = _dirs(stage)
    if not ind.exists():
        return 0
    count = 0
    for input_path in ind.glob("*.json"):
        answer_path = outd / input_path.name
        if not answer_path.exists():
            continue
        obj = _load_answer(answer_path)
        valid = obj is not None
        if valid and validate is not None:
            params = inspect.signature(validate).parameters
            job = json.loads(input_path.read_text())
            valid = validate(obj, job) if len(params) >= 2 else validate(obj)
        if valid:
            _promote_cache(input_path, answer_path)
            count += 1
    return count


def prepare(stage: str, jobs: list[dict], *, task: str) -> Path:
    """Write jobs to in/. Idempotent: if jobs already exist, leave them (don't clobber partial
    worker output). `task` is a one-paragraph description of this stage prepended to INSTRUCTIONS.
    Each job: {custom_id, prompt, tool, meta?, image_png? (bytes)}."""
    base, ind, outd = _dirs(stage)
    ind.mkdir(parents=True, exist_ok=True)
    outd.mkdir(parents=True, exist_ok=True)
    (base / "INSTRUCTIONS.md").write_text(f"## This stage: {stage}\n\n{task}\n\n{WORKER_PROTOCOL}")
    if any(ind.glob("*.json")):
        return base                                   # already prepared
    for j in jobs:
        cid = j["custom_id"]
        rec = {"custom_id": cid, "prompt": j["prompt"],
               "tool_name": j["tool"]["name"], "schema": j["tool"]["input_schema"]}
        if j.get("meta") is not None:
            rec["meta"] = j["meta"]
        image_png = j.get("image_png")
        rec["cache_key"] = _cache_key(rec, image_png)
        if image_png is not None:
            (ind / f"{cid}.png").write_bytes(image_png)
            rec["image"] = f"{cid}.png"
        (ind / f"{cid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2))
        cached = _cache_path(rec["cache_key"])
        if cached.exists():
            shutil.copy2(cached, outd / f"{cid}.json")
    return base


def has_jobs(stage: str) -> bool:
    _b, ind, _o = _dirs(stage)
    return ind.exists() and any(ind.glob("*.json"))


def inputs(stage: str) -> dict:
    """custom_id -> the full in/ record (incl. `meta`)."""
    _b, ind, _o = _dirs(stage)
    out = {}
    if ind.exists():
        for p in ind.glob("*.json"):
            out[p.stem] = json.loads(p.read_text())
    return out


def _attempts_path(stage: str) -> Path:
    return _dirs(stage)[0] / ".attempts.json"


def _load_attempts(stage: str) -> dict:
    p = _attempts_path(stage)
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            return {}
    return {}


def max_attempt(stage: str, stems: list[str] | None = None) -> int:
    """Highest validation-failure count among these jobs (used for selective escalation)."""
    attempts = _load_attempts(stage)
    wanted = set(stems or attempts)
    return max((int(n) for stem, n in attempts.items() if stem in wanted), default=0)


def _bump_attempt(stage: str, stem: str) -> int:
    a = _load_attempts(stage)
    a[stem] = a.get(stem, 0) + 1
    _attempts_path(stage).write_text(json.dumps(a, indent=2))
    return a[stem]


def needs_human(stage: str, max_attempts: int = 2) -> list[str]:
    """Jobs whose output kept failing validation past `max_attempts` retries. The orchestrator
    surfaces these instead of looping on them forever; their last bad output is quarantined."""
    return sorted(s for s, n in _load_attempts(stage).items() if n > max_attempts)


def pending(stage: str, validate=None, max_attempts: int = 2) -> list[str]:
    """custom_ids still needing a (re)run.

    A job is pending if it has no out/ file. With a `validate` callback, a job whose out/ file
    EXISTS but FAILS validation is also returned — so the orchestrator re-requests it — and the
    bad answer is renamed `<id>.rejected.<n>.json` (never silently overwritten, so you keep
    evidence). To avoid an infinite loop, a job that has already failed `max_attempts` times is
    NOT re-queued; it stays out of `pending` and is reported via `needs_human()` instead, leaving
    its (last) output in place for collect() to salvage what it can."""
    _b, ind, outd = _dirs(stage)
    if not ind.exists():
        return []
    out = []
    for p in sorted(ind.glob("*.json")):
        ans = outd / p.name
        if not ans.exists():
            try:
                cached = _cache_path(_ensure_cache_key(p))
                if cached.exists():
                    shutil.copy2(cached, ans)
            except Exception:
                pass
            if not ans.exists():
                out.append(p.stem)
                continue
        if validate is None:
            valid = True
        else:
            # Most stages only need the returned object.  Matching stages such as official
            # schemes also need the originating job so they can prove that every requested id
            # came back exactly once and in order.  Supporting both callback shapes keeps the
            # bridge generic while closing the gap where a plausible-looking partial response
            # could otherwise be collected silently.
            params = inspect.signature(validate).parameters
            valid = (validate(_load_answer(ans), json.loads(p.read_text()))
                     if len(params) >= 2 else validate(_load_answer(ans)))
        if valid:
            _promote_cache(p, ans)
            continue                                       # no validation, or it passed
        try:
            _cache_path(json.loads(p.read_text()).get("cache_key", "")).unlink(missing_ok=True)
        except Exception:
            pass
        n = _bump_attempt(stage, p.stem)
        if n > max_attempts:
            continue                                       # give up re-queueing; see needs_human()
        ans.rename(outd / f"{p.stem}.rejected.{n}.json")   # quarantine, then re-queue clean
        out.append(p.stem)
    return out


def _load_answer(path: Path):
    """Read a worker answer tolerantly: a bare JSON object, or wrapped in ```json fences, or
    {"result": {...}}. Returns the object, or None if unreadable."""
    txt = path.read_text().strip()
    if txt.startswith("```"):
        txt = txt.strip("`")
        txt = txt.split("\n", 1)[1] if "\n" in txt else txt
        txt = txt.rsplit("```", 1)[0] if "```" in txt else txt
    try:
        obj = json.loads(txt)
    except Exception:
        return None
    if isinstance(obj, dict) and set(obj.keys()) == {"result"}:
        return obj["result"]
    return obj


def as_content(tool_name: str, obj):
    """Wrap a worker answer object so existing parse_result(content) treats it as a tool_use."""
    return [SimpleNamespace(type="tool_use", name=tool_name, input=obj)]


def outputs(stage: str) -> dict:
    """custom_id -> content list (parse_result-ready) for every answered job."""
    _b, ind, outd = _dirs(stage)
    out = {}
    if not ind.exists():
        return out
    for p in ind.glob("*.json"):
        ans = outd / p.name
        if not ans.exists():
            continue
        rec = json.loads(p.read_text())
        obj = _load_answer(ans)
        out[p.stem] = as_content(rec.get("tool_name", ""), obj)
    return out


def is_collected(stage: str) -> bool:
    base, _i, _o = _dirs(stage)
    return (base / ".collected").exists()


def mark_collected(stage: str) -> None:
    base, _i, _o = _dirs(stage)
    base.mkdir(parents=True, exist_ok=True)
    (base / ".collected").write_text("done\n")


def worker_dir(stage: str) -> Path:
    return _dirs(stage)[0]
