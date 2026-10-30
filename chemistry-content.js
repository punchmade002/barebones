// Chemistry HL Content — notes, concept points and flashcards for all chapters.
// Past-paper exam questions live in exam-questions-db.js.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  function ch(id) { return COURSE_DATA.chapters.find(function (c) { return c.id === id; }); }

  // ── Chapter review questions ──
  // Every chapter is split into outline subsections whose notes and flashcards come from
  // content/chemistry/ (chemistry-notes.js). Their earlier test questions are kept here, on
  // each chapter's review outcome (<chapter>-1).
  (function () {
    var REVIEW_QUESTIONS = {
     "chem1": [
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between a scientific theory and a scientific law.",
       "model": "A scientific theory is a hypothesis verified by many experiments and widely accepted as the correct explanation for a phenomenon; it explains why/how something occurs and is provisional. A scientific law is a statement deduced from empirical evidence that describes what always happens under certain conditions; it does not explain why. Laws change little once established; theories are always refined as new evidence emerges."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "List the steps of the scientific method in the correct order.",
       "model": "1. Observation 2. Question 3. Research 4. Hypothesis 5. Prediction 6. Experiment 7. Data Analysis 8. Conclusion 9. Accept or Reject Hypothesis (form new hypothesis if rejected) 10. Report Results."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain why peer review is an important part of science.",
       "model": "Peer review requires that research is evaluated by independent experts in the same field before publication. It checks that methods are sound, data is correctly interpreted and conclusions are supported by evidence. This process helps to catch errors and fraud, and ensures only reliable and valid findings are published and built upon by the wider scientific community."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Name and explain each letter of the CARDS framework for evaluating sources.",
       "model": "C — Credibility: Is the source trustworthy and from a reputable organisation or journal with expert authors? A — Accuracy: Are the claims backed by reliable, consistent evidence free from errors? R — Relevance: Is the information directly related to your research question? D — Date: Is it recently published? Science evolves rapidly so older sources may be outdated. S — Sources: Are references and citations provided to back up the claims made?"
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Which of the following is scientifically investigable: 'Is plastic bad?' or 'How does temperature affect the tensile strength of this polymer?' Justify your choice.",
       "model": "The second question is investigable because temperature can be varied, tensile strength can be measured quantitatively and other variables can be controlled. 'Is plastic bad?' is value-laden and too broad: plastic type, meaning of harm, affected system and measurable outcome are unspecified."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Rewrite the claim 'natural acids are safer than synthetic acids' as a focused question suitable for chemical investigation.",
       "model": "A suitable question is: 'At equal molar concentration, how do the pH and skin-corrosion proxy of ethanoic acid and hydrochloric acid compare under the same conditions?' It specifies substances, concentration, measurable outcomes and controls. Safety still requires an approved laboratory method rather than testing on skin."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Form a testable hypothesis for the effect of concentration on reaction rate and outline a strategy that could test it.",
       "model": "Hypothesis: increasing reactant concentration increases initial rate because more particles per unit volume produce more frequent effective collisions. React equal volumes at several known concentrations, measure gas volume or mass change against time, keep temperature and other reactant amounts constant, repeat trials and compare initial gradients."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Compare two strategies for investigating how surface area affects reaction rate and identify which would give stronger evidence.",
       "model": "One strategy times disappearance of equal masses of different-sized solid; another records gas volume continuously with a gas syringe. Continuous gas data gives a rate curve and reduces subjective endpoint judgement, but both need equal moles, temperature and concentration. Precisely measured particle-size ranges strengthen validity."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between repeatability and reproducibility of an experiment.",
       "model": "Repeatability: the same scientist repeats the experiment in the same conditions and location and gets the same or very similar result. Reproducibility: other independent scientists reproduce the entire experiment and obtain the same results as the original scientists. Both are required for the scientific community to trust a result."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "A graph contains one anomalous result but otherwise shows a linear trend. Explain how the data should be analysed and how a conclusion should be justified.",
       "model": "Check units, transcription, apparatus and procedure, repeat the anomalous condition and retain the original value transparently. Use repeats, means, spread and an appropriate best-fit line rather than forcing the line through every point. State the supported relationship, its range and uncertainty without claiming more precision than the data allow."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Distinguish qualitative from quantitative chemical data and explain why a strong conclusion may require both.",
       "model": "Qualitative data describe observations such as colour change, precipitate or gas, whereas quantitative data use measurements such as mass, pH, temperature or volume. Measurements allow comparison and uncertainty analysis; observations help identify the chemical event and unexpected products. Agreement between both can strengthen interpretation."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "An investigation produced inconsistent titres. Evaluate the method and propose a justified improvement sequence.",
       "model": "Inspect technique before discarding results: condition the pipette and burette, remove the funnel and air bubble, read the meniscus at eye level, swirl continuously and approach the endpoint dropwise. Carry out a rough titre, then repeat until concordant values are obtained. Use only concordant titres for the mean and report remaining uncertainty."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain how skills learned in an acid-base titration could be applied to an unfamiliar redox titration.",
       "model": "Transfer accurate volumetric technique, rinsing, meniscus reading, repeat-to-concordance and stoichiometric calculation. Then identify the new balanced redox equation, indicator or self-indicating endpoint and relevant safety controls. The general measurement strategy transfers, but chemical assumptions and endpoint conditions must be re-evaluated."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Outline how experimental findings should be communicated so another chemist can evaluate and reproduce the work.",
       "model": "State the question and hypothesis, list materials with quantities, give a replicable method and safety controls, and identify variables. Present raw and processed data with units, uncertainty, labelled tables or graphs and sample calculations. Link the conclusion to evidence, discuss limitations and cite sources using correct chemical terminology and equations."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "A student graph has no units, a decorative curve and a title saying only 'Results'. Explain how it should be improved.",
       "model": "Name both variables and include units on the axes, choose scales that use the plotting area and plot points accurately. Use a best-fit line or curve supported by the data rather than joining points decoratively. Give an informative title identifying the relationship and include uncertainty or error bars where appropriate."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Assess the contribution of one named scientist to the development of an atomic model and explain why the model later changed.",
       "model": "Rutherford interpreted alpha-scattering evidence to propose a tiny dense positive nucleus and mostly empty space, overturning Thomson's diffuse positive model. The nuclear model could not explain stable electron arrangements or spectra. Later evidence led to quantised Bohr levels and then orbital models, showing that contribution includes both advance and limitation."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain why scientific discoveries are rarely the work of one isolated individual.",
       "model": "New work relies on earlier theories, instruments, technicians, shared data, funding and independent testing. Publication and peer review allow other scientists to challenge and reproduce claims. Credit should recognise a named contribution while also showing the collaborative and cumulative evidence that made acceptance possible."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Evaluate one way chemistry has benefited society while also creating a social or environmental problem.",
       "model": "Synthetic polymers provide sterile medical equipment, durable materials and low-mass transport components, but persistent waste, fossil feedstocks and microplastics create environmental costs. Chemistry also develops recycling and alternative materials. Evaluation must compare full life-cycle benefit, exposure and realistic alternatives rather than labelling the material simply good or bad."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain how societal priorities can influence chemical research, using one example.",
       "model": "Public health, regulation, markets and funding direct research towards urgent needs. Climate targets, for example, increase investment in battery chemistry, catalysts, carbon capture and low-emission fuels. Society shapes which questions receive resources, while chemical evidence informs policy; transparent methods are needed so commercial or political pressure does not distort conclusions."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Evaluate the media statement 'chemical-free cleaning products are safer for families'.",
       "model": "All cleaning products and natural substances consist of chemicals, so 'chemical-free' has no scientific meaning. Safety depends on identity, dose, exposure route and use, not whether a substance is natural. Check ingredients, hazard evidence, comparison conditions and commercial interest; the claim needs specific measurable outcomes before it can be tested."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "What evidence would you require before accepting a headline that a household chemical causes disease?",
       "model": "Look for peer-reviewed studies with appropriate controls, realistic exposure, adequate sample size, dose-response evidence and independent replication. Distinguish association from causation and relative from absolute risk. Consider confounding factors, mechanism, funding and whether the headline accurately represents the population and limitations of the study."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "For the process of evaporation, describe what is observed at the macroscopic level and explain what is happening at the microscopic level.",
       "model": "Macroscopic: the volume of liquid water decreases over time without being heated to boiling point — the water appears to 'disappear'. Microscopic: at the surface of the liquid, some water molecules have enough kinetic energy to overcome the intermolecular attractions holding them in the liquid phase and escape into the gas phase."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe two limitations of models used in chemistry.",
       "model": "1. Oversimplification: models leave out details to make them easier to understand, but this means they do not accurately represent the real system — e.g. dot-and-cross diagrams suggest electrons are static fixed points. 2. Assumptions: many models make assumptions that do not hold in reality — e.g. the ideal gas model assumes gas particles have no volume and no intermolecular forces, which breaks down at high pressures or low temperatures."
      }
     ],
     "chem2": [
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain what is meant by the term particulate nature of matter and describe a laboratory experiment that demonstrates it.",
       "model": "The particulate nature of matter refers to the idea that all substances are made up of tiny, invisible particles. Experiment: place cotton wool soaked in concentrated ammonia at one end of a sealed tube and cotton wool soaked in hydrochloric acid at the other end. A white ring of ammonium chloride forms inside the tube where the particles of ammonia and hydrogen chloride gas meet. This shows that both gases are made up of tiny moving particles (diffusion)."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State the two main assumptions of Dalton's atomic theory.",
       "model": "1. All matter is made up of very small particles called atoms. 2. All atoms are indivisible — they cannot be broken down into simpler particles."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe J.J. Thomson's experiment that led to the discovery of the electron.",
       "model": "Thomson produced a narrow beam of cathode rays and passed it between two parallel metal plates in a vacuum tube. When there was no charge on the plates, the beam passed straight down the tube. When a positive charge was applied to the top plate, the beam was deflected upwards (towards the positive plate). Since unlike charges attract, Thomson concluded that cathode rays consist of negatively charged particles, which he called electrons. Thomson also measured the charge-to-mass ratio of the electron."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe Rutherford's gold foil experiment, including his three observations and what conclusions he drew from each.",
       "model": "Rutherford bombarded a thin sheet of gold foil with alpha particles from a radioactive source and used a phosphorescent screen to detect them.\nObservations and conclusions:\n1. Most alpha particles passed straight through undeflected → most of the atom is empty space.\n2. Some alpha particles were deflected at large angles → the positive charge and mass are concentrated in a small dense core (nucleus) that repels the positive alpha particles.\n3. A very small number were reflected back along their original paths → some alpha particles collide head-on with the dense positive nucleus."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State the two limitations of Rutherford's original nuclear model of the atom.",
       "model": "1. Since like charges repel, the model could not explain why the nucleus does not fly apart due to the repulsion between the protons in it. 2. Since opposite charges attract, electrons should lose energy and spiral into the nucleus — yet most atoms are stable. The model could not explain why electrons remain in motion around the nucleus."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe how James Chadwick discovered the neutron and explain its importance for the nuclear model of the atom.",
       "model": "Chadwick (1932) bombarded beryllium with alpha particles. He detected neutral radiation coming from the beryllium — these neutral particles were difficult to detect directly, so he used paraffin wax, which the particles knocked protons out of. He found these particles had the same mass as a proton but no charge, and called them neutrons. The discovery of the neutron completed the nuclear model: neutrons help to 'cement' protons together in the nucleus, explaining why the nucleus does not fly apart due to proton–proton repulsion."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Give the relative charge, relative mass and location for each of the three sub-atomic particles.",
       "model": "Proton: relative charge +1, relative mass 1, located in the nucleus.\nNeutron: relative charge 0, relative mass 1, located in the nucleus.\nElectron: relative charge −1, relative mass 1/1838, located outside the nucleus (in the electron cloud)."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe the nuclear model of the atom as proposed after the discovery of the neutron (updated nuclear model).",
       "model": "1. Atoms consist of a small, dense positive core called the nucleus; most of the mass of the atom is concentrated there. 2. Positive particles called protons and neutral particles called neutrons are located in the nucleus. 3. The atom is mostly empty space. 4. Electrons are scattered around in the space surrounding the nucleus — this space is called the electron cloud. Limitation: the model cannot explain how electrons stay in motion around the nucleus without spiralling towards it and crashing into it."
      }
     ],
     "chem3": [
      {
       "type": "short",
       "marks": 4,
       "prompt": "State Heisenberg's Uncertainty Principle and explain how it undermines Bohr's model of the atom.",
       "model": "Heisenberg's Uncertainty Principle states that it is impossible to measure at the same time both the velocity and the position of an electron. Bohr's model assumes electrons travel in fixed orbits at a precise, constant distance from the nucleus — this implies both the position and velocity of the electron are known precisely. Heisenberg's principle shows this is impossible, so Bohr's model of fixed orbits cannot be correct."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State four limitations of Bohr's model of the atom.",
       "model": "1. Bohr's theory worked for hydrogen but failed to explain the emission spectra of atoms with more than one electron. 2. Bohr's model did not account for De Broglie's finding that electrons have wave-particle duality — if the electron has a wave motion, it cannot travel in a fixed orbit. 3. Bohr's model is in conflict with Heisenberg's Uncertainty Principle, which states that both the position and velocity of an electron cannot be known simultaneously. 4. Bohr's theory could not explain the splitting of certain spectral lines and did not account for the existence of energy sublevels."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define the term orbital and describe the shapes of s and p orbitals.",
       "model": "An orbital is a region in space within which there is a high probability (approximately 95%) of finding an electron. s orbitals are spherical in shape; all s orbitals differ only in size (1s < 2s < 3s). p orbitals are dumbbell-shaped. Each p sublevel consists of three dumbbell-shaped orbitals (pₓ, pᵧ, p_z) arranged at right angles to each other along the x, y and z axes. The three p orbitals in a sublevel are of equal energy and differ only in orientation."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between the terms orbit and orbital.",
       "model": "An orbit (used by Bohr) describes a fixed path in which an electron travels around the nucleus at a certain velocity and a precise, constant distance from the nucleus — both position and velocity are known. An orbital (used in the quantum mechanical model) is a region in space within which there is a high probability of finding an electron; it does not describe a fixed path but a probability distribution. Orbitals arise from Schrödinger's wave equations and are consistent with Heisenberg's Uncertainty Principle."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between a continuous spectrum and a line emission spectrum.",
       "model": "A continuous spectrum is a spread of all colours from red to violet with no gaps, produced when white light is passed through a prism. A line emission spectrum consists of a series of narrow coloured lines against a dark background, produced when light emitted by excited atoms of an element is passed through a prism. Each element has its own unique line emission spectrum."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain, using Bohr's theory, why the emission spectrum of hydrogen consists of lines rather than a continuous spectrum.",
       "model": "According to Bohr's theory, electrons can only exist in certain fixed energy levels (quantisation of energy). When an electron falls from a higher energy level to a lower one, it emits a photon of light with a definite frequency (E₂ − E₁ = hf). Since only definite amounts of energy can be emitted, only light of definite frequencies is given off. This produces specific coloured lines rather than a continuous spread of all colours."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Name the series of spectral lines in hydrogen that appear in the visible region, and state which energy level the electrons fall to in this series.",
       "model": "The Balmer series. Electrons fall to the n = 2 energy level. (The transition from n = 3 to n = 2 gives rise to a red coloured line.)"
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe the flame test experiment and state the colour produced by three different metals.",
       "model": "Using a damp wooden splint, hold a sample of a metal salt in the blue flame of a Bunsen burner. Repeat with different metal salts. Each metal gives a characteristic colour: Sodium — yellow; Potassium — lilac; Copper — blue-green; Lithium — crimson; Barium — green; Strontium — red. The colours can be used to identify the metal present in an unknown compound. (Any three metals + colours accepted for 4 marks.)"
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "How many sublevels are present in the n=3 main energy level? Name them and state the number of orbitals in each.",
       "model": "The n=3 main energy level contains 3 sublevels: 3s (1 orbital), 3p (3 orbitals), and 3d (5 orbitals). The number of sublevels in a main energy level is equal to the value of n."
      }
     ],
     "chem4": [
      {
       "type": "short",
       "marks": 4,
       "prompt": "State Mendeleev's Periodic Law and name two differences between Mendeleev's Periodic Table and the modern Periodic Table.",
       "model": "Mendeleev's Periodic Law: when elements are arranged in order of increasing atomic weight (relative atomic mass), the properties of the elements are repeated at regular intervals in other elements.\nDifferences (any two): (1) Mendeleev's table arranged by atomic weight; modern table by atomic number. (2) Mendeleev's table had gaps for undiscovered elements; modern table has no gaps. (3) Mendeleev's table had ~60 elements; modern table has over 100. (4) Transition elements are in a separate block in the modern table but were not in Mendeleev's."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe how Henry Moseley's work led to the development of the modern Periodic Table.",
       "model": "Henry Moseley (1913) used X-rays to study different elements. He found that the frequencies of the X-rays emitted varied with the quantity of positive charge in the nucleus, i.e. the number of protons (atomic number). This allowed him to determine the atomic number of each element. He found that arranging elements by atomic number (rather than atomic weight) removed the need to reverse the order of any elements. The modern Periodic Table is therefore an arrangement of elements in order of increasing atomic number."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define the terms (i) atomic number, (ii) mass number, and (iii) isotopes. Give an example of isotopes.",
       "model": "(i) Atomic number (Z): the number of protons in the nucleus of an atom. (ii) Mass number (A): the sum of the number of protons and neutrons in the nucleus of an atom. (iii) Isotopes: atoms of the same element (same atomic number) which have different mass numbers due to a different number of neutrons in their nuclei. Example: chlorine has two isotopes, ³⁵Cl (17 protons, 18 neutrons) and ³⁷Cl (17 protons, 20 neutrons)."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "How many (i) neutrons and (ii) electrons are in the ion ³⁵Cl⁻?",
       "model": "(i) Number of neutrons = mass number − atomic number = 35 − 17 = 18 neutrons.\n(ii) Cl⁻ has gained one electron, so number of electrons = 17 + 1 = 18 electrons."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Write the electron configuration (s, p notation) for (i) oxygen, (ii) potassium, (iii) calcium ion (Ca²⁺).",
       "model": "(i) Oxygen (Z=8): 1s², 2s², 2p⁴.\n(ii) Potassium (Z=19): 1s², 2s², 2p⁶, 3s², 3p⁶, 4s¹.\n(iii) Ca²⁺ (Z=20, lost 2 electrons → 18 electrons): 1s², 2s², 2p⁶, 3s², 3p⁶."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State the Aufbau Principle, Hund's Rule of Maximum Multiplicity, and the Pauli Exclusion Principle.",
       "model": "Aufbau Principle: when building up the electron configuration of an atom in its ground state, electrons occupy the lowest available energy levels first.\nHund's Rule of Maximum Multiplicity: when two or more orbitals of equal energy are available, electrons occupy them singly before filling them in pairs (maximising unpaired electrons).\nPauli Exclusion Principle: no more than two electrons may occupy an orbital and they must have opposite spin."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Write the s, p, d electron configuration for (i) chromium and (ii) copper, and explain why these are exceptions to what would normally be expected.",
       "model": "(i) Cr (Z=24): expected 1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d⁴. Actual: 1s², 2s², 2p⁶, 3s², 3p⁶, 3d⁵, 4s¹. One 4s electron moves to 3d because sublevels that are exactly half-filled have extra stability — this gives two half-filled sublevels (3d⁵ and 4s¹).\n(ii) Cu (Z=29): expected 1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d⁹. Actual: 1s², 2s², 2p⁶, 3s², 3p⁶, 3d¹⁰, 4s¹. One 4s electron moves to 3d because a completely filled 3d sublevel has extra stability."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "What do the ions O²⁻, F⁻, Na⁺ and Mg²⁺ have in common? Write their common electron configuration.",
       "model": "All four ions are isoelectronic — they each have 10 electrons and therefore the same electron configuration: 1s², 2s², 2p⁶. Although they have the same number of electrons, they have different numbers of protons and therefore different nuclear charges, which affects their ionic radii."
      }
     ],
     "chem5": [
      {
       "type": "short",
       "marks": 3,
       "prompt": "State the Octet Rule and give one exception to it.",
       "model": "Octet Rule: when bonding occurs, atoms tend to reach an electron arrangement with eight electrons in the outermost energy level. Exception (any one): transition metals do not usually obey the octet rule — they can have more or fewer than eight electrons in their outermost energy level. Also, helium and elements near helium (H, Li, Be) tend to achieve an arrangement of two outer electrons rather than eight."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain, using an example, the difference between ionic bonding and covalent bonding.",
       "model": "Ionic bonding involves the complete transfer of electrons from one atom to another, forming oppositely charged ions. The ionic bond is the force of attraction between these ions. Example: in NaCl, sodium loses one electron to chlorine → Na⁺ and Cl⁻ attract each other. Covalent bonding involves the sharing of electron pairs between atoms. No ions are formed. Example: in Cl₂, each chlorine atom shares one electron with the other to form a shared pair — a covalent bond."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between a sigma bond and a pi bond. Give two differences.",
       "model": "1. A sigma bond is formed by the head-on overlap of two orbitals; a pi bond is formed by the sideways overlap of p orbitals. 2. Sigma bonds involve more orbital overlap and are therefore stronger; pi bonds involve less overlap and are weaker. 3. All single covalent bonds are sigma bonds; pi bonds are only found in double and triple bonds. 4. A sigma bond can involve any orbital type (s, p, d); a pi bond only involves p (or d) orbitals."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Use the octet rule to predict the formula of the compound formed between magnesium and nitrogen, and draw a Lewis (dot-and-cross) diagram for it. State one limitation of the octet rule in predicting bonding.",
       "model": "Magnesium (2, 8, 2) loses two electrons to form Mg²⁺; nitrogen (2, 5) gains three electrons to form N³⁻. Both ions then have the stable neon configuration (2, 8). Charges must balance: 3 × (+2) = +6 and 2 × (−3) = −6, so the formula is Mg₃N₂. Lewis diagram: three [Mg]²⁺ ions with no outer electrons shown and two [N]³⁻ ions each with eight outer electrons (five dots and three crosses) in square brackets. Limitation (any one): some molecules are stable with fewer than eight outer electrons on the central atom (e.g. BF₃) or with more than eight (e.g. PCl₅ or SF₆); the rule says nothing about the shape of the molecule or whether the bonding is ionic or covalent."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe the laboratory test for the chloride ion in aqueous solution, including the confirmatory test.",
       "model": "1. Dissolve the chloride salt in deionised water. 2. Add a few drops of silver nitrate (AgNO₃) solution. 3. Observation: clear solution turns cloudy; a white precipitate of silver chloride forms. Equation: Ag⁺ + Cl⁻ → AgCl↓. 4. Confirmatory test: add dilute ammonia solution to the cloudy solution. The cloudiness disappears — silver chloride dissolves in dilute ammonia. Conclusion: chloride ions are present."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe how you would detect sulfate ions in aqueous solution and how you would distinguish them from sulfite ions.",
       "model": "To detect: dissolve the salt in deionised water. Add a few drops of barium chloride solution. A white precipitate forms for both sulfate (BaSO₄) and sulfite (BaSO₃). Ba²⁺ + SO₄²⁻ → BaSO₄↓; Ba²⁺ + SO₃²⁻ → BaSO₃↓.\nTo distinguish: add dilute hydrochloric acid to each white precipitate. The sulfate precipitate (BaSO₄) remains (insoluble in dilute HCl). The sulfite precipitate (BaSO₃) dissolves: SO₃²⁻ + 2H⁺ → SO₂ + H₂O."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe the Brown Ring test for the nitrate ion.",
       "model": "1. Dissolve the nitrate salt in deionised water. 2. Add freshly prepared iron(II) sulfate (FeSO₄) solution. 3. Using a dropper, carefully add concentrated sulfuric acid (H₂SO₄) down the inside wall of the test-tube — it forms a layer at the bottom due to its density. 4. Observation: a brown ring forms at the junction of the two liquid layers. 5. The brown ring is due to the formation of the substance FeSO₄·NO. Conclusion: nitrate ions are present. Note: concentrated H₂SO₄ must be used — dilute H₂SO₄ does not work."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "How would you test for the presence of carbonate ions in a solid sample and confirm your result?",
       "model": "1. Add dilute hydrochloric acid to the solid. 2. Observation: brisk effervescence (fizzing) is observed; a gas is given off. 3. Pass the gas through limewater. 4. The limewater turns milky (cloudy). This confirms the gas is carbon dioxide, produced by: CO₃²⁻ + 2H⁺ → CO₂ + H₂O; Ca(OH)₂ + CO₂ → CaCO₃↓ + H₂O. Conclusion: carbonate ions are present."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State the VSEPR theory and use it to predict the shapes of (i) methane and (ii) ammonia.",
       "model": "VSEPR Theory: the shape of a molecule depends on the number of pairs of electrons around the central atom. Since electron pairs are negatively charged, they repel each other and arrange themselves to be as far apart as possible.\n(i) Methane (CH₄): carbon has 4 bond pairs and 0 lone pairs. Four pairs as far apart as possible → tetrahedral shape; bond angle = 109.5°.\n(ii) Ammonia (NH₃): nitrogen has 4 pairs total (3 bond pairs + 1 lone pair). The lone pair exerts greater repulsion than a bond pair, reducing the bond angle from 109.5° to about 107°. Shape = pyramidal."
      }
     ],
     "chem6": [
      {
       "type": "short",
       "marks": 3,
       "prompt": "Define electronegativity and explain how it leads to the formation of a polar covalent bond.",
       "model": "Electronegativity is the relative attraction that an atom in a molecule has for the shared pair of electrons in a covalent bond. In a polar covalent bond, the two atoms have different electronegativity values — the more electronegative atom attracts the shared electron pair more strongly. This results in an unequal sharing: the more electronegative atom carries a partial negative charge (δ−) and the less electronegative atom carries a partial positive charge (δ+)."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Distinguish between a pure covalent bond and a polar covalent bond. Give one example of each.",
       "model": "A pure covalent bond involves equal sharing of the electron pair between two atoms with the same or very similar electronegativity values (E.N. difference ≈ 0), e.g. H−H or Cl−Cl. A polar covalent bond involves unequal sharing of the electron pair — the more electronegative atom attracts the pair more strongly, creating partial charges (δ+ and δ−), e.g. H−Cl or H−F."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Use electronegativity differences to predict the type of bonding in (i) NaCl and (ii) CH₄.",
       "model": "(i) NaCl: Na electronegativity = 0.93; Cl = 3.16. E.N. difference = 3.16 − 0.93 = 2.23 > 1.7 → ionic bonding.\n(ii) CH₄: C electronegativity = 2.55; H = 2.20. E.N. difference = 2.55 − 2.20 = 0.35 ≤ 0.4 → pure (non-polar) covalent bonding."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Compare the physical properties (state at room temperature, melting/boiling point, electrical conductivity, solubility in water) of ionic and covalent compounds.",
       "model": "State: ionic compounds are usually solids at room temperature (strong ionic bonds require much energy to break); most covalent compounds are liquids or gases (only weak intermolecular forces).\nM.p./B.p.: ionic have high m.p. and b.p. (e.g. NaCl m.p. = 801°C); covalent have low m.p. and b.p. (e.g. I₂ m.p. = 114°C).\nElectrical conductivity: ionic conduct when molten or dissolved in water (ions free to move); covalent do not usually conduct (no ions).\nSolubility: ionic are usually soluble in water (ion-dipole forces); polar covalent compounds are usually soluble; non-polar covalent compounds are usually insoluble in water ('like dissolves like')."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain how London dispersion forces arise and describe how molecular size affects their strength.",
       "model": "London dispersion forces arise because electrons are in constant motion within molecules. At any given instant, the electrons may be unevenly distributed, creating a temporary (instantaneous) dipole (δ+ on one side, δ− on the other). This temporary dipole can induce a dipole in a neighbouring molecule, leading to an attractive force between opposite charges — a London dispersion force.\n\nStrength increases with molecular size: larger molecules have more electrons and larger electron clouds. This gives them greater polarisability — temporary dipoles form more easily and are stronger. Therefore London dispersion forces increase in strength as molecular mass increases (e.g. F₂ < Cl₂ < Br₂ < I₂)."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define hydrogen bonding and state the three elements that hydrogen must be bonded to for hydrogen bonding to occur. Explain why H₂O has a higher boiling point than H₂S.",
       "model": "Hydrogen bonds are a particular type of dipole-dipole attraction between molecules in which hydrogen atoms bonded to N, O or F are attracted to a lone pair on a N, O or F atom in a neighbouring molecule. Hydrogen must be bonded to nitrogen, oxygen or fluorine (the three most electronegative elements — remember NOF).\n\nH₂O (b.p. = 100°C) has a much higher boiling point than H₂S (b.p. = -60°C) because hydrogen bonding exists in H₂O. Oxygen is electronegative enough to form hydrogen bonds with the H atoms; sulfur is not (smaller electronegativity difference between S and H). The hydrogen bonds between water molecules are much stronger than the dipole-dipole forces between H₂S molecules. Therefore more energy is required to separate H₂O molecules → higher boiling point."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Explain why water has a higher boiling point than hydrogen fluoride (HF), even though F is more electronegative than O.",
       "model": "Although fluorine is more electronegative than oxygen (so individual H bonds in HF are stronger), each water molecule can form TWICE as many hydrogen bonds as each HF molecule. This is because each O atom has two O−H bonds and two lone pairs, whereas each HF molecule has only one H−F bond. Therefore, overall, more energy is required to break the hydrogen bonds between water molecules than between HF molecules, giving water the higher boiling point."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain why carbon dioxide (CO₂) has two polar bonds but is a non-polar molecule overall.",
       "model": "The C=O bond is polar covalent because oxygen is more electronegative than carbon, so each oxygen carries a δ− charge and the carbon carries a δ+ charge. However, the CO₂ molecule is linear (bond angle = 180°). Because the molecule is symmetrical, the two C=O bond dipoles point in exactly opposite directions and cancel each other out. The centres of the partial positive and partial negative charges coincide — they are not separated by a distance. Therefore, there is an even distribution of charge overall and CO₂ is a non-polar molecule."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Explain what an ion-dipole force is and how it accounts for the solubility of NaCl in water.",
       "model": "An ion-dipole force is the force of attraction between an ion and a polar molecule. When NaCl is placed in water, the polar water molecules are attracted to the Na⁺ and Cl⁻ ions. The negative end (O atom) of water is attracted to Na⁺; the positive end (H atoms) is attracted to Cl⁻. These ion-dipole forces overcome the ionic bonding between the ions in the crystal lattice, pulling the ions away from the lattice and surrounding them with water molecules. The ions are said to dissolve."
      }
     ],
     "chem7": [
      {
       "type": "short",
       "marks": 5,
       "prompt": "Describe the properties of the halogens (Group 17) and explain why their reactivity increases up the group.",
       "model": "Properties of halogens: highly electronegative non-metals; very reactive; do not exist free in nature; poor conductors of electricity. States: F₂ is a colourless gas, Cl₂ is a pale green/yellow gas, Br₂ is a dark red volatile liquid, I₂ is a purple solid (sublimes on heating). Reactivity increases up Group 17 for two reasons: 1. Atomic radius decreases going up the group — the outermost electrons are closer to the nucleus and held more tightly. 2. Screening effect decreases going up — fewer inner energy levels. These two factors increase the electronegativity going up the group, so the halogen has a greater ability to attract electrons from other atoms, making it more reactive. Fluorine at the top is the most electronegative and most reactive halogen."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe what is observed when chlorine gas is bubbled through a solution containing bromide ions. Write a balanced equation for the reaction and explain why it occurs.",
       "model": "Observation: the colourless solution turns red/orange (red-brown), indicating the formation of bromine. Equation: Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂. Explanation: chlorine is more electronegative than bromine (E.N. of Cl = 3.16 vs Br = 2.96). Because of its greater electronegativity, chlorine has a greater attraction for electrons and removes them from the bromide ions in solution, converting them to bromine molecules. This is a halogen displacement reaction — the more reactive halogen (chlorine) displaces the less reactive halogen (bromine) from a solution of its ions."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State four properties of the alkali metals and give two reasons why their reactivity increases down Group 1.",
       "model": "Properties of alkali metals: (1) shiny, silvery solids; (2) stored under oil to prevent reaction with air and moisture; (3) low first ionisation energies — readily lose their single outer electron to form +1 ions; (4) not found free in nature; reactivity increases down the group. Why reactivity increases down Group 1: 1. Atomic radius increases — the outer electron is further from the nucleus and less strongly attracted, so it is easier to remove. 2. Screening effect increases — more inner energy levels shield the outer electron from the nucleus, further reducing the attractive force. Both factors cause the first ionisation energy to decrease down the group, making it progressively easier to lose the outer electron and increasing reactivity."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Outline the trends in electronegativity in the Periodic Table and explain the reasons for the trend down a group.",
       "model": "Electronegativity decreases down the groups and increases along the periods. Down a group, two reasons explain the decrease: 1. Increasing atomic radius — as atomic radius increases down a group, the shared pair of electrons in the covalent bond is further from the nucleus, so the attractive force on the shared pair decreases and electronegativity decreases. 2. Screening effect of inner electrons — the increasing number of inner energy levels screens the nucleus from the shared pair of electrons, reducing the attractive force and decreasing the electronegativity."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define atomic radius (covalent radius) and state the general trends in atomic radius across a period and down a group in the Periodic Table.",
       "model": "The atomic radius (covalent radius) of an atom is defined as half the distance between the nuclei of two atoms of the same element that are joined together by a single covalent bond (i.e. half the bond length). General trends: atomic radius decreases from left to right across a period (due to increasing effective nuclear charge with no increase in screening). Atomic radius increases down a group (due to the addition of new energy levels and the screening effect of inner electrons)."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Give two reasons why atomic radius increases down a group in the Periodic Table.",
       "model": "1. New energy level: as you move down a group, electrons are added to new, higher energy levels (orbitals) that are further from the nucleus, increasing the atomic radius. 2. Screening effect: the inner electrons in lower energy levels shield (screen) the outer electrons from the attractive force of the nucleus. Although nuclear charge increases going down a group, the increase is counteracted by the greater screening effect of the additional inner energy levels, so the outer electrons are not pulled in and atomic radius increases."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Give two reasons why atomic radius decreases across a period in the Periodic Table.",
       "model": "1. Increasing effective nuclear charge: as you move from left to right across a period, the number of protons increases. There is no corresponding increase in screening (all new electrons enter the same outer energy level). Therefore the effective nuclear charge increases, pulling outer electrons closer to the nucleus and decreasing atomic radius. 2. No increase in the screening effect: since there is no increase in the number of inner energy levels across a period, there is no additional shielding to counteract the increasing nuclear charge, so the outer electrons are pulled progressively closer."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Define first ionisation energy and write an equation to represent the first ionisation energy of potassium.",
       "model": "The first ionisation energy of an atom is the minimum energy required to completely remove the most loosely bound electron from a neutral gaseous atom in its ground state. Equation: K(g) → K⁺(g) + e⁻. (Units: kJ mol⁻¹; the state symbol (g) is essential.)"
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "In period 2, beryllium (Be) has a higher first ionisation energy than boron (B), and nitrogen (N) has a higher first ionisation energy than oxygen (O). Explain these observations.",
       "model": "Beryllium (Be = 1s², 2s²) has a higher IE than boron (B = 1s², 2s², 2p¹) because beryllium has a completely filled 2s sublevel. A completely filled sublevel has extra stability, so more energy is required to remove an electron from it than from the singly-occupied 2p sublevel of boron. Nitrogen (N = 1s², 2s², 2p³) has a higher IE than oxygen (O = 1s², 2s², 2p⁴) because nitrogen has an exactly half-filled 2p sublevel. A half-filled sublevel has extra stability, so more energy is required to remove an electron from it than from oxygen's 2p⁴ configuration (where one orbital is doubly occupied and gives an easier-to-remove electron)."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "The successive ionisation energies (kJ mol⁻¹) of an element are: 1st = 496; 2nd = 4563; 3rd = 6913. Identify the group of this element in the Periodic Table and explain your reasoning.",
       "model": "The element is in Group 1. There is a very large increase in ionisation energy between the 1st IE (496 kJ mol⁻¹) and the 2nd IE (4563 kJ mol⁻¹). This large jump indicates that the second electron is being removed from a different, closer (lower) energy level than the first electron. This means the first electron was in an outer energy level on its own — consistent with a Group 1 element that has one electron in its outermost energy level. The relatively small increase from 2nd to 3rd IE confirms that both the 2nd and 3rd electrons come from the same inner energy level."
      }
     ],
     "chem8": [
      {
       "type": "short",
       "marks": 3,
       "prompt": "Define the term mole and state the value of the Avogadro constant.",
       "model": "The mole is the SI unit of amount of substance. One mole of a substance contains 6.02 × 10²³ elementary entities of the substance. The Avogadro constant, Nₐ, has a value of 6.02 × 10²³ mol⁻¹."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain, using relative atomic masses, why one mole of magnesium has a mass of 24 g and one mole of carbon has a mass of 12 g, and why both samples contain the same number of atoms.",
       "model": "From the Periodic Table, the relative atomic mass of Mg is 24 and the relative atomic mass of C is 12. This means one Mg atom is twice as heavy as one C atom. Therefore, in any sample where Mg and C are present in the mass ratio 2:1, both elements contain the same number of atoms. When we weigh out 24 g of Mg and 12 g of C (the same ratio as their relative atomic masses), both samples must contain the same number of atoms. This number is 6.02 × 10²³ — one mole."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Calculate the relative molecular mass of sulfuric acid, H₂SO₄.",
       "model": "H₂SO₄: 2 H = 2 × 1.008 = 2.016; 1 S = 1 × 32.07 = 32.07; 4 O = 4 × 16.00 = 64.00. Relative molecular mass = 2.016 + 32.07 + 64.00 = 98.086."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Calculate the relative molecular mass of hydrated copper(II) sulfate, CuSO₄·5H₂O.",
       "model": "CuSO₄·5H₂O: Cu = 63.5; S = 32.07; 4 O = 4 × 16.00 = 64.00; 5 H₂O = 5 × 18.016 = 90.08. Relative molecular mass = 63.5 + 32.07 + 64.00 + 90.08 = 249.65."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Calculate the mass of 2.5 moles of water, H₂O.",
       "model": "Mr of H₂O: 2 H = 2 × 1.008 = 2.016; 1 O = 16.00. Mr = 18.016. Mass = Number of moles × Mr = 2.5 × 18.016 = 45.04 g."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Calculate the number of moles in 49 g of sulfuric acid, H₂SO₄.",
       "model": "Mr of H₂SO₄ = 98.086 (2 × 1.008 + 32.07 + 4 × 16.00). Number of moles = mass / Mr = 49 / 98.086 = 0.4996 ≈ 0.5 mol."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Calculate the number of molecules in 44 g of carbon dioxide, CO₂.",
       "model": "Step 1 — calculate Mr of CO₂: 1 C = 12.01; 2 O = 32.00. Mr = 44.01. Step 2 — calculate moles: n = 44 / 44.01 = 0.9998 ≈ 1.0 mol. Step 3 — calculate number of molecules: 1.0 × 6.02 × 10²³ = 6.02 × 10²³ molecules."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "How many atoms of aluminium are present in 9 × 10²² atoms of aluminium? Express your answer in moles.",
       "model": "Number of moles = number of atoms / Avogadro constant = 9 × 10²² / 6.02 × 10²³ = 0.15 mol."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "What is the mass (in grams) of 3 × 10²² molecules of ethanol, C₂H₅OH?",
       "model": "Step 1 — calculate Mr of C₂H₅OH: 2 C = 2 × 12.01 = 24.02; 5 H = 5 × 1.008 = 5.04; 1 O = 16.00; 1 H = 1.008. Mr = 46.068. Step 2 — calculate moles: n = 3 × 10²² / 6.02 × 10²³ = 0.04983 mol. Step 3 — calculate mass: mass = n × Mr = 0.04983 × 46.068 = 2.296 g."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Calculate the number of atoms in 28.75 g of sodium.",
       "model": "Step 1 — calculate moles of Na: Ar of Na = 22.99; n = 28.75 / 22.99 = 1.2505 mol. Step 2 — calculate number of atoms: 1.2505 × 6.02 × 10²³ = 7.528 × 10²³ atoms."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Define relative atomic mass and calculate the relative atomic mass of chlorine, which is 75% chlorine-35 and 25% chlorine-37.",
       "model": "Relative atomic mass is the average of the mass numbers of the isotopes of an element, as they occur naturally, taking their abundances into account, expressed on a scale where carbon-12 = exactly 12 units. Multiply each mass number by its percentage abundance, add the products and divide by 100: relative atomic mass = (75×35 + 25×37)/100 = 35.5."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State Avogadro's Law and use it to explain Gay-Lussac's Law of Combining Volumes. What volume does one mole of any gas occupy at s.t.p.?",
       "model": "Avogadro's Law states: equal volumes of gases contain equal numbers of molecules under the same conditions of temperature and pressure. This explains Gay-Lussac's Law: the ratio of volumes equals the ratio of molecules. For H₂ + Cl₂ → 2HCl: if 1 volume H₂ contains n molecules and 1 volume Cl₂ contains n molecules, then they produce 2n molecules of HCl → 2 volumes of HCl. The molecule ratio from the equation directly gives the volume ratio. At s.t.p., one mole of any gas occupies 22.4 litres (the molar volume)."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Describe the key steps in the experiment to measure the relative molecular mass of a volatile liquid using a conical flask.",
       "model": "A volatile liquid is one with a low boiling point. Key steps: (1) Weigh a clean, dry conical flask with rubber band and aluminium foil cap (with a tiny pinhole). Pour ~10 cm³ of the volatile liquid into the flask. Clamp in boiling water until all the liquid vaporises — the vapour fills the flask and excess escapes through the pinhole. Record temperature (boiling water temperature) and atmospheric pressure. (2) Remove flask; allow to cool — vapour condenses to a liquid. Dry the outside; reweigh. Mass of condensed liquid = (mass after) − (initial mass of empty flask). (3) Find the volume of the flask by filling completely with water and measuring in a graduated cylinder. (4) Calculate: n = pV/RT (using the Ideal Gas Equation); Mr = mass of condensed liquid / n."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Describe how to prepare 250.0 cm³ of 0.100 mol dm⁻³ sodium carbonate solution from a pure solid.",
       "model": "Calculate the required moles using n = cV, then mass using m = nMr. Accurately weigh the solid, dissolve it completely in deionised water, transfer quantitatively to a 250.0 cm³ volumetric flask and rinse all vessels into it. Make to the mark at eye level, stopper and invert repeatedly to mix."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain why a primary standard must be pure, stable and accurately weighable.",
       "model": "Its weighed mass must correspond reliably to a known number of moles. High purity avoids unknown reacting material, stability and low hygroscopicity prevent composition changing during storage or weighing, and a reasonably high molar mass reduces percentage weighing uncertainty. Complete predictable reaction is also required."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Convert 5.85 g dm⁻³ sodium chloride to mol dm⁻³ and then to mmol dm⁻³. Use Mr(NaCl) = 58.5.",
       "model": "Molar concentration is mass concentration divided by molar mass: 5.85 divided by 58.5 equals 0.100 mol dm⁻³. Multiplying by 1000 gives 100 mmol dm⁻³. Units must be converted explicitly; the numerical factor between mol dm⁻³ and mmol dm⁻³ is 1000."
      }
     ],
     "chem9": [
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define Brownian motion and explain how it provides evidence for the Kinetic Theory of Matter.",
       "model": "Brownian motion is the random, irregular, zig-zag, continuous movement of tiny particles (such as pollen grains or smoke particles) suspended in a liquid or gas. The movement results from the collisions of these tiny particles with the molecules of the liquid or gas. Evidence for KTM: the random movement of the pollen grains (visible particles) can only be explained if the smaller, invisible water molecules are in continuous, random motion, constantly bombarding the pollen from all sides. The random nature of the collisions causes the random, unpredictable movement. This directly supports the KTM assumption that all particles are in constant motion."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe an experiment to demonstrate diffusion of gases. What is observed and how does the result provide evidence for the Kinetic Theory of Matter?",
       "model": "Experiment: place cotton wool soaked in concentrated ammonia at one end of a dry glass tube, and cotton wool soaked in concentrated hydrochloric acid at the other end. Seal both ends. Observation: after a short time, a white ring of solid ammonium chloride (NH₄Cl) forms inside the tube, closer to the HCl end. Equation: NH₃(g) + HCl(g) → NH₄Cl(s). Explanation: both gases diffuse (move from high to low concentration) from their respective ends towards the middle. NH₃ molecules (Mr = 17) are lighter than HCl molecules (Mr = 36.5) and diffuse faster, so the ring forms closer to the HCl end. Evidence for KTM: this result demonstrates that gas molecules are in constant motion, spontaneously spreading out to occupy the available space — consistent with the KTM assumption that particles are always in motion."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State the Kinetic Theory of Matter and explain how it accounts for the arrangement of particles in a solid, liquid, and gas.",
       "model": "The Kinetic Theory of Matter states that all matter is made up of tiny particles (atoms or molecules) that are in constant random motion, and that temperature affects the speed of this motion. In solids: particles are packed closely together in fixed positions; they vibrate about fixed positions but do not move freely; strong forces hold them together → definite shape and volume. In liquids: particles are close together but not in fixed positions; they slide over each other; forces weaker than in solids → definite volume, no fixed shape. In gases: particles are far apart and continuously moving very fast in random directions; very weak forces between particles → no fixed shape or volume; gas fills its container."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "A mixture contains iron filings, sand and dissolved sodium chloride. Justify a sequence that separates all three components.",
       "model": "Remove iron with a magnet because it is magnetic. Add water if needed and filter: insoluble sand remains as residue while sodium chloride passes in solution. Wash and dry the sand. Evaporate some water and cool to crystallise sodium chloride, then filter and dry the crystals; simple evaporation to dryness risks impurity or spitting."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Choose between filtration, distillation and chromatography for three different separation problems and justify each choice.",
       "model": "Use filtration for an insoluble solid in a liquid because particle size prevents passage. Use distillation to recover a solvent or separate liquids with different boiling behaviour. Use chromatography for small amounts of soluble components whose different attractions to stationary and mobile phases cause different movement."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Give two reasons why real gases deviate from ideal gas behaviour, and state under what conditions of temperature and pressure real gases come closest to ideal behaviour.",
       "model": "Two reasons real gases deviate from ideal behaviour: (1) Real gases have small but significant attractive or repulsive intermolecular forces between molecules, contrary to the assumption of no intermolecular forces. Polar gases (e.g. NH₃, HCl, H₂O) have particularly strong forces (hydrogen bonds or dipole-dipole forces). (2) The volume of the molecules of a real gas is small but not negligible, especially at high pressures when molecules are forced close together. Real gases come closest to ideal behaviour at: high temperature (molecules move rapidly, so intermolecular forces have little effect) and low pressure (molecules are far apart, so molecular volume is negligible compared to the total volume)."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "State Boyle's Law and write an equation to express it mathematically.",
       "model": "Boyle's Law states: at constant temperature, the volume of a fixed mass of gas is inversely proportional to its pressure. Mathematical expression: V ∝ 1/p (at constant temperature), or equivalently pV = k (constant), or p₁V₁ = p₂V₂."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "A sample of nitrogen gas has a volume of 75 cm³ at 27 °C and a pressure of 95 kPa. Find the volume it would occupy at s.t.p. (273 K, 100 kPa).",
       "model": "Use the Combined Gas Law: p₁V₁/T₁ = p₂V₂/T₂. Given: p₁ = 95 kPa, V₁ = 75 cm³, T₁ = 27°C + 273 = 300 K; p₂ = 100 kPa, T₂ = 273 K. V₂ = (p₁V₁T₂)/(T₁p₂) = (95 × 75 × 273)/(300 × 100) = 1 944 375 / 30 000 = 64.84 cm³."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "State Gay-Lussac's Law of Combining Volumes and give one example of a reaction that illustrates this law.",
       "model": "Gay-Lussac's Law of Combining Volumes states: in a reaction between gases, the volumes of the reacting gases and the volumes of any gaseous products are in the ratio of small whole numbers, provided the volumes are measured at the same temperature and pressure. Example: H₂(g) + Cl₂(g) → 2HCl(g) — the volumes are in the ratio 1:1:2."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Write the Ideal Gas Equation, identify all variables and their units, and state the value of the Universal Gas Constant R.",
       "model": "The Ideal Gas Equation is: pV = nRT, where: p = pressure in pascals (Pa); V = volume in cubic metres (m³); n = number of moles; R = Universal Gas Constant = 8.31 J mol⁻¹ K⁻¹; T = temperature in Kelvin (K). The equation is also called the Equation of State for an Ideal Gas. Unit conversions to remember: pressure in kPa → multiply by 10³ to get Pa; volume in litres → divide by 10³ to get m³; volume in cm³ → divide by 10⁶ to get m³."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Calculate the volume occupied by 10 g of oxygen gas, O₂, at 25 °C and 200 kPa. [R = 8.31 J mol⁻¹ K⁻¹]",
       "model": "Step 1 — calculate n: Mr of O₂ = 32; n = 10/32 = 0.3125 mol. Step 2 — convert units: p = 200 kPa = 200 × 10³ Pa = 2 × 10⁵ Pa; T = 25°C + 273 = 298 K. Step 3 — apply pV = nRT: V = nRT/p = (0.3125 × 8.31 × 298)/(2 × 10⁵) = (774.18)/(200 000) = 3.87 × 10⁻³ m³ = 3.87 L ≈ 3.8 L."
      }
     ],
     "chem10": [
      {
       "type": "short",
       "marks": 3,
       "prompt": "Distinguish between a physical change and a chemical change. Give one example of each.",
       "model": "A physical change is a change that does not result in the formation of any new substance; only the physical appearance or state of the substance changes. Example: melting of ice (H₂O solid → H₂O liquid — same substance, different state). A chemical change is a change that results in the formation of one or more new substances. It is usually accompanied by an energy change (heat, light, or sound) and is difficult to reverse. Example: burning of magnesium in air (Mg + O₂ → MgO — a new substance, magnesium oxide, is formed)."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "State the Law of Conservation of Mass and explain what it means at the atomic level.",
       "model": "The Law of Conservation of Mass states that when a chemical reaction occurs, the total mass of the reactants is always equal to the total mass of the products. At the atomic level, this means that atoms cannot be created or destroyed during a chemical reaction — the atoms present in the reactants are simply rearranged to form the products. The number of atoms of each element is the same before and after the reaction, so the total mass remains unchanged."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe an experiment to verify the Law of Conservation of Mass. Include the precaution that must be taken and explain why.",
       "model": "Experiment: prepare two solutions — silver nitrate (AgNO₃) and sodium chloride (NaCl) — in separate containers connected so they can be mixed without opening. Weigh the entire closed system before reaction. Mix the solutions — a white precipitate of silver chloride (AgCl) forms: Ag⁺(aq) + Cl⁻(aq) → AgCl(s)↓. Weigh the system again after the reaction. Observation: the total mass is the same before and after the reaction. Precaution: the experiment must be carried out in a CLOSED SYSTEM (sealed container). This is necessary because if the container were open, gases could escape or air could enter the system during the reaction, making it appear that mass has been gained or lost, giving false results."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Balance the following equation: CH₄ + O₂ → CO₂ + H₂O. Show your reasoning.",
       "model": "Step 1: Count atoms — LHS: 1 C, 4 H, 2 O; RHS: 1 C, 2 H, 3 O. The equation is not balanced. Step 2: To get 4 H on the right, put a 2 before H₂O: CH₄ + O₂ → CO₂ + 2H₂O. Now count: LHS: 1 C, 4 H, 2 O; RHS: 1 C, 4 H, 4 O. H is now balanced but O is not. Step 3: To get 4 O on the left, put a 2 before O₂: CH₄ + 2O₂ → CO₂ + 2H₂O. Final check: LHS: 1 C, 4 H, 4 O; RHS: 1 C, 4 H, 4 O. The equation is now balanced."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "What is meant by the term stoichiometry? Interpret the equation 2H₂ + O₂ → 2H₂O in terms of moles and grams.",
       "model": "Stoichiometry is the branch of chemistry that tells us the relationship between the amounts of reactants and products in a balanced chemical equation. Interpreting 2H₂ + O₂ → 2H₂O: in terms of moles — 2 moles of H₂ react with 1 mole of O₂ to produce 2 moles of H₂O. In terms of grams — 4 g of H₂ (2 × 2 g mol⁻¹) react with 32 g of O₂ (1 × 32 g mol⁻¹) to produce 36 g of H₂O (2 × 18 g mol⁻¹). Note: 4 + 32 = 36, consistent with the Law of Conservation of Mass."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Calculate the percentage by mass of nitrogen in ammonium nitrate, NH₄NO₃. (H = 1, N = 14, O = 16)",
       "model": "Step 1: Calculate Mr of NH₄NO₃: 2 N = 2 × 14 = 28; 4 H = 4 × 1 = 4; 3 O = 3 × 16 = 48. Mr = 28 + 4 + 48 = 80. Step 2: Percentage of N = (mass of N / Mr) × 100 = (28/80) × 100 = 35%. Answer: 35% nitrogen by mass."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between molecular formula and empirical formula. Give one example of a compound where they differ.",
       "model": "The molecular formula of a compound shows the actual number and type of each atom present in one molecule of the compound. The empirical formula shows the simplest whole-number ratio of the different atoms present in the molecule. They are related by: Molecular formula = Empirical formula × n (where n is a whole number). Example where they differ: hydrogen peroxide — molecular formula H₂O₂ (2 H, 2 O per molecule); empirical formula HO (simplest ratio 1:1). Another example: benzene — molecular formula C₆H₆; empirical formula CH."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "A compound contains 52.17% carbon, 13.04% hydrogen and 34.79% oxygen. The relative molecular mass of the compound is 92. Calculate the empirical formula and then determine the molecular formula. (H = 1, C = 12, O = 16)",
       "model": "Step 1 — calculate moles of each element (assuming 100 g): C = 52.17/12 = 4.35 mol; H = 13.04/1 = 13.04 mol; O = 34.79/16 = 2.17 mol. Step 2 — divide by smallest (2.17): C = 4.35/2.17 = 2; H = 13.04/2.17 = 6; O = 2.17/2.17 = 1. Empirical formula = C₂H₆O. Mr of empirical formula = 2(12) + 6(1) + 16 = 46. Step 3 — find n: n = 92/46 = 2. Molecular formula = C₂H₆O × 2 = C₄H₁₂O₂."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "In an experiment, 1.02 g of copper powder was heated in air and found to form 1.28 g of copper oxide. Calculate the empirical formula of the oxide. (Cu = 63.5, O = 16)",
       "model": "Step 1 — apply LCM to find mass of O: mass of O = 1.28 − 1.02 = 0.26 g. Step 2 — calculate moles of each element: moles Cu = 1.02/63.5 = 0.0161 mol; moles O = 0.26/16 = 0.0163 mol. Step 3 — find simplest ratio: Cu:O = 0.0161:0.0163 ≈ 1:1. Therefore, empirical formula = CuO. (This is copper(II) oxide.)"
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Magnesium burns in oxygen according to: 2Mg + O₂ → 2MgO. Calculate the mass of magnesium oxide formed when 9 g of magnesium burns completely in excess oxygen. (Mg = 24, O = 16)",
       "model": "Write the mole relationship: 2 moles Mg → 2 moles MgO. Calculate masses: 2 × 24 = 48 g Mg → 2 × (24 + 16) = 80 g MgO. Scale to given amount: 1 g Mg → 80/48 g MgO. Therefore, 9 g Mg → 9 × 80/48 = 15 g MgO. Answer: 15 g of magnesium oxide is formed."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Carbon burns in excess oxygen: C + O₂ → CO₂. Calculate the volume of carbon dioxide produced (at s.t.p.) when 30 g of carbon is burned. (C = 12; molar volume at s.t.p. = 22.4 L)",
       "model": "Mole relationship: 1 mole C → 1 mole CO₂. At s.t.p.: 12 g C → 22.4 L CO₂. Scale: 1 g C → 22.4/12 L CO₂. Therefore, 30 g C → 30 × 22.4/12 = 56 L CO₂. Answer: 56 litres of CO₂ at s.t.p."
      }
     ],
     "chem11": [
      {
       "type": "short",
       "marks": 3,
       "prompt": "Define neutralisation and write a balanced equation for the reaction between sulfuric acid and calcium hydroxide.",
       "model": "Neutralisation is the reaction between an acid and a base to form a salt and water. The general equation is: Acid + Base → Salt + Water. Balanced equation for H₂SO₄ and Ca(OH)₂: H₂SO₄ + Ca(OH)₂ → CaSO₄ + 2H₂O. (Sulfuric acid + calcium hydroxide → calcium sulfate + water.)"
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain how antacid tablets work. Write a balanced chemical equation for the reaction of hydrochloric acid with sodium hydrogencarbonate.",
       "model": "The stomach produces hydrochloric acid (HCl) for digestion. If too much HCl is produced (due to overeating or stress), it can cause indigestion or ulcers. Antacid tablets contain a base that neutralises the excess HCl. For example, Alka-Seltzer and Bisodol contain sodium hydrogencarbonate (NaHCO₃), which reacts with the excess HCl in a neutralisation reaction. Balanced equation: HCl + NaHCO₃ → NaCl + H₂O + CO₂. The CO₂ gas produced causes the fizzing observed when the tablet dissolves."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Write a balanced chemical equation for the reaction between hydrochloric acid and calcium carbonate. State two observations and explain why the reaction is relevant to environmental chemistry.",
       "model": "Equation: 2HCl + CaCO₃ → CaCl₂ + H₂O + CO₂. Observations: (1) fizzing/effervescence (CO₂ gas is produced); (2) the calcium carbonate (marble) slowly dissolves. Environmental relevance: acid rain contains dilute sulfuric acid (H₂SO₄) and other acids. When acid rain falls on limestone buildings, bridges, and statues (all made of CaCO₃), the acid reacts with the calcium carbonate and gradually dissolves and erodes the structure: H₂SO₄ + CaCO₃ → CaSO₄ + H₂O + CO₂."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "State the general word equation for the reaction of an acid with a metal and write a balanced equation for sulfuric acid reacting with zinc.",
       "model": "General equation: Acid + Metal → Salt + Hydrogen gas. Balanced equation for H₂SO₄ and Zn: H₂SO₄ + Zn → ZnSO₄ + H₂. The hydrogen gas produced can be confirmed by holding a lit splint at the mouth of the test tube — the gas ignites with a 'pop'. Note: highly reactive metals such as sodium and potassium must never be added to acids as the reaction is dangerously violent."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State the Arrhenius definition of an acid and a base. Give one example of each with a dissociation equation.",
       "model": "Arrhenius acid: a substance that dissociates in water to produce H⁺ ions. Example: HCl → H⁺ + Cl⁻ (hydrochloric acid dissociates completely to give H⁺ and Cl⁻ ions). Arrhenius base: a substance that dissociates in water to produce OH⁻ ions. Example: NaOH → Na⁺ + OH⁻ (sodium hydroxide dissociates to give Na⁺ and OH⁻ ions). The OH⁻ ion is called the hydroxide ion."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "What is the hydronium ion? Explain how it forms when hydrogen chloride dissolves in water.",
       "model": "The hydronium ion (H₃O⁺) is the ion formed when a bare H⁺ ion (proton) reacts with a water molecule. A H⁺ ion is simply a bare proton and cannot exist independently in solution. When HCl dissolves in water, the H⁺ ion produced reacts with a water molecule via a dative (coordinate) covalent bond: H⁺ + H₂O → H₃O⁺. Both electrons in this bond are provided by the oxygen lone pair of the water molecule. Therefore, the dissociation of HCl in water is more accurately written as: HCl + H₂O → H₃O⁺ + Cl⁻."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State the Brønsted–Lowry definitions of an acid and a base. Give an example of a reaction that is classified as acid–base by Brønsted–Lowry but NOT by Arrhenius.",
       "model": "Brønsted–Lowry definition: an acid is a proton donor; a base is a proton acceptor. Example of a reaction classified as acid–base by B-L but not Arrhenius: HCl(g) + NH₃(g) → NH₄Cl(s). In this reaction, HCl (the gas) donates a proton to NH₃ (the gas) — HCl is the B-L acid and NH₃ is the B-L base. However, there is no water present in this reaction, so it cannot be classified as an acid–base reaction using the Arrhenius theory, which is limited to reactions occurring in aqueous (water) solution."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Give three ways in which the Brønsted–Lowry theory is an improvement on the Arrhenius theory.",
       "model": "1. Not limited to water: the Arrhenius theory is restricted to reactions occurring in aqueous solution, while the Brønsted–Lowry theory can be applied to reactions in the gaseous state and in solvents other than water. 2. Broader definition of bases: the Arrhenius theory classifies only substances that produce OH⁻ ions as bases. The Brønsted–Lowry theory has a more general classification — any substance that can accept a proton is a base, including carbonate (CO₃²⁻) and hydrogencarbonate (HCO₃⁻) ions. 3. Amphoteric substances: the Arrhenius theory cannot explain how a substance can act as both an acid and a base, but the Brønsted–Lowry theory explains this in terms of the ability to both donate and accept protons."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define the terms conjugate acid, conjugate base, and conjugate acid–base pair. Identify the two conjugate acid–base pairs in the following equation: CH₃COOH + H₂O ⇌ CH₃COO⁻ + H₃O⁺",
       "model": "Conjugate acid: the species formed when a base accepts a proton — a base changes into its conjugate acid when it accepts a proton. Conjugate base: the species formed when an acid donates a proton — an acid changes into its conjugate base when it donates a proton. Conjugate acid–base pair: any pair consisting of an acid and a base that differ by exactly one proton. In CH₃COOH + H₂O ⇌ CH₃COO⁻ + H₃O⁺: Conjugate pair 1: CH₃COOH (acid) / CH₃COO⁻ (conjugate base) — they differ by one proton. Conjugate pair 2: H₃O⁺ (acid) / H₂O (conjugate base) — they differ by one proton."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "What is an amphoteric (amphiprotic) substance? Explain why water is considered amphoteric.",
       "model": "An amphoteric (or amphiprotic) substance is one that can act both as an acid (proton donor) and as a base (proton acceptor), depending on what it reacts with. Water is amphoteric because: (1) When HCl dissolves in water, H₂O accepts a proton from HCl (acts as a B-L base): HCl + H₂O → H₃O⁺ + Cl⁻. (2) When NH₃ dissolves in water, H₂O donates a proton to NH₃ (acts as a B-L acid): NH₃ + H₂O → NH₄⁺ + OH⁻. In these two reactions, water acts as a base in the first and as an acid in the second — demonstrating its amphoteric character."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between a strong acid and a weak acid in terms of the Arrhenius theory. Give one example of each.",
       "model": "A strong acid is a substance that almost completely dissociates in water to give H⁺ ions — almost every molecule breaks up. Example: hydrochloric acid (HCl → H⁺ + Cl⁻; essentially all HCl molecules dissociate). A weak acid is a substance that only slightly dissociates in water to give H⁺ ions — only a small proportion of molecules break up. Example: ethanoic acid (CH₃COOH ⇌ CH₃COO⁻ + H⁺; most molecules remain undissociated in solution)."
      }
     ],
     "chem12": [
      {
       "type": "short",
       "marks": 2,
       "prompt": "Distinguish between qualitative analysis and quantitative analysis. Give one example of each.",
       "model": "Qualitative analysis: identifying the presence of substances without finding the quantities present. Example: testing for anions (e.g. Experiment 5.1 testing for sulfate ions). Quantitative analysis: finding the quantities or amounts of materials present. Example: determining the concentration of ethanoic acid in vinegar by volumetric analysis."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "Distinguish between a solute and a solvent. Identify the solute and solvent in a saltwater solution.",
       "model": "Solute: the substance that dissolves in a solvent; usually present in smaller amount. Solvent: the substance that dissolves the solute; usually present in larger amount. In saltwater: the solute is sodium chloride (NaCl) and the solvent is water (H₂O)."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Explain the difference between % w/w, % w/v, and % v/v as methods of expressing concentration. Give one example of each.",
       "model": "% w/w (weight per weight): (mass of solute / total mass of solution) × 100. Example: a 10% w/w NaCl solution contains 10 g NaCl per 100 g solution. % w/v (weight per volume): (mass of solute / total volume of solution) × 100. Example: a 10% w/v NaCl solution contains 10 g NaCl per 100 cm³ solution. % v/v (volume per volume): (volume of solute / total volume of solution) × 100. Example: a 10% v/v ethanol solution contains 10 cm³ ethanol per 100 cm³ solution. Alcohol in drinks is expressed as % v/v."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "What is meant by ppm? A chemist reports the concentration of fluoride in drinking water as 1 ppm. Express this in mg/L.",
       "model": "ppm = parts per million. It is a unit of concentration used for very dilute solutions. 1 ppm = 1 mg per litre of solution (for water, density 1 g/cm³). Therefore, 1 ppm fluoride = 1 mg/L."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Define molarity. Calculate the molarity of a solution containing 4.0 g of NaOH dissolved in 500 cm³ of solution. (H = 1, O = 16, Na = 23)",
       "model": "Molarity = the number of moles of solute per litre of solution; symbol M or mol/L. M_r of NaOH = 23 + 16 + 1 = 40. Moles of NaOH = 4.0 / 40 = 0.1 mol. This is dissolved in 500 cm³ = 0.5 litre. Molarity = 0.1 / 0.5 = 0.2 M (0.2 mol/L)."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "State six criteria that a substance must satisfy to be classified as a primary standard.",
       "model": "(1) Available in a highly pure state. (2) Stable in air — does not effloresce (lose water of crystallisation) or absorb water from the air (deliquesce or be hygroscopic). (3) Dissolves easily in water. (4) Has a fairly high relative molecular mass to minimise the percentage error in weighing. (5) Undergoes complete and rapid reaction when used in volumetric analysis. (6) If possible, should not be hydrated (i.e. should be anhydrous, with no water of crystallisation)."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain why sodium hydroxide (NaOH) cannot be used as a primary standard. Describe how you would prepare an approximately 0.1 M solution of NaOH.",
       "model": "NaOH cannot be used as a primary standard because it is deliquescent — it absorbs enough water vapour from the air to dissolve and form a solution. This means the exact mass of NaOH present cannot be known, so an accurately known concentration cannot be achieved by weighing alone. To prepare an approximately 0.1 M NaOH solution: weigh out approximately 1 g (0.1 mol × 40 g/mol = 4 g per litre → 1 g for 250 cm³) of NaOH, dissolve in deionised water, transfer to a 250 cm³ volumetric flask, make up to the graduation mark with deionised water, and invert about 20 times to mix. The concentration must then be standardised by titrating against a standard acid."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Describe the procedure for preparing a standard solution of sodium carbonate. State three important precautions.",
       "model": "Procedure: (1) Accurately weigh out a known mass of anhydrous sodium carbonate (Na₂CO₃) on a clock glass using a laboratory balance. (2) Transfer the Na₂CO₃ to a beaker containing a small amount of deionised water. (3) Stir with a glass rod until completely dissolved. (4) Use a wash bottle of deionised water to wash all traces of Na₂CO₃ from the clock glass into the beaker. (5) Transfer the solution to a 250 cm³ volumetric flask using a funnel and glass rod. (6) Wash all traces from the beaker, rod, and funnel into the flask. (7) Add deionised water slowly until the bottom of the meniscus is exactly at the graduation mark, viewed at eye level. (8) Stopper the flask and invert about 20 times to mix. Three precautions: (1) Use deionised water (not tap water, which contains dissolved substances). (2) Add water until the bottom of the meniscus is exactly level with the graduation mark at eye level. (3) Invert the flask (do not just shake) to ensure a homogeneous mixture."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define titration, equivalence point, and end point. Explain why the acid is usually placed in the burette (AABB rule).",
       "model": "Titration: a laboratory procedure where a measured volume of one solution is added to a known volume of another solution until the reaction is complete. Equivalence point: the stage in a titration when the two solutions have just reacted completely with each other. End point: the point at which the equivalence point is shown by a change in indicator colour. AABB rule (Acid Above, Base Below): acid is placed in the burette, base in the conical flask. Reasons: (1) Common bases such as NaOH are deliquescent and attack glass — NaOH can cause glass burette taps to stick (seize up). (2) NaOH also absorbs CO₂ from the air, forming a crust of Na₂CO₃ on the tap, which causes it to seize up further. Both problems are especially severe with plastic taps on modern burettes."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe how you would standardise a solution of hydrochloric acid using a standard sodium carbonate solution. Include the equation, indicator, and key observations.",
       "model": "Equation: Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂. Indicator: methyl orange. Procedure: (1) Rinse the pipette with the sodium carbonate solution. (2) Pipette 25 cm³ of the standard Na₂CO₃ solution into a conical flask. (3) Add a few drops of methyl orange indicator. (4) Rinse the burette with the dilute HCl; fill to the zero mark; remove the funnel; adjust meniscus to zero. (5) Place the conical flask on a white tile. (6) Carry out one rough titration and two accurate titrations agreeing to within 0.1 cm³. Observation: the methyl orange changes from yellow to red (pink) at the end point. Explanation: the indicator changes colour because the solution in the conical flask becomes acidic as all the base has been neutralised. Calculation: use the titre and the titration formula (V_a × M_a / n_a = V_b × M_b / n_b) to find the molarity of HCl."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "In a titration, 25 cm³ of a sodium hydroxide solution was titrated against 0.2 M hydrochloric acid. The average titration figure was 23.5 cm³. Calculate the concentration of the NaOH solution in (a) moles per litre and (b) grams per litre. (H = 1, O = 16, Na = 23)",
       "model": "Equation: HCl + NaOH → NaCl + H₂O; n_a = 1, n_b = 1. Using V_a × M_a / n_a = V_b × M_b / n_b: (23.5 × 0.2) / 1 = (25 × M_b) / 1. M_b = (23.5 × 0.2) / 25 = 4.7 / 25 = 0.188 mol/L. (b) M_r of NaOH = 40. Concentration in g/L = 0.188 × 40 = 7.52 g/L."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Using HIn ⇌ H+ + In−, explain how an acid-base indicator changes colour during a titration.",
       "model": "HIn and In− have different colours. Added acid increases H+, shifting equilibrium left towards HIn; added base removes H+, shifting it right towards In− by Le Châtelier's principle. The observed transition occurs over the pH range where the ratio changes substantially, so an indicator must match the titration's steep pH change."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Describe the experiment to determine the concentration of ethanoic acid (acetic acid) in vinegar using sodium hydroxide. Explain why the vinegar is diluted and why phenolphthalein is used.",
       "model": "Equation: CH₃COOH + NaOH → CH₃COONa + H₂O (weak acid–strong base). Dilution: because vinegar is much more concentrated than the NaOH solution (~0.1 M), a very small volume of NaOH would be needed without dilution — this would give a large percentage error. The vinegar is diluted by a factor of 5: pipette 2 × 25 cm³ samples of vinegar into a 250 cm³ volumetric flask and make up to the mark with deionised water. Indicator: phenolphthalein is used because this is a weak acid–strong base titration. Phenolphthalein is pink in the alkaline NaOH in the conical flask. Procedure: 25 cm³ of standard NaOH solution is pipetted into the conical flask; phenolphthalein added (turns pink); diluted vinegar is titrated from the burette. End point: phenolphthalein changes from pink to colourless. Calculation: calculate the concentration of CH₃COOH in the diluted vinegar (in mol/L and g/L), then multiply by 5 (the dilution factor) to get the concentration in the original vinegar; express as % w/v."
      }
     ],
     "chem13": [
      {
       "type": "short",
       "marks": 2,
       "prompt": "Distinguish between accuracy and precision. Give one example of each in the context of volumetric analysis.",
       "model": "Accuracy: how close a measurement is to the correct (true or actual) value. Example: if the correct titration figure is 23.0 cm³ and a student gets 23.1 cm³, the result is accurate. Precision: how close a set of repeated measurements are to each other (consistency). Example: if a student's three titration results are 23.5, 23.6, and 23.7 cm³, the results are precise (close to each other) even though they are not accurate (different from the correct value of 23.0 cm³)."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "A student washed the burette with deionised water before a titration but forgot to rinse it with the acid solution. Explain how this error affects (a) the accuracy and (b) the precision of the results.",
       "model": "(a) Accuracy: this error affects accuracy. The water remaining in the burette dilutes the acid solution placed in the burette. As a result, the solution is less concentrated than intended, so a larger volume of acid is needed to reach the end point. The titration figure obtained is too large, giving an inaccurate (too low) calculated concentration of the acid. (b) Precision: this error does not affect precision. Although the results are inaccurate, all three titrations will still give similar (close) results — the error is consistent. Therefore, the results are precise (close to each other) but not accurate."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "State five precautions a student should take to ensure accurate results when performing an acid-base titration.",
       "model": "(1) Only use equipment manufactured to a high degree of accuracy in measuring volumes, such as the burette, pipette, and volumetric flask — not graduated cylinders or beakers. (2) Take all volume readings at eye level to avoid parallax errors; always read where the bottom of the meniscus touches the graduation mark. (3) Rinse glassware correctly: rinse the pipette and burette first with deionised water, then with the solutions they are to contain. (4) As you near the end point, add the solution drop-by-drop from the burette to avoid overshooting and obtain an accurate end point. (5) When measuring unknown concentrations, always use standard solutions — solutions of accurately known concentration."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "State the four key formulas used in solving volumetric analysis problems.",
       "model": "(1) Number of moles = Mass (g) / Relative Molecular Mass. (2) Number of moles = (volume in cm³ × molarity) / 1000. (3) (V_a × M_a) / n_a = (V_b × M_b) / n_b, where V = volume (cm³), M = molarity (mol/L), n = moles from balanced equation. (4) Density = Mass / Volume."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "In an experiment, 25 cm³ of a sample of vinegar were diluted to 250 cm³ in a volumetric flask. The diluted solution was titrated against a sodium hydroxide solution prepared by dissolving 1.20 g of NaOH in 500 cm³ of solution. On average, 18.75 cm³ of the diluted vinegar were required to neutralise 25.0 cm³ of the NaOH solution. The equation for the reaction is: CH₃COOH + NaOH → CH₃COONa + H₂O. Calculate the concentration of ethanoic acid in the original vinegar in (a) moles per litre, (b) grams per litre, and (c) % w/v. (H = 1.008, C = 12.01, O = 16.00, Na = 22.99)",
       "model": "Step 1 — find molarity of NaOH: M_r NaOH = 22.99 + 16.00 + 1.008 = 40.00. Moles NaOH = 1.20 / 40.00 = 0.03 mol. 0.03 mol in 500 cm³ → 0.06 mol in 1000 cm³ → [NaOH] = 0.06 M. Step 2 — use Formula 3 (n_a = n_b = 1): (18.75 × M_a) / 1 = (25 × 0.06) / 1 → M_a = (25 × 0.06) / 18.75 = 1.5 / 18.75 = 0.08 M (diluted vinegar). Step 3 — dilution factor = 250 / 25 = 10. Concentration in original vinegar = 0.08 × 10 = (a) 0.80 mol/L. Step 4 — M_r CH₃COOH = (2 × 12.01) + (2 × 16.00) + (4 × 1.008) = 24.02 + 32.00 + 4.032 = 60.05. (b) g/L = 0.80 × 60.05 = 48.04 g/L. Step 5 — (c) % w/v = 48.04 g/L = 4.804 g/100 cm³ = 4.80% w/v."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "In a titration to determine the concentration of ethanoic acid in vinegar: 10.0 cm³ of the original vinegar was diluted to 50.0 cm³. On average, 12.4 cm³ of the diluted vinegar was required to neutralise 25.0 cm³ of 0.09 M NaOH. (i) Name a suitable indicator and state the colour change at the end point. (ii) Calculate the volume of undiluted vinegar that would be required to neutralise 25.0 cm³ of the NaOH solution. (iii) Calculate the concentration of ethanoic acid in the original vinegar in moles per litre.",
       "model": "(i) Indicator: phenolphthalein. Colour change at end point: from pink to colourless. (ii) Dilution factor = 50 / 10 = 5. Therefore, 12.4 / 5 = 2.48 cm³ of undiluted vinegar would be required to neutralise 25.0 cm³ NaOH. (iii) Using formula 3 (CH₃COOH + NaOH → CH₃COONa + H₂O; n_a = n_b = 1): (12.4 × M_a) / 1 = (25 × 0.09) / 1 → M_a = (25 × 0.09) / 12.4 = 2.25 / 12.4 = 0.1815 M (diluted vinegar). Concentration in original vinegar = 0.1815 × 5 = 0.91 mol/L."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "Explain why it is necessary to dilute vinegar before carrying out a titration with sodium hydroxide solution.",
       "model": "Vinegar contains a much higher concentration of ethanoic acid than the sodium hydroxide solution used (approximately 0.1 M). If the vinegar was not diluted, only a very small volume (e.g. 2–3 cm³) would be needed to neutralise 25 cm³ of NaOH. Such a small volume gives a very large percentage error, since even a slight misreading of the volume will have a greater impact on the result. Diluting the vinegar increases the volume required in the titration, making the percentage error smaller and the final result more accurate."
      }
     ],
     "chem14": [
      {
       "type": "short",
       "marks": 2,
       "prompt": "Define oxidation and reduction (a) in terms of oxygen and (b) in terms of electron transfer.",
       "model": "(a) In terms of oxygen: oxidation = the addition of oxygen to a substance; reduction = the removal of oxygen from a substance (or the addition of hydrogen). (b) In terms of electron transfer: oxidation = the loss of electrons; reduction = the gain of electrons. Memory aid: OIL RIG — Oxidation Is Loss, Reduction Is Gain."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "Define oxidising agent and reducing agent. State which is always oxidised and which is always reduced.",
       "model": "Oxidising agent = a substance that brings about oxidation in other substances. The oxidising agent is itself always reduced (it accepts electrons). Reducing agent = a substance that brings about reduction in other substances. The reducing agent is itself always oxidised (it donates electrons). Rule: the oxidising agent is reduced; the reducing agent is oxidised."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "In the reaction Zn + CuSO₄ → ZnSO₄ + Cu: (a) which species is oxidised and which is reduced? (b) identify the oxidising agent and the reducing agent.",
       "model": "(a) Zn is oxidised: its oxidation number increases from 0 to +2 (it loses 2 electrons). Cu²⁺ is reduced: its oxidation number decreases from +2 to 0 (it gains 2 electrons). (b) The oxidising agent is CuSO₄ (the Cu²⁺ ion) — it causes oxidation of Zn and is itself reduced. The reducing agent is Zn — it causes reduction of Cu²⁺ and is itself oxidised."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Explain why oxidation and reduction must always occur together. Use the reaction 2Na + Cl₂ → 2NaCl to illustrate your answer.",
       "model": "Oxidation and reduction must always occur together because if one substance loses electrons (is oxidised), there must be some other substance to accept (gain) those electrons (is reduced). The electrons cannot simply disappear. This is like a transfer of money: if one person gives money, another must receive it. In 2Na + Cl₂ → 2NaCl: Na loses one electron (0 → +1) → OXIDATION; Cl gains one electron (0 → -1) → REDUCTION. Note that neither oxygen nor hydrogen is present — this reaction demonstrates why the electron transfer definition is broader than the oxygen-based definition."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Name four common oxidising agents and state one use for each.",
       "model": "(1) Hydrogen peroxide (H₂O₂): used to bleach hair — oxidises the coloured pigment to a colourless form. (2) Iodine (I₂): used in tincture of iodine to prevent infection of cuts — kills germs by oxidation. (3) Chlorine gas (Cl₂): used to treat drinking water to make it safe — kills bacteria by oxidation. (4) Sodium hypochlorite (NaOCl): used as household bleach to remove colour from fabrics — the hypochlorite ion (ClO⁻) oxidises the dye pigment to a colourless form."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "State the rules used to assign oxidation numbers. Assign oxidation numbers to all elements in CuSO₄.",
       "model": "Key rules: (1) Uncombined element = 0. (2) Ion = same as its charge. (3) Sum in compound = 0. (4) O = -2 (exceptions: peroxides O = -1, OF₂ O = +2). (5) H = +1 (except metal hydrides, H = -1). (6) Halogens = -1 unless bonded to a more electronegative element. (8) Sum in polyatomic ion = ion's charge. For CuSO₄: the sulfate ion SO₄²⁻ has a charge of -2 (by Rule 2 applied to ions). Therefore Cu must be +2 to balance the overall compound to zero (Rule 3). Within SO₄²⁻: O = -2, four oxygens = -8; total charge = -2; so S + (-8) = -2 → S = +6. Answer: Cu = +2, S = +6, O = -2."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Calculate the oxidation number of (a) Mn in KMnO₄ and (b) Cr in K₂Cr₂O₇. State the systematic name for each compound.",
       "model": "(a) KMnO₄: K = +1, O = -2. Sum must = 0: (+1) + Mn + 4(-2) = 0 → Mn = +8 - 1 = +7. Systematic name: potassium manganate(VII). Common name: potassium permanganate. (b) K₂Cr₂O₇: K = +1, O = -2. Sum must = 0: 2(+1) + 2Cr + 7(-2) = 0 → 2 + 2Cr - 14 = 0 → 2Cr = 12 → Cr = +6. Systematic name: potassium dichromate(VI)."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Using oxidation numbers, balance the following equation: MnO₄⁻ + Fe²⁺ + H⁺ → Mn²⁺ + Fe³⁺ + H₂O. Identify the oxidising agent and reducing agent.",
       "model": "Step 1: Assign oxidation numbers. Mn = +7 in MnO₄⁻; Mn = +2 in Mn²⁺. Fe = +2 in Fe²⁺; Fe = +3 in Fe³⁺. Step 2: Changes: Mn and Fe change oxidation number. Step 3: Mn: +7 → +2, gains 5 electrons. Fe: +2 → +3, loses 1 electron. Step 4: To equalise, need 5 Fe²⁺ per 1 MnO₄⁻ (5 × 1e⁻ lost = 5e⁻ gained by Mn). Write: MnO₄⁻ + 5Fe²⁺ + H⁺ → Mn²⁺ + 5Fe³⁺ + H₂O. Step 5: Balance O (4 on LHS → need 4H₂O on RHS) and H (4H₂O = 8H → need 8H⁺ on LHS): MnO₄⁻ + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O. Check atoms: Mn 1/1, Fe 5/5, O 4/4, H 8/8 ✓. Check charges: LHS = -1 + 10 + 8 = +17; RHS = +2 + 15 = +17 ✓. Oxidising agent: MnO₄⁻ (Mn is reduced from +7 to +2). Reducing agent: Fe²⁺ (Fe is oxidised from +2 to +3)."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Design a displacement investigation to place magnesium, zinc and copper in order of reducing strength.",
       "model": "Place cleaned equal-sized metal samples into equal volumes and concentrations of the other metal-ion solutions under the same conditions. Record coating, colour or temperature evidence and use ionic equations. A metal that displaces another ion is the stronger reducing agent. Expected order is magnesium, zinc, copper; include repeats, eye protection and safe disposal."
      }
     ],
     "chem15": [
      {
       "type": "short",
       "marks": 3,
       "prompt": "State four properties of potassium permanganate (KMnO₄) relevant to its use in volumetric analysis.",
       "model": "(1) KMnO₄ is a purple-coloured solid and a strong oxidising agent. (2) It is NOT a primary standard: it cannot be obtained in a highly pure state and it is unstable — it decomposes in the presence of sunlight and heat, causing the concentration of its solutions to vary over time. (3) It must therefore be standardised by titration against a primary standard solution before use. (4) It acts as its own indicator (self-indicating): it is colourless in acidic solution after reaction, and a permanent faint pink colour at the end point indicates excess KMnO₄. (5) Because of its intense purple colour, the top of the meniscus is read (not the bottom)."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Write the half-equation for the reduction of MnO₄⁻ in acidic solution. State why H₂SO₄ is used to acidify the solution (and not HCl or HNO₃).",
       "model": "Half-equation: MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O (purple → colourless). H₂SO₄ is used to supply the H⁺ ions required for this reaction to take place. HCl cannot be used because the Cl⁻ ions would be oxidised to Cl₂ by the KMnO₄, interfering with the titration. HNO₃ cannot be used because it is itself a strong oxidising agent, which would also interfere with the titration."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "What is observed if insufficient acid is added to the conical flask in a KMnO₄/Fe²⁺ titration? Explain why.",
       "model": "Observation: a brown precipitate (solid) forms in the conical flask. Explanation: without sufficient H⁺ ions, the reaction MnO₄⁻ + 2H₂O + 3e⁻ → MnO₂↓ + 4OH⁻ takes place instead. This produces manganese dioxide (MnO₂), a brown solid precipitate. Mn changes from +7 (purple) to +4 (brown solid). The addition of excess sulfuric acid ensures sufficient H⁺ ions are present for the acidic half-reaction (MnO₄⁻ → Mn²⁺) to proceed correctly."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Explain why anhydrous FeSO₄ cannot be used as a primary standard for Fe²⁺ ions. What substance is used instead? Give its formula and explain why it is suitable.",
       "model": "Anhydrous FeSO₄ cannot be used as a primary standard because it is hygroscopic — it absorbs moisture from the air. This means the mass of FeSO₄ cannot be accurately known by weighing. Instead, ammonium iron(II) sulfate (also called ferrous ammonium sulfate) is used. Formula: (NH₄)₂SO₄·FeSO₄·6H₂O. It is suitable as a primary standard because: (1) it can be obtained in a highly pure state; (2) it is not affected by air; (3) it does not spontaneously lose its water of crystallisation (not efflorescent); (4) it has a high relative molecular mass (392.17), which minimises the percentage error in weighing."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "Explain why ammonium iron(II) sulfate must be dissolved in dilute sulfuric acid rather than deionised water.",
       "model": "Ammonium iron(II) sulfate must be dissolved in dilute sulfuric acid because the sulfuric acid prevents the Fe²⁺ ions from being oxidised to Fe³⁺ ions by oxygen in the air. Fe²⁺ ions are more stable in acidic solution, and this makes them less likely to react with dissolved oxygen. If deionised water were used instead, some of the Fe²⁺ would be oxidised to Fe³⁺ before the titration took place, giving an inaccurate result."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Distinguish between efflorescence, deliquescence, and hygroscopic. Give one example of each.",
       "model": "Efflorescence: the spontaneous loss of water of crystallisation from a hydrated crystalline salt to the surrounding air, without requiring heating. Example: CuSO₄·5H₂O (blue crystals lose water and turn white). Deliquescence: the spontaneous process by which a substance absorbs moisture from the atmosphere to the extent that it dissolves into a liquid solution. Example: NaOH (pellets absorb water vapour until a solution forms on the surface). Hygroscopic: a substance that spontaneously absorbs moisture from the surrounding air but does not dissolve into a liquid solution. Example: anhydrous FeSO₄ (absorbs water from the air to form the hydrated salt FeSO₄·7H₂O)."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe the end point in (a) a KMnO₄/Fe²⁺ titration and (b) an iodine/thiosulfate titration. Explain how each end point is detected.",
       "model": "(a) KMnO₄/Fe²⁺ titration: KMnO₄ acts as its own indicator (self-indicating). As long as Fe²⁺ ions are present in the conical flask, each drop of KMnO₄ added immediately becomes colourless (Mn²⁺ is colourless). When all the Fe²⁺ has been oxidised, the next single drop of KMnO₄ gives a faint permanent pink colour. This is the end point. (b) Iodine/thiosulfate titration: starch is used as the indicator. As Na₂S₂O₃ is added to I₂ solution, the reddish-brown colour of iodine fades to pale yellow. At this point, a few drops of starch solution are added — the solution turns blue-black (starch–iodine complex). The titration is continued drop by drop until the blue-black colour disappears. This colourless end point indicates all the iodine has reacted."
      },
      {
       "type": "short",
       "marks": 2,
       "prompt": "Why is starch indicator added only when the iodine solution is pale yellow, and not at the beginning of the titration?",
       "model": "Starch should not be added at the beginning of the titration because when a large amount of iodine is present, the iodine would be strongly adsorbed onto the starch. This adsorbed iodine would desorb slowly and react slowly with the thiosulfate, making it very difficult to detect an accurate end point. By waiting until the solution is pale yellow (i.e. most of the iodine has already reacted), the starch is only exposed to a very small amount of iodine when added. This gives a sharp, accurate colour change from blue-black to colourless at the end point."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "In the iodine/thiosulfate experiment, why is excess potassium iodide (KI) added to the conical flask? Give two reasons.",
       "model": "Two reasons for adding excess KI: (1) To ensure that all of the KMnO₄ (potassium permanganate) reacts completely with the I⁻ ions to produce the corresponding maximum number of moles of I₂ according to: 2MnO₄⁻ + 10I⁻ + 16H⁺ → 2Mn²⁺ + 5I₂ + 8H₂O. (2) To keep the iodine produced in solution. Iodine (I₂) is non-polar and is only sparingly soluble in water. However, in KI solution, the I₂ molecule reacts with the iodide ion to form the tri-iodide ion (I₃⁻): I₂ + I⁻ → I₃⁻. Since I₃⁻ is a charged ion, it dissolves easily in water, keeping the iodine in solution."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "25 cm³ of a 0.02 M KMnO₄ solution was pipetted into a conical flask. Some dilute H₂SO₄ was added and then excess KI was added. The liberated iodine was titrated against a sodium thiosulfate solution. The average titration figure was 18.7 cm³. Calculate the concentration of the sodium thiosulfate solution in (a) moles per litre and (b) grams per litre of crystalline Na₂S₂O₃·5H₂O. (Na = 23, S = 32, O = 16, H = 1.008)",
       "model": "Equations: 2MnO₄⁻ + 10I⁻ + 16H⁺ → 2Mn²⁺ + 5I₂ + 8H₂O; I₂ + 2S₂O₃²⁻ → S₄O₆²⁻ + 2I⁻. Combined: 2 moles MnO₄⁻ → 5 moles I₂ → 10 moles S₂O₃²⁻. Therefore n_ox = 2, n_red = 10. Using (V_ox × M_ox)/n_ox = (V_red × M_red)/n_red: (25 × 0.02)/2 = (18.7 × M_red)/10. 0.25 = (18.7 × M_red)/10. M_red = (0.25 × 10)/18.7 = 2.5/18.7 = 0.1337 mol/L. (b) M_r of Na₂S₂O₃·5H₂O: 2(23) + 2(32) + 3(16) + 5(18.016) = 46 + 64 + 48 + 80 = 238 → using M_r = 248.2 (from 2×23 + 2×32.07 + 3×16 + 10×1.008 + 5×16 = 248.2): g/L = 0.1337 × 248.2 = 33.18 g/L."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Outline how a redox titration could determine the percentage by mass of elemental iron in an iron tablet.",
       "model": "Accurately weigh and dissolve a tablet, ensuring iron is in the required oxidation state, and make to a known volume. Pipette an aliquot and titrate with standard oxidant to the specified endpoint, obtaining concordant titres. Use the balanced redox equation to find moles of iron in the aliquot, scale to the tablet, convert to mass and calculate percentage."
      }
     ],
     "chem16": [
      {
       "type": "short",
       "marks": 2,
       "prompt": "Define systematic error and random error. State one key difference between them.",
       "model": "Systematic error: a consistent, repeating error that always occurs in one direction — i.e. the measured value is always higher or always lower than the true value. Random error: an unpredictable fluctuation in a measurement around the true value, occurring due to variations in experimental conditions and procedures. Key difference: a systematic error always shifts results in ONE direction and cannot be reduced by repeating trials; a random error causes results to fluctuate in BOTH directions and can be reduced by repeating measurements and averaging results."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "A student carries out a titration three times and gets 22.1 cm³, 22.1 cm³, and 22.1 cm³. The true end point is 22.5 cm³. (a) Is there evidence of a systematic error? (b) Is there evidence of a random error? Justify both answers.",
       "model": "(a) Yes, there is evidence of a systematic error. All three titration values (22.1 cm³) are consistently lower than the true end point (22.5 cm³). The results are shifted in one direction (always too low), which is the defining characteristic of a systematic error. (b) No, there is no evidence of a random error. All three results agree with each other to within 0.1 cm³ — they are precise (clustered together). Random errors cause results to fluctuate in both directions; since all three results are identical, there is no evidence of random variation."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "State two causes of systematic errors in volumetric analysis. For each cause, state the direction of the effect on the titration figure.",
       "model": "(1) Using the wrong indicator: the end point is always detected too early or too late (depending on the indicator's pH range), so the titration figure is consistently too small or too large (always shifted in one direction). (2) Rinsing the burette only with deionised water (not with the acid it contains): the water remaining in the burette dilutes the acid solution. A greater volume of diluted acid is needed to reach the end point, so the titration figure is consistently too large. Both of these errors are systematic because they always affect the results in the same specific direction."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Give three examples of random errors that could occur during a titration. Explain how random errors differ from systematic errors in their effect on results.",
       "model": "Three examples of random errors in a titration: (1) Uneven shaking of the conical flask between trials — if shaken vigorously in one trial and gently in another, the ease of detecting the colour change at the end point may vary, giving inconsistently high or low results. (2) Varying the number of drops of indicator added in each trial — acid-base indicators are weak acids/bases; using different amounts changes the pH at which the colour change occurs, causing the titration figure to vary unpredictably. (3) Inconsistently reading the meniscus in the burette — if the volume is read at eye level in one trial, from above in another, and from below in a third, the readings fluctuate randomly. Difference from systematic errors: random errors cause results to fluctuate in both directions (some too high, some too low) and can be reduced by repeating and averaging; systematic errors always shift results in ONE direction and cannot be fixed by repeating."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "9.31 g of ammonium iron(II) sulfate, (NH₄)₂SO₄·FeSO₄·6H₂O, was dissolved in dilute sulfuric acid and made up to 250 cm³ of solution. 25.0 cm³ portions of this solution were titrated against a potassium permanganate solution. The average titration figure was 22.6 cm³. The equation is: MnO₄⁻ + 8H⁺ + 5Fe²⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O. Calculate the concentration of KMnO₄ in (a) moles per litre and (b) grams per litre. (M_r of (NH₄)₂SO₄·FeSO₄·6H₂O = 392.17; M_r of KMnO₄ = 158.04)",
       "model": "Step 1: Find molarity of ammonium iron(II) sulfate. Moles = 9.31 / 392.17 = 0.02374 mol in 250 cm³. In 1 litre: 0.02374 × 4 = 0.0950 M. Step 2: Using Formula 3 (n_ox = 1, n_red = 5): (22.6 × M_ox)/1 = (25 × 0.0950)/5. 22.6 × M_ox = 0.475. M_ox = 0.475/22.6 = 0.0210 M. (a) Concentration of KMnO₄ = 0.021 mol/L. (b) g/L = 0.021 × 158.04 = 3.32 g/L."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Explain how a systematic error arises from incorrect rinsing of (a) the burette and (b) the conical flask in a titration.",
       "model": "(a) Burette rinsed only with deionised water: water remaining in the burette dilutes the solution (acid) placed in the burette. Because the acid is more dilute than intended, a greater volume of acid is needed to neutralise the base in the conical flask. This gives a titration figure that is consistently too large — a systematic error in one direction. (b) Conical flask rinsed with the solution it is to contain: this leaves additional moles of the solution (usually base) in the conical flask beyond the 25 cm³ pipetted in. More moles of base are present, so a greater volume of acid from the burette is needed to neutralise it. This gives a titration figure that is consistently too large — again a systematic error in one direction."
      }
     ],
     "chem17": [
      {
       "type": "short",
       "marks": 2,
       "prompt": "Define the term rate of reaction. State one method by which the rate of a reaction can be measured in the laboratory.",
       "model": "The rate of reaction is defined as the change in concentration per unit time of any one reactant or product. One method: measure the volume of gas produced at regular time intervals using an inverted graduated cylinder filled with water. The volume produced per unit time gives the rate."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Give two reasons, using collision theory, why the rate of a reaction increases when temperature is raised. State which reason is more significant and why.",
       "model": "Reason 1: At higher temperature, molecules have more kinetic energy and move faster, so there are more collisions per second between reactant particles. Reason 2: At higher temperature, a greater fraction of molecules have energy greater than or equal to the activation energy, so there are more effective collisions. The more significant reason is (2) — the increase in the fraction of effective collisions. This is because, at higher temperatures, molecules with low energy still just bounce apart without reaction; only those that exceed Ea react. The rise in temperature greatly increases the proportion above Ea (the area under the Maxwell-Boltzmann curve above Ea increases dramatically), and this effect far exceeds the modest increase in collision frequency."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Describe an experiment to investigate the effect of concentration on the rate of reaction between sodium thiosulfate solution and hydrochloric acid. In your answer include: the reagents and concentrations used, the key steps in procedure, how the rate is determined, and what the results show.",
       "model": "Reaction: Na₂S₂O₃ + 2HCl → 2NaCl + SO₂ + S↓ + H₂O. Reagents: 0.2 M sodium thiosulfate (six concentrations: 0.20, 0.16, 0.12, 0.08, 0.04, 0.02 M) and dilute HCl. Procedure: (1) Pour 0.2 M Na₂S₂O₃ into a conical flask placed on white paper with a cross drawn on it. (2) Quickly add a fixed volume of HCl; start stopwatch immediately. (3) Observe the cross through the mixture from above. (4) Stop the stopwatch when the creamy yellow sulfur precipitate makes the cross invisible. (5) Record the time. (6) Repeat with decreasing concentrations of Na₂S₂O₃, keeping HCl concentration and volume constant. Rate determination: rate = 1/time for each run. Results: the more concentrated the Na₂S₂O₃, the shorter the time, i.e. the higher the rate. A graph of rate (1/t) versus concentration gives a straight line through the origin, showing rate is directly proportional to concentration."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between homogeneous and heterogeneous catalysis. Give one example of each type and name the catalyst in each case.",
       "model": "Homogeneous catalysis: the catalyst and the reactants are in the same phase; there is no boundary between the catalyst and the reactants. Example: the decomposition of hydrogen peroxide catalysed by potassium iodide solution — both H₂O₂ and KI are in aqueous solution (same phase). Catalyst: I⁻ ions. Heterogeneous catalysis: the catalyst and the reactants are in different phases; a physical boundary exists between them. Example: the decomposition of hydrogen peroxide catalysed by manganese dioxide — H₂O₂ is liquid and MnO₂ is solid (different phases). Catalyst: MnO₂."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Describe the function of a catalytic converter in a motor vehicle. Include: the catalysts used, one chemical equation for a reaction that takes place, and two ways in which the catalyst may be poisoned.",
       "model": "Function: a catalytic converter is fitted to the exhaust system of a vehicle to convert harmful exhaust gases (CO, NOₓ, unburned hydrocarbons) into less harmful substances (CO₂, N₂, H₂O). Catalysts: platinum (Pt), palladium (Pd), and rhodium (Rh) coated on a ceramic honeycomb structure inside a stainless steel case. The honeycomb provides a very large surface area for catalysis. This is an example of heterogeneous catalysis (solid catalysts, gaseous reactants). Chemical equation: 2CO + 2NO →(Pt/Pd/Rh) 2CO₂ + N₂. Two ways the catalyst may be poisoned: (1) Sulfur compounds in fuels can coat the catalyst surface and block the active sites. (2) Phosphorus compounds (entering if the engine burns oil) can permanently bind to the catalyst surface, blocking active sites. Note: lead compounds in leaded petrol were historically a major cause of poisoning; this is why unleaded petrol was introduced."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Draw and label a reaction profile diagram for an exothermic reaction (a) without a catalyst and (b) with a catalyst. On your diagrams, mark the activation energy (Ea) and the heat of reaction (ΔH).",
       "model": "Both diagrams have the y-axis labelled 'Energy' and x-axis labelled 'Progress of reaction (Time)'. (a) Without catalyst: reactants at a certain energy level; curve rises steeply to a peak (the activated complex); curve falls to products at a lower energy level than reactants. Ea = vertical distance from reactant energy level to the peak. ΔH = vertical distance from reactant level to product level (negative, since products are lower). (b) With catalyst: same reactant and product energy levels; the peak (activated complex) is lower — the catalyst provides an alternative reaction pathway with a lower activation energy. Ea(catalysed) < Ea(uncatalysed). ΔH is the same in both diagrams — the catalyst does not change the energy difference between reactants and products, only the energy barrier between them."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Describe the intermediate formation theory of catalysis. Illustrate your answer using the catalysis of the decomposition of hydrogen peroxide by iodide ions.",
       "model": "The intermediate formation theory (proposed by Arrhenius) states that the catalyst reacts with one of the reactants to form an intermediate compound. This intermediate then reacts with the second reactant (or decomposes) to give the products of the reaction AND regenerate the catalyst. The catalyst is therefore recovered at the end. Illustration — I⁻ catalysing 2H₂O₂ → 2H₂O + O₂: Step 1: H₂O₂ + I⁻ → H₂O + IO⁻ (the IO⁻ ion is the intermediate). Step 2: H₂O₂ + IO⁻ → H₂O + O₂ + I⁻ (catalyst I⁻ regenerated). Adding the two equations: 2H₂O₂ → 2H₂O + O₂ (I⁻ cancels out, unchanged). Evidence: the experiment with pink cobalt(II) chloride catalysing the oxidation of potassium sodium tartrate by H₂O₂. The solution turns green (the green colour is the intermediate compound) and then returns to pink, showing the Co²⁺ catalyst has been regenerated."
      }
     ],
     "chem18": [
      {
       "type": "short",
       "marks": 2,
       "prompt": "Define the term dynamic chemical equilibrium. Explain why the word 'dynamic' is used in this definition.",
       "model": "Dynamic chemical equilibrium is a state of dynamic balance in a reversible reaction where the rate of the forward reaction is equal to the rate of the backward reaction; the concentrations of all reactants and products remain constant. The word 'dynamic' is used because both the forward and backward reactions are still taking place (the system is not static) — the nitrogen and hydrogen are continuously forming ammonia while the ammonia is continuously decomposing back to form nitrogen and hydrogen. Even though overall concentrations appear unchanged, both reactions are occurring simultaneously."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Write the equilibrium constant expression (Kc) for the reaction N₂(g) + 3H₂(g) ⇌ 2NH₃(g). State the units of Kc for this reaction and explain why temperature is the only factor that affects the value of Kc.",
       "model": "Kc = [NH₃]² / ([N₂][H₂]³). Units: numerator = (mol/L)²; denominator = (mol/L)(mol/L)³ = (mol/L)⁴. Units of Kc = (mol/L)² / (mol/L)⁴ = (mol/L)⁻² = L²/mol². Temperature is the only factor that changes Kc because: concentration changes merely shift the position of equilibrium — the concentrations of all species change, but the ratio of products to reactants at the new equilibrium is the same (Kc is unchanged). Pressure changes (for gaseous reactions) shift concentrations but the ratio at the new equilibrium is unchanged. A catalyst speeds up both reactions equally and does not alter the equilibrium composition. Only temperature changes the actual energy balance between reactants and products, altering how far the reaction proceeds — i.e. changing the equilibrium ratio and therefore Kc."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "At 450°C, nitrogen gas and hydrogen gas were placed in a 1 litre container and allowed to reach equilibrium. At equilibrium: [N₂] = 13.6 mol/L, [H₂] = 1.0 mol/L, [NH₃] = 1.5 mol/L. (i) Write the Kc expression. (ii) Calculate the value of Kc at this temperature.",
       "model": "(i) N₂(g) + 3H₂(g) ⇌ 2NH₃(g). Kc = [NH₃]² / ([N₂][H₂]³). (ii) Since V = 1 L, concentrations equal molar amounts. Kc = (1.5)² / (13.6)(1.0)³ = 2.25 / 13.6 = 0.165. Answer: Kc = 0.165 L²/mol². (Note: the low value of Kc at 450°C indicates that at this temperature the equilibrium lies predominantly to the left — i.e. there is less ammonia than reactants at equilibrium.)"
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Phosphorus(V) chloride decomposes according to: PCl₅(g) ⇌ PCl₃(g) + Cl₂(g). A mass of 20.85 g of PCl₅ was placed in a closed 8 litre vessel at 523 K. At equilibrium, 80% of the PCl₅ had dissociated. (M_r of PCl₅ = 208.22.) Calculate the value of Kc.",
       "model": "Step 1: Find initial moles of PCl₅. Moles = 20.85 / 208.22 = 0.100 mol. Step 2: 80% dissociates → moles dissociated = 0.080 mol. At equilibrium: PCl₅ = 0.100 − 0.080 = 0.020 mol; PCl₃ = 0.080 mol; Cl₂ = 0.080 mol. Step 3: Divide by volume (8 L) to get concentrations. [PCl₅] = 0.020/8 = 0.0025 mol/L; [PCl₃] = 0.080/8 = 0.010 mol/L; [Cl₂] = 0.080/8 = 0.010 mol/L. Step 4: Kc = [PCl₃][Cl₂] / [PCl₅] = (0.010)(0.010) / 0.0025 = 0.0001 / 0.0025 = 0.04. Answer: Kc = 0.04 mol/L."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "State Le Chatelier's Principle. For the reaction 2NO₂(g) ⇌ N₂O₄(g) ΔH = −58.1 kJ/mol, predict and explain the effect on the equilibrium position of: (i) increasing the pressure, (ii) increasing the temperature, (iii) adding a catalyst.",
       "model": "Le Chatelier's Principle: if a stress is applied to a system at equilibrium, the system readjusts to relieve the stress applied. (i) Increasing pressure: equilibrium shifts to the RIGHT. There are 2 moles of gas on the left and 1 mole on the right. Increasing pressure favours the side with fewer moles of gas (the right side), which occupies a smaller volume, relieving the pressure. More N₂O₄ is produced. (ii) Increasing temperature: equilibrium shifts to the LEFT. The forward reaction is exothermic (ΔH = −58.1 kJ/mol), so the backward reaction is endothermic. Increasing temperature constitutes adding heat; the equilibrium shifts in the direction that absorbs the extra heat — i.e. the backward (endothermic) direction. More NO₂ is produced; the brown colour intensifies; the value of Kc decreases. (iii) Adding a catalyst: no effect on the position of equilibrium. A catalyst increases the rate of both forward and backward reactions equally. It helps the system reach equilibrium faster but does not change the ratio of concentrations at equilibrium, so neither the equilibrium position nor the value of Kc is affected."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "State the best conditions for the industrial manufacture of ammonia by the Haber Process. For each condition, explain using Le Chatelier's Principle why that condition is used, and state any compromise that must be made.",
       "model": "Reaction: N₂(g) + 3H₂(g) ⇌ 2NH₃(g) ΔH = −92.4 kJ/mol. N₂ obtained from air; H₂ from natural gas. (1) Pressure: High pressure is used. Le Chatelier's Principle: there are 4 moles of gas on the left and 2 moles on the right; high pressure shifts equilibrium to the right (smaller volume), producing more ammonia. Compromise: a very high pressure plant is expensive to build and maintain, and there is danger of gas leaks and explosions at very high pressures. A compromise pressure of approximately 200 atmospheres is used — giving a good yield while keeping costs and safety risks manageable. (2) Temperature: Low temperature favours ammonia production (exothermic forward reaction — Le Chatelier predicts equilibrium shifts right at low temperature, Kc is larger). However, at low temperature the reaction is too slow to be economically viable. A compromise temperature of approximately 500°C is used — rate is fast enough while still giving a satisfactory yield. (3) Catalyst: iron (Fe) catalyst is used. A catalyst does not change the equilibrium position or Kc, but it speeds up both reactions equally, allowing the system to reach equilibrium faster. This makes the process economically viable at 500°C."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Describe Experiment 18.1 used to investigate the effect of changes in concentration on the equilibrium between iron(III) chloride and potassium thiocyanate.",
       "model": "Reaction: Fe³⁺(aq) + CNS⁻(aq) ⇌ Fe(CNS)²⁺(aq). Fe³⁺ ions are yellow; CNS⁻ ions are colourless; Fe(CNS)²⁺ ions are blood-red. Procedure: mix ~5 cm³ of iron(III) chloride solution with one drop of potassium thiocyanate (KCNS) in a test-tube. Observation: a red colour forms — equilibrium lies on the right-hand side. The solution is divided into three test-tubes. Part (a) — add dilute HCl: Cl⁻ ions remove Fe³⁺ from solution (forming FeCl₃); this decreases [Fe³⁺]; equilibrium shifts left to replace the Fe³⁺; less Fe(CNS)²⁺ is present → red colour disappears. Part (b) — add more KCNS solution: [CNS⁻] increases; equilibrium shifts right to absorb the added CNS⁻; more Fe(CNS)²⁺ is produced → red colour intensifies. Both observations are in keeping with Le Chatelier's Principle."
      }
     ],
     "chem19": [
      {
       "type": "short",
       "marks": 4,
       "prompt": "What is the ionic product of water (Kw)? Write the equation for the self-ionisation of water. Calculate the concentration of H⁺ ions in pure water at 25°C, given that Kw = 1.0 × 10⁻¹⁴ mol²/L². Explain why the pH of pure water decreases at higher temperatures, yet water remains neutral.",
       "model": "The ionic product of water is Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴ at 25°C. Self-ionisation: H₂O ⇌ H⁺ + OH⁻. Since [H⁺] = [OH⁻] in pure water: [H⁺]² = 1.0 × 10⁻¹⁴ → [H⁺] = √(1.0 × 10⁻¹⁴) = 1.0 × 10⁻⁷ mol/L. At higher temperatures: the self-ionisation of water is endothermic (ΔH = +55.8 kJ/mol). By Le Chatelier's Principle, increasing temperature shifts equilibrium to the right, producing more H⁺ and OH⁻ ions. Therefore Kw increases. Since [H⁺] increases, pH = −log[H⁺] decreases. However, water remains neutral at all temperatures because [H⁺] always equals [OH⁻] — both increase equally. Neutral means [H⁺] = [OH⁻], not that pH = 7."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "State the ranges and colour changes of three common indicators. State which indicator is most suitable for each of the following titrations: (a) strong acid–strong base, (b) strong acid–weak base, (c) weak acid–strong base. Explain why no indicator is suitable for a weak acid–weak base titration.",
       "model": "Table of indicators: Methyl orange: range 3–5; red in acid, yellow in base. Litmus: range 5–8; red in acid, blue in base. Phenolphthalein: range 8–10; colourless in acid, pink in base. (a) Strong acid–strong base (e.g. HCl/NaOH): equivalence point at pH = 7; vertical pH jump spans approximately pH 3–10. All three indicators are suitable since all their ranges lie within the steep vertical part of the curve. Phenolphthalein is usually preferred; litmus is less reliable for accurate work. (b) Strong acid–weak base (e.g. HCl/NH₃): equivalence point below pH 7; vertical jump spans approximately pH 3–7. Only methyl orange (range 3–5) is suitable — its range lies within the jump. Phenolphthalein (8–10) would not change colour within the jump. (c) Weak acid–strong base (e.g. CH₃COOH/NaOH): equivalence point above pH 7; vertical jump spans approximately pH 7–10. Only phenolphthalein (range 8–10) is suitable. Methyl orange (3–5) lies outside the vertical part of the curve. Weak acid–weak base (e.g. CH₃COOH/NH₃): the pH rises very gradually — there is no sudden large jump in pH at any stage of the titration. Therefore there is no sharp endpoint and no indicator would show a sudden colour change. This titration cannot be used to find concentrations of the acid or base."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "Explain why a pH sensor is a more accurate way of measuring pH compared to using a universal indicator. Describe how a pH sensor is calibrated.",
       "model": "Two reasons a pH sensor is more accurate than universal indicator: (1) Precise numerical value — a pH sensor measures the voltage set up by hydrogen ions and gives an exact numerical reading, e.g. pH = 4.72. Universal indicator only allows estimation of colour shades, giving only an approximate value. (2) Removes subjectivity — the colour interpretation of universal indicator can vary from person to person. It can also be affected by the colour of the solution itself or by the lighting in the room. A pH sensor gives an objective digital reading regardless of solution colour. Calibration procedure: before use, set the pH sensor to read correct pH values using two standard buffer solutions of known pH (e.g. pH 3 and pH 10). The software in the datalogger is used to calibrate the sensor. Calibration ensures accuracy (readings close to the true value). After calibration, repeated readings in the same buffer test for precision."
      },
      {
       "type": "short",
       "marks": 3,
       "prompt": "(a) Calculate the pH of a solution with [H⁺] = 3.5 × 10⁻⁴ mol/L. (b) Calculate [H⁺] in a solution of pH 8.6. (c) A solution has a pH of 2. Is it acidic or basic? State the concentration of OH⁻ ions in this solution at 25°C.",
       "model": "(a) pH = −log₁₀[H⁺] = −log₁₀(3.5 × 10⁻⁴) = 3.46. (b) pH = 8.6 → [H⁺] = antilog(−8.6) = 10⁻⁸·⁶ = 2.51 × 10⁻⁹ mol/L. (c) pH = 2 → acidic (pH < 7 at 25°C). [H⁺] = 10⁻² = 0.01 mol/L. Using Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴: [OH⁻] = 1.0 × 10⁻¹⁴ / 0.01 = 1.0 × 10⁻¹² mol/L."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Calculate the pH of (a) a 0.025 M solution of hydrochloric acid and (b) a 0.025 M solution of sodium hydroxide at 25°C.",
       "model": "(a) HCl is a strong acid; fully dissociated. HCl → H⁺ + Cl⁻. [H⁺] = 0.025 mol/L. pH = −log₁₀(0.025) = 1.60. (b) NaOH is a strong base; fully dissociated. NaOH → Na⁺ + OH⁻. [OH⁻] = 0.025 mol/L. pOH = −log₁₀(0.025) = 1.60. pH = 14 − pOH = 14 − 1.60 = 12.40. (Note: the pH of the acid and the pOH of the base are equal in this case because both have the same concentration.) Cross-check: [H⁺][OH⁻] = 10⁻¹·⁶ × 10⁻¹²·⁴ = 10⁻¹⁴ = Kw ✓."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Write the expression for the acid dissociation constant Ka of ethanoic acid. Explain why [H₂O] is not included in the Ka expression. Calculate the pH of a 0.1 M solution of ethanoic acid given that Ka = 1.8 × 10⁻⁵. State the formula you use and show all steps.",
       "model": "Ka expression for CH₃COOH ⇌ CH₃COO⁻ + H⁺: Ka = [CH₃COO⁻][H⁺] / [CH₃COOH] = 1.8 × 10⁻⁵. [H₂O] is not included because Ka is defined purely in terms of the dissociation of the acid; [H₂O] is essentially constant (55.56 mol/L) and is absorbed into the constant. Calculation: formula [H⁺] = √(Ka × Macid) — this formula is NOT in the Formulae and Tables booklet. [H⁺] = √(1.8 × 10⁻⁵ × 0.1) = √(1.8 × 10⁻⁶) = 1.34 × 10⁻³ mol/L. pH = −log₁₀(1.34 × 10⁻³) = 2.87 ≈ 2.9. Note: the assumption made is that 0.1 − x ≈ 0.1, i.e. the amount dissociated is very small compared to the initial concentration, which is valid for weak acids."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Distinguish between a strong acid and a weak acid in terms of the Brønsted-Lowry theory. Explain, with reference to conjugate acid-base pairs, why the statement 'solutions of strong acids always have a low pH' is incorrect.",
       "model": "Strong acid: a good proton donor; almost completely dissociated in water into ions. Example: HCl → H⁺ + Cl⁻ (essentially goes to completion). Weak acid: a poor proton donor; only partially dissociated in water; an equilibrium exists. Example: CH₃COOH ⇌ CH₃COO⁻ + H⁺. Conjugate pairs: when a strong acid (HCl) donates its proton, the conjugate base (Cl⁻) is very weak — it has very little tendency to re-accept the proton, so the equilibrium lies far to the right. When a weak acid (CH₃COOH) donates its proton, the conjugate base (CH₃COO⁻) is relatively strong — it tends to re-accept the proton, so the equilibrium lies to the left. Explanation for incorrectness: pH depends on [H⁺] in solution, not on whether the acid is strong or weak. A strong acid that has been diluted to a very low concentration can have a higher pH than a concentrated weak acid solution. For example, a 0.00001 M solution of HCl (strong acid) has [H⁺] = 10⁻⁵ M → pH = 5. A 1 M solution of ethanoic acid (weak acid) has pH ≈ 2.4, which is lower. The statement is incorrect: it confuses acid strength with acid concentration."
      }
     ],
     "chem20": [
      {
       "type": "short",
       "marks": 4,
       "prompt": "Name the four main greenhouse gases (other than water vapour). Why is water vapour not assigned a Global Warming Potential (GWP) value despite being the most abundant greenhouse gas?",
       "model": "Four main greenhouse gases (other than water vapour): carbon dioxide (CO₂), methane (CH₄), nitrous oxide/dinitrogen oxide (N₂O), fluorinated gases (e.g. CFCs). Water vapour not assigned GWP: To be assigned a GWP, a gas must satisfy: (i) we directly release a standard kg of it; (ii) it stays in the atmosphere for a known time; (iii) it directly causes warming on its own. Water vapour fails all three: (i) its concentration depends on temperature (controlled by evaporation and condensation), not our direct emissions — we cannot control how much enters the atmosphere; (ii) residence time is only days/weeks (falls as rain), too short for a 100-year comparison period; (iii) water vapour is a feedback amplifier, not a primary driver — it increases only because CO₂/CH₄/N₂O first warm the atmosphere. Assigning water vapour a GWP in the same way as CO₂ would not be valid or meaningful."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Define the enhanced greenhouse effect. Give three pieces of evidence that it is occurring. Describe four consequences of the enhanced greenhouse effect.",
       "model": "Enhanced greenhouse effect: intensification of the Earth's natural greenhouse effect due to increased concentrations of greenhouse gases caused by human activities such as burning fossil fuels and deforestation, resulting in extra warming (global warming). Evidence: (1) Rising CO₂ levels — accurate measurements at Mauna Loa, Hawaii since 1958 show a steady, accelerating rise in atmospheric CO₂; levels have increased ~35–40% over the last 200 years as fossil fuel use increased. (2) Global temperature rise — Earth's average surface temperature has risen by over 1.1°C since 1880; most increase since 1970; this rise cannot be explained by natural factors alone. (3) Computer climate models — models using only natural factors do not match the observed warming trend; including human greenhouse gas emissions makes the models accurately match actual temperature data. Four consequences: (1) Global warming — glaciers and ice sheets melt; sea levels rise (~20 cm since 1900), threatening low-lying countries like Netherlands and Bangladesh. (2) Extreme weather events — storms become more frequent and violent due to more energy in the atmosphere. (3) Precipitation changes — increased evaporation means heavier rainfall and flooding in some regions; prolonged droughts in subtropical areas. (4) Ocean acidification — CO₂ dissolves in oceans forming H₂CO₃; dissolves CaCO₃ shells of marine organisms (oysters, clams, mussels); damages marine ecosystems."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Describe three ways in which human activity contributes to increased greenhouse gas emissions. For each, suggest one specific solution. State what is meant by carbon capture and storage.",
       "model": "(1) Burning fossil fuels: combustion of coal, oil, natural gas in power stations, homes and industry releases CO₂; car engines also release CO₂ and NOx. Solution: switch to renewable energy (solar, wind, hydroelectric); improve building and industrial energy efficiency; phase out fossil fuels. (2) Agriculture: livestock (cattle, sheep) produce CH₄ from enteric fermentation; nitrogenous fertilisers produce N₂O. Solution: breed animals that naturally produce less methane; install biogas systems to collect methane from animal manure and use it as a fuel; apply fertilisers at the correct amount and time; use nitrogen-fixing crops. (3) Deforestation and draining of peatlands: felling trees removes a major carbon sink (photosynthesis); decay/burning of cut wood releases stored carbon; drained peat decomposes releasing CO₂ and CH₄. Solution: plant more trees and forests; protect and restore peatlands and wetlands as carbon sinks. Carbon capture and storage (CCS): a process of trapping CO₂ from industrial/power plant chimneys before it enters the atmosphere; the CO₂ is removed, compressed into a liquid, transported by pipeline, and injected into depleted underground oil or gas fields for permanent storage."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Define water contamination. Name four causes of water contamination and for each, describe the biochemical consequence for a waterway.",
       "model": "Water contamination: the introduction of substances into water that makes it unsafe for consumption or harmful to ecosystems. (1) Sewage — contains high organic matter; bacteria consume dissolved O₂ breaking it down (high B.O.D.); reduced O₂ causes fish kills; anaerobic bacteria produce H₂S. (2) Agricultural effluent — nitrates/phosphates from fertilisers act as nutrients; cause eutrophication (algal bloom → O₂ depletion → fish kills). (3) Heavy metals (e.g. Pb, Hg) — cumulative poisons; interfere with enzyme function; damage kidneys, liver, nervous system; Pb²⁺ ions mimic Ca²⁺ causing neurological damage in children. (4) Acidification — acid rain/acidic industrial discharges lower pH; at pH < 5: enzyme activity disrupted; Al³⁺ ions dissolve from rocks and damage fish gills; carbonate shells of shellfish dissolved."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Define biochemical oxygen demand (B.O.D.). Describe the B.O.D. test fully, giving a reason for each specific experimental condition. State the B.O.D. value for clean water and for one highly polluted sample.",
       "model": "B.O.D. = the amount of dissolved O₂ consumed by biological (biochemical) action when a water sample is kept at 20°C in the dark for five days. Procedure: two bottles are completely filled with the water sample to be tested. The dissolved oxygen in bottle A is measured immediately. Bottle B is sealed and incubated at 20°C in the dark for 5 days; its dissolved O₂ is then measured. B.O.D. = difference between the two readings (mg/L). Reasons: (1) 20°C — O₂ solubility and rate of bacterial O₂ consumption are temperature-dependent; fixed temp allows valid comparison between samples. (2) Kept in the dark — prevents photosynthesis by plant material in the water, which would increase O₂ and give a falsely low B.O.D. reading. (3) Five days — standardised time long enough to measure significant oxygen depletion. Values: clean water = 1–2 mg/L. Silage effluent = 54,000 mg/L (accept pig slurry = 500 mg/L or raw sewage = 300 mg/L)."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Explain what eutrophication is and describe fully how it leads to fish kills. Name the ions responsible for artificial eutrophication and state their source.",
       "model": "Eutrophication = the enrichment of water with nutrients, leading to excessive growth of algae and other plants. Responsible ions: nitrate (NO₃⁻) and phosphate (PO₄³⁻). Sources: runoff of artificial fertilisers from farmland (agricultural effluent) and domestic sewage/wastewater. Mechanism of fish kill: high nutrient levels cause rapid algal bloom covering the water surface. The algae are short-lived; when they die they are decomposed by bacteria and other microorganisms. These microorganisms consume large amounts of dissolved O₂ (greatly increased B.O.D.). The dissolved O₂ level in the water falls sharply. At sufficiently low O₂, fish cannot get enough through their gills and die (fish kill). At near-zero O₂, anaerobic bacteria take over and produce H₂S, making the water foul-smelling."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Describe, with named chemicals where appropriate, five stages of the water treatment process, giving the purpose of each stage.",
       "model": "(1) Screening — water from river/lake passed through wire mesh screen; removes large floating debris (twigs, leaves, plastic bags). No chemicals added. (2) Flocculation — aluminium sulfate Al₂(SO₄)₃ added as flocculating agent; causes small suspended particles to coagulate into larger flocs; flocs settle out or are filtered more easily. (3) Sedimentation — water flows slowly through large settling tanks; flocs and heavier particles sink to bottom (sludge) under gravity; over 90% of suspended particles removed; sludge pumped out. (4) Filtration — water passes through layers of coarse and fine sand (on gravel); sand acts as a sieve trapping remaining suspended particles; microfiltration membranes (0.1–10 μm pores) also remove bacteria. (5) Chlorination — chlorine added: Cl₂ + H₂O → HOCl + HCl; hypochlorous acid kills harmful microorganisms; chlorine residual (~0.5 ppm) maintained for ongoing disinfection in pipes. (6) Fluoridation (accept any 5) — NaF or H₂SiF₆ added at ~1 ppm; reduces tooth decay by strengthening enamel. (7) pH adjustment — Ca(OH)₂ used to raise pH to 7.2 for limestone-area water; H₂SO₄ used to lower pH if too high; prevents corrosion of distribution pipes."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Explain the operation of a lithium-ion cell during discharge and assess two life-cycle impacts.",
       "model": "Lithium ions move through the electrolyte from the negative electrode to the positive electrode while electrons travel through the external circuit and do electrical work; charging reverses the processes using supplied energy. Mining lithium, nickel or cobalt can damage ecosystems and communities, while manufacture uses energy. Long service, responsible sourcing and material recovery reduce impacts but recycling is technically demanding."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain why charging a lithium-ion cell is not the same as simply storing electrons inside it.",
       "model": "The charger drives a non-spontaneous redox process. Electrons move through the external circuit while lithium ions migrate through the electrolyte and are inserted into electrode material, storing chemical potential in changed electrode states. Charge balance is maintained; loose electrons do not accumulate in the cell."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Evaluate a chemistry-based response to climate change through the themes of sustainability, health and technology.",
       "model": "Green hydrogen can store renewable energy and produce water at use, potentially reducing combustion pollution and carbon emissions. Electrolysis requires large amounts of low-carbon electricity, storage is difficult and current production often uses fossil fuels. A sound evaluation compares full life-cycle emissions, resource demand, safety, cost and the applications where alternatives are weaker."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Outline a research strategy for comparing two claims about a sustainable chemical technology.",
       "model": "Define measurable criteria such as life-cycle emissions, efficiency, toxicity, resource use and cost. Use recent peer-reviewed studies and transparent institutional data, evaluate system boundaries and conflicts of interest and compare like with like. Report uncertainty and distinguish laboratory potential from demonstrated large-scale performance."
      }
     ],
     "chem21": [
      {
       "type": "short",
       "marks": 10,
       "prompt": "Use bond enthalpies to explain why a reaction may be exothermic or endothermic.",
       "model": "Breaking reactant bonds absorbs energy, while forming product bonds releases energy. The approximate enthalpy change is the sum of bond enthalpies broken minus the sum formed. If formation releases more than breaking requires, ΔH is negative and the reaction is exothermic; the reverse gives a positive endothermic value."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define thermochemistry. Define enthalpy change (ΔH). Write a thermochemical equation for the complete combustion of propane. What does a negative ΔH value tell you about a reaction?",
       "model": "Thermochemistry: the study of heat changes that occur during chemical reactions. Enthalpy change (ΔH): the overall energy exchanged with the surroundings when a chemical or physical change is carried out at constant pressure; measured in kJ mol⁻¹. Thermochemical equation for propane combustion: C₃H₈(g) + 5O₂(g) → 3CO₂(g) + 4H₂O(l) ΔH = −2220 kJ mol⁻¹. A negative ΔH means the reaction is exothermic — heat energy is released to the surroundings; the products have lower enthalpy (are more stable) than the reactants."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Define enthalpy of neutralisation. In an experiment, 50 cm³ of 1.0 M HCl was added to 50 cm³ of 1.0 M NaOH in a polystyrene cup. The temperature rose by 6.8°C. Given that the specific heat capacity of the solution is 4200 J kg⁻¹ K⁻¹ and density is 1 g cm⁻³, calculate the enthalpy of neutralisation. Explain why the enthalpy of neutralisation of ethanoic acid and NaOH would be less than −57 kJ mol⁻¹.",
       "model": "Enthalpy of neutralisation: the heat change when one mole of H⁺ ions from an acid reacts with one mole of OH⁻ ions from a base. Calculation: Total volume = 100 cm³; mass = 100 g = 0.1 kg. Heat given out = m × c × Δt = 0.1 × 4200 × 6.8 = 2856 J = 2.856 kJ. Moles of HCl neutralised = (50 × 1.0) / 1000 = 0.05 mol. Enthalpy of neutralisation per mole = 2.856 / 0.05 = 57.12 kJ mol⁻¹ → ΔH = −57.1 kJ mol⁻¹. Explanation for weak acid: Ethanoic acid (CH₃COOH) is a weak acid — it is only partially dissociated in solution. For complete neutralisation to occur and for one mole of H₂O to be formed, the ethanoic acid must first be fully dissociated. This dissociation process requires energy (it is endothermic). Therefore, the net heat released is less than 57 kJ per mole of water formed (the energy needed for dissociation is subtracted from the energy released by the H⁺ + OH⁻ → H₂O reaction)."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Define enthalpy of formation. Why is the enthalpy of formation of carbon dioxide not zero? Write the equation for the enthalpy of formation of ammonia. Use Hess's Law to calculate the enthalpy of reaction for HCOOH(l) → CO₂(g) + H₂O(g), given heats of formation: HCOOH = −427.7; CO₂ = −393; H₂O = −285.8 kJ mol⁻¹.",
       "model": "Enthalpy of formation: the heat change when one mole of a compound in its standard state is formed from its elements in their standard states. CO₂ is NOT an element — it is a compound (formed from carbon and oxygen), so its enthalpy of formation is not zero (ΔH_f = −394 kJ mol⁻¹). Formation equation for ammonia: ½N₂(g) + 1½H₂(g) → NH₃(g) ΔH = −46 kJ mol⁻¹. Hess's Law calculation for HCOOH → CO₂ + H₂O: ΔH_reaction = ΔH_f(products) − ΔH_f(reactants) = [ΔH_f(CO₂) + ΔH_f(H₂O)] − ΔH_f(HCOOH) = [(−393) + (−285.8)] − (−427.7) = −678.8 + 427.7 = −251.1 kJ mol⁻¹."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Define bond enthalpy. State whether bond breaking is exothermic or endothermic. Using average bond enthalpy values from Table 21.3, calculate the enthalpy of reaction for CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l). State the values you use.",
       "model": "Bond enthalpy: the average energy required to break one mole of a particular covalent bond and to separate the neutral atoms completely from each other. Bond breaking is endothermic (energy must be supplied). Bond formation is exothermic (energy is released). Calculation for CH₄ + 2O₂ → CO₂ + 2H₂O: Bonds broken (reactants): 4 × C−H = 4 × 412 = 1648 kJ; 2 × O=O = 2 × 498 = 996 kJ. Total energy required = 2644 kJ. Bonds formed (products): 2 × C=O (in CO₂) = 2 × 799 = 1598 kJ; 4 × O−H (in 2H₂O) = 4 × 463 = 1852 kJ. Total energy released = 3450 kJ. ΔH = total energy in − total energy out = 2644 − 3450 = −806 kJ mol⁻¹. The negative value confirms the reaction is exothermic."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "State Hess's Law. Use the following heats of formation to calculate the enthalpy of formation of methane (C + 2H₂ → CH₄): (a) C(s) + O₂(g) → CO₂(g) ΔH = −393 kJ mol⁻¹; (b) H₂(g) + ½O₂(g) → H₂O(l) ΔH = −286 kJ mol⁻¹; (c) CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l) ΔH = −879 kJ mol⁻¹.",
       "model": "Hess's Law: if a chemical reaction takes place in a number of stages, the total heat change in the separate stages is equal to the heat change if the reaction is carried out in one stage (ΔH is independent of route). Calculation for C + 2H₂ → CH₄: Step 1 — required equation is: C + 2H₂ → CH₄ ΔH = ? Step 2 — keep equation (a): C + O₂ → CO₂ ΔH = −393 kJ mol⁻¹. Step 3 — multiply (b) × 2: 2H₂ + O₂ → 2H₂O ΔH = −572 kJ mol⁻¹. Step 4 — add (a) and (b)×2: C + 2H₂ + 2O₂ → CO₂ + 2H₂O ΔH = −965 kJ mol⁻¹. Step 5 — reverse (c): CO₂ + 2H₂O → CH₄ + 2O₂ ΔH = +879 kJ mol⁻¹. Step 6 — add to result of Step 4: C + 2H₂ + 2O₂ + CO₂ + 2H₂O → CO₂ + 2H₂O + CH₄ + 2O₂. Cancel: C + 2H₂ → CH₄ ΔH = −965 + 879 = −86 kJ mol⁻¹."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Explain why there is a steady increase in the enthalpy of combustion as the carbon chain length of alkanes increases. Why do primary alcohols have a lower enthalpy of combustion than the corresponding alkanes? Why do alkenes have a lower enthalpy of combustion than the corresponding alkanes?",
       "model": "Steady increase in alkanes: every time a CH₂ unit is added to an alkane, the larger alkane has two extra C−H bonds and one extra C−C bond to break, but also produces one extra CO₂ and one extra H₂O on combustion. The formation of an extra CO₂ molecule releases a large amount of energy (strong C=O bonds, 799 kJ mol⁻¹ each). The amount of bond breaking and bond making is the same for each CH₂ unit added, so the increase in heat of combustion is approximately constant at ~650 kJ mol⁻¹ per CH₂ unit (almost linear). Primary alcohols lower than corresponding alkanes: (1) All primary alcohols contain an −OH functional group. The carbon atom bonded to −OH is already partially oxidised (it already contains an oxygen atom). (2) Therefore, when the alcohol is fully combusted to CO₂ and H₂O, less additional oxidation is needed compared to the alkane. Less energy is released. (3) In other words, one fewer O₂ molecule needs to be absorbed, meaning fewer bonds are broken and fewer high-energy C=O bonds are formed. Alkenes lower than corresponding alkanes: (1) An alkene has fewer hydrogen atoms than an alkane of the same carbon number (one C=C double bond means 2 fewer H atoms). Fewer H atoms means less H₂O is produced on combustion, releasing less energy. (2) Additionally, the C=C double bond in the alkene must be broken (614 kJ mol⁻¹), which is stronger than the C−C single bond (348 kJ mol⁻¹), so more energy is needed to break bonds in the reactant."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Define heat of combustion. Describe Experiment 21.1 (spirit burner method) to determine the heat of combustion of methanol. Include a labelled description of apparatus, key steps, and calculation method.",
       "model": "Heat of combustion: the heat change when one mole of a substance is completely burned in excess oxygen at standard conditions (25°C, 1 atm). Experiment 21.1: Apparatus: copper calorimeter containing a known volume of water, spirit burner filled with methanol, draught shield, thermometer (or temperature sensor), balance, heatproof mat. Key procedure: (1) Record the initial mass of the spirit burner and methanol. (2) Fill the copper calorimeter with a known volume of water (e.g. 100 cm³ = 0.1 kg); record initial water temperature. (3) Light the spirit burner and allow it to heat the water; stir gently. (4) When temperature has risen sufficiently, extinguish the flame and record the maximum temperature reached. (5) Record the final mass of the spirit burner and methanol. Calculation: Mass of methanol burned = initial mass − final mass. Moles of methanol = mass burned / M_r(CH₃OH) = mass / 32.04. Heat given out = m × c × (t₂ − t₁), where m = mass of water in kg, c = 4200 J kg⁻¹ K⁻¹. Heat of combustion = heat given out / moles burned (express as kJ mol⁻¹ with negative sign). Note: the draught shield prevents air currents dispersing heat; the heat gained by the water is assumed equal to the heat released by the burning alcohol."
      }
     ],
     "chem22": [
      {
       "type": "short",
       "marks": 5,
       "prompt": "Distinguish between a primary cell and a secondary cell. Describe the reactions that take place during discharge of a lithium-ion cell. State two environmental problems associated with lithium-ion batteries.",
       "model": "Primary cell: a type of galvanic cell designed for single use; cannot be recharged; the chemical reactions are irreversible. Examples: zinc-carbon, alkaline, lithium (watch batteries). Secondary cell: a type of galvanic cell that can be recharged; the chemical reactions are reversible; can be reused many times. Examples: lithium-ion (≈3.8 V), lead-acid (≈2 V per cell). Lithium-ion cell — discharge (supplying electrical energy to a device): At the carbon/graphite anode (negative electrode, oxidation): LiCₓ → Li⁺ + e⁻ + Cₓ. Lithium ions leave the graphite, electrons flow through the external circuit to power the device. At the cobalt oxide cathode (positive electrode, reduction): Li⁺ + e⁻ + CoO₂ → LiCoO₂. Lithium ions travel through the electrolyte and enter the cobalt oxide. Overall: LiCₓ + CoO₂ → Cₓ + LiCoO₂. Li⁺ ions 'rock' from carbon electrode to cobalt oxide electrode. Environmental problems: (1) Fire hazard — organic solvent electrolyte is flammable; if battery is crushed or punctured, a dangerous internal short circuit and fire can result. (2) Leaching of heavy metals — cobalt and copper in the battery can leach into the soil and waterways if not disposed of properly."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define electrochemistry. Briefly describe the contributions of Luigi Galvani and Alessandro Volta to the founding of electrochemistry. What device did Volta build in 1800?",
       "model": "Electrochemistry: the branch of chemistry that studies the relationship between chemical reactions and electricity. Luigi Galvani (Bologna, 1771): dissecting a frog's leg, he observed that it twitched when the exposed nerve came into contact with two different metals (iron scalpel and copper hook). He believed this was 'animal electricity' coming from the frog itself. Alessandro Volta: realised that the electricity was actually produced by the two different metals in contact with the conducting liquid of the frog's leg (not animal electricity). He extended Galvani's work to non-biological systems. In 1800, Volta built the first battery, called a voltaic pile, consisting of round discs of copper and zinc separated by pieces of cardboard soaked in salt solution, stacked in a pile. When a wire was attached to the top and bottom, an electric current flowed."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Describe the zinc-copper galvanic cell. Write ionic half-equations for the reactions at each electrode. Write an overall ionic equation. State the function of the salt bridge. Use the term CROA in your answer.",
       "model": "Setup: zinc electrode dipping in 1 M ZnSO₄ solution; copper electrode dipping in 1 M CuSO₄ solution; the two half-cells connected by a wire and a salt bridge; voltmeter shows ≈1.1 V. CROA: Cathode = Reduction, Oxidation = Anode. At the zinc electrode (anode, negative): Zn(s) → Zn²⁺(aq) + 2e⁻. Zinc atoms lose electrons; this is oxidation; electrons flow away from zinc through the wire to copper. At the copper electrode (cathode, positive): Cu²⁺(aq) + 2e⁻ → Cu(s). Copper(II) ions from solution accept electrons and are deposited as copper metal; this is reduction. Overall ionic equation: Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s). Function of salt bridge: allows ions to flow between the two half-cells (e.g. K⁺ and NO₃⁻ ions from a KNO₃-soaked paper bridge) to maintain electrical neutrality — Zn²⁺ builds up in the zinc half-cell and Cu²⁺ is removed from the copper half-cell; without the salt bridge, a charge imbalance would build up and stop the current. The salt bridge allows ion flow without allowing the two solutions to mix directly."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "What is the electrochemical series? Explain how it can be used to predict whether a chemical reaction will occur. Write ionic equations for two displacement reactions predictable from the series.",
       "model": "Electrochemical series: a list of elements in order of their standard electrode potentials, i.e. in order of decreasing tendency for the element to be oxidised (lose electrons) under standard conditions. Elements at the top (e.g. lithium, potassium, sodium) are most easily oxidised (most reactive); elements at the bottom (e.g. copper, silver, gold) are very difficult to oxidise (least reactive/stable). Predicting reactions: a metal higher in the electrochemical series will displace a metal below it from a solution of that metal's ions — i.e. the higher metal will spontaneously reduce the lower metal's ions. Example 1: Magnesium displaces copper from copper sulfate solution: Mg(s) + Cu²⁺(aq) → Mg²⁺(aq) + Cu(s). [Mg is above Cu in the series.] Example 2: Copper displaces silver from silver nitrate solution: Cu(s) + 2Ag⁺(aq) → Cu²⁺(aq) + 2Ag(s). [Cu is above Ag.] Example 3: Fe + Cu²⁺(aq) → Fe²⁺(aq) + Cu(s) [used industrially to extract copper from dilute copper sulfate solution using scrap iron]."
      },
      {
       "type": "short",
       "marks": 4,
       "prompt": "Explain the term corrosion. State two ways of preventing corrosion of iron/steel. What is meant by cathodic protection, and how does it work?",
       "model": "Corrosion: any undesired process whereby a metal is converted to one of its compounds. The most common example is the rusting of iron and steel, which forms iron(III) oxide hydrate (Fe₂O₃·xH₂O) — requires both oxygen and water to be present. Methods of preventing corrosion: (1) Galvanising — coating iron or steel with a layer of zinc. Zinc is higher in the electrochemical series than iron, so it has a greater tendency to be oxidised. Even if the zinc surface is scratched, the zinc still preferentially corrodes and protects the iron. Used for wheelbarrows, buckets, building sheds. (2) Painting and greasing — creates a physical barrier between the metal surface and the air/water. However, if the paint is scratched, the exposed metal will corrode; must be maintained regularly. Cathodic protection: a large piece of zinc (or other more reactive metal) is physically bolted to the steel hull of ships, or to underground steel pipes. Because zinc is higher in the electrochemical series than iron, zinc acts as the anode (is oxidised/corrodes) and the steel hull becomes the cathode (cannot be oxidised). This protects the steel from corrosion. The zinc must be replaced periodically as it is gradually consumed. It is called cathodic protection because the steel is protected by being made the cathode of the cell."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Describe Experiment 22.2A (electrolysis of acidified water with inert electrodes). State observations, write ionic half-equations at each electrode, and explain why electrode signs are reversed compared to a galvanic cell. Also write ionic half-equations for the electrolysis of copper(II) chloride solution.",
       "model": "Experiment 22.2A — Electrolysis of acidified water: Dilute sulfuric acid is added to distilled water to make it conduct electricity. The experiment is set up in a Hofmann voltammeter or using inverted test tubes to collect the gases over each electrode. Inert carbon (or platinum) electrodes are used. The DC power supply is switched on. Observations: Gas is collected at both electrodes. The volume of gas at the negative electrode is twice that collected at the positive electrode (ratio 2:1). Tests show: the gas at the negative electrode ignites with a 'pop' = hydrogen; the gas at the positive electrode relights a glowing splint = oxygen. Ionic half-equations: Negative electrode (cathode, reduction): 2H⁺(aq) + 2e⁻ → H₂(g). H⁺ ions from H₂SO₄ are attracted to the negative electrode and accept electrons. Positive electrode (anode, oxidation): H₂O(l) → 2H⁺(aq) + ½O₂(g) + 2e⁻. Water molecules are destabilised and broken down; oxygen gas is released. Overall: H₂O(l) → H₂(g) + ½O₂(g). Why signs are reversed vs galvanic cells: In a galvanic cell, spontaneous redox reactions drive electron flow; the anode (oxidation) is naturally the negative electrode. In electrolysis, an external power source forces electrons in the opposite direction, so oxidation is now forced to occur at the positive electrode (anode). The battery 'pumps' electrons onto the negative electrode (forcing reduction there) and removes electrons from the positive electrode (forcing oxidation there). Electrolysis of copper(II) chloride (inert carbon electrodes): Negative (cathode, reduction): Cu²⁺(aq) + 2e⁻ → Cu(s) [brown solid deposits]. Positive (anode, oxidation): 2Cl⁻(aq) → Cl₂(g) + 2e⁻ [bubbles of chlorine gas, bleaches litmus]. Overall: Cu²⁺(aq) + 2Cl⁻(aq) → Cu(s) + Cl₂(g)."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Compare a conventional chemical cell with a hydrogen fuel cell.",
       "model": "Both use spatially separated redox half-reactions to drive electrons through an external circuit. A conventional cell stores finite reactants internally and eventually discharges, while a fuel cell operates while hydrogen and oxygen are supplied and products removed. Fuel cells can produce water at use, but hydrogen production, storage, catalysts and infrastructure affect overall sustainability."
      },
      {
       "type": "short",
       "marks": 5,
       "prompt": "Define a fuel cell. Describe the operation of a hydrogen-oxygen fuel cell, including the reactions at each electrode and the overall reaction. Give two advantages of a hydrogen fuel cell over a chemical cell.",
       "model": "Fuel cell: a device that converts the chemical energy stored in a fuel directly into electrical energy. Fuel cells work by using oxidation-reduction reactions to produce electricity; no combustion takes place. Operation of hydrogen-oxygen fuel cell: The fuel (H₂) is continuously fed to the negative electrode (anode); the oxidising agent (O₂ from air) is fed continuously to the positive electrode (cathode). Electrolyte = proton exchange membrane (PEM) — a solid plastic polymer which: (i) allows H⁺ ions to pass through; (ii) prevents electrons from passing through (forcing them through the external circuit); (iii) prevents H₂ and O₂ gases from mixing. At the anode (negative electrode, oxidation): H₂(g) → 2H⁺(aq) + 2e⁻. Electrons flow through the external circuit (generating electricity). H⁺ ions pass through the membrane to the cathode. At the cathode (positive electrode, reduction): ½O₂(g) + 2H⁺(aq) + 2e⁻ → H₂O(l). Overall reaction: H₂(g) + ½O₂(g) → H₂O(l). Only product is water — zero carbon emissions. Both electrodes contain porous carbon with a platinum catalyst. Advantages over chemical cells: (1) Environmental impact is very low — water is the only product, no CO₂ or carbon emissions when using green hydrogen; (2) No need for recharging — fuel and oxidising agent are continuously supplied as long as the fuel cell operates."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Assess one application of electrochemistry in sustainable technology.",
       "model": "Electrolysers can use renewable electricity to produce hydrogen that stores energy and supplies industry without carbon at point of use. Efficiency losses, water and catalyst needs, difficult storage and fossil-derived electricity can reduce benefit. The application is strongest where direct electrification is impractical and life-cycle emissions are verified."
      }
     ],
     "chem23": [
      {
       "type": "short",
       "marks": 10,
       "prompt": "Outline the principal sources of hydrocarbons and explain why their uses extend beyond fuels.",
       "model": "Crude oil and natural gas are the main fossil sources, separated and processed into useful fractions and feedstocks; biomass can supply some renewable hydrocarbons or related molecules. Hydrocarbons fuel transport and heating but also provide starting materials for polymers, solvents, detergents and pharmaceuticals. Their value depends on structure and chemical reactivity as well as combustion."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Assess one major societal impact of extensive hydrocarbon use.",
       "model": "Combustion supplied dense, transportable energy that enabled industrialisation and mobility, but releases carbon dioxide and often air pollutants affecting climate and health. Extraction and spills damage ecosystems and economies become dependent on finite resources. Efficiency, alternative energy and using scarce hydrocarbons as chemical feedstocks can reduce, not instantly remove, the impact."
      },
      {
       "type": "experiment",
       "marks": 12,
       "prompt": "Describe an experiment to prepare ethene in the laboratory from ethanol and outline the tests you would carry out to investigate the properties of ethene.",
       "model": "Preparation: Ethanol is poured into a boiling tube and glass wool is added so the glass wool soaks up the ethanol. A small heap of aluminium oxide (Al₂O₃) is placed inside the boiling tube at the end of the glass wool. The apparatus is set up with a delivery tube leading to a water trough. The aluminium oxide is gently heated with a Bunsen burner. The ethanol vapour passes over the hot aluminium oxide and is dehydrated (elimination reaction) to produce ethene: ethanol → ethene + water. Bubbles of ethene gas are collected in test tubes by displacement of water. The first test tube is discarded as it contains mainly air. Tests on ethene: (1) Physical properties — ethene is a colourless gas, insoluble in water, slight sweetish smell. (2) Combustion — a lighted taper is applied to the mouth of a test tube of ethene; it burns with a yellow luminous (slightly smoky) flame; limewater added to a test tube confirms CO₂ is produced (turns milky): C₂H₄ + 3O₂ → 2CO₂ + 2H₂O. (3) Addition of bromine water — bromine water (red/orange) is added to a test tube of ethene, the stopper replaced and the tube shaken; the red colour changes to colourless — this is a test for unsaturation (C=C double bond). (4) Addition of acidified KMnO₄ — the purple colour of potassium manganate(VII) changes to colourless — this is also a test for unsaturation."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Describe the laboratory preparation of ethene from ethanol and the tests used to investigate the product.",
       "model": "Pass ethanol vapour over a heated suitable catalyst or dehydrate it under the approved method, collect ethene over water and discard initial gas contaminated with air. Ethene is colourless and combustible and rapidly decolourises bromine water by addition across the double bond. Use small quantities, eye protection and strict control of flammable vapour and heat."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Compare alkanes, alkenes and alkynes in composition, bonding, shape and characteristic reactions.",
       "model": "Alkanes are saturated with C–C single sigma bonds and undergo combustion and substitution. Alkenes contain a C=C sigma-plus-pi bond with trigonal-planar carbon and undergo electrophilic addition. Alkynes contain a linear C≡C with one sigma and two pi bonds and also add reagents. Unsaturation increases characteristic addition reactivity."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain why members of one homologous hydrocarbon series have similar chemical but gradually changing physical properties.",
       "model": "They share the same functional bonding pattern and general formula, so react in similar ways. Increasing chain length raises electron number, surface contact and London dispersion forces, increasing boiling point and viscosity and lowering volatility. Branching changes contact area and can lower boiling point among isomers."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain why straight chain alkanes have higher boiling points than branched chain isomers of the same molecular formula, and why boiling points increase along the homologous series of straight chain alkanes.",
       "model": "Alkanes are non-polar molecules so the only intermolecular forces are London dispersion forces (temporary dipole–induced dipole forces). Straight chain vs branched isomers: straight chain alkanes have a larger surface area than branched isomers of the same molecular formula. A larger surface area allows greater contact between molecules, leading to stronger London dispersion forces. More energy is needed to overcome these stronger forces, so the boiling point of the straight chain isomer is higher (e.g., hexane 68.7°C > 2,3-dimethylbutane 58.0°C). Increasing carbon number along the series: as the number of carbon atoms increases, the size of the molecule increases and the number of electrons in the electron cloud increases. This allows stronger temporary dipoles to form more easily, increasing the strength of the London dispersion forces. Therefore, more energy is needed to separate the molecules, causing the boiling point to increase (e.g., methane −161°C, butane −0.5°C, hexane 69°C)."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain the relative chemical stability of alkanes compared with alkenes.",
       "model": "Alkanes contain strong localised carbon-carbon and carbon-hydrogen sigma bonds and have no electron-rich pi bond, so many reactions require high activation energy or radical conditions. An alkene's exposed pi electrons are more weakly held and readily attacked by electrophiles, allowing addition under milder conditions."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Explain how 3D molecular models show both the usefulness and limitations of representations of hydrocarbons.",
       "model": "Models show tetrahedral, trigonal-planar or linear geometry, bond rotation and different connectivity in isomers. They help distinguish chain and positional arrangements that flat formulae hide. Ball-and-stick models exaggerate bond gaps and fixed sizes, electron density is absent and molecules are dynamic, so the model is not a literal scale image."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Explain, with reference to bonding, why benzene does not undergo addition reactions despite containing carbon-carbon double bonds in its Kekulé structure.",
       "model": "Rather than having alternating single and double bonds (as in the Kekulé structure), benzene is a resonance hybrid. Each carbon atom forms three sigma bonds using three of its four outer electrons; the fourth electron is in a p orbital. The six p orbitals overlap sideways to form a pi bonding system in which all six electrons are delocalised — spread over all six carbon atoms rather than localised between pairs. This delocalisation gives benzene extra stability and accounts for its lack of reactivity towards addition reactions. There are no isolated C=C double bonds in benzene; all six C-C bonds are identical and intermediate in length."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Describe the shapes of ethane, ethene and ethyne, giving the bond angles at each carbon atom.",
       "model": "Ethane C₂H₆: each carbon atom has four sigma bonds and four electron pairs → tetrahedral geometry → bond angles approximately 109.5° → non-planar molecule. Ethene C₂H₄: the C=C consists of one sigma bond and one pi bond; for VSEPR only sigma bonds count, so each carbon has three sigma bonds and three electron pairs → trigonal planar geometry → bond angles approximately 120° → planar molecule, all four atoms (2C, 2H) in the same plane. Ethyne C₂H₂: the C≡C consists of one sigma bond and two pi bonds; each carbon has two sigma bonds and two electron pairs → linear geometry → bond angles 180° → planar (linear) molecule."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain what is meant by cis-trans (geometric) isomerism. Draw the cis and trans isomers of but-2-ene and state one similarity and one difference in their properties.",
       "model": "Cis-trans isomers (geometric isomers) are molecules with the same molecular formula and the same condensed structural formula but different arrangements of their atoms in space. Cis-trans isomerism occurs in alkenes because rotation around the C=C double bond is not possible (rotation would break the pi bond). It arises when each carbon in the double bond has two different atoms or groups attached to it. Cis-but-2-ene: both methyl groups are on the same side of the double bond. Trans-but-2-ene: the two methyl groups are on opposite sides of the double bond. Similarity: both have the same molecular formula (C₄H₈) and burn in oxygen to give the same products (C₄H₈ + 6O₂ → 4CO₂ + 4H₂O). Difference: they have slightly different boiling points (different spatial arrangements affect intermolecular forces)."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Describe the bonding and structure of graphite and explain why it is a good electrical conductor.",
       "model": "Graphite consists of carbon atoms, each joined to three other carbon atoms by single covalent bonds. This forms flat sheets of carbon atoms arranged in rings of six (hexagons), with bond angles of 120°. Each carbon atom uses only three of its four outer electrons in bonding. The fourth (spare) electron is a delocalised electron that is free to move between the layers and carry the electric current. This is why graphite is a good electrical conductor."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Compare the properties of diamond and graphite with reference to hardness, electrical conductivity and uses.",
       "model": "Hardness: Diamond is the hardest naturally occurring substance because each carbon atom is joined to four others in a giant interlocking network of strong covalent bonds. Graphite is soft and slippery because only weak London dispersion forces hold the layers together, allowing them to slide over each other. Electrical conductivity: Diamond does not conduct electricity — all four outer electrons of each carbon atom are in bonds, so there are no free electrons. Graphite is an excellent electrical conductor because each carbon atom has a delocalised electron that is free to move between the layers. Uses: Diamond is used in jewellery and drill bits; graphite is used in pencil leads, as electrodes in batteries, and as a lubricant."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Relate the structures of diamond, graphite and graphene to one societal use of each.",
       "model": "Diamond's 3D network of strong covalent bonds gives hardness for cutting tools. Graphite has strong sheets but weak interlayer forces and delocalised electrons, enabling lubrication and electrodes. Graphene is a one-atom-thick conductive, strong sheet with potential in sensors and composites; cost and scalable manufacture limit some proposed uses."
      }
     ],
     "chem24": [
      {
       "type": "short",
       "marks": 10,
       "prompt": "Outline two sources of organic compounds and assess one benefit and one impact of products made from them.",
       "model": "Crude oil supplies petrochemical feedstocks, while living or renewable sources supply compounds through biomass, fermentation or extraction. Organic products include medicines, solvents, polymers and fuels with major health and material benefits. Toxicity, persistent waste, land use and carbon emissions depend on product and life cycle, so source alone does not guarantee sustainability."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Distinguish between primary, secondary and tertiary alcohols. Give the IUPAC name and structural formula of one example of each.",
       "model": "A primary alcohol is one in which the carbon atom joined to the -OH group is attached to at most one other carbon atom. Example: ethanol (CH₃CH₂OH) — the C bearing -OH is attached to one other C.\nA secondary alcohol is one in which the carbon atom joined to the -OH group is attached to two other carbon atoms. Example: propan-2-ol (CH₃CH(OH)CH₃) — the C bearing -OH is attached to two C atoms.\nA tertiary alcohol is one in which the carbon atom joined to the -OH group is attached to three other carbon atoms. Example: 2-methylpropan-2-ol ((CH₃)₃COH) — the C bearing -OH is attached to three C atoms."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Name each of the following compounds: (a) CH₃CH₂CHO, (b) CH₃COCH₂CH₃, (c) CH₃CH₂COOH, (d) CH₃CH₂COOCH₃, (e) CH₃CH₂CH₂Cl.",
       "model": "(a) CH₃CH₂CHO: 3-carbon chain; -CHO at end; named from propane → propanal.\n(b) CH₃COCH₂CH₃: 4-carbon chain; C=O on C2 (or C3 from other end — use lower number = C2); named from butane → butan-2-one (butanone).\n(c) CH₃CH₂COOH: 3-carbon chain (including carboxyl C as C1); -COOH functional group; named from propane → propanoic acid.\n(d) CH₃CH₂COOCH₃: propanoic acid part (CH₃CH₂COO-) + methyl group (-CH₃) attached to bridging O → methyl propanoate.\n(e) CH₃CH₂CH₂Cl: 3-carbon chain; Cl on C1 (number from Cl end) → 1-chloropropane."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Draw the structural formula and give the IUPAC name for the ester formed between ethanoic acid and ethanol. Write the equation for this esterification reaction and state the type of reaction it is.",
       "model": "The ester formed is ethyl ethanoate.\nStructural formula: CH₃-C(=O)-O-CH₂CH₃ (expanded: H₃C-C(=O)-O-C₂H₅)\nEquation: CH₃COOH + C₂H₅OH → CH₃COOC₂H₅ + H₂O (catalysed by H⁺ ions)\nNaming steps: (1) draw structural formula; (2) divide into carboxylic acid part (CH₃COO-) and alcohol part (-C₂H₅); (3) alkyl group on bridging O = ethyl; (4) acid part = ethanoic → ethanoate; (5) name = ethyl ethanoate.\nType of reaction: esterification is a condensation reaction (two molecules combine to form a larger molecule with loss of water) and also a substitution reaction."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Compare empirical, molecular, structural and 3D representations of an organic molecule and state what each leaves out.",
       "model": "An empirical formula gives simplest atom ratio; a molecular formula gives actual numbers but neither shows connectivity. A displayed or condensed structural formula shows bonding order with differing detail, while a 3D model shows geometry and spatial arrangement. No single representation fully shows electron density, motion, scale and bulk behaviour."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Explain why ethanol has a much higher boiling point than ethane, and why the lower members of the alcohol homologous series are completely miscible with water.",
       "model": "Boiling points: ethanol has a much higher boiling point than ethane (ethanol 78°C vs ethane −89°C) because ethanol molecules can form hydrogen bonds with each other through their -OH groups. This hydrogen bonding is due to the highly polar O-H bond; oxygen is much more electronegative than hydrogen. Ethane molecules can only form weak London dispersion forces between them, so much less energy is needed to separate them. Miscibility with water: the lower members of the alcohol series (methanol, ethanol, propan-1-ol) are completely miscible with water because the -OH group of the alcohol can form hydrogen bonds with water molecules. This attraction between alcohol and water molecules allows them to mix in all proportions."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Explain why pure ethanoic acid is often called glacial ethanoic acid and why ethanoic acid has a much higher boiling point than ethanol.",
       "model": "Glacial ethanoic acid: pure ethanoic acid has a melting point of 17°C. If the room temperature falls below 17°C, the ethanoic acid solidifies to an ice-like solid material. Because it looks like ice (glacial), it is commonly called glacial ethanoic acid. High boiling point: the boiling point of ethanoic acid (118°C) is much higher than that of ethanol (78°C). This is because carboxylic acid molecules can form a much greater amount of hydrogen bonding than alcohol molecules. In pure ethanoic acid, pairs of molecules form dimers held together by two hydrogen bonds each (between the -OH and the C=O of adjacent molecules). This extensive hydrogen bonding requires significantly more energy to break, hence the much higher boiling point."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain why carboxylic acids are acidic. In your answer, refer to the stability of the carboxylate ion and the inductive effect. Give two examples of reactions of ethanoic acid that demonstrate its acidic properties.",
       "model": "Carboxylic acids can lose a proton (H⁺) from the -COOH group. Two reasons:\n(1) Stability of carboxylate ion: when the carboxyl group loses a proton it forms the carboxylate ion (RCOO⁻). X-ray diffraction shows the two C-O bonds are equal length — the structure is a resonance hybrid. The negative charge is delocalised (spread over) three atoms (C and both O atoms). This resonance stabilisation gives the carboxylate ion extra stability, so carboxylic acids lose protons readily.\n(2) Inductive effect: electron-withdrawing groups on the R group (e.g., Cl atoms in CCl₃) pull electron density away from the carboxylate carbon, stabilising the negative carboxylate anion → stronger acid. Result: CCl₃COOH > HCOOH > CH₃COOH in acid strength.\nReactions demonstrating acidity: (i) CH₃COOH + NaOH → CH₃COONa + H₂O (reacts with base to form salt and water); (ii) 2CH₃COOH + Mg → Mg(CH₃COO)₂ + H₂ (reacts with reactive metal to release hydrogen gas, confirmed by lighted taper popping)."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "What is meant by a natural product? Give two examples of natural products with medicinal uses, naming the plant source and active compound in each case. Explain why it is important that natural products can be synthesised in the laboratory.",
       "model": "A natural product is an organic compound found occurring in nature.\nExamples: (1) Willow bark → active compound: salicylic acid → medicinal use: pain relief and blood thinning (converted to aspirin); (2) Opium poppy → active compounds: morphine and codeine → medicinal use: pain relief (morphine is a powerful painkiller; codeine is a milder painkiller and cough suppressant); (3) Cinchona bark → quinine → anti-malarial medicine.\nImportance of laboratory synthesis: (1) plant sources may be unreliable due to seasonal/weather/location factors; (2) chemists can improve the medicinal properties of natural products by modifying their structure (e.g., salicylic acid irritated the stomach; Felix Hoffmann (1897, Bayer) synthesised acetylsalicylic acid (aspirin) which retained the pain-relieving properties but without the stomach irritation — salicylic acid was the precursor); (3) large-scale production in the laboratory or by biotechnology (fermentation) allows medicines to be manufactured in sufficient quantities to meet demand."
      }
     ],
     "chem25": [
      {
       "type": "experiment",
       "marks": 12,
       "prompt": "Describe Experiment 25.3 — two tests used to distinguish between ethanal (an aldehyde) and propanone (a ketone). State the observation and explanation in each case.",
       "model": "(i) Dilute acidified KMnO₄: add dilute acidified potassium permanganate to separate test tubes of ethanal and propanone; place in warm water bath. Observation with ethanal: purple colour changes to colourless (ethanal oxidised to ethanoic acid; MnO₄⁻ → Mn²⁺). Observation with propanone: no colour change. Explanation: ketones cannot be oxidised by dilute acidified KMnO₄ because this mild oxidising agent cannot break the C-C bonds required to oxidise a ketone.\n(ii) Fehling's reagent: mix Fehling's A and B to get clear royal blue solution (Cu²⁺ ions); add to test tubes of ethanal and propanone; warm in water bath. Observation with ethanal: brick-red precipitate forms (Cu₂O; Cu²⁺ reduced to Cu⁺). Observation with propanone: no colour change; no precipitate. Explanation: Fehling's is a weak oxidising agent; it can oxidise aldehydes (which are good reducing agents) but cannot oxidise ketones."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Describe chemical tests that distinguish an aldehyde from a ketone and demonstrate the acidic nature of a carboxylic acid.",
       "model": "Warm aldehyde with Fehling's solution to form a brick-red precipitate; a typical ketone gives no such oxidation result. Add carbonate or hydrogencarbonate to a carboxylic acid: carbon dioxide effervescence occurs and can turn limewater milky. Use fresh small-scale reagents and appropriate heating and disposal."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Classify five common types of organic reaction and give a defining change for each.",
       "model": "Addition joins groups across a multiple bond; substitution replaces one atom or group; elimination removes groups and forms a multiple bond; oxidation increases bonding to oxygen or decreases hydrogen; condensation joins molecules with loss of a small molecule. A reaction may fit more than one description depending on the feature analysed."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "An alcohol is converted to an alkene and then to a dibromoalkane. Identify and explain both reaction types.",
       "model": "Alcohol to alkene is elimination because water is removed and a carbon-carbon double bond forms. Alkene to dibromoalkane is addition because bromine adds across the pi bond, replacing it with two carbon-bromine bonds. Bromine decolourisation provides evidence for the second reaction."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Explain how you would analyse an unfamiliar organic reaction scheme to predict missing reagents or products.",
       "model": "Identify each functional group and compare bonds before and after every arrow. Classify the change as addition, substitution, elimination, oxidation, reduction, esterification or hydrolysis, then apply valency and atom conservation. Check conditions and plausible intermediates and verify that the proposed product matches the named test or observation."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Predict a two-step route from ethene to ethanoic acid and identify the reaction type at each step.",
       "model": "Hydrate ethene by adding water across the double bond to form ethanol; this is an addition reaction. Oxidise ethanol under suitable controlled conditions to ethanal and then ethanoic acid. The carbon skeleton is retained while bonding to oxygen increases and hydrogen decreases."
      },
      {
       "type": "experiment",
       "marks": 12,
       "prompt": "Describe Experiment 25.1 — the preparation of the ester methyl propanoate from propanoic acid and methanol using the reflux method. Include why a water bath is used and how the product is isolated.",
       "model": "Equation: C₂H₅COOH + CH₃OH ⇌ C₂H₅COOCH₃ + H₂O (catalysed by concentrated H₂SO₄).\nRefluxing: methanol, propanoic acid, concentrated H₂SO₄ (catalyst and dehydrating agent), and anti-bumping granules are added to a round-bottomed flask. A Liebig condenser is attached vertically on top. The flask is heated by a water bath. Vapours of the volatile liquids rise, are cooled in the condenser, and drip back into the flask. This keeps the liquid at its boiling point without loss of vapour. Esterification is an equilibrium reaction; refluxing provides energy while preventing evaporation of reactants.\nWater bath (not Bunsen): methanol and methyl propanoate are volatile and flammable; a Bunsen burner could cause a fire; the water bath (maximum 100°C) gives better temperature control.\nAnti-bumping granules: provide nucleation sites for bubble formation, preventing violent bumping of the liquid.\nIsolation: after heating, cooled mixture poured into separating funnel with water. Shake: upper organic layer (methyl propanoate) + lower aqueous layer (propanoic acid, methanol, H₂SO₄). Aqueous layer discarded. Na₂CO₃ solution added to neutralise remaining acids (prevents acid-catalysed hydrolysis); CO₂ evolved; tap opened to release pressure. Lower aqueous layer discarded. Organic layer transferred to dry conical flask; anhydrous CaCl₂ added (drying agent); liquid decanted. Purified ester may be further purified by distillation (methyl propanoate BP ~79.8°C)."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Describe the preparation and purification of an ester from a carboxylic acid and an alcohol.",
       "model": "Heat the acid and alcohol with a small amount of concentrated acid catalyst under reflux or the specified safe method. Cool, transfer and separate the ester layer, washing or neutralising residual acid as directed, then dry and purify by distillation if required. The reaction is reversible condensation producing ester and water; control flammable reagents and corrosive catalyst."
      },
      {
       "type": "experiment",
       "marks": 12,
       "prompt": "Describe Experiment 25.4A — the synthesis of benzoic acid by oxidation of phenylmethanol (benzyl alcohol) using KMnO₄ under alkaline conditions. Include observations, equation, and isolation of the product.",
       "model": "Introduction: Benzoic acid is a white crystalline solid used as a food preservative (sodium benzoate, E211). It is prepared by oxidising phenylmethanol with acidified potassium permanganate.\nEquation: 3C₆H₅CH₂OH + 4KMnO₄ → 3C₆H₅COOH + 4MnO₂ + H₂O + 4KOH\nProcedure: Phenylmethanol, a saturated solution of KMnO₄ and Na₂CO₃ solution are heated in a conical flask in a boiling water bath for ~20 minutes. Na₂CO₃ ensures alkaline conditions (reaction works best at alkaline pH). Observation: purple colour changes to brown (MnO₂ precipitate forms). Using a dropper, sodium sulfite solution (Na₂SO₃) is added to the conical flask until the brown MnO₂ precipitate dissolves fully (Mn⁴⁺ + 2e⁻ → Mn²⁺); white crystals of benzoic acid become visible. In the fume cupboard, concentrated HCl is added to: (i) convert sodium benzoate to benzoic acid; (ii) neutralise excess Na₂CO₃ and KOH; (iii) provide acidic medium. The conical flask is placed in ice (benzoic acid has low solubility in cold water → precipitates). Crystals isolated by vacuum filtration (Buchner flask/funnel). Crystals washed with ice-cold water, dried in a desiccator. Mass of crystals measured; % yield calculated."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Explain how yield, melting point and purity should be determined after synthesising benzoic acid.",
       "model": "Isolate crystals by filtration after cooling, wash with a small amount of cold solvent and dry to constant mass. Calculate percentage yield from actual dry moles divided by theoretical moles. Measure melting range with suitable apparatus: a sharp value close to the accepted point supports purity, while impurities commonly broaden and depress it."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Describe the mechanism of the monochlorination of methane, giving the three stages (initiation, propagation, termination) and the equations for each step.",
       "model": "Initiation: UV light causes homolytic fission of the Cl-Cl bond, producing two chlorine free radicals. Cl₂ → 2Cl• (A free radical is any atom or group of atoms with an unpaired electron.)\nPropagation 1: Cl• + CH₄ → HCl + •CH₃ (methyl free radical)\nPropagation 2: •CH₃ + Cl₂ → CH₃Cl + Cl• (chloromethane + new Cl radical)\nSteps 2 and 3 form a chain reaction: a product of one step (Cl•) is a reactant in another step. Thousands of CH₃Cl molecules are produced from one Cl₂ molecule broken by one photon of UV light.\nTermination: pairs of free radicals combine: Cl• + Cl• → Cl₂; •CH₃ + Cl• → CH₃Cl; •CH₃ + •CH₃ → C₂H₆. This stops the chain reaction."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Describe the mechanism of the ionic addition of chlorine to ethene (the four steps), and give one piece of evidence that supports this mechanism.",
       "model": "Step 1 — Polarisation: the C=C double bond is a region of high electron density. As a Cl₂ molecule approaches, repulsion from the pi electrons causes the Cl-Cl bond to become polarised (Clδ⁺-Clδ⁻).\nStep 2 — Heterolytic fission: the induced polarisation becomes so great that the Cl-Cl bond breaks heterolytically (both electrons go to one Cl) → Cl⁺ and Cl⁻ ions form.\nStep 3 — Carbonium ion formation: the Cl⁺ species attacks the pi bond, bonds to one carbon atom. The other carbon atom has lost one outer electron → becomes a positively charged carbonium ion (carbocation).\nStep 4 — Ionic addition: the Cl⁻ ion attacks the carbonium ion → forms 1,2-dichloroethane.\nEvidence: when ethene reacts with Cl₂ water (instead of pure Cl₂), both 1,2-dichloroethane AND 2-chloroethanol are produced. 2-chloroethanol forms when water molecules attack the carbonium ion intermediate. This would be impossible if both Cl atoms added simultaneously — it proves the existence of a positively charged carbonium ion intermediate."
      },
      {
       "type": "short",
       "marks": 10,
       "prompt": "Use organic examples to distinguish a redox reaction from an acid-base reaction.",
       "model": "Oxidising ethanol to ethanoic acid changes carbon oxidation state by increasing bonding to oxygen and decreasing hydrogen; electrons are transferred overall. Ethanoic acid reacting with hydroxide transfers a proton to form ethanoate and water, so it is Brønsted-Lowry acid-base chemistry. Some reactions may involve both, so electron and proton changes should be checked separately."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain how soap removes grease from the skin. Include the terms hydrophobic, hydrophilic, micelle, and emulsification.",
       "model": "Soap consists of the sodium or potassium salts of long-chain carboxylic acids. Each soap molecule has two parts: (1) a hydrophilic head (the polar carboxylate group COO⁻Na⁺, 'water-loving' — dissolves in water); (2) a hydrophobic tail (the long non-polar hydrocarbon chain, 'water-hating' — does not dissolve in water). When soap is added to water, it lowers the surface tension of the water, allowing it to spread out more easily and mix better with oil and grease. When you wash your hands: (1) the hydrophobic tails of the soap molecules align themselves with the oil and grease on the skin; (2) the hydrophilic heads remain in the water; (3) a spherical soap-oil micelle is formed, with the oil droplet in the centre, hydrophobic tails pointing inward and hydrophilic heads pointing outward into the water; (4) emulsification occurs — the oily substances are broken into tiny droplets that are dispersed and suspended in water; (5) rinsing removes the soap-oil micelles (and the trapped dirt and microorganisms) and the hands are left clean."
      },
      {
       "type": "short",
       "marks": 12,
       "prompt": "Outline the preparation of soap and explain how the amount of sodium hydroxide affects the final mixture.",
       "model": "Heat a measured fat or oil with sodium hydroxide so triglyceride ester bonds hydrolyse to glycerol and sodium salts of fatty acids. Salt may be added to precipitate soap, which is filtered, washed and dried. Insufficient NaOH leaves unreacted fat; excess leaves corrosive alkali requiring careful calculation, washing and safety control."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "Explain what is meant by an addition polymer and describe the structure and properties of PVC (poly(chloroethene)).",
       "model": "An addition polymer is a polymer formed by addition reactions in which monomer molecules containing C=C double bonds join together to form a long chain molecule. Usually only one type of monomer is involved. An addition reaction is one in which two or more molecules react together to form a single molecule.\nPVC: PVC (poly(chloroethene) or polyvinyl chloride) is made from chloroethene (vinyl chloride) monomers. In each chloroethene molecule the C=C double bond opens and molecules join in a long chain. Each repeating unit has the structure -CH₂-CHCl-. The Cl atom on each monomer unit polarises the C-Cl bond, giving rise to permanent dipole-dipole attractive forces between the polymer chains. This makes PVC a strong, rigid plastic. PVC is used to manufacture window frames, doors, gutters, drainpipes and bank cards. Like other addition polymers, PVC is non-biodegradable because microorganisms cannot break down the strong carbon-carbon bonds in the polymer backbone."
      }
     ],
     "chem26": [
      {
       "type": "short",
       "marks": 4,
       "prompt": "Define the terms (a) limiting reactant and (b) reactant in excess.",
       "model": "(a) The limiting reactant (limiting reagent) is the substance that is used up first in a chemical reaction and therefore determines the maximum amount of product that can be formed. Once the limiting reactant is used up, the reaction stops even if other reactants are still available.\n(b) The reactant in excess is the substance that is not completely used up in the reaction. The excess reactant is present in a greater amount than required to react with the limiting reactant; some of it always remains unreacted at the end of the reaction."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "A student reacted 10 g of iron with 10 g of sulfur: Fe + S → FeS. (a) Identify the limiting reactant, showing your working. (b) Calculate the maximum mass of iron sulfide that could be formed. (Mᵣ: Fe = 55.85, S = 32.07, FeS = 87.92)",
       "model": "(a) n(Fe) = 10/55.85 = 0.18 mol; n(S) = 10/32.07 = 0.31 mol. The balanced equation shows Fe:S = 1:1 (equal moles required). 0.18 mol Fe would need 0.18 mol S to react completely. We have 0.31 mol S — more than enough — so S is in excess and Fe is the limiting reactant.\n(b) 1 mol Fe → 1 mol FeS; 0.18 mol Fe → 0.18 mol FeS. Mass FeS = 0.18 × 87.92 = 15.83 g. Maximum mass of iron sulfide = 15.83 g."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Define theoretical yield and actual yield. Explain why the actual yield of a product is usually less than the theoretical yield.",
       "model": "Theoretical yield: the maximum amount of product that can be formed from a given mass of reactants, assuming that the reaction goes to completion (100% conversion of the limiting reactant into the desired product). Calculated from the balanced equation and mole ratios.\nActual yield: the amount of product that is obtained in practice from a chemical reaction under laboratory or industrial conditions.\nThe actual yield is usually less than the theoretical yield because: (1) the reaction may not go to completion (many reactions are reversible equilibrium reactions); (2) side reactions may occur, producing unwanted by-products; (3) some product may be lost during the purification and isolation steps."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "Starting with 20 g of ethanol, a student prepared ethene: C₂H₅OH → C₂H₄ + H₂O. If the student obtained 8 g of ethene, calculate the percentage yield of ethene. (Mᵣ: C₂H₅OH = 46.07, C₂H₄ = 28.05)",
       "model": "Step 1: Calculate moles of ethanol used: n(ethanol) = 20/46.07 = 0.434 mol.\nStep 2: Calculate theoretical yield of ethene: from the equation, 1 mol ethanol → 1 mol ethene; therefore 0.434 mol ethanol → 0.434 mol ethene. Theoretical mass of ethene = 0.434 × 28.05 = 12.17 g.\nStep 3: % yield = (actual yield / theoretical yield) × 100 = (8.0/12.17) × 100 = 65.7%."
      },
      {
       "type": "short",
       "marks": 8,
       "prompt": "A student oxidised 2 cm³ of phenylmethanol (density = 1.04 g/cm³) with 6.32 g of KMnO₄. The equation for the reaction is: 3C₆H₅CH₂OH + 4KMnO₄ → 3C₆H₅COOH + 4MnO₂ + H₂O + 4KOH. After recrystallisation, 1.05 g of benzoic acid was obtained. (i) Identify the limiting reactant. (ii) Calculate the percentage yield of benzoic acid. (Mᵣ: phenylmethanol = 108.13, KMnO₄ = 158.04, benzoic acid = 122.12)",
       "model": "(i) Identifying the limiting reactant:\nMass of phenylmethanol = density × volume = 1.04 × 2 = 2.08 g.\nn(phenylmethanol) = 2.08/108.13 = 0.019 mol.\nn(KMnO₄) = 6.32/158.04 = 0.040 mol.\nFrom balanced equation: mole ratio is 3 phenylmethanol : 4 KMnO₄. So 1 mol phenylmethanol reacts with 4/3 mol KMnO₄. 0.019 mol phenylmethanol needs 0.019 × (4/3) = 0.0253 mol KMnO₄. We have 0.040 mol KMnO₄ (more than enough) → KMnO₄ is in excess → phenylmethanol is the limiting reactant.\n(ii) % yield:\nFrom balanced equation: 3 mol phenylmethanol → 3 mol benzoic acid (1:1 ratio). 0.019 mol phenylmethanol → 0.019 mol benzoic acid. Theoretical yield = 0.019 × 122.12 = 2.32 g.\n% yield = (1.05/2.32) × 100 = 45.26%."
      },
      {
       "type": "short",
       "marks": 6,
       "prompt": "2.3 cm³ of ethanol (density = 0.8 g/cm³) was used to prepare ethene: C₂H₅OH → C₂H₄ + H₂O. If a 15% yield was obtained, calculate the volume of ethene (in cm³) collected at room temperature and pressure. (Molar volume at r.t.p. = 24.0 L; Mᵣ: C₂H₅OH = 46.07)",
       "model": "Step 1: mass ethanol = density × volume = 0.8 × 2.3 = 1.84 g.\nStep 2: n(ethanol) = 1.84/46.07 = 0.040 mol.\nStep 3: 1 mol ethanol → 1 mol ethene; 0.040 mol → 0.040 mol ethene. Theoretical volume of ethene = 0.040 × 24.0 = 0.96 L.\nStep 4: Actual volume = (15/100) × 0.96 = 0.144 L = 144 cm³."
      }
     ]
    };
    Object.keys(REVIEW_QUESTIONS).forEach(function (id) {
      ch(id).learningOutcomes[0].questions = REVIEW_QUESTIONS[id];
    });
  })();

})();
