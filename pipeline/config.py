"""Pipeline configuration. Paths, subjects, syllabus cutoffs, and the 'relevant years' rule.

The SEC archive (examinations.ie) serves exam papers and marking schemes as free PDFs.
Form-discovery (acquire_form.py) needs no subject codes — it drives the archive's own
dropdowns by visible text. The only per-subject knowledge that matters for "which papers
are relevant" is the syllabus-change cutoff year (see SYLLABUS_CUTOFF below).
"""
import datetime
import json as _json
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent          # the bare bones repo root
DATA = ROOT / "pipeline" / "_data"
RAW = DATA / "raw"                                      # downloaded PDFs
EXTRACTED = DATA / "extracted"                          # stage 2 page text/images
DIGEST = DATA / "digest"                                # app-ready per-paper digests
CANONICAL = DATA / "canonical"                          # one <subject>.json per subject
REPORTS = DATA / "reports"                              # manifests + coverage
RESOURCES = ROOT / "pipeline" / "resources"            # validated per-subject resource contract
RESOURCE_CACHE = DATA / "resources"                    # extracted corpus + bundle-derived metadata
for _p in (RAW, EXTRACTED, DIGEST, CANONICAL, REPORTS, RESOURCE_CACHE):
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

# ── Validation gate (validate.py) ─────────────────────────────────────────────
# A part is structurally broken if its question text is missing or is only a label
# stub like "Part (a)" / "Q1" / "(b)" — the actual question wording was lost upstream.
MIN_QUESTION_CHARS = 12
STUB_QUESTION_RE = _re.compile(r"^(part\s*)?\(?[a-z0-9]{1,4}\)?[\s.:;,)\-]*$", _re.I)
# An answer should be within this band of its mark-derived target word count, else flag it.
LENGTH_MIN_RATIO = 0.35
LENGTH_MAX_RATIO = 2.5
SEGMENT_RETRY_ATTEMPTS = 2         # times to re-segment papers that produced broken parts

# ── Publish gate (auto-publish if clean, else stop for review) ─────────────────
# After validation, run.py merges automatically only when the run is this clean; otherwise it
# stops and asks for `--merge`. (Tune per how much you trust the gate.)
MAX_QUARANTINE_FRAC = 0.05        # >5% of questions dropped as stubs -> needs a human look
MAX_SOFT_WARN_FRAC = 0.15         # >15% soft warnings (no_marks/length) -> needs a human look
TAG_REVIEW_THRESHOLD = 5          # > this many low-confidence tags -> raise a review bucket

# ── Flashcard standards (gate.py) ─────────────────────────────────────────────
# Duplicates across chapters are now ELIMINATED by flashcards.consolidate() rather than
# merely counted, so any survivor is a bug in that pass — the gate blocks on the first one.
# Syllabus coverage is verified against the guide's own topic taxonomy (syllabus.py): a deck
# that skips course topics fails the "covers all examinable knowledge" standard.
SYLLABUS_COVERAGE_MIN = 0.80      # below this, the deck is missing too much of the course
SYLLABUS_COVERAGE_GOOD = 0.95     # below this, worth a human look but not a blocker

# ── Resource-bundle retrieval (retrieval.py) ──────────────────────────────────
# Each job gets the slice of the bundle that concerns ITS topic, not a head slice of the whole
# corpus. Context size is the main cost lever in the pipeline: the worker reads every char of
# every job file, and these budgets are what it reads. Raise them only if answers/flashcards
# are visibly starved of source material.
RETRIEVAL_CHUNK_CHARS = 900        # retrieval window; ~a paragraph or two of a course guide
RETRIEVAL_CHUNK_OVERLAP = 150      # so a definition straddling a boundary stays retrievable
RETRIEVAL_MIN_SCORE = 0.0          # drop chunks at or below this BM25 score (0 = keep any match)
FLASHCARD_CTX_CHARS = 10_000       # per-chapter material for flashcards (was a shared 80k slice)
ANSWER_CTX_CHARS = 3_000           # per-question material for answers (was a shared 15k slice)
# Marker resources.py writes between pooled files; retrieval splits on it to label excerpts.
RETRIEVAL_SECTION_RE = _re.compile(r"^=====\s*[A-Z-]+:\s*(.+?)\s*=====$", _re.M)

# ── Worker model tiers (reform B) ─────────────────────────────────────────────
# Quality-critical stages (extraction, answer authoring) get a strong model; cheap
# classification/vision stays on Haiku. run.py prints the tier so /run-pipeline spawns
# the pipeline-worker subagent with that `model`.
STAGE_MODEL = {
    "scaffold":      "haiku",
    "exam-info":     "sonnet", # one call per subject; writes the student-facing exam breakdown
    "segment":       "opus",   # paper extraction — the foundation; must be exact
    "images":        "haiku",
    "images-verify": "haiku",  # confirm each crop is a real figure
    "schemes":       "sonnet", # match official answers out of the marking scheme
    "answers":       "sonnet", # author H1 answers where no official one exists
    "flashcards":    "haiku",
}


def model_for_stage(name: str) -> str:
    """Worker model recommended for a stage ('segment', 'answers', …)."""
    return STAGE_MODEL.get(name, "haiku")


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

# ── Answer length model (scheme points, fallback words-per-mark) ───────────────
# An answer should develop as many distinct points as the marking scheme rewards. When the
# scheme's point count for a part is known (schemes.py returns it), target = points × words/point.
# Otherwise fall back to a per-subject words-per-mark rule. That figure says how much CONTENT
# full marks needs; WRITING_WPM below says how much a student can physically produce in the
# time allowed, and caps it — a model answer nobody could write in the time is not a model answer.
WORDS_PER_POINT = 35            # a fully-developed exam point is ~30-40 words
DEFAULT_WORDS_PER_MARK = 9      # fallback when the scheme's point count is unknown
WORDS_PER_MARK = {             # per-subject overrides for the fallback (tune as needed)
    # "history": 11,
}

# ── Writing-speed model (what a student can actually produce in the time given) ─
# Sustained handwriting speed under exam pressure. This is a CEILING on every length
# target, never a target in itself, and it is also what turns a part's marks into the
# "how long should this take" label the app shows.
WRITING_WPM = 35

# Cache for the per-subject exam structure produced by exam_info.py. Keyed by subject ->
# (mtime, data) so a stage that regenerates the file mid-run isn't served a stale copy.
_EXAM_INFO_CACHE: dict[str, tuple[float, dict]] = {}


def words_per_mark(subject: str) -> int:
    return WORDS_PER_MARK.get(subject, DEFAULT_WORDS_PER_MARK)


def exam_info(subject: str) -> dict:
    """The subject's exam structure — totalMarks, totalMinutes, sections[] — as derived from
    the syllabus/specification bundle by exam_info.py. Returns {} until that stage has run,
    and every caller must treat {} as "timing unknown" rather than substituting a guess."""
    path = CANONICAL / f"exam-info.{subject}.json"
    try:
        mtime = path.stat().st_mtime
    except OSError:
        _EXAM_INFO_CACHE.pop(subject, None)
        return {}
    hit = _EXAM_INFO_CACHE.get(subject)
    if hit and hit[0] == mtime:
        return hit[1]
    try:
        data = _json.loads(path.read_text())
    except Exception:
        return {}
    if not isinstance(data, dict):
        return {}
    _EXAM_INFO_CACHE[subject] = (mtime, data)
    return data


def recommended_minutes(subject: str, marks: int) -> int | None:
    """How long a part should take: its share of the paper's marks, scaled to the paper's
    duration. None when marks are unknown or exam_info hasn't run — the caller then omits
    the label rather than inventing one."""
    info = exam_info(subject)
    total_marks, total_minutes = info.get("totalMarks"), info.get("totalMinutes")
    if not (marks and marks > 0 and total_marks and total_minutes):
        return None
    return max(1, round(marks / total_marks * total_minutes))


def writable_words(minutes: int | float | None) -> int | None:
    """The most a student can write in `minutes` at WRITING_WPM."""
    if not minutes or minutes <= 0:
        return None
    return max(15, round(minutes * WRITING_WPM))


def recommended_words(subject: str, marks: int, points: int | None = None,
                      minutes: int | None = None) -> int | None:
    """Target answer length (words), capped at what is writable in the time allowed.

    Two independent numbers meet here. The scheme-derived figure (reward points, else
    words-per-mark) is how much content full marks demands. The time-derived figure
    (minutes × WRITING_WPM) is how much a student can physically write. An exemplar has to
    be creditable AND writable, so the target is the smaller of the two; when the answer is
    squeezed the author is told to prioritise the highest-credit points rather than pad.
    """
    if minutes is None:
        minutes = recommended_minutes(subject, marks)
    ceiling = writable_words(minutes)
    if points and points > 0:
        target = max(15, round(points * WORDS_PER_POINT / 10) * 10)
    elif marks and marks > 0:
        target = max(15, round(marks * words_per_mark(subject) / 10) * 10)
    else:
        return ceiling
    return max(15, min(target, ceiling)) if ceiling else target


def cutoff_for(subject: str) -> tuple[int, bool]:
    """Return (cutoff_year, is_verified). Prefer a cutoff read from the subject's resource bundle
    (resources.py caches it); else the SYLLABUS_CUTOFF table; else DEFAULT_CUTOFF (unverified)."""
    meta = RESOURCE_CACHE / f"{subject}.meta.json"
    if meta.exists():
        try:
            d = _json.loads(meta.read_text())
            if d.get("cutoff"):
                return int(d["cutoff"]), True        # bundle-derived = authoritative
        except Exception:
            pass
    if subject in SYLLABUS_CUTOFF:
        year, verified = SYLLABUS_CUTOFF[subject]
        return year, verified
    return DEFAULT_CUTOFF, False


def relevant_years(subject: str, include_reference: bool = False) -> list[dict]:
    """The years worth pulling for a subject, newest first. Each item: {year, status}.
    Design decision: CURRENT SYLLABUS ONLY — no reference year by default. Pass
    include_reference=True to also pull the single pre-change year."""
    cutoff, _ = cutoff_for(subject)
    years = [{"year": y, "status": "on-course"} for y in range(CURRENT_YEAR, cutoff - 1, -1)]
    if include_reference:
        years.append({"year": cutoff - 1, "status": "reference"})
    return years


# Be a good citizen to a government archive.
USER_AGENT = "barebones-study-tool/1.0 (educational; contact: you@example.com)"
REQUEST_DELAY_S = 1.5              # polite pause between downloads
