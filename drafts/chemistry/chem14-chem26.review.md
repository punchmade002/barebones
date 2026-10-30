# Review: chemistry chapters 14–26 (packages and Haiku notes, 2026-10-30)

Chapters chem14–chem26 were split in `data.js` into the 72 subsections of
`course-outlines/chemistry.md`, with a "Chapter review" outcome (`chemN-1`) first, as chem1–chem13
were. Seven higher-model agents wrote one information package per subsection
(`course-outlines/packages/chemistry/`) from the 2025 specification, the retired app notes for
the chapter, and the past-paper topics still on the specification. Thirteen Haiku agents, one per
chapter, wrote the notes (`content/chemistry/`). All 137 chemistry files pass
`scripts/build_notes.py chemistry`; 26/26 chapters are complete and ship in `chemistry-notes.js`.

## Coverage, before and after (chem14–chem26)

| | Before | After |
|---|---:|---:|
| Units of study | 69 specification outcomes | 72 outline subsections (+ 13 reviews) |
| Note blocks | 122 (one paragraph each) | 497 (3370 bullets) |
| Words of notes (approx.) | 23 000 | 71 000 |
| Thin outcomes (under 150 words) | 25 | 0 |
| Flashcards | 158 | 611 |
| Practice and test questions | 121 | 336 (121 kept on the reviews + 215 new) |

Every learning outcome and "learn about" item of units 1.4.7 (part), 2.4, 3.1–3.5 (part), 4.1.2,
4.1.6–4.1.7, 4.2 and 4.3 has a subsection. Higher Level material is in blocks headed
"(Higher Level only)", checked against the bold (Lato-Black) text in the specification PDF.
Wholly Higher Level: chem14-s2, chem17-s5, chem18-s3, chem19-s3, chem21-s5, chem21-s6,
chem23-s9, chem24-s4, chem24-s5, chem25-s6, chem25-s7, chem26-s3.

## Restructure

- `data.js`: every chemistry chapter now lists `chemN-1` "Chapter review" and `chemN-s1…` with
  `syllabusRef`.
- `chemistry-content.js`: the old chem14–chem26 notes and flashcards (and the fix-ups that moved
  them between outcomes) are removed; all 121 of their test questions, including those from
  `chemistry-test-questions.js` (now empty), are on each chapter's review outcome.
- Package writers were told to carry every correct, on-specification fact from the old notes
  into a must-cover item; what they dropped is listed below.
- Tests: `chemistry-outcome-notes.test.cjs` now expects all 26 chapters split; the organic
  "cross-chapter" assertions on the old outcomes are gone with those outcomes.

## Checks done

- **Arithmetic:** every calculation and model answer re-run in Python by the package writers;
  the Haiku writers re-checked them and found two rounding errors (below).
- **Redox equations** checked for atom and charge balance by script (chem14–chem16).
- **`check_package_names.py`** on all 72 files: every name and number in the notes is in its
  package (remaining hits are sentence openers and intermediate working values).
- **Cross-references:** every quoted note title in all 137 files matches a `data.js` title.
- **In the app** (headless Chromium): all 137 subsections load as authored, each review keeps its
  questions, no script errors.

## Fixed during review

- Neutral pH of water: 7.48 at 0 °C and 6.15 at 100 °C (the package had 7.47 and 6.14).
- Heat of combustion per CH₂ for alcohols: "about 640–655 kJ mol⁻¹" (methanol to ethanol is 641).
- C=C bond enthalpy: 614 kJ mol⁻¹ in chem23-s6 to match chem21-s5 (was 612).
- Removed an unsupported "Ordinary level stops at element 20" note on oxidation numbers.
- Reworded a self-contradictory naming trap (methylpropane).

## Old-note content dropped (from the writers' reports)

- **Wrong:** ammonia Kb 6.6 × 10⁻⁵ (now 1.8 × 10⁻⁵); ethyne ΔHf −84.7 (ethane's value);
  CH₄ ΔHc −879 (now −890); "activated complex" called an intermediate; "3-chlorobutanoic acid"
  for a 4-chloro compound; butanone "completely miscible"; chloroalkanes "all liquids"; H₂/Ni
  reducing carboxylic acids; "condensation" as one of the five reaction types; percentage yield
  as mass ÷ mass; a methanol result more negative than the standard value; a thiosulfate answer
  mixing two Mr values; Fe³⁺ "removed as FeCl₃" by HCl.
- **Off the specification:** cracking, reforming and octane numbers; metal extraction; the
  Winkler method; CFCs; transition-metal theory; the bomb calorimeter; Faraday's laws; skeletal
  formulae; atom economy (listed under Traps).
- **Unverifiable figures:** Haber Kc values, BOD values for named wastes, taxol step counts,
  graphene and C₆₀ melting points, several Irish energy and pollution statistics.
- Decimal relative atomic masses replaced by the whole-number SEC values throughout.

## Decisions for the owner (not changed)

- **Bond enthalpies (chem21-s5):** the SEC *Formulae and Tables* booklet could not be fetched;
  the table uses the standard LC set (C–H 412, C–C 348, C=C 614, C≡C 839, O=O 498, C=O 799,
  O–H 463, H–H 436, Cl–Cl 242, C–Cl 338, H–Cl 431 kJ mol⁻¹). Check against the booklet.
- **Iron(III)–thiocyanate and temperature:** sources disagree on the sign of ΔH, so the notes
  give no direction and tell students to reason from the colour change given; concentration
  effects use FeSCN²⁺, temperature uses cobalt(II) chloride and NO₂/N₂O₄.
- **Higher Level splits that differ from the outline:** in 3.4.9 only the Ka/Kb deduction is
  bold (the dissociation equations are normal type); in 2.4.8 the σ/π explanation is bold even
  for ethane, ethene and ethyne.
- **Iodine (element 53)** is outside the "first 36 elements" for oxidation numbers: I₂ (0) and
  I⁻ (−1) are used, no oxidation numbers in iodine compounds.
- **Extras beyond the specification wording, kept:** Ka × Kb = Kw; the alkaline fuel cell; the
  Maxwell–Boltzmann distribution (at Ordinary level, for temperature); the reaction quotient Q;
  Haber and Contact processes as HL yield-optimisation examples; combustion analysis and
  multi-step overall yield in chem26; N₂O alongside NOx.
- **Environmental figures** use IPCC AR5 100-year GWPs (CH₄ 28, N₂O 265, AR6 noted) and AR6
  warming and sea-level values; Irish facts include fluoridation 0.6–0.8 mg L⁻¹ since 2007, the
  2007 Galway Cryptosporidium outbreak, lead pipes in houses built before about 1970, and the
  2021 Climate Act targets. Worth a spot-check before release.
- **Practice-question marks** are estimates; questions the packages call Higher Level carry no
  level label, since the question format has no field for it.
