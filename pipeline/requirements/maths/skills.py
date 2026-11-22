"""Hand-authored Leaving Cert Maths skills (2015 syllabus, examined from 2015).

A skill = one way of treating numbers/objects that turns a given input into a
definite output. Compound skills list the smaller skills they need (prereqs),
so "differentiate e^(2x) sin 3x" decomposes into product + chain + exp + trig.

Row: key | level | syllabus | title | input | output | prereqs (comma) | example
level: JC = Junior Cycle knowledge the syllabus assumes (examinable at OL and HL)
       OL = OL learning outcome (OL is a subset of HL, so HL needs it too)
       HL = HL only
syllabus: topic code in pipeline/resources/maths/spec-syllabus.pdf (1.1-5.2).
Source of scope is the syllabus, not past papers.
"""

import re

SKILLS = []
_chapter = None


def ch(cid):
    global _chapter
    _chapter = cid


def rows(text):
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        c = [x.strip() for x in re.split(r' \|(?= )', line + ' ')]  # spaced pipe only, so |x| moduli survive
        assert len(c) == 8, line
        SKILLS.append(dict(id=c[0], level=c[1], syllabus=c[2], chapter=_chapter, title=c[3],
                           input=c[4], output=c[5],
                           prereqs=[p.strip() for p in c[6].split(',') if p.strip()],
                           example=c[7]))


# ── Number systems & arithmetic foundations (3.1) ─────────────────────────────
ch('maths10')
rows('''
num-order-operations | JC | 3.1 | Apply order of operations | numerical expression with brackets/powers | single value | | 3 + 4 × (2 − 5)² → 39
num-fractions | JC | 3.1 | Operate on fractions | fractions/mixed numbers | simplified fraction | | 2/3 + 5/6 → 3/2
num-ratio-proportion | JC | 3.1 | Use ratio and direct/inverse proportion | quantities in proportion | divided shares or unknown quantity | num-fractions | €120 in ratio 3:5 → €45, €75
num-sets | OL | 3.1 | Classify numbers into N, Z, Q, R, C | a number | its smallest set; place on number line | | √9 ∈ N, √2 ∈ R∖Q
num-decimal-fraction | OL | 3.1 | Convert decimals and fractions | terminating/recurring decimal or fraction | equivalent form | num-fractions | 0.375 → 3/8
num-prime-factors | OL | 3.1 | Express a number as a product of primes | natural number | prime factorisation; HCF/LCM | | 360 → 2³·3²·5
num-surds | OL | 3.1 | Simplify and operate on surds | surd expression | simplified surd, rational denominator | num-prime-factors | √50 → 5√2; 1/(√3−1) → (√3+1)/2
num-sci-notation | OL | 3.1 | Work in scientific notation | numbers in a×10ⁿ form | result in a×10ⁿ, 1 ≤ a < 10 | ind-laws | (3×10⁴)(5×10⁻⁷) → 1.5×10⁻²
''')

# ── Expressions & factorising (4.1) ───────────────────────────────────────────
ch('maths2')
rows('''
alg-evaluate | OL | 4.1 | Evaluate an expression | expression + values of variables | number | num-order-operations | 3x² − 2y at x=2, y=5 → 2
alg-collect-like | JC | 4.1 | Collect like terms | expression | simplified expression | | 3x + 2y − x + 4y → 2x + 6y
alg-expand-single | JC | 4.1 | Expand a bracket by a term | a(bx ± cy ± d) | expanded expression | alg-collect-like | 3(2x − 5) → 6x − 15
alg-expand-binomials | OL | 4.1 | Multiply out two brackets | (x ± y)(w ± z) | expanded, simplified expression | alg-expand-single | (2x + 3)(x − 4) → 2x² − 5x − 12
alg-add-subtract | OL | 4.1 | Add/subtract linear and quadratic expressions | (ax²+bx+c) ± (dx²+ex+f) | simplified expression | alg-expand-single | (2x²−3x+1) − (x²+x−4) → x² − 4x + 5
alg-factor-hcf | JC | 4.1 | Factorise by highest common factor | expression | factor × bracket | | 6x² − 9x → 3x(2x − 3)
alg-factor-grouping | JC | 4.1 | Factorise by grouping | four-term expression | product of two brackets | alg-factor-hcf | ax + ay + bx + by → (a + b)(x + y)
alg-factor-dots | OL | 4.1 | Factorise a difference of two squares | a² − b² | (a − b)(a + b) | | 9x² − 16 → (3x − 4)(3x + 4)
alg-factor-quadratic | OL | 4.1 | Factorise a quadratic trinomial | ax² + bx + c | (px + q)(rx + s) | alg-expand-binomials | 2x² + 7x + 3 → (2x + 1)(x + 3)
alg-factor-cubes | HL | 4.1 | Factorise a sum/difference of two cubes | a³ ± b³ | (a ± b)(a² ∓ ab + b²) | alg-poly-multiply | 8x³ − 27 → (2x − 3)(4x² + 6x + 9)
alg-fractions-add | OL | 4.1 | Add/subtract algebraic fractions | a/(bx+c) ± p/(qx+r) | single fraction | num-fractions, alg-expand-binomials | 2/(x+1) + 3/(x−2) → (5x − 1)/((x+1)(x−2))
alg-fractions-simplify | HL | 4.1 | Multiply, divide and simplify rational expressions | rational algebraic expressions | simplified fraction | alg-fractions-add, alg-factor-quadratic | (x² − 4)/(x² + x − 6) → (x + 2)/(x + 3)
alg-poly-multiply | HL | 4.1 | Multiply polynomials | two polynomials | expanded polynomial | alg-expand-binomials | (x − 1)(x² + x + 1) → x³ − 1
alg-poly-divide | HL | 4.1 | Divide a polynomial by a linear or quadratic | dividend, divisor | quotient (and remainder) | alg-poly-multiply | (x³ − 7x + 6) ÷ (x − 1) → x² + x − 6
alg-surd-expressions | HL | 4.1 | Simplify algebraic expressions with surds | expression with surds and brackets | simplified / rationalised form | num-surds, alg-expand-binomials | (√x + 1)(√x − 1) → x − 1
alg-rearrange | OL | 4.1 | Rearrange a formula | formula + new subject | subject = expression | alg-expand-single, eq-linear | v² = u² + 2as → a = (v² − u²)/(2s)
alg-equate-coefficients | HL | 4.1 | Equate coefficients of identical polynomials | identity with unknown constants | values of the constants | alg-poly-multiply, sim-linear-2 | x² + 6x + c ≡ (x + a)² → a = 3, c = 9
alg-binomial-expand | HL | 4.1 | Expand with the binomial theorem | (a + b)ⁿ, n ∈ N | full expansion | prob-ncr, ind-laws | (1 + 2x)⁴ → 1 + 8x + 24x² + 32x³ + 16x⁴
alg-binomial-term | HL | 4.1 | Find a given term/coefficient of a binomial expansion | (a + b)ⁿ + required power | general term Tᵣ₊₁ and its value | alg-binomial-expand | coefficient of x² in (2 + x)⁵ → 80
''')

# ── Solving equations (4.2) ───────────────────────────────────────────────────
ch('maths6')
rows('''
eq-linear | OL | 4.2 | Solve a linear equation | ax + b = cx + d | x | alg-collect-like | 5x − 3 = 2x + 9 → x = 4
eq-linear-fractions | OL | 4.2 | Solve a linear equation with fractions | equation with numeric denominators | x | eq-linear, num-fractions | x/2 + (x − 1)/3 = 4 → x = 26/5
eq-rational | OL | 4.2 | Solve a/(bx+c) ± p/(qx+r) = e/f | equation with algebraic denominators | x (check denominators ≠ 0) | alg-fractions-add, quad-solve-factor | 1/x + 1/(x+1) = 5/6 → x = 2 or −3/5
eq-rational-hl | HL | 4.2 | Solve (ax+b)/(ex+f) ± (cx+d)/(qx+r) = k | equation with algebraic numerators and denominators | x | eq-rational, quad-solve-formula | (2x+1)/(x−1) − (x+3)/(x+1) = 1 → x = −5
eq-surd | HL | 4.2 | Solve an equation involving a square root | √(f(x)) = g(x) | x, extraneous roots rejected | quad-solve-factor | √(2x + 3) = x → x = 3
eq-word-problem | OL | 4.2 | Form and solve an equation from a context | verbal problem | equation, solution, interpretation | eq-linear, quad-solve-factor | width x, length x+3, area 40 → x = 5
''')

# ── Quadratics (4.2, 5.1) ─────────────────────────────────────────────────────
ch('maths4')
rows('''
quad-solve-factor | OL | 4.2 | Solve a quadratic by factorising | ax² + bx + c = 0 | roots | alg-factor-quadratic | x² − x − 6 = 0 → x = 3, −2
quad-solve-formula | OL | 4.2 | Solve a quadratic with the formula | ax² + bx + c = k (not necessarily factorisable) | exact (surd) or decimal roots | num-surds | x² − 4x − 1 = 0 → x = 2 ± √5
quad-form-from-roots | OL | 4.2 | Form a quadratic from its roots | two whole-number roots | ax² + bx + c = 0 | alg-expand-binomials | roots 3, −2 → x² − x − 6 = 0
quad-discriminant | HL | 4.2 | Use b² − 4ac for the nature of roots | quadratic (possibly with a parameter) | real/equal/complex roots; parameter value | quad-solve-formula | x² + kx + 9 = 0 has equal roots → k = ±6
quad-complete-square | HL | 5.1 | Express a quadratic in completed-square form | ax² + bx + c | a(x + p)² + q | alg-expand-binomials | x² − 6x + 11 → (x − 3)² + 2
quad-complete-square-use | HL | 5.1 | Use completed-square form for roots and turning point | a(x + p)² + q | roots, turning point, sketch | quad-complete-square | (x − 3)² + 2 → min (3, 2), no real roots
''')

# ── Cubics (4.2 HL) ───────────────────────────────────────────────────────────
ch('maths1')
rows('''
cubic-factor-theorem | HL | 4.2 | Test a factor with the Factor Theorem | polynomial f(x) and (x − a) | f(a) = 0 ⇒ factor | alg-evaluate | f(x) = x³ − 7x + 6, f(1) = 0 → (x − 1) is a factor
cubic-find-root | HL | 4.2 | Find an integer root by trial | cubic with integer coefficients | integer root (divisor of constant) | cubic-factor-theorem | x³ − 6x² + 11x − 6 → f(1) = 0
cubic-solve | HL | 4.2 | Solve a cubic with at least one integer root | cubic equation | all roots | cubic-find-root, alg-poly-divide, quad-solve-formula | x³ − 6x² + 11x − 6 = 0 → x = 1, 2, 3
cubic-unknown-coefficient | HL | 4.2 | Find unknown coefficients from given factors | polynomial with unknowns + factor(s) | unknown values | cubic-factor-theorem, sim-linear-2 | (x − 2) is a factor of x³ + kx² − 4x + 12 → k = −3
cubic-form-from-roots | HL | 4.2 | Form a cubic from its roots | three roots | cubic equation | alg-poly-multiply | roots 1, −2, 3 → x³ − 2x² − 5x + 6 = 0
''')

# ── Simultaneous equations (4.2) ──────────────────────────────────────────────
ch('maths5')
rows('''
sim-linear-2 | OL | 4.2 | Solve two linear equations in two unknowns | two linear equations | (x, y) | eq-linear | 2x + y = 7, x − y = 2 → (3, 1)
sim-linear-quadratic | OL | 4.2 | Solve one linear and one order-2 equation | linear (coefficient ±1) + quadratic | intersection points | sim-linear-2, quad-solve-factor | x + y = 5, x² + y² = 13 → (2, 3), (3, 2)
sim-linear-quadratic-hl | HL | 4.2 | Solve linear + order-2 with any coefficients | linear + quadratic in x, y | intersection points | sim-linear-quadratic, quad-solve-formula | 2x + 3y = 7, xy = 2 → (2, 1), (3/2, 4/3)
sim-linear-3 | HL | 4.2 | Solve three linear equations in three unknowns | three linear equations | (x, y, z) | sim-linear-2 | x+y+z=6, 2x−y+z=3, x+2y−z=2 → (1, 2, 3)
sim-word-problem | OL | 4.2 | Form simultaneous equations from a context | verbal problem | equations, solution, interpretation | sim-linear-2 | 3 adults + 2 kids = €34, 2 adults + 3 kids = €31 → €8, €5
''')

# ── Inequalities (4.3) ────────────────────────────────────────────────────────
ch('maths3')
rows('''
ineq-linear | OL | 4.3 | Solve a linear inequality | ax + b ≤ k (and <, >, ≥), domain N/Z/R | solution set on number line | eq-linear | 3 − 2x < 7 → x > −2
ineq-double | OL | 4.3 | Solve a combined (double) linear inequality | k₁ ≤ ax + b < k₂ | interval | ineq-linear | −3 ≤ 2x + 1 < 5 → −2 ≤ x < 2
ineq-quadratic | HL | 4.3 | Solve a quadratic inequality | ax² + bx + c ≤ k | interval(s) | quad-solve-factor, fn-graph-quadratic | x² − x − 6 ≤ 0 → −2 ≤ x ≤ 3
ineq-rational | HL | 4.3 | Solve a rational inequality | (ax + b)/(cx + d) ≤ k | interval(s), excluding x = −d/c | ineq-quadratic | (x + 1)/(x − 2) < 2 → x < 2 or x > 5
ineq-modulus | HL | 4.3 | Solve modulus inequalities | |x − a| < b, |x − a| > b and combinations | interval(s) | ineq-double, ineq-quadratic | |x − 3| < 2 → 1 < x < 5
ineq-prove | HL | 4.3 | Prove an algebraic inequality | inequality in a, b | proof via a square ≥ 0 | alg-expand-binomials | (a + b)² ≥ 4ab ⇐ (a − b)² ≥ 0
''')

# ── Indices & logs (3.2) ──────────────────────────────────────────────────────
ch('maths17')
rows('''
ind-laws | OL | 3.2 | Apply the laws of indices | expression with powers | simplified power | | a³·a⁵ / a² → a⁶
ind-negative-fractional | OL | 3.2 | Evaluate negative and fractional indices | a^(−p/q) | value or root form | ind-laws | 8^(−2/3) → 1/4
ind-express-as-power | OL | 3.2 | Write an expression as a power of a base | expression with roots/fractions | base^k | ind-negative-fractional | √8 / 4 → 2^(−1/2)
ind-solve-equation | OL | 3.2 | Solve an exponential equation with a common base | aᶠ⁽ˣ⁾ = aᵍ⁽ˣ⁾ | x | ind-express-as-power, eq-linear | 4ˣ = 8^(x − 1) → x = 3
ind-hidden-quadratic | HL | 3.2 | Solve an exponential equation reducible to a quadratic | a^(2x) + b·aˣ + c = 0 | x | ind-laws, quad-solve-factor | 2^(2x) − 6·2ˣ + 8 = 0 → x = 1, 2
log-definition | HL | 3.2 | Convert between log and index form (incl. e and ln) | log or exponential statement | equivalent form / value | ind-laws | log₂ 8 = 3 ⇔ 2³ = 8; eˣ = 5 ⇔ x = ln 5
log-laws | HL | 3.2 | Apply the laws of logs | log expression | single log or value | log-definition | log₂ 12 − log₂ 3 → 2
log-change-base | HL | 3.2 | Change the base of a log | logₐ x | log_b x / log_b a | log-laws | log₄ 8 → 3/2
log-solve | HL | 3.2 | Solve a log equation | equation in logs | x (reject invalid arguments) | log-laws, quad-solve-factor | log₂(x + 2) + log₂ x = 3 → x = 2
log-solve-exponential | HL | 3.2 | Solve aˣ = b by taking logs | aˣ = b | x | log-laws | 3ˣ = 20 → x = ln 20 / ln 3 ≈ 2.727
''')

# ── Sequences & series (3.1) ──────────────────────────────────────────────────
ch('maths21')
rows('''
seq-pattern | OL | 3.1 | Continue and generalise a pattern | terms or diagrams of a pattern | next terms; nth term in algebraic form | | 1, 4, 9, 16 → 25, Tₙ = n²
seq-classify | OL | 3.1 | Decide if a sequence is arithmetic, geometric or neither | list of terms | type with reason (differences/ratios) | seq-pattern | 3, 6, 12 → geometric, r = 2
seq-quadratic | OL | 3.1 | Find the nth term of a quadratic sequence | terms with constant second difference | Tₙ = an² + bn + c | seq-classify, sim-linear-2 | 2, 7, 14, 23 → n² + 2n − 1
seq-arith-nth | OL | 3.1 | Find the nth term of an arithmetic sequence | a, d (or terms) | Tₙ = a + (n − 1)d | seq-classify | 5, 8, 11 → Tₙ = 3n + 2, T₂₀ = 62
seq-arith-find-ad | OL | 3.1 | Find a and d from given terms or sums | two facts about the sequence | a, d | seq-arith-nth, sim-linear-2 | T₃ = 11, T₇ = 23 → a = 5, d = 3
seq-arith-sum | OL | 3.1 | Sum n terms of an arithmetic series | a, d, n | Sₙ = n/2 [2a + (n − 1)d] | seq-arith-nth | 5 + 8 + … to 20 terms → 670
seq-sigma | HL | 3.1 | Evaluate a series in Σ notation | Σ expression | value | seq-arith-sum | Σ_{r=1}^{10} (2r + 1) → 120
seq-geo-nth | HL | 3.1 | Find the nth term of a geometric sequence | a, r (or terms) | Tₙ = arⁿ⁻¹ | seq-classify, ind-laws | 3, 6, 12 → Tₙ = 3·2ⁿ⁻¹
seq-geo-sum | HL | 3.1 | Sum n terms of a geometric series | a, r, n | Sₙ = a(1 − rⁿ)/(1 − r) | seq-geo-nth | 3 + 6 + … to 6 terms → 189
seq-geo-unknown-n | HL | 3.1 | Find the number of terms needed in a geometric series | a, r, target term/sum | n via logs | seq-geo-sum, log-solve-exponential | 2ⁿ⁻¹ > 1000 → n = 11
seq-limits | HL | 3.1 | Find limits of sequences by inspection and limit rules | sequence | limit | | lim n/(n + 1) → 1; lim rⁿ (|r| < 1) → 0
seq-geo-sum-infinity | HL | 3.1 | Sum an infinite geometric series | a, r with |r| < 1 | S∞ = a/(1 − r) | seq-geo-sum, seq-limits | 8 + 4 + 2 + … → 16
seq-derive-sum-infinity | HL | 3.1 | Derive S∞ as the limit of partial sums | Sₙ formula | S∞ = a/(1 − r) | seq-geo-sum-infinity | lim a(1 − rⁿ)/(1 − r) = a/(1 − r)
seq-convergence-range | HL | 3.1 | Find values of x for which a geometric series converges | series with r in terms of x | interval of x | seq-geo-sum-infinity, ineq-modulus | Σ (2x)ⁿ → −½ < x < ½
seq-recurring-decimal | HL | 3.1 | Write a recurring decimal as a fraction | recurring decimal | fraction via S∞ | seq-geo-sum-infinity | 0.454545… → 5/11
seq-verify-formula | HL | 3.1 | Verify and justify a formula from a number pattern | pattern + proposed formula | checked/justified formula | seq-pattern | 1 + 3 + 5 + … + (2n − 1) = n²
''')

# ── Induction & proof (3.1 HL) ────────────────────────────────────────────────
ch('maths18')
rows('''
induction-sum | HL | 3.1 | Prove a series identity by induction | Σ identity | proof (base case, assume k, prove k + 1) | alg-expand-binomials | 1 + 2 + … + n = n(n + 1)/2
induction-geo-sum | HL | 3.1 | Prove the finite geometric series sum by induction | a + ar + … + arⁿ⁻¹ | proof | induction-sum, seq-geo-sum | Sₙ = a(1 − rⁿ)/(1 − r)
induction-divisibility | HL | 3.1 | Prove a divisibility result by induction | statement "d divides f(n)" | proof | induction-sum, ind-laws | 3 divides 4ⁿ − 1
induction-inequality | HL | 3.1 | Prove an inequality by induction | inequality in n with starting value | proof | induction-sum, ineq-linear | n! > 2ⁿ (n ≥ 4); (1 + x)ⁿ ≥ 1 + nx
proof-root2-irrational | HL | 3.1 | Prove √2 is irrational by contradiction | assumption √2 = p/q in lowest terms | contradiction | logic-terms-hl, num-prime-factors | p² = 2q² ⇒ p, q both even
''')

# ── Complex numbers (3.1, 4.4) ────────────────────────────────────────────────
ch('maths10')
rows('''
cx-arithmetic | OL | 3.1 | Add, subtract and multiply complex numbers | a + bi, c + di | result in a + bi form | alg-expand-binomials | (2 + 3i)(1 − i) → 5 + i
cx-powers-i | OL | 3.1 | Simplify powers of i | iⁿ | 1, i, −1 or −i | ind-laws | i⁷ → −i
cx-conjugate | OL | 3.1 | Find the conjugate | z = a + bi | z̄ = a − bi | | 3 − 4i → 3 + 4i
cx-divide | OL | 3.1 | Divide complex numbers | z₁ / z₂ | a + bi via conjugate of denominator | cx-arithmetic, cx-conjugate | (3 + 4i)/(1 − 2i) → −1 + 2i
cx-argand | OL | 3.1 | Plot complex numbers on an Argand diagram | z | point (Re, Im) | | 3 − 2i → (3, −2)
cx-modulus | OL | 3.1 | Find the modulus as distance from the origin | z = a + bi | |z| = √(a² + b²) | cx-argand, geo-thm14 | |3 − 4i| → 5
cx-equate-parts | OL | 3.1 | Equate real and imaginary parts | equation in complex numbers with unknowns | values of unknowns | cx-arithmetic, sim-linear-2 | a + bi = (2 + i)² → a = 3, b = 4
cx-transformations | OL | 3.1 | Interpret operations as transformations on the Argand diagram | z and an operation (+w, ×i, ×k) | translation / rotation / enlargement | cx-argand | ×i → rotation 90° anticlockwise
cx-conjugate-properties | HL | 3.1 | Use conjugates of sums and products | z₁, z₂ | conj(z₁ + z₂) = z̄₁ + z̄₂, conj(z₁z₂) = z̄₁z̄₂ | cx-conjugate, cx-arithmetic | verify for 1 + i, 2 − 3i
cx-quadratic | HL | 4.4 | Solve a quadratic with complex roots | quadratic with b² − 4ac < 0 | conjugate pair of roots | quad-solve-formula, cx-powers-i | z² − 4z + 13 = 0 → 2 ± 3i
cx-conjugate-root | HL | 4.4 | Use the Conjugate Root Theorem to find all roots | real polynomial + one complex root | all roots | cx-quadratic, alg-poly-divide | 1 + i is a root of z³ − 4z² + 6z − 4 → 1 ± i, 2
cx-polar | HL | 4.4 | Convert between rectangular and polar form | a + bi | r(cos θ + i sin θ), θ in correct quadrant | cx-modulus, trig-unit-circle, trig-radians | 1 + i√3 → 2(cos π/3 + i sin π/3)
cx-polar-multiply | HL | 4.4 | Multiply and divide in polar form | two numbers in polar form | product/quotient (multiply moduli, add arguments) | cx-polar, trig-compound | 2 cis(π/6) × 3 cis(π/3) → 6 cis(π/2) = 6i
cx-de-moivre-power | HL | 4.4 | Raise to a power with De Moivre's Theorem | zⁿ | rⁿ(cos nθ + i sin nθ) → a + bi | cx-polar | (1 + i)⁸ → 16
cx-de-moivre-roots | HL | 4.4 | Solve zⁿ = a (incl. nth roots of unity) | zⁿ = a | n roots in polar and rectangular form | cx-de-moivre-power, trig-solve-general | z³ = 8 → 2, −1 ± i√3
cx-de-moivre-identity | HL | 4.4 | Derive multiple-angle identities with De Moivre | cos nθ or sin nθ | identity in powers of cos θ / sin θ | cx-de-moivre-power, alg-binomial-expand, trig-pythag-identity | cos 3θ = 4cos³θ − 3cos θ
cx-de-moivre-prove | HL | 4.4 | Prove De Moivre's Theorem by induction | (cos θ + i sin θ)ⁿ, n ∈ N | proof | induction-sum, trig-compound, cx-arithmetic | P(k) ⇒ P(k + 1) using sin(A + B), cos(A + B)
''')

# ── Functions (5.1) ───────────────────────────────────────────────────────────
ch('maths14')
rows('''
fn-definition | OL | 5.1 | Recognise a function and its domain/codomain/range | mapping, rule or graph | is/isn't a function, domain, range | | {(1,2),(1,3)} → not a function
fn-evaluate | OL | 5.1 | Evaluate a function | f(x) + input value or expression | output | alg-evaluate | f(x) = 2x² − 3, f(−2) → 5
fn-composite | OL | 5.1 | Form a composite function | f(x), g(x) | f(g(x)) | fn-evaluate, alg-expand-binomials | f = 2x + 1, g = x² → f(g(x)) = 2x² + 1
fn-graph-linear | OL | 5.1 | Graph a linear function | ax + b, domain | straight-line graph | fn-evaluate | y = 2x − 1
fn-graph-quadratic | OL | 5.1 | Graph a quadratic function | ax² + bx + c, domain | parabola with roots, vertex, y-intercept | fn-evaluate, quad-solve-factor | y = x² − 2x − 3 → roots −1, 3, min (1, −4)
fn-graph-cubic | OL | 5.1 | Graph a cubic function | ax³ + bx² + cx + d, domain | cubic curve | fn-evaluate | y = x³ − 3x
fn-graph-exponential | OL | 5.1 | Graph an exponential function | a·bˣ (and eˣ at HL) | exponential curve | fn-evaluate, ind-negative-fractional | y = 3·2ˣ
fn-graph-log | HL | 5.1 | Graph a logarithmic function | logₐ x or ln x | log curve (reflection of aˣ in y = x) | log-definition, fn-inverse-sketch | y = log₂ x
fn-solve-graphically | OL | 5.1 | Solve equations approximately from graphs | graphs of f and g | x where f(x) = 0, f(x) = k, f(x) = g(x) | fn-graph-quadratic | x² − 2x − 3 = 2 → x ≈ −1.4, 3.4
fn-compare-graphs | OL | 5.1 | Interpret f(x) = g(x) as a comparison of functions | two functions/graphs | intersections, regions where f > g | fn-solve-graphically | 2ˣ vs x² → equal at x = 2, 4 and x ≈ −0.77
fn-transformations | HL | 5.1 | Transform a graph | f(x) and f(x) + k, f(x + h), kf(x) | transformed graph / equation | fn-evaluate | y = f(x − 2) + 1 → shift right 2, up 1
fn-injective-surjective | HL | 5.1 | Classify a function as injective, surjective, bijective | function with domain and codomain | classification with reason | fn-definition | f(x) = x², R → R → neither
fn-inverse | HL | 5.1 | Find the inverse of a bijective function | y = f(x) | f⁻¹(x) | fn-injective-surjective, alg-rearrange | f(x) = (2x − 1)/3 → f⁻¹(x) = (3x + 1)/2
fn-inverse-sketch | HL | 5.1 | Sketch the inverse from a graph | graph of f | reflection in y = x | fn-inverse | eˣ → ln x
fn-limit-concept | OL | 5.1 | Investigate the limit of a function | f(x) near x = a (table/graph) | limiting value | fn-evaluate | f(x) = 2x + 1 as x → 3 → 7
fn-limits-continuity | HL | 5.1 | Find limits and explore continuity informally | f(x), point a | lim f(x), continuous or not | fn-limit-concept, alg-factor-quadratic | lim_{x→2} (x² − 4)/(x − 2) → 4
fn-exp-model | HL | 5.1 | Fit an exponential model to data | A·e^(kt) or a·bˣ + two data points | A, k (or a, b); prediction | log-solve-exponential | N(0) = 50, N(3) = 200 → k = ln 4 / 3 ≈ 0.462
''')

# ── Differentiation rules (5.2) ───────────────────────────────────────────────
ch('maths12')
rows('''
diff-first-principles | HL | 5.2 | Differentiate from first principles | linear or quadratic f(x) | f′(x) via lim [f(x + h) − f(x)]/h | fn-limits-continuity, alg-expand-binomials | x² − 3x → 2x − 3
diff-poly | OL | 5.2 | Differentiate a polynomial by rule | linear, quadratic or cubic (any polynomial at HL) | f′(x) | ind-laws | 2x³ − 5x² + 4 → 6x² − 10x
diff-second | OL | 5.2 | Find the second derivative | f(x) | f″(x) | diff-poly | x³ − 3x → 6x
diff-rational-power | HL | 5.2 | Differentiate rational powers | xⁿ, n ∈ Q (roots, reciprocals) | nxⁿ⁻¹ | diff-poly, ind-express-as-power | √x → 1/(2√x); 1/x² → −2/x³
diff-exponential | HL | 5.2 | Differentiate exponential functions | e^(ax), aˣ | ae^(ax), aˣ ln a | diff-poly, log-definition | e^(3x) → 3e^(3x)
diff-log | HL | 5.2 | Differentiate logarithms | ln x, ln f(x) | 1/x, f′(x)/f(x) | diff-chain | ln(x² + 1) → 2x/(x² + 1)
diff-trig | HL | 5.2 | Differentiate trig functions (radians) | sin ax, cos ax, tan ax | derivative | trig-radians, trig-unit-circle | sin 4x → 4 cos 4x; tan x → sec² x
diff-inverse-trig | HL | 5.2 | Differentiate inverse trig functions | sin⁻¹(x/a), tan⁻¹(x/a) | 1/√(a² − x²), a/(a² + x²) | diff-chain | tan⁻¹(x/2) → 2/(4 + x²)
diff-product | HL | 5.2 | Apply the product rule | u·v | u′v + uv′ | diff-poly | x² sin x → 2x sin x + x² cos x
diff-quotient | HL | 5.2 | Apply the quotient rule | u/v | (u′v − uv′)/v² | diff-poly, alg-fractions-simplify | x/(x + 1) → 1/(x + 1)²
diff-chain | HL | 5.2 | Apply the chain rule | f(g(x)) | f′(g(x))·g′(x) | diff-poly, fn-composite | (3x² + 1)⁵ → 30x(3x² + 1)⁴
diff-combined | HL | 5.2 | Differentiate a function needing several rules | product/quotient of composites of exp, log, trig, powers | simplified derivative | diff-product, diff-quotient, diff-chain, diff-exponential, diff-trig, diff-log | e^(2x) sin 3x → e^(2x)(2 sin 3x + 3 cos 3x)
diff-show-identity | HL | 5.2 | Show a derivative satisfies a given relation | y = f(x) + relation in y, y′, y″ | verified identity | diff-combined, diff-second | y = e^(2x) → y″ − 4y = 0
''')

# ── Differentiation applications (5.2) ────────────────────────────────────────
ch('maths11')
rows('''
diff-slope-tangent | OL | 5.2 | Find the slope and equation of a tangent | f(x) and a point | slope f′(a); tangent line | diff-poly, line-equation | y = x² − 3x at x = 1 → y = −x − 1
diff-point-given-slope | OL | 5.2 | Find where a curve has a given slope | f(x) and slope m (or parallel line) | x (and point) | diff-poly, eq-linear, quad-solve-factor | y = x² − 3x, slope 1 → (2, −2)
diff-increasing | OL | 5.2 | Decide whether a function is increasing or decreasing at a point | f(x) + x value | sign of f′(a) | diff-poly | f = x² − 4x at x = 1 → f′ = −2 < 0, decreasing
diff-increasing-interval | HL | 5.2 | Find where a function is increasing/decreasing for all x or on intervals | f(x) | intervals where f′ > 0 / f′ < 0 | diff-increasing, ineq-quadratic | x³ + 3x increasing for all x (f′ = 3x² + 3 > 0)
diff-stationary | OL | 5.2 | Find and classify turning points | f(x) | max/min points via f′ = 0 and f″ | diff-second, quad-solve-factor, fn-evaluate | x³ − 3x → max (−1, 2), min (1, −2)
diff-inflection | HL | 5.2 | Find a point of inflection | f(x) | point where f″ = 0 and changes sign | diff-second, eq-linear | x³ − 6x² → (2, −16)
diff-curve-sketch | OL | 5.2 | Sketch a curve using calculus | f(x) | sketch with intercepts, turning points | diff-stationary, fn-graph-cubic | y = x³ − 3x
diff-sketch-derivative | HL | 5.2 | Sketch/match the graph of f′ from f | graph of f | graph of f′ (and vice versa) | diff-stationary, diff-increasing-interval | turning points of f ↔ roots of f′
diff-rates-of-change | OL | 5.2 | Apply differentiation to rates of change | quantity as a function of time | rate, velocity, acceleration at a time | diff-poly, diff-second | s = t³ − 6t² → v = 3t² − 12t, a = 6t − 12
diff-related-rates | HL | 5.2 | Solve connected rates of change | formula linking variables + one known rate | unknown rate via chain rule | diff-chain, mens-volume | V = 4/3 πr³, dr/dt = 0.5 at r = 3 → dV/dt = 18π
diff-optimisation | OL | 5.2 | Solve a max/min problem from a context | verbal problem with a constraint | optimal value and the quantity achieving it | diff-stationary, alg-rearrange, mens-perimeter-area | rectangle perimeter 40 → max area 100 at 10 × 10
diff-tangent-circle | HL | 5.2 | Find the slope of a tangent to a circle by differentiation | circle equation + point | slope dy/dx | diff-chain, circ-eq-origin | x² + y² = 25 at (3, 4) → −3/4
diff-apply-hl | HL | 5.2 | Apply derivatives of exp/log/trig functions to problems | context with non-polynomial model | rate, max/min, tangent | diff-combined, diff-stationary | T = 80e^(−0.1t) → rate at t = 5 ≈ −4.85
''')

# ── Integration (5.2 HL) ──────────────────────────────────────────────────────
ch('maths19')
rows('''
int-reverse | HL | 5.2 | Treat integration as reverse differentiation | f(x) | F(x) + c with F′ = f | diff-poly | d/dx(x³) = 3x² → ∫3x² dx = x³ + c
int-power | HL | 5.2 | Integrate powers, sums and constant multiples | Σ kxᵃ, a ∈ Q | antiderivative + c | int-reverse, ind-express-as-power | ∫(3x² − 4x) dx → x³ − 2x² + c; ∫√x dx → ⅔x^(3/2) + c
int-reciprocal | HL | 5.2 | Integrate 1/x | 1/x | ln|x| + c | int-reverse, log-definition | ∫(2/x) dx → 2 ln|x| + c
int-exponential | HL | 5.2 | Integrate exponentials | e^(ax), aˣ | (1/a)e^(ax) + c, aˣ/ln a + c | int-reverse, diff-exponential | ∫e^(2x) dx → ½e^(2x) + c
int-trig | HL | 5.2 | Integrate sin ax and cos ax | sin ax, cos ax | −(1/a)cos ax + c, (1/a)sin ax + c | int-reverse, diff-trig | ∫sin 3x dx → −⅓cos 3x + c
int-trig-identity | HL | 5.2 | Integrate using a trig formula | sin²x, cos²x, sin A cos B, … | antiderivative + c | int-trig, trig-double, trig-products-sums | ∫sin²x dx → ½x − ¼sin 2x + c
int-definite | HL | 5.2 | Evaluate a definite integral | ∫ₐᵇ f(x) dx | number | int-power, int-exponential, int-trig | ∫₀² 3x² dx → 8
int-find-function | HL | 5.2 | Find a function from its derivative and a point | f′(x) + a value of f | f(x) with c found | int-power, eq-linear | f′(x) = 6x, f(1) = 5 → f(x) = 3x² + 2
int-area-axis | HL | 5.2 | Find the area between a curve and the x-axis | curve, limits (or roots) | area (parts below axis taken positive) | int-definite, quad-solve-factor | y = 4 − x², x-axis → 32/3
int-area-between | HL | 5.2 | Find the area between two curves | two curves | area via ∫(top − bottom) | int-area-axis, sim-linear-quadratic | y = 2x and y = x² → 4/3
int-average-value | HL | 5.2 | Find the average value of a function on an interval | f(x), [a, b] | (1/(b − a))∫ₐᵇ f | int-definite | x² on [0, 3] → 3
''')

# ── Financial maths & applied arithmetic (3.3) ────────────────────────────────
ch('maths13')
rows('''
fin-percentages | JC | 3.3 | Calculate percentages and percentage change | quantities | %, % increase/decrease, original amount | num-fractions | €80 → €92 → 15% increase
fin-profit-margin | OL | 3.3 | Calculate cost/selling price, discount, mark-up and margin | prices | profit, mark-up (% of CP), margin (% of SP) | fin-percentages | CP €80, SP €100 → mark-up 25%, margin 20%
fin-compound-interest | OL | 3.3 | Apply compound interest | P, i, t | F = P(1 + i)ᵗ | fin-percentages, ind-laws | €5,000 at 3% for 4 years → €5,627.54
fin-depreciation | OL | 3.3 | Apply reducing-balance depreciation | P, i, t | F = P(1 − i)ᵗ | fin-compound-interest | €20,000 at 15% for 3 years → €12,282.50
fin-rate-conversion | OL | 3.3 | Convert between annual and periodic rates (AER/APR) | annual rate | equivalent monthly/weekly rate | fin-compound-interest, ind-negative-fractional | 5% AER → 0.4074% per month
fin-solve-rate-time | HL | 3.3 | Find the rate or time in a compound interest problem | P, F and t (or i) | i via roots, t via logs | fin-compound-interest, log-solve-exponential | €1,000 → €2,000 at 4% → t ≈ 17.7 years
fin-income-tax | OL | 3.3 | Calculate income tax, USC, PRSI and net pay | gross pay, rates, bands, credits, deductions | gross tax, net tax, net pay | fin-percentages | €50,000, SRCOP €42,000 at 20%/40%, credits €3,750 → tax €7,850
fin-costing | OL | 3.3 | Cost materials, labour and wastage | job specification | total cost | fin-percentages | 12 m² at €25 + 10% wastage + 3 h at €40 → €450
fin-units | OL | 3.3 | Change units (metric, imperial with factors, currency) | quantity + conversion factor | converted quantity | num-ratio-proportion | 60 mph, 1 mile = 1.609 km → 96.5 km/h
fin-error | OL | 3.3 | Calculate percentage error, tolerance and accumulated error | true/estimated values or limits | % error, range of values | fin-percentages | estimate 9.8, true 10 → 2% error
fin-estimate | OL | 3.3 | Estimate, round and check order of magnitude | calculation | estimate, rounded result, sense check | num-sci-notation | 49.7 × 0.21 ≈ 50 × 0.2 = 10
fin-average-rate | OL | 3.3 | Calculate an average rate of change over time | change in quantity, time | rate | num-ratio-proportion | 180 km in 2.5 h → 72 km/h
fin-present-value | HL | 3.3 | Find the present value of a future sum | F, i, t | P = F/(1 + i)ᵗ | fin-compound-interest | €5,000 in 3 years at 4% → €4,444.98
fin-annuity-fv | HL | 3.3 | Find the future value of regular savings | payment, i, number of payments | sum of a geometric series | fin-compound-interest, seq-geo-sum | €100/month for 12 months at 0.5%/month → €1,233.56
fin-annuity-pv | HL | 3.3 | Find the present value of a series of payments (pension/annuity) | payment, i, n | sum of present values | fin-present-value, seq-geo-sum | value now of €1,000/year for 10 years
fin-mortgage | HL | 3.3 | Find the repayment on a loan/mortgage | P, i, t | A = P i(1 + i)ᵗ / ((1 + i)ᵗ − 1) | fin-annuity-pv, fin-rate-conversion | €10,000 at 1%/month for 12 months → €888.49
fin-mortgage-derive | HL | 3.3 | Derive the mortgage repayment formula | loan = sum of PVs of repayments | formula | fin-mortgage, seq-geo-sum | P = A/(1 + i) + … + A/(1 + i)ᵗ ⇒ formula
fin-amortisation | HL | 3.3 | Build or complete a loan amortisation schedule | loan, rate, repayment | interest, capital repaid, balance each period | fin-mortgage | balance after one €888.49 repayment → €9,211.51
''')

# ── Length, area & volume (3.4, arc/sector 2.3) ───────────────────────────────
ch('maths7')
rows('''
mens-perimeter-area | OL | 3.4 | Find perimeter and area of plane figures | disc, triangle, rectangle, square, parallelogram, trapezium, sector, combinations | perimeter, area | | trapezium a = 4, b = 6, h = 3 → 15
mens-arc-sector | OL | 2.3 | Find arc length and sector area | r, angle (degrees or radians) | arc length, sector area | mens-perimeter-area | r = 6, θ = π/3 → arc 2π, area 6π
mens-nets | OL | 3.4 | Draw and interpret nets of prisms, cylinders and cones | solid | net and its dimensions | mens-perimeter-area | cylinder → two discs + rectangle 2πr × h
mens-surface-area | OL | 3.4 | Find surface area of solids | block, cylinder, cone, triangular prism, sphere, hemisphere | surface area | mens-perimeter-area, geo-thm14 | cone r = 3, h = 4 → l = 5, curved SA 15π
mens-volume | OL | 3.4 | Find volume of solids | block, cylinder, cone, triangular prism, sphere, hemisphere | volume | mens-perimeter-area | sphere r = 3 → 36π
mens-composite | OL | 3.4 | Find area/volume of compound solids | solid made of several shapes | total surface area/volume | mens-surface-area, mens-volume | cylinder r = 3, h = 10 + hemisphere → 108π
mens-equate-volumes | OL | 3.4 | Solve recasting, displacement and flow problems | equal-volume situation | unknown dimension or time | mens-volume, eq-linear | sphere r = 3 recast as cylinder r = 2 → h = 9
mens-trapezoidal | OL | 3.4 | Approximate area with the trapezoidal rule | strip width h, heights y₁…yₙ | h/2[(y₁ + yₙ) + 2(y₂ + … + yₙ₋₁)] | mens-perimeter-area | h = 2; 3, 5, 6, 4 → 29
''')

# ── Co-ordinate geometry of the line (2.2) ────────────────────────────────────
ch('maths9')
rows('''
line-distance | JC | 2.2 | Find the distance between two points | (x₁, y₁), (x₂, y₂) | √((x₂ − x₁)² + (y₂ − y₁)²) | geo-thm14 | (1, 2), (4, 6) → 5
line-midpoint | JC | 2.2 | Find the midpoint of a segment | two points | ((x₁ + x₂)/2, (y₁ + y₂)/2) | | (2, 3), (6, 7) → (4, 5)
line-slope | JC | 2.2 | Find the slope from two points or an equation | two points, or ax + by + c = 0 | m | | (1, 2), (3, 8) → 3; 2x + 3y = 6 → −2/3
line-equation | JC | 2.2 | Find the equation of a line | point + slope (or two points) | y − y₁ = m(x − x₁) → ax + by + c = 0 | line-slope | (1, 2), m = 3 → 3x − y − 1 = 0
line-point-on | OL | 2.2 | Test whether a point is on a line; find intercepts | line + point | yes/no; axis intercepts | alg-evaluate | 3x − y − 1 = 0 cuts x-axis at (1/3, 0)
line-intersection | OL | 2.2 | Find where two lines intersect | two line equations | point | sim-linear-2 | x + y = 5, x − y = 1 → (3, 2)
line-parallel-perp | OL | 2.2 | Use slopes to show/construct parallel and perpendicular lines | lines or points | m₁ = m₂ or m₁m₂ = −1; required line | line-equation | ⟂ to y = 2x through (0, 0) → x + 2y = 0
line-unknown-coefficient | OL | 2.2 | Find an unknown in a line from a condition | line with parameter + condition | parameter value | line-parallel-perp, eq-linear | kx + 2y = 5 ∥ 3x − y = 1 → k = −6
line-collinear | OL | 2.2 | Show points are collinear | three points | equal slopes (or zero area) | line-slope | (0, 1), (1, 3), (2, 5) → collinear
line-area-triangle | OL | 2.2 | Find the area of a triangle from vertices | three points | ½|x₁y₂ − x₂y₁| after translating a vertex to (0, 0) | geo-transformations | (0, 0), (4, 1), (2, 5) → 9
line-linear-model | OL | 2.2 | Interpret a linear relationship in context | table/graph/equation of a real situation | rate of change (slope) and start value (intercept); predictions | line-equation, fn-graph-linear | taxi: €4 + €1.50/km → slope 1.5
line-perp-distance | HL | 2.2 | Find the perpendicular distance from a point to a line | point + ax + by + c = 0 | |ax₁ + by₁ + c| / √(a² + b²) | line-equation | (1, 2) to 3x + 4y − 1 = 0 → 2
line-angle-between | HL | 2.2 | Find the angle between two lines | two slopes | tan θ = ±(m₁ − m₂)/(1 + m₁m₂) | line-slope, trig-ratios-right | m = 2, m = −3 → 45°
line-divide-ratio | HL | 2.2 | Divide a segment internally in a ratio | two points, ratio m : n | ((nx₁ + mx₂)/(m + n), (ny₁ + my₂)/(m + n)) | line-midpoint | (2, 1), (8, 7) in 1 : 2 → (4, 3)
line-from-distance | HL | 2.2 | Find lines through a point at a given distance/angle | point + distance or angle condition | slope(s) via quadratic, line equations | line-perp-distance, quad-solve-formula | through (0, 0), distance 2 from (4, 0) → m = ±1/√3
''')

# ── Co-ordinate geometry of the circle (2.2) ──────────────────────────────────
ch('maths8')
rows('''
circ-eq-origin | OL | 2.2 | Write/interpret a circle with centre (0, 0) | radius or point on circle | x² + y² = r² | line-distance | through (3, 4) → x² + y² = 25
circ-eq-centre-radius | OL | 2.2 | Write/interpret (x − h)² + (y − k)² = r² | centre and radius (or equation) | equation (or centre, radius) | circ-eq-origin | centre (2, −1), r = 3 → (x − 2)² + (y + 1)² = 9
circ-point-position | OL | 2.2 | Decide whether a point is inside, on or outside a circle | circle + point | inside/on/outside | alg-evaluate | (1, 2) and x² + y² = 9 → inside
circ-line-origin | OL | 2.2 | Find where a line meets a circle with centre (0, 0) | line + x² + y² = r² | intersection points | sim-linear-quadratic | y = x + 1, x² + y² = 25 → (3, 4), (−4, −3)
circ-tangent-at-point | OL | 2.2 | Find the tangent at a point on a circle | circle + point on it | tangent ⟂ radius | line-parallel-perp, geo-thm20 | x² + y² = 25 at (3, 4) → 3x + 4y = 25
circ-chord-length | OL | 2.2 | Find a chord length or distance from centre | radius + perpendicular distance (or chord) | chord length | geo-thm21, geo-thm14 | r = 5, distance 3 → chord 8
circ-general-form | HL | 2.2 | Use x² + y² + 2gx + 2fy + c = 0 | general equation | centre (−g, −f), r = √(g² + f² − c) | circ-eq-centre-radius | x² + y² − 4x + 6y − 12 = 0 → (2, −3), r = 5
circ-line-general | HL | 2.2 | Find where a line meets any circle | line + general circle | intersection points (or none) | circ-general-form, sim-linear-quadratic-hl | y = x and x² + y² − 4x = 0 → (0, 0), (2, 2)
circ-tangent-test | HL | 2.2 | Show a line is a tangent | line + circle | perpendicular distance = r | circ-general-form, line-perp-distance | 3x + 4y − 25 = 0 and x² + y² = 25 → distance 5 = r
circ-tangents-from-point | HL | 2.2 | Find tangents from an external point | circle + external point | tangent slopes and equations | circ-tangent-test, line-from-distance | x² + y² = 5 from (0, 5) → y = ±2x + 5
circ-tangent-length | HL | 2.2 | Find the length of a tangent from an external point | circle + external point | √(x₁² + y₁² + 2gx₁ + 2fy₁ + c) | circ-general-form, geo-thm14 | (7, 1) to x² + y² = 25 → 5
circ-from-conditions | HL | 2.2 | Find a circle's equation from conditions | e.g. three points, centre on a line, touches an axis | g, f, c | circ-general-form, sim-linear-3 | through (0, 0), (4, 0), (0, 6) → x² + y² − 4x − 6y = 0
circ-touching | HL | 2.2 | Decide whether circles touch internally or externally | two circles | |c₁c₂| = r₁ + r₂ or |r₁ − r₂| | circ-general-form, line-distance | (0, 0) r 3 and (8, 6) r 7 → touch externally
circ-common-chord | HL | 2.2 | Find the common chord/tangent of two circles | two circle equations | line by subtracting equations | circ-general-form | x² + y² = 25, x² + y² − 6x = 7 → x = 3
''')

# ── Synthetic geometry & transformations (2.1, 2.4) ───────────────────────────
ch('maths15')
_THEOREMS = [
    ('thm1', 'JC', 'Vertically opposite angles are equal'),
    ('thm2', 'JC', 'Isosceles triangle: equal sides ⇔ equal base angles'),
    ('thm3', 'JC', 'Alternate angles are equal ⇔ lines parallel'),
    ('thm4', 'JC', 'Angles in a triangle sum to 180°'),
    ('thm5', 'JC', 'Corresponding angles are equal ⇔ lines parallel'),
    ('thm6', 'JC', 'Exterior angle = sum of interior opposite angles'),
    ('thm7', 'OL', 'Greater side is opposite the greater angle (and converse)'),
    ('thm8', 'OL', 'Triangle inequality: two sides together exceed the third'),
    ('thm9', 'JC', 'Parallelogram: opposite sides and opposite angles equal'),
    ('thm10', 'JC', 'Diagonals of a parallelogram bisect each other'),
    ('thm11', 'OL', 'Three parallel lines cutting equal segments on one transversal cut equal segments on any'),
    ('thm12', 'OL', 'A line parallel to one side of a triangle divides the other two in the same ratio'),
    ('thm13', 'OL', 'Similar triangles have proportional sides'),
    ('thm14', 'JC', 'Pythagoras'),
    ('thm15', 'JC', 'Converse of Pythagoras'),
    ('thm16', 'OL', 'Base × height is the same for every side of a triangle'),
    ('thm17', 'OL', 'A diagonal bisects the area of a parallelogram'),
    ('thm18', 'OL', 'Area of a parallelogram = base × height'),
    ('thm19', 'HL', 'Angle at the centre is twice the angle at the circle'),
    ('thm20', 'OL', 'Tangent is perpendicular to the radius at the point of contact (and converse)'),
    ('thm21', 'OL', 'Perpendicular from the centre bisects a chord; perpendicular bisector of a chord passes through the centre'),
    ('cor1', 'HL', 'A diagonal divides a parallelogram into two congruent triangles'),
    ('cor2', 'HL', 'Angles standing on the same arc are equal'),
    ('cor3', 'JC', 'An angle in a semicircle is a right angle'),
    ('cor4', 'JC', 'A right angle at the circle stands on a diameter'),
    ('cor5', 'HL', 'Opposite angles of a cyclic quadrilateral sum to 180°'),
    ('cor6', 'OL', 'Circles sharing a tangent at a point: the centres and that point are collinear'),
]
for key, level, statement in _THEOREMS:
    num = key.replace('thm', 'Theorem ').replace('cor', 'Corollary ')
    SKILLS.append(dict(id='geo-' + key, level=level, syllabus='2.1', chapter=_chapter,
                       title=f'Apply {num}: {statement}',
                       input='geometric diagram with unknown angles/lengths',
                       output=f'unknown found, justified by citing {num}',
                       prereqs=['geo-congruence'] if key in ('thm9', 'thm10', 'cor1') else [],
                       example=''))
rows('''
geo-congruence | JC | 2.1 | Prove triangles congruent (SSS, SAS, ASA, RHS) | two triangles with given data | congruence with the case cited | | ΔABD ≡ ΔCBD by SAS
geo-similar-triangles | OL | 2.1 | Find lengths using similar triangles | two equiangular triangles | missing side via ratio | geo-thm13, num-ratio-proportion | ratio 3 : 5, side 6 → 10
geo-cuts | HL | 2.1 | Solve a geometry "cut" with a reasoned account | diagram + claim to prove | step-by-step deduction citing theorems | geo-thm4, geo-thm12, geo-thm13, geo-thm19, geo-cor5, geo-congruence | prove two triangles similar, then a length ratio
geo-prove-thm11 | HL | 2.1 | Prove Theorem 11 | statement | formal proof | geo-thm9, geo-congruence, logic-terms | three parallel lines → equal intercepts
geo-prove-thm12 | HL | 2.1 | Prove Theorem 12 | statement | formal proof | geo-prove-thm11 | parallel line divides sides in same ratio
geo-prove-thm13 | HL | 2.1 | Prove Theorem 13 | statement | formal proof | geo-prove-thm12 | similar triangles → proportional sides
geo-transformations | JC | 2.4 | Find images under translation, central symmetry, axial symmetry and rotation | point/shape + transformation | image; axes/centre of symmetry | | (2, 3) under central symmetry in (0, 0) → (−2, −3)
geo-enlargement | OL | 2.4 | Construct and analyse an enlargement | object, centre, scale factor k (0 < k < 1 or k > 1) | image; k from lengths; area × k² | num-ratio-proportion | k = 2.5, area 12 → 75
geo-enlargement-centre | OL | 2.4 | Find the centre and scale factor of an enlargement | object and image | centre (join corresponding points), k | geo-enlargement | image side 9, object side 6 → k = 1.5
''')

# ── Constructions & logic (2.1) ───────────────────────────────────────────────
ch('maths16')
_CONSTRUCTIONS = [
    (1, 'JC', 'Bisector of a given angle (compass and straight edge only)'),
    (2, 'JC', 'Perpendicular bisector of a segment (compass and straight edge only)'),
    (3, 'HL', 'Line perpendicular to a line l through a point not on l'),
    (4, 'JC', 'Line perpendicular to a line l through a point on l'),
    (5, 'JC', 'Line parallel to a given line through a given point'),
    (6, 'JC', 'Divide a segment into 2 or 3 equal parts without measuring'),
    (7, 'HL', 'Divide a segment into any number of equal parts without measuring'),
    (8, 'JC', 'Line segment of given length on a given ray'),
    (9, 'JC', 'Angle of a given number of degrees with a given ray as one arm'),
    (10, 'JC', 'Triangle given three sides (SSS)'),
    (11, 'JC', 'Triangle given SAS data'),
    (12, 'JC', 'Triangle given ASA data'),
    (13, 'JC', 'Right-angled triangle given hypotenuse and one other side'),
    (14, 'JC', 'Right-angled triangle given one side and an acute angle'),
    (15, 'JC', 'Rectangle given side lengths'),
    (16, 'OL', 'Circumcentre and circumcircle of a triangle (straight edge and compass)'),
    (17, 'OL', 'Incentre and incircle of a triangle (straight edge and compass)'),
    (18, 'OL', 'Angle of 60° without protractor or set square'),
    (19, 'OL', 'Tangent to a circle at a given point on it'),
    (20, 'OL', 'Parallelogram given side lengths and angles'),
    (21, 'OL', 'Centroid of a triangle'),
    (22, 'HL', 'Orthocentre of a triangle'),
]
_CON_PREREQS = {16: ['con-2'], 17: ['con-1'], 19: ['con-4'], 21: ['con-2'], 22: ['con-3']}
for n, level, task in _CONSTRUCTIONS:
    SKILLS.append(dict(id=f'con-{n}', level=level, syllabus='2.1', chapter=_chapter,
                       title=f'Construction {n}: {task}', input='given points/lines/measurements',
                       output='accurate construction with construction lines shown',
                       prereqs=_CON_PREREQS.get(n, []), example=''))
rows('''
logic-terms | OL | 2.1 | Use the language of deductive reasoning | statement or argument | correct use of theorem, proof, axiom, corollary, converse, implies | | converse of Theorem 14 is Theorem 15
logic-terms-hl | HL | 2.1 | Use equivalence, "if and only if" and proof by contradiction | statement | equivalent form, iff statement, contradiction structure | logic-terms | P ⇔ Q means P ⇒ Q and Q ⇒ P
num-construct-root2-3 | HL | 3.1 | Construct √2 and √3 geometrically | unit length | segments of length √2, √3 | geo-thm14, con-4 | right triangle 1, 1 → √2; then 1, √2 → √3
''')

# ── Trigonometry: triangles (2.3) ─────────────────────────────────────────────
ch('maths26')
rows('''
trig-ratios-right | JC | 2.3 | Use sin, cos, tan in a right-angled triangle | right triangle with a side and angle (or two sides) | missing side or angle | | opposite 5, hypotenuse 10 → 30°
trig-pythagoras | OL | 2.3 | Solve 2D problems with Pythagoras | right-angled situation | missing length | geo-thm14 | ladder 5 m, foot 3 m from wall → 4 m high
trig-elevation | JC | 2.3 | Solve heights-and-distances problems | angles of elevation/depression + a distance | height or distance | trig-ratios-right | 20 m away, elevation 35° → height ≈ 14.0 m
trig-area-triangle | OL | 2.3 | Find the area of a triangle with ½ab sin C | two sides + included angle | area (or a missing side/angle from area) | trig-unit-circle | a = 5, b = 8, C = 30° → 10
trig-sine-rule | OL | 2.3 | Apply the sine rule | side–angle pairs | missing side or angle | trig-unit-circle | a = 10, A = 30°, B = 45° → b ≈ 14.14
trig-sine-ambiguous | HL | 2.3 | Handle the ambiguous case of the sine rule | two sides + non-included angle | both possible triangles | trig-sine-rule, trig-solve-basic | a = 6, b = 8, A = 40° → B ≈ 59.0° or 121.0°
trig-cosine-rule | OL | 2.3 | Apply the cosine rule | SAS (find side) or SSS (find angle) | missing side or angle | trig-unit-circle | b = 5, c = 7, A = 60° → a = √39 ≈ 6.24
trig-triangle-problems | OL | 2.3 | Solve multi-step 2D triangle problems | context with several triangles | chained use of sine/cosine rules and area | trig-sine-rule, trig-cosine-rule, trig-area-triangle | quadrilateral split by a diagonal
trig-3d | HL | 2.3 | Solve 3D trigonometry problems | 3D context (pyramid, mast, box) | lengths/angles via right/non-right triangles | trig-triangle-problems, trig-pythagoras | angle between space diagonal and base of a cube → 35.3°
''')

# ── Trigonometry: functions & identities (2.3) ────────────────────────────────
ch('maths25')
rows('''
trig-unit-circle | OL | 2.3 | Define sin θ, cos θ, tan θ for all θ (unit circle) | any angle | value with correct sign (CAST, related angle) | trig-ratios-right | cos 240° → −½
trig-exact-values | OL | 2.3 | Use trig ratios in surd form | 30°, 45°, 60° and related angles | exact value | trig-unit-circle, num-surds | sin 135° → 1/√2
trig-solve-basic | OL | 2.3 | Solve sin θ = k, cos θ = k, tan θ = k in a range | equation + interval | all solutions in the interval | trig-unit-circle | cos θ = −½, 0° ≤ θ ≤ 360° → 120°, 240°
trig-radians | HL | 2.3 | Use radian measure | angle in degrees or radians | converted angle | | 135° → 3π/4
trig-pythag-identity | HL | 2.3 | Use cos²A + sin²A = 1 (formula 1) | one ratio + quadrant | other ratios; simplified expression | trig-unit-circle | sin A = 3/5, A acute → cos A = 4/5
trig-compound | HL | 2.3 | Apply compound angle formulae (4, 5, 7, 8, 9, 10) | A ± B | exact value / expansion | trig-exact-values | cos 75° → (√6 − √2)/4
trig-double | HL | 2.3 | Apply double/half angle formulae (6, 11–16) | 2A or A in terms of 2A | value / rewritten expression | trig-compound, trig-pythag-identity | sin A = 3/5 (acute) → sin 2A = 24/25
trig-products-sums | HL | 2.3 | Apply product-to-sum and sum-to-product formulae (17–24) | product or sum of trig terms | sum or product | trig-compound | sin 5x + sin x → 2 sin 3x cos 2x
trig-prove-identity | HL | 2.3 | Prove a trig identity | identity | one side transformed to the other | trig-double, trig-products-sums, alg-fractions-simplify | (1 − cos 2A)/sin 2A = tan A
trig-solve-general | HL | 2.3 | Solve trig equations giving all solutions | sin nθ = k, cos nθ = k, tan nθ = k | general solution / all solutions in range | trig-solve-basic, trig-radians | cos 2θ = ½ → θ = ±π/6 + nπ
trig-solve-quadratic | HL | 2.3 | Solve trig equations reducible to quadratics | equation in sin θ / cos θ (possibly via identities) | all solutions | trig-solve-basic, quad-solve-factor, trig-pythag-identity | 2sin²θ − sin θ − 1 = 0 → 90°, 210°, 330°
trig-graph | HL | 2.3 | Graph sin, cos and tan | function + domain | graph with period and range | trig-unit-circle, trig-radians | y = tan x has period π
trig-graph-abc | HL | 2.3 | Graph and analyse a + b sin cθ / a + b cos cθ | a, b, c (or the graph) | graph, period 2π/c, range [a − |b|, a + |b|]; a, b, c from graph | trig-graph | 2 + 3 sin 2θ → period π, range [−1, 5]
''')
_DERIVE = [
    (1, 'cos²A + sin²A = 1', ['trig-unit-circle', 'geo-thm14']),
    (2, 'the sine rule', ['trig-area-triangle']),
    (3, 'the cosine rule', ['trig-ratios-right', 'geo-thm14', 'trig-pythag-identity']),
    (4, 'cos(A − B) = cos A cos B + sin A sin B', ['line-distance', 'trig-cosine-rule', 'trig-unit-circle']),
    (5, 'cos(A + B) from formula 4', ['trig-derive-4']),
    (6, 'cos 2A = cos²A − sin²A from formula 5', ['trig-derive-5']),
    (7, 'sin(A + B) from formula 4', ['trig-derive-4']),
    (9, 'tan(A + B) from formulae 5 and 7', ['trig-derive-5', 'trig-derive-7']),
]
for n, what, pre in _DERIVE:
    SKILLS.append(dict(id=f'trig-derive-{n}', level='HL', syllabus='2.3', chapter='maths25',
                       title=f'Derive formula {n}: {what}', input='earlier formulae in the appendix order',
                       output='derivation', prereqs=pre, example=''))

# ── Probability & counting (1.1–1.3) ──────────────────────────────────────────
ch('maths20')
rows('''
prob-counting-principle | JC | 1.1 | List outcomes and apply the fundamental principle of counting | multi-stage choice | total number of outcomes | | 3 starters × 4 mains → 12 meals
prob-factorial | OL | 1.1 | Count arrangements of n distinct objects | n | n! | prob-counting-principle | 5 people in a row → 120
prob-npr | OL | 1.1 | Count arrangements of r objects from n | n, r | ⁿPᵣ | prob-factorial | 3 from 5 in order → 60
prob-arrangement-restrictions | OL | 1.1 | Count arrangements with restrictions | objects + condition (together, at ends, even…) | number of arrangements | prob-npr | letters of MATHS with M first → 24
prob-ncr | HL | 1.1 | Count selections and compute binomial coefficients | n, r | ⁿCᵣ | prob-factorial | 3 from 10 → 120
prob-selection-restrictions | HL | 1.1 | Count selections with restrictions | groups + condition | number of selections | prob-ncr | committee of 3 from 4 men, 5 women with exactly 1 woman → 30
prob-sample-space | JC | 1.3 | Construct a sample space for two independent events | two experiments | table/list of outcomes | prob-counting-principle | two dice → 36 outcomes
prob-equally-likely | JC | 1.3 | Find a probability with equally likely outcomes | sample space + event | favourable/total | prob-sample-space, num-fractions | two dice, sum 7 → 1/6
prob-relative-frequency | JC | 1.2 | Estimate probability from experimental data | trial results | relative frequency; expected frequency | num-fractions | 18 heads in 50 → 0.36
prob-venn | OL | 1.2 | Use set notation and Venn diagrams for probability | event data | P(A ∪ B), P(A ∩ B), P(A′), mutually exclusive check | prob-equally-likely | 30 students, 12 A, 15 B, 5 both → P(neither) = 8/30
prob-addition-rule | HL | 1.2 | Apply the addition rule | P(A), P(B), P(A ∩ B) | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | prob-venn | 0.5 + 0.4 − 0.2 → 0.7
prob-independent | OL | 1.3 | Find the probability two independent events both occur | P(A), P(B) | P(A)P(B) | prob-equally-likely | P(head and six) → 1/12
prob-independence-test | HL | 1.2 | Test whether events are independent | P(A), P(B), P(A ∩ B) | independent iff P(A ∩ B) = P(A)P(B) | prob-independent | 0.5 × 0.4 = 0.2 → independent
prob-conditional | HL | 1.2 | Apply conditional probability and the general multiplication rule | P(A ∩ B), P(B) (or table) | P(A|B); note P(A|B) ≠ P(B|A) | prob-venn | P(A ∩ B) = 0.2, P(B) = 0.5 → 0.4
prob-tree | OL | 1.3 | Use a tree diagram for multi-stage experiments | stages with probabilities | probability of combined outcomes | prob-independent | two coins → P(at least one head) = 3/4
prob-without-replacement | HL | 1.2 | Solve sampling problems with or without replacement | container contents + draws | probability | prob-tree, prob-conditional | 3 red, 2 blue, two drawn → P(both red) = 3/10
prob-expected-value | OL | 1.2 | Calculate expected value and judge fairness | outcomes with probabilities/payoffs | E(X) = Σ x P(x); fair or not | prob-equally-likely | win €10 (p = 0.2) else lose €3 → −€0.40
prob-bernoulli-3 | OL | 1.3 | Solve problems with up to 3 Bernoulli trials | p, up to 3 trials | probability of the outcomes asked for | prob-tree | P(exactly 2 sixes in 3 rolls) → 15/216
prob-first-success | OL | 1.3 | Find the probability the first success is on trial n | p, n | (1 − p)ⁿ⁻¹ p | prob-independent, ind-laws | first six on 3rd roll → 25/216
prob-binomial | HL | 1.3 | Find the probability of k successes in n trials | n, k, p | ⁿCₖ pᵏ(1 − p)ⁿ⁻ᵏ (incl. "at least") | prob-ncr, prob-independent | exactly 2 heads in 5 tosses → 0.3125
prob-kth-success | HL | 1.3 | Find the probability the kth success is on trial n | n, k, p | ⁿ⁻¹Cₖ₋₁ pᵏ(1 − p)ⁿ⁻ᵏ | prob-binomial | 2nd six on 5th roll → ≈ 0.0643
''')

# ── Descriptive statistics (1.4–1.6) ──────────────────────────────────────────
ch('maths22')
rows('''
stat-data-types | OL | 1.4 | Classify data | variable description | categorical (nominal/ordinal) or numerical (discrete/continuous); univariate/bivariate | | shoe size → numerical discrete
stat-populations-samples | OL | 1.4 | Distinguish population and sample; judge generalisation | study description | population, sample, how far conclusions generalise | | 100 students from one school ≠ all Irish students
stat-srs-bias | OL | 1.5 | Select a simple random sample and spot bias | population + sampling method | SRS procedure; source of bias | stat-populations-samples | phone poll at 11am → biased against workers
stat-study-types | OL | 1.5 | Identify surveys, observational studies and designed experiments | study description | type with reason | stat-populations-samples | random diet assignment → designed experiment
stat-sampling-methods-hl | HL | 1.5 | Define stratified, cluster and quota sampling; role of randomisation and controls | study description | method; biases, limitations, ethics; control group | stat-srs-bias, stat-study-types | sampling by year group proportionally → stratified
stat-plan-collect | OL | 1.5 | Design a plan and questions to collect data | research question | data-collection plan, unbiased questions | stat-srs-bias | leading question → neutral rewording
stat-averages | JC | 1.6 | Find mean, median and mode (incl. frequency tables) | data set or frequency table | mean, median, mode | num-order-operations | 2, 3, 3, 8 → mean 4, median 3, mode 3
stat-grouped-mean | OL | 1.6 | Estimate the mean of grouped data | grouped frequency table | mean via mid-interval values | stat-averages | 0–10: 4, 10–20: 6 → 11
stat-charts | JC | 1.6 | Draw bar, pie, line plot, histogram and stem-and-leaf | data set | correct graph | num-ratio-proportion | pie: 15 of 60 → 90° sector
stat-choose-display | OL | 1.6 | Select an appropriate graphical/numerical summary | data type + question | chosen method with reason | stat-data-types, stat-charts | bivariate numerical → scatter plot
stat-quartiles-iqr | OL | 1.6 | Find quartiles and the interquartile range | data set | Q₁, Q₂, Q₃, IQR | stat-averages | 2, 4, 5, 7, 9, 11, 12 → IQR 7
stat-sd | OL | 1.6 | Calculate standard deviation (calculator) | data set or frequency table | σ | stat-averages | 2, 4, 4, 4, 5, 5, 7, 9 → σ = 2
stat-distribution-shape | OL | 1.6 | Describe a distribution's shape | histogram/stem plot | symmetric, positive/negative skew; effect on mean vs median | stat-charts | long right tail → positive skew, mean > median
stat-back-to-back | OL | 1.6 | Compare data sets with back-to-back stem-and-leaf plots | two data sets | plot and comparison of centre/spread | stat-charts, stat-quartiles-iqr | boys vs girls reaction times
stat-compare-hl | HL | 1.6 | Analyse plots to explain differences in centre and spread | two distributions | reasoned comparison | stat-back-to-back, stat-sd, stat-distribution-shape | higher median but larger IQR
stat-outliers | OL | 1.6 | Recognise outliers | data set | outliers (e.g. beyond 1.5 × IQR) | stat-quartiles-iqr | 3, 4, 5, 5, 6, 30 → 30
stat-outlier-effect | HL | 1.6 | Explain the effect of outliers on summary statistics | data set with outlier | effect on mean/median/σ/IQR | stat-outliers, stat-sd | removing 30 lowers the mean much more than the median
stat-percentiles | HL | 1.6 | Use percentiles for relative standing | data set or distribution + value | percentile rank / value at percentile | stat-quartiles-iqr | 80th percentile → 80% score below
stat-scatter-correlation | OL | 1.6 | Read scatter plots and correlation | bivariate data/plot | strength and direction; match r to plot; correlation ≠ causation | stat-charts | r = −0.9 → strong negative linear
stat-correlation-calc | HL | 1.6 | Calculate the correlation coefficient (calculator) | bivariate data | r | stat-scatter-correlation | (1, 2), (2, 4), (3, 6) → r = 1
stat-line-best-fit | HL | 1.6 | Draw a line of best fit by eye and predict | scatter plot | line, equation, prediction | stat-scatter-correlation, line-equation | read y at x = 7 from the line
''')

# ── Inferential statistics (1.7) ──────────────────────────────────────────────
ch('maths23')
rows('''
inf-sampling-variability | OL | 1.7 | Recognise how sampling variability affects conclusions | sample statistics | statement about the population with caution | stat-populations-samples | two samples give different means
inf-interpret | OL | 1.7 | Interpret an analysis and relate it to the original question | results of analysis | conclusion in context | inf-sampling-variability | 60% prefer A → answer the survey question
inf-histogram | OL | 1.7 | Interpret a histogram in terms of distribution | histogram | shape, centre, spread in context | stat-distribution-shape | bimodal → two groups present
inf-margin-of-error | OL | 1.7 | Calculate the margin of error for a proportion | n | 1/√n | ind-negative-fractional | n = 400 → 5%
inf-hypothesis-concept | OL | 1.7 | State null and alternative hypotheses | claim | H₀, H₁, possible conclusions | | claim 30% → H₀: p = 0.3
inf-hypothesis-moe | OL | 1.7 | Test a claim about a proportion using margin of error | claimed p, p̂, n | interval p̂ ± 1/√n; reject/fail to reject | inf-margin-of-error, inf-hypothesis-concept | p̂ = 0.34, n = 400 → (0.29, 0.39), 0.3 inside → do not reject
inf-sampling-distribution | HL | 1.3 | Use the sampling distribution of the mean | μ, σ, n (or simulation) | mean μ, standard error σ/√n; probabilities for x̄ | stat-normal-prob | σ = 10, n = 25 → SE = 2
inf-ci-mean | HL | 1.7 | Construct a 95% confidence interval for a mean (large sample) | x̄, σ (or s), n | x̄ ± 1.96 σ/√n | inf-sampling-distribution | x̄ = 50, σ = 10, n = 100 → (48.04, 51.96)
inf-ci-proportion | HL | 1.7 | Construct a 95% confidence interval for a proportion | p̂, n | p̂ ± 1.96√(p̂(1 − p̂)/n) | inf-margin-of-error, stat-z-score | p̂ = 0.3, n = 400 → (0.255, 0.345)
inf-confidence-width | HL | 1.7 | Relate confidence level, sample size and interval width | interval requirements | wider/narrower; n needed for a margin | inf-ci-mean, inf-ci-proportion | halving the margin needs 4× the sample
inf-z-test | HL | 1.7 | Perform a two-tailed z-test of a population mean | H₀ μ, x̄, σ, n | z statistic vs ±1.96; conclusion | inf-ci-mean, inf-hypothesis-concept | μ₀ = 50, x̄ = 52, σ = 8, n = 64 → z = 2, reject H₀
inf-p-value | HL | 1.7 | Calculate and interpret a p-value | test statistic | p-value; compare with 0.05 | inf-z-test, stat-normal-prob | z = 2 → p ≈ 0.0456 < 0.05
''')

# ── Normal distribution & z-scores (1.3, 1.6, 1.7) ────────────────────────────
ch('maths24')
rows('''
stat-empirical-rule | OL | 1.7 | Make decisions with the empirical rule | μ, σ | 68% / 95% / 99.7% ranges | stat-sd | μ = 50, σ = 5 → 95% in [40, 60]
stat-z-score | HL | 1.6 | Standardise a value | x, μ, σ | z = (x − μ)/σ; relative standing | stat-sd | x = 130, μ = 100, σ = 15 → z = 2
stat-normal-prob | HL | 1.3 | Read probabilities from normal tables | normal X, interval | probability via z and tables (symmetry, 1 − P) | stat-z-score | P(X < 130), μ = 100, σ = 15 → 0.9772
stat-normal-inverse | HL | 1.3 | Work backwards from a normal probability | probability + some of μ, σ, x | z from tables → missing x, μ or σ | stat-normal-prob, sim-linear-2 | top 10% → z ≈ 1.28
''')
