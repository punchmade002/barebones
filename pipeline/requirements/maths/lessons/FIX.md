You repair skill lessons for Leaving Cert maths students. Do not explore the repo; read only the files named here. BATCH is in your prompt (e.g. F03).

1. Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/lessons/INSTRUCTIONS.md for the rules a lesson must follow (ignore its input/output file paths).
2. Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/lessons/fix/BATCH.json: a list of lessons, each with `skill`, `candidates` (the exam parts allowed), `lesson` (the current 3 problems) and `errors` (what a checker script found wrong).

For each lesson, fix every error and change nothing else that is already right:
- "ask must contain a question": rewrite that `ask` as a question that points at the move without giving it away.
- "LaTeX outside $…$": rewrite with Unicode (z₂, x², √3) or wrap the maths in `$…$`.
- "no \hl marks": add colour marks to that problem, using the same slots and legend as the other problems.
- "talks about the marking scheme": replace that problem with a different candidate (copy its steps exactly, add marks, asks, a note), keeping 3 different problems.
- "changed beyond adding \hl marks" / "title changed" / "final answer changed": copy that line, title or final from the candidate again exactly, then re-add only `\hl{n}{…}` marks.

Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/lessons/fixed/BATCH.json: a JSON list of `{"skill": "<id>", "problems": [3 problems in the same shape as INSTRUCTIONS.md]}`, one per lesson in the input. Valid JSON only (escape backslashes as `\\`).

Reply with just "fixed N lessons".
