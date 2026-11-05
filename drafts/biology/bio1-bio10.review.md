# Review: biology chapters 1–10 (packages and Haiku notes, 2026-10-22)

There are 37 subsections, split in `data.js` to match the outline. Five higher-model agents
wrote the packages, a chapter group each. The brief was the bio19–21 lesson: each must-cover
item carries its full teaching content. Four Haiku agents then wrote the notes. All 48 biology
files pass `scripts/build_notes.py biology` and are built into `biology-notes.js`.

**Density.** Chapters 1–10 average 6.0 points per block and about 1,100 words per subsection.
Chapters 19–21 averaged 3.7 points per block and 440 words. Richer packages fixed the thin
notes.

## Checks done

- **Must-cover coverage.** Each writer's reply maps every must-cover id to a block. I read
  every subsection in full against its package.
- **Unpackaged names.** `check_package_names.py` flags only sentence openers and possessive
  forms of names that are in the packages (St Mary's Hospital, King's College London).
- **Dates and figures.** Every dated or numeric claim in chapters 1, 3 and 4 was listed and
  checked: cell theory dates, Redi, Semmelweis, *H. pylori*, the HGP and the Bermuda
  Principles, Hwang, Amgen, Wakefield, the Danish MMR study, penicillin, insulin, DDT,
  ivermectin, thalidomide, the membrane and enzyme models, and Meselson–Stahl. The microscopy
  history and Nobel prizes, Stanley 1935 and myxoma 1950 were checked in chapters 6–7, and the
  bio8 nutrition facts too. No errors were found.
- **Worked examples.** The arithmetic is correct: bio2 means, ranges and rates; bio5 SA:V;
  bio7 actual size; bio8 dilutions. So are the bio10 base-pairing answers and the codon
  decoding.
- **Higher Level marking.** Only the bio7-s3 ER/Golgi block, all of bio9-s2 and all of
  bio10-s3 are marked, as the outline says.
- **Investigations.** bio7-s4, bio8-s7 and bio8-s8 are written in full: variables, controls,
  method, safety, results and errors.

## Fixed during review

- **Cross-references to titles that don't exist:**
  - "Vitamins and Minerals" (bio9-s2) → "Vitamins"
  - "Viruses: replication" (bio6-s1) → "Immunity"
  - "Investigation: growth of microorganisms" (bio2-s2) → "Microorganisms"
  - "Surveys" (bio2-s3) → "Investigating an Ecosystem"
- bio6-s2 said "pathogens such as *E. coli*"; it now says "some strains of *E. coli*".
- The bio2 subsection labels lost their leading numbers.
- data.js bio8-s2 is now titled "Structures of biomolecules", to match the cross-references.
- The build test's "untouched chapter" fixture moved from bio5 (now authored) to bio13.

## Minor points (not fixed)

- **Cross-references ahead of their chapters.** Notes refer to later material by the outline's
  subsection titles (e.g. "Evidence for evolution", "Generating a DNA profile"). These match
  once chapters 11–36 are split as the outline says, and must keep those titles.
- **Overlaps, kept short and cross-referred:**
  - hypothesis, the method cycle and reproducibility (bio1 and bio2)
  - correlation vs causation (bio2-s4 and bio3-s1)
  - the cell theory (bio1-s1 and bio5-s1)
  - Watson and Crick (bio4-s1 and bio10-s1)
  - antibiotic resistance (bio3-s2 and bio3-s3)
- **Assumed items beyond the outcomes.** These are taught as assumed knowledge: SA:V (bio5),
  70S/80S ribosomes (bio6, bio7), magnification formulae (bio7) and purines/pyrimidines
  (bio10).
- **Lipid tests.** bio8-s7 teaches both the grease-spot and Sudan III tests, because the
  specification names no reagent.
- **bio2-s7.** It keeps strictly to the specification's text on the Biology in Practice
  Investigation, with no SEC rules, word counts or dates.
- **Practice-question marks** (6/9/12) are guesses; there is no paper yet on this
  specification.
- **Old review questions.** Each chapter's review outcome (`bioN-1`) keeps the old test
  questions. Its old notes and flashcards are cleared.
