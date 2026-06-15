# pipeline/ — exam data extraction

Turns the free SEC archive PDFs into bare bones content. Full design: [`../DATA_PIPELINE.md`](../DATA_PIPELINE.md).

```
run.py           ⭐ re-invokable orchestrator: subject -> playable in the app, NO API key
agent_bridge.py  (NEW) file-based stand-in for the API: stages write jobs, a subagent answers
config.py        paths, subjects, SYLLABUS_CUTOFF, and the diagram-crop tunables
acquire_form.py  Stage 1 — form-discovery: no codes needed; downloads papers+schemes, HL+OL
acquire.py       Stage 1 (legacy) — direct URL enumeration once you know the code
digest.py        Stage 2+ — PDF -> paired paper+scheme page-text, app-ready JSON
scaffold_gen.py  Stage 2.5 — auto-derive scaffold/<subject>.json from digests when missing
segment.py       Stages 3-5 — questions + parts + marks + model answers + topic tags
images.py        Stage 7 — diagram crops -> exam-images/, sets part.diagram (subagent finds the box)
model_answers.py Stage 6a — H1 sample answers for questions the scheme doesn't model
flashcards.py    Stage 6b — deduplicated, per-chapter flashcards across all years
merge.py         Stage 8 — copy generated JS to repo root + wire <script> tags into app.html
scaffold/        per-subject section+chapter lists the tagger assigns to (auto-made if absent)
extract.py       Stage 2 (generic) — PDF -> page text + page PNGs
_data/           generated store (gitignore this) — raw, digest, canonical, reports, agent jobs
```

## ⭐ One command — no API key (a subagent does the model work)

There is **no `ANTHROPIC_API_KEY`**. The deterministic stages run as plain Python; each model
stage WRITES its jobs to `_data/agent/<stage>/in/` and the orchestrator stops, printing
`WORKER NEEDED <dir>`. A spawned **Haiku subagent** (`pipeline-worker`) reads those jobs (and any
page images), writes answers to `out/`, and you re-run `run.py` to collect them and advance.

The easiest way is the **`/run-pipeline` skill**, which runs that loop for you:

```
/run-pipeline biology
/run-pipeline biology --no-acquire --limit 2     # bounded smoke test
```

Doing it by hand is the same loop:

```bash
pip install pymupdf playwright --break-system-packages   # note: NO anthropic / no key
playwright install chromium

while :; do
  python3 run.py biology            # advance one model stage (or finish)
  # if it printed "WORKER NEEDED <dir>": spawn the pipeline-worker subagent on <dir>, then loop
  # if it printed "PIPELINE COMPLETE": stop
done
```

Modifiers:

| flag | effect |
|------|--------|
| `--no-acquire` | don't download; reuse `_data/raw/<subject>` |
| `--no-images` | skip the diagram-crop stage (Stage 7) |
| `--no-merge` | stop before wiring generated JS into `app.html` |
| `--regen-scaffold` | rebuild `scaffold/<subject>.json` even if it exists |
| `--limit N` | cap papers (segment) / candidates (images) — smoke tests |
| `--restart` | clear queued worker jobs and redo the model stages (keeps PDFs/digests/canonical) |
| `--headful`, `--include-irish` | acquire options |

## How the keyless model stages work

Stages 1-2 (acquire + digest) are plain Python. The five model stages each have a `prepare`
(write jobs) and `collect` (read answers) half, bridged by `agent_bridge.py`:

- `prepare` writes one `in/<id>.json` per unit of work — `{prompt, schema, meta, image?}`. For
  `images`, it also renders the page PNG into `in/` for the worker to look at.
- the **`pipeline-worker`** Haiku subagent fills `out/<id>.json` with JSON matching `schema`.
- `collect` reads `out/`, wraps each answer so the existing `parse_result`/`to_canonical`/crop
  code runs unchanged, and finalizes (canonical store, `.generated.js`, diagram crops, reports).

It's fully **idempotent / resumable**: a stage already collected is skipped, a worker job that
already has an `out/` file is never redone, segmented papers and cropped diagrams are not repeated,
and `images` records every checked part in `_data/reports/figures-<subject>.json`. The `images`
cost gate is `config.FIGURE_CUE_RE` — only figure-cued question parts get a worker call (widen it
if a subject's figures are being missed). For a big stage you can split the `in/` files across a
few parallel `pipeline-worker` agents — they only write `out/`, so they don't collide.

Output: `_data/canonical/<subject>.json` (source of truth, with diagram paths) +
`exam-questions-db.<subject>.generated.js` + `flashcards-<subject>.generated.js` +
`_data/reports/segment-<subject>.json` + `figures-<subject>.json`. `merge` then copies the JS to
`<subject>-exam-questions.js` / `<subject>-flashcards.js` at the repo root and wires `<script>`
tags into `app.html`.

> **Merge caveat:** `merge.py` overwrites the root `<subject>-*.js` files in place. That's the
> intent for *new* subjects. If a subject already has **hand-curated** flashcards/questions under
> the same filename, run with `--no-merge` and diff the generated files yourself before copying.

## Relevant years & digest output

**"Relevant" papers** = every year from the subject's current-syllabus cutoff
(`config.SYLLABUS_CUTOFF`) to now, plus the single pre-change **reference** year (kept
because content usually overlaps; files tagged `-REF`). History's cutoff is 2006
(documents-based study first examined) — confirmed, and both boundary years (2006 and the
2005 reference) were verified live to have full HL+OL papers. That's **22 years × 4 files
(HL/OL × paper/scheme, English) = up to 88 PDFs**.

Output:
```
_data/raw/history/2023-higher-EV-papers.pdf, …-scheme.pdf, 2005-…-REF.pdf, …
_data/digest/history/2023-higher.json   ← paper + marking scheme, page text, ready for Stage 3
_data/digest/history/_index.json        ← coverage: which sets have both paper + scheme
_data/reports/manifest-history.csv
```
Each digest pairs the paper with its marking scheme so the next stage can segment
questions and pull model answers/flashcards. Scanned older pages are flagged `needs_ocr`.

## Stage 1: form-discovery (no subject codes) — VERIFIED against the live site

```bash
pip install playwright --break-system-packages
playwright install chromium

python acquire_form.py history             # HL+OL papers + marking schemes (English)
python acquire_form.py history --headful   # watch it drive the form
python acquire_form.py history --include-irish
```

The archive's "download" links are **encrypted per-file tokens**
(`/exammaterialarchive/?fp=<~135 chars>`), not guessable static URLs — so you can't
enumerate filenames, you have to let the form produce the links. The script ticks the
terms box, drives the four cascading dropdowns (Type → Year → Examination → Subject,
each a POST reload), reads the results table (Higher/Ordinary × English/Irish), and
downloads each PDF through the same browser session. Confirmed working: 2023 LC History
HL English = a 0.97 MB `application/pdf`. Output: `_data/reports/manifest-history.csv` +
`_data/raw/history/<year>-<level>-<EV|IV>-<papers|scheme>.pdf`. Then run `extract.py`.

> `acquire.py` (direct-URL enumeration by subject code) is kept only as a fallback for the
> legacy `/archive/exampapers/YYYY/...pdf` static paths. The form path above is the
> reliable one — prefer it.

## Quick start (pilot one subject)

```bash
pip install pymupdf --break-system-packages

# 1. Open the SEC archive form once, pick e.g. Biology, read the PDF URL in the
#    network tab, and fill SUBJECTS["biology"]["code"] + the pattern in
#    acquire.py:archive_url(). Then:
python acquire.py biology       # download every Biology paper + scheme
python extract.py               # PDFs -> page text + images

# 2. Implement segment/pair/tag/derive in stages_3to8.py (these need an LLM +
#    embeddings — that's where the iteration is), write canonical/biology.json, then:
python stages_3to8.py load biology   # -> exam-questions-db.biology.generated.js
```

The generated `.js` is written beside the app file so you can **diff before merging** —
nothing auto-overwrites your hand-curated content.

## Why it's built this way
- Everything converges on the `Question`/`Part` dataclass in `stages_3to8.py`. The app
  `.js` files are a pure render of that — never hand-edit generated output.
- Every stage is cached/idempotent: re-running only does new work.
- The LLM is used only for segmentation edge cases, the topic-tag decision, and cleaning
  marking schemes — not bulk OCR. Keeps cost down.
