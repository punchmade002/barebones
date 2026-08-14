window.EXAM_BREAKDOWN = window.EXAM_BREAKDOWN || {};

window.EXAM_BREAKDOWN.business = {
  subject: "business",
  notice: "The Leaving Certificate Business course has been reworked for the new specification. No exam paper has been released yet under the new format, so a section-by-section breakdown is not available. This page will be updated as soon as a sample or live paper is published."
};

window.EXAM_BREAKDOWN.biology = {
  subject: "biology",
  totalMarks: 400,
  totalMinutes: 180,
  sections: [
    {
      id: "bio-sectionA",
      name: "Section A – Short Questions",
      marks: 100,
      color: "#F97316",
      minutesPerQuestion: 6,
      tips: {
        timing: "≤30 minutes — answer any 5 of the 7 questions (20 marks each, ~6 minutes per question). Attempt all 7 if time allows and your best 5 need not be chosen in advance.",
        structure: "Each answer requires 4–6 precise biological points. Define terms exactly as they appear on the course. Where a diagram is asked for, draw it large, label every structure, and add a title — an unlabelled diagram loses all diagram marks.",
        reminders: [
          "Read all 7 questions before choosing — pick the topics you know most confidently",
          "Use correct biological terminology throughout: generic answers score poorly",
          "Diagrams must be labelled with full structure names, not abbreviations",
          "Spend no more than 6 minutes per question and move on",
          "Section A can cover any part of the course — revise all units"
        ]
      },
      chapterIds: ["bio1","bio2","bio3","bio4","bio5","bio6","bio7","bio8","bio9","bio10","bio11","bio12","bio13","bio14","bio15","bio16","bio17","bio18","bio19","bio20","bio21","bio22","bio23","bio24","bio25","bio26","bio27","bio28","bio29","bio30","bio31","bio32","bio33","bio34","bio35"],
      questionIdPattern: "-AB-q[1-7]$"
    },
    {
      id: "bio-sectionB",
      name: "Section B – Medium Questions",
      marks: 60,
      color: "#10B981",
      minutesPerQuestion: 15,
      tips: {
        timing: "≤30 minutes — answer any 2 of the 3 questions (30 marks each, ~15 minutes per question).",
        structure: "These questions require more developed answers than Section A. Break your answer into clearly labelled sub-parts matching the marks available. For process questions (e.g. photosynthesis, mitosis), describe each stage in sequence. For experiment questions, state: aim, materials, method, result, conclusion.",
        reminders: [
          "Read all 3 questions before choosing your 2 — pick the topics you can develop most fully",
          "Check the mark allocation for each sub-part and write proportionally",
          "Experiment questions follow a fixed structure: aim → materials → procedure → result → conclusion",
          "Comparison questions require a table or paired statements — don't mix up your two items",
          "30 marks means roughly 6–8 developed points per question — don't write a one-line answer"
        ]
      },
      chapterIds: ["bio1","bio2","bio3","bio4","bio5","bio6","bio7","bio8","bio9","bio10","bio11","bio12","bio13","bio14","bio15","bio16","bio17","bio18","bio19","bio20","bio21","bio22","bio23","bio24","bio25","bio26","bio27","bio28","bio29","bio30","bio31","bio32","bio33","bio34","bio35"],
      questionIdPattern: "-AB-q([89]|10)$"
    },
    {
      id: "bio-sectionC",
      name: "Section C – Long Questions",
      marks: 240,
      color: "#3B82F6",
      minutesPerQuestion: 30,
      tips: {
        timing: "120 minutes — answer any 4 of the 6 questions (60 marks each, ~30 minutes per question). Section C questions are supplied on a separate booklet but answered in the same answerbook.",
        structure: "Each 60-mark question is divided into sub-parts. Allocate your time by marks: a 10-mark sub-part needs ~5 minutes; a 30-mark sub-part needs ~15 minutes. Write in full sentences with a point, explanation, and example (PEE). For diagrams: draw large, fully label, add a title. For experiments: always state a valid safety precaution and a control.",
        reminders: [
          "Read all 6 questions before choosing your 4 — Section C questions often focus on specific units (genetics, ecology, human biology)",
          "Section C questions are on a separate booklet — don't misplace it",
          "A correctly labelled diagram can be worth 10–15 marks on its own — invest the time",
          "For genetics questions: show your working in a Punnett square and state the ratio",
          "For ecology questions: know your food webs, energy flow, and at least one studied ecosystem with real species names"
        ]
      },
      chapterIds: ["bio1","bio2","bio3","bio4","bio5","bio6","bio7","bio8","bio9","bio10","bio11","bio12","bio13","bio14","bio15","bio16","bio17","bio18","bio19","bio20","bio21","bio22","bio23","bio24","bio25","bio26","bio27","bio28","bio29","bio30","bio31","bio32","bio33","bio34","bio35"],
      questionIdPattern: "-C-"
    }
  ]
};

window.EXAM_BREAKDOWN.pe = {
  subject: "pe",
  totalMarks: 250,
  totalMinutes: 150,
  sections: [
    {
      id: "pe-sectionA",
      name: "Section A – Short Answer",
      marks: 80,
      color: "#F97316",
      minutesPerQuestion: 5,
      tips: {
        timing: "~50 minutes — answer any 10 of the 12 questions (8 marks each, ~5 minutes per question). You are marked on your best 10, so attempt all 12 if time allows.",
        structure: "Each answer should be 4–6 concise points. Use correct PE terminology — vague answers lose marks. Where the question asks you to 'describe', name the concept and explain it; where it asks you to 'evaluate', give both strengths and a limitation.",
        reminders: [
          "You are marked on your best 10 out of 12 — attempt all 12 if possible",
          "Use PE-specific vocabulary in every answer (e.g. 'VO₂ max', 'periodisation', 'overload principle')",
          "Short questions can cover any topic on the course — revise all areas",
          "Spend no more than 5 minutes per question and move on",
          "If stuck on a question, skip it and return at the end — don't let one question eat your time"
        ]
      },
      chapterIds: ["pe1","pe2","pe3","pe4","pe5","pe6","pe7","pe8","pe9"],
      questionIdPattern: "q([1-9]|1[012])$"
    },
    {
      id: "pe-sectionB",
      name: "Section B – Case Study",
      marks: 50,
      color: "#10B981",
      minutesPerQuestion: 30,
      tips: {
        timing: "~30 minutes — question 13 is compulsory and is the only question in this section.",
        structure: "Read the case study extract carefully before writing anything. Every answer must reference the case study text explicitly — quote from it or refer to named details. Structure each sub-part as: point → explain → link back to the case study.",
        reminders: [
          "This question is compulsory — you must answer it",
          "Reference the case study directly in every sub-part — generic answers that ignore the extract lose marks",
          "Sub-parts are usually worth 10–20 marks each — look at the mark allocation and write proportionally",
          "Highlight or underline key information in the case study before answering",
          "Apply PE theory to the scenario — don't just describe what the person in the case study did"
        ]
      },
      chapterIds: ["pe1","pe2","pe3","pe4","pe5","pe6","pe7","pe8","pe9"],
      questionIdPattern: "q13$"
    },
    {
      id: "pe-sectionC",
      name: "Section C – Long Questions",
      marks: 120,
      color: "#3B82F6",
      minutesPerQuestion: 23,
      tips: {
        timing: "~70 minutes — answer any 3 of the 5 questions (~23 minutes each, 40 marks each).",
        structure: "Each question is worth 40 marks and is split into sub-parts (typically 10 + 10 + 20 marks). Write in clear paragraphs with a point, explanation, and real-world example (PEE structure). For the 20-mark sub-part, aim for 6–8 developed points with examples drawn from sport, athletes, or your own experience.",
        reminders: [
          "Read all 5 questions before choosing your 3 — pick topics you know in depth",
          "Check the mark breakdown of each sub-part and write proportionally",
          "Use real sporting examples (named athlete, sport, or training programme) to support every point",
          "Definitions alone are not enough — you must apply and evaluate concepts",
          "If a question asks you to 'design a training programme', include all required components: goal, methods, duration, overload, recovery"
        ]
      },
      chapterIds: ["pe1","pe2","pe3","pe4","pe5","pe6","pe7","pe8","pe9"],
      questionIdPattern: "q1[4-9]$"
    }
  ]
};

window.EXAM_BREAKDOWN.maths = {
  subject: "maths",
  totalMarks: 600,
  totalMinutes: 300,
  timingNote: "2 papers · 2h 30m each",
  sections: [
    {
      id: "maths-paper1",
      name: "Paper 1",
      marks: 300,
      color: "#F97316",
      minutesPerQuestion: 20,
      tips: {
        timing: "2 hours 30 minutes. Section A: answer any 5 of 6 questions (30 marks each, ~15 min each). Section B: answer any 3 of 4 questions (50 marks each, ~25 min each). Leave 5 minutes at the end to check units and simplification.",
        structure: "Show all working for every step — correct answers without supporting work lose marks. Set out your solution clearly: state what you are finding, show each algebraic or numerical step, and box your final answer. Where units apply, always include them. Give all answers in their simplest form unless the question says otherwise.",
        reminders: [
          "You will lose marks if relevant supporting work is not shown — never just write the answer",
          "Include units of measurement wherever they apply (e.g. cm², m/s, €)",
          "Simplify all answers fully — a correct but unsimplified answer may lose marks",
          "Paper 1 typically covers: Algebra, Functions, Calculus, Complex Numbers, Financial Maths, Sequences & Series",
          "If stuck on a part, move on and return — a blank earns zero but a partial attempt can earn method marks"
        ]
      },
      chapterIds: ["maths1","maths2","maths3","maths4","maths5","maths6","maths7","maths8","maths9","maths10","maths11","maths12","maths13","maths14","maths15","maths16","maths17","maths18","maths19","maths20","maths21","maths22","maths23","maths24","maths25","maths26"]
    },
    {
      id: "maths-paper2",
      name: "Paper 2",
      marks: 300,
      color: "#3B82F6",
      minutesPerQuestion: 20,
      tips: {
        timing: "2 hours 30 minutes. Same structure as Paper 1: Section A — any 5 of 6 (30 marks each); Section B — any 3 of 4 (50 marks each). Both papers are sat on different days.",
        structure: "Show all working at every step. For geometry and trigonometry, draw a clear, labelled diagram before calculating — it helps you set up the correct formula. For probability and statistics, state your formula, substitute values, and show every calculation step. Give answers in simplest form and include units where relevant.",
        reminders: [
          "You will lose marks if relevant supporting work is not shown — never just write the answer",
          "Include units of measurement wherever they apply (e.g. cm, m², degrees)",
          "Simplify all answers fully — a correct but unsimplified fraction or surd may lose marks",
          "Paper 2 typically covers: Statistics, Probability, Geometry, Trigonometry, Coordinate Geometry, Constructions",
          "For constructions: use a compass and ruler only, show all construction arcs clearly, and do not erase them"
        ]
      },
      chapterIds: ["maths1","maths2","maths3","maths4","maths5","maths6","maths7","maths8","maths9","maths10","maths11","maths12","maths13","maths14","maths15","maths16","maths17","maths18","maths19","maths20","maths21","maths22","maths23","maths24","maths25","maths26"]
    }
  ]
};

window.EXAM_BREAKDOWN.geography = {
  subject: "geography",
  totalMarks: 400,
  totalMinutes: 170,
  sections: [
    {
      id: "geo-part1",
      name: "Part 1 – Short Questions",
      marks: 80,
      color: "#F97316",
      minutesPerQuestion: 3,
      tips: {
        timing: "Aim to spend ~35 minutes on Part 1. You have 12 questions and are marked on your 10 best answers — you do not need to choose in advance. Attempt all 12 if time allows; your two weakest are simply dropped.",
        structure: "Each answer should be 3–5 focused sentences. Include a labelled diagram where it adds marks — a good diagram can carry a whole answer. Be specific and use correct geographic terminology.",
        reminders: [
          "You are marked on your 10 best answers out of 12 — attempt all 12 if possible",
          "Diagrams must be fully labelled to earn marks — an unlabelled diagram gets nothing",
          "Questions can come from anywhere: physical geography, volcanoes, plate boundaries, OS maps, surveys, regional geography",
          "Spend roughly 3 minutes per question — stop and move on rather than over-writing one answer",
          "OS map questions: always quote grid references, contour values, or specific map evidence"
        ]
      },
      chapterIds: ["geo1","geo2","geo3","geo4","geo5","geo6","geo7","geo8"],
      questionIdPattern: "Part1"
    },
    {
      id: "geo-part2",
      name: "Part 2 – Structured & Essay Questions",
      marks: 320,
      color: "#3B82F6",
      minutesPerQuestion: 34,
      tips: {
        timing: "~135 minutes for Part 2 (~34 minutes per question). You must answer 4 questions in total: one each from at least 3 of the 4 sections (Physical Environment, Regional Geography, Electives, Options), with your 4th question free choice from any section. Each question carries 80 marks.",
        structure: "Each 80-mark question is split into three parts: two 30-mark SRP essays and one 20-mark flexible question. For a 30-mark essay: write exactly 15 Significant Relevant Points (SRPs) — one standalone piece of geographic information per line. For the 20-mark part: follow the specific instruction carefully (it may be a comprehension extract, a sketch map of a studied region, or a shorter written piece).",
        reminders: [
          "Each SRP must be a distinct, standalone point — repeating or rewording the same idea earns zero for that line",
          "Name a real location in every SRP essay (e.g. 'The San Andreas Fault, California…' or 'The Shannon Region, Ireland…')",
          "For Regional Geography: name your studied region in the very first sentence — examiners need to know which region you are writing about",
          "For sketch maps: include a title, north arrow, legend, and at least 4 labelled features",
          "Budget your 34 minutes per question: ~11 min per 30-mark part, ~8 min for the 20-mark part, ~4 min planning",
          "You must take one question from at least 3 different sections — you cannot answer all 4 from the same section"
        ]
      },
      chapterIds: ["geo1","geo2","geo3","geo4","geo5","geo6","geo7","geo8"],
      questionIdPattern: "Part2"
    }
  ]
};

window.EXAM_BREAKDOWN.chemistry = {
  subject: "chemistry",
  totalMarks: 300,
  totalMinutes: 150,
  sections: [
    {
      id: "chem-sectionA",
      name: "Section A – Compulsory Question",
      marks: 50,
      color: "#F97316",
      minutesPerQuestion: 25,
      tips: {
        timing: "~25 minutes — Q1 is compulsory and worth 50 marks. It is an integrative question combining diagrams, data tables, graphs and multiple short parts across several topics.",
        structure: "Read the stimulus material carefully before writing anything. Each sub-part is worth a set number of marks — check the allocation and write proportionally. For graph/data questions: read the axes carefully, quote values from the graph, and use correct units in every answer.",
        reminders: [
          "Q1 is compulsory — you must answer it, there is no choice",
          "This question integrates content across multiple chapters — broad revision is essential",
          "Quote specific data from any graphs or tables provided — don't describe trends vaguely",
          "Include units in every numerical answer",
          "Diagrams and equations appear regularly — practise drawing and labelling key diagrams"
        ]
      },
      chapterIds: ["chem1","chem2","chem3","chem4","chem5","chem6","chem7","chem8","chem9","chem10","chem11","chem12","chem13","chem14","chem15","chem16","chem17","chem18","chem19","chem20","chem21","chem22","chem23","chem24","chem25","chem26"]
    },
    {
      id: "chem-sectionB",
      name: "Section B – Long Questions",
      marks: 250,
      color: "#3B82F6",
      minutesPerQuestion: 25,
      tips: {
        timing: "~125 minutes — answer any 5 of Q2–Q7 (~25 minutes each, 50 marks each). Read all six questions before choosing your five.",
        structure: "Each 50-mark question is structured with sub-parts and is context-based — a scenario, industrial process, or real-world chemical situation is provided. Answer each sub-part separately and match the depth of your answer to the marks available. For calculations: show every step, include units, and box the final answer.",
        reminders: [
          "Read all 6 questions before choosing your 5 — pick topics where you can show breadth and analysis, not just recall",
          "Questions are context-based — read the scenario carefully and link your answers back to it",
          "Show all working in calculations — a correct answer without working loses marks",
          "Expect cross-topic integration (e.g. a question may combine equilibrium with acids/bases)",
          "The AAC project counts for 40% of your LC grade — the written paper rewards analysis and application over memorisation"
        ]
      },
      chapterIds: ["chem1","chem2","chem3","chem4","chem5","chem6","chem7","chem8","chem9","chem10","chem11","chem12","chem13","chem14","chem15","chem16","chem17","chem18","chem19","chem20","chem21","chem22","chem23","chem24","chem25","chem26"]
    }
  ]
};

window.EXAM_BREAKDOWN.history = {
  subject: "history",
  totalMarks: 400,
  totalMinutes: 170,
  sections: [
    {
      id: "hist-section1",
      name: "Section 1 – Documents",
      color: "#F97316"
    },
    {
      id: "hist-section2",
      name: "Section 2 – Short Questions",
      color: "#10B981"
    },
    {
      id: "hist-section3",
      name: "Section 3 – Long Questions",
      color: "#3B82F6"
    }
  ]
};
