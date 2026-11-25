You are building the subsection-level prerequisite graph for the Leaving Certificate Physical Education course (Irish, Higher Level, written paper), for a feature that cuts the least valuable content from a student's course. This graph is the coarse net: later, individual note points may only link to points in their own subsection or in a subsection it needs here. A missed link here hides every point link under it, so be thorough, but don't link subsections that merely share a theme.

Every student studies all eight chapters below, so links may cross chapters (e.g. a subsection on planning a training programme can need the subsection that teaches the principles of training or fitness components).

Read the WHOLE catalogue file /Users/gabrielwhelan/barebones/drafts/crunch/pe/catalogue.txt, every "covers:" line included. Each entry is `id | chapter | subsection title`, then `covers:` the headings of its note blocks.

Process every subsection id in /Users/gabrielwhelan/barebones/drafts/crunch/pe/batch-1.txt. For each one, list the other subsections whose content it directly USES and does not teach itself: a concept, term, model, theory or method that the other subsection explains (e.g. a subsection on goal setting in training plans uses the subsection that teaches SMART goals).
- "strength": "essential" (can't be understood without it) or "helpful" (easier with it).
- Skip chain links: if A needs B and B needs C, don't give A a link to C unless A uses C directly.
- Never link a subsection to itself or list one twice. An empty list is fine.
- "why": at most 12 words naming the idea used.
- "confidence": whether the link is REAL ("high" or "low"), not its strength.

Write ONLY this JSON to /Users/gabrielwhelan/barebones/drafts/crunch/pe/prereqs-1.json with the Write tool, one key per batch subsection in batch order:
{"pe-planning-optimum-performance-s2": [{"needs": "pe-performance-demands-s1", "strength": "essential", "why": "uses the components of fitness", "confidence": "high"}], "pe-ethics-fair-play-s1": []}
Then check it parses and has every batch id exactly once, with every "needs" id in the batch file. Reply with just: subsection count, link count, how many essential, how many low-confidence.
Decide every subsection explicitly; never fill with a default. Use the Write tool for files, never a shell heredoc. If you write a helper script, put it only in /Users/gabrielwhelan/barebones/drafts/crunch/pe/tmp/ and never run a script you didn't write.
