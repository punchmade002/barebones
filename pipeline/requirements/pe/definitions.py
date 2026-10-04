"""Hand-authored PE requirements. No exam-derived or card-count targets.

Rows: stable key | capability | semicolon-separated acceptance criteria
Optional columns: basis (explicit/decomposition), evidence (recall/reasoning/
application/investigation/performance/project), refresh (stable/current).
Catalogues expand explicitly named syllabus items; they do not generate questions.
"""

OUTCOMES = []
POINTS = []


def outcome(code, page, title, summary, content):
    OUTCOMES.append(dict(id=code, pdfPage=page, printedPage=page - 1,
                         title=title, requirement=summary, content=content))
    return code


def rows(parent, text):
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        cells = [c.strip() for c in line.split('|')]
        key, statement, criteria = cells[:3]
        POINTS.append(dict(id='pe26-' + key, outcomeIds=[parent], statement=statement,
                           acceptanceCriteria=[x.strip() for x in criteria.split(';') if x.strip()],
                           basis=cells[3] if len(cells) > 3 else 'explicit',
                           evidenceModes=(cells[4] if len(cells) > 4 else 'reasoning').split(','),
                           refresh=cells[5] if len(cells) > 5 else 'stable'))


def catalog(parent, prefix, entries, statement, criteria, basis='explicit', evidence='reasoning'):
    for key, term in entries:
        POINTS.append(dict(id=f'pe26-{prefix}-{key}', outcomeIds=[parent],
                           statement=statement.format(term=term),
                           acceptanceCriteria=[c.format(term=term) for c in criteria],
                           basis=basis, evidenceModes=[evidence], refresh='stable'))


o = outcome('S1.01', 15, 'Stages of skill learning',
            'Describe the stages through which skill learning progresses.',
            ['Beginner, intermediate and advanced stages.'])
catalog(o, 'learning-stage', [('beginner','beginner'),('intermediate','intermediate'),('advanced','advanced')],
        'Describe the {term} stage of skill learning.',
        ['Describe observable performance and learning characteristics at the {term} stage.',
         'Use a physical-activity example to distinguish this stage from the other stages.'])
rows(o, '''
learning-progression | Explain progression between stages of learning. | Compare changes in attention, consistency and control; Use performance evidence rather than age alone to justify a learner's stage | decomposition | application
''')

o = outcome('S1.02', 15, 'Factors influencing skill learning',
            'Investigate how practice and feedback influence skill acquisition.',
            ['Feedback and practice.', 'Whole, part, variable, fixed, massed, distributed and random practice.'])
catalog(o, 'practice', [(x,x) for x in ['whole','part','variable','fixed','massed','distributed','random']],
        'Explain and select {term} practice for a learning task.',
        ['Describe how {term} practice is organised.', 'Give an activity-specific example.',
         'Explain its advantages and limitations for the learner, skill and stage of learning.'])
rows(o, '''
learning-feedback | Investigate how feedback affects skill learning. | Identify the feedback supplied and the learning task; Explain how feedback guides correction and refinement; Use observations or comparison evidence to judge its usefulness | explicit | investigation
practice-investigation | Investigate the effect of a practice approach on learning. | Identify the learner, skill, practice method and success measure; Collect and compare performance evidence; Consider other factors and limitations before drawing a conclusion | explicit | investigation
practice-selection | Choose and justify practice methods for contrasting learning needs. | Compare suitable alternatives; Relate the choice to the skill, learner and available time; Explain how the choice would change as the learner progresses | decomposition | application
''')

o = outcome('S1.03', 15, 'Designing effective practice',
            'Design sessions and schedules using principles of effective practice for a selected activity.',
            ['Variety, progressive, specific, measurable, achievable, realistic, time, exciting, challenging and recorded.'])
catalog(o, 'practice-principle', [('variety','variety'),('progressive','progression'),('specific','specificity'),
        ('measurable','measurability'),('achievable','achievability'),('realistic','realism'),('time','time'),
        ('exciting','excitement and engagement'),('challenging','challenge'),('recorded','recording')],
        'Apply {term} in practice design.',
        ['Explain what {term} contributes to effective practice.',
         'Show an identifiable design decision applying this principle to a selected skill.'])
rows(o, '''
practice-session-design | Design a coherent practice session for a selected activity. | State the learner's starting point and performance goal; Specify tasks, progression, time, feedback and measures of success; Justify the design using practice principles | explicit | application
practice-schedule-design | Plan a sequence of practice sessions. | Sequence sessions towards a performance goal; Include review points and evidence recording; Explain how the schedule will adapt to progress | explicit | application
''')

o = outcome('S1.04', 15, 'Evaluating effective practice',
            'Evaluate the contribution of effective-practice principles.',
            ['Evaluate the principles shared with outcome S1.03, rather than only naming them.'])
rows(o, '''
practice-evaluation | Evaluate a practice plan against effective-practice principles. | Assess the use of all relevant principles from S1.03; Link strengths and limitations to learning evidence; Justify improvements and acknowledge trade-offs | explicit | reasoning
practice-review | Evaluate whether practice improved the intended skill. | Compare initial and subsequent performance using consistent criteria; Distinguish evidence of improvement from attendance alone; Recommend a justified change to subsequent practice | decomposition | investigation
''')

o = outcome('S1.05', 15, 'Sport skills and decisions',
            'Demonstrate skills and tactical decisions across varied physical activities.',
            ['Refinement of skill and technique; application of tactics and decision making.',
             'Gross, fine, open, closed, discrete, serial, continuous, internally paced and externally paced skills.'])
catalog(o, 'skill-class', [(x.replace(' ','-'),x) for x in ['gross','fine','open','closed','discrete','serial','continuous','internally paced','externally paced']],
        'Recognise and apply the {term} classification of skill.',
        ['Explain the defining feature of a {term} skill.',
         'Classify an activity-specific example and justify the classification.',
         'Explain a consequence for practice or performance.'])
rows(o, '''
skill-refinement | Refine the execution of a selected skill. | Identify a specific technical improvement using appropriate criteria; Apply feedback in practice; Demonstrate and review the change in execution | explicit | performance
tactical-decisions | Demonstrate appropriate tactical decisions in varied activities. | Identify relevant cues and possible actions; Select and execute a response suited to the situation; Explain and adapt the decision when the situation changes | explicit | performance
''')

o = outcome('S1.06', 15, 'Characteristics of skilled performance',
            'Identify observable characteristics of skilled performance.',
            ['Kinaesthetic awareness, anticipation, consistency and accuracy of movement or technique.'])
catalog(o, 'skilled-performance', [('kinaesthetic-awareness','kinaesthetic awareness'),('anticipation','anticipation'),
        ('consistency','consistency'),('accuracy','accuracy')],
        'Explain and recognise {term} in skilled performance.',
        ['Explain {term} in the context of movement.',
         'Identify observable evidence in a selected performance.',
         'Explain how it contributes to successful performance.'])

o = outcome('S1.07', 15, 'Skill and ability',
            'Discuss how learned skill differs from ability.', ['Skill and ability, including their relationship in learning and performance.'])
rows(o, '''
skill-versus-ability | Distinguish skill from ability and explain their relationship. | Explain both terms without treating them as synonyms; Use a relevant example of each; Discuss how ability and learning interact in developing performance | explicit | reasoning
''')

o = outcome('S1.08', 15, 'Critical analysis of skill',
            'Analyse skill performance critically to identify and justify improvements.',
            ["Newton's first, second and third laws.", 'Skill-analysis checklists, coaching points, video-analysis software and model performers.',
             'Economy of movement and creative use of skill.'])
catalog(o, 'newton', [('inertia',"Newton's first law (inertia)"),('acceleration',"Newton's second law (acceleration)"),
        ('action-reaction',"Newton's third law (action and reaction)")],
        'Apply {term} to analyse a movement.',
        ['Explain the law accurately.', 'Identify the relevant forces, objects and movement in an activity example.',
         'Use the law to justify a technical improvement.'])
catalog(o, 'skill-analysis-tool', [('checklist','a skill-analysis checklist'),('coaching-points','key coaching points'),
        ('video','video-analysis software'),('model','a model performer')],
        'Use {term} to analyse skill execution.',
        ['Select appropriate performance criteria and explain the tool or reference.',
         'Identify strengths and a specific technical weakness from evidence.',
         'Justify an improvement while considering limitations of the analysis.'], evidence='application')
rows(o, '''
movement-economy | Analyse economy of movement. | Explain movement economy; Identify unnecessary or inefficient movement in an example; Justify a change that preserves effective performance | explicit | application
skill-creativity | Analyse creative application of a skill. | Identify how a skill is adapted to a new or changing situation; Explain the purpose and suitability of the adaptation; Evaluate its effectiveness from performance evidence | explicit | application
skill-critical-analysis | Produce an evidence-based analysis of a skill and a plan to improve it. | Describe the skill and performance criteria; Combine observations with relevant mechanical principles; Justify prioritised improvements and a way to reassess them | explicit | investigation
''')

o = outcome('S1.09', 16, 'Aesthetic and artistic movement',
            'Appraise and compare aesthetic and artistic criteria in movement.',
            ['Create and participate in a group performance.', 'Aesthetic and artistic criteria across different activities.', 'Methods for analysing choreography.'])
rows(o, '''
aesthetic-artistic-criteria | Explain aesthetic and artistic criteria for movement. | Distinguish qualities of movement from expressive or creative intentions where appropriate; Identify relevant criteria for an activity; Explain how those criteria can be observed | explicit | reasoning
aesthetic-comparison | Compare criteria across contrasting activities. | Use appropriate criteria for each activity; Identify meaningful similarities and differences; Explain why identical criteria cannot always be applied unchanged | explicit | application
choreography-analysis | Analyse choreography using an appropriate method. | Select criteria and a recording or observation method; Relate movement choices to artistic intent and execution; Support judgements with specific evidence | explicit | investigation
group-performance | Create and take part in a group performance. | Contribute to planning and rehearsing the composition; Demonstrate coordinated participation; Review the group's performance against agreed artistic and aesthetic criteria | explicit | performance
''')

o = outcome('S1.10', 16, 'Body responses to physical activity',
            'Investigate physiological responses to participation in physical activity.',
            ['Functions and roles of the cardiovascular and respiratory systems.', 'Measure and monitor heart rate, breathing and body temperature.'])
rows(o, '''
cardiovascular-function | Explain how the cardiovascular system supports physical activity. | Identify the roles of the heart, blood and blood vessels; Explain transport to and from working tissues; Relate changes in activity demand to cardiovascular response | explicit | reasoning
respiratory-function | Explain how the respiratory system supports physical activity. | Describe ventilation and gas exchange at a relevant level; Explain the supply of oxygen and removal of carbon dioxide; Relate breathing responses to activity demand | explicit | reasoning
cardiorespiratory-integration | Explain how the cardiovascular and respiratory systems work together. | Trace the movement of oxygen to working muscles and carbon dioxide away from them; Explain how coordinated responses support activity | decomposition | reasoning
heart-rate-response | Measure and interpret heart-rate responses to activity. | Use an appropriate measurement method; Record comparable resting, activity and recovery observations; Explain patterns and measurement limitations | explicit | investigation
breathing-response | Measure and interpret breathing responses to activity. | State what aspect of breathing is measured and how; Record comparable observations; Explain patterns and limitations | explicit | investigation
temperature-response | Monitor and explain body-temperature responses to activity. | Use an appropriate safe monitoring approach; Distinguish measurement from subjective perception; Explain the observed response and limits of the evidence | explicit | investigation
body-response-investigation | Conduct an investigation of body responses to activity. | Define the activity conditions and measures; Collect and present data safely; Explain results using physiology and consider confounding factors | explicit | investigation
''')

o = outcome('S1.11', 16, 'Physical activity across life stages',
            'Assess participation in physical activity across the life course.',
            ['Infancy, childhood, adolescence, adulthood and older adulthood.',
             'Physical-health, mental-health, social and economic benefits at different stages.'])
catalog(o, 'life-stage', [('infancy','infancy'),('childhood','childhood'),('adolescence','adolescence'),
        ('adulthood','adulthood'),('older-adulthood','older adulthood')],
        'Assess being physically active during {term}.',
        ['Explain age- and context-appropriate participation opportunities and needs.',
         'Consider physical, mental, social and economic benefits at this stage.',
         'Use examples without assuming identical abilities or circumstances for everyone.'])
catalog(o, 'activity-benefit', [('physical','physical-health'),('mental','mental-health'),('social','social'),('economic','economic')],
        'Explain {term} benefits of physical activity across life stages.',
        ['Explain a plausible link between participation and the benefit.',
         'Use examples at contrasting life stages.', 'Distinguish individual benefits from wider community effects where relevant.'])

o = outcome('S2.01', 17, 'Fitness components, assessment and methods',
            'Apply fitness components to the demands of physical-activity performance.',
            ['Health-related and performance-related fitness and their relevance to activities.',
             'Appropriate fitness tests, their validity and reliability.',
             'Continuous, interval, fartlek, circuit, resistance, plyometric and stretching methods.'])
rows(o, '''
fitness-categories | Distinguish health-related and performance-related fitness. | Explain the purpose of each category; Classify the main components accurately; Explain that both can contribute to an activity | explicit | reasoning
''')
catalog(o, 'fitness-component', [('cardiorespiratory-endurance','cardiorespiratory endurance'),('muscular-endurance','muscular endurance'),
        ('strength','muscular strength'),('flexibility','flexibility'),('body-composition','body composition'),
        ('agility','agility'),('balance','balance'),('coordination','coordination'),('power','power'),('speed','speed'),('reaction-time','reaction time')],
        'Explain and apply {term} as a fitness component.',
        ['Define the component and distinguish it from related components.',
         'Explain its contribution to a specific activity or role.',
         'Identify a suitable way to assess and develop it, with limitations.'], basis='decomposition')
rows(o, '''
fitness-needs-analysis | Analyse the fitness demands of an activity and performer. | Identify relevant components for the activity and role; Justify their relative importance; Identify individual strengths and development needs from evidence | explicit | application
fitness-test-selection | Select appropriate fitness tests and a test battery. | Match each test to the component and activity need; Explain safe protocols and recorded measures; Justify feasibility and suitability for the performer | explicit | application
fitness-test-validity | Evaluate the validity of a fitness test. | Explain whether the test measures the intended component; Consider relevance to the activity and performer; Identify limitations in conclusions drawn from the test | explicit | reasoning
fitness-test-reliability | Evaluate and improve the reliability of fitness testing. | Explain repeatability; Identify protocol, equipment and participant factors affecting consistency; Propose standardisation and interpret repeated measures | explicit | reasoning
fitness-test-data | Use fitness-test results to inform training decisions. | Present results with suitable units and context; Interpret strengths and limitations without unsupported labels; Use the results to justify training priorities | decomposition | investigation
''')
catalog(o, 'training-method', [('continuous','continuous training'),('interval','interval training'),('fartlek','fartlek training'),
        ('circuit','circuit training'),('resistance','resistance training'),('plyometric','plyometric training'),('stretching','stretching')],
        'Select and apply {term} to a fitness goal.',
        ['Describe how the method is organised.', 'Link the method to relevant fitness components and activity demands.',
         'Give a suitable example and explain advantages, limitations and safe adaptation.'])
rows(o, '''
training-method-comparison | Compare training methods for different activity demands. | Compare methods using the same performer and goal; Explain trade-offs rather than ranking a method as universally best; Justify a suitable combination | decomposition | application
''')

o = outcome('S2.02', 17, 'Training principles and FITT',
            'Apply principles of training to pursue optimum performance.',
            ['Readiness, specificity, progressive overload, rest, recovery, reversibility and tedium.',
             'FITT: frequency, intensity, time and type.'])
catalog(o, 'training-principle', [('readiness','readiness'),('specificity','specificity'),('progressive-overload','progressive overload'),
        ('rest','rest'),('recovery','recovery'),('reversibility','reversibility'),('tedium','tedium')],
        'Apply {term} to a training programme.',
        ['Explain the principle.', 'Show a concrete programme decision applying it.',
         'Explain how inappropriate application can undermine the goal or the performer.'])
catalog(o, 'fitt', [('frequency','frequency'),('intensity','intensity'),('time','time'),('type','type')],
        'Use {term} within the FITT framework.',
        ['Explain and specify this training variable using appropriate units or descriptors.',
         'Justify it for the performer, fitness component and goal.',
         'Explain how changing it affects overall programme demands.'])
rows(o, '''
training-programme-design | Design and justify a programme combining FITT and training principles. | Start from assessed needs and a performance goal; Specify a coherent progression of training; Explain individualisation and how progress will be monitored | explicit | application
''')

o = outcome('S2.03', 17, 'Recovery, overtraining and periodisation',
            'Discuss recovery strategies and apply periodisation in programme design.',
            ['Recovery strategies and overtraining.', 'Role and application of periodisation.', 'Integrating recovery and periodisation into training.'])
rows(o, '''
recovery-strategies | Compare recovery strategies for training and performance. | Explain the purpose of recovery; Compare suitable strategies in context; Justify choices and recognise limits of the evidence | explicit | reasoning
overtraining | Explain overtraining and recognise when a programme needs review. | Explain the imbalance between load and recovery; Interpret relevant changes in performance or wellbeing cautiously; Propose adjustments and appropriate support rather than diagnose from one symptom | explicit | application
periodisation | Explain the purpose and organisation of periodisation. | Describe planned variation over time; Relate training phases to goals and competition or performance demands; Explain where recovery is incorporated | explicit | reasoning
periodised-plan | Design a periodised programme with recovery built in. | Set a relevant time horizon and performance goal; Sequence training emphasis, progression and recovery; Justify adaptations using monitoring information | explicit | application
''')

o = outcome('S2.04', 17, 'Psychological preparedness and assessment',
            'Analyse psychological factors affecting practice and performance.',
            ['Confidence, anxiety, motivation and concentration.', 'Self-assessment, observation, interviews and questionnaires.'])
catalog(o, 'psychological-factor', [('confidence','confidence'),('anxiety','anxiety'),('motivation','motivation'),('concentration','concentration')],
        'Analyse how {term} affects practice and performance.',
        ['Explain the factor and recognise it in context.', 'Explain how it can influence practice and performance.',
         'Use evidence and acknowledge that responses vary between people and situations.'])
catalog(o, 'psychological-assessment', [('self-assessment','self-assessment'),('observation','observation'),
        ('interview','interview techniques'),('questionnaire','questionnaires')],
        'Use {term} to investigate psychological preparedness.',
        ['Select an appropriate approach for the factor and performer.',
         'Collect and interpret evidence responsibly.',
         'Explain limitations such as bias, context or inconsistent measures.'], evidence='investigation')

o = outcome('S2.05', 17, 'Psychological strategies and feedback',
            'Evaluate psychological strategies and feedback before, during and after participation.',
            ['Goal setting, self-talk, thought stopping, visualisation, relaxation and performance routines, including benefits and drawbacks.',
             'Intrinsic, extrinsic, knowledge of results, knowledge of performance, concurrent, terminal, positive and negative feedback.'])
catalog(o, 'psychological-strategy', [('goal-setting','goal setting'),('self-talk','self-talk'),('thought-stopping','thought stopping'),
        ('visualisation','visualisation'),('relaxation','relaxation'),('routine','performance routines')],
        'Evaluate the use of {term} in psychological preparation.',
        ['Explain the strategy and give an activity-specific application.',
         'Justify when it may be used before, during or after participation.',
         'Assess benefits, drawbacks and suitability for the individual.'])
catalog(o, 'feedback', [('intrinsic','intrinsic'),('extrinsic','extrinsic'),('results','knowledge of results'),
        ('performance','knowledge of performance'),('concurrent','concurrent'),('terminal','terminal'),
        ('positive','positive'),('negative','negative')],
        'Explain and evaluate {term} feedback.',
        ['Distinguish this feedback type from related types.', 'Give a clear example in practice or performance.',
         'Evaluate its timing, usefulness and possible drawbacks for the learner.'])
rows(o, '''
feedback-combination | Select an appropriate combination of feedback for a performer. | Explain that feedback categories describe different dimensions and may overlap; Relate the combination to skill stage, task and psychological needs; Justify delivery and timing | decomposition | application
''')

o = outcome('S2.06', 18, 'Psychological action plans',
            'Investigate personal action plans grounded in psychological principles.',
            ['Use assessment data for confidence, concentration, motivation and anxiety.',
             'Select suitable strategies before, during and after physical activity.'])
rows(o, '''
psychological-data-to-goals | Use psychological assessment data to set personal goals. | Interpret evidence for relevant psychological factors; Identify a priority with a clear rationale; Set a goal and a way to measure change | explicit | investigation
psychological-action-plan | Design and investigate a personal psychological action plan. | Match strategies to assessed needs; Specify actions before, during and after activity; Explain the psychological rationale and how the plan will be monitored | explicit | investigation
psychological-plan-evaluation | Evaluate and adapt a psychological action plan. | Compare follow-up evidence with baseline and goals; Consider other influences and limitations; Retain or modify strategies with reasons | decomposition | investigation
''')

o = outcome('S2.07', 18, 'Nutrition and physical performance',
            'Examine how nutrition supports performance.',
            ['Macronutrients, micronutrients and hydration.', 'Nutrient timing for performance and recovery; nutritional planning.',
             'Roles, benefits and challenges of caffeine, creatine, nitrate, beta-alanine and sodium bicarbonate supplements.'])
catalog(o, 'nutrient', [('carbohydrate','carbohydrate'),('protein','protein'),('fat','fat'),('vitamins','vitamins'),('minerals','minerals')],
        'Explain the relevance of {term} to physical performance.',
        ['Identify the nutrient category and its relevant functions.',
         'Give suitable food-source examples.', 'Explain its role in meeting activity and recovery needs without assuming identical needs for all performers.'], basis='decomposition')
rows(o, '''
hydration | Examine hydration needs in physical activity. | Explain why fluid balance matters; Relate needs to activity, environment and the individual; Evaluate a sensible hydration approach using reliable guidance | explicit | reasoning | current
nutrition-before | Explain nutrition choices before participation. | Relate food and fluid choices to the activity and timing; Consider energy availability, tolerance and individual needs; Justify choices rather than prescribing one universal meal | explicit | application
nutrition-during | Explain nutrition choices during participation. | Relate needs to duration, intensity and conditions; Explain when food or fluid intake may be relevant; Justify a suitable approach | explicit | application
nutrition-after | Explain nutrition choices after participation. | Relate choices to recovery and future demands; Consider replenishment, repair and rehydration; Justify timing and suitable choices | explicit | application
nutrition-plan | Design and justify a performance-related nutritional plan. | Consider activity demands and the individual's context; Include nutrition and hydration before, during and after activity; Give a reasoned explanation and identify where qualified guidance is needed | explicit | application
''')
catalog(o, 'supplement', [('caffeine','caffeine'),('creatine','creatine'),('nitrate','nitrate'),('beta-alanine','beta-alanine'),
        ('sodium-bicarbonate','sodium bicarbonate')],
        'Examine the role, possible benefits and challenges of {term} as a sports supplement.',
        ['Explain its proposed performance role and the activity contexts in which it is considered.',
         'Evaluate evidence, limitations and risks using current authoritative guidance.',
         'Distinguish learning about a supplement from recommending personal use.'])
for point in POINTS:
    if point['id'].startswith('pe26-supplement-'):
        point['refresh'] = 'current'
rows(o, '''
supplement-decisions | Critically assess claims about sports supplements. | Distinguish food, supplement and prohibited-substance issues; Consider evidence quality, product risks and suitability; Explain why a performance claim alone does not justify use | decomposition | reasoning | current
''')

o = outcome('S2.08', 18, 'Energy systems',
            'Analyse the role and relative contribution of energy systems during activity.',
            ['ATP-PC/alactic, anaerobic lactic and aerobic/oxidative systems.',
             'Duration, intensity, fuel source, by-products and activity type.'])
catalog(o, 'energy-system', [('atp-pc','ATP-PC (alactic) system'),('anaerobic-lactic','anaerobic lactic system'),
        ('aerobic','aerobic (oxidative) system')],
        'Explain the role of the {term} during activity.',
        ['Describe its role in ATP supply, fuel source and relevant by-products.',
         'Relate its contribution to activity intensity and duration.',
         'Use an activity example without implying that only one system operates.'])
rows(o, '''
energy-system-interaction | Analyse changing relative contributions of the energy systems. | Compare demands at different intensities, durations and stages of an activity; Explain contributions using the activity rather than rigid on/off time boundaries; Interpret a suitable example or data representation | explicit | application
energy-systems-preparation | Use energy-system analysis to justify preparation and recovery. | Identify relevant activity demands; Connect those demands to training, nutrition or recovery decisions; Explain the reasoning and avoid a one-system-only model | decomposition | application
''')

o = outcome('S2.09', 18, 'Muscular and skeletal systems in movement',
            'Recognise how muscular and skeletal systems support human movement.',
            ['Relevant muscle groups, bones and joint actions.', 'Muscular and skeletal functions in movement.',
             'Planes and axes in anatomical movement.'])
rows(o, '''
muscular-functions | Explain muscular-system functions relevant to movement. | Relate muscle action to force and movement; Explain coordinated action across a relevant muscle group; Apply the explanation to a selected activity | explicit | reasoning
skeletal-functions | Explain skeletal-system functions relevant to movement. | Explain support, joint structure and movement-related functions; Relate bones and joints to a selected movement; Distinguish skeletal structures from muscle actions | explicit | reasoning
movement-muscles | Identify relevant muscle groups in a selected movement. | Locate and name the muscles required by the chosen example; Describe their contribution to that movement; Link the anatomy to a technique or movement analysis | explicit | application
movement-bones | Identify relevant bones and joints in a selected movement. | Locate and name the structures required by the chosen example; Relate their arrangement to the movement; Use appropriate anatomical terminology | explicit | application
joint-actions | Identify and explain joint actions in physical activity. | Identify the joint and action in each relevant phase of a movement; Use correct movement terminology; Explain how the actions contribute to the overall skill | explicit | application
planes-axes | Analyse movement using anatomical planes and axes. | Distinguish a plane from an axis; Identify the appropriate plane-axis relationship for a movement; Justify the classification using the direction of movement | explicit | application
''')
catalog(o, 'anatomical-plane', [('sagittal','sagittal plane'),('frontal','frontal plane'),('transverse','transverse plane')],
        'Recognise movement in the {term}.',
        ['Describe the plane using anatomical orientation.', 'Identify its perpendicular axis.',
         'Give and explain a physical-activity example.'], basis='decomposition')
catalog(o, 'joint-action', [('flexion-extension','flexion and extension'),('abduction-adduction','abduction and adduction'),
        ('rotation','rotation'),('circumduction','circumduction'),('ankle','dorsiflexion and plantar flexion')],
        'Recognise {term} in movement.',
        ['Describe the action or contrasting actions accurately.',
         'Identify an appropriate joint and an activity example.',
         'Connect the movement to its muscular and skeletal context.'], basis='decomposition')

o = outcome('S2.10', 18, 'Planning for optimum performance',
            'Analyse the factors and evidence used to plan for optimum performance.',
            ['Factors affecting performance; performance analysis; goals; evidence-based improvement planning; programme effectiveness; communication.'])
rows(o, '''
performance-factors | Analyse interacting factors affecting a performer's performance. | Consider relevant skill, tactical, physical, psychological and nutritional factors; Explain interactions rather than present an isolated list; Prioritise factors using evidence | explicit | application
performance-baseline | Establish a defensible performance baseline. | Select relevant criteria and analysis methods; Gather and interpret evidence; Identify strengths, development needs and measurement limitations | explicit | investigation
performance-goals | Set justified performance goals from analysis. | Link each goal to an evidenced need; Make success and review timing observable; Explain feasibility and priorities | explicit | application
performance-improvement-plan | Design an improvement plan from collected evidence. | Link actions to goals and underlying PE principles; Specify practice or training, progression and monitoring; Explain why the plan suits the performer | explicit | application
programme-effectiveness | Evaluate the effectiveness of a performance programme. | Compare outcomes to baseline and goals; Use evidence to explain progress or lack of progress; Identify limitations and justified next changes | explicit | investigation
performance-communication | Communicate performance analysis and planning clearly. | Use accurate PE terminology; Present relevant evidence in an appropriate form; Explain recommendations coherently for the intended audience | explicit | application
''')

o = outcome('S2.11', 18, 'High-performance sport in Ireland',
            'Analyse provision and support for high-performance sport in Ireland.',
            ['Pathways to high performance; underage player-development programmes.',
             'Sport Ireland and national governing bodies at local, national and international levels.'])
rows(o, '''
high-performance-pathways | Analyse a pathway to high performance in a selected activity. | Describe relevant stages and access routes; Explain available support and barriers; Evaluate how effectively the pathway supports development | explicit | investigation | current
underage-development | Analyse an underage player-development programme. | Explain its purpose, structure and intended participants; Examine how development and progression are supported; Evaluate provision using current evidence | explicit | investigation | current
sport-ireland | Explain and evaluate Sport Ireland's role in high-performance provision. | Identify relevant responsibilities and supports; Distinguish its role from that of individual governing bodies; Use current examples and evaluate contribution | explicit | reasoning | current
governing-bodies | Analyse governing-body support at local, national and international levels. | Identify the relevant bodies for a selected activity; Explain their roles and relationships; Evaluate provision and gaps with current evidence | explicit | investigation | current
''')

o = outcome('S3.01', 19, 'Safe practice and organisation',
            'Examine safe approaches to participation, performance and activity organisation.',
            ['Rules and regulations; safety regulations.', 'Warm-up and cool-down, including injury prevention.',
             'Safe use and maintenance of attire, facilities and equipment.'])
rows(o, '''
activity-rules | Explain and apply rules and regulations of a selected activity. | Identify relevant rules and their purposes; Apply them to a scenario; Use current governing-body rules where details can change | explicit | application | current
safety-regulations | Apply relevant safety regulations to activity organisation. | Identify applicable safety requirements; Explain responsibilities and practical checks; Justify a response to a safety concern | explicit | application | current
warm-up | Explain and plan a suitable warm-up. | Connect preparation to the activity and participants; Explain the purpose of each element; Discuss injury-risk reduction without claiming guaranteed prevention | explicit | application
cool-down | Explain and plan a suitable cool-down. | Relate the plan to the preceding activity and performer; Explain purposes using supported physiological reasoning; Avoid unsupported claims that it guarantees prevention of soreness or injury | explicit | application
safe-attire | Assess the suitability and maintenance of activity attire. | Match clothing or protective kit to activity needs; Check fit, condition and relevant rules; Explain action when equipment is unsuitable | explicit | application
safe-equipment | Assess safe use and maintenance of activity equipment. | Identify activity-specific checks; Explain correct use and maintenance responsibilities; Respond appropriately to a defect | explicit | application
safe-facilities | Assess facilities and the environment for safe participation. | Identify relevant hazards and controls; Consider the participants and activity; Explain checks before and during participation | explicit | application
safe-event | Plan safe organisation of a physical activity. | Integrate rules, roles, equipment, facilities and participant needs; Specify checks and responses to foreseeable problems; Explain how the plan supports safe participation | explicit | application
''')

o = outcome('S3.02', 19, 'Structures, tactics and composition',
            'Apply structures, tactics and compositional elements across physical activities.',
            ['Structures, tactics and composition used to outperform opponents, control situations or express creativity.'])
rows(o, '''
activity-structures | Explain and apply structures in physical activity. | Describe the organisation or formation; Explain individual roles and relationships; Demonstrate how the structure supports an activity objective | explicit | performance
activity-tactics | Apply and adapt tactics to outperform opponents or control situations. | Identify cues, options and opponent strengths or weaknesses; Select and execute a justified tactic; Adapt it and review its effect | explicit | performance
composition-elements | Apply compositional elements creatively in physical activity. | Identify relevant elements such as space, timing and relationships; Combine them purposefully in a performance; Explain and evaluate the effect | explicit | performance
strategy-transfer | Compare and adapt approaches across contrasting physical activities. | Explain how context changes the suitability of a structure, tactic or composition; Apply an approach to more than one activity; Justify adaptations using activity-specific evidence | decomposition | application
''')

o = outcome('S3.03', 19, 'Officiating',
            'Describe the knowledge, preparation and interpersonal demands of officiating.',
            ['Knowledge, physical fitness, psychological readiness, attire and equipment.',
             'Effective-official characteristics, communication styles and conflict management.'])
catalog(o, 'official-readiness', [('knowledge','activity and rules knowledge'),('fitness','physical fitness'),
        ('psychological','psychological readiness'),('attire','personal attire'),('equipment','equipment')],
        'Explain the officiating requirement for {term}.',
        ['Describe the requirement in a selected activity.', 'Explain how it supports effective and fair officiating.',
         'Give a preparation or checking example.'])
rows(o, '''
official-characteristics | Describe characteristics of an effective official. | Identify appropriate personal and professional qualities; Explain their effects on fair and safe activity; Support the explanation with a scenario | explicit | reasoning
official-communication | Evaluate communication styles used by officials. | Compare relevant verbal and non-verbal approaches; Select an appropriate style for a situation; Explain clarity, respect and assertiveness | explicit | application
official-conflict | Explain and apply conflict-management strategies in officiating. | Identify the conflict and relevant rules or responsibilities; Propose a proportionate communication and management response; Explain how fairness and safety are maintained | explicit | application
''')

o = outcome('S3.04', 19, 'Coaches and choreographers',
            'Explore how coaches and choreographers guide performance and reflection.',
            ['Physical, personal and technical knowledge.', 'Guidance towards optimum performance.', 'Strategies supporting ongoing performer reflection.'])
catalog(o, 'coach-knowledge', [('physical','physical'),('personal','personal'),('technical','technical')],
        'Explain the {term} knowledge and qualities needed by a coach or choreographer.',
        ['Describe the requirement in a relevant activity context.',
         'Explain how it supports the performer.', 'Use a concrete coaching or choreography example.'])
rows(o, '''
coach-guidance | Plan how to guide a performer towards optimum performance. | Establish needs and goals collaboratively; Select suitable practice, feedback and support; Explain monitoring and adaptation | explicit | application
coach-reflection | Use strategies to support ongoing performer reflection. | Prompt the performer to examine evidence and decisions; Connect reflection to future practice; Explain how the coach supports increasing performer independence | explicit | application
''')

o = outcome('S3.05', 19, 'Ethical practice',
            'Examine ethical principles and factors influencing ethical practice in sport.',
            ['Integrity, respect, fairness, equity and codes of ethics.', 'Sportsmanship, gamesmanship and their relationship to participation.'])
catalog(o, 'ethics', [('integrity','integrity'),('respect','respect'),('fairness','fairness'),('equity','equity')],
        'Apply {term} as a principle of ethical practice.',
        ['Explain the principle and distinguish it from related principles where appropriate.',
         'Apply it to a sporting decision or dilemma.', 'Justify the effect on participants and fair participation.'])
rows(o, '''
codes-of-ethics | Examine a code of ethics for a physical activity. | Identify responsibilities of relevant stakeholders; Apply the code to a scenario; Evaluate how a code supports ethical participation in practice | explicit | application | current
sportsmanship | Explain sportsmanship and its effect on engagement. | Explain the concept; Identify an activity-specific example; Discuss effects on participants and the sporting environment | explicit | reasoning
gamesmanship | Explain gamesmanship and its effect on engagement. | Distinguish it from sportsmanship and rule-breaking; Analyse an example; Discuss ethical tensions and effects on participation | explicit | reasoning
ethical-influences | Analyse factors that influence ethical choices in sport. | Identify relevant personal, social or competitive pressures; Consider stakeholder perspectives and competing values; Justify a response using ethical principles | explicit | application
''')

o = outcome('S3.06', 20, 'Performance-enhancing drugs and regulation',
            'Discuss performance-enhancing drugs and doping regulation.',
            ['Drug categories; implications for performer and sport.', 'Irish anti-doping rules and enforcement.', 'Therapeutic use exemptions.'])
rows(o, '''
doping-categories | Describe categories of performance-enhancing drugs using current sources. | Distinguish relevant categories and give verified examples; Explain their intended performance effects; Separate performance claims from health risks and prohibited status | explicit | reasoning | current
doping-performer | Analyse implications of doping for the performer. | Consider health, sanctions, reputation and ethical responsibilities; Explain consequences with reliable evidence; Avoid treating potential performance gain as justification | explicit | reasoning | current
doping-sport | Analyse implications of doping for sport and its participants. | Consider fairness, trust and effects on other participants; Explain wider consequences for an activity or organisation; Support a balanced judgement | explicit | reasoning | current
irish-anti-doping | Explain current Irish anti-doping rules and enforcement. | Use current official Irish anti-doping guidance; Explain relevant responsibilities, testing and enforcement processes; Apply requirements to a scenario without relying on stale rules | explicit | application | current
therapeutic-use-exemption | Explain therapeutic use exemptions in sport. | Explain purpose and the relationship to prohibited medicines; Describe the relevant official application or verification process; Apply the distinction between medical need and automatic permission | explicit | reasoning | current
''')

o = outcome('S3.07', 20, 'Technology in physical activity',
            'Discuss the effects of technological developments on physical activity.',
            ['Impacts on performers, coaches/choreographers, officials and spectators.',
             'Optimising performance and personal use of technology.'])
catalog(o, 'technology-impact', [('performer','performers'),('coach','coaches and choreographers'),
        ('official','officials'),('spectator','spectators')],
        'Evaluate technological developments from the perspective of {term}.',
        ['Explain a relevant technology and its use.', 'Analyse benefits and limitations for this stakeholder.',
         'Use an activity-specific example and consider access or fairness where relevant.'])
rows(o, '''
technology-performance | Evaluate technology used to optimise performance. | Explain what information or capability it provides; Assess usefulness and limitations; Connect its use to an evidence-based performance decision | explicit | application
personal-technology | Review personal use of technology in physical activity. | Explain the purpose and actual use; Evaluate the information or feedback obtained; Justify continued use, adaptation or an alternative | explicit | investigation
''')

o = outcome('S3.08', 20, 'Media, body image and sponsorship',
            'Appreciate how media and sponsorship influence physical activity and sport.',
            ['Media coverage and participation, including different gender groups.',
             'Body-image portrayals and participation.', 'Sport-related sponsorship messages.', 'Strategies to improve media coverage.'])
rows(o, '''
media-participation | Analyse how media coverage can affect participation. | Examine the amount, type or framing of coverage; Explain effects for different gender groups; Use evidence and distinguish association from unsupported causal claims | explicit | investigation
media-body-image | Analyse how media portrayals of body image influence participation. | Identify relevant representations and messages; Explain possible effects on confidence, belonging or participation; Consider different experiences and avoid assuming one effect for everyone | explicit | reasoning
sponsorship-messages | Analyse sport-related sponsorship messages and participation implications. | Identify the sponsor's message and intended audience; Explain possible benefits and tensions; Evaluate implications for participation and sport | explicit | application
media-coverage-strategies | Evaluate strategies to improve coverage of physical activity. | Identify an evidenced coverage gap and target audience; Propose practical strategies; Explain how impact and unintended effects could be assessed | explicit | application
''')

o = outcome('S3.09', 20, 'Access, inclusion and lifelong participation',
            'Examine factors affecting access, inclusion, participation and performance throughout life.',
            ['Participation barriers and supports.', 'Measuring and tracking activity participation.',
             'Promotion, lifestyle activity, and cultural attitudes, values and traditions.'])
rows(o, '''
participation-barriers | Analyse barriers to access, participation and performance. | Identify barriers in an individual's or group's context; Explain how barriers interact across personal, social and environmental circumstances; Distinguish evidence from assumptions about groups | explicit | application
participation-supports | Analyse supports for access, inclusion and performance. | Identify supports relevant to an individual or group; Explain how each addresses a need; Evaluate accessibility and limitations | explicit | application
participation-measurement | Measure and track participation in physical activity. | Select suitable measures and collection methods; Record and interpret patterns responsibly; Discuss accuracy, bias and limitations | explicit | investigation
participation-promotion | Explain how promotion can influence participation. | Identify an audience and desired change; Explain a plausible route from promotion to engagement; Distinguish awareness from sustained participation | explicit | reasoning
lifestyle-activity | Explain lifestyle physical activity and its contribution to participation. | Distinguish everyday activity from organised exercise or sport; Give context-appropriate examples; Evaluate opportunities and barriers to maintaining it | explicit | reasoning
cultural-attitudes | Examine how cultural attitudes affect participation. | Identify a relevant attitude without stereotyping a whole population; Explain its influence on access, participation or performance; Use evidence and consider variation | explicit | reasoning
cultural-values | Examine how cultural values affect participation. | Explain a relevant value and its relationship to physical activity; Consider effects on inclusion and choices; Use contextual evidence | explicit | reasoning
cultural-traditions | Examine how cultural traditions affect participation. | Give a relevant contextual example; Explain supportive and restrictive effects where appropriate; Consider how traditions and participation can change | explicit | reasoning
lifelong-participation | Explain how participation factors interact over a person's life. | Connect changing circumstances with access, inclusion and activity choices; Consider supports for continuation or re-entry; Justify an approach suited to the individual | explicit | application
''')

o = outcome('S3.10', 20, 'Evaluating physical-activity promotion',
            'Evaluate strategies used to promote physical activity.',
            ['Gender stereotyping and adapted physical activity.', 'Tracked participation data and strategies addressing group imbalances.',
             'Barriers and supports; school-community pathways; mass-participation events.'])
rows(o, '''
gender-stereotyping | Evaluate strategies addressing gender stereotyping in physical activity. | Explain how a stereotype can influence participation; Propose a context-appropriate response; Judge the response using participation and inclusion evidence | explicit | application
adapted-activity | Evaluate adapted physical activity as a means of inclusion. | Identify participation needs and an appropriate adaptation; Explain how meaningful involvement and the activity's learning aims are retained; Assess effectiveness without assuming one adaptation fits everyone | explicit | application
participation-imbalance | Use tracked data to address participation imbalances between groups. | Identify a gap and limitations of the data; Investigate relevant barriers and supports; Propose and evaluate a targeted response | explicit | investigation
promotion-barrier-response | Evaluate a promotion strategy against the barriers and supports it addresses. | Link planned actions to evidenced needs; Explain feasibility and access; Judge effects using suitable measures rather than publicity alone | explicit | application
school-community-pathways | Evaluate ways to strengthen school-community activity pathways. | Identify a relevant transition or access gap; Explain the roles of schools, clubs or community providers; Evaluate an achievable strategy for continued participation | explicit | application
mass-participation-events | Evaluate the impact of mass-participation events. | Explain opportunities for engagement and inclusion; Consider barriers, limitations and follow-through; Use evidence to assess sustained participation rather than attendance alone | explicit | reasoning
promotion-evaluation-design | Design an evaluation of a physical-activity promotion intervention. | Specify intended outcomes and baseline measures; Collect follow-up evidence and participant perspectives; Consider limitations and recommend justified improvements | decomposition | investigation
''')

# Practical and assessment capabilities are separate from the 32 theory outcomes.
o = outcome('PRACTICE', 13, 'Learning through physical activity',
            'Participate in a broad range of activities and connect movement with theory.',
            ['Skill and technique; tactical/compositional components; fitness demands; psychological preparedness; nutrition.',
             'Focus on one or two areas while engaging with a broad range; regular active participation; progression and reflection.'])
rows(o, '''
practical-engagement | Participate actively in a broad range of physical activities. | Record or demonstrate meaningful engagement across activities; Explain how experiences connect to course learning; Focus development while retaining breadth | explicit | performance
practical-theory-transfer | Apply theoretical learning in practical activity. | Connect skill, tactics or composition, fitness, psychological preparation and nutrition to relevant experiences; Explain decisions using PE concepts; Review how application affected participation or performance | explicit | performance
practical-progression | Demonstrate progression through practical learning. | Identify a starting point and development goal; Use practice and feedback to refine performance; Reflect on evidence of progress and future needs | explicit | performance
''')

o = outcome('AAC', 24, 'Physical Education Project capabilities',
            'Demonstrate planning, engagement, skill and analysis, evaluation and communication in the project.',
            ['Pages 22–24 of the PDF: assessment structure and brief-led project process.',
             'Planning; engagement; skill proficiency and analysis; evaluation; communication.',
             'Annual SEC brief controls activity/theme selection and reporting details.'])
rows(o, '''
project-brief | Interpret the applicable project brief and its requirements. | Identify the specified activities, themes and deliverables from the actual brief; Check permitted activity and reporting requirements; Keep annual instructions distinct from stable course knowledge | explicit | project | current
project-planning | Produce justified, coherent project planning. | Use relevant needs analysis; Justify goals against the brief; Show how planning connects to later project phases | explicit | project
project-engagement | Demonstrate purposeful project engagement. | Provide evidence of sustained participation; Apply feedback and adapt the plan; Demonstrate safe and ethical engagement | explicit | project
project-skill-analysis | Demonstrate skill proficiency and analyse performance in the project. | Select and perform appropriate skills with control; Use relevant criteria and analysis tools; Explain performance demands using evidence | explicit | performance,project
project-evaluation | Evaluate project planning, activity and outcomes. | Connect experience and evidence to goals and PE concepts; Assess results and limitations; Propose justified improvements | explicit | project
project-communication | Communicate the project coherently. | Use accurate PE terminology; Present data and analysis using appropriate tools; Maintain a clear connection between project sections | explicit | project
project-eligibility | Select a project activity from the official eligible list and applicable brief. | Check the activity against Appendix 2 and the annual brief; Identify any appropriate adaptations; Retain evidence of the selection basis | explicit | project | current
''')

ELIGIBLE_ACTIVITIES = {
    'Athletics': ['Running events', 'Throwing events', 'Jumping events'],
    'Artistic and Aesthetic': ['Gymnastics', 'Dance'],
    'Aquatics': ['Swimming strokes', 'Water polo', 'Synchronised swimming'],
    'Adventure Activities': ['Orienteering', 'Kayaking', 'Indoor roped climbing', 'Water-based rowing', 'Cycling (road, mountain)'],
    'Games – Invasion': ["Gaelic football (men’s/ladies)", 'Hurling/camogie', 'Soccer', 'Rugby', 'Basketball', 'Hockey', 'Netball', 'Olympic handball'],
    'Games – Net/Wall': ['Badminton', 'Tennis', 'Volleyball', 'Table tennis', 'GAA handball', 'Squash'],
    'Games – Striking/Fielding': ['Cricket', 'Softball', 'Rounders'],
    'Games – Target/Striking': ['Golf'],
}
