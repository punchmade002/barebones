You review and repair skill lessons for Leaving Cert maths students. Do not explore the repo; read only the files named here. BATCH is in your prompt (e.g. R07).

1. Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/lessons/INSTRUCTIONS.md: the rules a lesson must follow (ignore its file paths and reply line).
2. Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/lessons/review/BATCH.json: a list of lessons, each with `skill`, `lesson` (its 3 problems, each copied from a candidate exam part) and `other_candidates` (exam parts tagged with this skill that the lesson does not use, with their full worked solutions).

How a student uses a lesson: they see problem 1's exam part, try it in their copybook, then reveal the solution one step at a time, answering each step's `ask` first. "Not yet" moves them to problem 2, then 3, each with a `note` saying what changed. `\hl{n}{…}` colours a quantity so it can be followed line to line and on the graph; `legend` names each colour.

The steps, titles and finals are copied from a checked bank and verified by script, so do not judge or change the maths in them. Judge what was added, for each lesson:
- **Fit.** Is each problem mainly this skill, using the same method as problem 1? A problem that is mostly a different skill (a percentage-error step on an integral; a by-hand formula when the skill is the calculator method; plotting points for a geometry theorem) should be swapped for a better one from `other_candidates`. If none fits better, keep it.
- **Backups.** Does each backup change roughly one thing from the problem before? Are problems 2 and 3 different from each other? Reorder or swap if a better sequence exists.
- **Asks.** Each must contain a question, point at the move, and not give away the result, the shape or the answer.
- **Notes.** Accurate about everything that changed, and what stays the same.
- **Colours.** The 2–4 quantities that carry the method are marked. Each slot is one ROLE with the same number and legend wording in all 3 problems; slots run from 1 with no gaps; a given value never sits in the answer's slot. In a text line a mark must sit inside `$…$` (use `$\hl{1}{\text{words}}$` for words).
- **Graph** (if present): the function from the question, sensible box, points on the curve with short names; `tangent: true` only for differentiation skills.

Then write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/lessons/reviewed/BATCH.json: a JSON list with one object per input lesson, in order:
`{"skill": "<id>", "verdict": "good" | "fixed", "issues": "<one line: what you changed, or empty>", "problems": null | [3 problems]}`
- `verdict: "good"` with `"problems": null` when nothing needs changing. Don't rewrite good lessons.
- `verdict: "fixed"` with the full corrected list of 3 problems (same shape as the input `lesson`) when you changed anything. When you bring in a candidate, copy its steps, titles, lines and final EXACTLY, then add only `\hl` marks, an `ask` per step, a `note`, the `legend` and an optional `graph`. Removing your `\hl{n}{` and its `}` must give back each original line exactly.

Valid JSON only (escape backslashes as `\\`). Reply with just "reviewed N lessons, fixed M".
