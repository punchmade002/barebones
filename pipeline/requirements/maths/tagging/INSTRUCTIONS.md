Tag Leaving Cert maths exam parts with skill ids. Do not explore the repo; read only the files named here. BATCH is given in your prompt (e.g. b017).

1. Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/tagging/catalog.txt. Each line is `<skill id> [level, chapter] title`.
2. Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/tagging/in/BATCH.json: a list of exam parts, each with `part` (its id), `level`, `chapters` and `solution` (the worked solution).
3. For EVERY part, decide:
   - `primary`: the ONE skill this part mainly tests, i.e. what a student would say they practised. Choose the most specific skill that matches (e.g. `cubic-solve` rather than `quad-solve-formula` when the part solves a cubic).
   - `skills`: every skill the solution actually performs, primary included. Include supporting steps that are real work (solving a quadratic along the way, differentiating, comparing coefficients, using a theorem). Leave out trivial arithmetic (`num-order-operations`, `num-fractions`, `alg-collect-like`) unless the part is mainly about it. Usually 1–6 ids.
   Use only ids that appear exactly in catalog.txt. Never invent an id.
4. Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/tagging/out/BATCH.json containing one JSON object keyed by the exact `part` string:
   {"maths-pp-2015-higher-p1-q1#(a)": {"primary": "seq-geo-nth", "skills": ["seq-geo-nth"]}, ...}
   Every part in the input must appear. Valid JSON only.

Reply with just "done N parts".
