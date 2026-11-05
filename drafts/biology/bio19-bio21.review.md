# Review: biology chapters 19–21 (Haiku notes from information packages, 2026-10-20)

Eleven subsections were written by Haiku, one agent per chapter, from
`course-outlines/packages/biology/`. All 11 files pass `scripts/build_notes.py biology` and are
built into `biology-notes.js`, so they show in the app.

## Checks done

- Every must-cover id, including the (assumed) items, maps to a block in each writer's
  report. I read every block against its package.
- `scripts/check_package_names.py biology`: the only flagged words are sentence openers
  ("Around", "Damaged", "Examples of", "Arrival of", "Conclusion of", "Diagram", "Protection").
  No names, figures or examples were added from memory.
- Traps were obeyed throughout: no cranial nerves or autonomic system, no electrochemistry,
  no glucagon, no skin structure, no tropisms, no eye or ear.
- The Higher Level material is marked correctly: every bio19-s5 heading, and the FSH/LH/ADH
  block in bio20-s1. No other headings are marked.
- No factual errors were found.

## Minor points (not fixed)

- bio19-s5 "The cycle at a synapse" restates the release stages from bio19-s4. The package
  asked for the full cycle as a model, so the overlap is deliberate but breaks "each fact once".
- Cocaine and dopamine reuptake, and Parkinson's disease, each appear in both bio19-s5 and
  bio19-s6. Both packages required them, and each instance cross-references the other.
- The adrenaline-in-danger example appears in both bio21-s1 and bio21-s3. Both packages required it.
- bio21-s1: the writer added diagram cues the package didn't ask for (following the biology
  rule in NOTES_STANDARD). They are reasonable.
- bio20-s2 "Evaluating the use of hormones" is two generic points; the package's E1 was thin.
- Flashcards have no Higher Level marking: bio19-s5's key terms are all Higher Level material
  but show without a label. The writer of bio20-s1 kept FSH, LH and ADH out of the key terms for
  this reason. If flashcards should carry a level, `keyTerms` needs a field for it.
- Density is lower than geography's (most blocks 2–6 points), because the packages give one
  item per fact. Practice-question marks (6–15) are guesses, as there is no paper yet on the
  2025 specification.

## Package lessons for the next chapters

- Writers follow packages literally. Thin package items, such as bio20-s2 E1, produce thin blocks.
- Telling writers that a fact is in another subsection works: they cross-refer by title.
- Say in each package whether diagram cues beyond the ones listed are wanted.
