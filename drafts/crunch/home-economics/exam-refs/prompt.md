You are linking Leaving Certificate Home Economics (Higher Level) exam question parts to the note subsections they test, for a feature that works out which notes earn exam marks.

1. Read the WHOLE catalogue /Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/catalogue.txt, every "covers:" line included. Each entry is `id | chapter | Core or Elective | subsection title`, then `covers:` the headings of its note blocks.
2. Read your batch file. Each QUESTION has PARTs, each with its label, marks, the question (Q) and its model answer (A). "filed under" is the question's chapter, a hint only: parts often test other chapters.
3. For EVERY part, list the subsection ids whose notes a student needs to earn that part's marks: usually 1 or 2, at most 4. Judge by what the model answer says, not just the question's topic words. A part asking to "evaluate" or "discuss" still maps to the subsection that teaches the content. Never leave a part empty: if nothing fits well, give the closest subsection.

Write ONLY this JSON to your output path with the Write tool, one key per question in batch order, one key per part label exactly as printed after PART:
{"homeeconomics-pp-2025-HI-sectiona-carbohydrates-Q1": {"(whole)": ["hom-carbohydrates-s3"]}, "homeeconomics-pp-2008-HI-sectionc-...-Q3": {"3(a)(i)": ["hom-housing-s4", "hom-housing-s1"], "3(a)(ii)": ["hom-housing-s6"]}}
Then check it parses, has every question and part label of the batch, and every id is in the catalogue. Reply with just: question count, part count, average subsections per part.
Files can be longer than one Read returns. After each Read, check you reached the last line of the file; if not, keep reading with offset until you have every line.
Use the Write tool for files, never a shell heredoc. If you write a helper script, put it only in /Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/tmp/ and never run a script you didn't write.
