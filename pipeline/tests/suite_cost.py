"""Cost gates, cheap-first routing, and content-addressed worker result cache."""
import json
import tempfile
from pathlib import Path

import agent_bridge as bridge
import cost_control
from config import model_for_stage, cost_tier_for_stage


def test_cost_stats_count_only_pending_jobs_and_images():
    records = {
        "a": {"prompt": "x" * 40, "image": "a.png"},
        "b": {"prompt": "y" * 80},
    }
    stats = cost_control.stage_stats("stage", records, ["a"])
    assert stats["pending_jobs"] == 1 and stats["prompt_chars"] == 40
    assert stats["image_jobs"] == 1 and stats["estimated_input_tokens"] > 1200
    assert stats["estimated_total_tokens"] > stats["estimated_input_tokens"]


def test_cost_gate_blocks_over_limit():
    stats = {"pending_jobs": 11, "prompt_chars": 100, "image_jobs": 0,
             "estimated_total_tokens": 500}
    assert cost_control.violations(stats, max_jobs=10, max_chars=1000, max_images=5)
    assert not cost_control.violations(stats, max_jobs=11, max_chars=100, max_images=0)


def test_model_routing_is_cheap_first_and_selective():
    assert cost_tier_for_stage("segment", 0) == "economy"
    assert cost_tier_for_stage("segment", 1) == "standard"
    assert cost_tier_for_stage("segment", 2) == "premium"
    assert model_for_stage("answers", 0) == "haiku"
    assert model_for_stage("answers", 1) == "sonnet"


def test_valid_result_cache_survives_stage_reset():
    old_agent, old_cache = bridge.AGENT, bridge.AGENT_CACHE
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        bridge.AGENT, bridge.AGENT_CACHE = root / "agent", root / "cache"
        job = {"custom_id": "one", "prompt": "answer exactly", "tool": {
            "name": "emit", "input_schema": {"type": "object"}}}
        try:
            bridge.prepare("demo", [job], task="test")
            out = bridge.worker_dir("demo") / "out" / "one.json"
            out.write_text(json.dumps({"answer": "ok"}))
            assert bridge.pending("demo", validate=lambda obj: obj.get("answer") == "ok") == []
            bridge.reset("demo")
            bridge.prepare("demo", [job], task="test")
            assert (bridge.worker_dir("demo") / "out" / "one.json").exists()
            assert bridge.pending("demo", validate=lambda obj: obj.get("answer") == "ok") == []
            bridge.reset("demo")
            changed = {**job, "prompt": "a materially changed source prompt"}
            bridge.prepare("demo", [changed], task="test")
            assert not (bridge.worker_dir("demo") / "out" / "one.json").exists()
        finally:
            bridge.AGENT, bridge.AGENT_CACHE = old_agent, old_cache


TESTS = [(n[5:].replace("_", " "), f) for n, f in sorted(globals().items())
         if n.startswith("test_") and callable(f)]
