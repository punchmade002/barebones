# Review: biology chapters 11–18 and 22 (packages and Haiku notes, 2026-10-26)

Chapters 10, 19, 20 and 21 were already written and were left alone. The other nine chapters in
10–22 were split in `data.js` to match the outline, 49 subsections in all (bio11 has 12, bio12 4,
bio13 4, bio14 5, bio15 5, bio16 5, bio17 3, bio18 4, bio22 7). Six higher-model agents wrote the
packages and ten Haiku agents wrote the notes, with the same briefs as chapters 1–10 (exemplars and
the chapter 1–10 review added). All 97 biology files pass `scripts/build_notes.py biology` and are
built into `biology-notes.js`; 22/22 split chapters are complete.

**Chapter titles.** The all-caps titles (Investigating in Science, Science in Society, Biological
Reasoning, Homeostasis, Immunity, Human Reproduction, Plant Reproduction) are now title case in
`data.js`, `pipeline/scaffold/biology.json` and the `bio-content.js` comments.

**Density.** This batch averages 7.6 points per block, against 6.0 for chapters 1–10 and 3.7 for
chapters 19–21, and is about 10% longer per subsection than chapters 1–10.

## Checks done

- **Every subsection read in full** against its package, with `check_package_names.py` on each
  (it flags only sentence openers).
- **Crosses and arithmetic.** Every Punnett square and ratio in bio11 (monohybrid, incomplete
  dominance, dihybrid including RrYy × Rryy and the incomplete-dominance dihybrid, linkage,
  sex-linked) was worked by hand; Mendel's counts and ratios; 2²³ and 7 × 10¹³ (bio12); the
  mitotic index (bio16); codon decoding, frameshift and template examples, nucleotide counts and
  Meselson–Stahl bands (bio17); R₀, R and herd-immunity thresholds (bio22). All correct.
- **Dates and named facts checked:** Mendel, de Vries/Correns 1900, Correns 1909, mtDNA 37 genes,
  UK mitochondrial donation 2015, the epigenetic examples (honeybee 2008, Waterland and Jirtle
  2003, Dutch Hunger Winter and the 2008 IGF2 study, FLC, toadflax 1999); Darwin, Wallace and the
  1858 Linnean meeting, Archaeopteryx 1861, Tiktaalik 2004, cytochrome c, the Lederbergs 1952,
  Weismann, Spartina anglica, the Grants 1977; Ruben/¹⁸O, Mitchell 1961 and Nobel 1978; HeLa 1951,
  Doll and Hill 1950, the 2004 Irish smoking ban, BreastCheck, CervicalCheck, the Swedish 2020
  HPV study, Allison and Honjo 2018, sickle-cell, F508del, cri du chat, CMT1A, the factor VIII
  inversion, the Philadelphia chromosome (1960, 1973); bone and vertebra counts; Prusiner, vCJD,
  Jenner 1796, smallpox 1980, AZT 1987, the 2020 pandemic declaration, Mary Mallon, Ug99, 2009
  H1N1, bluetongue 2006, ash dieback in Ireland 2012, Schmallenberg 2011, ToBRFV, Ebola 2014–16,
  Nipah, HIV 1983 and Nobel 2008, H5N1 in US cattle 2024. No errors found.
- **Higher Level marking** matches the outline: all of bio11-s6 to s9 and s11, the HL blocks of
  bio11-s1 to s4, bio13-s2, bio14-s3 to s5, bio15-s3 to s5, the HL blocks of bio16-s1, all of
  bio17, the cell-mediated block of bio22-s2, and bio22-s5.
- **Investigations** (bio13-s3 for each of five factors, bio14-s2 for three factors, bio15-s2)
  have aims, variables, controls, method, safety, expected results, conclusions and errors.
- **Spec wording.** The packages follow the specification's own simplified wording for the
  light-dependent reactions (photolysis by the positive chlorophyll) and the proton mechanism
  (charge difference attracting protons from donor molecules), with textbook names noted once.

## Fixed during review

- bio11-s1 to s3: Higher Level terms added to the flashcards (histone, nucleosome, chromatid,
  centromere; epigenetic expression, incomplete dominance, linkage, sex-linkage; non-nuclear
  inheritance, mitochondrial DNA, maternal inheritance). The writer had left them out; earlier
  batches include HL flashcards.
- bio16-s2: removed a bullet that described the comparison table instead of teaching.
- bio14-s2: split a method bullet that ran steps 1 and 2 together.
- bio13-s3: "hydrogen ions in more acidic or alkaline conditions" now says a higher or lower
  hydrogen-ion concentration.
- bio22-s6: SARS-CoV-2 variants are no longer called antigenic drift; they are attributed to
  mutation.
- bio11-s9: garbled phrase in a model answer ("the reason of crossing over").
- Cross-references to block headings inside the same note (bio13-s1, bio13-s4, bio14-s5,
  bio22-s6) reworded as "the block on … below/above"; bio17-s2 now names the note as well as the
  block for the ER and Golgi.
- bio6-s1: its replication pointer goes back to "Viruses: replication", which now exists.
- The build test's "untouched chapter" fixture moved from bio13 (now authored) to bio23.

## Decisions and minor points (not changed)

- **Crossing over.** Named once, as a source of variation in meiosis (bio16-s2, bio12-s1) and as
  why linked genes occasionally separate (bio11-s9); never described. The specification says
  knowledge of it is not required.
- **Cross-references ahead of their chapters.** These titles must survive when chapters 23–35 are
  split: Bacteria and fungi, The microbiome, Microorganisms in industry, Blood, Gas exchange and
  the breathing mechanism, Gametes and fertilisation, Prenatal and postnatal care, Genetic
  engineering, Generating a DNA profile, DNA sequencing, Bioinformatics: genome databases, Ethics
  of genetic technologies.
- **Overlaps, kept short and cross-referred:** 2²³ and random fertilisation (bio12-s1, bio16-s2);
  lactase persistence and mutagens (bio12-s1 at both levels, bio17-s3 at HL); antibiotic
  resistance (bio12-s3 as evidence, bio22-s6 as a factor in spread); the Lumper potato (bio12-s1,
  bio22-s6); helper/suppressor T cells (process in bio22-s2, cell features in bio22-s5).
- **Content beyond the spec's list,** kept to what the outcomes need: activation energy, Duchenne
  muscular dystrophy, pedigrees, Y-linked traits, the alginate-bead method (an old mandatory
  experiment), long-bone structure and joint types, complement, interferons, antibody structure,
  vaccine types, latency and the HIV cycle, glycolysis ATP/NADH counts, the 3 ATP : 2 NADPH ratio.
- **bio11-s4.** The epigenetics concept and mechanisms are Ordinary and Higher, as the outline
  marks only "research one example" HL, although "epigenetic expression" is HL in bio11-s2.
- **Practice-question marks** are guesses, as before. Some sets are ordered 6/12/9 rather than
  6/9/12.
- **Old review questions** stay in each chapter's `bioN-1` outcome; its old notes are cleared.
