# bare bones — Exam Data Pipeline

How to extract the same dataset Examly has — every Leaving Cert question, sorted by
topic, with marking schemes and derived flashcards — and load it into bare bones, for
all subjects, mostly automatically.

---

## 0. The key insight

Examly is not built on secret data. Every question, marking scheme, and flashcard they
have comes from **one public source**: the State Examinations Commission archive at
[examinations.ie](https://www.examinations.ie/exammaterialarchive/). It hosts every LC
and Junior Cycle **exam paper** and **marking scheme** as free PDFs, by subject, year,
level and language.

Everything Examly sells on top of that is *derived processing* of those PDFs:

| Examly feature | What it really is |
|---|---|
| "Every question sorted by topic" | PDFs segmented into questions, each tagged to a syllabus topic |
| "50,000+ flashcards from state papers" | Marking-scheme points turned into term/definition cards |
| "Marking schemes beside every question" | The marking-scheme PDF paired to its paper, question-by-question |
| "H1 model answers / AI corrections" | An LLM prompted with question + marking scheme |

So the goal is not "find the data" — it's **a pipeline that turns the SEC PDFs into
bare bones' schema at scale**. The data is already free; the moat is the processing.

---

## 1. Target output (what the pipeline must produce)

bare bones already has a clean schema. The pipeline's job is to fill it, never to
invent a new one. The three outputs, all generated — never hand-edited:

**a) Chapter scaffold → `data.js`**
`COURSE_DATA.chapters[]` — `{ id, number, subject, title, strand, learningOutcomes[], examQuestions:[] }`.
Built once per subject from the official syllabus (Stage 0).

**b) Exam questions → `exam-questions-db.js`**
`window.EXAM_QUESTIONS_DB[]` entries, exactly the existing shape:
```js
{ id, subject, chapterId, sectionId, source, year,
  parts: [ { label, question, marks, model, diagram } ] }
```
`model` = the cleaned marking-scheme answer. `diagram` = a cropped page image.

**c) Flashcards → `<subject>-content.js`**
`keyTerms[]` injected onto each learning outcome: `{ term, definition, section }`.
Plus richer `notes[]` where the syllabus/marking scheme supports it.

**d) Diagrams → `exam-images/<subject>/<year>-<paper>-<q>.png`**
Cropped from the source PDF page for any question that references a figure.

Everything is generated from a **canonical intermediate store** (one JSON per subject).
The `.js` files the app loads are a pure render step (`build.py`). This means if the app
schema ever changes, you re-render — you never re-extract.

---

## 2. The pipeline — eight stages

```
   examinations.ie PDFs
           │
  [0] Syllabus scaffold ── curriculumonline.ie  ─────────►  data.js skeleton
           │
  [1] ACQUIRE      download every paper + scheme  ───────►  raw/<subject>/*.pdf  + manifest
           │
  [2] EXTRACT      pdf → page text + page images   ──────►  extracted/<doc>.json
           │
  [3] SEGMENT      pages → questions & sub-parts    ─────►  questions[] (label, text, marks)
           │
  [4] PAIR         match question ↔ marking scheme  ─────►  question.model (raw)
           │
  [5] TAG          assign each question to a topic  ─────►  question.chapterId / sectionId
           │
  [6] DERIVE       marking points → flashcards      ─────►  keyTerms[] + clean model answers
           │
  [7] LOAD         canonical JSON → bare bones files ────►  exam-questions-db.js, *-content.js, images
           │
  [8] QA           validate, dedupe, coverage report ───►  review queue + reports
```

Each stage reads the previous stage's output and is **cached and idempotent** — re-running
only does new work. The LLM is used *surgically* (segmentation edge cases, topic
decisions, cleaning marking-scheme shorthand), never for bulk OCR — that keeps cost low.

### Stage 0 — Syllabus scaffold (once per subject)
You can't sort questions "by topic" until you have the list of topics. For each subject
pull the official specification from **curriculumonline.ie (NCCA)**. Its strands /
learning outcomes become your `chapters[]` and `learningOutcomes[]` in `data.js`. This is
the schema every question gets tagged against, so do it first and get it right. (For the
subjects you already cover, this exists — reuse it.)

### Stage 1 — Acquire
The archive is a cascading form (verified live 2026-06-06): tick a terms box, then
*Type (Exam Papers / Marking Schemes) → Year → Examination (LC/JC/LCA) → Subject*, each
selection a POST reload that reveals the next dropdown. It then shows a results table —
Higher/Ordinary level × English/Irish version — where each "download" link is an
**encrypted per-file token** (`/exammaterialarchive/?fp=<~135 chars>`), *not* a guessable
static path. So you can't enumerate filenames; you drive the form and harvest the links.

- **Form-driven (the way):** drive the form with Playwright, read the `?fp=` links from
  the results table, download each through the same browser session (the token needs the
  session). This is implemented and verified in `pipeline/acquire_form.py`.
- **Direct static paths (fallback only):** a legacy pattern
  `/archive/exampapers/<year>/<code>.pdf` still resolves for some files, but it's not what
  the live form produces — treat it as a best-effort fallback, not the primary route.

Build a **manifest** row per `(subject, year, level, version, type)` → local path. Cache
aggressively (never re-download), rate-limit, and set a real User-Agent. Scale: ~20 years
× 2 levels × {paper, scheme} × 26 subjects ≈ a few thousand PDFs, a few GB. Tractable.

### Stage 2 — Extract
Per PDF: pull text + layout with **PyMuPDF / pdfplumber**, and render each page to PNG.
Modern papers are real text. Older papers and many practical-subject schemes are scans →
fall back to **OCR (Tesseract)** or a vision-LLM pass. Output one JSON per document:
pages, each with `text` and an image path.

### Stage 3 — Segment
Split continuous text into discrete questions and sub-parts. Papers are well-structured:
`Section A/B/C`, `Q1…Qn`, `(a)(b)(c)`, `(i)(ii)(iii)`, marks in `(… marks)`. Use regex for
the obvious markers, an **LLM pass for messy layouts** and to capture marks reliably. Crop
the page region for any question with a figure → `exam-images`. Maps straight onto your
`parts[]` (`label`, `question`, `marks`, `diagram`). Apply your existing text rules
(strip booklet/page chrome into `source`; one `\n` per sub-part; don't re-describe
diagrams).

### Stage 4 — Pair question ↔ marking scheme
Marking schemes mirror the paper's numbering, so align on
`(subject, year, level, paper, question, part)`. The scheme text becomes the raw `model`
answer and the source for flashcards. Alignment is mostly deterministic; the LLM only
resolves ambiguous numbering.

### Stage 5 — Topic-tag (the high-value step)
This is Examly's real moat — "by topic" is what makes 40,000 questions usable. For each
question: **embed it and every syllabus learning outcome, take the top-k LOs by cosine
similarity, then have an LLM pick the best `chapterId` / `sectionId` from those few
candidates.** Cheap, accurate, auditable. Store a confidence score; low-confidence items
go to the Stage-8 review queue rather than being guessed. (Your existing `appliesTo`
field handles questions that legitimately belong to several chapters.)

### Stage 6 — Derive flashcards + clean model answers
From each marking scheme, every distinct marking point / definition becomes a `keyTerm`
`{ term, definition, section }` on the matched LO — *this is exactly how Examly gets
"50,000 flashcards from state papers."* Optionally an LLM rewrites marking-scheme
shorthand into a readable `model` answer, while you keep the raw scheme text for fidelity.

### Stage 7 — Load
Render the canonical JSON into the files the app actually loads: append
`EXAM_QUESTIONS_DB` entries, inject `keyTerms` into the `<subject>-content.js` sidecar,
write chapter scaffolds into `data.js`, copy cropped diagrams into `exam-images/`. This is
a dumb, deterministic render — all judgement happened upstream.

### Stage 8 — QA
Validate every record against `SUBJECT_TEMPLATE` required fields; dedupe on
`(subject, year, paper, q)`; flag "⚠ may not match current course" using syllabus change
dates (you already use this tag); sample for spot-checks; work the low-confidence review
queue. Emit a **coverage report**: questions per chapter per subject, so you can see gaps
the way Examly never shows you theirs.

---

## 3. Architecture decisions that matter

- **Canonical store, generated outputs.** Extraction writes one JSON per subject; the
  `.js` files are render artifacts. Decouples the slow/expensive extraction from your app
  format and lets you re-render freely. *Never hand-edit generated files.*
- **Stages are cached + idempotent.** Each reads the prior stage from disk. A crash or a
  schema tweak re-runs only what's needed. Thousands of PDFs make this non-negotiable.
- **LLM used surgically.** Bulk OCR is Tesseract; the LLM only does segmentation edge
  cases, the final tag decision over k candidates, and marking-scheme cleanup. This is the
  difference between a €20 run and a €2,000 one.
- **Human-in-the-loop only at the review queue.** Confidence thresholds route the doubtful
  few percent to you; the rest flow through untouched.

---

## 4. Rollout for all 26 subjects

Effort is front-loaded into building the pipeline, not into each subject. Once it works
for one subject end-to-end, every new subject is mostly *config* (subject code + syllabus
scaffold) plus a QA pass.

- **Phase 0 — Pilot:** one subject you already know well (Biology). Run all 8 stages,
  tune segmentation + tagging until a coverage report looks right.
- **Phase 1 — Your current subjects:** Business, PE, Geography, Maths, Chemistry. Same
  pipeline, new scaffolds. Validates the "new subject = config" claim.
- **Phase 2 — Text-heavy subjects:** History, English, languages, Economics, Politics &
  Society. High LLM leverage, clean PDFs, fast wins.
- **Phase 3 — The long tail:** practical/scanned subjects (Art, Construction, DCG,
  Engineering, Music) needing OCR and more manual QA.

## 5. Realistic expectations

The acquire → extract → segment → pair stages are deterministic engineering — a week or
two to get solid. **Topic tagging is where the time goes and where the value is**; budget
your iteration there. A single developer with this pipeline can plausibly reach
Examly-comparable *coverage*. What you won't get for free is their polish, AI-correction
UX, and game modes — but that's product surface, not data, and it's exactly where bare
bones can choose to differ rather than copy.

## 6. One caution

SEC papers and marking schemes are free to access but remain © State Examinations
Commission / Government of Ireland. Reproducing them for a small invite-only cohort is low
risk; redistributing them publicly or commercially (as Examly does) is a question worth
real legal advice before any public launch. Keep the canonical store private and gate the
app as you already do.

---

*See `pipeline/` for a runnable Stage 1–2 proof of concept and stage stubs.*
