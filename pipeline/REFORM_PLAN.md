# Pipeline reform — implementation plan

> **STATUS: implemented (2026-06-20).** All six phases below are built and unit-tested on branch
> `worktree-pipeline-reform`. Not yet run end-to-end on a real subject with live workers — that
> needs a resource bundle in `pipeline/resources/<subject>/` and a full `/run-pipeline` loop.

Design source: grilling session 2026-06-19 (see memory `project_pipeline_design`). This plan turns
that design into code. It builds on the partial reform already on branch `worktree-pipeline-reform`
(commit 2df0fe8): paper-only `segment.py`, `schemes.py`, per-stage models, `validate.py`,
mandatory marks, `scaffold/<subject>.spec.txt`, pre-merge sample.

Legend: ✅ already built · 🔨 new/changed in this plan.

---

## Phase 0 — Already built (reform commit 2df0fe8)
- ✅ Paper-only `segment.py` (no scheme in context); marks required > 0.
- ✅ `schemes.py` — scheme-only official-answer matching by part id.
- ✅ Per-stage model tiers (`config.STAGE_MODEL`): opus segment, sonnet schemes/answers, haiku rest.
- ✅ `validate.py` — stub/zero-mark detection, post-segment auto-retry, quarantine, sample report.
- ✅ `scaffold_gen.py` reads `scaffold/<subject>.spec.txt` when present.

These stay; later phases extend them.

---

## Phase 1 — Resource-bundle ingestion (foundation; everything depends on it)

Goal: a per-subject drop folder becomes a pooled, text-extracted corpus the rest of the pipeline reads.

🔨 **New `resources.py`**
- `corpus(subject) -> str`: read every file in `pipeline/resources/<subject>/` (PDF, .txt, .md, .docx),
  extract text (reuse `extract.py` / pdfminer for PDFs; plain read for text), concatenate with
  per-file headers, cache to `_data/resources/<subject>.corpus.txt`. Cap at a sane char budget.
- `roles(subject) -> dict`: light filename heuristic (`guide-*`, `summary-*`, `worked-*`) so later
  stages can weight, but no manifest required.
- `has_bundle(subject) -> bool`.

🔨 **Cutoff from the bundle** (`config.py` + `resources.py`)
- `resources.extract_cutoff(subject) -> int | None`: regex/short-model scan of the corpus for the
  syllabus introduction year ("first examined 20XX", "revised syllabus 20XX").
- `config.cutoff_for` prefers the bundle-derived cutoff; if none found, print a clear FLAG and fall
  back to the existing `SYLLABUS_CUTOFF` estimate (still marked unverified).

🔨 **`run.py`**: run resource ingestion at the top (after digest), print a one-line summary
(`N resource files, M chars, cutoff 20XX [from bundle|estimate]`). Warn loudly if no bundle.

**Verify:** drop a sample PDF + txt in `resources/zz-test/`; assert corpus extracts both and cutoff
is read from a line like "first examined 2004".

---

## Phase 2 — Scaffold & flashcards from the bundle

### 2a. Scaffold from the corpus
🔨 `scaffold_gen.py`: source = `resources.corpus(subject)` (authoritative) when a bundle exists,
falling back to `spec.txt`, then papers. Papers stay only as a secondary hint for section names.
Prompt already supports a spec branch — point it at the corpus.

### 2b. Flashcards rewrite (the deferred reform E)
This is the biggest rewrite. Flashcards must come from the GUIDE, not past-paper question text.

🔨 `flashcards.py` — replace `pool_by_chapter` (which pooled raw question text — the bug):
- Source pooled text per chapter = the **resource corpus**, sliced/attributed to each scaffold
  chapter (ask the model which chapter each concept belongs to, or pool whole corpus per call with
  the chapter title as the focus). NOT question text.
- One model call per chapter: "from this course material, produce the atomic concepts a student must
  know for <chapter>", output in the existing app shape `{term, definition, section, type}`.
- For concepts the guide covers but papers never tested: still produce the card (definition straight
  from the guide). Question bank is untouched — no invented questions.
- `type`: make subject-appropriate. Drop the history-flavoured enum
  (person/event/movement/policy/law/concept); either infer a small per-subject set or default all to
  `concept`. Keep the field so the app shape is unchanged.
- **Dedup against existing curated flashcards**: read the subject's live cards (from the app's
  `*-content.js` keyTerms / `FLASHCARDS_DB`); drop generated cards whose term already exists
  (curated wins). Reuse/extend the merge dedup from Phase 4.

**Verify:** run flashcards on a subject with a small corpus; assert no card `term` is a question stem
(no leading "Define/Describe/Using/Comment"), all in app shape, none duplicating curated terms.

---

## Phase 3 — Answer grounding + scheme-point length

### 3a. Scheme-point length targets
🔨 `schemes.py`: while reading each scheme, also return per part a `points` count (how many distinct
credited points the scheme rewards). Add to `emit_scheme_answers` schema; store on the part as
`scheme_points`.
🔨 `config.recommended_words`: if a part has `scheme_points`, target = points × words-per-point
(tunable); else fall back to the existing words-per-mark/time model. Add `WORDS_PER_POINT` and a
per-subject `WORDS_PER_MARK` fallback.

### 3b. Answer grounding in resources
🔨 `model_answers.py`: `cached_prefix` includes a capped slice of `resources.corpus(subject)` as
"COURSE MATERIAL (ground your answer in this)", alongside the marking scheme. Stays cache-friendly
(corpus is stable per subject).
🔨 Length enforcement = over-target upfront: prompt states the target AND a hard minimum
("write at least N words; develop every scheme point fully; do not stop short"). No retry loop for
length — `validate` still surfaces under-length as a soft warning.

**Verify:** a high-mark essay part comes back ≥ its hard minimum and cites material present in the
corpus; a low-mark part stays concise.

---

## Phase 4 — Curated-wins merge / dedup

🔨 **New `curated.py`** (or extend `merge.py`):
- `load_curated_questions(subject)`: parse the app's existing hand-curated questions for the subject
  (the `*-content.js` packs / `EXAM_QUESTIONS_DB`) into a comparable shape.
- Dedup key: `(year, level, question-label)` plus fuzzy question-text match.
🔨 `merge.py`: before writing the generated JS, drop generated questions that duplicate a curated one
(curated wins); only the gap-fillers are published. Never overwrite curated `*-content.js`. Same
dedup principle already needed by flashcards (Phase 2b) — share the helper.

**Verify:** on a subject that already has curated questions, assert generated output contains no
`(year,level,label)` that exists in curated, and curated files are byte-unchanged.

---

## Phase 5 — Tagging review bucket + diagram visual validation

### 5a. Tagging
🔨 `segment.py` already returns `tag_confidence`. In `validate`/`segment.collect`: questions below the
confidence threshold keep their best-guess chapter (usable). If the count of low-confidence questions
for a subject is **> 5**, write them to a `_data/reports/tag-review-<subject>.json` bucket and surface
it in the gate summary for human review.

### 5b. Diagram visual validation
🔨 `images.py`: after cropping a candidate figure, add a second worker job that Reads the crop PNG and
confirms it actually shows the figure (not blank/text/partial). Only attach `part.diagram` when
confirmed; otherwise skip and record in `figures-<subject>.json` as "rejected-crop" for review.
(One extra haiku vision call per cropped image.)

**Verify:** feed one good crop and one blank/text crop; assert only the good one attaches.

---

## Phase 6 — Auto-publish-if-clean gate

🔨 `config.py`: thresholds `MAX_QUARANTINE_FRAC` (~0.05) and `MAX_SOFT_WARN_FRAC` (~0.15).
🔨 `validate.enforce` returns the quarantine fraction and soft-warning fraction.
🔨 `run.py` final gate: if both fractions are under threshold AND no tag-review bucket was raised →
**merge automatically** and print `PIPELINE COMPLETE`. Otherwise print the sample/quarantine/review
paths and STOP, requiring `--merge` to override. (`--no-merge` still forces stop; `--merge` still
forces publish.)

**Verify:** a clean synthetic subject auto-merges; one with >5% quarantined stops for review.

---

## Suggested build order & checkpoints
1. Phase 1 (resources + cutoff) — nothing else is right without it.
2. Phase 2a scaffold, then 2b flashcards (depends on corpus + scaffold).
3. Phase 3 answers (depends on corpus + schemes points).
4. Phase 4 dedup (shared by 2b and merge).
5. Phase 5 tagging + diagrams (independent, can parallelise).
6. Phase 6 gate flip (last — depends on the metrics the other phases emit).

After each phase: `python3 -m py_compile pipeline/*.py` + the phase's verify step on a `zz-test`
sandbox subject. Full end-to-end re-run of a real subject (home-economics, scrapped & rebuilt) only
after Phase 6, via `/run-pipeline home-economics --restart`.

## Out of scope (explicit)
- No invented exam questions ever.
- No change to the app's flashcard/question data shapes (term/definition/section/type; parts schema).
- Curated `*-content.js` files are read-only inputs, never overwritten.
