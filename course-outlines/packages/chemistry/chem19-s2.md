# Package: chem19-s2 — pH calculations and dissociation constants

- **loId:** `chem19-s2` · **chapterId:** `chem19` · **syllabusRef:** 3.4.8, 3.4.9, 3.4.10
- **Merged:** this subsection combines "pH calculations" (formerly `chem19-s3`), "Dissociation constants" (formerly `chem19-s4`), "Degree of dissociation" (formerly `chem19-s5`). Each part below is the package for one of them; write the notes as one subsection, in this order.

## Part: pH calculations (formerly `chem19-s3`)

- **loId:** `chem19-s3` · **chapterId:** `chem19` · **syllabusRef:** 3.4.8
- **Syllabus:** 3.4.8 "**solve mathematical problems involving pH for dilute aqueous
  solutions**". Learn about: "**problems involving pH to include: dilute aqueous solutions of
  strong acids and bases; dilute aqueous solutions of weak acids and bases involving
  appropriate Ka and Kb values (mixtures not required)**". All bold: the whole subsection is
  Higher Level only. Mark every block heading " (Higher Level only)".
- **Prepared by:** a higher model, 2026-10-30. The method for each of the four solution types,
  each with worked examples one step per bullet, then reverse problems. Every number has been
  checked in Python. The definition of pH and converting pH ↔ [H⁺] are in "pH and its
  measurement"; Kw and pH + pOH = 14 are in "Self-ionisation of water and pH"; the Ka and Kb
  expressions and where the √(Ka × c) formula comes from are in "Dissociation constants".
  Use them; don't re-derive them here.

### 1. Must cover

Strong acids (Higher Level only; one block)
- [ ] A1 [HL] A strong acid is fully dissociated, so [H⁺] = concentration of the acid × number of H⁺ released per formula unit (the basicity).
- [ ] A2 [HL] Monoprotic (monobasic) strong acids, HCl and HNO₃: [H⁺] = [acid]. Example: 0.010 M HCl: [H⁺] = 0.010 mol L⁻¹; pH = −log₁₀(0.010) = 2.00.
- [ ] A3 [HL] Example: 0.025 M HCl: pH = −log₁₀(0.025) = 1.60.
- [ ] A4 [HL] Sulfuric acid is diprotic and is treated as fully dissociated: H₂SO₄ → 2H⁺ + SO₄²⁻, so [H⁺] = 2 × [H₂SO₄]. Example: 0.050 M H₂SO₄: [H⁺] = 0.10 mol L⁻¹; pH = 1.00.

Strong acid from a mass (Higher Level only; one block, one step per bullet)
- [ ] B1 [HL] Problem: 5.0 g of sulfuric acid (H₂SO₄ = 98 g mol⁻¹) is dissolved in water and made up to 250 cm³. Find the pH.
- [ ] B2 [HL] Step 1: Concentration in g L⁻¹ = 5.0 ÷ 0.250 = 20 g L⁻¹.
- [ ] B3 [HL] Step 2: Concentration in mol L⁻¹ = 20 ÷ 98 = 0.204 mol L⁻¹.
- [ ] B4 [HL] Step 3: [H⁺] = 2 × 0.204 = 0.408 mol L⁻¹.
- [ ] B5 [HL] Step 4: pH = −log₁₀(0.408) = 0.39.

Strong bases (Higher Level only; one block)
- [ ] S1 [HL] A strong base is fully dissociated, so [OH⁻] = concentration of the base × number of OH⁻ per formula unit (NaOH, KOH: 1; Ca(OH)₂: 2).
- [ ] S2 [HL] Method: find [OH⁻]; pOH = −log₁₀[OH⁻]; pH = 14 − pOH (at 25 °C). Or: [H⁺] = Kw ÷ [OH⁻] = 1.0 × 10⁻¹⁴ ÷ [OH⁻], then pH = −log₁₀[H⁺]. Both give the same answer.
- [ ] S3 [HL] Example: 0.010 M NaOH: [OH⁻] = 0.010; pOH = 2.00; pH = 14 − 2.00 = 12.00.
- [ ] S4 [HL] Example: 0.15 M NaOH: pOH = −log₁₀(0.15) = 0.82; pH = 13.18.
- [ ] S5 [HL] Example: 0.010 M Ca(OH)₂: Ca(OH)₂ → Ca²⁺ + 2OH⁻, so [OH⁻] = 0.020 mol L⁻¹; pOH = 1.70; pH = 12.30.
- [ ] S6 [HL] Example from a mass: 9.0 g of KOH (56 g mol⁻¹) made up to 500 cm³: 18 g L⁻¹ ÷ 56 = 0.321 mol L⁻¹ = [OH⁻]; pOH = 0.49; pH = 13.51.

Weak acids (Higher Level only; one block)
- [ ] W1 [HL] A weak acid is only slightly dissociated, so [H⁺] is much less than the acid concentration and must be found from Ka.
- [ ] W2 [HL] Formula: [H⁺] = √(Ka × c), where c is the concentration of the acid in mol L⁻¹ (derived in "Dissociation constants"); this formula must be learned.
- [ ] W3 [HL] It assumes the acid is monoprotic, that the amount dissociated is very small compared with c (so c − x ≈ c), and that the H⁺ from water is negligible.
- [ ] W4 [HL] Example: 0.10 M ethanoic acid, Ka = 1.8 × 10⁻⁵: [H⁺] = √(1.8 × 10⁻⁵ × 0.10) = √(1.8 × 10⁻⁶) = 1.34 × 10⁻³ mol L⁻¹; pH = −log₁₀(1.34 × 10⁻³) = 2.87.
- [ ] W5 [HL] Example: 0.50 M ethanoic acid: [H⁺] = √(1.8 × 10⁻⁵ × 0.50) = √(9.0 × 10⁻⁶) = 3.0 × 10⁻³ mol L⁻¹; pH = 2.52.
- [ ] W6 [HL] Example: 0.10 M methanoic acid, Ka = 1.8 × 10⁻⁴: [H⁺] = √(1.8 × 10⁻⁵) = 4.24 × 10⁻³ mol L⁻¹; pH = 2.37 (a lower pH than ethanoic acid at the same concentration, because methanoic acid is the stronger acid).
- [ ] W7 [HL] Example from a mass: 1.48 g of propanoic acid (CH₃CH₂COOH, 74 g mol⁻¹) in 200 cm³: moles = 1.48 ÷ 74 = 0.0200 mol; c = 0.0200 ÷ 0.200 = 0.100 mol L⁻¹; Ka = 1.3 × 10⁻⁵; [H⁺] = √(1.3 × 10⁻⁵ × 0.100) = 1.14 × 10⁻³ mol L⁻¹; pH = 2.94.

Weak bases (Higher Level only; one block)
- [ ] K1 [HL] Formula: [OH⁻] = √(Kb × c), with the same assumptions as W3; then pOH = −log₁₀[OH⁻] and pH = 14 − pOH.
- [ ] K2 [HL] Example: 0.10 M ammonia, Kb = 1.8 × 10⁻⁵: [OH⁻] = √(1.8 × 10⁻⁵ × 0.10) = 1.34 × 10⁻³ mol L⁻¹; pOH = 2.87; pH = 14 − 2.87 = 11.13.
- [ ] K3 [HL] Example: 0.050 M ammonia: [OH⁻] = √(1.8 × 10⁻⁵ × 0.050) = 9.49 × 10⁻⁴ mol L⁻¹; pOH = 3.02; pH = 10.98.

Reverse problems (Higher Level only; one block)
- [ ] R1 [HL] Concentration of a strong acid from its pH: [acid] = [H⁺] = 10⁻ᵖᴴ for a monoprotic acid. Example: a strong monoprotic acid HX with pH 5.65 has [HX] = 10⁻⁵·⁶⁵ = 2.24 × 10⁻⁶ mol L⁻¹.
- [ ] R2 [HL] [OH⁻] from pH: [OH⁻] = Kw ÷ [H⁺]. Example: pH 5.65: pOH = 14 − 5.65 = 8.35, so [OH⁻] = 10⁻⁸·³⁵ = 4.47 × 10⁻⁹ mol L⁻¹ (the same as 1.0 × 10⁻¹⁴ ÷ 10⁻⁵·⁶⁵).
- [ ] R3 [HL] Ka of a weak acid from its pH: [H⁺] = 10⁻ᵖᴴ, then Ka = [H⁺]² ÷ c. Example: 0.10 M weak monoprotic acid with pH 3.00: [H⁺] = 1.0 × 10⁻³; Ka = (1.0 × 10⁻³)² ÷ 0.10 = 1.0 × 10⁻⁵.
- [ ] R4 [HL] Concentration of a weak acid from its pH and Ka: c = [H⁺]² ÷ Ka. Example: ethanoic acid of pH 3.00: c = (1.0 × 10⁻³)² ÷ 1.8 × 10⁻⁵ = 0.0556 mol L⁻¹.

Good practice (Higher Level only; one block)
- [ ] G1 [HL] First decide: acid or base? Strong or weak? For a strong species use the concentration directly; for a weak species use √(Ka × c) or √(Kb × c).
- [ ] G2 [HL] For any base, find [OH⁻] first, then convert to pH; don't put [OH⁻] into −log₁₀ and call it pH.
- [ ] G3 [HL] Convert masses to mol L⁻¹ first (n = m ÷ M; c = n ÷ V in litres).
- [ ] G4 [HL] Check the answer is sensible: acids below 7, bases above 7; a weak acid has a higher pH than a strong acid of the same concentration.
- [ ] G5 [HL] pH answers are usually given to two decimal places.

### 2. Checked facts and examples

| Item | Fact |
|---|---|
| W4, W5 | Ka(ethanoic acid, CH₃COOH) = 1.8 × 10⁻⁵ at 25 °C. |
| W6 | Ka(methanoic acid, HCOOH) = 1.8 × 10⁻⁴ at 25 °C. |
| W7 | Ka(propanoic acid) = 1.3 × 10⁻⁵ at 25 °C. |
| K2, K3 | Kb(ammonia, NH₃) = 1.8 × 10⁻⁵ at 25 °C. |
| B1, S6, W7 | M: H₂SO₄ 98; KOH 56; CH₃CH₂COOH 74 g mol⁻¹. |

All worked examples are checked; values are for 25 °C (Kw = 1.0 × 10⁻¹⁴). The exact
quadratic answer for 0.10 M ethanoic acid is pH 2.88, so the approximation W2 is good to about
0.01 pH unit.

### 3. Traps

- Don't use √(Ka × c) for a strong acid, or [H⁺] = c for a weak acid.
- Sulfuric acid gives 2H⁺ and calcium hydroxide 2OH⁻ per formula unit.
- pH + pOH = 14 only at 25 °C.
- Volumes in cm³ must be converted to litres before finding mol L⁻¹.
- Mixtures (e.g. the pH after mixing an acid and a base, or buffer calculations) are not required.
- The √(Ka × c) formula is not in the *Formulae and Tables* booklet; learn it.

### 4. What exams ask (topics only)

- Calculate the pH of a strong acid, strong base, weak acid (given Ka) or weak base (given Kb) of given concentration.
- Calculate pH from a mass of solute dissolved in a stated volume.
- Calculate the concentration of a strong acid with a given pH, or [OH⁻] in a solution of given pH.
- Calculate Ka from the pH and concentration of a weak acid.

### 5. Practice questions to write

1. 9 marks: "Calculate the pH of (i) 0.20 M nitric acid, (ii) 0.040 M potassium hydroxide, (iii) 0.020 M sulfuric acid." Model answer: (i) pH = −log₁₀(0.20) = 0.70; (ii) pOH = −log₁₀(0.040) = 1.40, pH = 12.60; (iii) [H⁺] = 0.040, pH = 1.40.
2. 9 marks: "Calculate the pH of (i) a 0.20 M solution of ethanoic acid (Ka = 1.8 × 10⁻⁵), (ii) a 0.20 M solution of ammonia (Kb = 1.8 × 10⁻⁵)." Model answer: (i) [H⁺] = √(3.6 × 10⁻⁶) = 1.90 × 10⁻³ mol L⁻¹, pH = 2.72; (ii) [OH⁻] = 1.90 × 10⁻³, pOH = 2.72, pH = 11.28.
3. 9 marks: "A 0.050 M solution of a weak monoprotic acid has a pH of 2.90. Calculate the Ka of the acid, and the concentration of a strong monoprotic acid that would have the same pH." Model answer: [H⁺] = 10⁻²·⁹⁰ = 1.26 × 10⁻³ mol L⁻¹; Ka = (1.26 × 10⁻³)² ÷ 0.050 = 3.17 × 10⁻⁵ (keeping the unrounded [H⁺] in the calculator); strong acid concentration = 1.26 × 10⁻³ mol L⁻¹.

## Part: Dissociation constants (formerly `chem19-s4`)

- **loId:** `chem19-s4` · **chapterId:** `chem19` · **syllabusRef:** 3.4.9
- **Syllabus:** 3.4.9 "**deduce mathematical representations for weak acid dissociation
  constant (Ka) and weak base dissociation constant (Kb)**". Learn about: "dissociation of
  acids (HA) and bases (BOH): **Ka = [H₃O⁺][A⁻] ÷ [HA] and Kb = [B⁺][OH⁻] ÷ [B]**". Bold =
  Higher Level only. The outcome is all bold; only the learn-about phrase "dissociation of acids
  (HA) and bases (BOH)" is normal type, so the first block is unmarked and the rest is Higher
  Level.
- **Prepared by:** a higher model, 2026-10-30. The dissociation equations (normal), then
  deducing Ka and Kb, what their values mean, and the derivation of [H⁺] = √(Ka × c) used in "pH
  calculations" (Higher Level). Writing Kc expressions is in "Dynamic equilibrium and Kc"; strong
  vs weak is in "Acid–base theories and strength"; conjugate pairs and the strength of
  conjugates are in "Acid–base theories and strength"; comparing acids by Ka and percentage
  dissociation is in "Degree of dissociation". Don't repeat them.

### 1. Must cover

Dissociation of acids and bases (one block)
- [ ] D1 A general acid is written HA. In water it dissociates by donating a proton to water: HA(aq) + H₂O(l) ⇌ H₃O⁺(aq) + A⁻(aq), or simply HA(aq) ⇌ H⁺(aq) + A⁻(aq).
- [ ] D2 Example: ethanoic acid, CH₃COOH(aq) ⇌ CH₃COO⁻(aq) + H⁺(aq); A⁻ is the ethanoate ion.
- [ ] D3 A general base that contains hydroxide is written BOH: BOH(aq) ⇌ B⁺(aq) + OH⁻(aq).
- [ ] D4 A base such as ammonia (written B) produces OH⁻ by accepting a proton from water: NH₃(aq) + H₂O(l) ⇌ NH₄⁺(aq) + OH⁻(aq); here B⁺ is the ammonium ion, NH₄⁺ (BH⁺ in some books).
- [ ] D5 For a strong acid or base the dissociation goes to completion (single arrow →); for a weak acid or base it is an equilibrium (⇌) that lies well to the left.

Deducing Ka (Higher Level only; one block, one step per bullet)
- [ ] A1 [HL] Step 1: Write the equilibrium: HA + H₂O ⇌ H₃O⁺ + A⁻.
- [ ] A2 [HL] Step 2: Write Kc as products over reactants: Kc = [H₃O⁺][A⁻] ÷ ([HA][H₂O]).
- [ ] A3 [HL] Step 3: In a dilute solution [H₂O] is effectively constant (55.6 mol L⁻¹), so it is combined with Kc: Ka = Kc × [H₂O].
- [ ] A4 [HL] Result: Ka = [H₃O⁺][A⁻] ÷ [HA], or in simplified form Ka = [H⁺][A⁻] ÷ [HA]. Ka is the acid dissociation constant.
- [ ] A5 [HL] Example: for ethanoic acid, Ka = [CH₃COO⁻][H⁺] ÷ [CH₃COOH] = 1.8 × 10⁻⁵ at 25 °C.
- [ ] A6 [HL] Units of Ka are mol L⁻¹ (concentration² ÷ concentration); they are often omitted.

Deducing Kb (Higher Level only; one block)
- [ ] B1 [HL] For B + H₂O ⇌ B⁺ + OH⁻ (or BOH ⇌ B⁺ + OH⁻), the same steps give the base dissociation constant: Kb = [B⁺][OH⁻] ÷ [B] (or [B⁺][OH⁻] ÷ [BOH]); [H₂O] is again constant and absorbed into Kb.
- [ ] B2 [HL] Example: for ammonia, Kb = [NH₄⁺][OH⁻] ÷ [NH₃] = 1.8 × 10⁻⁵ at 25 °C.

What Ka and Kb tell you (Higher Level only; one block)
- [ ] M1 [HL] Ka measures the strength of an acid, its tendency to donate a proton: the larger Ka, the further the equilibrium lies to the right and the stronger the acid. Likewise, the larger Kb, the stronger the base.
- [ ] M2 [HL] Weak acids have small Ka values (much less than 1): e.g. methanoic acid 1.8 × 10⁻⁴, benzoic acid 6.3 × 10⁻⁵, ethanoic acid 1.8 × 10⁻⁵, propanoic acid 1.3 × 10⁻⁵ (strongest to weakest).
- [ ] M3 [HL] Strong acids (HCl, HNO₃, H₂SO₄) and strong bases (NaOH, KOH) dissociate essentially completely, so their Ka or Kb values are very large and the expressions are not used; Ka and Kb are used for weak acids and bases.
- [ ] M4 [HL] Like all equilibrium constants, Ka and Kb are constant at a given temperature and don't change with concentration; values are quoted at 25 °C.

Deriving [H⁺] = √(Ka × c) (Higher Level only; one block, one step per bullet)
- [ ] F1 [HL] Step 1: Start with c mol L⁻¹ of a weak acid HA; let x mol L⁻¹ dissociate. At equilibrium: [HA] = c − x, [H⁺] = x, [A⁻] = x.
- [ ] F2 [HL] Step 2: Ka = x × x ÷ (c − x) = x² ÷ (c − x).
- [ ] F3 [HL] Step 3: A weak acid dissociates so little that x is tiny compared with c, so c − x ≈ c and Ka = x² ÷ c.
- [ ] F4 [HL] Step 4: x² = Ka × c, so [H⁺] = √(Ka × c).
- [ ] F5 [HL] The same steps for a weak base give [OH⁻] = √(Kb × c). Worked uses of both formulas are in "pH calculations".

### 2. Checked facts and examples

| Item | Fact |
|---|---|
| A5, M2 | Ka at 25 °C: methanoic acid 1.8 × 10⁻⁴; benzoic acid 6.3 × 10⁻⁵; ethanoic acid 1.8 × 10⁻⁵; propanoic acid 1.3 × 10⁻⁵. |
| B2 | Kb(NH₃) = 1.8 × 10⁻⁵ at 25 °C. |
| A3 | [H₂O] = 1000 ÷ 18 = 55.6 mol L⁻¹. |

### 3. Traps

- Don't put [H₂O] in the Ka or Kb expression.
- Products go on top: Ka = [H⁺][A⁻] ÷ [HA], not the reverse.
- Ka and Kb measure strength, not concentration; they don't change on dilution (the degree of dissociation does: see "Degree of dissociation").
- The approximation c − x ≈ c is valid only for weak acids and bases.
- Ka of indicators is not required (see "Titration curves, indicators and vinegar").

### 4. What exams ask (topics only)

- Write the Ka expression for a named weak acid, or Kb for ammonia; explain why [H₂O] is left out.
- Explain what Ka (or Kb) indicates about an acid (or base); use Ka values to decide which acid is stronger.
- Is a given acid strong or weak? Give a reason (its small Ka, or its partial dissociation).

### 5. Practice questions to write

1. 6 marks: "Write equations for the dissociation in water of (i) a weak acid HA, (ii) ammonia, and state the difference between the dissociation of a strong acid and a weak acid." Model answer: D1, D4, D5.
2. 9 marks (Higher Level): "Write the expression for the acid dissociation constant, Ka, of ethanoic acid. Explain why [H₂O] does not appear in it, and what a small Ka value tells you about the acid." Model answer: A5, A3, M1.
3. 9 marks (Higher Level): "Starting from the Ka expression, show that the hydrogen ion concentration of a weak acid of concentration c is approximately √(Ka × c), stating the assumption made." Model answer: F1–F4.

## Part: Degree of dissociation (formerly `chem19-s5`)

- **loId:** `chem19-s5` · **chapterId:** `chem19` · **syllabusRef:** 3.4.10
- **Syllabus:** 3.4.10 "compare degrees of dissociation of strong and weak acids, and strong
  and weak bases, **using Ka and Kb values**". Bold = Higher Level only: the comparison itself
  is normal type; doing it with Ka and Kb values is Higher Level.
- **Prepared by:** a higher model, 2026-10-30. What the degree of dissociation is and how strong
  and weak species compare (normal), then calculating and comparing it from Ka and Kb, the
  effect of dilution, and the Ka–Kb link for conjugate pairs (Higher Level). The definitions of
  strong and weak and the experimental evidence (pH, conductivity, rate with magnesium) are in
  "Acid–base theories and strength"; the Ka and Kb expressions are in "Dissociation
  constants"; pH calculations are in "pH calculations"; conjugate pairs are in "Applying
  Brønsted–Lowry theory". Point to them; don't repeat.

### 1. Must cover

Degree of dissociation (one block)
- [ ] D1 The degree of dissociation is the fraction of the acid (or base) molecules that have dissociated into ions in solution; as a percentage: % dissociation = (concentration dissociated ÷ initial concentration) × 100.
- [ ] D2 For an acid HA: % dissociation = ([H⁺] at equilibrium ÷ initial [HA]) × 100; for a base: ([OH⁻] ÷ initial [base]) × 100.
- [ ] D3 Strong acids (HCl, HNO₃, H₂SO₄) and strong bases (NaOH, KOH) are essentially 100% dissociated in dilute solution: the reaction goes to completion.
- [ ] D4 Weak acids (e.g. ethanoic acid) and weak bases (e.g. ammonia) are only slightly dissociated, typically a few per cent or less: 0.10 M ethanoic acid is about 1.3% dissociated, so about 99 out of every 100 molecules remain as CH₃COOH.
- [ ] D5 So at the same concentration a strong acid gives a much higher [H⁺] than a weak acid (lower pH, better conductivity, faster reaction with magnesium); the evidence is in "Acid–base theories and strength".
- [ ] D6 In terms of Brønsted–Lowry theory, a strong acid is a good proton donor whose conjugate base (e.g. Cl⁻) has almost no tendency to take the proton back, so the equilibrium lies completely to the right; a weak acid's conjugate base (e.g. CH₃COO⁻) readily takes the proton back, so the equilibrium lies to the left.

Using Ka and Kb values (Higher Level only; one block)
- [ ] K1 [HL] At the same concentration and temperature, the acid with the larger Ka is dissociated to a greater degree and is the stronger acid; the base with the larger Kb is the stronger base.
- [ ] K2 [HL] Example: methanoic acid (Ka 1.8 × 10⁻⁴) is a stronger acid than ethanoic acid (Ka 1.8 × 10⁻⁵): at 0.10 M, methanoic acid is 4.2% dissociated and ethanoic acid 1.3%.
- [ ] K3 [HL] Formula: degree of dissociation (fraction) = [H⁺] ÷ c = √(Ka × c) ÷ c = √(Ka ÷ c); for a weak base, √(Kb ÷ c).
- [ ] K4 [HL] Worked example: 0.10 M ethanoic acid: [H⁺] = √(1.8 × 10⁻⁵ × 0.10) = 1.34 × 10⁻³ mol L⁻¹; % dissociation = (1.34 × 10⁻³ ÷ 0.10) × 100 = 1.34%.
- [ ] K5 [HL] Worked example: 0.10 M ammonia (Kb 1.8 × 10⁻⁵): [OH⁻] = 1.34 × 10⁻³ mol L⁻¹, so 1.34% of the ammonia has reacted to form NH₄⁺ and OH⁻.
- [ ] K6 [HL] A very small Ka (or Kb) means a very low degree of dissociation; the Ka values of strong acids are so large that dissociation is complete, which is why Ka is used only to compare weak acids.

Effect of dilution (Higher Level only; one block)
- [ ] E1 [HL] Ka is constant at a given temperature, but the degree of dissociation of a weak acid increases as the solution is diluted, because √(Ka ÷ c) gets larger as c gets smaller.
- [ ] E2 [HL] Example: ethanoic acid is 0.42% dissociated at 1.0 M, 1.34% at 0.10 M and 4.2% at 0.010 M.
- [ ] E3 [HL] Le Châtelier explanation: dilution lowers the concentration of all species, and the equilibrium HA ⇌ H⁺ + A⁻ shifts to the right (the side with more dissolved particles) to oppose the change.
- [ ] E4 [HL] Even though the degree of dissociation rises, [H⁺] still falls on dilution, so the pH still rises (see "Self-ionisation of water and pH").
- [ ] E5 [HL] A strong acid is fully dissociated at every dilute concentration, so its degree of dissociation does not change on dilution.

Conjugate pairs and Ka × Kb (Higher Level only; one block)
- [ ] C1 [HL] For a conjugate acid–base pair in water, Ka (of the acid) × Kb (of its conjugate base) = Kw = 1.0 × 10⁻¹⁴ at 25 °C.
- [ ] C2 [HL] So the larger the Ka of an acid, the smaller the Kb of its conjugate base: the stronger the acid, the weaker its conjugate base.
- [ ] C3 [HL] Example: Kb of the ethanoate ion = 1.0 × 10⁻¹⁴ ÷ 1.8 × 10⁻⁵ = 5.6 × 10⁻¹⁰; Ka of the ammonium ion = 1.0 × 10⁻¹⁴ ÷ 1.8 × 10⁻⁵ = 5.6 × 10⁻¹⁰.

### 2. Checked facts and examples

| Item | Fact |
|---|---|
| K2, K4, E2 | Ka(ethanoic acid) 1.8 × 10⁻⁵; Ka(methanoic acid) 1.8 × 10⁻⁴; % dissociation: ethanoic 0.42% (1.0 M), 1.34% (0.10 M), 4.2% (0.010 M); methanoic 4.2% (0.10 M) (checked). |
| K5, C3 | Kb(NH₃) = 1.8 × 10⁻⁵; Kb(CH₃COO⁻) = Ka(NH₄⁺) = 5.6 × 10⁻¹⁰ (checked). |

### 3. Traps

- Degree of dissociation measures strength only when acids are compared at the same concentration; it changes with concentration, while Ka does not.
- Diluting a weak acid raises its percentage dissociation but lowers its [H⁺].
- "Strong" means fully dissociated, not concentrated (see "Acid–base theories and strength").
- Don't use Ka to describe HCl; it is fully dissociated.
- Mixtures and buffers are not required.

### 4. What exams ask (topics only)

- Compare the degree of dissociation of a strong and a weak acid (or base).
- Use Ka values to decide which of two weak acids is stronger and justify the choice.
- Calculate the approximate percentage dissociation of a weak acid of given concentration and Ka.

### 5. Practice questions to write

1. 6 marks: "Compare the degree of dissociation of 0.10 M hydrochloric acid and 0.10 M ethanoic acid, and explain, using conjugate bases, why they differ." Model answer: D1, D3, D4, D6.
2. 9 marks (Higher Level): "Benzoic acid has Ka = 6.3 × 10⁻⁵ and propanoic acid has Ka = 1.3 × 10⁻⁵. State which is the stronger acid and calculate the percentage dissociation of each in a 0.10 M solution." Model answer: K1 (benzoic acid, larger Ka); benzoic: √(6.3 × 10⁻⁵ ÷ 0.10) × 100 = 2.5%; propanoic: √(1.3 × 10⁻⁵ ÷ 0.10) × 100 = 1.1%.
3. 6 marks (Higher Level): "Explain why the percentage dissociation of ethanoic acid increases when the solution is diluted, even though its Ka stays the same." Model answer: E1, E2, E3.
