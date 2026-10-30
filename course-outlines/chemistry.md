# Leaving Cert Chemistry (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format,
  and a worked example). This outline says what to cover; that file says how to write it.
- **The specification:** the NCCA *Curriculum Specification for Leaving Certificate Chemistry*,
  "for introduction to schools in September 2025". Students who started fifth year in September
  2025 sit it for the first time in **June 2027**, so this is the document the app's students
  are examined on. The official PDF is `pipeline/resources/chemistry/spec-syllabus.pdf` (also
  `relevant-resources/syllabi/chemistry.pdf`), re-downloaded from curriculumonline.ie on
  2026-10-19 and identical to the repo copy. References in brackets, e.g. **[2.2.4]**, mean
  strand 2, unit 2.2, learning outcome 4. **[U2.3]** means the Unifying Strand, U2, outcome 3.
  **[1.2 LA]** means the "Students learn about" column of unit 1.2 (the left-hand column).
- **Do not use the previous syllabus** (the 1999 *Leaving Certificate Chemistry Syllabus*, first
  examined 2002 and last examined June 2026). It is a different course. Every past paper in the
  app (`chemistry-exam-questions.js`) was set on it. Parts on topics outside this specification
  were removed on 2026-10-19 (see Appendix A), but the remaining questions still follow the old
  paper layout. Never teach content because a past paper asked it. Not on this specification:
  radioactivity and nuclear equations, the mass spectrometer, instrumental analysis (AAS, IR,
  GC, HPLC), the ozone layer and CFCs, the nitrogen cycle, fuels and octane numbers (cracking,
  reforming, oxygenates), the bomb calorimeter, ethyne preparation from calcium carbide,
  Tollens' reagent, transition metals and variable valency, industrial chemistry case studies,
  metal extraction (blast furnace, aluminium, the Downs cell), alloys and anodising, X-ray
  crystallography and crystal types, water-analysis methods (EDTA hardness titration, Winkler
  dissolved oxygen, free chlorine by colorimeter, suspended and dissolved solids) and the stages
  of sewage treatment.
- **Chapters** are the app's 26 chemistry chapter IDs (`data.js`, `pipeline/scaffold/chemistry.json`).
  Past exam questions, test questions and flashcards are tagged to these IDs, so keep every ID
  exactly as written. The specification doesn't follow the chapter order. Each heading below
  lists the outcomes the chapter covers. Chapters chem1–chem13 are split in `data.js` into a
  chapter review (`<chapter>-1`, holding the old test questions) and one subsection per numbered
  item below (`<chapter>-s1`, `-s2`…), whose notes are in `content/chemistry/` and whose
  information packages are in `course-outlines/packages/chemistry/`. Chapters chem14–chem26 still
  use the specification's outcomes as their `data.js` entries.
- **What each subsection contains:**
  - **"Syllabus"** is what the specification says students learn about and should be able to
    do, close to its own wording. This is the required scope; every item must be covered.
  - **"Settings"** are the examples the specification itself names (e.g. "calcium carbonate and
    hydrochloric acid"). Use them; they are the examples an examiner expects. Where it says
    "including, but not limited to", the named examples are the minimum.
  - **"SimpleStudy"** names the matching topic in SimpleStudy's Higher Level course (taxonomy
    recorded 2026-08-07 in `pipeline/resources/chemistry/guide-simplestudy.md`). Use it for
    structure only; write all prose in your own words.
- **Higher vs Ordinary level:** Ordinary level studies "only the learning outcomes that are
  presented in normal type"; Higher level studies "all learning outcomes including those in bold
  type". Items in bold in the specification are marked **[HL]** here. Nothing else is Higher
  Level only. Many outcomes are partly bold; only the marked part is [HL]. Write [HL] content
  in full, as the app's students take Higher Level. Two bold items appear as brackets: "first 20
  (36) elements" means Ordinary level stops at element 20 and Higher level goes to 36 (krypton),
  in electron arrangements, periodic trends, bonding predictions and oxidation numbers.
- **Investigations.** The specification marks outcomes that are primarily an Experimental
  Investigation (EI) or a Research-based Investigation (RI). Write each EI as a full
  investigation: question or hypothesis, variables and controls, apparatus and reagents, safety
  and risk assessment, method, measurements, results and calculation, sources of error,
  conclusion. Write each RI as a research brief: the question, the kinds of source and how to
  evaluate them, the key chemistry, the evidence on each side, and a justified conclusion.
  - EI: conservation of mass [1.1.5] — `chem10`; ions in an unknown salt [2.1.5] — `chem5`; ΔH
    of neutralisation [3.1.3] — `chem21`; energy change of combustion [3.1.8] — `chem21`;
    factors affecting rate [3.2.3] — `chem17`; ethanoic acid in vinegar [4.1.5] — `chem12`;
    iron in iron tablets [4.1.6] — `chem15`.
  - RI: one major impact of hydrocarbons on society [2.4.2] — `chem23`; a role of
    electrochemistry in sustainability and technology [3.5.9] — `chem22`; organic compounds in
    pharmaceutical products [4.2.15] — `chem24`; a research investigation through a
    cross-cutting theme [4.3.8] — `chem20`.
  - Other practical work the outcomes require ("conduct", "investigate", "create", "measure"):
    flame tests and emission spectra [1.2.4] — `chem3`; Mr of a gas from a volatile liquid
    [1.4.4] — `chem8`; preparing solutions and primary standards [1.4.5] — `chem8`; separation
    techniques [1.1.3] — `chem9`; preparing ethene [2.4.3] — `chem23`; 3D models of
    hydrocarbons [2.4.7] — `chem23`; equilibrium shifts [3.3.5] — `chem18`; measuring pH [3.4.6]
    — `chem19`; displacement reactions [3.5.3] — `chem14`; galvanic and electrolytic cells
    [3.5.5–3.5.6] — `chem22`; titrations [4.1.2] — `chem12`, `chem15`; pH titration curves
    [4.1.3, HL] — `chem12`; aldehyde/ketone and carboxylic acid tests [4.2.4] — `chem25`; ester
    [4.2.8], benzoic acid [4.2.9] and soap [4.2.14] — `chem25`.
- **Where the specification sets a choice or an open example, cover every reasonable option,**
  so students can pick: one major impact of hydrocarbons [2.4.2] (climate change; air quality
  and health; plastic waste; economic and energy dependence); a role of electrochemistry
  [3.5.9] (rechargeable batteries and electric vehicles; hydrogen from electrolysis powered by
  renewables; fuel cells; corrosion protection); a cross-cutting research area [4.3.8] (give a
  worked example for each of health, sustainability and technology); "two general catalytic
  mechanisms" [3.2.5, HL] (intermediate formation and surface adsorption, the two the
  specification names); "suitable examples" of oxidation and reduction [3.5.1] (all four it
  lists).
- **The cross-cutting themes** are Health, Sustainability and Technology. The written exam
  includes questions on "application of chemistry to issues relating to the cross-cutting
  themes", so each chapter's notes should name the health, sustainability and technology links
  the specification makes.
- **Command words.** Appendix 1 of the specification is a glossary of action verbs (e.g.
  "appreciate", "evaluate", "justify", "model"). The verb in each outcome sets the depth the
  exam expects. Teach to that verb.
- **Assessment:**
  - Written examination: **60%**, at Higher and Ordinary level, set by the SEC. It uses "a range
    of question types" and assesses the four contextual strands and the unifying strand, plus
    the application of chemistry to the cross-cutting themes. Differentiation between levels
    comes through the stimulus material and the amount of structured support. The specification
    doesn't give the paper's sections or timing, and no sample paper is in the repo.
  - Additional assessment component, the **Chemistry in Practice Investigation: 40%**, at a
    common level, set and marked by the SEC. It is covered in `chem1`.
  - Grades are H1–H8 and O1–O8, in 10% bands from 30% to 100%.

---

## Unifying Strand — The Nature of Science [U1–U4]

All students. No bold outcomes. The written exam assesses this strand directly, and it is the
main content of the Chemistry in Practice Investigation. Its practices run through every
contextual strand.

### chem1 — The Nature of Science [U1.1–U4.2; additional assessment component]
1. **How scientists work and how ideas change** [U1.1]: how scientific ideas are modified over
   time; the nature and evolution of scientific knowledge; recognising bias.
   SimpleStudy: How Scientists Work.
2. **Models and their limits** [U1 LA]: the power of models for developing understanding and
   meaning, and the limitations of models.
   SimpleStudy: Models in Chemistry and Chemistry in Society.
3. **Science as a global enterprise** [U1 LA]: one that relies on evidence, clear communication,
   international conventions, peer review, repeatability and reproducibility.
   SimpleStudy: Scientific Ideas and Science as a Global Enterprise.
4. **Researching a scientific issue** [U1.2]: conduct research relevant to a scientific issue;
   evaluate different sources of information, including secondary data, understanding that a
   source may lack detail or show bias.
5. **Questions and hypotheses** [U2.1–U2.2]: recognise questions that are appropriate for
   scientific investigation in chemistry; pose testable hypotheses developed using scientific
   theories and explanations; evaluate and compare strategies for investigating hypotheses.
6. **Designing and conducting investigations** [U2.3; U2 LA]: design, plan and conduct
   investigations; explain how reliability, validity, accuracy, precision, error, fairness,
   safety, integrity and the selection of suitable equipment have been considered; safe
   laboratory practice and appropriate risk assessment.
7. **Measurement and error** [U2 LA]: SI units and conversion to and from commonly used units;
   potential sources of random and systematic error; the limits of the precision and accuracy
   of measurement.
8. **Producing and analysing data** [U2.4; U2 LA]: produce and select data, qualitatively and
   quantitatively; use trends in categories, tables, graphs and data to make predictions;
   manipulate mathematical representations of data and use scientific notation; critically
   analyse data to identify patterns and relationships; identify anomalous observations; draw
   and justify conclusions.
9. **Reflecting and recording** [U2.5; U2 LA]: review and reflect on the skills and thinking
   used in investigations; apply learning and skills to solving problems in unfamiliar
   contexts; record and analyse findings using appropriate methods, including a portfolio/log of
   experimental and research data.
10. **Communicating findings** [U2.6; U3 LA]: organise and communicate research and
    investigative findings using relevant scientific terminology and representations;
    communicate results to a range of audiences; justify opinions in evaluating other arguments,
    citing reliable sources.
11. **Chemistry in society** [U3.1–U3.2; U3 LA]: research and present information on the
    contribution scientists make to discovery and invention, and its impact on society;
    appreciate the role of chemistry in society, its personal, social and global importance,
    and how society influences scientific research; being more personally effective in
    addressing the impact of science and technology on society. The strand overview adds that
    applying chemistry to real-world issues can be influenced by economic, social,
    sustainability and ethical factors.
12. **Evaluating claims in the media** [U3.3; U3 LA]: how to discuss scientific claims; evaluate
    media-based arguments concerning science and technology.
13. **Abstraction to representation** [U4.1–U4.2; U4 LA]: relate observable phenomena to
    chemical processes at the atomic, sub-atomic or molecular level; visualisation as a key part
    of understanding core concepts; generating and using models; models are simplified
    representations of complex systems with underlying assumptions, can be modified as more data
    becomes available, and can predict the behaviour of a system; the evolving nature of models.
14. **The Chemistry in Practice Investigation (40%)** [Assessment]:
    - The SEC publishes an Investigation Brief each year in term two of Year 1. It sets out the
      requirements, includes stimulus material to set a context, lets students develop ideas
      they want to pursue, and lets them keep an investigative log.
    - Students carry out scientific research on an issue related to the brief (gather, process
      and evaluate information from secondary sources) and an experiment related to an issue
      within the brief (hypothesis, plan, design, laboratory work, primary data, analysis,
      conclusions).
    - They develop an evidence-based argument in response to the brief and submit a report in
      Year 2, in a format prescribed by the SEC. The specification envisages up to 20 hours of
      work. A separate document, *Guidelines to support the Chemistry in Practice
      Investigation*, covers organisation.
    - Descriptors of quality, at high, moderate and low achievement: knowledge and
      understanding; investigative skills (design and method); investigative skills (analysis
      and conclusions); relation to the work of scientists in society. Describe what high
      achievement looks like for each: e.g. a probing research question and testable hypothesis
      underpinned by chemical concepts; a thorough design that collects high-quality primary
      data; valid conclusions justified by the data; a thorough evaluation acknowledging
      limitations; a considered reflection locating the outcomes within broader societal and
      scientific issues.
    - Students should give an authentic account of how their work unfolded and how they might
      revise the process. The specification stresses learning from the process, not seeking a
      perfect answer.
    - SimpleStudy: Chemistry in Practice Investigation; Written Exam.

---

## Contextual strands — chapters in the app's order

The four contextual strands are Strand 1, Nature of Matter [1.1–1.4]; Strand 2, Behaviour of
Matter [2.1–2.4]; Strand 3, Interactions of Matter [3.1–3.5]; and Strand 4, Matter in our World
[4.1–4.3]. The app's chapters mix strands, so they appear here in chapter order; each heading
gives the outcomes it covers.

### chem2 — Atomic Structure: The Nuclear Model [1.2.1; 1.2 LA]
1. **Models of the atom** [1.2.1; 1.2 LA]: the nuclear, Bohr and orbital models of atomic
   structure; evaluate previous models of the atom against the current model. **[HL]**
   Consider, and state, the assumptions and limitations of each model. The strand overview
   says previous models "still have use", and the current model is "the best fit for the
   evidence available".
   SimpleStudy: Atomic Structure ("The Nuclear Model" lesson).
2. **Subatomic particles** [1.2 LA]: properties of the proton, neutron and electron (mass,
   charge, location).
3. **Atomic number, mass number, relative atomic mass and isotopes** [1.2 LA]: including a
   definition of the term isotope. The calculation of relative atomic mass from isotopic
   abundance is [1.4.2], in `chem8`.

### chem3 — Atomic Structure: The Bohr and Orbital Models [1.2.2–1.2.5]
1. **The current orbital model** [1.2.2]: describe the atom using the current orbital model of
   atomic theory, including subatomic particles.
   SimpleStudy: Atomic Structure.
2. **Energy levels and the hydrogen emission spectrum** [1.2.3; 1.2 LA] **[HL]**: electron
   transition, photon energy and frequency, ground state, excited states, Em − En = hf; describe
   and explain the origin of lines on the atomic emission spectrum of hydrogen.
3. **Identifying elements** [1.2.4; 1.2 LA]: identify an element using appropriate primary or
   secondary data, from flame tests and from line emission spectra.
   - Settings: flame tests (primary data) limited to salts of Na, K, Cu, Li, Ba and Sr; line
     emission spectra (primary or secondary data) limited to salts of Na, Sr and Cu.
   - SimpleStudy: Experiments and Investigations — flame tests.
4. **Electronic structure** [1.2.5; 1.2 LA]: describe the electronic structure of elements and
   associated ions, identifying stable electronic configurations; arrangements of electrons in
   main energy levels for the first 20 elements and their ions, excluding transition metal
   ions. **[HL]** Arrangements also in sublevels and in orbitals, for the first 36 elements;
   s, p and d sublevels; the shapes of s and p orbitals.

### chem4 — The Periodic Table: Arrangement of Electrons [1.3.1, 1.3.3]
1. **Development of the modern periodic table** [1.3.1; 1.3 LA]: the significance of the
   contribution of Mendeleev, with key refinements, to the development of the modern periodic
   table.
   SimpleStudy: The Periodic Table.
2. **Groups, periods and blocks** [1.3.3]: examine and explain the arrangement of elements in
   groups and periods in the periodic table. **[HL]** And in blocks.
3. **Using the table as a predictive guide** [1.3 LA]: the periodic table, and trends in it, as
   a guide to useful and predictive relationships. The trends themselves are in `chem7`.

### chem5 — Chemical Bonding and Structure [2.1.1, 2.1.3, 2.1.5, 2.2.5]
1. **Types of chemical bonding** [2.1.1; 2.1 LA]: describe and compare different types of
   chemical bonding; the nature of chemical bonds as lying on a continuum from ionic through
   polar covalent to pure covalent.
   SimpleStudy: Chemical Bonding and Structure.
2. **Modelling bonding and predicting formulae** [2.1.3; 2.1 LA]: model different types of
   bonding to predict chemical formulae; Lewis diagrams to represent bonds; bonding described
   in terms of orbital overlap; predicting how atoms bond using valence and the octet rule, for
   the first 20 elements. **[HL]** The orbital overlap in sigma and pi bonds, and delocalised
   bonding; the octet rule for the first 36 elements; outline the limitations in predicting
   bonding between atoms.
3. **Identifying ions in salts and solutions — EI** [2.1.5; 2.1 LA]: investigate, using primary
   data, the presence of ions in salts and in solutions, above certain minimum concentrations,
   and identify an anion and a cation in an unknown salt, using flame tests and reactions with
   reagents (equations required).
   - Settings: the specific anions, "linked to treatment, hardness and contamination of water":
     chlorides, nitrates, phosphates, sulfates, sulfites, carbonates, hydrogencarbonates.
     Cations by flame test (the six salts in `chem3` §3).
   - SimpleStudy: Experiments and Investigations — anion detection; flame tests.
4. **VSEPR theory** [2.2.5; 2.2 LA] **[HL]**: use VSEPR theory to predict and model the shapes of
   molecules of the form ABn with up to four pairs of electrons around a central atom, single
   bonds only, visualised using diagrams, 3D models and digital models.

### chem6 — Electronegativity and the Continuum of Chemical Bonding [2.1.2, 2.1.4, 2.2.1–2.2.4]
1. **Electronegativity and bond type** [2.1.2; 2.1 LA]: predict the nature of chemical bonds
   between atoms using trends in electronegativity values; explain those trends;
   electronegativity places a bond on the ionic–polar covalent–pure covalent continuum. Uses
   the Pauling scale, as in `chem7`.
   SimpleStudy: Electronegativity and the Continuum of Chemical Bonding.
2. **Bonding and properties** [2.1.4; 2.1 LA]: relate the properties of simple compounds to the
   nature of the bonding present: electrical conductivity, melting and boiling points,
   solubility in water, and state of matter at room temperature.
3. **Intramolecular bonding and intermolecular forces** [2.2.1; 2.2 LA]: distinguish between
   intramolecular bonding and a range of intermolecular forces, collectively under the
   umbrella of van der Waals forces: London dispersion forces; permanent dipole–dipole forces,
   including hydrogen bonding. **[HL]** Ion–dipole forces. Dipole moments are not required.
4. **Intermolecular forces and physical properties** [2.2.2; 2.2 LA]: relate observed physical
   properties (changes of state and solubility) for a range of compounds to the type of
   intermolecular forces, analysing appropriate secondary data. **[HL]** Account for trends.
   Settings: the range of compounds includes water and appropriate inorganic and organic
   compounds.
5. **Polarity and symmetry** [2.2.3; 2.2 LA] **[HL]**: explain qualitatively the influence of
   polarity and symmetry on intermolecular forces; how symmetry can give rise to non-polar
   compounds even where individual polar bonds exist in the molecule.
6. **Shape, polarity and properties** [2.2.4; 2.2 LA]: use the shapes and polarity of molecules
   of simple compounds to predict physical properties; how shape can determine overall
   polarity.

### chem7 — Families and Trends in the Periodic Table [1.3.2, 1.3.4, 1.3.5]
1. **Specific groups** [1.3.2; 1.3 LA]: identify specific groups of elements and relate group
   properties to position in the periodic table.
   - Settings: Groups 1, 2, 17 and 18 (state, conductivity and reactivity).
   - SimpleStudy: Families and Trends in the Periodic Table.
2. **Trends and relationships** [1.3.4; 1.3 LA]: examine trends and relationships in the
   periodic table, for the first 20 elements, in atomic number and relative atomic mass,
   electronic structure, electronegativity (Pauling scale), chemical reactivity (including the
   octet rule) and physical properties. **[HL]** Also atomic (covalent) radius, first
   ionisation energy and successive ionisation energies, for the first 36 elements.
3. **Ionisation energies and atomic radii** [1.3.5] **[HL]**: explain trends in first
   ionisation energies, including exceptions, and in successive ionisation energies and atomic
   radii.

### chem8 — The Mole: The Chemist's Counting Unit [1.4.1–1.4.6]
1. **The mole** [1.4.1; 1.4 LA]: define and explain the mole in terms of the Avogadro constant;
   relate the mole to how the amount of a substance can be quantified; the significance and
   scale of the mole; how the mole links number of particles, mass, relative atomic/molecular
   mass, volume (for gases) and moles; definitions of molar mass, relative molecular mass and
   density.
   SimpleStudy: The Mole.
2. **Relative atomic mass from isotopic abundance** [1.4.2]: solve problems involving relative
   atomic mass and percentage abundance of isotopes.
3. **Molar volume and Avogadro's law** [1.4.3; 1.4 LA]: state Avogadro's law and deduce the
   molar volume of a gas; the conditions for standard temperature (K) and pressure (STP).
4. **Relative molecular mass of a gas from a volatile liquid** [1.4.4]: conduct an experiment to
   determine the relative molecular mass of a gas derived from a liquid.
   SimpleStudy: Experiments and Investigations — relative molecular mass of a volatile liquid.
5. **Solutions and concentration** [1.4.5; 1.4 LA]: explain and model the concept of
   concentration; outline how to prepare a range of solutions of different concentrations,
   including primary standard solutions. Terms: solutions, solutes, solvents, dilution and
   serial dilutions, concentration, unsaturated, saturated and supersaturated solutions,
   standard solutions, solutions made from primary standards, taking into account precision,
   accuracy, volumes and glassware required.
   SimpleStudy: Experiments and Investigations — preparing sodium carbonate (standard
   solution).
6. **Units of concentration** [1.4.6; 1.4 LA]: convert between units of concentration: g/L,
   mol/L, %w/w, %v/v and %w/v. **[HL]** Also p.p.m.

### chem9 — Kinetic Theory of Matter and Behaviour of Gases [1.1.1–1.1.3, 2.3.1–2.3.2]
1. **The particulate nature of matter** [1.1 LA]: pure substances (elements, compounds) or
   mixtures of substances.
   SimpleStudy: Kinetic Theory of Matter and Behaviour of Gases.
2. **Evidence for the kinetic theory** [1.1.1; 1.1 LA]: understand experimental evidence for the
   kinetic theory of matter: Brownian motion and diffusion of gases (calculations not
   required).
3. **Using the kinetic theory** [1.1.2; 1.1 LA]: analyse the kinetic theory to explain the
   nature and behaviour of matter at the particulate level and to model how matter changes
   state: solid ↔ liquid, solid ↔ gas, liquid ↔ gas (qualitative analysis). **[HL]** Include
   the assumptions and limitations of the model.
4. **Separation techniques** [1.1.3; 1.1 LA]: justify the use of different separation
   techniques for isolating one or more components from a mixture; how they apply to
   homogeneous and heterogeneous mixtures within appropriate experimental activities. The
   specification names no particular techniques. Cover filtration, evaporation,
   crystallisation, simple and fractional distillation, chromatography and the use of a
   separating funnel. Benzoic acid crystallisation is in `chem25` and the ester separation in
   `chem25`.
5. **Gas relationships and the ideal gas** [2.3.1; 2.3 LA]: relationships between pressure,
   volume and temperature of gases; the model of an ideal gas, developed to analyse and predict
   how gases behave. **[HL]** Account for deviations of real gases from ideal gas behaviour.
6. **The ideal gas equation** [2.3.2; 2.3 LA]: solve and interpret quantitative problems using
   PV = nRT; how to verify and use the ideal gas equation. The van der Waals equation is not
   required.

### chem10 — Law of Conservation of Mass: Introducing Stoichiometry [1.1.4, 1.1.5, 1.4.7 (part)]
1. **Physical and chemical change** [1.1.4; 1.1 LA]: distinguish between physical and chemical
   change; chemical and physical properties.
   SimpleStudy: Law of Conservation of Mass: Introducing Stoichiometry.
2. **Conservation of mass and energy — EI** [1.1.5; 1.1 LA]: the laws of conservation of mass
   and of energy that underpin all physical and chemical changes; verify the law of
   conservation of mass using primary data and explain it through the use of models.
   SimpleStudy: Experiments and Investigations — conservation of mass.
3. **Empirical and molecular formulae** [1.4.7; 1.4 LA]: use the mole to determine empirical
   and molecular formulae; percentage composition.
4. **Balancing equations** [1.4.7; 1.4 LA]: balance equations for reactions where reactants and
   products are specified; balancing is underpinned by the law of conservation of mass.

### chem11 — Acids and Bases [3.4.1–3.4.4, 3.4.7]
1. **Categorising acids and bases** [3.4.1; 3.4 LA]: justify categorising commonly used
   substances as acid or base, based on the properties they display; common acid–base
   indicators; outline common everyday examples of neutralisation.
   - Settings: vinegar, citric juices, antacids, toothpaste; the use of lime in agriculture;
     remedies for acid indigestion.
   - SimpleStudy: Acids and Bases.
2. **Acid–base reactions** [3.4.2; 3.4 LA]: predict the products of, and write balanced
   equations for, acid–base reactions: acid–base neutralisation, acid–metal and
   acid–carbonate.
3. **Two theories** [3.4.3; 3.4 LA]: compare the Arrhenius and Brønsted–Lowry theories of
   acid–base systems, and justify why Brønsted–Lowry is a more extensive model for explaining
   behaviour.
4. **Applying Brønsted–Lowry theory** [3.4.4] **[HL]**: identify, in chemical equations,
   conjugate acid–base pairs and the species acting as acids and as bases.
5. **Strong vs weak, concentrated vs dilute** [3.4.7]: distinguish between weak and strong acids
   (and bases), and between concentrated and dilute acids (and bases).

### chem12 — Volumetric Analysis: Acid–Base [4.1.1–4.1.5]
1. **Primary standards and standard solutions** [4.1.1; 4.1 LA]: recognise the importance of
   primary standards and standard solutions for acid–base and redox volumetric analysis.
   Preparing them is in `chem8` §5.
   SimpleStudy: Volumetric Analysis — Acid-Base.
2. **Acid–base titrations** [4.1.2; 4.1 LA]: determine the concentration of analytes by
   titration, using primary standard solutions and/or solutions standardised using primary
   standards, with indicators.
   - Settings: strong acid–strong base; strong acid–weak base.
   - SimpleStudy: Experiments and Investigations — standardising hydrochloric acid and sodium
     hydroxide; ammonia concentration.
3. **pH titration curves** [4.1.3; 4.1 LA] **[HL]**: investigate pH titration curves using
   primary data from acid–base reactions, justifying the appropriate indicator for each
   titration; issues around generating curves for weak acid–weak base systems (limited to
   monoprotic, single-inflection-point curves).
4. **How indicators work** [4.1.4] **[HL]**: explain how weak acid and weak base acid–base
   indicators function, using Le Châtelier's principle.
5. **Ethanoic acid in vinegar — EI** [4.1.5]: investigate, using primary data, how to find the
   concentration of ethanoic acid in vinegar.
   SimpleStudy: Experiments and Investigations — vinegar concentration.

### chem13 — Acid–Base Volumetric Exam-Style Questions [4.1.7]
1. **Solving acid–base volumetric problems** [4.1.7; 4.1 LA]: solve volumetric problems for
   acid–base titrations in familiar contexts, using varied units (see the quantifying-matter
   section, `chem8`). **[HL]** Also in unfamiliar contexts.
   SimpleStudy: Volumetric Analysis — Acid-Base.
2. **Worked problem types** [4.1.7]: the specification lists no problem types. Suggested: one
   fully worked example each for a concentration in mol/L and g/L; back-calculating from a
   diluted sample (e.g. vinegar diluted ×10); a formula from titration data; and, for HL, a
   problem in an unfamiliar context.

### chem14 — Oxidation and Reduction [3.5.1–3.5.3]
1. **Oxidation and reduction** [3.5.1; 3.5 LA]: describe oxidation and reduction with examples
   emphasising electron transfer; identify oxidising and reducing agents in given reactions.
   **[HL]** Assign oxidation numbers, restricted to compounds of the first 36 elements.
   - Settings: corrosion and its prevention; combustion of fuels; respiration; iron in iron
     tablets.
   - SimpleStudy: Oxidation and Reduction.
2. **Balancing redox equations** [3.5.2] **[HL]**: apply oxidation numbers to balance redox
   reaction equations.
3. **The electrochemical series and displacement** [3.5.3; 3.5 LA]: the electrochemical series
   as a guide to the relative tendency of metals to be oxidised; investigate displacement
   reactions of metals, using primary or secondary data, relating them to the series.

### chem15 — Volumetric Analysis: Oxidation-Reduction [4.1.2, 4.1.6]
1. **Redox titrations** [4.1.2; 4.1 LA]: determine the concentration of analytes by redox
   titration, using primary standard solutions and/or solutions standardised using primary
   standards; use the appropriate indicator, or the self-indicating colour change.
   - Settings: iodine–thiosulfate; iron(II).
   - SimpleStudy: Volumetric Analysis — Oxidation-Reduction; Experiments and Investigations —
     standardising potassium permanganate and sodium thiosulfate.
2. **Iron in iron tablets — EI** [4.1.6]: investigate, using primary data, the percentage of
   elemental iron in iron tablets.
   SimpleStudy: Experiments and Investigations — iron in a tablet.

### chem16 — Oxidation–Reduction Volumetric Exam-Style Questions [4.1.7]
1. **Solving redox volumetric problems** [4.1.7; 4.1 LA]: solve volumetric problems for redox
   titrations in familiar contexts, using the mole ratio from the balanced redox equation and
   varied units. **[HL]** Also in unfamiliar contexts.
   SimpleStudy: Volumetric Analysis — Oxidation-Reduction.
2. **Worked problem types** [4.1.7]: the specification lists no problem types. Suggested: one
   fully worked example each for permanganate–iron(II) (percentage iron in a tablet) and
   iodine–thiosulfate, and, for HL, a problem in an unfamiliar context.

### chem17 — Rates of Reaction [3.2.1–3.2.5]
1. **Rate of reaction** [3.2.1; 3.2 LA]: define and explain rate of reaction.
   SimpleStudy: Rates of Reactions.
2. **Collision theory** [3.2.2; 3.2 LA]: describe collision theory; give examples of slow and
   fast reactions; the factors that collision theory explains: concentration, surface area,
   temperature, the presence of a catalyst, and (for gaseous reactions) pressure. **[HL]**
   Limitations: concentration may not always affect the rate, catalysts can become saturated or
   poisoned, and collisions need to be oriented correctly.
3. **Investigating rates — EI** [3.2.3; 3.2 LA]: investigate, using primary data, the factors
   that affect rate, and interpret rate-of-reaction graphs from primary and secondary data;
   measuring initial and average rates. **[HL]** Also instantaneous rates.
   - Settings (including, but not limited to): calcium carbonate and hydrochloric acid; sodium
     thiosulfate and hydrochloric acid; decomposition of hydrogen peroxide.
   - SimpleStudy: Experiments and Investigations — hydrogen peroxide decomposition; surface
     area, concentration and temperature.
4. **Catalysis and energy profiles** [3.2.4; 3.2 LA]: catalysed and uncatalysed reactions,
   including an enzyme as a biological catalyst; compare the energy profile diagrams of
   catalysed and uncatalysed reactions, for both exothermic and endothermic reactions.
5. **Catalytic mechanisms** [3.2.5; 3.2 LA] **[HL]**: model two general catalytic mechanisms:
   surface adsorption and the formation of intermediates.

### chem18 — Chemical Equilibrium [3.3.1–3.3.5]
1. **Dynamic equilibrium** [3.3.1; 3.3 LA]: appreciate that some reactions tend to be
   reversible; explain dynamic chemical equilibrium: concentrations of reactants and products
   constant (closed system); forward and reverse rates equal; equilibrium can be reached from
   either direction.
   SimpleStudy: Chemical Equilibrium.
2. **The equilibrium constant** [3.3.2; 3.3 LA]: Kc and its mathematical representation: for
   aA + bB ⇌ cC + dD, Kc = [C]^c[D]^d / [A]^a[B]^b; explain the factors that affect the value of
   Kc. **[HL]** Use the mathematical model of Kc to describe and predict how given reactions
   would proceed.
3. **Kc calculations** [3.3.3; 3.3 LA] **[HL]**: solve problems with Kc: calculate Kc from
   equilibrium concentrations; calculate equilibrium concentrations from the value of Kc.
4. **Le Châtelier's principle** [3.3.4; 3.3 LA]: apply it to a variety of processes to predict
   the response to a disturbance; changes in temperature, concentration and pressure (but not
   the use of a catalyst) can disturb dynamic equilibrium. **[HL]** Predict conditions for
   optimising the yield of product.
5. **Investigating equilibrium** [3.3.5; 3.3 LA]: investigate, using primary and/or secondary
   data, how changes in temperature and concentration affect the state of equilibrium.
   - Settings (including, but not limited to): iron(III) chloride–potassium thiocyanate;
     digital simulations.
   - SimpleStudy: Experiments and Investigations — equilibrium changes.

### chem19 — pH and Indicators [3.4.5, 3.4.6, 3.4.8–3.4.10]
1. **Self-ionisation of water** [3.4.5; 3.4 LA]: explain the self-ionisation of water.
   **[HL]** The ionic product of water, Kw = [H₃O⁺][OH⁻] = [H⁺][OH⁻] (simplified); deduce this
   representation and account for its temperature dependence.
   SimpleStudy: pH and Indicators.
2. **pH and its measurement** [3.4.6; 3.4 LA]: measure pH using indicators and/or meters or
   sensors; explain the pH scale; pH = −log₁₀[H⁺]. **[HL]** The factors that affect the pH of a
   solution: pH as a function of the tendency to dissociate, including concentration and
   temperature.
3. **pH calculations** [3.4.8; 3.4 LA] **[HL]**: solve problems involving pH for dilute aqueous
   solutions of strong acids and bases, and of weak acids and bases using the appropriate Ka
   and Kb values. Mixtures are not required.
4. **Dissociation constants** [3.4.9; 3.4 LA] **[HL]**: the dissociation of acids (HA) and bases
   (BOH); deduce the mathematical representations of the weak acid dissociation constant (Ka)
   and the weak base dissociation constant (Kb).
5. **Degree of dissociation** [3.4.10]: compare the degrees of dissociation of strong and weak
   acids, and of strong and weak bases. **[HL]** Use Ka and Kb values.

### chem20 — Environmental Chemistry [4.3.1–4.3.5, 4.3.8]
1. **The natural greenhouse effect** [4.3.1; 4.3 LA]: describe it and explain its significance;
   the significance of the carbon cycle for natural and human-influenced climate change and for
   sustainability.
   SimpleStudy: Environmental Chemistry.
2. **The enhanced greenhouse effect** [4.3.2; 4.3 LA]: discuss the evidence for it and possible
   solutions to anthropogenic influences on the atmosphere; greenhouse gases have different
   sources, abundances and greenhouse factors (global warming potentials).
   - Settings (including, but not limited to): methane, carbon dioxide, NOx, sulfur oxides,
     water vapour; effects: global warming, precipitation, ocean acidification.
3. **Water contamination** [4.3.3; 4.3 LA]: discuss the causes of water contamination and its
   biochemical consequences; water as a finite resource whose processing has an energy and
   environmental impact.
   - Settings: sewage, industrial and agricultural effluent, microplastics, heavy metals,
     acidification; consequences including, but not limited to, eutrophication and increased
     BOD.
4. **Treating drinking water** [4.3.4; 4.3 LA]: describe the steps in treating drinking water;
   appreciate the impact of providing clean water for human use.
   Settings: sedimentation, flocculation, filtration (sand and micro), chlorination,
   fluoridation, pH adjustment, UV treatment.
5. **The lithium-ion cell** [4.3.5; 4.3 LA]: describe how a simple lithium-ion cell works: a
   galvanic cell when discharging and an electrolytic cell when recharging; discuss its
   life-cycle: mining, usage and applications, disposal and recycling. Link to `chem22`.
6. **Researching chemistry — RI** [4.3.8; 4.3 LA]: research an area of the course through one of
   the cross-cutting themes (health, sustainability, technology); chemistry as a collaborative,
   human endeavour whose social and global importance can be appreciated through personal
   research. Give one worked research outline per theme.

### chem21 — Thermochemistry [3.1.1–3.1.8]
1. **Bond enthalpy and energy change** [3.1.1; 3.1 LA]: the law of conservation of energy
   underpins all thermochemical processes; define bond enthalpy; explain enthalpy changes as
   bond-breaking (requires energy) and bond-making (releases energy); physical change also
   involves enthalpy change.
   - Settings (including, but not limited to): combustion, neutralisation, thermal
     decomposition, rusting of iron, photosynthesis, respiration.
   - SimpleStudy: Thermochemistry.
2. **Exothermic and endothermic** [3.1.2]: explain, and model diagrammatically, energy transfer
   in exothermic and endothermic reactions.
3. **ΔH of neutralisation — EI** [3.1.3; 3.1 LA]: ΔH as the heat change at constant pressure;
   investigate, using primary data, how to determine ΔH for a suitable neutralisation.
   SimpleStudy: Experiments and Investigations — heats of neutralisation.
4. **Calculating ΔH and energy profiles** [3.1.4; 3.1 LA]: calculate ΔH for a reaction by
   measurement; enthalpy changes are relative to standard conditions of temperature and
   pressure; describe the energy transfer with a simple energy profile diagram.
5. **ΔH from bond enthalpies** [3.1.5; 3.1 LA] **[HL]**: analyse a reaction involving covalent
   molecules to explain and predict ΔH using average bond enthalpy values.
6. **Hess's law** [3.1.6; 3.1 LA] **[HL]**: calculate and predict enthalpy changes using Hess's
   law, including from standard heats of formation of reactants and products; model Hess's law
   diagrammatically as a series of reactions and energy cycles.
7. **Combustion** [3.1.7; 3.1 LA]: construct balanced equations for the complete combustion of
   hydrocarbons with no more than one double or triple bond, and of primary alcohols up to C6.
   **[HL]** Explain trends in the associated standard ΔH values.
8. **Energy change of combustion — EI** [3.1.8; 3.1 LA]: investigate, using primary data, the
   energy change of combustion and compare experimental values with standard values,
   accounting for differences.
   - Settings: the heat of combustion of a series of alcohols, estimated using spirit burners.
   - SimpleStudy: Experiments and Investigations — heats of combustion.

### chem22 — Electrochemistry [3.5.4–3.5.9]
1. **Primary and secondary cells** [3.5.4; 3.5 LA]: compare a primary and a secondary cell, with
   examples; the function of the cathode, anode and electrolyte.
   SimpleStudy: Electrochemistry.
2. **The galvanic cell** [3.5.5; 3.5 LA]: create a simple galvanic cell and explain its
   operation: how redox reactions produce a flow of electrons.
   - Settings: including, but not limited to, the copper–zinc system.
   - SimpleStudy: Experiments and Investigations — galvanic cells.
3. **The electrolytic cell** [3.5.6; 3.5 LA]: create a simple electrolytic cell and explain its
   operation; how an external electrical source drives redox reactions; split water using
   electrolysis. **[HL]** The reactions at the electrodes.
   - Settings: electrolysis of acidified water and of salt solutions, including copper(II)
     chloride and potassium iodide, using inert electrodes.
   - SimpleStudy: Experiments and Investigations — inert-electrode electrolysis.
4. **Chemical cells and fuel cells** [3.5.7; 3.5 LA]: compare a chemical cell (converts the
   chemical energy of its reactants to electrical energy until they are used up) with a fuel
   cell (needs a constant supply of external reactants, with products continuously removed).
5. **The hydrogen fuel cell** [3.5.8; 3.5 LA]: explain the operation of a simple hydrogen fuel
   cell: a galvanic cell that converts the chemical energy of a fuel and an oxidising agent
   through a redox reaction.
6. **Electrochemistry and sustainability — RI** [3.5.9; 3.5 LA]: research a role of
   electrochemistry in an area related to sustainability and technology in everyday life; more
   sustainable uses of energy, such as electrochemical cells and rechargeable batteries;
   electrolysis and its potential for producing hydrogen fuel using electricity from
   sustainable sources. The lithium-ion cell [4.3.5] is in `chem20`.

### chem23 — Allotropes of Carbon. Hydrocarbons [2.4.1–2.4.9, 4.3.6–4.3.7]
1. **Hydrocarbons, sources and uses** [2.4.1; 2.4 LA]: organic compounds divide into many
   groups, with hydrocarbons (C and H only) the simplest; outline the main sources of
   hydrocarbons (fossil fuels, living matter, synthesis) and their uses in industry and
   society.
   SimpleStudy: Allotropes of Carbon and Hydrocarbons.
2. **Impact of hydrocarbons — RI** [2.4.2; 2.4 LA]: identify and research one major impact on
   society of the continued, extensive use of hydrocarbons. Cover every option listed under
   "Read this first".
3. **Preparing ethene** [2.4.3; 2.4 LA]: conduct an experiment to prepare ethene from ethanol,
   observe its physical properties and investigate some chemical properties: combustion, and
   tests for unsaturation with bromine water and acidified potassium manganate(VII).
   SimpleStudy: Experiments and Investigations — ethene.
4. **Groups of hydrocarbons** [2.4.4; 2.4 LA]: describe and compare aliphatic (alkanes,
   alkenes, alkynes) and aromatic hydrocarbons (exemplified by benzene) by composition,
   bonding and structure, relating these to characteristic properties; IUPAC naming up to C6.
5. **Explaining and predicting properties** [2.4.5; 2.4 LA]: explain and predict differences
   in properties within: straight-chain alkanes of different carbon number; alkanes of the same
   carbon number; mono-unsaturated straight-chain alkenes. The properties are state, boiling
   point, combustion, solubility in water and non-polar solvents, and reactivity (aliphatics
   only), explained through the carbon–carbon bonds, intermolecular forces and relative
   molecular mass. Predict the behaviour of alkanes and alkenes up to C6.
6. **Stability of alkanes** [2.4.6; 2.4 LA]: explain the relative chemical stability of alkanes,
   including their low polarity. **[HL]** And sigma bonding.
7. **3D models and formulae** [2.4.7; 2.4 LA]: construct and examine 3D models of hydrocarbons;
   explain how bonding and isomers influence the spatial arrangement of atoms; relate models to
   condensed and expanded molecular formulae; structural isomers of alkanes and alkenes up to
   C6.
8. **Shapes in terms of sigma and pi bonds** [2.4.8]: explain and compare the shapes of ethane,
   ethene and ethyne. **[HL]** And benzene, in terms of sigma and pi bonds, including
   delocalised pi bonding.
9. **Structural and geometric isomerism** [2.4.9; 2.4 LA] **[HL]**: distinguish between
   structural and geometric isomerism, including how isomerism gives rise to different
   properties; cis–trans isomers exemplified by butene.
10. **Allotropes of carbon** [4.3.6; 4.3 LA]: compare the properties and structures of the
    allotropes of carbon: diamond, graphite, graphene and fullerene.
11. **Uses of carbon allotropes** [4.3.7; 4.3 LA]: discuss their use in society: nanotechnology,
    electrochemistry, electronics and common commercial products.

### chem24 — More Families of Organic Compounds [4.2.1–4.2.3, 4.2.5, 4.2.12, 4.2.15]
1. **Sources and impact of organic products** [4.2.1; 4.2 LA]: outline sources of organic
   compounds and the use and impact of products based on them.
   - Settings: fuels, pharmaceuticals, plastics, pesticides, synthetics.
   - SimpleStudy: More Families of Organic Compounds.
2. **Functional groups and nomenclature** [4.2.2; 4.2 LA]: reactivity is characterised by
   other atoms or groups bound to the hydrocarbon; apply IUPAC rules (up to C6) and classify each
   functional group by general formula and structure: alkanes (including cyclohexane), alkenes,
   alkynes, aromatics (limited to benzene), alcohols (primary, secondary, tertiary),
   haloalkanes, monocarboxylic acids, esters (from monocarboxylic acids and primary alcohols
   only), aldehydes and ketones.
3. **Representing organic molecules** [4.2.3; 4.2 LA]: construct and compare molecular formulae,
   condensed structural formulae, expanded structures and 3D physical models (tetrahedral and
   planar geometry around carbon); use R to represent part of a molecule; comparisons involving
   structural isomerism.
4. **Physical properties** [4.2.5; 4.2 LA] **[HL]**: relate the solubility, melting point and
   boiling point of organic molecules to molecular size and the type of bonding present.
5. **Acidity of carboxylic acids and alcohols** [4.2.12; 4.2 LA] **[HL]**: explain the acidity
   of carboxylic acid and alcohol functional groups: inductive effects in carboxylic acids,
   resonance of the carboxylate ion, polarity in the alcohol structure.
6. **Pharmaceuticals — RI** [4.2.15; 4.2 LA]: explore the use of organic compounds in
   pharmaceutical products; organic compounds in natural products for medicinal or narcotic
   use; most modern pharmaceuticals are large, complex organic molecules with multiple
   functional groups made from simpler organic precursors.
   Settings (including, but not limited to): willow bark, cinchona bark, opium poppy; aspirin,
   penicillin, taxol, opiates.

### chem25 — Reactions of Organic Compounds [4.2.4, 4.2.6–4.2.11, 4.2.13, 4.2.14, 4.2.16]
1. **Identifying tests** [4.2.4; 4.2 LA]: conduct tests to distinguish aldehydes from ketones
   (Fehling's test) and to show the acidic nature of carboxylic acids. In "Fehling's oxidising
   test" the word "oxidising" is bold, so **[HL]** explain the test as Fehling's reagent
   oxidising the aldehyde. Tollens' reagent is not on the specification.
   - Settings: reactions of carboxylic acids with suitable metals (e.g. magnesium) and suitable
     bases (e.g. NaOH and sodium carbonate).
   - SimpleStudy: Reactions of Organic Compounds; Experiments and Investigations —
     aldehyde/ketone distinction.
2. **Five reaction types** [4.2.6; 4.2 LA]: describe addition, substitution, redox, acid–base
   and elimination reactions. Conditions (temperature, solvent, catalyst, pressure) are not
   required unless specified. **[HL]** Analyse a given reaction in terms of the type(s) of
   reaction taking place.
3. **Reaction schemes** [4.2.7; 4.2 LA]: analyse an organic reaction scheme to describe the
   relationships between compounds and to predict possible reactions and products. **[HL]**
   Predict reactions and explain behaviour (changes in geometry; why some reactions are not
   possible).
4. **Preparing an ester** [4.2.8; 4.2 LA]: conduct an experiment to prepare an ester using a
   reflux method.
   SimpleStudy: Experiments and Investigations — ester.
5. **Synthesising benzoic acid** [4.2.9; 4.2 LA]: synthesise benzoic acid by oxidation of
   phenylmethanol using KMnO₄ under basic conditions, including crystallisation; determine
   purity, melting point and yield.
   SimpleStudy: Experiments and Investigations — benzoic acid.
6. **Reaction mechanisms** [4.2.10; 4.2 LA] **[HL]**: describe reaction mechanisms involving the
   movement of electrons, including supporting evidence; use curved arrows or fishhooks for
   ionic addition of chlorine and of hydrogen chloride to ethene, and for free-radical
   substitution of methane and ethane with chlorine.
7. **Redox and acid–base reactions of organic compounds** [4.2.11; 4.2 LA] **[HL]**: redox
   reactions of alcohols, aldehydes, carboxylic acids and ketones; acid–base reactions involving
   base hydrolysis of esters, including tri-esters in fats and oils.
   Settings: the redox reagents that convert between functional groups: hydrogen with a nickel
   catalyst as reducing agent; Fehling's solution; potassium permanganate in acidic and basic
   conditions.
8. **Surfactants and soap** [4.2.13; 4.2 LA]: outline how a soap works as an example of a
   surfactant; applications of surfactants in everyday life; how surfactants have contributed to
   the health and sanitisation of society.
9. **Preparing soap** [4.2.14; 4.2 LA]: conduct a simple activity using household reactants to
   make soap on a small scale, with NaOH either limiting or in excess (reflux not required).
   **[HL]** The consequences of having limiting or excess NaOH for the manufacture of soap.
   SimpleStudy: Experiments and Investigations — soap.
10. **Addition polymers** [4.2.16; 4.2 LA]: define polymer; describe the structure and
    applications of addition polymers. **[HL]** How non-biodegradability is related to their
    chemical stability.
    - Settings: poly(ethene), poly(chloroethene) and poly(phenylethene); applications including
      fuels, food production and household products.

### chem26 — Stoichiometry: Limiting Reactants and Percentage Yield [1.4.7 (part)]
1. **Quantitative problems from balanced equations** [1.4.7; 1.4 LA]: use the mole to analyse
   and solve quantitative problems based on balanced equations: masses, volumes of gases, simple
   unit analysis, gravimetric analysis.
   SimpleStudy: Limiting Reactants and Percentage Yield.
2. **Yield** [1.4.7; 1.4 LA]: theoretical, actual and percentage yields.
3. **Limiting reagents** [1.4.7; 1.4 LA] **[HL]**: limiting reagents and reagents in excess.

---

## Appendix A — Where the specification differs from SimpleStudy and from the repo

- **SimpleStudy follows this specification.** Its 15 units and 54 topics (recorded 2026-08-07)
  match the app's chapter titles, which were taken from it. The recorded taxonomy goes only to
  topic level, so differences can be checked only at that level:
  - **In the specification but not named in SimpleStudy's topics or experiment list:** the four
    research investigations [2.4.2, 3.5.9, 4.2.15, 4.3.8]; displacement reactions and the
    electrochemical series [3.5.3]; pH titration curves [4.1.3, HL]; the lithium-ion cell and
    its life-cycle [4.3.5]; graphene and fullerene [4.3.6–4.3.7]; reaction mechanisms [4.2.10,
    HL]; surfactants [4.2.13]; addition polymers [4.2.16]; pharmaceuticals [4.2.15]; water
    treatment and contamination [4.3.3–4.3.4]; the categorisation of everyday acids and bases
    [3.4.1].
  - **In SimpleStudy but not named in the specification:** "concentration decrease" (read it as
    dilution and serial dilution [1.4.5]); standardising potassium permanganate and sodium
    thiosulfate (allowed, as the specification requires "solutions standardised using primary
    standards" [4.1.2], but it names only the five titrations in `chem12` and `chem15`).
- **Corrections to the repo:**
  - `data.js` had the acid–base outcome codes shifted by one: spec 3.4.1 (categorising everyday
    acids and bases) was missing and every later 3.4 code was one too low. The codes are now
    3.4.2–3.4.4 and 3.4.7 in `chem11` and 3.4.5, 3.4.6 and 3.4.8–3.4.10 in `chem19`. Outcome IDs
    are unchanged.
  - `pipeline/scaffold/chemistry.json` describes Section A (mandatory experiments) and Section B
    (theory). That is the old paper's layout, and it is still right for tagging the legacy
    papers. The 2027 written paper's structure isn't in the specification. Don't write notes
    around "Section A experiments".
  - `pipeline/config.py` recorded the chemistry cutoff as an unverified 2002. It is now marked
    verified: the previous syllabus (NCCA, © 1999) was first examined in 2002 and last examined
    in June 2026. Those papers are LEGACY practice; the bundle's firstExamYear 2027 takes over
    once June 2027 has passed.
- **Wrong-course content removed from the app on 2026-10-19:**
  - `chemistry-exam-questions.js`: 422 question parts on topics outside this specification
    (radioactivity, mass spectrometry, instrumental analysis, ozone and CFCs, the nitrogen
    cycle, fuels and octane numbers, the bomb calorimeter, ethyne from calcium carbide,
    industrial chemistry, metal extraction, alloys and anodising, crystals and X-ray
    crystallography, water-analysis methods, sewage treatment, transition metals). 14
    questions with no parts left were removed. 617 questions and 3,701 parts remain.
  - `chemistry-content.js`: the transition-metal notes, flashcards and questions; the mass
    spectrometer flashcard, question and uses; Tollens' reagent from the aldehyde/ketone notes
    and question. `chemistry-test-questions.js`: Tollens' reagent from one model answer.
  - Not changed: the 2001 papers (51 questions) predate even the previous syllabus (it was
    first examined in 2002). Their remaining parts were checked by topic like the others but are
    still in the app.

## Appendix B — Specification content with no exact home in an existing chapter

No new chapter is needed; every outcome has a home. These placements need a decision or a
cross-reference:

- **3.4.1 (categorising everyday acids and bases)** had no learning-outcome entry in `data.js`;
  since chem11 was split into subsections (2026-10-30) it is `chem11-s1`.
- **4.1.2 (determining concentration by titration)** covers both acid–base and redox
  titrations, but `data.js` attaches it only to `chem15`. The acid–base side is written in
  `chem12` §2.
- **4.1.7 (solve volumetric problems)** is attached to both `chem13` (acid–base) and `chem16`
  (redox); each chapter covers its own titration type.
- **1.4.7 (use the mole)** is split between `chem10` (formulae and balancing) and `chem26`
  (quantitative problems, yield, limiting reagents).
- **4.3.5 (lithium-ion cell)** sits in `chem20` (environmental) but is electrochemistry.
  Cross-reference it from `chem22`.
- **4.3.6–4.3.7 (carbon allotropes)** sit in `chem23` with the hydrocarbons.
- **The 1.2 "learn about" items on subatomic particles, isotopes and atomic number** have no
  outcome of their own; they are placed in `chem2`.
- **Separation techniques [1.1.3]** name no specific techniques; `chem9` §4 lists the standard
  ones.
- **The Chemistry in Practice Investigation** (assessment, not an outcome) is in `chem1` §14.

## Count

26 chapters; 137 subsections. All 124 learning outcomes in the specification are placed (13 in
the Unifying Strand; 22, 21, 37 and 31 in Strands 1–4), together with every "Students learn
about" item.
