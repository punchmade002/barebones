// Course Data — structural skeleton.
// All chapter content (notes, keyTerms, questions) lives in the per-subject content files.
// Past-paper exam questions live in exam-questions-db.js.
const COURSE_DATA = {
  meta: {
    course: "Leaving Certificate Business — Higher Level",
    textbook: "Back In Business",
    subtitle: "Chapter notes and exam practice"
  },
  chapters: [
    {
      id: "ch1", number: 1, subject: "business", title: "Key Stakeholders in Business", strand: 1,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo1-1", code: "1.1", title: "Internal & external stakeholders and their importance", notes: [], keyTerms: [], questions: [] },
      { id: "lo1-2", code: "1.2", title: "How stakeholders interact and potential conflicts", notes: [], keyTerms: [], questions: [] },
      { id: "lo1-3", code: "1.3", title: "Avoiding and resolving conflict between stakeholders", notes: [], keyTerms: [], questions: [] },
      { id: "lo1-4", code: "1.4", title: "Stakeholder mapping and prioritising stakeholder interests", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch6", number: 6, subject: "business", title: "Enterprise in Action", strand: 2,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo6-1", code: "6.1", title: "Innovation, intrapreneurship & entrepreneurship — and importance of innovation", notes: [], keyTerms: [], questions: [] },
      { id: "lo6-2", code: "6.2", title: "Competencies of innovators", notes: [], keyTerms: [], questions: [] },
      { id: "lo6-3", code: "6.3", title: "Role of government in supporting enterprise", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch7", number: 7, subject: "business", title: "Idea Development", strand: 2,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo7-1", code: "7.1", title: "Factors impacting idea development", notes: [], keyTerms: [], questions: [] },
      { id: "lo7-2", code: "7.2", title: "Design thinking — iterative, person- and solution-centred", notes: [], keyTerms: [], questions: [] },
      { id: "lo7-3", code: "7.3", title: "Conducting a feasibility study", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch8", number: 8, subject: "business", title: "Business Planning", strand: 2,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo8-1", code: "8.1", title: "Importance and key functions of a business plan", notes: [], keyTerms: [], questions: [] },
      { id: "lo8-2", code: "8.2", title: "Ethics and sustainability in business planning", notes: [], keyTerms: [], questions: [] },
      { id: "lo8-3", code: "8.3", title: "What a business model is and its role in the business plan", notes: [], keyTerms: [], questions: [] },
      { id: "lo8-4", code: "8.4", title: "Business Model Canvas (BMC)", notes: [], keyTerms: [], questions: [] },
      { id: "lo8-5", code: "8.5", title: "Common business models", notes: [], keyTerms: [], questions: [] },
      { id: "lo8-6", code: "8.6", title: "Digital technology as a driver of change", notes: [], keyTerms: [], questions: [] },
      { id: "lo8-7", code: "8.7", title: "Technology-driven business models", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch9", number: 9, subject: "business", title: "The Target Market", strand: 2,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo9-1", code: "9.1", title: "Importance of market research and identifying the target market", notes: [], keyTerms: [], questions: [] },
      { id: "lo9-2", code: "9.2", title: "The 7 P's of the marketing mix", notes: [], keyTerms: [], questions: [] },
      { id: "lo9-3", code: "9.3", title: "USP analysis for a product/service", notes: [], keyTerms: [], questions: [] },
      { id: "lo9-4", code: "9.4", title: "Evaluating and improving an existing marketing mix", notes: [], keyTerms: [], questions: [] },
      { id: "lo9-5", code: "9.5", title: "Disruptive impact of digital technology on market research and marketing", notes: [], keyTerms: [], questions: [] },
      { id: "lo9-6", code: "9.6", title: "Influence of ethics and sustainability on marketing", notes: [], keyTerms: [], questions: [] },
      { id: "lo9-7", code: "9.7", title: "Power-interest grid for customers", notes: [], keyTerms: [], questions: [] },
      { id: "lo9-8", code: "9.8", title: "STEEPLE analysis", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch10", number: 10, subject: "business", title: "Operations and Finance", strand: 2,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo10-1", code: "10.1", title: "Operational model — Key Partners, Activities & Resources", notes: [], keyTerms: [], questions: [] },
      { id: "lo10-2", code: "10.2", title: "Costs, sources of finance, revenue streams across the lifecycle", notes: [], keyTerms: [], questions: [] },
      { id: "lo10-3", code: "10.3", title: "Cashflow analysis", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch11", number: 11, subject: "business", title: "Growth, Development and Expansion", strand: 2,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo11-1", code: "11.1", title: "Importance of identifying competition", notes: [], keyTerms: [], questions: [] },
      { id: "lo11-2", code: "11.2", title: "Porter's Five Forces", notes: [], keyTerms: [], questions: [] },
      { id: "lo11-3", code: "11.3", title: "Strategies to adapt or expand", notes: [], keyTerms: [], questions: [] },
      { id: "lo11-4", code: "11.4", title: "Technology supporting adaptation and expansion", notes: [], keyTerms: [], questions: [] },
      { id: "lo11-5", code: "11.5", title: "Cost-Benefit Analysis (CBA) of expansion", notes: [], keyTerms: [], questions: [] },
      { id: "lo11-6", code: "11.6", title: "Adapting marketing mix or business model", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch12", number: 12, subject: "business", title: "Managing Risk", strand: 2,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo12-1", code: "12.1", title: "Challenges and risks of enterprise", notes: [], keyTerms: [], questions: [] },
      { id: "lo12-2", code: "12.2", title: "Importance of assessing and managing risks", notes: [], keyTerms: [], questions: [] },
      { id: "lo12-3", code: "12.3", title: "Risk management strategies and types of insurance", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch16", number: 16, subject: "business", title: "The Rationale for Planning", strand: 3,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo16-1", code: "16.1", title: "Internal and external changes facing organisations", notes: [], keyTerms: [], questions: [] },
      { id: "lo16-2", code: "16.2", title: "Reasons for resistance to change", notes: [], keyTerms: [], questions: [] },
      { id: "lo16-3", code: "16.3", title: "Practices that promote innovation and intrapreneurial thinking", notes: [], keyTerms: [], questions: [] },
      { id: "lo16-4", code: "16.4", title: "Overcoming resistance to change", notes: [], keyTerms: [], questions: [] },
      { id: "lo16-5", code: "16.5", title: "Strategic planning as an ongoing process", notes: [], keyTerms: [], questions: [] },
      { id: "lo16-6", code: "16.6", title: "Benefits of strategic planning", notes: [], keyTerms: [], questions: [] },
      { id: "lo16-7", code: "16.7", title: "Force-Field Analysis", notes: [], keyTerms: [], questions: [] },
      { id: "lo16-8", code: "16.8", title: "Contingency planning for crisis management", notes: [], keyTerms: [], questions: [] },
      { id: "lo16-9", code: "16.9", title: "Factors to consider when developing a contingency plan", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "ch17", number: 17, subject: "business", title: "Making Informed Decisions as a Consumer", strand: 4,
      examQuestions: [],
      learningOutcomes: [
      { id: "lo17-1", code: "17.1", title: "Consumer rights and responsibilities under current legislation", notes: [], keyTerms: [], questions: [] },
      { id: "lo17-2", code: "17.2", title: "Ethics, sustainability and the circular economy", notes: [], keyTerms: [], questions: [] },
      { id: "lo17-3", code: "17.3", title: "Impact of digital technology on consumer behaviour", notes: [], keyTerms: [], questions: [] },
      { id: "lo17-4", code: "17.4", title: "Personal data protection — GDPR", notes: [], keyTerms: [], questions: [] },
      { id: "lo17-5", code: "17.5", title: "Importance of making informed consumer decisions", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe1", number: 1, subject: "pe", title: "Physical Demands of Performance",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe1-1", code: "1.1", title: "Health, fitness, components and fitness testing", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe2", number: 2, subject: "pe", title: "Training Methods and Fitness Plans",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe2-1", code: "2.1", title: "Principles, methods, recovery and periodisation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe3", number: 3, subject: "pe", title: "Psychological Demands of Performance",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe3-1", code: "3.1", title: "Confidence, anxiety, arousal, motivation and mental strategies", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe4", number: 4, subject: "pe", title: "Diet and Nutrition",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe4-1", code: "4.1", title: "Macronutrients, micronutrients, energy systems and supplements", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe5", number: 5, subject: "pe", title: "Skill, Ability and Skilled Performance",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe5-1", code: "5.1", title: "Classification, learning, guidance, feedback and practice", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe6", number: 6, subject: "pe", title: "Biomechanics",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe6-1", code: "6.1", title: "Planes, axes, levers, motion and economy of movement", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe7", number: 7, subject: "pe", title: "Structures and Strategies",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe7-1", code: "7.1", title: "Compositional elements, team structures and strategies", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe8", number: 8, subject: "pe", title: "Safe Practice in Sport and PA",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe8-1", code: "8.1", title: "Safety, injuries, first aid, overtraining and load management", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe9", number: 9, subject: "pe", title: "Rules, Rituals, Coach and Officials",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe9-1", code: "9.1", title: "Roles of the coach and the official, communication and reflection", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe-casestudy", number: 13, subject: "pe", title: "Case Study", isCaseStudy: true,
      examQuestions: [],
      learningOutcomes: [
      { id: "pe-cs-1", code: "CS.1", title: "Case study practice", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "pe-acronyms", number: 10, subject: "pe", title: "Acronyms and Mnemonics",
      examQuestions: [],
      learningOutcomes: [
      { id: "pe-acronyms-1", code: "A.1", title: "Acronyms and mnemonics to learn", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio1", number: 1, subject: "biology", title: "Scientific Knowledge",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio1-1", code: "1.1", title: "Scientific knowledge, method and publishing", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio2", number: 2, subject: "biology", title: "INVESTIGATING IN SCIENCE",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio2-1", code: "2.1", title: "Understand how scientific investigations are designed, conducted, and evaluated with rigour and integrity", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio3", number: 3, subject: "biology", title: "SCIENCE IN SOCIETY",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio3-1", code: "3.1", title: "Evaluate scientific evidence critically and understand the relationship between science and society across economic, social, sustainability, and ethical dimensions", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio4", number: 4, subject: "biology", title: "BIOLOGICAL REASONING",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio4-1", code: "4.1", title: "Apply key biological concepts — including systems, interdependence, evolution, and the transfer of information, matter, and energy — to explain living phenomena", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio5", number: 5, subject: "biology", title: "Characteristics of Life",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio5-1", code: "5.1", title: "Characteristics of life and levels of organisation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio6", number: 6, subject: "biology", title: "Viruses, Classification and Domains of Life",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio6-1", code: "6.1", title: "Viruses, classification and the three domains", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio7", number: 7, subject: "biology", title: "The Unit of Life — The Cell",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio7-1", code: "7.1", title: "Cell theory, microscopy and organelles", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio8", number: 8, subject: "biology", title: "Biomolecules — The Chemicals of Life",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio8-1", code: "8.1", title: "Biomolecules, food tests and nutritional roles", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio9", number: 9, subject: "biology", title: "Transfer Molecules",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio9-1", code: "9.1", title: "The structure and roles of ATP, NAD+ and NADP+ as energy-carrying transfer molecules in cells", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio10", number: 10, subject: "biology", title: "DNA, RNA and the Genetic Code",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio10-1", code: "10.1", title: "The structure of DNA and RNA, the functions of DNA, and how the genetic code directs protein synthesis", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio11", number: 11, subject: "biology", title: "Genetic Inheritance",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio11-1", code: "11.1", title: "The principles of genetic inheritance including chromosome structure, Mendel's laws, sex linkage and gene linkage", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio12", number: 12, subject: "biology", title: "Evolution: The Origins of Life",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio12-1", code: "12.1", title: "The mechanisms and evidence for evolution, including variation, mutation, natural selection and the importance of evolutionary theory", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio13", number: 13, subject: "biology", title: "Enzymes",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio13-1", code: "13.1", title: "Enzyme structure, action, factors and industrial uses", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio14", number: 14, subject: "biology", title: "Photosynthesis",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio14-1", code: "14.1", title: "Photosynthesis: stages, factors and leaf adaptations", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio15", number: 15, subject: "biology", title: "Respiration",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio15-1", code: "15.1", title: "Aerobic and anaerobic respiration, fermentation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio16", number: 16, subject: "biology", title: "Cell Division and Cancer",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio16-1", code: "16.1", title: "Cell cycle, mitosis, meiosis and cancer", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio17", number: 17, subject: "biology", title: "DNA Replication, Protein Synthesis and Mutations",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio17-1", code: "17.1", title: "How DNA is copied and used to build proteins, and how mutations arise", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio18", number: 18, subject: "biology", title: "The Musculoskeletal System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio18-1", code: "18.1", title: "The structure and functions of the skeleton, muscles and joints", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio19", number: 19, subject: "biology", title: "The Nervous System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio19-1", code: "19.1", title: "The structure and function of the nervous system, from neurons to brain regions", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio20", number: 20, subject: "biology", title: "The Endocrine System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio20-1", code: "20.1", title: "How hormones are produced and used by the body, and their applications in health, sport and agriculture", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio21", number: 21, subject: "biology", title: "HOMEOSTASIS",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio21-1", code: "21.1", title: "How organisms maintain a stable internal environment through feedback mechanisms and coordinated organ systems", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio22", number: 22, subject: "biology", title: "IMMUNITY",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio22-1", code: "22.1", title: "How the immune system defends the body against pathogens through innate and acquired immunity, B cells, T cells, and vaccination", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio23", number: 23, subject: "biology", title: "HUMAN REPRODUCTION",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio23-1", code: "23.1", title: "The structure and function of the human male and female reproductive systems, the menstrual cycle, fertilisation, embryonic development, and fertility control", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio24", number: 24, subject: "biology", title: "PLANT REPRODUCTION",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio24-1", code: "24.1", title: "The structure of flowers, pollination, fertilisation, seed and fruit formation, dispersal, and germination in plants", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio25", number: 25, subject: "biology", title: "Transport Across Membranes",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio25-1", code: "25.1", title: "Diffusion, osmosis, active transport", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio26", number: 26, subject: "biology", title: "The Urinary System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio26-1", code: "26.1", title: "Kidney structure, nephron, ADH and osmoregulation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio27", number: 27, subject: "biology", title: "The Digestive System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio27-1", code: "27.1", title: "Digestion, absorption and the liver", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio28", number: 28, subject: "biology", title: "The Breathing System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio28-1", code: "28.1", title: "Breathing mechanics, gas exchange and lung structure", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio29", number: 29, subject: "biology", title: "The Circulatory System and Blood",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio29-1", code: "29.1", title: "Heart, blood vessels, blood and circulation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio30", number: 30, subject: "biology", title: "Transport in Plants",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio30-1", code: "30.1", title: "Xylem, phloem, transpiration and mineral uptake", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio31", number: 31, subject: "biology", title: "Ecology, Ecosystems and Biodiversity",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio31-1", code: "31.1", title: "The structure of ecosystems, the meaning of biodiversity, and how energy and populations are managed within ecological systems", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio32", number: 32, subject: "biology", title: "Investigating an Ecosystem",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio32-1", code: "32.1", title: "The practical methods used to collect, identify and quantify organisms in a grassland ecosystem, and the abiotic and biotic factors that shape it", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio33", number: 33, subject: "biology", title: "Microorganisms",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio33-1", code: "33.1", title: "The characteristics, nutrition, growth and industrial importance of bacteria and fungi, and the role of the human microbiome", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio34", number: 34, subject: "biology", title: "Nutrient Cycling",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio34-1", code: "34.1", title: "How carbon and nitrogen cycle through ecosystems via biological and chemical processes, and the ethical issues arising from nutrient management", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio35", number: 35, subject: "biology", title: "Genetic Engineering",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio35-1", code: "35.1", title: "The principles and steps of genetic engineering, DNA profiling and sequencing, and the ethical issues surrounding genetic technologies", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio-acronyms", number: 36, subject: "biology", title: "Biology Acronyms and Key Terms",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio-acronyms-1", code: "A.1", title: "Acronyms and key terms to learn", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "geo1", number: 1, subject: "geography", title: "Plate Tectonics",
      examQuestions: [],
      learningOutcomes: [
      { id: "geo1-1", code: "1.1", title: "Theory of Plate Tectonics", notes: [], keyTerms: [], questions: [] },
      { id: "geo1-2", code: "1.2", title: "Destructive (Convergent) Plate Boundaries", notes: [], keyTerms: [], questions: [] },
      { id: "geo1-3", code: "1.3", title: "Constructive (Divergent) Plate Boundaries", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "geo2", number: 2, subject: "geography", title: "Volcanoes & Earthquakes",
      examQuestions: [],
      learningOutcomes: [
      { id: "geo2-1", code: "2.1", title: "Positive Impacts of Volcanoes", notes: [], keyTerms: [], questions: [] },
      { id: "geo2-2", code: "2.2", title: "Global Distribution of Volcanoes", notes: [], keyTerms: [], questions: [] },
      { id: "geo2-3", code: "2.3", title: "Global Distribution of Fold Mountains", notes: [], keyTerms: [], questions: [] },
      { id: "geo2-4", code: "2.4", title: "Earthquake Prediction and Mitigation", notes: [], keyTerms: [], questions: [] },
      { id: "geo2-5", code: "2.5", title: "Volcanic Activity and Ireland's Landscape", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "geo3", number: 3, subject: "geography", title: "Tectonic Activity / Folding & Faulting",
      examQuestions: [],
      learningOutcomes: [
      { id: "geo3-1", code: "3.1", title: "Impact of Tectonic Activity on Ireland's Landscape", notes: [], keyTerms: [], questions: [] },
      { id: "geo3-2", code: "3.2", title: "Folding and Faulting Landforms", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "geo4", number: 4, subject: "geography", title: "Weathering",
      examQuestions: [],
      learningOutcomes: [
      { id: "geo4-1", code: "4.1", title: "Physical Weathering — Role of Temperature", notes: [], keyTerms: [], questions: [] },
      { id: "geo4-2", code: "4.2", title: "Physical and Chemical Weathering", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "geo5", number: 5, subject: "geography", title: "Karst Regions / Limestone Landscapes",
      examQuestions: [],
      learningOutcomes: [
      { id: "geo5-1", code: "5.1", title: "Limestone Pavement Formation", notes: [], keyTerms: [], questions: [] },
      { id: "geo5-2", code: "5.2", title: "Underground Karst Landforms", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "geo6", number: 6, subject: "geography", title: "Surface Processes — Rivers, Coasts & Mass Movement",
      examQuestions: [],
      learningOutcomes: [
      { id: "geo6-1", code: "6.1", title: "Erosion — Meander Formation", notes: [], keyTerms: [], questions: [] },
      { id: "geo6-2", code: "6.2", title: "Deposition — Beach and Spit Formation", notes: [], keyTerms: [], questions: [] },
      { id: "geo6-3", code: "6.3", title: "Human Activity — Flood Control on Rivers", notes: [], keyTerms: [], questions: [] },
      { id: "geo6-4", code: "6.4", title: "Mass Movement — Landslides", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "geo7", number: 7, subject: "geography", title: "Concept of a Region / Regional Geography",
      examQuestions: [],
      learningOutcomes: [
      { id: "geo7-1", code: "7.1", title: "Defining a Climatic Region", notes: [], keyTerms: [], questions: [] },
      { id: "geo7-2", code: "7.2", title: "Defining a Language/Cultural Region", notes: [], keyTerms: [], questions: [] },
      { id: "geo7-3", code: "7.3", title: "Defining a Geomorphological Region", notes: [], keyTerms: [], questions: [] },
      { id: "geo7-4", code: "7.4", title: "Causes and Impacts of Industrial Decline", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "geo8", number: 8, subject: "geography", title: "Economic Activity & Social-Economic Regions",
      examQuestions: [],
      learningOutcomes: [
      { id: "geo8-1", code: "8.1", title: "Tourism in Irish Regions — GDA and West of Ireland", notes: [], keyTerms: [], questions: [] },
      { id: "geo8-2", code: "8.2", title: "Core vs Peripheral Regions — GDA and West of Ireland", notes: [], keyTerms: [], questions: [] },
      { id: "geo8-3", code: "8.3", title: "Agriculture in Contrasting Irish Regions", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths1", number: 1, subject: "maths", title: "Algebra - Cubics",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths1-1", code: "M1.1", title: "Cubic equations — key methods", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths2", number: 2, subject: "maths", title: "Algebra - Expressions & Factorising",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths2-1", code: "M2.1", title: "Algebraic expressions and factorisation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths3", number: 3, subject: "maths", title: "Algebra - Inequalities",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths3-1", code: "M3.1", title: "Solving inequalities", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths4", number: 4, subject: "maths", title: "Algebra - Quadratics",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths4-1", code: "M4.1", title: "Quadratic equations and the discriminant", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths5", number: 5, subject: "maths", title: "Algebra - Simultaneous Equations",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths5-1", code: "M5.1", title: "Solving simultaneous equations", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths6", number: 6, subject: "maths", title: "Algebra - Solving Equations",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths6-1", code: "M6.1", title: "Solving equations — general methods", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths7", number: 7, subject: "maths", title: "Area & Volume",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths7-1", code: "M7.1", title: "Area and volume formulae", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths8", number: 8, subject: "maths", title: "Co-Ordinate Geometry of the Circle",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths8-1", code: "M8.1", title: "Circle equations and properties", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths9", number: 9, subject: "maths", title: "Co-Ordinate Geometry of the Line",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths9-1", code: "M9.1", title: "Lines — equations and properties", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths10", number: 10, subject: "maths", title: "Complex Numbers",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths10-1", code: "M10.1", title: "Complex numbers — arithmetic and geometry", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths11", number: 11, subject: "maths", title: "Differentiation - Applications",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths11-1", code: "M11.1", title: "Applications of differentiation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths12", number: 12, subject: "maths", title: "Differentiation - Rules",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths12-1", code: "M12.1", title: "Rules of differentiation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths13", number: 13, subject: "maths", title: "Financial Maths",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths13-1", code: "M13.1", title: "Financial maths — interest and annuities", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths14", number: 14, subject: "maths", title: "Functions",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths14-1", code: "M14.1", title: "Functions — definitions and operations", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths15", number: 15, subject: "maths", title: "Geometry",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths15-1", code: "M15.1", title: "Geometry theorems and proofs", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths16", number: 16, subject: "maths", title: "Geometry - Constructions & Proofs",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths16-1", code: "M16.1", title: "Geometric constructions", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths17", number: 17, subject: "maths", title: "Indices and Logs",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths17-1", code: "M17.1", title: "Laws of indices and logarithms", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths18", number: 18, subject: "maths", title: "Induction",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths18-1", code: "M18.1", title: "Proof by mathematical induction", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths19", number: 19, subject: "maths", title: "Integration",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths19-1", code: "M19.1", title: "Integration — rules and applications", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths20", number: 20, subject: "maths", title: "Probability",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths20-1", code: "M20.1", title: "Probability — rules and distributions", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths21", number: 21, subject: "maths", title: "Sequences & Series",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths21-1", code: "M21.1", title: "Arithmetic and geometric sequences and series", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths22", number: 22, subject: "maths", title: "Statistics - Descriptive Statistics",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths22-1", code: "M22.1", title: "Descriptive statistics", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths23", number: 23, subject: "maths", title: "Statistics - Inferential Statistics",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths23-1", code: "M23.1", title: "Hypothesis testing and confidence intervals", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths24", number: 24, subject: "maths", title: "Statistics - Z Scores",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths24-1", code: "M24.1", title: "Normal distribution and z-scores", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths25", number: 25, subject: "maths", title: "Trigonometry - Functions & Identities",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths25-1", code: "M25.1", title: "Trig functions, identities and equations", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "maths26", number: 26, subject: "maths", title: "Trigonometry - Triangles",
      examQuestions: [],
      learningOutcomes: [
      { id: "maths26-1", code: "M26.1", title: "Sine rule, cosine rule and area", notes: [], keyTerms: [], questions: [] }
      ],
    },

    /* =================== LC CHEMISTRY HL =================== */
    {
      id: "chem1", number: 1, subject: "chemistry", title: "The Nature of Science",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem1-1", code: "C1", title: "The Nature of Science", notes: [], keyTerms: [], questions: [] },
      ],
    },
    { id: "chem2",  number: 2,  subject: "chemistry", title: "Atomic Structure: The Nuclear Model",                            examQuestions: [], learningOutcomes: [{ id: "chem2-1",  code: "C2",  title: "Atomic Structure: The Nuclear Model",                            notes: [], keyTerms: [], questions: [] }] },
    { id: "chem3",  number: 3,  subject: "chemistry", title: "Atomic Structure: The Bohr and Orbital Models",                   examQuestions: [], learningOutcomes: [{ id: "chem3-1",  code: "C3",  title: "Atomic Structure: The Bohr and Orbital Models",                   notes: [], keyTerms: [], questions: [] }] },
    { id: "chem4",  number: 4,  subject: "chemistry", title: "The Periodic Table: Arrangement of Electrons",                    examQuestions: [], learningOutcomes: [{ id: "chem4-1",  code: "C4",  title: "The Periodic Table: Arrangement of Electrons",                    notes: [], keyTerms: [], questions: [] }] },
    { id: "chem5",  number: 5,  subject: "chemistry", title: "Chemical Bonding and Structure",                                  examQuestions: [], learningOutcomes: [{ id: "chem5-1",  code: "C5",  title: "Chemical Bonding and Structure",                                  notes: [], keyTerms: [], questions: [] }] },
    { id: "chem6",  number: 6,  subject: "chemistry", title: "Electronegativity and the Continuum of Chemical Bonding",         examQuestions: [], learningOutcomes: [{ id: "chem6-1",  code: "C6",  title: "Electronegativity and the Continuum of Chemical Bonding",         notes: [], keyTerms: [], questions: [] }] },
    { id: "chem7",  number: 7,  subject: "chemistry", title: "Families and Trends in the Periodic Table",                      examQuestions: [], learningOutcomes: [{ id: "chem7-1",  code: "C7",  title: "Families and Trends in the Periodic Table",                      notes: [], keyTerms: [], questions: [] }] },
    { id: "chem8",  number: 8,  subject: "chemistry", title: "The Mole: The Chemist's Counting Unit",                          examQuestions: [], learningOutcomes: [{ id: "chem8-1",  code: "C8",  title: "The Mole: The Chemist's Counting Unit",                          notes: [], keyTerms: [], questions: [] }] },
    { id: "chem9",  number: 9,  subject: "chemistry", title: "Kinetic Theory of Matter and Behaviour of Gases",                 examQuestions: [], learningOutcomes: [{ id: "chem9-1",  code: "C9",  title: "Kinetic Theory of Matter and Behaviour of Gases",                 notes: [], keyTerms: [], questions: [] }] },
    { id: "chem10", number: 10, subject: "chemistry", title: "Law of Conservation of Mass: Introducing Stoichiometry",          examQuestions: [], learningOutcomes: [{ id: "chem10-1", code: "C10", title: "Law of Conservation of Mass: Introducing Stoichiometry",          notes: [], keyTerms: [], questions: [] }] },
    { id: "chem11", number: 11, subject: "chemistry", title: "Acids and Bases",                                                 examQuestions: [], learningOutcomes: [{ id: "chem11-1", code: "C11", title: "Acids and Bases",                                                 notes: [], keyTerms: [], questions: [] }] },
    { id: "chem12", number: 12, subject: "chemistry", title: "Volumetric Analysis: Acid–Base",                                  examQuestions: [], learningOutcomes: [{ id: "chem12-1", code: "C12", title: "Volumetric Analysis: Acid–Base",                                  notes: [], keyTerms: [], questions: [] }] },
    { id: "chem13", number: 13, subject: "chemistry", title: "Acid–Base Volumetric Exam-Style Questions",                       examQuestions: [], learningOutcomes: [{ id: "chem13-1", code: "C13", title: "Acid–Base Volumetric Exam-Style Questions",                       notes: [], keyTerms: [], questions: [] }] },
    { id: "chem14", number: 14, subject: "chemistry", title: "Oxidation and Reduction",                                         examQuestions: [], learningOutcomes: [{ id: "chem14-1", code: "C14", title: "Oxidation and Reduction",                                         notes: [], keyTerms: [], questions: [] }] },
    { id: "chem15", number: 15, subject: "chemistry", title: "Volumetric Analysis: Oxidation-Reduction",                        examQuestions: [], learningOutcomes: [{ id: "chem15-1", code: "C15", title: "Volumetric Analysis: Oxidation-Reduction",                        notes: [], keyTerms: [], questions: [] }] },
    { id: "chem16", number: 16, subject: "chemistry", title: "Oxidation–Reduction Volumetric Exam-Style Questions",             examQuestions: [], learningOutcomes: [{ id: "chem16-1", code: "C16", title: "Oxidation–Reduction Volumetric Exam-Style Questions",             notes: [], keyTerms: [], questions: [] }] },
    { id: "chem17", number: 17, subject: "chemistry", title: "Rates of Reaction",                                               examQuestions: [], learningOutcomes: [{ id: "chem17-1", code: "C17", title: "Rates of Reaction",                                               notes: [], keyTerms: [], questions: [] }] },
    { id: "chem18", number: 18, subject: "chemistry", title: "Chemical Equilibrium",                                            examQuestions: [], learningOutcomes: [{ id: "chem18-1", code: "C18", title: "Chemical Equilibrium",                                            notes: [], keyTerms: [], questions: [] }] },
    { id: "chem19", number: 19, subject: "chemistry", title: "pH and Indicators",                                               examQuestions: [], learningOutcomes: [{ id: "chem19-1", code: "C19", title: "pH and Indicators",                                               notes: [], keyTerms: [], questions: [] }] },
    { id: "chem20", number: 20, subject: "chemistry", title: "Environmental Chemistry",                                         examQuestions: [], learningOutcomes: [{ id: "chem20-1", code: "C20", title: "Environmental Chemistry",                                         notes: [], keyTerms: [], questions: [] }] },
    { id: "chem21", number: 21, subject: "chemistry", title: "Thermochemistry",                                                 examQuestions: [], learningOutcomes: [{ id: "chem21-1", code: "C21", title: "Thermochemistry",                                                 notes: [], keyTerms: [], questions: [] }] },
    { id: "chem22", number: 22, subject: "chemistry", title: "Electrochemistry",                                                examQuestions: [], learningOutcomes: [{ id: "chem22-1", code: "C22", title: "Electrochemistry",                                                notes: [], keyTerms: [], questions: [] }] },
    { id: "chem23", number: 23, subject: "chemistry", title: "Allotropes of Carbon. Hydrocarbons",                              examQuestions: [], learningOutcomes: [{ id: "chem23-1", code: "C23", title: "Allotropes of Carbon. Hydrocarbons",                              notes: [], keyTerms: [], questions: [] }] },
    { id: "chem24", number: 24, subject: "chemistry", title: "More Families of Organic Compounds",                              examQuestions: [], learningOutcomes: [{ id: "chem24-1", code: "C24", title: "More Families of Organic Compounds",                              notes: [], keyTerms: [], questions: [] }] },
    { id: "chem25", number: 25, subject: "chemistry", title: "Reactions of Organic Compounds",                                  examQuestions: [], learningOutcomes: [{ id: "chem25-1", code: "C25", title: "Reactions of Organic Compounds",                                  notes: [], keyTerms: [], questions: [] }] },
    { id: "chem26", number: 26, subject: "chemistry", title: "Stoichiometry: Limiting Reactants and Percentage Yield",          examQuestions: [], learningOutcomes: [{ id: "chem26-1", code: "C26", title: "Stoichiometry: Limiting Reactants and Percentage Yield",          notes: [], keyTerms: [], questions: [] }] },

    // ── History ────────────────────────────────────────────────────────────────
    { id: "hist-ire1", number: 1,  subject: "history", title: "Ireland T1 — Ireland and the Union, 1815-1870",                              examQuestions: [], learningOutcomes: [{ id: "hist-ire1-1", code: "Ire.1", title: "Ireland and the Union, 1815-1870",                              notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-ire2", number: 2,  subject: "history", title: "Ireland T2 — Movements for political and social reform, 1870-1914",          examQuestions: [], learningOutcomes: [{ id: "hist-ire2-1", code: "Ire.2", title: "Movements for political and social reform, 1870-1914",          notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-ire3", number: 3,  subject: "history", title: "Ireland T3 — The pursuit of sovereignty and the impact of partition, 1912-1949", examQuestions: [], learningOutcomes: [{ id: "hist-ire3-1", code: "Ire.3", title: "The pursuit of sovereignty and the impact of partition, 1912-1949", notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-ire4", number: 4,  subject: "history", title: "Ireland T4 — The Irish diaspora, 1840-1966",                                 examQuestions: [], learningOutcomes: [{ id: "hist-ire4-1", code: "Ire.4", title: "The Irish diaspora, 1840-1966",                                 notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-ire5", number: 5,  subject: "history", title: "Ireland T5 — Politics and society in Northern Ireland, 1949-1993",            examQuestions: [], learningOutcomes: [{ id: "hist-ire5-1", code: "Ire.5", title: "Politics and society in Northern Ireland, 1949-1993",            notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-ire6", number: 6,  subject: "history", title: "Ireland T6 — Government, economy and society in the Republic, 1949-1989",     examQuestions: [], learningOutcomes: [{ id: "hist-ire6-1", code: "Ire.6", title: "Government, economy and society in the Republic, 1949-1989",     notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-eur1", number: 7,  subject: "history", title: "Europe T1 — Nationalism and state formation in Europe, 1815-1871",            examQuestions: [], learningOutcomes: [{ id: "hist-eur1-1", code: "Eur.1", title: "Nationalism and state formation in Europe, 1815-1871",            notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-eur2", number: 8,  subject: "history", title: "Europe T2 — Nation states and international tensions, 1871-1920",             examQuestions: [], learningOutcomes: [{ id: "hist-eur2-1", code: "Eur.2", title: "Nation states and international tensions, 1871-1920",             notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-eur3", number: 9,  subject: "history", title: "Europe T3 — Dictatorship and democracy in Europe, 1920-1945",                 examQuestions: [], learningOutcomes: [{ id: "hist-eur3-1", code: "Eur.3", title: "Dictatorship and democracy in Europe, 1920-1945",                 notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-eur4", number: 10, subject: "history", title: "Europe T4 — Division and realignment in Europe, 1945-1992",                   examQuestions: [], learningOutcomes: [{ id: "hist-eur4-1", code: "Eur.4", title: "Division and realignment in Europe, 1945-1992",                   notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-eur5", number: 11, subject: "history", title: "Europe T5 — European retreat from empire and the aftermath, 1945-1990",       examQuestions: [], learningOutcomes: [{ id: "hist-eur5-1", code: "Eur.5", title: "European retreat from empire and the aftermath, 1945-1990",       notes: [], keyTerms: [], questions: [] }] },
    { id: "hist-eur6", number: 12, subject: "history", title: "Europe T6 — The United States and the world, 1945-1989",                      examQuestions: [], learningOutcomes: [{ id: "hist-eur6-1", code: "Eur.6", title: "The United States and the world, 1945-1989",                      notes: [], keyTerms: [], questions: [] }] },
  ],
};