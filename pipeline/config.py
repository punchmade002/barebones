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
EXAM_DB_OUT  = ROOT / "exam-questions-db.js"   # .with_name() used to produce generated variant

# ── Diagram crops (Stage 7, images.py) ───────────────────────────────────────
import re as _re
IMAGE_DPI = 150                    # render DPI for page->PNG crops (enough for screen + zoom)
BBOX_PADDING = 0.03                # pad the vision-returned bbox by 3% of page on each side
# Only spend a vision call on a part whose text hints it leans on a figure. Cheap pre-filter;
# the crop itself is fully vision-guided. Widen this if a subject's figures are being missed.
FIGURE_CUE_RE = _re.compile(
    r"\b(diagram|figure|fig\.?|graph|table|map|photograph|photo|image|chart|sketch|"
    r"shown below|shown above|shown in the|illustrat|labelled|label the|the apparatus)\b", _re.I)

# ── Years ────────────────────────────────────────────────────────────────────
CURRENT_YEAR = datetime.date.today().year
DEFAULT_CUTOFF = CURRENT_YEAR - 20          # used when a subject's cutoff is unknown

# Year a subject's CURRENT syllabus was first examined. Papers from this year on are
# "on-course"; the single year before it is pulled as REFERENCE (often >50% topic
# overlap, useful for extra practice) and tagged so it can be flagged in the app.
# Value is (year, verified): verified=True means confirmed; False is a best estimate that
# the runner prints as UNVERIFIED so you know to check it on the SEC "Syllabus Changes"
# page. Anything not listed falls back to DEFAULT_CUTOFF (also flagged unverified).
SYLLABUS_CUTOFF = {
    "history":   (2006, True),    # confirmed: documents-based study first examined 2006
    "pe":        (2022, True),    # LCPE is a new exam subject, first examined 2022
    "maths":     (2012, True),    # Project Maths national rollout (phased 2012-2015)
    "geography": (2006, False),   # estimate — revised syllabus ~2006; verify
    "biology":   (2004, False),   # estimate — current syllabus ~2004; verify
    "chemistry": (2002, False),   # estimate; verify
    "business":  (1999, False),   # estimate; verify
    "english":   (2001, False),   # estimate; verify
    "home-economics": (2004, False),  # estimate — current S&S syllabus ~2004; verify
}

# subject_key must match bare bones `subject` ids. `code` is optional now (form-discovery
# doesn't need it); kept for the legacy direct-URL fallback in acquire.py.
# `label` MUST match the archive's Subject dropdown text exactly (form-discovery matches
# on it). `code` is the 3-digit SEC subject code — all read live from 2024 papers
# (e.g. "2024L004" -> History 004). Codes aren't needed for form-discovery; kept for
# the legacy direct-URL fallback and tidy filenames.
# `display` is what a STUDENT sees in a source line ("LC Home Economics Higher 2019 — Q1").
# It is deliberately separate from `label`: `label` is archive-dropdown text, so reusing it
# would publish "LC Home Economics S & S Higher". Defaults to `label` when they agree.
SUBJECTS = {
    "history":   {"code": "004", "label": "History"},
    "english":   {"code": "002", "label": "English"},
    "biology":   {"code": "025", "label": "Biology"},
    "business":  {"code": "033", "label": "Business"},
    "chemistry": {"code": "022", "label": "Chemistry"},
    "geography": {"code": "005", "label": "Geography"},
    "maths":     {"code": "003", "label": "Mathematics", "display": "Mathematics"},
    "pe":        {"code": "225", "label": "Physical Education"},
    "home-economics": {"code": "180", "label": "Home Economics S & S",  # exact SEC dropdown text
                       "display": "Home Economics"},
}


def display_name(subject: str) -> str:
    """The student-facing subject name for source lines and report headings.

    Never use `subject.capitalize()`: it renders every hyphenated subject wrong
    ("home-economics" -> "Home-economics") and silently lowercases the rest of the words.
    Unknown subjects fall back to a title-cased de-hyphenation rather than raising, so a
    subject not yet in SUBJECTS still publishes something sane.
    """
    entry = SUBJECTS.get(subject) or {}
    return entry.get("display") or entry.get("label") or subject.replace("-", " ").title()

LEVELS = ("AL", "GL")              # AL = Higher (Ardleibhéal), GL = Ordinary

# ── Answer length model ──────────────────────────────────────────────────────
# A model answer should be as long as a student could realistically WRITE in the time the
# marks buy them — not an unbounded essay. Time for a question = (its marks / paper marks)
# × exam minutes. A third of that is thinking, so writing time = 2/3. Length = writing time
# × handwriting speed.
WRITING_WPM = 22            # average sustained exam handwriting speed (words/minute)
THINKING_FRACTION = 1 / 3   # share of available time spent planning, not writing
# A model answer is an exemplar, so it's allowed to be fuller than a time-pressured student
# answer. This scale lifts the realistic-time length to the target exemplar length. At 1.45
# a 100-mark question lands at ~900 words.
MODEL_ANSWER_SCALE = 1.45

# Per subject: total written-paper marks a candidate answers, and the exam length (minutes).
# History: written paper = 400 marks in 2h50m (the 100-mark research report is separate).
EXAM_FORMAT = {
    "history":   {"marks": 400, "minutes": 170},
    "chemistry": {"marks": 400, "minutes": 180},   # answer 8 of 11 Qs × 50 marks, 3 hours
    "maths":     {"marks": 300, "minutes": 150},   # per paper: Section A+B, 2h30m each
    "home-economics": {"marks": 320, "minutes": 150},  # written paper 320 marks (A 60 / B 180 / C 80), 2h30m
}


def recommended_words(subject: str, marks: int) -> int | None:
    """Realistic answer length in words for a question worth `marks`. None if unknown subject."""
    fmt = EXAM_FORMAT.get(subject)
    if not fmt or not marks:
        return None
    available = (marks / fmt["marks"]) * fmt["minutes"]      # minutes for this question
    writing = available * (1 - THINKING_FRACTION)            # minus thinking time
    words = writing * WRITING_WPM * MODEL_ANSWER_SCALE       # exemplar length
    return max(15, round(words / 10) * 10)                   # rounded to nearest 10


def cutoff_for(subject: str) -> tuple[int, bool]:
    """Return (cutoff_year, is_verified). Unknown subjects use DEFAULT_CUTOFF (unverified)."""
    if subject in SYLLABUS_CUTOFF:
        year, verified = SYLLABUS_CUTOFF[subject]
        return year, verified
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
