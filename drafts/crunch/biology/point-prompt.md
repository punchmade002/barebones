You are building prerequisite links and learning-cost ratings between individual note points of a Leaving Certificate Biology course (Irish, new spec), for a feature that cuts the least valuable points from a student's course.

Read ONLY the package file you are given. It has:
- TARGET <subsection>: the items you must process, each as `[item-id] text`. Ids ending in `.b` are a block's explanation paragraph; the rest are bullet points.
- CANDIDATES <subsection>: items from other subsections that targets may link to. Do not process these.

For EVERY target item, output:
1. "cost": 1 or 2. 2 = long or complicated: a student would need roughly twice as long to learn it as a short, simple fact (a multi-step process, several names or numbers to remember, or abstract reasoning). 1 = otherwise.
2. "needs": the items (target or candidate) whose content this item directly USES and does not explain itself, e.g. it uses a term, structure, molecule or process that another item defines or explains.
   - "strength": "essential" (the item can't be understood without it) or "helpful" (easier with it).
   - Link to the ONE item that most directly teaches that idea, not every item that mentions it.
   - Skip chain links: if A needs B and B needs C, don't give A a link to C unless A uses C's content directly.
   - Never link an item to itself. An empty list is fine (most simple definitions need nothing).
   - "why": at most 8 words naming the idea used.
   - "confidence": "high" or "low".

Write ONLY this JSON to the output path you are given, one key per target item in order:
{"bio15-s1.0.b": {"cost": 1, "needs": []}, "bio15-s1.0.0": {"cost": 2, "needs": [{"id": "bio9-s1.1.2", "strength": "essential", "why": "ATP as energy carrier", "confidence": "high"}]}}
Then check it: it must parse, contain every TARGET id exactly once, and every "id" in needs must appear in the package. Reply with just: item count, link count, how many cost 2, how many low-confidence.
