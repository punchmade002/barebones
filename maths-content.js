// Maths HL Content — notes, concept points and flashcards for all chapters.
// Past-paper exam questions live in exam-questions-db.js.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  function ch(id) { return COURSE_DATA.chapters.find(function (c) { return c.id === id; }); }

  // ── maths1: Algebra - Cubics ──────────────────────────────────────────────
  (function () {
    var c = ch("maths1");
    // M1.1 — Cubic equations — key methods
    c.learningOutcomes[0].notes = [
      {
        h: "Factor Theorem",
        b: "If f(a) = 0 then (x − a) is a factor of f(x). Substitute integer values ±1, ±2, ±3, … to find a root, then use that factor to reduce the cubic to a quadratic."
      },
      {
        h: "Remainder Theorem",
        b: "When f(x) is divided by (x − a), the remainder equals f(a). Useful for finding unknowns in a polynomial when the remainder is given."
      },
      {
        h: "Long Division / Synthetic Division",
        b: "Once one linear factor (x − a) is found, divide the cubic by it to obtain a quadratic ax² + bx + c, then factorise or solve the quadratic."
      },
      {
        h: "Fully solving a cubic",
        b: "Step 1 — Find one root by trial (Factor Theorem). Step 2 — Divide to get a quadratic. Step 3 — Factorise the quadratic (inspection or formula). Step 4 — State all three roots."
      }
    ];
  })();

  // ── maths2: Algebra - Expressions & Factorising ───────────────────────────
  (function () {
    var c = ch("maths2");
    // M2.1 — Algebraic expressions and factorisation
    c.learningOutcomes[0].notes = [
      {
        h: "Expanding brackets",
        b: "Multiply every term inside by the term outside, or use FOIL for two binomials: (a+b)(c+d) = ac + ad + bc + bd."
      },
      {
        h: "Difference of two squares",
        b: "a² − b² = (a − b)(a + b). Recognise the pattern when both terms are perfect squares with a minus sign."
      },
      {
        h: "Factorising a quadratic expression",
        b: "ax² + bx + c: find two numbers that multiply to ac and add to b. Split the middle term and factor by grouping."
      },
      {
        h: "Algebraic fractions",
        b: "To add/subtract: find a common denominator. To simplify: factorise numerator and denominator fully, then cancel common factors."
      }
    ];
  })();

  // ── maths3: Algebra - Inequalities ────────────────────────────────────────
  (function () {
    var c = ch("maths3");
    // M3.1 — Solving inequalities
    c.learningOutcomes[0].notes = [
      {
        h: "Linear inequalities",
        b: "Solve like an equation but flip the inequality sign when multiplying or dividing by a negative number. e.g. −2x > 6 ⟹ x < −3."
      },
      {
        h: "Quadratic inequalities",
        b: "Step 1 — Solve the equality to find critical values. Step 2 — Sketch the parabola or test a point in each region. Step 3 — Write the solution set in the correct interval form."
      },
      {
        h: "Sign diagram method",
        b: "Mark the roots on a number line. Test a value in each interval to determine the sign of the expression. Select intervals where the sign matches the inequality."
      },
      {
        h: "Notation",
        b: "Use interval notation where required: e.g. x ∈ (−3, 2) means −3 < x < 2; x ∈ (−∞, −3) ∪ (2, ∞) for the outside regions."
      }
    ];
  })();

  // ── maths4: Algebra - Quadratics ──────────────────────────────────────────
  (function () {
    var c = ch("maths4");
    // M4.1 — Quadratic equations and the discriminant
    c.learningOutcomes[0].notes = [
      {
        h: "Quadratic formula",
        b: "For ax² + bx + c = 0: x = (−b ± √(b² − 4ac)) / 2a. Always state the formula in full before substituting."
      },
      {
        h: "Discriminant",
        b: "Δ = b² − 4ac. If Δ > 0: two distinct real roots. If Δ = 0: one repeated real root. If Δ < 0: no real roots (two complex roots)."
      },
      {
        h: "Completing the square",
        b: "Write ax² + bx + c in the form a(x + p)² + q. Useful for finding the vertex of a parabola and for proving the quadratic formula."
      },
      {
        h: "Sum and product of roots",
        b: "If α and β are roots: α + β = −b/a and α × β = c/a. Use to form a new quadratic when roots are given in terms of α and β."
      }
    ];
  })();

  // ── maths5: Algebra - Simultaneous Equations ──────────────────────────────
  (function () {
    var c = ch("maths5");
    // M5.1 — Solving simultaneous equations
    c.learningOutcomes[0].notes = [
      {
        h: "Elimination method",
        b: "Multiply equations to make coefficients of one variable equal, then add or subtract to eliminate it. Substitute back to find the second variable."
      },
      {
        h: "Substitution method",
        b: "Express one variable in terms of the other from one equation, then substitute into the second equation."
      },
      {
        h: "Linear and non-linear systems",
        b: "When one equation is quadratic, substitute the linear expression into the quadratic to get a quadratic in one unknown. Solve, then find the corresponding values of the other variable."
      },
      {
        h: "Three unknowns",
        b: "Use a combination of elimination: reduce three equations to two, then two to one. Substitute back step by step."
      }
    ];
  })();

  // ── maths6: Algebra - Solving Equations ───────────────────────────────────
  (function () {
    var c = ch("maths6");
    // M6.1 — Solving equations — general methods
    c.learningOutcomes[0].notes = [
      {
        h: "Rational equations",
        b: "Multiply both sides by the LCD to clear fractions, then solve the resulting polynomial equation. Check solutions do not make any denominator zero."
      },
      {
        h: "Equations with surds",
        b: "Isolate the surd, then square both sides. Check all solutions in the original equation as squaring can introduce extraneous roots."
      },
      {
        h: "Modulus equations",
        b: "|f(x)| = k ⟹ f(x) = k or f(x) = −k. Solve each case separately and check both solutions."
      },
      {
        h: "Checking solutions",
        b: "Always substitute the solution back into the original equation to verify it is valid, especially after squaring or clearing denominators."
      }
    ];
  })();

  // ── maths7: Area & Volume ─────────────────────────────────────────────────
  (function () {
    var c = ch("maths7");
    // M7.1 — Area and volume formulae
    c.learningOutcomes[0].notes = [
      {
        h: "Cylinder",
        b: "Volume = πr²h. Curved surface area = 2πrh. Total surface area = 2πrh + 2πr²."
      },
      {
        h: "Cone",
        b: "Volume = (1/3)πr²h. Curved surface area = πrl where l = √(r² + h²) is the slant height."
      },
      {
        h: "Sphere",
        b: "Volume = (4/3)πr³. Surface area = 4πr²."
      },
      {
        h: "Composite solids",
        b: "Break the shape into standard parts (e.g. cylinder + hemisphere). Calculate each part separately then add or subtract as required."
      },
      {
        h: "Trapezoidal rule (Area)",
        b: "Area ≈ (h/2)[y₀ + 2(y₁ + y₂ + … + yₙ₋₁) + yₙ] where h is the strip width. Used when the boundary is not a standard shape."
      }
    ];
  })();

  // ── maths8: Co-Ordinate Geometry of the Circle ────────────────────────────
  (function () {
    var c = ch("maths8");
    // M8.1 — Circle equations and properties
    c.learningOutcomes[0].notes = [
      {
        h: "Equation of a circle",
        b: "Centre (h, k), radius r: (x − h)² + (y − k)² = r². Standard form with centre at origin: x² + y² = r²."
      },
      {
        h: "General form",
        b: "x² + y² + 2gx + 2fy + c = 0. Centre = (−g, −f). Radius = √(g² + f² − c)."
      },
      {
        h: "Tangent to a circle",
        b: "A tangent is perpendicular to the radius at the point of contact. Find the slope of the radius, then use the negative reciprocal for the tangent slope."
      },
      {
        h: "Intersection of line and circle",
        b: "Substitute the line equation into the circle equation to get a quadratic. Use the discriminant: Δ = 0 for tangent, Δ > 0 for two intersections, Δ < 0 for no intersection."
      }
    ];
  })();

  // ── maths9: Co-Ordinate Geometry of the Line ──────────────────────────────
  (function () {
    var c = ch("maths9");
    // M9.1 — Lines — equations and properties
    c.learningOutcomes[0].notes = [
      {
        h: "Slope formula",
        b: "m = (y₂ − y₁) / (x₂ − x₁). Parallel lines have equal slopes. Perpendicular lines have slopes m₁ × m₂ = −1."
      },
      {
        h: "Equation of a line",
        b: "Slope-intercept: y = mx + c. Point-slope: y − y₁ = m(x − x₁). Two-intercept form: x/a + y/b = 1."
      },
      {
        h: "Distance from a point to a line",
        b: "Distance from (x₁, y₁) to ax + by + c = 0 is |ax₁ + by₁ + c| / √(a² + b²)."
      },
      {
        h: "Midpoint and distance",
        b: "Midpoint of (x₁,y₁) and (x₂,y₂): ((x₁+x₂)/2, (y₁+y₂)/2). Distance = √((x₂−x₁)² + (y₂−y₁)²)."
      }
    ];
  })();

  // ── maths10: Complex Numbers ──────────────────────────────────────────────
  (function () {
    var c = ch("maths10");
    // M10.1 — Complex numbers — arithmetic and geometry
    c.learningOutcomes[0].notes = [
      {
        h: "Definition",
        b: "A complex number z = a + bi where a is the real part and b is the imaginary part. i² = −1."
      },
      {
        h: "Modulus and argument",
        b: "|z| = √(a² + b²). arg(z) = θ where tan(θ) = b/a; adjust quadrant. Polar form: z = r(cos θ + i sin θ)."
      },
      {
        h: "De Moivre's Theorem",
        b: "[r(cos θ + i sin θ)]ⁿ = rⁿ(cos nθ + i sin nθ). Used to find powers and roots of complex numbers."
      },
      {
        h: "Conjugate and division",
        b: "Conjugate of z = a + bi is z̄ = a − bi. To divide: multiply numerator and denominator by the conjugate of the denominator."
      },
      {
        h: "Roots of unity / quadratics",
        b: "Complex roots of a real quadratic occur in conjugate pairs. If α = a + bi is a root, then ā = a − bi is also a root."
      }
    ];
  })();

  // ── maths11: Differentiation - Applications ───────────────────────────────
  (function () {
    var c = ch("maths11");
    // M11.1 — Applications of differentiation
    c.learningOutcomes[0].notes = [
      {
        h: "Finding turning points",
        b: "Set f′(x) = 0 and solve. Then use the second derivative test: f″(x) > 0 ⟹ local minimum; f″(x) < 0 ⟹ local maximum; f″(x) = 0 ⟹ test further (point of inflection possible)."
      },
      {
        h: "Curve sketching",
        b: "Find: (1) intercepts with axes; (2) stationary points and their nature; (3) behaviour as x → ±∞; (4) points of inflection where f″(x) = 0 and sign changes."
      },
      {
        h: "Rates of change",
        b: "dy/dx represents the instantaneous rate of change of y with respect to x. Use the chain rule for related rates: dy/dt = (dy/dx) × (dx/dt)."
      },
      {
        h: "Optimisation",
        b: "Form an equation for the quantity to be maximised/minimised as a function of one variable. Differentiate, set equal to zero, solve, and verify using the second derivative."
      }
    ];
  })();

  // ── maths12: Differentiation - Rules ──────────────────────────────────────
  (function () {
    var c = ch("maths12");
    // M12.1 — Rules of differentiation
    c.learningOutcomes[0].notes = [
      {
        h: "First principles",
        b: "f′(x) = lim[h→0] (f(x+h) − f(x)) / h. Required for proving d/dx(xⁿ) = nxⁿ⁻¹ or differentiating specific functions from scratch."
      },
      {
        h: "Standard results",
        b: "d/dx(xⁿ) = nxⁿ⁻¹. d/dx(sin x) = cos x. d/dx(cos x) = −sin x. d/dx(eˣ) = eˣ. d/dx(ln x) = 1/x."
      },
      {
        h: "Chain rule",
        b: "If y = f(g(x)) then dy/dx = f′(g(x)) × g′(x). Identify the outer and inner functions clearly before differentiating."
      },
      {
        h: "Product rule",
        b: "If y = u × v then dy/dx = u(dv/dx) + v(du/dx). Label u and v, find du/dx and dv/dx separately, then substitute."
      },
      {
        h: "Quotient rule",
        b: "If y = u/v then dy/dx = (v(du/dx) − u(dv/dx)) / v². Alternatively, rewrite as a product and use the product rule."
      }
    ];
  })();

  // ── maths13: Financial Maths ──────────────────────────────────────────────
  (function () {
    var c = ch("maths13");
    // M13.1 — Financial maths — interest and annuities
    c.learningOutcomes[0].notes = [
      {
        h: "Compound interest",
        b: "F = P(1 + i)ⁿ where P = principal, i = interest rate per period, n = number of periods, F = final amount."
      },
      {
        h: "Present value",
        b: "P = F / (1 + i)ⁿ. The present value is how much you need to invest now to reach F in n periods at rate i."
      },
      {
        h: "Annuity (present value)",
        b: "PV = A × [1 − (1 + i)⁻ⁿ] / i where A is the regular payment. Used for mortgages and loans — the formula is on the LC formula sheet."
      },
      {
        h: "Annuity (future value)",
        b: "FV = A × [(1 + i)ⁿ − 1] / i. Used to find the accumulated value of regular savings over time."
      },
      {
        h: "APR",
        b: "Annual Percentage Rate — the effective annual interest rate accounting for compounding. Found by solving (1 + i_monthly)¹² = 1 + APR."
      }
    ];
  })();

  // ── maths14: Functions ────────────────────────────────────────────────────
  (function () {
    var c = ch("maths14");
    // M14.1 — Functions — definitions and operations
    c.learningOutcomes[0].notes = [
      {
        h: "Domain and range",
        b: "Domain: the set of valid input values of x. Range: the set of corresponding output values f(x). Restrictions arise from division by zero, square roots of negatives, or context."
      },
      {
        h: "Composite functions",
        b: "f∘g means apply g first, then f: (f∘g)(x) = f(g(x)). Note: f∘g ≠ g∘f in general."
      },
      {
        h: "Inverse function",
        b: "f⁻¹ reverses f: f(f⁻¹(x)) = x. To find: swap x and y in y = f(x) and solve for y. The graph of f⁻¹ is the reflection of f in the line y = x."
      },
      {
        h: "Injective / surjective",
        b: "A function is injective (one-to-one) if different inputs give different outputs. Surjective (onto) if every element of the codomain is an output. An inverse exists iff the function is injective."
      }
    ];
  })();

  // ── maths15: Geometry ─────────────────────────────────────────────────────
  (function () {
    var c = ch("maths15");
    // M15.1 — Geometry theorems and proofs
    c.learningOutcomes[0].notes = [
      {
        h: "Key theorems (LC list)",
        b: "Theorem 11: If three parallel lines cut equal intercepts on one transversal, they cut equal intercepts on every transversal. Theorem 12: In a triangle, a line parallel to one side divides the other two sides proportionally. Theorem 13: If two triangles are equiangular they are similar."
      },
      {
        h: "Theorem 19 (Pythagoras)",
        b: "In a right-angled triangle the square on the hypotenuse equals the sum of the squares on the other two sides: a² + b² = c²."
      },
      {
        h: "Corollaries",
        b: "Learn the corollaries listed in the LC syllabus — these are frequently asked alongside theorems. State the corollary number and result precisely."
      },
      {
        h: "Proof structure",
        b: "State: (1) what is given; (2) what is to be proved; (3) construction (if any); (4) each step of the proof with justification. Marks are awarded per step."
      }
    ];
  })();

  // ── maths16: Geometry - Constructions & Proofs ────────────────────────────
  (function () {
    var c = ch("maths16");
    // M16.1 — Geometric constructions
    c.learningOutcomes[0].notes = [
      {
        h: "Required constructions",
        b: "LC HL requires: bisecting a line segment, bisecting an angle, constructing a perpendicular from a point, dividing a line in a given ratio, tangent to a circle, circumscribed/inscribed circle of a triangle."
      },
      {
        h: "Execution marks",
        b: "Marks are awarded for accuracy and visible construction arcs. Leave all arcs showing. Use compass and ruler only — do not use a protractor unless explicitly permitted."
      },
      {
        h: "Formal proofs",
        b: "For proofs such as 'prove the angle in a semicircle is 90°', set out the proof step by step using the LC theorem framework: Given / To Prove / Construction / Proof."
      }
    ];
  })();

  // ── maths17: Indices and Logs ─────────────────────────────────────────────
  (function () {
    var c = ch("maths17");
    // M17.1 — Laws of indices and logarithms
    c.learningOutcomes[0].notes = [
      {
        h: "Laws of indices",
        b: "aᵐ × aⁿ = aᵐ⁺ⁿ. aᵐ / aⁿ = aᵐ⁻ⁿ. (aᵐ)ⁿ = aᵐⁿ. a⁰ = 1. a⁻ⁿ = 1/aⁿ. a^(1/n) = ⁿ√a."
      },
      {
        h: "Laws of logarithms",
        b: "log(AB) = log A + log B. log(A/B) = log A − log B. log(Aⁿ) = n log A. Change of base: log_a(x) = log(x) / log(a)."
      },
      {
        h: "Solving exponential equations",
        b: "Take logarithms of both sides. e.g. 3ˣ = 20 ⟹ x log 3 = log 20 ⟹ x = log 20 / log 3. Or use natural logs if the base involves e."
      },
      {
        h: "Natural logarithm",
        b: "ln(x) = log_e(x). ln(eˣ) = x and e^(ln x) = x. Used in differentiation and integration of exponential functions."
      }
    ];
  })();

  // ── maths18: Induction ────────────────────────────────────────────────────
  (function () {
    var c = ch("maths18");
    // M18.1 — Proof by mathematical induction
    c.learningOutcomes[0].notes = [
      {
        h: "Structure of a proof by induction",
        b: "Step 1 (Base case): Prove the statement P(1) is true. Step 2 (Inductive step): Assume P(k) is true (inductive hypothesis), then prove P(k+1) is true. Step 3 (Conclusion): By the principle of mathematical induction, P(n) is true for all n ∈ ℕ."
      },
      {
        h: "Common induction types",
        b: "Summation formulae (e.g. Σk = n(n+1)/2), divisibility results (e.g. 3ⁿ − 1 is divisible by 2), and inequalities."
      },
      {
        h: "Key technique for P(k+1)",
        b: "Start from P(k) (the assumption) and manipulate to reach the P(k+1) form. Add the (k+1)th term to both sides of the summation, simplify, and factorise to show it matches the formula with n = k+1."
      }
    ];
  })();

  // ── maths19: Integration ──────────────────────────────────────────────────
  (function () {
    var c = ch("maths19");
    // M19.1 — Integration — rules and applications
    c.learningOutcomes[0].notes = [
      {
        h: "Standard integrals",
        b: "∫xⁿ dx = xⁿ⁺¹/(n+1) + c (n ≠ −1). ∫sin x dx = −cos x + c. ∫cos x dx = sin x + c. ∫eˣ dx = eˣ + c. ∫(1/x) dx = ln|x| + c."
      },
      {
        h: "Integration by substitution",
        b: "Let u = g(x), then du = g′(x) dx. Rewrite the integral in terms of u, integrate, then substitute back."
      },
      {
        h: "Integration by parts",
        b: "∫u dv = uv − ∫v du. Choose u to be the function that simplifies when differentiated (LIATE order: Log, Inverse trig, Algebraic, Trig, Exponential)."
      },
      {
        h: "Definite integrals and area",
        b: "∫[a to b] f(x) dx = F(b) − F(a). Area between two curves: ∫[a to b] |f(x) − g(x)| dx. Check which function is on top in each interval."
      }
    ];
  })();

  // ── maths20: Probability ──────────────────────────────────────────────────
  (function () {
    var c = ch("maths20");
    // M20.1 — Probability — rules and distributions
    c.learningOutcomes[0].notes = [
      {
        h: "Basic rules",
        b: "P(A ∪ B) = P(A) + P(B) − P(A ∩ B). P(A|B) = P(A ∩ B) / P(B). Independent events: P(A ∩ B) = P(A) × P(B)."
      },
      {
        h: "Bernoulli trial",
        b: "A single experiment with exactly two outcomes: success (probability p) and failure (probability 1−p)."
      },
      {
        h: "Binomial distribution",
        b: "X ~ B(n, p). P(X = k) = C(n,k) × pᵏ × (1−p)ⁿ⁻ᵏ. Mean = np. Variance = np(1−p). Used when there are n independent Bernoulli trials."
      },
      {
        h: "Expected value",
        b: "E(X) = Σ x × P(X = x). For a binomial: E(X) = np. Use expected value to compare fair games or calculate long-run averages."
      }
    ];
  })();

  // ── maths21: Sequences & Series ───────────────────────────────────────────
  (function () {
    var c = ch("maths21");
    // M21.1 — Arithmetic and geometric sequences and series
    c.learningOutcomes[0].notes = [
      {
        h: "Arithmetic sequence",
        b: "Tₙ = a + (n−1)d where a = first term, d = common difference. Sₙ = n/2 × (2a + (n−1)d) = n/2 × (a + l) where l = last term."
      },
      {
        h: "Geometric sequence",
        b: "Tₙ = arⁿ⁻¹ where r = common ratio. Sₙ = a(1 − rⁿ)/(1 − r) for r ≠ 1. For infinite series: S∞ = a/(1−r) provided |r| < 1."
      },
      {
        h: "Identifying the type",
        b: "Check: if Tₙ₊₁ − Tₙ = constant ⟹ arithmetic. If Tₙ₊₁ / Tₙ = constant ⟹ geometric."
      },
      {
        h: "Sum to infinity",
        b: "A geometric series converges (has a finite sum to infinity) only when |r| < 1. If |r| ≥ 1 the series diverges."
      }
    ];
  })();

  // ── maths22: Statistics - Descriptive Statistics ──────────────────────────
  (function () {
    var c = ch("maths22");
    // M22.1 — Descriptive statistics
    c.learningOutcomes[0].notes = [
      {
        h: "Measures of centre",
        b: "Mean: x̄ = Σx / n (or Σfx / Σf for grouped data). Median: middle value when sorted. Mode: most frequent value."
      },
      {
        h: "Measures of spread",
        b: "Range = max − min. Standard deviation σ = √(Σ(x − x̄)² / n). Variance = σ². For a sample: use (n−1) in the denominator."
      },
      {
        h: "Grouped data",
        b: "Use midpoints of class intervals for mean and standard deviation calculations. Modal class = the class with the highest frequency."
      },
      {
        h: "Charts and plots",
        b: "Histogram: area proportional to frequency. Stem-and-leaf: preserves raw data. Box-and-whisker plot: shows five-number summary (min, Q1, median, Q3, max)."
      }
    ];
  })();

  // ── maths23: Statistics - Inferential Statistics ──────────────────────────
  (function () {
    var c = ch("maths23");
    // M23.1 — Hypothesis testing and confidence intervals
    c.learningOutcomes[0].notes = [
      {
        h: "Hypothesis testing (two-tailed)",
        b: "H₀: null hypothesis (e.g. μ = μ₀). H₁: alternative hypothesis. Calculate z = (x̄ − μ₀) / (σ/√n). If |z| > 1.96 (at 5% significance), reject H₀."
      },
      {
        h: "Confidence interval",
        b: "95% CI for a mean: x̄ ± 1.96 × (σ/√n). Interpretation: we are 95% confident the true population mean lies within this interval."
      },
      {
        h: "Margin of error",
        b: "Margin of error E = 1.96 × (σ/√n) for a 95% CI. For proportions: E ≈ 1/√n (approximate formula used in LC)."
      },
      {
        h: "p-value",
        b: "The probability of obtaining a result as extreme as the observed result, assuming H₀ is true. Reject H₀ if p-value < significance level (e.g. 0.05)."
      }
    ];
  })();

  // ── maths24: Statistics - Z Scores ────────────────────────────────────────
  (function () {
    var c = ch("maths24");
    // M24.1 — Normal distribution and z-scores
    c.learningOutcomes[0].notes = [
      {
        h: "Standard normal distribution",
        b: "Z ~ N(0, 1). The z-score tells you how many standard deviations a value is from the mean: z = (x − μ) / σ."
      },
      {
        h: "Using z-tables",
        b: "The LC tables give P(Z ≤ z) for z ≥ 0. For P(Z ≤ −z): use symmetry, P(Z ≤ −z) = 1 − P(Z ≤ z). For P(a ≤ Z ≤ b): subtract the two table values."
      },
      {
        h: "Finding x from a probability",
        b: "If P(X ≤ x) is given, find z from the table (inverse lookup), then x = μ + zσ."
      },
      {
        h: "Normal approximation to binomial",
        b: "For large n: X ~ B(n,p) ≈ N(np, np(1−p)). Apply a continuity correction: P(X ≤ k) ≈ P(Z ≤ (k + 0.5 − np)/√(np(1−p)))."
      }
    ];
  })();

  // ── maths25: Trigonometry - Functions & Identities ────────────────────────
  (function () {
    var c = ch("maths25");
    // M25.1 — Trig functions, identities and equations
    c.learningOutcomes[0].notes = [
      {
        h: "Fundamental identity",
        b: "sin²θ + cos²θ = 1. Derived identities: 1 + tan²θ = sec²θ; 1 + cot²θ = cosec²θ."
      },
      {
        h: "Double angle formulae",
        b: "sin 2A = 2 sin A cos A. cos 2A = cos²A − sin²A = 1 − 2sin²A = 2cos²A − 1. tan 2A = 2 tan A / (1 − tan²A)."
      },
      {
        h: "Compound angle formulae",
        b: "sin(A ± B) = sin A cos B ± cos A sin B. cos(A ± B) = cos A cos B ∓ sin A sin B. These are on the LC formula sheet."
      },
      {
        h: "General solution",
        b: "For sin θ = k: θ = sin⁻¹(k) + 360°n or θ = 180° − sin⁻¹(k) + 360°n. For cos θ = k: θ = ±cos⁻¹(k) + 360°n. For tan θ = k: θ = tan⁻¹(k) + 180°n."
      }
    ];
  })();

  // ── maths26: Trigonometry - Triangles ─────────────────────────────────────
  (function () {
    var c = ch("maths26");
    // M26.1 — Sine rule, cosine rule and area
    c.learningOutcomes[0].notes = [
      {
        h: "Sine rule",
        b: "a/sin A = b/sin B = c/sin C. Use when you know: two angles and one side (AAS), or two sides and a non-included angle (SSA — check for ambiguous case)."
      },
      {
        h: "Cosine rule",
        b: "a² = b² + c² − 2bc cos A. Rearranged: cos A = (b² + c² − a²) / 2bc. Use when you know: three sides (SSS), or two sides and the included angle (SAS)."
      },
      {
        h: "Area of a triangle",
        b: "Area = ½ab sin C. Use when you know two sides and the included angle. Always state which angle is between the two given sides."
      },
      {
        h: "3D problems",
        b: "Identify the relevant triangles within the 3D figure. Apply sine/cosine rule or Pythagoras to each triangle in turn. Draw and label each triangle clearly."
      }
    ];
  })();

})();