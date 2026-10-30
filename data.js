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
      { id: "bio1-1", code: "BIO1", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio1-s1", code: "BIO1.1", syllabusRef: "U1.1", title: "The nature of scientific knowledge", notes: [], keyTerms: [], questions: [] },
      { id: "bio1-s2", code: "BIO1.2", syllabusRef: "U1.1", title: "Science as a global enterprise", notes: [], keyTerms: [], questions: [] },
      { id: "bio1-s3", code: "BIO1.3", syllabusRef: "U1.2", title: "Recognising bias and evaluating sources", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio2", number: 2, subject: "biology", title: "Investigating in Science",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio2-1", code: "BIO2", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio2-s1", code: "BIO2.1", syllabusRef: "U2.1", title: "Questioning and predicting", notes: [], keyTerms: [], questions: [] },
      { id: "bio2-s2", code: "BIO2.2", syllabusRef: "U2.3", title: "Designing and conducting investigations", notes: [], keyTerms: [], questions: [] },
      { id: "bio2-s3", code: "BIO2.3", syllabusRef: "U2.3", title: "Objectivity and data quality", notes: [], keyTerms: [], questions: [] },
      { id: "bio2-s4", code: "BIO2.4", syllabusRef: "U2.4", title: "Producing and analysing data", notes: [], keyTerms: [], questions: [] },
      { id: "bio2-s5", code: "BIO2.5", syllabusRef: "U2.5", title: "Reflecting on investigations", notes: [], keyTerms: [], questions: [] },
      { id: "bio2-s6", code: "BIO2.6", syllabusRef: "U2.6", title: "Communicating results", notes: [], keyTerms: [], questions: [] },
      { id: "bio2-s7", code: "BIO2.7", syllabusRef: "Assessment", title: "The Biology in Practice Investigation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio3", number: 3, subject: "biology", title: "Science in Society",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio3-1", code: "BIO3", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio3-s1", code: "BIO3.1", syllabusRef: "U3.1", title: "Evaluating evidence", notes: [], keyTerms: [], questions: [] },
      { id: "bio3-s2", code: "BIO3.2", syllabusRef: "U3.2", title: "Science, scientists and society", notes: [], keyTerms: [], questions: [] },
      { id: "bio3-s3", code: "BIO3.3", syllabusRef: "Strands overview", title: "The cross-cutting themes", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio4", number: 4, subject: "biology", title: "Biological Reasoning",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio4-1", code: "BIO4", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio4-s1", code: "BIO4.1", syllabusRef: "U4.1", title: "Models", notes: [], keyTerms: [], questions: [] },
      { id: "bio4-s2", code: "BIO4.2", syllabusRef: "U4.2", title: "Explaining biological phenomena", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio5", number: 5, subject: "biology", title: "Characteristics of Life",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio5-1", code: "BIO5", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio5-s1", code: "BIO5.1", syllabusRef: "1.1.1", title: "Characteristics of living things", notes: [], keyTerms: [], questions: [] },
      { id: "bio5-s2", code: "BIO5.2", syllabusRef: "1.3.1", title: "Levels of organisation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio6", number: 6, subject: "biology", title: "Viruses, Classification and Domains of Life",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio6-1", code: "BIO6", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio6-s1", code: "BIO6.1", syllabusRef: "1.1.2", title: "Viruses", notes: [], keyTerms: [], questions: [] },
      { id: "bio6-s2", code: "BIO6.2", syllabusRef: "1.1.3", title: "Domains of life", notes: [], keyTerms: [], questions: [] },
      { id: "bio6-s3", code: "BIO6.3", syllabusRef: "1.1.4", title: "Classification", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio7", number: 7, subject: "biology", title: "The Unit of Life — The Cell",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio7-1", code: "BIO7", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio7-s1", code: "BIO7.1", syllabusRef: "1.3.2", title: "Prokaryotic and eukaryotic cells", notes: [], keyTerms: [], questions: [] },
      { id: "bio7-s2", code: "BIO7.2", syllabusRef: "1.3.3", title: "Microscopy", notes: [], keyTerms: [], questions: [] },
      { id: "bio7-s3", code: "BIO7.3", syllabusRef: "1.3.3", title: "Structures and organelles of animal and plant cells", notes: [], keyTerms: [], questions: [] },
      { id: "bio7-s4", code: "BIO7.4", syllabusRef: "1.3.3", title: "Investigation: plant and animal cells", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio8", number: 8, subject: "biology", title: "Biomolecules — The Chemicals of Life",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio8-1", code: "BIO8", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio8-s1", code: "BIO8.1", syllabusRef: "1.2.1", title: "Biomolecules and metabolism", notes: [], keyTerms: [], questions: [] },
      { id: "bio8-s2", code: "BIO8.2", syllabusRef: "1.2.1", title: "Structures of biomolecules", notes: [], keyTerms: [], questions: [] },
      { id: "bio8-s3", code: "BIO8.3", syllabusRef: "1.2.1", title: "Metabolic roles and nutritional sources", notes: [], keyTerms: [], questions: [] },
      { id: "bio8-s4", code: "BIO8.4", syllabusRef: "1.2.2", title: "Minerals", notes: [], keyTerms: [], questions: [] },
      { id: "bio8-s5", code: "BIO8.5", syllabusRef: "1.2.3", title: "Vitamins", notes: [], keyTerms: [], questions: [] },
      { id: "bio8-s6", code: "BIO8.6", syllabusRef: "1.2.4", title: "Water", notes: [], keyTerms: [], questions: [] },
      { id: "bio8-s7", code: "BIO8.7", syllabusRef: "1.2.5", title: "Investigation: food tests", notes: [], keyTerms: [], questions: [] },
      { id: "bio8-s8", code: "BIO8.8", syllabusRef: "1.2.6", title: "Investigation: reducing sugars, quantitatively", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio9", number: 9, subject: "biology", title: "Transfer Molecules",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio9-1", code: "BIO9", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio9-s1", code: "BIO9.1", syllabusRef: "1.2.8", title: "ATP", notes: [], keyTerms: [], questions: [] },
      { id: "bio9-s2", code: "BIO9.2", syllabusRef: "1.2.8", title: "NAD+ and NADP+", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio10", number: 10, subject: "biology", title: "DNA, RNA and the Genetic Code",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio10-1", code: "BIO10", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio10-s1", code: "BIO10.1", syllabusRef: "1.2.7", title: "Nucleotides, DNA and RNA", notes: [], keyTerms: [], questions: [] },
      { id: "bio10-s2", code: "BIO10.2", syllabusRef: "1.2.9", title: "Genes, proteins and traits", notes: [], keyTerms: [], questions: [] },
      { id: "bio10-s3", code: "BIO10.3", syllabusRef: "1.2.9", title: "The genetic code", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio11", number: 11, subject: "biology", title: "Genetic Inheritance",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio11-1", code: "BIO11", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s1", code: "BIO11.1", syllabusRef: "1.4.1", title: "Chromosome structure and genes", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s2", code: "BIO11.2", syllabusRef: "1.4.1", title: "Key concepts of information transfer", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s3", code: "BIO11.3", syllabusRef: "1.4.2", title: "Nuclear and non-nuclear inheritance", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s4", code: "BIO11.4", syllabusRef: "1.4.3", title: "Genetic and epigenetic mechanisms", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s5", code: "BIO11.5", syllabusRef: "1.4.4", title: "Monohybrid crosses", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s6", code: "BIO11.6", syllabusRef: "1.4.5", title: "Incomplete dominance", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s7", code: "BIO11.7", syllabusRef: "1.4.6", title: "Mendel's Laws", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s8", code: "BIO11.8", syllabusRef: "1.4.7", title: "Dihybrid crosses", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s9", code: "BIO11.9", syllabusRef: "1.4.8", title: "Linkage", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s10", code: "BIO11.10", syllabusRef: "1.4.9", title: "Sex determination", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s11", code: "BIO11.11", syllabusRef: "1.4.10", title: "Sex-linked traits", notes: [], keyTerms: [], questions: [] },
      { id: "bio11-s12", code: "BIO11.12", syllabusRef: "1.4.11", title: "Benefits and limitations of Mendelian genetics", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio12", number: 12, subject: "biology", title: "Evolution: The Origins of Life",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio12-1", code: "BIO12", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio12-s1", code: "BIO12.1", syllabusRef: "1.5.1", title: "Variation", notes: [], keyTerms: [], questions: [] },
      { id: "bio12-s2", code: "BIO12.2", syllabusRef: "1.5.2", title: "The theory of evolution by natural selection", notes: [], keyTerms: [], questions: [] },
      { id: "bio12-s3", code: "BIO12.3", syllabusRef: "1.5.3", title: "Evidence for evolution", notes: [], keyTerms: [], questions: [] },
      { id: "bio12-s4", code: "BIO12.4", syllabusRef: "1.5.3", title: "The importance of the theory", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio13", number: 13, subject: "biology", title: "Enzymes",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio13-1", code: "BIO13", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio13-s1", code: "BIO13.1", syllabusRef: "2.1.1", title: "Enzymes as catalysts", notes: [], keyTerms: [], questions: [] },
      { id: "bio13-s2", code: "BIO13.2", syllabusRef: "2.1.2", title: "Enzyme structure and specificity", notes: [], keyTerms: [], questions: [] },
      { id: "bio13-s3", code: "BIO13.3", syllabusRef: "2.1.3", title: "Investigation: rate of enzyme activity", notes: [], keyTerms: [], questions: [] },
      { id: "bio13-s4", code: "BIO13.4", syllabusRef: "2.1.4", title: "Industrial enzymes", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio14", number: 14, subject: "biology", title: "Photosynthesis",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio14-1", code: "BIO14", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio14-s1", code: "BIO14.1", syllabusRef: "2.2.1", title: "Photosynthesis as an anabolic process", notes: [], keyTerms: [], questions: [] },
      { id: "bio14-s2", code: "BIO14.2", syllabusRef: "2.2.2", title: "Investigation: rate of photosynthesis", notes: [], keyTerms: [], questions: [] },
      { id: "bio14-s3", code: "BIO14.3", syllabusRef: "2.2.4", title: "The light-dependent reactions", notes: [], keyTerms: [], questions: [] },
      { id: "bio14-s4", code: "BIO14.4", syllabusRef: "2.2.4", title: "The light-independent reactions", notes: [], keyTerms: [], questions: [] },
      { id: "bio14-s5", code: "BIO14.5", syllabusRef: "2.2.5", title: "The chloroplast's internal structure", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio15", number: 15, subject: "biology", title: "Respiration",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio15-1", code: "BIO15", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio15-s1", code: "BIO15.1", syllabusRef: "2.2.1", title: "Respiration as a catabolic process", notes: [], keyTerms: [], questions: [] },
      { id: "bio15-s2", code: "BIO15.2", syllabusRef: "2.2.3", title: "Investigation: conditions for fermentation", notes: [], keyTerms: [], questions: [] },
      { id: "bio15-s3", code: "BIO15.3", syllabusRef: "2.2.4", title: "First-stage process", notes: [], keyTerms: [], questions: [] },
      { id: "bio15-s4", code: "BIO15.4", syllabusRef: "2.2.4", title: "Second-stage process", notes: [], keyTerms: [], questions: [] },
      { id: "bio15-s5", code: "BIO15.5", syllabusRef: "2.2.5", title: "The mitochondrion's internal structure and ATP synthase", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio16", number: 16, subject: "biology", title: "Cell Division and Cancer",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio16-1", code: "BIO16", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio16-s1", code: "BIO16.1", syllabusRef: "2.3.1", title: "The cell cycle", notes: [], keyTerms: [], questions: [] },
      { id: "bio16-s2", code: "BIO16.2", syllabusRef: "2.3.2", title: "Mitosis and meiosis", notes: [], keyTerms: [], questions: [] },
      { id: "bio16-s3", code: "BIO16.3", syllabusRef: "2.3.3", title: "DNA replication and mitosis in the cell cycle", notes: [], keyTerms: [], questions: [] },
      { id: "bio16-s4", code: "BIO16.4", syllabusRef: "2.3.7", title: "Cancer", notes: [], keyTerms: [], questions: [] },
      { id: "bio16-s5", code: "BIO16.5", syllabusRef: "2.3.8", title: "Causes, prevention and treatment of cancer", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio17", number: 17, subject: "biology", title: "DNA Replication, Protein Synthesis and Mutations",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio17-1", code: "BIO17", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio17-s1", code: "BIO17.1", syllabusRef: "2.3.4", title: "Modelling DNA replication and information flow", notes: [], keyTerms: [], questions: [] },
      { id: "bio17-s2", code: "BIO17.2", syllabusRef: "2.3.5", title: "Transcription and translation", notes: [], keyTerms: [], questions: [] },
      { id: "bio17-s3", code: "BIO17.3", syllabusRef: "2.3.6", title: "Mutations", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio18", number: 18, subject: "biology", title: "The Musculoskeletal System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio18-1", code: "BIO18", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio18-s1", code: "BIO18.1", syllabusRef: "2.4.1", title: "The musculoskeletal system as a system for response", notes: [], keyTerms: [], questions: [] },
      { id: "bio18-s2", code: "BIO18.2", syllabusRef: "2.4.2", title: "The axial skeleton", notes: [], keyTerms: [], questions: [] },
      { id: "bio18-s3", code: "BIO18.3", syllabusRef: "2.4.2", title: "The appendicular skeleton", notes: [], keyTerms: [], questions: [] },
      { id: "bio18-s4", code: "BIO18.4", syllabusRef: "2.4.3", title: "Muscles and joints", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio19", number: 19, subject: "biology", title: "The Nervous System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio19-1", code: "BIO19", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio19-s1", code: "BIO19.1", syllabusRef: "2.4.4", title: "CNS and PNS", notes: [], keyTerms: [], questions: [] },
      { id: "bio19-s2", code: "BIO19.2", syllabusRef: "2.4.4", title: "The reflex action", notes: [], keyTerms: [], questions: [] },
      { id: "bio19-s3", code: "BIO19.3", syllabusRef: "2.4.6", title: "Neurons", notes: [], keyTerms: [], questions: [] },
      { id: "bio19-s4", code: "BIO19.4", syllabusRef: "2.4.7", title: "Neurotransmission", notes: [], keyTerms: [], questions: [] },
      { id: "bio19-s5", code: "BIO19.5", syllabusRef: "2.4.8", title: "Conduction across the synaptic cleft and its disruption", notes: [], keyTerms: [], questions: [] },
      { id: "bio19-s6", code: "BIO19.6", syllabusRef: "2.4.9", title: "Dopamine and endorphins", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio20", number: 20, subject: "biology", title: "The Endocrine System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio20-1", code: "BIO20", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio20-s1", code: "BIO20.1", syllabusRef: "2.4.10", title: "Glands, locations and hormones", notes: [], keyTerms: [], questions: [] },
      { id: "bio20-s2", code: "BIO20.2", syllabusRef: "2.4.11", title: "Hormonal manipulation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio21", number: 21, subject: "biology", title: "Homeostasis",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio21-1", code: "BIO21", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio21-s1", code: "BIO21.1", syllabusRef: "2.4.1", title: "Structures and systems for response", notes: [], keyTerms: [], questions: [] },
      { id: "bio21-s2", code: "BIO21.2", syllabusRef: "2.4.5", title: "Homeostasis as a stimulus-response model", notes: [], keyTerms: [], questions: [] },
      { id: "bio21-s3", code: "BIO21.3", syllabusRef: "2.4.5", title: "Nervous vs hormonal coordination", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio22", number: 22, subject: "biology", title: "Immunity",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio22-1", code: "BIO22", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio22-s1", code: "BIO22.1", syllabusRef: "2.4.12", title: "Pathogens", notes: [], keyTerms: [], questions: [] },
      { id: "bio22-s2", code: "BIO22.2", syllabusRef: "2.4.12", title: "Innate and adaptive immunity", notes: [], keyTerms: [], questions: [] },
      { id: "bio22-s3", code: "BIO22.3", syllabusRef: "2.4.12", title: "Acquired immunity, prevention and treatment", notes: [], keyTerms: [], questions: [] },
      { id: "bio22-s4", code: "BIO22.4", syllabusRef: "2.4.13", title: "Viruses: replication", notes: [], keyTerms: [], questions: [] },
      { id: "bio22-s5", code: "BIO22.5", syllabusRef: "2.4.14", title: "White blood cells", notes: [], keyTerms: [], questions: [] },
      { id: "bio22-s6", code: "BIO22.6", syllabusRef: "2.4.15", title: "Emergence and spread of infectious disease", notes: [], keyTerms: [], questions: [] },
      { id: "bio22-s7", code: "BIO22.7", syllabusRef: "2.4.16", title: "Emerging diseases and society", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio23", number: 23, subject: "biology", title: "Human Reproduction",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio23-1", code: "BIO23", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio23-s1", code: "BIO23.1", syllabusRef: "2.5.1", title: "The male reproductive system", notes: [], keyTerms: [], questions: [] },
      { id: "bio23-s2", code: "BIO23.2", syllabusRef: "2.5.1", title: "The female reproductive system", notes: [], keyTerms: [], questions: [] },
      { id: "bio23-s3", code: "BIO23.3", syllabusRef: "2.5.1", title: "Gametes and fertilisation", notes: [], keyTerms: [], questions: [] },
      { id: "bio23-s4", code: "BIO23.4", syllabusRef: "2.5.2", title: "The menstrual cycle", notes: [], keyTerms: [], questions: [] },
      { id: "bio23-s5", code: "BIO23.5", syllabusRef: "2.5.3", title: "Pregnancy", notes: [], keyTerms: [], questions: [] },
      { id: "bio23-s6", code: "BIO23.6", syllabusRef: "2.5.4", title: "Hormones in reproduction", notes: [], keyTerms: [], questions: [] },
      { id: "bio23-s7", code: "BIO23.7", syllabusRef: "2.5.5", title: "Prenatal and postnatal care", notes: [], keyTerms: [], questions: [] },
      { id: "bio23-s8", code: "BIO23.8", syllabusRef: "2.5.6", title: "Fertility control and infertility", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio24", number: 24, subject: "biology", title: "Plant Reproduction",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio24-1", code: "BIO24", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio24-s1", code: "BIO24.1", syllabusRef: "2.5.7", title: "Flower structure and pollination", notes: [], keyTerms: [], questions: [] },
      { id: "bio24-s2", code: "BIO24.2", syllabusRef: "2.5.7", title: "Investigation: insect- and wind-pollinated plants", notes: [], keyTerms: [], questions: [] },
      { id: "bio24-s3", code: "BIO24.3", syllabusRef: "2.5.8", title: "Seeds", notes: [], keyTerms: [], questions: [] },
      { id: "bio24-s4", code: "BIO24.4", syllabusRef: "2.5.8", title: "Fruit and seed dispersal", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio25", number: 25, subject: "biology", title: "Transport Across Membranes",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio25-1", code: "BIO25", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio25-s1", code: "BIO25.1", syllabusRef: "2.6.1", title: "Diffusion, osmosis and active transport", notes: [], keyTerms: [], questions: [] },
      { id: "bio25-s2", code: "BIO25.2", syllabusRef: "2.6.1", title: "Osmosis in food preservation and plant health", notes: [], keyTerms: [], questions: [] },
      { id: "bio25-s3", code: "BIO25.3", syllabusRef: "2.6.2", title: "Investigation: rate of osmosis", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio26", number: 26, subject: "biology", title: "The Urinary System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio26-1", code: "BIO26", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio26-s1", code: "BIO26.1", syllabusRef: "2.6.3", title: "The urinary system", notes: [], keyTerms: [], questions: [] },
      { id: "bio26-s2", code: "BIO26.2", syllabusRef: "2.6.3", title: "The nephron", notes: [], keyTerms: [], questions: [] },
      { id: "bio26-s3", code: "BIO26.3", syllabusRef: "2.6.3", title: "ADH and osmoregulation", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio27", number: 27, subject: "biology", title: "The Digestive System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio27-1", code: "BIO27", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio27-s1", code: "BIO27.1", syllabusRef: "2.6.4", title: "The digestive system", notes: [], keyTerms: [], questions: [] },
      { id: "bio27-s2", code: "BIO27.2", syllabusRef: "2.6.4", title: "Mechanical breakdown", notes: [], keyTerms: [], questions: [] },
      { id: "bio27-s3", code: "BIO27.3", syllabusRef: "2.6.4", title: "Chemical breakdown", notes: [], keyTerms: [], questions: [] },
      { id: "bio27-s4", code: "BIO27.4", syllabusRef: "2.6.5", title: "Absorption, transport and storage", notes: [], keyTerms: [], questions: [] },
      { id: "bio27-s5", code: "BIO27.5", syllabusRef: "2.6.6", title: "Diet", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio28", number: 28, subject: "biology", title: "The Breathing System",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio28-1", code: "BIO28", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio28-s1", code: "BIO28.1", syllabusRef: "2.6.7", title: "Gas exchange and the breathing mechanism", notes: [], keyTerms: [], questions: [] },
      { id: "bio28-s2", code: "BIO28.2", syllabusRef: "2.6.8", title: "CO₂ as a controlling factor in breathing", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio29", number: 29, subject: "biology", title: "The Circulatory System and Blood",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio29-1", code: "BIO29", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio29-s1", code: "BIO29.1", syllabusRef: "2.6.9", title: "Investigation: the heart", notes: [], keyTerms: [], questions: [] },
      { id: "bio29-s2", code: "BIO29.2", syllabusRef: "2.6.10", title: "Circulation", notes: [], keyTerms: [], questions: [] },
      { id: "bio29-s3", code: "BIO29.3", syllabusRef: "2.6.11", title: "Heartbeat", notes: [], keyTerms: [], questions: [] },
      { id: "bio29-s4", code: "BIO29.4", syllabusRef: "2.6.12", title: "Blood", notes: [], keyTerms: [], questions: [] },
      { id: "bio29-s5", code: "BIO29.5", syllabusRef: "2.6.13", title: "Blood vessels", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio30", number: 30, subject: "biology", title: "Transport in Plants",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio30-1", code: "BIO30", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio30-s1", code: "BIO30.1", syllabusRef: "2.6.14", title: "Plant structures for transport", notes: [], keyTerms: [], questions: [] },
      { id: "bio30-s2", code: "BIO30.2", syllabusRef: "2.6.15", title: "Transport of water and minerals", notes: [], keyTerms: [], questions: [] },
      { id: "bio30-s3", code: "BIO30.3", syllabusRef: "2.6.15", title: "Transport of CO₂ and photosynthetic products", notes: [], keyTerms: [], questions: [] },
      { id: "bio30-s4", code: "BIO30.4", syllabusRef: "2.6.8", title: "CO₂ as a controlling factor in plant stomata", notes: [], keyTerms: [], questions: [] },
      { id: "bio30-s5", code: "BIO30.5", syllabusRef: "2.6.16", title: "Investigation: rate of transpiration", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio31", number: 31, subject: "biology", title: "Ecology, Ecosystems and Biodiversity",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio31-1", code: "BIO31", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s1", code: "BIO31.1", syllabusRef: "3.1.1", title: "Biosphere, ecosystems, habitats and biodiversity", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s2", code: "BIO31.2", syllabusRef: "3.1.2", title: "Biodiversity loss and conservation", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s3", code: "BIO31.3", syllabusRef: "3.1.3", title: "Investigation: human activity and species diversity", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s4", code: "BIO31.4", syllabusRef: "3.1.4", title: "Simpson's Diversity Index", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s5", code: "BIO31.5", syllabusRef: "3.1.5", title: "Carrying capacity and limiting factors", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s6", code: "BIO31.6", syllabusRef: "3.1.6", title: "Population curves", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s7", code: "BIO31.7", syllabusRef: "3.1.7", title: "Energy and nutrient transfer", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s8", code: "BIO31.8", syllabusRef: "3.1.8", title: "Pyramids of numbers", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s9", code: "BIO31.9", syllabusRef: "3.1.9", title: "Pyramids of biomass", notes: [], keyTerms: [], questions: [] },
      { id: "bio31-s10", code: "BIO31.10", syllabusRef: "3.1.10", title: "The niche", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio32", number: 32, subject: "biology", title: "Investigating an Ecosystem",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio32-1", code: "BIO32", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio32-s1", code: "BIO32.1", syllabusRef: "3.1.11", title: "Collection and identification", notes: [], keyTerms: [], questions: [] },
      { id: "bio32-s2", code: "BIO32.2", syllabusRef: "3.1.11", title: "Surveys", notes: [], keyTerms: [], questions: [] },
      { id: "bio32-s3", code: "BIO32.3", syllabusRef: "3.1.11", title: "Abiotic factors", notes: [], keyTerms: [], questions: [] },
      { id: "bio32-s4", code: "BIO32.4", syllabusRef: "3.1.11", title: "Biotic factors and relationships", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio33", number: 33, subject: "biology", title: "Microorganisms",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio33-1", code: "BIO33", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio33-s1", code: "BIO33.1", syllabusRef: "3.2.1", title: "Bacteria and fungi", notes: [], keyTerms: [], questions: [] },
      { id: "bio33-s2", code: "BIO33.2", syllabusRef: "3.2.2", title: "Investigation: growth of microorganisms", notes: [], keyTerms: [], questions: [] },
      { id: "bio33-s3", code: "BIO33.3", syllabusRef: "3.2.3", title: "Microorganisms in industry", notes: [], keyTerms: [], questions: [] },
      { id: "bio33-s4", code: "BIO33.4", syllabusRef: "3.2.4", title: "The microbiome", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio34", number: 34, subject: "biology", title: "Nutrient Cycling",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio34-1", code: "BIO34", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio34-s1", code: "BIO34.1", syllabusRef: "3.2.5", title: "The carbon cycle", notes: [], keyTerms: [], questions: [] },
      { id: "bio34-s2", code: "BIO34.2", syllabusRef: "3.2.6", title: "The nitrogen cycle", notes: [], keyTerms: [], questions: [] },
      { id: "bio34-s3", code: "BIO34.3", syllabusRef: "3.2.7", title: "Ethics and sustainability of nutrient cycling", notes: [], keyTerms: [], questions: [] },
      { id: "bio34-s4", code: "BIO34.4", syllabusRef: "3.2.8", title: "Climate change and biological strategies", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio35", number: 35, subject: "biology", title: "Genetic Engineering",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio35-1", code: "BIO35", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio35-s1", code: "BIO35.1", syllabusRef: "3.3.1", title: "Genetic engineering", notes: [], keyTerms: [], questions: [] },
      { id: "bio35-s2", code: "BIO35.2", syllabusRef: "3.3.2", title: "DNA profiling", notes: [], keyTerms: [], questions: [] },
      { id: "bio35-s3", code: "BIO35.3", syllabusRef: "3.3.3", title: "Generating a DNA profile", notes: [], keyTerms: [], questions: [] },
      { id: "bio35-s4", code: "BIO35.4", syllabusRef: "3.3.4", title: "DNA sequencing", notes: [], keyTerms: [], questions: [] },
      { id: "bio35-s5", code: "BIO35.5", syllabusRef: "3.3.5", title: "Bioinformatics: genome databases", notes: [], keyTerms: [], questions: [] },
      { id: "bio35-s6", code: "BIO35.6", syllabusRef: "3.3.6", title: "Investigation: DNA-profile patterns", notes: [], keyTerms: [], questions: [] },
      { id: "bio35-s7", code: "BIO35.7", syllabusRef: "3.3.7", title: "Ethics of genetic technologies", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "bio-acronyms", number: 36, subject: "biology", title: "Biology Acronyms and Key Terms",
      examQuestions: [],
      learningOutcomes: [
      { id: "bio-acronyms-1", code: "BIO36", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
      { id: "bio-acronyms-s1", code: "BIO36.1", syllabusRef: "Appendix 1", title: "Acronyms and key terms", notes: [], keyTerms: [], questions: [] },
      { id: "bio-acronyms-s2", code: "BIO36.2", syllabusRef: "Appendix 1", title: "Action verbs", notes: [], keyTerms: [], questions: [] }
      ],
    },
    { id: "geo-plate-tectonics", number: 1, subject: "geography", title: "Plate Tectonics — Earth's Structure, Continental Drift, Sea-Floor Spreading, Plate Boundaries", examQuestions: [], learningOutcomes: [
        { id: "geo-plate-tectonics-1", code: "GEO1", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-plate-tectonics-s1", code: "GEO1.1", syllabusRef: "1.1", title: "The internal structure of the earth", notes: [], keyTerms: [], questions: [] },
        { id: "geo-plate-tectonics-s2", code: "GEO1.2", syllabusRef: "1.1", title: "The plate tectonics model", notes: [], keyTerms: [], questions: [] },
        { id: "geo-plate-tectonics-s3", code: "GEO1.3", syllabusRef: "1.1", title: "Plate boundaries as zones of crustal construction and destruction", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-volcanoes-earthquakes", number: 2, subject: "geography", title: "Volcanic and Earthquake Activity", examQuestions: [], learningOutcomes: [
        { id: "geo-volcanoes-earthquakes-1", code: "GEO2", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-volcanoes-earthquakes-s1", code: "GEO2.1", syllabusRef: "1.1", title: "The geography of volcanoes", notes: [], keyTerms: [], questions: [] },
        { id: "geo-volcanoes-earthquakes-s2", code: "GEO2.2", syllabusRef: "1.1", title: "The geography of earthquakes", notes: [], keyTerms: [], questions: [] },
        { id: "geo-volcanoes-earthquakes-s3", code: "GEO2.3", syllabusRef: "1.3", title: "Landforms from volcanic and plutonic structures", notes: [], keyTerms: [], questions: [] },
        { id: "geo-volcanoes-earthquakes-s4", code: "GEO2.4", syllabusRef: "1.3", title: "Landforms from sedimentary structures", notes: [], keyTerms: [], questions: [] },
        { id: "geo-volcanoes-earthquakes-s5", code: "GEO2.5", syllabusRef: "1.3", title: "Landforms from structures of deformation", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-rocks-weathering", number: 3, subject: "geography", title: "Rocks, Weathering and Mass Movement", examQuestions: [], learningOutcomes: [
        { id: "geo-rocks-weathering-1", code: "GEO3", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rocks-weathering-s1", code: "GEO3.1", syllabusRef: "1.2", title: "The rock cycle and rock formation", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rocks-weathering-s2", code: "GEO3.2", syllabusRef: "1.2", title: "Human interaction with the rock cycle", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rocks-weathering-s3", code: "GEO3.3", syllabusRef: "1.2", title: "Weathering processes", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rocks-weathering-s4", code: "GEO3.4", syllabusRef: "1.4", title: "Landforms associated with particular rock types", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rocks-weathering-s5", code: "GEO3.5", syllabusRef: "1.2", title: "Mass movement (mass wasting) processes and the factors governing them", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rocks-weathering-s6", code: "GEO3.6", syllabusRef: "1.2", title: "Erosion by wind", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rocks-weathering-s7", code: "GEO3.7", syllabusRef: "1.7", title: "Human interaction: mass movement", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-glaciation", number: 4, subject: "geography", title: "Glaciation — Glacial Processes, Landforms and Isostasy", examQuestions: [], learningOutcomes: [
        { id: "geo-glaciation-1", code: "GEO4", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-glaciation-s1", code: "GEO4.1", syllabusRef: "1.5", title: "Glacial processes, patterns and associated landforms", notes: [], keyTerms: [], questions: [] },
        { id: "geo-glaciation-s2", code: "GEO4.2", syllabusRef: "1.6", title: "Isostasy", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-rivers", number: 5, subject: "geography", title: "Rivers — Fluvial Processes and Landforms", examQuestions: [], learningOutcomes: [
        { id: "geo-rivers-1", code: "GEO5", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rivers-s1", code: "GEO5.1", syllabusRef: "1.5", title: "Fluvial processes, patterns and associated landforms", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rivers-s2", code: "GEO5.2", syllabusRef: "1.6", title: "Fluvial adjustment to base level", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rivers-s3", code: "GEO5.3", syllabusRef: "1.6", title: "Cyclic landscape development and peneplains", notes: [], keyTerms: [], questions: [] },
        { id: "geo-rivers-s4", code: "GEO5.4", syllabusRef: "1.7", title: "Human interaction: river processes", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-sea", number: 6, subject: "geography", title: "The Sea at Work — Coastal Processes and Landforms", examQuestions: [], learningOutcomes: [
        { id: "geo-sea-1", code: "GEO6", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-sea-s1", code: "GEO6.1", syllabusRef: "1.5", title: "Coastal processes, patterns and associated landforms", notes: [], keyTerms: [], questions: [] },
        { id: "geo-sea-s2", code: "GEO6.2", syllabusRef: "1.7", title: "Human interaction: coastal processes", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-aerial-photographs", number: 7, subject: "geography", title: "Aerial Photographs — Interpretation, Location, Sketch Maps and Land Use", examQuestions: [], learningOutcomes: [
        { id: "geo-aerial-photographs-1", code: "GEO7", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-aerial-photographs-s1", code: "GEO7.1", syllabusRef: "3", title: "Aerial photograph interpretation", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-mapwork", number: 8, subject: "geography", title: "Ordnance Survey Mapwork and the Geographical Investigation", examQuestions: [], learningOutcomes: [
        { id: "geo-mapwork-1", code: "GEO8", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-mapwork-s1", code: "GEO8.1", syllabusRef: "3", title: "Map interpretation", notes: [], keyTerms: [], questions: [] },
        { id: "geo-mapwork-s2", code: "GEO8.2", syllabusRef: "3", title: "Textual sources", notes: [], keyTerms: [], questions: [] },
        { id: "geo-mapwork-s3", code: "GEO8.3", syllabusRef: "3", title: "The Geographical Investigation (20%)", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-weather-climate", number: 9, subject: "geography", title: "Weather and Climate — Weather Maps and Satellite Imagery", examQuestions: [], learningOutcomes: [
        { id: "geo-weather-climate-1", code: "GEO9", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-weather-climate-s1", code: "GEO9.1", syllabusRef: "3", title: "Weather maps and weather data", notes: [], keyTerms: [], questions: [] },
        { id: "geo-weather-climate-s2", code: "GEO9.2", syllabusRef: "3", title: "Satellite imagery", notes: [], keyTerms: [], questions: [] },
        { id: "geo-weather-climate-s3", code: "GEO9.3", syllabusRef: "3", title: "Geographical information systems (GIS)", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-graph-skills", number: 10, subject: "geography", title: "Tables, Graphs and Data Skills", examQuestions: [], learningOutcomes: [
        { id: "geo-graph-skills-1", code: "GEO10", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-graph-skills-s1", code: "GEO10.1", syllabusRef: "3", title: "Figure interpretation", notes: [], keyTerms: [], questions: [] },
        { id: "geo-graph-skills-s2", code: "GEO10.2", syllabusRef: "3", title: "Census of population data", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-region-concept", number: 11, subject: "geography", title: "The Concept of a Region — Defining and Classifying Regions", examQuestions: [], learningOutcomes: [
        { id: "geo-region-concept-1", code: "GEO11", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-concept-s1", code: "GEO11.1", syllabusRef: "2.1", title: "Physical regions", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-concept-s2", code: "GEO11.2", syllabusRef: "2.1", title: "Administrative regions at different scales", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-concept-s3", code: "GEO11.3", syllabusRef: "2.1", title: "Cultural regions", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-concept-s4", code: "GEO11.4", syllabusRef: "2.1", title: "Socio-economic regions", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-concept-s5", code: "GEO11.5", syllabusRef: "2.1", title: "Nodal/city/urban regions", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-region-ireland", number: 12, subject: "geography", title: "Irish Regions — Core and Peripheral", examQuestions: [], learningOutcomes: [
        { id: "geo-region-ireland-1", code: "GEO12", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-ireland-s1", code: "GEO12.1", syllabusRef: "2.2", title: "A Core Irish Region", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-ireland-s2", code: "GEO12.2", syllabusRef: "2.2", title: "A Peripheral Irish Region", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-region-european", number: 13, subject: "geography", title: "European Regions — Core, Peripheral and Complexity of Regions", examQuestions: [], learningOutcomes: [
        { id: "geo-region-european-1", code: "GEO13", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-european-s1", code: "GEO13.1", syllabusRef: "2.2", title: "A Core European Region: the Paris Basin", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-european-s2", code: "GEO13.2", syllabusRef: "2.2", title: "A Peripheral European Region: the Mezzogiorno", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-european-s3", code: "GEO13.3", syllabusRef: "2.3", title: "The complexity of regions (i)", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-european-s4", code: "GEO13.4", syllabusRef: "2.4", title: "The complexity of regions (ii)", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-region-continental", number: 14, subject: "geography", title: "A Continental / Subcontinental Region", examQuestions: [], learningOutcomes: [
        { id: "geo-region-continental-1", code: "GEO14", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-region-continental-s1", code: "GEO14.1", syllabusRef: "2.2", title: "India", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-economic-development", number: 15, subject: "geography", title: "Economic Development — Measuring Development and the Distribution of Wealth", examQuestions: [], learningOutcomes: [
        { id: "geo-economic-development-1", code: "GEO15", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-development-s1", code: "GEO15.1", syllabusRef: "4.1", title: "Measuring economic development", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-development-s2", code: "GEO15.2", syllabusRef: "4.2", title: "Spatial variations in development", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-development-s3", code: "GEO15.3", syllabusRef: "4.2", title: "Case study of a developing economy", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-development-s4", code: "GEO15.4", syllabusRef: "4.2", title: "Global issues and a justice perspective", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-economic-activities", number: 16, subject: "geography", title: "Primary, Secondary and Tertiary Economic Activities", examQuestions: [], learningOutcomes: [
        { id: "geo-economic-activities-1", code: "GEO16", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-activities-s1", code: "GEO16.1", syllabusRef: "4.2", title: "Case study of a developed economy", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-activities-s2", code: "GEO16.2", syllabusRef: "4.3", title: "The mobility of modern economic activities and factors in their location", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-economic-environment", number: 17, subject: "geography", title: "Economic Activity and Environmental Impact", examQuestions: [], learningOutcomes: [
        { id: "geo-economic-environment-1", code: "GEO17", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-environment-s1", code: "GEO17.1", syllabusRef: "4.5", title: "Renewable and non-renewable resources in the economy", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-environment-s2", code: "GEO17.2", syllabusRef: "4.5", title: "Burning fossil fuels and using alternative energy sources", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-environment-s3", code: "GEO17.3", syllabusRef: "4.5", title: "Environmental pollution", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-environment-s4", code: "GEO17.4", syllabusRef: "4.5", title: "Sustainable economic development", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-environment-s5", code: "GEO17.5", syllabusRef: "4.5", title: "Conflicts between economic interests and environmental interests", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-economic-eu", number: 18, subject: "geography", title: "Ireland and the European Union", examQuestions: [], learningOutcomes: [
        { id: "geo-economic-eu-1", code: "GEO18", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-eu-s1", code: "GEO18.1", syllabusRef: "4.4", title: "EU trading patterns", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-eu-s2", code: "GEO18.2", syllabusRef: "4.4", title: "Irish trading patterns with the EU", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-eu-s3", code: "GEO18.3", syllabusRef: "4.4", title: "How the EU influences the Irish economy", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-economic-globalisation", number: 19, subject: "geography", title: "The Global Economy — Multinationals and Globalisation", examQuestions: [], learningOutcomes: [
        { id: "geo-economic-globalisation-1", code: "GEO19", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-globalisation-s1", code: "GEO19.1", syllabusRef: "4.3", title: "One multinational company (MNC)", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-globalisation-s2", code: "GEO19.2", syllabusRef: "4.3", title: "The MNC and change", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-globalisation-s3", code: "GEO19.3", syllabusRef: "4.3", title: "Patterns in world trade", notes: [], keyTerms: [], questions: [] },
        { id: "geo-economic-globalisation-s4", code: "GEO19.4", syllabusRef: "4.3", title: "How the global economy is organised", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-population-migration", number: 20, subject: "geography", title: "Population Dynamics, Overpopulation and Migration", examQuestions: [], learningOutcomes: [
        { id: "geo-population-migration-1", code: "GEO20", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-population-migration-s1", code: "GEO20.1", syllabusRef: "5.1", title: "Changing population characteristics", notes: [], keyTerms: [], questions: [] },
        { id: "geo-population-migration-s2", code: "GEO20.2", syllabusRef: "5.2", title: "Overpopulation", notes: [], keyTerms: [], questions: [] },
        { id: "geo-population-migration-s3", code: "GEO20.3", syllabusRef: "5.3", title: "Changing migration patterns in Ireland", notes: [], keyTerms: [], questions: [] },
        { id: "geo-population-migration-s4", code: "GEO20.4", syllabusRef: "5.3", title: "Migration policy in Ireland and the EU", notes: [], keyTerms: [], questions: [] },
        { id: "geo-population-migration-s5", code: "GEO20.5", syllabusRef: "5.3", title: "Ethnic, racial and religious issues arising from migration", notes: [], keyTerms: [], questions: [] },
        { id: "geo-population-migration-s6", code: "GEO20.6", syllabusRef: "5.3", title: "Rural-to-urban migration in developed and developing regions", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-urban", number: 21, subject: "geography", title: "Urban Geography — Settlement, Urban Land Use, Planning and Urban Problems", examQuestions: [], learningOutcomes: [
        { id: "geo-urban-1", code: "GEO21", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-urban-s1", code: "GEO21.1", syllabusRef: "5.4", title: "Pre-historic and historic settlement", notes: [], keyTerms: [], questions: [] },
        { id: "geo-urban-s2", code: "GEO21.2", syllabusRef: "5.4", title: "Rural settlement", notes: [], keyTerms: [], questions: [] },
        { id: "geo-urban-s3", code: "GEO21.3", syllabusRef: "5.4", title: "Urban settlement: site, hierarchy, hinterland and central place theory", notes: [], keyTerms: [], questions: [] },
        { id: "geo-urban-s4", code: "GEO21.4", syllabusRef: "5.5", title: "Urban land use and planning", notes: [], keyTerms: [], questions: [] },
        { id: "geo-urban-s5", code: "GEO21.5", syllabusRef: "5.6", title: "Urban problems in developed-world cities", notes: [], keyTerms: [], questions: [] },
        { id: "geo-urban-s6", code: "GEO21.6", syllabusRef: "5.6", title: "Urban planning and renewal", notes: [], keyTerms: [], questions: [] },
        { id: "geo-urban-s7", code: "GEO21.7", syllabusRef: "5.6", title: "Developing-world cities", notes: [], keyTerms: [], questions: [] },
        { id: "geo-urban-s8", code: "GEO21.8", syllabusRef: "5.6", title: "The future of urbanism", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-option-atmosphere-ocean", number: 22, subject: "geography", title: "Option — The Atmosphere-Ocean Environment", examQuestions: [], learningOutcomes: [
        { id: "geo-option-atmosphere-ocean-1", code: "GEO22", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-atmosphere-ocean-s1", code: "GEO22.1", syllabusRef: "9.1", title: "The atmosphere and oceans as linked systems", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-atmosphere-ocean-s2", code: "GEO22.2", syllabusRef: "9.2", title: "Solar energy and its redistribution", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-atmosphere-ocean-s3", code: "GEO22.3", syllabusRef: "9.3", title: "Exchanges of water between oceans and atmosphere", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-atmosphere-ocean-s4", code: "GEO22.4", syllabusRef: "9.4", title: "Atmospheric and oceanic circulation", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-atmosphere-ocean-s5", code: "GEO22.5", syllabusRef: "9.5", title: "Climatic environments and climate change", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-atmosphere-ocean-s6", code: "GEO22.6", syllabusRef: "9.6", title: "Climate and economic development", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-option-culture-identity", number: 23, subject: "geography", title: "Option — Culture and Identity", examQuestions: [], learningOutcomes: [
        { id: "geo-option-culture-identity-1", code: "GEO23", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-culture-identity-s1", code: "GEO23.1", syllabusRef: "8.1", title: "Racial groupings", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-culture-identity-s2", code: "GEO23.2", syllabusRef: "8.1", title: "Language as a cultural indicator", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-culture-identity-s3", code: "GEO23.3", syllabusRef: "8.1", title: "Religion as a cultural indicator", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-culture-identity-s4", code: "GEO23.4", syllabusRef: "8.1", title: "Everyday expressions of culture and identity", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-culture-identity-s5", code: "GEO23.5", syllabusRef: "8.2", title: "Nationality and the nation state", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-culture-identity-s6", code: "GEO23.6", syllabusRef: "8.3", title: "A European regional case study of identity", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-option-geoecology", number: 24, subject: "geography", title: "Option — Geoecology (Soils and Biomes)", examQuestions: [], learningOutcomes: [
        { id: "geo-option-geoecology-1", code: "GEO24", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-geoecology-s1", code: "GEO24.1", syllabusRef: "7.1", title: "Soil composition and characteristics", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-geoecology-s2", code: "GEO24.2", syllabusRef: "7.2", title: "Soil processes and the global pattern of soils", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-geoecology-s3", code: "GEO24.3", syllabusRef: "7.2", title: "Human interference with soils", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-geoecology-s4", code: "GEO24.4", syllabusRef: "7.3", title: "One major biome in detail", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-geoecology-s5", code: "GEO24.5", syllabusRef: "7.4", title: "Human alteration of biomes", notes: [], keyTerms: [], questions: [] }
    ] },
    { id: "geo-option-global-interdependence", number: 25, subject: "geography", title: "Option — Global Interdependence", examQuestions: [], learningOutcomes: [
        { id: "geo-option-global-interdependence-1", code: "GEO25", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-global-interdependence-s1", code: "GEO25.1", syllabusRef: "6.1", title: "Views of development and underdevelopment", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-global-interdependence-s2", code: "GEO25.2", syllabusRef: "6.2", title: "An interdependent global economy", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-global-interdependence-s3", code: "GEO25.3", syllabusRef: "6.3", title: "Empowering people: linking economic growth with human development", notes: [], keyTerms: [], questions: [] },
        { id: "geo-option-global-interdependence-s4", code: "GEO25.4", syllabusRef: "6.4", title: "Sustainable development as a model for the future", notes: [], keyTerms: [], questions: [] }
    ] },
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
    /* All chemistry chapters are split into the subsections of course-outlines/chemistry.md:
       <chapter>-1 is the chapter review (it keeps the chapter's test questions) and
       <chapter>-s<n> are the outline's subsections, whose notes come from content/chemistry/
       via chemistry-notes.js. `syllabusRef` is the specification reference (NCCA
       specification introduced Sept 2025, first examined June 2027). */
    {
      id: "chem1", number: 1, subject: "chemistry", title: "The Nature of Science",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem1-1", code: "CHEM1", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem1-s1", code: "CHEM1.1", syllabusRef: "U1.1, U1 LA", title: "How science works: ideas and models", notes: [], keyTerms: [], questions: [] },
        { id: "chem1-s2", code: "CHEM1.2", syllabusRef: "U1 LA, U1.2", title: "Science as a global enterprise and researching an issue", notes: [], keyTerms: [], questions: [] },
        { id: "chem1-s3", code: "CHEM1.3", syllabusRef: "U2.1–U2.2, U2.3", title: "Questions, hypotheses and designing investigations", notes: [], keyTerms: [], questions: [] },
        { id: "chem1-s4", code: "CHEM1.4", syllabusRef: "U2 LA, U2.4", title: "Measurement, error and data", notes: [], keyTerms: [], questions: [] },
        { id: "chem1-s5", code: "CHEM1.5", syllabusRef: "U2.5, U2.6", title: "Reflecting, recording and communicating findings", notes: [], keyTerms: [], questions: [] },
        { id: "chem1-s6", code: "CHEM1.6", syllabusRef: "U3.1–U3.2, U3.3", title: "Chemistry in society and the media", notes: [], keyTerms: [], questions: [] },
        { id: "chem1-s7", code: "CHEM1.7", syllabusRef: "U4.1–U4.2, Assessment", title: "Representation and the Chemistry in Practice Investigation", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem2", number: 2, subject: "chemistry", title: "Atomic Structure: The Nuclear Model",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem2-1", code: "CHEM2", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem2-s1", code: "CHEM2.1", syllabusRef: "1.2.1, 1.2 LA", title: "Atomic structure: the nuclear model", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem3", number: 3, subject: "chemistry", title: "Atomic Structure: The Bohr and Orbital Models",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem3-1", code: "CHEM3", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem3-s1", code: "CHEM3.1", syllabusRef: "1.2.2, 1.2.3, 1.2.4, 1.2.5", title: "The orbital model and electronic structure", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem4", number: 4, subject: "chemistry", title: "The Periodic Table: Arrangement of Electrons",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem4-1", code: "CHEM4", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem4-s1", code: "CHEM4.1", syllabusRef: "1.3.1, 1.3.3, 1.3 LA", title: "The periodic table: arrangement and use", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem5", number: 5, subject: "chemistry", title: "Chemical Bonding and Structure",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem5-1", code: "CHEM5", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem5-s1", code: "CHEM5.1", syllabusRef: "2.1.1, 2.1.3, 2.2.5", title: "Bonding, formulae and shapes", notes: [], keyTerms: [], questions: [] },
        { id: "chem5-s2", code: "CHEM5.2", syllabusRef: "2.1.5", title: "Investigation: identifying ions in salts and solutions", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem6", number: 6, subject: "chemistry", title: "Electronegativity and the Continuum of Chemical Bonding",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem6-1", code: "CHEM6", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem6-s1", code: "CHEM6.1", syllabusRef: "2.1.2, 2.1.4, 2.2.1", title: "Bond type and intermolecular forces", notes: [], keyTerms: [], questions: [] },
        { id: "chem6-s2", code: "CHEM6.2", syllabusRef: "2.2.2, 2.2.3, 2.2.4", title: "Polarity, shape and physical properties", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem7", number: 7, subject: "chemistry", title: "Families and Trends in the Periodic Table",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem7-1", code: "CHEM7", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem7-s1", code: "CHEM7.1", syllabusRef: "1.3.2, 1.3.4, 1.3.5", title: "Families and trends in the periodic table", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem8", number: 8, subject: "chemistry", title: "The Mole: The Chemist's Counting Unit",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem8-1", code: "CHEM8", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem8-s1", code: "CHEM8.1", syllabusRef: "1.4.1, 1.4.2, 1.4.3, 1.4.4", title: "The mole and molar volume", notes: [], keyTerms: [], questions: [] },
        { id: "chem8-s2", code: "CHEM8.2", syllabusRef: "1.4.5, 1.4.6", title: "Solutions and concentration", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem9", number: 9, subject: "chemistry", title: "Kinetic Theory of Matter and Behaviour of Gases",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem9-1", code: "CHEM9", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem9-s1", code: "CHEM9.1", syllabusRef: "1.1 LA, 1.1.1", title: "The kinetic theory and its evidence", notes: [], keyTerms: [], questions: [] },
        { id: "chem9-s2", code: "CHEM9.2", syllabusRef: "1.1.2, 1.1.3", title: "Using the kinetic theory: separation techniques", notes: [], keyTerms: [], questions: [] },
        { id: "chem9-s3", code: "CHEM9.3", syllabusRef: "2.3.1, 2.3.2", title: "Gas laws and the ideal gas equation", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem10", number: 10, subject: "chemistry", title: "Law of Conservation of Mass: Introducing Stoichiometry",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem10-1", code: "CHEM10", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem10-s1", code: "CHEM10.1", syllabusRef: "1.1.4, 1.1.5", title: "Physical and chemical change", notes: [], keyTerms: [], questions: [] },
        { id: "chem10-s2", code: "CHEM10.2", syllabusRef: "1.4.7", title: "Formulae and balancing equations", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem11", number: 11, subject: "chemistry", title: "Acids and Bases",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem11-1", code: "CHEM11", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem11-s1", code: "CHEM11.1", syllabusRef: "3.4.1, 3.4.2", title: "Acids, bases and their reactions", notes: [], keyTerms: [], questions: [] },
        { id: "chem11-s2", code: "CHEM11.2", syllabusRef: "3.4.3, 3.4.4, 3.4.7", title: "Acid–base theories and strength", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem12", number: 12, subject: "chemistry", title: "Volumetric Analysis: Acid–Base",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem12-1", code: "CHEM12", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem12-s1", code: "CHEM12.1", syllabusRef: "4.1.1, 4.1.2", title: "Standard solutions and acid–base titrations", notes: [], keyTerms: [], questions: [] },
        { id: "chem12-s2", code: "CHEM12.2", syllabusRef: "4.1.3, 4.1.4, 4.1.5", title: "Titration curves, indicators and vinegar", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem13", number: 13, subject: "chemistry", title: "Acid–Base Volumetric Exam-Style Questions",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem13-1", code: "CHEM13", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem13-s1", code: "CHEM13.1", syllabusRef: "4.1.7", title: "Acid–base volumetric problems", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem14", number: 14, subject: "chemistry", title: "Oxidation and Reduction",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem14-1", code: "CHEM14", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem14-s1", code: "CHEM14.1", syllabusRef: "3.5.1", title: "Oxidation and reduction", notes: [], keyTerms: [], questions: [] },
        { id: "chem14-s2", code: "CHEM14.2", syllabusRef: "3.5.2, 3.5.3", title: "Balancing redox equations and the electrochemical series", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem15", number: 15, subject: "chemistry", title: "Volumetric Analysis: Oxidation-Reduction",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem15-1", code: "CHEM15", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem15-s1", code: "CHEM15.1", syllabusRef: "4.1.2, 4.1.6", title: "Redox titrations and iron tablets", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem16", number: 16, subject: "chemistry", title: "Oxidation–Reduction Volumetric Exam-Style Questions",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem16-1", code: "CHEM16", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem16-s1", code: "CHEM16.1", syllabusRef: "4.1.7", title: "Redox volumetric problems", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem17", number: 17, subject: "chemistry", title: "Rates of Reaction",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem17-1", code: "CHEM17", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem17-s1", code: "CHEM17.1", syllabusRef: "3.2.1, 3.2.2", title: "Rate of reaction and collision theory", notes: [], keyTerms: [], questions: [] },
        { id: "chem17-s2", code: "CHEM17.2", syllabusRef: "3.2.3", title: "Investigation: factors affecting rate", notes: [], keyTerms: [], questions: [] },
        { id: "chem17-s3", code: "CHEM17.3", syllabusRef: "3.2.4, 3.2.5", title: "Catalysis", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem18", number: 18, subject: "chemistry", title: "Chemical Equilibrium",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem18-1", code: "CHEM18", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem18-s1", code: "CHEM18.1", syllabusRef: "3.3.1, 3.3.2, 3.3.3", title: "Dynamic equilibrium and Kc", notes: [], keyTerms: [], questions: [] },
        { id: "chem18-s2", code: "CHEM18.2", syllabusRef: "3.3.4, 3.3.5", title: "Le Châtelier's principle", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem19", number: 19, subject: "chemistry", title: "pH and Indicators",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem19-1", code: "CHEM19", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem19-s1", code: "CHEM19.1", syllabusRef: "3.4.5, 3.4.6", title: "Self-ionisation of water and pH", notes: [], keyTerms: [], questions: [] },
        { id: "chem19-s2", code: "CHEM19.2", syllabusRef: "3.4.8, 3.4.9, 3.4.10", title: "pH calculations and dissociation constants", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem20", number: 20, subject: "chemistry", title: "Environmental Chemistry",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem20-1", code: "CHEM20", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem20-s1", code: "CHEM20.1", syllabusRef: "4.3.1, 4.3.2", title: "The greenhouse effect", notes: [], keyTerms: [], questions: [] },
        { id: "chem20-s2", code: "CHEM20.2", syllabusRef: "4.3.3", title: "Water contamination", notes: [], keyTerms: [], questions: [] },
        { id: "chem20-s3", code: "CHEM20.3", syllabusRef: "4.3.4", title: "Treating drinking water", notes: [], keyTerms: [], questions: [] },
        { id: "chem20-s4", code: "CHEM20.4", syllabusRef: "4.3.5", title: "The lithium-ion cell", notes: [], keyTerms: [], questions: [] },
        { id: "chem20-s5", code: "CHEM20.5", syllabusRef: "4.3.8", title: "Researching chemistry", notes: [], keyTerms: [], questions: [] }
      ],
    },
    {
      id: "chem21", number: 21, subject: "chemistry", title: "Thermochemistry",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem21-1", code: "CHEM21", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem21-s1", code: "CHEM21.1", syllabusRef: "3.1.1, 3.1.2", title: "Energy changes in reactions", notes: [], keyTerms: [], questions: [] },
        { id: "chem21-s2", code: "CHEM21.2", syllabusRef: "3.1.3, 3.1.4", title: "Calculating ΔH and the heat of neutralisation", notes: [], keyTerms: [], questions: [] },
        { id: "chem21-s3", code: "CHEM21.3", syllabusRef: "3.1.5", title: "ΔH from bond enthalpies", notes: [], keyTerms: [], questions: [] },
        { id: "chem21-s4", code: "CHEM21.4", syllabusRef: "3.1.6", title: "Hess's law", notes: [], keyTerms: [], questions: [] },
        { id: "chem21-s5", code: "CHEM21.5", syllabusRef: "3.1.7, 3.1.8", title: "Combustion and heats of combustion", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem22", number: 22, subject: "chemistry", title: "Electrochemistry",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem22-1", code: "CHEM22", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem22-s1", code: "CHEM22.1", syllabusRef: "3.5.4, 3.5.5, 3.5.6", title: "Galvanic and electrolytic cells", notes: [], keyTerms: [], questions: [] },
        { id: "chem22-s2", code: "CHEM22.2", syllabusRef: "3.5.7, 3.5.8, 3.5.9", title: "Fuel cells and sustainability", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem23", number: 23, subject: "chemistry", title: "Allotropes of Carbon. Hydrocarbons",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem23-1", code: "CHEM23", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem23-s1", code: "CHEM23.1", syllabusRef: "2.4.1, 2.4.2", title: "Hydrocarbons: sources, uses and impact", notes: [], keyTerms: [], questions: [] },
        { id: "chem23-s2", code: "CHEM23.2", syllabusRef: "2.4.3", title: "Investigation: preparing ethene", notes: [], keyTerms: [], questions: [] },
        { id: "chem23-s3", code: "CHEM23.3", syllabusRef: "2.4.4, 2.4.5, 2.4.6", title: "Groups of hydrocarbons and their properties", notes: [], keyTerms: [], questions: [] },
        { id: "chem23-s4", code: "CHEM23.4", syllabusRef: "2.4.7, 2.4.8, 2.4.9", title: "Shapes, bonding and isomerism", notes: [], keyTerms: [], questions: [] },
        { id: "chem23-s5", code: "CHEM23.5", syllabusRef: "4.3.6, 4.3.7", title: "Allotropes of carbon and their uses", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem24", number: 24, subject: "chemistry", title: "More Families of Organic Compounds",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem24-1", code: "CHEM24", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem24-s1", code: "CHEM24.1", syllabusRef: "4.2.2, 4.2.3", title: "Functional groups, naming and representation", notes: [], keyTerms: [], questions: [] },
        { id: "chem24-s2", code: "CHEM24.2", syllabusRef: "4.2.5, 4.2.12", title: "Physical properties and acidity", notes: [], keyTerms: [], questions: [] },
        { id: "chem24-s3", code: "CHEM24.3", syllabusRef: "4.2.1, 4.2.15", title: "Organic products and pharmaceuticals", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem25", number: 25, subject: "chemistry", title: "Reactions of Organic Compounds",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem25-1", code: "CHEM25", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem25-s1", code: "CHEM25.1", syllabusRef: "4.2.6, 4.2.16", title: "Types of organic reaction and addition polymers", notes: [], keyTerms: [], questions: [] },
        { id: "chem25-s2", code: "CHEM25.2", syllabusRef: "4.2.4, 4.2.7, 4.2.8", title: "Tests, reaction schemes and preparing an ester", notes: [], keyTerms: [], questions: [] },
        { id: "chem25-s3", code: "CHEM25.3", syllabusRef: "4.2.9", title: "Investigation: synthesising benzoic acid", notes: [], keyTerms: [], questions: [] },
        { id: "chem25-s4", code: "CHEM25.4", syllabusRef: "4.2.10", title: "Reaction mechanisms", notes: [], keyTerms: [], questions: [] },
        { id: "chem25-s5", code: "CHEM25.5", syllabusRef: "4.2.11", title: "Redox and acid–base reactions of organic compounds", notes: [], keyTerms: [], questions: [] },
        { id: "chem25-s6", code: "CHEM25.6", syllabusRef: "4.2.13, 4.2.14", title: "Surfactants and soap", notes: [], keyTerms: [], questions: [] },
      ],
    },
    {
      id: "chem26", number: 26, subject: "chemistry", title: "Stoichiometry: Limiting Reactants and Percentage Yield",
      examQuestions: [],
      learningOutcomes: [
        { id: "chem26-1", code: "CHEM26", title: "Chapter review", notes: [], keyTerms: [], questions: [] },
        { id: "chem26-s1", code: "CHEM26.1", syllabusRef: "1.4.7", title: "Quantitative problems from balanced equations", notes: [], keyTerms: [], questions: [] },
        { id: "chem26-s2", code: "CHEM26.2", syllabusRef: "1.4.7", title: "Theoretical, actual and percentage yield", notes: [], keyTerms: [], questions: [] },
        { id: "chem26-s3", code: "CHEM26.3", syllabusRef: "1.4.7", title: "Limiting reagents", notes: [], keyTerms: [], questions: [] }
      ],
    },

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

    // ── Home Economics ─────────────────────────────────────────────────────────
    { id: "hom-carbohydrates",        number: 1,  subject: "home-economics", title: "Carbohydrates and Dietary Fibre",            examQuestions: [], learningOutcomes: [{ id: "hom-carbohydrates-1",        code: "HOM1",  title: "Carbohydrates and Dietary Fibre",            notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-proteins",             number: 2,  subject: "home-economics", title: "Proteins and Amino Acids",                   examQuestions: [], learningOutcomes: [{ id: "hom-proteins-1",             code: "HOM2",  title: "Proteins and Amino Acids",                   notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-lipids",               number: 3,  subject: "home-economics", title: "Lipids and Fats",                            examQuestions: [], learningOutcomes: [{ id: "hom-lipids-1",               code: "HOM3",  title: "Lipids and Fats",                            notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-vitamins-minerals",    number: 4,  subject: "home-economics", title: "Vitamins and Minerals",                      examQuestions: [], learningOutcomes: [{ id: "hom-vitamins-minerals-1",    code: "HOM4",  title: "Vitamins and Minerals",                      notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-digestion-metabolism", number: 5,  subject: "home-economics", title: "Digestion and Metabolism",                   examQuestions: [], learningOutcomes: [{ id: "hom-digestion-metabolism-1", code: "HOM5",  title: "Digestion and Metabolism",                   notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-energy-nutrition",     number: 6,  subject: "home-economics", title: "Energy Balance and Nutritional Needs",       examQuestions: [], learningOutcomes: [{ id: "hom-energy-nutrition-1",     code: "HOM6",  title: "Energy Balance and Nutritional Needs",       notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-meat-preparation",     number: 7,  subject: "home-economics", title: "Meat: Selection, Properties, and Cooking",   examQuestions: [], learningOutcomes: [{ id: "hom-meat-preparation-1",     code: "HOM7",  title: "Meat: Selection, Properties, and Cooking",   notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-fish-seafood",         number: 8,  subject: "home-economics", title: "Fish and Seafood",                           examQuestions: [], learningOutcomes: [{ id: "hom-fish-seafood-1",         code: "HOM8",  title: "Fish and Seafood",                           notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-dairy-eggs",           number: 9,  subject: "home-economics", title: "Dairy Products and Eggs",                    examQuestions: [], learningOutcomes: [{ id: "hom-dairy-eggs-1",           code: "HOM9",  title: "Dairy Products and Eggs",                    notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-cereals-grains",       number: 10, subject: "home-economics", title: "Cereals and Grains",                         examQuestions: [], learningOutcomes: [{ id: "hom-cereals-grains-1",       code: "HOM10", title: "Cereals and Grains",                         notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-cooking-methods",      number: 11, subject: "home-economics", title: "Cooking Methods and Heat Transfer",          examQuestions: [], learningOutcomes: [{ id: "hom-cooking-methods-1",      code: "HOM11", title: "Cooking Methods and Heat Transfer",          notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-food-preservation",    number: 12, subject: "home-economics", title: "Food Preservation and Storage",              examQuestions: [], learningOutcomes: [{ id: "hom-food-preservation-1",    code: "HOM12", title: "Food Preservation and Storage",              notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-food-safety",          number: 13, subject: "home-economics", title: "Food Safety and Microorganisms",             examQuestions: [], learningOutcomes: [{ id: "hom-food-safety-1",          code: "HOM13", title: "Food Safety and Microorganisms",             notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-meal-planning",        number: 14, subject: "home-economics", title: "Meal Planning and Special Diets",            examQuestions: [], learningOutcomes: [{ id: "hom-meal-planning-1",        code: "HOM14", title: "Meal Planning and Special Diets",            notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-food-additives",       number: 15, subject: "home-economics", title: "Food Additives and Processing",              examQuestions: [], learningOutcomes: [{ id: "hom-food-additives-1",       code: "HOM15", title: "Food Additives and Processing",              notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-consumer-rights",      number: 16, subject: "home-economics", title: "Consumer Rights and Protection",             examQuestions: [], learningOutcomes: [{ id: "hom-consumer-rights-1",      code: "HOM16", title: "Consumer Rights and Protection",             notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-personal-finance",     number: 17, subject: "home-economics", title: "Personal Finance and Budgeting",             examQuestions: [], learningOutcomes: [{ id: "hom-personal-finance-1",     code: "HOM17", title: "Personal Finance and Budgeting",             notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-housing",              number: 18, subject: "home-economics", title: "Housing and Accommodation",                  examQuestions: [], learningOutcomes: [{ id: "hom-housing-1",              code: "HOM18", title: "Housing and Accommodation",                  notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-textiles-fibres",      number: 19, subject: "home-economics", title: "Textiles and Fabric Properties",             examQuestions: [], learningOutcomes: [{ id: "hom-textiles-fibres-1",      code: "HOM19", title: "Textiles and Fabric Properties",             notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-clothing-selection",   number: 20, subject: "home-economics", title: "Clothing Selection and Care",                examQuestions: [], learningOutcomes: [{ id: "hom-clothing-selection-1",   code: "HOM20", title: "Clothing Selection and Care",                notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-environmental-issues", number: 21, subject: "home-economics", title: "Environmental Issues and Sustainability",    examQuestions: [], learningOutcomes: [{ id: "hom-environmental-issues-1", code: "HOM21", title: "Environmental Issues and Sustainability",    notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-appliances-equipment", number: 22, subject: "home-economics", title: "Household Appliances and Equipment",         examQuestions: [], learningOutcomes: [{ id: "hom-appliances-equipment-1", code: "HOM22", title: "Household Appliances and Equipment",         notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-sociological-concepts", number: 23, subject: "home-economics", title: "Sociological Terms and Concepts",             examQuestions: [], learningOutcomes: [{ id: "hom-sociological-concepts-1", code: "HOM23", title: "Sociological Terms and Concepts",             notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-family-society",        number: 24, subject: "home-economics", title: "The Family in Society",                       examQuestions: [], learningOutcomes: [{ id: "hom-family-society-1",        code: "HOM24", title: "The Family in Society",                       notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-family-caring",         number: 25, subject: "home-economics", title: "The Family as a Caring Unit",                 examQuestions: [], learningOutcomes: [{ id: "hom-family-caring-1",         code: "HOM25", title: "The Family as a Caring Unit",                 notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-marriage",              number: 26, subject: "home-economics", title: "Marriage",                                    examQuestions: [], learningOutcomes: [{ id: "hom-marriage-1",              code: "HOM26", title: "Marriage",                                    notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-family-law",            number: 27, subject: "home-economics", title: "Family Law",                                  examQuestions: [], learningOutcomes: [{ id: "hom-family-law-1",            code: "HOM27", title: "Family Law",                                  notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-social-change",         number: 28, subject: "home-economics", title: "Social Change and the Family",                 examQuestions: [], learningOutcomes: [{ id: "hom-social-change-1",         code: "HOM28", title: "Social Change and the Family",                 notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-education",             number: 29, subject: "home-economics", title: "Education",                                   examQuestions: [], learningOutcomes: [{ id: "hom-education-1",             code: "HOM29", title: "Education",                                   notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-work-leisure",          number: 30, subject: "home-economics", title: "Work and Leisure",                            examQuestions: [], learningOutcomes: [{ id: "hom-work-leisure-1",          code: "HOM30", title: "Work and Leisure",                            notes: [], keyTerms: [], questions: [] }] },
    { id: "hom-unemployment-poverty",  number: 31, subject: "home-economics", title: "Unemployment, Poverty, and Social Responses", examQuestions: [], learningOutcomes: [{ id: "hom-unemployment-poverty-1",  code: "HOM31", title: "Unemployment, Poverty, and Social Responses", notes: [], keyTerms: [], questions: [] }] },
  ],
};
