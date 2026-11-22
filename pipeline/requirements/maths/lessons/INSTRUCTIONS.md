You build skill lessons for Leaving Cert maths students. Do not explore the repo; read only the file named here. BATCH is in your prompt (e.g. L07).

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/lessons/in/BATCH.json: a list of skills, each with `skill` and up to 6 `candidates` (real exam parts with their checked worked solution: `steps` of `{title, lines}` where a line is `{"tex": …}` or `{"text": …}`, plus `final`).

For EACH skill write one lesson:

1. **Choose 3 candidates.** Problem 1 is the clearest, most typical example of the skill. Problems 2 and 3 are backups for a student who didn't get it: each should change ONE thing compared with the problem before (a maximum instead of a minimum, a cubic instead of a quadratic, a context instead of bare algebra, decimals…). Avoid two candidates that are the same in every way.
2. **Copy each chosen solution exactly**: same steps, same step titles, same lines in the same order, same `final`. You may NOT reword, add, remove or reorder anything. The only change allowed is wrapping parts of lines in colour marks (step 3).
3. **Colour marks.** Wrap a term in `\hl{n}{…}` (n = 1–4) so the student can follow it from line to line. Give every appearance of the same quantity the same slot, in tex lines, inside `$…$` in text lines, and in `final`. Keep the slot meanings the same across all 3 problems of a skill. Give a short `legend` naming each slot you used, e.g. `{"1": "the slope, f′(x)", "2": "x at the turning point", "3": "y at the turning point", "4": "max or min test"}`. Mark the 2–4 quantities that carry the method, not everything. A mark must wrap a complete term: never split `\frac{…}{…}`, `\sqrt{…}`, `\left( … \right)` or an `&` alignment point, and never put `&` or `\\` inside a mark.
4. **Think-first prompts.** For every step add `ask`: one short question the student answers in their copy before seeing that step. Make it point at the move, not give it away. Good: "What is the slope at a turning point? Use that to find x." Bad: "Set 6x − 6 = 0." Write maths in `ask` and `note` as plain text with Unicode (z₂, x², √3, π, θ) or inside `$…$`; never bare LaTeX like `z_2`, `x^2` or `\sqrt` outside `$…$`.
5. **What's different.** For problems 2 and 3 add `note`: one or two plain sentences saying what changed from the previous problem and what stays the same. Problem 1 has `"note": null`.
6. **Graph (optional).** Only when the part is about a function y = f(x) of one variable that a student would sketch (functions, quadratics, cubics, exponentials, calculus). Otherwise `"graph": null`. Shape:
   `{"f": "3*x**2 - 6*x + 7", "box": [xmin, ymax, xmax, ymin], "tangent": true, "points": [{"x": 1, "y": 4, "name": "min (1, 4)"}], "line": null, "slots": {"x": 2, "y": 3, "line": 4}}`
   - `f` in Python/SymPy syntax (`**`, `exp(x)`, `log(x)`, `sin(x)`, `pi`). Use the exact function from the question.
   - `box` frames the interesting part with a margin; every point must be inside it and on the curve.
   - `tangent: true` only for differentiation skills (a draggable tangent shows the slope).
   - `points`: the key points the solution finds (turning points, roots, intersections), with short names.
   - `line`: two points of a straight line the question uses, or null.
   - `slots`: which colour slot holds the points' x values, y values, and the line (null if unused). Guides appear on the graph only when that slot is first revealed in the steps.

Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/lessons/out/BATCH.json: a JSON list, one object per skill:

```json
[{"skill": "diff-stationary", "problems": [
  {"part": "<candidate part id, exact>", "note": null,
   "legend": {"1": "the slope, f′(x)", "2": "x at the turning point", "3": "y at the turning point", "4": "max or min test"},
   "steps": [
     {"ask": "The question says \"use calculus\". What do you do to f(x) first?", "title": "Differentiate $f(x)$",
      "lines": [{"tex": "f(x) &= 3x^2 - 6x + 7"}, {"tex": "\\hl{1}{f'(x)} &= \\hl{1}{6x - 6}"}]},
     {"ask": "What is the slope at a turning point? Use that to find x.", "title": "Set the derivative equal to 0 to find the turning point",
      "lines": [{"tex": "\\hl{1}{6x - 6} &= \\hl{1}{0}"}, {"tex": "6x &= 6"}, {"tex": "\\hl{2}{x} &= \\hl{2}{1}"}]}
   ],
   "final": "(\\hl{2}{1}, \\hl{3}{4})",
   "graph": {"f": "3*x**2 - 6*x + 7", "box": [-0.9, 16, 2.9, -1.5], "tangent": true,
             "points": [{"x": 1, "y": 4, "name": "min (1, 4)"}], "line": null, "slots": {"x": 2, "y": 3, "line": null}}},
  {"part": "…", "note": "The x² term is negative, so the curve is ∩-shaped and the turning point is a maximum. Same steps.", "…": "…"},
  {"part": "…", "note": "…", "…": "…"}
]}]
```

Every skill in the input must appear, with exactly 3 problems. Valid JSON only (escape backslashes as `\\`). Before writing, re-read each line against the candidate: removing your `\hl{n}{` and its closing `}` must give back the original line exactly.

Reply with just "done N lessons".
