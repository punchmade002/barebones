"""Per-question timing labels — "how long should this take".

Requirement: every exam question carries year, marks, TIME, level, chapter. Year/marks/level/
chapter come out of segmentation; time is derived here, from two facts the pipeline already has:

  * the part's marks (segment.py, mandatory and non-zero), and
  * the paper's total marks and duration (exam_info.py, read from the specification).

A part's time is its share of the paper's marks scaled to the paper's duration — the same rule a
teacher gives ("a mark a minute"), generalised to whatever the real ratio is. The value is STORED
on the record rather than computed in the browser, so that a question exported, reviewed or
served anywhere carries its own timing, and so the answer author and the validator are working to
exactly the number the student is shown.

Stamping is idempotent and safe to re-run: it recomputes from marks every time, so fixing a
part's marks or regenerating exam-info corrects the labels on the next pass.
"""
from __future__ import annotations

from config import recommended_minutes


def stamp(subject: str, rows: list[dict]) -> dict:
    """Write `time_minutes` onto every part, and the question's total onto the question.

    Returns a small report. Parts whose marks are unknown, or subjects with no exam-info store,
    get no label at all — an invented duration is worse than an absent one, and the gate reports
    the gap instead.
    """
    stamped = missing = 0
    for q in rows:
        total = 0
        for p in q.get("parts", []):
            mins = recommended_minutes(subject, p.get("marks", 0))
            if mins:
                p["time_minutes"] = mins
                total += mins
                stamped += 1
            else:
                p.pop("time_minutes", None)
                missing += 1
        if total:
            q["time_minutes"] = total
        else:
            q.pop("time_minutes", None)
    return {"stamped": stamped, "missing": missing,
            "questions": sum(1 for q in rows if q.get("time_minutes"))}
