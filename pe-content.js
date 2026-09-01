// Physical Education Content — notes, concept points and flashcards for all chapters.
// Past-paper exam questions live in exam-questions-db.js.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  function ch(id) { return COURSE_DATA.chapters.find(function (c) { return c.id === id; }); }

  // ── pe1: Physical Demands of Performance ──────────────────────────────────
  (function () {
    var c = ch("pe1");
    // 1.1 — Health, fitness, components and fitness testing
    c.learningOutcomes[0].notes = [
      {
        h: "What is Health, Fitness, Well-being?", b: "Health (WHO): state of complete physical, mental and social well-being, not merely absence of disease. Fitness: ability to carry out everyday tasks without becoming overly tired. Well-being: combination of mental and social elements that contribute to fulfilment. Regular exercise reduces risk of heart disease, obesity, high blood pressure, adult-onset diabetes, osteoporosis and stroke."
      },
      {
        h: "What are the two categories of fitness?", b: "Health-related fitness — 5 components essential for health (mnemonic: Cows Make Milk For Bones). Performance-related (skill-related) fitness — 6 components that enhance performance (mnemonic: All Big Cats Pounce Really Softly)."
      },
      {
        h: "What are the 5 health-related components of fitness?", b: "1. Cardiorespiratory endurance — delivering oxygen and nutrients to muscles over a sustained period. 2. Muscular endurance — ability of a muscle/muscle group to generate force repetitively without fatiguing. 3. Muscular strength — maximal force a muscle can produce. 4. Flexibility — range of motion at a joint. 5. Body composition — percentage of body fat vs non-fat mass."
      },
      {
        h: "What is Body composition and somatotypes?", b: "Measured by body fat % or BMI (mass kg / height m squared; high muscle mass can give a false high BMI). Ectomorph: long, lean, low body fat, low musculature, fast metabolism (high jumper, long-distance runner). Mesomorph: broad shoulders, narrow hips, high musculature, moderate fat, gains muscle easily (sprinter, swimmer). Endomorph: apple-shaped, high body fat, slow metabolism, gains fat and muscle easily (sumo wrestler, prop forward)."
      },
      {
        h: "What is Performance-related components (6)?", b: "1. Agility — change direction and speed quickly and efficiently. 2. Balance — maintain equilibrium (static = stationary, dynamic = moving). 3. Coordination — move two or more body parts in a controlled, smooth way. 4. Power — exert maximal force in as short a time as possible (Power = force x time). 5. Reaction time — how quickly the brain initiates a response to a stimulus. 6. Speed — how fast a body is moving."
      },
      {
        h: "What are the steps of Needs analysis?", b: "Process of determining the qualities necessary for a sport, an athlete, or a combination. Allows a training programme to target sport-specific fitness based on the demands of the sport, position and role."
      },
      {
        h: "What is Fitness testing?", b: "Form of assessment for performer needs and optimum performance. Identifies strengths and weaknesses to set realistic goals. Test battery: collection of tests specific to the sport. Field tests are practical and school-friendly; lab tests are more accurate."
      },
      {
        h: "Which fitness test measures each component of fitness?", b: "Cardiorespiratory endurance: Cooper 12-minute run (estimates VO2 max) or multistage 20m bleep test. Muscular endurance: push-up test, sit-up test. Muscular strength: standing broad jump (lower), seated medicine ball throw (upper), 1RM/3RM, hand grip dynamometer. Flexibility: sit-and-reach. Body composition: BMI, body fat callipers, BODPOD, DEXA scan. Agility: Illinois Agility Test, T-drill. Balance: stork balance test. Coordination: alternative hand wall toss. Power: vertical jump. Reaction time: ruler drop test. Speed: 30m sprint."
      },
      {
        h: "What is Factors affecting assessment?", b: "Standardised test: same protocol every time. Valid: measures what it claims to measure. Reliable: produces consistent results when repeated. Normative data: results compared against population norms."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline the five health-related components of fitness and briefly explain why each is important for general health.",
        model: "Cardiorespiratory endurance allows the heart and lungs to deliver oxygen to working muscles for sustained activity. Muscular endurance lets muscles work repeatedly without fatigue. Muscular strength is the maximal force a muscle can produce, important for lifting and pushing tasks. Flexibility provides pain-free range of motion at the joints. Body composition (lower body fat, higher lean mass) reduces the risk of obesity-related disease."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Compare the three somatotypes and give a sporting example of each.",
        model: "Ectomorphs are tall and lean with low muscle mass and a fast metabolism, suited to long-distance running or high jump. Mesomorphs have broad shoulders, narrow hips and gain muscle easily, suiting sprinting and swimming. Endomorphs are short and rounded with higher body fat and slow metabolism, suited to sumo wrestling or prop forward in rugby."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Describe two fitness tests, identifying the component each measures and one strength of each test.",
        model: "The Cooper 12-minute run measures cardiorespiratory endurance by recording distance covered in 12 minutes; it is cheap, simple and estimates VO2 max. The sit-and-reach test measures hamstring and lower-back flexibility; it is standardised and provides reliable, normative data for comparison."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Explain the difference between a valid and a reliable fitness test.",
        model: "A valid test measures what it claims to measure — for example, the vertical jump genuinely measures leg power. A reliable test produces consistent results when repeated under the same conditions. A test can be reliable without being valid; a good test battery should be both."
      }
    ];
  })();

  // ── pe2: Training Methods and Fitness Plans ───────────────────────────────
  (function () {
    var c = ch("pe2");
    // 2.1 — Principles, methods, recovery and periodisation
    c.learningOutcomes[0].notes = [
      {
        h: "What does Principles of training (SPORRT) state?", b: "Specificity — training must match the activity and goals (energy systems, muscles, components, intensity, time). Progressive overload — gradually increase Frequency, Intensity, Time or Type. Recovery — time for the body to repair and adapt. Reversibility — training effects diminish without progression (use it or lose it). Tedium — vary training to avoid boredom and keep performers motivated."
      },
      {
        h: "What is FITT formula?", b: "Frequency (how often), Intensity (how hard), Time (how long), Type (what kind). Used to apply progressive overload."
      },
      {
        h: "What does the principle of diminishing returns state?", b: "Rate of fitness improvement decreases over time as fitness approaches its potential. Fitter performers gain less from each training session."
      },
      {
        h: "What is Continuous training?", b: "Exercising continuously without rest. Low intensity, minimum 20 minutes in the aerobic zone (70-80% MHR). Develops cardiorespiratory endurance."
      },
      {
        h: "What is Fartlek training?",
        b: "Swedish 'speed play' — continuous training with varied speed and terrain. Develops aerobic AND anaerobic systems, lactate threshold and recovery times."
      },
      {
        h: "What is an Interval training?", b: "Periods of intense work followed by timed rest or cardiac-readiness rest. Structured in sets and reps; intensity expressed as % HR. Improves cardiorespiratory endurance, muscular endurance, speed and recovery."
      },
      {
        h: "What are the types of circuit training?", b: "Series of 8-10 stations performed one after another, working different muscle groups. Types: aerobic, local muscular endurance, anaerobic, strength, flexibility, skill-related."
      },
      {
        h: "What is Weight training?", b: "Uses external weights. Strength = high weight, low reps. Endurance = low weight, high reps. Power = moderate weight, explosive reps."
      },
      {
        h: "What is Plyometric training?", b: "Uses speed and force to build muscle power: bounding, hopping, jumping, box jumps. Eccentric contraction (landing) followed quickly by concentric contraction (jumping)."
      },
      {
        h: "What is Flexibility training?", b: "Deliberate programme to permanently increase range of motion. Static (hold at resistance), active (partner-assisted), ballistic (momentum, bouncing), PNF (stretch + contract — most effective): stretch to resistance, contract 5-6 sec, relax, hold 20-30 sec, recover 30 sec, repeat 2-4 times."
      },
      {
        h: "What is an Adaptation and recovery?", b: "Adaptation is the body getting accustomed to training through repeated exposure. Without rest, performance decreases and overtraining occurs. Strategies: passive recovery (complete rest), active recovery (low-intensity activity, improves blood flow), sleep (7-8 hours; non-REM releases growth hormones), nutrition, cryotherapy, foam rolling (self-myofascial release for DOMS), compression garments."
      },
      {
        h: "What is Periodisation?", b: "Division of a training plan (usually yearly) into cycles. Macrocycle: full long-term cycle (yearly or 4-year Olympic plan) with preparation, competition and transition phases. Mesocycle: weeks emphasising the same type of adaptation. Microcycle: a small number of training sessions, often a daily breakdown."
      },
      {
        h: "What is an Overtraining, peaking and tapering?", b: "Overtraining: imbalance between load and recovery, causing performance to fall. Peaking: performer in best physical, emotional and mental condition for the most important competition. Tapering: reduction in training VOLUME (intensity maintained) before competition to be fresh for peak performance."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 10,
        prompt: "Outline the principles of training using the acronym SPORRT.",
        model: "Specificity: training matches the demands of the activity (energy systems, muscles, components). Progressive overload: gradually increase frequency, intensity, time or type. Recovery: schedule rest for the body to repair and adapt. Reversibility: gains are lost if training stops or fails to progress. Tedium: vary sessions to maintain motivation and prevent boredom."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain how the FITT formula is used to apply progressive overload in a training plan.",
        model: "The coach increases one variable at a time to keep stressing the body. Frequency raises the number of sessions per week; Intensity increases the difficulty (e.g. heavier weight or higher % MHR); Time lengthens session duration; Type introduces a new training method (e.g. switching from continuous to fartlek) to keep adaptations occurring."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Compare continuous training and interval training, including one fitness component each develops best.",
        model: "Continuous training is steady-state exercise at low-to-moderate intensity for at least 20 minutes, primarily developing cardiorespiratory endurance through the aerobic system. Interval training alternates intense work with timed rest, building both aerobic and anaerobic capacity, lactate tolerance and speed. Continuous is suited to marathon runners; interval is suited to team-sport athletes who repeat sprints."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Describe two recovery strategies and explain how each promotes adaptation.",
        model: "Active recovery (easy jog or gentle cycle) keeps blood flowing through muscles, removing waste products and reducing soreness. Sleep — particularly non-REM deep sleep — releases growth hormone and allows tissue repair; 7-8 hours per night maximises adaptation gained from training."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Distinguish between a macrocycle, mesocycle and microcycle in periodisation.",
        model: "A macrocycle is the full long-term plan, usually a season or four-year Olympic cycle, divided into preparation, competition and transition phases. A mesocycle is a block of weeks focused on one adaptation (e.g. strength). A microcycle is the smallest unit, typically a week of training broken down session by session."
      }
    ];
  })();

  // ── pe3: Psychological Demands of Performance ─────────────────────────────
  (function () {
    var c = ch("pe3");
    // 3.1 — Confidence, anxiety, arousal, motivation and mental strategies
    c.learningOutcomes[0].notes = [
      {
        h: "What are the steps of Psychological preparedness?", b: "Forming the mental functions, processes and personality traits required to solve problems during training and competition."
      },
      {
        h: "Confidence and self-efficacy",
        b: "Self-confidence: belief in one's skills and ability. Self-efficacy: self-belief that enables better performance in a specific task. Trait confidence: confident in many situations. State confidence: confident only in specific situations. Extroverts tend to have high self-confidence."
      },
      {
        h: "Bandura's model of self-efficacy",
        b: "Self-efficacy is formed and changed through four information sources: enactive mastery (past success), vicarious experiences (seeing others succeed), verbal persuasion (encouragement) and physiological arousal (how the body feels). High self-efficacy pursues challenges and persists; low self-efficacy avoids challenges and gives up."
      },
      {
        h: "What is an Anxiety?", b: "Feeling of unease, worry or fear, ranging from mild to severe. Trait anxiety is part of personality across life areas. State anxiety is temporary, in specific situations. Cognitive anxiety: mental worries and expectations. Somatic anxiety: physical effects such as sweaty palms, raised HR and butterflies. SCAT (Sports Competition Anxiety Test, 1990) measures anxiety level."
      },
      {
        h: "Arousal and the Inverted-U",
        b: "Arousal is a state of physical and mental readiness on a continuum from low to high. Inverted-U theory: performance improves with arousal up to an optimal point, then worsens. Low arousal = boredom; medium arousal = the 'zone'; high arousal = over-arousal and panic. Extroverts need higher arousal; introverts perform better at lower arousal."
      },
      {
        h: "What is Motivation?", b: "Level of enthusiasm or desire to train and compete. Intrinsic motivation comes from within (satisfaction, pride). Extrinsic motivation comes from outside: tangible rewards (medals, money — use sparingly with young athletes) and intangible rewards (praise, recognition — use regularly). Amotivation: lack of motivation; performer likely to quit."
      },
      {
        h: "What is Mental strategies — before performance?", b: "Positive self-talk: encouragement (I can, I will) maintains self-confidence and regulates thoughts. Mental rehearsal: imagining successful performance. Visualisation/imagery: like mental rehearsal but uses all five senses to recreate or create a successful experience. Pre-performance ritual: routine to focus the mind and combat anxiety. Music: matching rhythm to movement and uplifting lyrics energise the performer."
      },
      {
        h: "What is Mental strategies — during performance?", b: "Accept anxiety as part of sport; reduce it when overwhelming. Manage emotions: accept and use them. Concentration: focus on the moment, resist distractions, regain focus when lost. Breathing control: slow, deep diaphragmatic breaths reduce anxiety and control arousal."
      },
      {
        h: "Reframing and after performance",
        b: "Reframing: putting a new, growth-mindset frame on a setback to build confidence. WWW technique — 'What Will Work?' before and 'What Went Well?' after. After performance: breathing control, music, speak with coach/mentor, reframing and goal-setting."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Using Bandura's model, outline how a coach can build self-efficacy in a young athlete.",
        model: "The coach uses the four information sources. Enactive mastery: set achievable tasks so the athlete experiences success. Vicarious experiences: show video of similar athletes performing well. Verbal persuasion: give specific, sincere encouragement. Physiological arousal: teach breathing and warm-up routines so the athlete reads their body's signals as readiness rather than fear."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Use the Inverted-U theory to explain how arousal affects performance.",
        model: "Performance improves as arousal rises from a low, bored state to an optimal mid-range 'zone', where focus and physical readiness are at their best. Beyond this peak, further arousal causes muscle tension, narrow attention and poor decision-making, so performance drops. Different personalities and skills require different optimal points — introverts and fine-skill performers usually need lower arousal."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Distinguish between cognitive and somatic anxiety with a sporting example of each.",
        model: "Cognitive anxiety is mental — negative thoughts, worry and self-doubt — such as a footballer obsessing over missing a penalty before taking it. Somatic anxiety is physical — sweaty palms, raised heart rate, butterflies — such as a sprinter's hands shaking on the blocks. Cognitive anxiety responds to mental strategies like reframing; somatic anxiety responds to physical strategies like breathing control."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Explain two strategies a performer can use before competition to enhance psychological preparation.",
        model: "Visualisation: the athlete uses all five senses to imagine a successful performance, building confidence and rehearsing the motor programme without physical fatigue. Pre-performance ritual: a consistent routine (kit, warm-up, music) quiets the mind, reduces anxiety and signals readiness to compete."
      }
    ];
    c.examQuestions = [
      {
        id: "pe3-eq-1",
        source: "LC Physical Education Past Paper — Q4",
        parts: [
          {
            label: "Q4. (a)",
            question: "Define the following types of goals related to physical activity: (i) Short term goal and (ii) Performance goal.",
            marks: 6,
            model: "Short term goal: A specific target set to be achieved in the near future (days or weeks), designed to provide motivation and measurable progress towards a longer-term aim. Example: I will improve my 100m sprint time by 0.3 seconds within the next two weeks. Performance goal: A goal focused on achieving a specific quality or level of performance based on the athlete's own previous standard, independent of comparison with others. It is entirely within the athlete's control. Example: I will successfully complete 80% of my set shots from the free-throw line during this week's training sessions.",
            diagram: ""
          },
          {
            label: "Q4. (b)",
            question: "Write a short term performance goal.",
            marks: 4,
            model: "Example: By the end of this week's training, I will maintain a plank position for 60 seconds without breaking form. This is a short term performance goal because it is specific, time-bound, measurable, and entirely based on my own personal performance standard rather than comparing myself to others. (Use the SMART framework: Specific, Measurable, Achievable, Relevant, Time-bound.)",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── pe4: Diet and Nutrition ───────────────────────────────────────────────
  (function () {
    var c = ch("pe4");
    // 4.1 — Macronutrients, micronutrients, energy systems and supplements
    c.learningOutcomes[0].notes = [
      {
        h: "What is Balanced diet?", b: "Variety of foods providing adequate nutrients for good health. The food pyramid: bottom five levels eaten daily in varying amounts; top level limited. Ensures correct macronutrients, micronutrients, fibre and water."
      },
      {
        h: "What is Carbohydrates?", b: "Main energy source. Stored as glycogen in muscles and liver, broken down to glucose during exercise. 1g = 4 calories; 50-60% of total daily calories. Daily intake: 5-7g/kg moderate, 7-10g/kg endurance, 10-12g/kg extreme. Complex (slow release: brown pasta, potatoes). Simple (quick release: juice, sweets)."
      },
      {
        h: "Distinguish between Glycogen and carb loading.", b: "Used by endurance athletes. 1 week pre-competition: 2-3 days high-protein/fat with intense exercise to deplete glycogen, then 3 days high-carb plus tapering. Supercompensates glycogen stores up to 2x normal, delaying fatigue."
      },
      {
        h: "What is the role of Protein?", b: "Provides amino acids for muscle growth and repair, immune function and hormones. 1.7-2g/kg/day for performers. 1g = 4 calories."
      },
      {
        h: "What is the role of Fats?", b: "Most concentrated energy source; primary fuel for endurance; aids brain/cell function; insulates organs; absorbs fat-soluble vitamins. 1g = 9 calories. Saturated (limit): butter, fatty meat. Unsaturated (aim for): nuts, seeds, vegetable oils."
      },
      {
        h: "What roles do fibre, vitamins and minerals play in the diet?", b: "Fibre: indigestible, helps absorb vitamins, removes waste, creates fullness. Vitamins: fat-soluble (A, D, E, K) stored in fatty tissue; water-soluble (B, C) must be replenished daily. Minerals: calcium, potassium, iron."
      },
      {
        h: "What is Hydration and dehydration?", b: "Water transports oxygen, nutrients and hormones; lost through sweat which also removes salts. 2% body-weight fluid loss reduces performance; 3%+ risks heat exhaustion. Athletes can sweat 6-10% body weight in competition."
      },
      {
        h: "What is an Energy systems (ATP)?", b: "All produce ATP for muscle contraction. ATP-PCr system: immediate, max intensity, 8-10 sec, recovers in 2-3 min (100m sprint, powerlifting). Anaerobic glycolysis: uses glycogen without oxygen, up to 1-2 min, produces lactic acid (800m, circuit training); lactate clears in ~8 min. Aerobic glycolysis: uses oxygen with fats and carbs, 2 min to hours, recovery hours-3 days (marathon, long-distance cycling). The energy continuum describes how all three contribute together."
      },
      {
        h: "What should a performer know about supplements and sports drinks?", b: "WADA and Sport Ireland do not endorse supplements; performers must check the prohibited list. Sports drinks: water + electrolytes + 6-8% carbohydrates, no stimulants. Energy drinks: contain stimulants (caffeine, guarana). Key supplements: protein (muscle repair), creatine (extends ATP-PCr), caffeine (CNS stimulant, fat metabolism), nitrates (oxygen uptake)."
      },
      {
        h: "What is Metabolism and BMR?", b: "Metabolism converts food into energy. BMR (Basal Metabolic Rate): calories required at rest. Affected by gender, weight, height, age, body composition, genetics. Males have a 10-15% higher BMR; BMR falls 2-3% per decade after age 18."
      },
      {
        h: "What is Nutrition planning?", b: "Targets: =55% carbs, =30% fat, 15% protein. Before (fuel up): carb-rich; avoid high fat. During: usually no food if <2 hours. After (3 Rs): refuel glycogen, repair muscle, rehydrate."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline the three macronutrients and the role of each in an athlete's diet.",
        model: "Carbohydrates are the primary fuel for exercise, stored as glycogen and broken into glucose to power high-intensity work; they should provide 50-60% of calories. Proteins supply amino acids for muscle growth and repair, immune function and hormone production; athletes need 1.7-2g/kg/day. Fats are the most concentrated energy source (9 cal/g), fuel endurance work, insulate organs and carry fat-soluble vitamins; unsaturated sources should be prioritised."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Describe the three energy systems and give a sporting example of each.",
        model: "ATP-PCr: produces ATP rapidly for 8-10 seconds of max effort (100m sprint, powerlifting); recovers in 2-3 minutes. Anaerobic glycolysis: breaks down glycogen without oxygen for 1-2 minutes of high intensity (800m, circuit training), producing lactic acid that causes fatigue. Aerobic system: uses oxygen with fats and carbs to make large amounts of ATP for endurance work lasting 2 minutes to several hours (marathon, road cycling)."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain the process of carbohydrate loading and the benefit to an endurance athlete.",
        model: "About a week before competition the athlete spends 2-3 days on high-protein, high-fat, low-carb intake with intense training to deplete glycogen, then switches to 3 days of high-carb intake while tapering. The body supercompensates by storing up to twice the normal level of glycogen, which delays fatigue and helps the athlete maintain pace during long races such as a marathon."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Discuss the risks of dehydration on sporting performance.",
        model: "A 2% fluid loss already reduces performance, causing reduced concentration, increased fatigue and decreased strength. At 3%+ the risk of heat exhaustion and heatstroke rises sharply. Electrolytes lost through sweat must also be replaced. Athletes should hydrate before, during and after exercise to maintain performance and avoid these risks."
      }
    ];
    c.examQuestions = [
      {
        id: "pe4-eq-1",
        source: "LC Physical Education Past Paper — Q5",
        parts: [
          {
            label: "Q5.",
            question: "Describe two categories of performance-enhancing drugs. You are not permitted to use anabolic steroids as one of your answers.",
            marks: 8,
            model: "1. Beta-blockers: Drugs that reduce heart rate, lower anxiety and steady fine motor control. Used in precision sports such as archery, shooting and golf to reduce tremors and improve accuracy. Health risks: fatigue, depression, reduced exercise capacity. 2. Stimulants: Drugs that increase alertness, reduce perceived fatigue and elevate aggression or confidence. Used by athletes in endurance and power sports to mask tiredness. Examples: amphetamines, cocaine, ephedrine. Health risks: cardiovascular damage, addiction, aggression, overheating. (Other valid categories: Diuretics — used to rapidly lose weight or mask other drugs; EPO / blood doping — increases red blood cell count and oxygen delivery.)",
            diagram: ""
          }
        ]
      },
      {
        id: "pe4-eq-2",
        source: "LC Physical Education Past Paper — Q10",
        parts: [
          {
            label: "Q10. (a)",
            question: "Outline two benefits of sports drinks for performers.",
            marks: 6,
            model: "1. Rehydration: Sports drinks contain water and electrolytes (sodium, potassium, magnesium) that replace the fluids and salts lost through sweat during exercise. Maintaining fluid balance prevents dehydration, sustaining muscular function and cognitive performance. 2. Energy provision: Sports drinks contain carbohydrates (glucose, maltodextrin) that provide a rapid and sustained energy source during prolonged exercise. This maintains blood glucose levels, spares muscle glycogen and delays the onset of fatigue.",
            diagram: ""
          },
          {
            label: "Q10. (b)",
            question: "Name a sports supplement used by athletes and justify why athletes might use this supplement.",
            marks: 6,
            model: "Supplement: Creatine (creatine monohydrate). Justification: Creatine is stored in muscle as phosphocreatine (PCr), which rapidly regenerates ATP during short, maximal-intensity efforts (e.g. sprinting, weightlifting, jumping). Supplementing with creatine increases the PCr stores in muscle, enabling athletes to perform more repetitions at high intensity before fatigue, potentially increasing muscle mass and strength over time through a greater training volume. It is most beneficial in repeated short-burst sports.",
            diagram: ""
          }
        ]
      },
      {
        id: "pe4-eq-3",
        source: "LC Physical Education Past Paper — Q12",
        parts: [
          {
            label: "Q12. (a)",
            question: "Identify three ways in which Irish anti-doping rules are enforced.",
            marks: 6,
            model: "1. In-competition testing: Athletes selected (randomly or by targeting) must provide urine or blood samples immediately following competition. 2. Out-of-competition testing: Athletes may be tested at any time, without prior notice — at training venues, their home or anywhere — to catch athletes who time drug use to avoid detection during competition. 3. Whereabouts programme: Elite athletes must register their current location with Sport Ireland Anti-Doping on a quarterly basis so testers can locate them for unannounced out-of-competition tests (missing three tests in 12 months is treated as a doping violation).",
            diagram: ""
          },
          {
            label: "Q12. (b)",
            question: "Under what circumstance can an athlete compete with banned substances in their system?",
            marks: 4,
            model: "Under a Therapeutic Use Exemption (TUE). If an athlete has a legitimate diagnosed medical condition that requires treatment with a substance that appears on the prohibited list (e.g. asthma requiring corticosteroids, ADHD requiring stimulants, or testosterone deficiency requiring replacement therapy), they may apply to Sport Ireland Anti-Doping for a TUE before competition. If granted, the athlete may use the medication without committing a doping violation, provided it is used solely for therapeutic medical purposes at the prescribed dose.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── pe5: Skill, Ability and Skilled Performance ───────────────────────────
  (function () {
    var c = ch("pe5");
    // 5.1 — Classification, learning, guidance, feedback and practice
    c.learningOutcomes[0].notes = [
      {
        h: "What is Skill?", b: "A sequence of movements performed effectively and efficiently to achieve a predetermined goal."
      },
      {
        h: "What is Characteristics of skilful movement (ACE FACE)?", b: "Aesthetic (looks good), Coordinated, Efficient, Fluent, Accurate, Controlled/Consistent, Economical."
      },
      {
        h: "Qualities of a skilled performer (TACK)",
        b: "Technique: correct practical procedure. Anticipation: reading and predicting opponents' movements. Consistency: repeating quality movement under various conditions. Kinaesthetic sense (muscle memory): awareness of own movement during execution, enabling error correction."
      },
      {
        h: "What is the difference between Skill and ability?", b: "Skills are LEARNED through practice and produce permanent behaviour change. Abilities are INHERITED, INNATE and enduring traits that make tasks possible (coordination, flexibility, balance, power, endurance, speed)."
      },
      {
        h: "Domains of skill",
        b: "Psychomotor (the 'do' — physical movement, hand-eye, foot-eye). Cognitive (the 'think' — selecting skills, tactics, rules). Perceptual (the 'feel' — senses interpret the situation)."
      },
      {
        h: "What is Skill classification continua?", b: "Gross-Fine (muscle size). Open-Closed (environmental influence — open is externally paced and unpredictable; closed is self-paced and fixed). Simple-Complex (cognitive demand). Externally paced-Self-paced (timing). Discrete-Serial-Continuous (defined start/end). Individual-Coactive-Interactive (athlete interaction)."
      },
      {
        h: "What is an Information-processing model?", b: "Four stages: 1. Perceiving (input via senses), 2. Decision-making (short-term memory ~30 sec and long-term memory store motor programmes), 3. Acting (output), 4. Evaluating (feedback adapts performance)."
      },
      {
        h: "What is Fitts and Posner stages of learning (1967)?", b: "Cognitive: inconsistent, trial and error, relies on coach cues, 2-3/10 success. Associative: motor memories forming, internal feedback developing, 5-7/10 success. Autonomous: skill is automatic and motor programmes are in long-term memory, focus shifts to tactics, 9/10 success — must keep practising to retain. Learning plateau: performance levels off temporarily or at the limit of ability."
      },
      {
        h: "What is Types of guidance (VVMM)?", b: "Visual: demonstrations, diagrams, videos (early stages, builds a model). Verbal: brief, focused explanation of key cues. Manual: physical support from coach (complex or dangerous skills). Mechanical: equipment assists or guides the movement."
      },
      {
        h: "What is Feedback?", b: "Intrinsic: internal information from proprioception during execution. Extrinsic: from external sources (coach, video, results). Concurrent: during the action. Terminal: after the action. Knowledge of performance: feedback on the QUALITY of execution. Knowledge of results: feedback on the SUCCESS or final outcome."
      },
      {
        h: "What is Practice types and organisation?", b: "Fixed (drill): repeated practice of one skill — suits closed skills. Variable: same skill in many contexts — suits open skills. Massed: no breaks; for fit, experienced performers. Distributed: rest breaks; for beginners or low fitness. Whole: skill in entirety (simple skills). Part: one element at a time (complex skills). Progressive-part: chain sub-routines together. Whole-part-whole: whole, isolate weakness, whole again. Effective practice (GAP VAT): Goal-orientated, Appropriate, Progressive, Varied, Adaptable, Time-bound."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Distinguish between skill and ability and give a sporting example of each.",
        model: "An ability is innate and enduring — for example, natural reaction speed that a sprinter is born with. A skill is learned and produces a permanent change in behaviour through practice — for example, the smooth start out of the blocks the sprinter develops over years of training. Abilities are the raw material; skills are the polished movement built on top."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Outline Fitts and Posner's three stages of motor-skill learning.",
        model: "Cognitive stage: the learner is inconsistent, makes many errors and relies on external cues from the coach; success is low (2-3/10). Associative stage: motor memories form, simple parts become fluent and the performer begins self-correcting using kinaesthetic feedback; success rises to 5-7/10. Autonomous stage: the skill is automatic, attention can switch to tactics and opponents, and success is around 9/10 — but practice must continue to retain the level."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Compare knowledge of performance and knowledge of results as types of feedback.",
        model: "Knowledge of performance focuses on the QUALITY of the technique — for example, a coach noting that a golfer's hip rotation was incomplete. Knowledge of results focuses on the OUTCOME — for example, the ball landing 10 metres short of the green. Knowledge of performance helps refine the skill, while knowledge of results confirms whether the action achieved its goal."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain two methods of practice a coach could use to teach a complex skill.",
        model: "Part practice breaks a complex skill into its sub-routines so the performer can perfect one element at a time, e.g. practising only the toss in a tennis serve. Progressive-part practice then chains those sub-routines together — toss, then toss + swing, then full serve — building the skill up while keeping cognitive load manageable."
      }
    ];
    c.examQuestions = [
      {
        id: "pe5-eq-1",
        source: "LC Physical Education Past Paper — Q2",
        parts: [
          {
            label: "Q2.",
            question: "Outline four types of feedback that can be beneficial to athlete performance.",
            marks: 8,
            model: "1. Intrinsic (internal) feedback: Sensory information received from within the performer's own body during or after movement — proprioceptive sensations of balance, muscle tension and joint position. Example: a gymnast feeling whether their body alignment is correct during a handstand. 2. Extrinsic (augmented/external) feedback: Information received from an outside source — coach instruction, video analysis, score or performance data — that the athlete could not obtain unaided. 3. Knowledge of Results (KR): Feedback about the outcome or end result of a performance. Example: 'You scored 7 out of 10 free throws.' It motivates athletes and informs them whether they are achieving goals. 4. Knowledge of Performance (KP): Feedback about the movement pattern or technique used rather than the result. Example: 'Your release point was too early in the throw.' Helps the performer refine technique.",
            diagram: ""
          }
        ]
      },
      {
        id: "pe5-eq-2",
        source: "LC Physical Education Past Paper — Q6",
        parts: [
          {
            label: "Q6. (a)",
            question: "Outline two principles of effective practice.",
            marks: 6,
            model: "1. Specificity of practice: Practice should closely replicate the conditions, movements and demands of actual performance so that the skill transfers effectively. A sprinter should practise start technique from blocks in race-like conditions, not just jog. 2. Variability of practice: Exposing the learner to slightly varied practice conditions (different speeds, distances, opponents) develops a more adaptable motor programme, improving the performer's ability to adapt the skill to changing game situations.",
            diagram: ""
          },
          {
            label: "Q6. (b)",
            question: "How would you use one of the principles outlined in Q6(a) to develop skill in a practice session?",
            marks: 6,
            model: "Applying Specificity of practice — Example: Basketball free throw. Initially I have the athlete practise uncontested free throws to groove the basic technique. I then progressively make the practice more specific: simulate game fatigue by having the athlete complete a sprint before each throw, add the crowd noise and pressure of a decisive final-minute scenario, and introduce a real defender making noise nearby. Each stage more closely replicates the specific physical and psychological conditions of an actual game, ensuring the skill transfers from training to competition.",
            diagram: ""
          }
        ]
      },
      {
        id: "pe5-eq-3",
        source: "LC Physical Education Past Paper — Q8",
        parts: [
          {
            label: "Q8. (a)",
            question: "As part of your studies in LC Physical Education you compared your personal performance to that of a more skilled/model performer. Describe how you conducted this analysis.",
            marks: 6,
            model: "I selected my physical activity (e.g. 100m sprint). I recorded a video of my own performance from a consistent camera angle and distance. I also sourced a video of a skilled/model performer (e.g. a national or international sprinter) performing the same skill from an equivalent angle. I created a structured observation checklist of key technical components: drive phase mechanics, arm action, knee lift, body lean and stride frequency. I watched both videos multiple times and compared each component against the checklist, identifying where my technique differed from the model. For example: my arm action crossed the midline of my body, whereas the model performer drove their arms straight forward and back, which is more efficient. I then prioritised these differences and set goals to address the most significant technical weaknesses.",
            diagram: ""
          },
          {
            label: "Q8. (b)",
            question: "Outline two aesthetic/artistic criteria of performance in a named physical activity of your choice.",
            marks: 6,
            model: "Physical activity: Contemporary Dance. 1. Fluency and continuity: Movements flow seamlessly from one to the next without abrupt stops or jarring transitions. A skilled dancer connects each movement phrase smoothly, creating a continuous stream of motion that gives the impression of effortless control. 2. Expression and interpretation: The performer communicates emotion, narrative or the intent of the choreography through dynamic variation (contrast between powerful and gentle movements), facial expression and spatial awareness. A skilled dancer makes the audience feel the intended mood of the piece rather than simply executing correct technical positions.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── pe6: Biomechanics ─────────────────────────────────────────────────────
  (function () {
    var c = ch("pe6");
    // 6.1 — Planes, axes, levers, motion and economy of movement
    c.learningOutcomes[0].notes = [
      {
        h: "What is the role of Biomechanics?", b: "The study of structure, function and movement of a living body. Used to increase performance (speed, power, technique, economy) and reduce injury risk (lessen joint impact, fix technique, address imbalances)."
      },
      {
        h: "What is Planes (3)?", b: "Sagittal plane — divides body LEFT/RIGHT; movements are flexion/extension, forward/backward (running, squatting). Frontal plane — divides FRONT/BACK; movements are abduction/adduction. Transverse plane — horizontal, divides UPPER/LOWER; movements are rotation (360 twist)."
      },
      {
        h: "What is an Axes (3)?", b: "Sagittal axis: runs horizontally back-to-front. Vertical axis: runs vertically top-to-bottom. Frontal (transverse) axis: runs horizontally left-to-right."
      },
      {
        h: "What is Planes and axes paired?", b: "Frontal plane rotates around the sagittal axis (FP/SA). Transverse plane rotates around the vertical axis (TP/VA). Sagittal plane rotates around the frontal axis (SP/FA)."
      },
      {
        h: "What is a lever, and what forms the lever system in the body?", b: "A lever is a rigid body moving around a fulcrum. In the body: bones are the lever, joints are the fulcrum, muscles supply the effort, body parts or weights are the load."
      },
      {
        h: "What are the three classes of lever?", b: "1st class — fulcrum in the middle (neck nodding). 2nd class — load in the middle (standing on tiptoe; gastrocnemius is the effort, body weight is the load, ball of foot is fulcrum). 3rd class — effort in the middle (biceps curl); most common in the human body."
      },
      {
        h: "Distinguish between Mechanical advantage and disadvantage.", b: "Load arm: load to fulcrum. Effort arm: effort to fulcrum. Mechanical advantage: effort arm longer than load arm — lifts large loads with small effort. 2nd class always has mechanical advantage; 3rd class always has mechanical disadvantage."
      },
      {
        h: "What is the difference between scalar and vector quantities?", b: "Scalar = magnitude only (time, length, mass, speed, temperature). Vector = magnitude + direction (force, weight, velocity, acceleration, displacement). Force/weight in Newtons (N), acceleration m/s2, velocity m/s, displacement m, mass kg."
      },
      {
        h: "What is the difference between Distance and displacement?", b: "Distance is the scalar interval covered along the path. Displacement is the shortest straight-line vector from start to finish. A 400m runner finishing in the same lane has covered 400m distance but 0m displacement."
      },
      {
        h: "What is Speed, velocity, acceleration?", b: "Speed = distance / time. Velocity = displacement / time (vector). Acceleration = rate of change of velocity (vector); deceleration is negative acceleration. Mass = amount of matter (kg); Weight = mass x gravity (N)."
      },
      {
        h: "Newton's laws",
        b: "1st (Inertia): a body stays at rest or in uniform motion unless acted on by an external force — a ball stays still until kicked. 2nd (Acceleration): F = MA; a tennis smash applies more force than a drop shot, producing greater acceleration. 3rd (Counterforce): every action has an equal and opposite reaction — a runner pushes into the ground, the ground pushes back."
      },
      {
        h: "What is an Economy of movement?", b: "Energy efficiency of the body. Internal factors (controlled by performer): technique, coordination, mobility, stability. External factors: gravity, friction (a weightlifter uses chalk to increase grip), wind, weather. Creative application of skill is performing a skill in a new, high-risk, high-reward way."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Outline the three planes of motion and give one example of movement in each.",
        model: "The sagittal plane divides the body into left and right and allows flexion/extension movements such as squatting or running. The frontal plane divides front from back and allows abduction/adduction such as a jumping jack. The transverse plane is horizontal, divides upper from lower and allows rotation such as a 360-degree twist in gymnastics."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Describe the three classes of levers, giving a body example of each.",
        model: "First-class levers have the fulcrum in the middle (e.g. neck nodding — neck joint is fulcrum, head is load, neck muscles provide effort). Second-class levers have the load in the middle (standing on tiptoe — ball of foot is fulcrum, body weight is load, calf muscle provides effort); they always give mechanical advantage. Third-class levers have the effort in the middle (biceps curl — elbow is fulcrum, hand is load, biceps is effort); they are most common in the body and always have mechanical disadvantage."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain Newton's three laws of motion using sporting examples.",
        model: "1st (Inertia): a hockey ball stays still until struck and continues until stopped by another force. 2nd (F = MA): the same hurler applies more force on a long puck than a short pass, producing greater acceleration of the sliotar. 3rd (Counterforce): a sprinter pushes back into the blocks and the blocks push the sprinter forward with equal force."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Distinguish between a scalar and a vector quantity and provide two examples of each.",
        model: "Scalar quantities have magnitude only — examples include speed and mass. Vector quantities have magnitude AND direction — examples include velocity and displacement. The difference matters in biomechanics because a 400m runner has speed throughout the lap but ends with zero displacement."
      }
    ];
  })();

  // ── pe7: Structures and Strategies ────────────────────────────────────────
  (function () {
    var c = ch("pe7");
    // 7.1 — Compositional elements, team structures and strategies
    c.learningOutcomes[0].notes = [
      {
        h: "What is Composition?", b: "Arrangement of a series of movements or skills in a desired manner to achieve a performance goal."
      },
      {
        h: "What is Compositional elements (5)?", b: "1. Shape — element of space: low (on ground), medium (standing), high (in air); symmetry vs asymmetry. 2. Space — path and pattern (straight, zigzag, circular, curved). 3. Timing — tempo (steady or varied) and rhythm. 4. Dynamics — variation in energy/effort (slow, sustained, powerful, explosive). 5. Relationships — connections with space, objects and people (lifts, passes, ribbons)."
      },
      {
        h: "What is the role of Structures?", b: "Set-up of an activity, competition format, or team formation. Examples: soccer 4-4-2, GAA backs/midfield/forwards, cycling stage races. A team is more than two people in an organised set-up where players take on positions, roles and responsibilities."
      },
      {
        h: "What is Strategies (tactics)?", b: "Game plans pre-arranged and rehearsed to maximise the chance of success. Performers must adapt during performance through problem-solving and decision-making (who does what, use of space, on/off-ball action)."
      },
      {
        h: "What is Modifying structures and strategies (ACT)?", b: "Anticipate (read the opponent), Correct (adjust the plan), Timing (act at the right moment). Used to exploit opponent weaknesses or recover from setbacks."
      },
      {
        h: "Distinguish between Demands of performance and qualities of a performer.", b: "Physical qualities: health- and performance-related components. Personal qualities: personality and character. Technical qualities: execution of skill."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline the five compositional elements and apply each to a chosen sport or dance performance.",
        model: "Shape: the body or team adopts different levels and symmetry — e.g. a gymnast holding a high asymmetric balance. Space: paths through the area — e.g. a basketball point guard cutting on a curved drive. Timing: tempo and rhythm — e.g. a dancer matching steps to musical beat. Dynamics: explosive vs sustained effort — e.g. a hurler changing pace before a side-step. Relationships: connections with people/objects — e.g. a rugby lift in a line-out."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain how a coach can modify team structures and strategies during a game using the ACT model.",
        model: "Anticipate: read patterns in the opponent's play (e.g. they target the left wing). Correct: adjust the structure to counter — drop a midfielder into that channel. Timing: pick the right moment to make the change, e.g. at the start of the second half before the opponent commits to its plan, so the team gains an advantage without giving the opponent time to react."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Distinguish between a structure and a strategy in team performance.",
        model: "A structure is the physical set-up — formation, positions and roles (e.g. a soccer 4-4-2). A strategy is the plan of action within that structure — the tactics for using space, on- and off-ball movement, and exploiting the opposition. The structure is the framework; the strategy is how the team plays inside it."
      }
    ];
    c.examQuestions = [
      {
        id: "pe7-eq-1",
        source: "LC Physical Education Past Paper — Q11",
        parts: [
          {
            label: "Q11.",
            question: "Explain two structures OR two strategies that can help an athlete or team succeed. Support your answer with physical activity examples.",
            marks: 8,
            model: "STRUCTURES: 1. Periodisation: The systematic division of the training year into phases (macrocycles, mesocycles, microcycles) so the athlete peaks physically at the right time, avoids overtraining and systematically develops fitness, technique and tactical skills. Example: A 1500m runner builds an aerobic base in the off-season (general preparation), transitions to speed work in pre-competition, then tapers in the final two weeks before the national championships to ensure peak form on race day. 2. Support staff structure: A clearly defined coaching team — head coach, assistant coaches, sports scientist, physiotherapist, nutritionist — ensures every aspect of an athlete's preparation is covered by a specialist, reducing gaps and maximising performance. Example: An elite rugby team with a dedicated lineout and set-piece specialist coach enables the team to gain a significant tactical advantage at restarts. STRATEGIES: 1. High press (soccer): A collective tactical strategy in which all outfield players immediately press the ball-carrier high up the pitch after losing possession, reducing the opposition's time and space and forcing errors or long balls. Example: Liverpool FC's gegenpressing under Klopp. 2. Zone defence (basketball): Players each guard a designated area rather than a specific opponent, protecting the key, reducing the opposition's ability to drive to the basket, and forcing difficult perimeter shots.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── pe8: Safe Practice in Sport and PA ────────────────────────────────────
  (function () {
    var c = ch("pe8");
    // 8.1 — Safety, injuries, first aid, overtraining and load management
    c.learningOutcomes[0].notes = [
      {
        h: "What is Safe practice?", b: "Procedures to ensure safety of all stakeholders: safe facilities, fit equipment, correct attire, warm-up/cool-down and first-aid knowledge."
      },
      {
        h: "What is Clothing and protective equipment?", b: "Compression clothing aids muscle recovery; base layers regulate temperature; supports and braces protect joints. Protective equipment (helmets, mouth guards, padding) must be maintained in good condition."
      },
      {
        h: "What is an Injury prevention?", b: "Warm-up increases body temperature, blood flow, flexibility and range of motion. Cool-down removes lactic acid, prevents DOMS and blood pooling, and returns HR gradually to rest."
      },
      {
        h: "What are intrinsic and extrinsic risk factors?", b: "Intrinsic: personal to the performer (previous injury, age, fitness). Extrinsic: external (surface, weather, equipment)."
      },
      {
        h: "What is Common injuries?", b: "Ankle sprain, pulled groin, hamstring strain, shin splints, ACL tear, patellofemoral knee syndrome, tennis elbow (epicondylitis), head injury."
      },
      {
        h: "What is Types of injuries?", b: "Acute injuries (specific impact): hard tissue acute = dislocations, fractures; soft tissue acute = tears, strains, sprains. Chronic injuries (overuse): hard tissue chronic = stress fractures; soft tissue chronic = shin splints, tendinosis. Sprain grades: 1 = overstretched ligament, 2 = partial tear, 3 = full tear with popping sound."
      },
      {
        h: "What is Concussion?", b: "Acute injury from head trauma. Symptoms: headache, dizziness, balance issues, nausea, possible loss of consciousness. Managed with the 6 Rs: Recognise, Remove, Refer, Rest, Recover, Return."
      },
      {
        h: "What is First aid — SALTAPS?", b: "Stop the play, Ask about the injury, Look (bleeding, swelling), Touch with consent (pain/sensation), Active movement (can athlete move it?), Passive movement (full range?), Strength test (walk/run/jump?)."
      },
      {
        h: "What is PRICE protocol?", b: "Treats sprains, strains and closed fractures. Protection (stop activity), Rest (2-3 days), Ice (15-20 min several times a day), Compression (bandage to limit swelling), Elevation (above heart level)."
      },
      {
        h: "What is an Overtraining, fatigue and supercompensation?", b: "Overtraining is an imbalance between training load and recovery and causes performance to fall. Overreaching is a temporary, recoverable version. Fatigue is lack of energy. Supercompensation: after training and adequate recovery, the body adapts BEYOND pre-training levels — repeated cycles produce steady improvement."
      },
      {
        h: "What is Monitoring load?", b: "Borg RPE: subjective rating of how hard exercise feels (1-10). Daily wellness parameters: sleep, mood, soreness, motivation, nutrition. Training load = duration x intensity (training units = RPE x session time). External exertion is measurable (kg lifted); internal exertion is perceived. Performance management: set goals, monitor load, evaluate and re-evaluate."
      },
      {
        h: "What is BREAKS checklist?", b: "Body, Rules, Equipment, Ability, Kit, Surface — used before participation to ensure safe practice."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Outline the steps of the SALTAPS protocol for assessing injury.",
        model: "Stop the play to prevent further damage. Ask the athlete where it hurts and what happened. Look at the area for swelling, bleeding or bruising. Touch the site (with consent) to check for pain and sensation. Active movement — ask the athlete to move it themselves. Passive movement — gently test the full range of motion. Strength — see if the athlete can walk, run or jump on it before deciding whether they can return."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Describe how the PRICE protocol is used to treat a Grade 1 ankle sprain.",
        model: "Protection: stop the activity immediately. Rest the ankle for 2-3 days before reintroducing movement. Ice the area for 15-20 minutes several times a day to reduce swelling. Compression with a bandage limits further swelling and supports the joint. Elevation of the ankle above heart level draws fluid away from the injury and reduces inflammation."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Distinguish between acute and chronic injuries with one example of each.",
        model: "Acute injuries are caused by a specific impact or traumatic event — for example, an ankle sprain when landing awkwardly from a jump. Chronic injuries develop slowly from overuse and insufficient recovery — for example, shin splints in a runner who has increased mileage too quickly. Acute injuries need immediate first aid; chronic injuries need load management and addressing underlying causes."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Explain supercompensation and how it leads to fitness improvements.",
        model: "After a training session the body is temporarily fatigued and performance dips, but during recovery it adapts and rebuilds BEYOND the previous baseline — this is supercompensation. If the next training stimulus is timed during this raised state and rest is adequate, fitness climbs in a stepwise pattern. Insufficient recovery results in overtraining instead of compensation."
      }
    ];
  })();

  // ── pe9: Rules, Rituals, Coach and Officials ──────────────────────────────
  (function () {
    var c = ch("pe9");
    // 9.1 — Roles of the coach and the official, communication and reflection
    c.learningOutcomes[0].notes = [
      {
        h: "What is the role of Rules, roles, rituals?", b: "Rules: agreed-upon principles governing a sport — for safety, sportsmanship and fair competition. Roles: playing (defender, captain) and non-playing (referee, coach). Rituals: behaviours believed to have a specific purpose or power (e.g. the Haka). Superstition: belief in supernatural good/bad luck attached to actions. Pre-performance rituals are task-relevant routines that prepare mind and body. Conventions (etiquette): unwritten rules such as the coin flip in soccer or glove touch in boxing."
      },
      {
        h: "What is Role of the coach?", b: "Ensures each athlete or team reaches full potential. Duties: skill and strategy practice, line-ups, leadership, communication and support, working with the manager, considering both physical and psychological elements."
      },
      {
        h: "What is the role of Effective coach roles?", b: "Facilitator of learning, problem-solver, time manager, innovator, aware of health and safety, good role model, motivator and inspiration."
      },
      {
        h: "Coaching qualities",
        b: "Emotional intelligence: understanding and managing one's emotions positively to relieve stress, empathise and defuse conflict. Interpersonal skills: communicating with others. Intrapersonal skills: managing one's own emotions, self-awareness, self-control."
      },
      {
        h: "What is Motivational strategies (coach)?", b: "Communicate effectively and openly. Create a positive training environment and healthy competition. Use praise appropriately. Avoid punishment to eliminate mistakes. Use SMARTER goal-setting (Specific, Measurable, Achievable, Realistic, Time-bound, Evaluated, Reviewed). Share a vision for success."
      },
      {
        h: "Communication",
        b: "Non-verbal: gestures, facial expressions, tone, eye contact, body language, posture. Verbal: positive feedback and constructive criticism. A coach must be aware of their own non-verbal cues and read the performer's."
      },
      {
        h: "Performance analysis and reflection",
        b: "Notational analysis: factual recording of events (tactics, technique, work rate). Video analysis: immediate feedback, highlights strengths/weaknesses. Sports analytics: statistical principles for competitive advantage. Reflection — concurrent ('in' action, during) and terminal ('on' action, after); self-, peer- or coach-reflection. Sport Ireland Coaching Development Programme: 50+ NGBs, 25,000 coaches per year, 130 awards."
      },
      {
        h: "What is the role of Role of the official?", b: "Ensure competition is safe and fair, implement rules, protect player safety, guided by codes of conduct. Roles: athlete, rule enforcer, decision-maker, timekeeper, conflict manager, record-keeper. Characteristics: knowledge of rules, fitness, calmness, moral courage, safety awareness."
      },
      {
        h: "What is Scoring and recording?", b: "Officials record goals, fouls and cards. In aesthetic sports (gymnastics, dance) judges rate performance against criteria; in outcome sports the result decides the winner."
      },
      {
        h: "What is Psychological readiness (3 Cs)?", b: "Concentration: task-oriented focus on rules and events. Coping: handle the conditions using techniques. Confidence: belief in own knowledge and decisions."
      },
      {
        h: "What is the role of Mental tools (4 Ms)?", b: "Moves: pre-performance routine to get into the zone. Maps: reflect on performance, set goals, use self-talk. Mood: control and monitor mood (relaxation, deep breathing). Movies: mental imagery of performing the role."
      },
      {
        h: "Managing conflict (official)",
        b: "Recognise causes early, be respectful, stay calm, step back if needed, avoid raising the voice, keep hand movements slow and open, be assertive not aggressive, ask for help from other officials, communicate with the captain, breathe deeply, self-talk ('Relax'), be proactive not reactive."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline four qualities of an effective coach and the impact each has on a team.",
        model: "Effective communication keeps players informed of expectations and tactics, reducing confusion and conflict. Emotional intelligence allows the coach to read mood, empathise and defuse tension, building trust. Knowledge of the sport and of training methods means sessions are well planned and progressive. Being a good role model — punctual, fair, calm — sets the standard players model themselves on."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Describe two motivational strategies a coach can use, including one practical example of each.",
        model: "SMARTER goal-setting: agree a Specific, Measurable, Achievable, Realistic, Time-bound goal that is Evaluated and Reviewed — e.g. 'improve free-throw success from 60% to 75% by April'. Creating a positive training environment: praise effort, allow mistakes and use healthy internal competition — e.g. small-sided games with rotating teams so players are challenged but not embarrassed."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain how an official can manage on-pitch conflict.",
        model: "The official recognises early warning signs, remains calm and respectful, and communicates assertively with the captain rather than confronting every player. Body language is open, hand movements slow, and the official may take a step back, breathe deeply and use self-talk to control mood. If needed they consult fellow officials and apply cards in line with the rules, staying proactive rather than reactive."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Distinguish between concurrent reflection and terminal reflection.",
        model: "Concurrent reflection happens DURING the event ('reflection in action') — for example, a midfielder noticing the press is too high and dropping deeper. Terminal reflection happens AFTER the event ('reflection on action') — for example, reviewing match video the next day to identify what worked. Both feed into future performance, but concurrent reflection adjusts in the moment while terminal reflection adjusts the plan."
      }
    ];
  })();

  // ── pe-casestudy: Case Study ──────────────────────────────────────────────
  (function () {
    var c = ch("pe-casestudy");
    // CS.1 — Case study practice
    c.learningOutcomes[0].notes = [
      {
        h: "What is the Case Study?", b: "Question 13 in the LC PE exam is a 50-mark Case Study. A text (with images, tables and figures) is provided in the exam paper and all sub-questions refer to that text. Sub-questions draw on multiple chapters — biomechanics, skill learning, fitness, nutrition, ethics."
      },
      {
        h: "What is How to Prepare?", b: "Practise applying concepts from multiple chapters to unseen scenarios. Read the case study carefully before answering, underlining key facts. Structure answers using specific PE terminology and physical activity examples."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 5,
        prompt: "List the key concepts likely to appear in a PE Case Study question.",
        model: "Concepts of physical activity (play, sport, physical education), FMS (locomotor, body control, manipulative), fitness components, skill learning and practice methods, biomechanical principles (levers, planes of movement), nutrition/supplementation, ethical practice in sport."
      }
    ];
    c.examQuestions = [
      {
        id: "pe-cs-eq-1",
        source: "LC Physical Education Past Paper — Q13 (Case Study: Throwing — 50 marks)",
        caseStudy: true,
        context: "Throwing\n\nThrowing can be a fun, open-ended activity that provides opportunities for children to explore, experiment and learn through play.\n\nFundamental movement skills (FMS) are believed to be the building blocks from which many other sporting movements are developed. FMS are grouped into three different categories: locomotor or movement skills such as running and jumping; body control or stability skills such as catching and throwing; or manipulative skills such as catching and throwing. When you examine Figure 6 you can understand how FMS like throwing can be viewed as the building block for skills in different sports.\n\nAthlete note (Figure 6): Volleyball — Spike; Badminton — Smash; Netball — Overhead pass; Baseball — Pitch; Javelin — Release; Tennis — Serve.\n\nThe javelin can be described simply as: a straight run of approximately 10-15 steps, during which the athlete continues running but the body turns to position to throw the javelin. The athlete must then ensure they stay within the throwing zone after releasing the javelin.\n\nFigure 9 shows a training plan for a javelin thrower during their competitive phase. The plan includes: Technique/throwing specifics, Full throw, Strength, Speed, Competition, Rest — distributed across M/T/W/T/F/S.\n\nInterestingly, many throwing coaches now advocate for throwing both light and heavy implements in training. It is believed that these training approaches can help develop different components of fitness relevant to the javelin.\n\nUnfortunately, some javelin throwers looking to gain an edge over competitors turn to unethical practices. DP Manu tested positive for the anabolic steroid methyltestosterone in 2024 and missed the Olympic Games as a result.",
        parts: [
          {
            label: "13. (a) (i)",
            question: "Identify and define two concepts of physical activity named in the case study.",
            marks: 8,
            model: "Concept 1: Play — a free, intrinsically motivated, open-ended and enjoyable physical activity undertaken for its own sake, without defined rules or outcomes. The case study states throwing can be a fun, open-ended activity for children to explore and learn through play. Concept 2: Sport — a structured, rule-governed physical activity involving competition, with defined objectives and outcomes. The case study identifies javelin as part of Athletics Ireland's track and field programme, with athletes competing according to rules (throwing zone, step count).",
            diagram: ""
          },
          {
            label: "13. (a) (ii)",
            question: "Discuss the personal and social benefits, mentioned in the case study, for children engaging in throwing activities.",
            marks: 8,
            model: "Personal benefits: 1. Development of Fundamental Movement Skills — throwing develops body control/stability and manipulative FMS, which are the building blocks for more complex sporting skills later in life. 2. Physical development and coordination — practising throwing improves hand-eye coordination, upper-body strength and kinaesthetic awareness. Social benefits: 1. Transferable participation — by developing throwing as an FMS, children gain the competence to participate in multiple sports (volleyball, badminton, netball, baseball, javelin, tennis as shown in Figure 6), expanding their opportunities for social inclusion through sport. 2. Shared enjoyment — the open-ended, playful nature of throwing creates an inclusive, low-pressure social environment in which children can experiment, collaborate and experience enjoyment together.",
            diagram: ""
          },
          {
            label: "13. (b)",
            question: "Name a skill that uses a 3rd class lever from a named physical activity of your choice. Justify why this skill is an example of a 3rd class lever.",
            marks: 10,
            model: "Physical activity: Athletics (Javelin). Skill: The javelin throwing action. A 3rd class lever has the effort (muscular force) applied between the fulcrum (joint/pivot) and the load (resistance/implement). In the javelin throw: the shoulder joint acts as the fulcrum; muscle force (deltoid, triceps, rotator cuff) is applied to the upper arm close to the shoulder, between the shoulder joint and the javelin held in the hand (the load). Because the effort arm is shorter than the load arm, this arrangement sacrifices force advantage in exchange for a large range of motion and high velocity at the end of the lever (hand). This generates the high release speed required to throw the javelin as far as possible. (Alternatively: bicep curl — elbow joint = fulcrum; bicep muscle force = effort applied between elbow and hand; load = weight held in hand.)",
            diagram: ""
          },
          {
            label: "13. (c) (i)",
            question: "Based on the description of javelin in the case study, name a skill practice method appropriate for developing the skill of a javelin thrower.",
            marks: 4,
            model: "Part practice (also called progressive part practice or segmentation). The javelin throw is a complex, multi-phase closed skill (run-up, cross-step, body rotation, release, follow-through/recovery within the throwing zone). Breaking it into component parts allows the learner to master each sub-routine before recombining them.",
            diagram: ""
          },
          {
            label: "13. (c) (ii)",
            question: "Explain how you would apply the practice method you named in 13(c)(i) to improve the skill of a javelin thrower.",
            marks: 8,
            model: "Applying Part practice to the javelin throw: Phase 1 — Grip and release: practise the correct grip and wrist-flick release action from a standing position, focusing on a clean, controlled release point. Phase 2 — Throwing action: add the shoulder rotation and arm drive from a standing position only, without the run-up. Phase 3 — Cross-step: practise the penultimate cross-steps (the body rotation phase) without throwing, developing rhythm and balance. Phase 4 — Combine cross-step + throw: integrate the rotation with the release. Phase 5 — Run-up: add the straight run-up and practise the full approach. Phase 6 — Full skill (Whole): combine all phases continuously at full speed, including a controlled recovery within the throwing zone. The coach provides KP feedback after each phase to correct errors in technique before moving to the next.",
            diagram: ""
          },
          {
            label: "13. (c) (iii)",
            question: "Hammer throwers mainly move in which plane of movement?",
            marks: 4,
            model: "The transverse (horizontal) plane. The hammer thrower rotates their entire body horizontally around a vertical axis during the spinning turns. All rotational movement — the turning of the trunk, hips and arms — occurs in the transverse plane.",
            diagram: ""
          },
          {
            label: "13. (d) (i)",
            question: "Use Figure 9 (the training plan) to suggest which component of fitness might be developed by throwing light implements. Justify your answer.",
            marks: 6,
            model: "Component of fitness: Speed (or speed-strength/power — speed component). Justification: Throwing a lighter implement allows the athlete to accelerate and release the implement at a much higher velocity than they can with a standard or heavy implement. By repeatedly practising this high-velocity movement, the athlete overloads the speed dimension of the power equation (Power = Force x Velocity), training the neuromuscular system to fire muscle fibres at a faster rate and improving the speed of the throwing action. This transfers to a faster release speed when throwing the standard implement.",
            diagram: ""
          },
          {
            label: "13. (d) (ii)",
            question: "Use Figure 9 (the training plan) to suggest which component of fitness might be developed by throwing heavy implements. Justify your answer.",
            marks: 6,
            model: "Component of fitness: Muscular Strength (or power — strength component). Justification: A heavier implement requires the athlete to generate significantly greater muscular force to accelerate it through the throwing motion. This overloads the strength component of the movement. Over time, repeatedly applying maximal or near-maximal force against a heavier load stimulates the muscles, tendons and neural pathways to adapt, increasing muscle cross-sectional area (hypertrophy) and improving motor unit recruitment. This strength gain transfers to greater force production when throwing the standard implement.",
            diagram: ""
          },
          {
            label: "13. (e) (i)",
            question: "Suggest two effects that anabolic steroids can have on athlete performance.",
            marks: 8,
            model: "1. Increased muscle mass and strength: Anabolic steroids (synthetic testosterone) accelerate protein synthesis in muscle cells and increase nitrogen retention, leading to greater muscle hypertrophy. The athlete gains more lean muscle mass and can produce greater force, improving performance in power and strength events such as javelin throwing. 2. Faster recovery: Anabolic steroids reduce muscle protein breakdown and inflammatory responses after intense training sessions. This allows athletes to train more frequently and at higher intensity without accumulating fatigue, enabling greater training volumes and faster adaptation. (Additional valid effects: increased aggression/assertiveness which may improve competitive drive; increased red blood cell production in some cases.)",
            diagram: ""
          },
          {
            label: "13. (e) (ii)",
            question: "Explain how DP Manu did NOT adhere to the principles of ethical practice when he took methyltestosterone. You must refer to at least two principles of ethical practice.",
            marks: 8,
            model: "1. Fair Play: By taking methyltestosterone (an anabolic steroid banned by the World Anti-Doping Code), DP Manu artificially enhanced his throwing performance beyond what was achievable through natural talent, training and dedication. This violated the principle of fair play, which requires all athletes to compete on an equal basis using only legally permitted means. Other competitors who trained drug-free were at an unfair disadvantage. 2. Integrity/Honesty: By using a prohibited substance while competing, Manu misrepresented his true, naturally achievable capabilities to his fellow competitors, officials and the public. He deliberately circumvented the rules of his sport, showing a disregard for the honesty and transparency that are fundamental to ethical competition. His actions undermined trust in athletics and resulted in his disqualification from the 2024 Olympic Games.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── pe-acronyms: Acronyms and Mnemonics ───────────────────────────────────
  (function () {
    var c = ch("pe-acronyms");
    // A.1 — Acronyms and mnemonics to learn
    c.learningOutcomes[0].notes = [
      {
        h: "What is SPORRT?", b: "Principles of training: Specificity, Progressive overload, Recovery, Reversibility, Tedium."
      },
      {
        h: "What is FITT?", b: "Progressive overload formula: Frequency, Intensity, Time, Type."
      },
      {
        h: "What is Cows Make Milk For Bones?", b: "Five health-related components of fitness: Cardiorespiratory endurance, Muscular endurance, Muscular strength, Flexibility, Body composition."
      },
      {
        h: "What is an All Big Cats Pounce Really Softly?", b: "Six performance-related components: Agility, Balance, Coordination, Power, Reaction time, Speed."
      },
      {
        h: "What is an ACE FACE?", b: "Characteristics of skilful movement: Aesthetic, Coordinated, Efficient, Fluent, Accurate, Controlled, Economical."
      },
      {
        h: "What is TACK?", b: "Qualities of a skilled performance: Technique, Anticipation, Consistency, Kinaesthetic sense."
      },
      {
        h: "What are the types of VVMM?", b: "Types of guidance: Visual, Verbal, Manual, Mechanical."
      },
      {
        h: "What is GAP VAT?", b: "Effective practice design: Goal-orientated, Appropriate, Progressive, Varied, Adaptable, Time-bound."
      },
      {
        h: "What is SCAT?", b: "Sports Competition Anxiety Test (1990) — measures level of anxiety with a points system."
      },
      {
        h: "What is WWW?", b: "Reframing technique: What Will Work? (before performance) and What Went Well? (after performance)."
      },
      {
        h: "What is SMARTER?", b: "Goal-setting framework: Specific, Measurable, Achievable, Realistic, Time-bound, Evaluated, Reviewed."
      },
      {
        h: "What is an ACT?", b: "Modifying structures and strategies: Anticipate, Correct, Timing."
      },
      {
        h: "What is SALTAPS?", b: "Injury assessment: Stop, Ask, Look, Touch, Active movement, Passive movement, Strength test."
      },
      {
        h: "What is PRICE?", b: "Injury treatment: Protection, Rest, Ice, Compression, Elevation."
      },
      {
        h: "What is BREAKS?", b: "Safe practice checklist: Body, Rules, Equipment, Ability, Kit, Surface."
      },
      {
        h: "What is 6 Rs?", b: "Concussion management: Recognise, Remove, Refer, Rest, Recover, Return."
      },
      {
        h: "What is RPE?", b: "Rating of Perceived Exertion (Borg scale) — measures intensity by how hard the performer feels they are working."
      },
      {
        h: "What is 3 Cs?", b: "Psychological readiness of officials: Concentration, Coping, Confidence."
      },
      {
        h: "What is 4 Ms?", b: "Mental tools for officials: Moves, Maps, Mood, Movies."
      },
      {
        h: "F = MA",
        b: "Newton's 2nd Law: Force = Mass x Acceleration."
      },
      {
        h: "What is Plane-Axis pairs?", b: "FP/SA: Frontal plane rotates around sagittal axis. TP/VA: Transverse plane rotates around vertical axis. SP/FA: Sagittal plane rotates around frontal axis."
      },
      {
        h: "What is an Energy and testing acronyms?", b: "ATP: Adenosine Triphosphate. ATP-PCr: Adenosine Triphosphate-Phosphocreatine system. BMI: Body Mass Index. BMR: Basal Metabolic Rate. VO2 max: maximum oxygen consumption. DOMS: Delayed Onset Muscle Soreness. LME: Local Muscular Endurance. PNF: Proprioceptive Neuromuscular Facilitation. HIIT: High Intensity Interval Training. MHR: Maximum Heart Rate. 1RM/3RM: One/Three Repetition Maximum. DEXA: Dual-Energy X-ray Absorptiometry."
      },
      {
        h: "What is Governance and bodies?", b: "WHO: World Health Organization. WADA: World Anti-Doping Agency. NGB: National Governing Body. GAA: Gaelic Athletic Association. FAI: Football Association of Ireland. FIFA: Federation Internationale de Football Association. RSA: Road Safety Authority."
      },
      {
        h: "What is Periodisation cycles?", b: "Macrocycle: full long-term plan (year+). Mesocycle: weeks emphasising one type of adaptation. Microcycle: small number of sessions, often a week or day plan."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 5,
        prompt: "State what each letter of SPORRT stands for and give a one-line meaning for each.",
        model: "Specificity — training matches the activity. Progressive overload — gradually increase the demand. Recovery — schedule rest to allow adaptation. Reversibility — gains fade without progression. Tedium — vary training to keep performers motivated."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain the SALTAPS and PRICE acronyms and when each is used.",
        model: "SALTAPS (Stop, Ask, Look, Touch, Active, Passive, Strength) is used pitch-side immediately after an injury to ASSESS severity and decide if the athlete can continue. PRICE (Protection, Rest, Ice, Compression, Elevation) is then used to TREAT soft-tissue injuries like sprains and strains in the hours and days afterwards."
      },
      {
        type: "short",
        marks: 6,
        prompt: "List the four parts of the FITT formula and apply each to a 4-week running plan.",
        model: "Frequency: progress from 3 runs/week to 4. Intensity: lift average pace from 70% MHR to 80% MHR for a portion of the run. Time: increase long-run duration from 30 to 45 minutes. Type: introduce one fartlek session per week alongside continuous running to vary the stimulus and avoid plateau."
      },
      {
        type: "short",
        marks: 5,
        prompt: "State the SMARTER goal-setting acronym and write one SMARTER goal for a club hurler.",
        model: "Specific, Measurable, Achievable, Realistic, Time-bound, Evaluated, Reviewed. Example goal: 'Raise free-taking success rate from 65% to 80% over the next 8 weeks by completing 50 frees per training session, reviewed weekly with the coach using video.'"
      }
    ];
  })();

})();