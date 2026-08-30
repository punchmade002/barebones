// Build exam-ready chapter notes from the project's authored content sources.
//
// Flashcards remain atomic retrieval prompts. Notes are deliberately different:
// they connect concepts, retain every examinable detail, add application and
// examples, and show how the material is developed into a full-mark response.
(function () {
  if (typeof COURSE_DATA === "undefined") return;

  var supportedSubjects = new Set(["geography", "home-economics", "pe"]);
  var decks = globalThis.FLASHCARDS_DB || {};
  var examQuestions = Array.isArray(globalThis.EXAM_QUESTIONS_DB) ? globalThis.EXAM_QUESTIONS_DB : [];

  var chapterOverview = {
    // Geography
    "geo-plate-tectonics": "Plate tectonics links the layered structure of Earth to crustal movement. A complete explanation should move from mantle convection, ridge push and slab pull to continental drift and sea-floor spreading, then compare constructive, destructive and conservative boundaries using located examples such as the Mid-Atlantic Ridge, the Andes and the San Andreas Fault.",
    "geo-volcanoes-earthquakes": "Volcanoes and earthquakes occur because stress and magma are concentrated at plate margins and hotspots. High-mark answers connect a named tectonic setting to the sequence of events, resulting landforms, spatial distribution, impacts and human responses; use a developed case study rather than a list of effects.",
    "geo-rocks-weathering": "The rock cycle continuously transforms igneous, sedimentary and metamorphic rocks through endogenic and exogenic processes. Explain weathering in situ, distinguish it from erosion and mass movement, and develop named processes such as freeze-thaw action, carbonation and soil creep with conditions, sequence and resulting landforms.",
    "geo-glaciation": "Glacial landscapes reflect erosion, transport and deposition by moving ice. Trace how plucking and abrasion create erosional features, how till is transported and deposited, and how landforms such as corries, arêtes, U-shaped valleys, drumlins and eskers provide evidence of former glaciation; link isostatic adjustment to crustal recovery after melting.",
    "geo-rivers": "A river system transfers water and sediment through a drainage basin from source to mouth. Full explanations connect velocity, discharge, gradient and load to erosion, transportation and deposition, then show the ordered formation of landforms such as waterfalls, meanders, oxbow lakes, floodplains and deltas and evaluate flood-management choices.",
    "geo-sea": "Coastal landscapes result from the interaction of waves, geology, sediment supply and human management. Distinguish constructive and destructive waves, explain erosion and longshore drift step by step, and develop the formation of cliffs, caves, arches, stacks, beaches, spits and bars before evaluating hard and soft engineering.",
    "geo-aerial-photographs": "Aerial-photograph questions reward systematic evidence. State photograph type and orientation, locate features using foreground/middle distance/background and compass directions, identify relief, drainage, settlement, transport and land use from visible evidence, and support every inference with a precise feature from the image.",
    "geo-mapwork": "Mapwork combines accurate technique with geographical interpretation. Master four- and six-figure grid references, scale and distance, direction, contour patterns, gradient, cross-sections and conventional symbols; in descriptive answers identify a pattern, quote map evidence and explain the physical or human reason for it.",
    "geo-weather-climate": "Weather is the short-term condition of the atmosphere, while climate is the long-term average. Connect unequal heating to pressure and global circulation, interpret isobars, fronts, wind and satellite imagery, and explain the sequence of weather associated with depressions and anticyclones using evidence from a synoptic chart.",
    "geo-graph-skills": "Data questions require selection, calculation, presentation and interpretation. Choose a graph suited to the variable, use correct scales, units, titles and labels, calculate totals, percentages and change accurately, and describe patterns with quoted figures before explaining anomalies or relationships without claiming causation from correlation alone.",
    "geo-region-concept": "A region is an area unified by selected characteristics rather than a fixed natural fact. Compare physical, cultural, administrative, functional and perceptual regions, explain how boundaries and scale vary, and apply core-periphery ideas while recognising that regions overlap and change over time.",
    "geo-region-ireland": "Irish regional contrasts arise from cumulative differences in accessibility, population, services, investment and physical resources. Compare the Greater Dublin Area with a peripheral western region across primary, secondary and tertiary activity, using named places and statistics while explaining how infrastructure and policy reinforce or reduce inequality.",
    "geo-region-european": "European core and peripheral regions differ in market access, population density, infrastructure, urbanisation and economic structure. Use named European regions to compare agriculture, industry and services, explain the historical and policy causes of uneven development, and show why a region may contain both core and peripheral areas.",
    "geo-region-continental": "A continental or subcontinental study must connect large-scale physical systems to population and economic activity. Organise the answer around relief, climate, soils, resources, settlement and development, use named sub-regions and located examples, and explain internal contrasts instead of treating the whole continent as uniform.",
    "geo-economic-development": "Development is multidimensional, so GDP or GNI alone cannot show quality of life or distribution. Compare economic, social and composite indicators such as income, life expectancy, literacy and HDI, examine the causes and consequences of unequal wealth, and evaluate aid, trade, debt relief and sustainable development using contrasting countries.",
    "geo-economic-activities": "Primary, secondary and tertiary activities form an interdependent production chain. Explain location using physical, labour, market, transport, capital and policy factors, then develop a named agriculture, fishing, manufacturing or service example and assess multiplier effects, linkages and regional change.",
    "geo-economic-environment": "Economic activity creates benefits and costs across environmental, social and economic dimensions. A balanced answer identifies the activity, explains specific impacts through causal chains, distinguishes short- and long-term effects, and evaluates regulation, planning, technology and sustainable management rather than merely listing positives and negatives.",
    "geo-economic-eu": "EU membership reshaped Ireland through access to the single market, free movement, investment and regional and sectoral policies. Explain CAP and fisheries policy as mechanisms with winners, costs and reforms, use Irish examples, and evaluate how EU funding and regulation influence both development and environmental management.",
    "geo-economic-globalisation": "Globalisation intensifies flows of capital, goods, services, people and information. Explain why MNCs choose locations, distinguish advantages such as employment, exports and skills from risks such as profit repatriation, dependency and environmental pressure, and use a named company or Irish region to support each developed point.",
    "geo-population-migration": "Population changes through births, deaths and migration and is represented by density, distribution and age-sex structure. Use demographic-transition logic, distinguish push and pull factors and voluntary from forced migration, and develop source and destination impacts with a named migration flow or rapidly growing population case study.",
    "geo-urban": "Settlements develop according to site, situation and function and change through urbanisation, suburbanisation, counter-urbanisation and renewal. Apply land-use models cautiously, explain problems such as sprawl, congestion, segregation and housing pressure, and evaluate planning responses through a named city or rural settlement example.",
    "geo-option-atmosphere-ocean": "The atmosphere and oceans redistribute solar energy and moisture and therefore control weather and climate. Connect radiation balance, circulation, ocean currents, humidity, condensation and precipitation, then apply the system to a climatic environment and evaluate human influence and hazards using process-based explanation.",
    "geo-option-culture-identity": "Identity is expressed through both physical territory and cultural indicators such as language, religion, ethnicity and nationality. Explain how identities are constructed and contested at different scales, use Switzerland or another detailed case study, and evaluate the roles of borders, migration, globalisation and political power.",
    "geo-option-geoecology": "Geoecology links soil-forming factors, soil profiles, climate, vegetation and nutrient cycling. Develop one soil and two biome case studies by explaining processes and adaptations, use accurate profile or cycle terminology, and assess how human interference changes productivity, biodiversity and sustainability.",
    "geo-option-global-interdependence": "Global interdependence means development in one place is shaped by trade, finance, aid, technology and political relationships elsewhere. Compare development models, explain unequal terms of exchange and dependency, and evaluate empowerment and sustainability strategies through named countries, agencies or projects.",

    // Home Economics
    "hom-carbohydrates": "Carbohydrates should be studied from chemistry to health: composition and classification, sources, digestion to glucose, absorption, energy release, glycogen and fat storage, dietary fibre and the effects of deficiency or excess. In food-science answers also connect starch and sugar to gelatinisation, dextrinisation, caramelisation and their practical cooking applications.",
    "hom-proteins": "Link amino-acid structure and peptide bonding to protein classification, biological value, complementation, digestion and body functions. For full marks explain denaturation, coagulation, gluten formation and Maillard browning with conditions and food examples, and relate intake to growth, repair, energy balance and deficiency.",
    "hom-lipids": "Treat lipids as both nutrients and functional food ingredients. Compare saturated, mono- and polyunsaturated fatty acids, cis/trans structure and essential fatty acids; explain digestion, absorption and transport, health effects and recommendations, then apply plasticity, shortening, emulsification, aeration and smoke point to food preparation.",
    "hom-vitamins-minerals": "For each micronutrient know classification, main functions, reliable sources, deficiency, toxicity where relevant and interactions that affect absorption. High-mark answers make links—for example vitamin D and calcium, vitamin C and iron—and distinguish fat-soluble storage risk from the more regular intake required for water-soluble vitamins.",
    "hom-digestion-metabolism": "Digestion combines mechanical breakdown, enzyme-controlled hydrolysis, absorption and assimilation. Trace carbohydrate, protein and fat through the alimentary canal with named enzymes, substrates, products and sites; explain villus adaptations and transport routes, then distinguish basal metabolism from total energy expenditure and factors affecting each.",
    "hom-energy-nutrition": "Energy balance compares intake with basal metabolism, physical activity and the thermic effect of food. Use correct energy yields and calculations, explain positive and negative balance, and adapt nutritional requirements to age, sex, activity, pregnancy, lactation and health while applying current healthy-eating guidance rather than prescribing a generic diet.",
    "hom-meat-preparation": "Connect the structure of muscle fibres, connective tissue and fat to tenderness, nutritive value and choice of cooking method. Cover selection, storage, hygiene, ageing and tenderising, then explain the effects of heat—protein coagulation, collagen conversion, fat melting, shrinkage and browning—and match moist or dry methods to the cut.",
    "hom-fish-seafood": "Classify fish as white, oily, flat or round and shellfish as crustaceans or molluscs, linking structure and fat content to nutrition, spoilage and cooking. A complete answer covers selection for freshness, hygienic storage, preparation, suitable quick cooking methods and the effects of heat on delicate short muscle fibres.",
    "hom-dairy-eggs": "For milk, relate composition to processing methods such as pasteurisation, UHT treatment, homogenisation, fermentation and cheese production. For eggs, connect structure and freshness to coagulation, aeration, emulsification, binding, coating and glazing; include nutrition, safe storage and the effect of heat in each application.",
    "hom-cereals-grains": "Know grain structure—bran, endosperm and germ—and connect milling to nutrient and fibre losses. Compare wheat, rice, oats and other cereals, explain gluten development and starch changes during cooking, and apply flour type and raising-agent choice to bread, pastry and other cereal products.",
    "hom-cooking-methods": "Cooking transfers heat by conduction, convection, radiation or microwaves and changes safety, digestibility, flavour, texture and nutrients. Compare moist, dry and combination methods by procedure, suitable foods, advantages and disadvantages, and explain the underlying changes to protein, starch, sugar, fats, vitamins and pigments.",
    "hom-food-preservation": "Preservation controls microorganisms, enzymes and chemical spoilage by changing temperature, water availability, acidity, oxygen or packaging. Explain the principle and procedure behind freezing, canning, drying, fermentation, irradiation and modified-atmosphere or vacuum packaging, including effects on quality, nutrition, safety and shelf life.",
    "hom-food-safety": "Food safety answers need named hazards, conditions for microbial growth, high-risk foods and prevention at every stage. Apply HACCP logic—hazard, critical control point, limit, monitoring and corrective action—and explain personal hygiene, cross-contamination control, temperature control, storage, reheating and the symptoms and sources of major food-poisoning organisms.",
    "hom-meal-planning": "Meal planning balances nutritional adequacy with age, health, activity, culture, budget, time, skills, equipment, season and preference. Justify every menu choice, adapt texture and nutrients for life stages or special diets, and show variety in colour, flavour and method while observing food safety and realistic portioning.",
    "hom-food-additives": "Explain why additives are used, how they are classified and regulated, and the difference between technological function, E number and acceptable daily intake. Apply preservatives, antioxidants, colours, flavours, emulsifiers, stabilisers and sweeteners to named foods, then weigh convenience and safety benefits against concerns without assuming all additives are harmful.",
    "hom-consumer-rights": "Consumer answers should separate rights, responsibilities, contracts, redress and enforcement. For purchases made from 29 November 2022, the Consumer Rights Act 2022 is central to goods, services and digital content; also understand the syllabus's older legislation, misleading practices, guarantees, online purchasing, complaint procedure, CCPC support and small-claims redress.",
    "hom-personal-finance": "Personal finance links income, deductions and household priorities to budgeting, saving, borrowing, insurance and investment. Show calculations clearly, compare products using APR or AER, term, risk, return, liquidity and total cost, and match the source of finance to purpose while explaining consumer safeguards and the consequences of over-indebtedness.",
    "hom-housing": "Housing decisions change across the family life cycle and depend on tenure, location, design, finance and sustainability. Compare renting, buying and social housing; explain mortgages and purchase costs; apply planning, ergonomics, insulation, ventilation, lighting and universal design to a safe, efficient home.",
    "hom-textiles-fibres": "Start with fibre origin and structure, then link properties to end use and care. Compare natural, regenerated and synthetic fibres; explain yarn and fabric construction, finishes and testing; and justify fibre or fabric selection using absorbency, strength, elasticity, warmth, durability, flammability, care and environmental impact.",
    "hom-clothing-selection": "Clothing choices combine function, comfort, appearance, quality, cost and sustainability. Evaluate construction details and labels, match care procedures to fibre properties, explain detergent action and stain removal, and cover washing, drying, ironing, storage and repair in ways that protect both the garment and the environment.",
    "hom-environmental-issues": "Apply environmental, social and economic sustainability to household decisions. Explain the waste hierarchy, circular economy, energy and water conservation, pollution and climate impacts, then evaluate realistic actions using life-cycle thinking so that a claimed benefit is not simply shifted to another stage.",
    "hom-appliances-equipment": "Appliance selection should compare fitness for purpose, capacity, purchase and running cost, energy label, safety, reliability, guarantees and disposal. Explain how key appliances work, identify safe use and maintenance, calculate lifetime cost where possible, and connect efficient operation to resource conservation.",
    "hom-sociological-concepts": "Use sociological terms precisely and show their relationships: culture communicates values and norms through socialisation, while roles, status, institutions and sanctions organise behaviour. Apply concepts to concrete family or community examples and distinguish correlation, stereotype and value judgement from evidence-based explanation.",
    "hom-family-society": "The family is a changing social institution rather than one fixed structure. Compare nuclear, extended, lone-parent and blended forms; explain functions and roles; and analyse how demographic, economic, legal, cultural and technological change affects size, relationships, resources and everyday family life.",
    "hom-family-caring": "Families provide physical, emotional, economic and social care across the life cycle. Explain changing and shared roles, rights and responsibilities, communication and conflict resolution, then apply support needs to children, older people, illness, disability and family stress while recognising the role of community and statutory services.",
    "hom-marriage": "Marriage combines personal commitment, cultural practice and legal status. Cover reasons and preparation, conditions for a valid marriage, rights and responsibilities, communication and adjustment, and sources of support; distinguish marriage from other partnerships without making value judgements.",
    "hom-family-law": "Family-law answers must name the relevant protection and explain its practical effect. Organise maintenance, the family home, domestic violence, guardianship, custody, access, separation and divorce around rights, responsibilities and remedies, and use legislation accurately rather than listing Acts without application.",
    "hom-social-change": "Social change alters family size, roles, work, housing, education, leisure and relationships. Develop each cause-to-effect chain—for example urbanisation, technology or women's employment—then balance gains in choice and opportunity against pressures such as time scarcity, isolation, childcare cost or unequal access.",
    "hom-education": "Education supports physical, intellectual, emotional, moral and social development and transmits culture through formal and informal processes. Compare provision and access, analyse the influence of class, gender and policy, and connect qualifications and lifelong learning to employment, mobility and personal fulfilment.",
    "hom-work-leisure": "Work includes paid, unpaid and voluntary activity and meets economic, social and psychological needs. Explain changing work patterns and employment rights, work-life balance and household roles, then relate leisure choice to time, income, age, facilities and health while evaluating individual and social benefits.",
    "hom-unemployment-poverty": "Distinguish types and causes of unemployment and absolute, relative and consistent poverty. Trace effects on income, identity, health, family relationships and society, explain the poverty cycle, and evaluate education, training, welfare, community action and employment policy as responses rather than assuming one measure solves every cause.",

    // Physical Education pipeline taxonomy
    "pe-learning-skill-technique": "A skilled performance is consistent, accurate, controlled, efficient and adaptable. Distinguish inherited ability from learned skill and the specific movement pattern of technique, then use biomechanical and movement analysis, practice, guidance and feedback to explain exactly how performance improves in a named activity.",
    "pe-performance-demands": "Performance depends on interacting physical and psychological demands. Select relevant health- and performance-related fitness components, energy or movement demands and mental factors for a named role, explain how they affect outcomes, and justify a valid method of assessment or preparation.",
    "pe-structures-strategies-roles-conventions": "Structures organise performers; strategies are planned ways of achieving an objective; roles assign responsibilities; conventions and rules make activity coherent and fair. Apply each to a named activity and explain how communication, leadership, affiliation and tactical adaptation influence collective performance.",
    "pe-planning-optimum-performance": "Planning begins with valid performance analysis, a prioritised need and a SMART goal. Design a progressive training or practice programme, justify methods and load, monitor comparable evidence, account for recovery and safety, and adapt the plan from results so evaluation is tied to the original goal.",
    "pe-promoting-physical-activity": "Participation is shaped by personal biography and social, cultural, economic, environmental and institutional factors. Distinguish play, recreation, physical education and sport, analyse supports and barriers for a named group, and propose targeted promotion whose likely effect can be measured.",
    "pe-ethics-fair-play": "Ethics goes beyond obeying rules: integrity, respect, fairness and equity guide decisions where interests conflict. Apply a code of ethics to doping, therapeutic-use exemptions, gamesmanship, violence, technology or inclusion, consider stakeholders and consequences, and justify a proportionate response.",
    "pe-physical-activity-inclusion": "Inclusion means meaningful and dignified participation, not simply access to the venue. Identify specific barriers, then explain how adapted rules, equipment, communication, facilities, pathways, trained leaders and representative organisations can remove them without unnecessarily reducing challenge.",
    "pe-technology-media-sport": "Technology can improve analysis, safety, access and officiating but also raises cost, privacy, fairness and dependency issues. Media shapes funding, scheduling, role models, gender representation and spectator behaviour; balanced answers use named technologies or coverage examples and evaluate both intended and unintended effects.",
    "pe-gender-physical-activity": "Gender participation patterns are produced through socialisation, opportunity, body image, media representation and institutional practice rather than biology alone. Use evidence and examples to explain imbalance, hegemonic expectations and regulation of bodies, then evaluate practical strategies for equitable participation and leadership.",
    "pe-business-enterprise-sport": "Sport is also an industry involving sponsorship, endorsement, merchandising, events, advertising and media rights. Distinguish each revenue relationship, apply codes and ethical responsibilities, and analyse benefits and risks for athletes, organisations, businesses, consumers and the integrity of sport.",
    "pe-adventure-activities": "Adventure activities combine environmental uncertainty, decision-making, technical skill and managed risk. For a named activity explain equipment, technique, route or condition assessment, communication, group responsibility, environmental care and emergency procedures, linking each safety control to the hazard it reduces.",
    "pe-aquatics": "Aquatics requires efficient movement in water alongside rigorous safety. Explain body position, breathing, propulsion and coordination for the relevant stroke or task, and apply lifesaving priorities—recognition, safe rescue choice, communication and aftercare—without placing the rescuer at unnecessary risk.",
    "pe-artistic-aesthetic-movement": "Artistic and aesthetic performance combines technical execution with composition and communication. Apply space, time, dynamics, relationships, transitions and form to choreography, then distinguish aesthetic quality from artistic intention and evaluate performance against explicit criteria.",
    "pe-athletics": "Athletics demands event-specific technique and energy-system preparation. Break a named running, jumping or throwing event into phases, explain the biomechanical purpose of each, identify rules and safety requirements, and justify training and feedback matched to the event's dominant demands.",
    "pe-games": "Games require technical skill, perception, decision-making and coordinated strategy under rules. Use a named game to explain individual role, attacking and defensive principles, transitions, communication and officiating, and show how a strategy changes in response to opponents or performance evidence.",
    "pe-personal-exercise-fitness": "Exercise methods produce different adaptations depending on frequency, intensity, time, type and recovery. Compare continuous, interval, fartlek, resistance and studio-based methods, match each to a goal and performer, and explain progression, monitoring, safety and the consequences of insufficient recovery."
  };

  var subjectMethod = {
    geography: "For full marks, define the idea precisely, explain the process or pattern as a linked sequence, and support each developed point with a named and located example, statistic, diagram or piece of map/data evidence. Use cause-and-effect language such as because, therefore and as a result; a list of facts is not a developed geographical explanation.",
    "home-economics": "For full marks, answer the command word directly and develop each point by linking structure or cause to function, effect and a relevant food, household or social example. Where appropriate include classification, sources, procedure, underlying principle, advantages, limitations, safety and current legislation; do not award yourself the same point twice in different wording.",
    pe: "For full marks, define the concept, apply it to a named physical activity, performer or group, and explain the resulting effect on learning, performance, safety, fairness or participation. When asked to evaluate, use evidence to balance strengths and limitations and finish with a justified judgement rather than a descriptive list."
  };

  var chapterApplication = {
    "pe-promoting-physical-activity": "Developed application: suppose the target group is teenage girls whose participation falls after the transition to secondary school. First gather evidence through participation records, a questionnaire and a focus group so the stated barriers are demonstrated rather than assumed. A suitable response might combine low-cost social sessions, choice of non-competitive and competitive activities, visible female leaders, safe transport and a timetable shaped by the group. Each action needs a rationale: choice supports autonomy; friends strengthen affiliation; cost and transport remove practical barriers; role models challenge stereotypes. Promotion should use channels the group actually encounters and inclusive images and language. Evaluate the programme against a baseline using attendance, retention, enjoyment and self-reported confidence, while noting that increased awareness alone does not prove sustained participation.",
    "pe-physical-activity-inclusion": "Developed application: to include a wheelchair user in a games lesson, begin with the person's goals and functional needs instead of treating a diagnosis as a complete description. Use the STEP framework—adapt Space, Task, Equipment and People—while preserving the central challenge of the activity. Examples include a smaller playing area, additional time in possession, a lighter or audible ball, zones or matched support and rules that require meaningful involvement by every player. Explain the effect of each adaptation on access, safety and success, then review it with the participant because an adaptation can become patronising or reduce challenge if it is imposed without consultation. Facility access, trained staff, affordable pathways and representative organisations support continued participation beyond one lesson. Distinguish integration, where the person enters an unchanged programme, from inclusion, where provision responds to difference. Universal design can remove barriers in advance, but individual choice remains essential. Pathways towards excellence should also connect school or community participation to appropriate clubs, coaching and competition rather than offering only occasional introductory sessions.",
    "pe-technology-media-sport": "Developed application: GPS and heart-rate data can quantify distance, speed zones and internal load, while video analysis can identify positioning or technique that observation misses. The coach must interpret the data in context: a high workload may reflect tactical role, and a number is not automatically a diagnosis. Benefits include objective feedback, individualised training and injury-risk monitoring; limitations include cost, validity, privacy, over-reliance and unequal access. Officiating technology such as goal-line systems can improve accuracy, but delays, camera angles and inconsistent intervention can affect flow and trust. Collect only necessary performer data, obtain informed consent, control access and specify retention because biometric information is sensitive. Media coverage can attract sponsorship, participants and role models, but selective scheduling and commentary can reinforce gender stereotypes or prioritise spectator appeal over performer welfare. A strong evaluation names the technology or media example, identifies the stakeholder affected and weighs improved information or visibility against fairness, consent and commercial pressure.",
    "pe-gender-physical-activity": "Developed application: lower participation by a gender group should be explained through interacting opportunities and expectations, not attributed to lack of interest. Family and peer socialisation, school activity choices, facility access, cost, body image, sexualisation, limited leadership pathways and unequal media visibility can influence whether participation feels possible and valued. Hegemonic masculinity may pressure boys to favour dominance and avoid activities labelled feminine, while narrow body ideals can discourage any participant who expects judgement. Effective responses include equal facility time and funding, varied activity choices, inclusive kit, anti-harassment procedures, representative coaches and officials, balanced media coverage and programmes co-designed with the target group. Evaluate change using participation, retention, leadership representation and reported belonging, not enrolment alone.",
    "pe-business-enterprise-sport": "Developed application: distinguish sponsorship, in which a business supplies money or resources for association and exposure, from endorsement, in which an athlete promotes a product, and merchandising, in which branded goods are sold. A named event can generate entry fees, tourism, employment, media rights and local spending, while a sponsor gains audience reach and brand image. An enterprise answer can also identify a need, target market, value proposition, resources, promotion, costs, revenue and risk for a sport-related product, service or event. Risks include dependence on commercial income, ambush marketing, unhealthy-product promotion, pressure on scheduling or rules, reputational damage and exclusion through high prices. Analyse the relationship from several stakeholder perspectives—business, performer, governing body, spectator and community—and apply advertising and sponsorship codes. Separate direct income from wider economic impact and consider opportunity cost, environmental load and whether benefits remain locally. A justified conclusion should state whether the commercial arrangement supports the activity's values and long-term development, not merely whether it makes money."
  };

  function clean(value) {
    return String(value || "")
      .replace(/\s+/g, " ")
      .replace(/\bBlank Page\b.*$/i, "")
      .replace(/\bLEAVING CERTIFICATE\b.*$/i, "")
      .trim();
  }

  function sentenceFor(card) {
    var term = clean(card.term) || "Key idea";
    var definition = clean(card.definition);
    return term + ": " + definition + (/[.!?]$/.test(definition) ? "" : ".");
  }

  function conceptBlocks(cards, subject) {
    var size = subject === "home-economics" ? 5 : 4;
    var blocks = [];
    for (var index = 0; index < cards.length; index += size) {
      var group = cards.slice(index, index + size);
      var names = group.map(function (card) { return clean(card.term); }).filter(Boolean);
      var lead = subject === "geography"
        ? "These ideas should be used together as part of a process, comparison or case-study explanation. "
        : subject === "home-economics"
          ? "Connect the scientific or social principle to its practical effect instead of learning the terms in isolation. "
          : "Apply these connected concepts to the same named activity or performer so the answer explains performance rather than reciting definitions. ";
      blocks.push({
        h: "Connected course content — " + names.join(", "),
        b: lead + group.map(sentenceFor).join(" ")
      });
    }
    return blocks;
  }

  function scorePart(part, question) {
    var model = clean(part.model);
    if (model.length < 80) return -1;
    if (/This addresses the requirement in part/i.test(model)) return -1;
    var sourceBonus = part.model_source === "scheme" ? 80 : 0;
    return sourceBonus + Number(part.marks || 0) * 4 + Math.min(model.length, 1200) / 30 + Number(question.year || 0) / 1000;
  }

  function examBlueprints(chapter) {
    var candidates = [];
    examQuestions.forEach(function (question) {
      if (question.chapterId !== chapter.id) return;
      (question.parts || []).forEach(function (part) {
        var score = scorePart(part, question);
        if (score >= 0) candidates.push({ question: question, part: part, score: score });
      });
    });
    chapter.learningOutcomes.forEach(function (outcome) {
      (outcome.questions || []).forEach(function (question, index) {
        var part = {
          question: question.prompt,
          model: question.model,
          marks: question.marks,
          model_source: "authored"
        };
        var score = scorePart(part, { year: 0 });
        if (score >= 0) candidates.push({
          question: { year: 0, id: chapter.id + "-practice-" + index },
          part: part,
          score: score + 30
        });
      });
    });
    candidates.sort(function (a, b) { return b.score - a.score; });

    var used = new Set();
    return candidates.filter(function (candidate) {
      var prompt = clean(candidate.part.question);
      var key = prompt.toLowerCase().slice(0, 100);
      if (!prompt || used.has(key)) return false;
      used.add(key);
      return true;
    }).slice(0, 2).map(function (candidate) {
      var prompt = clean(candidate.part.question);
      var model = clean(candidate.part.model).slice(0, 1800);
      return {
        h: "Past-paper application — " + prompt.slice(0, 150),
        b: "Question focus: " + prompt + " Model content: " + model
      };
    });
  }

  COURSE_DATA.chapters.forEach(function (chapter) {
    if (!supportedSubjects.has(chapter.subject)) return;
    if (!Array.isArray(chapter.learningOutcomes) || !chapter.learningOutcomes.length) return;

    var outcome = chapter.learningOutcomes[0];
    var cards = Array.isArray(decks[chapter.id])
      ? decks[chapter.id].filter(function (card) { return card && card.term && card.definition; })
      : [];
    var existing = chapter.learningOutcomes.flatMap(function (item) { return item.notes || []; });
    var overview = chapterOverview[chapter.id]
      || ("This chapter connects the central ideas in " + chapter.title + ". Explain relationships and applications, not isolated definitions.");

    var notes = [{ h: "Chapter overview and connections", b: overview }];
    if (chapterApplication[chapter.id]) {
      notes.push({ h: "Developed application", b: chapterApplication[chapter.id] });
    }
    if (existing.length) notes = notes.concat(existing);
    notes = notes.concat(conceptBlocks(cards, chapter.subject));
    notes = notes.concat(examBlueprints(chapter));
    notes.push({ h: "How to build a full-mark answer", b: subjectMethod[chapter.subject] });

    outcome.notes = notes;
    if (cards.length && (!Array.isArray(outcome.keyTerms) || !outcome.keyTerms.length)) {
      outcome.keyTerms = cards.slice();
    }
    chapter.learningOutcomes.slice(1).forEach(function (item) {
      item.notes = [];
    });
  });
})();
