"""One command: a subject -> playable in the app, with NO API key.

The model work (scaffold, segment, diagrams, model answers, flashcards) is done by a spawned
Haiku **subagent**, not the Anthropic API. This script is a re-invokable orchestrator: it runs
the plain-Python stages, and at each model stage it either COLLECTS the worker's answers or
PREPARES new jobs and stops, printing `WORKER NEEDED <dir>`. The driving agent then spawns the
`pipeline-worker` subagent on that directory and re-runs this command. Repeat until it prints
`PIPELINE COMPLETE`. (The `/run-pipeline` skill automates that loop.)

    python run.py biology                 # advance the pipeline one model stage, then stop/finish
    python run.py biology --no-acquire    # don't download; reuse PDFs already on disk
    python run.py biology --restart       # wipe queued/inflight worker jobs and start the model
                                          #   stages fresh (does not delete PDFs/digests/canonical)
    python run.py biology --merge         # after validation passes, publish into the app

After all model stages, run.py runs the validation gate (validate.py): it quarantines any
broken questions and writes a sample for review. If the run is clean (quarantine/soft-warning
fractions under threshold, no tag-review bucket, coverage not flagged low) it publishes
automatically; otherwise it STOPS and you re-run with `--merge` to publish anyway.

Modifiers: --no-acquire  --no-images  --no-merge  --merge  --regen-scaffold  --limit N
           --headful  --include-irish  --restart  --force-merge (alias for --merge)
"""
import sys

import acquire_form
import digest
import agent_bridge as bridge
from config import relevant_years, cutoff_for, SUBJECTS, model_for_stage


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


def _request_worker(stage: str, n: int, model: str) -> None:
    d = bridge.worker_dir(stage)
    print(f"\n>>> WORKER NEEDED: {n} job(s) for stage '{stage}'")
    print(f">>> dir: {d}")
    print(f">>> model: {model}")
    print(f">>> Spawn the `pipeline-worker` subagent (Agent tool, model={model}) on that dir")
    print(">>> (read in/*.json, write out/*.json), then re-run this exact command to collect.")


def main() -> None:
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), None)
    if not subject:
        raise SystemExit("usage: python run.py <subject> [--no-acquire] [--no-images] "
                         "[--no-merge] [--merge] [--regen-scaffold] [--limit N] [--restart] "
                         "[--headful] [--include-irish]")
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

    if "--restart" in args:
        for mod in (scaffold_gen, segment, images, images_verify, schemes, model_answers, flashcards):
            bridge.reset(mod._stage(subject))
        validate._reset_attempts(subject)
        print("restarted: cleared all queued worker jobs for this subject.\n")

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
        model = model_for_stage(name)
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
                _request_worker(stage, len(pend), model); return
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
                    _request_worker(stage, len(bridge.pending(stage)), model); return
            bridge.mark_collected(stage)
            continue
        n = prep()                                    # not prepared yet -> write jobs
        if n == 0:
            bridge.mark_collected(stage)              # nothing to do; treat as done
            continue
        _request_worker(stage, n, model); return      # stop so the agent can run the worker

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
    why = "clean — auto-published" if (gate["clean"] and not coverage_low) else "published (--merge override)"
    print(f"\nPIPELINE COMPLETE ({why}): {subject} is acquired, digested, scaffolded, segmented, "
          f"{'(images skipped) ' if '--no-images' in args else 'diagrammed, '}"
          f"scheme-matched, answered, flashcarded, validated, and merged into app.html.")


if __name__ == "__main__":
    main()
