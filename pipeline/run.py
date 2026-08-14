"""One command: a subject -> playable in the app, with NO API key.

The model work (scaffold, segment, diagrams, model answers, flashcards) is done by a file-backed
low-cost worker, not a built-in API. This script is a re-invokable orchestrator: it runs
the plain-Python stages, and at each model stage it either COLLECTS the worker's answers or
PREPARES new jobs and stops, printing `WORKER NEEDED <dir>`. The driving agent then spawns the
`pipeline-worker` subagent on that directory and re-runs this command. Repeat until it prints
`PIPELINE COMPLETE`. (The `/run-pipeline` skill automates that loop.)

    python run.py biology                 # advance the pipeline one model stage, then stop/finish
    python run.py biology --no-acquire    # don't download; reuse PDFs already on disk
    python run.py biology --restart       # start derived model stages fresh; retains acquired
                                          #   PDFs, digests, resources, and scaffold
    python run.py biology --merge         # after validation passes, publish into the app

After all model stages, run.py runs the validation gate (validate.py): it quarantines any
broken questions and writes a sample for review. If the run is clean (quarantine/soft-warning
fractions under threshold, no tag-review bucket, coverage not flagged low) it publishes
automatically; otherwise it STOPS and you re-run with `--merge` to publish anyway.

Modifiers: --no-acquire  --no-images  --no-merge  --merge  --regen-scaffold  --limit N
           --headful  --include-irish  --restart  --force-merge (alias for --merge)
           --estimate-cost  --approve-cost  --max-jobs N  --max-prompt-chars N  --max-images N
           --max-estimated-tokens N
"""
import shutil
import sys

import acquire_form
import digest
import agent_bridge as bridge
from config import (relevant_years, cutoff_for, SUBJECTS, model_for_stage, cost_tier_for_stage,
                    CANONICAL, REPORTS, EXAM_IMAGES)


def _restart_marker(subject: str):
    return REPORTS / f".restart-{subject}.active"


def _reset_subject_outputs(subject: str, modules: tuple) -> None:
    """Clear every derived model-stage output while preserving acquired PDFs, digests,
    resources, and the subject scaffold. This is what a user reasonably expects `--restart`
    to mean; retaining canonical rows made the segment stage silently skip every old paper.
    """
    cached = 0
    for mod in modules:
        cached += bridge.cache_valid_outputs(mod._stage(subject), getattr(mod, "validate_output", None))
        bridge.reset(mod._stage(subject))
    if cached:
        print(f"restart: preserved {cached} validated worker result(s) in the persistent cache")
    for path in (
        CANONICAL / f"{subject}.json",
        CANONICAL / f"{subject}.quarantine.json",
        CANONICAL / f"exam-questions-db.{subject}.generated.js",
        CANONICAL / f"flashcards.{subject}.json",
        CANONICAL / f"flashcards-{subject}.generated.js",
        REPORTS / f"segment-{subject}.json",
        REPORTS / f"figures-{subject}.json",
        REPORTS / f"answers-{subject}.json",
        REPORTS / f"validate-{subject}.json",
        REPORTS / f"sample-{subject}.md",
        REPORTS / f"tag-review-{subject}.json",
        REPORTS / f"gate-baseline-{subject}.json",
    ):
        path.unlink(missing_ok=True)
    image_dir = EXAM_IMAGES / subject
    if image_dir.exists():
        shutil.rmtree(image_dir)


def _arg(args, flag):
    return int(args[args.index(flag) + 1]) if flag in args else None


def _coverage_low(subject: str) -> bool:
    """True if segment.collect flagged this subject's coverage as low (few papers segmented, or a
    chapter with zero questions). Read from the report so the gate is independent of run order."""
    import json
    from config import REPORTS
    rep = REPORTS / f"segment-{subject}.json"
    if not rep.exists():
        return False
    try:
        return bool(json.loads(rep.read_text()).get("low_coverage"))
    except Exception:
        return False


def _request_worker(subject: str, stage_name: str, stage: str, pending: list[str], args: list[str]) -> bool:
    """Print a provider-neutral worker request after enforcing the hard cost preflight.

    Returns True when execution must stop (estimate, budget block, or worker needed).
    """
    import cost_control
    attempt = bridge.max_attempt(stage, pending)
    model = model_for_stage(stage_name, attempt)
    tier = cost_tier_for_stage(stage_name, attempt)
    stats = cost_control.stage_stats(stage, bridge.inputs(stage), pending)
    problems = cost_control.violations(
        stats, max_jobs=_arg(args, "--max-jobs"),
        max_chars=_arg(args, "--max-prompt-chars"), max_images=_arg(args, "--max-images"),
        max_tokens=_arg(args, "--max-estimated-tokens"))
    report = cost_control.write_report(subject, stats, model, tier, problems)
    print(f"\n>>> COST PREFLIGHT: {cost_control.format_stats(stats)}")
    print(f">>> tier: {tier}; model hint: {model}; report: {report}")
    if "--estimate-cost" in args:
        print(">>> ESTIMATE ONLY — no worker requested. Remove --estimate-cost to continue.")
        return True
    if problems and "--approve-cost" not in args:
        print(">>> COST BUDGET BLOCKED: " + "; ".join(problems))
        print(">>> Reduce the workload/limits, or explicitly pass --approve-cost after review.")
        return True
    d = bridge.worker_dir(stage)
    print(f"\n>>> WORKER NEEDED: {len(pending)} job(s) for stage '{stage}'")
    print(f">>> dir: {d}")
    print(f">>> cost tier: {tier} (provider hint: {model})")
    if attempt:
        print(f">>> escalation reason: {attempt} prior validator failure(s); retry ONLY pending jobs")
    print(">>> Run one `pipeline-worker` on that dir using the cheapest model in this tier.")
    print(">>> (read in/*.json, write out/*.json), then re-run this exact command to collect.")
    print(">>> Do not parallelise merely for speed: parallel agents consume the same total input again.")
    return True


def main() -> None:
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), None)
    if not subject:
        raise SystemExit("usage: python run.py <subject> [--no-acquire] [--no-images] "
                         "[--no-merge] [--merge] [--regen-scaffold] [--limit N] [--restart] "
                         "[--headful] [--include-irish] [--estimate-cost] [--approve-cost]")
    if subject not in SUBJECTS:
        print(f"note: '{subject}' isn't in config.SUBJECTS; using it as the archive subject label anyway.")

    limit = _arg(args, "--limit")

    # Stage 0: ingest the resource bundle FIRST — it is the source of truth for the scaffold,
    # flashcards, answer grounding, AND the syllabus cutoff that drives which years we pull.
    import resources
    resources.require_bundle(subject)
    rs = resources.ingest(subject)
    if rs["bundle"]:
        print(f"resources: {rs['files']} file(s) {rs['roles']}, {rs['chars']} chars, "
              f"cutoff {rs['cutoff'] or '(not stated — using estimate)'}")
    else:
        print(f"resources: NO bundle at {resources.subject_dir(subject)} — scaffold/flashcards/"
              f"answers will be weaker. Drop the course guide/summary there for best accuracy.")

    cutoff, verified = cutoff_for(subject)             # now bundle-aware
    yrs = relevant_years(subject)                      # current-syllabus only (no reference year)
    print(f"=== {subject} ===  cutoff {cutoff}{'' if verified else ' (UNVERIFIED)'} | "
          f"{len(yrs)} years ({yrs[-1]['year']} … {yrs[0]['year']})\n")

    # Stage 1-2: acquire + digest — plain Python, idempotent, zero model work.
    if "--no-acquire" not in args:
        acquire_form.run(subject, headful=("--headful" in args),
                         include_irish=("--include-irish" in args))
    digest.run(subject)

    import scaffold_gen
    import segment
    import images
    import images_verify
    import schemes
    import model_answers
    import flashcards
    import validate
    import merge

    marker = _restart_marker(subject)
    if "--restart" in args:
        if marker.exists():
            print("restart already applied for this run; continuing queued stages.\n")
        else:
            _reset_subject_outputs(
                subject, (scaffold_gen, segment, images, images_verify, schemes,
                          model_answers, flashcards))
            validate._reset_attempts(subject)
            marker.write_text("active\n")
            print("restarted: cleared derived model outputs for this subject; retained PDFs, "
                  "digests, resources, and scaffold.\n")
    else:
        # A later explicit restart should be possible after the caller has left restart mode.
        marker.unlink(missing_ok=True)

    # Ordered model stages. Each must be fully collected before the next starts. Order matters:
    # segment (paper only) -> images -> schemes (official answers from the scheme) -> answers
    # (H1 fill for the rest) -> flashcards. prepare() returns 0 when there's nothing to do.
    stages = [
        ("scaffold",   scaffold_gen, lambda: scaffold_gen.prepare(subject, regen=("--regen-scaffold" in args))),
        ("segment",    segment,      lambda: segment.prepare(subject, limit=limit)),
    ]
    if "--no-images" not in args:
        stages.append(("images", images, lambda: images.prepare(subject, limit=limit)))
        stages.append(("images-verify", images_verify, lambda: images_verify.prepare(subject)))
    stages += [
        ("schemes",    schemes,       lambda: schemes.prepare(subject)),
        ("answers",    model_answers, lambda: model_answers.prepare(subject, limit=limit)),
        ("flashcards", flashcards,    lambda: flashcards.prepare(subject)),
    ]

    for name, mod, prep in stages:
        stage = mod._stage(subject)
        if bridge.is_collected(stage):
            continue                                  # finished in an earlier invocation
        if bridge.has_jobs(stage):                    # prepared already — worker may have run
            # A stage may expose validate_output(answer)->bool; pending() then re-queues outputs
            # that exist but fail it, so a bad answer is re-requested instead of accepted silently.
            # NB: not named `validate` — that would shadow the validate *module* imported above,
            # and the post-segment gate below calls validate.post_segment().
            check = getattr(mod, "validate_output", None)
            pend = bridge.pending(stage, validate=check)
            if pend:
                _request_worker(subject, name, stage, pend, args); return
            stuck = bridge.needs_human(stage)
            if stuck:
                shown = ", ".join(stuck[:5]) + (" …" if len(stuck) > 5 else "")
                print(f"\n>>> NEEDS HUMAN: {len(stuck)} job(s) in '{stage}' failed validation "
                      f"repeatedly and were given up on: {shown}")
                print(">>> their last (rejected) output is kept; collect() salvages what it can.")
            mod.collect(subject)                      # all answers present -> finalize
            # Validation gate after segment: re-segment broken papers, else quarantine stubs.
            if name == "segment":
                outcome = validate.post_segment(subject, limit=limit)
                if outcome == "retry":                # offending papers re-queued -> run worker
                    pend = bridge.pending(stage)
                    _request_worker(subject, name, stage, pend, args); return
            bridge.mark_collected(stage)
            continue
        n = prep()                                    # not prepared yet -> write jobs
        if n == 0:
            bridge.mark_collected(stage)              # nothing to do; treat as done
            continue
        check = getattr(mod, "validate_output", None)
        pend = bridge.pending(stage, validate=check)
        if not pend:                                  # every prepared job was restored from cache
            print(f"[cache] restored all {n} job(s) for '{stage}' — collecting without a worker")
            mod.collect(subject)
            if name == "segment":
                outcome = validate.post_segment(subject, limit=limit)
                if outcome == "retry":
                    pend = bridge.pending(stage)
                    _request_worker(subject, name, stage, pend, args); return
            bridge.mark_collected(stage)
            continue
        _request_worker(subject, name, stage, pend, args); return

    # All model stages done — VALIDATION GATE before anything reaches the app (reform C/G).
    gate = validate.enforce(subject)
    print(f"\n=== VALIDATION GATE ===")
    print(f"quarantined {gate['dropped_parts']} stub part(s) / {gate['dropped_questions']} question(s) "
          f"({gate['quarantine_frac']:.0%}); dropped {gate['dup_dropped']} curated-duplicate question(s); "
          f"{gate['kept_questions']} clean questions kept; "
          f"{gate['remaining_soft']} soft warning(s) ({gate['soft_frac']:.0%}); "
          f"{gate['low_confidence']} low-confidence tag(s).")
    if gate.get("quarantine"):
        print(f"quarantine: {gate['quarantine']}")
    if gate.get("tag_review"):
        print(f"TAG REVIEW ({gate['low_confidence']} low-confidence questions): {gate['tag_review']}")
    print(f"report:  {gate['report']}")
    print(f"SAMPLE FOR REVIEW:  {gate['sample']}")

    if "--no-merge" in args:
        print("\nVALIDATED (not merged: --no-merge).")
        return

    # Low coverage is a separate signal from the gate's defect fractions: the questions we DID
    # extract can be flawless while whole papers or chapters are missing. Both must be clean
    # for an unattended publish.
    coverage_low = _coverage_low(subject)
    if coverage_low:
        print(f"\n>>> ⚠ COVERAGE LOW — few papers segmented, or a chapter has zero questions. "
              f"Review reports/segment-{subject}.json.")

    override = "--merge" in args or "--force-merge" in args
    if (not gate["clean"] or coverage_low) and not override:
        why = []
        if not gate["clean"]:
            why.append("validation exceeded the clean thresholds (or raised a tag-review bucket)")
        if coverage_low:
            why.append("coverage is low")
        print(f"\nNEEDS REVIEW — {' and '.join(why)}. Check the sample above, then re-run with "
              f"--merge to publish anyway.")
        return
    # merge.run applies gate.py's blockers on top of the validation gate and returns False if it
    # refused to publish. Printing PIPELINE COMPLETE regardless would tell the /run-pipeline loop
    # the subject shipped when nothing was written.
    if not merge.run(subject, force=override):
        print("\nNOT PUBLISHED — the merge gate blocked it (see the failures above). "
              f"Fix them, or re-run: python3 run.py {subject} --merge")
        return
    marker.unlink(missing_ok=True)
    why = "clean — auto-published" if (gate["clean"] and not coverage_low) else "published (--merge override)"
    print(f"\nPIPELINE COMPLETE ({why}): {subject} is acquired, digested, scaffolded, segmented, "
          f"{'(images skipped) ' if '--no-images' in args else 'diagrammed, '}"
          f"scheme-matched, answered, flashcarded, validated, and merged into app.html.")


if __name__ == "__main__":
    main()
