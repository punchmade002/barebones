# Course restructure playbook (one subject per session)

Geography was the first subject done this way. Its outputs are the reference:
`course-outlines/geography.md` (the outline) and `course-outlines/NOTES_STANDARD.md` (how notes
are written, shared by all subjects). Repeat the process below for each other subject. **Do not
write notes**; notes are written later, by other agents, from your outline.

## Lessons from geography

1. **Find which syllabus the target exam uses before anything else.** The app is for students
   sitting the **June 2027** Leaving Cert. Senior cycle is mid-reform, so some subjects have two
   documents: an old syllabus still being examined, and a new specification for later cohorts.
   The repo had geography pointed at the wrong one (the 2026 spec, first examined 2028). That
   mistake had already put wrong-course content into the app. Check curriculumonline.ie: the
   subject page labels each document, e.g. "for examination to June 2027" vs "for introduction
   September 2026". Example: biology, chemistry and business have new specifications first
   examined in 2027, so the new one is correct for them. Verify each subject; don't assume.
2. **Work from the official NCCA document, never from memory.** Download it from
   curriculumonline.ie; the environment allows that domain. If the download fails, stop and ask
   the user rather than reconstructing the syllabus yourself. In geography, the version from
   memory had wrong Higher Level-only markings, the wrong number of required biomes, and many
   missing topics.
3. **SimpleStudy is secondary.** Its structure is useful for chapter breakdown and naming, but it
   can follow an outdated syllabus and skip required topics. A topic list already exists for
   each subject in `pipeline/resources/<subject>/guide-simplestudy.md`. Treat the syllabus as
   the authority, and list every difference.
4. **Keep the existing chapter IDs.** Past exam questions, flashcards and test questions are
   tagged to the chapter IDs in `data.js` and `pipeline/scaffold/<subject>.json`. Add
   subsections inside chapters; don't rename or split chapters.
5. **Copy the syllabus's own structure and rules exactly:**
   - its section numbers
   - its "students should study" items
   - its example settings
   - the choices it sets (e.g. "one of the following"); notes must cover every option
   - which units are Higher Level only. Mark only what the document marks, and nothing else.
6. **Audit the app's existing content for the wrong course.** Look for flashcards, test
   questions and the chapter overviews in `generated-notes-content.js` that come from the
   syllabus not being examined. Geography had 22 such flashcards. Remove them and bump the
   `?v=` cache numbers in `app.html`.
7. **Make the repo consistent with the correct syllabus:**
   - `pipeline/resources/<subject>/`: `manifest.json` (url, effectiveFrom, firstExamYear),
     `spec-syllabus.pdf` (the official PDF), and `guide-simplestudy.md` (keep its required
     headings: `## Source`, `## Unit and topic structure`, `## Pipeline guidance`)
   - `relevant-resources/syllabi/<subject>.pdf` and `relevant-resources/relevant-resources.js`
   - the `SYLLABUS_CUTOFF` entry in `pipeline/config.py`
   - the subject's row in `pipeline/resources/README.md`

   Keep a superseded or future document under a clear name, e.g. `<subject>-2026-spec.pdf`.

## Steps

1. Read `course-outlines/geography.md` and `course-outlines/NOTES_STANDARD.md` to see the target.
2. Identify the syllabus examined in June 2027 (lesson 1), then download and read it in full
   (lesson 2).
3. List the subject's chapter IDs from `data.js` and the scaffold, and read the subject's
   `guide-simplestudy.md`.
4. Write `course-outlines/<subject>.md` in the same shape as the geography outline:
   - a "Read this first" header: which syllabus and why; that it must not be confused with the
     other document; a link to `NOTES_STANDARD.md`; the level rules; the choices; the assessment
     structure and weightings
   - one `### <chapter-id> — Title [syllabus refs]` per existing chapter, with numbered
     subsections. Each subsection has **Syllabus** (what the document requires, close to its
     wording), **Settings** (the syllabus's own examples, if any) and **SimpleStudy** (matching
     topic names)
   - **Appendix A**: what the syllabus requires that SimpleStudy lacks, what SimpleStudy has that
     the syllabus doesn't, and any corrections to the repo's previous assumptions
   - an appendix listing any syllabus content that has no home in an existing chapter, with a
     proposed placement. Don't create new chapters without the user's approval.
5. Check that every chapter ID appears in the outline, and that every "students should study"
   item in the syllabus appears in some subsection.
6. Do the content audit (lesson 6) and the repo fixes (lesson 7).
7. Run the tests:
   - `for f in tests/*.cjs; do node --test "$f"; done`
   - `python3 pipeline/tests/run_tests.py resources`
   - `python3 -c "import sys; sys.path.insert(0,'pipeline'); import resources; print(resources.validate_bundle('<subject>'))"`

   One pipeline test ("visual evidence filter") fails without PyMuPDF installed; that failure
   doesn't come from your changes.
8. Information packages (`course-outlines/packages/`, see its README) are written later, by a
   higher model, before any notes. They are not part of this restructure unless the user asks.
9. Commit and push to your session's branch. Report to the user:
   - which syllabus you used and why
   - chapters and subsections before vs after, and how many syllabus items there are
   - roughly how many subsections the app currently covers fully, thinly, or not at all
   - the wrong-course content you removed
   - anything uncertain or needing a decision
