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
# Padding is page-relative. Three percent pulled one or two neighbouring lines of exam prose
# into almost every otherwise-correct crop. 0.8% leaves a safe 10–14 px screen margin at 150dpi;
# the context-aware verifier below rejects any box that is incomplete or still too loose.
BBOX_PADDING = 0.008
# Correctness-first mode. The former regex-only cost gate missed stimulus wording such as
# "pictured above", food labels, advertisements, and unlabelled tables. Keep the cue regex for
# prioritisation and smoke tests, but inspect every part during a full run.
SCAN_ALL_PARTS_FOR_FIGURES = True
FIGURE_CUE_RE = _re.compile(
    r"\b(diagram|figure|fig\.?|graph|table|map|photograph|photo|image|chart|sketch|"
    r"shown below|shown above|shown in the|pictured|symbols? shown|food label|advertis|"
    r"infographic|data presented|illustrat|labelled|label the|the apparatus)\b", _re.I)
# Phrases that assert the paper supplied a visual stimulus. Unlike a bare word such as
# "diagram", these do not match instructions asking the student to draw their own.
SUPPLIED_FIGURE_RE = _re.compile(
    # Bare "shown on/in" is too broad: "shown on your sketch" and "charges shown on a bill"
    # describe student-created work or ordinary prose, not a supplied exam visual.
    r"\b(shown|pictured|illustrated|presented)\s+(above|below)\b|"
    r"\b(shown|pictured|illustrated|presented)\s+(in|on)\s+(the|this|following)\s+"
    r"(diagram|figure|graph|table|map|photograph|photo|image|chart|food label|advertisement|"
    r"infographic)\b|"
    r"\b(refer to|study|examine|using)\s+(the\s+)?(following\s+)?"
    r"(diagram|figure|graph|table|map|photograph|photo|image|chart|food label|advertisement|"
    r"infographic)|\b(the|following)\s+(diagram|figure|graph|table|map|photograph|photo|image|"
    r"chart|food label|advertisement|infographic)\s+(shows|illustrates|gives|presents)\b", _re.I)

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

# ── Resource-bundle retrieval (retrieval.py) ──────────────────────────────────
# Each job gets the slice of the bundle that concerns ITS topic, not a head slice of the whole
# corpus. Context size is the main cost lever in the pipeline: the worker reads every char of
# every job file, and these budgets are what it reads. Raise them only if answers/flashcards
# are visibly starved of source material.
RETRIEVAL_CHUNK_CHARS = 900        # retrieval window; ~a paragraph or two of a course guide
RETRIEVAL_CHUNK_OVERLAP = 150      # so a definition straddling a boundary stays retrievable
RETRIEVAL_MIN_SCORE = 0.0          # drop chunks at or below this BM25 score (0 = keep any match)
FLASHCARD_CTX_CHARS = 6_000        # retrieved per-chapter material; compact enough for cheap workers
ANSWER_CTX_CHARS = 3_000           # per-question material for answers (was a shared 15k slice)
SCHEME_MATCH_CTX_CHARS = 21_000    # fair per-part scheme windows, never a repeated full PDF
SCHEME_ANSWER_CTX_CHARS = 4_000    # scheme criteria retrieved for one authored answer
ANSWER_BATCH_SIZE = 3              # several short answers per worker invocation
# Marker resources.py writes between pooled files; retrieval splits on it to label excerpts.
RETRIEVAL_SECTION_RE = _re.compile(r"^=====\s*[A-Z-]+:\s*(.+?)\s*=====$", _re.M)

# ── Worker cost policy ────────────────────────────────────────────────────────
# All providers start on their cheapest capable model. A stronger model is requested ONLY for
# an individual job that failed the stage's structural validator. Provider-specific aliases are
# hints; the provider-neutral `cost_tier_for_stage` value printed by run.py is authoritative.
STAGE_MODEL = {name: "haiku" for name in
               ("scaffold", "segment", "images", "images-verify", "schemes", "answers", "flashcards")}
STAGE_ESCALATION_MODEL = {
    "segment": "sonnet", "schemes": "sonnet", "answers": "sonnet",
}
STAGE_FINAL_MODEL = {"segment": "opus"}

# A stage cannot ask an agent to spend beyond these defaults without the operator explicitly
# passing --approve-cost. They are estimates, not billing promises, and work with any provider.
COST_MAX_PENDING_JOBS = 200
COST_MAX_PROMPT_CHARS = 1_500_000
COST_MAX_IMAGE_JOBS = 160
COST_IMAGE_INPUT_TOKENS = 1_200   # deliberately conservative per attached page/composite
COST_MAX_ESTIMATED_TOKENS = 1_000_000
COST_OUTPUT_TOKENS_PER_JOB = {     # typical upper estimate, not the provider's hard max
    "scaffold": 3_000, "segment": 6_000, "images": 300, "images-verify": 400,
    "schemes": 4_000, "answers": 6_000, "flashcards": 2_500,
}


def model_for_stage(name: str, attempt: int = 0) -> str:
    """Provider alias for a stage. First pass is always economy; validation failures escalate."""
    if attempt >= 2:
        return STAGE_FINAL_MODEL.get(name, STAGE_ESCALATION_MODEL.get(name, "haiku"))
    if attempt >= 1:
        return STAGE_ESCALATION_MODEL.get(name, "haiku")
    return STAGE_MODEL.get(name, "haiku")


def cost_tier_for_stage(name: str, attempt: int = 0) -> str:
    """Provider-neutral routing understood by non-Anthropic/non-ChatGPT orchestrators."""
    if attempt >= 2 and name in STAGE_FINAL_MODEL:
        return "premium"
    if attempt >= 1 and name in STAGE_ESCALATION_MODEL:
        return "standard"
    return "economy"


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
# Otherwise fall back to a per-subject words-per-mark rule. The author is told to MEET OR EXCEED
# this — it's a floor for the exemplar, not a time-pressured student's realistic length.
WORDS_PER_POINT = 35            # a fully-developed exam point is ~30-40 words
DEFAULT_WORDS_PER_MARK = 9      # fallback when the scheme's point count is unknown
WORDS_PER_MARK = {             # per-subject overrides for the fallback (tune as needed)
    # "history": 11,
}


def words_per_mark(subject: str) -> int:
    return WORDS_PER_MARK.get(subject, DEFAULT_WORDS_PER_MARK)


def recommended_words(subject: str, marks: int, points: int | None = None) -> int | None:
    """Target answer length (words). Prefer the scheme's reward-point count; else words-per-mark.
    None when neither marks nor points are known."""
    if points and points > 0:
        return max(15, round(points * WORDS_PER_POINT / 10) * 10)
    if marks and marks > 0:
        return max(15, round(marks * words_per_mark(subject) / 10) * 10)
    return None


def cutoff_for(subject: str) -> tuple[int, bool]:
    """Return (cutoff_year, is_verified). Prefer a cutoff read from the subject's resource bundle
    (resources.py caches it); else the SYLLABUS_CUTOFF table; else DEFAULT_CUTOFF (unverified).

    A bundle cutoff in the FUTURE is ignored. Bundles increasingly describe a Senior Cycle
    Redevelopment spec that is published but not yet examined (geography's says
    firstExamYear 2028), and taking it literally makes relevant_years() empty — the run then
    downloads nothing and crashes. Papers only exist for the syllabus being examined today,
    so fall back to the table for those subjects.
    """
    meta = RESOURCE_CACHE / f"{subject}.meta.json"
    if meta.exists():
        try:
            d = _json.loads(meta.read_text())
            if d.get("cutoff") and int(d["cutoff"]) <= CURRENT_YEAR:
                return int(d["cutoff"]), True        # bundle-derived = authoritative
            if d.get("cutoff"):
                print(f"note: {subject} resource bundle states first exam year {d['cutoff']}, "
                      f"which has not happened yet — using the SYLLABUS_CUTOFF table instead.")
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
