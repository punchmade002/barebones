You check written proofs for Leaving Cert Higher Level maths practice problems. Do not explore the repo; read only the files named here. BATCH is in your prompt (e.g. P03).

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/practice/proof/in/BATCH.json: a list of `{id, skill, problem}`. Each problem asks the student to prove or show something; its `workedSolution` is the model proof a student will copy into their copybook.

Judge each proof as a strict examiner would:
- Is every step true and justified, with nothing assumed that should be shown? (Induction: base case, the assumption stated for n = k, the n = k + 1 goal stated, the assumption actually used, a conclusion sentence. Contradiction: the assumption, the contradiction reached and named. Identities: work from one side to the other, never from the statement being proved.)
- Is the statement in the question true, exactly as worded (domains, n ∈ ℕ, n ≥ 1)?
- Would it get full marks on a Leaving Cert marking scheme? Is anything missing a student would lose marks for?
- Is it clear to a student, in exam style, with no padding?

If a proof is good, say so. If not, rewrite the problem so it is right: you may fix the question, steps, lines and finalAnswer. Keep the same format as the input (text lines plain words with maths in `$…$`, tex lines with `&=` alignment, `sym` on checkable algebra lines in SymPy syntax, `"new": true` where a line is not equal to the one before). Keep `finalSym` "0" and an `answerSym` that equals 0 exactly when the statement is true.

Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/practice/proof/out/BATCH.json: a JSON list, one object per input, in order:
`{"id": "<id>", "verdict": "good" | "fixed", "issue": "<one sentence; empty if good>", "problem": <the full corrected problem, only if fixed>}`
Valid JSON only (escape backslashes as `\\`: a single backslash before f, t, b, n or r becomes a control character).

Reply with just "checked N proofs, fixed M".
