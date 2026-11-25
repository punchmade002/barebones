You write search keywords for pages on a Leaving Cert (Ireland) maths revision site. Each page teaches one maths skill. Do not explore the repo; use only the files named here. BATCH is in your prompt (e.g. K03).

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/keywords/in/BATCH.json: a list of skills, each with `skill`, `title`, `chapter`, `level` (HL = Higher only, JC/OL = on both courses), `input`, `output`, `example`, `what` (a description, with maths in $…$) and `question` (the page's worked example).

For each skill write 20 to 30 keywords: the words and phrases an Irish student would type into a search engine when they need exactly this skill. Include:
- the skill's own names and synonyms ("quadratic formula", "minus b formula", "roots of a quadratic"),
- the method and the terms it uses ("discriminant", "b squared minus 4ac"),
- how students phrase the task ("how to solve a quadratic equation", "find the roots"),
- notation spelled out in words ("x squared", "nCr", "sin squared"), and common exam wording ("show that", "hence find", "verify"),
- one or two that name the Leaving Cert ("leaving cert quadratic formula").
Every keyword must be true of this skill and specific to it; nothing generic ("maths", "revision", "study"), nothing about another skill. Lower case, no LaTeX, no duplicates, each at most 6 words.

Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/keywords/out/BATCH.json: {"<skill id>": ["keyword", ...], ...} with one entry per skill in the batch. Valid JSON only.

Reply with just "wrote N".
