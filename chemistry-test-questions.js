// Targeted exam-style questions for Chemistry outcomes lacking a written Test item.
// Requires chemistry-content.js to be loaded first. Existing authored questions are
// preserved; these additions only fill uncovered outcomes.
(function () {
  if (typeof COURSE_DATA === "undefined") return;

  function q(marks, prompt, model) {
    return { type: "short", marks: marks, prompt: prompt, model: model };
  }

  var ADDITIONS = {
    "chem14-3": [
      q(10, "Design a displacement investigation to place magnesium, zinc and copper in order of reducing strength.", "Place cleaned equal-sized metal samples into equal volumes and concentrations of the other metal-ion solutions under the same conditions. Record coating, colour or temperature evidence and use ionic equations. A metal that displaces another ion is the stronger reducing agent. Expected order is magnesium, zinc, copper; include repeats, eye protection and safe disposal."),
    ],
    "chem15-2": [
      q(12, "Outline how a redox titration could determine the percentage by mass of elemental iron in an iron tablet.", "Accurately weigh and dissolve a tablet, ensuring iron is in the required oxidation state, and make to a known volume. Pipette an aliquot and titrate with standard oxidant to the specified endpoint, obtaining concordant titres. Use the balanced redox equation to find moles of iron in the aliquot, scale to the tablet, convert to mass and calculate percentage."),
    ],
    "chem20-5": [
      q(12, "Explain the operation of a lithium-ion cell during discharge and assess two life-cycle impacts.", "Lithium ions move through the electrolyte from the negative electrode to the positive electrode while electrons travel through the external circuit and do electrical work; charging reverses the processes using supplied energy. Mining lithium, nickel or cobalt can damage ecosystems and communities, while manufacture uses energy. Long service, responsible sourcing and material recovery reduce impacts but recycling is technically demanding."),
      q(8, "Explain why charging a lithium-ion cell is not the same as simply storing electrons inside it.", "The charger drives a non-spontaneous redox process. Electrons move through the external circuit while lithium ions migrate through the electrolyte and are inserted into electrode material, storing chemical potential in changed electrode states. Charge balance is maintained; loose electrons do not accumulate in the cell."),
    ],
    "chem20-6": [
      q(10, "Evaluate a chemistry-based response to climate change through the themes of sustainability, health and technology.", "Green hydrogen can store renewable energy and produce water at use, potentially reducing combustion pollution and carbon emissions. Electrolysis requires large amounts of low-carbon electricity, storage is difficult and current production often uses fossil fuels. A sound evaluation compares full life-cycle emissions, resource demand, safety, cost and the applications where alternatives are weaker."),
      q(8, "Outline a research strategy for comparing two claims about a sustainable chemical technology.", "Define measurable criteria such as life-cycle emissions, efficiency, toxicity, resource use and cost. Use recent peer-reviewed studies and transparent institutional data, evaluate system boundaries and conflicts of interest and compare like with like. Report uncertainty and distinguish laboratory potential from demonstrated large-scale performance."),
    ],
    "chem21-1": [
      q(10, "Use bond enthalpies to explain why a reaction may be exothermic or endothermic.", "Breaking reactant bonds absorbs energy, while forming product bonds releases energy. The approximate enthalpy change is the sum of bond enthalpies broken minus the sum formed. If formation releases more than breaking requires, ΔH is negative and the reaction is exothermic; the reverse gives a positive endothermic value."),
    ],
    "chem22-4": [
      q(10, "Compare a conventional chemical cell with a hydrogen fuel cell.", "Both use spatially separated redox half-reactions to drive electrons through an external circuit. A conventional cell stores finite reactants internally and eventually discharges, while a fuel cell operates while hydrogen and oxygen are supplied and products removed. Fuel cells can produce water at use, but hydrogen production, storage, catalysts and infrastructure affect overall sustainability."),
    ],
    "chem22-6": [
      q(10, "Assess one application of electrochemistry in sustainable technology.", "Electrolysers can use renewable electricity to produce hydrogen that stores energy and supplies industry without carbon at point of use. Efficiency losses, water and catalyst needs, difficult storage and fossil-derived electricity can reduce benefit. The application is strongest where direct electrification is impractical and life-cycle emissions are verified."),
    ],
    "chem23-1": [
      q(10, "Outline the principal sources of hydrocarbons and explain why their uses extend beyond fuels.", "Crude oil and natural gas are the main fossil sources, separated and processed into useful fractions and feedstocks; biomass can supply some renewable hydrocarbons or related molecules. Hydrocarbons fuel transport and heating but also provide starting materials for polymers, solvents, detergents and pharmaceuticals. Their value depends on structure and chemical reactivity as well as combustion."),
    ],
    "chem23-2": [
      q(10, "Assess one major societal impact of extensive hydrocarbon use.", "Combustion supplied dense, transportable energy that enabled industrialisation and mobility, but releases carbon dioxide and often air pollutants affecting climate and health. Extraction and spills damage ecosystems and economies become dependent on finite resources. Efficiency, alternative energy and using scarce hydrocarbons as chemical feedstocks can reduce, not instantly remove, the impact."),
    ],
    "chem23-3": [
      q(12, "Describe the laboratory preparation of ethene from ethanol and the tests used to investigate the product.", "Pass ethanol vapour over a heated suitable catalyst or dehydrate it under the approved method, collect ethene over water and discard initial gas contaminated with air. Ethene is colourless and combustible and rapidly decolourises bromine water by addition across the double bond. Use small quantities, eye protection and strict control of flammable vapour and heat."),
    ],
    "chem23-4": [
      q(12, "Compare alkanes, alkenes and alkynes in composition, bonding, shape and characteristic reactions.", "Alkanes are saturated with C–C single sigma bonds and undergo combustion and substitution. Alkenes contain a C=C sigma-plus-pi bond with trigonal-planar carbon and undergo electrophilic addition. Alkynes contain a linear C≡C with one sigma and two pi bonds and also add reagents. Unsaturation increases characteristic addition reactivity."),
      q(8, "Explain why members of one homologous hydrocarbon series have similar chemical but gradually changing physical properties.", "They share the same functional bonding pattern and general formula, so react in similar ways. Increasing chain length raises electron number, surface contact and London dispersion forces, increasing boiling point and viscosity and lowering volatility. Branching changes contact area and can lower boiling point among isomers."),
    ],
    "chem23-6": [
      q(8, "Explain the relative chemical stability of alkanes compared with alkenes.", "Alkanes contain strong localised carbon-carbon and carbon-hydrogen sigma bonds and have no electron-rich pi bond, so many reactions require high activation energy or radical conditions. An alkene's exposed pi electrons are more weakly held and readily attacked by electrophiles, allowing addition under milder conditions."),
    ],
    "chem23-7": [
      q(10, "Explain how 3D molecular models show both the usefulness and limitations of representations of hydrocarbons.", "Models show tetrahedral, trigonal-planar or linear geometry, bond rotation and different connectivity in isomers. They help distinguish chain and positional arrangements that flat formulae hide. Ball-and-stick models exaggerate bond gaps and fixed sizes, electron density is absent and molecules are dynamic, so the model is not a literal scale image."),
    ],
    "chem23-11": [
      q(10, "Relate the structures of diamond, graphite and graphene to one societal use of each.", "Diamond's 3D network of strong covalent bonds gives hardness for cutting tools. Graphite has strong sheets but weak interlayer forces and delocalised electrons, enabling lubrication and electrodes. Graphene is a one-atom-thick conductive, strong sheet with potential in sensors and composites; cost and scalable manufacture limit some proposed uses."),
    ],
    "chem24-1": [
      q(10, "Outline two sources of organic compounds and assess one benefit and one impact of products made from them.", "Crude oil supplies petrochemical feedstocks, while living or renewable sources supply compounds through biomass, fermentation or extraction. Organic products include medicines, solvents, polymers and fuels with major health and material benefits. Toxicity, persistent waste, land use and carbon emissions depend on product and life cycle, so source alone does not guarantee sustainability."),
    ],
    "chem24-3": [
      q(10, "Compare empirical, molecular, structural and 3D representations of an organic molecule and state what each leaves out.", "An empirical formula gives simplest atom ratio; a molecular formula gives actual numbers but neither shows connectivity. A displayed or condensed structural formula shows bonding order with differing detail, while a 3D model shows geometry and spatial arrangement. No single representation fully shows electron density, motion, scale and bulk behaviour."),
    ],
    "chem25-1": [
      q(12, "Describe chemical tests that distinguish an aldehyde from a ketone and demonstrate the acidic nature of a carboxylic acid.", "Warm aldehyde with Fehling's solution to form a brick-red precipitate; a typical ketone gives no such oxidation result. Add carbonate or hydrogencarbonate to a carboxylic acid: carbon dioxide effervescence occurs and can turn limewater milky. Use fresh small-scale reagents and appropriate heating and disposal."),
    ],
    "chem25-2": [
      q(12, "Classify five common types of organic reaction and give a defining change for each.", "Addition joins groups across a multiple bond; substitution replaces one atom or group; elimination removes groups and forms a multiple bond; oxidation increases bonding to oxygen or decreases hydrogen; condensation joins molecules with loss of a small molecule. A reaction may fit more than one description depending on the feature analysed."),
      q(8, "An alcohol is converted to an alkene and then to a dibromoalkane. Identify and explain both reaction types.", "Alcohol to alkene is elimination because water is removed and a carbon-carbon double bond forms. Alkene to dibromoalkane is addition because bromine adds across the pi bond, replacing it with two carbon-bromine bonds. Bromine decolourisation provides evidence for the second reaction."),
    ],
    "chem25-3": [
      q(12, "Explain how you would analyse an unfamiliar organic reaction scheme to predict missing reagents or products.", "Identify each functional group and compare bonds before and after every arrow. Classify the change as addition, substitution, elimination, oxidation, reduction, esterification or hydrolysis, then apply valency and atom conservation. Check conditions and plausible intermediates and verify that the proposed product matches the named test or observation."),
      q(8, "Predict a two-step route from ethene to ethanoic acid and identify the reaction type at each step.", "Hydrate ethene by adding water across the double bond to form ethanol; this is an addition reaction. Oxidise ethanol under suitable controlled conditions to ethanal and then ethanoic acid. The carbon skeleton is retained while bonding to oxygen increases and hydrogen decreases."),
    ],
    "chem25-4": [
      q(12, "Describe the preparation and purification of an ester from a carboxylic acid and an alcohol.", "Heat the acid and alcohol with a small amount of concentrated acid catalyst under reflux or the specified safe method. Cool, transfer and separate the ester layer, washing or neutralising residual acid as directed, then dry and purify by distillation if required. The reaction is reversible condensation producing ester and water; control flammable reagents and corrosive catalyst."),
    ],
    "chem25-5": [
      q(12, "Explain how yield, melting point and purity should be determined after synthesising benzoic acid.", "Isolate crystals by filtration after cooling, wash with a small amount of cold solvent and dry to constant mass. Calculate percentage yield from actual dry moles divided by theoretical moles. Measure melting range with suitable apparatus: a sharp value close to the accepted point supports purity, while impurities commonly broaden and depress it."),
    ],
    "chem25-7": [
      q(10, "Use organic examples to distinguish a redox reaction from an acid-base reaction.", "Oxidising ethanol to ethanoic acid changes carbon oxidation state by increasing bonding to oxygen and decreasing hydrogen; electrons are transferred overall. Ethanoic acid reacting with hydroxide transfers a proton to form ethanoate and water, so it is Brønsted-Lowry acid-base chemistry. Some reactions may involve both, so electron and proton changes should be checked separately."),
    ],
    "chem25-9": [
      q(12, "Outline the preparation of soap and explain how the amount of sodium hydroxide affects the final mixture.", "Heat a measured fat or oil with sodium hydroxide so triglyceride ester bonds hydrolyse to glycerol and sodium salts of fatty acids. Salt may be added to precipitate soap, which is filtered, washed and dried. Insufficient NaOH leaves unreacted fat; excess leaves corrosive alkali requiring careful calculation, washing and safety control."),
    ],
  };

  Object.keys(ADDITIONS).forEach(function (outcomeId) {
    COURSE_DATA.chapters.some(function (chapter) {
      var outcome = (chapter.learningOutcomes || []).find(function (item) { return item.id === outcomeId; });
      if (!outcome) return false;
      outcome.questions = (outcome.questions || []).concat(ADDITIONS[outcomeId]);
      return true;
    });
  });
})();
