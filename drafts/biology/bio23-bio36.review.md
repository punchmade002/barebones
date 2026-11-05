# Review: biology chapters 23–36 (packages and Haiku notes, 2026-10-29)

Chapters 23–35 and chapter 36 (Biology Acronyms and Key Terms, `bio-acronyms`) were split in
`data.js` to match the outline: 66 subsections. Nine higher-model agents wrote the packages and
eleven Haiku agents wrote the notes, with the earlier briefs plus one new instruction: grep the
written notes for each subsection title and cover what they defer there. All 163 biology files
pass `scripts/build_notes.py biology`; 36/36 chapters are complete and the whole course is now
written.

**Titles.** Two `data.js` titles differ from the outline: bio31-s1 is "Biosphere, ecosystems,
habitats and biodiversity" (the outline's "Key terms" was too vague in the app), and the three
CO₂ titles in bio28 and bio30 use the subscript, as the notes do. bio4-s2's pointers were updated
to match.

**Density.** 7.2 points per block (chapters 11–22: 7.6; 1–10: 6.1; 19–21: 3.7).

## Checks done

- **Every subsection read in full** against its package, with `check_package_names.py` on each.
- **Arithmetic re-worked:** Simpson's index (all eight examples and the practice set), capture–
  recapture, density and population, percentage frequency and cover, soil water/air/humus,
  stream flow, potometer volume and rate per cm², percentage mass loss, osmosis mass changes,
  surface areas of cut potato, zone-of-inhibition area, growth-curve generations, BMI, PCR
  doubling, the sequencing-gel reading, and the forensic and paternity band matching.
- **Action verbs** (acronyms chapter) checked word for word against the specification glossary
  by script.
- **Dates and named facts checked**, including: Louise Brown 1978 and Edwards' Nobel 2010, WHO
  infertility estimate 2023, the Irish heel-prick programme (PKU, CF, congenital hypothyroidism,
  galactosaemia; 72–120 hours; Temple Street), Nitsch 1950, the All-Ireland Pollinator Plan
  2015, Velcro, Dixon and Joly 1894, Landsteiner 1901/1930 and Rhesus 1940, anti-D within 72
  hours, the Irish Food Pyramid 2016, WHO sugar limits 2015, the 2018 sugar tax, the 1967 sugar
  review, Castle Forbes 1911, zebra (1997) and quagga (2021) mussels, Killarney 1932, the 2019
  biodiversity emergency, the 2023 Citizens' Assembly, Powerscourt 1860, the 1841 census, the
  Nitrates Directive, Climate Action Act 2021 targets, warming potentials, Bord na Móna 2021,
  Cohen and Boyer, Jeffreys and Pitchfork, Mullis, Sanger, OMIM numbers and gene locations, the
  Huntington's repeat thresholds, Dolly, Yamanaka, He Jiankui, the Disability Act 2005, the
  2014 DNA database act, S and Marper, Fleming/Florey/Chain, GM insulin 1982 and Quorn. No
  errors found.
- **Higher Level marking** matches the outline, and Ordinary blocks avoid HL-only terms.
- **Investigations** (pollination comparison, osmosis for three factors, heart dissection,
  transpiration for six factors, human activity and diversity, the fieldwork subsections,
  microbial growth for six factors, DNA-profile patterns) have every part.

## Fixed during review

- **Build check:** the filler-phrase check now matches whole phrases only; it had rejected the
  specification's own definition of "evaluate" ("…in conclusions").
- **Run-together method steps** split into one bullet per step across the batch (and in a few
  earlier notes: bio4-s1, bio10-s3, bio11-s11, bio12-s3), with each step capitalised.
- **Wording:** bio34-s4 strategy bullets reworded as "For …", "Against …", "Judgement on …";
  bio35-s7 "For:" relabelled "Risk:" where it described the risk the law prevents; bio23-s3 no
  longer names FSH in an Ordinary block; bio32-s4 no longer names Rhizobium or makes it a
  flashcard (names of nitrogen-cycle microorganisms are not required; bio33-s3 keeps it for
  agricultural inoculants).
- **Labels:** "Higher Level:" prompt prefixes and "(Higher Level)" flashcard labels removed to
  match the earlier chapters.
- **Cross-references** to blocks in the same note reworded ("the block … below/above"), and two
  apostrophes matched to their titles.
- **Tests:** the untouched-chapter test now builds from a copy of the content with one chapter
  left out, so it no longer depends on which chapters are written.

## Decisions and minor points (not changed)

- **Membrane structure** is recapped in bio25-s1 and taught in "Models" (fluid mosaic), not
  re-taught, although bio7-s3 says it is in "Transport Across Membranes".
- **Cardiac cycle** is kept out entirely (no systole/diastole); the pacemaker section includes
  the SA and AV nodes and conducting fibres.
- **Batch and continuous culture** are in the Higher Level growth-curve block of
  "Microorganisms in industry"; bio13-s4 points there from an Ordinary block.
- **Content beyond the specification's list,** kept to what the outcomes need: hCG, Duchenne-
  style health links, CRISPR, iPS cells and cloning (needed for the ethics outcome), the onion
  DNA extraction, the alginate and potometer methods, pedigree and gel-reading skills,
  biomagnification, the hygiene hypothesis, and the acronyms chapter's chemical formulas and SEC
  entry.
- **Invented data** in worked examples is labelled "sample data".
- **Older batch:** seven subsections in chapters 19–21 have two practice questions rather than
  three.
- **Practice-question marks** are guesses, as before; old review questions stay in `bioN-1`.
