# Package: bio31-s4 — Simpson's Diversity Index

- **loId:** `bio31-s4` · **chapterId:** `bio31` · **syllabusRef:** 3.1.4
- **Syllabus (Higher Level only):** "species diversity index, Ds, the variety of species in a
  given area, calculated using the Simpson's Diversity Index Equation: Ds = 1 − Σn(n−1) /
  N(N−1); n = total number of organisms of a particular species; N = total number of organisms
  of all species." Outcome 4: "model species diversity in ecosystems using the Simpson's
  Diversity Index equation."
- **Level:** every block in this subsection ends its heading with " (Higher Level only)".
- **Prepared by:** a higher model, 2026-10-29. "Model" means use the equation to calculate
  and compare diversity, and interpret the values. All arithmetic below has been checked.
  Write the equation in plain text exactly as: Ds = 1 − Σn(n − 1) / N(N − 1), and say in words
  that the sum Σn(n − 1) is divided by N(N − 1). Species richness and evenness are defined in
  "Biosphere, ecosystems, habitats and biodiversity"; use them without redefining.

## 1. Must cover

The index (one block)
- [ ] I1 A diversity index is a single number that measures the species diversity of a sample, taking into account both the number of species (richness) and how evenly the individuals are spread among them (evenness). Simpson's Diversity Index is the one in the specification.
- [ ] I2 The equation: Ds = 1 − Σn(n − 1) / N(N − 1), where n is the total number of organisms of a particular species, N is the total number of organisms of all species in the sample, and Σ (the Greek capital letter sigma) means "the sum of", so n(n − 1) is worked out for each species and the results are added.
- [ ] I3 What it means: Ds is the probability that two individuals picked at random from the sample (the first not put back) belong to different species. Σn(n − 1) / N(N − 1) is the probability that both belong to the same species, and Ds is 1 minus this.
- [ ] I4 Range of values: Ds lies between 0 and 1. Ds = 0 when only one species is present (no diversity). The closer Ds is to 1, the higher the diversity. For a given number of species, Ds is highest when all species have equal numbers. A species represented by one individual contributes 1 × 0 = 0 to the sum.
- [ ] I5 Why it is better than species richness alone: it gives less weight to rare species and shows when a habitat is dominated by one or two species. Two samples with the same species list can have very different Ds.

Method (one Skills block)
- [ ] M1 1. Draw a table with columns: species, n, n − 1, n(n − 1). 2. Fill in n for each species from the sample. 3. Calculate n − 1, then n(n − 1), for each species. 4. Add the n column to get N. 5. Add the n(n − 1) column to get Σn(n − 1). 6. Calculate N(N − 1). 7. Divide Σn(n − 1) by N(N − 1). 8. Subtract the answer from 1 to get Ds. 9. Give Ds to two decimal places and interpret it (compare it with another sample, or say whether it is near 0 or 1).
- [ ] M2 Common errors: using n² instead of n(n − 1); forgetting to subtract from 1; working out N(N − 1) for each species instead of once for the whole sample; rounding too early (keep four decimal places until the last step).

Worked example 1: an untrampled meadow (one block)
- [ ] W1 Sample: daisy 10, dandelion 5, white clover 3, buttercup 2. N = 10 + 5 + 3 + 2 = 20.
- [ ] W2 n(n − 1): daisy 10 × 9 = 90; dandelion 5 × 4 = 20; clover 3 × 2 = 6; buttercup 2 × 1 = 2. Σn(n − 1) = 90 + 20 + 6 + 2 = 118.
- [ ] W3 N(N − 1) = 20 × 19 = 380. Σn(n − 1) / N(N − 1) = 118 / 380 = 0.31 (0.3105). Ds = 1 − 0.3105 = 0.69.

Worked example 2: a trampled path in the same field (one block)
- [ ] W4 Sample: daisy 16, dandelion 2, white clover 1, buttercup 1. N = 20. Same four species (same richness) as example 1.
- [ ] W5 n(n − 1): daisy 16 × 15 = 240; dandelion 2 × 1 = 2; clover 1 × 0 = 0; buttercup 1 × 0 = 0. Σn(n − 1) = 242.
- [ ] W6 N(N − 1) = 380. 242 / 380 = 0.64 (0.6368). Ds = 1 − 0.6368 = 0.36.
- [ ] W7 Interpretation: both samples have four species and 20 plants, but the path is dominated by one trampling-tolerant species (daisy), so its evenness and its diversity are lower (0.36 against 0.69). Species richness alone would have shown no difference. (Link to "Investigation: human activity and species diversity".)

Worked example 3: comparing evenness and richness (one block)
- [ ] W8 Perfectly even sample: four species with 5 individuals each. N = 20. n(n − 1) = 5 × 4 = 20 for each, so Σn(n − 1) = 80. 80 / 380 = 0.2105. Ds = 0.79, the highest possible for four species and 20 individuals.
- [ ] W9 One species only: 20 individuals of one species. Σn(n − 1) = 20 × 19 = 380; 380 / 380 = 1; Ds = 1 − 1 = 0.
- [ ] W10 A richer sample, e.g. a rocky-shore quadrat: barnacles 12, limpets 8, dog whelks 6, periwinkles 3, beadlet anemone 1. N = 30. n(n − 1): 132, 56, 30, 6, 0; Σn(n − 1) = 224. N(N − 1) = 30 × 29 = 870. 224 / 870 = 0.2575. Ds = 0.74.
- [ ] W11 A six-species sample: 9, 6, 4, 3, 2, 1. N = 25. n(n − 1): 72, 30, 12, 6, 2, 0; Σ = 122. N(N − 1) = 25 × 24 = 600. 122 / 600 = 0.2033. Ds = 0.80.

Using the index (one block)
- [ ] U1 Uses: comparing the diversity of two habitats or sites (e.g. trampled and untrampled grassland, upstream and downstream of a pollution source, a native woodland and a conifer plantation); monitoring the same site over time to see if diversity is falling or recovering (e.g. after bog rewetting or a change in farming); judging the effect of conservation or human activity.
- [ ] U2 A high Ds generally indicates a stable, healthy ecosystem that is more resilient to change; a low Ds indicates domination by a few species, often after disturbance or pollution.
- [ ] U3 Limitations: it depends on accurate identification and counting; samples must be large and taken at random, by the same method, for a fair comparison; it is hard to count individual plants that grow in clumps (e.g. grasses), so percentage cover is sometimes used instead, which this equation does not take; it treats all species as equally important, so it does not show whether the species are native, rare or invasive; a sample is a snapshot at one time of year.
- [ ] U4 Other versions of Simpson's index exist in textbooks and websites (e.g. D = Σn(n − 1) / N(N − 1) without subtracting from 1, where a low value means high diversity, or its reciprocal). The specification uses Ds = 1 − Σn(n − 1) / N(N − 1); always use this form.

## 2. Checked facts and examples

| Item | Fact (all arithmetic checked) |
|---|---|
| W1–W3 | 10, 5, 3, 2; N = 20; Σn(n − 1) = 118; N(N − 1) = 380; 118/380 = 0.3105; Ds = 0.69 (0.6895). |
| W4–W6 | 16, 2, 1, 1; N = 20; Σ = 242; 242/380 = 0.6368; Ds = 0.36 (0.3632). |
| W8 | 5, 5, 5, 5; Σ = 80; 80/380 = 0.2105; Ds = 0.79 (0.7895). |
| W9 | 20 of one species; Ds = 0. |
| W10 | 12, 8, 6, 3, 1; N = 30; Σ = 224; N(N − 1) = 870; 224/870 = 0.2575; Ds = 0.74 (0.7425). |
| W11 | 9, 6, 4, 3, 2, 1; N = 25; Σ = 122; N(N − 1) = 600; 122/600 = 0.2033; Ds = 0.80 (0.7967). |

The sample data are invented for practice; say "sample data". No real site data.

## 3. Traps

- Every block is Higher Level only; mark every heading. Simpson's Diversity Index, Ds, species diversity index are Higher Level key terms.
- n(n − 1), not n². N(N − 1) is calculated once, for the whole sample.
- Ds near 1 = high diversity; Ds = 0 = one species. Don't use the other versions of the index (U4) in worked examples.
- Rounding: keep at least four decimal places until the last step, then give Ds to two decimal places.
- The sampling methods that produce n (quadrats, kick samples, pitfall traps) belong to "Investigating an Ecosystem"; name them only.
- Richness and evenness are defined in "Biosphere, ecosystems, habitats and biodiversity"; use them, don't redefine.
- No diagram cues; the table layout in M1 is the only visual.

## 4. What exams ask (topics only)

No legacy questions (the index is new to this specification). Expect:
- Calculate Ds from a table of species counts, showing working.
- Compare Ds for two sites and explain the difference in terms of richness and evenness.
- State what a value of 0 or close to 1 means; give a limitation of the index.

## 5. Practice questions to write

1. 6 marks, Higher: "State the Simpson's Diversity Index equation and explain what n and N represent. What does a value of Ds close to 1 indicate?" Model answer: I2, I4.
2. 12 marks, Higher: "A sample from a hedgerow contained: hawthorn 8, bramble 6, ivy 4, holly 2. Calculate Ds, showing your working, and explain what your answer shows." Model answer: N = 20; n(n − 1) = 56, 30, 12, 2; Σ = 100; N(N − 1) = 380; 100/380 = 0.2632; Ds = 0.74; fairly high diversity, fairly even spread among four species. (Arithmetic checked.)
3. 9 marks, Higher: Give the W1 and W4 samples. "Both sites contain the same four species. Calculate Ds for each and explain why the values differ." Model answer: 0.69 and 0.36 (W3, W6); W7 explanation (dominance by daisy lowers evenness; trampling favours tolerant species).
