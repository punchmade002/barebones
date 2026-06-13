"""Pipeline configuration. Paths, subjects, syllabus cutoffs, and the 'relevant years' rule.

The SEC archive (examinations.ie) serves exam papers and marking schemes as free PDFs.
Form-discovery (acquire_form.py) needs no subject codes — it drives the archive's own
dropdowns by visible text. The only per-subject knowledge that matters for "which papers
are relevant" is the syllabus-change cutoff year (see SYLLABUS_CUTOFF below).
"""
import datetime
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent          # the bare bones repo root
DATA = ROOT / "pipeline" / "_data"
RAW = DATA / "raw"                                      # downloaded PDFs
EXTRACTED = DATA / "extracted"                          # stage 2 page text/images
DIGEST = DATA / "digest"                                # app-ready per-paper digests
CANONICAL = DATA / "canonical"                          # one <subject>.json per subject
REPORTS = DATA / "reports"                              # manifests + coverage
for _p in (RAW, EXTRACTED, DIGEST, CANONICAL, REPORTS):
    _p.mkdir(parents=True, exist_ok=True)

EXAM_IMAGES = ROOT / "exam-images"

# ── Years ────────────────────────────────────────────────────────────────────
CURRENT_YEAR = datetime.date.today().year
DEFAULT_CUTOFF = CURRENT_YEAR - 20          # used when a subject's cutoff is unknown

# Year a subject's CURRENT syllabus was first examined. Papers from this year on are
# "on-course"; the single year before it is pulled as REFERENCE (often >50% topic
# overlap, useful for extra practice) and tagged so it can be flagged in the app.
#   - Confirmed: History = 2006 (documents-based study + research report first examined).
#   - Add others as you verify them on the SEC "Syllabus Changes" page; unknown subjects
#     fall back to DEFAULT_CUTOFF and are flagged so you can refine later.
SYLLABUS_CUTOFF = {
    "history": 2006,
}

# subject_key must match bare bones `subject` ids. `code` is optional now (form-discovery
# doesn't need it); kept for the legacy direct-URL fallback in acquire.py.
SUBJECTS = {
    "history":   {"code": "004", "label": "History"},      # code confirmed live (2023L004…)
    "biology":   {"code": "002", "label": "Biology"},
    "business":  {"code": "??",  "label": "Business"},
    "chemistry": {"code": "??",  "label": "Chemistry"},
    "geography": {"code": "??",  "label": "Geography"},
    "maths":     {"code": "??",  "label": "Mathematics"},
    "pe":        {"code": "??",  "label": "Physical Education"},
}

LEVELS = ("AL", "GL")              # AL = Higher (Ardleibhéal), GL = Ordinary


def cutoff_for(subject: str) -> tuple[int, bool]:
    """Return (cutoff_year, is_verified). Unverified subjects use DEFAULT_CUTOFF."""
    if subject in SYLLABUS_CUTOFF:
        return SYLLABUS_CUTOFF[subject], True
    return DEFAULT_CUTOFF, False


def relevant_years(subject: str, include_reference: bool = True) -> list[dict]:
    """The years worth pulling for a subject, newest first.
    Each item: {year, status} where status is 'on-course' or 'reference'.
    'reference' = the single pre-change year (kept for overlapping content)."""
    cutoff, _ = cutoff_for(subject)
    years = [{"year": y, "status": "on-course"} for y in range(CURRENT_YEAR, cutoff - 1, -1)]
    if include_reference:
        years.append({"year": cutoff - 1, "status": "reference"})
    return years


# Be a good citizen to a government archive.
USER_AGENT = "barebones-study-tool/1.0 (educational; contact: you@example.com)"
REQUEST_DELAY_S = 1.5              # polite pause between downloads
