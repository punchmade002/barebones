# Package: bio35-s4 — DNA sequencing

- **loId:** `bio35-s4` · **chapterId:** `bio35` · **syllabusRef:** 3.3.4
- **Syllabus (Higher Level only):** "sequencing data (nucleotide bases) – generate a collection of
  DNA fragments, each of which is one nucleotide shorter than the next, and separated on a gel
  electrophoresis." Outcome 4: "outline the principle of DNA sequencing."
- **Level:** every block in this subsection ends its heading with " (Higher Level only)".
- **Prepared by:** a higher model, 2026-10-29. "Outline the principle" means the idea of the
  chain-termination method at the specification's own level: copy the DNA so that copying stops
  at random at every base, giving fragments that differ in length by one nucleotide; separate
  them by gel electrophoresis; read the order of bases from shortest to longest. No chemistry of
  the terminator beyond one sentence. Earlier notes defer to this title for: point mutations
  being detected by sequencing ("Mutations") and DNA sequencing as a technology that produces
  huge amounts of genetic data ("The cross-cutting themes", "Classification"). Gel
  electrophoresis (charge, size separation, agarose, ladder) is taught in "Generating a DNA
  profile"; PCR and primers likewise; use them without re-teaching. Complementary base pairing
  and DNA polymerase are assumed from "Nucleotides, DNA and RNA" and "Modelling DNA replication
  and information flow".

## 1. Must cover

What sequencing is (one block)
- [ ] Q1 DNA sequencing is working out the exact order of the bases (A, T, C, G) along a piece of DNA. A profile ("DNA profiling") only compares fragment lengths; sequencing reads every base.
- [ ] Q2 Scale (assumed context): the human genome contains about 3 billion base pairs and about 20,000 protein-coding genes. The Human Genome Project (1990–2003; see "Science as a global enterprise") produced the first reference sequence; the first complete, gap-free human sequence, including the repeated regions that had been impossible to read, was published in 2022.

The principle: chain termination (one Process block, numbered)
- [ ] P1 The method is the chain-termination method, developed by Frederick Sanger in 1977 (Sanger sequencing). Sanger won the Nobel Prize in Chemistry twice: in 1958 for working out the amino-acid sequence of insulin, and in 1980 (shared) for DNA sequencing.
- [ ] P2 1. Many copies of the DNA to be sequenced are made (e.g. by PCR) and separated into single strands; each strand is the template.
- [ ] P3 2. The template is mixed with a primer (which binds at the start of the region to be read), DNA polymerase, a large supply of the four normal nucleotides, and a small amount of each of four modified "terminator" nucleotides. A terminator nucleotide can be added to a growing strand like a normal one, but it lacks the chemical group needed to attach the next nucleotide, so once it is added the strand can grow no further.
- [ ] P4 3. DNA polymerase builds new strands complementary to the template. At each position it usually adds a normal nucleotide, but occasionally, by chance, it adds a terminator, and that strand stops there. Because there are millions of template copies, strands stop at every possible position.
- [ ] P5 4. The result is a collection of DNA fragments of every length, each one nucleotide shorter than the next, and each ending in a terminator that shows which base is at its last position.
- [ ] P6 5. The terminators are identified: in Sanger's original method four separate reactions were run, each with only one kind of terminator (A, T, C or G), and run in four lanes of a gel; in the modern automated method each of the four terminators carries a different coloured fluorescent dye, so one reaction is enough and a laser reads the colour of each fragment.
- [ ] P7 6. The fragments are separated by gel electrophoresis (in a thin capillary tube in modern machines). The gel must separate fragments that differ by a single nucleotide; the shortest move furthest.
- [ ] P8 7. The sequence is read from the shortest fragment to the longest (from the bottom of the gel, furthest from the wells, upwards): the last base of each successive fragment gives the next base of the new strand. The template's sequence is the complement of this.
- [ ] P9 Diagram: a four-lane gel labelled A, C, G, T at the top (wells, negative electrode), bands at different heights, an arrow up the side labelled "read from the bottom (shortest fragment) to the top", and the sequence written beside it; label wells, lanes, bands, shortest and longest fragment, + and − electrodes. Also, beside it, a short template with the set of growing strands each stopped one base later than the last.

Reading a sequencing gel (one Skills block with the worked example)
- [ ] W1 Method: 1. Find the band nearest the bottom (furthest from the wells); its lane gives the first base of the new strand. 2. Move up one band at a time, whichever lane it is in, writing down the lane letter each time. 3. Stop at the top band. 4. To give the template, write the complementary base for each (A↔T, C↔G).
- [ ] W2 Worked example: a gel has bands at eight heights. From the bottom up, the bands are in lanes T, A, C, C, G, T, A, G. So the new strand reads TACCGTAG, and the template strand is ATGGCATC. Lane by lane: lane A has bands at positions 2 and 7 from the bottom; lane C at 3 and 4; lane G at 5 and 8; lane T at 1 and 6. The shortest fragment (position 1) is one nucleotide longer than the primer; each band above is one nucleotide longer than the one below.
- [ ] W3 Automated output (one bullet): the machine prints a trace of coloured peaks, one colour per base, in order of fragment length, with the base letter above each peak; it is read left to right in the same way.

Modern sequencing and uses (one block)
- [ ] M1 Newer (next-generation) methods sequence millions of short DNA fragments at the same time and use computers to assemble the overlapping fragments into the full sequence. They are far faster and cheaper than the original method, so whole genomes are now sequenced routinely. The huge amount of data is stored and analysed in genome databases (see "Bioinformatics: genome databases").
- [ ] M2 Uses: finding point mutations and diagnosing genetic diseases (see "Mutations"); choosing cancer drugs by sequencing a tumour's DNA (see "Causes, prevention and treatment of cancer"); comparing DNA of different species to work out evolutionary relationships and classification (see "Classification"); identifying and tracking pathogens, e.g. the genome of the virus that causes COVID-19 was sequenced and shared online in January 2020 (see "Science as a global enterprise"). One bullet each, cross-referring.

## 2. Checked facts and examples

| Item | Fact |
|---|---|
| Q2 | Human genome about 3 billion base pairs; about 20,000 protein-coding genes; Human Genome Project 1990–2003; first complete gap-free human sequence published 2022. |
| P1 | Frederick Sanger, chain-termination method, 1977; Nobel Prizes in Chemistry 1958 (insulin sequence) and 1980 (shared, DNA sequencing). |
| P6 | Original method: four reactions, four lanes; modern: four fluorescent dyes, one reaction, capillary, laser. |
| W2 | Lanes from bottom: T, A, C, C, G, T, A, G → new strand TACCGTAG; template ATGGCATC (checked base by base). |
| M2 | SARS-CoV-2 genome shared online January 2020 (as in "Science as a global enterprise"). |

No other names, dates or figures (no costs, run times or read lengths; no names of sequencing
companies or machines).

## 3. Traps

- Every block is Higher Level only; mark every heading.
- Read from the shortest fragment (bottom, furthest from the wells) to the longest. Reading top-down gives the sequence backwards.
- The bands give the new (copied) strand; the template is its complement. Say which one an answer gives.
- Terminators are added at random, a small proportion at each position, so every length is made; don't say the polymerase "chooses" to stop.
- Keep to the principle: don't use the terms dideoxynucleotide or ddNTP beyond, at most, one optional mention in brackets in P3; don't teach the 3′-OH group, 5′/3′ direction or antiparallel strands (not on the specification).
- Sequencing reads the bases; profiling compares lengths. Don't confuse them.
- How gel electrophoresis works (charge, pores, agarose, ladder, staining) belongs to "Generating a DNA profile"; P7 states only what is special here (one-nucleotide resolution).
- Searching databases for disease alleles belongs to "Bioinformatics: genome databases".
- Diagram cues: P9 only. No other diagram cues.

## 4. What exams ask (topics only)

No legacy questions on sequencing. Expect:
- Outline the principle of DNA sequencing (fragments one nucleotide different in length, terminated at each base, separated by gel electrophoresis, read in order).
- Read a base sequence from a diagram of a sequencing gel or trace; give the complementary template sequence.
- Distinguish DNA sequencing from DNA profiling; give a use of sequencing.

## 5. Practice questions to write

1. 9 marks, Higher: "Outline the principle of DNA sequencing by the chain-termination method." Model answer: P2–P8: template, primer, polymerase, normal and terminator nucleotides; random termination giving fragments one nucleotide apart; separation by gel electrophoresis; reading from shortest to longest.
2. 6 marks, Higher: "A sequencing gel has bands which, read from the bottom upwards, are in lanes G, A, T, T, C, A. Give the sequence of the new strand and of the template strand." Model answer: new strand GATTCA; template CTAAGT (W1 method).
3. 6 marks, Higher: "Distinguish between DNA sequencing and DNA profiling, and give one use of DNA sequencing." Model answer: Q1 (order of every base vs comparison of fragment lengths); one use from M2.
