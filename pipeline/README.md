# pipeline/ — exam data extraction

Turns the free SEC archive PDFs into bare bones content. Full design: [`../DATA_PIPELINE.md`](../DATA_PIPELINE.md).

```
run.py           ⭐ one command: input a subject -> all relevant papers, digested
config.py        paths, subjects, and SYLLABUS_CUTOFF (the 'relevant years' rule)
acquire_form.py  Stage 1 — form-discovery: no codes needed; downloads papers+schemes, HL+OL
acquire.py       Stage 1 (legacy) — direct URL enumeration once you know the code
digest.py        Stage 2+ — PDF -> paired paper+scheme page-text, app-ready JSON
extract.py       Stage 2 (generic) — PDF -> page text + page PNGs
stages_3to8.py   Stages 3–8 — segment, pair, tag, derive, load, QA (typed stubs)
_data/           generated store (gitignore this) — raw, digest, reports
```

## ⭐ One command per subject

```bash
p2
playwright install chromium

python run.py history                 # all relevant papers + schemes, then digest them
python run.py history --headful       # watch the browser drive the archive
python run.py history --no-acquire    # re-digest already-downloaded PDFs
```

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
