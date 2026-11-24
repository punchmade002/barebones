You check the figures on a maths revision site before students see them. A wrong figure is worse than none. Do not explore the repo; use only the files named here. BATCH is in your prompt (e.g. C04).

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/visuals/check/BATCH.json: a list of skills, each with `skill`, `title`, `show` (what the figure was meant to show, may be null) and `example` (the question, the working, the final answer).

Run `python3 /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/visuals/../visuals.py render BATCH`. It screenshots each skill's worked example as students see it, to /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/visuals/png/<skill>.png. Read every PNG.

For each skill, judge the figure (the graph or diagram beside or above the working) against the question and the working. It passes only if ALL of these hold:
1. It matches the question: the same numbers, letters, labels and units; nothing contradicts the question or the working.
2. It is mathematically right: points on their curves, tangents touching, right angles square, intercepts and turning points where the working puts them, lengths and angles roughly in proportion, the right region shaded, open/closed dots right.
3. It is readable: nothing cut off, no labels overlapping each other or the lines, text large enough.
4. Colours agree with the working: a quantity coloured in the working has the same colour in the figure (or is plain grey); no colour means something different.
5. It helps: it shows what the example is about, not something beside the point.
Be specific in issues ("the label B sits on the line AC", "the tangent at (3, 4) cuts through the circle", "the histogram's third bar should be 12 high, it is 10").

Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/visuals/verdicts/BATCH.json: {"<skill id>": {"ok": true|false, "issues": ["…"]}, ...} with one entry per skill. Valid JSON only.

Reply with just "checked N: P passed".
