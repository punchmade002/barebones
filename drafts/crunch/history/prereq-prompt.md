You are building the subsection-level prerequisite graph for a Leaving Certificate History course (Irish, Higher Level, Later Modern field), for a feature that cuts the least valuable content from a student's course. This graph is the coarse net: later, individual note points may only link to points in their own subsection or in a subsection it needs here. A missed link here hides every point link under it, so be thorough, but don't link subsections that merely share a theme or period.

Students study only some topics (e.g. two Irish and two European), and each topic is taught and examined on its own. So link ONLY to subsections in the SAME topic (same id prefix before "-s", e.g. hist-ire3-s5 may only need hist-ire3-s*). Never link across topics.

Read the WHOLE catalogue file you are given, every "covers:" line included. Each entry is `id | topic | subsection title`, then `covers:` the headings of its note blocks.

You process every subsection id in your batch file. For each one, list the other subsections of its topic whose content it directly USES and does not teach itself: a person, event, organisation, policy, term or earlier development that the other subsection explains (e.g. a subsection on the Treaty debates uses the Treaty negotiations).
- "strength": "essential" (can't be understood without it) or "helpful" (easier with it).
- Skip chain links: if A needs B and B needs C, don't give A a link to C unless A uses C directly.
- Never link a subsection to itself or list one twice. An empty list is fine.
- "why": at most 12 words naming the idea used.
- "confidence": whether the link is REAL ("high" or "low"), not its strength.

Write ONLY this JSON to the output path you are given, one key per batch subsection in batch order:
{"hist-ire3-s2": [{"needs": "hist-ire3-s1", "strength": "essential", "why": "uses the Home Rule crisis and the Ulster Volunteers", "confidence": "high"}], "hist-ire3-s1": []}
Then check it parses and has every batch id exactly once, with every "needs" id in the same topic. Reply with just: subsection count, link count, how many essential, how many low-confidence.
Decide every subsection explicitly; never fill with a default. If you write a helper script, put it only in /Users/gabrielwhelan/barebones/drafts/crunch/history/tmp/batch-<n>/ and never run a script you didn't write.
