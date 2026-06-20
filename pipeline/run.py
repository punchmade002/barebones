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

Modifiers: --no-acquire  --no-images  --no-merge  --regen-scaffold  --limit N  --headful
           --include-irish  --restart  --force-merge (publish despite low coverage / gate)
"""
import sys

import acquire_form
import digest
import agent_bridge as bridge
from config import relevant_years, cutoff_for, SUBJECTS


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


def _request_worker(stage: str, n: int) -> None:
    d = bridge.worker_dir(stage)
    print(f"\n>>> WORKER NEEDED: {n} job(s) for stage '{stage}'")
    print(f">>> dir: {d}")
    print(">>> Spawn the `pipeline-worker` subagent on that dir (read in/*.json, write out/*.json),")
    print(">>> then re-run this exact command. It will collect the answers and continue.")


def main() -> None:
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), None)
    if not subject:
        raise SystemExit("usage: python run.py <subject> [--no-acquire] [--no-images] "
                         "[--no-merge] [--regen-scaffold] [--limit N] [--restart] [--headful] "
                         "[--include-irish]")
    if subject not in SUBJECTS:
        print(f"note: '{subject}' isn't in config.SUBJECTS; using it as the archive subject label anyway.")

    limit = _arg(args, "--limit")

    cutoff, verified = cutoff_for(subject)
    yrs = relevant_years(subject)
    print(f"=== {subject} ===  cutoff {cutoff}{'' if verified else ' (UNVERIFIED)'} | "
          f"{len(yrs)} years ({yrs[-1]['year']}=reference … {yrs[0]['year']})\n")

    # Stage 1-2: acquire + digest — plain Python, idempotent, zero model work.
    if "--no-acquire" not in args:
        acquire_form.run(subject, headful=("--headful" in args),
                         include_irish=("--include-irish" in args))
    digest.run(subject)

    import scaffold_gen
    import segment
    import images
    import model_answers
    import flashcards
    import merge

    if "--restart" in args:
        for mod in (scaffold_gen, segment, images, model_answers, flashcards):
            bridge.reset(mod._stage(subject))
        print("restarted: cleared all queued worker jobs for this subject.\n")

    # Ordered model stages. Each must be fully collected before the next starts (segment feeds
    # images/answers/flashcards). prepare() returns 0 when there's nothing to do.
    stages = [
        ("scaffold",   scaffold_gen, lambda: scaffold_gen.prepare(subject, regen=("--regen-scaffold" in args))),
        ("segment",    segment,      lambda: segment.prepare(subject, limit=limit)),
    ]
    if "--no-images" not in args:
        stages.append(("images", images, lambda: images.prepare(subject, limit=limit)))
    stages += [
        ("answers",    model_answers, lambda: model_answers.prepare(subject, limit=limit)),
        ("flashcards", flashcards,    lambda: flashcards.prepare(subject)),
    ]

    for _name, mod, prep in stages:
        stage = mod._stage(subject)
        if bridge.is_collected(stage):
            continue                                  # finished in an earlier invocation
        if bridge.has_jobs(stage):                    # prepared already — worker may have run
            # A stage may expose validate_output(answer)->bool; pending() then re-queues outputs
            # that exist but fail it, so a bad answer is re-requested instead of accepted silently.
            validate = getattr(mod, "validate_output", None)
            pend = bridge.pending(stage, validate=validate)
            if pend:
                _request_worker(stage, len(pend)); return
            stuck = bridge.needs_human(stage)
            if stuck:
                shown = ", ".join(stuck[:5]) + (" …" if len(stuck) > 5 else "")
                print(f"\n>>> NEEDS HUMAN: {len(stuck)} job(s) in '{stage}' failed validation "
                      f"repeatedly and were given up on: {shown}")
                print(">>> their last (rejected) output is kept; collect() salvages what it can.")
            mod.collect(subject)                      # all answers present -> finalize
            bridge.mark_collected(stage)
            continue
        n = prep()                                    # not prepared yet -> write jobs
        if n == 0:
            bridge.mark_collected(stage)              # nothing to do; treat as done
            continue
        _request_worker(stage, n); return             # stop so the agent can run the worker

    # All model stages done.
    merged = False
    if "--no-merge" not in args:
        force_merge = "--force-merge" in args
        if _coverage_low(subject) and not force_merge:
            print(f"\n>>> ⚠ COVERAGE LOW — not auto-merging. Review "
                  f"reports/segment-{subject}.json, then either:")
            print(f">>>   python3 merge.py {subject}            (merge by hand; the gate still applies)")
            print(f">>>   python3 run.py {subject} --force-merge  (skip this coverage stop)")
        else:
            merged = merge.run(subject, force=force_merge)
    tail = (", and merged into app.html" if merged
            else " (merge skipped)" if "--no-merge" in args
            else " (merge pending — see above)")
    print(f"\nPIPELINE COMPLETE: {subject} is acquired, digested, scaffolded, segmented, "
          f"{'(images skipped) ' if '--no-images' in args else 'diagrammed, '}"
          f"answered, flashcarded{tail}.")


if __name__ == "__main__":
    main()
