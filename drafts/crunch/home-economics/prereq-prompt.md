You are building the subsection-level prerequisite graph for the Leaving Certificate Home Economics course (Irish, Higher Level, written paper), for a feature that cuts the least valuable content from a student's course. This graph is the coarse net: later, individual note points may only link to points in their own subsection or in a subsection it needs here. A missed link here hides every point link under it, so be thorough, but don't link subsections that merely share a theme.

Every student studies the Core (syllabus areas 1 to 3) and ONE of three electives, so: a Core subsection may need only Core subsections; an Elective subsection may need Core subsections or subsections of its OWN elective, never another elective. Within those limits links may cross chapters (e.g. a subsection on meal planning for coeliacs uses the subsections that teach gluten and dietary guidelines).

Read the WHOLE catalogue file /Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/catalogue.txt, every "covers:" line included. Each entry is `id | chapter | Core or Elective | subsection title`, then `covers:` the headings of its note blocks.

Process every subsection id in your batch file. For each one, list the other subsections whose content it directly USES and does not teach itself: a nutrient, concept, term, law, process or method that the other subsection explains.
- "strength": "essential" (can't be understood without it) or "helpful" (easier with it).
- Skip chain links: if A needs B and B needs C, don't give A a link to C unless A uses C directly.
- Never link a subsection to itself or list one twice. An empty list is fine.
- "why": at most 12 words naming the idea used.
- "confidence": whether the link is REAL ("high" or "low"), not its strength.

Write ONLY this JSON to your output path with the Write tool, one key per batch subsection in batch order:
{"hom-meal-planning-s3": [{"needs": "hom-proteins-s1", "strength": "helpful", "why": "uses high and low biological value protein", "confidence": "high"}], "hom-marriage-s1": []}
Then check it parses and has every batch id exactly once, with every "needs" id in the catalogue. Reply with just: subsection count, link count, how many essential, how many low-confidence.
Decide every subsection explicitly; never fill with a default. Use the Write tool for files, never a shell heredoc. If you write a helper script, put it only in /Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/tmp/ and never run a script you didn't write.
Files can be longer than one Read returns. After each Read, check you reached the last line of the file; if not, keep reading with offset until you have every line.
