You are building the subsection-level prerequisite graph for a Leaving Certificate Geography course (Irish, Higher Level), for a feature that cuts the least valuable content from a student's course. This graph is the coarse net: later, individual note points may only link to points in their own subsection or in a subsection it needs here. A missed link here hides every point link under it, so be thorough, but don't link subsections that merely share a theme.

Read the WHOLE catalogue, every "covers:" line included (with the Read tool in chunks via offset/limit if it's too big at once): /Users/gabrielwhelan/barebones/drafts/crunch/geography/catalogue.txt
Each entry is `id | chapter | subsection title`, then `covers:` the headings of its note blocks.

You process ONLY the subsection ids listed in your batch file. For each one, list the other subsections (anywhere in the catalogue) whose content it directly USES and does not teach itself: a term, process, landform, skill or case study that the other subsection teaches.
- "strength": "essential" (can't be understood without it) or "helpful" (easier with it).
- Skip chain links: if A needs B and B needs C, don't give A a link to C unless A uses C directly.
- Skills count: a subsection that reads OS maps, aerial photographs or graphs needs the subsection that teaches that skill.
- Never link a subsection to itself or list one twice. An empty list is fine.
- "why": at most 12 words naming the idea used.
- "confidence": whether the link is REAL ("high" or "low"), not its strength.

Write ONLY this JSON to the output path you are given, one key per batch subsection in batch order:
{"geo-rivers-s2": [{"needs": "geo-rivers-s1", "strength": "essential", "why": "uses river terms such as source, tributary, watershed", "confidence": "high"}], "geo-rivers-s1": []}
Then check it parses and has every batch id exactly once, with every "needs" id in the catalogue. Reply with just: subsection count, link count, how many essential, how many low-confidence.
Decide every subsection explicitly; never fill with a default. If you write a helper script, put it only in /Users/gabrielwhelan/barebones/drafts/crunch/geography/tmp/batch-<n>/ and never run a script you didn't write.
