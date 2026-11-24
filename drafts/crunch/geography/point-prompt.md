You are building prerequisite links and learning-cost ratings between individual note points of a Leaving Certificate Geography course (Irish, Higher Level), for a feature that cuts the least valuable points from a student's course.

Read ONLY the package files you are given (1 to 3), one at a time, in order. Each starts with a MODE line, then has:
- TARGET <subsection>: the items you must process, each as `[item-id] text`. Ids ending in `.b` are a block's explanation paragraph; the rest are bullet points.
- CANDIDATES <subsection>: items from other subsections that targets may link to. Do not process these.

For EVERY target item, output:
1. "cost": 1 or 2. 2 = long or complicated: a student would need roughly twice as long to learn it as a short, simple fact (a multi-step process, several names, statistics or case-study facts to remember, or abstract reasoning). 1 = otherwise.
2. "needs": the items (target or candidate) whose content this item directly USES and does not explain itself, e.g. it uses a term, process, landform, map or graph skill, or case-study fact that another item defines or explains.
   - "strength": "essential" (the item can't be understood without it) or "helpful" (easier with it).
   - Link to the ONE item that most directly teaches that idea, not every item that mentions it.
   - Skip chain links: if A needs B and B needs C, don't give A a link to C unless A uses C's content directly.
   - Never link an item to itself. An empty list is fine (most simple definitions need nothing).
   - "why": at most 8 words naming the idea used.
   - "confidence": "high" or "low".

For each package, write ONLY this JSON to its output path, one key per target item in order:
{"geo-rivers-s4.0.b": {"cost": 1, "needs": []}, "geo-rivers-s4.0.0": {"cost": 2, "needs": [{"id": "geo-rivers-s1.0.3", "strength": "essential", "why": "uses the term gradient", "confidence": "high"}]}}
Then check it: it must parse, contain every TARGET id exactly once, and every "id" in needs must appear in the package. Reply with just, per package: item count, link count, how many cost 2 (cost packages only), how many low-confidence.

If you write any helper script, put it ONLY in /Users/gabrielwhelan/barebones/drafts/crunch/geography/tmp/<your subsection id>/ (create it). Other agents run at the same time; never use /tmp or a shared scratchpad, and never run a script you didn't write.
Read every item's FULL text before rating it (use the Read tool on the package). Never shorten or truncate item text when printing it; a cost rating made on a cut-off item is wrong.
"confidence" is about whether the link is REAL, not its strength: a helpful link you are sure of is "high"; an essential link you are unsure of is "low".
Decide EVERY target item explicitly. Never fill items with a default (e.g. "cost 1, no links unless listed"); an unjudged item is an error.
Some packages are one PART of a large subsection: process only the TARGET items in your package, and link to any item in the package.
MODE "cost and links": rate cost and give links, as above. MODE "links only": another package rates cost, so output only {"<id>": {"needs": [...]}} for EVERY target item (an empty list is fine), linking only to items in THIS package. Your packages share the same TARGET items with different candidates; decide links for each package from that package's candidates (and the targets), and don't repeat a link you gave in an earlier package.
