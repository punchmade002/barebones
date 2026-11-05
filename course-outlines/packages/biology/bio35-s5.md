# Package: bio35-s5 — Bioinformatics: genome databases

- **loId:** `bio35-s5` · **chapterId:** `bio35` · **syllabusRef:** 3.3.5
- **Syllabus:** "the value of technology in analysing large quantities of genetic information to
  identify patterns and search for anomalies." Outcome 5: "use a genome database to search for
  alleles that are known to cause (or be responsible for) specific genetic diseases." Ordinary
  and Higher level. No Higher Level only material.
- **Prepared by:** a higher model, 2026-10-29. "Use" means a practical skill: write it as a Skills
  block with a worked method in a real, free public database, a results table for at least two
  diseases, and a conclusion. Three databases are described: OMIM (the main worked method),
  NCBI (Gene and ClinVar) and Ensembl. Only interface features I am sure of are given; the notes
  must describe the interface in these general terms and must not invent menu names, buttons or
  screen layouts. Earlier notes defer to this title for: genome databases as shared online
  resources ("Science as a global enterprise"); genetic tests and databases identifying alleles
  known to cause single-gene diseases ("Benefits and limitations of Mendelian genetics"; "Causes,
  prevention and treatment of cancer", BRCA); comparing genomes of species ("The importance of
  the theory"); computers analysing huge amounts of genetic data ("The cross-cutting themes").
  Inheritance patterns (recessive, dominant), the mutations behind cystic fibrosis and
  sickle-cell anaemia, and sequencing are assumed from "Monohybrid crosses", "Mutations" and
  "DNA sequencing"; name them, don't re-teach.

## 1. Must cover

Bioinformatics and the value of technology (one block)
- [ ] B1 Bioinformatics is the use of computers and software to store, search, compare and analyse biological information, especially DNA, RNA and protein sequences. A genome database is an online store of genome sequences and information about genes, their variants (alleles) and their effects, which anyone can search.
- [ ] B2 Why computers are essential: one human genome is about 3 billion base pairs (see "DNA sequencing"), and sequencing machines produce data on many genomes quickly; no person could read or compare this by eye. Computers compare sequences in seconds, store them permanently and let scientists anywhere share them, much of it freely (as the Human Genome Project did; see "Science as a global enterprise").
- [ ] B3 Identifying patterns: software lines up (aligns) sequences to find similarities, e.g. genes shared by different species, which show evolutionary relationships and help work out what a newly found gene does (a gene similar to a known gene in another species often has a similar job). The NCBI tool BLAST takes a sequence typed or pasted in and finds the most similar sequences in the database, e.g. to identify the species or gene a DNA sample came from.
- [ ] B4 Searching for anomalies: a person's sequence is compared with a reference genome (a standard sequence) and the computer lists every difference (variant). Most variants are harmless; the database shows which have been recorded in people with a disease, so a disease-causing allele can be recognised. Worked example (one bullet): reference beta-globin gene … CCT GAG GAG …; patient … CCT GTG GAG …; the computer flags one substitution, A to T in the codon GAG → GTG, which is the sickle-cell allele (glutamic acid replaced by valine; see "Mutations"; databases show the DNA strand with the same sequence as the mRNA, so GTG here matches GUG in the mRNA).
- [ ] B5 Benefits for health and research: diagnosing rare genetic diseases quickly by comparing a patient's genome with databases; carrier testing and genetic counselling (see "Benefits and limitations of Mendelian genetics"); finding which genes are mutated in a tumour to choose a treatment (see "Causes, prevention and treatment of cancer"); tracking the spread and evolution of pathogens; and finding genes that raise the risk of common diseases.

The databases (one block, one bullet each)
- [ ] D1 OMIM (Online Mendelian Inheritance in Man, omim.org): a catalogue of human genes and genetic disorders and the relationships between them, written and updated by scientists at Johns Hopkins University in the USA. It was begun by the geneticist Victor McKusick. Each entry has a six-digit MIM number. Searching is free on the website.
- [ ] D2 NCBI (the National Center for Biotechnology Information, ncbi.nlm.nih.gov), part of the US National Library of Medicine: hosts many linked databases, including GenBank (DNA sequences), Gene (one record per gene, with its location and a summary of its function), ClinVar (variants found in patients and their classification) and the BLAST tool. A search box at the top of the home page searches all of them, or one chosen database.
- [ ] D3 Ensembl (ensembl.org): a genome browser run by the European Bioinformatics Institute (EMBL-EBI) near Cambridge, UK. It shows the genomes of humans and many other animals as maps on which genes, their structure and known variants can be viewed and compared between species.

Worked method: OMIM (one Skills block, numbered)
- [ ] O1 Aim: to use a genome database to find the gene and the alleles responsible for two named genetic diseases, cystic fibrosis and Huntington's disease, and record the gene, its chromosome location, the pattern of inheritance and the disease-causing allele.
- [ ] O2 1. Go to omim.org and type the disease name (e.g. "cystic fibrosis") in the search box. 2. The results list entries, each with a MIM number and a title. A symbol before the number shows the type of entry: # means a description of a disease or other phenotype whose molecular basis (gene) is known; * means a gene. 3. Open the disease entry (the # entry: cystic fibrosis is #219700; Huntington's disease is #143100).
- [ ] O3 4. Near the top of the disease entry, a table of phenotype–gene relationships gives the chromosome location (cytogenetic band), the phenotype, its pattern of inheritance (e.g. "AR" for autosomal recessive, "AD" for autosomal dominant), and the gene responsible, with a link to the gene's own (*) entry. 5. Read the text sections of the entry (e.g. clinical features, inheritance, molecular genetics) for a description of the disease and of the mutations that cause it. 6. Follow the link to the gene entry; its section on allelic variants lists selected disease-causing alleles, each with a description of the change in the DNA and the protein.
- [ ] O4 7. Record the findings in a table (columns: disease; gene; chromosome location; inheritance; disease-causing allele; protein affected). 8. Repeat for the second disease. 9. Check one result in a second database (e.g. search the gene name in NCBI Gene or Ensembl) to confirm the location (a check of reliability, see "Recognising bias and evaluating sources").
- [ ] O5 Reading a chromosome location: 7q31.2 means chromosome 7, the long arm (q), band 31.2; 4p16.3 means chromosome 4, the short arm (p), band 16.3. One bullet.

Expected results (one bullet per disease; this is the table the notes should give)
- [ ] R1 Cystic fibrosis: gene CFTR (cystic fibrosis transmembrane conductance regulator), chromosome 7 (7q31.2); autosomal recessive; the commonest disease-causing allele is F508del, a deletion of three bases that removes one phenylalanine from the CFTR protein (see "Mutations"), and many hundreds of other disease-causing alleles are listed; protein affected: CFTR, a channel that moves chloride ions across cell membranes.
- [ ] R2 Huntington's disease: gene HTT (huntingtin), chromosome 4 (4p16.3); autosomal dominant; the disease-causing allele has too many repeats of the three bases CAG near the start of the gene: 40 or more repeats cause the disease, 36 to 39 may or may not, and unaffected people usually have 26 or fewer; each CAG codes for the amino acid glutamine, so the huntingtin protein carries an abnormally long chain of glutamines, which damages nerve cells in the brain.
- [ ] R3 Third example (optional, may be given as a row in the table): sickle-cell anaemia: gene HBB (beta-globin), chromosome 11 (11p15.4); autosomal recessive; allele: one base substitution changing glutamic acid to valine in beta-globin (haemoglobin S; B4 and "Mutations").

Using NCBI and Ensembl (one block, kept general)
- [ ] N1 NCBI: choose the Gene database, search the gene name with "human" (e.g. "CFTR human"), and open the human gene record, which gives the official name, the chromosome location, a summary of what the gene does and links to OMIM and ClinVar. In ClinVar, a search for the gene lists the variants reported in patients, each with a classification: pathogenic, likely pathogenic, uncertain significance, likely benign or benign. A disease-causing allele is one classified as pathogenic.
- [ ] N2 Ensembl: choose the human genome, search for the gene name and open the gene page, which shows the gene's position on the chromosome, its coding and non-coding sections, and a table of known variants with their consequences; the same gene can be viewed in other species to see how similar it is.

Conclusion and limitations (one block)
- [ ] C1 Conclusion (from R1–R2): each disease is caused by alleles of a single gene at a known chromosome location; cystic fibrosis is recessive, so a person needs two disease-causing alleles, while Huntington's disease is dominant, so one is enough (see "Monohybrid crosses"); databases record many different disease-causing alleles of the same gene.
- [ ] C2 Limitations: many variants are of "uncertain significance" (it isn't yet known whether they cause disease); most common diseases (e.g. heart disease, type 2 diabetes) involve many genes and the environment, so no single allele "causes" them (see "Benefits and limitations of Mendelian genetics"); databases contain far more data from people of European ancestry than from other populations, so variants in other groups are less well understood; databases are for research and professionals, so a result should be interpreted with a doctor or genetic counsellor. Privacy of genetic data is in "Ethics of genetic technologies".

## 2. Checked facts and examples

| Item | Fact |
|---|---|
| B3 | BLAST is an NCBI tool that finds the most similar sequences to one entered. |
| B4 | Sickle-cell: GAG → GTG in the DNA (GUG in mRNA), glutamic acid → valine, beta-globin (as in "Mutations"). |
| D1 | OMIM = Online Mendelian Inheritance in Man, omim.org, Johns Hopkins University, begun by Victor McKusick; six-digit MIM numbers. |
| D2 | NCBI = National Center for Biotechnology Information, part of the US National Library of Medicine; GenBank, Gene, ClinVar, BLAST. |
| D3 | Ensembl, ensembl.org, run by EMBL-EBI near Cambridge, UK. |
| O2 | OMIM prefixes: # = phenotype with known molecular basis; * = gene. Cystic fibrosis #219700; Huntington's disease #143100. |
| N1 | ClinVar classifications: pathogenic, likely pathogenic, uncertain significance, likely benign, benign. |
| R1 | CFTR, 7q31.2, autosomal recessive, F508del commonest allele; chloride channel. |
| R2 | HTT (huntingtin), 4p16.3, autosomal dominant; CAG repeat: 40 or more cause the disease, 36–39 may or may not, 26 or fewer usual; CAG = glutamine. |
| R3 | HBB, 11p15.4, autosomal recessive. |

No other MIM numbers, variant numbers, accession numbers, counts of variants or screen
details. Don't name OMIM sections or NCBI/Ensembl buttons beyond the general terms in O2–O3 and
N1–N2.

## 3. Traps

- An allele "known to cause" a disease is a pathogenic variant recorded in the database; not every difference from the reference is harmful (B4, C2).
- Huntington's disease is dominant and caused by a repeat expansion (too many CAG repeats), not by a single base substitution. Cystic fibrosis's commonest allele is a three-base deletion, not a frameshift (see "Mutations").
- OMIM covers human genes only; Ensembl and NCBI cover many species.
- Don't invent interface details (menu names, tabs, button labels, screenshots). Websites change; keep to O2–O3 and N1–N2.
- Don't write "the database diagnoses" a person: it holds knowledge; diagnosis needs a test of the person's DNA and medical interpretation.
- How sequencing works belongs to "DNA sequencing"; ethics of genetic data and testing to "Ethics of genetic technologies"; Mendelian crosses to "Monohybrid crosses".
- No diagram cues. (Optionally the results table is written as bullets, one per disease.)

## 4. What exams ask (topics only)

No legacy questions (the outcome is new). Expect:
- Explain what bioinformatics is and why computers are needed to analyse genetic information.
- Describe how a genome database could be used to find information about the allele that causes a named genetic disease.
- Interpret given database output (gene, chromosome location, inheritance pattern, variant).
- Compare a patient's sequence with a reference sequence and identify the mutation.

## 5. Practice questions to write

1. 6 marks: "What is meant by bioinformatics? Give two reasons why computers are needed to analyse genetic information." Model answer: B1; two of B2 (size of genome, speed, storage, sharing).
2. 12 marks: "Describe how you would use a named genome database to find information about the allele that causes a named genetic disease, and state what you would expect to find." Model answer: named database (D1); O2–O4 steps; findings for one disease from R1 or R2 (gene, location, inheritance, allele); one limitation from C2.
3. 9 marks: "Part of a reference sequence of a gene is CCT GAG GAG and the same part in a patient is CCT GTG GAG. Identify the type of mutation, name the condition it causes and explain how a genome database helps to show that this change causes disease." Model answer: B4 (substitution, sickle-cell anaemia, glutamic acid to valine); database records the variant as pathogenic in affected people (N1).
