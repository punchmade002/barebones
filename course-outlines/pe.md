# Leaving Cert Physical Education (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format,
  and a worked example). This outline says what to cover; that file says how to write it.
- **The syllabus:** the NCCA *Leaving Certificate Physical Education Curriculum Specification
  (Ordinary and Higher Level)*, © 2017, published 2018. Curriculum Online labels it
  "Leaving Certificate Physical Education (2018) Specification (for examination to June 2027)".
  Teaching began in September 2018 and it was first examined in 2020. The official PDF is
  `pipeline/resources/pe/spec-syllabus.pdf` (also in `relevant-resources/syllabi/pe.pdf`).
  Numbers in brackets, e.g. **[2.7]**, are the specification's own "students learn about"
  numbers.
- **Do not use the 2026 specification**
  (`relevant-resources/syllabi/pe-2026-spec.pdf`, "for introduction September 2026"). It is a
  different course, first examined in 2028, with three different strands, new anatomy and
  physiology outcomes (cardiovascular, respiratory, muscular and skeletal systems; the body's
  response to activity), and a different assessment (written exam 50%, Physical Education
  Project 50%). None of that is examined in June 2027.
- **Curriculum Online clarification for the current cohort:** on p. 44 of the specification
  (personal exercise and fitness), training may be **aerobic and/or anaerobic**.
- **Chapters** are the app's 16 PE chapter IDs (`pipeline/scaffold/pe.json`, built into the app
  by `pe-pipeline-content.js`). Past exam questions and flashcards are tagged to these IDs, so
  keep every ID exactly as written. The legacy `pe1`–`pe9` chapters in `data.js` are only a
  source of older notes; don't write to them.
- **What each subsection contains:**
  - **"Syllabus"** is what the specification says students should be able to do, close to its
    own wording. This is the required scope; every item must be covered.
  - **"Settings"** are the specification's own named examples and lists. They are part of the
    scope where the specification lists them.
  - **"SimpleStudy"** names the matching topic(s) in SimpleStudy's Higher Level course
    (recorded 2026-08-07, `pipeline/resources/pe/guide-simplestudy.md`). Use them for structure
    only; write all prose in your own words.
- **Higher vs Ordinary level:** the specification marks **no topic or learning outcome as
  Higher Level only**. Both levels study the same content. Higher Level expects theoretical
  concepts and abstract thinking "with significant depth in selected areas", in-depth analysis
  of a range of activities, and problem-solving in unfamiliar contexts. The performance
  assessment is at a common level.
- **Choices the specification sets. Write content for every option:**
  - **Strand 2, Topics 7–10:** all students study Topics 5 and 6. Two of Topics 7–10 are
    prescribed for each cohort, and the SEC names them in a circular (for 2027: S51/25,
    "Prescribed Topics for Written Examination in Leaving Certificate examination 2027"). Those
    two topics are examined; the other two are not. **This outline covers all four** because
    the 2027 pair has not been confirmed in this repo (see Appendix C).
  - **Three physical activities**, each from a different one of the six physical activity
    areas (Section 6). Within an area, students pick one activity (e.g. one athletics event,
    one game). Write every activity listed.
  - **[7.1]:** supports and barriers for "at least two" of six groups. Write all six.
  - **[7.3]:** developments over the last twenty years "from one group's perspective". Write
    one section per group.
  - **Physical activity project:** done as **performer or coach/choreographer**.
- **Assessment:** physical activity project 20% (Higher and Ordinary); performance assessment
  30% (common level, assessed by the SEC); written examination 50% (Higher and Ordinary). The
  project and the performance assessment must be in **two different activities**. The written
  paper (2 h 30 min, 250 marks; see `pe-exam-info.js`) has Section A, short questions (any 10
  of 12, 80 marks); Section B, a compulsory case study (50 marks); and Section C, long
  questions (any 3 of 5, 40 marks each). The specification says the exam tests theoretical
  knowledge and the links between factors, concept and process knowledge, applying learning to
  a case study in a physical activity scenario, and clarity and coherence. Notes should
  therefore always apply each concept to a named physical activity.

---

## Strand 1 — Towards optimum performance (Topics 1–4)

All students. The strand covers psychological, physiological, biomechanical, sociological and
cultural factors that shape performance. Students apply them to plan for their own optimum
performance (the best they can achieve at this point) in three physical activities.

### pe-learning-skill-technique — Learning and Improving Skill and Technique [1.1–1.3]
The specification's own definition, to use throughout: a skilled performance is one where a
sequence of movements is performed fluently and with control, the right options are selected,
and the skills and techniques used fully reflect the performer's ability and experience.
Technique is the way the skills are executed.

1. **Defining a skilled performance** [1.1]: identify the characteristics of a skilled
   performance; discuss the difference between skill and ability.
   SimpleStudy: Learning and Improving Skill and Technique ("Defining a Skilled Performance").
2. **Biomechanical analysis** [1.2]: analyse selected skills and techniques using planes and
   axes and levers.
   SimpleStudy: Learning and Improving Skill and Technique.
3. **Movement analysis** [1.2]: analyse selected skills and techniques using vectors and
   scalars and Newton's laws of motion.
   SimpleStudy: Learning and Improving Skill and Technique.
4. **Quality and effectiveness** [1.2]: analyse selected skills and techniques for economy of
   movement and the creative application of skill.
   SimpleStudy: Learning and Improving Skill and Technique.
5. **Stages of learning a new skill** [1.3]: outline the stages of learning a new skill.
   SimpleStudy: Learning and Improving Skill and Technique.
6. **How skills are learned effectively** [1.3]: describe how skills are learned effectively.
   Past papers also examine skill classification, guidance and feedback here.
   SimpleStudy: Learning and Improving Skill and Technique.
7. **Designing practice schedules** [1.3]: design practice schedules that use the principles of
   effective practice and a variety of practice methods.
   SimpleStudy: Learning and Improving Skill and Technique.

### pe-performance-demands — Physical and Psychological Demands of Performance [2.1–2.8]
The four demands the specification names: health-related fitness, performance-related
fitness, psychological preparation, and appropriate diet and nutrition. Each is applied to the
three selected activities, and to self-assessment and planning for improvement.

1. **Physical fitness** [2.1]: discuss the difference between health-related and
   performance-related fitness.
   SimpleStudy: Physical and Psychological Demands of Performance.
2. **Health-related fitness** [2.2]: define its components: cardio-respiratory endurance,
   muscular endurance, strength, flexibility and body composition.
3. **Performance-related fitness** [2.3]: define its components: agility, balance,
   coordination, power, speed and reaction time.
4. **Applying the components of fitness** [2.4]: examine how far each health- and
   performance-related component matters in the selected physical activities; research ways
   to develop them in a demanding practice context; design a combined approach to health- and
   performance-related fitness training.
5. **Fitness testing** [2.5]: design a fitness test battery for a physical activity, based on
   an analysis of that activity's particular fitness demands.
6. **Principles of training and the FITT formula** [2.5]: evaluate the principles of training
   from a performance perspective; apply the FITT formula to each component of physical
   fitness.
7. **Designing a fitness plan** [2.6]: compare different methods of physical fitness training
   in the context of the three selected activities; discuss training in the activity and
   outside it; use fitness test data to design a physical fitness programme for a selected
   activity.
8. **Recovery, adaptation and periodisation** [2.6]: suggest strategies to support recovery and
   adaptation after competition, performance and training; show an understanding of
   periodisation in the design of training programmes.
9. **Psychological factors and strategies** [2.7]: discuss how confidence, anxiety,
   motivation, concentration and feedback affect practice and performance; evaluate strategies
   to enhance confidence, motivation and concentration before, during and after practice
   and/or performance; analyse strategies to improve mental preparedness before, during and
   after practice or performance.
   SimpleStudy: Physical and Psychological Demands of Performance.
10. **Feedback** [2.7]: discuss different types of feedback and why each matters in selected
    practices and/or performance.
11. **Personal psychological action plan** [2.7]: design a personal action plan, with a
    rationale, to support a positive psychological disposition before, during and after
    performance.
12. **Nutrition and hydration** [2.8]: examine the nutritional considerations before, during and
    after performance; discuss the importance of hydration in different physical activities
    and settings.
13. **Sports supplements and sports drinks** [2.8]: discuss the role and challenges of using
    sports supplements, including sports drinks. (Topic 6 [6.5] covers best practice in
    supplement use; keep the two consistent and don't repeat facts.)
14. **Energy systems** [2.8]: analyse the role and relative contribution of the energy systems
    in relation to the duration, intensity and type of activity; explain how understanding the
    energy systems informs preparation for practice, performance and recovery.
15. **A dietary plan** [2.8]: design a dietary plan, with a rationale, for one selected
    physical activity.

### pe-structures-strategies-roles-conventions — Structures, Strategies, Roles and Conventions [3.1–3.6]
The topic covers structures, strategies and compositional elements (team games; group
composition and choreography in dance and gymnastics); rules, roles, conventions and safe
practice; affiliation, team building and responsible leadership; and the non-playing roles of
coach/choreographer and official.

1. **Structures, strategies and compositional elements** [3.1]: show understanding of the main
   structures, strategies and/or compositional elements in selected activities; evaluate your
   own and others' use of them with appropriate methods of analysis; modify selected
   structures and/or strategies for different performance scenarios. Settings: individual and
   team roles in games; performance design elements and choreographic approaches in dance and
   gymnastics.
   SimpleStudy: Structures, Strategies, Roles, and Conventions.
2. **Roles and relationships** [3.2]: investigate the physical, personal and technical
   qualities different roles need for a successful performance; identify opponents' weaknesses
   in order to exploit them. The topic introduction adds affiliation, team building and
   responsible leadership towards shared performance goals.
3. **Safe practice in training, performance and events** [3.3]: demonstrate safe practice in
   training, performance and organising physical activity events; suggest warm-up and
   cool-down practices that prevent injury and prepare participants; discuss the importance of
   selecting and maintaining suitable attire, equipment and facilities for selected
   activities.
4. **Common injuries and first aid** [3.3]: describe common injuries in the selected
   activities, their causes and first-aid treatment.
5. **Overtraining and fatigue** [3.3]: evaluate training and practice schedules designed to
   avoid the problems of overtraining, including player or participant fatigue.
6. **Rules, rituals and conventions** [3.4]: organise an event or performance that respects the
   activity's rules, roles, rituals and conventions; communicate respectfully with performers,
   players and officials.
7. **The role of coach/choreographer** [3.5]: discuss the demands of non-playing roles,
   including the interpersonal skills needed. The coach/choreographer should be able to:
   - guide the performer in identifying and planning short- and long-term goals
   - design a physical fitness and skills programme for a specific performer in one of the
     selected activities
   - communicate in a way that supports positive coach–performer interaction
   - suggest modifications to practice or performance as the need arises
   - use strategies that keep the performer motivated to train or practise
   - guide the performer's ongoing reflection on practice and performance
   - plan and manage practice and training time effectively
   - analyse their own coaching against a coach/choreographer they admire.
8. **The role of the official** [3.6]: the official should be able to:
   - explain the rules and regulations of the selected activities
   - describe their safety regulations and procedures
   - carry out safety checks on equipment, facilities and player clothing
   - use the activity's scoring and recording systems
   - describe the demands of officiating: personal fitness, psychological readiness,
     personal attire and suitable equipment
   - communicate assertively with participants
   - identify strategies to manage conflict between official and participants, or between
     participants
   - evaluate their own officiating against an official they admire.

### pe-planning-optimum-performance — Planning for Optimum Performance [4.1–4.4]
The planning cycle the specification sets out: analyse performance at the outset, set
realistic goals on sound theoretical principles, design a training or practice programme,
monitor and adapt it, then evaluate a concluding performance with the same methods of analysis
used at the start. Students do this for each of the three activities.

1. **Personal performance analysis** [4.1]: examine the factors that influence personal
   performance in physical activity and sport.
   SimpleStudy: Personal Performance Analysis.
2. **Methods of analysis** [4.2]: identify suitable methods for analysing skill and technique;
   structures and strategies; choreography; performance-related fitness; and psychological
   preparedness. Use a range of tools, including video and analysis software, to analyse your
   own and others' performances; compare your performance with a more skilled or model
   performer; identify four areas of your performance that need further development.
   SimpleStudy: Methods of Analysis.
3. **Aesthetic and artistic considerations** [4.3]: identify the artistic and/or aesthetic
   criteria of performance; compare physical activities by these criteria; evaluate personal
   and/or group performance from artistic and aesthetic perspectives.
   SimpleStudy: Aesthetic and Artistic Considerations.
4. **Planning for optimum performance** [4.4]: explain how performance-analysis information
   informed planning; present performance goals that address areas for improvement; design a
   practice or training plan to improve performance against those goals; provide evidence of
   how well the programme achieved them.
   SimpleStudy: Planning for Optimum Performance: An Overview.
5. **The physical activity project (20%)** [Section 7]: an 8–10 week project in one activity,
   as performer or coach/choreographer, completed in digital format. Its four sections:
   performance analysis; identifying four performance goals; evidence of ongoing training or
   practice and reflection; concluding analysis. It must be in a different activity from the
   performance assessment.
   SimpleStudy: Assessment (Physical Activity Project).

---

## Strand 2 — Contemporary issues in physical activity (Topics 5–10)

The strand develops students as literate and critical participants. They examine the personal,
social and contextual barriers and supports to participation and performance, and question
and critique what happens in sport at local, national and international level. **Topics 5 and
6 are for all students. Two of Topics 7–10 are prescribed for each cohort** (see Read this
first and Appendix C).

### pe-promoting-physical-activity — Promoting Physical Activity [5.1–5.4]
1. **Benefits of physical activity** [5.1]: discuss the personal, social and economic benefits
   of physical activity for health and wellbeing at different life stages.
   SimpleStudy: Benefits of Physical Activity Participation.
2. **Concepts of physical activity** [5.1]: explain play; leisure and recreation; physical
   education; mass-participation sports; outdoor and adventure activities; sport.
   SimpleStudy: Benefits of Physical Activity Participation.
3. **Physical activity biographies, supports and barriers** [5.2]: present a physical activity
   biography for yourself and for someone whose activity profile differs from yours; discuss
   supports and barriers to participation in school and in the community.
   SimpleStudy: Physical Activity Participation.
4. **Measuring participation** [5.2]: use different methods of collecting participation data,
   e.g. pedometers, activity diaries; analyse participation patterns in a specific group in the
   school community.
   SimpleStudy: Physical Activity Participation.
5. **Approaches to promotion and policy** [5.2, 5.3]: evaluate different approaches to
   promoting physical activity; analyse the role of national and local policies in promoting
   it.
   SimpleStudy: Physical Activity Promotion.
6. **National governing bodies** [5.3]: examine the role of the national governing bodies of
   the selected activities, including how each activity is provided for at local, national and
   international level.
   SimpleStudy: Physical Activity Promotion.
7. **Promotion tip sheets and significant people** [5.3]: design a physical activity promotion
   and adherence tip sheet for a specific target group; discuss the characteristics of
   significant people who promote and support others' participation.
   SimpleStudy: Physical Activity Promotion.
8. **Pathways to excellence** [5.4]: suggest ways to strengthen pathways between school-based
   and community-based physical activity and sport; analyse current provision and support for
   excellence in the three selected activities.
   SimpleStudy: Pathways to Excellence in Physical Activity.

### pe-ethics-fair-play — Ethics and Fair Play [6.1–6.5]
The specification places responsibility for ethics with participants, officials,
leaders/coaches, national governing bodies, and local and national groups responsible for
sport.

1. **Principles of ethical practice** [6.1]: explain the principles of ethical practice in sport
   and the importance of integrity, respect, fairness and equity in the selected activities.
   SimpleStudy: Ethics and Fair Play.
2. **Codes of ethics** [6.2]: examine the code of ethics in the selected activities from the
   perspective of participants, parents, spectators, coaches and/or club officials.
3. **Sportsmanship and gamesmanship** [6.2]: investigate both concepts and their influence on
   engagement in physical activity and sport.
4. **Categories of performance-enhancing drugs** [6.3]: describe the categories of
   performance-enhancing drugs, with examples of how each affects performance.
5. **Implications of drug use** [6.3, 6.4]: analyse, and discuss, the implications of using
   performance-enhancing drugs for the performer and for the sport or activity. (The
   specification lists this twice; write it once.)
6. **Irish anti-doping rules** [6.4]: describe the current Irish anti-doping rules and how they
   are enforced; explain therapeutic use exemption for medicines in sport.
7. **Best practice in supplement use** [6.5]: investigate the uses of dietary supplements meant
   to optimise performance in one of the selected activities.

### pe-physical-activity-inclusion — Physical Activity and Inclusion [7.1–7.4] (prescribed-topic option)
1. **Supports and barriers for selected groups** [7.1]: analyse supports and barriers to
   participation for at least two of these groups. Write all six:
   - women
   - older adults
   - people with physical disability
   - people with intellectual disability
   - different ethnic groups
   - different socio-economic groups.

   SimpleStudy: Physical Activity and Inclusion.
2. **Discrimination, stereotyping and prejudice** [7.1]: discuss examples of discrimination,
   stereotyping, inclusiveness and/or prejudice in physical activity provision for these
   groups.
3. **Media coverage and these groups** [7.1]: investigate media coverage of sport from these
   groups' perspective.
4. **Addressing barriers** [7.2]: discuss how barriers have been, or might be, addressed by the
   individuals themselves, their representative groups, and voluntary and statutory
   organisations.
5. **Developments over the past twenty years** [7.3]: discuss developments in physical activity
   and sport over the last twenty years from one group's perspective. Write one section for
   each of the six groups.
6. **Adapted physical activity** [7.4]: examine whether and how participants with a disability
   could take part in the three selected activities; evaluate adapted physical activity
   provision in the school and/or community; examine pathways towards excellence in adapted
   physical activities.

### pe-technology-media-sport — Technology, Media and Sport [8.1–8.2] (prescribed-topic option)
1. **Impact of technology on participants** [8.1]: examine how developments in technology
   affect the performer, coach/choreographer, official and spectator in the selected
   activities.
   SimpleStudy: Technology, Media, and Sport.
2. **Personal use of technology** [8.1]: discuss your own use of technology in planning for
   optimum performance in the selected activities.
3. **Technology in analysing training and performance** [8.1]: evaluate the role of technology
   in analysing training and evaluating sporting performance.
4. **Media coverage of elite and mass participation** [8.2]: investigate media coverage of both
   elite performance and mass participation.
5. **Media and gender stereotypes** [8.2]: examine the media's role in maintaining gender
   stereotypes of men and women in sport.
6. **Media and spectator appeal** [8.2]: identify what gives, or could give, the selected
   activities media and/or spectator appeal.
7. **Media and spectator behaviour** [8.2]: analyse the impact of media coverage on spectator
   behaviour.
   Settings for the topic: television, the internet, newspapers and digital media.

### pe-gender-physical-activity — Gender and Physical Activity [9.1–9.3] (prescribed-topic option)
The topic asks why young women participate less than young men, and why young men and women
choose different activities, applied to the three selected activities.

1. **Influences on participation** [9.1]: examine the main influences on boys' and girls'
   participation patterns in physical activity and sport.
   SimpleStudy: Gender and Physical Activity.
2. **Addressing the imbalance** [9.1]: suggest ways to address the imbalance between boys' and
   girls' participation levels, in school and in the community.
3. **Body image** [9.2]: discuss how body image influences, and is influenced by, the
   participation of males and females.
4. **Media representations of the body** [9.2]: debate how media representations of the body
   may affect young men's and young women's participation.
5. **Social regulation of the body** [9.3]: examine how social regulation of the body has
   affected, and still affects, men's and women's participation.
6. **Hegemonic masculinity and femininity** [9.3]: explain why the characteristics associated
   with each might affect boys' and girls' participation in sport and physical activity.

### pe-business-enterprise-sport — Business and Enterprise in Physical Activity and Sport [10.1–10.4] (prescribed-topic option)
1. **Sponsorship, endorsements and merchandising** [10.1]: examine their impact on sport and
   performers.
   SimpleStudy: Business and Enterprise in Physical Activity and Sport.
2. **Sport-related advertising** [10.1]: analyse different forms of sport-related advertising
   for the messages they give young people.
3. **Advantages and disadvantages of sponsorship** [10.1]: discuss them for the national
   governing body, the performers and the sport or activity.
4. **A code of practice for sponsorship** [10.1]: suggest a code of practice for choosing
   commercial sponsorship in sport and physical activity that young people take part in.
5. **The business dimension** [10.2]: investigate a selected business's involvement in sport.
6. **Mass participation events** [10.3]: examine the growth of mass participation sporting
   events and the business and enterprise opportunities they provide.
7. **Tourism and sport** [10.4]: discuss the potential of sports marketing to develop tourism
   in Ireland.

---

## Section 6 — Physical activity areas (applied throughout; basis of the 30% performance assessment)

Students study three activities, each from a different area. In each activity they aim to
develop the standard of their performance, be creative as an individual and/or a team or
group member, and perform consistently well. For the performance assessment (30%, common
level, assessed by the SEC), each student performs in **one** of the three, captured
digitally in conditioned practice, fully competitive play and/or personal performance. They
must show the listed skills and techniques; apply and adapt tactics, strategies and
compositional knowledge to different scenarios; and know and apply the rules, regulations and
codes of practice. Each subsection below lists the activity's required skills and techniques
as the specification gives them. Notes should cover each skill's technique and teaching points,
plus the activity's rules, safety and tactics, so that every Strand 1 and 2 topic can be
applied to it.
SimpleStudy: Physical Activity Areas; Assessment (Performance Assessment).

### pe-adventure-activities — Adventure Activities [Section 6]
Individual and co-operative activities in a challenging, usually outdoor, environment, where
elements that can't be fully controlled affect which skills and strategies are chosen. The
specification stresses interpersonal skills and reflection. Students choose one activity.
SimpleStudy: Adventure Activities.

1. **Orienteering:** map-reading; pacing; navigation; route-planning; following safe-practice
   procedures; respect for the environment.
2. **Kayaking (moving/white water):** launching and landing at a low wall or bank; paddling
   (forwards, backwards, stopping, sweep and reverse sweep strokes, edging, stern rudder, ferry
   glide and reverse ferry glide); breaking in and out of a current (into an eddy with bow
   rudder/low brace and no brace; out of an eddy with low brace and bow rudder); negotiating
   and using currents and water features (stoppers, standing waves, whirlpools, green water);
   capsize drill, Eskimo roll, self-rescue and recovery; two advanced or group skills from
   capsize and rescue, self and with rope (e.g. combat roll, high cross, hanging draw).
3. **Kayaking (inland flat water/coastal):** launching and landing at a low wall or bank;
   paddling (forwards, backwards, stopping, sweep and reverse sweep strokes, static and
   moving; stern rudder; bow rudder; figure-of-8 course forwards and backwards; ferry glide
   and reverse ferry glide); draw strokes and support strokes (draw/sculling draw, sculling
   for support); capsize drill, rolls, self-rescue and recovery; deep-water rescues (swimmer
   to boat/X-rescue, rafting). The activity list says "Canoeing/Kayaking"; the skills tables
   cover kayaking only.
4. **Rock-climbing (outdoors or indoor wall, single pitch):** using equipment and safe
   procedures; basic knots; climbing calls and communication; climbing bottom and top rope
   (single and multiple anchors), rope management, belaying, hand/finger/foot jams, 3-point
   and/or 2-point contact, lay-backing, undercling, bridging; climbing an overhang and/or
   mantle shelf; traversing with feet and hands; abseiling straight, including locking off to
   collect equipment part-way down.
5. **Sailing:** leaving and returning to a windward shore; leaving and returning to a leeward
   shore; tacking/going about (upwind); gybing; capsize drill and recovery; sailing a course
   up and downwind.
6. **Rowing/sculling:** sculling strokes; rowing on stroke side; rowing on bow side; paddling
   with square blades; single stroke to hands away.

### pe-aquatics — Aquatics [Section 6]
Water-based activities that use swimming and/or diving skills for performance, water safety
or recreation. Students choose one activity.
SimpleStudy: Aquatics.

1. **Lifesaving:** entries into water, including unknown conditions; strokes and propulsion over
   a distance to a casualty or with a casualty; lifesaving kick/side stroke; approaching a
   casualty and manoeuvring them when turning; contact and non-contact tows with rigid and
   non-rigid aids, conserving energy, breath and heat; two different types of rescue.
2. **Survival swimming:** entries into water, including unknown conditions; straddle entry and
   submerging (feet first, head first, surface dive to depth); floating, maintaining buoyancy
   with or without an aid; treading water; stamina swimming in clothing, maintaining form,
   propelling and sculling; underwater swimming; turns in distance swimming; conserving energy,
   breath and heat (HELP position; HUDDLE position with at least two others).
3. **Two swimming strokes:** body position and alignment; hand entry, glide and exit positions;
   kick; stroke coordination; head action and breathing; starts, turns and finishes; sprint and
   distance swimming. The specification doesn't name the strokes, so write all four competitive
   strokes (front crawl, backstroke, breaststroke, butterfly).
4. **Water-polo:** passing and receiving (various); shooting (various); moving with the ball;
   moving free; marking and intercepting.
5. **Synchronised swimming:** back layout and tuck position; front layout and front pike; back
   pike and ballet leg; fishtail, flamingo and bent-knee vertical; dolphin arch, surface arch,
   split walkover front; a duet or trio performance combining these and other movements.

### pe-artistic-aesthetic-movement — Artistic and Aesthetic Movement [Section 6]
Artistic activities: creative crafting and performance of imaginative combinations of skills
and movements in the style of the event. Aesthetic activities: appreciating the qualities of
the movement and the performers' expressiveness, using aesthetic criteria to plan, perform
and evaluate. Students choose one activity. Link to [4.3].
SimpleStudy: Artistic and Aesthetic Movement.

1. **Artistic gymnastics:**
   - Basic elements: jumps (at least 2: tuck, pike, straddle, 180° turn); rolls (at least 2:
     forward, backward, other); balances (at least 2: handstand, headstand, arabesque, other);
     weight transference (at least 2: cartwheel, round-off, handspring, back flip).
   - A short floor sequence with at least four of: backward roll to handstand; handspring;
     back flip; front somersault; handstand ½ turn; one-handed cartwheel; back somersault;
     back/forward walkovers.
   - At least two vaults from: handspring; short-arm overswing; an optional vault of similar
     tariff (not a through or straddle vault).
2. **Rhythmic gymnastics:** a short floor sequence showing balances; pivots and rolls; splits;
   hops, leaps and skips; body waves, bends, circles, swings and turns. Routines are set to
   music using different apparatus from ball, hoop, ribbon, rope or club.
3. **Dance:** an individual and a group dance showing:
   - technical ability: posture, alignment, coordination, balance, strength, flexibility,
     mobility and control
   - choreographic design: choreographic content (use of space, e.g. levels and pathways;
     timing; relationship to other dancers); choreographic construction (motif and variation);
     choreographic form (e.g. canon, unison, binary, rondo)
   - dance style: contemporary, folk, modern, ballet, jazz, tap, ethnic or traditional
   - use of props and music
   - overall sense of performance, including communicating artistically and aesthetically with
     an audience.

### pe-athletics — Athletics [Section 6]
Running, jumping, throwing and walking events, indoors or outdoors, measurable against the
performer's own ability and against others' standards. Students choose one category, and the
assessment focuses on one event in it (e.g. discus).
SimpleStudy: Athletics.

1. **Running** (sprints, middle distance, long distance, hurdles): starts and finishes; upper
   body action (head and arms); lower body action (legs); overall efficiency. Write each
   event.
2. **Throwing** (shot-put, discus, javelin, hammer): grip, stance and preparation; movement into
   the throwing action; release and follow-through; overall efficiency. Write each event.
3. **Jumping** (high jump, long jump, triple jump): run-up; take-off; flight; landing; overall
   efficiency. Write each event.

### pe-games — Games [Section 6]
Individual, pair or team games that need activity-specific skills, game appreciation,
decision-making, tactical knowledge and strategic thinking towards a defined goal. Students
choose one category, and the assessment focuses on one game in it (e.g. Gaelic football).
SimpleStudy: Games.

1. **Gaelic football:** handling (passing/receiving, fielding, hand pass, pick-up);
   tackling/intercepting (challenging, front, shoulder, displacing, blocking); running/moving
   with the ball (soloing, toe-to-hand, dummying, dribbling, sidestep, swerve, change of
   pace); kicking (hand, ground, instep/drop, driven, clearance, return to play); shooting
   (long, short, 45s).
2. **Hurling/camogie:** handling (passing/receiving, fielding, hand pass, pick-up);
   tackling/intercepting (challenging, front, shoulder, displacing, blocking); running/moving
   with the ball (soloing, pick-up, dummying, dribbling, sidestep, swerve, change of pace);
   hitting (hand, ground, in the air, drop, clearance); shooting (long, short, 65s).
3. **Rugby union:** handling (passing/receiving long and short, stationary and running, high
   and low; pick-up from ground; quick spin; diving; switch); tackling/intercepting (front,
   rear, side, smother); retaining the ball in a maul; retaining possession on the ground in a
   maul; running with the ball (swerve, sidestep, dummy, change of pace).
4. **Soccer:** outfield: passing/receiving/control (short, long, ground, lofted, chip, both
   feet); dribbling (both feet); shooting (short, long, volley, half-volley); heading in
   defence and attack; tackling, jockeying, closing down, intercepting. Goalkeeping:
   receiving and distributing; kicking from hand and dead ball; shot-stopping (high, low);
   taking the ball at the feet; taking high crosses and punching.
5. **Basketball:** passing/receiving (handling, chest, bounce, side, overhead, running,
   stationary); dribbling (both hands, change of pace, reverse); shooting (left/right, lay-ups,
   driving; set, jump, 3-point); marking/intercepting (1v1, against the ball handler,
   rebounding); footwork.
6. **Hockey:** outfield: passing/receiving/control (push, stopping, short, long, slap, hitting,
   reverse, left/right); dribbling (open, reverse, change of pace); flicking (short, long,
   high, low, penalties); shooting (left/right in the circle, close, distance); tackling,
   jockeying, closing down, intercepting. Goalkeeping: receiving and distributing (both feet);
   defending short corners; saving penalty flicks; shot-stopping (high, low, edge of circle);
   sliding tackle on an attacking player.
7. **Netball:** passing/receiving/control (one- and two-handed, shoulder, lob, bounce, running,
   chest pass); footwork (one- and two-foot landings, pivot); shooting (close, distance,
   running; one- and two-handed; forward and backward step shots); moving free (dodge, change
   of pace); marking, intercepting and rebounding.
8. **Olympic handball:** passing/receiving/control (one- and two-handed catches at various
   heights, stationary and moving); footwork (one- and two-foot landings, pivot); shooting
   (close, distance, running; one-handed, jump, penalty); moving with the ball; marking,
   jockeying, intercepting; moving free (dodge, change of pace).
9. **Badminton:** service (high, low); net play (forehand, backhand); clears (forehand,
   backhand); drop shots; smash.
10. **Tennis:** service (variations); drives (forehand, backhand); volleys (forehand, backhand);
    lob; smash.
11. **Table tennis:** service (forehand and backhand variations); drives (forehand, backhand);
    push (forehand, backhand); block; smash.
12. **Volleyball:** service (underarm, overarm, frontal, floating/side floating); volleying (set
    forward and backward); forearm pass/dig; smash/spike; blocking.
13. **Squash:** service (forehand and backhand variations); drives (forehand, backhand); volleys
    (forehand, backhand); boasts; lob.
14. **Handball (60×30 and 40×20 courts):** underarm stroke; overhand stroke; back-wall shot;
    straight hit from the short line; fly shot; side-arm stroke (40×20 only); serve.
15. **Cricket:** batting (straight, on- and off-drive, forward and back; cut, pull, glance);
    bowling (medium, fast or spin; line and length); fielding close; fielding deep.
16. **Softball/rounders:** catching, receiving and throwing (various); hitting/striking/batting;
    pitching/bowling (various: medium, fast, swerve, spin; line and length); fielding on base
    and close; fielding deep and outfield.

Settings: invasion games (1–8), net/wall games (9–14), striking/fielding games (15–16).

### pe-personal-exercise-fitness — Personal Exercise and Fitness Activities [Section 6]
Active, purposeful participation in a personally designed exercise and fitness programme that
reflects personal interests, goals and the principles of training. Students choose one aerobic
training method and one conditioning and resistance method. Curriculum Online clarifies that
training may be aerobic and/or anaerobic. Link to [2.4]–[2.6].
SimpleStudy: Personal Exercise and Fitness Activities.

1. **Continuous training:** constant intensity; purpose; FITT formula; intermediate slow
   distance (20–60 min); long slow distance (over 60 min).
2. **Interval training:** readiness; work:recovery ratios; interval duration; FITT formula.
3. **Fartlek training:** readiness; terrain; interval duration; FITT formula.
4. **Aerobics/step aerobics:** technical description of skills; routine; transitions; timing and
   rhythm; training zones; FITT formula.
5. **Spinning:** spinning techniques; workout intensity; session design; training zones; FITT
   formula.
6. **Indoor rowing:** time; distance; targets; resistance; session design.
7. **Weight training:** upper-body pushing (pressing, extensions); upper-body pulling (rows,
   curls); lower-body exercises (squats, lunges).
8. **Core stability:** relaxation and breathing; control; routine; alignment; flow.
9. **Circuit training:** exercises chosen for themes, equipment and work–recovery intervals.
10. **Applying training to every method:** the principles of training (readiness, specificity,
    progression, overload, rest/recovery); training zones; thresholds; work–recovery
    intervals; warm-up and cool-down. Students must also show relevant progressions,
    adaptations and safe practice.
11. **The assessed programme:** a 5-minute warm-up with its necessary elements; a 15-minute
    development section with a cardiovascular part and a muscular strength and endurance part
    (a circuit format is allowed); a 5-minute cool-down with its necessary elements. The
    programme aims to improve either performance in a physical activity or health-related
    fitness.

---

## Appendix A — Where the specification differs from SimpleStudy and from the repo's previous assumptions

- **No Higher Level-only content.** The specification marks no topic or outcome as Higher
  Level only, so the notes shouldn't either.
- **Prescribed topics.** SimpleStudy presents Topics 7–10 as four ordinary units and doesn't
  say that only two are examined in a given year. The specification prescribes two per cohort.
  The app shows all four with equal weight.
- **In the specification but not visible in SimpleStudy's taxonomy:** SimpleStudy has one topic
  each for Topics 1, 2, 3 and 6–10, so its taxonomy doesn't show the finer items. Check these
  specifically: vectors and scalars and Newton's laws [1.2]; practice schedule design [1.3];
  the fitness test battery and combined training approach [2.4–2.5]; training in and outside
  the activity [2.6]; the personal psychological action plan and the dietary plan [2.7–2.8];
  energy systems informing recovery [2.8]; identifying opponents' weaknesses [3.2];
  organising an event [3.4]; the full coach/choreographer and official lists [3.5–3.6];
  identifying four areas for development [4.2]; the physical activity biography and
  participation data [5.2]; the tip sheet and significant people [5.3]; therapeutic use
  exemption [6.4]; the six groups and the twenty-year developments [7.1, 7.3]; adapted
  physical activity pathways [7.4]; hegemonic masculinity and femininity [9.3]; a sponsorship
  code of practice and sport tourism in Ireland [10.1, 10.4]. Also the activity-by-activity
  skills lists in Section 6.
- **In SimpleStudy but not a syllabus topic:** the "Assessment" unit (Physical Activity
  Project; Performance Assessment; Written Exam). This is assessment information from Section
  7. Here it goes in `pe-planning-optimum-performance` (subsection 5) and the Section 6
  header.
- **Wording:** the specification calls the area both "artistic and aesthetic activities"
  (p. 33) and "artistic and aesthetic movement" (p. 37); SimpleStudy and the app use the
  latter. Adventure activities lists "Canoeing/Kayaking" but tabulates only kayaking.
- **Content past papers examine that the specification doesn't name word for word:** skill
  classification, guidance types, reversibility and tedium as training principles, and named
  supplements such as creatine. These are taught as part of [1.3], [2.5] and [2.8]/[6.5], and
  SEC papers from 2022–2026 ask about them, so they stay. Don't import the 2026
  specification's anatomy and physiology outcomes.
- **Corrections to the repo:**
  - `firstExamYear` / `SYLLABUS_CUTOFF` said 2022. The first LCPE exam was in **2020**: the
    Department of Education's announcement of 23 February 2018 says students starting in
    September 2018 "will sit the first … LCPE exam in 2020". It is now 2020. The app's past
    papers start at 2022. If the SEC archive has 2020 or 2021 LCPE papers, they're on-course
    and missing.
  - The app status for the document said "Current". It now says "Current; examined to June
    2027", and the 2026 specification is stored separately as `pe-2026-spec.pdf`.
  - `pe-pipeline-content.js` copies legacy notes into the new chapters by `legacySources`, and
    some mappings are off-topic. `pe-ethics-fair-play` receives `pe9` (coach and official
    roles), not ethics. `pe-adventure-activities` and `pe-aquatics` receive `pe8` (general
    safety and injuries). `pe-athletics` receives `pe1` (fitness testing). The new notes
    replace these, so they don't need patching now.
  - Every chapter currently has a single "Core Concepts" subsection (`<id>-core`). This
    outline's numbered subsections are the intended breakdown.

## Appendix B — Specification content with no exact home in an existing chapter

No new chapters are needed. Proposed placements:

- **The physical activity project (20%)** → `pe-planning-optimum-performance` subsection 5;
  the project follows the Topic 4 planning cycle.
- **The performance assessment (30%)** → the Section 6 header, applied in each activity-area
  chapter.
- **Section B case-study technique (written exam)** → no syllabus topic of its own; the case
  study applies any topic to a physical activity scenario. Proposed home:
  `pe-planning-optimum-performance` or the exam-technique panel (`pe-exam-info.js`), not a new
  chapter. The legacy `pe-casestudy` and `pe-acronyms` chapters in `data.js` are dropped by
  `pe-pipeline-content.js` and no longer appear in the app. Decide whether to restore either
  as a chapter.
- **Strand overviews** (the strand 1 perspectives; the strand 2 critical-literacy aims) and the
  topic introductions (affiliation, team building, responsible leadership in Topic 3) → placed
  inside the matching chapters above.

## Appendix C — Prescribed Strand 2 topics for June 2027 (needs confirmation)

The SEC circular **S51/25**, "Leaving Certificate Physical Education — Prescribed Topics for
Written Examination in Leaving Certificate examination 2027", names the two of Topics 7–10
examined in 2027. It is linked from PEAI's LCPE resources page
(`https://www.examinations.ie/docs/viewer.php?q=cf8fc63b2b7440740391278bc6d85a8a70437b0b`),
but examinations.ie's bot protection blocked every download attempt, so the pair is
unconfirmed here. Until it is confirmed, write notes for all four topics. Once confirmed, mark
the two non-prescribed chapters as not examined in 2027 (don't delete them: their questions
and flashcards are tagged, and later cohorts may need them).

For reference, the topic chapters tagged in the app's past-paper bank by year (this reflects
tagging, not the circulars): 2022–2023 mostly business and inclusion; 2024 business and
technology; 2025–2026 inclusion and technology; gender has no tagged questions.
