# PE coverage audit — outline vs what the site shows now (2026-10-15)

Compares each of the 120 subsections in `course-outlines/pe.md` with what a student sees in the
app today. To reproduce the app's view, load `data.js` → `pe-content.js` →
`pe-exam-questions.js` → `pe-flashcards.js` → `pe-pipeline-content.js` →
`pe-test-questions.js` → `generated-notes-content.js`, in the order `app.html` loads them.

## What the site shows per chapter

Each of the 16 chapters has **one** page ("Core Concepts", `<id>-core`). It is built from:

1. a one-paragraph chapter overview (`generated-notes-content.js`)
2. for five Strand 2 chapters only, one "Developed application" paragraph
3. old notes copied from the legacy `pe1`–`pe9` chapters by `legacySources` in
   `pe-pipeline-content.js`
4. "Connected course content" blocks, which are the flashcards strung together
5. two "Past-paper application" blocks (a question plus its model answer)
6. a generic "How to build a full-mark answer" paragraph.

## Status key

- **Covered:** a dedicated note block with specific, examinable facts for this subsection, in
  this chapter.
- **Elsewhere:** covered, but only in another chapter's page.
- **Thin:** only an overview sentence, a flashcard definition, a practice question or a single
  model answer.
- **None:** nothing beyond the chapter title.

## Totals

| | Covered | Elsewhere | Thin | None | Subsections |
|---|---:|---:|---:|---:|---:|
| Strand 1 (Topics 1–4) | 17 | 7 | 8 | 3 | 35 |
| Strand 2 (Topics 5–10) | 0 | 4 | 30 | 7 | 41 |
| Physical activity areas | 5 | 0 | 2 | 37 | 44 |
| **All** | **22** | **11** | **40** | **47** | **120** |

## Per subsection

### pe-learning-skill-technique — 6 covered, 1 thin
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Defining a skilled performance | Covered | Skill definition; ACE FACE; TACK; skill vs ability |
| 2 | Biomechanical analysis | Covered | Planes, axes, pairings; levers, classes, mechanical advantage |
| 3 | Movement analysis | Covered | Scalars and vectors; distance and displacement; speed, velocity, acceleration; Newton's laws |
| 4 | Quality and effectiveness | Thin | Economy of movement covered; creative application gets one sentence |
| 5 | Stages of learning | Covered | Fitts and Posner; learning plateau |
| 6 | How skills are learned effectively | Covered | Domains; classification; information processing; guidance; feedback |
| 7 | Practice schedules | Covered | Practice types; GAP VAT; one past-paper model |

### pe-performance-demands — 8 covered, 4 elsewhere, 2 thin, 1 none
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Physical fitness | Covered | Health, fitness and wellbeing; the two categories |
| 2 | Health-related fitness | Covered | The five components; body composition; somatotypes |
| 3 | Performance-related fitness | Covered | The six components |
| 4 | Applying the components | Thin | A one-line needs analysis; no combined-training design |
| 5 | Fitness testing | Covered | Test battery; a test per component; validity and reliability |
| 6 | Principles of training and FITT | Elsewhere | SPORRT and FITT are in the planning and personal-exercise chapters |
| 7 | Designing a fitness plan | Elsewhere | Training methods in planning and personal-exercise; nothing on training in vs outside the activity |
| 8 | Recovery, adaptation and periodisation | Elsewhere | In planning and personal-exercise |
| 9 | Psychological factors and strategies | Covered | Confidence and self-efficacy; anxiety; arousal; motivation; strategies before, during and after |
| 10 | Feedback | Elsewhere | In the skill chapter |
| 11 | Personal psychological action plan | None | |
| 12 | Nutrition and hydration | Covered | Macronutrients; micronutrients; hydration; before, during and after |
| 13 | Supplements and sports drinks | Covered | One block: sports vs energy drinks; named supplements |
| 14 | Energy systems | Covered | The three systems; the continuum; a past-paper model on preparation |
| 15 | Dietary plan | Thin | Nutrition targets only |

### pe-structures-strategies-roles-conventions — 3 covered, 3 elsewhere, 2 thin
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Structures, strategies and compositional elements | Covered | Composition; five elements; structures; strategies; ACT |
| 2 | Roles and relationships | Thin | One block on qualities; nothing on affiliation, team building or leadership |
| 3 | Safe practice | Elsewhere | Safe practice, clothing, warm-up and cool-down appear only in adventure and aquatics |
| 4 | Common injuries and first aid | Elsewhere | Injuries, concussion, SALTAPS and PRICE appear only in adventure and aquatics |
| 5 | Overtraining and fatigue | Elsewhere | In adventure, aquatics and planning |
| 6 | Rules, rituals and conventions | Thin | Definitions only; nothing on organising an event |
| 7 | Role of coach/choreographer | Covered | Role, qualities, motivation, communication, reflection |
| 8 | Role of official | Covered | Role, scoring, readiness, conflict |

### pe-planning-optimum-performance — 3 thin, 2 none
The chapter mostly shows training-methods notes (SPORRT, FITT, methods, periodisation). These
belong to [2.5]–[2.6].
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Personal performance analysis | None | |
| 2 | Methods of analysis | Thin | Flashcard; a performance-analysis block appears only in structures, ethics and games |
| 3 | Aesthetic and artistic considerations | Thin | Flashcard; model answers are filed in the skill and business chapters |
| 4 | Planning for optimum performance | Thin | The overview mentions SMART goals; flashcards |
| 5 | Physical activity project (20%) | None | Its "Case Study" notes are about the written exam |

### pe-promoting-physical-activity — 6 thin, 2 none
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Benefits at different life stages | None | |
| 2 | Concepts of physical activity | Thin | Flashcard definitions of the six concepts |
| 3 | Biographies, supports and barriers | Thin | One past-paper model on community supports |
| 4 | Measuring participation | Thin | One practice question |
| 5 | Approaches to promotion and policy | Thin | Developed application; nothing on policy |
| 6 | National governing bodies | Thin | Flashcard |
| 7 | Tip sheets and significant people | None | |
| 8 | Pathways to excellence | Thin | Flashcard |

### pe-ethics-fair-play — 5 thin, 1 elsewhere, 1 none
The chapter's copied notes are the **coach and official notes** (from `pe9`), not ethics.
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Principles of ethical practice | Thin | Flashcards for integrity, respect, fairness, equity |
| 2 | Codes of ethics | Thin | Flashcard |
| 3 | Sportsmanship and gamesmanship | None | One word in the overview |
| 4 | Categories of performance-enhancing drugs | Thin | Examples appear only inside one model answer |
| 5 | Implications of drug use | Thin | One past-paper model |
| 6 | Irish anti-doping rules; TUE | Thin | Flashcard; one line mentioning Sport Ireland |
| 7 | Best practice in supplement use | Elsewhere | A supplements block in performance demands; a model answer here |

### pe-physical-activity-inclusion — 4 thin, 2 none
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Supports and barriers for the six groups | Thin | Disability only (developed application, practice questions) |
| 2 | Discrimination, stereotyping and prejudice | None | |
| 3 | Media coverage and these groups | Thin | One model answer on women's media coverage, which is an [8.2] question |
| 4 | Addressing barriers | Thin | Developed application; flashcards |
| 5 | Developments over the past twenty years | None | |
| 6 | Adapted physical activity | Thin | STEP framework; flashcards |

### pe-technology-media-sport — 4 thin, 2 elsewhere, 1 none
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Impact of technology on participants | Thin | Developed application; spectator model; a performer model filed in performance demands |
| 2 | Personal use of technology | None | |
| 3 | Technology in analysing performance | Thin | Developed application (GPS, heart rate, video) |
| 4 | Media coverage of elite and mass participation | Elsewhere | Model answer filed in inclusion |
| 5 | Media and gender stereotypes | Elsewhere | Model answer filed in inclusion |
| 6 | Media and spectator appeal | Thin | Flashcard |
| 7 | Media and spectator behaviour | Thin | One past-paper model |

### pe-gender-physical-activity — 5 thin, 1 elsewhere
The two "Past-paper application" blocks here are authored practice questions, not real papers.
No real exam question is tagged to this chapter.
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Influences on participation | Thin | Developed application; a short model |
| 2 | Addressing the imbalance | Thin | A short model |
| 3 | Body image | Thin | Practice question |
| 4 | Media representations of the body | Elsewhere | Past-paper model filed in promoting |
| 5 | Social regulation of the body | Thin | Flashcard |
| 6 | Hegemonic masculinity and femininity | Thin | Developed application; flashcards |

### pe-business-enterprise-sport — 6 thin, 1 none
| # | Subsection | Status | What the site has |
|---|---|---|---|
| 1 | Sponsorship, endorsements and merchandising | Thin | Developed application; flashcards |
| 2 | Sport-related advertising | Thin | One past-paper model |
| 3 | Advantages and disadvantages of sponsorship | Thin | Risks listed in the developed application |
| 4 | A code of practice for sponsorship | Thin | Flashcard |
| 5 | The business dimension | None | |
| 6 | Mass participation events | Thin | Developed application; flashcard |
| 7 | Tourism and sport | Thin | One mention |

### Physical activity area chapters — 5 covered, 2 thin, 37 none
None of these chapters has any activity-specific skill or technique content. Their flashcards
say only "X: an … activity listed in LCPE". Their copied notes come from unrelated legacy
chapters: adventure and aquatics show general safety and injuries; athletics shows fitness
testing and biomechanics; games shows coach and official notes; artistic shows compositional
elements.

| Chapter | Subsections | Status |
|---|---|---|
| pe-adventure-activities | 6 (orienteering, two kayaking, rock-climbing, sailing, rowing) | All none |
| pe-aquatics | 5 | All none |
| pe-artistic-aesthetic-movement | 3 | Artistic and rhythmic gymnastics none; dance thin (the five compositional elements) |
| pe-athletics | 3 (running, throwing, jumping) | All none (no event phases) |
| pe-games | 16 | All none |
| pe-personal-exercise-fitness | 11 | Covered: continuous, interval, fartlek, circuit, applying principles. Thin: weight training (one line). None: aerobics, spinning, indoor rowing, core stability, the 5/15/5 assessed programme |

## Structural problems found

1. **Duplication.** The pages show 190 copied note blocks, but only 97 are distinct; 75
   appear in two or more chapters. The `pe9` coach and official notes appear in structures,
   ethics and games. The `pe2` training notes appear in planning and personal-exercise. `pe1`
   and `pe6` repeat in athletics. This breaks NOTES_STANDARD rule 2 (say each fact once).
2. **Off-topic notes.** Ethics shows no ethics notes. Planning shows training methods.
   Adventure and aquatics show general injury notes. The cause is the `legacySources` map in
   `pe-pipeline-content.js`.
3. **Mis-tagged past-paper questions** visible on the pages:
   - an aesthetics question in the skill chapter
   - a technology question in performance demands
   - skill-learning and economy-of-movement questions in structures
   - a media and body-image question in promoting
   - two media questions in inclusion
   - an aesthetics question in business
   - nutrition and concentration questions in athletics.

   These are `chapterId` tags in `pe-exam-questions.js`.
4. **Practice questions labelled as past papers.** `generated-notes-content.js` labels
   authored practice questions "Past-paper application" in six chapters (planning, gender,
   adventure, aquatics, games, personal-exercise). Practice questions are also misplaced: a
   recovery question in ethics, planes and levers in artistic, carb loading in aquatics.
5. **Filler.** Every "Connected course content" block opens with the same sentence ("Apply
   these connected concepts…"), which NOTES_STANDARD rule 3 bans.
6. **No real past-paper question** is tagged to planning, gender, adventure, aquatics, games or
   personal-exercise.
