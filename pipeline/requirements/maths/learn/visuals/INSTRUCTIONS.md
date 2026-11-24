You draw the figure for a Leaving Cert maths worked example, shown beside the working on the Learn page. Do not explore the repo; use only the files named here. BATCH is in your prompt (e.g. V07).

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/visuals/in/BATCH.json: a list of skills, each with `skill`, `title`, `show` (what the figure should show) and `example` (the question, the steps of the working with their rows of maths, and the final answer).

A skill with `issues` had its figure rejected by a checker for those reasons: draw it again from scratch and fix every one.

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/figlib.py and draw every figure with it, in one Python script per batch (in /private/tmp, never in the repo). Compute every position from the example's own numbers; never place a point by eye.

What a good figure is:
- It shows exactly this question: the same numbers, letters, labels and units as the question and the working. Nothing that contradicts them; nothing the student has to ignore.
- It is correct: points lie on their curves, tangents touch, right angles are right angles (use `equal=True` for anything with circles or angles on a co-ordinate plane), lengths are in proportion, shaded regions are the right ones.
- It is clear and quiet: the few things that matter, labelled once, no clutter, no title, no legend unless two curves need naming. Labels never overlap lines or each other.
- Colour links it to the working: where the working colours a quantity with `\hl{n}{…}`, draw that same quantity in colour n (e.g. the root found in \hl{2}{…} is marked in colour 2). Everything else stays pencil grey.
- Fits the page: about 320 by 240 px (figlib's default), readable at that size.
- A construction shows the finished construction with its arcs; a statistical chart uses the example's actual data; a number line shows the solution set with open or closed dots as the inequality requires.

Save /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/visuals/out/BATCH.json: a JSON object {"<skill id>": "<svg string from Fig.svg()>", ...} with one entry per skill in the batch.

Then run `python3 /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/visuals.py render BATCH`. It screenshots each skill's worked example on the real page with your figure in place, to /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/visuals/png/<skill>.png. Look at every PNG (Read it) next to the question and working, as a strict teacher would. Fix and re-render until each one is right.

Reply with just "drew N figures".
