# Package: chem19-s3 — pH calculations

- **loId:** `chem19-s3` · **chapterId:** `chem19` · **syllabusRef:** 3.4.8
- **Syllabus:** 3.4.8 "**solve mathematical problems involving pH for dilute aqueous
  solutions**". Learn about: "**problems involving pH to include: dilute aqueous solutions of
  strong acids and bases; dilute aqueous solutions of weak acids and bases involving
  appropriate Ka and Kb values (mixtures not required)**". All bold: the whole subsection is
  Higher Level only. Mark every block heading " (Higher Level only)".
- **Prepared by:** a higher model, 2026-10-30. The method for each of the four solution types,
  each with worked examples one step per bullet, then reverse problems. Every number has been
  checked in Python. The definition of pH and converting pH ↔ [H⁺] are in "pH and its
  measurement"; Kw and pH + pOH = 14 are in "Self-ionisation of water"; the Ka and Kb
  expressions and where the √(Ka × c) formula comes from are in "Dissociation constants".
  Use them; don't re-derive them here.

## 1. Must cover

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

## 2. Checked facts and examples

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

## 3. Traps

- Don't use √(Ka × c) for a strong acid, or [H⁺] = c for a weak acid.
- Sulfuric acid gives 2H⁺ and calcium hydroxide 2OH⁻ per formula unit.
- pH + pOH = 14 only at 25 °C.
- Volumes in cm³ must be converted to litres before finding mol L⁻¹.
- Mixtures (e.g. the pH after mixing an acid and a base, or buffer calculations) are not required.
- The √(Ka × c) formula is not in the *Formulae and Tables* booklet; learn it.

## 4. What exams ask (topics only)

- Calculate the pH of a strong acid, strong base, weak acid (given Ka) or weak base (given Kb) of given concentration.
- Calculate pH from a mass of solute dissolved in a stated volume.
- Calculate the concentration of a strong acid with a given pH, or [OH⁻] in a solution of given pH.
- Calculate Ka from the pH and concentration of a weak acid.

## 5. Practice questions to write

1. 9 marks: "Calculate the pH of (i) 0.20 M nitric acid, (ii) 0.040 M potassium hydroxide, (iii) 0.020 M sulfuric acid." Model answer: (i) pH = −log₁₀(0.20) = 0.70; (ii) pOH = −log₁₀(0.040) = 1.40, pH = 12.60; (iii) [H⁺] = 0.040, pH = 1.40.
2. 9 marks: "Calculate the pH of (i) a 0.20 M solution of ethanoic acid (Ka = 1.8 × 10⁻⁵), (ii) a 0.20 M solution of ammonia (Kb = 1.8 × 10⁻⁵)." Model answer: (i) [H⁺] = √(3.6 × 10⁻⁶) = 1.90 × 10⁻³ mol L⁻¹, pH = 2.72; (ii) [OH⁻] = 1.90 × 10⁻³, pOH = 2.72, pH = 11.28.
3. 9 marks: "A 0.050 M solution of a weak monoprotic acid has a pH of 2.90. Calculate the Ka of the acid, and the concentration of a strong monoprotic acid that would have the same pH." Model answer: [H⁺] = 10⁻²·⁹⁰ = 1.26 × 10⁻³ mol L⁻¹; Ka = (1.26 × 10⁻³)² ÷ 0.050 = 3.17 × 10⁻⁵ (keeping the unrounded [H⁺] in the calculator); strong acid concentration = 1.26 × 10⁻³ mol L⁻¹.
