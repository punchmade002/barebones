// Biology HL Content — notes, concept points and flashcards for all chapters.
// Past-paper exam questions live in exam-questions-db.js.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  function ch(id) { return COURSE_DATA.chapters.find(function (c) { return c.id === id; }); }

  // ── bio1: Scientific Knowledge ────────────────────────────────────────────
  (function () {
    var c = ch("bio1");
    // 1.1 — Scientific knowledge, method and publishing
    c.learningOutcomes[0].notes = [
      {
        h: "What is science?",
        b: "A systematic way of building knowledge about the natural world through observation, testing and reasoning, producing explanations supported by repeatable evidence."
      },
      {
        h: "What are the steps of the scientific method?",
        b: "Steps: Observation -> Question -> Hypothesis -> Prediction -> Experiment -> Data collection -> Analysis -> Conclusion -> Publish/repeat."
      },
      {
        h: "What is a hypothesis?",
        b: "A testable, provisional explanation for an observation (e.g. 'plants grow taller with more sunlight'). Early stage and can be rejected."
      },
      {
        h: "What is a theory?",
        b: "A well-supported explanation built from many tested hypotheses (e.g. cell theory, evolution). Stronger than a hypothesis."
      },
      {
        h: "What is a principle or law?",
        b: "A concise statement of a consistently observed relationship in nature, often expressed mathematically (e.g. law of conservation of mass)."
      },
      {
        h: "What is the difference between primary and secondary data?",
        b: "Primary data: collected first-hand by the experimenter. Secondary data: obtained from existing sources such as papers or databases."
      },
      {
        h: "What is peer review?",
        b: "Independent scientists in the same field check the work for flaws before publication. Prevents fraud, errors and duplication."
      },
      {
        h: "What is reproducibility?",
        b: "Other scientists must be able to repeat the experiment and get similar results, confirming reliability."
      },
      {
        h: "What is bias in scientific research?",
        b: "A preference or assumption that distorts results. Sources: poor sampling, funding interests, researcher expectations. Reduced by blind/double-blind methods, large samples and peer review."
      },
      {
        h: "What are the limits of science?",
        b: "Cannot address morality, beauty or faith. Always provisional — new evidence can revise conclusions. Limited by technology, ethics and complexity of natural systems."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is science?",
        definition: "The systematic study of the natural world through observation, testing and reasoning, producing explanations supported by repeatable evidence.",
        section: "1.1"
      },
      {
        term: "What are the steps of the scientific method?",
        definition: "Steps: Observation → Question → Hypothesis → Prediction → Experiment → Data collection → Analysis → Conclusion → Publish/repeat.",
        section: "1.1"
      },
      {
        term: "What is a hypothesis?",
        definition: "A testable, provisional explanation for an observation. Can be supported or rejected by experimental evidence.",
        section: "1.1"
      },
      {
        term: "What is a theory?",
        definition: "A well-supported explanation built from many tested hypotheses. Much stronger than a hypothesis but still open to revision.",
        section: "1.1"
      },
      {
        term: "What is a principle (law)?",
        definition: "A concise statement of a consistently observed relationship in nature, often expressed mathematically. Based on a theory validated over a long time.",
        section: "1.1"
      },
      {
        term: "What is primary data?",
        definition: "Data collected first-hand by the experimenter themselves during an investigation.",
        section: "1.1"
      },
      {
        term: "What is secondary data?",
        definition: "Data obtained from existing sources such as published papers, databases or textbooks.",
        section: "1.1"
      },
      {
        term: "What is peer review?",
        definition: "Independent scientists in the same field evaluate work before publication, checking for errors, fraud and methodological flaws.",
        section: "1.1"
      },
      {
        term: "What is reproducibility?",
        definition: "Other scientists must be able to repeat an experiment and obtain similar results, confirming the reliability of findings.",
        section: "1.1"
      },
      {
        term: "What is bias?",
        definition: "An unfair preference or assumption that distorts results. Reduced by blind/double-blind methods, large samples and peer review.",
        section: "1.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "List the steps of the scientific method in order.",
        model: "Observation, Question, Hypothesis, Prediction, Experiment, Data collection, Analysis, Conclusion, Publish/repeat."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Distinguish between a hypothesis and a theory.",
        model: "A hypothesis is a provisional, testable explanation based on limited evidence. A theory is a well-supported explanation built from many tested hypotheses over time; it is much stronger evidence but still subject to revision."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain what peer review is and why it is important.",
        model: "Peer review is the process where independent experts in the same field scrutinise a study before publication. It catches errors and fraud, ensures methods are sound and allows findings to be trusted and built upon by the wider scientific community."
      },
      {
        type: "short",
        marks: 4,
        prompt: "What is bias in science and give two ways it can be reduced?",
        model: "Bias is a preference or assumption that distorts results (e.g. funding source influencing conclusions). It can be reduced by using blind or double-blind trials so researchers don't know which group is which, and by using large random samples to avoid skewed data."
      },
      {
        type: "short",
        marks: 3,
        prompt: "Give two limitations of the scientific method.",
        model: "Science cannot address questions of morality or faith. All conclusions are provisional and can be overturned by new evidence. It is also limited by available technology and ethical constraints on experimentation."
      }
    ];
    c.examQuestions = [
      {
        id: "bio1-eq-1",
        source: "LC Biology Past Paper — Q7",
        parts: [
          {
            label: "7. (a)",
            question: "In the scientific method, a testable statement is known as a ___. Write the missing word.",
            marks: 3,
            model: "Hypothesis — a testable, provisional explanation for an observation that can be supported or rejected by experiment.",
            diagram: ""
          },
          {
            label: "7. (b)",
            question: "How can this statement be tested?",
            marks: 3,
            model: "By designing a controlled experiment in which all variables are kept constant except the independent variable being investigated; the outcome (dependent variable) is measured and compared to a control.",
            diagram: ""
          },
          {
            label: "7. (c)",
            question: "What is the function of a scientific control?",
            marks: 3,
            model: "A control is an identical experimental setup in which the variable being tested is absent (or at a standard value). It provides a baseline for comparison, ensuring any observed change is caused by the variable under investigation and not by other factors.",
            diagram: ""
          },
          {
            label: "7. (d)",
            question: "Give two limitations of the scientific method.",
            marks: 4,
            model: "1. Science cannot address moral, ethical or faith-based questions — these lie outside its scope. 2. All scientific conclusions are provisional and can be overturned or revised when new evidence becomes available.",
            diagram: ""
          },
          {
            label: "7. (e)",
            question: "Where does a biologist normally publish their results?",
            marks: 3,
            model: "In a peer-reviewed scientific journal, where independent experts in the same field evaluate the methodology and conclusions before publication.",
            diagram: ""
          },
          {
            label: "7. (f)",
            question: "What is meant by the term theory?",
            marks: 3,
            model: "A theory is a well-supported explanation for a body of observations, built from many tested and confirmed hypotheses. It is backed by substantial evidence from repeated experiments and peer review, but remains open to revision if new evidence emerges.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio1-eq-2",
        source: "LC Biology Past Paper — Q2 (Scientific Method)",
        parts: [
          {
            label: "2. (a)",
            question: "After making an observation, a biologist often develops a hypothesis. What is a hypothesis?",
            marks: 4,
            model: "A hypothesis is a testable, provisional explanation proposed to account for an observation. It must be stated in a way that allows it to be supported or rejected through experimental evidence. Example: If soil pH increases above 7, the germination rate of grass seeds will decrease.",
            diagram: ""
          },
          {
            label: "2. (b)",
            question: "A biologist tests their hypothesis by designing an experiment. State two principles of good experimentation.",
            marks: 4,
            model: "1. Control: include an identical setup with the variable being tested absent, to provide a standard of comparison. 2. Repetition/reproducibility: conduct multiple trials to ensure results are consistent and not due to chance or experimental error.",
            diagram: ""
          },
          {
            label: "2. (c)",
            question: "Outline the steps of the scientific method that follow the design of an experiment.",
            marks: 5,
            model: "1. Conduct the experiment and collect data carefully. 2. Analyse the data using tables, graphs or statistical methods. 3. Draw a conclusion — does the evidence support or contradict the hypothesis? 4. Publish findings in a peer-reviewed journal. 5. Allow other scientists to repeat the experiment to verify reproducibility.",
            diagram: ""
          },
          {
            label: "2. (d)",
            question: "The scientific method also has limitations. State any one limitation of the scientific method.",
            marks: 3,
            model: "Science cannot answer questions of morality, ethics or faith — these lie outside its scope. Alternatively: all scientific conclusions are provisional and subject to revision when new evidence is found.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio1-eq-3",
        source: "LC Biology Past Paper — Q2 (Germination Investigation)",
        parts: [
          {
            label: "2. (a)",
            question: "Draw a vertical line on the graph to indicate the pH most suitable for germination of grass seeds.",
            marks: 3,
            model: "Draw the line at approximately pH 6 — this corresponds to the peak of the germination curve where the highest percentage of grass seeds germinate according to the graph.",
            diagram: "images/germination-graph.png"
          },
          {
            label: "2. (b)",
            question: "Explain the term hypothesis.",
            marks: 3,
            model: "A hypothesis is a testable, provisional statement proposed to explain an observation; it can be supported or rejected by experimental evidence.",
            diagram: ""
          },
          {
            label: "2. (c)",
            question: "State one variable from the investigation described above.",
            marks: 2,
            model: "Independent variable: soil pH (the variable changed by the investigator). Dependent variable: percentage germination of grass seeds (the outcome measured).",
            diagram: ""
          },
          {
            label: "2. (d)",
            question: "Controls are often used in investigations. What is the function of a control?",
            marks: 3,
            model: "A control is an experimental setup identical to the test except that the independent variable (soil pH) is kept at a standard or natural value. It allows results to be compared against a baseline, ensuring differences in germination rate are due to pH change alone.",
            diagram: ""
          },
          {
            label: "2. (e)",
            question: "Where might the horticulturist first publish the results of their research?",
            marks: 2,
            model: "In a peer-reviewed scientific journal, where independent scientists evaluate the methodology and findings before publication.",
            diagram: ""
          },
          {
            label: "2. (f)",
            question: "Give two limitations of the scientific method.",
            marks: 3,
            model: "1. Science cannot answer moral, ethical or faith-based questions. 2. All scientific conclusions are provisional and may be revised or overturned as new evidence emerges.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio2: INVESTIGATING IN SCIENCE ────────────────────────────────────────
  (function () {
    var c = ch("bio2");
    // 2.1 — Understand how scientific investigations are designed, conducted, and evaluated with rigour and integrity
    c.learningOutcomes[0].notes = [
      {
        h: "What makes a good scientific question?",
        b: "A question suitable for scientific investigation must be based on a hypothesis, testable by direct observation or scientific tools, and free from opinions or value judgements. A good scientific question is specific, asks only a single thing, and must be something that can actually be tested."
      },
      {
        h: "What is a prediction in scientific investigation?",
        b: "A prediction is the expected outcome if the hypothesis is true — for example, 'If temperature is increased, the rate of germination of cress seeds will increase.' The purpose of running an experiment is to gather evidence that either supports or refutes that prediction."
      },
      {
        h: "What are variables in experiments and how are they classified?",
        b: "A variable is any factor that may change in an experiment. The independent variable is the factor deliberately changed; the dependent variable is the factor measured or observed in response; and controlled variables are all other factors kept the same to ensure a fair test."
      },
      {
        h: "What factors affect the quality of experimental results?",
        b: "Reliability is the degree to which repeated experiments under identical conditions produce the same findings. Accuracy describes how close a measured value is to the true value, while precision describes how closely repeated measurements of the same item agree with each other. Random (statistical) errors arise by chance and are unpredictable, whereas systematic errors are consistent deviations caused by equipment that is old, incorrectly calibrated, or used incorrectly."
      },
      {
        h: "How can fairness be ensured in experiments?",
        b: "To maximise fairness, experiments should include a control set-up (an identical set-up with the key variable absent, used as a comparison), a large random sample, and, where appropriate, a double-blind test in which neither the tester nor the participants know who is receiving the real treatment versus a placebo."
      },
      {
        h: "What are the key safety practices in laboratory work?",
        b: "Laboratory safety requires tying back long hair, wearing a lab coat and goggles where necessary, never tasting or consuming anything in the lab, keeping electrical equipment away from water, and reporting all accidents immediately."
      },
      {
        h: "What is scientific integrity?",
        b: "Scientific integrity means following all rules and values that govern how scientific activities are conducted, reported, and applied. Upholding integrity ensures that scientific reports are clear, unbiased, and repeatable by others."
      },
      {
        h: "What should be considered when selecting equipment for experiments?",
        b: "When choosing equipment for an experiment, consider accuracy (can it measure small amounts?), size (be as specific as possible), and safety (always read chemical safety labels before use)."
      },
      {
        h: "What is the difference between repeatability and reproducibility?",
        b: "Repeatability means that the same person or group using the same equipment and methods obtains very similar results when they repeat a measurement — it is a measure of precision. Reproducibility means that a different person or group, using different equipment or methods, can replicate the findings, demonstrating that the results are not unique to one set of conditions."
      },
      {
        h: "What is data and how should it be displayed?",
        b: "Data is the information or measurements obtained during an investigation. Qualitative data describes something in non-numerical terms, while quantitative data can be counted or measured and expressed as a number, making it objective and statistically analysable. Data is analysed to identify patterns, show relationships, recognise anomalous observations, and draw justified conclusions. Graphs are the preferred way to display data because they make trends easier to identify; the independent variable goes on the x-axis and the dependent variable on the y-axis, with all axes labelled including units."
      },
      {
        h: "What is the difference between correlation and causation?",
        b: "Correlation means there is an association between two variables — they change together. Causation is stronger: it means that a change in one variable is the direct result of a change in the other. Correlation does not automatically imply causation."
      },
      {
        h: "What are anomalous results and why do they occur?",
        b: "An anomalous result is one that does not fit the pattern formed by the rest of the data. Anomalous results can arise from human error, wrong or faulty equipment, or poorly controlled variables, and should be identified and accounted for when drawing conclusions."
      },
      {
        h: "What should a scientific conclusion include?",
        b: "A conclusion is a summary of what an investigation has shown. It should briefly restate the hypothesis, identify the main findings, acknowledge limitations and errors, state whether the hypothesis was supported or not, and suggest improvements or next steps for further investigation."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is an independent variable?",
        definition: "The factor that is deliberately changed by the experimenter in an investigation. Only one independent variable should be altered at a time.",
        section: "2.1"
      },
      {
        term: "What is a dependent variable?",
        definition: "The factor that is measured or observed in an experiment. It changes in response to the independent variable.",
        section: "2.1"
      },
      {
        term: "What is a controlled variable?",
        definition: "A factor kept constant throughout an experiment to ensure that any change in the dependent variable is caused only by the independent variable, making the test fair.",
        section: "2.1"
      },
      {
        term: "What is reliability?",
        definition: "The degree to which repeated experiments, conducted under identical conditions, produce the same or very similar results.",
        section: "2.1"
      },
      {
        term: "What is accuracy?",
        definition: "How close a measured value is to the true or accepted value of the quantity being measured.",
        section: "2.1"
      },
      {
        term: "What is precision?",
        definition: "How closely repeated measurements of the same item agree with one another. High precision means measurements are clustered together, regardless of whether they are close to the true value.",
        section: "2.1"
      },
      {
        term: "What is random error?",
        definition: "An unpredictable, chance mistake in measurement that does not recur consistently. Also called a statistical error.",
        section: "2.1"
      },
      {
        term: "What is systematic error?",
        definition: "A consistent, repeatable deviation between the measured and true value, usually caused by equipment that is old, incorrectly calibrated, or used incorrectly.",
        section: "2.1"
      },
      {
        term: "What is a control experiment?",
        definition: "An experimental set-up that is identical to the main experiment except that the independent variable is absent. It acts as a standard against which the experimental results are judged.",
        section: "2.1"
      },
      {
        term: "What is a double-blind test?",
        definition: "A test in which neither the participants nor the tester know who is receiving the real treatment and who is receiving the placebo, eliminating bias from both sides.",
        section: "2.1"
      },
      {
        term: "What is qualitative data?",
        definition: "Data that describes characteristics or observations in non-numerical terms, such as colour, texture, or shape.",
        section: "2.1"
      },
      {
        term: "What is quantitative data?",
        definition: "Data that can be counted or measured and expressed as a numerical value. It is objective and can be analysed statistically.",
        section: "2.1"
      },
      {
        term: "What is correlation?",
        definition: "A statistical association between two variables — when one changes, the other tends to change too. Correlation does not by itself prove causation.",
        section: "2.1"
      },
      {
        term: "What is an anomalous result?",
        definition: "A result that does not fit the pattern formed by the rest of the data. It may be caused by human error, faulty equipment, or poorly controlled variables.",
        section: "2.1"
      }
    ];
  })();

  // ── bio3: SCIENCE IN SOCIETY ──────────────────────────────────────────────
  (function () {
    var c = ch("bio3");
    // 3.1 — Evaluate scientific evidence critically and understand the relationship between science and society across economic, social, sustainability, and ethical dimensions
    c.learningOutcomes[0].notes = [
      {
        h: "How should scientific evidence be evaluated?",
        b: "To evaluate is to make a judgement about the value of something. Scientific evidence is information gathered from properly conducted research, and each source should be judged under three headings: relevance, accuracy, and bias."
      },
      {
        h: "What is relevant evidence?",
        b: "Relevant evidence is information directly related to the topic under consideration. When judging relevance, consider whether the source closely matches your needs, how specific it is, whether the content relates to your own understanding, and how recently it was published."
      },
      {
        h: "What does accuracy mean in scientific evidence?",
        b: "Accuracy refers to how close a measurement or claim is to the true or accepted value. Checking accuracy involves verifying the truth of the information, whether it is grounded in prior research, whether it used rigorous methods such as randomised double-blind testing with a control, whether it has been peer reviewed, and whether the source is primary or secondary."
      },
      {
        h: "What is biased evidence and how can it be detected?",
        b: "Bias means unfairly selecting or favouring one outcome over another. To detect bias, consider who published the evidence and their purpose, who created the information and what their expertise is, whether the source presents a balanced or one-sided view, whether it targets a particular audience, and who funded the research."
      },
      {
        h: "How do science and society influence each other?",
        b: "Science and society influence each other: new scientific discoveries improve disease control, medicines, food production, agriculture, biotechnology, and our understanding of how organisms interact, while society shapes the direction of scientific research by encouraging some areas and discouraging others. When evaluating the relationship between science and society, four factors must be considered: economic, social, sustainability, and ethical."
      },
      {
        h: "What are the economic factors linking science and society?",
        b: "Basic (pure) science seeks to develop knowledge for its own sake, while applied science (technology) uses scientific knowledge to solve real-world problems. Technology is the application of scientific knowledge for practical purposes, and science has generated significant commercial and financial gains for society, such as increased agricultural crop yields."
      },
      {
        h: "What are the social factors linking science and society?",
        b: "Science has improved society by making life easier and more comfortable through better healthcare, communication, travel, and housing. By reducing the effort required for daily survival, science has freed people to pursue art, education, justice, and improvements to human welfare. However, scientific advances can also harm health indirectly by encouraging sedentary behaviour and increasing access to high-energy foods."
      },
      {
        h: "What are the sustainability factors linking science and society?",
        b: "Sustainability means meeting present needs without compromising the ability of future generations to meet their own needs. It has three interconnected parts: economic development (allowing progress without overconsuming resources), social development (advancing society while reducing pollution and environmental damage), and environmental protection (safeguarding surroundings and controlling use of natural resources)."
      },
      {
        h: "What are the ethical factors linking science and society?",
        b: "Ethics concerns whether an action is right or wrong; bioethics applies this to biology and scientific research. Scientific groups in Ireland have agreed that research should be conducted with honesty, reliability, objectivity, fairness, open communication, duty of care for participants, proper referencing, responsibility for future scientists, and adherence to ethical principles throughout design and conduct."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What does it mean to evaluate?",
        definition: "To make a judgement about the value or quality of something. In science, evaluating evidence involves assessing its relevance, accuracy, and potential bias.",
        section: "3.1"
      },
      {
        term: "What are the steps of peer review?",
        definition: "The process by which scientific work is scrutinised by independent experts in the same field before publication, helping to ensure accuracy and validity.",
        section: "3.1"
      },
      {
        term: "What is a primary source?",
        definition: "An original research report written by the scientists who conducted the study. It is considered more reliable than a secondary source, which summarises or interprets original work.",
        section: "3.1"
      },
      {
        term: "What is basic (pure) science?",
        definition: "Scientific research conducted to develop knowledge for its own sake, without an immediate practical application in mind.",
        section: "3.1"
      },
      {
        term: "What is applied science (technology)?",
        definition: "The use of scientific knowledge to solve real-world practical problems. Technology is the application of scientific knowledge for practical purposes.",
        section: "3.1"
      },
      {
        term: "What is sustainability?",
        definition: "Meeting the needs of the present without compromising the ability of future generations to meet their own needs. It encompasses economic development, social development, and environmental protection.",
        section: "3.1"
      },
      {
        term: "What is bioethics?",
        definition: "The branch of ethics that examines whether actions in biology and scientific research are right or wrong, covering areas such as genetic research, medical trials, and environmental impact.",
        section: "3.1"
      },
      {
        term: "What is a placebo?",
        definition: "An inactive treatment (such as a sugar pill) given to a control group in a clinical trial. Participants do not know whether they have received the real treatment or the placebo.",
        section: "3.1"
      },
      {
        term: "What is objectivity?",
        definition: "The quality of making interpretations and conclusions based solely on evidence, free from personal feelings or external influences.",
        section: "3.1"
      }
    ];
  })();

  // ── bio4: BIOLOGICAL REASONING ────────────────────────────────────────────
  (function () {
    var c = ch("bio4");
    // 4.1 — Apply key biological concepts — including systems, interdependence, evolution, and the transfer of information, matter, and energy — to explain living phenomena
    c.learningOutcomes[0].notes = [
      {
        h: "What is a biological phenomenon?",
        b: "A phenomenon is an observable fact or event that is typically unusual or difficult to fully explain. A biological phenomenon is one associated with a living thing or biological process, and studying such phenomena is a central activity of biology."
      },
      {
        h: "What are models and why are they used?",
        b: "Models are simplified representations of complex systems or phenomena, used to make them easier to understand and communicate. They take many forms, including word descriptions, diagrams, equations, physical scale models, and computer simulations."
      },
      {
        h: "What is the difference between reductionist and systems approaches?",
        b: "A system is a group of structures (often organs in biology) that work together to carry out a particular task. A reductionist approach understands complex systems by breaking them down into increasingly smaller parts, while a systems approach focuses instead on the interactions among those parts, viewing the system as a whole."
      },
      {
        h: "What is interdependence?",
        b: "Interdependence means that living things interact with and rely upon each other and their surroundings in order to survive. No organism exists in complete isolation; all are connected through feeding relationships, competition, symbiosis, and the shared use of environmental resources."
      },
      {
        h: "What is meant by the unity and diversity of life?",
        b: "The unity of life refers to the many features shared by all living things, which exist because all life descended from a common ancestor. The diversity of life refers to the enormous variety of organisms on Earth. Evolution — the gradual change in inherited characteristics over generations — is the single underlying explanation for both unity and diversity."
      },
      {
        h: "What does the principle of 'form fits function' mean?",
        b: "The principle of 'form fits function' states that there is a direct relationship between the structure (form) of a biological object and its role (function). The physical shape or composition of a structure is not arbitrary but is specifically suited to the job it performs."
      },
      {
        h: "What is the transfer of information in living systems?",
        b: "The transfer of information in biology describes how genetic information is used within cells, passed between cells, and transmitted from one generation to the next. Genes, made of DNA, carry the instructions a cell needs to build all its molecules, and also serve as the units of inheritance that pass those instructions to offspring."
      },
      {
        h: "What is the transfer of matter in ecosystems?",
        b: "Matter is anything with mass that takes up space. In biology, matter is transferred from the environment into plants (which absorb chemicals from air and soil), then into animals when they eat plants. When organisms die, decomposers break down plant and animal matter and return it to the environment, where it can be absorbed and reused by plants, completing the cycle."
      },
      {
        h: "What is the transfer of energy in biological systems?",
        b: "Energy is the ability to do work. In biological systems, energy flows in one direction: it enters as sunlight, is captured by plants during photosynthesis, passes through living things via feeding, and is ultimately lost to the surroundings as heat. Unlike matter, energy is not recycled — it flows through and out of ecosystems."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a biological phenomenon?",
        definition: "An observable fact or event associated with a living thing or biological process, often unusual or difficult to fully explain.",
        section: "4.1"
      },
      {
        term: "What is a model (scientific)?",
        definition: "A simplified representation of a complex system or phenomenon, such as a diagram, equation, physical model, or computer simulation, used to aid understanding.",
        section: "4.1"
      },
      {
        term: "What is the reductionist approach?",
        definition: "A method of understanding complex systems by breaking them down into progressively smaller component parts and studying each part separately.",
        section: "4.1"
      },
      {
        term: "What is the systems approach?",
        definition: "A method of understanding complex systems by examining the interactions among all the different parts together, rather than studying parts in isolation.",
        section: "4.1"
      },
      {
        term: "What is interdependence?",
        definition: "The relationship in which living things interact with and rely upon each other and their environment in order to survive.",
        section: "4.1"
      },
      {
        term: "What is the unity of life?",
        definition: "The principle that all living things share many common features (such as the use of DNA) because they all descended from a common ancestor.",
        section: "4.1"
      },
      {
        term: "What is the diversity of life?",
        definition: "The enormous variety of different organisms found on Earth, arising through evolution by natural selection acting over billions of years.",
        section: "4.1"
      },
      {
        term: "What is evolution?",
        definition: "The gradual change in inherited characteristics of populations over successive generations, driven by natural selection. Explains both the unity of life (shared ancestry) and its diversity (adaptation to different environments).",
        section: "4.1"
      },
      {
        term: "What does 'form fits function' mean?",
        definition: "The biological principle that the physical structure (form) of an organ, tissue, or molecule is directly suited to the job (function) it performs.",
        section: "4.1"
      },
      {
        term: "What is the transfer of information?",
        definition: "The process by which genetic information encoded in DNA is used within cells, passed between cells during division, and transmitted from parents to offspring during reproduction.",
        section: "4.1"
      },
      {
        term: "What is the transfer of matter?",
        definition: "The cycling of physical material (atoms and molecules) from the environment into living things through feeding and absorption, and back to the environment through decomposition.",
        section: "4.1"
      },
      {
        term: "What is the transfer of energy?",
        definition: "The one-way flow of energy through biological systems: from the sun into plants via photosynthesis, through food chains via feeding, and ultimately lost to the surroundings as heat.",
        section: "4.1"
      }
    ];
  })();

  // ── bio5: Characteristics of Life ─────────────────────────────────────────
  (function () {
    var c = ch("bio5");
    // 5.1 — Characteristics of life and levels of organisation
    c.learningOutcomes[0].notes = [
      {
        h: "What are the levels of organisation in living organisms?",
        b: "Unicellular -> Multicellular -> Tissue -> Organ -> Organ system -> Organism. Each level is built from the previous."
      },
      {
        h: "What is a tissue?",
        b: "A group of similar cells with a shared function. Human: muscle, nervous, epithelial, connective. Plant: dermal, vascular, ground."
      },
      {
        h: "What is an organ?",
        b: "Structure of several tissues performing a specific function. Human: heart, lung, kidney. Plant: roots, stems, leaves."
      },
      {
        h: "What is a response to stimulus?",
        b: "Detecting and reacting to a stimulus. Animals: fast via nervous system. Plants: slower growth responses called tropisms (phototropism = toward light; geotropism = toward gravity)."
      },
      {
        h: "What is aerobic respiration?",
        b: "Uses oxygen; occurs mainly in mitochondria; breaks glucose down to produce ~38 ATP, CO2 and water."
      },
      {
        h: "What is anaerobic respiration?",
        b: "Without oxygen; occurs in cytoplasm; only ~2 ATP. Produces lactic acid (animals) or ethanol + CO2 (yeast/plants)."
      },
      {
        h: "What is the difference between autotrophic and heterotrophic nutrition?",
        b: "Autotrophic: makes own food via photosynthesis (plants, algae). Heterotrophic: takes in ready-made food (animals, fungi)."
      },
      {
        h: "What is excretion?",
        b: "Removal of metabolic waste. Plants: O2 and CO2 through stomata. Humans: CO2 via lungs; urea via kidneys; water/salts via skin."
      },
      {
        h: "What is the difference between asexual and sexual reproduction?",
        b: "Asexual: one parent, genetically identical offspring (e.g. binary fission). Sexual: two parents, gametes fuse, genetically varied offspring."
      },
      {
        h: "What is metabolism?",
        b: "Sum of all chemical reactions. Anabolic: build complex from simple (require energy, e.g. photosynthesis). Catabolic: break complex down (release energy, e.g. respiration)."
      },
      {
        h: "What is homeostasis?",
        b: "Maintenance of stable internal conditions. Human examples: body temperature (sweating/shivering), blood glucose (insulin/glucagon), water balance (ADH)."
      },
      {
        h: "What are heredity and mutation?",
        b: "Heredity: passing genetic information via DNA. Mutation: change in DNA sequence. Most are neutral/harmful; rare beneficial ones drive evolution (e.g. antibiotic resistance)."
      },
      {
        h: "How are cell sizes measured and calculated?",
        b: "Cells measured in micrometres (um). Bacteria: 1-10 um; animal/plant cells: 10-100 um. Actual size = Image size / Magnification."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a tissue?",
        definition: "A group of similar cells performing a shared function. Examples: muscle, nervous (animals); vascular, dermal (plants).",
        section: "5.1"
      },
      {
        term: "What is an organ?",
        definition: "A structure made of several tissue types performing a specific function. Examples: heart, kidney (animals); root, leaf (plants).",
        section: "5.1"
      },
      {
        term: "What is a response?",
        definition: "Detecting and reacting to a stimulus. Animals respond quickly via the nervous system; plants respond slowly via tropisms.",
        section: "5.1"
      },
      {
        term: "What is aerobic respiration?",
        definition: "Respiration using oxygen, occurring mainly in mitochondria. Produces ~38 ATP, CO2 and water from glucose.",
        section: "5.1"
      },
      {
        term: "What is anaerobic respiration?",
        definition: "Respiration without oxygen, occurring in the cytoplasm. Produces only ~2 ATP. Yields lactic acid (animals) or ethanol + CO2 (yeast).",
        section: "5.1"
      },
      {
        term: "What is autotrophic nutrition?",
        definition: "An organism makes its own food using light energy (photosynthesis). Examples: plants and algae.",
        section: "5.1"
      },
      {
        term: "What is heterotrophic nutrition?",
        definition: "An organism must consume ready-made organic food. Examples: animals and fungi.",
        section: "5.1"
      },
      {
        term: "What is excretion?",
        definition: "The removal of metabolic waste products from an organism. Examples: CO2 and O2 via stomata (plants); CO2 via lungs and urea via kidneys (humans).",
        section: "5.1"
      },
      {
        term: "What is asexual reproduction?",
        definition: "Reproduction from one parent producing genetically identical offspring. Example: binary fission in bacteria.",
        section: "5.1"
      },
      {
        term: "What is sexual reproduction?",
        definition: "Reproduction involving two parents; gametes fuse to produce genetically varied offspring.",
        section: "5.1"
      },
      {
        term: "What is metabolism?",
        definition: "The sum of all chemical reactions in an organism. Anabolic reactions build complex molecules (require energy); catabolic reactions break them down (release energy).",
        section: "5.1"
      },
      {
        term: "What is homeostasis?",
        definition: "The maintenance of stable internal conditions despite changes in the external environment. Examples: body temperature regulation; blood glucose regulation by insulin/glucagon.",
        section: "5.1"
      },
      {
        term: "What is a mutation?",
        definition: "A change in DNA sequence. Most are neutral or harmful; rare beneficial mutations can drive evolution (e.g. antibiotic resistance).",
        section: "5.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Name the seven characteristics of life.",
        model: "Response, Respiration, Nutrition, Excretion, Reproduction, Growth/Metabolism, Homeostasis. A common mnemonic is MRS GREN: Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, Nutrition."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Distinguish between aerobic and anaerobic respiration.",
        model: "Aerobic respiration uses oxygen and occurs mainly in mitochondria, producing ~38 ATP plus CO2 and water. Anaerobic respiration occurs without oxygen in the cytoplasm, producing only ~2 ATP; it yields lactic acid in animals or ethanol + CO2 in yeast."
      },
      {
        type: "short",
        marks: 4,
        prompt: "What is homeostasis? Give two examples in humans.",
        model: "Homeostasis is the maintenance of stable internal conditions. Examples: (1) body temperature — sweating cools, shivering warms; (2) blood glucose — insulin lowers it when high, glucagon raises it when low."
      },
      {
        type: "short",
        marks: 3,
        prompt: "Distinguish between autotrophic and heterotrophic nutrition.",
        model: "Autotrophic organisms make their own food using light energy (photosynthesis), e.g. plants and algae. Heterotrophic organisms must consume ready-made organic food, e.g. animals and fungi."
      }
    ];
  })();

  // ── bio6: Viruses, Classification and Domains of Life ─────────────────────
  (function () {
    var c = ch("bio6");
    // 6.1 — Viruses, classification and the three domains
    c.learningOutcomes[0].notes = [
      {
        h: "What is virus structure?",
        b: "Non-cellular. Protein coat (capsid) surrounding genetic material (DNA or RNA). Some have a lipid envelope. Not alive — no cells, no respiration, no independent reproduction."
      },
      {
        h: "What are the different virus shapes?",
        b: "Helical (TMV), icosahedral (adenovirus), complex (bacteriophages), enveloped (influenza, HIV)."
      },
      {
        h: "What are examples of viral diseases in humans, plants and animals?",
        b: "Human: influenza, measles, HIV/AIDS, COVID-19. Plant: Tobacco Mosaic Virus, Potato Leaf Roll Virus. Animal: foot-and-mouth, rabies, bird flu."
      },
      {
        h: "What are beneficial uses of viruses?",
        b: "Bacteriophage therapy targets antibiotic-resistant bacteria. Biological control (e.g. myxomatosis). Gene therapy and vaccine production use modified viruses."
      },
      {
        h: "What is classification and why is it important?",
        b: "Grouping organisms by shared features. Taxonomy: science of classifying and naming. Importance: organises diversity, allows prediction of features, supports communication."
      },
      {
        h: "What is the binomial system of nomenclature?",
        b: "Every species has a two-word Latin name: Genus species (e.g. Homo sapiens). Genus capitalised; species lowercase; both italicised or underlined."
      },
      {
        h: "What is the difference between prokaryotes and eukaryotes?",
        b: "Prokaryotes: no membrane-bound nucleus, circular DNA, small ribosomes. Eukaryotes: true nucleus, membrane-bound organelles, linear DNA, larger ribosomes."
      },
      {
        h: "What are the three domains of life (Carl Woese, 1990)?",
        b: "Bacteria, Archaea, Eukarya. Archaea are prokaryotic extremophiles differing in cell wall chemistry and rRNA sequences."
      },
      {
        h: "What is phylogeny?",
        b: "Study of evolutionary relationships. DNA sequencing compares base order; more similar = more recent common ancestor. Shown as a phylogenetic tree with branch points (nodes) = common ancestors."
      },
      {
        h: "What is a dichotomous key?",
        b: "An identification tool giving two contrasting choices at each step to lead to the correct identification of an unknown organism."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a virus?",
        definition: "A non-cellular infectious particle consisting of a protein capsid surrounding DNA or RNA. Not alive — cannot reproduce independently.",
        section: "6.1"
      },
      {
        term: "What is a capsid?",
        definition: "The protein coat surrounding a virus's genetic material. Gives the virus its shape (helical, icosahedral, complex or enveloped).",
        section: "6.1"
      },
      {
        term: "What is classification?",
        definition: "The grouping of organisms based on shared features. The science of classifying and naming is called taxonomy.",
        section: "6.1"
      },
      {
        term: "What is the binomial system?",
        definition: "Linnaeus's naming system: every species has a two-part Latin name (Genus species), e.g. Homo sapiens. Genus capitalised; species lowercase; both italicised.",
        section: "6.1"
      },
      {
        term: "What is a prokaryote?",
        definition: "An organism with no membrane-bound nucleus, circular DNA and small ribosomes. Examples: Bacteria and Archaea.",
        section: "6.1"
      },
      {
        term: "What is a eukaryote?",
        definition: "An organism with a true membrane-bound nucleus, linear chromosomes and membrane-bound organelles. Examples: animals, plants, fungi, protists.",
        section: "6.1"
      },
      {
        term: "What are the three domains?",
        definition: "Carl Woese (1990): all life is divided into Bacteria, Archaea and Eukarya based on rRNA sequence differences.",
        section: "6.1"
      },
      {
        term: "What are archaea?",
        definition: "Prokaryotic extremophiles found in hot springs and salt lakes. Differ from Bacteria in cell wall chemistry and rRNA sequences.",
        section: "6.1"
      },
      {
        term: "What is phylogeny?",
        definition: "The study of evolutionary relationships between organisms using DNA sequencing. More similar DNA = more recent common ancestor. Shown as a phylogenetic tree.",
        section: "6.1"
      },
      {
        term: "What is a dichotomous key?",
        definition: "An identification tool that presents two contrasting choices at each step, leading to the correct identification of an unknown organism.",
        section: "6.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Why are viruses considered non-living?",
        model: "Viruses lack cells, cannot carry out respiration, do not grow independently, and cannot reproduce outside a host cell. They have no homeostasis. They are considered non-living because they fail to meet the cell-based criteria for life."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain the binomial naming system and give one example.",
        model: "The binomial system (Linnaeus) gives each species a two-part Latin name: Genus species. The genus is capitalised, species is lowercase, and both are italicised (e.g. Homo sapiens for humans). It allows scientists worldwide to identify organisms unambiguously."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Name the three domains of life and state which organisms belong to each.",
        model: "Bacteria: prokaryotic microorganisms such as E. coli. Archaea: prokaryotic extremophiles found in hot springs and salt lakes. Eukarya: all eukaryotic organisms including animals, plants, fungi and protists."
      },
      {
        type: "short",
        marks: 4,
        prompt: "How is DNA sequencing used to determine evolutionary relationships?",
        model: "Scientists compare the order of DNA bases between species. The more similar two sequences are, the more recently those species shared a common ancestor. Results are displayed on a phylogenetic tree where branch points show divergence events."
      }
    ];
    c.examQuestions = [
      {
        id: "bio6-eq-1",
        source: "LC Biology Past Paper — Q5 (Bacterial Cell)",
        parts: [
          {
            label: "5. (a)",
            question: "The diagram shows a transmission electron microscope (TEM) image of a bacterial cell. There are three types of bacterial shape. Which type is shown in the picture?",
            marks: 2,
            model: "Rod-shaped (bacillus). The three bacterial shapes are: coccus (spherical), bacillus (rod/cylinder-shaped) and spirillum (spiral-shaped).",
            diagram: "images/bacteria-tem.png"
          },
          {
            label: "5. (b)",
            question: "On the diagram, draw an arrow from the letter X to show the location of the bacterial cell wall.",
            marks: 2,
            model: "The bacterial cell wall is the dense layer surrounding and just outside the cell membrane — it appears as the outermost rigid boundary of the cell in the TEM image. Arrow should point to this outer layer.",
            diagram: "images/bacteria-tem.png"
          },
          {
            label: "5. (c)",
            question: "The bacterium is reproducing asexually. What term describes how bacteria reproduce asexually?",
            marks: 2,
            model: "Binary fission. The bacterium replicates its circular DNA, elongates, then divides symmetrically into two genetically identical daughter cells.",
            diagram: ""
          },
          {
            label: "5. (d)",
            question: "Give any one factor that affects the growth of bacteria.",
            marks: 2,
            model: "Temperature: bacteria grow best at their optimal temperature (e.g. ~37 C for human pathogens); temperatures too high or too low slow growth or kill the bacteria. Other valid answers: pH, nutrient availability, oxygen level, presence of antibiotics.",
            diagram: ""
          },
          {
            label: "5. (e)",
            question: "Name any one harmful bacterium.",
            marks: 2,
            model: "Salmonella (food poisoning), Mycobacterium tuberculosis (tuberculosis), Helicobacter pylori (gastric ulcers), Staphylococcus aureus (MRSA/skin infections) or Clostridium tetani (tetanus).",
            diagram: ""
          },
          {
            label: "5. (f) (i)",
            question: "The partially drawn graph represents the microorganism growth curve. By drawing on the graph, complete the first part of the curve.",
            marks: 3,
            model: "The complete growth curve has four phases: (1) Lag phase — flat section at the start as cells adapt to the environment. (2) Log (exponential) phase — steep upward curve as population doubles at a constant rate. (3) Stationary phase — the line levels off (birth rate = death rate). (4) Death/decline phase — downward curve as nutrients deplete and waste builds up. Draw the lag and early log phases to complete the curve.",
            diagram: "images/bacteria-growth.png"
          },
          {
            label: "5. (f) (ii)",
            question: "Name the stage indicated by the letter Z.",
            marks: 2,
            model: "Stationary phase — the rate of cell division equals the death rate so population size remains constant. Nutrients are being used up and waste products are accumulating.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio7: The Unit of Life — The Cell ─────────────────────────────────────
  (function () {
    var c = ch("bio7");
    // 7.1 — Cell theory, microscopy and organelles
    c.learningOutcomes[0].notes = [
      {
        h: "What are the three main points of cell theory?",
        b: "1. All living things are made of one or more cells. 2. The cell is the basic unit of structure and function. 3. All cells come from pre-existing cells."
      },
      {
        h: "What is the difference between light and electron microscopes?",
        b: "Light: visible light + lenses, up to ~1500x, views living cells. Electron: beams of electrons, up to ~500,000x, dead specimens only. TEM = 2D ultrastructure; SEM = 3D surface."
      },
      {
        h: "How is magnification calculated?",
        b: "Magnification = Image size / Actual size. Rearrange for any unknown. Total magnification = eyepiece x objective lens."
      },
      {
        h: "What is the nucleus and what is its function?",
        b: "Control centre; contains chromosomes (DNA + histone proteins); nuclear pores allow mRNA and ribosomes in/out."
      },
      {
        h: "What is the structure and function of mitochondria?",
        b: "Site of aerobic respiration (ATP). Bean-shaped, double membrane; inner membrane (cristae) folded to maximise surface area for the electron transport chain."
      },
      {
        h: "In which cell types are mitochondria abundant?",
        b: "High: muscle, liver, sperm, kidney tubules, root meristems. Low: skin cells, red blood cells."
      },
      {
        h: "What is the function and location of ribosomes?",
        b: "Site of protein synthesis. Free in cytoplasm or on rough ER. Example product: haemoglobin."
      },
      {
        h: "What is the structure and function of chloroplasts?",
        b: "Site of photosynthesis. Thylakoids (stacked into grana) hold chlorophyll; stroma contains enzymes for the dark stage."
      },
      {
        h: "What are the functions of the rough endoplasmic reticulum and Golgi apparatus?",
        b: "Rough ER: ribosome-studded; processes/folds proteins. Golgi: modifies, packages and ships proteins/lipids in vesicles."
      },
      {
        h: "What are the differences between plant and animal cells?",
        b: "Plant only: cellulose cell wall, large central vacuole, chloroplasts, regular box shape. Animal only: no wall, no chloroplasts, irregular shape, small vacuoles."
      },
      {
        h: "How are microscope slides prepared for viewing cells?",
        b: "Cheek cells: scrape, smear, add methylene blue stain, coverslip. Onion cells: peel, place, add iodine stain, coverslip. Lower coverslip at angle to avoid air bubbles."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the cell theory?",
        definition: "Three points: (1) All living things are made of cells. (2) The cell is the basic unit of structure and function. (3) All cells come from pre-existing cells.",
        section: "7.1"
      },
      {
        term: "What is a light microscope?",
        definition: "Uses visible light and glass lenses; maximum magnification ~1,500×; can view living cells. Cheaper but lower resolution than electron microscope.",
        section: "7.1"
      },
      {
        term: "What is an electron microscope?",
        definition: "Uses electron beams; magnification up to ~500,000×; only dead specimens. TEM = 2D ultrastructure; SEM = 3D surface detail.",
        section: "7.1"
      },
      {
        term: "What is magnification?",
        definition: "Magnification = Image size ÷ Actual size. Total magnification = eyepiece lens × objective lens.",
        section: "7.1"
      },
      {
        term: "What is the nucleus?",
        definition: "Control centre of the cell; contains chromosomes (DNA + histones). Nuclear pores allow mRNA and ribosomes to pass in and out.",
        section: "7.1"
      },
      {
        term: "What are mitochondria?",
        definition: "Site of aerobic respiration (ATP production). Double membrane — inner membrane folded into cristae to maximise surface area for the electron transport chain.",
        section: "7.1"
      },
      {
        term: "What are ribosomes?",
        definition: "Site of protein synthesis. Found free in the cytoplasm or on the rough endoplasmic reticulum.",
        section: "7.1"
      },
      {
        term: "What are chloroplasts?",
        definition: "Site of photosynthesis in plant cells. Thylakoids stacked into grana hold chlorophyll; stroma contains Calvin cycle enzymes.",
        section: "7.1"
      },
      {
        term: "What are the roles of the rough ER and Golgi apparatus?",
        definition: "Rough ER: ribosome-studded; processes and folds proteins. Golgi apparatus: modifies, packages and ships proteins and lipids in vesicles.",
        section: "7.1"
      },
      {
        term: "What are the differences between plant and animal cells?",
        definition: "Plant cells only: cellulose cell wall, large central vacuole, chloroplasts, regular box shape. Animal cells only: no wall, no chloroplasts, irregular shape.",
        section: "7.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 3,
        prompt: "State the three points of cell theory.",
        model: "1. All living things are made of one or more cells. 2. The cell is the basic unit of structure and function in living organisms. 3. All cells arise from pre-existing cells."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Compare the light microscope and electron microscope.",
        model: "Light microscope uses visible light and glass lenses; maximum magnification ~1500x; can view living specimens; cheaper. Electron microscope uses electron beams; magnification up to ~500,000x; only dead, prepared specimens; reveals ultrastructure (organelles like ribosomes)."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain why mitochondria have a folded inner membrane.",
        model: "The inner membrane is folded into cristae to greatly increase surface area. This provides more space for the electron transport chain enzymes and ATP synthase, maximising the rate of ATP production during aerobic respiration."
      },
      {
        type: "short",
        marks: 4,
        prompt: "List three structures found in plant cells but not in animal cells and give the function of each.",
        model: "Cell wall (cellulose): provides structural support and prevents bursting. Large central vacuole: stores water, maintains turgor pressure. Chloroplasts: carry out photosynthesis to make glucose from CO2 and water using light energy."
      }
    ];
    c.examQuestions = [
      {
        id: "bio7-eq-1",
        source: "LC Biology Past Paper — Q4 (Cell Membrane)",
        parts: [
          {
            label: "4. (a)",
            question: "The diagram shows the ultrastructure of a cell membrane with parts labelled X and Y. Name the parts labelled X and Y.",
            marks: 4,
            model: "X: Protein molecule — embedded in or spanning the phospholipid bilayer; functions in transport and control of what enters and leaves the cell. Y: Phospholipid molecule — has a hydrophilic phosphate head (facing the watery exterior/interior) and hydrophobic fatty-acid tails (pointing inward), forming the bilayer.",
            diagram: "images/cell-membrane.png"
          },
          {
            label: "4. (b)",
            question: "Give a function of the cell membrane.",
            marks: 3,
            model: "The cell membrane controls what enters and leaves the cell (selective permeability), maintaining a stable internal environment. It allows useful substances such as glucose and oxygen in while keeping harmful substances out.",
            diagram: ""
          },
          {
            label: "4. (c) (i)",
            question: "What term describes cells without membrane-bound organelles?",
            marks: 2,
            model: "Prokaryotic (prokaryotes). Examples: bacteria and archaea. They lack a true nucleus and membrane-bound organelles.",
            diagram: ""
          },
          {
            label: "4. (c) (ii)",
            question: "What term describes cells with membrane-bound organelles?",
            marks: 2,
            model: "Eukaryotic (eukaryotes). Examples: animal, plant, fungal and protist cells. They have a membrane-bound nucleus and organelles.",
            diagram: ""
          },
          {
            label: "4. (d) (i)",
            question: "Plant cells have a cell wall in addition to a cell membrane. Sketch the basic structure of a plant cell, clearly labelling the cell membrane and the cell wall.",
            marks: 5,
            model: "Sketch a rectangular box-shaped cell showing: outer cell wall (thick, cellulose layer), inner cell membrane (thin layer just inside the wall), large central vacuole, chloroplasts in the cytoplasm, and a nucleus. Label both the cell wall (outermost) and cell membrane (inside the wall).",
            diagram: ""
          },
          {
            label: "4. (d) (ii)",
            question: "Give one function of a plant cell wall.",
            marks: 2,
            model: "The cellulose cell wall provides structural support and rigidity to the plant cell. It prevents the cell from bursting when it becomes turgid (after water enters by osmosis), giving non-woody plants their firmness.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio8: Biomolecules — The Chemicals of Life ────────────────────────────
  (function () {
    var c = ch("bio8");
    // 8.1 — Biomolecules, food tests and nutritional roles
    c.learningOutcomes[0].notes = [
      {
        h: "What are carbohydrates and their functions?",
        b: "Elements: C, H, O (H:O ratio 2:1). Monosaccharides (glucose, fructose) -> disaccharides (sucrose, lactose) -> polysaccharides (starch, glycogen, cellulose). Main fuel; storage; structural (cellulose)."
      },
      {
        h: "What are lipids and their functions?",
        b: "Elements: C, H, O (less O than carbs). Glycerol + fatty acids. Triglyceride = 1 glycerol + 3 fatty acids (storage). Phospholipid = 1 glycerol + 2 fatty acids + phosphate = basis of all membranes."
      },
      {
        h: "What is the phospholipid bilayer?",
        b: "Hydrophilic head (phosphate) faces water; hydrophobic tails (fatty acids) face inward. Forms the cell membrane."
      },
      {
        h: "What are proteins and their different types?",
        b: "Elements: C, H, O, N (sometimes S). Basic unit: amino acid (20 types). Fibrous: long, strong, insoluble (keratin, collagen). Globular: rounded, soluble, functional (enzymes, haemoglobin, antibodies, insulin)."
      },
      {
        h: "What are mineral elements and their dietary sources?",
        b: "Calcium (bones/teeth — dairy), iron (haemoglobin — red meat/leafy greens), iodine (thyroid hormone — fish/salt)."
      },
      {
        h: "What is the difference between fat-soluble and water-soluble vitamins?",
        b: "Fat-soluble: A, D, E, K (stored in fat). Water-soluble: B-group, C (not stored, needed daily). Vitamin C deficiency = scurvy. Vitamin D deficiency = rickets (children), osteomalacia (adults)."
      },
      {
        h: "What are the main roles of water in living organisms?",
        b: "Solvent for reactions, transport medium, temperature regulation, lubrication, raw material in photosynthesis, removes wastes."
      },
      {
        h: "How is starch detected in a food test?",
        b: "Reagent: iodine solution. Positive result: blue-black colour."
      },
      {
        h: "How is reducing sugar detected in a food test?",
        b: "Reagent: Benedict's solution + heat. Positive: brick-red precipitate."
      },
      {
        h: "How is protein detected in a food test?",
        b: "Reagent: biuret (NaOH + CuSO4). Positive: purple/violet colour."
      },
      {
        h: "How are lipids detected in a food test?",
        b: "Rub on filter paper: positive = translucent grease spot. Or ethanol emulsion test: cloudy white suspension."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What are carbohydrates?",
        definition: "Contain C, H, O (H:O ratio 2:1). Monosaccharides → disaccharides → polysaccharides. Functions: main energy fuel; storage (starch, glycogen); structural (cellulose).",
        section: "8.1"
      },
      {
        term: "What is a monosaccharide?",
        definition: "The simplest carbohydrate unit. Examples: glucose, fructose, galactose (all C6H12O6).",
        section: "8.1"
      },
      {
        term: "What is a polysaccharide?",
        definition: "Many monosaccharides bonded together. Examples: starch (plant energy store), glycogen (animal/liver store), cellulose (plant cell wall).",
        section: "8.1"
      },
      {
        term: "What is a triglyceride?",
        definition: "A lipid composed of one glycerol + three fatty acids. Used for long-term energy storage in adipose tissue.",
        section: "8.1"
      },
      {
        term: "What is a phospholipid?",
        definition: "One glycerol + two fatty acids + one phosphate group. Hydrophilic head faces water; hydrophobic tails face inward. Forms the cell membrane bilayer.",
        section: "8.1"
      },
      {
        term: "What is the role of fibrous proteins?",
        definition: "Long, strong, insoluble protein with a structural role. Examples: collagen (tendons, skin), keratin (hair, nails).",
        section: "8.1"
      },
      {
        term: "What is the role of globular proteins?",
        definition: "Rounded, soluble protein with a functional role. Examples: enzymes, haemoglobin, antibodies, insulin.",
        section: "8.1"
      },
      {
        term: "What is an amino acid?",
        definition: "The basic monomer unit of proteins. There are 20 different amino acids joined by peptide bonds to form polypeptides.",
        section: "8.1"
      },
      {
        term: "What are fat-soluble vitamins?",
        definition: "Vitamins A, D, E and K. Stored in body fat and the liver; not needed daily. Vitamin D deficiency causes rickets (children).",
        section: "8.1"
      },
      {
        term: "What are water-soluble vitamins?",
        definition: "B-group vitamins and Vitamin C. Not stored in the body — must be consumed daily. Vitamin C deficiency causes scurvy.",
        section: "8.1"
      },
      {
        term: "What is the food test for starch?",
        definition: "Reagent: iodine solution. Positive result: blue-black colour.",
        section: "8.1"
      },
      {
        term: "What is the food test for reducing sugar?",
        definition: "Reagent: Benedict's solution + heat. Positive result: brick-red precipitate.",
        section: "8.1"
      },
      {
        term: "What is the food test for protein?",
        definition: "Reagent: biuret reagent (NaOH + CuSO4). Positive result: purple/violet colour.",
        section: "8.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Describe the food test for starch and protein.",
        model: "Starch: add iodine solution to the sample; a positive result gives a blue-black colour. Protein: add biuret reagent (NaOH then CuSO4) to the sample; a positive result gives a purple/violet colour."
      },
      {
        type: "short",
        marks: 4,
        prompt: "What is the difference between a triglyceride and a phospholipid?",
        model: "A triglyceride has one glycerol molecule joined to three fatty acids; it is a storage molecule. A phospholipid has one glycerol, two fatty acids and one phosphate group; the phosphate head is hydrophilic and the fatty acid tails are hydrophobic, so phospholipids form the bilayer of cell membranes."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Distinguish between fibrous and globular proteins, giving one example of each.",
        model: "Fibrous proteins are long, strong and insoluble, serving structural roles (e.g. collagen in tendons and skin). Globular proteins are rounded, soluble and carry out functional roles (e.g. haemoglobin transporting oxygen, or enzymes catalysing reactions)."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Give two symptoms of vitamin C deficiency and explain why they occur.",
        model: "Vitamin C is needed for collagen synthesis. Deficiency (scurvy) causes bleeding gums (collagen in blood vessel walls breaks down) and poor wound healing (collagen is needed to form scar tissue). Regular intake of citrus fruit, peppers or broccoli prevents this."
      }
    ];
    c.examQuestions = [
      {
        id: "bio8-eq-1",
        source: "LC Biology Past Paper — Q1 (Carbohydrates & Proteins)",
        parts: [
          {
            label: "1. (a)",
            question: "Write the general formula for carbohydrates.",
            marks: 3,
            model: "CH2O (or (CH2O)n / Cn(H2O)n). The ratio of hydrogen to oxygen in carbohydrates is always 2:1, the same as in water.",
            diagram: ""
          },
          {
            label: "1. (b)",
            question: "Give the four chemical elements found in all proteins.",
            marks: 4,
            model: "Carbon (C), Hydrogen (H), Oxygen (O) and Nitrogen (N). Some proteins also contain Sulfur (S), but C, H, O, N are present in ALL proteins.",
            diagram: ""
          },
          {
            label: "1. (c)",
            question: "State one structural role of proteins in the body.",
            marks: 3,
            model: "Collagen: the most abundant structural protein in the body; forms tendons, ligaments, cartilage, bone matrix and skin, providing tensile strength. Alternatively: Keratin forms hair, nails and the outer layer of skin.",
            diagram: ""
          },
          {
            label: "1. (d)",
            question: "Name the small subunits that make protein.",
            marks: 2,
            model: "Amino acids. There are 20 different amino acids joined by peptide bonds to form polypeptide chains, which fold into functional proteins.",
            diagram: ""
          },
          {
            label: "1. (e)",
            question: "Name one water-soluble vitamin.",
            marks: 2,
            model: "Vitamin C (ascorbic acid), or any B-group vitamin (B1 thiamine, B2 riboflavin, B12 cobalamin, etc.). Water-soluble vitamins are not stored in the body and must be consumed regularly.",
            diagram: ""
          },
          {
            label: "1. (f)",
            question: "Give one example of a trace element found in food.",
            marks: 2,
            model: "Iron (Fe) — found in red meat, spinach and legumes; required for haemoglobin synthesis. Other valid examples: Iodine (fish/iodised salt, thyroid hormone) or Calcium (dairy, bones/teeth).",
            diagram: ""
          }
        ]
      },
      {
        id: "bio8-eq-2",
        source: "LC Biology Past Paper — Q1 (Lipids)",
        parts: [
          {
            label: "1. (a)",
            question: "Which three chemical elements are present in all lipids?",
            marks: 3,
            model: "Carbon (C), Hydrogen (H) and Oxygen (O). Lipids contain significantly less oxygen relative to hydrogen compared to carbohydrates, making them a more concentrated energy store.",
            diagram: ""
          },
          {
            label: "1. (b)",
            question: "How do fats and oils differ at room temperature?",
            marks: 3,
            model: "Fats are solid at room temperature (e.g. butter, lard) — they are typically of animal origin and contain mainly saturated fatty acids. Oils are liquid at room temperature (e.g. olive oil) — they are typically of plant origin and contain mainly unsaturated fatty acids.",
            diagram: ""
          },
          {
            label: "1. (c)",
            question: "Give one way phospholipids differ from triglycerides.",
            marks: 3,
            model: "A phospholipid has two fatty-acid tails instead of three — the third is replaced by a phosphate group. This gives the phospholipid a hydrophilic (water-attracting) head and hydrophobic (water-repelling) tails, allowing it to form the cell membrane bilayer. Triglycerides are energy-storage molecules.",
            diagram: ""
          },
          {
            label: "1. (d)",
            question: "Give one metabolic role of lipids in cells.",
            marks: 3,
            model: "Lipids are a concentrated energy store — containing approximately twice as much energy per gram as carbohydrates. Adipose tissue stores triglycerides that can be broken down by lipase for use in cellular respiration when glucose is scarce.",
            diagram: ""
          },
          {
            label: "1. (e)",
            question: "Give one structural role of lipids in cells.",
            marks: 3,
            model: "Phospholipids form the phospholipid bilayer of all cell membranes, providing a selectively permeable boundary that controls what enters and leaves the cell.",
            diagram: ""
          },
          {
            label: "1. (f)",
            question: "Name one fat-soluble vitamin.",
            marks: 2,
            model: "Vitamin A, D, E or K. These vitamins dissolve in fats and oils, are absorbed with dietary fat from the gut, and can be stored in adipose tissue and the liver.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio8-eq-3",
        source: "LC Biology Past Paper — Q1 (Carbohydrates — detailed)",
        parts: [
          {
            label: "1. (a)",
            question: "Name the three chemical elements present in all carbohydrates.",
            marks: 3,
            model: "Carbon (C), Hydrogen (H) and Oxygen (O). The H:O ratio is always 2:1.",
            diagram: ""
          },
          {
            label: "1. (b)",
            question: "Give the general formula for carbohydrates.",
            marks: 2,
            model: "CH2O (or (CH2O)n / Cn(H2O)n).",
            diagram: ""
          },
          {
            label: "1. (c)",
            question: "Name the smallest unit of a carbohydrate.",
            marks: 2,
            model: "Monosaccharide (single sugar). Examples: glucose, fructose, galactose (all with formula C6H12O6).",
            diagram: ""
          },
          {
            label: "1. (d)",
            question: "Name the type of carbohydrate formed when many monosaccharide units bond together.",
            marks: 2,
            model: "Polysaccharide. Examples: starch (energy storage in plants), glycogen (energy storage in animals/liver), cellulose (structural in plant cell walls).",
            diagram: ""
          },
          {
            label: "1. (e)",
            question: "Give one structural role of carbohydrates in living organisms.",
            marks: 3,
            model: "Cellulose — a polysaccharide composed of beta-glucose units — forms the rigid cell wall of plant cells, providing mechanical support and preventing the cell from bursting when turgid.",
            diagram: ""
          },
          {
            label: "1. (f)",
            question: "Carbohydrates are an important component of the diet. State one dietary source of carbohydrates.",
            marks: 2,
            model: "Bread, pasta, rice, potatoes, cereals, fruit or vegetables — any starch- or sugar-containing food.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio9: Transfer Molecules ──────────────────────────────────────────────
  (function () {
    var c = ch("bio9");
    // 9.1 — The structure and roles of ATP, NAD+ and NADP+ as energy-carrying transfer molecules in cells
    c.learningOutcomes[0].notes = [
      {
        h: "ADP (adenosine diphosphate)",
        b: "ADP is a low-energy molecule built from three components: adenine (a nitrogen base), ribose (a five-carbon sugar), and two phosphate groups. It serves as the precursor molecule that is converted into the high-energy carrier ATP."
      },
      {
        h: "ATP (adenosine triphosphate)",
        b: "ATP is a high-energy molecule formed when ADP gains a phosphate group and energy, either from sunlight during photosynthesis or from the breakdown of food during respiration. It acts as the cell's universal energy carrier: when ATP is broken down by water it releases energy and regenerates ADP and a free phosphate group, and that energy drives cellular processes such as protein synthesis, mitosis and active transport. ATP is advantageous because it is high-energy, easily broken down, releases energy readily, and is reusable."
      },
      {
        h: "NAD+ (nicotinamide adenine dinucleotide)",
        b: "NAD+ is a low-energy coenzyme derived from the B-group vitamin niacin that functions during respiration. It accepts two high-energy electrons and a hydrogen ion (proton) to become NADH, a high-energy molecule. When NADH is subsequently broken down it releases energy, electrons and a hydrogen ion, making NAD+/NADH a key electron and energy shuttle in respiration."
      },
      {
        h: "NADP+ (nicotinamide adenine dinucleotide phosphate)",
        b: "NADP+ is a low-energy molecule that plays the equivalent role to NAD+ but specifically in photosynthesis. It accepts two high-energy electrons and a hydrogen ion to form NADPH. When NADPH breaks down it releases those electrons and a hydrogen ion, which are used in photosynthesis to synthesise the sugar glucose, making NADP+/NADPH an essential electron and energy carrier in the light-dependent and light-independent reactions."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is ADP (adenosine diphosphate)?",
        definition: "A low-energy molecule composed of adenine, ribose and two phosphate groups. It is the precursor to ATP and is regenerated when ATP releases its energy.",
        section: "9.1"
      },
      {
        term: "What is ATP (adenosine triphosphate)?",
        definition: "The cell's primary high-energy carrier molecule, formed by adding a phosphate group and energy to ADP. When hydrolysed by water it releases energy for cellular processes such as protein synthesis, mitosis and active transport.",
        section: "9.1"
      },
      {
        term: "What is phosphorylation?",
        definition: "The addition of a phosphate group to a molecule. When ADP is phosphorylated using energy from respiration or photosynthesis, ATP is produced.",
        section: "9.1"
      },
      {
        term: "What is NAD+ (nicotinamide adenine dinucleotide)?",
        definition: "A low-energy coenzyme derived from the vitamin niacin that functions as an electron and hydrogen carrier in respiration. It is reduced to NADH by accepting two electrons and one hydrogen ion.",
        section: "9.1"
      },
      {
        term: "What is NADH?",
        definition: "The high-energy, reduced form of NAD+. When NADH is oxidised it releases energy, electrons and a hydrogen ion for use in the electron transport chain of respiration.",
        section: "9.1"
      },
      {
        term: "What is NADP+ (nicotinamide adenine dinucleotide phosphate)?",
        definition: "A low-energy coenzyme used in photosynthesis that accepts two electrons and a hydrogen ion to become NADPH. It is the photosynthetic equivalent of NAD+ in respiration.",
        section: "9.1"
      },
      {
        term: "What is NADPH?",
        definition: "The high-energy, reduced form of NADP+. It donates electrons and a hydrogen ion during the light-independent reactions of photosynthesis to drive the synthesis of glucose.",
        section: "9.1"
      },
      {
        term: "What is a coenzyme?",
        definition: "A non-protein molecule that assists an enzyme in carrying out its function. NAD+ and NADP+ are coenzymes that carry electrons and hydrogen ions between reactions.",
        section: "9.1"
      }
    ];
  })();

  // ── bio10: DNA, RNA and the Genetic Code ──────────────────────────────────
  (function () {
    var c = ch("bio10");
    // 10.1 — The structure of DNA and RNA, the functions of DNA, and how the genetic code directs protein synthesis
    c.learningOutcomes[0].notes = [
      {
        h: "What are nucleic acids and what are their principal types?",
        b: "Nucleic acids are large biomolecules assembled from repeating sub-units called nucleotides. The two principal nucleic acids are DNA (deoxyribonucleic acid) and RNA (ribonucleic acid), both of which carry genetic information."
      },
      {
        h: "What is the structure of DNA?",
        b: "DNA was discovered by James Watson and Francis Crick. Each nucleotide consists of a phosphate group, the sugar deoxyribose, and one of four nitrogen-containing bases: adenine (A), thymine (T), guanine (G) or cytosine (C). Nucleotides link into polynucleotide chains, and two chains pair via hydrogen bonds — A pairs with T (two bonds) and G pairs with C (three bonds) — forming the rungs of a double helix whose outer backbone is composed of alternating phosphate and deoxyribose groups."
      },
      {
        h: "What is the relationship between chromosomes, DNA and genes?",
        b: "Chromosomes are composed of approximately 60% protein and 40% DNA, with the DNA molecule tightly wrapped around the protein. Genes are specific sections of DNA located along a chromosome that encode the information needed to produce a particular protein. Gene expression is the process by which that genetic instruction is converted into a functional protein."
      },
      {
        h: "What is the structure of RNA?",
        b: "RNA nucleotides contain the sugar ribose (rather than deoxyribose) and use uracil (U) in place of thymine, while retaining adenine, guanine and cytosine. Unlike DNA, RNA is single-stranded and is generally a much shorter molecule, allowing it to move out of the nucleus to carry instructions to ribosomes."
      },
      {
        h: "What are the main functions of DNA?",
        b: "DNA has three core functions: it stores inherited information (each gene encodes a protein that controls cell activities), it passes on inherited information through DNA replication so genetic information is transmitted from cell to cell and generation to generation via sperm and egg cells, and it directs protein synthesis through gene expression, where genes produce RNA that travels to ribosomes to assemble amino acids into proteins."
      },
      {
        h: "What is the difference between coding and non-coding DNA?",
        b: "Coding DNA contains the genetic instructions that are translated into proteins. Non-coding DNA does not produce a protein and accounts for up to 98% of the human genome. Protein formation follows a defined sequence: a gene in the nucleus produces RNA, the RNA moves to a ribosome in the cytoplasm, a specific sequence of amino acids assembles at the ribosome and bonds together, and the resulting chain folds into a functional protein."
      },
      {
        h: "What is the relationship between genes, proteins and traits?",
        b: "A characteristic is an inherited feature that varies among individuals (e.g. eye colour), while a trait is one particular variant of that characteristic (e.g. blue eyes). Genes produce proteins that determine traits — for example, the gene(s) for brown eyes causes production of pigment proteins that result in brown colouration."
      },
      {
        h: "What is the genetic code?",
        b: "The genetic code is the set of rules by which sequences of bases in DNA, read in groups of three called codons (or triplets), specify a particular amino acid and therefore the sequence of a protein. A start codon marks the beginning of a gene, most codons specify an amino acid, and a stop codon signals the end of the gene."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a nucleotide?",
        definition: "The monomer sub-unit of nucleic acids, consisting of a phosphate group, a five-carbon sugar and a nitrogen-containing base. Nucleotides link together to form polynucleotide chains.",
        section: "10.1"
      },
      {
        term: "What is DNA (deoxyribonucleic acid)?",
        definition: "A double-stranded helical nucleic acid whose sequence of bases stores and transmits genetic information. It contains the bases adenine, thymine, guanine and cytosine, and uses the sugar deoxyribose.",
        section: "10.1"
      },
      {
        term: "What is the double helix?",
        definition: "The three-dimensional structure of DNA, consisting of two antiparallel polynucleotide strands coiled around each other, with complementary base pairs forming the internal rungs held by hydrogen bonds.",
        section: "10.1"
      },
      {
        term: "What is base pairing?",
        definition: "The specific hydrogen-bond pairing between complementary bases in DNA: adenine pairs with thymine (two bonds) and guanine pairs with cytosine (three bonds). In RNA, uracil replaces thymine.",
        section: "10.1"
      },
      {
        term: "What is a gene?",
        definition: "A section of DNA on a chromosome that encodes the instructions for producing a specific protein, thereby controlling a cell activity or determining a trait.",
        section: "10.1"
      },
      {
        term: "What are the steps of gene expression?",
        definition: "The process by which the information in a gene is used to direct the synthesis of a protein. It involves transcription of DNA into RNA followed by translation of RNA into a polypeptide at a ribosome.",
        section: "10.1"
      },
      {
        term: "What is RNA (ribonucleic acid)?",
        definition: "A single-stranded nucleic acid that uses the sugar ribose and the base uracil instead of thymine. RNA carries genetic instructions from DNA in the nucleus to ribosomes in the cytoplasm.",
        section: "10.1"
      },
      {
        term: "What is a codon (triplet)?",
        definition: "A sequence of three consecutive nucleotide bases in DNA or RNA that specifies a particular amino acid. Start codons signal the beginning of a gene and stop codons signal its end.",
        section: "10.1"
      },
      {
        term: "What is coding DNA?",
        definition: "Regions of DNA that contain genetic instructions transcribed and translated into protein. It contrasts with non-coding DNA, which comprises up to 98% of the human genome and does not produce protein.",
        section: "10.1"
      },
      {
        term: "What is a trait?",
        definition: "A specific variant of an inherited characteristic; for example, blue eyes is a trait of the characteristic eye colour. Traits are ultimately determined by the proteins encoded by genes.",
        section: "10.1"
      }
    ];
  })();

  // ── bio11: Genetic Inheritance ────────────────────────────────────────────
  (function () {
    var c = ch("bio11");
    // 11.1 — The principles of genetic inheritance including chromosome structure, Mendel's laws, sex linkage and gene linkage
    c.learningOutcomes[0].notes = [
      {
        h: "What is the structure of a chromosome?",
        b: "Chromosomes are structures found in the cell nucleus, each consisting of one long DNA molecule wrapped around histone proteins. During interphase (when cells are not dividing), chromosomes are highly elongated and indistinguishable from one another — in this state they are collectively called chromatin. Human diploid cells contain 46 chromosomes, while haploid cells (sperm and egg) contain 23."
      },
      {
        h: "What are genes and what is inheritance?",
        b: "Genes are sections of DNA located on chromosomes; they are both the instructions for producing proteins and the basic units of inheritance. The genome is the complete set of all genetic material of an organism, and genomics is its study. Nuclear DNA — located in the nucleus — is inherited equally from each parent via sperm and eggs, a process called nuclear inheritance."
      },
      {
        h: "What are genetic and epigenetic mechanisms?",
        b: "Heredity is the passing of features from parents to offspring via genes, and genetics is the scientific study of heredity. Epigenetics studies how traits are inherited through mechanisms that do not alter the DNA sequence itself. Epigenetic factors can switch genes on or off, change naturally during a person's lifetime or in response to external factors such as smoking, affect health, and be passed on to subsequent generations."
      },
      {
        h: "What is the terminology used in genetic crosses?",
        b: "A locus is the specific position of a gene on a chromosome; alleles are different forms of the same gene. The dominant allele prevents the recessive allele from being expressed. Homozygous individuals carry two identical alleles; heterozygous individuals carry two different alleles. Genotype refers to the actual alleles present, while phenotype is the observable physical expression of those alleles. A monohybrid cross studies one characteristic; a dihybrid cross studies two. A Punnett square displays all possible offspring genotypes, and a pedigree diagrams the inheritance pattern in a family."
      },
      {
        h: "What is the difference between autosomes and heterosomes?",
        b: "Somatic cells are all body cells that do not produce gametes. A homologous pair consists of two chromosomes with similar gene sequences, one from each parent. Of the 46 human chromosomes, 44 are autosomes (non-sex chromosomes) and 2 are heterosomes (sex chromosomes): XX produces a female and XY produces a male."
      },
      {
        h: "What are Mendel's laws of inheritance?",
        b: "Gregor Mendel, 'the father of genetics', established two fundamental laws. His first law (law of segregation) states that inherited characteristics are controlled by pairs of alleles that separate at gamete formation, so each gamete carries only one allele from each pair. His second law (law of independent assortment) states that during gamete formation, either allele of one pair is equally likely to combine with either allele of a second pair. Mendelian genetics enables prediction of inheritance patterns, supports genetic counselling, underpins selective breeding, and aids understanding of evolution; its limitations are that it applies only to single-gene traits and does not account for environmental interactions, epigenetics, or linked genes."
      },
      {
        h: "What is sex linkage?",
        b: "The female always contributes an X chromosome to the egg; the male determines the sex of a child by contributing either an X chromosome (producing a female, XX) or a Y chromosome (producing a male, XY) in his sperm. Sex linkage means a trait is controlled by a gene on a sex chromosome, usually the X chromosome, making recessive sex-linked phenotypes more common in males. Examples include colour blindness, haemophilia, and Duchenne muscular dystrophy."
      },
      {
        h: "What are the different dominance patterns?",
        b: "Complete dominance occurs when the dominant allele fully prevents the recessive allele from being expressed in a heterozygote. Incomplete dominance occurs when neither allele is fully dominant, so both alleles are expressed in the heterozygous individual, producing an intermediate phenotype."
      },
      {
        h: "What is non-nuclear DNA?",
        b: "Non-nuclear (extranuclear) DNA is found outside the nucleus in mitochondria (mtDNA) and chloroplasts (cpDNA). Mitochondrial DNA is inherited exclusively through the maternal line, as mitochondria are passed from mother to offspring via the egg cell."
      },
      {
        h: "What is gene linkage?",
        b: "Gene linkage means that two or more genes are located on the same chromosome and therefore tend to be inherited together, reducing variation among gametes. Gene linkage contradicts Mendel's law of independent assortment, which assumes genes on different chromosomes assort freely."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is chromatin?",
        definition: "The dispersed, elongated form of chromosomes visible during interphase, when cells are not dividing. Chromatin consists of DNA wrapped around histone proteins.",
        section: "11.1"
      },
      {
        term: "What is an allele?",
        definition: "One of two or more different forms of the same gene, located at the same locus on homologous chromosomes. Alleles may be dominant or recessive.",
        section: "11.1"
      },
      {
        term: "What is a genotype?",
        definition: "The complete genetic make-up of an organism — the specific alleles it carries at one or more gene loci, regardless of whether those alleles are expressed.",
        section: "11.1"
      },
      {
        term: "What is a phenotype?",
        definition: "The observable physical characteristics of an organism that result from the interaction of its genotype with the environment.",
        section: "11.1"
      },
      {
        term: "What is epigenetics?",
        definition: "The study of heritable changes in gene expression that do not involve changes to the DNA sequence itself. Epigenetic factors can switch genes on or off and may be influenced by environmental factors such as smoking.",
        section: "11.1"
      },
      {
        term: "What is the law of segregation (Mendel's first law)?",
        definition: "Mendel's principle that the two alleles controlling a characteristic separate from each other during gamete formation, so each gamete carries only one allele for each gene.",
        section: "11.1"
      },
      {
        term: "What is the law of independent assortment (Mendel's second law)?",
        definition: "Mendel's principle that when gametes are formed, either allele of one gene pair is equally likely to combine with either allele of a second gene pair, provided the genes are on different chromosomes.",
        section: "11.1"
      },
      {
        term: "What is sex linkage?",
        definition: "A pattern of inheritance in which a trait is controlled by a gene located on a sex chromosome (usually the X chromosome). Recessive sex-linked traits are more common in males because they have only one X chromosome.",
        section: "11.1"
      },
      {
        term: "What is incomplete dominance?",
        definition: "A pattern of inheritance in which neither allele is fully dominant over the other, so the heterozygote displays an intermediate phenotype that is a blend of both homozygous phenotypes.",
        section: "11.1"
      },
      {
        term: "What is gene linkage?",
        definition: "The tendency of two genes located on the same chromosome to be inherited together rather than assorting independently, which contradicts Mendel's second law and reduces genetic variation in gametes.",
        section: "11.1"
      },
      {
        term: "What is mitochondrial DNA (mtDNA)?",
        definition: "DNA found in mitochondria, outside the nucleus. It is inherited exclusively through the maternal line, as mitochondria are contributed to the zygote by the egg cell.",
        section: "11.1"
      }
    ];
  })();

  // ── bio12: Evolution: The Origins of Life ─────────────────────────────────
  (function () {
    var c = ch("bio12");
    // 12.1 — The mechanisms and evidence for evolution, including variation, mutation, natural selection and the importance of evolutionary theory
    c.learningOutcomes[0].notes = [
      {
        h: "What is variation and what are its types?",
        b: "Variation refers to differences between members of the same species, such as hair colour, skin colour and height in humans, or flower colour and leaf shape in plants. Acquired variations are not inherited — they are learned or developed during life (e.g. speaking a language). Inherited variations are genetically controlled (e.g. blood group, eye colour, ear shape)."
      },
      {
        h: "What are the main causes of inherited variation?",
        b: "The two main causes of inherited variation are sexual reproduction and mutations. Sexual reproduction generates diversity because meiosis produces non-identical haploid gametes through independent assortment and crossing over. Mutations are spontaneous changes in the amount or structure of DNA that can produce genetic disorders or, occasionally, beneficial new adaptations."
      },
      {
        h: "What are the different types of mutations?",
        b: "A gene (or point) mutation is a change within a single gene; examples include cystic fibrosis, haemophilia and albinism. A chromosomal mutation involves a large change in the structure or number of one or more chromosomes; examples include Down syndrome and changes in sex chromosomes."
      },
      {
        h: "What is artificial selection or selective breeding?",
        b: "Artificial selection is the human-directed process of choosing organisms with particular desirable traits to breed together, so that those traits are more prevalent in subsequent generations. Examples include breeding cattle for higher milk or meat yields, and selecting dogs for temperament or appearance."
      },
      {
        h: "What is natural selection?",
        b: "Natural selection is the process by which organisms whose genetically controlled characteristics make them well adapted to their environment survive and reproduce, passing those advantageous traits to future generations. A classic example is camouflaged animals, which tend to survive and reproduce more successfully than poorly camouflaged ones."
      },
      {
        h: "What is evolution?",
        b: "Evolution is the gradual genetic change in living things over long periods of time, leading to new forms of life. The theory of evolution by natural selection was independently proposed by naturalists Charles Darwin and Alfred Russel Wallace."
      },
      {
        h: "What is Darwin and Wallace's theory of evolution by natural selection?",
        b: "Darwin and Wallace's theory rests on three observations and two conclusions: organisms overproduce offspring; population sizes nonetheless remain roughly constant, implying a struggle for existence; and inherited variation exists within populations. The conclusions are that there is competition for scarce resources, and that better-adapted individuals are more likely to survive, reproduce, and pass on advantageous variations — natural selection."
      },
      {
        h: "Evidence for the theory of evolution",
        b: "Multiple independent lines of evidence support evolution: embryology shows that distantly related species have similar embryo stages, suggesting common ancestry; the fossil record documents how life has changed over geological time; phylogeny classifies organisms by evolutionary history to reveal species relationships; comparative anatomy shows that similar bone structures in different species indicate a common ancestor; antibiotic resistance demonstrates evolution in action, as bacteria mutate and become resistant to drugs; and speciation — the formation of new species through accumulation of genetic changes — has been observed."
      },
      {
        h: "The importance of the theory of evolution",
        b: "Evolutionary theory is foundational to biology for three reasons: it explains how distinct species arise from a common ancestor through inherited change (diversity); it explains why all living things share so many fundamental traits, having descended from a common ancestor (unity of life); and it has predictive power across medicine, agriculture, conservation, disease control, biotechnology and the study of human origins."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is variation?",
        definition: "Differences in characteristics between members of the same species. Variation may be inherited (genetically controlled) or acquired (developed during an individual's lifetime and not passed on).",
        section: "12.1"
      },
      {
        term: "What is a gene (point) mutation?",
        definition: "A change affecting a single gene in the DNA sequence. Examples include the mutations responsible for cystic fibrosis, haemophilia and albinism.",
        section: "12.1"
      },
      {
        term: "What is a chromosomal mutation?",
        definition: "A large-scale change in the structure or number of one or more chromosomes. Down syndrome (an extra chromosome 21) is a well-known example.",
        section: "12.1"
      },
      {
        term: "What are the steps of natural selection?",
        definition: "The process by which individuals with genetically controlled traits that make them better adapted to their environment survive and reproduce more successfully, passing those advantageous traits to offspring over generations.",
        section: "12.1"
      },
      {
        term: "What is artificial selection?",
        definition: "The human-directed form of selection in which individuals with desired traits are chosen to breed, so that those traits become more frequent in subsequent generations. Used in agriculture and animal breeding.",
        section: "12.1"
      },
      {
        term: "What is evolution?",
        definition: "The gradual genetic change in populations of living organisms over long periods of time, leading to the origin of new species. The theory of evolution by natural selection was independently proposed by Darwin and Wallace.",
        section: "12.1"
      },
      {
        term: "What are the steps of speciation?",
        definition: "The evolutionary process by which new species arise through the accumulation of genetic changes in isolated populations over time.",
        section: "12.1"
      },
      {
        term: "What is the fossil record?",
        definition: "The collection of fossilised remains and traces of past organisms preserved in rock. The fossil record provides direct evidence that life has changed over geological time, consistent with evolution.",
        section: "12.1"
      },
      {
        term: "What is comparative anatomy?",
        definition: "The study of structural similarities and differences in the body plans of different species. Similar bone structures (homologous structures) in distantly related species suggest descent from a common ancestor.",
        section: "12.1"
      }
    ];
  })();

  // ── bio13: Enzymes ────────────────────────────────────────────────────────
  (function () {
    var c = ch("bio13");
    // 13.1 — Enzyme structure, action, factors and industrial uses
    c.learningOutcomes[0].notes = [
      {
        h: "Enzyme Basics",
        b: "Globular proteins that act as biological catalysts: speed up reactions without being used up; lower activation energy. Each has a specific active site."
      },
      {
        h: "Substrate and Product",
        b: "Substrate: molecule the enzyme acts on. Product: molecule made. Enzyme specificity: only one substrate fits the active site (lock and key / induced fit)."
      },
      {
        h: "Induced Fit Model",
        b: "Active site changes shape slightly to fit the substrate snugly, like a hand in a glove."
      },
      {
        h: "Temperature Effect",
        b: "Activity rises with temperature up to the optimum (~37 C in humans) then falls sharply as the enzyme denatures (active site shape destroyed — irreversible)."
      },
      {
        h: "pH Effect",
        b: "Activity peaks at the optimum pH (pepsin pH 2, amylase pH 7). Extremes of pH denature the enzyme."
      },
      {
        h: "Denaturation",
        b: "Active site loses its specific shape; substrate can no longer bind. Usually irreversible. Caused by high temperature or extreme pH."
      },
      {
        h: "Immobilised Enzymes",
        b: "Enzyme attached to or trapped in an inert material (e.g. alginate beads). Advantages: reusable (lower cost), product not contaminated, more stable to temperature/pH."
      },
      {
        h: "Catalase Experiment",
        b: "Enzyme: catalase. Substrate: H2O2. Products: water + oxygen. Source: celery, potato or liver. Washing-up liquid traps O2 as foam; foam height measures activity."
      },
      {
        h: "Controlling Variables",
        b: "Change temperature with a water bath; control pH with buffer solutions. Only one variable changed at a time so any effect is attributed to that factor."
      },
      {
        h: "Industrial Enzyme Uses",
        b: "Amylase: bread/beer. Lactase: lactose-free milk. Pectinase: clear fruit juice. Rennin: cheese. Streptokinase: dissolves blood clots. Cellulase/amylase: bioethanol production."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is an enzyme?",
        definition: "A globular protein that acts as a biological catalyst: speeds up reactions without being used up; lowers activation energy; highly specific.",
        section: "13.1"
      },
      {
        term: "What is the active site?",
        definition: "The uniquely shaped region on an enzyme where the substrate binds. Its shape determines the enzyme's specificity.",
        section: "13.1"
      },
      {
        term: "What is an induced fit model?",
        definition: "The active site changes shape slightly to fit the substrate, like a hand fitting into a glove. More accurate than the original lock-and-key model.",
        section: "13.1"
      },
      {
        term: "What is a substrate?",
        definition: "The specific molecule an enzyme acts upon. Only the correct substrate fits the active site.",
        section: "13.1"
      },
      {
        term: "What is denaturation?",
        definition: "Permanent change to an enzyme's active site shape, caused by high temperature or extreme pH. The substrate can no longer bind — activity is lost irreversibly.",
        section: "13.1"
      },
      {
        term: "What is optimum temperature?",
        definition: "The temperature at which an enzyme works fastest (~37°C in humans). Above this, denaturation occurs; below it, activity slows.",
        section: "13.1"
      },
      {
        term: "What is optimum pH?",
        definition: "The pH at which an enzyme is most active. Pepsin: pH 2 (stomach); amylase: pH 7 (mouth). Extremes of pH denature the enzyme.",
        section: "13.1"
      },
      {
        term: "What are immobilised enzymes?",
        definition: "Enzymes attached to or trapped in an inert material (e.g. alginate beads). Advantages: reusable (lower cost); product not contaminated; more stable to temperature/pH.",
        section: "13.1"
      },
      {
        term: "What is catalase?",
        definition: "Enzyme that breaks down hydrogen peroxide (H2O2) into water and oxygen. Source: celery, potato or liver. Used in the catalase investigation.",
        section: "13.1"
      },
      {
        term: "What are the uses of industrial enzymes?",
        definition: "Amylase: bread/beer. Lactase: lactose-free milk. Pectinase: clear fruit juice. Rennin: cheese. Streptokinase: dissolves blood clots.",
        section: "13.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Explain what is meant by enzyme specificity.",
        model: "Each enzyme has an active site with a unique three-dimensional shape. Only the correct substrate molecule can fit into that active site (induced-fit model — the site adjusts slightly). This means each enzyme catalyses only one specific reaction."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Describe how temperature affects enzyme activity.",
        model: "As temperature increases, molecules move faster and collisions between enzyme and substrate are more frequent, so activity rises. At the optimum (~37 C for human enzymes), activity is greatest. Above this, high energy breaks the bonds maintaining the active site's shape — the enzyme denatures and activity falls sharply to zero."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Give three advantages of using immobilised enzymes in industry.",
        model: "1. The enzyme can be recovered and reused, lowering production costs. 2. The product is not contaminated with enzyme protein. 3. The immobilised enzyme is more stable to temperature and pH changes than free enzyme."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Describe the catalase experiment to investigate the effect of temperature on enzyme activity.",
        model: "Fill test tubes with equal volumes of hydrogen peroxide. Add a fixed amount of catalase source (e.g. equal discs of potato). Place tubes in water baths at different temperatures (e.g. 10, 20, 37, 60 C). Add washing-up liquid to trap O2 as foam. After a set time (e.g. 2 min) measure foam height. Keep the same pH (buffer), same amount of enzyme and substrate. Plot temperature vs foam height. Activity should peak at ~37 C and drop sharply above due to denaturation."
      }
    ];
    c.examQuestions = [
      {
        id: "bio13-eq-1",
        source: "LC Biology Past Paper — Q9",
        parts: [
          {
            label: "9. (a) (i)",
            question: "Briefly explain the term enzyme.",
            marks: 4,
            model: "An enzyme is a globular protein that acts as a biological catalyst — it speeds up chemical reactions in living organisms without being consumed. It does this by lowering the activation energy needed to start a reaction. Each enzyme has a uniquely shaped active site that binds only one specific substrate (induced fit model).",
            diagram: ""
          },
          {
            label: "9. (a) (ii)",
            question: "State one advantage of immobilising enzymes.",
            marks: 4,
            model: "The enzyme can be recovered and reused many times, significantly reducing the cost of industrial processes. (Alternatively: the product is not contaminated with enzyme protein, giving a purer product.)",
            diagram: ""
          },
          {
            label: "9. (b) (i)",
            question: "Name the enzyme or cell you immobilised.",
            marks: 3,
            model: "Lactase (enzyme) — used to convert lactose in milk to glucose and galactose, producing lactose-free milk. (Acceptable alternatives: catalase, yeast cells.)",
            diagram: ""
          },
          {
            label: "9. (b) (ii)",
            question: "Describe the procedure you used to immobilise the enzyme or cell. You may include a labelled diagram if you wish.",
            marks: 10,
            model: "1. Dissolve sodium alginate powder in warm distilled water to make a 2% solution. 2. Mix the enzyme (e.g. lactase) thoroughly into the sodium alginate solution. 3. Fill a syringe with the mixture. 4. Drop the mixture dropwise into a beaker of calcium chloride solution — each drop forms a bead immediately as alginate reacts with Ca2+ ions to form an insoluble gel. 5. Leave beads in the CaCl2 solution for a few minutes to harden. 6. Remove beads with a spatula and rinse with distilled water to remove excess calcium chloride. 7. Place beads in a small column or syringe for use.",
            diagram: ""
          },
          {
            label: "9. (b) (iii)",
            question: "Describe how you examined the application of the immobilised enzyme or cell.",
            marks: 6,
            model: "Pass a lactose solution (or milk) slowly through the column of immobilised lactase beads. Collect the liquid that drips out from the bottom. Test both the original lactose solution and the collected product using Benedict's solution: heat both samples with Benedict's reagent. The original lactose solution (a non-reducing sugar) gives no colour change. The collected product contains glucose and galactose (reducing sugars) and turns brick-red, confirming the lactase successfully hydrolysed the lactose.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio13-eq-2",
        source: "LC Biology Past Paper — Q10(b)",
        parts: [
          {
            label: "10. (b) (i)",
            question: "During your practical studies you investigated the action of digestive enzymes in germinating seeds using either starch agar or skimmed milk plates. Describe how you set up the apparatus for this investigation.",
            marks: 10,
            model: "Starch agar method: 1. Prepare starch agar plates by dissolving starch and agar in boiling water, pouring into petri dishes and allowing to set. 2. Germinate barley or wheat seeds on moist cotton wool for 2–3 days. 3. Crush the germinating seeds in a pestle and mortar with a little distilled water to extract the enzyme. 4. Use a cork borer to cut wells in the starch agar. 5. Pipette a measured volume of the seed extract into the wells. As a control, add distilled water to another well. 6. Incubate at room temperature or 25–30°C for 24–48 hours. 7. Flood the plate with iodine solution and observe for clear (unstained) zones. Skimmed milk plate method: Use the same setup but with skimmed milk agar. After incubation, observe for clear transparent zones (halos) around the wells where protein was digested.",
            diagram: ""
          },
          {
            label: "10. (b) (ii)",
            question: "Explain how you knew digestion had occurred.",
            marks: 6,
            model: "On starch agar: the plate was flooded with iodine solution. Iodine turns undigested starch blue-black. A clear (unstained) halo around the seed extract well showed that the enzyme (amylase) in the extract had digested the starch. No clear zone appeared around the control well. On skimmed milk plates: a clear transparent zone (halo) formed around the well containing seed extract, indicating that protease activity had broken down the milk protein (casein). The greater the zone of clearance, the greater the enzyme activity.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio13-eq-3",
        source: "LC Biology Past Paper — Q5 (Bioreactor)",
        parts: [
          {
            label: "5. (a)",
            question: "What is the common name given to this piece of equipment? (large vessel used in food processing with microorganisms/enzymes)",
            marks: 3,
            model: "Fermenter (or bioreactor). It is used in industrial biotechnology to grow microorganisms or use enzymes under controlled conditions to produce food products or medicines.",
            diagram: ""
          },
          {
            label: "5. (b)",
            question: "Name two factors controlled by the piece of equipment that could affect the growth of bacteria, other than nutrient availability.",
            marks: 4,
            model: "1. Temperature — maintained at the optimum for enzyme activity and microbial growth. 2. pH — kept at the optimum to prevent enzyme denaturation and maintain microbial health. (Other valid: oxygen/aeration level, stirring/mixing speed.)",
            diagram: ""
          },
          {
            label: "5. (c)",
            question: "Name the two stages X and Y on the population growth curve.",
            marks: 4,
            model: "X: Lag phase — microorganisms adapt to their new environment; cells synthesise enzymes and adjust their metabolism; little or no increase in population. Y: Log (exponential) phase — population doubles at a constant rapid rate; nutrients are plentiful and conditions are optimal.",
            diagram: ""
          },
          {
            label: "5. (d)",
            question: "The equipment is keeping the bacteria in steady growth phase Y. Which type of food processing technique is represented?",
            marks: 3,
            model: "Continuous culture (continuous fermentation) — fresh nutrient medium is continuously added and products/spent cells are continuously removed, maintaining bacteria in the exponential growth phase at a steady population.",
            diagram: ""
          },
          {
            label: "5. (e)",
            question: "If the bacteria in the equipment were to run out of nutrients, draw on the graph to show how the line would continue.",
            marks: 3,
            model: "After nutrient depletion, the curve enters the Stationary phase (levels off — death rate = birth rate) and then the Death/Decline phase (curves downward — death rate exceeds birth rate as toxins accumulate).",
            diagram: ""
          }
        ]
      },
      {
        id: "bio13-eq-4",
        source: "LC Biology Past Paper — Q10 (Yeast Investigation)",
        parts: [
          {
            label: "10. (a) (i)",
            question: "To which kingdom of living organisms do yeast belong?",
            marks: 2,
            model: "Fungi (kingdom Fungi). Yeast are unicellular fungi that reproduce by budding.",
            diagram: ""
          },
          {
            label: "10. (a) (ii)",
            question: "Working with microorganisms often involves sterility. Explain the term sterility.",
            marks: 4,
            model: "Sterility is the complete absence of ALL living microorganisms, including spores and non-pathogenic organisms. A sterile environment or piece of equipment contains no viable microorganisms, ensuring that only the intended organism grows in an investigation.",
            diagram: ""
          },
          {
            label: "10. (b) (i)",
            question: "Describe how you set up an investigation to grow leaf yeast. Include one safety precaution. You may include a labelled diagram.",
            marks: 8,
            model: "1. Prepare sterile nutrient agar plates (melt agar, pour into petri dishes in a sterile environment, allow to set). 2. Take a leaf and gently wash it in a small volume of sterile distilled water to dislodge surface microorganisms. 3. Using a sterile spreader or loop, spread the leaf-wash onto the agar plate surface. 4. Replace the lid, invert the plate and incubate at approximately 25 C for 48-72 hours. 5. Observe colonies that develop. Control: a plate of agar with sterile distilled water (no leaf-wash) spread on it. Safety precaution: Treat all incubated plates as potential biohazards; do not open plates after incubation; autoclave or disinfect plates before disposal.",
            diagram: ""
          },
          {
            label: "10. (b) (ii)",
            question: "Describe the result of the investigation, assuming the leaf yeast grew successfully.",
            marks: 4,
            model: "Colonies of yeast would be visible on the surface of the agar plate — small, round, cream-coloured raised colonies. Each colony grew from a single yeast cell or spore present on the leaf surface. The control plate (no leaf-wash) would show no colonies, confirming that colonies on the experimental plate came from the leaf and not from contamination.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio13-eq-5",
        source: "LC Biology Past Paper — Q10 (Asepsis and Sterility)",
        parts: [
          {
            label: "10. (a)",
            question: "Distinguish between the terms asepsis and sterility as applied to living organisms.",
            marks: 4,
            model: "Asepsis: the absence of pathogenic (disease-causing) microorganisms from a specific area, surface or material. It refers to maintaining conditions that prevent infection without necessarily eliminating ALL microorganisms (e.g. aseptic technique in a lab). Sterility: the complete absence of ALL living microorganisms including spores and non-pathogens. Sterility is a more absolute state than asepsis — sterilisation kills every living organism present.",
            diagram: ""
          },
          {
            label: "10. (b) (i) 1.",
            question: "Name a nutrient added to the agar to enable growth of leaf yeast.",
            marks: 2,
            model: "Glucose (as a carbon and energy source). Other valid nutrients: peptone or yeast extract (nitrogen source/amino acids), potassium phosphate (minerals).",
            diagram: ""
          },
          {
            label: "10. (b) (i) 2.",
            question: "Describe the control you used in the investigation of leaf yeast growth.",
            marks: 3,
            model: "A sterile agar plate to which sterile distilled water (not the leaf-wash) was added and spread. It was incubated under identical conditions (same temperature, same time period). If the control showed no colonies, this confirmed that any colonies on the experimental plate came from the leaf surface microorganisms and not from airborne contamination or contaminated agar.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio14: Photosynthesis ─────────────────────────────────────────────────
  (function () {
    var c = ch("bio14");
    // 14.1 — Photosynthesis: stages, factors and leaf adaptations
    c.learningOutcomes[0].notes = [
      {
        h: "Overview",
        b: "Anabolic process: plants use light energy to make glucose from CO2 and water. Equation: 6CO2 + 6H2O -> C6H12O6 + 6O2. Chlorophyll captures light."
      },
      {
        h: "Carbon Sink",
        b: "Plants remove CO2 from the atmosphere and lock the carbon into biomass (glucose, starch, cellulose). Vital in regulating atmospheric CO2."
      },
      {
        h: "Raw Material Sources",
        b: "CO2: through stomata from air. Water: root hairs absorb from soil, transported up xylem. Sunlight: captured by chlorophyll."
      },
      {
        h: "What happens in the light-dependent stage of photosynthesis?",
        b: "In thylakoid membranes. Light splits water (photolysis): 2H2O -> 4H+ + 4e- + O2. ATP and NADPH produced. O2 is the waste product released."
      },
      {
        h: "What happens in the light-independent (dark) stage of photosynthesis?",
        b: "In stroma (Calvin cycle). CO2 fixed and reduced using ATP and NADPH to form glucose. Enzyme-controlled, so temperature affects this stage strongly."
      },
      {
        h: "What are the adaptations of chloroplasts?",
        b: "Thylakoids stacked into grana (large SA for chlorophyll). Stroma contains Calvin cycle enzymes. Double membrane."
      },
      {
        h: "What are the adaptations of leaves for photosynthesis?",
        b: "Large flat shape (maximise light). Thin (short diffusion path). Stomata (gas exchange). Chloroplasts in palisade mesophyll (max light absorption). Vascular tissue (transport)."
      },
      {
        h: "What factors affect the rate of photosynthesis?",
        b: "Light intensity, CO2 concentration, temperature. Each can be the limiting factor if too low. Graphs show a rising curve levelling off when another factor becomes limiting."
      },
      {
        h: "Investigating Rate (Elodea)",
        b: "Submerged pondweed; count O2 bubbles per minute. IV = light distance/temperature/CO2 (NaHCO3 conc). DV = bubble rate. Controls = all other factors."
      },
      {
        h: "Glucose Uses",
        b: "Respiration (energy), starch (storage), cellulose (cell walls), proteins, lipids, nucleic acids."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What are the steps of photosynthesis?",
        definition: "Anabolic process: 6CO2 + 6H2O → C6H12O6 + 6O2. Light energy captured by chlorophyll drives the synthesis of glucose from CO2 and water.",
        section: "14.1"
      },
      {
        term: "What is a carbon sink?",
        definition: "A system that removes CO2 from the atmosphere and stores the carbon in biomass (glucose, starch, cellulose). Plants are major carbon sinks.",
        section: "14.1"
      },
      {
        term: "What is the light-dependent stage?",
        definition: "Occurs in thylakoid membranes. Light splits water (photolysis): 2H2O → 4H⁺ + 4e⁻ + O2. Produces ATP and NADPH. O2 is the waste product.",
        section: "14.1"
      },
      {
        term: "What is the light-independent (dark) stage?",
        definition: "Occurs in the stroma (Calvin cycle). CO2 is fixed and reduced using ATP and NADPH to form glucose. Temperature is a key limiting factor here.",
        section: "14.1"
      },
      {
        term: "What is photolysis?",
        definition: "The splitting of water molecules using light energy in the thylakoid. Releases O2, electrons and H⁺ ions used in ATP and NADPH production.",
        section: "14.1"
      },
      {
        term: "What is chlorophyll?",
        definition: "The green pigment in thylakoid membranes that absorbs light energy (mainly red and blue wavelengths) to drive photosynthesis.",
        section: "14.1"
      },
      {
        term: "What is a limiting factor (in photosynthesis)?",
        definition: "Light intensity, CO2 concentration or temperature — whichever is too low limits the overall rate of photosynthesis.",
        section: "14.1"
      },
      {
        term: "What are leaf adaptations?",
        definition: "Large flat shape (maximise light); thin (short diffusion path); stomata (gas exchange); palisade mesophyll (maximum light absorption); vascular tissue (transport).",
        section: "14.1"
      },
      {
        term: "What is the Elodea investigation?",
        definition: "Submerged pondweed used to measure photosynthesis rate by counting O2 bubbles per minute. IV = light distance/temperature/CO2 (NaHCO3). DV = bubble rate.",
        section: "14.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Write the balanced chemical equation for photosynthesis and state where each reactant comes from.",
        model: "6CO2 + 6H2O -> C6H12O6 + 6O2. CO2 enters through stomata from the air. Water is absorbed by root hairs from the soil and transported up the xylem to leaves. Light energy (from sunlight) drives the reaction via chlorophyll."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Distinguish between the light-dependent and light-independent stages of photosynthesis.",
        model: "The light-dependent stage occurs in thylakoid membranes; light splits water (photolysis) releasing O2, and produces ATP and NADPH. The light-independent (dark/Calvin cycle) stage occurs in the stroma; ATP and NADPH are used to fix CO2 into glucose via enzyme-controlled reactions."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Describe an experiment to investigate the effect of light intensity on photosynthesis.",
        model: "Place Elodea in a beaker of water with NaHCO3 (CO2 source). Position a lamp at set distances (e.g. 5, 10, 20, 40 cm) and count O2 bubbles per minute at each distance. Keep temperature and CO2 level constant. As light intensity increases, bubble rate increases until another factor (CO2 or temperature) becomes limiting and the graph levels off."
      },
      {
        type: "short",
        marks: 3,
        prompt: "Explain what is meant by a carbon sink and why plants are important in this role.",
        model: "A carbon sink removes CO2 from the atmosphere and stores the carbon. Plants fix atmospheric CO2 into glucose during photosynthesis, then store it in biomass as starch, cellulose and other organic molecules. This reduces atmospheric CO2 levels, helping to regulate the greenhouse effect."
      }
    ];
    c.examQuestions = [
      {
        id: "bio14-eq-1",
        source: "LC Biology Past Paper — Q7 (Photosynthesis)",
        parts: [
          {
            label: "7. (a) (i)",
            question: "The graph shows absorption spectra for chlorophyll a and chlorophyll b. Which colour of light is absorbed most by chlorophyll a?",
            marks: 2,
            model: "Chlorophyll a has peak absorption in the blue-violet region (~430 nm) and the red region (~680 nm). The strongest peak is in the red region. Answer: Red light (with a secondary peak in blue-violet).",
            diagram: "images/photosynthesis-spectrum.png"
          },
          {
            label: "7. (a) (ii)",
            question: "Which colour of light is absorbed most by chlorophyll b?",
            marks: 2,
            model: "Chlorophyll b absorbs most strongly in the blue region (~460 nm) and in the orange-red region (~640 nm). Answer: Blue light (strongest absorption).",
            diagram: "images/photosynthesis-spectrum.png"
          },
          {
            label: "7. (a) (iii)",
            question: "What happens to green and yellow light when they strike chlorophyll?",
            marks: 2,
            model: "Green and yellow light are mostly reflected (not absorbed) by chlorophyll molecules — this is why plants appear green to our eyes. These wavelengths contribute very little to photosynthesis.",
            diagram: "images/photosynthesis-spectrum.png"
          },
          {
            label: "7. (b)",
            question: "The function of chlorophyll is to absorb sunlight and use this energy to energise electrons. Give two fates of these energised electrons in photosynthesis.",
            marks: 6,
            model: "1. Energised electrons are passed along the electron transport chain in the thylakoid membrane, releasing energy that drives ATP synthase to produce ATP from ADP + Pi (photophosphorylation). 2. Energised electrons reduce NADP+ to NADPH by combining with a proton (H+). NADPH acts as a reducing agent in the Calvin cycle, providing hydrogen to reduce CO2 to glucose.",
            diagram: ""
          },
          {
            label: "7. (c)",
            question: "Name another molecule which can provide electrons during photosynthesis.",
            marks: 2,
            model: "Water (H2O). During the light-dependent stage, water is split by photolysis: 2H2O -> 4H+ + 4e- + O2. The electrons released replace those lost by chlorophyll, and oxygen is released as a by-product.",
            diagram: ""
          },
          {
            label: "7. (d)",
            question: "Identify a source of the molecule you named in part (c) for photosynthesis in a plant.",
            marks: 2,
            model: "Water is absorbed from the soil by root hair cells and transported upward to the leaves through the xylem vessels of the vascular bundles.",
            diagram: ""
          },
          {
            label: "7. (e)",
            question: "Suggest one reason why horticulturists might use carbon dioxide enrichment in a greenhouse.",
            marks: 3,
            model: "CO2 is a raw material for the Calvin (light-independent) stage of photosynthesis. Enriching the greenhouse atmosphere with CO2 removes CO2 as a limiting factor, allowing plants to fix more carbon and produce more glucose per unit time, leading to faster growth and higher crop yields.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio15: Respiration ────────────────────────────────────────────────────
  (function () {
    var c = ch("bio15");
    // 15.1 — Aerobic and anaerobic respiration, fermentation
    c.learningOutcomes[0].notes = [
      {
        h: "ATP",
        b: "Adenosine Triphosphate: the cell's energy currency. ATP -> ADP + Pi releases energy used by cells for movement, synthesis, transport and growth."
      },
      {
        h: "Aerobic Respiration Overview",
        b: "Catabolic: glucose + oxygen -> CO2 + water + ~38 ATP. Carbon from glucose is released as CO2; protons end up in water."
      },
      {
        h: "Glycolysis",
        b: "Stage 1. In cytoplasm, no oxygen needed. Glucose (6C) -> 2 pyruvic acid (3C) + 2 ATP + 2 NADH."
      },
      {
        h: "Citric Acid (Krebs) Cycle",
        b: "Stage 2. In mitochondrial matrix. Pyruvic acid -> acetyl CoA -> enters cycle with oxaloacetate -> releases CO2, NADH, FADH2, small ATP."
      },
      {
        h: "Electron Transport Chain (ETC)",
        b: "Stage 3. On inner mitochondrial membrane (cristae). NADH/FADH2 drive ATP synthase via H+ flow -> ~34 ATP. Final electron acceptor: O2 -> water formed."
      },
      {
        h: "NAD+ and ATP Synthase",
        b: "NAD+: coenzyme carrying H+ and electrons (as NADH) to the ETC. ATP synthase: enzyme on cristae that builds ATP as H+ flows through it."
      },
      {
        h: "Anaerobic: Lactic Acid",
        b: "Animal muscle/some bacteria. Glucose -> 2 lactic acid + 2 ATP. Lactic acid removed by liver (converted back to glucose or oxidised). Causes oxygen debt."
      },
      {
        h: "Anaerobic: Alcohol Fermentation",
        b: "Yeast/plants. Glucose -> 2 ethanol + 2 CO2 + 2 ATP. CO2 carbon comes from glucose. Used in bread-making and brewing."
      },
      {
        h: "Fermentation Experiment",
        b: "Anaerobic: seal with oil or fermentation lock. Yeast provides zymase enzymes. Fermentation lock + limewater traps CO2 (turns cloudy). Optimum temp ~30-35 C."
      },
      {
        h: "Ethanol Detection",
        b: "Add acidified potassium dichromate: orange -> green confirms ethanol present."
      },
      {
        h: "ATP Yield Comparison",
        b: "Aerobic: ~38 ATP per glucose. Anaerobic: ~2 ATP per glucose (only glycolysis)."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is ATP (adenosine triphosphate)?",
        definition: "The cell's energy currency. ATP → ADP + Pi releases energy used for movement, synthesis, active transport and growth.",
        section: "15.1"
      },
      {
        term: "What is glycolysis?",
        definition: "Stage 1 of aerobic respiration. In the cytoplasm (no O2 needed). Glucose (6C) → 2 pyruvic acid (3C) + 2 ATP + 2 NADH.",
        section: "15.1"
      },
      {
        term: "What is the Krebs (citric acid) cycle?",
        definition: "Stage 2. In the mitochondrial matrix. Pyruvic acid → acetyl CoA → enters cycle, releasing CO2, NADH, FADH2 and small amounts of ATP.",
        section: "15.1"
      },
      {
        term: "What is the electron transport chain (ETC)?",
        definition: "Stage 3. On inner mitochondrial membrane (cristae). NADH/FADH2 drive ATP synthase via H⁺ flow → ~34 ATP. Final electron acceptor: O2 → water.",
        section: "15.1"
      },
      {
        term: "What is NAD+?",
        definition: "A coenzyme that picks up H⁺ and electrons in glycolysis and the Krebs cycle to become NADH. NADH carries them to the ETC to drive ATP synthesis.",
        section: "15.1"
      },
      {
        term: "What is lactic acid fermentation?",
        definition: "Anaerobic respiration in animal muscle and some bacteria. Glucose → 2 lactic acid + 2 ATP. Lactic acid builds up causing muscle fatigue.",
        section: "15.1"
      },
      {
        term: "What is alcohol fermentation?",
        definition: "Anaerobic respiration in yeast and plants. Glucose → 2 ethanol + 2 CO2 + 2 ATP. Used in bread-making and brewing.",
        section: "15.1"
      },
      {
        term: "What is oxygen debt?",
        definition: "Extra O2 consumed after intense exercise to convert accumulated lactic acid back to glucose or oxidise it to CO2 and water in the liver.",
        section: "15.1"
      },
      {
        term: "How does ATP yield compare between aerobic and anaerobic respiration?",
        definition: "Aerobic respiration: ~38 ATP per glucose. Anaerobic respiration: ~2 ATP per glucose (glycolysis only).",
        section: "15.1"
      },
      {
        term: "How is ethanol detected?",
        definition: "Acidified potassium dichromate: orange → green confirms ethanol present. Used to confirm alcohol production in yeast fermentation experiments.",
        section: "15.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Name the three stages of aerobic respiration, state where each occurs and give the main products.",
        model: "1. Glycolysis: cytoplasm -> 2 pyruvic acid + 2 ATP + 2 NADH. 2. Krebs cycle: mitochondrial matrix -> CO2 + NADH + FADH2 + small ATP. 3. Electron transport chain: inner mitochondrial membrane -> ~34 ATP + water."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain how lactic acid is produced and removed during intense exercise.",
        model: "During intense exercise O2 supply to muscles is insufficient for aerobic respiration; anaerobic respiration in the cytoplasm converts glucose to lactic acid, producing only 2 ATP. Lactic acid builds up causing fatigue. After exercise, extra O2 is consumed (oxygen debt) to allow the liver to convert lactic acid back to glucose or oxidise it to CO2 and water."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Describe an experiment to demonstrate anaerobic respiration in yeast.",
        model: "Set up a flask with a glucose-yeast solution and seal with a fermentation lock containing limewater. Boil a second flask of yeast first (kills it) as a control — run the same setup with dead yeast. Leave for 20-30 min at ~30 C. In the live yeast flask, CO2 bubbles through and turns the limewater cloudy. No cloudiness in the control. Test the liquid with acidified potassium dichromate: orange -> green confirms ethanol was produced. Keep temperature constant between flasks."
      },
      {
        type: "short",
        marks: 3,
        prompt: "What is the role of NAD+ in aerobic respiration?",
        model: "NAD+ is a coenzyme that picks up hydrogen ions (H+) and electrons from glycolysis and the Krebs cycle to become NADH. NADH then carries these to the electron transport chain where the energy released as electrons pass down the chain powers ATP synthase to make ATP. NAD+ is regenerated and recycled."
      }
    ];
    c.examQuestions = [
      {
        id: "bio15-eq-1",
        source: "LC Biology Past Paper — Q3 (Aerobic Respiration)",
        parts: [
          {
            label: "3. (a)",
            question: "Aerobic respiration is a two-stage process. Stage 2 occurs in the cell organelle shown (diagram of mitochondrion). Name the cell organelle shown.",
            marks: 2,
            model: "Mitochondrion (plural: mitochondria). It is the site of stages 2 and 3 of aerobic respiration — the Krebs cycle (matrix) and the electron transport chain (inner membrane/cristae).",
            diagram: "images/mitochondrion.png"
          },
          {
            label: "3. (b)",
            question: "Name the cycle of reactions that occurs in stage 2 of aerobic respiration.",
            marks: 2,
            model: "The Citric Acid Cycle (Krebs Cycle). Occurs in the mitochondrial matrix; pyruvic acid is converted to acetyl CoA, which enters the cycle and is oxidised, releasing CO2 and producing NADH and FADH2.",
            diagram: ""
          },
          {
            label: "3. (c)",
            question: "ATP is produced in large quantities by aerobic respiration. What does ATP stand for?",
            marks: 2,
            model: "ATP stands for Adenosine Triphosphate — the cell's main energy currency. Energy is released when the terminal phosphate bond is broken: ATP -> ADP + Pi + energy.",
            diagram: ""
          },
          {
            label: "3. (d)",
            question: "NAD+ is an important molecule in respiration. Give the function of NAD+.",
            marks: 3,
            model: "NAD+ (nicotinamide adenine dinucleotide) is a coenzyme that acts as an electron and hydrogen carrier. During glycolysis and the Krebs cycle, NAD+ accepts hydrogen (H+ + electrons) to become NADH. NADH then transports these to the electron transport chain on the inner mitochondrial membrane, where their energy drives ATP synthase to produce large amounts of ATP, and NAD+ is regenerated.",
            diagram: ""
          },
          {
            label: "3. (e)",
            question: "Suggest a condition under which anaerobic respiration might occur.",
            marks: 2,
            model: "During intense physical exercise, when the rate of O2 delivery to muscle cells cannot keep pace with the demand for ATP — the cells switch to anaerobic respiration. Alternatively: in a sealed or low-oxygen environment such as a fermentation vessel (e.g. yeast producing ethanol).",
            diagram: ""
          },
          {
            label: "3. (f)",
            question: "State where anaerobic respiration occurs in a cell.",
            marks: 2,
            model: "In the cytoplasm (cytosol). Anaerobic respiration (glycolysis and fermentation) does not require mitochondria and takes place entirely in the cytoplasm.",
            diagram: ""
          },
          {
            label: "3. (g)",
            question: "Name one main product of anaerobic respiration.",
            marks: 2,
            model: "In animal cells/bacteria: Lactic acid (lactate). In yeast/plant cells: Ethanol and carbon dioxide. (Both pathways also produce 2 ATP per glucose molecule.)",
            diagram: ""
          }
        ]
      },
      {
        id: "bio15-eq-2",
        source: "LC Biology Past Paper — Q9 (Anaerobic Respiration & Yeast Fermentation)",
        parts: [
          {
            label: "9. (a) (i)",
            question: "What is meant by the term anaerobic?",
            marks: 3,
            model: "Anaerobic means without oxygen. Anaerobic respiration is a form of cellular respiration that takes place in the absence of oxygen. It occurs in the cytoplasm and produces only 2 ATP per glucose molecule (compared to approximately 38 ATP by aerobic respiration).",
            diagram: ""
          },
          {
            label: "9. (a) (ii)",
            question: "What other substance is produced in animal cells as a result of anaerobic respiration?",
            marks: 2,
            model: "Lactic acid (lactate). Glucose -> 2 lactic acid + 2 ATP. Lactic acid accumulates in muscles during intense exercise, contributing to fatigue and muscle soreness.",
            diagram: ""
          },
          {
            label: "9. (b) (i)",
            question: "Draw a labelled diagram showing how you set up the apparatus to prepare alcohol using yeast.",
            marks: 6,
            model: "Diagram should show: (1) Conical flask containing glucose solution and yeast. (2) A one-hole bung with a glass delivery tube leading from the flask. (3) The delivery tube leading into limewater (to detect CO2). (4) A fermentation lock or layer of oil sealing the flask to exclude air. Incubate at 30-35 C. Labels: flask, glucose + yeast solution, delivery tube/fermentation lock, limewater/CO2 detector.",
            diagram: ""
          },
          {
            label: "9. (b) (ii)",
            question: "Explain the importance of keeping the yeast cells at an optimum temperature.",
            marks: 3,
            model: "Yeast fermentation enzymes (e.g. zymase) have an optimum temperature of approximately 30-35 C. At this temperature, enzyme activity and fermentation rate are maximised. Below the optimum, enzyme activity slows due to reduced molecular kinetic energy. Above the optimum, enzymes are denatured — their active site shape is permanently altered — and fermentation stops.",
            diagram: ""
          },
          {
            label: "9. (b) (iii)",
            question: "Alcohol production eventually stops. Explain why this happens.",
            marks: 3,
            model: "Ethanol accumulates to a toxic concentration (typically around 12-15% by volume) that inhibits and kills the yeast cells. Their enzymes are denatured by the high alcohol concentration. Nutrient (glucose) depletion may also contribute to stopping fermentation.",
            diagram: ""
          },
          {
            label: "9. (b) (iv)",
            question: "How did you know when the reaction had stopped?",
            marks: 2,
            model: "When the limewater in the delivery tube stopped turning milky/cloudy, indicating that CO2 was no longer being produced. CO2 is a by-product of yeast fermentation; its absence signals the reaction has ceased.",
            diagram: ""
          },
          {
            label: "9. (b) (v)",
            question: "Name a test for alcohol and give the final colour observed if alcohol was present.",
            marks: 4,
            model: "Test: Acidified potassium dichromate. Add a few drops to a sample of the fermented liquid. Final colour if alcohol present: Green. The solution starts orange and turns green in the presence of ethanol.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio16: Cell Division and Cancer ───────────────────────────────────────
  (function () {
    var c = ch("bio16");
    // 16.1 — Cell cycle, mitosis, meiosis and cancer
    c.learningOutcomes[0].notes = [
      {
        h: "Cell Cycle Phases",
        b: "Interphase (G1, S, G2 — growth + DNA replication), Mitosis (nuclear division), Cytokinesis (cytoplasm divides). Biomolecules formed in interphase: DNA and proteins."
      },
      {
        h: "DNA Replication",
        b: "In S phase. Helix unwinds; DNA polymerase reads each strand and adds complementary nucleotides -> two identical DNA molecules. Essential so each daughter cell gets a full genome."
      },
      {
        h: "Haploid and Diploid",
        b: "Haploid (n = 23): one set of chromosomes; gametes. Diploid (2n = 46): two sets; body cells. Fusion of two haploid gametes at fertilisation restores diploid number."
      },
      {
        h: "Mitosis",
        b: "Produces two genetically identical diploid daughter cells. Role: growth, repair, asexual reproduction. Stages: prophase, metaphase, anaphase, telophase."
      },
      {
        h: "Cytokinesis",
        b: "Animal cells: cleavage furrow pinches inward. Plant cells: cell plate forms between daughters, becoming the new cell wall."
      },
      {
        h: "Meiosis",
        b: "Produces four genetically varied haploid daughter cells (gametes). Two divisions; halves chromosome number; variation from crossing over and independent assortment."
      },
      {
        h: "Mitosis vs Meiosis",
        b: "Mitosis: 1 division -> 2 diploid identical cells (growth/repair). Meiosis: 2 divisions -> 4 haploid varied cells (gametes)."
      },
      {
        h: "Cancer",
        b: "Uncontrolled cell division forming a tumour. Benign: contained, non-spreading. Malignant: invades tissues, metastasis (spreads via blood/lymph), can be fatal."
      },
      {
        h: "Cancer Causes",
        b: "Genetic (inherited mutations, e.g. BRCA1/2), environmental carcinogens (UV, smoking, asbestos), infectious (HPV -> cervical cancer; HepB/C -> liver cancer)."
      },
      {
        h: "Cancer Treatments",
        b: "Surgery (remove tumour), chemotherapy (kill fast-dividing cells), radiation therapy (damage tumour DNA), immunotherapy (stimulate immune system), vaccination (HPV, HepB)."
      },
      {
        h: "Risk Factors",
        b: "Not controllable: age, family history, genetics, gender. Controllable: smoking, alcohol, diet, obesity, sun exposure, exercise, HPV vaccination."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the cell cycle?",
        definition: "Interphase (G1, S, G2: growth and DNA replication) → Mitosis (nuclear division) → Cytokinesis (cytoplasm division).",
        section: "16.1"
      },
      {
        term: "What is DNA replication?",
        definition: "Occurs in S phase of interphase. Helix unwinds; DNA polymerase adds complementary nucleotides → two identical DNA double helices.",
        section: "16.1"
      },
      {
        term: "What is haploid (n)?",
        definition: "A cell with one set of chromosomes. In humans: n = 23 chromosomes. Gametes (sperm and eggs) are haploid. Produced by meiosis.",
        section: "16.1"
      },
      {
        term: "What is diploid (2n)?",
        definition: "A cell with two sets of chromosomes. In humans: 2n = 46 chromosomes. All body (somatic) cells are diploid. Produced by mitosis.",
        section: "16.1"
      },
      {
        term: "What is the role of mitosis?",
        definition: "Cell division producing two genetically identical diploid daughter cells. Stages: prophase, metaphase, anaphase, telophase. Role: growth, repair, asexual reproduction.",
        section: "16.1"
      },
      {
        term: "What is meiosis?",
        definition: "Cell division producing four genetically varied haploid daughter cells (gametes). Two divisions; variation through crossing over and independent assortment.",
        section: "16.1"
      },
      {
        term: "What is cytokinesis?",
        definition: "Division of the cytoplasm after mitosis. Animal cells: cleavage furrow. Plant cells: cell plate forms between daughter cells.",
        section: "16.1"
      },
      {
        term: "What is a benign tumour?",
        definition: "A contained mass of cells that does not invade surrounding tissue or spread to other parts of the body.",
        section: "16.1"
      },
      {
        term: "What is a malignant tumour?",
        definition: "A tumour that invades nearby tissues and can metastasise — cancer cells spread via blood or lymph to form secondary tumours. Can be fatal.",
        section: "16.1"
      },
      {
        term: "What are cancer risk factors?",
        definition: "Controllable: smoking, UV exposure, alcohol, obesity. Uncontrollable: age, inherited genetic mutations (e.g. BRCA1), family history.",
        section: "16.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Describe the key events of mitosis.",
        model: "Prophase: chromosomes condense, spindle forms. Metaphase: chromosomes align at the cell equator attached to spindle fibres. Anaphase: sister chromatids are pulled to opposite poles. Telophase: new nuclear envelopes form around each set of chromosomes. Cytokinesis then divides the cytoplasm to give two identical diploid daughter cells."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Compare mitosis and meiosis.",
        model: "Mitosis: one division produces two genetically identical diploid (2n = 46) daughter cells used for growth and repair. Meiosis: two divisions produce four genetically different haploid (n = 23) daughter cells (gametes). Meiosis introduces variation through crossing over (prophase I) and independent assortment."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Distinguish between benign and malignant tumours.",
        model: "A benign tumour is a contained mass of cells that does not invade surrounding tissue or spread to other parts of the body; it is often non-fatal. A malignant tumour invades nearby tissues and can metastasise — cancer cells break away and travel via blood or lymph to form secondary tumours elsewhere; it can be fatal."
      },
      {
        type: "short",
        marks: 4,
        prompt: "List two controllable and two uncontrollable risk factors for cancer.",
        model: "Controllable: smoking (causes lung/throat cancer), excess UV exposure (skin cancer). Uncontrollable: age (most cancers are more common with age), inherited genetic mutations (e.g. BRCA1 mutation raises breast cancer risk). Controllable risks can be reduced by lifestyle changes; uncontrollable ones can only be monitored."
      }
    ];
    c.examQuestions = [
      {
        id: "bio16-eq-1",
        source: "LC Biology Past Paper — Q6(d)",
        parts: [
          {
            label: "6. (d)",
            question: "Distinguish between the terms haploid and diploid.",
            marks: 6,
            model: "Haploid (n): a cell or organism that contains a single set of chromosomes — 23 chromosomes in humans. Haploid cells are the gametes (sperm and egg cells) and are produced by meiosis. Diploid (2n): a cell or organism that contains two complete sets of chromosomes — 46 chromosomes in humans. Diploid cells are all body (somatic) cells and are produced by mitosis. At fertilisation, two haploid gametes fuse to restore the diploid number in the zygote.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio16-eq-2",
        source: "LC Biology Past Paper — Q6 (f)",
        parts: [
          {
            label: "6. (f)",
            question: "Give a brief biological explanation: Meiosis halves the number of chromosomes in cells.",
            marks: 4,
            model: "Meiosis is a specialised type of cell division that produces gametes (sex cells — sperm and eggs). Starting from a diploid parent cell (2n = 46 chromosomes in humans), two successive divisions (meiosis I separates homologous chromosomes; meiosis II separates sister chromatids) produce four haploid daughter cells, each with n = 23 chromosomes. Halving the chromosome number is essential so that when two gametes fuse at fertilisation, the normal diploid chromosome number (2n = 46) is restored in the zygote.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio17: DNA Replication, Protein Synthesis and Mutations ───────────────
  (function () {
    var c = ch("bio17");
    // 17.1 — How DNA is copied and used to build proteins, and how mutations arise
    c.learningOutcomes[0].notes = [
      {
        h: "DNA Replication",
        b: "DNA replication is the process of producing two identical copies of DNA from one original molecule, and it occurs during interphase of the cell cycle. The double helix first unwinds and the two strands separate, exposing the bases. Incoming complementary bases then attach (A to T, G to C), catalysed by DNA polymerase, and each new double strand rewinds to form a complete helix — yielding two identical DNA molecules."
      },
      {
        h: "Protein Synthesis Overview",
        b: "In protein synthesis, information flows from DNA through mRNA to protein, following the central dogma of molecular biology. Synthesis itself occurs on ribosomes. The sequence of bases on DNA acts as a code, read in groups of three called triplets or codons, with each gene containing one start codon, multiple amino-acid-coding codons, and one stop codon."
      },
      {
        h: "Transcription",
        b: "Transcription is the conversion of a DNA base sequence into a complementary strand of messenger RNA (mRNA). Enzymes unwind the DNA double helix in the nucleus, RNA polymerase joins complementary RNA nucleotides to the exposed DNA template strand, and the resulting mRNA strand detaches and exits through a nuclear pore into the cytoplasm. The original two DNA strands are left unchanged and rejoin."
      },
      {
        h: "Translation",
        b: "Translation is the conversion of the mRNA base sequence into a protein, and it takes place in the ribosome. As mRNA threads through the ribosome, tRNA molecules carrying specific amino acids enter; each tRNA anticodon pairs with the complementary mRNA codon, the amino acid is detached and bonded to the growing chain, and the tRNA leaves. This continues until a stop codon is reached, at which point the completed protein folds into its functional shape."
      },
      {
        h: "Roles of the Three Types of RNA",
        b: "mRNA (messenger RNA) forms a complementary copy of the DNA template and carries the protein-building instructions from the nucleus to the ribosome. tRNA (transfer RNA) carries specific amino acids to the ribosome, matching each anticodon to the corresponding mRNA codon. rRNA (ribosomal RNA) forms part of the physical structure of the ribosome itself."
      },
      {
        h: "Mutations",
        b: "A mutation is a sudden change in the amount or structure of DNA. Spontaneous mutations arise when DNA fails to copy or repair itself accurately; if the gene sequence is wrong, the resulting amino acid chain will not form the correct protein. Mutagens are agents that cause mutations — examples include UV radiation, tobacco smoke and certain viruses — and a mutagen that specifically causes cancer is called a carcinogen."
      },
      {
        h: "Point (Gene) Mutations",
        b: "A point mutation is a change affecting one or a small number of bases within a single gene, typically arising from incorrect base pairing during DNA replication. Because only part of the code is altered, the effect can range from mild to severe depending on which amino acid is changed. Well-known examples of diseases caused by point mutations include cystic fibrosis, haemophilia and albinism."
      },
      {
        h: "Chromosomal Mutations",
        b: "Chromosomal mutations are larger-scale changes that affect the structure or number of entire chromosomes. Types include deletion (a fragment is lost), duplication (a fragment reattaches to the same chromosome), inversion (a fragment reattaches upside down) and translocation (a fragment reattaches to a non-homologous chromosome). Examples include Down syndrome (an extra chromosome 21, giving 47 total) and sex-chromosome variations such as XXX females or XYY males."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What are the steps of DNA replication?",
        definition: "The process by which a DNA molecule is copied to produce two identical double-stranded DNA molecules, occurring during interphase and catalysed by DNA polymerase.",
        section: "17.1"
      },
      {
        term: "What is DNA polymerase?",
        definition: "The enzyme that catalyses the joining of complementary incoming nucleotides to the exposed template strands during DNA replication.",
        section: "17.1"
      },
      {
        term: "What is transcription?",
        definition: "The synthesis of a complementary mRNA strand from a DNA template in the nucleus, carried out by RNA polymerase.",
        section: "17.1"
      },
      {
        term: "What are the steps of translation?",
        definition: "The ribosomal process that reads the mRNA base sequence (in codons) and assembles the corresponding chain of amino acids to form a protein.",
        section: "17.1"
      },
      {
        term: "What is a codon?",
        definition: "A sequence of three bases on mRNA that codes for a specific amino acid (or signals start/stop of translation).",
        section: "17.1"
      },
      {
        term: "What is an anticodon?",
        definition: "A complementary triplet of bases on tRNA that pairs with a specific mRNA codon during translation, ensuring the correct amino acid is added.",
        section: "17.1"
      },
      {
        term: "What is a mutagen?",
        definition: "Any agent that increases the rate of mutation in DNA, such as UV radiation, tobacco smoke or certain viruses.",
        section: "17.1"
      },
      {
        term: "What is a carcinogen?",
        definition: "A mutagen that specifically causes cancer by inducing mutations in genes that control cell division.",
        section: "17.1"
      },
      {
        term: "What is a point mutation?",
        definition: "A change in one or a few bases within a single gene, caused by incorrect base pairing during replication; examples include cystic fibrosis and haemophilia.",
        section: "17.1"
      },
      {
        term: "What is a chromosomal mutation?",
        definition: "A large-scale change in chromosome structure or number, including deletions, duplications, inversions and translocations; Down syndrome is an example.",
        section: "17.1"
      },
      {
        term: "What is the difference between mRNA and tRNA?",
        definition: "mRNA carries the genetic code from DNA to ribosomes for protein synthesis. tRNA brings specific amino acids to the ribosome and matches them to mRNA codons. Both are essential for translation.",
        section: "17.1"
      }
    ];
  })();

  // ── bio18: The Musculoskeletal System ─────────────────────────────────────
  (function () {
    var c = ch("bio18");
    // 18.1 — The structure and functions of the skeleton, muscles and joints
    c.learningOutcomes[0].notes = [
      {
        h: "Stimulus, Response and Adaptation",
        b: "A stimulus is anything that causes a reaction in an organism or any of its parts, while a response is the resulting activity of a cell or organism. An adaptation is any alteration that improves an organism's chances of survival and reproduction; plant anatomical adaptations include thorns and spikes to deter herbivores, while chemical adaptations include toxic compounds in leaves."
      },
      {
        h: "Functions of the Musculoskeletal System",
        b: "The musculoskeletal system provides support, protection, movement and shape for the body. An additional vital function is the manufacture of blood components — red blood cells, white blood cells and platelets are all produced within bone tissue."
      },
      {
        h: "The Axial Skeleton",
        b: "The axial skeleton consists of the skull, spine, vertebrae and sternum, and its primary role is to protect important internal organs. The spine is composed of 33 vertebrae separated by cartilage discs, divided into five regions: 7 cervical, 12 thoracic, 5 lumbar, 5 sacral and 4 coccygeal vertebrae. The rib cage comprises the sternum and 24 ribs (12 pairs): the top 7 are true ribs (attached to spine and sternum), the next 3 are false ribs (attached to a higher rib), and the lowest 2 are floating ribs (attached only to the spine)."
      },
      {
        h: "The Appendicular Skeleton",
        b: "The appendicular skeleton is composed of the limbs (arms and legs) together with the pectoral and pelvic girdles. The pectoral (shoulder) girdle consists of the clavicle (collarbone) and scapula (shoulder blade), while the pelvic (hip) girdle consists of the two hip halves joined to the sacrum. Key limb bones include the femur, patella, tibia and fibula in the legs, and the humerus, radius and ulna in the arms."
      },
      {
        h: "Antagonistic Muscles",
        b: "Antagonistic muscles are pairs of muscles that produce opposite effects, allowing controlled movement. The biceps is a flexor that contracts to raise (bend) the forearm, while the triceps is an extensor that contracts to straighten the forearm. Because they pull in opposite directions, precise and reversible joint movements are possible."
      },
      {
        h: "Joints",
        b: "A joint is any point where two or more bones meet, and joints are classified by their degree of movement. Immovable (fixed or fused) joints are found in the skull; slightly movable joints connect the vertebrae; synovial (freely movable) joints — which include ball-and-socket joints at the shoulder and hip, and hinge joints at the elbow and knee — allow the widest range of motion."
      },
      {
        h: "Connective Tissues at Joints",
        b: "Ligaments connect bone to bone, stabilising joints and limiting excessive movement. Tendons connect muscle to bone, transmitting the pulling force of a muscle contraction to the skeleton. Synovial fluid lubricates freely movable joints and reduces friction, while cartilage acts as a shock absorber and allows friction-free movement between bone surfaces."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the axial skeleton?",
        definition: "The central bony framework of the body comprising the skull, spine (33 vertebrae), ribs and sternum, which protects vital organs.",
        section: "18.1"
      },
      {
        term: "What is the appendicular skeleton?",
        definition: "The part of the skeleton made up of the limbs (arms and legs) and the pectoral and pelvic girdles, enabling movement.",
        section: "18.1"
      },
      {
        term: "What are antagonistic muscles?",
        definition: "A pair of muscles with opposing actions; one contracts while the other relaxes — e.g. biceps (flexor) and triceps (extensor) at the elbow.",
        section: "18.1"
      },
      {
        term: "What is a ligament?",
        definition: "A tough connective tissue that connects bone to bone, stabilising joints and limiting excessive movement.",
        section: "18.1"
      },
      {
        term: "What is a tendon?",
        definition: "A connective tissue that attaches muscle to bone, transmitting the force of muscle contraction to produce skeletal movement.",
        section: "18.1"
      },
      {
        term: "What is a synovial joint?",
        definition: "A freely movable joint (e.g. ball-and-socket or hinge) lubricated by synovial fluid, allowing a wide range of motion.",
        section: "18.1"
      },
      {
        term: "What is synovial fluid?",
        definition: "A lubricating fluid found in freely movable joints that reduces friction and allows smooth movement between bone surfaces.",
        section: "18.1"
      },
      {
        term: "What is cartilage?",
        definition: "Flexible connective tissue at joint surfaces that acts as a shock absorber and permits friction-free movement.",
        section: "18.1"
      },
      {
        term: "What is the pectoral girdle?",
        definition: "The bony structure (clavicle and scapula) that connects the upper limbs to the axial skeleton.",
        section: "18.1"
      },
      {
        term: "What is the pelvic girdle?",
        definition: "The bony structure (two hip bones joined to the sacrum) that connects the lower limbs to the axial skeleton.",
        section: "18.1"
      }
    ];
  })();

  // ── bio19: The Nervous System ─────────────────────────────────────────────
  (function () {
    var c = ch("bio19");
    // 19.1 — The structure and function of the nervous system, from neurons to brain regions
    c.learningOutcomes[0].notes = [
      {
        h: "Parts of the Nervous System",
        b: "The central nervous system (CNS) consists of the brain and spinal cord; it acts as the main control region, processing information and coordinating responses. The peripheral nervous system (PNS) consists of all nerves outside the CNS and carries impulses to and from it. Together they enable the body to detect stimuli and produce appropriate responses."
      },
      {
        h: "The Brain and Meninges",
        b: "The brain and spinal cord are protected by three membranes called meninges, with cerebrospinal fluid between the inner two layers acting as a shock absorber. Meningitis is the inflammation of the meninges; it can be viral or bacterial, with viral meningitis being more common but less severe, while only bacterial meningitis responds to antibiotic treatment."
      },
      {
        h: "Structure of the Brain",
        b: "The cerebrum (forebrain) is the largest region; its outer cerebral cortex (grey matter, containing cell bodies) controls voluntary movement, the senses, learning, memory and emotions, with each hemisphere controlling the opposite side of the body. The cerebellum (hindbrain) controls muscular coordination and balance. The thalamus relays all incoming impulses to the correct brain region, and the hypothalamus regulates homeostasis — monitoring temperature, appetite, thirst and blood pressure — while linking with the pituitary gland to control hormone production. The medulla oblongata connects brain and spinal cord and controls involuntary actions such as breathing, blood pressure, swallowing and coughing."
      },
      {
        h: "The Pituitary Gland",
        b: "Located below the hypothalamus, the pituitary is a pea-sized gland not technically part of the brain but known as the master gland because it produces and regulates a wide range of hormones, including TSH, oxytocin, prolactin, FSH and LH, and stores and releases ADH. By controlling other endocrine glands, it acts as the central regulator of the body's hormonal system."
      },
      {
        h: "Neurons and Their Structure",
        b: "A neuron is a nerve cell — the basic unit of the nervous system. Sensory neurons carry impulses from sense organs to the CNS; motor neurons carry impulses from the CNS to muscles or glands; interneurons link sensory and motor neurons within the CNS. Dendrites carry impulses towards the cell body; axons carry them away. Schwann cells produce the myelin sheath, a fat-rich insulating layer that speeds up impulse transmission. Axon terminals pass impulses on via neurotransmitter swellings."
      },
      {
        h: "Synapses and Neurotransmitters",
        b: "A synapse is a region where two neurons come into close contact, separated by a tiny synaptic cleft. Impulses are electrical within neurons but chemical across synapses: neurotransmitters released from the pre-synaptic neuron diffuse across the cleft, bind to receptors on the post-synaptic neuron to generate a new electrical impulse, and are then inactivated and returned to be reused. Synapses direct the flow of impulses, prevent overstimulation of effectors, and can be blocked or enhanced by drugs."
      },
      {
        h: "Neurotransmitters and Mood",
        b: "Acetylcholine plays a crucial role in muscle function, memory and learning; its deficiency is linked to Alzheimer's disease, which can be partially treated with drugs that inhibit the enzyme breaking it down. Endorphins are released during exercise, pleasure, pain and stress, acting to block pain, reduce inflammation and trigger dopamine release. Dopamine produces feelings of pleasure and motivation and is central to addiction as a reward substance; lifestyle factors including exercise and diet significantly affect natural dopamine and endorphin levels."
      },
      {
        h: "Reflex Actions",
        b: "A reflex action is an automatic, involuntary response to a stimulus whose function is to protect the body. Reflex reactions are rapid because they bypass the brain entirely, routing through the spinal cord instead: sensory neurons carry the impulse into the cord via the dorsal root, an interneuron passes it to a motor neuron, and the motor neuron exits via the ventral root to the effector (muscle or gland), producing an immediate response such as withdrawing a hand from heat."
      },
      {
        h: "Disruption to Neurotransmitter Function",
        b: "Psychoactive drugs disturb normal brain function by acting as artificial neurotransmitters, increasing natural neurotransmitter production or blocking their reuptake. Non-medical use of substances such as cocaine, cannabis, alcohol and nicotine artificially elevates dopamine and endorphin levels but suppresses the body's natural production, leading to dependency and addiction. Opioid painkillers bind to pain receptors in post-synaptic neurons, blocking pain and triggering large dopamine releases, explaining their high addiction potential."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the central nervous system (CNS)?",
        definition: "The brain and spinal cord; acts as the main processing and coordination centre for all nervous activity.",
        section: "19.1"
      },
      {
        term: "What is the peripheral nervous system (PNS)?",
        definition: "All nerves outside the CNS; carries sensory impulses to the CNS and motor impulses away from it.",
        section: "19.1"
      },
      {
        term: "What is the cerebrum?",
        definition: "The largest brain region (forebrain); its cortex controls voluntary movement, senses, memory, learning and emotion, with each hemisphere controlling the opposite side of the body.",
        section: "19.1"
      },
      {
        term: "What is the cerebellum?",
        definition: "The hindbrain region that controls muscular coordination and balance.",
        section: "19.1"
      },
      {
        term: "What is the medulla oblongata?",
        definition: "The brain region connecting to the spinal cord that controls involuntary actions such as breathing, blood pressure, swallowing and coughing.",
        section: "19.1"
      },
      {
        term: "What is the hypothalamus?",
        definition: "A brain region below the thalamus that regulates homeostasis (temperature, appetite, thirst, blood pressure) and links with the pituitary to control hormone release.",
        section: "19.1"
      },
      {
        term: "What is a neuron?",
        definition: "A nerve cell, the basic functional unit of the nervous system; types include sensory, motor and interneurons.",
        section: "19.1"
      },
      {
        term: "What is the myelin sheath?",
        definition: "A fat-rich insulating layer around axons, produced by Schwann cells, that speeds up the transmission of electrical impulses.",
        section: "19.1"
      },
      {
        term: "What is a synapse?",
        definition: "The junction between two neurons where impulse transmission switches from electrical (within neurons) to chemical (across the synaptic cleft via neurotransmitters).",
        section: "19.1"
      },
      {
        term: "What is a neurotransmitter?",
        definition: "A chemical released from axon terminals into the synaptic cleft that binds to receptors on the next neuron to generate or inhibit a new electrical impulse.",
        section: "19.1"
      },
      {
        term: "What is a reflex action?",
        definition: "An automatic, involuntary response to a stimulus that bypasses the brain and routes via the spinal cord, enabling a faster protective reaction.",
        section: "19.1"
      },
      {
        term: "What is the role of dopamine?",
        definition: "A neurotransmitter that produces feelings of pleasure, satisfaction and motivation; plays a central role in reward and addiction.",
        section: "19.1"
      }
    ];
  })();

  // ── bio20: The Endocrine System ───────────────────────────────────────────
  (function () {
    var c = ch("bio20");
    // 20.1 — How hormones are produced and used by the body, and their applications in health, sport and agriculture
    c.learningOutcomes[0].notes = [
      {
        h: "Endocrine Glands and Hormones",
        b: "Endocrine glands are ductless glands that secrete hormones directly into the bloodstream. A hormone is a chemical messenger produced by an endocrine gland, transported in the blood, and acting on a specific target tissue elsewhere in the body to produce a particular effect."
      },
      {
        h: "The Pituitary Gland",
        b: "The pituitary is a pea-sized gland located under the brain in the middle of the head and is known as the master gland because it produces hormones (including TSH, oxytocin, prolactin, FSH and LH) that regulate other endocrine glands, and also stores and releases ADH. By controlling other endocrine glands, it acts as the central coordinator of the hormonal system."
      },
      {
        h: "The Thyroid and Parathyroid Glands",
        b: "The thyroid is an H-shaped gland on the trachea in the neck that produces thyroxine, which controls metabolic rate and energy levels throughout the body. Just behind it sit four small parathyroid glands that produce parathyroid hormone (PTH), which regulates calcium levels in the blood — essential for bone health and nerve function."
      },
      {
        h: "The Adrenal Glands and Pancreas",
        b: "The two adrenal glands sit on top of the kidneys and produce adrenaline, which prepares the body for a stress response by increasing heart rate and energy availability. The pancreas, located just below the stomach, is a dual-function gland: it produces digestive enzymes and also contains the islets of Langerhans, which produce insulin to regulate blood glucose levels."
      },
      {
        h: "The Gonads",
        b: "The gonads produce sex hormones that drive reproductive development and function. The ovaries in females produce oestrogen and progesterone, which regulate the menstrual cycle and support pregnancy. The testes in males produce testosterone, which drives the development of male secondary sexual characteristics and supports sperm production."
      },
      {
        h: "Hormonal Manipulation in Sport",
        b: "Hormonal manipulation refers to the deliberate regulation of hormone levels for specific purposes. Several hormones are used illegally in sport: anabolic steroids build muscle, speed recovery after injury and strengthen bones; human growth hormone (somatotropin) stimulates growth and muscle development; and erythropoietin (EPO) increases red blood cell count, boosting oxygen delivery and available energy — all of which give unfair competitive advantages."
      },
      {
        h: "Hormones in Medicine",
        b: "Hormones have important therapeutic applications in medicine. Contraceptive pills use oestrogen and progesterone to prevent conception. Hormone replacement therapy (HRT) replaces the oestrogen and progesterone that decline at menopause, alleviating symptoms. Insulin injections are used to control blood glucose in type 1 diabetes, where the pancreas cannot produce sufficient insulin naturally."
      },
      {
        h: "Hormones in Agriculture",
        b: "Hormones are widely used in agriculture to increase productivity and manage reproduction. Progesterone regulates reproductive cycles in cattle to synchronise breeding. Growth hormones and anabolic steroids are used in some countries to promote growth and increase milk and meat yields. Plant hormones can be applied to ripen fruit, increase fruit size, stimulate root formation in cuttings and act as selective weedkillers."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a hormone?",
        definition: "A chemical messenger produced by an endocrine gland, transported in the bloodstream, and acting on a specific target tissue to produce a defined effect.",
        section: "20.1"
      },
      {
        term: "What is an endocrine gland?",
        definition: "A ductless gland that secretes hormones directly into the bloodstream rather than through a duct.",
        section: "20.1"
      },
      {
        term: "What is the pituitary gland?",
        definition: "The 'master gland' located under the brain that produces hormones (TSH, FSH, LH, oxytocin, prolactin) regulating other endocrine glands, and stores/releases ADH.",
        section: "20.1"
      },
      {
        term: "What is thyroxine?",
        definition: "A hormone produced by the thyroid gland that controls the body's metabolic rate and energy levels.",
        section: "20.1"
      },
      {
        term: "What is parathyroid hormone (PTH)?",
        definition: "A hormone produced by the four parathyroid glands that regulates calcium levels in the blood.",
        section: "20.1"
      },
      {
        term: "What is adrenaline?",
        definition: "A hormone produced by the adrenal glands (on top of the kidneys) that prepares the body for a stress response by increasing heart rate and energy availability.",
        section: "20.1"
      },
      {
        term: "What is insulin?",
        definition: "A hormone produced by the islets of Langerhans in the pancreas that lowers blood glucose levels; injected to manage type 1 diabetes.",
        section: "20.1"
      },
      {
        term: "What are the islets of Langerhans?",
        definition: "Hormone-producing clusters of cells within the pancreas responsible for secreting insulin to regulate blood glucose.",
        section: "20.1"
      },
      {
        term: "What are anabolic steroids?",
        definition: "Synthetic hormones used (often illegally in sport) to build muscle, accelerate recovery and strengthen bones by mimicking testosterone.",
        section: "20.1"
      },
      {
        term: "What is erythropoietin (EPO)?",
        definition: "A hormone that stimulates red blood cell production; misused in sport to increase oxygen-carrying capacity and endurance.",
        section: "20.1"
      },
      {
        term: "What is hormone replacement therapy (HRT)?",
        definition: "Medical treatment that replaces declining oestrogen and progesterone levels at menopause to relieve associated symptoms.",
        section: "20.1"
      }
    ];
  })();

  // ── bio21: HOMEOSTASIS ────────────────────────────────────────────────────
  (function () {
    var c = ch("bio21");
    // 21.1 — How organisms maintain a stable internal environment through feedback mechanisms and coordinated organ systems
    c.learningOutcomes[0].notes = [
      {
        h: "What is Homeostasis?",
        b: "Homeostasis is the ability of an organism to maintain a constant internal environment despite changes in external or internal conditions. An external change is a change in the surroundings in which an organism lives (e.g. freshwater or seawater for fish), while an internal change is a change in the surroundings of cells in a multicellular organism (e.g. tissue fluid in humans)."
      },
      {
        h: "Key Processes: Diffusion and Osmosis",
        b: "Diffusion is the spreading out of molecules from a region of high concentration to a region of low concentration. Osmosis is the movement of water molecules across a selectively permeable membrane from a region of high water concentration to a region of low water concentration."
      },
      {
        h: "Key Process: Active Transport",
        b: "Active transport is the use of energy to move molecules across biological membranes against a concentration gradient, that is, from low concentrations to high concentrations. Unlike diffusion and osmosis, active transport requires the cell to expend energy (ATP)."
      },
      {
        h: "Organs Involved in Homeostasis",
        b: "Several organs contribute to homeostasis: the liver absorbs or releases glucose and generates heat; the lungs excrete water and carbon dioxide and release heat; the kidneys (via nephrons) excrete or reabsorb water and salts; the skin regulates body temperature through sweating; and the testes produce testosterone in males."
      },
      {
        h: "Components of a Homeostatic System",
        b: "Every homeostatic system has three components: a receptor that detects a stimulus or change in the environment; a control centre that receives and processes information and sends instructions; and an effector that carries out the response."
      },
      {
        h: "Negative Feedback",
        b: "Negative feedback means that when the correct level of a factor is reached, it inhibits a previous step in the cycle, preventing the level from going any higher. In vertebrates, negative feedback operates through both hormonal and nervous pathways."
      },
      {
        h: "Negative Feedback: Thyroxine Regulation (Hormonal)",
        b: "When thyroxine levels are low, the hypothalamus signals the pituitary gland, which releases TSH (thyroid-stimulating hormone), which in turn stimulates the thyroid to produce thyroxine. Once thyroxine reaches the correct level, the hypothalamus stops signalling, TSH production ceases, and thyroxine production stops."
      },
      {
        h: "Negative Feedback: Temperature Control (Nervous)",
        b: "When body temperature is normal or low, the brain does not send nerve impulses to the skin, sweating does not occur, and heat is retained. When body temperature is high, the brain sends nerve impulses to the skin, causing sweating; as sweat evaporates, the body cools down."
      },
      {
        h: "Natural Variations in the Internal Environment",
        b: "The internal environment is not perfectly constant at all times. Body temperature drops by about 1°C during sleep, fever raises temperature to fight infection, and hormonal changes during the menstrual cycle, puberty, and menopause all alter internal conditions."
      },
      {
        h: "Nervous vs Hormonal Coordination: Speed and Medium",
        b: "Nervous coordination is fast-acting and uses nerve cells (neurons) to carry mostly electrical signals, producing short-lived, localised effects (e.g. catching an object). Hormonal coordination is slower-acting and uses blood to carry chemical signals, producing longer-lasting effects that may be widespread throughout the body (e.g. growth)."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is negative feedback?",
        definition: "A control mechanism in which the correct level of a factor inhibits a previous step in the regulatory cycle, preventing further change in that direction.",
        section: "21.1"
      },
      {
        term: "What is a receptor?",
        definition: "A component of a homeostatic system that detects a stimulus or change in the environment.",
        section: "21.1"
      },
      {
        term: "What is an effector?",
        definition: "A component of a homeostatic system that carries out the response instructed by the control centre.",
        section: "21.1"
      },
      {
        term: "What is active transport?",
        definition: "The use of energy (ATP) to move molecules across a biological membrane against a concentration gradient, from low to high concentration.",
        section: "21.1"
      },
      {
        term: "What is osmosis?",
        definition: "The movement of water molecules across a selectively permeable membrane from a region of high water concentration to a region of low water concentration.",
        section: "21.1"
      },
      {
        term: "What is TSH (thyroid-stimulating hormone)?",
        definition: "A hormone released by the pituitary gland that stimulates the thyroid gland to produce thyroxine; part of the negative feedback loop regulating thyroxine levels.",
        section: "21.1"
      },
      {
        term: "What is nervous coordination?",
        definition: "A fast-acting, short-lived, localised form of communication in the body that uses electrical signals carried by neurons.",
        section: "21.1"
      },
      {
        term: "What is hormonal coordination?",
        definition: "A slower-acting, longer-lasting form of communication in the body that uses chemical signals carried in the blood and can have widespread effects.",
        section: "21.1"
      }
    ];
  })();

  // ── bio22: IMMUNITY ───────────────────────────────────────────────────────
  (function () {
    var c = ch("bio22");
    // 22.1 — How the immune system defends the body against pathogens through innate and acquired immunity, B cells, T cells, and vaccination
    c.learningOutcomes[0].notes = [
      {
        h: "Pathogens",
        b: "A pathogen is an organism or agent that causes disease. Pathogens include prions (misfolded proteins that convert other proteins, e.g. CJD), viruses (e.g. HIV, chickenpox), bacteria (e.g. cholera, tetanus), fungi, protists (mostly unicellular eukaryotes such as Amoeba), and parasitic animals such as roundworms, lice, and ticks."
      },
      {
        h: "Innate and Acquired Immunity",
        b: "Immunity is the ability to resist infection. Innate immunity is a defence system we are born with that does not depend on previous exposure to a pathogen. Acquired (or adaptive) immunity is long-lasting protection against reinfection that develops following infection with, or immunisation against, a specific pathogen."
      },
      {
        h: "Three Lines of Defence",
        b: "The first line of defence consists of physical and chemical barriers such as skin, mucus, sebum, lysozyme, hydrochloric acid in the stomach, cilia, and beneficial bacteria. The second line involves internal defences including phagocytes (e.g. macrophages), complement proteins, interferons, inflammation, and fever. The third line involves antibodies produced by B cells and T cells that destroy infected cells."
      },
      {
        h: "Antigens and Antibodies",
        b: "An antigen is a foreign molecule that stimulates the production of antibodies; antigens are found on the coats of viruses and the cell walls of bacteria, fungi, and other microorganisms. An antibody is a Y-shaped protein produced by lymphocytes in response to a specific antigen. Each antibody is complementary to a single antigen. Antibodies inactivate antigens, help phagocytes engulf pathogens, and cause pathogens to clump together."
      },
      {
        h: "Active Immunity",
        b: "Active immunity involves a person producing their own antibodies in response to foreign antigens and gives long-term resistance to infection. Natural active immunity arises when a pathogen enters the body naturally (e.g. getting flu). Artificial active immunity arises through vaccination, where a non-disease-causing dose of a pathogen or its toxin is administered to stimulate antibody production."
      },
      {
        h: "Vaccination and Immunisation",
        b: "Vaccination is the administration of a vaccine to stimulate antibody production. Immunisation is the broader process of making a person resistant to an infectious disease. A second vaccine dose reinforces immune memory by stimulating B lymphocytes to produce more effective, longer-lasting antibodies. Common vaccines include those for hepatitis, polio, tetanus, and MMR (measles, mumps, and rubella)."
      },
      {
        h: "Passive Immunity",
        b: "Passive immunity occurs when an individual is given antibodies formed by another organism, providing only short-term resistance (weeks to months). Natural passive immunity occurs when a child receives antibodies from its mother across the placenta or through breastfeeding. Artificial passive immunity occurs when a person is given an injection of antibodies produced by another organism."
      },
      {
        h: "Viral Replication",
        b: "Viruses are obligate parasites that replicate by entering a host cell and using its energy and organelles. The stages are: attachment to the host cell; entry (injecting viral DNA or RNA); synthesis of new viral nucleic acids and proteins using host organelles; assembly of new viruses inside the cell; and release as the host cell bursts. An obligate parasite can only take food from a living host, whereas a facultative parasite can take food from a living or dead host."
      },
      {
        h: "Emerging Infectious Diseases and R0",
        b: "New diseases emerge through microbial mutation, antibiotic misuse, zoonosis (disease jumping from animals to humans), environmental changes, or accidental laboratory releases. Disease spread depends on pathogen survival, population immunity, population mobility, and contagiousness (R0). If R0 is less than 1, the disease will die out; if R0 equals 1, it persists at the same level; if R0 exceeds 1, the disease spreads and may cause an epidemic."
      },
      {
        h: "White Blood Cell Types",
        b: "White blood cells (leucocytes) are made in bone marrow and include three main types: phagocytes, which engulf and destroy microorganisms; monocytes (or macrophages), which engulf microorganisms and display antigens on their surface; and lymphocytes, which include natural killer (NK) cells (destroying virus-infected and cancer cells), B cells (maturing in bone marrow), and T cells (maturing in the thymus gland)."
      },
      {
        h: "B Cell and T Cell Types",
        b: "The humoral immune response involves B cells: plasma B cells produce antibodies, while memory B cells survive for years and can quickly produce the specific antibody if the same pathogen returns. The cell-mediated response involves T cells: helper T cells stimulate B cells and killer T cells; killer T cells destroy virus-infected and cancer cells; suppressor T cells inhibit the immune response; and memory T cells provide long-term immunity by reactivating specific B and killer T cells upon re-infection."
      },
      {
        h: "Preventing and Treating Microbial Diseases",
        b: "Prevention strategies include personal hygiene, food and water sanitation, vaccination, and avoiding antibiotic misuse. Treatment options depend on the type of pathogen: antibiotics for bacteria, antiviral drugs for viruses, antifungal drugs for fungi, immunotherapy, and bacteriophages for bacterial infections."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a pathogen?",
        definition: "An organism or agent that causes disease, including prions, viruses, bacteria, fungi, protists, and parasitic animals.",
        section: "22.1"
      },
      {
        term: "What is an antigen?",
        definition: "A foreign molecule (e.g. from a virus coat or bacterial cell wall) that stimulates the production of antibodies by the immune system.",
        section: "22.1"
      },
      {
        term: "What is an antibody?",
        definition: "A Y-shaped protein produced by B lymphocytes in response to a specific antigen; each antibody is complementary to a single antigen.",
        section: "22.1"
      },
      {
        term: "What is innate immunity?",
        definition: "A non-specific defence system present from birth that does not depend on previous exposure to a pathogen; includes physical barriers and phagocytes.",
        section: "22.1"
      },
      {
        term: "What is acquired (adaptive) immunity?",
        definition: "Long-lasting, pathogen-specific protection that develops after infection or immunisation, involving B cells and T cells.",
        section: "22.1"
      },
      {
        term: "What is vaccination?",
        definition: "The administration of a vaccine (a non-disease-causing dose of a pathogen or its toxin) to stimulate the production of antibodies and immunological memory.",
        section: "22.1"
      },
      {
        term: "What is passive immunity?",
        definition: "Short-term immunity (weeks to months) obtained by receiving antibodies produced by another organism, rather than producing them oneself.",
        section: "22.1"
      },
      {
        term: "What is R0 (basic reproduction number)?",
        definition: "A measure of how contagious an infectious disease is; indicates the average number of people one infected person will pass the disease to in a fully susceptible population.",
        section: "22.1"
      },
      {
        term: "What are memory B cells?",
        definition: "Long-lived B lymphocytes that persist after an infection and can rapidly produce the specific antibody if the same pathogen is encountered again.",
        section: "22.1"
      },
      {
        term: "What are helper T cells?",
        definition: "T lymphocytes that stimulate both B cells (to produce antibodies) and killer T cells (to destroy infected cells), coordinating the adaptive immune response.",
        section: "22.1"
      },
      {
        term: "What is a phagocyte?",
        definition: "A white blood cell that engulfs and destroys microorganisms and foreign particles by phagocytosis.",
        section: "22.1"
      },
      {
        term: "What is a zoonosis?",
        definition: "An infectious disease that has jumped from a non-human animal to a human, one mechanism by which new emerging infectious diseases arise.",
        section: "22.1"
      }
    ];
  })();

  // ── bio23: HUMAN REPRODUCTION ─────────────────────────────────────────────
  (function () {
    var c = ch("bio23");
    // 23.1 — The structure and function of the human male and female reproductive systems, the menstrual cycle, fertilisation, embryonic development, and fertility control
    c.learningOutcomes[0].notes = [
      {
        h: "The Male Reproductive System",
        b: "The testis is the male gonad, located outside the body in the scrotum because meiosis occurs optimally at 35°C, not at body temperature (37°C). The testes produce sperm and testosterone. Sperm mature and are stored in the epididymis for up to 6 weeks before travelling via the sperm duct to the urethra. The seminal vesicles and prostate gland produce seminal fluid, which nourishes sperm (containing fructose) and provides a swimming medium; seminal fluid combined with sperm forms semen."
      },
      {
        h: "Structure of a Sperm Cell",
        b: "Each sperm cell has four key parts: an acrosome containing enzymes that digest the egg's membrane; a nucleus with 23 chromosomes; a midpiece (collar) packed with mitochondria to supply energy for swimming; and a tail (flagellum) that propels the sperm. During fertilisation, only the head of the sperm enters the egg."
      },
      {
        h: "Male Hormones: FSH, LH, and Testosterone",
        b: "FSH (follicle-stimulating hormone) causes diploid sperm-producing cells in the testes to divide by meiosis and produce haploid sperm. LH (luteinising hormone) stimulates the testes to produce testosterone. Testosterone causes primary male sex characteristics (e.g. growth of the penis) and secondary male characteristics such as growth of body and facial hair, deepening of the voice, and increased muscular and bone development."
      },
      {
        h: "The Female Reproductive System",
        b: "The ovaries are the female gonads, producing eggs and the hormones oestrogen and progesterone. At ovulation, an egg is released from an ovary and moved along the Fallopian tube by cilia and muscular peristalsis; the egg can only be fertilised for 24 hours after ovulation. The endometrium is the inner lining of the uterus, which thickens each month with cells and blood. The cervix is the opening into the uterus; the vagina serves as the entry for sperm and the birth canal."
      },
      {
        h: "The Menstrual Cycle",
        b: "The menstrual cycle is a series of events averaging 28 days, occurring when fertilisation has not taken place. Menstruation (shedding of the endometrium) occurs from Day 1 to Day 5. The follicular phase (Days 1–14) sees meiosis produce potential eggs surrounded by Graafian follicles, with oestrogen causing the endometrium to thicken and inhibiting new egg formation. Ovulation occurs on Day 14. The luteal phase follows, during which progesterone maintains the endometrium and inhibits further eggs and ovulation. If fertilisation does not occur, progesterone falls and the cycle restarts on Day 28."
      },
      {
        h: "Hormonal Control of the Menstrual Cycle",
        b: "FSH stimulates Graafian follicle development and thereby oestrogen production. Oestrogen develops the endometrium and inhibits FSH by negative feedback. A surge in LH triggers ovulation and causes the remains of the Graafian follicle to become the corpus luteum, which produces progesterone. Progesterone maintains the endometrium, inhibits FSH and LH to prevent further ovulation, and prevents uterine contractions."
      },
      {
        h: "Fertilisation and Early Zygote Development",
        b: "Fertilisation occurs in the Fallopian tube when the sperm nucleus fuses with the egg nucleus, forming a diploid zygote with 46 chromosomes. Once one sperm enters, a fertilisation membrane forms to prevent further entry. The zygote divides by mitosis to form a solid morula (after ~3 days), then a hollow blastocyst of ~100 cells (after ~5 days). About 10 days after fertilisation, the inner cell mass differentiates into three germ layers: ectoderm (skin, nervous system), mesoderm (muscles, skeleton, circulatory system), and endoderm (digestive and respiratory linings, liver, pancreas)."
      },
      {
        h: "Implantation and the Placenta",
        b: "Implantation is the embedding of the embryo into the uterine lining, occurring 6–9 days after fertilisation. The amnion develops around the embryo, secreting amniotic fluid that acts as a shock absorber. The placenta forms from both maternal uterine tissue and embryonic tissue and is connected to the embryo by the umbilical cord. The placenta exchanges gases, nutrients, waste, antibodies, and some hormones between mother and embryo by diffusion, prevents the two blood supplies from mixing (incompatible blood types; pressure difference), and produces progesterone."
      },
      {
        h: "Gestation and Labour",
        b: "Gestation is the time from fertilisation to birth, lasting 266 days (38 weeks) in humans. Throughout pregnancy, progesterone is produced in increasing amounts to prevent uterine contractions (first by the ovary, then after 10 weeks by the placenta). Labour begins when the placenta stops producing progesterone and the pituitary gland releases oxytocin, causing strong uterine contractions. Birth follows as contractions push the foetus head-first through the vagina, the umbilical cord is cut, and the placenta is expelled as afterbirth."
      },
      {
        h: "Milk Production (Lactation)",
        b: "Lactation is the secretion of milk by the mammary glands of the female. The pituitary gland produces prolactin to stimulate milk production. Colostrum, a thick yellow fluid produced in the first days after birth, is high in minerals, proteins, and antibodies and provides early nutrition and infection protection. Breastfeeding benefits the baby (ideal nutrients, antibodies, sterile supply) and the mother (uterine contraction recovery, fat loss, reduced breast cancer risk)."
      },
      {
        h: "Contraception Methods",
        b: "Contraception is the deliberate prevention of fertilisation or pregnancy. Natural methods involve avoiding intercourse during the fertile period (unreliable). Mechanical methods use physical barriers such as condoms, diaphragms, caps, and IUDs; condoms also reduce STI transmission. Surgical methods (sterilisation for females, vasectomy for males) are highly effective but largely permanent. Chemical methods use spermicides or hormones (e.g. the contraceptive pill containing progesterone and oestrogen) to prevent ovulation."
      },
      {
        h: "Infertility and IVF",
        b: "Infertility is the inability to produce offspring. Male infertility may be caused by low sperm count, poor sperm motility, or blockages; treatment includes lifestyle changes, hormone therapy, surgery, or assisted reproductive technology (ART). Female infertility may be caused by failure to ovulate or blocked Fallopian tubes; treatment includes hormone injections, artificial insemination, or IVF. In vitro fertilisation (IVF) involves stimulating multiple egg production with fertility drugs, surgically removing the eggs, mixing them with sperm in a dish, and placing resulting embryos into the uterus."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a gonad?",
        definition: "An organ that produces sex cells (gametes) in animals; the testis is the male gonad and the ovary is the female gonad.",
        section: "23.1"
      },
      {
        term: "What is the acrosome?",
        definition: "A cap-like structure at the head of a sperm cell containing enzymes that digest the membrane of the egg to allow fertilisation.",
        section: "23.1"
      },
      {
        term: "What is ovulation?",
        definition: "The release of a mature egg from a Graafian follicle in the ovary, normally occurring on Day 14 of the menstrual cycle.",
        section: "23.1"
      },
      {
        term: "What is the menstrual cycle?",
        definition: "A series of hormonal and physiological events averaging 28 days in the female, involving the maturation of an egg, ovulation, endometrium thickening, and menstruation if fertilisation does not occur.",
        section: "23.1"
      },
      {
        term: "What is oestrogen?",
        definition: "A female hormone produced by cells surrounding the egg in the ovary; causes the endometrium to thicken and inhibits FSH by negative feedback.",
        section: "23.1"
      },
      {
        term: "What is progesterone?",
        definition: "A hormone produced by the corpus luteum that maintains the endometrium, inhibits FSH and LH, and prevents uterine contractions during pregnancy.",
        section: "23.1"
      },
      {
        term: "What is fertilisation?",
        definition: "The fusion of the nucleus of a sperm with the nucleus of an egg in the Fallopian tube, producing a diploid zygote with 46 chromosomes.",
        section: "23.1"
      },
      {
        term: "What is a blastocyst?",
        definition: "A hollow ball of approximately 100 cells that forms about five days after fertilisation from the morula, prior to implantation in the uterine wall.",
        section: "23.1"
      },
      {
        term: "What is implantation?",
        definition: "The embedding of the embryo into the lining of the uterus (endometrium), occurring approximately 6–9 days after fertilisation.",
        section: "23.1"
      },
      {
        term: "What is the placenta?",
        definition: "An organ formed from maternal and embryonic tissue that allows exchange of gases, nutrients, waste, and antibodies between mother and embryo, prevents blood mixing, and produces progesterone.",
        section: "23.1"
      },
      {
        term: "What is oxytocin?",
        definition: "A hormone produced by the pituitary gland immediately before and during labour that stimulates strong contractions of the uterine muscle.",
        section: "23.1"
      },
      {
        term: "What is in vitro fertilisation (IVF)?",
        definition: "An assisted reproductive technology in which eggs removed from the ovaries are fertilised by sperm in a dish outside the body, with resulting embryos transferred to the uterus.",
        section: "23.1"
      }
    ];
  })();

  // ── bio24: PLANT REPRODUCTION ─────────────────────────────────────────────
  (function () {
    var c = ch("bio24");
    // 24.1 — The structure of flowers, pollination, fertilisation, seed and fruit formation, dispersal, and germination in plants
    c.learningOutcomes[0].notes = [
      {
        h: "Parts of a Flower",
        b: "The flower's function is sexual reproduction. The receptacle supports all floral parts. Sepals protect the flower in bud. Petals in animal-pollinated plants are large and brightly coloured to attract insects, while in wind-pollinated plants they are small or absent. Stamens are the male parts, each consisting of a filament and an anther that produces pollen grains by meiosis. Carpels are the female parts, each consisting of a stigma (where pollen lands), a style (through which the pollen tube grows), and an ovary containing ovules; meiosis in the ovule produces a haploid egg cell."
      },
      {
        h: "Pollination",
        b: "Pollination is the transfer of pollen from an anther to a stigma of a flower of the same species. Self-pollination transfers pollen within the same plant; cross-pollination transfers it between different plants, allowing greater genetic variation and preventing inbreeding. Wind pollination is wasteful of pollen and occurs in conifers, grasses, oak, hazel, and alder. Animal pollination (mostly by insects) wastes less pollen and occurs in orchids, dandelions, primroses, snapdragons, daisies, and buttercups."
      },
      {
        h: "Adaptations for Wind vs Insect Pollination",
        b: "Wind-pollinated flowers have small or absent petals, no scent or nectaries, large amounts of light smooth dry pollen, large loosely attached anthers positioned outside petals, and large feathery stigmas outside petals. Insect-pollinated flowers have large, brightly coloured, scented petals with nectaries, small amounts of large heavy sticky pollen, small firmly attached anthers inside petals, and small sticky stigmas inside petals."
      },
      {
        h: "Fertilisation in Plants",
        b: "Fertilisation in plants is the union of the sperm nucleus (from the pollen tube) and the egg nucleus in the ovule to form a diploid zygote. After fertilisation, the ovule develops into the seed and the ovary develops into the fruit."
      },
      {
        h: "Seed Formation",
        b: "The fertilised ovule swells with food and becomes the seed. The ovule walls dry up to form the testa (seed coat). The zygote divides by mitosis to form an embryo consisting of the radicle (which develops into a root) and the plumule (which develops into a shoot). The endosperm is the food store (fats, protein, starch) surrounding the embryo. Some embryo cells form cotyledons (seed leaves): monocots have one cotyledon; dicots have two."
      },
      {
        h: "Fruit Formation",
        b: "A fruit is a developed or mature ovary. The wall of the ovary becomes the pericarp (the fruit wall). Fruits protect seeds and aid in their dispersal. Fruits may be succulent or fleshy (e.g. tomatoes, grapes) or dry (e.g. pea pods, popcorn grains)."
      },
      {
        h: "Growth Regulators in Plants",
        b: "A growth regulator is a chemical that controls plant growth, typically produced in one part of the plant and transported via vascular tissue (xylem and phloem) to act elsewhere. Growth promoters include auxins (made in seeds; stimulate fruit formation), cytokinins (control seed development, cell division, and stimulate germination), and gibberellins (stimulate fruit formation and germination). Growth inhibitors include ethene (ripens fruit) and abscisic acid (ABA), which inhibits germination and maintains seed dormancy."
      },
      {
        h: "Fruit and Seed Dispersal",
        b: "Dispersal is the transfer of a seed or fruit away from the parent plant, allowing seeds to avoid competition and colonise new areas. Wind dispersal occurs with light seeds (orchids) and parachute structures (dandelions, thistles) or winged fruits (sycamore, ash). Water dispersal uses light air-filled fruits that float (coconut, alder, water lily). Animal dispersal includes sticky hooked fruits (burdock, goose grass) and edible fruits whose seeds pass unharmed through digestive systems (strawberries). Self-dispersal uses explosive seed pods (peas, beans, gorse)."
      },
      {
        h: "Germination",
        b: "Germination is the growth of a seed when environmental conditions are suitable. Three conditions are required: water, which activates enzymes; oxygen, which is needed for aerobic respiration to supply energy; and a suitable temperature, which allows enzyme activity to proceed at the necessary rate."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the stamen?",
        definition: "The male reproductive structure of a flower, consisting of a filament and an anther that produces haploid pollen grains by meiosis.",
        section: "24.1"
      },
      {
        term: "What is the carpel?",
        definition: "The female reproductive structure of a flower, consisting of a stigma, style, and ovary containing ovules; after fertilisation the ovule becomes a seed and the ovary becomes a fruit.",
        section: "24.1"
      },
      {
        term: "What is pollination?",
        definition: "The transfer of pollen from an anther to a stigma of a flower from the same species, either by wind, insects, or other animals.",
        section: "24.1"
      },
      {
        term: "What is cross-pollination?",
        definition: "The transfer of pollen from an anther on one plant to a stigma on a different plant of the same species, promoting genetic variation and preventing inbreeding.",
        section: "24.1"
      },
      {
        term: "What is the testa?",
        definition: "The hard outer coat of a seed, formed from the dried walls of the ovule, that protects the embryo.",
        section: "24.1"
      },
      {
        term: "What is a cotyledon?",
        definition: "A seed leaf within the embryo that swells with stored food absorbed from the endosperm; monocots have one and dicots have two cotyledons.",
        section: "24.1"
      },
      {
        term: "What is the endosperm?",
        definition: "The nutrient-rich food store (containing fats, protein, and starch) surrounding the embryo inside a seed, used to fuel germination.",
        section: "24.1"
      },
      {
        term: "What is auxin?",
        definition: "A plant growth promoter produced in seeds that stimulates fruit formation and, in shoots, promotes cell elongation.",
        section: "24.1"
      },
      {
        term: "What is abscisic acid (ABA)?",
        definition: "A plant growth inhibitor that suppresses seed germination and maintains seed dormancy until environmental conditions are favourable.",
        section: "24.1"
      },
      {
        term: "What is dispersal?",
        definition: "The transfer of a seed or fruit away from the parent plant by wind, water, animals, or explosive self-dispersal mechanisms, reducing competition and enabling colonisation of new areas.",
        section: "24.1"
      },
      {
        term: "What is germination?",
        definition: "The resumption of growth by a seed when conditions are suitable; requires water (to activate enzymes), oxygen (for aerobic respiration), and a suitable temperature.",
        section: "24.1"
      }
    ];
  })();

  // ── bio25: Transport Across Membranes ─────────────────────────────────────
  (function () {
    var c = ch("bio25");
    // 25.1 — Diffusion, osmosis, active transport
    c.learningOutcomes[0].notes = [
      {
        h: "Diffusion",
        b: "Movement of particles from high to low concentration. Passive — no ATP required; driven by concentration gradient. Examples: O2 into blood from alveoli; CO2 the reverse."
      },
      {
        h: "Selectively Permeable Membrane",
        b: "Allows some molecules through (small/non-polar) and blocks others (large/charged). Cell membrane, nuclear membrane and organelle membranes are all selectively permeable."
      },
      {
        h: "Osmosis",
        b: "Movement of WATER from high water concentration (low solute) to low water concentration (high solute) across a selectively permeable membrane. Special case of diffusion."
      },
      {
        h: "Osmosis vs Diffusion",
        b: "Osmosis: only water moves, only across a selectively permeable membrane. Diffusion: any dissolved particle, across any barrier."
      },
      {
        h: "Isotonic, Hypotonic, Hypertonic",
        b: "Isotonic: same concentration as cytoplasm — no net movement. Hypotonic outside: water enters — animal swells/bursts (haemolysis); plant becomes turgid. Hypertonic outside: water leaves — animal shrinks (crenation); plant becomes flaccid/plasmolysed."
      },
      {
        h: "Turgor Pressure",
        b: "Pressure of cell contents against the cell wall in plants. Keeps non-woody plants firm. Cellulose wall resists bursting. Loss of turgor = wilting."
      },
      {
        h: "Active Transport",
        b: "Movement of substances AGAINST a concentration gradient using ATP. Examples: mineral uptake by root hairs; sodium-potassium pump in nerve cells; glucose reabsorption in kidney tubules."
      },
      {
        h: "Osmosis Experiment (Visking Tubing)",
        b: "IV = temperature/sucrose concentration/surface area. DV = mass change of tubing. Tubing partially filled so it can expand. Increase in mass = water entered by osmosis."
      },
      {
        h: "Osmosis Applications",
        b: "Salting meat: high salt draws water out of microbes by osmosis, killing them. Plant turgor supports stems. Rehydration therapy replaces water and salts."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is diffusion?",
        definition: "Passive movement of particles from high to low concentration. No ATP required; driven by the concentration gradient.",
        section: "25.1"
      },
      {
        term: "What is a selectively permeable membrane?",
        definition: "Allows some molecules through (small/non-polar) and blocks others (large/charged). All cell membranes are selectively permeable.",
        section: "25.1"
      },
      {
        term: "What is an isotonic solution?",
        definition: "A solution with the same solute concentration as the cell's cytoplasm — no net movement of water by osmosis occurs.",
        section: "25.1"
      },
      {
        term: "What is a hypotonic solution?",
        definition: "A solution more dilute than the cell's cytoplasm. Water enters the cell by osmosis. Animal cells swell/burst (haemolysis); plant cells become turgid.",
        section: "25.1"
      },
      {
        term: "What is a hypertonic solution?",
        definition: "A solution more concentrated than the cell's cytoplasm. Water leaves the cell by osmosis. Animal cells shrink (crenation); plant cells become flaccid/plasmolysed.",
        section: "25.1"
      },
      {
        term: "What is turgor pressure?",
        definition: "Pressure of cell contents pushing against the cellulose cell wall in a turgid plant cell. Keeps non-woody plants firm; loss of turgor = wilting.",
        section: "25.1"
      },
      {
        term: "What is active transport?",
        definition: "Movement of substances AGAINST a concentration gradient using ATP and carrier proteins. Examples: mineral uptake by root hairs; Na⁺/K⁺ pump; glucose reabsorption in kidneys.",
        section: "25.1"
      },
      {
        term: "What is haemolysis?",
        definition: "Bursting of an animal (red blood) cell when placed in a hypotonic solution — water enters by osmosis and the cell lacks a rigid wall to resist expansion.",
        section: "25.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Define osmosis and explain how it differs from diffusion.",
        model: "Osmosis is the movement of water molecules from an area of high water concentration (low solute) to an area of low water concentration (high solute) across a selectively permeable membrane. It differs from diffusion in that only water molecules move, and only across a selectively permeable membrane; diffusion can involve any dissolved substance and does not require a membrane."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain what happens to an animal cell and a plant cell when placed in a hypotonic solution.",
        model: "In a hypotonic solution (more water outside), water enters both cells by osmosis. The animal cell swells and may burst (haemolysis) because it has no rigid wall. The plant cell also gains water and becomes turgid; the cellulose cell wall resists the swelling pressure, so the plant cell does not burst."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Describe active transport and give two examples.",
        model: "Active transport is the movement of substances against their concentration gradient (low to high) using ATP and carrier proteins. Examples: (1) mineral ion uptake by root hair cells from dilute soil water. (2) Glucose reabsorption in kidney tubule cells, pumped back into the blood from dilute filtrate."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Describe an experiment using Visking tubing to investigate the effect of concentration gradient on the rate of osmosis.",
        model: "Fill three pieces of Visking tubing with different sucrose concentrations (e.g. 0.1, 0.5, 1.0 M). Weigh each. Place each in beakers of distilled water for 30 min. Reweigh. The increase in mass shows water entered by osmosis. Higher sucrose concentration inside produces a steeper gradient and greater mass increase. Keep temperature, surface area and time constant."
      }
    ];
    c.examQuestions = [
      {
        id: "bio25-eq-1",
        source: "LC Biology Past Paper — Q9 (Osmosis)",
        parts: [
          {
            label: "9. (a)",
            question: "Explain the term osmosis.",
            marks: 4,
            model: "Osmosis is the movement of water molecules from a region of high water concentration (low solute concentration) to a region of low water concentration (high solute concentration) across a selectively permeable membrane. It is a passive process — no ATP is required — and is a special case of diffusion involving only water.",
            diagram: ""
          },
          {
            label: "9. (b) (i)",
            question: "Name the tissue or membrane that you used in a laboratory activity to demonstrate osmosis.",
            marks: 2,
            model: "Visking tubing (dialysis/cellophane tubing) — a selectively permeable membrane. Alternatively: potato tissue or beetroot tissue, which contain natural selectively permeable membranes.",
            diagram: ""
          },
          {
            label: "9. (b) (ii)",
            question: "Describe how you carried out this activity, including the result. You may include a labelled diagram.",
            marks: 10,
            model: "Method using Visking tubing: 1. Soak a piece of Visking tubing in water to make it pliable; tie one end tightly. 2. Fill the tubing with a concentrated sucrose solution (e.g. 1 mol/L); tie the other end, leaving slack for expansion; weigh the tubing. 3. Place the filled tubing in a beaker of distilled water and leave for 20-30 minutes. 4. Remove, dry the outside gently and reweigh. Control: identical tubing filled with distilled water placed in distilled water — no mass change expected. Result: The tubing filled with sucrose solution increases in mass and becomes more turgid, because water moved by osmosis from the distilled water (high water concentration) across the selectively permeable Visking tubing membrane into the sucrose solution (lower water concentration). The control tube shows no change in mass, confirming the result is due to the concentration gradient.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio26: The Urinary System ─────────────────────────────────────────────
  (function () {
    var c = ch("bio26");
    // 26.1 — Kidney structure, nephron, ADH and osmoregulation
    c.learningOutcomes[0].notes = [
      {
        h: "Urinary System Components",
        b: "Two kidneys, two ureters, one bladder, one urethra. Kidneys flanking the spine at the back of the abdomen."
      },
      {
        h: "Kidney Zones",
        b: "Cortex (outer, filtration), medulla (inner, loops of Henle), pelvis (collects urine -> ureter). Blood in via renal artery, out via renal vein."
      },
      {
        h: "Kidney Functions",
        b: "Excretion of urea and wastes. Osmoregulation (water/salt balance). Blood pH maintenance (~7.4). All via filtration, reabsorption and secretion in nephrons."
      },
      {
        h: "Filtration",
        b: "Glomerulus: high-pressure knot of capillaries forces small molecules into Bowman's capsule. Filtered: water, glucose, salts, urea, amino acids. NOT filtered: red blood cells, plasma proteins, platelets."
      },
      {
        h: "Reabsorption",
        b: "PCT: glucose, amino acids, salts, water, vitamins (active transport — microvilli + many mitochondria). Loop of Henle: water + salts. DCT: fine-tunes salts and pH. Collecting duct: water (ADH-controlled)."
      },
      {
        h: "Urine Composition",
        b: "Normal urine: water (95%), urea, salts, creatinine. Normal urine does NOT contain glucose, protein or blood cells."
      },
      {
        h: "Urea Production",
        b: "Produced in the liver by deamination of excess amino acids. Filtered at glomerulus; not fully reabsorbed; excreted in urine."
      },
      {
        h: "ADH (Antidiuretic Hormone)",
        b: "Released from posterior pituitary. Makes collecting ducts more permeable -> more water reabsorbed -> concentrated urine."
      },
      {
        h: "ADH Feedback",
        b: "Dehydrated (high solute): hypothalamus detects -> pituitary releases ADH -> more reabsorption -> small concentrated urine. Over-hydrated: less ADH -> dilute, plentiful urine."
      },
      {
        h: "Diabetes Insipidus",
        b: "Without ADH: collecting ducts cannot reabsorb water -> large volumes of dilute urine -> severe thirst."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a nephron?",
        definition: "The functional unit of the kidney. Consists of Bowman's capsule, PCT, loop of Henle, DCT and collecting duct. Performs filtration, reabsorption and secretion.",
        section: "26.1"
      },
      {
        term: "What is glomerular filtration?",
        definition: "High blood pressure in the glomerulus forces small molecules (water, glucose, urea, salts, amino acids) into the Bowman's capsule. Large molecules and blood cells remain in the blood.",
        section: "26.1"
      },
      {
        term: "What is reabsorption (in the PCT)?",
        definition: "The proximal convoluted tubule reabsorbs glucose, amino acids, salts, water and vitamins by active transport. Microvilli and many mitochondria maximise efficiency.",
        section: "26.1"
      },
      {
        term: "What is urea?",
        definition: "Waste product of protein metabolism; produced in the liver by deamination. Filtered at the glomerulus; not fully reabsorbed; excreted in urine.",
        section: "26.1"
      },
      {
        term: "What is ADH (antidiuretic hormone)?",
        definition: "Released from the posterior pituitary when blood is too concentrated. Makes collecting ducts more permeable to water → more water reabsorbed → small, concentrated urine.",
        section: "26.1"
      },
      {
        term: "What is osmoregulation?",
        definition: "The regulation of water and salt balance in the body. Controlled mainly by ADH acting on the collecting ducts of the nephron.",
        section: "26.1"
      },
      {
        term: "What is deamination?",
        definition: "Removal of the amino group from excess amino acids in the liver. Produces urea (excreted by kidneys) and a carbon residue used for energy.",
        section: "26.1"
      },
      {
        term: "What is normal urine composition?",
        definition: "Water (~95%), urea, salts, creatinine. Normal urine does NOT contain glucose, plasma proteins or blood cells.",
        section: "26.1"
      },
      {
        term: "What is diabetes insipidus?",
        definition: "Condition where ADH is absent or ineffective — collecting ducts cannot reabsorb water → large volumes of dilute urine → severe thirst.",
        section: "26.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Describe the process of filtration in the nephron.",
        model: "Blood enters the glomerulus (a knot of capillaries in the Bowman's capsule) at high pressure. This pressure forces small molecules — water, glucose, urea, salts and amino acids — out of the blood into the Bowman's capsule (glomerular filtrate). Large molecules such as plasma proteins and blood cells are too big to cross and remain in the blood."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain the role of ADH in controlling urine volume.",
        model: "ADH (antidiuretic hormone) is released from the posterior pituitary when blood plasma is too concentrated (e.g. dehydration). ADH makes the collecting ducts more permeable to water, so more water is reabsorbed back into the blood. This produces a small volume of concentrated urine. When fluid intake is high, ADH release is suppressed, less water is reabsorbed and large volumes of dilute urine are produced."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Name three substances that should NOT normally be found in urine and explain why.",
        model: "1. Glucose: completely reabsorbed in the PCT by active transport (if present, suggests diabetes mellitus). 2. Plasma proteins: too large to pass through the glomerular filter. 3. Red blood cells: too large to filter (presence indicates kidney damage or infection)."
      },
      {
        type: "short",
        marks: 3,
        prompt: "Why is urea found in urine?",
        model: "Urea is a waste product of protein metabolism. Excess amino acids undergo deamination in the liver: the amino group is removed and converted via ammonia to less-toxic urea. Urea enters the blood, is filtered at the glomerulus and is not completely reabsorbed by the tubules, so it is excreted in urine."
      }
    ];
    c.examQuestions = [
      {
        id: "bio26-eq-1",
        source: "LC Biology Past Paper — Q6 (d)",
        parts: [
          {
            label: "6. (d)",
            question: "Give a brief biological explanation: Urine volume will be low if a person does not regularly drink fluids.",
            marks: 4,
            model: "When a person is dehydrated, the water content of the blood falls and blood solute concentration rises. The hypothalamus detects this increased osmolarity and signals the posterior pituitary gland to release ADH (antidiuretic hormone). ADH travels in the blood to the kidneys and makes the collecting ducts of the nephrons more permeable to water, causing more water to be reabsorbed back into the bloodstream. The result is a small volume of highly concentrated (dark) urine, reducing further water loss.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio27: The Digestive System ───────────────────────────────────────────
  (function () {
    var c = ch("bio27");
    // 27.1 — Digestion, absorption and the liver
    c.learningOutcomes[0].notes = [
      {
        h: "Mechanical vs Chemical Digestion",
        b: "Mechanical: physical breakdown — teeth (mouth) and churning (stomach). Chemical: enzyme breakdown — amylase (mouth), pepsin (stomach), pancreatic/intestinal enzymes (small intestine)."
      },
      {
        h: "Peristalsis",
        b: "Wave-like smooth muscle contractions propelling food along the gut. Dietary fibre adds bulk so muscles have something to push against."
      },
      {
        h: "Stomach",
        b: "HCl: kills microbes, denatures proteins, optimal pH (~2) for pepsin. Pepsin: protease that breaks proteins into polypeptides."
      },
      {
        h: "Pancreatic Enzymes",
        b: "Amylase (starch -> maltose), lipase (lipid -> fatty acids + glycerol), trypsin (peptides -> amino acids). Sodium bicarbonate neutralises acidic chyme from stomach."
      },
      {
        h: "Bile",
        b: "Made in liver from bile salts, bile pigments and cholesterol. Stored in gall bladder. Functions: emulsifies fats (increases SA for lipase), neutralises acidic chyme."
      },
      {
        h: "Liver Functions",
        b: "Makes bile (digestion). Detoxification. Glycogen storage (blood glucose regulation). Plasma protein synthesis. Deamination -> urea production."
      },
      {
        h: "Villus Adaptations",
        b: "Large surface area, one-cell-thick wall, rich capillary network (glucose/amino acids -> blood), lacteal (fats -> lymph as chylomicrons). Maximise absorption rate."
      },
      {
        h: "Hepatic Portal System",
        b: "Hepatic portal vein: nutrient-rich blood from small intestine -> liver. Hepatic artery: O2-rich blood to liver. Hepatic vein: processed blood + urea -> vena cava."
      },
      {
        h: "Deamination",
        b: "Removal of amino group from excess amino acids in the liver. Produces urea (excreted by kidneys) and a carbon residue (used for energy or stored)."
      },
      {
        h: "Large Intestine",
        b: "Reabsorbs water, stores and excretes faeces. Components: caecum, appendix, colon, rectum, anus."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is peristalsis?",
        definition: "Wave-like smooth muscle contractions that propel food along the gut. Dietary fibre adds bulk so muscles have something to push against.",
        section: "27.1"
      },
      {
        term: "What is mechanical digestion?",
        definition: "Physical breakdown of food without chemical change. Examples: teeth grinding food in the mouth; stomach churning.",
        section: "27.1"
      },
      {
        term: "What is chemical digestion?",
        definition: "Enzyme-driven breakdown of large food molecules into small absorbable units. Examples: amylase (mouth), pepsin (stomach), pancreatic enzymes (small intestine).",
        section: "27.1"
      },
      {
        term: "What is bile?",
        definition: "Made in the liver, stored in the gall bladder, released into the duodenum. Emulsifies fats (increases SA for lipase) and neutralises acidic chyme. Contains no enzymes.",
        section: "27.1"
      },
      {
        term: "What is emulsification?",
        definition: "Bile salts break large fat globules into tiny droplets, greatly increasing the surface area available for lipase to act on.",
        section: "27.1"
      },
      {
        term: "What are villus adaptations?",
        definition: "Finger-like projections in the ileum. Maximise absorption: large SA; one-cell-thick wall; rich capillary network; central lacteal for fat absorption.",
        section: "27.1"
      },
      {
        term: "What is a lacteal?",
        definition: "A lymph vessel inside each villus. Absorbs digested fats (as chylomicrons) into the lymphatic system.",
        section: "27.1"
      },
      {
        term: "What is the hepatic portal vein?",
        definition: "Carries nutrient-rich blood from the small intestine directly to the liver for processing before it reaches the general circulation.",
        section: "27.1"
      },
      {
        term: "What are the functions of the liver?",
        definition: "Makes bile; detoxifies substances; stores glycogen; synthesises plasma proteins; deaminates excess amino acids → produces urea.",
        section: "27.1"
      },
      {
        term: "What are pancreatic enzymes?",
        definition: "Amylase (starch → maltose), lipase (lipids → fatty acids + glycerol), trypsin (peptides → amino acids). Sodium bicarbonate neutralises stomach acid.",
        section: "27.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Explain the role of bile in digestion.",
        model: "Bile is produced by the liver, stored in the gall bladder and released into the duodenum. It does not contain enzymes but: (1) emulsifies fats — bile salts break large fat globules into smaller droplets, increasing surface area for lipase; (2) neutralises acidic chyme from the stomach, creating a neutral/slightly alkaline pH optimal for pancreatic enzymes."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Describe the adaptations of the villi that make them efficient at absorption.",
        model: "Villi are finger-like projections lining the ileum. They maximise absorption because: large total surface area; walls only one cell thick (minimal diffusion distance); dense capillary network for rapid uptake of glucose and amino acids; central lacteal absorbs fats as chylomicrons into the lymphatic system."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Name the three enzymes produced by the pancreas and state what each digests.",
        model: "Amylase: digests starch into maltose. Lipase: digests lipids into fatty acids and glycerol. Trypsin: digests polypeptides into amino acids."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Describe the path of a fat molecule from the duodenum to the bloodstream.",
        model: "In the duodenum, bile emulsifies fat into small droplets. Pancreatic lipase digests these into fatty acids and glycerol. They are absorbed through villus epithelium and reassembled into chylomicrons, which enter the lacteal (lymph vessel). Lymph carries them via the lymphatic system into the bloodstream through the thoracic duct."
      }
    ];
    c.examQuestions = [
      {
        id: "bio27-eq-1",
        source: "LC Biology Past Paper — Q3 (Alimentary Canal)",
        parts: [
          {
            label: "3. (a)",
            question: "The diagram shows the human alimentary canal. Name tube A, organ B and gland C, and give the function of each.",
            marks: 6,
            model: "Tube A: Oesophagus (gullet) — muscular tube transporting food (as a bolus) from the pharynx to the stomach by peristalsis. Organ B: Stomach — muscular sac where mechanical churning and chemical digestion of proteins occur (HCl + pepsin). Gland C: Pancreas — produces pancreatic juice (amylase, lipase, trypsin, NaHCO3) secreted into the duodenum.",
            diagram: "images/alimentary-canal.png"
          },
          {
            label: "3. (b)",
            question: "Give one function of tube A.",
            marks: 2,
            model: "The oesophagus transports the food bolus from the pharynx (throat) to the stomach by peristalsis — coordinated, wave-like contractions of smooth muscle that propel food downward.",
            diagram: ""
          },
          {
            label: "3. (c)",
            question: "Give one function of organ B.",
            marks: 2,
            model: "The stomach mechanically churns food and chemically digests proteins: HCl (hydrochloric acid) lowers gastric pH to approximately 2 (killing microbes and denaturing proteins) and activates pepsin, a protease that hydrolyses proteins into polypeptides.",
            diagram: ""
          },
          {
            label: "3. (d)",
            question: "Give one function of gland C in relation to the digestive system.",
            marks: 2,
            model: "The pancreas produces and secretes pancreatic juice into the duodenum via the pancreatic duct. Pancreatic juice contains: amylase (starch to maltose), lipase (fats to fatty acids + glycerol), trypsin (polypeptides to amino acids), and sodium bicarbonate (neutralises acidic chyme from the stomach).",
            diagram: ""
          },
          {
            label: "3. (e)",
            question: "State one structural feature of the small intestine that enables it to carry out its function.",
            marks: 3,
            model: "The inner lining of the small intestine is covered with villi — finger-like projections that increase the surface area for absorption. Each villus is further covered with microvilli (the brush border), further maximising surface area. Each villus has a capillary network and a lacteal for absorbing nutrients into the blood and lymph respectively.",
            diagram: ""
          },
          {
            label: "3. (f)",
            question: "Symbiotic bacteria are present in the alimentary canal. Give two functions of these symbiotic bacteria.",
            marks: 4,
            model: "1. Vitamin synthesis: gut bacteria produce Vitamin K and certain B-group vitamins that the body cannot make in sufficient quantities on its own. 2. Protection: the resident bacteria prevent harmful (pathogenic) bacteria from growing and causing infection in the gut.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio28: The Breathing System ───────────────────────────────────────────
  (function () {
    var c = ch("bio28");
    // 28.1 — Breathing mechanics, gas exchange and lung structure
    c.learningOutcomes[0].notes = [
      {
        h: "Why We Breathe",
        b: "Inhale O2 to supply aerobic respiration in cells; exhale CO2 produced by respiration. Controlled by CO2 levels detected by chemoreceptors in the medulla oblongata."
      },
      {
        h: "Airway Pathway",
        b: "Nose/mouth -> pharynx -> larynx -> trachea -> bronchi -> bronchioles -> alveoli."
      },
      {
        h: "Nose Benefits",
        b: "Warms, moistens and filters inhaled air. Mucus and hairs trap dust and microbes."
      },
      {
        h: "Epiglottis and Larynx",
        b: "Epiglottis: closes trachea during swallowing so food goes into the oesophagus. Larynx: voice box, produces sound. Cartilage rings keep airway open against pressure changes."
      },
      {
        h: "Cilia and Mucus",
        b: "Cilia line trachea/bronchi; sweep mucus + trapped particles upward to the throat to be swallowed or expelled."
      },
      {
        h: "Pleural Membranes",
        b: "Two thin layers surrounding each lung with fluid between them. Reduce friction during breathing; keep lungs attached to thoracic wall."
      },
      {
        h: "Alveoli Adaptations",
        b: "Very large total surface area. Walls one cell thick. Rich capillary network. Moist surface. All maximise O2/CO2 diffusion rate."
      },
      {
        h: "What happens during inhalation?",
        b: "Diaphragm contracts (flattens) + external intercostal muscles contract (ribs up/out) -> thorax volume increases -> pressure drops -> air flows in. Requires ATP."
      },
      {
        h: "What happens during exhalation at rest?",
        b: "Diaphragm relaxes (domes up) + intercostal muscles relax (ribs fall) -> thorax volume decreases -> pressure rises -> air flows out. Elastic recoil — no ATP needed at rest."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What are alveoli?",
        definition: "Tiny air sacs at the end of bronchioles. Adaptations: huge total surface area; one-cell-thick walls; rich capillary network; moist surface — all maximise gas exchange.",
        section: "28.1"
      },
      {
        term: "What is inhalation (active)?",
        definition: "Diaphragm contracts (flattens) + external intercostal muscles contract (ribs up/out) → thorax volume increases → pressure drops → air flows in. Requires ATP.",
        section: "28.1"
      },
      {
        term: "What is exhalation (passive)?",
        definition: "Diaphragm and intercostal muscles relax → thorax volume decreases → pressure rises → air flows out. Elastic recoil — no ATP needed at rest.",
        section: "28.1"
      },
      {
        term: "What is the epiglottis?",
        definition: "A flap of cartilage that closes over the trachea during swallowing, directing food into the oesophagus and preventing choking.",
        section: "28.1"
      },
      {
        term: "What are cilia and mucus?",
        definition: "Cilia line the trachea and bronchi; sweep mucus containing trapped dust and microbes upward to the throat to be swallowed or expelled.",
        section: "28.1"
      },
      {
        term: "What are the pleural membranes?",
        definition: "Two thin membranes surrounding each lung with fluid between them. Reduce friction during breathing and keep lungs attached to the thoracic wall.",
        section: "28.1"
      },
      {
        term: "What is the airway pathway?",
        definition: "Nose/mouth → pharynx → larynx → trachea → bronchi → bronchioles → alveoli.",
        section: "28.1"
      },
      {
        term: "How is breathing controlled?",
        definition: "Controlled by CO2 levels detected by chemoreceptors in the medulla oblongata. Rising CO2 triggers increased breathing rate.",
        section: "28.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Describe the mechanism of inhalation.",
        model: "The diaphragm contracts and flattens. The external intercostal muscles contract, pulling the ribs up and outward. These actions increase the volume of the thoracic cavity. As volume increases, pressure inside the lungs drops below atmospheric pressure, so air flows in. Inhalation is an active process requiring ATP for muscle contraction."
      },
      {
        type: "short",
        marks: 4,
        prompt: "List four adaptations of the alveoli for efficient gas exchange.",
        model: "1. Enormous total surface area to maximise diffusion area. 2. Walls only one cell thick to minimise diffusion distance. 3. Rich capillary network maintains a steep concentration gradient. 4. Moist surface allows gases to dissolve before diffusing through."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain why exhalation at rest is described as passive.",
        model: "At rest, exhalation occurs by elastic recoil — as the diaphragm and intercostal muscles relax, the elastic lung tissue springs back to its resting volume. This decreases thoracic volume and raises internal pressure above atmospheric, pushing air out. No muscle contraction is required so no ATP is used."
      },
      {
        type: "short",
        marks: 3,
        prompt: "What is the role of the epiglottis and the cilia?",
        model: "The epiglottis is a flap of cartilage that closes over the trachea during swallowing, directing food into the oesophagus and preventing choking. Cilia are tiny hair-like structures lining the trachea and bronchi; they beat in coordinated waves to sweep mucus containing trapped dust and microbes upward to the throat."
      }
    ];
  })();

  // ── bio29: The Circulatory System and Blood ───────────────────────────────
  (function () {
    var c = ch("bio29");
    // 29.1 — Heart, blood vessels, blood and circulation
    c.learningOutcomes[0].notes = [
      {
        h: "What are the different types of blood vessels?",
        b: "Arteries: away from heart, high pressure, thick walls, no valves. Veins: to heart, low pressure, valves prevent backflow. Capillaries: one cell thick, site of exchange. Arterioles/venules connect them."
      },
      {
        h: "What are the layers of blood vessel walls?",
        b: "Tunica externa (fibrous outer), tunica media (smooth muscle + elastic fibres — vasoconstriction/dilation), tunica intima (smooth inner lining). Lumen = hollow centre."
      },
      {
        h: "What is the structure of the heart?",
        b: "In thoracic cavity, behind sternum. Pericardium: protective membrane + fluid to reduce friction. Atria (upper, receive blood), ventricles (lower, pump blood out)."
      },
      {
        h: "What are the heart valves and their functions?",
        b: "Tricuspid (right AV, 3 flaps), bicuspid/mitral (left AV, 2 flaps), semilunar valves (at exits of both ventricles). Prevent backflow. Lub = AV valves closing; dub = semilunar valves closing."
      },
      {
        h: "What is the path of blood flow through the heart?",
        b: "Deoxygenated: vena cava -> right atrium -> tricuspid -> right ventricle -> pulmonary artery -> lungs. Oxygenated: pulmonary vein -> left atrium -> bicuspid -> left ventricle -> aorta -> body."
      },
      {
        h: "What are the benefits of double circulation?",
        b: "Blood reaches body at high pressure. Oxygenated and deoxygenated blood never mix. More efficient delivery to active tissues."
      },
      {
        h: "What is the role of the SA node and AV node?",
        b: "SA node: pacemaker in right atrium wall, triggers atrial contraction. AV node: delays and relays impulse to ventricles -> ventricular contraction."
      },
      {
        h: "What are the components of blood?",
        b: "Plasma (~90% water, dissolved proteins/hormones/gases/nutrients), red blood cells (haemoglobin), white blood cells (phagocytes + lymphocytes), platelets (clotting)."
      },
      {
        h: "What is the structure and function of red blood cells?",
        b: "Produced in red bone marrow. No nucleus or mitochondria (maximises haemoglobin). Haemoglobin + O2 -> oxyhaemoglobin in lungs; O2 released in tissues."
      },
      {
        h: "What are blood groups and how does blood clotting work?",
        b: "ABO system (A, B, AB, O). Incompatible blood -> agglutination (fatal). Rhesus factor: Rh+ has the protein; Rh- does not. Platelets -> clotting factors -> fibrin mesh seals wounds."
      },
      {
        h: "What is coronary heart disease?",
        b: "Coronary arteries supply heart muscle. Blockage -> angina or heart attack. Treatments: stent (keep artery open) or coronary bypass (graft around blockage)."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is an artery?",
        definition: "Blood vessel carrying blood AWAY from the heart at high pressure. Thick, muscular, elastic walls; no valves.",
        section: "29.1"
      },
      {
        term: "What is a vein?",
        definition: "Blood vessel carrying blood TOWARDS the heart at low pressure. Thin walls; valves prevent backflow.",
        section: "29.1"
      },
      {
        term: "What is a capillary?",
        definition: "Smallest blood vessel; wall is one cell thick. Site of exchange of gases, nutrients and wastes between blood and tissues.",
        section: "29.1"
      },
      {
        term: "What are heart valves?",
        definition: "Tricuspid (right AV), bicuspid/mitral (left AV), semilunar valves (at exits of ventricles). All prevent backflow of blood. 'Lub' = AV valves closing; 'dub' = semilunar closing.",
        section: "29.1"
      },
      {
        term: "What is double circulation?",
        definition: "The human circulatory system has two loops: pulmonary (heart → lungs → heart) and systemic (heart → body → heart). Keeps oxygenated and deoxygenated blood separate.",
        section: "29.1"
      },
      {
        term: "What is the SA node (pacemaker)?",
        definition: "Sinoatrial node in the right atrium wall. Generates the electrical impulse that triggers atrial contraction and sets the heart rate (~60–80 bpm at rest).",
        section: "29.1"
      },
      {
        term: "What is the AV node?",
        definition: "Atrioventricular node — receives the impulse from the SA node, delays it, then relays it to the ventricles, triggering ventricular contraction.",
        section: "29.1"
      },
      {
        term: "What is haemoglobin?",
        definition: "Iron-containing protein in red blood cells. Binds O2 in the lungs (→ oxyhaemoglobin) and releases it in respiring tissues.",
        section: "29.1"
      },
      {
        term: "What are red blood cells?",
        definition: "Produced in red bone marrow; no nucleus or mitochondria (maximises haemoglobin). Biconcave shape increases surface area for gas exchange.",
        section: "29.1"
      },
      {
        term: "What are ABO blood groups?",
        definition: "Determined by antigens on red blood cells. Incompatible transfusion causes agglutination (clumping) which can block vessels and be fatal.",
        section: "29.1"
      },
      {
        term: "What is coronary heart disease?",
        definition: "Narrowing/blockage of coronary arteries (which supply heart muscle) → angina or heart attack. Treated by stent or coronary bypass surgery.",
        section: "29.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Trace the path of a deoxygenated red blood cell from the vena cava to the aorta.",
        model: "Vena cava -> right atrium -> tricuspid valve -> right ventricle -> pulmonary semilunar valve -> pulmonary artery -> lungs (oxygenated) -> pulmonary vein -> left atrium -> bicuspid (mitral) valve -> left ventricle -> aortic semilunar valve -> aorta."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain why the left ventricle has a thicker wall than the right ventricle.",
        model: "The left ventricle pumps oxygenated blood through the aorta to the entire body (systemic circuit), requiring much higher pressure to overcome the resistance of the long circuit. The right ventricle only pumps to the nearby lungs (pulmonary circuit), which has lower resistance. The left ventricular wall is therefore thicker with more muscle to generate the greater force needed."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Describe the role of haemoglobin in oxygen transport.",
        model: "Haemoglobin is an iron-containing globular protein in red blood cells. In the lungs (high O2 partial pressure) it binds up to four O2 molecules to form oxyhaemoglobin. In respiring tissues (low O2) oxyhaemoglobin dissociates and releases O2 to cells. RBCs lack a nucleus and mitochondria to maximise haemoglobin space and avoid consuming the O2 they transport."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain the ABO blood group system and why compatibility matters for transfusions.",
        model: "ABO groups (A, B, AB, O) are determined by antigens on red blood cells and antibodies in plasma. Transfusing incompatible blood causes the recipient's antibodies to attack donor RBCs, causing agglutination (clumping) which can block vessels and be fatal. Blood must be matched before transfusion."
      }
    ];
    c.examQuestions = [
      {
        id: "bio29-eq-1",
        source: "LC Biology Past Paper — Q6(e)",
        parts: [
          {
            label: "6. (e)",
            question: "Distinguish clearly between systole and diastole.",
            marks: 6,
            model: "Systole: the phase of the cardiac cycle during which the heart muscle contracts. Ventricular systole forces blood out of the ventricles — from the right ventricle into the pulmonary artery and from the left ventricle into the aorta. Diastole: the phase during which the heart muscle relaxes and the chambers refill with blood. The atria and ventricles fill during diastole. The two phases alternate continuously to produce each heartbeat.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio29-eq-2",
        source: "LC Biology Past Paper — Q6 (g)",
        parts: [
          {
            label: "6. (g)",
            question: "Give a brief biological explanation: The septum separates the two sides of the human heart.",
            marks: 4,
            model: "The septum is a thick muscular wall of cardiac tissue that divides the heart vertically into a right side and a left side. The right side receives deoxygenated blood returning from the body (via the vena cava) and pumps it to the lungs (pulmonary circuit). The left side receives oxygenated blood from the lungs (via pulmonary veins) and pumps it to the body (systemic circuit). The septum ensures that oxygenated and deoxygenated blood never mix, maintaining the efficiency of double circulation.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio29-eq-3",
        source: "LC Biology Past Paper — Q10 (b) (ii) (Heart Dissection)",
        parts: [
          {
            label: "10. (b) (ii) 1.",
            question: "Name one instrument you used to make incisions when dissecting an ox/sheep heart.",
            marks: 2,
            model: "Scalpel (or dissection scissors). A scalpel is used to make precise incisions through the muscular walls of the heart to expose the internal chambers, valves and septum.",
            diagram: ""
          },
          {
            label: "10. (b) (ii) 2.",
            question: "Describe one difference between the walls of the right and left ventricles.",
            marks: 3,
            model: "The wall of the left ventricle is significantly thicker (approximately 3 times) than the wall of the right ventricle. This is because the left ventricle must generate much higher pressure to pump oxygenated blood through the aorta to the entire body (systemic circuit, high resistance). The right ventricle only needs to pump deoxygenated blood to the nearby lungs (pulmonary circuit, low resistance) and therefore requires less muscular force.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio30: Transport in Plants ────────────────────────────────────────────
  (function () {
    var c = ch("bio30");
    // 30.1 — Xylem, phloem, transpiration and mineral uptake
    c.learningOutcomes[0].notes = [
      {
        h: "What are the types of plant tissues?",
        b: "Dermal: outer covering, protection/gas exchange (epidermis, cuticle). Vascular: transports water, minerals, sugars (xylem + phloem). Ground: bulk tissue — storage, support, photosynthesis."
      },
      {
        h: "What is xylem and what does it do?",
        b: "Dead hollow tubes (tracheids + vessels) with lignified walls. Carries water + minerals upward from roots. Lignin provides strength; no cross-walls allow continuous flow; narrow tubes enable capillary action."
      },
      {
        h: "What is phloem and what does it do?",
        b: "Living sieve tube elements (no nucleus) with sieve plates. Companion cells alongside provide energy via plasmodesmata. Transports dissolved sugars (sucrose) in both directions (translocation)."
      },
      {
        h: "What is the difference between xylem and phloem?",
        b: "Xylem: dead cells, one direction (up), water + minerals. Phloem: living cells, both directions, dissolved sugars."
      },
      {
        h: "What is the structure and function of root hair cells?",
        b: "High solute concentration so water enters from soil by osmosis. Minerals absorbed by active transport (ATP needed). Long extensions maximise surface area."
      },
      {
        h: "What is the path of water through a plant?",
        b: "Soil -> root hair -> cortex -> endodermis -> xylem -> stem xylem -> leaf xylem -> mesophyll cells -> evaporates through stomata (transpiration)."
      },
      {
        h: "What is the cohesion-tension model?",
        b: "Water molecules hydrogen-bond to each other (cohesion) and to xylem walls (adhesion). Transpiration creates tension (pull) at the top. Cohesion + tension draws a continuous water column up from roots."
      },
      {
        h: "What factors affect the rate of transpiration?",
        b: "More transpiration with: higher light (stomata open more), higher temperature (faster evaporation), lower humidity (steeper gradient), higher wind (removes water vapour). Measured with a potometer."
      },
      {
        h: "How do guard cells regulate stomatal opening?",
        b: "Guard cells regulate stomata. Turgid -> stomate opens (light, low CO2). Flaccid -> stomate closes. High CO2 inside -> close; low CO2 -> open."
      },
      {
        h: "What adaptations reduce water loss in plants?",
        b: "Waxy cuticle. Stomata mainly on lower leaf surface. Sunken stomata (xerophytes). Rolled/hairy leaves. Thick cell walls."
      },
      {
        h: "What are the essential minerals needed by plants?",
        b: "Nitrogen (proteins, chlorophyll), phosphorus (DNA, ATP, membranes), potassium (enzyme activation, stomata), magnesium (chlorophyll), calcium (cell walls). Absorbed by active transport in root hairs."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is xylem?",
        definition: "Dead hollow tubes with lignified walls. Transports water and dissolved minerals upward from roots. Narrow tubes enable capillary action; provides structural support.",
        section: "30.1"
      },
      {
        term: "What is phloem?",
        definition: "Living sieve tube elements with companion cells. Transports dissolved sugars (sucrose) in both directions (translocation) from leaves to all parts of the plant.",
        section: "30.1"
      },
      {
        term: "What is transpiration?",
        definition: "The evaporation of water from leaves through stomata. Creates the tension that pulls water up through the xylem (cohesion-tension model).",
        section: "30.1"
      },
      {
        term: "What is the cohesion-tension model?",
        definition: "Water molecules hydrogen-bond to each other (cohesion) and to xylem walls (adhesion). Transpiration creates tension at the top, pulling a continuous water column up from roots.",
        section: "30.1"
      },
      {
        term: "What are guard cells?",
        definition: "Regulate stomatal opening. When turgid (K⁺ absorbed → water enters by osmosis) → stomate opens. When flaccid → stomate closes, reducing water loss.",
        section: "30.1"
      },
      {
        term: "What are root hair cells?",
        definition: "Have a high solute concentration, so water enters from soil by osmosis. Minerals absorbed by active transport (ATP needed). Long extensions maximise surface area.",
        section: "30.1"
      },
      {
        term: "What factors affect transpiration?",
        definition: "Transpiration increases with: higher light (stomata open), higher temperature (faster evaporation), lower humidity (steeper gradient), higher wind (removes vapour).",
        section: "30.1"
      },
      {
        term: "What is a potometer?",
        definition: "Apparatus used to measure transpiration rate by tracking the movement of an air bubble in a capillary tube as water is taken up by a shoot.",
        section: "30.1"
      },
      {
        term: "What are essential minerals?",
        definition: "Nitrogen (proteins/chlorophyll), phosphorus (DNA/ATP), potassium (enzyme activation/stomata), magnesium (chlorophyll), calcium (cell walls). Absorbed by active transport in root hairs.",
        section: "30.1"
      },
      {
        term: "What is translocation?",
        definition: "The transport of dissolved organic compounds (mainly sucrose) through phloem from source (leaves) to sink (roots, fruits, growing regions).",
        section: "30.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Compare xylem and phloem.",
        model: "Xylem: dead, hollow cells with lignified walls; transports water and dissolved minerals upward only from roots to leaves; provides structural support. Phloem: living sieve tube elements with companion cells; transports dissolved sugars (sucrose) in both directions from leaves to all parts of the plant (translocation)."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain the cohesion-tension model of water transport.",
        model: "As water evaporates through stomata (transpiration), it creates tension (a pulling force) at the top of the xylem column. Water molecules are held together by hydrogen bonds (cohesion) and also adhere to xylem walls. This combination pulls a continuous column of water up from the roots to replace what is lost, without the plant expending ATP."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Describe how a potometer is used to measure the effect of humidity on transpiration.",
        model: "Set up a leafy shoot in a water-filled potometer in a sealed system. Mark the position of an air bubble in the capillary tube. In high humidity, record the bubble movement per minute (low = low transpiration rate). Move to low humidity and repeat. The bubble moves faster in low humidity because the water-vapour gradient between leaf and air is steeper, driving faster evaporation."
      },
      {
        type: "short",
        marks: 4,
        prompt: "How do guard cells regulate stomatal opening?",
        model: "In light (and when CO2 is low), guard cells absorb K+ ions by active transport, lowering their water potential. Water enters by osmosis making them turgid; their curved shape causes them to bow outward, opening the stoma. In darkness or high CO2 or drought, K+ leaves, guard cells become flaccid and the stoma closes, reducing water loss."
      }
    ];
    c.examQuestions = [
      {
        id: "bio30-eq-1",
        source: "LC Biology Past Paper — Q2 (Plant Root Section)",
        parts: [
          {
            label: "2. (a)",
            question: "The diagram shows a longitudinal section through the root of a plant. Name the structure indicated by letter X and give its function.",
            marks: 4,
            model: "X: Root cap (calyptra). Function: Protects the root apical meristem (the zone of actively dividing cells at the root tip) from mechanical damage as the root pushes through the soil. The outermost cells are continuously shed and replaced.",
            diagram: "images/root.png"
          },
          {
            label: "2. (b)",
            question: "Name the tissue type indicated by letter Y and give its function.",
            marks: 4,
            model: "Y: Vascular tissue (xylem and phloem forming the central vascular cylinder). Function: Xylem transports water and dissolved mineral ions from roots upward to shoots and leaves. Phloem transports dissolved sugars (sucrose, products of photosynthesis) from leaves to all living regions of the plant.",
            diagram: "images/root.png"
          },
          {
            label: "2. (c)",
            question: "Name the tissue indicated by letter Z where rapid mitosis is occurring.",
            marks: 2,
            model: "Meristematic tissue (root apical meristem / zone of cell division). These are undifferentiated cells that divide rapidly by mitosis, producing new cells that elongate and differentiate into the various root tissues.",
            diagram: "images/root.png"
          },
          {
            label: "2. (d)",
            question: "Draw and label a transverse section of the root as it would appear if cut at the position of the dashed line.",
            marks: 5,
            model: "Sketch should show (from outside inward): Epidermis (outermost single layer, some cells extended as root hairs), Cortex (wide zone of large thin-walled parenchyma cells, used for storage), Endodermis (single layer with Casparian strip), Pericycle, and central Vascular cylinder with Xylem (X-shaped, thick walls) in the centre and Phloem located between the arms of the xylem. Label all tissues.",
            diagram: "images/root.png"
          }
        ]
      },
      {
        id: "bio30-eq-2",
        source: "LC Biology Past Paper — Q4 (Xylem and Phloem)",
        parts: [
          {
            label: "4. (a)",
            question: "The diagram shows a longitudinal view of xylem vessels and phloem. Label any one structure on the diagram.",
            marks: 2,
            model: "Label either: Xylem vessel — dead, hollow, lignified tube transporting water upward. Phloem sieve tube — living cell with sieve plates transporting sugars. Companion cell — living cell alongside phloem sieve tube, providing metabolic support.",
            diagram: "images/xylem-phloem.png"
          },
          {
            label: "4. (b)",
            question: "To which type of plant tissue do xylem and phloem belong?",
            marks: 2,
            model: "Vascular tissue (vascular bundle). This is one of the three fundamental plant tissue systems, alongside dermal tissue and ground tissue.",
            diagram: ""
          },
          {
            label: "4. (c)",
            question: "Give one function of xylem.",
            marks: 2,
            model: "Xylem transports water and dissolved mineral salts (e.g. nitrates, phosphates, potassium) from the roots upward to the leaves and all aerial parts of the plant.",
            diagram: ""
          },
          {
            label: "4. (d)",
            question: "Give one function of phloem.",
            marks: 2,
            model: "Phloem transports dissolved organic substances — principally sucrose produced by photosynthesis in the leaves — bidirectionally to all living parts of the plant that need energy and building materials (a process called translocation).",
            diagram: ""
          },
          {
            label: "4. (e) (i)",
            question: "The image shows the arrangement of xylem and phloem in a transverse section of a stem. Is this stem from a monocot or a dicot? Justify your answer.",
            marks: 4,
            model: "This is a monocot stem. In monocotyledonous plants (e.g. maize, grass), vascular bundles are scattered irregularly throughout the ground tissue. In dicotyledonous plants (e.g. sunflower, bean), vascular bundles are arranged in a ring near the periphery of the stem. The scattered pattern of bundles in the image is characteristic of a monocot.",
            diagram: ""
          },
          {
            label: "4. (f)",
            question: "State the location of the tissue containing xylem and phloem in a transverse section of a root.",
            marks: 2,
            model: "In the centre of the root, forming the central vascular cylinder (stele). The xylem forms a star/X-shape at the very centre with phloem bundles positioned between the xylem arms. This is surrounded by the pericycle and endodermis.",
            diagram: ""
          }
        ]
      },
      {
        id: "bio30-eq-3",
        source: "LC Biology Past Paper — Q10 (b) (iv) (Dicot Stem Section)",
        parts: [
          {
            label: "10. (b) (iv) 1.",
            question: "Explain the importance of the section being thin when viewing a transverse section of a dicot stem under the light microscope.",
            marks: 3,
            model: "A thin section allows sufficient light to pass through the specimen so that a clear image can be formed. If the section were too thick, insufficient light would reach the eyepiece, the image would be too dark to observe detail, and overlapping tissue layers would make identification of individual tissue types impossible.",
            diagram: ""
          },
          {
            label: "10. (b) (iv) 2.",
            question: "Sketch what you observed under the light microscope when viewing a transverse section of a dicot stem.",
            marks: 5,
            model: "Sketch (from outside to centre): 1. Epidermis — single outer ring of cells. 2. Cortex — several layers of larger, thin-walled cells (may include collenchyma). 3. Vascular bundles arranged in a ring near the periphery: each bundle has Phloem (outer, smaller living cells) and Xylem (inner, large dead cells with thick walls). 4. Pith — large thin-walled parenchyma cells filling the centre. Label: epidermis, cortex, phloem, xylem, pith.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── bio31: Ecology, Ecosystems and Biodiversity ───────────────────────────
  (function () {
    var c = ch("bio31");
    // 31.1 — The structure of ecosystems, the meaning of biodiversity, and how energy and populations are managed within ecological systems
    c.learningOutcomes[0].notes = [
      {
        h: "Ecology and the Biosphere",
        b: "Ecology is the study of the interactions between living organisms and between organisms and their environment. The biosphere is the part of the planet where life can exist, encompassing all ecosystems."
      },
      {
        h: "Ecosystems, Populations and Communities",
        b: "An ecosystem is a group of clearly distinguished organisms that interact with their environment as a unit; examples include woodlands, grasslands, bogs, lakes, sand dunes, salt-marshes, rocky seashores and hedgerows. A population is all members of the same species in an area, while a community is all the different populations together."
      },
      {
        h: "Biodiversity and Its Three Levels",
        b: "Biodiversity is the variety of life in a specific area. It operates at three levels: species diversity (number and variety of species), genetic diversity (variety of genes within a species) and ecosystem diversity (variety of ecosystems in a region)."
      },
      {
        h: "Causes of Biodiversity Loss",
        b: "The main drivers of biodiversity loss are changes in land use that destroy habitats, overexploitation of species, pollution, climate change and the introduction of invasive species."
      },
      {
        h: "Impacts of Biodiversity Loss",
        b: "Biodiversity loss has environmental impacts (ecosystem disruption, increased extinctions, reduced resilience), economic impacts (loss of crop yields, fish stocks and new medicines), social impacts (reduced quality of life and health risks) and cultural impacts (loss of connection to traditional knowledge, folklore and land)."
      },
      {
        h: "Conservation",
        b: "Conservation is the wise management, preservation or protection of the environment to maintain biodiversity and prevent extinction. Its benefits include limiting biodiversity loss, preserving useful organisms, maintaining the balance of nature and providing enjoyable natural spaces."
      },
      {
        h: "Carrying Capacity and Limiting Factors",
        b: "The carrying capacity of an ecosystem is the maximum population size that can be supported by available resources. It is determined by abiotic limiting factors (water, oxygen, space, temperature, soil) and biotic limiting factors (food, disease, competition and predation)."
      },
      {
        h: "Niche and Species Interactions",
        b: "The niche is the functional role of an organism in its ecosystem. Two species with identical niches cannot coexist long-term because they compete for the same resources. Introducing exotic species can be harmful (increasing competition or predation) or beneficial (providing food, shelter or pest control)."
      },
      {
        h: "Species Diversity Index (Simpson's Ds)",
        b: "A species diversity index is a mathematical measure of biodiversity using species richness (number of different species) and relative abundance (proportion each species represents). Simpson's index Ds = 1 − (Σn(n−1) / N(N−1)), where n is the count of each species and N is the total count of all organisms; values range from 0 (no diversity) to 1 (infinite diversity)."
      },
      {
        h: "Population Curves",
        b: "A J-shaped (exponential) population curve occurs when resources are unlimited and each generation adds more individuals than the last. An S-shaped curve occurs when resources are limited, causing growth to slow as the population approaches carrying capacity."
      },
      {
        h: "Energy Flow and Feeding Relationships",
        b: "The sun is the primary energy source. Energy flows through an ecosystem but only about 10% is passed to the next trophic level; the rest is lost as heat or used in life processes. Matter and nutrients, unlike energy, are recycled within ecosystems."
      },
      {
        h: "Food Chains, Webs and Trophic Levels",
        b: "A food chain shows the transfer of energy from producers to primary, secondary and tertiary consumers. A food web consists of two or more interlinked food chains. Omnivores eat both plants and animals; top consumers have no predators feeding on them."
      },
      {
        h: "Ecological Pyramids",
        b: "A pyramid of numbers shows the number of organisms at each trophic level and can be upright, inverted or spindle-shaped. A pyramid of biomass shows the total mass at each level and is typically upright but can be inverted in aquatic systems where producers reproduce rapidly."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is ecology?",
        definition: "The study of interactions between living organisms and between organisms and their environment.",
        section: "31.1"
      },
      {
        term: "What is an ecosystem?",
        definition: "A group of clearly distinguished organisms that interact with their environment as a unit (e.g. woodland, grassland, bog).",
        section: "31.1"
      },
      {
        term: "What is biodiversity?",
        definition: "The variety of life in a specific area, measured at the levels of species diversity, genetic diversity and ecosystem diversity.",
        section: "31.1"
      },
      {
        term: "What is carrying capacity?",
        definition: "The maximum population size an ecosystem can support given the available abiotic and biotic resources.",
        section: "31.1"
      },
      {
        term: "What is an ecological niche?",
        definition: "The functional role an organism plays within its ecosystem, including how it obtains food and interacts with other species.",
        section: "31.1"
      },
      {
        term: "What is Simpson's Diversity Index (Ds)?",
        definition: "A mathematical measure of biodiversity calculated as Ds = 1 − (Σn(n−1) / N(N−1)); values range from 0 (no diversity) to 1 (maximum diversity).",
        section: "31.1"
      },
      {
        term: "What is a trophic level?",
        definition: "A feeding stage in a food chain; producers occupy the first level, followed by primary, secondary and tertiary consumers.",
        section: "31.1"
      },
      {
        term: "What is biomass?",
        definition: "The total mass of all organisms at a given trophic level in a food chain or ecosystem.",
        section: "31.1"
      },
      {
        term: "What is a J-shaped population curve?",
        definition: "A pattern of exponential population growth seen when resources are unlimited, with each generation adding more individuals than the last.",
        section: "31.1"
      },
      {
        term: "What is an S-shaped population curve?",
        definition: "A pattern of logistic population growth seen when resources are limited; growth slows as the population approaches carrying capacity.",
        section: "31.1"
      },
      {
        term: "What is conservation?",
        definition: "The wise management, preservation or protection of the environment to maintain biodiversity and prevent extinction.",
        section: "31.1"
      }
    ];
  })();

  // ── bio32: Investigating an Ecosystem ─────────────────────────────────────
  (function () {
    var c = ch("bio32");
    // 32.1 — The practical methods used to collect, identify and quantify organisms in a grassland ecosystem, and the abiotic and biotic factors that shape it
    c.learningOutcomes[0].notes = [
      {
        h: "Grassland Organisms",
        b: "The defining plants of a grassland are grasses, often grown alongside clover (which hosts nitrogen-fixing bacteria). Other flora includes buttercups, dandelions, daisies, nettles, poppies and thistles. Fauna ranges from earthworms, snails and beetles in the soil to aphids and caterpillars on leaves, bees and butterflies on flowers, and larger animals such as rabbits, foxes and hawks."
      },
      {
        h: "Adaptations",
        b: "An adaptation is an alteration that improves an organism's chances of survival and reproduction. Adaptations may be structural (physical features), behavioural (actions or responses) or competitive (traits that improve success in competition for resources)."
      },
      {
        h: "Qualitative vs. Quantitative Study",
        b: "A qualitative study simply records the presence or absence of organisms in a habitat. A quantitative study records the actual numbers present, providing far more detail about abundance and distribution."
      },
      {
        h: "Animal Collection Devices",
        b: "A pooter sucks insects and spiders into a jar; a beating tray collects insects, spiders and caterpillars shaken from vegetation; a pitfall trap (set flush in soil) catches crawling insects, snails and slugs; a sweep net collects flying insects from grass; a plankton net gathers plankton from water."
      },
      {
        h: "Further Collection Devices",
        b: "A Tullgren funnel uses heat from a bulb to drive centipedes, millipedes and small insects from leaf litter downwards into a collecting jar. A Baermann funnel uses heat to move water snails and worms out of wet soil. A mammal trap uses bait and a trigger door to catch shrews or mice unharmed. A cryptozoic trap (a flat board on soil) attracts slugs, snails, worms and woodlice that prefer dark, moist conditions."
      },
      {
        h: "Identifying Organisms",
        b: "A key is a tool for naming organisms by working through a series of questions with alternative answers. A dichotomous key divides organisms into two groups at each step and is a common identification method in ecosystem studies."
      },
      {
        h: "Abiotic Factors",
        b: "Abiotic factors are non-living environmental factors. In air these include temperature, rainfall, day length, light intensity and wind speed. Ground factors include altitude, aspect (direction habitat faces), slope and space. Aquatic factors include light, currents, wave action, salt content and oxygen concentration. Edaphic (soil) factors include pH, soil type, humus content, and water, air and mineral content."
      },
      {
        h: "Random Sampling with Quadrats",
        b: "To ensure random sampling, an object is thrown over the shoulder and a quadrat is placed where it lands. Percentage cover (proportion of quadrat ground covered by a species) and percentage frequency (chance of finding a species in any single quadrat placement) are both recorded. The procedure is repeated at least 10 times to ensure reliability."
      },
      {
        h: "Transects (Non-random Method)",
        b: "A line transect records all species touching a marked line, sampling a narrow strip of habitat. A belt transect places a quadrat along the line for more detailed sampling and is better for showing how species distribution changes across an environmental gradient."
      },
      {
        h: "Capture–Recapture Method",
        b: "This method estimates the population size of mobile animals. A sample is caught, marked (tagged or ringed without causing harm) and released. On a second visit some days later, a new sample is caught and the number of marked individuals counted. Population size = (number caught and marked on first visit × number caught on second visit) ÷ number marked on second visit."
      },
      {
        h: "Biotic Factors: Predation and Competition",
        b: "Biotic factors are living influences within an ecosystem. Predation (e.g. blackbirds eating earthworms) regulates prey populations and can be used in biological pest control. Intra-specific competition occurs between members of the same species; inter-specific competition occurs between different species. Contest competition gives all the resource to one individual; scramble competition shares the resource among all competitors."
      },
      {
        h: "Symbiosis",
        b: "Symbiosis is a close association between two different species in which at least one benefits. Mutualism benefits both (e.g. nitrogen-fixing bacteria in clover roots). Commensalism benefits one without affecting the other (e.g. birds nesting in trees). Parasitism benefits the parasite but harms the host (e.g. fleas on a dog, tapeworms in humans)."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is an adaptation?",
        definition: "A structural, behavioural or competitive alteration that improves an organism's chances of survival and reproduction in its habitat.",
        section: "32.1"
      },
      {
        term: "What is a quadrat?",
        definition: "A square frame placed randomly in a habitat to sample the number or cover of species within it.",
        section: "32.1"
      },
      {
        term: "What is percentage cover?",
        definition: "An estimate of the proportion of ground within a quadrat that is covered by a named species, expressed as a percentage.",
        section: "32.1"
      },
      {
        term: "What is percentage frequency?",
        definition: "The probability of finding a named species in any single random placement of a quadrat, calculated as (quadrats containing species ÷ total quadrats) × 100.",
        section: "32.1"
      },
      {
        term: "What is a transect?",
        definition: "A line used for non-random sampling. A line transect records species touching the line; a belt transect places quadrats along the line for more detailed data.",
        section: "32.1"
      },
      {
        term: "What is capture–recapture?",
        definition: "A method for estimating the population size of mobile animals by marking and releasing individuals, then recapturing a second sample and counting the marked proportion.",
        section: "32.1"
      },
      {
        term: "What are abiotic factors?",
        definition: "Non-living factors in an ecosystem such as temperature, light, pH, rainfall and soil composition that influence organism distribution and growth.",
        section: "32.1"
      },
      {
        term: "What are edaphic factors?",
        definition: "Soil-related abiotic factors including pH, soil type, humus content, and water, air and mineral content.",
        section: "32.1"
      },
      {
        term: "What is intra-specific competition?",
        definition: "Competition for resources between members of the same species (e.g. dandelions competing for space).",
        section: "32.1"
      },
      {
        term: "What is inter-specific competition?",
        definition: "Competition for resources between members of different species (e.g. blackbirds and thrushes competing for insects).",
        section: "32.1"
      },
      {
        term: "What is symbiosis?",
        definition: "A close association between two different species in which at least one benefits; includes mutualism, commensalism and parasitism.",
        section: "32.1"
      },
      {
        term: "What is a pitfall trap?",
        definition: "A collecting device set flush with the soil surface used to capture crawling invertebrates such as insects, snails and slugs.",
        section: "32.1"
      }
    ];
  })();

  // ── bio33: Microorganisms ─────────────────────────────────────────────────
  (function () {
    var c = ch("bio33");
    // 33.1 — The characteristics, nutrition, growth and industrial importance of bacteria and fungi, and the role of the human microbiome
    c.learningOutcomes[0].notes = [
      {
        h: "Types of Microorganisms",
        b: "Microorganisms are living things too small to be seen individually without a microscope. They include bacteria, fungi, archaea and protists such as plankton."
      },
      {
        h: "Bacterial Structure",
        b: "Bacteria belong to the Monera kingdom and are prokaryotic, meaning they have no nucleus or membrane-enclosed organelles. Key structures include a cell wall (prevents bursting in dilute solutions), a cell membrane, a protective capsule, a single chromosome, plasmids (small DNA loops carrying genes for antibiotic resistance), cytoplasm with ribosomes, and flagella for movement."
      },
      {
        h: "Bacterial Nutrition",
        b: "Bacteria feed in four ways grouped as autotrophic or heterotrophic. Photosynthetic bacteria (e.g. purple sulfur bacteria) use light to make food; chemosynthetic bacteria (e.g. nitrifying bacteria) use energy from chemical reactions. Heterotrophic bacteria are either saprophytes (absorb food from dead organic matter) or parasites (live in a host causing harm, e.g. TB and cholera)."
      },
      {
        h: "Fungal Structure (Rhizopus)",
        b: "Fungi are eukaryotic. Rhizopus is composed of hyphae — thread-like tubes with cell walls made of chitin. A visible mass of hyphae is called a mycelium. Rhizoids grow into the substrate to absorb nutrients; stolons are aerial hyphae for rapid spreading; sporangiophores are upright hyphae that support sporangia, which produce haploid spores for asexual reproduction."
      },
      {
        h: "Fungal Nutrition",
        b: "Fungi are heterotrophic and mostly saprophytic — they absorb food from dead organic matter (e.g. Rhizopus, mushrooms, mould) and act as decomposers. Some fungi are parasitic (e.g. athlete's foot, ringworm). Some fungi are edible (e.g. field mushrooms, truffles) while others are highly poisonous (e.g. death cap mushroom)."
      },
      {
        h: "Factors Affecting Microbial Growth",
        b: "Microorganism growth is affected by pH (extreme pH denatures enzymes), nutrients (carbohydrates, proteins, lipids, minerals, vitamins), water availability, external solute concentration (high concentrations dehydrate the cell), temperature (optimal 20–40°C; refrigeration slows growth) and antimicrobials such as antibiotics and disinfectants."
      },
      {
        h: "Industrial Importance of Microorganisms",
        b: "Microorganisms are used across industries: in pharmaceuticals (antibiotics, vaccines), agriculture (pest control, soil nutrient supply), medicine (probiotics) and food production (butter, cheese, yoghurt, alcohol and other fermented products)."
      },
      {
        h: "The Microbiome",
        b: "A microbiome is all the microorganisms in a particular environment, comprising bacteria, archaea, fungi, protists and viruses. The human microbiome is acquired from the birth canal, breast milk, food, and contact with people and surroundings."
      },
      {
        h: "Microbiome in the Gastrointestinal Tract",
        b: "Gut bacteria assist digestion by breaking down complex carbohydrates and dietary fibre, and produce vitamins B1, B9, B12 and K. The microbiome also supports immune signalling (helping distinguish beneficial from harmful microorganisms) and metabolic health (reducing inflammation, enabling insulin action, decreasing fat storage and regulating appetite hormones)."
      },
      {
        h: "Growth Curves of Microorganisms",
        b: "In a closed system, microbial population growth follows a predictable five-phase curve. The lag phase: numbers are constant as cells adapt. The log (exponential) phase: numbers rise rapidly at maximum reproduction rate. The stationary phase: new cells balance dying cells. The decline (death) phase: death rate exceeds reproduction. The survival phase: a small number persist as dormant spores."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a plasmid?",
        definition: "A small circular loop of DNA found in bacteria, separate from the main chromosome, which often carries genes for antibiotic resistance and is used in genetic engineering.",
        section: "33.1"
      },
      {
        term: "What is a saprophyte?",
        definition: "An organism that obtains nutrients by absorbing them from dead organic matter, acting as a decomposer; examples include Rhizopus and many bacteria.",
        section: "33.1"
      },
      {
        term: "What is a hypha (pl. hyphae)?",
        definition: "A thread-like tube forming the body of a fungus; hyphae collectively form a mycelium and have cell walls made of chitin.",
        section: "33.1"
      },
      {
        term: "What is a sporangium?",
        definition: "A structure borne on upright hyphae (sporangiophores) in fungi such as Rhizopus that produces haploid spores for asexual reproduction.",
        section: "33.1"
      },
      {
        term: "What is the microbiome?",
        definition: "The entire community of microorganisms (bacteria, archaea, fungi, protists and viruses) that exist in a particular environment, such as the human gut.",
        section: "33.1"
      },
      {
        term: "What is the lag phase?",
        definition: "The initial phase of a microbial growth curve during which cell numbers remain constant while organisms adapt to their new environment.",
        section: "33.1"
      },
      {
        term: "What is the log (exponential) phase?",
        definition: "The phase of microbial growth during which cell numbers increase most rapidly as organisms reproduce at their maximum rate.",
        section: "33.1"
      },
      {
        term: "What is an antimicrobial?",
        definition: "A chemical (e.g. antibiotic, disinfectant) that kills or prevents the growth of bacteria and/or fungi.",
        section: "33.1"
      },
      {
        term: "What are chemosynthetic bacteria?",
        definition: "Autotrophic bacteria that make their own food using energy released from chemical reactions rather than from light (e.g. nitrifying bacteria).",
        section: "33.1"
      }
    ];
  })();

  // ── bio34: Nutrient Cycling ───────────────────────────────────────────────
  (function () {
    var c = ch("bio34");
    // 34.1 — How carbon and nitrogen cycle through ecosystems via biological and chemical processes, and the ethical issues arising from nutrient management
    c.learningOutcomes[0].notes = [
      {
        h: "Nutrient Cycling",
        b: "Nutrients cannot be created or destroyed, so they must be recycled through biogeochemical cycles. The two key cycles in LC Biology are the carbon cycle and the nitrogen cycle."
      },
      {
        h: "The Carbon Cycle — Overview",
        b: "The carbon cycle is the process by which carbon from the environment is converted into carbon-containing molecules in living things (carbohydrates, lipids, proteins) and later released back into the environment. The four main processes are photosynthesis, respiration, decomposition and combustion."
      },
      {
        h: "Events in the Carbon Cycle",
        b: "Plants absorb CO₂ by photosynthesis to make glucose, and release CO₂ via respiration. Animals obtain carbon by eating plants and return CO₂ through respiration. When organisms die, bacteria and fungi decompose them, releasing CO₂. Burning fossil fuels (combustion) also returns stored carbon dioxide to the atmosphere."
      },
      {
        h: "Carbon Sinks and Sources",
        b: "A carbon sink absorbs more carbon than it releases; examples include plants, algae, phytoplankton, forests, oceans, soil and fossil fuels. A carbon source releases more carbon than it absorbs; examples include burning fossil fuels, deforestation, respiration and volcanic eruptions."
      },
      {
        h: "Climate Change and Greenhouse Gases",
        b: "Rising CO₂ (from increased fossil fuel combustion and deforestation) and more than doubled methane concentrations (from agriculture and landfill) are contributing to climate change. Both are greenhouse gases: they allow solar heat radiation in but trap reflected heat, causing global warming, rising sea levels and altered weather patterns."
      },
      {
        h: "Climate Warming and Soil Microbiomes",
        b: "Higher temperatures increase soil microorganism activity, releasing more CO₂ and methane. They also alter microbiome diversity, accelerate decomposition (potentially destroying soil structure), encourage plant pathogen growth, and cause thawing permafrost to release stored greenhouse gases."
      },
      {
        h: "Biological Strategies to Reduce Greenhouse Gases",
        b: "Reforestation increases CO₂ absorption. Research into GM plants may allow greater carbon capture and storage in roots. Encouraging phytoplankton and coastal plant growth can increase oceanic carbon sinks. Altering cattle gut microbiomes can reduce their methane production."
      },
      {
        h: "The Nitrogen Cycle — Overview",
        b: "The nitrogen cycle converts atmospheric nitrogen gas (N₂) into nitrogen compounds that living organisms can use for making proteins, DNA, RNA and other biomolecules. Key stages are nitrogen fixation, decomposition, nitrification and denitrification."
      },
      {
        h: "Events in the Nitrogen Cycle",
        b: "Nitrogen fixation converts N₂ to nitrates via volcanic action, lightning, industrial processes or nitrogen-fixing bacteria (which form a mutualistic relationship with legumes such as clover). Decomposers (bacteria and fungi) break down dead organisms and waste, releasing ammonia. Nitrifying bacteria convert ammonia to nitrites and then nitrates. Plants absorb nitrates to make proteins; animals obtain nitrogen by eating plants. Denitrifying bacteria convert nitrates back to N₂, completing the cycle."
      },
      {
        h: "Ethical and Sustainability Issues",
        b: "Modern intensive farming removes large quantities of nutrients from soil. Overuse of fertilisers leads to eutrophication — excess nutrients cause algal blooms, oxygen depletion and death of aquatic life. Phosphorus is a globally limited nutrient. Intensive farming and poor soil practices also increase greenhouse gas production."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the carbon cycle?",
        definition: "The biogeochemical cycle in which carbon moves between the atmosphere, living organisms and the Earth via photosynthesis, respiration, decomposition and combustion.",
        section: "34.1"
      },
      {
        term: "What is a carbon source?",
        definition: "Any process or reservoir that releases more carbon into the atmosphere than it absorbs; examples include burning fossil fuels, deforestation and volcanic eruptions.",
        section: "34.1"
      },
      {
        term: "What is a greenhouse gas?",
        definition: "A gas (e.g. CO₂ or methane) that allows solar heat radiation to enter the atmosphere but traps reflected heat, contributing to global warming.",
        section: "34.1"
      },
      {
        term: "What is nitrogen fixation?",
        definition: "The conversion of atmospheric nitrogen gas (N₂) into nitrates or other usable nitrogen compounds, carried out by lightning, volcanic action and nitrogen-fixing bacteria.",
        section: "34.1"
      },
      {
        term: "What is nitrification?",
        definition: "The conversion of ammonia and ammonium ions to nitrites and then to nitrates, carried out by chemosynthetic nitrifying bacteria in the soil.",
        section: "34.1"
      },
      {
        term: "What is denitrification?",
        definition: "The conversion of nitrates back to nitrogen gas by denitrifying bacteria in the soil, completing the nitrogen cycle.",
        section: "34.1"
      },
      {
        term: "What are the steps of eutrophication?",
        definition: "The process by which excess fertiliser nutrients (especially nitrates and phosphates) enter water, causing algal blooms, oxygen depletion and death of aquatic life.",
        section: "34.1"
      },
      {
        term: "What is permafrost?",
        definition: "Permanently frozen ground found in arctic regions that, when thawed by climate warming, releases stored methane and CO₂ into the atmosphere.",
        section: "34.1"
      },
      {
        term: "What is decomposition?",
        definition: "The breakdown of dead organic matter by bacteria and fungi, which releases carbon dioxide into the atmosphere and ammonia into the soil as part of nutrient cycling.",
        section: "34.1"
      }
    ];
  })();

  // ── bio35: Genetic Engineering ────────────────────────────────────────────
  (function () {
    var c = ch("bio35");
    // 35.1 — The principles and steps of genetic engineering, DNA profiling and sequencing, and the ethical issues surrounding genetic technologies
    c.learningOutcomes[0].notes = [
      {
        h: "Genetic Engineering and Biotechnology",
        b: "Genetic engineering is the artificial manipulation or alteration of genes, typically by cutting a target gene from one organism's DNA and inserting it into another. The resulting DNA is called recombinant DNA and the organism carrying it is a genetically modified organism (GMO). Biotechnology is the industrial manipulation of organisms or their components to create useful products."
      },
      {
        h: "Steps in Genetic Engineering",
        b: "Using the example of inserting a human gene into a bacterium: (1) DNA isolation — the target gene is removed from human cells and a plasmid is extracted from the bacterium; (2) Cutting — both are cut with the same restriction enzyme, producing complementary sticky ends; (3) Ligation — DNA ligase joins the human DNA and plasmid DNA to form recombinant DNA; (4) Transformation — bacteria take up the recombinant plasmid; (5) Expression — bacteria reproduce and express (produce) the protein encoded by the target gene."
      },
      {
        h: "Restriction Enzymes and Ligation",
        b: "Restriction enzymes cut DNA only at specific nucleotide sequences. When the same restriction enzyme cuts DNA from two different organisms, the resulting sticky ends are complementary and will base-pair when mixed. DNA ligase then seals the sugar-phosphate backbone to form a stable recombinant DNA molecule."
      },
      {
        h: "Applications in Pharmaceuticals",
        b: "Organisms genetically engineered to produce medical products include bacteria that make insulin, human growth hormone, antibiotics, antibodies, vaccines and cancer-inhibiting chemicals. These allow large-scale, cost-effective production of medicines that were previously difficult to obtain."
      },
      {
        h: "Applications in Agriculture and Environment",
        b: "GM plants can be engineered to resist herbicides, produce toxins against insect pests, have increased nutritional value or be more resilient to climate change. In environmental science, GM bacteria can produce fermented products, extract heavy metals from soil or water, or break down pollutants such as oil and plastic into harmless substances."
      },
      {
        h: "DNA Profiling",
        b: "DNA profiling creates a unique pattern of DNA bands from an individual's genome for comparison with others. Steps include: obtaining a cell sample, extracting DNA, amplifying it using PCR, cutting it into fragments of different lengths with restriction enzymes, separating fragments by gel electrophoresis and comparing the resulting band patterns."
      },
      {
        h: "Uses of DNA Profiling",
        b: "DNA profiling has forensic uses (identifying suspects at crime scenes), legal uses (establishing paternity or maternity), humanitarian uses (identifying unknown human remains by comparison with relatives) and food safety uses (verifying that a product contains the species it claims to contain, e.g. detecting horse meat in beef products)."
      },
      {
        h: "Polymerase Chain Reaction (PCR)",
        b: "PCR amplifies small DNA samples using the heat-stable enzyme Taq polymerase. The DNA is heated above 90°C to denature (separate) the two strands, then cooled to approximately 50°C to allow the polymerase to build new complementary strands (annealing). Repeated cycles exponentially amplify the target DNA."
      },
      {
        h: "DNA Sequencing (Sanger Method)",
        b: "DNA sequencing determines the exact order of A, T, G and C bases in a gene or DNA segment. In Sanger sequencing: the DNA is amplified and separated; normal nucleotide bases plus small amounts of chain-terminating modified bases are added in four vessels, producing DNA fragments of many different lengths; these fragments are then separated by gel electrophoresis to read the sequence."
      },
      {
        h: "Bioinformatics",
        b: "Bioinformatics uses computer science and statistics to collect, store, organise and analyse large amounts of biological data, particularly DNA sequences. Genome databases such as GenBank store nucleotide sequences and can be searched for genes and alleles linked to specific genetic diseases."
      },
      {
        h: "Ethical Issues in Genetic Technologies",
        b: "Key ethical concerns include access (who can view a person's genetic data, and can employers or insurers use it to discriminate?), genetic modification (safety of GMOs, whether it constitutes 'playing God', and whether unnatural modification should be permitted) and DNA testing (whether consent is truly informed and people fully understand the implications of their results)."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is genetic engineering?",
        definition: "The artificial manipulation or alteration of an organism's genes, typically by inserting a target gene from one organism into the DNA of another.",
        section: "35.1"
      },
      {
        term: "What is recombinant DNA?",
        definition: "DNA that has been artificially formed by combining DNA from two different organisms using restriction enzymes and DNA ligase.",
        section: "35.1"
      },
      {
        term: "What is a GMO (genetically modified organism)?",
        definition: "An organism whose DNA has been altered by genetic engineering to carry a gene from another organism.",
        section: "35.1"
      },
      {
        term: "What is a restriction enzyme?",
        definition: "An enzyme that cuts DNA at specific nucleotide sequences, producing complementary sticky ends that allow DNA from different sources to be joined.",
        section: "35.1"
      },
      {
        term: "What is DNA ligase?",
        definition: "An enzyme that seals the sugar-phosphate backbone between two sections of DNA, fully bonding the plasmid and target gene to form recombinant DNA.",
        section: "35.1"
      },
      {
        term: "What is transformation?",
        definition: "The uptake of recombinant plasmid DNA into a bacterial cell, enabling the bacteria to express the target gene.",
        section: "35.1"
      },
      {
        term: "What is a plasmid (as a cloning vector)?",
        definition: "A small circular bacterial DNA molecule used to carry a target gene into a host cell during genetic engineering; it replicates as the bacteria reproduce.",
        section: "35.1"
      },
      {
        term: "What is DNA profiling?",
        definition: "A technique that creates a unique pattern of DNA bands from an individual's genome using restriction enzymes and gel electrophoresis, used in forensics, paternity testing and food authentication.",
        section: "35.1"
      },
      {
        term: "What is PCR (polymerase chain reaction)?",
        definition: "A technique that amplifies tiny DNA samples by repeated cycles of heating (denaturation above 90°C) and cooling (annealing at ~50°C) using the heat-stable enzyme Taq polymerase.",
        section: "35.1"
      },
      {
        term: "What is gel electrophoresis?",
        definition: "A technique that separates DNA fragments by size by passing them through a gel under an electric current; smaller fragments travel further.",
        section: "35.1"
      },
      {
        term: "What is bioinformatics?",
        definition: "The use of computer science and statistics to collect, store, organise and analyse large biological datasets, especially DNA sequences stored in databases such as GenBank.",
        section: "35.1"
      },
      {
        term: "What is Sanger sequencing?",
        definition: "A method of DNA sequencing in which chain-terminating modified nucleotides are used to produce DNA fragments of different lengths that are then separated by gel electrophoresis to read the base sequence.",
        section: "35.1"
      }
    ];
  })();

  // ── bio-acronyms: Biology Acronyms and Key Terms ──────────────────────────
  (function () {
    var c = ch("bio-acronyms");
    // A.1 — Acronyms and key terms to learn
    c.learningOutcomes[0].notes = [
      {
        h: "DNA / RNA",
        b: "DNA: Deoxyribonucleic Acid. RNA: Ribonucleic Acid."
      },
      {
        h: "ATP / ADP",
        b: "ATP: Adenosine Triphosphate (energy currency). ADP: Adenosine Diphosphate (ATP after energy release)."
      },
      {
        h: "NAD+ / NADH / NADP+ / NADPH",
        b: "NAD+: Nicotinamide Adenine Dinucleotide (oxidised). NADH: reduced form, carries electrons to ETC. NADP+/NADPH: phosphorylated version used in photosynthesis."
      },
      {
        h: "FAD / FADH2",
        b: "Flavin Adenine Dinucleotide — coenzyme that carries electrons to the ETC from the Krebs cycle."
      },
      {
        h: "ER / TEM / SEM",
        b: "ER: Endoplasmic Reticulum (smooth = lipids; rough = proteins). TEM: Transmission Electron Microscope (2D). SEM: Scanning Electron Microscope (3D)."
      },
      {
        h: "ETC",
        b: "Electron Transport Chain — on inner mitochondrial membrane; uses NADH/FADH2 to drive ATP synthesis."
      },
      {
        h: "SA Node / AV Node",
        b: "SA node: Sinoatrial node — heart pacemaker in right atrium. AV node: Atrioventricular node — delays and relays impulse to ventricles."
      },
      {
        h: "ADH",
        b: "Antidiuretic Hormone (vasopressin) — released by posterior pituitary; makes collecting ducts more permeable to water."
      },
      {
        h: "PCT / DCT",
        b: "PCT: Proximal Convoluted Tubule (reabsorbs glucose, amino acids, water). DCT: Distal Convoluted Tubule (fine-tunes salts and pH)."
      },
      {
        h: "RBC / WBC",
        b: "RBC: Red Blood Cell — carries haemoglobin. WBC: White Blood Cell — phagocytes (engulf microbes) and lymphocytes (produce antibodies)."
      },
      {
        h: "Pulmonary / Systemic Circuit",
        b: "Pulmonary: heart -> lungs -> heart (gas exchange). Systemic: heart -> body -> heart (delivers O2, collects CO2)."
      },
      {
        h: "ABO / Rh",
        b: "ABO: four main blood groups (A, B, AB, O). Rh: Rhesus factor — Rh+ has the protein, Rh- does not."
      },
      {
        h: "Classification Hierarchy",
        b: "Domain -> Kingdom -> Phylum -> Class -> Order -> Family -> Genus -> Species. Mnemonic: 'Dear King Philip Came Over For Good Soup'."
      },
      {
        h: "Three Domains",
        b: "Bacteria (prokaryotes, e.g. E. coli), Archaea (prokaryotic extremophiles), Eukarya (all eukaryotes)."
      },
      {
        h: "Photosynthesis Equation",
        b: "6CO2 + 6H2O -> C6H12O6 + 6O2 (in light, with chlorophyll)."
      },
      {
        h: "Aerobic Respiration Equation",
        b: "C6H12O6 + 6O2 -> 6CO2 + 6H2O + ~38 ATP."
      },
      {
        h: "ATP Yields",
        b: "Aerobic respiration: ~38 ATP per glucose. Anaerobic respiration: ~2 ATP per glucose (glycolysis only)."
      },
      {
        h: "Experiment Variables",
        b: "IV: Independent Variable (changed by experimenter). DV: Dependent Variable (measured). CV: Control Variables (kept constant)."
      },
      {
        h: "Food Tests Summary",
        b: "Iodine -> blue-black = starch. Benedict's + heat -> brick-red = reducing sugar. Biuret -> purple = protein. Ethanol emulsion -> cloudy white = lipid. Acidified potassium dichromate orange -> green = ethanol."
      },
      {
        h: "Limewater",
        b: "Turns cloudy/milky white in the presence of CO2. Used to confirm CO2 production in respiration experiments."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 5,
        prompt: "State the classification hierarchy from domain to species and give the mnemonic.",
        model: "Domain -> Kingdom -> Phylum -> Class -> Order -> Family -> Genus -> Species. Mnemonic: 'Dear King Philip Came Over For Good Soup'."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Write the equations for photosynthesis and aerobic respiration and state the ATP yield of each.",
        model: "Photosynthesis: 6CO2 + 6H2O -> C6H12O6 + 6O2 (uses light energy; net producer of glucose and oxygen). Aerobic respiration: C6H12O6 + 6O2 -> 6CO2 + 6H2O + ~38 ATP. Anaerobic respiration yields only ~2 ATP per glucose."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Name four food tests, the reagent used and a positive result for each.",
        model: "Starch: iodine -> blue-black. Reducing sugar: Benedict's solution + heat -> brick-red precipitate. Protein: biuret reagent (NaOH + CuSO4) -> purple/violet. Lipid: ethanol emulsion test -> cloudy white suspension."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Explain the roles of the SA node and ADH.",
        model: "SA node (sinoatrial node): acts as the heart's pacemaker in the right atrium wall; generates electrical impulses that trigger atrial contraction and set heart rate (~60-80 bpm at rest). ADH (antidiuretic hormone): released from the posterior pituitary when blood is too concentrated; makes collecting ducts more permeable to water so more is reabsorbed, producing concentrated urine and restoring normal blood water content."
      }
    ];
  })();

})();