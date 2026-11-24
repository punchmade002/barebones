You write practice problems for Leaving Cert maths skills that have too few past exam questions. Do not explore the repo; read only the file named here. BATCH is in your prompt (e.g. W07).

Read /Users/gabrielwhelan/barebones/pipeline/requirements/maths/practice/in/BATCH.json: a list of skills. Each has `skill` (id, title, `level` JC/OL/HL, input → output, an example, the smaller skills it `needs`), `write` (how many problems to write) and `references`: up to 2 real exam parts that use the skill, as worked solutions, showing the exam's style and the solution format.

For each skill write exactly `write` problems. They join the skill's real exam parts (`examParts` of them) to make a 3-problem lesson: one main problem, then backups for a student who didn't get it.

**The problems**
- Exam style, like a Leaving Cert part: the same wording, notation and size. `level` is "ordinary" for a JC or OL skill and "higher" for an HL skill. `marks` is 5, 10 or 15, as the exam would give it.
- Each one mainly tests THIS skill, with the same method every time. Earlier skills may appear as steps.
- They must differ from each other and from the references. Change about one thing each time: a negative instead of a positive, a fraction, a different form, a context instead of bare algebra. Not just new numbers.
- Self-contained in words: the student sees only the `question` text, no picture. A geometry problem describes its figure fully, e.g. "A, B and C are points on a circle with centre O. ∠AOC = 110°. Find ∠ABC." For a skill that really needs a figure, add `diagram`: a small clean SVG (viewBox about 0 0 300 220, stroke #1A1916, no fill colour, text in font-family Outfit, labels only).
- Numbers that come out clean, as on the exam. One part per problem, no (i)/(ii).

**Fields** (each problem):
- `question`: the question text. Maths inside `$…$` (KaTeX), never bare LaTeX outside `$…$`. Use `\n` between sentences that belong on separate lines.
- `level`, `marks`.
- `workedSolution`: `{"steps": [{"title": "...", "lines": [...]}], "finalAnswer": "<tex>"}`, the same format as the references. Step titles are short and say what the step does; they may use `$…$`. A line is `{"text": "plain words, maths in $…$"}` or `{"tex": "lhs &= rhs", "sym": "<SymPy>"}`. Use `&=` (or `&\le` etc.) to align the lines of a step. 2–5 steps, every step a real move a student makes.
- `sym` on EVERY tex line that has maths a computer can check, in SymPy syntax: an expression, `Eq(a, b)`, an inequality, an And/Or of those, or a list `[a, b]` of values. Use `**` for powers, `sqrt()`, `pi`, `I` for i, `log` for ln, `exp`. Consecutive `sym` lines in one step must be mathematically equivalent, because a checker tests each against the one before. When a line states something that is not equal to the line before (a derivative, a value substituted, a new equation, the reference angle and then the argument), add `"new": true`. A rounded line gets `"approx": true`.
- `finalSym`: the final answer in SymPy, e.g. `[3, -1]`, `(2, 5)`, `Eq(y, 2*x + 1)`, `sqrt(13)`.
- `answerSym`: the same answer worked out INDEPENDENTLY from the question's givens, in one SymPy expression, e.g. `solve(Eq(3*x**2 - 6*x - 9, 0), x)`, `diff(x**3 - 2*x, x, 2).subs(x, 1)`, `sqrt((5 - 1)**2 + (4 - 1)**2)`, `Abs(3 + 4*I)`. A checker evaluates it and it must equal `finalSym`. It catches a wrong set-up that the line checks can't. One plain expression: no `list(...)`, `[...][0]`, loops or comprehensions (the parser can't read them); `solve(...)`, `div(...)` and `linsolve(...).args[0]` already give lists and tuples.
- `diagram` (optional): SVG string.

**Proof skills** (prove, show that, derive, induction): the problem asks the student to prove a specific statement, in exam style ("Prove by induction that $1 + 3 + 5 + \dots + (2n - 1) = n^2$ for all $n \in \mathbb{N}$."). The worked solution is the proof, step by step, with `sym` on the algebra lines that can be checked (the inductive step's algebra, the expansion in a derivation). Set `finalSym` to `0` and `answerSym` to an expression that equals 0 exactly when the statement is true, e.g. `simplify(summation(2*k - 1, (k, 1, n)) - n**2)`, `simplify(sin(2*x) - 2*sin(x)*cos(x))`, or for divisibility a test case such as `Mod(7**5 - 1, 6)`.

Before writing, solve each problem yourself a second way and make sure `answerSym` really computes the answer from the question, not from your working.

Write /Users/gabrielwhelan/barebones/pipeline/requirements/maths/practice/out/BATCH.json: a JSON list, one object per input skill, in order:
`{"skill": "<id>", "problems": [ {question, level, marks, workedSolution, finalSym, answerSym, diagram?}, ... ]}`

Valid JSON only (escape backslashes as `\\`).

Then run `python3 /Users/gabrielwhelan/barebones/pipeline/requirements/maths/practice.py check BATCH` (with your batch name). It runs the SymPy checks on your file. Fix every problem it lists (usually a missing `"new": true`, a `sym` that doesn't match its tex, or an `answerSym` that doesn't compute the answer) and run it again until it prints "all problems pass". Never change a correct line just to satisfy the checker; fix the `sym` instead.

Reply with just "wrote N problems".
