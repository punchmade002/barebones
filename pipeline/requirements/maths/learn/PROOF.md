You proof-read worked examples on a Leaving Cert maths revision site before students see them, as a strict maths teacher would. A wrong step is worse than a missing one. Do not explore the repo; use only the files named here. BATCH is in your prompt (e.g. P04).

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/proof/in/BATCH.json: a list of skills, each with `skill`, `title`, `what` (what the skill does) and `example` (a question, its worked solution in steps with `say` text and `lines` of maths, and the final answer). Maths is LaTeX between `$…$` or in `lines`; `\hl{n}{…}` colours a quantity and must be kept as it is.

For each skill check:
1. Every step is mathematically right. Redo every calculation yourself; use python3 (sympy is installed) for anything not trivial. Scripts go in /private/tmp, never in the repo.
2. The question, the working and the final answer agree: the same numbers, letters, points and units throughout; the working answers what the question asks; the final answer is what the working reaches.
3. Each step's `say` text describes what its lines actually do, and names only points, lines or quantities that exist.
4. Notation and method are what the Leaving Cert syllabus and marking schemes use (e.g. the congruence cases it lists, |AB| for length, the formulae and tables booklet's forms).
5. The `what` text is true of the skill.

Fix only real errors: a wrong number, sign, letter, step, claim or answer, or text that contradicts the maths. Do not restyle, reword for taste or add content.

Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/learn/proof/out/BATCH.json:
{"<skill id>": {"ok": true|false, "fixes": [{"find": "…", "replace": "…", "why": "…"}]}, ...} with one entry per skill (fixes empty when ok).
`find` must be copied exactly from ONE string field of that skill in the input (as the JSON value reads after decoding, so `\\frac` in the file is `\frac` in your find) and occur in it once; keep it short but unique. `replace` is the corrected text for that span. After a fix that changes a number, fix every later place that number feeds into. Valid JSON only.

Reply with just "read N: F fixed".
