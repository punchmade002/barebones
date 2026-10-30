# Geography content snapshot — 2026-10-19

The geography content as it stood before the syllabus-based rebuild. Nothing in this folder is
loaded by the app.

| File | What it is |
|---|---|
| `rendered-geography-content.json` | Every geography chapter exactly as the app showed it: the notes assembled by `generated-notes-content.js`, key terms and test questions, for all 25 chapters. |
| `geography-flashcards.js` | The flashcard deck at the time of the snapshot (after the 2026-spec cards were removed). |
| `geography-flashcards-before-2026-spec-removal.js` | The deck before the 22 cards from the 2026 specification were removed. |
| `geography-test-questions.js` | The authored test questions (3 per chapter). |
| `geo-content.js` | The earlier hand-written geography notes, retired from the app on 2026-08-14 and kept in the repo root until this snapshot moved it here. |

The live app still loads `geography-flashcards.js` and `geography-test-questions.js` from the
repo root. Each chapter keeps showing its old generated notes until new subsection notes are
written for it (see `course-outlines/NOTES_STANDARD.md` and `scripts/build_notes.py`).
