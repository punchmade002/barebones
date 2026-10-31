# Leaving Cert Physical Education (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format,
  and a worked example). This outline says what to cover; that file says how to write it.
- **Information packages:** before notes are written, a higher model writes a package per
  subsection in `course-outlines/packages/pe/` (scope checklist plus checked facts). The
  writing model works from the package. Done: all 16 chapters (73 subsections), with
  subsections defined in `data.js` and notes in `content/pe/` built into `pe-notes.js`.
- **Assumed knowledge:** the specification lists outcomes, not the basics they rest on. Notes
  must also teach what a student needs to meet each outcome (`NOTES_STANDARD.md` rule 9), e.g.
  the stages-of-learning model behind "outline the stages of learning a new skill", the named
  planes and axes and the three lever classes, the FITT formula and the principles of training,
  the three energy systems, and named fitness tests for each component.
- **The specification:** the NCCA *Leaving Certificate Physical Education Curriculum
  Specification* (Ordinary and Higher Level), © 2017, introduced in phase-1 schools in
  September 2018 and first examined in 2020. curriculumonline.ie labels it "Leaving Certificate
  Physical Education (2018) Specification (for examination to June 2027)", so it is the
  document the app's June 2027 students sit. The official PDF is
  `pipeline/resources/pe/spec-syllabus.pdf` (also `relevant-resources/syllabi/pe.pdf`),
  checked against curriculumonline.ie on 2026-10-30. Section numbers in brackets, e.g.
  **[2.6]**, are the specification's own "Students learn about" numbers; **[S6]** means its
  Section 6, *Physical activity areas*.
- **Clarification from NCCA:** curriculumonline.ie adds, for the current cohort, that "on page
  44 of the PDF specification, training may be aerobic and/or anaerobic" (the *Personal
  exercise and fitness* area). It is reflected in `pe-personal-exercise-fitness`.
- **Do not use the 2026 specification** (`relevant-resources/syllabi/pe-2026-spec.pdf`, "for
  introduction September 2026", first examined 2028). It is a different course: three strands
  (Skill learning, participation and performance; Physical and psychological demands of
  performance; Factors influencing participation), no prescribed topics, a 50% written exam and
  a 50% Physical Education Project. Content found only in it, such as the muscular and skeletal
  systems, joint actions, the cardiovascular and respiratory response to exercise, and its named
  supplement list, is not on the June 2027 course.
- **Chapters** are the app's 16 PE chapter IDs (`pe-pipeline-content.js`,
  `pipeline/scaffold/pe.json`). Past exam questions and flashcards are tagged to these IDs, so
  keep every ID exactly as written. The ten theory chapters follow the specification's ten
  topics; the six activity chapters follow its six physical activity areas. (`data.js` still
  holds the legacy shells `pe1`–`pe9`, `pe-casestudy` and `pe-acronyms`; `pe-pipeline-content.js`
  replaces them with the 16 chapters at load time, so they are not chapter IDs.)
- **What each subsection contains:**
  - **"Syllabus"** is what the specification says students "should be able to" do, close to its
    own wording. This is the required scope; every item must be covered.
  - **"Settings"** are the examples the specification itself names (e.g. "pedometers, activity
    diaries"). Use them; they are the examples an examiner expects.
  - **"SimpleStudy"** names the matching topic in SimpleStudy's Higher Level course (taxonomy
    recorded 2026-08-07 in `pipeline/resources/pe/guide-simplestudy.md`). Use it for structure
    only; write all prose in your own words.
- **Higher vs Ordinary level:** the specification marks no content as Higher Level only. Both
  levels study every topic; the levels differ in "the structure of the examination paper and
  the style of questioning" (more scaffolding at Ordinary level). Write everything at Higher
  Level depth.
- **Prescribed topics for June 2027.** All students study Topics 1–6. Of Topics 7–10, the SEC
  prescribes two per cohort. SEC circular **S51/25** (September 2025,
  `relevant-resources/syllabi/pe-2027-prescribed-topics.pdf`) prescribes for the 2027
  examination:
  - **Topic 9 — Gender and physical activity** (`pe-gender-physical-activity`)
  - **Topic 10 — Business and enterprise in physical activity and sport**
    (`pe-business-enterprise-sport`)

  **Topic 7 (`pe-physical-activity-inclusion`) and Topic 8 (`pe-technology-media-sport`) are
  not prescribed for 2027** and will not be examined as topics. Their chapters keep their IDs
  and past-paper questions (earlier cohorts were examined on them), but write their notes last.
  Some of their content is still examinable through other topics: media and gender stereotypes
  [8.2] overlap with [9.2]; video and analysis software [8.1] with [4.2]; barriers for women
  [7.1] with [9.1].
- **Where the specification sets a choice, write content for every option**, so students can
  pick:
  - students study three physical activities, each from a different one of the six areas; every
    activity listed in [S6] needs a profile in its area's chapter
  - within an area: one adventure activity; one aquatics activity (or two swimming strokes);
    one gymnastics or dance form; one athletics event from running, throwing or jumping; one
    game from invasion, net/wall or striking/fielding; one aerobic method plus one conditioning
    and resistance activity
  - supports and barriers "for at least two" of six groups [7.1] (write all six); developments
    "from one group's perspective" [7.3] (write each group)
  - a dietary plan for "one selected physical activity" [2.8]; supplements in "one of their
    selected physical activities" [6.5]; "a selected business" in sport [10.2]
- **"A named physical activity of your choice".** The written exam asks most theory questions
  in the context of the student's own activity. Each theory subsection should show its outcome
  applied to at least two contrasting named activities (e.g. a team game and an individual
  event). The specification's own example trio is lifesaving (Aquatics), basketball (Games) and
  orienteering (Adventure activities).
- **Assessment** [Section 7]:
  - **Written examination, 50%**, Higher and Ordinary level. It examines knowledge of the
    theoretical factors affecting participation and performance and the relationships between
    them; concept and process knowledge; "engagement with a case study designed to require
    learners to apply their learning in a particular physical activity scenario"; and clarity
    and coherence of answers. Recent papers (2022–2026, see `pipeline/exam-info/pe.json`) run
    2 h 30 min for 250 marks: Section A, 10 of 12 short questions (80 marks); Section B, a
    compulsory case study (50 marks); Section C, 3 of 5 long questions at 40 marks each (120
    marks). Each year's paper includes questions across Topics 1–6 plus the two prescribed
    topics (S51/25).
  - **Physical activity project (PAP), 20%**, Higher and Ordinary level. An 8–10 week project
    in the role of performer or coach/choreographer, submitted digitally in four sections:
    performance analysis; four performance goals; evidence of ongoing training/practice and
    reflection; concluding analysis.
  - **Performance assessment, 30%**, common level, assessed by the SEC from video captured by
    the student. One of the class's three activities, showing the [S6] skills and techniques,
    tactics/compositional knowledge, and rules and safe practice.
  - The PAP and the performance assessment must be in two different activities.

---

## Strand 1 — Towards optimum performance (Topics 1–4)

The strand covers the interrelationship between performance and the psychological,
physiological, biomechanical, sociological and cultural factors that shape it. "Optimum" means
the best performance the learner can achieve at this point in time.

### pe-learning-skill-technique — Learning and Improving Skill and Technique [Topic 1: 1.1–1.3]
1. **Defining a skilled performance** [1.1]: identify the characteristics of a skilled
   performance; discuss the difference between skill and ability. The specification defines a
   skilled performance as a fluent, controlled sequence of movements in which the right options
   are selected, and technique as the way a skill is executed.
   SimpleStudy: Learning and Improving Skill and Technique (lesson "Defining a Skilled
   Performance").
2. **Analysing skill: the biomechanical perspective** [1.2]: analyse selected skills and
   techniques using planes and axes, and levers.
   SimpleStudy: Learning and Improving Skill and Technique.
3. **Analysing skill: movement and quality perspectives** [1.2]: analyse selected skills and
   techniques using vectors and scalars and Newton's laws of motion; and for
   quality/effectiveness, economy of movement and the creative application of skill.
   SimpleStudy: Learning and Improving Skill and Technique.
4. **Skill acquisition** [1.3]: outline the stages of learning a new skill; describe how skills
   are learned effectively; design practice schedules incorporating the principles of effective
   practice and a variety of practice methods.
   SimpleStudy: Learning and Improving Skill and Technique.

### pe-performance-demands — Physical and Psychological Demands of Performance [Topic 2: 2.1–2.8]
The demands are health-related fitness, performance-related fitness, psychological preparation,
and diet and nutrition. Students learn each generally and as it applies to each of their three
activities.
1. **Physical fitness** [2.1]: discuss the difference between health- and performance-related
   fitness.
   SimpleStudy: Physical and Psychological Demands of Performance.
2. **Health-related fitness** [2.2]: define its components: cardio-respiratory endurance,
   muscular endurance, strength, flexibility and body composition.
   SimpleStudy: Physical and Psychological Demands of Performance.
3. **Performance-related fitness** [2.3]: define its components: agility, balance,
   co-ordination, power, speed and reaction time.
   SimpleStudy: Physical and Psychological Demands of Performance.
4. **Applying the fitness components** [2.4]: examine how far each health- and
   performance-related component matters in the selected activities; research how they can be
   developed in a demanding practice context; design a combined approach to health- and
   performance-related fitness training.
   SimpleStudy: Physical and Psychological Demands of Performance.
5. **Assessing fitness and the principles of training** [2.5]: design a fitness test battery for
   a physical activity from an analysis of its particular fitness demands; evaluate the
   principles of training from a performance perspective; apply the FITT formula to each
   component of physical fitness.
   - Settings: the principles listed in [S6] (readiness, specificity, progression, overload,
     rest/recovery), with training zones, thresholds, work-recovery intervals and
     warm-up/cool-down.
   - SimpleStudy: Physical and Psychological Demands of Performance.
6. **Designing a fitness plan** [2.6]: compare methods of physical fitness training for the
   three selected activities; discuss training in the activity and outside it; use fitness test
   data to design a fitness programme for a selected activity; suggest strategies to support
   recovery and adaptation after competition/performance and training; demonstrate an
   understanding of periodisation in programme design.
   - Settings: the training methods named in [S6] (continuous, interval, fartlek,
     aerobics/step, spinning, indoor rowing, weights, core stability, circuits).
   - SimpleStudy: Physical and Psychological Demands of Performance.
7. **Psychological preparation** [2.7]: discuss how confidence, anxiety, motivation,
   concentration and feedback affect practice and performance; evaluate strategies to enhance
   confidence, motivation and concentration before, during and after practice and/or
   performance; discuss types of feedback and their importance; analyse strategies to improve
   mental preparedness before, during and after practice/performance; design a personal action
   plan, with a rationale, to support a positive psychological disposition before, during and
   after performance.
   SimpleStudy: Physical and Psychological Demands of Performance.
8. **Diet, nutrition and hydration** [2.8]: examine nutritional considerations before, during
   and after performance; discuss the importance of hydration in different activities and
   settings; discuss the role and challenges of sports supplements, including sports drinks;
   design a dietary plan, with a rationale, for one selected activity.
   SimpleStudy: Physical and Psychological Demands of Performance.
9. **Energy systems** [2.8]: analyse the role and relative contribution of the energy systems
   by duration, intensity and type of activity; explain how understanding them informs
   preparation for practice, performance and recovery.
   SimpleStudy: Physical and Psychological Demands of Performance.

### pe-structures-strategies-roles-conventions — Structures, Strategies, Roles and Conventions [Topic 3: 3.1–3.6]
Covers team structures and strategies; performance-design and choreographic elements in dance
and gymnastics; rules, roles, conventions and safe practice; affiliation, team building and
responsible leadership; and the non-playing roles of coach/choreographer and official.
1. **Structures, strategies and compositional elements** [3.1]: demonstrate an understanding of
   the main structures, strategies and/or compositional elements in performing the selected
   activities; evaluate their own and others' use of them using appropriate methods of
   analysis; modify selected structures and/or strategies for different performance scenarios.
   SimpleStudy: Structures, Strategies, Roles, and Conventions.
2. **Roles and relationships** [3.2]: investigate the physical, personal and technical qualities
   different roles need for a successful performance; identify opponents' weaknesses in order
   to exploit them.
   SimpleStudy: Structures, Strategies, Roles, and Conventions.
3. **Safe practice** [3.3]: demonstrate safe practice in training, performance and organising
   events; suggest warm-up and cool-down practices that prevent injury and prepare
   participants; discuss selecting and maintaining suitable attire, equipment and facilities;
   describe common injuries in the selected activities, their causes and first aid treatment;
   evaluate training/practice schedules designed to avoid overtraining, including fatigue.
   SimpleStudy: Structures, Strategies, Roles, and Conventions.
4. **Rules, rituals and conventions** [3.4]: organise an event or performance that respects the
   activity's rules, roles, rituals and conventions; communicate respectfully with
   performers/players and officials.
   SimpleStudy: Structures, Strategies, Roles, and Conventions.
5. **The role of coach/choreographer** [3.5]: discuss the demands of non-playing roles,
   including desirable interpersonal skills; guide a performer in setting short- and long-term
   goals; design a fitness and skills programme for a specific performer in one selected
   activity; communicate effectively with the performer; suggest modifications to
   practice/performance as needed; use strategies to sustain the performer's motivation to
   train/practise; guide the performer's ongoing reflection; plan and manage practice/training
   time effectively; analyse their own coaching against a coach/choreographer they admire.
   SimpleStudy: Structures, Strategies, Roles, and Conventions.
6. **The role of official** [3.6]: explain the rules and regulations of the selected
   activities; describe their safety regulations and procedures; implement safety checks on
   equipment, facilities and player clothing; use the right scoring/recording systems; describe
   the demands of officiating (personal fitness, psychological readiness, attire, equipment);
   communicate assertively with participants; identify strategies to manage conflict between
   official and participants and between participants; evaluate their own officiating against
   an official they admire.
   SimpleStudy: Structures, Strategies, Roles, and Conventions.

### pe-planning-optimum-performance — Planning for Optimum Performance [Topic 4: 4.1–4.4]
The planning cycle: analyse performance, set realistic goals from sound theory, design a
training/practice programme, monitor and adapt it, then evaluate a concluding performance with
the same methods of analysis. The PAP follows this cycle (see Appendix B).
1. **Personal performance analysis** [4.1]: examine the factors that influence personal
   performance in physical activity and sport.
   SimpleStudy: Personal Performance Analysis.
2. **Methods of analysis** [4.2]: identify appropriate methods of analysing skill and technique,
   structures and strategies, choreography, performance-related fitness, and psychological
   preparedness; use tools including video and analysis software to analyse their own and
   others' performances; compare their performance with a more skilled/model performer;
   identify four areas of their performance needing further development.
   SimpleStudy: Methods of Analysis.
3. **Aesthetic and artistic considerations** [4.3]: identify the artistic and/or aesthetic
   criteria of performance; compare activities by those criteria; evaluate personal and/or
   group performance from artistic and/or aesthetic perspectives.
   SimpleStudy: Aesthetic and Artistic Considerations.
4. **Planning for optimum performance** [4.4]: explain how performance analysis informed
   planning; present performance goals that address areas for improvement; design a
   practice/training plan to meet them; provide evidence of how well the programme achieved the
   goals.
   SimpleStudy: Planning for Optimum Performance: An Overview.

---

## Strand 2 — Contemporary issues in physical activity (Topics 5–10)

Students examine the personal, social and contextual barriers and supports to participation and
performance, and learn to question, critique and challenge what happens in the name of physical
activity and sport at local, national and international level. Topics 5 and 6 are compulsory;
for June 2027, Topics 9 and 10 are prescribed and Topics 7 and 8 are not.

### pe-promoting-physical-activity — Promoting Physical Activity [Topic 5: 5.1–5.4]
1. **Benefits of physical activity participation** [5.1]: discuss the personal, social and
   economic benefits of physical activity for health and wellbeing at different life stages;
   explain the concepts of play, leisure and recreation, physical education, mass-participation
   sports, outdoor and adventure activities, and sport.
   SimpleStudy: Benefits of Physical Activity Participation.
2. **Physical activity participation** [5.2]: present a physical activity biography for
   themselves and for someone with a different activity profile; discuss supports and barriers
   to participation in school and in the community; use different methods of collecting
   participation data; analyse participation patterns in a specific group in their school
   community; evaluate different approaches to promoting physical activity.
   - Settings: pedometers, activity diaries.
   - SimpleStudy: Physical Activity Participation.
3. **Physical activity promotion** [5.3]: analyse the role of national and local policies in
   promoting physical activity; examine the role of the national governing bodies of their
   selected activities, including provision at local, national and international level; design
   a physical activity promotion and adherence tip sheet for a specific target group; discuss
   the characteristics of significant people who promote and support others' participation.
   SimpleStudy: Physical Activity Promotion.
4. **Pathways to excellence in physical activity** [5.4]: suggest ways to strengthen pathways
   between school- and community-based activity/sport; analyse current provision and support
   for excellence in the three selected activities.
   SimpleStudy: Pathways to Excellence in Physical Activity.

### pe-ethics-fair-play — Ethics and Fair Play [Topic 6: 6.1–6.5]
Responsibility for ethics and fair play lies with participants, officials, leaders/coaches,
national governing bodies and the groups responsible for sport at local and national level.
1. **Principles of ethical practice** [6.1]: explain the principles of ethical practice in sport
   and the importance of integrity, respect, fairness and equity in the selected activities.
   SimpleStudy: Ethics and Fair Play.
2. **Codes of ethics** [6.2]: examine the code of ethics in the selected activities from the
   perspective of participants, parents, spectators, coaches and/or club officials; investigate
   sportsmanship and gamesmanship and their influence on engagement in physical activity and
   sport.
   SimpleStudy: Ethics and Fair Play.
3. **Drugs and sport** [6.3]: describe the categories of performance-enhancing drugs, with
   examples of how they affect performance; analyse the implications of using them for the
   performer and the sport.
   SimpleStudy: Ethics and Fair Play.
4. **Anti-doping rules** [6.4]: describe the current Irish anti-doping rules and how they are
   enforced; explain therapeutic use exemption for medicines in sport; discuss the implications
   of performance-enhancing drugs for the performer and the activity.
   SimpleStudy: Ethics and Fair Play.
5. **Best practice for the use of supplements** [6.5]: investigate the uses of dietary
   supplements designed to optimise performance in one selected activity.
   SimpleStudy: Ethics and Fair Play.

### pe-physical-activity-inclusion — Physical Activity and Inclusion [Topic 7: 7.1–7.4] — NOT PRESCRIBED FOR JUNE 2027
Write last (see "Prescribed topics" above).
1. **Supports and barriers for selected groups** [7.1]: analyse the supports and barriers to
   participation for at least two groups; discuss examples of discrimination, stereotyping,
   inclusiveness and/or prejudice in provision for these groups; investigate how the media
   cover sport from these groups' perspective.
   - Settings: women; older adults; people with physical disability; people with intellectual
     disability; different ethnic groups; different socio-economic groups. Write all six.
   - SimpleStudy: Physical Activity and Inclusion.
2. **Addressing barriers to physical activity** [7.2]: discuss how barriers might be or have
   been addressed by the individuals themselves, their representative groups and/or voluntary
   and statutory organisations.
   SimpleStudy: Physical Activity and Inclusion.
3. **Developments over the past twenty years** [7.3]: discuss developments in physical activity
   and sport over the last twenty years from one group's perspective. Write one for each group
   in 7.1.
   SimpleStudy: Physical Activity and Inclusion.
4. **Adapted physical activity** [7.4]: examine whether and how participants with a disability
   could take part in the three selected activities; evaluate provision for adapted activity in
   their school and/or community; examine pathways towards excellence in adapted physical
   activities.
   SimpleStudy: Physical Activity and Inclusion.

### pe-technology-media-sport — Technology, Media and Sport [Topic 8: 8.1–8.2] — NOT PRESCRIBED FOR JUNE 2027
Write last (see "Prescribed topics" above).
1. **The impact of technology on sport and physical activity** [8.1]: examine how developments
   in technology affect the performer, coach/choreographer, official and spectator in the
   selected activities; discuss their own use of technology in planning for optimum
   performance; evaluate technology's role in analysing training and evaluating performance.
   SimpleStudy: Technology, Media, and Sport.
2. **Media in sport** [8.2]: investigate media coverage of elite performance and of mass
   participation; examine the media's role in maintaining gender stereotypes of men and women
   in sport; identify what gives the selected activities media and/or spectator appeal; analyse
   the impact of media coverage on spectator behaviour.
   - Settings: television, internet, newspapers and digital media (from the topic
     introduction).
   - SimpleStudy: Technology, Media, and Sport.

### pe-gender-physical-activity — Gender and Physical Activity [Topic 9: 9.1–9.3] — PRESCRIBED FOR JUNE 2027
The specification frames the topic with two questions: why young women have lower participation
levels, and why young men and women favour different activities. It asks students to consider
these in the context of their three selected activities.
1. **Gender, sport and physical activity** [9.1]: examine the main influences on boys' and
   girls' participation patterns; suggest ways to address the imbalance between boys' and
   girls' participation levels in school and in the community.
   SimpleStudy: Gender and Physical Activity.
2. **Gender, media and body image** [9.2]: discuss how body image influences, and is influenced
   by, the participation of males and females; debate how media representations of the body may
   affect young men's and young women's participation.
   SimpleStudy: Gender and Physical Activity.
3. **Gender socialisation and its impact on participation** [9.3]: examine how the social
   regulation of the body has affected, and continues to affect, men's and women's
   participation; explain why the characteristics of hegemonic masculinity and hegemonic
   femininity might affect boys' and girls' participation.
   SimpleStudy: Gender and Physical Activity.

### pe-business-enterprise-sport — Business and Enterprise in Physical Activity and Sport [Topic 10: 10.1–10.4] — PRESCRIBED FOR JUNE 2027
The introduction frames sport as big business: groups that compete for audiences and control
what is broadcast, and sponsorship as the lifeblood of many sports and events.
1. **Sponsorship and advertising** [10.1]: examine the impact of sponsorship, endorsements and
   merchandising on sport and performers; analyse the messages sport-related advertising gives
   young people; discuss the advantages and disadvantages of sponsorship for the national
   governing body, the performers and the sport; suggest a code of practice for selecting
   commercial sponsors for sport in which young people take part.
   SimpleStudy: Business and Enterprise in Physical Activity and Sport.
2. **The business dimension** [10.2]: investigate the involvement of a selected business in
   sport. Write at least two contrasting real businesses.
   SimpleStudy: Business and Enterprise in Physical Activity and Sport.
3. **Mass participation in sport** [10.3]: examine the growth of mass-participation sporting
   events and the business and enterprise opportunities they provide.
   SimpleStudy: Business and Enterprise in Physical Activity and Sport.
4. **Tourism and sport** [10.4]: discuss the potential of sports marketing to develop tourism
   in Ireland.
   - Settings: Ireland.
   - SimpleStudy: Business and Enterprise in Physical Activity and Sport.

---

## Physical activity areas (Section 6)

Students study three activities, each from a different area. In each, they aim to develop the
standard of their performance, be creative as an individual and/or team member, and be
consistent in the quality of their performance. The skills and techniques below are the ones
the performance assessment requires; the written exam uses them as the "named physical
activity" contexts for Topics 1–10. Each chapter's first subsection covers the area as a whole
and the choice rule; each later subsection is one activity's profile, built around the
specification's listed skills and techniques and linked to the rules, safety, structures and
strategies, fitness demands and analysis methods from the theory chapters.

### pe-adventure-activities — Adventure Activities [S6]
1. **The adventure activities area:** individual and co-operative activities in a challenging,
   usually outdoor, environment where uncontrollable elements influence the choice and use of
   skills and strategies; emphasis on interpersonal skills and reflection. Learners choose one
   of orienteering, canoeing/kayaking, rock-climbing, sailing or rowing/sculling.
   SimpleStudy: Adventure Activities.
2. **Orienteering:** map-reading; pacing skills; navigation skills; route-planning; adhering to
   safe-practice procedures; demonstrating respect for the environment.
3. **Kayaking:** two variants with separate skill lists.
   - Moving/white water: launching and landing at a low wall/bank; paddling (forwards,
     backwards, stopping, sweep and reverse sweep, edging, stern rudder, ferry glide and reverse
     ferry glide); breaking in and out of a current (into the eddy with bow rudder/low brace and
     no brace, out of it with low brace and bow rudder); negotiating currents and water features
     (stoppers, standing waves, whirlpools, green water); capsize drill, Eskimo roll, self-rescue
     and recovery; two advanced/group skills from capsize and rescue (self and with rope), e.g.
     combat roll, high cross, hanging draw.
   - Inland flat water/coastal: launching and landing; paddling (forwards, backwards, stopping,
     sweep and reverse sweep static and moving, stern rudder, bow rudder, figure-of-8 course
     forwards and backwards, ferry glide and reverse ferry glide); draw strokes/sculling draw and
     sculling for support; capsize drill, rolls, self-rescue and recovery; deep-water rescues
     (swimmer to boat/X-rescue, rafting).
4. **Rock-climbing** (outdoors or indoor wall, single pitch): using equipment and safe
   procedures; basic knots; climbing calls and communication; climbing bottom and top rope
   (single and multiple anchors), rope management, belaying, hand/finger/foot jams, 3-point
   and/or 2-point contact, lay backing, undercling, bridging; climbing an overhang and/or mantle
   shelf; traversing; abseiling straight, locking off to collect equipment part-way down.
5. **Sailing:** leaving and returning to a windward shore and a leeward shore; tacking/going
   about (upwind); gybing; capsize drill and recovery; sailing a course up/downwind.
6. **Rowing/sculling:** sculling strokes; rowing on stroke side; rowing on bow side; paddling
   with square blades; single stroke to hands away.

### pe-aquatics — Aquatics [S6]
1. **The aquatics area:** water-based activities using swimming and/or diving skills for
   performance, water safety or recreation. Learners choose one of lifesaving, survival swim,
   two swimming strokes, water-polo or synchronised swimming.
   - Settings: lifesaving is the specification's own example activity.
   - SimpleStudy: Aquatics.
2. **Lifesaving:** entries into water, including into unknown conditions; strokes/propelling
   over a distance to a casualty or with a casualty; life-saving kick/side stroke; approaching
   a casualty and manoeuvring a casualty when turning; contact and non-contact tows using rigid
   and non-rigid aids, conserving energy, breath and heat; two different types of rescue.
3. **Survival swimming:** entries into water, including unknown conditions; straddle and
   submerging (feet first, head first, surface dive to depth); floating with or without an aid;
   treading water; stamina swimming in clothing, keeping form, propelling and sculling;
   underwater swimming; turns in distance swimming; conserving energy, breath and heat (HELP
   position; HUDDLE position with at least two others).
4. **Two swimming strokes:** body position/alignment; hand entry, glide and exit positions; kick;
   stroke co-ordination; head action and breathing; starts, turns and finishes; sprint and
   distance swimming. Profile all four competitive strokes so any pair can be chosen.
5. **Water-polo:** passing/receiving (various); shooting (various); moving with the ball; moving
   free; marking/intercepting.
6. **Synchronised swimming:** back layout and tuck position; front layout and front pike; back
   pike and ballet leg; fishtail, flamingo and bent-knee vertical; dolphin arch, surface arch,
   split walkover front; a duet or trio performance combining these and other movements.

### pe-artistic-aesthetic-movement — Artistic and Aesthetic Movement [S6]
1. **The artistic and aesthetic area:** artistic activities involve the creative crafting and
   performance of imaginative combinations of skills in the style of the event; aesthetic
   activities involve appreciating the qualities of movement and the performers' expressiveness,
   using aesthetic criteria to plan, perform and evaluate. Learners choose gymnastics (artistic
   or rhythmic) or dance (contemporary, folk, modern, ballet, jazz, tap, ethnic, traditional).
   Links to [3.1] compositional elements and [4.3] aesthetic and artistic criteria.
   SimpleStudy: Artistic and Aesthetic Movement.
2. **Artistic gymnastics:** jumps (at least 2: tuck, pike, straddle, 180° turn); rolls (at least
   2: forward, backward, other); balances (at least 2: handstand, headstand, arabesque, other);
   weight transference (at least 2: cartwheel, round-off, handspring, back flip). The short
   floor sequence must include at least four of: backward roll to handstand, handspring, back
   flip, front somersault, handstand ½ turn, one-handed cartwheel, back somersault,
   back/forward walkovers. At least two vaults from handspring, short-arm overswing, or an
   optional vault of similar tariff (not through or straddle).
3. **Rhythmic gymnastics:** a short floor sequence showing balances; pivots/rolls; splits;
   hops/leaps/skips; body waves, bends, circles, swings and turns. Routines are set to music
   using different apparatus from ball, hoop, ribbon, rope or club.
4. **Dance:** an individual and a group dance showing technical ability (posture, alignment,
   co-ordination, balance, strength, flexibility, mobility, control); choreographic design,
   covering content (use of space such as levels and pathways, timing, relationship to other
   dancers), construction (motif and variation) and form (e.g. canon, unison, binary, rondo);
   dance style; use of props and music; and an overall sense of performance that communicates
   artistically and aesthetically with an audience.

### pe-athletics — Athletics [S6]
1. **The athletics area:** running, jumping, throwing and walking events, indoors or outdoors,
   measured against the performer's own ability and others' standards. Learners select one
   category (running, throwing or jumping) and are assessed on one event within it, e.g.
   discus.
   SimpleStudy: Athletics.
2. **Running** (sprints, middle distance, long distance, hurdles): starts and finishes; upper-body
   action (head and arms); lower-body action (legs); overall efficiency.
3. **Throwing** (shot-put, discus, javelin, hammer): grip, stance and preparation; movement into
   the throwing action; release and follow-through; overall efficiency.
4. **Jumping** (high jump, long jump, triple jump): run-up; take-off; flight; landing; overall
   efficiency.

### pe-games — Games [S6]
1. **The games area:** individual, pair or team games needing activity-specific skills, game
   appreciation, decision-making, tactical knowledge and strategic thinking towards a defined
   goal. Learners study one category (invasion, striking/fielding or net/wall) and are assessed
   on one game, e.g. Gaelic football.
   - Settings: basketball is the specification's own example activity.
   - SimpleStudy: Games.
2. **Invasion games:** Gaelic football; hurling/camogie; rugby union; soccer (outfield and
   goalkeeping); basketball; hockey (outfield and goalkeeping); netball; Olympic handball. Each
   game's listed skill families must be profiled: e.g. for Gaelic football, handling,
   tackling/intercepting, running with the ball, kicking and shooting (including 45s); for
   basketball, passing/receiving, dribbling, shooting (lay-ups, set, jump, 3-point),
   marking/intercepting/rebounding and footwork. Use the [S6] tables for the full list per game.
3. **Net/wall games:** badminton; tennis; volleyball; table tennis; handball (60×30 and 40×20);
   squash. Profile each game's listed strokes and serves, e.g. badminton: high/low serve,
   forehand/backhand net play and clears, drop shots, smash.
4. **Striking/fielding games:** cricket (batting drives, cut/pull/glance; bowling medium, fast
   or spin with line and length; close and deep fielding); softball/rounders
   (catching/receiving/throwing; hitting/striking/batting; pitching/bowling; fielding on base,
   close, deep and outfield).

### pe-personal-exercise-fitness — Personal Exercise and Fitness Activities [S6]
1. **The personal exercise and fitness area:** active, purposeful participation in a
   personally designed programme reflecting personal interests, goals and the principles of
   training. Learners choose one aerobic training method and one conditioning and resistance
   activity. NCCA clarification: training may be aerobic and/or anaerobic. The performance
   shows a programme aimed at either performance in an activity or health-related fitness: a
   five-minute warm-up; a fifteen-minute development section with cardiovascular and muscular
   strength and endurance parts (which may use a circuit format); and a five-minute cool-down.
   Learners show knowledge of relevant progressions, adaptations and safe practice.
   SimpleStudy: Personal Exercise and Fitness Activities.
2. **Aerobic training methods:** continuous training (constant intensity, purpose, FITT,
   intermediate slow distance 20–60 min, long slow distance over 60 min); interval training
   (readiness, work:recovery ratios, interval duration, FITT); fartlek (readiness, terrain,
   interval duration, FITT); aerobics/step aerobics (technical description of skills, routine,
   transition, timing and rhythm, training zones, FITT); spinning (techniques, workout
   intensity, session design, training zones, FITT); indoor rowing (time, distance, targets,
   resistance, session design).
3. **Conditioning and resistance:** weight training (upper-extremity pushing: pressing,
   extensions; upper-extremity pulling: rows, curls; lower-extremity: squats, lunges); core
   stability (relaxation and breathing, control, routine, alignment, flow); circuit training
   (exercises specific to themes, equipment and work-recovery intervals).
4. **Applying training principles to each method:** principles of training (readiness,
   specificity, progression, overload, rest/recovery); training zones; thresholds;
   work-recovery intervals; warm-up/cool-down. Cross-reference [2.5]–[2.6] without repeating
   them.

---

## Appendix A — Where the specification differs from SimpleStudy and from the repo's earlier assumptions

- **Prescribed topics were not recorded anywhere in the repo.** The specification makes Topics
  7–10 a rotating choice set by the SEC. For June 2027, SEC circular S51/25 prescribes Topics 9
  and 10 only. Earlier app content and `pipeline/resources/pe/guide-simplestudy.md` treat all
  four as equal course content.
- **First examination year was wrong.** The repo had 2022 (`pipeline/config.py`, the bundle
  manifest and the README). SEC S51/25 states the specification "was examined for the first time
  in 2020". 2020 had no written exam (calculated grades), but 2021 did, and the pipeline never
  pulled the 2021 papers.
- **The 2018 specification is being replaced,** not simply "Current": curriculumonline.ie labels
  it "for examination to June 2027", and the 2026 specification starts with fifth years in
  September 2026.
- **No Higher Level-only content:** unlike biology, nothing in the 2018 specification is bold
  or marked HL.
- **In the specification but not visible as separate SimpleStudy topics:** SimpleStudy records
  Topics 1, 2, 3 and 6–10 as one topic each, so its structure gives no checklist for 1.1–1.3,
  2.1–2.8, 3.1–3.6 or 6.1–6.5. In particular, levers, vectors/scalars and Newton's laws [1.2];
  energy systems [2.8]; periodisation [2.6]; officiating and conflict management [3.6];
  therapeutic use exemption [6.4]. Lesson-level coverage of these topics was not recorded and
  should be checked when the information packages are written.
- **In SimpleStudy but not a specification topic:** the "Assessment" unit (Physical Activity
  Project; Performance Assessment; Written Exam). This is assessment guidance, not examinable
  content; see Appendix B.
- **Content in the app that neither specification names** (kept as assumed knowledge or
  teaching aids, not removed): somatotypes; the information-processing model; Bandura's
  self-efficacy sources; the inverted-U hypothesis; SPORRT including reversibility and tedium;
  SMARTER goals; the STEP inclusion framework. One test question uses the **COM-B model**
  (`pe-test-questions.js`, Promoting Physical Activity), which is outside both specifications.
  See the decisions list in the restructure report.
- **App structure:** `pe-pipeline-content.js` copies notes from the legacy `pe1`–`pe9`
  chapters into the 16 chapters by a fixed map, and several notes land outside their syllabus
  topic. Safe practice, injuries and first aid (`pe8`, Topic 3.3) feed Adventure Activities and
  Aquatics. Training principles, methods and periodisation (`pe2`, Topic 2.5–2.6) feed Planning
  for Optimum Performance. Drugs and anti-doping answers sit in `pe4` (Diet) questions, not
  Ethics. The `pe-acronyms` notes are not shown anywhere. When notes are rewritten, place each
  fact under the subsection this outline gives it.

## Appendix B — Specification content with no home in an existing chapter

No new chapters are proposed. Placements:

- **Physical activity project (PAP, 20%)**: its four sections (performance analysis, four
  performance goals, training/practice and reflection, concluding analysis) mirror Topic 4.
  Proposed home: a short closing block in `pe-planning-optimum-performance` subsection 4,
  explaining the link, with no coursework instructions.
- **Performance assessment (30%)**: what a student must show in the assessed activity. Proposed
  home: subsection 1 of each activity-area chapter (one or two points each).
- **Written exam and case-study technique**: the case study is a fixed exam section (Section B,
  50 marks), not a topic. Proposed home: the app's exam guide (`pipeline/exam-info/pe.json`,
  shown via `pe-exam-info.js`), which already holds section tips; no notes chapter.
- **Aims, objectives, key skills, learning in/through/about physical activity**: framing only;
  not examined as content. No home needed.
- **Legacy `pe-casestudy` and `pe-acronyms` chapters** (in `data.js`, not among the 16 IDs): fold
  the useful mnemonics into the matching subsections when notes are written; the case-study
  advice belongs with the exam guide above.

## Appendix C — SimpleStudy structure as recorded (2026-08-07)

For reference only, from `pipeline/resources/pe/guide-simplestudy.md`.

1. Learning and Improving Skill and Technique — Learning and Improving Skill and Technique
2. Physical and Psychological Demands of Performance — Physical and Psychological Demands of
   Performance
3. Structures, Strategies, Roles, and Conventions — Structures, Strategies, Roles, and
   Conventions
4. Planning for Optimum Performance — Personal Performance Analysis; Methods of Analysis;
   Aesthetic and Artistic Considerations; Planning for Optimum Performance: An Overview
5. Promoting Physical Activity — Benefits of Physical Activity Participation; Physical Activity
   Participation; Physical Activity Promotion; Pathways to Excellence in Physical Activity
6. Ethics and Fair Play — Ethics and Fair Play
7. Physical Activity and Inclusion — Physical Activity and Inclusion
8. Technology, Media, and Sport — Technology, Media, and Sport
9. Gender and Physical Activity — Gender and Physical Activity
10. Business and Enterprise in Physical Activity and Sport — Business and Enterprise in Physical
    Activity and Sport
11. Physical Activity Areas — Adventure Activities; Aquatics; Artistic and Aesthetic Movement;
    Athletics; Games; Personal Exercise and Fitness Activities
12. Assessment — Physical Activity Project; Performance Assessment; Written Exam
