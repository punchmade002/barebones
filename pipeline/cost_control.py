"""Provider-neutral cost preflight for file-backed model stages.

The pipeline cannot know a provider's live price, so it gates stable workload units instead:
pending jobs, prompt characters, image inputs, and approximate input tokens. This makes the
safety limit apply whether the worker is ChatGPT, Claude, Gemini, a local model, or a human.
"""
from __future__ import annotations
import json
import math
from pathlib import Path

from config import (COST_MAX_PENDING_JOBS, COST_MAX_PROMPT_CHARS, COST_MAX_IMAGE_JOBS,
                    COST_IMAGE_INPUT_TOKENS, COST_MAX_ESTIMATED_TOKENS,
                    COST_OUTPUT_TOKENS_PER_JOB, REPORTS)


def stage_stats(stage: str, records: dict, pending_ids: list[str]) -> dict:
    pending = set(pending_ids)
    selected = [r for cid, r in records.items() if cid in pending]
    chars = sum(len(str(r.get("prompt", ""))) for r in selected)
    images = sum(bool(r.get("image")) for r in selected)
    input_tokens = math.ceil(chars / 4) + images * COST_IMAGE_INPUT_TOKENS
    kind = next((name for name in sorted(COST_OUTPUT_TOKENS_PER_JOB, key=len, reverse=True)
                 if stage == name or stage.startswith(name + "-")), "")
    output_tokens = len(selected) * COST_OUTPUT_TOKENS_PER_JOB.get(kind, 2_000)
    return {
        "stage": stage,
        "pending_jobs": len(selected),
        "prompt_chars": chars,
        "image_jobs": images,
        "estimated_input_tokens": input_tokens,
        "estimated_output_tokens": output_tokens,
        "estimated_total_tokens": input_tokens + output_tokens,
    }


def violations(stats: dict, *, max_jobs: int | None = None, max_chars: int | None = None,
               max_images: int | None = None, max_tokens: int | None = None) -> list[str]:
    limits = {
        "pending_jobs": max_jobs if max_jobs is not None else COST_MAX_PENDING_JOBS,
        "prompt_chars": max_chars if max_chars is not None else COST_MAX_PROMPT_CHARS,
        "image_jobs": max_images if max_images is not None else COST_MAX_IMAGE_JOBS,
        "estimated_total_tokens": (max_tokens if max_tokens is not None
                                   else COST_MAX_ESTIMATED_TOKENS),
    }
    return [f"{key}={stats[key]:,} exceeds {limit:,}" for key, limit in limits.items()
            if limit >= 0 and stats[key] > limit]


def write_report(subject: str, stats: dict, model: str, cost_tier: str,
                 problems: list[str]) -> Path:
    path = REPORTS / f"cost-{subject}.json"
    report = {}
    if path.exists():
        try:
            report = json.loads(path.read_text())
        except Exception:
            report = {}
    report[stats["stage"]] = {**stats, "model_hint": model, "cost_tier": cost_tier,
                               "budget_violations": problems}
    path.write_text(json.dumps(report, indent=2))
    return path


def format_stats(stats: dict) -> str:
    return (f"{stats['pending_jobs']} job(s), {stats['prompt_chars']:,} prompt chars, "
            f"{stats['image_jobs']} image job(s), ~{stats['estimated_input_tokens']:,} input + "
            f"~{stats['estimated_output_tokens']:,} output tokens")
