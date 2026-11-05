# Leaving Cert Home Economics – Scientific and Social (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format,
  and a worked example). This outline says **what** each chapter's notes must cover; that file
  says **how** to write them. Do not write notes from this outline alone: an information package
  (`course-outlines/packages/home-economics/`, see `packages/README.md`) is written first.
- **The syllabus:** the NCCA *Leaving Certificate Home Economics – Scientific and Social Syllabus
  (Ordinary Level and Higher Level)*, © 2001, introduced in schools in September 2002 and first
  examined in 2004. It is the syllabus examined in **June 2027**. The official PDF is
  `pipeline/resources/home-economics/spec-syllabus.pdf` (also
  `relevant-resources/syllabi/home-economics.pdf`), downloaded from curriculumonline.ie
  (`SCSEC21_Home_Economics_syllabus_eng.pdf`). Section numbers in brackets, e.g. **[1.1.2]**, are
  the syllabus's own topic numbers.
- **Do not use the new Leaving Certificate Home Economics specification.** The NCCA is
  redeveloping the subject in Senior Cycle Tranche 3: a draft specification was out for public
  consultation from 9 February to 17 April 2026, for introduction in schools no earlier than
  September 2027 (first examination 2029 at the earliest). It is a different course. The SEC's
  *Assessment Arrangements 2027* lists Home Economics Scientific and Social among the subjects
  that are **not** revised (only tranche-1 subjects are asterisked), and sets 2027 adjustments
  to the existing syllabus. Ignore any content written for the draft specification or for
  Junior Cycle Home Economics.
- **Chapters** are the app's 36 home economics chapter IDs (`data.js`,
  `pipeline/scaffold/home-economics.json`). The 31 original IDs are unchanged; five were added on
  2026-11-05 when the syllabus content with no natural home was given its own chapter:
  `hom-food-industry`, `hom-fruit-vegetables`, `hom-resource-management`, `hom-home-interior` and
  `hom-home-services`. Each chapter has a review outcome `<chapter-id>-1` (the chapter's test
  questions and generated notes) and one learning outcome per numbered subsection below,
  `<chapter-id>-s<n>`, in the same order. Notes are written per subsection.
- **Legislation and public bodies:** use the Acts, regulations, schemes and bodies in force for
  the June 2027 examination, as named in this outline. Where the 2001 syllabus names an Act or
  body that has since been replaced, revoked or renamed, this outline gives the current one in
  its place; do not write notes on the superseded ones. Appendix A lists each change.
- **What each subsection contains:**
  - **"Syllabus"** is the syllabus's "content: expected knowledge and understanding" column, close
    to its wording. This is the required scope; every item must be covered. Items marked
    **[HL]** are printed in black in the syllabus, which means Higher Level only.
  - **"Settings"** are the syllabus's own examples (its "e.g." items) and the specific
    activities in its "activities to support the course objectives" column. They are
    suggestions, not requirements, but they are good default examples and practical contexts.
  - **"Also examined"** lists things SEC papers (2004–2026, in
    `home-economics-exam-questions.js`) have asked that go beyond the syllabus wording, with the
    years. Notes must cover them too: the syllabus says that where legislation or regulations
    are referred to, candidates are expected to know the **most recent developments**.
  - **"SimpleStudy"** names the matching topic(s) in SimpleStudy's Higher Level course (recorded
    2026-08-07, see `pipeline/resources/home-economics/guide-simplestudy.md`). Use them for
    structure and pacing only; write all prose in your own words. "None" means SimpleStudy has
    no matching topic.
- **Higher vs Ordinary level:** one common syllabus. Some content is Higher Level only and is
  marked **[HL]** here; mark nothing else as HL. The complete HL list is in Appendix C. Higher
  Level students are also expected to show greater depth of understanding and proficiency.
- **Structure and weightings:** Core = Food Studies **45%**, Resource Management and Consumer
  Studies **25%**, Social Studies **10%**; one Elective = **20%**. Students take **one** of:
  Elective 1 Home Design and Management, Elective 2 Textiles, Fashion and Design, or Elective 3
  Social Studies. Notes must be written for all three electives.
- **Where the syllabus sets a number or choice, write content for every option:** one large and
  one small appliance [2.1.5]; one appliance with a motor, one with a heating element, one
  refrigeration appliance and a microwave oven [2.1.5]; one fire-retardant finish [2.1.6]; three
  common food poisoning bacteria [1.3.8]; two types of pastry [1.3.4]; two methods of
  preservation applied in practice [1.3.9]; three profiles of processed food [1.3.5]; one system
  of central heating [4.5.3]; one natural fabric, one manufactured fabric and one blend [5.2];
  two (OL) or three (HL) fabric construction techniques and finishes, two colour application
  methods, two design application methods and two performance tests [5.2]; two child care options
  [6.3.2]; two leisure facilities [6.4]. Give enough options that a student can choose (e.g. at
  least three bacteria, several fabrics, several heating systems).
- **Assessment (June 2027),** from SEC documents:
  - **Written paper** (2 hours 30 minutes; Higher and Ordinary Level), as set out on the SEC's
    2025 Higher Level paper and marking scheme:
    - Section A, **60 marks**: answer ten questions, 6 marks each (14 questions set).
    - Section B, **180 marks**: Question 1 (compulsory, data-based, 80 marks) and any two of
      Questions 2–5 (50 marks each).
    - Section C, **40 or 80 marks**: one elective question or Question 4 (core), answering part
      (a) and either (b) or (c). Electives 1 and 3 and Question 4 are worth 80 marks [(a) 50,
      (b) or (c) 30]; Elective 2 is worth 40 marks [(a) 25, (b) or (c) 15]. Candidates who
      submitted Textiles, Fashion and Design coursework may attempt only Question 2.
    - Paper total **320 marks**, or **280 marks** for Elective 2 candidates. The SEC grades the
      paper on these totals (2025 Higher Level H1: 288–320, or 252–280).
  - **2027 adjustments** (SEC *Assessment Arrangements 2027*): Section A has 14 questions, answer
    10; Section C includes the 80-mark core Question 4, examining Food Studies, Resource
    Management and Consumer Studies and Social Studies in the same layout and choice as the
    elective questions. Core chapters therefore need notes deep enough for an 80-mark Section C
    question as well as Section B.
  - **Food Studies practical coursework** (all candidates): **20% of total marks** (SEC). Each
    assignment is marked out of 80: investigation (analysis and research) 32, planning and
    preparation 8, implementation 28, evaluation 12. Normally four of the five SEC assignments
    are presented; **for 2027, two of five**, and where more are presented the two
    highest-scoring count. Details are in `hom-cooking-methods` s7.
  - **Textiles, Fashion and Design coursework** (Elective 2 only): a garment, 100 marks weighted
    to **10%**; for 2027 the garment must include one mandatory process from a choice of three
    set by the SEC.
  - The written paper is therefore the remaining 80% (70% for Elective 2 candidates, whose
    garment carries 10%).
  - Sources: SEC *Assessment Arrangements 2027* (Home Economics Scientific and Social page); SEC
    Leaving Certificate 2025 Home Economics Higher Level Section A answerbook, Section B and C
    paper and marking scheme; SEC *Food Studies Assignments (20% of Total Marks)*; SEC Food
    Studies Practical – Coursework Journal (2025).

---

## Core Area 1 — Food Studies (45%)

### hom-proteins — Proteins and Amino Acids [1.1.2, 1.3.2]
1. **Composition and amino acids** [1.1.2]: elements in protein; basic structure of amino acids;
   **[HL]** essential amino acids, peptides, the peptide bond, hydrolysis.
   - Also examined: essential vs non-essential amino acids with examples (2026H, 2017H); the
     diagram of the basic amino acid structure (2004H); peptide bond formation (2011H, 2008H).
   - SimpleStudy: none.
2. **Structure** [1.1.2]: outline knowledge of primary structure; **[HL]** secondary and
   tertiary structure.
   Settings: models using different-coloured blocks or shapes to show amino acids.
3. **Classification** [1.1.2]: simple proteins — animal (**[HL]** fibrous, globular) and plant
   (**[HL]** glutelins, prolamines); conjugated proteins.
   Settings: a poster of examples of each class.
4. **Sources** [1.1.2]: animal and plant protein sources; distribution in food of albumin,
   casein, gelatine and gluten, and **[HL]** myosin, actin and collagen.
   Also examined: naming a food source of named proteins (2016H, 2011H, 2005H).
5. **Properties** [1.1.2]: denaturation–coagulation; **[HL]** foam formation and gel formation;
   the effects of dry and moist heat, mechanical action, pH and enzymes on protein during
   preparation, cooking and digestion.
   - Settings: experiments or cookery activities showing these properties in practice.
   - Also examined: Maillard reaction (2015O); causes of denaturation with examples (2026H,
     2021H, 2007H).
6. **Biological functions** [1.1.2]: structural proteins, physiologically active proteins and
   nutrient proteins.
7. **Biological value** [1.1.2]: complete and incomplete protein; complementation (supplementary
   value).
   - Settings: planning and preparing simple meals that illustrate protein complementation.
   - Also examined: high and low biological value foods (2017O, 2007O); low-cost protein foods
     and value for money when buying protein foods (2026H, 2014H, 2006H).
8. **Energy value** [1.1.2]: contribution to the total energy value of the average diet; protein
   as a supplementary energy source; **[HL]** deamination.
   Also examined: deamination (2026H, 2024H, 2015H).
9. **Alternative (novel) protein foods** [1.3.2, "meat, fish, eggs and alternatives"]: the
   alternatives to meat as a food commodity: nutritional significance, contribution to the diet,
   selection, storage, preparation, cooking and processing.
   - Also examined: plant and micro-organism sources and products (2024H, 2012H); stages in
     manufacture of one (2022H, 2018H); tofu and other vegan protein alternatives (2021H,
     2016H); protein bars and high-protein products evaluated from data (2026H, 2023O).
   - SimpleStudy: Alternative Protein Foods.

Digestion and absorption of protein is in `hom-digestion-metabolism`.

### hom-carbohydrates — Carbohydrates and Dietary Fibre [1.1.3]
1. **Formation of carbohydrates in plants** [1.1.3]: photosynthesis.
2. **Composition, structure and classification** [1.1.3]: elements; **[HL]** basic structure of
   a monosaccharide; **[HL]** formation of disaccharides and polysaccharides; classification into
   monosaccharides, disaccharides and polysaccharides.
   - Settings: labelled blocks to show the formation of disaccharides and polysaccharides.
   - Also examined: chemical formula and example for each class in a table (2026H, 2017H, 2015H,
     2011H).
3. **Sources** [1.1.3]: of monosaccharides, disaccharides, starch, cellulose, pectin and
   non-starch polysaccharides (dietary fibre).
   Settings: a collage or poster of sources.
4. **Properties** [1.1.3]: sweetness, solubility, gelatinisation of starch; **[HL]** hydrolysis,
   to include inversion; **[HL]** crystallisation, caramelisation, dextrinisation; **[HL]**
   pectin extraction and gel formation; the effects of dry and moist heat on carbohydrates
   during cooking; the effects of enzymes on carbohydrates during digestion.
   - Settings: experiments or cookery activities showing caramelisation, inversion of sugar,
     dextrinisation and gelatinisation of starch.
   - Also examined: properties of sugar with a culinary use for each (2024H, 2021H, 2017H);
     hygroscopic starch (2012O).
5. **Functions** [1.1.3]: biological functions of sugars, starch and non-starch polysaccharides;
   culinary functions of sugars, starch and pectin.
6. **Energy value and dietary fibre targets** [1.1.3]: contribution to the total energy value of
   the average diet; dietary targets for non-starch polysaccharide intake and how they can be
   achieved.
   - Settings: a comparative study of the energy value of foods with and without added sugar
     (e.g. breakfast cereals); comparing the energy in a food (e.g. a bar of chocolate) with the
     time an activity takes to use it up.
   - Also examined: the EFSA fibre recommendation and strategies to meet it (2016H); reducing
     sugar intake (2024H, 2019O); effects of high sugar intake (2018O, 2017H); artificial
     sweeteners (2026H, 2011H — also in `hom-food-additives`).

Digestion, absorption and utilisation of glucose is in `hom-digestion-metabolism`.

### hom-lipids — Lipids and Fats [1.1.4, 1.3.2]
1. **Fatty acids** [1.1.4]: classification as saturated, monounsaturated and polyunsaturated;
   essential fatty acids; **[HL]** cis and trans fatty acids; **[HL]** structure of saturated,
   monounsaturated and polyunsaturated fatty acids.
   Also examined: omega-3 fatty acids, their function and sources (2016H, 2015O, 2007H); LDL and
   HDL (2012H); significance of fatty acids in the diet (2025H, 2018H).
2. **Triglycerides and the classification of lipids** [1.1.4]: **[HL]** chemical composition and
   molecular structure of a triglyceride; classification of lipids according to source and
   proportion of saturated, monounsaturated and polyunsaturated fatty acids.
3. **Sources** [1.1.4]: animal, marine and vegetable sources; **[HL]** distribution of
   saturated, monounsaturated and polyunsaturated fatty acids in food.
   Settings: a poster of sources.
4. **Properties** [1.1.4]: melting, smoke and flash points; formation of emulsions, **[HL]** to
   include the identification and function of emulsifying agents and stabilisers; **[HL]**
   plasticity, rancidity and hydrogenation; **[HL]** identification and functions of
   antioxidants.
   - Settings: comparing the melting, smoke and flash points of common fats and oils; making
     mayonnaise or other dressings to show emulsion formation.
   - Also examined: oxidative and hydrolytic rancidity (2021H, 2013H).
5. **Functions and energy value** [1.1.4]: biological functions of lipids in the diet;
   contribution to the total energy value of the average diet.
   Also examined: health effects of a diet high in saturated fat (2024H); cholesterol (2007H).
6. **Fats and oils as a food commodity** [1.3.2]: nutritional significance, contribution to the
   diet, selection, effects of storage, preparation, cooking and processing of fats and oils
   (butter, margarine and spreads, oils); storage of foods containing lipids; use of fats and
   oils in cooking.
   - Also examined: production of margarine with packaging and labelling (2024H); low-fat and
     functional dairy spreads (2013H); evaluating spreads from data (2008H).
   - SimpleStudy: Food Commodities and Extras.

Digestion, absorption and utilisation of triglycerides is in `hom-digestion-metabolism`.

### hom-vitamins-minerals — Vitamins and Minerals [1.1.5, 1.1.6]
1. **Fat-soluble vitamins** [1.1.5]: sources, functions, effects of deficiency, RDAs and
   **[HL]** properties of vitamins A (retinol and beta-carotene), D (cholecalciferol),
   E (tocopherols) and K (naphthoquinones).
   - Settings: evaluating fresh and processed foods as providers of vitamins, using food labels
     and food composition tables.
   - SimpleStudy: Vitamins.
2. **Water-soluble vitamins C, B12 and folate** [1.1.5]: sources, functions, effects of
   deficiency, RDAs and **[HL]** properties of vitamin C (ascorbic acid), B12 (cobalamin) and
   folate.
   SimpleStudy: Vitamins.
3. **The other B-group vitamins** [1.1.5]: sources, functions, effects of deficiency and
   **[HL]** properties of the other B-complex vitamins as a group, to include B1 (thiamine),
   B2 (riboflavin), niacin and B6 (pyridoxine).
   Also examined: deficiency diseases matched to the vitamin (2025H, 2021H, 2004H).
4. **Mineral elements** [1.1.6]: identification of the major mineral elements and **[HL]** trace
   mineral elements needed in the diet; sources, functions, effects of deficiency and RDAs of
   calcium and iron, and **[HL]** zinc, iodine, potassium and sodium.
   - Also examined: anaemia (2017H, 2012O); goitre and osteomalacia (2019H); sodium (2025H,
     2012H); potassium (2008H).
   - SimpleStudy: Minerals.
5. **Factors affecting the absorption of minerals** [1.1.6]: the role of vitamins in the
   absorption of calcium and iron; haem and non-haem iron; **[HL]** the effects of phytates and
   oxalates on the absorption of calcium.
   Also examined: 2026H, 2024H, 2023H, 2021H, 2014H; calcium inhibitors (2025H, 2007H).

Vegetables and fruit as a food commodity are in `hom-fruit-vegetables`.

### hom-digestion-metabolism — Digestion and Metabolism [1.1.2, 1.1.3, 1.1.4]
1. **Digestion and absorption of protein** [1.1.2]: hydrolysis of protein and the digestion
   sequence (organ, secretion, enzyme, substrate, product); absorption, and **[HL]** outline of
   the utilisation of amino acids.
   Also examined: completing the organ–secretion–enzyme–substrate–product table (2025H, 2010H);
   rennin and caseinogen (2008O).
2. **Digestion and absorption of carbohydrates** [1.1.3]: hydrolysis, digestion sequence and
   absorption mechanism; **[HL]** outline of the utilisation of glucose.
   Also examined: the digestion table for carbohydrates (2022H, 2007H).
3. **Digestion and absorption of lipids** [1.1.4]: hydrolysis, digestion sequence and absorption
   mechanism; **[HL]** outline of the utilisation of triglycerides.
   Also examined: the digestion table for lipids (2014H, 2005H).

Each subsection must name the full route through the alimentary canal (mouth, stomach, small
intestine, villi and lacteals, hepatic portal vein, liver) for that nutrient. SimpleStudy: none.

### hom-energy-nutrition — Energy Balance and Nutritional Needs [1.2.1, 1.2.2, 1.2.4, 1.1.7]

1. **Energy requirements and the role of energy** [1.2.1]: factors determining energy
   requirements; the role of energy in the body: basal metabolic rate, growth, physical activity.
   - Also examined: BMR and the factors affecting it (2026H, 2023H, 2021H).
   - SimpleStudy: Nutrition and Energy.
2. **Energy balance** [1.2.1]: the importance of balancing energy intake and output.
   - Settings: case studies of lifestyle and diet with recommendations to adjust intake and
     expenditure; menus for the individuals or groups in the case studies.
   - Also examined: causes and health risks of obesity (2015O, 2013H, 2007O); BMI from data
     (2017H).
3. **Energy value of the nutrients** [1.1.2, 1.1.3, 1.1.4]: the energy value of protein,
   carbohydrate and lipid and the contribution of each to the total energy value of the average
   diet.
4. **Dietary guidelines** [1.2.2]: current nutritional guidelines: how and why they are
   formulated; use of RDAs; use of food composition tables.
   - Settings: food composition tables, current dietary guidelines and computer programs.
   - Also examined: the food pyramid (2026O, 2013O); serving recommendations (2007O); food
     supplements (2013O); lifestyle guidelines for health (2026O).
   - SimpleStudy: Diet and Health.
5. **The Irish diet** [1.2.4]: changes in food and eating patterns in the Irish diet since the
   beginning of the twentieth century; comparison of the Irish diet with current dietary
   guidelines; aspects of malnutrition currently identified — low dietary fibre, high saturated
   fat, relatively low iron and calcium intakes — with causes, effects and corrective measures.
   - Settings: comparing a typical day's menu from the start of the twentieth century with one
     from today against current guidelines; a visiting speaker on diet and disease (e.g. Irish
     Cancer Society, Irish Heart Foundation, a dietitian, the Health Promotion Unit).
   - Also examined: contemporary trends in Irish eating patterns (2024H, 2021H, 2015O, 2010H);
     data-based questions on Irish consumption (Q1 most years).
   - SimpleStudy: Food Choices and Irish Food.
6. **Water** [1.1.7]: general properties; biological importance. Placed here provisionally
   (see Appendix B).
   Also examined: biological functions of water (2019H, 2015H, 2012O, 2005H); water in pregnancy
   and sport (2026O, 2023O).

### hom-meal-planning — Meal Planning and Special Diets [1.1.1, 1.2.3, 1.3.3]
1. **Food choices** [1.1.1]: factors affecting food choices: culture, eating patterns, sensory
   aspects, nutritional awareness, health status, availability, finance, marketing and
   advertising.
   - Settings: discussing differences in meal patterns between societies; a theme day or week
     on the foods of a culture or period.
   - Also examined: Q1 data questions on food choices (2025H, 2024H, 2023H, 2019H); food choices
     of teenagers, students and pre-school children (2022O, 2017O, 2005O).
   - SimpleStudy: Food Choices and Irish Food.
2. **Dietary requirements through the life cycle** [1.2.3, 1.3.3]: factors affecting dietary and
   food requirements — age, sex, health status, pregnancy and activity; the requirements of
   babies, children, adolescents, adults, older people, pregnant and breastfeeding women,
   convalescents and active people.
   - Settings: case studies showing the limits on low-income families when planning menus.
   - Also examined: pregnancy (2026O, 2024H, 2017O); pre-school children (2025O, 2022O);
     teenagers (2022H, 2012O); older people (2025H); recovery from illness (2022O); irregular
     work schedules (2021H, 2016H).
   - SimpleStudy: Diet and Health.
3. **Diet-related problems** [1.2.3]: the inter-relationship of dietary deficiencies and
   excesses with bowel disease, osteoporosis, obesity, coronary heart disease, diabetes and
   dental caries.
   - Also examined: types of diabetes (2021H, 2019H, 2011H); bowel disease (2016H, 2019O);
     osteoporosis (2025H, 2024H, 2023O — tagged to `hom-vitamins-minerals`).
   - SimpleStudy: Diet and Health.
4. **Modified diets** [1.2.3]: the specific dietary requirements of the coronary heart disease
   and lacto-vegetarian diets, and **[HL]** the vegan, coeliac and diabetic diets.
   Also examined: CHD guidelines (2019H, 2008O, 2007H); coeliac guidelines (2025H, 2022H, 2006H);
   vegan menus and nutrients (2022H, 2009H, 2004H); how manufacturers and retailers meet special
   dietary needs (2009H); food labelling for special diets (2024H, 2023O).
5. **Meal management and planning** [1.3.3]: planning meals with reference to current dietary
   guidelines; dietary requirements through the life cycle; the requirements in [1.2.3] and
   [1.2.4]; resources available — knowledge and skills, time, money, equipment, choice of foods.
   - Also examined: setting out a three-meal menu for a stated person (most Ordinary Level
     papers); money, time and equipment in family meal planning (2025O, 2008O); reducing food
     waste and the food bill (2024O, 2009O).
   - SimpleStudy: Food Preparation.

### hom-food-industry — The Irish Food Industry [1.3.1]
1. **Structure of the Irish food industry** [1.3.1]: brief outline of its structure, to include
   identification of the various sectors and the major food imports and exports.
   - Settings: collect information on a local factory, business or home enterprise and assess
     how it fits into the industry structure, what it contributes to the area and the careers it
     offers.
   - Also examined: sectors of the food industry (2024O, 2019H, 2012H); food exports and imports
     (2012O, 2010H, 2008O); state agencies in the food industry, including Bord Bia (2014H,
     2010O, 2007H, 2006O).
2. **Small businesses and home enterprises** [1.3.1]: their role within the food industry.
   Also examined: artisan producers and small businesses (2024H, 2017H, 2011H, 2009H); speciality
   foods (2022H, 2012H); the growth of small Irish producers (2021O, 2012O).
3. **Careers in food and related industries** [1.3.1]: outline knowledge.
   Also examined: 2010H, 2010O, 2005H.

SimpleStudy: none.

### hom-meat-preparation — Meat: Selection, Properties, and Cooking [1.3.2]
1. **Nutritional significance and structure of meat** [1.3.2]: nutritional significance and
   contribution to the diet of meat (red meat, poultry, offal); the structure of meat (muscle
   fibres, connective tissue, fat) and the proteins in meat.
   Also examined: nutritive and dietetic value (2025H, 2023O, 2010O); proteins in meat (2018H,
   2006H).
2. **Selection and storage** [1.3.2]: buying meat and meat products; effects of storage and safe
   storage.
   Also examined: Bord Bia Quality Assurance Scheme and other measures to keep meat safe (2025H,
   2023H); factors affecting consumer decisions when buying meat (2010H, 2005O).
3. **Preparation and cooking** [1.3.2]: causes of toughness; methods of tenderising and their
   principles; effects of cooking on meat; suitable cooking methods for different cuts.
   Also examined: evaluating one method of cooking meat (2023H); low-income family menus with
   meat (2023O, 2010O).
4. **Meat processing and meat products** [1.3.2]: processed meats; one process used to extend
   the shelf life of meat (method and underlying principle).
   Also examined: 2014H, 2010O.

SimpleStudy for all four: Food Commodities and Extras.

### hom-fish-seafood — Fish and Seafood [1.3.2]
1. **Classification, nutritional significance and contribution to the diet** [1.3.2]: white,
   oily and shellfish (crustaceans and molluscs); nutritive and dietetic value; omega-3 fatty
   acids and vitamin D in oily fish.
   Also examined: 2023H, 2022O, 2016H, 2015O, 2010H, 2004H.
2. **Selection, spoilage and storage** [1.3.2]: freshness and quality on buying; causes of fish
   spoilage; effects of storage; freezing fresh fish.
   Also examined: causes of spoilage (2016H, 2006H); buying guidelines (2022O, 2004H).
3. **Preparation and cooking** [1.3.2]: effects of cooking on fish; moist and dry methods
   suitable for fish and their underlying principles.
   Also examined: 2022H, 2015O, 2010H.
4. **Fish processing and fish products** [1.3.2]: methods of processing to extend shelf life
   (freezing, canning, smoking, salting); processed fish products.
   Also examined: hot and cold smoking (2025H, 2019H); one process in detail (2023H).

SimpleStudy for all four: Food Commodities and Extras.

### hom-dairy-eggs — Dairy Products and Eggs [1.3.2, 1.3.5]
1. **Milk: nutritional significance and contribution to the diet** [1.3.2]: composition;
   nutritive and dietetic value; types of milk (whole, low-fat, fortified and others).
   - Also examined: whole, skimmed, semi-skimmed and fortified milk (2014O, 2010O); milk in
     young children's diets (2021H); choosing milk from data (2022O).
   - SimpleStudy: Milk and Milk Products.
2. **Milk processing** [1.3.2, 1.3.5]: pasteurisation, homogenisation, sterilisation and
   ultra-heat treatment (temperature, time, effect); milk as the syllabus's example of "food
   processed to extend shelf life" in a processed-food profile (stages of production, packaging,
   labelling).
   Also examined: milk processing table (2026H, 2017H, 2008H); one process in full (2024O, 2021H,
   2011H).
3. **Cream, butter and yoghurt** [1.3.2]: nutritional significance, selection, storage, uses and
   processing.
   Also examined: yoghurt manufacture (2024H, 2006H); bio-yoghurt cultures (2008O); measures
   taken by the dairy industry to meet consumer trends (2021H, 2006H).
4. **Cheese** [1.3.2]: classification; nutritive and dietetic value; production (lactic acid
   bacteria, rennet, stages, packaging and labelling); effects of cooking; culinary uses.
   Also examined: production of cheese (2025H, 2017H, 2024H, 2010H); Irish farmhouse cheese
   (2026O, 2019O).
5. **Eggs: structure, nutritional significance and contribution to the diet** [1.3.2].
   Also examined: 2021H, 2016O, 2015H.
6. **Eggs: selection, storage, properties and culinary uses** [1.3.2]: quality and labelling;
   storage; coagulation, aeration (foam formation) and emulsification and their culinary uses;
   effects of heat.
   Also examined: egg labelling (2021H, 2011O); quality assurance in egg production (2015H);
   organic eggs and lecithin (2019H).

### hom-cereals-grains — Cereals and Grains [1.3.2, 1.3.4, 1.3.5]
1. **Structure and nutritional significance** [1.3.2]: structure of the grain (bran, endosperm,
   germ) and the nutritional significance of each part; nutritive and dietetic value of
   cereals; wholegrain cereals.
   Also examined: 2026H, 2022O, 2015H, 2012O.
2. **Cereals and cereal products** [1.3.2]: the main cereals (wheat, rice, oats, maize, barley,
   rye) and products made from each; breakfast cereals; selection and effects of storage.
   Also examined: products from named cereals (2023O, 2018O, 2008H); storing cereal products
   (2018O); fortification (2012O).
3. **Milling and flour** [1.3.2, 1.3.5]: production of flour; types of flour and their uses;
   flour as the syllabus's example of "food that undergoes extensive processing" in a
   processed-food profile (stages of production, packaging, labelling).
   Also examined: production of flour (2026H); types of flour and uses (2021O, 2013H, 2010O).
4. **Preparation and cooking of cereals** [1.3.2, 1.3.4]: effects of heat on cereals and starch;
   raising agents and the principles behind them.
   Also examined: raising agents for named baked products (2023O, 2011O); effects of cooking on
   rice (2025O).
5. **Two types of pastry** [1.3.4]: classification, preparation, cooking and presentation of two
   types of pastry, with the principles for success.
   Also examined: 2026O, 2024O, 2022H, 2019O, 2010H.

SimpleStudy: Food Commodities and Extras; Food Preparation.

### hom-fruit-vegetables — Fruit and Vegetables [1.3.2]
The syllabus lists "vegetables and fruit" among the main food commodities: their nutritional
significance, contribution to the diet, selection, effects of storage, preparation, cooking and
processing.
1. **Classification, nutritional significance and contribution to the diet** [1.3.2]: classes of
   vegetables and of fruit; nutritive and dietetic value; contribution to the diet and current
   healthy-eating guidance on servings.
   - Also examined: classes (2019O, 2016O, 2012O, 2004O); nutritional significance of vegetables
     (2026H, 2022H, 2019H, 2012H, 2008H); ways to eat more fruit and vegetables (2025O, 2019H,
     2017O, 2004O); consumption data (2017O, 2011O).
   - SimpleStudy: Food Commodities and Extras.
2. **Selection, storage and spoilage** [1.3.2]: buying fresh, frozen, canned, dried and
   pre-prepared fruit and vegetables; quality and grading; effects of storage and storage
   guidelines; causes of spoilage.
   Also examined: EU grading classes (2006H); options when buying (2012H); pre-prepared fruit and
   vegetables (2017O); storage (2024O, 2021O); spoilage by enzymes, moisture loss and microbial
   contamination (2026H).
3. **Preparation and cooking** [1.3.2]: the effects of preparation and cooking on nutrients,
   colour, texture and flavour; guidelines that retain nutrients.
   Also examined: 2026H, 2021O, 2019H, 2016O, 2012O, 2011O, 2008O, 2005O.
4. **Processing** [1.3.2]: commercial processing of fruit and vegetables (freezing, canning,
   drying) and its effects; processed and convenience products.
   Also examined: canning and dehydration (2021H); effects of freezing and canning on vitamin C
   and sodium (2005H); additives in processed fruit and vegetables (2004O).

Home preservation of fruit and vegetables is in `hom-food-preservation`.

### hom-cooking-methods — Cooking Methods and Heat Transfer [1.3.4]
1. **Physical and chemical changes during preparation and cooking** [1.3.4]: enzymic browning,
   non-enzymic browning, loss of nutrients.
   - Settings: an investigation to assess the control of enzymic browning, e.g. on a fresh apple.
   - Also examined: 2023H, 2021H, 2019H, 2009O, 2009H.
2. **Heat transfer and the principles of cooking** [1.3.4]: principles underlying the cooking of
   food and their correct application to the commodities in [1.3.2]; conduction, convection and
   radiation.
   Also examined: 2025H, 2024O, 2018H, 2012H.
3. **Choice of cooking method** [1.3.4]: choosing and applying suitable cooking methods to
   conserve nutrients and improve palatability; moist, dry and fat-based methods.
   Also examined: poaching and pot roasting (2007H); grilling (2023O); steaming for an older
   person (2025H).
4. **Soups and sauces** [1.3.4]: classification, preparation, cooking and presentation of soups
   and sauces.
   Also examined: roux sauces (2023H); classes of sauces and soups (2022O, 2015H, 2014O, 2006H);
   convenience soups (2014O).
5. **Food preparation and cooking equipment** [1.3.4]: selection, safe use and care.
6. **Recipe balance, presentation and dishes for different needs** [1.3.4]: recipe balance and
   adaptation; aesthetic awareness in choosing, preparing and presenting food; preparation and
   presentation of dishes and meals for individuals, family groups and the modified diets in
   [1.2.3] and [1.2.4].
   Also examined: reasons for modifying recipes (2013H); aesthetic awareness (2013H).
7. **Food Studies practical coursework (20% of total marks)** [assessment]: how the SEC
   coursework works, from the SEC's own documents.
   - Areas of Practice: A Application of Nutritional Principles; B Food Preparation and Cooking
     Processes (new skills or equipment); C Food Technology; D Properties of a Food; E
     Comparative Analysis including Sensory Analysis.
   - What the investigation covers in each area (SEC recording criteria): A — the nutritional
     needs investigated, appropriate meal-planning guidelines, suitable or modified dishes; B —
     the preparation process, skill or equipment, the key points for success, dishes that
     illustrate it; C — the processing method and its principles, containers, packaging and
     labelling, suitable foods or dishes; D — definition of the property, the associated
     principles, dishes that illustrate it; E — the testing technique and possible outcomes, the
     foods or products tested, the conditions to control. Every area cites sources of
     information.
   - Marks for each assignment: Investigation (analysis and research) 32; Planning and
     Preparation (ingredients with quantities and costing, key equipment) 8; Implementation (the
     procedure followed, key factors considered, safety and hygiene) 28; Evaluation (of the
     implementation and of the assignment's specific requirements) 12.
   - Rules: each assignment is recorded in the SEC's digital Food Studies Practical Coursework
     Journal under these headings; dishes must meet the assignment, may not be repeated or
     partially repeated across assignments, and should use fresh foods rather than convenience
     foods. For 2027 candidates present two of the five assignments the SEC set, and the two
     highest-scoring count.
   - The 2027 assignment titles are in the SEC brief linked from *Assessment Arrangements 2027*;
     add them to the package when available.

Pastry is in `hom-cereals-grains`; critical evaluation, comparison of home-made and commercial
products, and sensory analysis are in `hom-food-additives`. SimpleStudy: Food Preparation.

### hom-food-additives — Food Additives and Processing [1.3.4, 1.3.5, 1.3.6]
1. **Processed foods and three processed-food profiles** [1.3.5]: the range of processed foods
   available; profiles of three types of processed food: food that undergoes extensive
   processing, food processed to extend shelf life, and added-value food.
   - Settings: flour (extensive processing — see `hom-cereals-grains`), milk (extending shelf
     life — see `hom-dairy-eggs`), prepared foods or meals (added value); a visit to a local
     factory or processing plant, e.g. a creamery, mill or cheese plant.
   - Also examined: added-value food profile (2023H, 2009H); functional foods (2025H, 2014H);
     genetically modified and organic food (2016H); merits of processed and convenience foods
     (2026H, 2018H, 2006H); ultra-processed foods (2025O); fortification (2016H).
2. **Packaging and labelling** [1.3.5]: packaging materials and their suitability for purpose
   and environmental impact; food labelling as a source of consumer information.
   Also examined: packaging materials (2026O, 2022H, 2010H); modified atmosphere and
   biodegradable packaging (2017H, 2004H); labelling (2026H, 2024O, 2016H, 2005H).
3. **Contaminants in the food chain** [1.3.5]: contaminants that may enter at various stages of
   processing, e.g. antibiotics and chemicals.
   Also examined: pesticides and metal residues (2013H); 2024H, 2004H.
4. **Classes of food additives** [1.3.6]: classification, examples, origin and functions of food
   additives, to include colourings, flavourings, sweeteners, preservatives, nutritional
   supplements and **[HL]** physical conditioning agents.
   - Settings: examining food labels to find the additives used and suggest reasons.
   - Also examined: physical conditioning agents (2025H, 2023H, 2010H, 2006H); artificial
     sweeteners (2026H, 2021H, 2011H); antioxidants, flavourings and emulsifiers (2018H, 2012H,
     2011H).
5. **Legal control of additives in the EU** [1.3.6]: outline of the legal control of the use of
   preservatives, colours, emulsifiers and antioxidants in the European Union under Regulation
   (EC) No 1333/2008 on food additives, to include E numbers.
   Also examined: 2022H, 2018H, 2006H.
6. **Evaluation and sensory analysis** [1.3.4]: critical evaluation of dishes and meals;
   comparative assessment of home-made and commercial products or meals; **[HL]** sensory
   analysis.
   Also examined: categories of sensory test and one test from each (2013H, 2007H, 2005H); one
   difference test in full (2026H, 2017H); preference tests (2023H); conditions for accurate
   testing (2026H, 2024H, 2017H, 2015H, 2007H); uses in the food industry (2013H, 2009H); the
   senses and food choice (2017H, 2007H).

SimpleStudy: Food Processing, Safety, and Hygiene; Food Commodities and Extras.

### hom-food-preservation — Food Preservation and Storage [1.3.9]
1. **Principles of food preservation** [1.3.9]: why food is preserved; the principles that
   underlie all methods (removing the conditions micro-organisms and enzymes need).
   Also examined: causes of food spoilage (2025O, 2010O); advantages of preservation (2025O).
2. **Freezing** [1.3.9]: principles and methods; quick and slow freezing; commercial and home
   freezing; blanching; effects on food.
   Also examined: quick freezing (2022H, 2013H); freezing vegetables (2016H, 2011H); commercial
   methods (2006H); benefits of frozen foods in meal planning (2021H, 2016H).
3. **Heat processing** [1.3.9]: canning, bottling and other heat treatments; jam making and its
   principles.
   Also examined: principles of jam making (2024H); canning and dehydration of fruit and
   vegetables (2021H).
4. **Dehydration** [1.3.9]: principles and methods, including accelerated freeze drying.
5. **Chemical preservation** [1.3.9]: sugar, salt, vinegar, smoke and permitted chemical
   preservatives; chutneys and pickles.
   Also examined: chutney making (2026O, 2011O).
6. **Fermentation** [1.3.9] **[HL]**.
   Also examined: fermentation and its by-products (2017H, 2009H).
7. **Irradiation** [1.3.9] **[HL]**.
   Also examined: 2022H, 2013H, 2008H, 2004H.
8. **Comparative evaluation of preserved foods** [1.3.9] **[HL]**: comparing foods preserved by
   different methods.
   Also examined: a study of one food preserved two ways (2010H); data on vitamin C and sodium
   after freezing and canning (2005H).
9. **Practical application of two methods of preservation** [1.3.9]: two home methods carried
   out in full (method, suitable foods, steps, packaging, safety).
   Also examined: 2022H, 2022O, 2010O, 2008H.

Food storage and reheating are in `hom-food-safety`. SimpleStudy: Food Processing, Safety, and
Hygiene.

### hom-food-safety — Food Safety and Microorganisms [1.3.7, 1.3.8, 1.3.10]
1. **Moulds and yeasts** [1.3.8] **[HL]**: habitat, sources, environmental factors affecting
   growth, structure and reproduction.
   Also examined: one type of mould (2022H, 2015H); conditions for mould growth (2015H, 2006H);
   labelled diagrams of a yeast cell, a mould and a bacterial cell (2016H, 2012H, 2007H).
   SimpleStudy: Microbiology.
2. **Food poisoning bacteria** [1.3.8] **[HL]**: three common strains, with habitat, sources,
   environmental factors affecting growth, high-risk foods, incubation period, toxic and
   infectious food poisoning, and symptoms.
   - Settings: media reports of specific food poisoning cases, identifying contributing factors.
   - Also examined: toxic vs infectious food poisoning (2026H, 2024H, 2021H, 2014H, 2004H);
     psychrophiles, mesophiles and thermophiles (2018H); aerobic, anaerobic and facultative
     micro-organisms (2013H).
   - SimpleStudy: Microbiology.
3. **Micro-organisms and the control of microbial spoilage** [1.3.8]: the role of
   micro-organisms in food spoilage; the principles underlying the control of microbial
   spoilage.
   Also examined: conditions for growth of micro-organisms (2026O, 2013O).
4. **Uses of micro-organisms in food production** [1.3.8]: outline knowledge.
   Also examined: 2022H, 2015H, 2014H, 2008H.
5. **Enzymes and food spoilage** [1.3.8]: the role of enzymes in food spoilage; **[HL]** the
   principles underlying the control of enzymic spoilage.
   Also examined: 2022H, 2015H, 2013H, 2009H.
6. **Safe food preparation** [1.3.10]: food storage, reheating procedures, personal hygiene and
   kitchen hygiene.
   Also examined: 2025H, 2023O, 2022O, 2021H, 2012H, 2004H.
7. **HACCP and ISO 9000** [1.3.10] **[HL]**: hazard analysis in food processing operations.
   Also examined: stages of a HACCP system for a named dish (2021H, 2014H, 2008H); benefits
   (2010H, 2004H).
8. **National agencies in food safety** [1.3.10]: a brief outline of the role of national
   agencies in food safety, to include **[HL]** the Food Safety Authority of Ireland; the
   Department of Health, under which the FSAI operates; and the official agencies that carry out
   food controls under contract to the FSAI — the Health Service Executive (its Environmental
   Health Service and the Public Analyst Laboratories), the Department of Agriculture, Food and
   the Marine, the Sea-Fisheries Protection Authority and the local authorities.
   - Settings: students gather information on national agencies involved in food safety and
     build a file.
   - Also examined: FSAI (2026H, 2023H, 2009H, 2005H); Public Analyst Laboratories (2023H); HSE
     (2019H); Department of Agriculture, Food and the Marine (2012H); environmental health
     officers (2008H).
9. **Food legislation** [1.3.7]: a brief outline of the protection given to the consumer by
   current national and European food legislation, to include:
   - food hygiene: Regulation (EC) No 852/2004 on the hygiene of foodstuffs, given effect in
     Ireland by the European Communities (Hygiene of Foodstuffs) Regulations 2006 (amended 2009
     and 2010);
   - **[HL]** food labelling: Regulation (EU) No 1169/2011 on the provision of food information
     to consumers, given effect by the European Union (Provision of Food Information to
     Consumers) Regulations 2014;
   - **[HL]** the general framework of food law: the Food Safety Authority of Ireland Act 1998
     and Regulation (EC) No 178/2002 (general food law);
   - **[HL]** official controls: Regulation (EU) 2017/625, given effect by the European Union
     (Official Controls in Relation to Food Legislation) Regulations 2020.
   - Settings: students research one piece of legislation and build a shared file.
   - Also examined: the European Communities (Hygiene of Foodstuffs) Regulations 2006, amended
     2009 and 2010 (2025H); food labelling regulations (2010H).

SimpleStudy: Food Processing, Safety, and Hygiene; Microbiology.

---

## Core Area 2 — Resource Management and Consumer Studies (25%)

### hom-resource-management — Family Resource Management [2.1, 2.1.1, 2.1.2]
1. **Family resource management** [2.1]: the purpose of resource management; management systems;
   the family as a managerial unit.
   - Also examined: purpose of family resource management (2015H, 2009H, 2005O); how good
     management systems contribute to a well-run home (2021H, 2006H).
   - SimpleStudy: Resource Management.
2. **Components of management and decision-making** [2.1.1]: **[HL]** inputs (human and material
   resources, needs, wants, goals), throughputs (planning, organising, implementing) and outputs
   (goals achieved, changes in values, goals and standards, satisfaction, evaluation and
   effective use of feedback); decision-making and communication.
   - Settings: case studies planning routines for modern patterns of living, including work
     sharing, responsibility for family tasks, delegation and gender equity; checklists for
     routines and work schedules.
   - Also examined: naming the components (2017H, 2015H, 2011H); applying the management
     framework to a named event (2021H, 2013H, 2006H); decision-making (2013H); resources other
     than money (2011O).
   - SimpleStudy: Resource Management.
3. **Factors that affect management** [2.1.2]: stages in the life cycle, employment pattern,
   culture, values, standards, sex roles, managing a dual role, lifestyle as determined by
   socio-economic status and family composition.
   Also examined: 2023H, 2022O, 2013H, 2011O.

### hom-personal-finance — Personal Finance and Budgeting [2.1.3]
1. **Household income** [2.1.3]: the household as a financial unit within the economy;
   household income and social factors (age, sex, social class, culture); wages, salaries,
   pensions, social welfare allowances and benefits as sources of income.
   - Also examined: gross and net income, PAYE, PRSI, USC and tax credits (2022H, 2018H, 2014O,
     2005H); social insurance and social assistance payments (2024H, 2009H); named welfare
     payments such as the Working Family Payment, Supplementary Welfare Allowance and Child
     Benefit (2023H, 2023O); contributory and non-contributory State pensions (2026H).
   - SimpleStudy: Household Income and Spending Patterns; Management of Household Financial
     Resources.
2. **Household expenditure and budgeting** [2.1.3]: patterns of household expenditure at varying
   levels of income; essential and discretionary expenditure; planning personal and family
   budgets, including credit.
   - Settings: case studies of sample budgets for families on varying incomes.
   - Also examined: a budget plan for a stated household and net income (2025O, 2021O, 2015H,
     2004H); MABS (2026H, 2025O, 2019H, 2010H).
   - SimpleStudy: Budgeting.
3. **Methods of payment and credit** [2.1.3]: methods of payment (cash or credit) for household
   goods and services, with criteria for selection and availability; a brief outline of the
   protection given to the consumer by the Consumer Credit Act 1995 (as amended), including
   hire-purchase and other credit agreements.
   - Settings: investigating forms of credit from advertisements, brochures and credit card
     material; comparing cash prices with the cost of credit.
   - Also examined: Consumer Credit Act 1995 (2026O, 2025H, 2023H, 2010H, 2004H).
   - SimpleStudy: Payment Options and Credit.
4. **Saving** [2.1.3]: methods of saving.
   Also examined: choosing a savings scheme — security, interest, access, tax (2023H, 2015H,
   2010H).
   SimpleStudy: Savings.
5. **Insurance** [2.1.3]: pay-related social insurance, health insurance, household insurance,
   life assurance.
   Also examined: types of life assurance (2025H, 2022H); premium, policy and broker (2017H,
   2006H); household insurance (2023O, 2019O).
   SimpleStudy: Insurance.

Housing finance [2.1.3] is in `hom-housing`.

### hom-consumer-rights — Consumer Rights and Protection [2.2.1, 2.2.2, 2.2.3]
1. **Consumer choices** [2.2.1]: factors that affect consumer decision-making, with specific
   reference to varying household income, merchandising and advertising, packaging and
   labelling.
   - Settings: investigating merchandising techniques and shopping systems — advertising,
     packaging, mail order, "easy-pay" systems, television buying, shopper loyalty schemes,
     discount offers.
   - Also examined: merchandising techniques (2025H, 2023H, 2016H, 2009H, 2005H); online
     shopping (2026O, 2021O, 2018O).
   - SimpleStudy: Consumer Choice; Role of Advertising.
2. **The purchasing process** [2.2.1] **[HL]**: classification of retail outlets, retail
   psychology, shopping patterns, consumer research.
   - Also examined: desk and field research (2025H, 2021H, 2012H); changes in shopping patterns
     (2026H, 2024H, 2016H); classes of retail outlet (2021H).
   - SimpleStudy: Consumer Research.
3. **Consumer responsibility: information and rights** [2.2.2]: the responsibility of the
   consumer in informed decision-making with regard to consumer information and rights.
   Also examined: consumer responsibilities (2023H, 2021H, 2006H).
   SimpleStudy: Consumer Rights and Responsibilities.
4. **Consumer protection legislation** [2.2.3]: the rights of the consumer as defined by current
   legislation, to include the Consumer Rights Act 2022 (statutory rights and remedies for
   goods, services and digital content bought by consumers) and the Consumer Protection Act
   2007 (misleading, aggressive and prohibited commercial practices, enforced by the CCPC).
   - Also examined: Consumer Protection Act 2007 (2024H, 2017H).
   - SimpleStudy: Consumer Protection.
5. **Voluntary and statutory consumer protection bodies** [2.2.3]: e.g. the Competition and
   Consumer Protection Commission, Citizens Information, the Financial Services and Pensions
   Ombudsman, the Advertising Standards Authority.
   Also examined: 2024H, 2022H, 2019H, 2016H, 2015H, 2013H.
   SimpleStudy: Consumer Protection.
6. **Complaints and the small claims procedure** [2.2.3]: procedures to follow when a problem
   occurs with a product or service; the function and operation of the small claims procedure.
   Also examined: 2024O, 2021H, 2018O, 2013O, 2010O.
   SimpleStudy: Consumer Protection.

The environmental part of [2.2.2] is in `hom-environmental-issues`.

### hom-environmental-issues — Environmental Issues and Sustainability [2.2.2]
1. **Renewable and non-renewable resources** [2.2.2]: the consumer's responsibility in managing
   the environment through the use of renewable and non-renewable resources.
   Also examined: 2019H, 2016O, 2012O, 2009H, 2004H.
2. **Recycling and waste management** [2.2.2].
   Also examined: sustainable waste management (2019H, 2014H); initiatives to reduce excess
   packaging (2007H); green dot and eco-label symbols (2022H, 2009O); disposal of electrical
   appliances (2026O, 2008O).
3. **Pollution** [2.2.2]: types, causes and effects of pollution and how consumers can reduce
   it.
   Also examined: air, water and noise pollution (2026O, 2023H, 2017O, 2016H, 2004O); government
   initiatives against pollution (2014O, 2004O).
4. **Environmentally responsible practices in the home** [2.2.2]: the effects on the environment
   of everyday household activities and ways to counteract harmful effects.
   - Settings: group studies of heating the home, washing clothes and food consumption, with
     recommendations.
   - Also examined: being environmentally aware when shopping for food (2016O); environmentally
     responsible choice, use and disposal of appliances (2025H, 2024H, 2014H).

SimpleStudy: Consumer Responsibility to the Environment. Energy efficiency, fuels and emissions
in the home are Elective 1 content in `hom-home-services`.

### hom-appliances-equipment — Household Appliances and Equipment [2.1.5]
1. **Household technology and home management** [2.1.5]: technological developments available to
   the household and their contribution to managing the home.
   Also examined: 2018H, 2018O, 2010O.
2. **Selecting a large and a small household appliance** [2.1.5]: consumer considerations —
   selection criteria, obtaining consumer information, design, efficiency.
   - Settings: individual studies of one large and one small appliance.
   - Also examined: energy labelling (2026O, 2022O, 2018H, 2012H); refrigerator star rating
     (2007H); quality and safety marks (2011H, 2008O); sources of consumer information (2017O,
     2009O).
3. **An appliance with a motor** [2.1.5]: guidelines for use, and **[HL]** underlying working
   principles.
   Also examined: 2024H, 2009O.
4. **An appliance with a heating element** [2.1.5]: guidelines for use, and **[HL]** underlying
   working principles.
   Also examined: 2022H, 2004H.
5. **A refrigeration appliance** [2.1.5]: guidelines for use, and **[HL]** underlying working
   principles.
   Also examined: functions of the compressor, condenser, evaporator, refrigerant and
   thermostat (2024H, 2021H, 2015H, 2013H, 2005H); a full study (2025H, 2018H).
6. **A microwave oven** [2.1.5]: guidelines for use, and **[HL]** underlying working principles.
   Also examined: magnetron, transformer, wave guide and turntable (2026H, 2019H, 2014O, 2008H);
   a full study (2026O, 2014H, 2005H).

SimpleStudy: Household Technology.

---

## Core Area 3 — Social Studies (10%)

### hom-sociological-concepts — Sociological Terms and Concepts [3.1.1]
These concepts are integrated throughout the social studies sections.
1. **Society, culture, norms and mores, values** [3.1.1].
2. **Role, status, socio-economic groupings, social mobility** [3.1.1].
3. **Primary and secondary social groups, kinship, socialisation** [3.1.1].
   Also examined: monogamy (2023H).
4. **Social institutions** [3.1.1].
5. **Social change** [3.1.1].

Also examined across the chapter: explaining sets of terms (2019H, 2013H). SimpleStudy:
Sociological Terms and Concepts.

### hom-family-society — The Family in Society [3.1.2, 3.1.3, 3.1.4]
1. **Defining the family** [3.1.2]: the universality of the concept of family; definitions of
   "the family".
   - Settings: case studies of family situations in other societies, e.g. extracts from
     literature or films; group definitions of the family.
   - Also examined: 2021H, 2011H, 2023H.
2. **The historical development of the Irish family** [3.1.3] **[HL]**: from the beginning of
   the twentieth century to the present day.
   Also examined: 2025H, 2023H, 2014H.
3. **Modern family structures** [3.1.3]: characteristics of lone-parent, nuclear, extended and
   blended families.
   Settings: comparing Irish families with families in other European countries by structure,
   size and roles.
4. **Changes affecting family structures** [3.1.3] **[HL]**: social, economic and technological
   changes affecting modern family structures.
   Also examined: 2024H, 2019H, 2016H.
5. **Family functions** [3.1.4]: physical, economic, emotional, educational and social
   functions; how these functions may be adopted or supplemented by other social institutions.
   - Settings: brainstorming all the functions a family carries out and classifying them into
     the five categories.
   - Also examined: how the State supports the family in each function (2025H, 2024O, 2014H,
     2010H).

SimpleStudy: The Family in Society.

### hom-family-caring — The Family as a Caring Unit [3.1.6]
1. **Roles and responsibilities in the family** [3.1.6]: roles and responsibilities of family
   members and how they change through the family life cycle; gender issues in family roles;
   **[HL]** social and economic factors that have changed the roles of family members in recent
   times; **[HL]** role conflict.
   - Settings: case studies or interviews with older people on how family roles have changed in
     the last fifty to one hundred years.
   - Also examined: roles of adolescents (2021O, 2007O); parenting roles (2005H).
2. **Child–parent relationships** [3.1.6]: physical and psychological needs of young children
   and adolescents and how the family meets them; the rights of children within the family;
   conflict between adolescents and adults and how it can be dealt with; the importance of good
   communication within the family.
   - Settings: role-play on communication and avoiding or dealing with conflict.
   - Also examined: 2024H, 2018H, 2016H, 2012H, 2010O.
3. **Older people in the family** [3.1.6]: the importance of independence for the older person;
   generation conflict and how to deal with it.
   - Settings: investigating accommodation options for older family members, with advantages
     and disadvantages; role-play and case studies on generation conflict.
   - Also examined: supports for older people (2024H, 2013O); roles of grandparents (2025H,
     2018O, 2014H).
4. **Family members with special needs** [3.1.6] **[HL]**: the response of the family unit to a
   member with special physical, mental or emotional needs, to include statutory and voluntary
   services available.
   - Settings: a short investigative study of how a family might respond.
   - Also examined: challenges for the family (2026H, 2021H, 2016H, 2007H); named voluntary
     organisations, e.g. the Rehab Group (2026H, 2007H).

SimpleStudy: The Family as a Caring Unit.

### hom-marriage — Marriage [3.1.5]
1. **Definition of marriage** [3.1.5].
   Also examined: marriage in Irish law and its legal requirements and conditions for validity
   (2024O, 2022H, 2015H, 2014O, 2005O).
2. **Cultural variations and the marriage relationship** [3.1.5]: outline knowledge of cultural
   variations in marital arrangements, commitment, customs, legal obligation, and rights and
   responsibilities within marriage.
   Settings: case studies, photographs, media or literature extracts on cultural variations.
3. **Preparing for marriage** [3.1.5]: facilities and services available to those preparing for
   marriage.
   Also examined: pre-marriage courses (2025O, 2017H, 2014O, 2009H).
4. **When a marriage breaks down** [3.1.5]: marriage counselling, family mediation, legal
   separation, legal nullity, divorce.
   Also examined: conditions for divorce under the Family Law (Divorce) Act 1996, as amended by
   the Family Law Act 2019 (2015H, 2006H).

SimpleStudy: Marriage.

### hom-family-law — Family Law [3.1.7]
Protection available for families under current Irish family law. Refer to these Acts wherever
appropriate in the social studies sections.
1. **The Family Law (Maintenance of Spouses and Children) Act 1976** [3.1.7].
   Also examined: 2018H, 2012O.
2. **The Family Home Protection Act 1976** [3.1.7].
   Also examined: 2004H.
3. **Barring orders under the Domestic Violence Act 2018** [3.1.7] **[HL]**.
4. **The Judicial Separation and Family Law Reform Act 1989** [3.1.7] **[HL]**.
5. **The Child Care Act 1991** [3.1.7] **[HL]**.
   Also examined: protection for children under current family law (2013H, 2012H).
6. **Making a will** [3.1.7]: the importance of, and outline procedure for, making a will under
   the Succession Act 1965.
   Also examined: 2026H, 2022H, 2017O, 2011O, 2010H.

SimpleStudy: Family Law.

---

## Elective 1 — Home Design and Management (20%)

Assessed by the written examination only. Elective 1 is split across three chapters: `hom-housing`
(housing styles, provision, location, planning and design), `hom-home-interior` and
`hom-home-services`. `hom-housing` also holds the core housing content [2.1.3, 2.1.4].

### hom-housing — Housing and Accommodation [2.1.3, 2.1.4, 4.1, 4.2]
1. **Housing choices** [2.1.4, core]: factors that determine individual and family housing
   choices — socio-economic factors, national housing policy (the current national plan is
   *Delivering Homes, Building Communities 2025–2030*), trends in housing development,
   availability.
   - Also examined: features of national housing policy (2024H, 2014H, 2008H); buying vs renting
     (2021O, 2018O, 2014H); private rented sector (2014H).
   - SimpleStudy: Housing.
2. **Housing finance** [2.1.3, core] **[HL]**: factors determining requirements, sources and
   conditions attaching; mortgage protection.
   - Settings: investigating types of home finance, comparing costs and conditions.
   - Also examined: conditions for mortgage approval (2025H, 2022H, 2017H, 2011H); types of
     mortgage and interest rates (2023H, 2017H, 2007H, 2004H).
   - SimpleStudy: Housing.
3. **Housing styles** [4.1.1, Elective 1]: **[HL]** outline of the historical development of
   housing styles in Ireland from the nineteenth century; popular housing styles in Ireland
   today; social, cultural, economic and environmental factors influencing the choice of housing
   style.
   Settings: a school visit to houses from different periods; photographs of house styles as
   stimulus for discussing suitability to their surroundings.
4. **Housing provision** [4.1.2, Elective 1]: the housing requirements of families, single
   people, older people, people with disabilities and homeless people; evaluation of housing
   provision in Ireland today — **[HL]** distribution of housing (rented or owner-occupied,
   private or social, urban or rural), quality of accommodation, comparative costs of buying and
   renting, **[HL]** adequacy of provision to meet varying requirements; social housing
   provision (local authority, voluntary and co-operative housing); provision of local amenities
   and services (schools, shops, community centres, transport, play areas, street lighting,
   refuse collection).
   Settings: a group housing study of a local area (townland, village, housing estate).
5. **Location, planning and professional services** [4.2, Elective 1]: factors that influence
   the choice of location and house style; the procedure for obtaining planning permission from
   the local authority under the Planning and Development Act 2024, with appeals to An
   Coimisiún Pleanála; professional services — architects, engineers, surveyors, solicitors,
   builders, books of house plans.
   - Settings: a case study of a person or family with particular needs, used for the location,
     house design, interior and services tasks that follow (see `hom-home-interior` and
     `hom-home-services`).
   - Also examined: outline and full planning permission (2024O, 2021H, 2016H, 2012O).
6. **House design and building standards** [4.2, Elective 1]: factors that influence house
   design — aesthetic and environmental factors, present and future family requirements, energy
   efficiency, ergonomics, initial and maintenance costs, technological developments; **[HL]**
   regulation of house-building standards — the Building Regulations and building control
   (certificates of compliance required under the Building Control (Amendment) Regulations
   2014), structural defects warranties such as HomeBond's, and grant provision such as SEAI
   home energy grants.
   Also examined: the BER certificate (2017H); legislation regulating building standards (2011H);
   evaluating a house plan for a stated family (2026O, 2017H, 2015O).

### hom-home-interior — Designing the House Interior [4.3]
Elective 1. Builds on the case-study house in `hom-housing`.
1. **Elements and principles of design and factors in interior design** [4.3]: the elements and
   principles of design and their application to the home; factors that influence the interior
   design of the home — aesthetic and comfort factors, ergonomics, family size and
   circumstances, special needs, cost, environmental awareness.
   - Settings: evaluating rooms from photographs or magazines against the elements and
     principles of design and other criteria; designing one room for the case study.
   - Also examined: design principles applied to a room (2024H, 2010H, 2005H); colour, pattern
     and texture (2025O, 2022H, 2017O, 2010O, 2007O); factors in kitchen or room design (2025H,
     2024H, 2023H, 2015H); evaluating a room or layout (2023O, 2022O, 2016O).
2. **Floors, walls, furniture and soft furnishings** [4.3]: selection, properties and uses of
   flooring and floor coverings, wall finishes, furniture and soft furnishings.
   - Settings: recommendations for the floor coverings, wall finishes, furniture and soft
     furnishings of one room.
   - Also examined: floor coverings (2022H, 2018H, 2016O, 2013H, 2007H); wall finishes (2026O,
     2019H, 2014H, 2013O, 2008H, 2006O); furniture (2018O, 2016H, 2015O, 2009H); soft furnishings
     (2021O, 2017O, 2010H, 2008O).
3. **Materials used in the home** [4.3] **[HL]**: criteria for selection, properties and uses of
   wood, metal, glass, plastics and fabric.
   Also examined: thermoplastic and thermosetting plastics (2015H, 2005H); one solid wood (2009H).

SimpleStudy: none.

### hom-home-services — The Energy-Efficient Home, Systems and Services [4.4, 4.5]
Elective 1. Builds on the case-study house in `hom-housing`.
1. **Energy supplies to the home** [4.4]: electricity, gas, oil, solid fuels and solar energy;
   their sources and the sustainability of these sources.
   Also examined: one renewable or non-renewable source in detail (2026H, 2022H, 2014H, 2011H,
   2007H).
2. **Emissions, energy inefficiency and energy efficiency** [4.4]: **[HL]** emissions produced by
   burning fuels in the home and their effects on the environment; identifying potential energy
   inefficiencies in the home; strategies to improve energy efficiency and reduce emissions.
   - Settings: a small investigative study of energy inefficiency in the home (heat loss, how hot
     water is heated, inefficient use of fuels, cooking practices); recommendations for an
     energy-efficient house design.
   - Also examined: 2024H, 2023H, 2018H, 2017H, 2008H, 2004H.
3. **Electricity** [4.5.1]: household electricity supply and **[HL]** the structure of the ring
   circuit; voltage, wattage, amperage, kilowatt-hour, tariffs and costings; safety in the use
   of electricity — fuses, circuit breakers, earth.
   - Settings: recommendations for heating, lighting and ventilation for one room of the
     case-study house.
   - Also examined: miniature circuit breakers and the earth wire (2024H, 2022O, 2019H, 2015H);
     charges on an electricity bill (2015H, 2008O); safe use of electricity and gas (2023O,
     2019H, 2008O).
4. **Water** [4.5.2]: cold water supply and storage in the house.
   Also examined: parts of the cold water system (2025H, 2023O, 2015O); public water treatment
   (2024O, 2018O, 2010H); preventing freezing (2024O, 2004O); water conservation (2025H, 2021H,
   2015O).
5. **Heating** [4.5.3]: levels of thermal comfort and their control, including the principle and
   uses of thermostats; heating options and factors in choosing a heating system; the
   scientific principles of one system of domestic central heating and their application.
   Also examined: 2026H, 2026O, 2023H, 2019O, 2016H, 2012H, 2008H, 2006H.
6. **Insulation** [4.5.4]: underlying principles and methods of insulation.
   - Settings: evaluating the insulation in the student's own home and recommending improvements.
   - Also examined: 2025O, 2024H, 2022H, 2021O, 2009H, 2005H.
7. **Ventilation** [4.5.5]: underlying principles and their application; natural and artificial
   methods.
   - Settings: evaluating ventilation in the home economics room or a room at home.
   - Also examined: 2025H, 2024O, 2022H, 2017H, 2012H, 2004H; condensation (2015H).
8. **Lighting** [4.5.6]: **[HL]** properties of light and their application; principles for
   planning lighting systems; outline of contemporary lighting developments; underlying
   principles and uses of energy-efficient lighting.
   - Settings: investigating contemporary lighting through magazines, brochures and shop visits.
   - Also examined: 2025H, 2023H, 2022O, 2021H, 2013H, 2011H, 2006H.

SimpleStudy: none.

---

## Elective 2 — Textiles, Fashion and Design (20%)

Assessed by practical coursework (the garment) and the written examination. Household textiles
[2.1.6] are core content for all students.

### hom-textiles-fibres — Textiles and Fabric Properties [2.1.6, 5.2]
1. **Textiles as a household resource** [2.1.6, core]: the use of textiles as a resource for
   household and clothing purposes; selection criteria — fitness for purpose and suitability in
   use determined by fabric properties, cost, personal choice, aesthetic appeal.
   - Also examined: functions and uses of household textiles (2025O, 2023O, 2009O); fabric
     properties such as absorbent, flammable, crease-resistant, colourfast (2026O, 2007O).
   - SimpleStudy: Textiles Overview.
2. **Safety in household textiles** [2.1.6, core]: safety considerations in selecting household
   textiles; the identification and effects of one fire-retardant finish; **[HL]** the fire
   safety requirements for domestic upholstered furniture, which from July 2026 are those of the
   EU General Product Safety Regulation (Regulation (EU) 2023/988).
   Also examined: properties of fabric for upholstered furniture (2016H, 2004H); fire-retardant
   finishes (2018H, 2014H, 2011O, 2009O, 2006H).
3. **Fibre classification** [5.2, Elective 2]: classification, sources and uses of natural,
   regenerated and synthetic fibres.
   Also examined: regenerated vs synthetic (2022H, 2016H, 2008H).
4. **Fabric profiles** [5.2, Elective 2]: profiles of one fabric made from natural fibres, one
   made from manufactured fibres and **[HL]** one blend, to include fibre production and
   properties, identification by burning tests and microscopic evaluation, yarn production, and
   **[HL]** yarn or filament modification.
   - Settings: observing and feeling fabrics; investigating fabrics for fibre origin, yarn
     production, construction and design application.
   - Also examined: a fabric profile in almost every Elective 2 question (2026H, 2024H, 2023H,
     2021H, 2017H); filament modification (2022H, 2008H).
5. **Fabric construction, finishes, colour, design and testing** [5.2, Elective 2]: fabric
   construction techniques (two; **[HL]** three); finishes (two; **[HL]** three); colour
   application (two methods); design application (two methods); **[HL]** fabric performance
   testing (two tests).
   - Settings: simple scientific tests on fabrics for performance characteristics.
   - Also examined: knitted fabric (2019H, 2009H, 2005H); functional finishes (2014H, 2011O);
     colour and design application (2026O, 2016H); performance tests (2025H, 2008H).

### hom-clothing-selection — Clothing Selection and Care [2.1.6, 5.1, 5.3, 5.4]
1. **Textile care** [2.1.6, core]: the basic scientific principles underlying the care of
   fabrics relative to their general properties.
   - Settings: simple scientific tests comparing shrinkage, water-repellence and crease recovery
     of a variety of fabrics.
   - Also examined: fabric care symbols (Ordinary Level Section A most years: 2025O, 2023O,
     2022O, 2021O); detergent components — surfactants, enzymes, fluorescents (2013H).
2. **Influences on clothing** [5.1]: **[HL]** social, economic and industrial influences on the
   design and construction of clothing; factors that influence clothing requirements — function,
   cost versus money available, availability, new fibres, the media, trendsetters, fashion,
   social and cultural influences.
   - Settings: family photographs and magazine pictures from different decades showing the
     "look" of the time; comparing past fashion trends with recent ones.
   - Also examined: 2026H, 2024H, 2021H, 2019H, 2018H, 2009H.
3. **Current fashion trends** [5.1]: critical evaluation of current fashion trends (male and
   female) with reference to colour, shape, line, proportion, pattern, texture, influences,
   accessories and other factors.
   - Settings: magazine pictures and videos as stimulus for discussion.
   - Also examined: athleisure, vintage and pre-loved clothing, social media and trendsetters
     (2026O, 2023H, 2022O, 2021H, 2017H); accessories (2016H, 2006H); a sketched outfit
     reflecting a current trend (most Elective 2 questions).
4. **Elements and principles of design in clothing** [5.1, 5.3]: the elements and principles of
   design; their application to garment construction and evaluation; evaluating garments or
   outfits for the relationship between design and function, comfort and aesthetic appeal.
   - Settings: evaluating garments or pictures of garments against the elements and principles.
   - Also examined: using colour and design to flatter body size and shape (2022H, 2014H).
5. **The design process and garment construction** [5.3]: knowledge and application of the
   design process to construct a garment using a range of prescribed processes (commercial
   patterns may be used); selection and **[HL]** modification of a commercial pattern to meet a
   specific need; the Elective 2 coursework garment (100 marks, 10%; for 2027 one mandatory
   process from a choice of three set by the SEC).
   - Settings: a fashion sketch of a garment or outfit for a specific brief; testing fabrics for
     suitability (absorbency, shrinkage, water-repellence, crease recovery).
   - Also examined: steps of the design process (2021H); pattern modification (2022H, 2018H,
     2008H); pattern selection and envelope information (2025O, 2019O, 2009O).
6. **The clothing and textile industries in Ireland** [5.4]: an overview of the structure of the
   industries; the role of small businesses and cottage industries; career opportunities in
   clothing, textiles and related industries.
   - Settings: a visit to a factory or craft worker.
   - Also examined: Irish fashion designers (2024H, 2019H, 2016H, 2014H); challenges facing the
     industry (2014H, 2018O, 2007H); traditional crafts (2022H, 2013H).

SimpleStudy: Textiles Overview (subsection 1); no topics for subsections 2–6.

---

## Elective 3 — Social Studies (20%)

Assessed by the written examination only. A study of social issues that relate to the family.

### hom-social-change — Social Change and the Family [6.1]
The impact of social and economic change on family life, to include:
1. **Changes in settlement patterns from rural to urban** [6.1].
   Also examined: 2022O, 2018O, 2009O; initiatives to keep population in rural areas (2012O,
   2006H).
2. **Working hours, leisure time and conditions of work** [6.1]: reduction in working hours and
   increase in leisure time; improved pay and conditions of work.
3. **Education and social welfare** [6.1]: improvements in the provision of education and social
   welfare.
   Also examined: 2025H, 2021H, 2004O.
4. **Changing attitudes** [6.1]: to marriage, parenting and traditional roles within the family.
5. **Women in the workforce and equality legislation** [6.1]: increased participation of women in
   the workforce; legislation on equal pay and employment opportunities.
6. **Unemployment** [6.1]: the impact of unemployment on family life.

- Settings: comparing family life a hundred years ago with today (roles, leisure time, who
  attended school, number of children); interviewing an older relative or community member.
- Also examined across the chapter: 2026H, 2026O, 2023H, 2023O, 2014H, 2011H.

SimpleStudy: none.

### hom-education — Education [6.2]
1. **The purpose of education** [6.2]: as a method of socialisation; in the physical, emotional,
   moral and intellectual development of the individual; as a preparation for work.
2. **Factors that influence educational achievement** [6.2].
3. **The provision of education in Ireland** [6.2]: pre-school, primary, second-level,
   third-level, adult and second-chance education, and **[HL]** special needs education.
   Also examined: pre-school initiatives (2026H, 2013O); work experience (2021O, 2011O); supports
   for special educational needs (2024H, 2009H, 2005H).
4. **Equality of opportunity in education** [6.2] **[HL]**: with reference to gender inequity,
   socio-economic status, disadvantaged students and early school leavers.
5. **Contemporary initiatives to improve access to education** [6.2] **[HL]**.
   Also examined: named initiatives (2022H, 2015H, 2014H, 2011H, 2008H, 2006H, 2004H).

SimpleStudy: none.

### hom-work-leisure — Work and Leisure [6.3, 6.4]
1. **Concepts of work and attitudes to work** [6.3.1]: defining work — paid employment, unpaid
   work in the home and home-related activities, voluntary work; attitudes to work and work
   attainment — extrinsic and intrinsic satisfaction, work ethic, variations according to
   occupation.
   Settings: case studies of job descriptions, judging the worker's satisfaction and how it
   could be improved.
2. **Changes in patterns of work** [6.3.1] **[HL]**: the effect of developing technology on
   industry; the decline in primary and secondary industries and growth in services; increased
   educational requirements; increased participation by women; improved working conditions;
   increasing flexibility in working hours, e.g. job-sharing, flexible hours, parental leave.
   Settings: investigating Ireland's current occupational structure compared with fifty years
   ago.
3. **Unpaid and voluntary work** [6.3.1]: the role of unpaid and voluntary work in the community
   and the benefits to the volunteer and the community.
   Also examined: 2026H, 2021H, 2018H, 2014H, 2005H.
4. **The Protection of Young Persons (Employment) Act (1996)** [6.3.1]: brief outline.
   Also examined: other legislation protecting people in employment (2026O, 2019H, 2011H).
5. **Reconciling employment with family responsibilities** [6.3.2]: changing patterns in sex
   roles in the family; the impact of dual-earner families on family life — role overload, role
   conflict, distribution of parental and home-care responsibilities.
   Settings: a class survey and questionnaire on male and female roles in twenty home tasks.
6. **Child care** [6.3.2]: family requirements for child care and the options available; **[HL]**
   evaluation of two types of child care option.
   Settings: investigating the child care options in the area.
7. **Leisure** [6.4]: defining leisure and its function and value in today's society; influences
   on leisure patterns — social and cultural influences, occupation, age, gender; the role of
   individual and family leisure in physical, social and emotional development.
   Settings: students list and cost their leisure pursuits and their benefits; case studies of
   families at different stages of the life cycle; a time-use breakdown for each day.
8. **Evaluating leisure facilities** [6.4] **[HL]**: evaluation of the leisure facilities in the
   community, to include a cost and value comparison of two facilities.

SimpleStudy: none.

### hom-unemployment-poverty — Unemployment, Poverty, and Social Responses [6.5, 6.6, 6.7]
1. **Defining unemployment** [6.5]: defining unemployment, and **[HL]** knowledge of the extent of
   unemployment in Ireland.
2. **Causes of unemployment** [6.5] **[HL]**: seasonal, geographical, technical, difficulty in
   adapting to the changing requirements of industry, level of demand for products and
   services, residual.
   Also examined: groups who find it hard to get work (2024H, 2007H).
3. **Effects of unemployment** [6.5]: on the individual, the family unit and society.
4. **Concepts of poverty** [6.6.1]: defining poverty, to include absolute and relative poverty and
   the poverty line; the extent and distribution of poverty in Ireland today and the groups at
   risk of poverty.
   - Settings: photographs as stimuli for discussing the relative nature of poverty.
   - Also examined: consistent poverty and the at-risk-of-poverty rate (2011O).
5. **Causes and effects of poverty** [6.6.2]: reasons why poverty continues to be a feature of
   modern western society, to include **[HL]** the cycle of poverty, **[HL]** the influence of
   social policy on poverty, **[HL]** the cycle of deprivation in families and geographical
   areas, and **[HL]** the poverty trap; the effects of poverty.
   Also examined: effects of poverty on families and children (2025O, 2004O).
6. **Statutory responses** [6.7]: social welfare assistance and benefits; **[HL]** initiatives
   encouraging foreign investment; schemes to reduce expenditure for low-income families.
   - Settings: small groups investigate one statutory service and present a synopsis.
   - Also examined: statutory initiatives to create employment (2026H, 2022H, 2015H, 2012H,
     2009H); schemes for low-income families (2023H, 2017H, 2008H).
7. **Community responses** [6.7]: the work of voluntary organisations; community-based
   education, training and employment initiatives; the emergence of co-operatives and cottage
   industries.
   - Settings: investigating one local initiative or group that has responded to community need.
   - Also examined: named national voluntary organisations working on poverty (2022O, 2016H,
     2010H); the Combat Poverty Agency (2007O).

SimpleStudy: none.

---

## Appendix A — Where the syllabus differs from SimpleStudy and from the repo's earlier assumptions

- **The syllabus examined in June 2027 is the 2001 Scientific and Social syllabus, first examined
  2004.** The repo already pointed at the right document (`spec-syllabus.pdf` is byte-identical
  to the curriculumonline.ie PDF), but `pipeline/config.py` marked the 2004 cutoff as an
  unverified estimate and the manifest gave no effective date. Both are now confirmed.
- **Higher Level-only content is printed in black.** Plain-text copies of the syllabus lose this,
  which is why earlier content did not mark HL items. The markings in this outline were read from
  the PDF's print colour (Appendix C lists every one). Notable HL-only items: essential amino
  acids, peptides and the peptide bond; caramelisation, crystallisation, dextrinisation and
  inversion; cis/trans fatty acids, triglyceride structure, plasticity, rancidity and
  hydrogenation; moulds, yeasts and the food poisoning bacteria; fermentation and irradiation;
  HACCP; the vegan, coeliac and diabetic diets; sensory analysis; inputs, throughputs and
  outputs; housing finance; working principles of appliances; the purchasing process; three of
  the five family law Acts.
- **In the syllabus but missing from SimpleStudy** (no topic at all): carbohydrate and lipid
  chemistry [1.1.3, 1.1.4]; digestion and absorption [1.1.2–1.1.4]; water [1.1.7]; dietary
  guidelines and food composition tables [1.2.2]; the Irish food industry [1.3.1]; physical and
  chemical changes in cooking, soups, sauces and pastry [1.3.4]; profiles of processed food,
  packaging and contaminants [1.3.5]; food legislation [1.3.7]; preservation methods in detail
  [1.3.9]; national food safety agencies [1.3.10]; the working principles of appliances
  [2.1.5]; textile care, fire-retardant finishes and furniture fire safety [2.1.6]; all of
  Elective 1 except housing choices and finance [4.1–4.5]; all of Elective 2 except a textiles
  overview [5.1–5.4]; and all of Elective 3 [6.1–6.7].
- **In SimpleStudy but not named in the syllabus:** none of substance; "Food Commodities and
  Extras" and "Diet and Health" are broader groupings of syllabus content.
- **Beyond the syllabus wording but examined by the SEC:** listed under "Also examined" in each
  subsection. Main themes: current legislation and renamed bodies; income deductions (PAYE,
  PRSI, USC, tax credits); welfare payments and pensions; MABS; novel protein foods; functional,
  GM, organic and ultra-processed foods; Bord Bia quality assurance; national housing policy and
  the BER certificate; online shopping; current fashion trends.
- **Legislation and bodies updated to June 2027.** The syllabus (2001) names Acts and bodies that
  have since been replaced, revoked or renamed. The outline uses only the current ones:

  | Syllabus names | Used for June 2027 |
  |---|---|
  | Food Hygiene Regulations (1950–1989) [1.3.7] | Regulation (EC) No 852/2004, given effect by the European Communities (Hygiene of Foodstuffs) Regulations 2006 (amended 2009, 2010) |
  | Labelling Regulations (1982, 1991) [1.3.7, HL] | Regulation (EU) No 1169/2011, given effect by the European Union (Provision of Food Information to Consumers) Regulations 2014 |
  | Sale of Food and Drugs Acts (1875–1936) [1.3.7, HL] | Food Safety Authority of Ireland Act 1998 and Regulation (EC) No 178/2002 (general food law) |
  | Health (Official Control of Foodstuffs) Regulations (1991) [1.3.7, HL] | Regulation (EU) 2017/625, given effect by the European Union (Official Controls in Relation to Food Legislation) Regulations 2020 |
  | EU control of additives [1.3.6] | Regulation (EC) No 1333/2008 on food additives |
  | Department of Agriculture, Food and Rural Development; Department of Health and Children; Regional Health Boards; Food Safety Authority; Director of Consumer Affairs [1.3.10, HL] | FSAI; Department of Health; the official agencies under FSAI service contracts — HSE (Environmental Health Service, Public Analyst Laboratories), Department of Agriculture, Food and the Marine, Sea-Fisheries Protection Authority, local authorities |
  | Hire Purchase Acts (1946, 1960) [2.1.3] | Consumer Credit Act 1995 (as amended), which governs hire-purchase agreements |
  | Sale of Goods and Supply of Services Act (1980); Consumer Information Act (1978) [2.2.3] | Consumer Rights Act 2022; Consumer Protection Act 2007 (CCPC) |
  | Fire Safety (Domestic Furniture) Order (1988) [2.1.6, HL] | revoked July 2026 (S.I. 357/2026); EU General Product Safety Regulation (EU) 2023/988 |
  | Family Law Act (1976) s.22 barring orders [3.1.7, HL] | Domestic Violence Act 2018 |
  | Judicial Separation Act (1989) [3.1.7, HL] | Judicial Separation and Family Law Reform Act 1989 (as amended) |
  | Divorce (examined) | Family Law (Divorce) Act 1996, as amended by the Family Law Act 2019 |
  | Planning permission or bye-law approval [4.2] | planning permission under the Planning and Development Act 2024; appeals to An Coimisiún Pleanála (replaced An Bord Pleanála, June 2025) |
  | National house building guarantee scheme, certificates, grants [4.2, HL] | Building Regulations and building control certificates (Building Control (Amendment) Regulations 2014); structural defects warranties such as HomeBond's; SEAI grants |
  | National housing policy [2.1.4] | *Delivering Homes, Building Communities 2025–2030* |

  The Family Law (Maintenance of Spouses and Children) Act 1976, the Family Home Protection Act
  1976, the Child Care Act 1991, the Consumer Credit Act 1995 and the Protection of Young Persons
  (Employment) Act 1996 remain in force (as amended) and keep their syllabus names. SEC papers up
  to 2026 sometimes still named a superseded Act (e.g. the Sale of Goods and Supply of Services
  Act 1980 in 2026); the outline follows the current law.
- **Wrong-course content removed from the app** (Junior Cycle household-skills topics with no
  basis in this syllabus and never examined at Leaving Cert in 2004–2026): ten flashcards — in
  `hom-clothing-selection`: Wash-load preparation, Stain-removal principles, Protein stains,
  Grease stains, Tannin stains, Clothing storage, Garment repair; in `hom-housing`: Functions of
  the home, Home safety measures, Home security measures. The `hom-clothing-selection`,
  `hom-family-law` and `hom-sociological-concepts` chapter overviews in
  `generated-notes-content.js` were reworded to the syllabus.
- **Kept, although not named in the syllabus,** because they apply a syllabus item or SEC papers
  examine them: care symbols and detergents [2.1.6 textile care]; ultra-processed food [1.3.5];
  BMI, food pyramid and life-stage nutrition [1.2.2, 1.2.3]; allergies and intolerances [1.2.3
  health status]; waste, recycling and pollution cards [2.2.2]; tenancy and BER cards [2.1.4,
  4.1.2, 4.2]; fast fashion and sustainable clothing [2.2.2 washing clothes, 5.1].
- **Exam-bank tagging caution:** `home-economics-exam-questions.js` tags each multi-part question
  by its first part, so some chapters carry off-topic parts (for example `hom-dairy-eggs` holds
  parts on saving schemes and marriage; `hom-meat-preparation` holds mortgage parts), and no
  question is yet tagged to the five new chapters. The bank is due to be regenerated and
  re-tagged against these 36 chapters. Until then, package writers should take a chapter's past
  questions by topic, using the "Also examined" years in this outline, not by `chapterId` alone.

## Appendix B — Where syllabus content without an obvious chapter was placed

Five chapters were added on 2026-11-05 for content that had no natural home: `hom-food-industry`
[1.3.1], `hom-fruit-vegetables` [1.3.2], `hom-resource-management` [2.1–2.1.2],
`hom-home-interior` [4.3] and `hom-home-services` [4.4–4.5]. The remaining placements are:

| Syllabus content | Placed in |
|---|---|
| Food choices [1.1.1] | `hom-meal-planning` s1 |
| Water [1.1.7] | `hom-energy-nutrition` s6 |
| Alternatives to meat [1.3.2] | `hom-proteins` s9 |
| Fats and oils as a commodity [1.3.2] | `hom-lipids` s6 |
| Pastry [1.3.4] | `hom-cereals-grains` s5 |
| Sensory analysis and evaluation [1.3.4] | `hom-food-additives` s6 |
| Food legislation [1.3.7] | `hom-food-safety` s9 |
| Food Studies coursework | `hom-cooking-methods` s7 |
| Housing choices and housing finance [2.1.3, 2.1.4] (core) | `hom-housing` s1–s2 |
| Household textile care [2.1.6] (core) | `hom-clothing-selection` s1 |
| Household textiles and safety [2.1.6] (core) | `hom-textiles-fibres` s1–s2 |

## Appendix C — Higher Level-only content (black print in the syllabus), complete list

Read from the print colour of the official PDF (2026-11-05). Everything else is common to both
levels.

- **[1.1.2] Protein:** essential amino acids, peptides, peptide bond, hydrolysis; secondary and
  tertiary structure; fibrous and globular (animal) and glutelins and prolamines (plant);
  myosin, actin and collagen; foam formation and gel formation; deamination; outline of the
  utilisation of amino acids.
- **[1.1.3] Carbohydrates:** basic structure of a monosaccharide; formation of disaccharides and
  polysaccharides; hydrolysis to include inversion, crystallisation, caramelisation,
  dextrinisation, pectin extraction and gel formation; outline of the utilisation of glucose.
- **[1.1.4] Lipids:** cis and trans fatty acids; structure of saturated, monounsaturated and
  polyunsaturated fatty acids; chemical composition and molecular structure of a triglyceride;
  distribution of the fatty acid types in food; identification and function of emulsifying
  agents and stabilisers; plasticity, rancidity and hydrogenation; identification and functions
  of antioxidants; outline of the utilisation of triglycerides.
- **[1.1.5] Vitamins:** properties of all the named vitamins (fat-soluble, C, B12, folate and the
  B group).
- **[1.1.6] Minerals:** trace mineral elements; zinc, iodine, potassium and sodium; the effects of
  phytates and oxalates on calcium absorption.
- **[1.2.3]** The vegan, coeliac and diabetic modified diets.
- **[1.3.4]** Sensory analysis.
- **[1.3.6]** Physical conditioning agents.
- **[1.3.7]** Food labelling law, the general framework of food law and official controls (the
  current instruments are in `hom-food-safety` s9 and Appendix A).
- **[1.3.8]** Micro-organisms that cause spoilage and foodborne disease (moulds, yeasts and three
  food poisoning bacteria, with all listed details); the principles underlying the control of
  enzymic spoilage.
- **[1.3.9]** Fermentation and irradiation; comparative evaluation of foods preserved by
  different methods.
- **[1.3.10]** HACCP and ISO 9000; the named national agencies.
- **[2.1.1]** Inputs, throughputs and outputs.
- **[2.1.3]** Housing finance.
- **[2.1.5]** Underlying working principles of the four appliances.
- **[2.1.6]** Fire safety requirements for domestic upholstered furniture (now the EU General
  Product Safety Regulation).
- **[2.2.1]** The purchasing process.
- **[3.1.3]** The historical development of the Irish family; social, economic and technological
  changes affecting family structures.
- **[3.1.6]** Social and economic factors affecting changing roles; role conflict; the family's
  response to special needs.
- **[3.1.7]** Barring orders (Domestic Violence Act 2018); the Judicial Separation and Family Law
  Reform Act 1989; the Child Care Act 1991.
- **[4.1.1]** Historical development of housing styles. **[4.1.2]** Distribution of housing;
  adequacy of housing provision. **[4.2]** Regulation of house-building standards (building
  control certificates, structural warranties, grants). **[4.3]** Materials: wood, metal, glass, plastics, fabric.
  **[4.4]** Emissions from burning fuels. **[4.5.1]** Structure of the ring circuit. **[4.5.6]**
  Properties of light.
- **[5.1]** Social, economic and industrial influences on clothing. **[5.2]** One blend; yarn or
  filament modification; the third construction technique and third finish; fabric performance
  testing. **[5.3]** Modification of a commercial pattern.
- **[6.2]** Special needs education; equality of opportunity; contemporary access initiatives.
  **[6.3.1]** Changes in patterns of work. **[6.3.2]** Evaluation of two child care options.
  **[6.4]** Evaluation of leisure facilities. **[6.5]** Extent of unemployment; causes of
  unemployment. **[6.6.2]** Cycle of poverty, social policy, cycle of deprivation, poverty trap.
  **[6.7]** Initiatives encouraging foreign investment.

## Appendix D — SimpleStudy structure as recorded (2026-08-07)

For reference only. Names are exactly as the guide records them.

1. The Family — Sociological Terms and Concepts; The Family in Society; The Family as a Caring
   Unit
2. Marriage and Family Law — Marriage; Family Law
3. Household Finances — Housing; Budgeting; Insurance; Management of Household Financial
   Resources; Payment Options and Credit; Resource Management; Savings
4. Consumer Studies — Role of Advertising; Household Income and Spending Patterns; Consumer
   Choice; Consumer Research; Consumer Rights and Responsibilities; Consumer Protection; Consumer
   Responsibility to the Environment
5. Nutrition — Protein — Alternative Protein Foods
6. Nutrition — Vitamins and Minerals — Nutrition and Energy; Minerals; Vitamins
7. Diet and Health — Food Choices and Irish Food; Diet and Health
8. Meal Planning and Preparation — Food Preparation
9. Foods — Food Commodities and Extras; Milk and Milk Products
10. Food Safety, Spoilage and Hygiene — Food Processing, Safety, and Hygiene; Microbiology
11. Household Appliances — Household Technology
12. Textiles — Textiles Overview
