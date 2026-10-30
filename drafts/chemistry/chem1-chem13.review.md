# Review: chemistry chapters 1–13 (packages and Haiku notes, 2026-10-30)

Chapters chem1–chem13 were split in `data.js` into the 65 subsections of
`course-outlines/chemistry.md`, with a "Chapter review" outcome (`chemN-1`) first. A higher model
wrote one information package per subsection (`course-outlines/packages/chemistry/`), from the
2025 specification (bold items marked [HL]) and the past-paper topics still on it. Thirteen Haiku
agents, one per chapter, wrote the notes (`content/chemistry/`). All 65 files pass
`scripts/build_notes.py chemistry`; 13/13 split chapters are complete and ship in
`chemistry-notes.js`.

## Coverage, before and after (chem1–chem13)

| | Before | After |
|---|---:|---:|
| Units of study | 56 specification outcomes | 65 outline subsections (+ 13 reviews) |
| Note blocks | 183 (one paragraph each) | 309 (5.7 bullets per block, 1759 bullets) |
| Words of notes (approx.) | 20 000 | 31 000 |
| Thin outcomes (one short paragraph) | 25 | 0 |
| Flashcards | 192 | 517 |
| Practice and test questions | 145 | 285 (145 kept on the reviews + 140 new) |

Every learning outcome of the specification in these chapters, every "learn about" item, and
spec 3.4.1 (which had no `data.js` entry) has a subsection. Higher Level material is in its own
blocks headed "(Higher Level only)"; seven subsections are wholly Higher Level (chem3-s2,
chem5-s4, chem6-s5, chem7-s3, chem11-s4, chem12-s3, chem12-s4).

## Restructure

- `data.js`: chem1–chem13 now list `chemN-1` "Chapter review" and `chemN-s1…` with
  `syllabusRef`. chem14–chem26 are unchanged.
- `chemistry-content.js`: the old chem1–chem13 notes and flashcards (and the fix-ups that moved
  them between outcomes) are removed; all 145 of their test questions, including the 22 from
  `chemistry-test-questions.js`, are kept on each chapter's review outcome. No question was lost.
- Tests: `chemistry-outcome-notes.test.cjs` checks the split chapters (review first, every
  subsection authored, with flashcards and a question) and that `chemistry-notes.js` is up to
  date; the counts in `science-subject-test-questions.test.cjs` follow the new structure.

## Checks done

- **Every quoted cross-reference** checked against the app's titles by script; two pointed to
  subsections that don't exist in the unsplit hydrocarbons chapter and now name the chapter.
- **`check_package_names.py`** on all 65 files: every number and name in the notes is in its
  package (the remaining hits are sentence openers and cm³ → L conversions).
- **Arithmetic** in every package re-worked by script before writing (gas law, Mr of a volatile
  liquid, molar volume, isotopic abundance, empirical formulae, hydrates, concentration units,
  all titration and back-titration problems).
- **Higher Level marking** checked by script: wholly-HL subsections are marked throughout; every
  package with [HL] items has HL blocks; no unmarked package has any.
- **Read in full:** electron configurations (chem3-s4), conjugate pairs (chem11-s4), and the
  investigation blocks to which writers added variables and controls.
- **In the app** (headless Chromium): all 65 subsections load as authored, each review keeps its
  questions, no script errors.

## Fixed during review

- **Bond angles:** the VSEPR package gave 104.5° for H₂S and 107° for PH₃ (the writer flagged
  H₂S). Measured angles are about 92° and 93.5°; package and notes now say so.
- **Literal reading of the facts rule:** the first writers dropped examples written inside
  must-cover items (only the "Checked facts" table looked allowed). The rule was clarified for
  all later writers and the chem2 and chem4 writers restored what they had removed.
- **Packages corrected before writing:** a confusing copper abundance example (chem8-s2), a
  garbled practice prompt (chem12-s4), and chapter-number pointers replaced by chapter titles.

## Decisions and minor points (not changed)

- **Old notes for chem1–chem13 are retired, not merged.** They predate the outline and were
  organised by specification outcome; the old test questions stay on the review outcomes.
- **Values used:** Pauling electronegativities and first ionisation energies as in the SEC
  Formulae and Tables; STP 273 K and 101.3 kPa with 22.4 L mol⁻¹ (the IUPAC 100 kPa / 22.7 L is
  noted); typical school glassware tolerances are given as "typical".
- **Content beyond the specification's list,** kept to what the outcomes need: Döbereiner and
  Newlands, Dalton and Thomson, the Aufbau, Pauli and Hund rules, Gay-Lussac's law of combining
  volumes, paper chromatography and the separating funnel, back titration (HL unfamiliar
  context), and one bullet on metallic bonding.
- **Invented data** in worked examples is labelled "sample data"; practice-question marks are
  guesses.
- **Past papers:** the app's chemistry past papers are from the 1999 syllabus; packages list
  only question topics still on the 2025 specification.
