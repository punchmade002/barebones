You are building the subsection-level prerequisite graph for the Leaving Certificate Chemistry course (Irish, Higher Level, written paper, 2025 specification), for a feature that cuts the least valuable content from a student's course. This graph is the coarse net: later, individual note points may only link to points in their own subsection or in a subsection it needs here. A missed link here hides every point link under it, so be thorough, but don't link subsections that merely share a theme.

Every student studies the whole course, so links may cross chapters (e.g. a subsection on titration calculations uses the subsection that teaches the mole and concentration).

Read the WHOLE catalogue file /Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/catalogue.txt, every "covers:" line included. Each entry is `id | chapter | subsection title`, then `covers:` the headings of its note blocks.

Process every subsection id in your batch file. For each one, list the other subsections whose content it directly USES and does not teach itself: a concept, term, model, law, calculation method or technique that the other subsection explains.
- "strength": "essential" (can't be understood without it) or "helpful" (easier with it).
- Skip chain links: if A needs B and B needs C, don't give A a link to C unless A uses C directly.
- Never link a subsection to itself or list one twice. An empty list is fine.
- "why": at most 12 words naming the idea used.
- "confidence": whether the link is REAL ("high" or "low"), not its strength.

Write ONLY this JSON to your output path with the Write tool, one key per batch subsection in batch order:
{"chem12-s2": [{"needs": "chem8-s1", "strength": "essential", "why": "uses moles and molar mass in titration sums", "confidence": "high"}], "chem1-s1": []}
Then check it parses and has every batch id exactly once, with every "needs" id in the catalogue. Reply with just: subsection count, link count, how many essential, how many low-confidence.
Decide every subsection explicitly; never fill with a default. Use the Write tool for files, never a shell heredoc. If you write a helper script, put it only in /Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/tmp/ and never run a script you didn't write.
Files can be longer than one Read returns. After each Read, check you reached the last line of the file; if not, keep reading with offset until you have every line.
