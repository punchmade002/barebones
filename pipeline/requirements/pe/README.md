# PE requirements — three-strand specification

This is a requirements bank for the **three-strand Leaving Certificate PE specification**, selected by the user. It is independent of the current app chapter list and the questions that have appeared in examinations. It does not change, replace or certify any existing flashcards.

## Read the result

- `requirements.md`: the reviewable learning-point list, grouped by official outcome.
- `requirements.json`: the same source-backed requirements with stable IDs, acceptance criteria, evidence modes and provenance.
- `audit.json`: structural reconciliation, explicit content checks, outstanding editorial checks and source accounting.
- `existing-content-review.json`: 121 existing PE notes and 137 canonical flashcards preserved as candidate content, plus the older guide cross-check and factual/scope review flags. Their existence does not count as coverage; this is not an audit of all runtime content.
- `sources/specification-2026.pdf`: the three-strand official specification, kept separately from the older two-strand resource pack.
- `sources/specification-pages.json`: full, page-addressed text extraction and source fingerprint.

## What a required learning point means

A specific knowledge, reasoning or performance capability that contributes to an official requirement and can be checked against explicit acceptance criteria. A topic label, keyword match or card count does not establish coverage. One learning point may need multiple cards; one card may contribute to multiple points, but each acceptance criterion must be assessed separately.

`syllabus-explicit` means the item is directly named or explicitly requested by the specification. `supported-decomposition` means the item is an editorial breakdown needed to make a broad official requirement assessable; it is not a claim that the specification prescribes those exact words, examples or quantities. Existing notes and the older specification never automatically create new mandatory requirements.

## Scope and version

The target is the specification with three strands, not a guessed exam year. NCCA labels this specification for introduction in September 2026; the user reports studying the three-strand course in sixth year. That administrative mismatch is recorded, not resolved by overriding the user's course selection. Confirm the applicable SEC assessment brief before activating an exam-year profile.

The three strands have 11, 11 and 10 official outcomes. All are included. This specification does not carry forward the older bank's Topics 7–10 prescription filter. Current annual project themes, deadlines, reporting formats and any adjustments are a separate overlay; they are not invented here.

Default editorial depth is Higher Level, consistent with the existing resource manifest. The official outcomes apply at both levels; Higher Level requires deeper analysis, justified decisions and application in unfamiliar contexts. Practical requirements need observed or recorded performance. Flashcards can support preparation, but cannot certify those skills.

## Completion and future changes

Structural checks establish that all official outcomes and the audited named content have requirements. They do **not** prove factual correctness of future cards or that every useful teaching detail has been captured. This bank remains an editorial baseline pending teacher/source-depth review; it must not be advertised as independently certified exhaustive.

Keep point IDs stable. Add or revise individual requirements and invalidate only their dependent content. Never silently renumber IDs, delete unmatched existing content or transfer study progress using text similarity. No automatic card matches have been accepted in this task.

Run `python3 pipeline/requirements/pe/build.py` to rebuild the JSON and Markdown from the authored definitions. Run `python3 pipeline/requirements/pe/validate.py` to check the saved artifacts independently. Building needs only the standard library once source extraction is saved.
