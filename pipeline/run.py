"""One command: input a subject, output every relevant paper digested and app-ready.

    python run.py history                # acquire all relevant papers+schemes, then digest
    python run.py history --headful      # watch the browser drive the archive
    python run.py history --no-acquire   # re-digest already-downloaded PDFs only

"Relevant" = every year from the current syllabus cutoff to now (config.SYLLABUS_CUTOFF),
plus the single pre-change "reference" year. Output:
    _data/raw/<subject>/*.pdf            the PDFs (papers + marking schemes, HL+OL)
    _data/digest/<subject>/<year>-<level>.json   paired, page-text, ready for Stage 3+
    _data/reports/manifest-<subject>.csv
"""
import sys

import acquire_form
import digest
from config import relevant_years, cutoff_for, SUBJECTS


def main() -> None:
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), None)
    if not subject:
        raise SystemExit("usage: python run.py <subject> [--headful] [--no-acquire] [--include-irish]")
    if subject not in SUBJECTS:
        print(f"note: '{subject}' isn't in config.SUBJECTS; using it as the archive subject label anyway.")

    cutoff, verified = cutoff_for(subject)
    yrs = relevant_years(subject)
    print(f"=== {subject} ===  cutoff {cutoff}"
          f"{'' if verified else ' (UNVERIFIED)'} | {len(yrs)} years "
          f"({yrs[-1]['year']}=reference … {yrs[0]['year']})\n")

    if "--no-acquire" not in args:
        acquire_form.run(subject, headful=("--headful" in args),
                         include_irish=("--include-irish" in args))
    digest.run(subject)

    if "--segment" in args:                 # the model stages (Haiku)
        import segment
        segment.run(subject, sync=("--sync" in args), limit=None)
        if "--model-answers" in args:       # H1 samples for essays with no official answer
            import model_answers
            model_answers.run(subject, sync=("--sync" in args))
        if "--flashcards" in args:          # deduplicated, per-chapter, after segmentation
            import flashcards
            flashcards.run(subject, sync=("--sync" in args))
        extras = [n for n, f in (("H1 answers", "--model-answers"), ("deduped flashcards", "--flashcards")) if f in args]
        print("\nDone end-to-end: PDFs -> digests -> tagged questions"
              + (" + " + " + ".join(extras) if extras else "") + ".")
    else:
        print("\nDone (acquire + digest). Add --segment (and optionally --flashcards) to "
              "run the Haiku stages, or run `python3 segment.py {0}` / "
              "`python3 flashcards.py {0}` separately.".format(subject))


if __name__ == "__main__":
    main()
