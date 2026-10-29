# Leaving Cert Biology (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format,
  and a worked example). This outline says what to cover; that file says how to write it.
- **Assumed knowledge:** the specification lists outcomes, not the basics they rest on. Notes
  must also teach what a student needs to meet each outcome (`NOTES_STANDARD.md` rule 9), e.g.
  enzyme active sites, named heart valves and vessels, Punnett squares, base-pairing rules,
  guard cells. Information packages list these as "(assumed)" items.
- **The specification:** the NCCA *Curriculum Specification for Leaving Certificate Biology*,
  "for introduction to schools in September 2025" (published August 2024). Students who started
  fifth year in September 2025 sit it for the first time in **June 2027**, so this is the
  document the app's students are examined on. The official PDF is
  `pipeline/resources/biology/spec-syllabus.pdf` (also `relevant-resources/syllabi/biology.pdf`),
  downloaded from curriculumonline.ie on 2026-10-15. References in brackets, e.g. **[2.2.4]**,
  mean strand 2, unit 2.2, learning outcome 4. **[U2.3]** means the Unifying Strand, U2,
  outcome 3.
- **Do not use the previous syllabus** (the 2001 *Leaving Certificate Biology Syllabus*, first
  examined 2004 and last examined June 2026). It is a different course. Every past paper in the
  app (`exam-questions-db.js`, tagged `[LEGACY — pre-2027 syllabus]`) was set on it. Use those
  papers only where the topic is also in this outline, and never teach content because a legacy
  paper asked it: e.g. the cardiac cycle, germination, seed dormancy, tropisms and skin
  thermoregulation are not on this specification.
- **Chapters** are the app's 36 biology chapter IDs (`data.js`, `pipeline/scaffold/biology.json`).
  Questions and flashcards are tagged to these IDs, so keep every ID exactly as written. The
  specification doesn't follow the chapter order; each heading gives the outcomes it covers.
- **What each subsection contains:**
  - **"Syllabus"** is what the specification says students learn about and should be able to
    do, close to its own wording. This is the required scope; every item must be covered.
  - **"Settings"** are the examples the specification itself names (e.g. "colour blindness and
    haemophilia"). Use them; they are the examples an examiner expects.
  - **"SimpleStudy"** names the matching topic in SimpleStudy's Higher Level course (taxonomy
    recorded 2026-08-07 in `pipeline/resources/biology/guide-simplestudy.md`). Use it for
    structure only; write all prose in your own words.
- **Higher vs Ordinary level:** Ordinary level studies "only the learning outcomes that are
  presented in normal type"; Higher level studies "all learning outcomes including those in bold
  type". Items in bold in the specification are marked **[HL]** here. Nothing else is Higher
  Level only. Write [HL] content in full, as the app's students take Higher Level. Some outcomes
  are partly bold; only the marked part is [HL].
- **Where the specification sets a choice or an open example, cover every reasonable option:**
  one water-soluble and one fat-soluble vitamin with their deficiency diseases [1.2.3]; one
  example of epigenetic inheritance in nature [1.4.3]; "known examples" of point and
  chromosomal mutations [2.3.6]; "different cancers" [2.3.8]; a "chosen ecosystem" [3.1.11]
  (write it for a grassland, the app's existing chapter, and note how methods change for a
  woodland, rocky shore or freshwater habitat); "specific genetic diseases" in a genome database
  [3.3.5].
- **The cross-cutting themes** are Health, Sustainability and Technology. The written exam
  includes questions on "application of Biology to issues relating to the cross-cutting
  themes", so each chapter's notes should name its health, sustainability and technology links
  where the specification makes them.
- **Practical work:** the specification requires primary data in these "investigate" outcomes.
  Each must be written as a full investigation (question or hypothesis, variables, control,
  method, measurement, safety, results, conclusion), in the chapter shown:
  - qualitative food tests [1.2.5] and quantitative reducing-sugar test [1.2.6] — `bio8`
  - cells under the light microscope, with SEM images as secondary data [1.3.3] — `bio7`
  - factors affecting enzyme rate [2.1.3] — `bio13`
  - factors affecting photosynthesis rate [2.2.2] — `bio14`
  - conditions necessary for fermentation [2.2.3] — `bio15`
  - insect- and wind-pollinated flower structures [2.5.7] — `bio24`
  - factors affecting the rate of osmosis [2.6.2] — `bio25`
  - heart structure [2.6.9] — `bio29`
  - factors affecting the rate of transpiration [2.6.16] — `bio30`
  - effects of human activity on species diversity (primary or secondary data) [3.1.3] — `bio31`
  - the chosen ecosystem [3.1.11] — `bio32`
  - factors affecting the growth of microorganisms [3.2.2] — `bio33`
  - genome database search [3.3.5] and DNA-profile patterns [3.3.6] — `bio35`
- **Assessment:**
  - Written examination: **60%**, at Higher and Ordinary level, set by the SEC. It uses a range
    of question types and assesses all four strands plus the cross-cutting themes.
    Differentiation between levels comes through the stimulus material and the amount of
    structured support. The specification doesn't give the paper's sections or timing, and no
    sample paper is in the repo.
  - Additional assessment component, the **Biology in Practice Investigation: 40%**, at a
    common level, set and marked by the SEC. It is covered in `bio2`.
  - Grades are H1–H8 and O1–O8, in 10% bands from 30% to 100%.

---

## Unifying Strand — Nature of Science [U1–U4]

All students. No bold outcomes. The written exam assesses this strand directly, and it is the
main content of the Biology in Practice Investigation.

### bio1 — Scientific Knowledge [U1]
1. **The nature of scientific knowledge** [U1.1]: how scientists work; how scientific ideas are
   modified over time; hypothesis, theory and law.
   SimpleStudy: Scientific Knowledge.
2. **Science as a global enterprise** [U1.1]: one that relies on clear communication,
   international conventions, peer review and reproducibility.
3. **Recognising bias and evaluating sources** [U1.2]: conduct research relevant to a scientific
   issue; evaluate different sources of information, including secondary data, understanding
   that a source may lack detail or show bias.

### bio2 — Investigating in Science [U2; additional assessment component]
1. **Questioning and predicting** [U2.1–U2.2]: recognise questions appropriate for scientific
   investigation; pose testable hypotheses developed using scientific theories and
   explanations; evaluate and compare strategies for investigating hypotheses.
   SimpleStudy: Investigating in Science.
2. **Designing and conducting investigations** [U2.3]: design, plan and conduct investigations;
   explain how reliability, accuracy, precision, error, fairness, safety, integrity and the
   selection of suitable equipment have been considered.
3. **Objectivity and data quality** [U2.3–U2.4]: identifying potential sources of random and
   systematic error; evaluating data in terms of repeatability and reproducibility.
4. **Producing and analysing data** [U2.4]: produce and select qualitative and quantitative
   data; critically analyse data to identify patterns and relationships; identify anomalous
   observations; draw and justify conclusions.
5. **Reflecting on investigations** [U2.5]: review and reflect on the skills and thinking used;
   apply learning and skills to solving problems in unfamiliar contexts.
6. **Communicating results** [U2.6]: organise and communicate research and investigative
   findings in ways fit for purpose and audience, using relevant scientific terminology and
   representations.
7. **The Biology in Practice Investigation (40%)** [Assessment]:
   - The SEC publishes an Investigation Brief each year in term two of Year 1. It sets out the
     requirements, includes stimulus material to set a context, and lets students develop
     ideas they want to pursue and keep an investigative log.
   - Students carry out scientific research on an issue related to the brief (gathering,
     processing and evaluating information from secondary sources) and an experiment related
     to an issue within the brief (hypothesis, plan, design, primary data, analysis,
     conclusions).
   - They develop an evidence-based argument in response to the brief and submit a report in
     Year 2, in a format prescribed by the SEC. The specification envisages up to 20 hours of
     work.
   - Descriptors of quality: knowledge and understanding; investigative skills (design and
     method); investigative skills (analysis and conclusions); relating the investigative work
     to the work of scientists in society. Describe what high, moderate and low achievement look
     like for each.
   - Students should give an authentic account of how their work unfolded and how they might
     revise the process. A separate SEC/NCCA document, *Guidelines for the Biology in Practice
     Investigation*, covers organisation.
   - SimpleStudy: Assessment: Biology in Practice Investigation.

### bio3 — Science in Society [U3]
1. **Evaluating evidence** [U3.1]: evaluating evidence for relevance, accuracy and bias;
   evaluating media-based arguments concerning science and technology.
   SimpleStudy: Science in Society.
2. **Science, scientists and society** [U3.2]: research and present information on the
   contribution scientists make to discovery and invention, and evaluate its impact on
   society, considering economic, social, sustainability and ethical factors.
3. **The cross-cutting themes** [Strands overview]: Health, Sustainability and Technology as
   lenses for contemporary issues in biology.

### bio4 — Biological Reasoning [U4]
1. **Models** [U4.1]: generating and using models; models are simplified representations of
   complex systems or phenomena with underlying assumptions; they can be modified as more data
   become available; they can predict the behaviour of a system. The specification's footnote
   defines a model as a representation of ideas, structures, processes or systems in words,
   diagrams, equations, physical models or simulations.
   SimpleStudy: Biological Reasoning.
2. **Explaining biological phenomena** [U4.2]: using appropriate means, including systems;
   interdependence, unity and diversity of life; form fits function; transfer of information,
   matter and energy.

---

## Strand 1 — Organisation of Life [1.1–1.5]

### bio5 — Characteristics of Life [1.1.1, 1.3.1]
1. **Characteristics of living things** [1.1.1]: outline the characteristics of living things.
   The specification lists eleven: organisation, response, respiration, nutrition, excretion,
   reproduction, growth, metabolism, homeostasis, heredity and cellular basis. Cover all eleven.
   SimpleStudy: Characteristics of Life.
2. **Levels of organisation** [1.3.1]: organisation of life in increasing complexity from
   individual cells to organism level (cell, tissue, organ, organ system, organism); describe
   the complexity of multicellular organisms.

### bio6 — Viruses, Classification and Domains of Life [1.1.2–1.1.4]
1. **Viruses** [1.1.2]: the structure and functions of a virus, including its constituents (DNA
   or RNA, protein coat); discuss the difficulty of defining viruses, and their economic and
   medical importance. Virus replication and DNA vs RNA viruses are in `bio22`.
   SimpleStudy: Classification of Life (the "Viruses" unit).
2. **Domains of life** [1.1.3]: archaea, bacteria and eukaryota; outline the domains of life
   system based on genetic characteristics.
3. **Classification** [1.1.4]: classification systems as evolving and important; taxonomic
   classification including the kingdoms bacteria, archaea, protista, fungi, plantae and
   animalia; prokaryotic and eukaryotic as a means of classifying; phylogeny (classification
   based on evolutionary development, with reference to genus and species); emerging evidence
   that enhances classification systems. Use classification principles to identify and classify
   living things in known and unknown contexts (e.g. with a key); outline why classification
   matters in biology.
   - Settings: the six kingdoms as listed. The previous syllabus's five-kingdom system with
     "Monera" is not used.

### bio7 — The Unit of Life — The Cell [1.3.2–1.3.3]
1. **Prokaryotic and eukaryotic cells** [1.3.2]: compare their structure, using images of cells
   and their parts from light and electron microscopes.
   SimpleStudy: Unit of Life: The Cell.
2. **Microscopy** [1.3.3]: existing and emerging fields, including optical and electron
   microscopy; the use and function of a light microscope; preparing and mounting a slide for
   viewing.
3. **Structures and organelles of animal and plant cells** [1.3.3]: cell wall, cell membrane,
   cytoplasm, vacuole, mitochondrion, chloroplast, nucleus, nuclear pore, ribosome, chromosome,
   **[HL] endoplasmic reticulum, [HL] Golgi apparatus**; relate each to its function.
4. **Investigation: plant and animal cells** [1.3.3]: investigate the structures and organelles
   using primary data from a light microscope and secondary data from scanning electron
   microscope imagery.
   SimpleStudy: Experiments: light-microscope cell investigation.

### bio8 — Biomolecules — The Chemicals of Life [1.2.1–1.2.6]
1. **Biomolecules and metabolism** [1.2.1]: biomolecules in living cells involved in anabolism,
   catabolism, energy transfer, the formation of structural units and rearrangement into new
   molecules.
   SimpleStudy: Biomolecules: The Chemicals of Life.
2. **Structures** [1.2.1]:
   - carbohydrates, Cx(H2O)y: mono-, di- and polysaccharides
   - lipids: the triglyceride unit and different combinations in fats, oils and phospholipids
   - proteins: peptides and polypeptides folded into shapes, made of amino acids, containing C,
     H, O, N and sometimes S, P or other elements
   - nucleic acids, made of nucleotides (detail in `bio10`).
3. **Metabolic roles and nutritional sources** [1.2.1]: hormones as regulators; protein roles
   including enzymes, hormones, membrane interactions and immunity; proteins needed for
   molecular mechanisms, including channel proteins, transporters, structural proteins and
   receptors; carbohydrates and lipids in catabolic, anabolic, respiratory and photosynthetic
   functions; nutritional sources of carbohydrate, lipid and protein.
4. **Minerals** [1.2.2]: needed in small amounts, not necessarily integrated into biomolecules,
   for pH balance, regulation of enzyme systems, nerve impulse transfer and muscle contraction;
   their sources.
5. **Vitamins** [1.2.3]: water-soluble and fat-soluble vitamins; the biological significance of
   vitamin solubility; the role of **one water-soluble and one fat-soluble vitamin** in humans,
   with the associated deficiency disease. Cover at least vitamin C (scurvy) and vitamin D
   (rickets), and note others students may choose.
6. **Water** [1.2.4]: main roles in living organisms, including a medium for transport and
   chemical reactions, regulation of temperature, pH and osmoregulation.
7. **Investigation: food tests** [1.2.5]: investigate qualitatively the presence of
   carbohydrates, protein and lipids in a range of food samples; use primary data to support
   conclusions.
8. **Investigation: reducing sugars, quantitatively** [1.2.6]: investigate the level of
   reducing sugars in a range of food samples; use primary data to support conclusions.
   SimpleStudy (items 7–8): Experiments: substance tests; reducing sugars in foods.

### bio9 — Transfer Molecules [1.2.8]
1. **ATP** [1.2.8]: transfer molecules in cell activities, including ATP in transferring energy;
   outline the role of ATP in metabolic pathways.
   SimpleStudy: Transfer Molecules.
2. **[HL] NAD+ and NADP+** [1.2.8]: their role in electron transfer, with different roles in
   photosynthesis (NADP+) and respiration (NAD+); outline their role in metabolic pathways. Their
   use in each process is detailed in `bio14` and `bio15`.

### bio10 — DNA, RNA and the Genetic Code [1.2.7, 1.2.9]
1. **Nucleotides, DNA and RNA** [1.2.7]: describe the basic structure and function of a DNA and
   an RNA nucleotide: a sugar (ribose in RNA, deoxyribose in DNA), a phosphate and a nitrogenous
   base. DNA is a double-stranded helix with adenine–thymine and cytosine–guanine base pairs.
   The basic structure of RNA, with reference to uracil.
   SimpleStudy: DNA, RNA, and the Genetic Code.
2. **Genes, proteins and traits** [1.2.9]: relate genes, proteins and traits in organisms.
3. **[HL] The genetic code** [1.2.9]: DNA contains a genetic code, which is read by cellular
   machinery to produce proteins, with reference to codons and anticodons; outline the concept
   of the genetic code. Transcription and translation are in `bio17`.

### bio11 — Genetic Inheritance [1.4]
1. **Chromosome structure and genes** [1.4.1]: chromosome structure, including protein
   **[HL] (histones)** and DNA, **[HL] chromatids, [HL] centromere**, reference to chromatin,
   and coding and non-coding DNA; describe the structure of a chromosome and the role of a gene.
   SimpleStudy: Genetic Inheritance.
2. **Key concepts of information transfer** [1.4.1]: species, gamete, sexual reproduction,
   fertilisation, heredity, chromosome, allele, gene expression, dominance, recessive, genotype,
   phenotype, **[HL] epigenetic expression, [HL] incomplete dominance, [HL] linkage, [HL]
   sex-linkage**.
3. **Nuclear and non-nuclear inheritance** [1.4.2]: explain nuclear inheritance (transmission of
   DNA); **[HL] compare it to non-nuclear inheritance in mitochondrial and chloroplast DNA.**
4. **Genetic and epigenetic mechanisms** [1.4.3]: inheritance through passing on DNA; the
   concept of epigenetics (how behaviours and environment influence gene expression, some
   changes being reversible); compare genetic and epigenetic mechanisms; **[HL] research one
   example of epigenetic inheritance in nature.** Write more than one example (e.g. the Dutch
   Hunger Winter, agouti mice, honeybee queen/worker caste, vernalisation in plants) and check
   each fact.
5. **Monohybrid crosses** [1.4.4]: model inheritance to the first generation of a single
   unlinked trait, in crosses involving homozygous and heterozygous parents.
6. **[HL] Incomplete dominance** [1.4.5]: model a cross involving incomplete dominance.
7. **[HL] Mendel's Laws** [1.4.6]: illustrate and state Mendel's Laws of Segregation and
   Independent Assortment.
8. **[HL] Dihybrid crosses** [1.4.7]: model inheritance to the second generation of two
   unlinked traits, in crosses involving homozygous and heterozygous parents.
9. **[HL] Linkage** [1.4.8]: explain how linkage affects Mendel's Law of Independent
   Assortment. The specification says "knowledge of crossing over not required"; don't teach
   it here.
10. **Sex determination** [1.4.9]: model sex determination by X and Y chromosomes in humans.
11. **[HL] Sex-linked traits** [1.4.10]: model the inheritance of sex-linked traits from known
    examples. Settings: colour blindness and haemophilia.
12. **Benefits and limitations of Mendelian genetics** [1.4.11]: its predictive power; Mendel's
    Laws do not apply to complex traits involving multiple gene interactions or environmental
    factors; identify benefits and limitations for understanding heredity in the modern world.

### bio12 — Evolution: The Origins of Life [1.5]
1. **Variation** [1.5.1]: explain the variation that comes from sexual reproduction and from
   mutations (gene and chromosome).
   SimpleStudy: Evolution: The Origins of Life.
2. **The theory of evolution by natural selection** [1.5.2]: evolutionary theory as a mechanism
   for explaining and predicting common origins and future directions for highly specialised
   organisms; natural vs artificial selection; the rationale for, and basis of, the theory.
3. **Evidence for evolution** [1.5.3]: consider the evidence. Settings: embryology, fossil
   records, phylogeny, comparative anatomy, antibiotic resistance, speciation, "etc."
4. **The importance of the theory** [1.5.3]: the concept of a theory; evolution as one of the
   most widely accepted and tested theories in science; why it presents the best available
   explanation for how life on Earth has evolved and continues to evolve; its importance in
   understanding biology.

---

## Strand 2 — Structures and Processes of Life [2.1–2.6]

### bio13 — Enzymes [2.1]
1. **Enzymes as catalysts** [2.1.1]: enzymes as selective catalysts that control biochemical
   reactions; their importance in metabolism; explain how enzymes facilitate catalysis.
   SimpleStudy: Enzymes.
2. **[HL] Enzyme structure and specificity** [2.1.2]: the importance of 3D structure for
   enzyme specificity and activity; illustrate enzyme activity using the Induced Fit model.
3. **Investigation: rate of enzyme activity** [2.1.3]: rate (conversion of substrate into
   product per unit time) is influenced by substrate concentration, enzyme concentration,
   environmental pH and temperature, and is subject to denaturation. Investigate these factors;
   use primary and secondary data to support conclusions. Write the investigation for each
   factor.
   SimpleStudy: Experiments: enzyme-rate factors.
4. **Industrial enzymes** [2.1.4]: research the use of enzymes in industries and recognise
   their central role, including immobilised enzymes. Settings: food and beverages, biofuels,
   medicine, pharmaceuticals.

### bio14 — Photosynthesis [2.2.1–2.2.2, 2.2.4–2.2.5]
1. **Photosynthesis as an anabolic process** [2.2.1]: photosynthesis as a carbon sink, producing
   glucose in plants and leading to sucrose and complex carbohydrates; the sources of reactants
   and products; the overall sequence, its cellular location and the balanced equation; outline
   the process.
   SimpleStudy: Photosynthesis.
2. **Investigation: rate of photosynthesis** [2.2.2]: factors including temperature, light
   intensity and CO2 levels; use primary and secondary data to support conclusions.
   SimpleStudy: Experiments: photosynthesis-rate factors.
3. **[HL] The light-dependent reactions** [2.2.4]:
   - Non-cyclic pathway: a photon of light is absorbed and passed from one pigment molecule to
     others in the chloroplast until it reaches a reaction centre in a chlorophyll molecule.
     Photolysis of water, caused by attraction from the positively charged chlorophyll molecule,
     produces oxygen. Electron transfer produces ATP and NADPH (from NADP+).
   - Cyclic pathway: some electrons return to chlorophyll and transfer surplus energy to form ATP
     in an alternative pathway.
4. **[HL] The light-independent reactions** [2.2.4]: NADPH and ATP enter the reactions; protons
   and electrons are transferred from NADPH to CO2 to produce C6H12O6, with energy from ATP; ADP
   and NADP+ return to the light-dependent reactions to be re-used. Model the two-stage
   process, with particular reference to the transfer molecules.
5. **[HL] The chloroplast's internal structure** [2.2.5]: an electron transport chain of protein
   complexes and mobile electron carriers embedded in the thylakoid membrane; recognise how the
   internal structure of chloroplasts facilitates photosynthesis.

### bio15 — Respiration [2.2.1, 2.2.3–2.2.5]
1. **Respiration as a catabolic process** [2.2.1]: its role in carbon release and energy
   transfer (as ATP) for cellular activities; the sources of reactants and products; the
   overall sequence, cellular locations and balanced equations; outline anaerobic and aerobic
   respiration.
   SimpleStudy: Respiration.
2. **Investigation: conditions for fermentation** [2.2.3]: the presence of sugars and
   microorganisms (yeast or bacteria), an anaerobic environment and a suitable temperature; use
   primary and secondary data to support conclusions.
   SimpleStudy: Experiments: fermentation conditions.
3. **[HL] First-stage process** [2.2.4]: glycolysis, the conversion of a six-carbon
   carbohydrate to pyruvate, generating ATP. Fermentation products, depending on organism and
   conditions, are either ethanol or lactic acid.
4. **[HL] Second-stage process** [2.2.4]: pyruvate is broken down to produce acetyl CoA and one
   molecule of carbon dioxide; acetyl CoA enters the citric acid cycle, producing CO2 and H2O.
   Electrons from the cycle are transferred through an electron transport chain; energy from
   this transfer produces ATP for other biochemical reactions. Model the two-stage process,
   with particular reference to the transfer molecules.
5. **[HL] The mitochondrion's internal structure and ATP synthase** [2.2.5]:
   - Electron transport chains of protein complexes and mobile electron carriers are embedded
     in the mitochondrial membrane.
   - Transfer of electrons to the complexes causes a charge difference that attracts protons,
     given by donor molecules.
   - The protons pass through the complex to outside the mitochondrial inner membrane, creating
     a high proton concentration there.
   - The protons flow back down the gradient, across the inner membrane, through the enzyme ATP
     synthase, which harnesses the flow to make ATP.
   - Recognise how the internal structures of mitochondria facilitate respiration, and compare
     with the thylakoid membrane in `bio14`.

### bio16 — Cell Division and Cancer [2.3.1–2.3.3, 2.3.7–2.3.8]
1. **The cell cycle** [2.3.1]: growth, DNA synthesis and division; outline the cell cycle.
   **[HL] Its stages: interphase (cell growth and DNA replication); nuclear division (prophase,
   metaphase, anaphase and telophase); cytokinesis.** The concepts of haploid and diploid.
   SimpleStudy: Cell Division and Cancer.
2. **Mitosis and meiosis** [2.3.2]: cell division as transmission of the genetic code to the
   next generation. In mitosis the genetic information remains the same; meiosis varies it.
   Compare their roles in transmitting genetic information in unicellular and multicellular
   organisms.
3. **DNA replication and mitosis in the cell cycle** [2.3.3]: DNA replication is facilitated by
   enzymes and separates the double strand into two single strands, each a template for a
   complementary strand; explain the role of replication and mitosis in the cell cycle. The
   [HL] model of replication is in `bio17`.
4. **Cancer** [2.3.7]: the characteristics and growth of cancer cells, including abnormal
   regulation of mitotic division and rate; outline how uncontrolled cell proliferation can
   lead to cancers.
5. **Causes, prevention and treatment of cancer** [2.3.8]: examine the role of infectious
   agents, environmental factors and/or genetic susceptibility in the development of different
   cancers; evaluate factors that affect their development. Emerging evidence in cancer
   research. Settings: early detection, treatments, vaccination, lifestyle changes.

### bio17 — DNA Replication, Protein Synthesis and Mutations [2.3.4–2.3.6]
1. **[HL] Modelling DNA replication and information flow** [2.3.4]: model how DNA is replicated
   and how information flows through mRNA to protein. Genetic information is transcribed from
   DNA to mRNA, which moves to ribosomes where it is translated into specific proteins.
   SimpleStudy: DNA Replication, Protein Synthesis, and Mutations.
2. **[HL] Transcription and translation** [2.3.5]: the roles of DNA, mRNA, tRNA, rRNA,
   polymerase and ribosomes in transcribing and translating the genetic code into amino acids,
   arranged in the correct sequence to make the protein, which folds into its functional shape.
   Model the processes; relate the structure of tRNA to the codon nature of the genetic code.
3. **[HL] Mutations** [2.3.6]:
   - Point mutation: incorrect base pairing during replication changes the nucleotide sequence,
     by deletion, insertion or substitution.
   - Chromosomal mutation: a change in genes in one or more chromosomes, by deletion,
     duplication, inversion or translocation.
   - Model how both occur, with known examples of each (e.g. sickle-cell anaemia and cystic
     fibrosis for point mutations; cri du chat, a deletion, and the Philadelphia translocation
     in chronic myeloid leukaemia for chromosomal). Down syndrome is a change in chromosome
     number, not one of the four structural changes listed; say so if it is used. Check each
     example.

### bio18 — The Musculoskeletal System [2.4.1, 2.4.2–2.4.3]
1. **The musculoskeletal system as a system for response** [2.4.1]: its place among the
   structures and systems for response (overview in `bio21`).
   SimpleStudy: The Musculoskeletal System.
2. **The axial skeleton** [2.4.2]: skull, vertebrae, ribs, sternum; the position and function of
   discs in relation to the vertebrae; relate structure to function.
3. **The appendicular skeleton** [2.4.2]: the pectoral girdle (clavicle, scapula); the pelvic
   girdle (names of its bones not required); the limbs (femur, patella, tibia, fibula, humerus,
   radius, ulna); relate structure to function.
4. **Muscles and joints** [2.4.3]: model the function of an antagonistic muscle pair; relate the
   functions of cartilage, ligaments and tendons in synovial joints.
   - Disorders of the musculoskeletal system aren't on this specification.

### bio19 — The Nervous System [2.4.4, 2.4.6–2.4.9]
1. **CNS and PNS** [2.4.4]: the central nervous system (brain and spinal cord); the peripheral
   nervous system (location of nerve fibres and cell bodies); relate the structure of their
   parts to their functions.
   SimpleStudy: The Nervous System.
2. **The reflex action** [2.4.4]: its role, structure and mechanism. Cranial nerves and the
   sympathetic and parasympathetic systems are not required.
3. **Neurons** [2.4.6]: cell body, dendrites, axon, myelin sheath, Schwann cell and
   neurotransmitter vesicles; relate the structures of a motor and a sensory neuron to their
   functions.
4. **Neurotransmission** [2.4.7]: transmission of the impulse via sensory, motor and
   interneurons; explain the role of neurotransmitters at a synapse in conducting impulses,
   involving the movement of ions (detailed electrochemistry not required).
5. **[HL] Conduction across the synaptic cleft and its disruption** [2.4.8]:
   - Neurotransmitters, activated by ions, are released into the cleft for a short time,
     transmitting the impulse to the next neuron.
   - The neurotransmitter is then inactivated by an enzyme and reabsorbed by the presynaptic
     neuron to make new neurotransmitter.
   - Disruptions to this mechanism cause acute and chronic disorders. These are treated with
     drugs that inhibit the enzymes that degrade neurotransmitters, or that inhibit their
     reuptake at the synapse, creating an enhanced effect. Psychoactive drugs and painkillers
     work in similar ways.
   - Model impulse travel across the cleft and consider the impact of disruptions.
6. **Dopamine and endorphins** [2.4.9]: neurotransmission affects mood and behaviour; the
   functions of endorphins and dopamine; lifestyle choices that affect their levels (non-medical
   drug use, exercise, dietary choices); discuss their roles.

### bio20 — The Endocrine System [2.4.10–2.4.11]
1. **Glands, locations and hormones** [2.4.10]: identify the location of each gland and
   describe the functions of its hormones:
   - adrenal (adrenaline)
   - pituitary (oxytocin, TSH, **[HL] FSH, [HL] LH, [HL] ADH**)
   - thyroid (thyroxine)
   - parathyroid (parathyroid hormone)
   - pancreas (insulin)
   - testes (testosterone)
   - ovaries (oestrogen, progesterone).
   - SimpleStudy: The Endocrine System.
2. **Hormonal manipulation** [2.4.11]: recognise the impact of hormonal manipulation on
   organisms. Settings: sport, health and agriculture.

### bio21 — Homeostasis [2.4.1, 2.4.5; 1.1.1]
1. **Structures and systems for response** [2.4.1]: outline the structures and systems for
   response in humans (hormonal, nervous, musculoskeletal and immune systems) and in plants
   ("various anatomical and chemical adaptations in plants"). The plant part has no other home
   in the app; see Appendix B.
   SimpleStudy: Homeostasis.
2. **Homeostasis as a stimulus–response model** [2.4.5]: resistance to external or internal
   change; appropriate responses occur via negative feedback; in vertebrates, nervous and
   hormonal pathways link a control centre with receptors and effectors. Homeostasis is also one
   of the characteristics of life [1.1.1].
3. **Nervous vs hormonal coordination** [2.4.5]: compare them.

### bio22 — Immunity [2.4.12–2.4.16]
1. **Pathogens** [2.4.12]: prions, viruses, bacteria, fungi, protists and parasitic animals.
   SimpleStudy: Immunity.
2. **Innate and adaptive immunity** [2.4.12]: the innate immune response to pathogens; the
   adaptive immune response of vertebrates, including the antigen–antibody response; **[HL] B
   and T lymphocyte roles in the cell-mediated immune response**; distinguish innate from
   acquired immunity.
3. **Acquired immunity, prevention and treatment** [2.4.12]: immunity acquired by infection,
   by vaccination (active), or by donor transfer of antibodies (passive), e.g. antibody booster
   injections and breastfeeding; outline strategies to prevent and treat microbial diseases.
4. **Viruses: replication** [2.4.13]: modes of action and replication; differences between DNA
   and RNA viruses; model how viruses replicate within cells.
5. **[HL] White blood cells** [2.4.14]: monocytes, natural killer cells, B lymphocytes, and T
   lymphocytes (helper, killer, suppressor and memory); compare their roles in the immune
   response.
6. **Emergence and spread of infectious disease** [2.4.15]: transmission facilitated by local,
   regional and global movement of organisms. Emergence and spread depend on interrelated
   factors: persistence of the pathogen in a host; mutations; antibiotic or chemical
   resistance; the level of immunity in the population; mobility of affected populations; the
   reproduction number (R0). Explore these factors in plants and animals.
7. **Emerging diseases and society** [2.4.16]: novel viruses in plants and animals;
   autoimmune diseases; understanding the factors that increase numbers enables strategies to
   control the increase; discuss why knowledge of emerging diseases matters to society.

### bio23 — Human Reproduction [2.5.1–2.5.6]
1. **The male reproductive system** [2.5.1]: penis, foreskin, glans, scrotum, testes,
   epididymis, urethra, vas deferens, seminal vesicle, prostate; relate structure to function.
   SimpleStudy: Human Reproduction.
2. **The female reproductive system** [2.5.1]: vulva, clitoris, labia, vagina, cervix, uterus,
   endometrium, fallopian tube, ovary; relate structure to function.
3. **Gametes and fertilisation** [2.5.1]: gamete production by meiosis; fertilisation.
4. **The menstrual cycle** [2.5.2]: its four phases (menstruation, follicular phase, ovulation,
   luteal phase); outline them. **[HL] The changes in levels of oestrogen, progesterone, LH and
   FSH in each phase, with reference to the Graafian follicle and corpus luteum.**
5. **Pregnancy** [2.5.3]: fertilisation, implantation, placenta formation, foetal development
   (zygote, **[HL] morula, blastocyst, germ layers, embryo, foetus**), labour and birth; describe
   pregnancy from the fertilised zygote to birth.
6. **Hormones in reproduction** [2.5.4]: their influence on puberty, sperm and egg production,
   the menstrual cycle, implantation, growth of the foetus, birth, production of colostrum and
   milk, and menopause. The roles and levels of testosterone, progesterone, oestrogen, oxytocin,
   prolactin, **[HL] FSH and [HL] LH**. Model their role in the male and female systems.
7. **Prenatal and postnatal care** [2.5.5]: monitoring the health of the mother and developing
   foetus; appreciate the impact of modern technology. Settings: antenatal screening, genetic
   screening, postnatal screening (including for PKU).
8. **Fertility control and infertility** [2.5.6]:
   - Fertile periods: continuous for males, cyclical for females.
   - Natural, mechanical, surgical and chemical methods of contraception and their use,
     including prevention of STIs; freezing eggs.
   - Treatments for infertility based on the biology of fertility: stimulating ovulation,
     artificial insemination, intracytoplasmic sperm injection (ICSI), in vitro fertilisation.
   - Discuss the use and biological implications of these strategies and treatments.

### bio24 — Plant Reproduction [2.5.7–2.5.8]
1. **Flower structure and pollination** [2.5.7]: the reproductive structures of flowering
   plants (flowers, seeds, fruits) and their functions; flower structures (sepal, petal, stamen,
   anther, filament, stigma, style, ovary, carpel, receptacle) and their functions; the role of
   flowers in pollination.
   SimpleStudy: Plant Reproduction.
2. **Investigation: insect- and wind-pollinated plants** [2.5.7]: adaptations of these
   structures depending on whether the plant is insect- or wind-pollinated; investigate and
   compare the structures and relate them to their functions; use primary and secondary data to
   support conclusions.
   SimpleStudy: Experiments: insect- and wind-pollinated plant structures.
3. **Seeds** [2.5.8]: seed structures (testa, plumule, radicle, embryo, endosperm) and their
   functions; the role of seeds in producing growth regulators that stimulate growth of fruit
   tissues; describe the role of seeds in plant reproduction.
4. **Fruit and seed dispersal** [2.5.8]: methods including wind, water and animal (internal
   and external).
   - Germination, seed dormancy and vegetative propagation aren't on this specification.

### bio25 — Transport Across Membranes [2.6.1–2.6.2]
1. **Diffusion, osmosis and active transport** [2.6.1]: the transport and transfer of materials
   across membranes; distinguish the three processes.
   SimpleStudy: Transport Across Membranes.
2. **Osmosis in food preservation and plant health** [2.6.1]: examine its role in each.
3. **Investigation: rate of osmosis** [2.6.2]: factors including temperature, concentration
   gradient and surface area, across semi-permeable membranes; use primary data to support
   conclusions.
   SimpleStudy: Experiments: osmosis-rate factors.

### bio26 — The Urinary System [2.6.3]
1. **The urinary system** [2.6.3]: transport and transfer of nutrients and wastes between the
   internal and external environment in humans; kidneys, ureters, urinary bladder and urethra;
   regulation of body fluids by the kidney; filtration and reabsorption in the cortex, medulla
   and renal pelvis; transport of urine from kidney to urethra. Relate the macrostructure to its
   function in filtering and removing waste.
   SimpleStudy: The Urinary System.
2. **[HL] The nephron** [2.6.3]: nephron structure and blood supply. Filtration of blood, and
   reabsorption of water, glucose, amino acids and some salts, in Bowman's capsule, glomerulus,
   proximal convoluted tubule, loop of Henle and distal convoluted tubule. Outline the
   filtration of blood in the nephron.
3. **[HL] ADH and osmoregulation** [2.6.3]: the role of ADH in osmoregulation.

### bio27 — The Digestive System [2.6.4–2.6.6]
1. **The digestive system** [2.6.4]: ingestion, digestion, absorption and egestion; the mouth,
   oesophagus, stomach, pancreas, liver, gallbladder, small intestine, large intestine, rectum
   and anus.
   SimpleStudy: The Digestive System.
2. **Mechanical breakdown** [2.6.4]: the role of teeth, peristalsis, the stomach, and bile salts
   in emulsification.
3. **Chemical breakdown** [2.6.4]: digestion by enzymes and bile salts, including their roles,
   production sites, the pH at a named location, and the products of an amylase, a protease and
   a lipase. Model how the system digests fats, carbohydrates and proteins.
4. **Absorption, transport and storage** [2.6.5]: absorption of nutrients and water into the
   blood through the villi; the hepatic portal vein; glycogen storage and deamination of
   proteins in the liver; absorption of water and elimination of faeces through the large
   intestine.
5. **Diet** [2.6.6]: the importance of a balanced diet as related to health, age, gender,
   activity, variety of foods, sufficient water and dietary fibre; research the biological
   implications of dietary choices.

### bio28 — The Breathing System [2.6.7–2.6.8]
1. **Gas exchange and the breathing mechanism** [2.6.7]: exchange of gases between the internal
   and external environment, facilitated by the breathing system; the macrostructure and
   function of the breathing tract; the breathing mechanism (diaphragm, intercostal muscles,
   brain, CO2 levels); exchange at the alveoli and capillaries. Relate anatomy and physiology to
   gaseous exchange in the lungs.
   SimpleStudy: The Breathing System.
2. **[HL] CO2 as a controlling factor in breathing** [2.6.8]: outline the role of carbon dioxide
   concentration as a controlling factor in the human breathing system. Its role in plant
   stomata is in `bio30`.

### bio29 — The Circulatory System and Blood [2.6.9–2.6.13]
1. **Investigation: the heart** [2.6.9]: structures (septum, atria, ventricles, arteries, veins,
   valves, cardiac muscle tissue); investigate them and relate them to their functions; use
   primary and secondary data to support conclusions.
   SimpleStudy: The Circulatory System; Experiments: heart structure.
2. **Circulation** [2.6.10]: transport of materials within humans; the two-circuit system
   (pulmonary and systemic); the pathways of blood circulation (pulmonary, systemic, portal).
   Model the interaction between the circulatory system and other body systems.
3. **Heartbeat** [2.6.11]: the role of the pacemaker in regulating heartbeat; pulse and blood
   pressure; the heart sustained by its own blood supply via coronary arteries and cardiac
   veins. The specification says "cardiac cycle not required"; leave out systole, diastole and
   the cycle's phases.
4. **Blood** [2.6.12]: composition of blood; structure and role of red blood cells, white blood
   cells, platelets and plasma; blood groups; Rhesus factors. Relate composition to function;
   appreciate why knowledge of blood grouping matters for health.
5. **Blood vessels** [2.6.13]: distinguish arteries, veins and capillaries by macrostructure and
   role.

### bio30 — Transport in Plants [2.6.8, 2.6.14–2.6.16]
1. **Plant structures for transport** [2.6.14]: leaves and lenticels; the root and shoot system
   (root hairs, root cortex) and its tissues: dermal, ground and vascular (xylem and phloem).
   Relate the structure of root, stem and leaf and their tissues to function.
   SimpleStudy: Transport in Plants.
2. **Transport of water and minerals** [2.6.15]: osmosis, diffusion, **[HL] root pressure, [HL]
   cohesion and tension**, transpiration and stomata.
3. **Transport of CO2 and photosynthetic products** [2.6.15]: carbon dioxide (respiring cells
   and stomata); photosynthetic products; **[HL] CO2 as a controlling factor in plant stomata**.
   Explain the transport of water, minerals, CO2 and photosynthetic products.
4. **[HL] CO2 as a controlling factor in plant stomata** [2.6.8]: outline its role; link to
   breathing in `bio28`.
5. **Investigation: rate of transpiration** [2.6.16]: factors including air movement,
   temperature, surface area, presence or absence of cuticle, light intensity and CO2
   concentration; use primary and secondary data to support conclusions.
   SimpleStudy: Experiments: transpiration-rate factors.

---

## Strand 3 — Interactions of Life [3.1–3.3]

### bio31 — Ecology, Ecosystems and Biodiversity [3.1.1–3.1.10]
1. **Key terms** [3.1.1]: outline what is meant by the biosphere, ecosystems, habitats and
   biodiversity.
   SimpleStudy: Ecology, Ecosystems, and Biodiversity.
2. **Biodiversity loss and conservation** [3.1.2]: explore local ecosystems through current news
   and local media; biodiversity loss has environmental, economic, social and cultural impacts;
   discuss its impact in local ecosystems and the role of conservation in limiting it.
3. **Investigation: human activity and species diversity** [3.1.3]: evaluate primary or
   secondary data on the effects of human activity on species diversity.
   SimpleStudy: Experiments: human effects on species diversity.
4. **[HL] Simpson's Diversity Index** [3.1.4]: species diversity index Ds, the variety of
   species in a given area, calculated as Ds = 1 − Σn(n−1) / N(N−1), where n is the total
   number of organisms of a particular species and N is the total number of organisms of all
   species. Model species diversity using the equation, with worked examples.
5. **Carrying capacity and limiting factors** [3.1.5]: abiotic factors (water, oxygen, space,
   temperature, soil) and biotic factors (food, disease, competition, predation); illustrate how
   they determine carrying capacity for species in Irish ecosystems.
6. **[HL] Population curves** [3.1.6]: S-shaped curves in resource-limited environments;
   J-shaped curves where resources are unlimited; consider how carrying capacity for species in
   Irish ecosystems varies with limiting factors.
7. **Energy and nutrient transfer** [3.1.7]: models for the movement of matter and energy through
   ecosystems, used to explain and predict the impact of change; trophic levels; food chains and
   webs; consider how nutrients pass between trophic levels, with energy lost at each level.
8. **Pyramids of numbers** [3.1.8]: outline their use in the study of ecosystems. **[HL] Their
   shapes and limitations.**
9. **[HL] Pyramids of biomass** [3.1.9]: compare the use of pyramids of numbers and pyramids of
   biomass in the study of ecosystems.
10. **The niche** [3.1.10]: outline the concept, with examples, as it applies to adaptations of
    organisms in ecosystems.

### bio32 — Investigating an Ecosystem [3.1.11]
1. **Collection and identification** [3.1.11]: observation and collection methods (traps,
   pooter, nets, etc.); identifying organisms.
   SimpleStudy: Investigating an Ecosystem; Experiments: organism identification.
2. **Surveys** [3.1.11]: qualitative and quantitative surveys; model a habitat in the chosen
   ecosystem, including its size, species, and relevant biotic and abiotic factors, using
   primary data.
   SimpleStudy: Experiments: qualitative ecosystem survey.
3. **Abiotic factors** [3.1.11]: measurement of air, ground, aquatic and edaphic factors,
   including water, oxygen, space, temperature, soil, aspect, wind speed and slope;
   investigate quantitatively how variation in an abiotic factor affects the distribution and
   abundance of a species.
   SimpleStudy: Experiments: abiotic factors and species distribution.
4. **Biotic factors and relationships** [3.1.11]: predation, **[HL] competition, [HL] symbiosis
   (mutualism, commensalism, parasitism)**; explain the feeding **[HL] and symbiotic**
   relationships between organisms. Use examples from the chosen ecosystem.

### bio33 — Microorganisms [3.2.1–3.2.4]
1. **Bacteria and fungi** [3.2.1]: organisms involved in nutrient cycling; the structure of a
   bacterial cell and of the fungus Rhizopus; nutrition (autotrophic, heterotrophic,
   saprophytic, parasitic); cellular nature (bacteria prokaryotic, fungi eukaryotic).
   Distinguish bacteria and fungi in structure, nutrition and cellular nature.
   SimpleStudy: Microorganisms (the "Bacteria" unit).
2. **Investigation: growth of microorganisms** [3.2.2]: factors including pH, nutrients, water,
   external solute concentrations, temperature, and the presence of antibacterial or antifungal
   chemicals; use primary and secondary data to support conclusions.
   SimpleStudy: Experiments: microorganism growth.
3. **Microorganisms in industry** [3.2.3]: their use in pharmaceutical, agricultural, medical and
   food production industries; discuss their importance. **[HL] Growth curves of
   microorganisms (lag, log, stationary, decline/death, survival), and knowledge of growth
   curves used to increase yields in industry.**
4. **The microbiome** [3.2.4]: outline the concept of a microbiome; the gut microbiome's role in
   human health (digestion, immune signalling, metabolic health); soil microbiomes cycling
   multiple nutrients; how climate warming influences the functioning of soil microbiomes.
   Explore the role of microbiomes in human health and in nutrient cycling in soils.

### bio34 — Nutrient Cycling [3.2.5–3.2.8]
1. **The carbon cycle** [3.2.5]: model it, with reference to photosynthesis, respiration,
   decomposers (bacteria and fungi), fossil fuels and carbon sinks.
   SimpleStudy: Nutrient Cycling.
2. **The nitrogen cycle** [3.2.6]: model it, with reference to nitrogen fixation, nitrification,
   decomposition and denitrification. Names of microorganisms are not required.
3. **Ethics and sustainability of nutrient cycling** [3.2.7]: evaluate the ethical and
   sustainability issues involved.
4. **Climate change and biological strategies** [3.2.8]: carbon sinks (plants, algae,
   phytoplankton, bogs, etc.); the link between atmospheric CO2, methane and climate change;
   evaluate biological strategies to reduce the levels of these gases; the role biology will
   play in a post-fossil-fuel world.

### bio35 — Genetic Engineering [3.3]
1. **Genetic engineering** [3.3.1]: including earlier methods using plasmids or other vectors.
   The process is DNA isolation, cutting with restriction enzymes, ligation, and transformation
   and expression. Outline the concept and its applications.
   SimpleStudy: Genetic Engineering.
2. **DNA profiling** [3.3.2]: outline what it is and its potential uses.
3. **[HL] Generating a DNA profile** [3.3.3]: DNA extraction, the polymerase chain reaction (PCR)
   and gel electrophoresis; model the steps.
4. **[HL] DNA sequencing** [3.3.4]: sequencing data (nucleotide bases): generate a collection of
   DNA fragments, each one nucleotide shorter than the next, and separate them by gel
   electrophoresis; outline the principle.
5. **Bioinformatics: genome databases** [3.3.5]: the value of technology in analysing large
   quantities of genetic information to identify patterns and search for anomalies; use a
   genome database to search for alleles known to cause specific genetic diseases. Give a worked
   method with a real public database (e.g. NCBI, Ensembl or OMIM) and at least two diseases.
6. **Investigation: DNA-profile patterns** [3.3.6]: investigate patterns using a DNA profile;
   use primary or secondary data to support conclusions (e.g. paternity and forensic band
   matching).
   SimpleStudy: Experiments: DNA-profile patterns.
7. **Ethics of genetic technologies** [3.3.7]: genetic data access and use (agriculture, health,
   industry, reproduction, forensics, etc.); genetic modification; DNA testing; uses of stem
   cells (therapeutic, cloning). Discuss the ethical issues arising from advances in these
   technologies.

---

## Cross-course vocabulary

### bio-acronyms — Biology Acronyms and Key Terms [Appendix 1; all strands]
This chapter has no learning outcomes of its own. Use it for:
1. **Acronyms and key terms** drawn from the chapters above (e.g. ATP, NAD+, NADP+, ADH, FSH,
   LH, TSH, PCR, R0, Ds). Only include terms that appear in this outline.
2. **Action verbs** [Appendix 1]: the specification's glossary of the action verbs used in its
   outcomes, each with its meaning: analyse, apply, appreciate, classify, compare, conduct,
   consider, describe, design, discuss, distinguish, evaluate (data), evaluate (ethical
   judgement), examine, explain, explore, identify, illustrate, investigate, interpret,
   justify, measure, model, organise, outline, plan, pose, predict, produce, recognise,
   reflect, research, relate, review, use. Exam questions use these verbs, so students need
   their meanings.

---

## Appendix A — Where the specification differs from SimpleStudy and from the repo

**Coverage check.** The specification has **125 learning outcomes**: 12 in the Unifying Strand,
30 in Strand 1, 57 in Strand 2 and 26 in Strand 3. Every one appears in a subsection above.
19 outcomes are wholly in bold ([HL]) and 7 more are partly bold.

**In the specification but not in SimpleStudy's topic list.** The SimpleStudy taxonomy records
topic names only, so these are gaps at topic level; its lessons may cover more.
- Response in plants (anatomical and chemical adaptations) [2.4.1] has no SimpleStudy topic;
  it is placed in `bio21`.
- The genome-database search [3.3.5] is missing from SimpleStudy's experiments list.
- Modelling a habitat, and feeding and symbiotic relationships, are parts of the ecosystem
  investigation [3.1.11] that SimpleStudy's "qualitative ecosystem survey" doesn't name. The
  specification also requires a quantitative study of an abiotic factor.
- SimpleStudy lists "substance tests"; the specification names carbohydrates, protein and
  lipids [1.2.5], plus a separate quantitative reducing-sugar investigation [1.2.6].
- The glossary of action verbs [Appendix 1] has no SimpleStudy topic.

**In SimpleStudy but not a separate unit in the specification.**
- "Homeostasis" is a SimpleStudy unit. In the specification it sits inside 2.4 Response (the
  nervous-system outcomes) and the characteristics of life [1.1.1].
- SimpleStudy files viruses under "Classification of Life" and bacteria under
  "Microorganisms". The specification splits viruses across 1.1.2 (`bio6`) and 2.4.13 (`bio22`).

**Corrections to the repo's previous assumptions and content.**
- `pipeline/config.py` described the 2004 cutoff as "estimate — current syllabus ~2004". The
  2001 syllabus (introduced 2002, first examined 2004) is the *previous* course. The 2025
  specification is first examined in 2027. The cutoff stays 2004, now marked verified, because
  those are the only papers that exist; they are LEGACY practice, not on-course papers.
- Removed from the app as previous-syllabus content: a "seven characteristics of life" question
  (the specification lists eleven); the "Germination" note and the "germination" and "abscisic
  acid (dormancy)" flashcards (`bio24`); a germination test question (`bio24`) and a
  musculoskeletal-disorders test question (`bio18`), each replaced with a question from this
  specification; the "digestive enzymes in germinating seeds" past question (`bio13`); the
  "systole and diastole" past question (`bio29`, cardiac cycle not required); the
  continuous-culture part of the bioreactor question (`bio13`); and "Monera" in the
  bacterial-structure note (`bio33`).
- Remaining items for the notes writers to check against this outline, not removed because
  they are partly on-spec:
  - brain regions (cerebrum, cerebellum, medulla, hypothalamus, meninges) in `bio19`; the
    specification asks only for "parts of the central nervous system"
  - glucagon in `bio5` and in a `bio20` test question (the specification names insulin only)
  - plant tropisms in `bio5`
  - cytokinins, gibberellins, ethene and abscisic acid in the `bio24` growth-regulators note
    (the specification asks only for seeds' growth regulators stimulating fruit growth)
  - FADH2 and "~38 ATP" yields in `bio15`, which the specification doesn't require
  - the hormonal and nervous examples of negative feedback in `bio21` (thyroxine, temperature);
    keep them, as the specification requires negative feedback but names no example.
- The scaffold's sections `bio-sectionA/B/C` copy the previous paper's structure (A short
  questions, B experiments, C long questions). The specification doesn't set paper sections.

## Appendix B — Specification content with no exact home in an existing chapter

No new chapters are proposed. These items are placed in the nearest existing chapter:
- **Response in plants** [2.4.1]: `bio21` (Homeostasis), with the human systems for response.
  The alternative is a new chapter, "Response in Plants", which needs the user's approval.
- **Levels of organisation** [1.3.1]: `bio5`, because `bio7` covers cell structure only.
- **The Biology in Practice Investigation** [Assessment]: `bio2`.
- **The cross-cutting themes**: `bio3`, and named within each chapter's notes.
- **The glossary of action verbs** [Appendix 1]: `bio-acronyms`.
- **Outcomes split across two chapters**: 2.2.1, 2.2.4 and 2.2.5 between `bio14` and `bio15`;
  2.6.8 between `bio28` and `bio30`; virus content between `bio6` and `bio22`; DNA replication
  between `bio16` (2.3.3) and `bio17` (2.3.4).
