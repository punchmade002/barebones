# Information packages

Notes are written in two stages:

1. **A higher model writes the package** (`packages/<subject>/<loId>.md`). This sets the scope
   and supplies every specific fact the notes may use. It needs knowledge and judgement, so it
   is done by a strong model (Opus or Sonnet class).
2. **A smaller model writes the notes** (`content/<subject>/<loId>.json`) from the package and
   `NOTES_STANDARD.md`. This is the long, cheap writing.

Why: in the geography trial (`drafts/geography/geo-glaciation-s1.review.md`), Haiku wrote clear
explanations of processes but gave one wrong example as a fact (Castle Rock as a roche
moutonnée), left out examples it was unsure of, missed items the outline didn't list, and copied
figures from past papers. Each package section below prevents one of those failures.

## Package format (copy `geography/geo-glaciation-s1.md`)

1. **Must cover:** a checklist with an id for each item. Every syllabus point, plus anything
   past exams ask. One bullet or block per item. This replaces the writer's guesswork about
   scope.
2. **Checked facts and examples:** the only named places, dates and figures the notes may use.
   Include only what you are sure of. Where you aren't sure, write "No checked example. Do not
   name one."
3. **Traps:** known wrong examples, confusable terms, and what belongs to a neighbouring
   subsection.
4. **What exams ask:** question topics and expected answers from past papers, without question
   wording or past-paper figures.
5. **Practice questions to write:** marks, prompt, and what the model answer must and mustn't
   contain.

Writing a package for a subsection:
- Read the syllabus wording (official PDF), the outline entry, and the chapter's past exam
  questions (`<subject>-exam-questions.js`, filter by `chapterId`).
- Accurate before complete: a missing example costs a reviewer a minute; a wrong one can go
  unnoticed.
- Write packages for a whole chapter at a time, so the boundaries between its subsections are
  clear.

## Prompt for the writing model

Replace `<loId>` and `<subject>`; run once per subsection, a whole chapter at a time.

> You are writing Leaving Certificate revision notes for one subsection of a study app. Work in
> the repository root.
>
> Read in full: `course-outlines/NOTES_STANDARD.md` (rules, JSON format, worked example; match
> its density and style) and `course-outlines/packages/<subject>/<loId>.md` (your scope and
> facts).
>
> Write `content/<subject>/<loId>.json`.
> - Cover every item in the package's "Must cover" list, in a sensible teaching order. Every
>   item needs at least one bullet.
> - Name only the places, dates and figures in the package's "Checked facts" table. If an item
>   has no example there, describe it without one. Don't add examples from memory.
> - Obey the "Traps" section.
> - Write the practice questions in section 5 exactly as specified.
> - Plain text only; each fact once; no filler.
>
> Then run `python3 scripts/build_notes.py <subject> --check` and fix every error. A warning
> that the chapter is only partly written is fine. Edit no other file and don't commit.
>
> Reply with: the check output; a list of the must-cover ids and the block that covers each;
> anything you left out and why.

## Reviewing the notes

After the writer finishes, check each file before it ships:
- Its reply maps every must-cover id to a block; spot-check that the blocks really cover them.
- `python3 scripts/check_package_names.py <subject> <loId>` lists names and numbers in the notes
  that its package doesn't contain. Sentence openers appear too; look for real place names,
  dates and figures and confirm or remove each one.
- Read the case-study and example lines for accuracy.
- Build and publish whole chapters only (`python3 scripts/build_notes.py <subject>`).
