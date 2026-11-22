# Prompt: rewrite Home Economics and Business notes

Paste everything below the line into a new Claude Code session on this repository.

---

You're continuing a notes rewrite in this repo (a Leaving Cert study app). Biology, Chemistry,
Geography and PE are done; History is running in another session. Your job: **Home Economics
(199 subsections, 36 chapters) and Business (66 subsections, 20 chapters)**. Do Home Ec first,
then Business. The end quality must match the finished subjects: notes that read like a good
textbook (a lead paragraph per block, terms glossed in line, reasons and mechanisms given,
exam tips taken only from the package), with **no fact lost from the old notes** and **no fact
added that isn't in the package**.

## 0. Setup

- Work from the latest `uxtinker-qwro9d` (`git fetch origin uxtinker-qwro9d && git checkout
  FETCH_HEAD`); it has the script fixes you need. Commit on your session's branch.
- Another session is writing History on the same branch. Touch only `content/<subject>/`,
  `course-outlines/packages/<subject>/`, `<subject>-notes.js`, and your own inputs under
  `drafts/`. If you need to change `scripts/` or `NOTES_STANDARD.md`, keep it small and say so
  in the commit message.
- Before you change any notes, record the baseline commit: `git rev-parse HEAD`. `drafts/` is
  git-ignored and won't survive the container, so the final report rebuilds the old notes from
  this commit.
- Commit and push checkpoints as files land. Agents write into the tree for hours, and a
  stop hook will ask you to commit.

## 1. Read first

- `course-outlines/NOTES_STANDARD.md`: the standard. Rules 1–6 are how notes read, 7–11 what
  they contain; also the "Subject notes: home economics" section and "Rewriting existing notes".
- `course-outlines/packages/README.md`: what an information package is and its 5 sections.
- `course-outlines/homeeconomics.md` and `course-outlines/business.md`, the "Read this first"
  sections in full. They say which syllabus applies and what not to use.
- `scripts/notes_rewrite.py`: `prep <subject> [loId]` writes `drafts/notes-rewrite/<subject>/`
  (BRIEF.md, `<loId>.job.md` = old notes + package, `<loId>.old.json` = baseline);
  `check <subject> <loId>` validates `<loId>.new.json`, warns about lost numbers, terms,
  equations, diagrams, HL blocks, shrinkage, unexplained bullets and cross-references, and
  applies it to `content/` only if there are no errors; `report <subject>` re-checks every
  subsection. `prep` skips subsections with no package, and treats a subsection as done once
  any block has a `tip`. Neither subject has tips yet.
- Finished packages to copy the layout from: `course-outlines/packages/biology/` (closest to
  Home Ec's food science) and `course-outlines/packages/history/hist-eur1-s1.md`.

## 2. What's different about each subject

**Home Economics**
- The current notes were written by Haiku from the outline, without packages, and only
  spot-checked. **Expect wrong facts in the old notes.** The package writer must check every
  name, Act, body, date and figure. Anything doubtful goes under Traps as "Do not use: …,
  because …" rather than into Checked facts, and the rewrite must then drop it. That is the one
  case where a fact from the old notes may be lost.
- Follow the outline's legislation rules: only Acts and bodies in force for June 2027 (its
  Appendix A). Never use superseded ones, even where a marking scheme names them. Leave out
  changing figures (tax, welfare amounts, prices, rates); stable figures (energy values,
  temperatures) are fine.
- Past exam data: `home-economics-exam-questions.js` (`window.EXAM_QUESTIONS_DB`, filter by
  `chapterId`; parts carry `question`, `marks` and `model`). `notesRefs` doesn't narrow to a
  subsection, so make **one extract per chapter**: `source`, each part's `question` and the
  first ~220 characters of `model`. Keep each chapter's extract to roughly 10k words.
- Chemistry in plain Unicode, `Diagram:` bullets for anything students draw, and Investigation
  blocks for experiments, as the subject notes say. [HL] items get their own
  "(Higher Level only)" block, and only where the outline marks them.

**Business**
- New specification, **first examined June 2027**. Every SEC paper from 1999 to 2026 is the old
  syllabus; use one only as legacy practice, and only where its topic is also in the new
  specification. The outline's **Exam** lines (from the 2025 sample papers) are the exam source,
  so you don't need an extract file.
- `NOTES_STANDARD.md` has **no "Subject notes: business" section**. Before writing any package,
  add one (about 10 bullets), taken from the outline's "Read this first": the new spec only; no
  HL-only marking; the spec's 7 Ps list (packaging, not physical evidence); glossary definitions
  consistent with spec Appendix 2; the ethics, sustainability and digital angle in every
  chapter; real named Irish firms from the package only; changing figures left out unless the
  package verified them. The rewrite brief picks this section up automatically.
- Facts marked *(verify)* in the outline change over time. The package writer must check each
  one against a current primary source using web search or fetch. If it can't verify one, the
  package says "No checked example. Do not name one."
- Business chapters are small (2–6 subsections), so the per-chapter package approach below fits
  well.

## 3. Pipeline (one Workflow per batch; you have permission to use workflows for this)

Models: **Sonnet for everything except the verifier, which is Haiku.** Don't use Opus agents:
it costs too much here. Give every agent prompt this line: "Edit files only with the Edit,
Write or Bash tools. Never call the Artifact tool or publish anything." (An agent once
published a package as an Artifact.)

**Packages: one agent per chapter, not per subsection.** The README says to write a whole
chapter at a time so the boundaries between subsections are clear. It also means the outline,
exam extract and example package are read once instead of 5–9 times, which was the biggest
cost in History.
1. **Package writer** (Sonnet, per chapter): reads the README, one example package, the
   subject's NOTES_STANDARD section, the chapter's outline entry, every subsection's current
   `content/<subject>/<loId>.json` and the chapter's exam extract. It writes
   `course-outlines/packages/<subject>/<loId>.md` for each subsection, about 1,500–2,500 words
   each:
   - header: loId, chapterId, Syllabus scope;
   - §1 Must cover: an id'd checklist of every outline item, every in-scope fact in the current
     notes, and assumed knowledge marked "(assumed)";
   - §2 Checked facts and examples: a table of the only names, dates, figures and quotations
     the notes may use. Accurate before complete;
   - §3 Traps, including "Do not use" lines and what belongs to a neighbouring subsection,
     named by subject, not id;
   - §4 What exams ask: concrete enough that each item can become an exam tip;
   - §5 "Not needed: the subsection's practice questions already exist."
2. **Package fact-check** (Sonnet, per chapter, structured output `{issues:[{where, problem}]}`):
   tries to refute every date, figure, name, Act, body and quotation in §1–§2. Reports only
   confident errors or doubtful items. Edits nothing.
3. **Package fix** (Sonnet, per chapter, only if there are issues): judges each issue, corrects
   it or moves it to "Do not use", and edits only those package files.

Then, **per subsection** (fan the chapter's subsections out after its package fix):

4. **Writer** (Sonnet): `python3 scripts/notes_rewrite.py prep <subject> <loId>`, then read
   `BRIEF.md` and `<loId>.job.md` and nothing else. Write `<loId>.new.json` and run `check`
   until it says applied. Fix each warning or name it as a false alarm. Follow the package's
   "Do not use" lines over the old notes, and never refer to another note.
5. **Verifier** (Haiku, structured `{issues}`): compares `.old.json` with `.new.json`, using the
   job file's package as the source of truth. It reports only real problems: an old fact
   missing or changed (unless the package says not to use it), an unsupported name, date or
   figure, a tip not grounded in the package, or a cross-reference. Edits nothing.
6. **Fixer** (Sonnet, only if there are issues): fixes the real ones, rejects false ones,
   re-runs `check` until it says applied.

Use `pipeline()` with the chapter as the item: stage 1 is package writer → fact-check → fix
for the chapter, then a `parallel()` over that chapter's subsections running 4 → 5 → 6. Note
that `pipeline()` queues every item's first stage before later stages get slots. With ~36
chapters, run **batches of 6–10 chapters per workflow**, so finished subsections land and can be
committed and inspected between batches.

**Pilot first:** run one chapter of each subject alone and read the output yourself: one
package in full, and two rewritten subsections next to their old notes. Check that it reads
well, nothing was lost, the tips come from the package, and the Home Ec legislation is current.
Tighten the prompts if needed, then scale up.

## 4. Finish each subject

1. Rebuild baselines and run the report:
   ```
   for f in content/<subject>/*.json; do lo=$(basename $f .json)
     git show <baseline>:$f | python3 -c "import json,sys;print(json.dumps(json.load(sys.stdin)['notes'],ensure_ascii=False,indent=1))" > drafts/notes-rewrite/<subject>/$lo.old.json
     python3 -c "import json;print(json.dumps(json.load(open('$f'))['notes'],ensure_ascii=False))" > drafts/notes-rewrite/<subject>/$lo.new.json
   done
   python3 scripts/notes_rewrite.py report <subject>
   ```
   Expect every subsection to be "ok" and to have grown. Look into every warning:
   - Lost numbers or terms: is the package's "Do not use" or a no-figures rule the reason? If
     so, it's fine. If not, restore the fact.
   - Over-long bullets: split them.
   - Cross-references: remove them.
   - False alarms ("covered in" meaning physically covered, "see" as an ordinary verb) can stay.
2. Confirm every subsection has a tip (that's how `prep` counts it done) and that none failed
   in the workflow result.
3. Note mismatches outside `notes`. The rewrite changes only the notes array, so `keyTerms` and
   `factCards` can still hold a fact the package now says not to use. List them for the user;
   don't silently change them.
4. `python3 scripts/build_notes.py <subject>` (must report every file valid and every chapter
   complete). Then commit with a message saying what was checked, and push.
5. Check the workflow transcripts for any `Artifact` tool_use calls, and list any to the user so
   they can be deleted.

Report to the user: counts done, what the report flagged and what you did about each, any
fact-card mismatches, and the token use of each run.
