# Leaving Cert Business (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format,
  worked example). This outline says **what** to cover; that file says **how** to write it. An
  information package (`course-outlines/packages/business/<loId>.md`, see `packages/README.md`)
  must be written for each subsection before its notes. None exist yet for business.
- **The syllabus:** the NCCA *Curriculum Specification for Leaving Certificate Business*, for
  introduction to schools in September 2025, published August 2024. It is **first examined in
  June 2027**, so it is the correct document for this app's students. The official PDF is
  `pipeline/resources/business/spec-syllabus.pdf` (also `relevant-resources/syllabi/business.pdf`);
  on 2026-11-05 both were checked byte-for-byte against the copy on curriculumonline.ie.
- **Do not use the old *Leaving Certificate Business Syllabus*** (Government of Ireland © 1996,
  first examined 1999, labelled on curriculumonline.ie "for examination to June 2026"), or its
  2018 Legislation Guidelines. It is a different course: Units 1–7, ratios, contract law,
  household management, the Applied Business Question. Appendix A4 lists what it had that this
  course does not. **Every SEC paper from 1999 to 2026 was set on the old syllabus.** Use one only
  as legacy practice, and only where its topic is also in this specification.
- **References** in square brackets are the specification's own numbering:
  **[2.4.3]** = Strand 2, section 4 ("The target market"), learning outcome 3. **[U3.2]** = the
  Unifying Strand, section U3, learning outcome 2. **[2.4]** alone = the whole section.
- **Chapters** are the app's 20 business chapter IDs (`data.js`; business has no
  `pipeline/scaffold` file yet). Keep every ID exactly as written. The IDs follow the
  specification's section order: ch0 = the Unifying Strand; ch1–ch5 = 1.1–1.5; ch6–ch12 =
  2.1–2.7; ch13–ch16 = 3.1–3.4; ch17–ch19 = 4.1–4.3. The original 10 chapters (ch1, ch6–ch12,
  ch16, ch17) are outlined in the strand sections below. The 10 added on 2026-11-05 with the
  user's approval (ch0, ch2–ch5, ch13–ch15, ch18–ch19) are outlined in Appendix B. They have no
  notes yet: 86 of the 138 learning outcomes (62%) still have no content in the app.
- **Subsection ids** for notes are `<chapter-id>-s<n>` (e.g. `ch9-s3`), in the order below.
  Every chapter uses them in `data.js` (split 2026-11-05, when notes were first written for
  the whole course). The old per-outcome entries (`lo1-1` etc.) and `business-content.js`, which
  held the pre-restructure notes, were retired then; they remain in git history.
- **What each subsection contains:**
  - **Syllabus**: what the specification says students learn about and should be able to do,
    close to its wording. This is the required scope; every item must be covered.
  - **Cover**: what the notes for the subsection should contain, including the assumed knowledge
    (NOTES_STANDARD rule 9) that the outcomes rest on. Facts marked *(verify)* change over time
    and the package must check them against a current primary source before notes use them.
  - **Exam**: how the SEC's 2025 sample papers (Higher Level Sample 1 and Sample 2) test it, where
    they do. Question wording is paraphrased; never copy it into notes.
  - **SimpleStudy**: the matching topic(s) in SimpleStudy's Higher Level course (recorded
    2026-08-07, `pipeline/resources/business/guide-simplestudy.md`). Structure and naming only.
- **Settings:** the specification names no example businesses or places. Notes use the
  package's checked Irish examples. The sample papers show the style the SEC uses: real, current,
  named Irish firms and news stories (ProjectOne, Grá Chocolates, Dexcom Athenry, Glanbia,
  Spectrum.Life, The Local Table, Bank of Ireland, Storm Éowyn insurance claims).
- **Higher vs Ordinary level:** the specification marks **no** learning outcome as Higher Level
  only. Both levels study everything; Higher Level answers need "sophisticated understanding",
  evaluation of unfamiliar problems and justified viewpoints (Table 1). Mark nothing as HL only.
- **Choices the specification sets** (write content for more than one option so students can
  choose):
  - three Irish government policies affecting three different sectors [1.4.1] (Appendix B, ch4);
  - one EU regulation and one EU directive of the student's choice [1.4.6]. **They must be
    different from any legislation used in 4.1 (consumer) and 4.3 (employee)** (spec footnote 1),
    so GDPR and the employment directives cannot be the 1.4.6 choices;
  - a marketing mix for a product **and** a service of choice, each with a USP analysis [2.4.3];
  - one leadership style "you have studied" (sample paper wording) [3.1.3]: cover several.
- **Cross-cutting themes:** ethics and sustainability, entrepreneurial thinking, business and
  financial literacy, digital transformation. The written exam explicitly assesses applying them,
  so every chapter's notes should include the ethical, sustainability and digital angle of the
  topic where one exists.
- **"Applying my learning"** sections [1.6], [2.8], [3.5], and the media outcomes in [4.1.5],
  [4.2.9] and [4.3.6] require students to analyse business news and give an informed opinion. They
  are not separate subsections. Each chapter should end its last subsection with one or two
  current Irish news examples linked to the topic *(verify)*.
- **Glossary:** terms marked * in the specification have official definitions in its Appendix 2.
  Notes must use definitions consistent with them; they are listed per chapter.
- **The 7 Ps in this specification are** product/service, pricing, promotion, people,
  **packaging**, process and place [2.4]. It does not list "physical evidence". Teach the
  specification's list.
- **Assessment (spec pp. 31–35; SEC 2027 materials):**
  - **Written examination, 60% (300 marks).** Higher and Ordinary papers. Higher Level: 2 hours
    30 minutes; **Question 1, "The Business World", is compulsory (90 marks)**, a case study
    with parts (a)–(e); then **any three of Questions 2–5 (70 marks each)**. Questions are built
    on short real-world stimulus (news headlines, company profiles, a graph) and mix
    fill-in-the-blank, true/false, "identify", "outline", "explain", "analyse", "discuss",
    "evaluate", and applied tools (stakeholder mapping, Porter's five forces, force-field
    analysis, cost-benefit analysis, design thinking). The command words are defined in the
    specification's Appendix 1; notes should give enough distinct points per topic to answer at
    "discuss/evaluate" depth (3–4 developed points per part).
  - **Business Alive Investigative Study (AAC), 40% (200 marks).** Common brief from the SEC each
    year, issued in term two of 5th year; up to 20 hours; individual digital report of **at most
    1,500 words and 10 images**. Sections: Introduction (~200 words), Investigation and Findings
    (~400), Analysis and Evaluation (~600), Conclusions (~300), References. Marks: Introduction
    20; Investigation, Findings, Analysis and Evaluation 100; Conclusion 30; Overall coherence 50.
    **The live 2027 brief:** investigate how a work practice that uses digital technology is
    impacting either employers or employees, supported by primary and/or secondary data; submit to
    the class teacher by **12 March 2027** (SEC brief 2027L033C2EL). See chapter ch0 and
    ch14-s5.
  - Sources: SEC sample papers 2027L033A1ES1 (Sample 1) and Sample 2, sample brief 2027L033C2ES,
    live brief — all at examinations.ie/scr and examinations.ie (coursework, 2027).

---

## Strand 1 — Exploring the Business Environment

Chapters ch2–ch5 (sections 1.2–1.6) are outlined in Appendix B.

### ch1 — Key Stakeholders in Business [1.1]

Glossary: stakeholder mapping; power-interest grid.

1. **Stakeholders, their importance and interdependence** [1.1.1]
   - Syllabus: key stakeholders in business (including business owners, investors, employees,
     consumers, suppliers, local community and government); their importance in business; their
     interdependencies; the needs and wants of different stakeholders at different stages of
     business development. Outline the key internal and external stakeholders and demonstrate
     their importance in the business environment.
   - Cover: internal vs external stakeholders; for each of the seven named stakeholders (plus
     managers and interest groups as assumed knowledge): who they are, their role, why they
     matter, what they need and want; how needs and wants change from start-up to growth to
     maturity (e.g. investors want security early, return later; employees want job security vs
     progression); interdependence (each depends on the others; one change ripples through);
     an applied Irish example per stakeholder *(verify)*.
   - Exam: S1 Q2(a)(ii) importance of a founder's relationship with suppliers; S1 Q1(a) how a firm
     contributes to the local economy.
   - SimpleStudy: Key Stakeholders in Business.
2. **Stakeholder interaction, conflict and its resolution** [1.1.2, 1.1.3]
   - Syllabus: demonstrate how stakeholders interact and identify potential conflict between
     stakeholders; suggest appropriate ways of avoiding and resolving conflict between them.
   - Cover: co-operative vs competitive relationships; common conflicts with causes (owners vs
     employees over pay; business vs community over planning or pollution; business vs consumers
     over price and quality; business vs suppliers over price and payment terms; investors vs
     management over risk and dividends; business vs government over tax and regulation);
     avoiding conflict (communication and consultation, CSR, fair contracts, shared goals,
     transparency); resolving it (negotiation, compromise, mediation, partnership agreements,
     third parties, and the legislative routes taught in ch17 and ch19 — refer, don't repeat).
   - SimpleStudy: Key Stakeholders in Business.
3. **Stakeholder mapping and prioritising stakeholder interests** [1.1.4]
   - Syllabus: conduct stakeholder mapping and explain the importance of prioritising different
     stakeholder interests.
   - Cover: what stakeholder mapping is (glossary: written or visual; includes stakeholders,
     interdependencies, inter-relationships, power and influence on decisions); the
     power-interest grid and its four quadrants with the action for each (manage closely, keep
     satisfied, keep informed, monitor); step-by-step method for mapping a given decision; why
     prioritise (limited resources, decision speed, avoiding conflict, legitimacy); limitations
     (positions change; subjective judgements); one fully worked mapping of an Irish case.
   - Exam: S2 Q1(b)(i) conduct stakeholder mapping to identify and prioritise four stakeholders
     affected by a restaurant's menu decision.
   - SimpleStudy: Key Stakeholders in Business.

---

## Strand 2 — Understanding Enterprise

### ch6 — Enterprise in Action [2.1; 2.8]

Glossary: competencies (of entrepreneurs).

1. **Enterprise, innovation, intrapreneurship, entrepreneurship and the competencies of
   innovators** [2.1.1, 2.1.2; 2.8.1]
   - Syllabus: the range of different reasons for starting an enterprise; how enterprise and
     innovation are present in, and important for, government, society, business, the community
     and students' own lives; the competencies that support innovation and enterprise
     development. Identify examples of innovation, intrapreneurship and entrepreneurship
     locally, nationally and internationally, and explain the importance of innovation for
     business, the economy and society; identify the competencies of innovators and outline why
     they matter when starting a business. Analyse news about enterprise and innovation.
   - Cover: definitions of enterprise (broad sense, not only start-ups), innovation (product,
     process, business-model), entrepreneur, intrapreneur; reasons for starting an enterprise
     (financial and non-financial: independence, a gap in the market, a social goal,
     redundancy, passion, recognition); enterprise in government, community, social enterprise
     and personal life; local, national and international examples of each *(verify)*;
     importance of innovation for the business (competitive advantage, growth), the economy
     (jobs, exports, tax) and society (solutions to problems, sustainability); the competencies
     of innovators (glossary: knowledge, skills, values and dispositions), e.g. creativity,
     risk-taking, resilience, self-confidence, decisiveness, vision, initiative, networking,
     adaptability, with why each matters at start-up.
   - Exam: S1 Q2(a)(i) identify four key competencies of innovators.
   - SimpleStudy: Enterprise.
2. **The role of government in supporting enterprise** [2.1.3]
   - Syllabus: the role of the Irish government in supporting business and enterprise in
     Ireland both locally and nationally; investigate how government fosters enterprise and
     supports business development and growth.
   - Cover: the main state agencies and what each offers *(verify all names, schemes and
     amounts)*: Local Enterprise Offices (grants, mentoring, training, Trading Online Voucher),
     Enterprise Ireland (high-potential start-ups, exporters), IDA Ireland (FDI; detail in ch5),
     Údarás na Gaeltachta, MicroFinance Ireland, the SBCI and state-backed loan schemes;
     tax measures (low corporation tax, R&D tax credit, start-up reliefs, EIIS); education and
     training (Skillnet, ETBs); infrastructure and broadband; regional and rural supports;
     enterprise policy (White Paper on Enterprise); government as a regulator that also
     protects business. Benefits and limits of state support.
   - Exam: S2 Q4(e) discuss three ways the Irish government can support a growing Irish firm.
   - SimpleStudy: Enterprise.

### ch7 — Idea Development [2.2]

Glossary: design thinking.

1. **How business ideas are developed** [2.2.1]
   - Syllabus: how business ideas are developed; determine the factors that impact on the
     development of business ideas.
   - Cover: internal sources (staff and intrapreneurs, R&D, brainstorming, existing products,
     sales data) and external sources (customers, competitors, market research, trends,
     technology, travel, hobbies, government and university research); idea generation and
     screening; factors that help or hinder development (market demand, competition, finance,
     skills and experience, technology, legal and regulatory constraints, economic conditions,
     ethics and sustainability, timing); examples of Irish ideas developed from each source
     *(verify)*.
   - SimpleStudy: Idea Development.
2. **Design thinking** [2.2.2]
   - Syllabus: the significance of design thinking, including the four phases of clarify,
     ideate, develop and implement, to support idea development; outline design thinking as an
     innovative approach and appreciate how the process is iterative and both solution- and
     person-centred.
   - Cover: the glossary definition (innovative, non-linear, focused on solutions for the end
     user); each of the four phases in the specification's own names (clarify, ideate, develop,
     implement) with what happens and the tools used (empathy and user research, problem
     statement, brainstorming, prototyping, testing, feedback, launch); what "iterative",
     "person-centred" and "solution-centred" mean; benefits and drawbacks; a worked example of
     a product going through all four phases.
   - Exam: S1 Q1(d) outline how a firm can use each of the four phases of design thinking to meet
     a client's expectations.
   - SimpleStudy: Idea Development.
3. **The feasibility study** [2.2.2, 2.2.3]
   - Syllabus: the importance of evaluating a business idea to determine its potential future
     viability; appreciate the importance of conducting a feasibility study.
   - Cover: what a feasibility study is and when it is done; its parts (market, financial —
     start-up and running costs, projected revenue, break-even as assumed knowledge, cash needs —
     technical/production, organisational and staffing, legal and regulatory, environmental and
     ethical); outcomes (proceed, modify, abandon); benefits (reduces risk, supports funding,
     identifies problems early); limitations (cost, time, forecast uncertainty).
   - SimpleStudy: Idea Development.

### ch8 — Business Planning [2.3]

Glossary: business model; business model canvas.

1. **The business plan, and ethics and sustainability in planning** [2.3.1, 2.3.2]
   - Syllabus: the importance of a coherent business plan at different stages of business
     development and how it supports start-up, operations, funding and development; the need to
     consider ethical and sustainability factors. Outline the key functions of a business plan
     and the importance of ethics and sustainability when planning.
   - Cover: definition; functions (direction and goals, raising finance, a benchmark for
     control, testing viability, communicating with stakeholders); typical sections (executive
     summary, business description, market analysis, marketing plan, operations, management and
     staffing, financial plan with cash-flow forecast, risks); how the plan's role changes from
     start-up to growth; ethical factors (fair treatment of staff and suppliers, honest marketing,
     responsible sourcing) and sustainability factors (environmental impact, circular design,
     social impact, long-term viability), and why investors and customers now expect them (link
     to ESG in ch2).
   - SimpleStudy: Business Planning.
2. **Business models and the business model canvas** [2.3.3, 2.3.4]
   - Syllabus: the role of business models in generating income and creating, delivering and
     capturing value for the enterprise and its customers; the importance of the business model
     and the elements of the business model canvas. Explain what a business model is and its
     role within the business plan; identify the key elements of the canvas and outline the role
     of business models in successful enterprises.
   - Cover: the glossary definitions; value creation, delivery and capture; the nine canvas
     blocks (key partners, key activities, key resources, value proposition, customer
     relationships, channels, customer segments, cost structure, revenue streams), each with a
     definition and an example; how the canvas links to the plan; a completed canvas for one
     Irish business *(verify)*; why a sound model underpins success.
   - SimpleStudy: Business Planning.
3. **Common business models** [2.3.5]
   - Syllabus: a range of business models including retail, manufacturing, subscription,
     franchise and affiliate; identify and compare the most common business models.
   - Cover: each of the five named models: how it makes money, key features, advantages,
     disadvantages and an example *(verify)*; franchising in detail (franchisor vs franchisee,
     fees and royalties); a comparison of the models on revenue, cost, control, risk and
     scalability.
   - SimpleStudy: Business Planning.
4. **The digital economy and technology-driven business models** [2.3.6, 2.3.7]
   - Syllabus: the digital economy, including marketplace, subscription, crowdfunding and
     advertising-supported models; their similarities to and differences from non-digital
     models; how businesses have adapted to or developed from the digital economy and other
     internal or external drivers. Outline how digital technology drives change in business;
     identify and compare technology-driven models and their key characteristics.
   - Cover: digital technology as a driver of change (e-commerce, platforms, data, AI,
     automation); each of the four named models with characteristics, how revenue is earned,
     advantages, disadvantages and an example *(verify)*; crowdfunding as both a model and a
     source of finance (reward, equity and lending types); comparison with non-digital models;
     examples of Irish firms that adapted (moved online, launched subscriptions).
   - Exam: S1 Q2(b) explain crowdfunding; explain two characteristics of the subscription and
     advertising models. S2 Q3(d) compare a subscription service with another technology-driven
     model under headings such as revenue generation, access and cost, scalability.
   - SimpleStudy: Business Planning.

### ch9 — The Target Market [2.4]

Glossary: disruptive impact; power-interest grid; STEEPLE analysis.

1. **Market research and identifying the target market** [2.4.1]
   - Syllabus: the importance of identifying the target market; conducting market research;
     appreciate its importance and discuss how businesses conduct it.
   - Cover: purpose of market research; desk (secondary) vs field (primary) research, with
     methods (surveys, interviews, focus groups, observation, test marketing, CSO and industry
     reports, online analytics) and the strengths and weaknesses of each; quantitative vs
     qualitative data; sampling as assumed knowledge; market segmentation (demographic,
     geographic, psychographic, behavioural) as the way a target market is identified; niche vs
     mass markets; consumer profiles.
   - SimpleStudy: Market Research and Market Analysis.
2. **The marketing mix and the target market** [2.4.2]
   - Syllabus: outline the elements of the marketing mix — product/service, pricing, promotion,
     people, packaging, process and place — and explain their significance for a business and
     how they are influenced by the target market.
   - Cover: each of the seven elements in the specification's list (not "physical evidence"):
     definition, the decisions it involves and how the target market shapes it. Product:
     features, quality, branding, product life cycle as assumed knowledge. Pricing strategies:
     cost-plus, penetration, skimming, competitive, psychological, premium, loss leader.
     Promotion: advertising, sales promotion, personal selling, PR, sponsorship,
     social-media and influencer marketing. People, packaging, process. Place: channels of
     distribution, direct and online.
   - SimpleStudy: The Marketing Mix.
3. **Developing, evaluating and improving a marketing mix; the USP** [2.4.3, 2.4.4]
   - Syllabus: identifying the unique selling point, developing and modifying the marketing mix;
     develop a marketing mix for a product **and** a service of choice with a USP analysis for
     each; evaluate and suggest ways of improving an existing marketing mix.
   - Cover: what a USP is and how to analyse one (what makes it unique, why customers value it,
     whether it can be copied); a fully developed 7-P mix for one product and one service, each
     with a USP analysis (Irish examples, *verify*); criteria for evaluating a mix (fit with the
     target market, consistency between the Ps, competitiveness, profitability, ethics and
     sustainability); typical improvements; how a mix is modified over time.
   - Exam: S1 Q1(e)(ii) identify a firm's competitive advantage and recommend a launch strategy.
   - SimpleStudy: The Marketing Mix.
4. **Digital technology, ethics and sustainability in marketing** [2.4.5, 2.4.6]
   - Syllabus: how technology changes market research and marketing; the disruptive impact of
     digital technology on both; the importance of ethics and sustainability in marketing,
     including its influence on marketing companies and strategies; evaluate that influence.
   - Cover: the glossary's "disruptive impact" (positive and negative); digital research (online
     surveys, web analytics, social listening, big data, AI) and digital marketing (social
     media, influencers, search and targeted ads, e-commerce, personalisation), with benefits
     and drawbacks for firms and consumers; ethical marketing (honest claims, no exploitation
     of children or vulnerable groups, data privacy, influencer disclosure); sustainability in
     marketing (green products and packaging, greenwashing and its risks, regulation such as the
     EU green-claims rules *(verify)*); how ethics and sustainability shape strategy and
     reputation.
   - Exam: S1 Q5(b) outline three ways ethics matters when designing a marketing strategy. The
     2025 sample AAC brief was on ethics in marketing for a service business.
   - SimpleStudy: The Marketing Mix; Market Research and Market Analysis.
5. **Analytical tools: the power-interest grid for customers and STEEPLE** [2.4.7, 2.4.8]
   - Syllabus: the potential of a range of analytical tools to analyse customer interest and the
     external environment; use a power-interest grid to analyse customer interest and adjust the
     marketing mix as necessary; conduct a STEEPLE analysis to understand the external
     environment and identify issues of concern for a business.
   - Cover: applying the power-interest grid (defined in ch1-s3) to customer groups, with how the
     mix is adjusted for each quadrant; the seven STEEPLE factors (social, technological,
     economic, environmental, political, legal, ethical) with examples of each for an Irish
     business; STEEPLE assesses **external** factors only; how findings feed decisions; limits
     of both tools.
   - Exam: S1 Q4(a)(ii) true/false: "STEEPLE assesses internal factors" (false).
   - SimpleStudy: Market Research and Market Analysis.

### ch10 — Operations and Finance [2.5]

1. **The operational model: key partners, activities and resources** [2.5.1]
   - Syllabus: the elements of the operational aspect of the business, including key partners,
     key activities and key resources, and how they may evolve over time; outline the main
     elements of a business's operational model and explain why they may change.
   - Cover: each element defined (with the canvas link from ch8-s2) and illustrated; types of
     key resources (physical, human, intellectual, financial); key activities (production,
     problem-solving, platform); key partners (suppliers, strategic alliances, outsourcing);
     production methods (job, batch, mass) as assumed knowledge; why each changes over time
     (growth, technology, cost pressure, sustainability goals, supply-chain shocks).
   - SimpleStudy: Operations and Finance.
2. **Costs and revenue streams** [2.5.2]
   - Syllabus: the key costs incurred (variable costs, fixed costs) and the potential revenue
     streams (single transactions or recurring sales); understanding that these may evolve over
     time; identify key costs and explore why they change over the lifecycle of the product or
     service.
   - Cover: fixed vs variable costs with examples (classification questions are examined);
     start-up vs running costs; total cost; revenue streams (one-off transaction vs recurring:
     subscription, licensing, usage fees, advertising); how costs and revenues change through the
     product life cycle (introduction, growth, maturity, decline) and the business lifecycle;
     profit as revenue minus costs and break-even as assumed knowledge.
   - Exam: S1 Q4(a)(ii) true/false: "variable costs include wages, insurance and electricity".
   - SimpleStudy: Operations and Finance.
3. **Sources of finance across the lifecycle** [2.5.2]
   - Syllabus: identify the key sources of finance for a business and explore why these may
     change over the lifecycle.
   - Cover (assumed knowledge, needed to meet the outcome): short-term sources (bank overdraft,
     trade credit, accrued expenses, factoring, credit card), medium-term (term loan, leasing,
     hire purchase), long-term (owner's equity, share capital, venture capital, business angels,
     long-term loans and debentures, grants, retained earnings, crowdfunding); for each: what it
     is, cost, control, security, advantages and disadvantages; matching finance to purpose;
     equity vs debt; why sources change from start-up (savings, family, grants, micro-loans) to
     growth (venture capital, loans) to maturity (retained earnings, share issues). State
     schemes *(verify)* belong to ch6-s2 — refer, don't repeat.
   - SimpleStudy: Operations and Finance.
4. **Cash-flow analysis** [2.5.3]
   - Syllabus: the business may need to take action to address issues that arise; analyse the
     cash flow of a business and recommend a suitable course of action to address the issues
     the analysis identifies.
   - Cover: purpose of a cash-flow forecast; its layout (receipts, payments, net cash flow,
     opening and closing balance) with a fully worked numerical example; how to read it
     (months with deficits, causes such as seasonality, large capital payments, late debtors);
     remedies (arrange an overdraft in advance, delay or reschedule payments, chase debtors,
     lease instead of buy, cut costs, inject capital, invoice discounting); cash vs profit.
   - SimpleStudy: Operations and Finance.

### ch11 — Growth, Development and Expansion [2.6]

Glossary: Porter's five forces model.

1. **Competition, competitive advantage and Porter's five forces** [2.6.1, 2.6.2]
   - Syllabus: the importance of identifying potential competition and competitors, the
     significance of a business's competitive advantage and how it can capitalise on it; use
     Porter's five forces model to identify and analyse competition and to identify a business's
     competitive advantage.
   - Cover: direct vs indirect competitors; why identify them; competitive advantage (cost,
     differentiation, focus) and how a firm capitalises on it; each of the five forces (threat
     of new entrants, bargaining power of suppliers, bargaining power of customers, threat of
     substitutes, competitive rivalry) with the factors that make it high or low; a fully
     worked five-forces analysis of an Irish market *(verify)* ending in a conclusion about
     industry attractiveness and the firm's advantage.
   - Exam: S1 Q1(e)(i) analyse the competitive forces in a market using Porter's five forces;
     (ii) identify a competitive advantage and recommend a strategy.
   - SimpleStudy: Growth, Development, and Expansion.
2. **Strategies to adapt or expand, and the role of technology** [2.6.3, 2.6.4]
   - Syllabus: how enterprise is not static and how a business may develop and may use
     technology to support growth; outline the strategies a business uses to adapt or expand;
     appreciate the potential of technology to support adaptation and expansion.
   - Cover: reasons to expand (economies of scale, market share, diversification of risk,
     survival); organic (internal) strategies: new products, new markets, increased capacity,
     franchising out, e-commerce, exporting; inorganic (external) strategies: merger, takeover
     or acquisition, strategic alliance, joint venture; advantages and disadvantages of each;
     finance for expansion (refer to ch10-s3); technology enabling growth (e-commerce and
     marketplaces, automation, cloud, data and AI, remote working); risks of growing too fast.
   - Exam: S1 Q2(c) outline three factors to consider before expanding into an international
     market (links ch5).
   - SimpleStudy: Growth, Development, and Expansion.
3. **Cost-benefit analysis of expansion** [2.6.5]
   - Syllabus: the importance of considering both potential benefits and potential costs when
     making business decisions; conduct a cost-benefit analysis to analyse the implications of
     business expansion.
   - Cover: what CBA is; steps (identify the decision; list financial and non-financial costs and
     benefits for the firm and wider stakeholders; quantify where possible; compare; decide);
     tangible vs intangible items; opportunity cost; short- vs long-term; a fully worked CBA of
     an expansion (takeover or new site) in a table, with a justified recommendation;
     limitations.
   - Exam: S2 Q5(b) conduct a cost-benefit analysis of a proposed takeover (given share price,
     premium, profits and regulatory risk).
   - SimpleStudy: Growth, Development, and Expansion.
4. **Adapting to external drivers through the marketing mix and business model** [2.6.6]
   - Syllabus: how a business may have to adapt to external drivers (including customer
     demographics, competition and economic factors) to enhance financial sustainability, and
     address issues through its product/service, pricing, promotion, people, packaging, process
     and place and/or business model; outline such strategies.
   - Cover: the named external drivers and others from STEEPLE; for each P, how it can be
     adapted (with an example); adapting the business model (new revenue streams, new channels,
     subscription, outsourcing); financial sustainability as the aim; a worked example of a firm
     responding to rising costs or a demographic shift *(verify)*.
   - Exam: S2 Q1(b)(ii) challenges of introducing new products and how to address them; S2
     Q1(a) impact of a minimum-wage increase on a restaurant.
   - SimpleStudy: Growth, Development, and Expansion.

### ch12 — Managing Risk [2.7]

1. **The risks of enterprise and why risk management matters** [2.7.1, 2.7.2]
   - Syllabus: the nature of risk within entrepreneurship and the importance of risk management;
     outline the challenges and risks of enterprise and entrepreneurship, and the importance of
     assessing and managing risks.
   - Cover: challenges of starting a business (finance, competition, time, skills, regulation);
     categories of risk (financial, market, operational, legal and compliance, reputational,
     cyber and technological, environmental and climate, personal risk to the entrepreneur);
     risk assessment (identify, evaluate likelihood and impact, prioritise in a risk matrix,
     act, monitor); why manage risk (survival, lower costs and premiums, legal duty under health
     and safety law, investor and lender confidence, continuity).
   - Exam: S2 Q3(a) explain two reasons why managing risk is important (stimulus: Storm Éowyn
     insurance costs).
   - SimpleStudy: Risk Management and Insurance.
2. **Risk management strategies and insurance** [2.7.3]
   - Syllabus: a range of risk management strategies including avoidance, spread and prevention,
     and the importance of choosing suitable insurance products; analyse strategies used to
     respond to the challenges and risks of business.
   - Cover: the specification's named strategies — avoidance, spread (diversification of
     products, markets and suppliers) and prevention (reduction: training, safety, maintenance,
     cyber security) — plus transfer (insurance, contracts) and retention as assumed knowledge;
     analysis of each (when it suits, cost, limits); insurance basics needed to choose products
     (premium, policy, claim, excess, insurable vs uninsurable risk); main business insurance
     products and what each covers (property, public liability, employer's liability, product
     liability, professional indemnity, motor, business interruption, cyber, goods in transit,
     key-person); how to choose (risk exposure, cost vs cover, legal requirements). The six
     principles of insurance and averaging calculations were old-syllabus content; leave them
     out.
   - Exam: S1 Q3(e) discuss four risk management strategies.
   - SimpleStudy: Risk Management and Insurance.

---

## Strand 3 — Leading in Business

Chapters ch13–ch15 (sections 3.1–3.3 and 3.5) are outlined in Appendix B.

### ch16 — The Rationale for Planning [3.4]

Glossary: force-field analysis.

1. **Change, resistance to change and fostering innovation** [3.4.1–3.4.4]
   - Syllabus: the internal and external changes that impact on an organisation, how resistance
     to change can arise, and how to foster innovation and approach resistance. Outline the
     internal and external changes organisations meet over their lifetime; analyse the reasons
     for resistance; identify the practices that promote innovation and
     entrepreneurial/intrapreneurial thinking; outline approaches to overcoming resistance.
   - Cover: internal changes (new leadership, restructuring, new technology, growth, new
     products) and external changes (STEEPLE factors: economy, competition, regulation,
     technology, climate, pandemics); reasons for resistance (fear of job loss, loss of status
     or control, uncertainty, habit, lack of trust or information, extra workload); practices
     that promote innovation (empowerment, idea schemes, time for projects, rewarding risk,
     cross-functional teams, tolerance of failure); approaches to overcoming resistance
     (communication, consultation and participation, training, support, negotiation and
     incentives, leading by example, phased change).
   - Exam: S1 Q5(d) analyse four reasons for resistance to change; S2 Q3(b) outline two ways to
     overcome it (stimulus: a return-to-office mandate).
   - SimpleStudy: The Rationale for Planning.
2. **Strategic planning and force-field analysis** [3.4.5–3.4.7]
   - Syllabus: the significance of strategic planning as an ongoing process, how it supports
     leading and managing change, and how a force-field analysis can support strategic
     decision-making. Outline strategic planning and why it is ongoing; describe its benefits;
     explain the importance of planning for change and discuss how a force-field analysis could
     support strategic planning for change.
   - Cover: strategic vs tactical vs operational planning as assumed knowledge; mission,
     vision, goals; the strategic planning cycle (analyse, set objectives, choose strategy,
     implement, monitor and review) and why it is continuous; tools that feed it (SWOT as
     assumed knowledge, STEEPLE from ch9-s5); benefits (direction, coordination, resource
     allocation, anticipating change, motivation, control); force-field analysis: driving vs
     restraining forces (internal and external), scoring, deciding, strengthening drivers and
     weakening restraints, with a fully worked example and its limitations.
   - Exam: S2 Q1(d) use a force-field analysis to examine a decision to close two restaurants;
     S1 Q4(a)(ii) true/false: "strategic planning sets out long-term objectives".
   - SimpleStudy: Force Field Analysis and Strategic Planning.
3. **Contingency planning and crisis management** [3.4.8, 3.4.9]
   - Syllabus: the importance of contingency planning for effective crisis management, which may
     arise locally or nationally, and the need to consider factors including cost, time and risk
     when developing a contingency plan. Explain contingency planning in terms of crisis
     management; discuss the factors to consider.
   - Cover: definitions of crisis, crisis management and contingency plan; examples of local and
     national crises (fire, cyber-attack, product recall, storm, pandemic, supply failure, key
     staff loss) *(verify Irish examples)*; stages of crisis management (prevention,
     preparation, response, recovery, review); what a contingency plan contains (triggers,
     responsibilities, communication plan, backups, alternative suppliers); the factors to weigh
     (cost, time, risk likelihood and impact, resources, legal duties, stakeholders); benefits
     and limits.
   - SimpleStudy: Force Field Analysis and Strategic Planning.

---

## Strand 4 — Being Informed and Making Informed Decisions

Chapters ch18–ch19 (sections 4.2 and 4.3) are outlined in Appendix B.

### ch17 — Making Informed Decisions as a Consumer [4.1]

Glossary: circular economy; shadow economy.

Footnote 2 of the specification: students engage with **current** legislation; where it changes
during the two years, either version may be used. Packages must check every Act, regulator and
monetary limit against a current primary source *(verify)*.

1. **Consumer rights, responsibilities and legislation** [4.1.1]
   - Syllabus: how different pieces of legislation set out rights and responsibilities that
     consumers should be aware of regarding products, services and digital services and their
     promotion, and how these rights change when buying outside the EU; investigate the rights
     and responsibilities of consumers using current consumer legislation.
   - Cover: the Consumer Rights Act 2022 (goods, services, digital content and digital services;
     remedies of repair, replacement, price reduction and termination; time limits; unfair contract
     terms); the Consumer Protection Act 2007 (misleading and aggressive practices, prohibited
     practices, advertising and promotion); the CCPC and its powers; other promotion rules
     (advertising standards code); consumer responsibilities (keep receipts, read terms, act
     promptly, use goods properly); redress steps (complain to the seller, ADR, Small Claims
     procedure — limit and fee *(verify)*, courts); buying inside vs outside the EU (EU-wide
     rights, European Consumer Centre Ireland, UK after Brexit, customs and VAT on non-EU
     purchases, weaker remedies).
   - SimpleStudy: Consumer Rights.
2. **Ethical and sustainable consumption, the shadow economy and digital technology** [4.1.2,
   4.1.3]
   - Syllabus: the importance of ethics and sustainability, including the consequences of
     participating in the shadow economy for the consumer, the business and the economy, and how
     consumers contribute to the circular economy; how technology affects consumers positively
     and negatively; demonstrate how consumer behaviour might be informed by ethical and
     sustainability concerns; investigate how digital technology affects consumer behaviour.
   - Cover: ethical consumer choices (fair trade, labour standards, animal welfare, local
     sourcing) and sustainable ones (reduce, reuse, repair, recycle, second-hand, energy labels);
     the circular economy (glossary definition) and what consumers can do in it, including Irish
     schemes such as the deposit return scheme *(verify)*; the shadow economy (glossary:
     illegal goods or transactions outside the law or reporting rules) and its consequences —
     for consumers (no rights or guarantees, safety risks), businesses (unfair competition) and
     the economy (lost tax revenue, worse public services); digital technology's positive effects
     (choice, price comparison, convenience, reviews) and negative ones (impulse buying,
     targeted advertising, dark patterns, fraud, data use, influencer pressure).
   - Exam: S1 Q3(d) analyse three ways digital technology influences consumer behaviour; S2
     Q3(e) evaluate the impact of digital technology on consumer behaviour; S2 Q5(c)(ii) four ways
     a consumer can contribute to the circular economy; S2 Q2(a) fill-in "circular economy".
   - SimpleStudy: Making Informed Consumer Decisions.
3. **Protecting personal data; making informed consumer decisions** [4.1.4, 4.1.5]
   - Syllabus: how European regulation protects personal data; investigate it; appreciate the
     importance of informed consumer decisions and discuss consumer stories in the news.
   - Cover: the GDPR (an EU regulation): personal data, data controller and processor, lawful
     bases including consent, the core principles, data-subject rights (access, rectification,
     erasure, portability, objection), breach notification, fines; the Data Protection Commission
     and the Data Protection Act 2018 *(verify)*; what it means for consumers and for
     businesses; how to protect your own data; why informed decisions matter (value for money,
     avoiding fraud, sustainability); one or two current consumer news stories *(verify)*.
     GDPR used here cannot be the student's EU regulation for [1.4.6].
   - SimpleStudy: Making Informed Consumer Decisions.

---

## Appendix A — Where the specification differs from SimpleStudy and from the repo's earlier assumptions

### A1. In the specification but missing from SimpleStudy (as a named topic)

SimpleStudy's 35 topics follow the specification's section names, so most gaps are at the level
of named items within a topic. Its topic list does not show:

- **U6 Acknowledging sources** (it has U1–U5 only).
- The **"Applying my learning"** sections [1.6, 2.8, 3.5] and the media outcomes [4.1.5, 4.2.9,
  4.3.6].
- **Semi-state** enterprises, nationalisation and privatisation [1.2.1–2]; **ESG** reporting
  [1.2.5] — check inside "Forms of Business; Business Regulation and Governance".
- The **value of the business economy in Ireland** (turnover and employment patterns) [1.3.2].
- **EU regulations vs directives vs opinions** and the evaluation of one of each [1.4.5–6] —
  SimpleStudy's "The European Union" unit may not cover the required choice.
- **Balance of payments and balance of trade calculations** [1.5.6].
- **Central Bank Digital Currency** vs stablecoins and crypto-assets [4.2.8]; **fintech**
  [4.2.4]; **financial fraud** [4.2.7]; **switching providers** [4.2.3] — check inside
  "Making Informed Financial Decisions; Financial Regulation".
- **Corporate wellness** [3.2.14–15], **remote and blended working** [3.2.11–13] and
  **sustainable workplaces** [3.2.10] — check inside "Human Capital Management".
- **The annual government budget's impact on workers** [4.3.5] and the **gig economy** [4.3.4].

### A2. In SimpleStudy but not in the specification as named

- Unit titles carried over from the old syllabus: "Management Skills: Leading and Motivating",
  "Management Activities: Planning, Organising and Controlling", "Conflict Resolution:
  Industrial Relations", "Insurance and Managing Risk", "Getting Started in Business",
  "Identifying Business Opportunities". The topics inside them use the new section names; the
  old frameworks (planning-organising-controlling, industrial-relations machinery as a unit) are
  not specification headings.
- "Market Segmentation" is not named in the specification; it is kept as assumed knowledge for
  identifying the target market (ch9-s1).
- "Sources of Finance and Cash Flow Management" mixes [2.5] (business finance) with [4.2] and
  financial regulation (personal finance). Keep them apart: ch10 is the business, ch18 the
  consumer.
- "Assessment: Written Exam" is an assessment node, not content.

### A3. Corrections to the repo's earlier assumptions (made in this restructure)

- **Cutoff:** `pipeline/config.py` had business at `(1999, False)`, "estimate; verify". The
  previous syllabus (© 1996, introduced 1997) was first examined in 1999 and last examined June
  2026 (curriculumonline.ie labels it "for examination to June 2026"). It is now `(1999, True)`
  with the same note as biology and chemistry: papers before 2027 are legacy practice, and the
  bundle's `firstExamYear` 2027 takes over from 2027.
- **Bundle and links:** the manifest, `relevant-resources.js` and the resources README now say
  the 2025 specification is first examined June 2027, and the manifest records the check of the
  PDF against the official file.
- **The app's business chapters covered only 10 of the 19 contextual sections** and none of the
  Unifying Strand. The 10 missing chapters were added to `data.js` on 2026-11-05 (Appendix B).
- **Assessment weighting** is 60% written exam / 40% AAC. The old syllabus was 100% written
  exam with an Applied Business Question; nothing in the app should describe that format.
- **The 7 Ps** are the specification's list, including packaging and not physical evidence.
  The existing ch9 notes merge "physical evidence" into packaging; new notes should not.
- `exam-breakdown.js` still says no paper has been released for the new course. The SEC has
  published two Higher and two Ordinary Level sample papers (2025); the breakdown can now be
  written (not done here; outside this restructure).
- `app.js` `FALLBACK_CHAPTERS` vocabulary (shown only if `data.js` fails to load) includes a
  chapter "14" with "Management: planning, organizing, and controlling", an old-syllabus
  framing. Low priority; not changed.

### A4. Old-syllabus content that must not be taught as topics

The old syllabus (Units 1–7) had these; the 2025 specification does not. Don't write notes on
them. Where one is needed as a small piece of assumed knowledge it is named in the subsection's
Cover line.

- Contract law (offer, acceptance, consideration, capacity; termination; remedies).
- Household management; personal taxation computations and tax forms (PAYE calculations).
- Monitoring the business: final accounts, balance sheets, profitability and liquidity ratios,
  debt/equity ratio.
- Management activities as planning, organising and controlling; organisation structures
  (functional, matrix, span of control) as a topic.
- Written business communication formats: memos, reports, business letters, agendas and minutes,
  duties of the chairperson and secretary; visual presentation of data as a drafting exercise.
- Classic motivation theories (Maslow, McGregor) as topics. [3.2.4] asks for the *factors* that
  affect motivation; a theory may be mentioned in one line where it explains a factor.
- Total quality management and empowerment as named topics.
- The six principles of insurance; averaging and premium calculations.
- Categories of industry and community development as units; transnational companies as a
  separate topic (globalisation and FDI now cover multinationals).
- The Applied Business Question (ABQ) exam format.

---

## Appendix B — Chapters added 2026-11-05 for specification content the app had no chapter for

These sections are in the specification and examined, but the app had no chapter for them. The
user approved adding them on 2026-11-05; they are now in `data.js` with the subsection ids below
(`ch0-s1` etc.) and no notes yet. Their IDs fill the gaps in the existing numbering, which
follows the specification's section order.

### ch0 — Investigating Business (Unifying Strand) and the Business Alive Investigative Study [U1–U6]

The specification weaves this strand through the four contextual strands and assesses it mainly
through the AAC (40%), though the written exam also assesses "the learning described in ... the
unifying strand".

Glossary: SMART objectives (for research); sources of information.

1. **Developing research questions, managing information and acknowledging sources** [U1.1,
   U2.1–U2.6, U6.1]
   - Syllabus: develop and refine questions to ensure clarity and the availability of sufficient,
     quality information, using SMART objectives; use a range of information and data;
     consider a variety of perspectives; assess sources for credibility, context, accuracy, bias,
     reliability and value; ensure data are representative and comprehensive; identify key
     points; analyse importance for different groups; identify gaps and their impact on
     conclusions; record and acknowledge all sources, primary or secondary, in any format.
   - Cover: SMART (specific, measurable, achievable, relevant, timebound) applied to a research
     question, with weak vs refined examples; primary vs secondary sources (glossary) and the
     methods for each; judging a source (author and expertise, date, purpose and bias, evidence,
     corroboration); representative samples; recording data; identifying gaps; referencing (a
     consistent style such as Harvard; in-text citation and reference list); the SEC rule that AI
     use must also be acknowledged; plagiarism.
   - SimpleStudy: Developing Questions to Research; Managing Information.
2. **Project planning** [U3.1–U3.3]
   - Syllabus: the significance of a detailed project plan and of monitoring progress; a plan with
     a clear purpose, goals and criteria for success that includes roles and responsibilities,
     resources, objectives, a detailed time schedule, risk assessment, monitoring and evaluation.
   - Cover: each element of a project plan defined with an example; Gantt-style time schedule
     as assumed knowledge; a short risk assessment for a project; monitoring (milestones, logs,
     the investigative folder the specification recommends) and evaluation; why planning and
     monitoring matter; a complete sample plan for a 20-hour study.
   - SimpleStudy: Project Planning.
3. **Analysing, evaluating and presenting findings** [U4.1–U4.5, U5.1–U5.4]
   - Syllabus: analyse and interpret information and data; evaluate the range of perspectives;
     synthesise findings; appraise the value of information; evaluate findings to make decisions,
     reach conclusions or make recommendations; communicate in a format and style suited to the
     audience (oral, visual, written, multimodal); use graphs, charts, diagrams and graphics;
     identify how and why one's perspective changed; present conclusions logically using correct
     business terminology.
   - Cover: interpreting tables and charts (trends, comparisons, percentages, averages);
     choosing the right chart; analysis vs evaluation vs synthesis (with the specification's
     command-word definitions); drawing justified conclusions and recommendations; stating
     limitations; reflective writing on how a perspective changed; writing for an audience.
   - SimpleStudy: Analysing and Evaluating Information; Presenting Findings and Perspectives.
4. **The Business Alive Investigative Study (AAC)**
   - Syllabus: the AAC section of the specification (pp. 32–34) and its Descriptors of Quality
     (planning; investigating; applying; communicating).
   - Cover: the 2027 requirements from the SEC brief (40%, 200 marks; ≤1,500 words, ≤10 images;
     formatting rules; the five report sections with suggested word counts; the mark allocation;
     authentication; submission to the teacher by 12 March 2027); the six stages (getting
     started; developing a question; project plan; sources and data; analysis and evaluation;
     applying learning and conclusions); what high achievement looks like for each descriptor;
     the 2027 topic (a digital work practice and its impact on employers or employees) with
     links to ch14-s5 and ch15-s2. Guidance only: never write a student's report.
   - SimpleStudy: Assessment: Investigative Study.

### ch2 — Forms of Business, Business Regulation and Governance [1.2]

Glossary: not-for-profit enterprises; Environmental, Social and Governance (ESG) factors.

1. **Public, private, semi-state and not-for-profit enterprises** [1.2.1]
   - Syllabus: distinguish between public, private and not-for-profit enterprises (the "learn
     about" adds semi-state) and analyse the contribution of each locally and nationally.
   - Cover: definitions and aims of each type; examples *(verify)*: government departments,
     local authorities, HSE; commercial semi-state bodies; private firms; charities, social
     enterprises and NGOs (glossary); each type's contribution (jobs, services, infrastructure,
     community, social goals) locally and nationally; how they are funded and held to account.
   - SimpleStudy: Forms of Business.
2. **Forms of ownership and how ownership changes** [1.2.2]
   - Syllabus: the nature of business ownership and how it may evolve over the lifecycle of a
     business, including nationalisation and privatisation; sole traders, partnerships, private
     limited companies, public listed companies, franchises, co-operatives and public sector
     organisations; outline how ownership differs and how it can change.
   - Cover: for each of the seven forms: ownership, liability (limited vs unlimited), control,
     finance, legal formation (Companies Act 2014 and the CRO *(verify)*), profit distribution,
     advantages and disadvantages, an Irish example; the typical path from sole trader to
     company to PLC (flotation); nationalisation and privatisation defined, with reasons, effects
     and Irish examples *(verify)*.
   - Exam: S1 Q3(b)(ii) fill-in: selling off state-owned enterprises is privatisation.
   - SimpleStudy: Forms of Business.
3. **Regulation, governance and ESG** [1.2.3–1.2.5]
   - Syllabus: how organisations are regulated internally and externally, including audit, risk
     management and compliance; outline the purpose of regulation; explain governance; outline
     the three factors in an ESG report.
   - Cover: purpose of regulation (protect stakeholders, fair competition, safety, trust);
     internal regulation (board and directors' duties, internal audit, risk management,
     compliance function, codes of conduct); external regulation (statutory external audit,
     regulators such as the Central Bank, CCPC, Corporate Enforcement Authority, Revenue, HSA,
     EPA, Data Protection Commission *(verify)*); corporate governance (definition,
     accountability, transparency, board structure); ESG — environmental, social and governance
     pillars with examples of each, why reporting matters, and the EU Corporate Sustainability
     Reporting Directive as transposed in Ireland in 2024 *(verify)*.
   - Exam: S1 Q3(a) identify the three elements of an ESG report.
   - SimpleStudy: Business Regulation and Governance.

### ch3 — Business and the Economy [1.3]

1. **Economic indicators and their impact on business** [1.3.1]
   - Syllabus: the relevance of inflation, employment rates, interest rates, economic growth and
     development, exchange rates and consumer confidence for business development and growth;
     explain how they impact on business.
   - Cover: each indicator defined, how it is measured in Ireland (CSO consumer price index,
     labour force survey, GDP, GNP and modified GNI*) *(verify)*, who sets it where relevant (the
     ECB sets euro-area interest rates), and how rises and falls affect costs, demand, borrowing,
     exports and expansion decisions; growth vs development; reading an indicator from a graph.
   - Exam: S1 Q2(d) explain the impact of three economic indicators on business growth; S1
     Q3(b)(v) interest rates in Ireland are set by the ECB; S2 Q5(c)(i) explain the indicator
     shown in an infographic.
   - SimpleStudy: Key Economic Indicators.
2. **The value of the business economy in Ireland** [1.3.2]
   - Syllabus: the value of the business economy in Ireland, including turnover and employment
     patterns; outline it.
   - Cover: what the "business economy" means in CSO statistics; headline figures for number of
     enterprises, turnover, GVA and persons employed; SMEs vs large firms; Irish-owned vs
     foreign-owned shares; sector and regional patterns; recent trends *(verify all figures from
     the latest CSO "Business in Ireland" release)*; what the patterns mean for Irish business
     (dependence on a few large foreign firms, SME employment).
   - SimpleStudy: Key Economic Indicators.

### ch4 — The Influence of National and EU Policy [1.4]

Glossary: Irish government policy; sector of the economy (in Ireland).

1. **Irish government policy, legislation and how business influences policy** [1.4.1–1.4.3]
   - Syllabus: how Irish government policy impacts across different sectors, how policy and
     legislation differ, and how business stakeholders inform and influence policy (interest
     groups and lobbying); outline three government policies that affect three different
     sectors; explain the difference between policy and legislation; outline business's role in
     national policy.
   - Cover: policy vs legislation (statement of intent vs law passed by the Oireachtas); the CSO
     sectors (glossary); at least four well-documented policies, each tied to a sector, with
     their aims and effects on business *(verify)* — e.g. the Climate Action Plan (energy,
     transport, agriculture), Housing for All (construction), the National Development Plan,
     Food Vision 2030 (agri-food), tourism or digital strategies; how business influences
     policy: representative bodies (IBEC, ISME, Chambers Ireland, sector bodies), trade unions,
     consultations and submissions, social dialogue, pre-Budget submissions, lobbying and the
     Regulation of Lobbying Act 2015 and its register *(verify)*.
   - Exam: S1 Q3(b)(i) fill-in: interest groups engage in lobbying.
   - SimpleStudy: National Policy and Business.
2. **EU decision-makers and types of EU law** [1.4.4, 1.4.5]
   - Syllabus: the key actors in EU policy development (the Council of the European Union, the
     European Commission, the European Parliament and the European Central Bank); the difference
     between EU regulations, directives and opinions based on how the Irish government must
     respond; identify the decision-makers; distinguish the three.
   - Cover: each institution's membership, role and powers; the ordinary legislative procedure
     (Commission proposes; Parliament and Council adopt); the ECB's monetary-policy role;
     regulation (binding, directly applicable, no national law needed), directive (binding as to
     result; transposed by Act or statutory instrument by a deadline), opinion (not binding);
     recommendations and decisions as assumed knowledge.
   - SimpleStudy: The European Union.
3. **Evaluating one EU regulation and one EU directive** [1.4.6]
   - Syllabus: how the EU affects business in Ireland, focusing on a directive's or regulation's
     purpose, how it has been implemented in Ireland, its positive and negative impact on
     different stakeholders, and whether it fosters ethical and sustainable practice and/or the
     use of technology; evaluate one regulation and one directive of the student's choice
     (different from the legislation used in 4.1 and 4.3).
   - Cover: write at least two complete options for each so students can choose, each with
     purpose, Irish implementation, positive and negative impacts on named stakeholders, and an
     ethics/sustainability/technology verdict *(verify all details)*. Candidate regulations: the
     Digital Services Act (Coimisiún na Meán as Ireland's coordinator); the AI Act. Candidate
     directives: the Corporate Sustainability Reporting Directive (links ESG, ch2-s3); the
     Single-Use Plastics Directive. Avoid GDPR (used in ch17) and employment directives such as
     Work-Life Balance or Platform Work (used in ch19).
   - Exam: S1 Q5(c) name an EU regulation, explain its Irish implementation, and examine two
     positive and two negative impacts on stakeholders; S2 Q5(d) name an EU directive, explain
     its purpose and evaluate its impact on business in Ireland.
   - SimpleStudy: The European Union.

### ch5 — Irish Business Globally and Internationally [1.5; 1.6]

Glossary: international trade (including trade on the island of Ireland between Ireland and
Northern Ireland); globalisation; interdependence; human capital.

1. **Trading blocs and Ireland's membership of the EU** [1.5.1–1.5.3]
   - Syllabus: the importance of trading blocs for Irish businesses, Ireland's EU membership and
     its impact on the economy, businesses and consumers; explain a trading bloc; identify the
     blocs most relevant to Irish business; evaluate EU membership from the perspective of the
     economy, businesses and consumers.
   - Cover: definition and types (free-trade area, customs union, single market); the blocs most
     relevant to Ireland *(verify)*: the EU single market and customs union, USMCA, Mercosur
     (EU–Mercosur agreement), ASEAN, EFTA/EEA; the UK after Brexit and all-island trade under the
     Windsor Framework; EU membership evaluated: benefits (market access, the euro, funding,
     FDI, consumer rights) and costs (loss of national control over some policy, regulation,
     competition, contributions) for each of the three perspectives.
   - Exam: S2 Q4(b) explain a trading bloc; identify one relevant bloc other than the EU and
     Mercosur; S1 Q3(b)(iii) fill-in "trading bloc".
   - SimpleStudy: International Business; The European Union.
2. **Trading internationally, and the balance of payments** [1.5.4–1.5.6]
   - Syllabus: why organisations based in Ireland expand internationally and the factors to
     consider (taxes and tariffs, costs, exchange rates, regulation, competition,
     language/culture); explain why Irish businesses trade globally with reference to Ireland's
     open economy; compare benefits and challenges; distinguish balance of payments and balance
     of trade and calculate both from given figures.
   - Cover: Ireland as a small open economy (small home market, export dependence); reasons to
     trade internationally (growth, economies of scale, spreading risk, access to inputs); each
     named factor explained; benefits vs challenges; methods of entering markets as assumed
     knowledge (exporting, agents, licensing, joint ventures, direct investment); balance of
     trade (visible exports minus visible imports) vs balance of payments (current account —
     goods, services, income — plus capital and financial accounts); surplus and deficit; worked
     calculations of both; Ireland's recent position *(verify)*.
   - Exam: S1 Q2(c) three factors before entering an international market; S1 Q3(b)(iv) and S2
     Q2(a)(i) fill-ins on the balance of trade.
   - SimpleStudy: International Business; Internationalisation and Globalisation.
3. **Globalisation, interdependence and technology** [1.5.7–1.5.9]
   - Syllabus: the social and environmental consequences of globalisation, including political
     risks, financial risks and cultural barriers; evaluate the impact of Irish organisations
     trading internationally (positive and negative, social and environmental); explain how
     globalisation increases interdependence and evaluate the consequences for businesses and
     consumers; the role of technology in globalisation (trade, work practices, how the business
     operates); evaluate it.
   - Cover: the glossary definitions; drivers of globalisation; positive effects (jobs, choice,
     lower prices, growth) and negative ones (job relocation, exploitation, carbon emissions and
     transport, cultural homogenisation); political, financial and cultural risks; supply-chain
     interdependence with recent disruptions *(verify)*; global marketing (standardise vs
     adapt); technology's role (e-commerce, logistics, communications, remote global teams,
     data flows).
   - Exam: S2 Q2(d) three challenges for Irish consumers from the country's reliance on
     globalisation.
   - SimpleStudy: Internationalisation and Globalisation.
4. **Foreign direct investment** [1.5.10, 1.5.11; 1.6.1]
   - Syllabus: the concept of FDI and how Ireland attracts it (human capital development,
     pro-enterprise policy, access to markets, research); its opportunities and challenges for
     Ireland in employment, revenue, research, infrastructure and innovation; explain FDI,
     investigate how the government promotes it, outline its contribution. Analyse business news
     and give an informed opinion [1.6].
   - Cover: definition; IDA Ireland's role; why firms locate in Ireland (each of the four named
     factors, plus the corporation tax regime and the OECD minimum-tax change *(verify)*,
     English language, EU access, clusters); opportunities (jobs, tax revenue, R&D, skills
     transfer, supplier linkages, regional development) and challenges (dependence and
     concentration of tax receipts, footloose investment, pressure on housing and
     infrastructure, profit repatriation, effect on Irish SMEs); one or two current FDI news
     stories *(verify)*.
   - Exam: S1 Q4(a)(i) two reasons a firm would locate in Ireland; S1 Q4(b) two opportunities
     and two challenges of FDI.
   - SimpleStudy: International Business.

### ch13 — Leading and Managing an Organisation [3.1; 3.5]

1. **Leadership, management, organisational culture and leadership styles** [3.1.1–3.1.3;
   3.5.1]
   - Syllabus: the role of leaders and managers; the significance of organisational culture and
     applying innovative approaches; how leadership styles influence organisations; distinguish
     leadership from management; analyse culture and innovation in successful organisations;
     outline how leadership styles foster culture and innovation. Analyse news about leadership.
   - Cover: leadership vs management (vision vs execution; influence vs authority; change vs
     stability) with at least five differences; roles of leaders and of managers; organisational
     culture (values, norms, behaviours) and what shapes it; how culture drives innovation and
     success, with Irish examples *(verify)*; leadership styles — autocratic, democratic,
     laissez-faire, transformational, servant, transactional — with how each affects culture and
     innovation and when each suits; one or two current leadership news stories *(verify)*.
   - Exam: S2 Q4(d) outline how a leadership style fosters innovation; examine three differences
     between leadership and management. S1 Q1(c) analyse three ways culture contributed to a
     firm's success.
   - SimpleStudy: Leading and Managing an Organisation.
2. **Conflict in the workplace and its resolution** [3.1.4–3.1.6]
   - Syllabus: why conflict arises in the workplace and how it affects the workplace; different
     approaches to resolution; conciliation and arbitration as external approaches; analyse how
     employees and employers deal with conflict internally; outline external approaches.
   - Cover: causes (pay and conditions, workload, change, poor communication, personality clashes,
     discrimination, unclear roles); effects (positive: new ideas; negative: absenteeism, low
     morale, strikes); internal approaches (grievance and disciplinary procedures, negotiation,
     collective bargaining, the shop steward, HR, internal mediation); external approaches
     (conciliation — a third party helps the sides agree but imposes nothing; mediation;
     arbitration — a third party decides; adjudication) through the Workplace Relations
     Commission and the Labour Court *(verify)*; types of industrial action as assumed knowledge.
   - Exam: S1 Q4(a)(ii) true/false: conciliation is a process where a third party issues a
     recommendation (false); S2 Q2(a)(v) fill-in: shop steward.
   - SimpleStudy: Leading and Managing an Organisation; Employee Governance.

### ch14 — Leading and Managing People [3.2]

Glossary: human capital; corporate wellness.

1. **Workforce planning, recruitment and selection** [3.2.1–3.2.3]
   - Syllabus: internal and external factors affecting workforce planning; the key stages in
     recruitment — identification, application and selection; the significance of ethics,
     including equality, diversity and inclusion; how digital developments change recruitment
     and selection; evaluate them.
   - Cover: workforce planning (definition; internal factors such as growth, turnover,
     retirements, skills; external factors such as the labour market, legislation, technology,
     economy); recruitment stages (identifying the vacancy, job description, person
     specification, internal vs external recruitment, advertising, applications and CVs,
     shortlisting, interviews and tests, references, offer, contract); ethical and EDI-based
     recruitment (non-discriminatory adverts and interviews, the nine grounds from ch19,
     reasonable accommodation, blind shortlisting); digital recruitment (online job boards,
     LinkedIn, applicant tracking and AI screening, video interviews, gamified tests), evaluated:
     reach, speed and cost vs bias, privacy and exclusion.
   - Exam: S1 Q4(c) evaluate how digital technologies influence recruitment and selection.
   - SimpleStudy: Leading and Managing People; Human Capital Management.
2. **Motivation and appraisal** [3.2.4–3.2.6]
   - Syllabus: motivation and the importance of appraisal; how organisations may use different
     approaches to appraisal, including self-appraisal, formative and summative appraisal and the
     360-degree approach, to review performance and motivate employees; investigate the factors
     that affect motivation; describe effective appraisal; analyse how the approaches contribute
     to motivation.
   - Cover: financial motivators (pay, bonuses, profit-sharing, share schemes, benefits) and
     non-financial (recognition, responsibility, job enrichment and rotation, flexible work,
     teamwork, culture, career progression, wellbeing); intrinsic vs extrinsic; what effective
     appraisal involves (clear criteria, regular, two-way, fair, linked to development) and its
     purposes; each named approach defined, with strengths, weaknesses and its effect on
     motivation; risks of poor appraisal.
   - Exam: S2 Q2(b) explain two ways to ensure an effective appraisal process.
   - SimpleStudy: Leading and Managing People.
3. **Human capital management, induction, training and development** [3.2.7, 3.2.8]
   - Syllabus: the significance of human capital management, induction, training and
     professional development for organisations and employees, and how employees learn from
     experience; explain HCM and how the organisational environment affects it; investigate the
     types of training and development and why ongoing development matters.
   - Cover: human capital (glossary) and HCM; the organisational environment's role (culture,
     leadership, resources, learning climate); induction ("onboarding") and its purpose; on-the-
     job vs off-the-job training, mentoring, coaching, job rotation, e-learning, further
     education, CPD; benefits for employer and employee; learning from experience (reflection,
     feedback).
   - Exam: S1 Q4(a)(ii) true/false: induction training is also known as onboarding (true).
   - SimpleStudy: Human Capital Management.
4. **Teamwork and sustainable workplaces** [3.2.9, 3.2.10]
   - Syllabus: teamwork and how collaboration affects the employee and the organisation; the
     opportunities and challenges of teams for employees and employers; how employers and
     employees can contribute to more sustainable workplaces.
   - Cover: what makes an effective team; stages of team development as assumed knowledge;
     opportunities (skills sharing, creativity, motivation, productivity) and challenges
     (conflict, free-riding, groupthink, slower decisions) for each side; a sustainable
     workplace (environmental and social): energy and waste reduction, sustainable travel, green
     procurement, hybrid work's footprint, green teams, fair work; what each side contributes.
   - SimpleStudy: Leading and Managing People.
5. **Digital technology in the workplace: remote and blended working** [3.2.11–3.2.13]
   - Syllabus: the disruptive impact of digital technology, focusing on how diverse ways of
     working, including remote and blended work, affect employers, employees and the world of
     work; investigate digital technology's impact on the workplace; identify the opportunities
     and challenges of remote and blended work for both sides; analyse the associated ethical and
     sustainability issues.
   - Cover: digital technologies changing work (collaboration platforms, cloud, automation and
     AI, monitoring software); remote vs blended (hybrid) work defined; opportunities and
     challenges for employers (talent pool, office costs, productivity; supervision, culture,
     security) and employees (flexibility, commuting, work-life balance; isolation, always-on,
     career visibility); the right to request remote work under the Work Life Balance Act 2023
     and the WRC code of practice *(verify)*; ethical issues (surveillance, fairness, the right
     to disconnect) and sustainability issues (fewer commutes vs home energy use; regional
     development). **This is the 2027 AAC brief's topic.**
   - Exam: S1 Q1(b) identify three challenges of a firm's four-day week and blended working; S2
     Q2(e) evaluate how digital technologies have affected the modern workplace.
   - SimpleStudy: Human Capital Management.
6. **Corporate wellness and the leader's role** [3.2.14, 3.2.15]
   - Syllabus: the importance of maintaining a focus on wellbeing in the workplace and the key
     role of the leader; outline corporate wellness and investigate its impact on motivation and
     culture; identify the role of leadership in promoting it.
   - Cover: corporate wellness (glossary: equality, diversity, inclusivity and overall wellbeing);
     typical initiatives (employee assistance programmes, mental-health supports, flexible work,
     health promotion, EDI policies, physical-activity schemes); impact on motivation, retention,
     absenteeism and culture; the leader's role (modelling, resourcing, policy, psychological
     safety); limits (tokenism, cost).
   - Exam: S1 Q4(d) discuss four ways motivation can be influenced by corporate wellness
     initiatives.
   - SimpleStudy: Human Capital Management.

### ch15 — The Importance of Communication [3.3]

1. **Why communication matters and how to improve it** [3.3.1, 3.3.4]
   - Syllabus: the significance of effective communication in an organisation, including
     supporting collaboration, avoiding conflict, increasing engagement, promoting positive
     culture, managing change and promoting innovation; how to improve communication, including
     setting clear goals, listening actively, ensuring ongoing engagement and choosing the
     correct mode; explain and discuss both.
   - Cover: each of the six named purposes, explained with a workplace example; barriers to
     effective communication as assumed knowledge (jargon, information overload, poor
     listening, wrong medium, culture and language, hierarchy, timing); each named improvement
     plus feedback and two-way channels.
   - Exam: S2 Q4(c) explain three reasons, apart from avoiding conflict, why communication
     matters; S2 Q5(a)(ii) two ways to improve communication apart from choosing the mode.
   - SimpleStudy: The Importance of Communication.
2. **Modes of communication and the impact of technology** [3.3.2, 3.3.3]
   - Syllabus: the parameters around different modes (verbal and non-verbal) and the impact of
     technology on communication (modes, speed, cost, access, collaboration, sustainable
     practices, productivity and security); identify modes and analyse their efficacy; discuss
     how technology enables communication.
   - Cover: verbal (face-to-face, meetings, phone, video call) and non-verbal (body language)
     communication, written and visual modes; criteria for choosing a mode (urgency, cost,
     confidentiality, audience, need for a record, complexity, feedback); efficacy analysis of
     each mode; technology's impact on each of the eight named parameters, positive and negative
     (e.g. security: phishing and data breaches).
   - Exam: S2 Q5(a)(i) outline two considerations when choosing a mode of communication.
   - SimpleStudy: The Importance of Communication.

### ch18 — Making Informed Financial Decisions [4.2]

Glossary: fintech; Central Bank Digital Currency (CBDC).

1. **Saving, investing and borrowing** [4.2.1]
   - Syllabus: informed decision-making about saving and investing, considering inflation, risk,
     interest rates, taxes and charges, the time frame (short, medium, long term) and return on
     investment; examine the factors in saving, investing and borrowing.
   - Cover: saving vs investing vs borrowing; each named factor explained; real vs nominal
     return; AER and APR as assumed knowledge; DIRT and other taxes on returns *(verify)*;
     common products (deposit accounts, state savings, shares, funds, pensions; overdrafts,
     credit cards, personal loans, mortgages, buy-now-pay-later, credit-union loans); a worked
     comparison of two loans or two savings options.
   - Exam: S2 Q2(c) explain three factors a consumer should consider before borrowing.
   - SimpleStudy: Making Informed Financial Decisions.
2. **Risk tolerance, reliable information, switching providers and credit ratings** [4.2.2,
   4.2.3, 4.2.5]
   - Syllabus: analysing risks when acquiring financial products and why consumers should
     consider switching providers; explain risk tolerance and the risks facing consumers of
     financial products, and how to find reliable financial information; outline the importance
     of switching; how a credit rating is established, what affects it, and the consequences of
     a poor rating, which travels with a person over time.
   - Cover: risk tolerance; risks (losing capital, inflation, interest-rate changes, mis-selling,
     hidden charges, over-indebtedness); reliable sources (CCPC money tools, Central Bank,
     MABS, regulated advisers) vs unreliable ones (unregulated "finfluencers"); switching
     (savings, lower charges, better rates; the process; barriers); the Central Credit Register
     and credit bureaus, what is recorded, how long *(verify)*; factors that affect the rating
     (repayment history, arrears, level of debt, applications, judgments); consequences
     (refusals, higher interest).
   - Exam: S1 Q3(c) outline three factors that can affect a person's credit rating.
   - SimpleStudy: Making Informed Financial Decisions.
3. **Fintech, Central Bank Digital Currency and crypto-assets** [4.2.4, 4.2.8]
   - Syllabus: the opportunities and challenges of fintech for consumers; explain how technology
     affects the provision of financial products; the advantages and disadvantages of CBDC as an
     electronic equivalent of cash, and how it differs from stablecoins and crypto-assets;
     describe CBDC and examine the potential impact of digital currency on consumers and
     businesses.
   - Cover: fintech (glossary) and examples (mobile banking, payment apps, neobanks, robo-
     advisers, open banking, BNPL); benefits and challenges for consumers; CBDC per the glossary
     (central-bank money in digital form, complementing cash) and the ECB's digital euro project
     *(verify status)*; stablecoins (value depends on the issuer's pledge) and crypto-assets (no
     liable issuer); a comparison table; impacts on consumers and businesses (cost, speed,
     inclusion; privacy, cyber risk, bank disintermediation); crypto risks and EU MiCA
     regulation *(verify)*.
   - Exam: S2 Q3(c) describe two differences between CBDC and crypto-assets; explain one impact
     of digital currency on consumers and on businesses.
   - SimpleStudy: Making Informed Financial Decisions; Financial Regulation.
4. **Regulation of financial services and financial fraud** [4.2.6, 4.2.7, 4.2.9]
   - Syllabus: regulation of the financial products market by the Irish government and the EU, and
     managing risk, including pensions, mortgages, credit-based products and crypto-finance;
     investigate how the industry is regulated and discuss the consequences of under-regulation;
     outline financial fraud and how consumers can protect themselves; discuss finance stories
     in the news.
   - Cover: the Central Bank of Ireland's roles (consumer protection code, prudential
     supervision, mortgage measures) *(verify)*; the Financial Services and Pensions Ombudsman;
     the deposit guarantee scheme; EU supervisors (ECB banking supervision, EBA, ESMA) and EU
     rules; risk in pensions, mortgages, credit products and crypto; consequences of
     under-regulation (the 2008 banking crisis, tracker-mortgage scandal *(verify)*);
     fraud types (phishing, smishing, vishing, investment scams, identity theft, money muling,
     card fraud) and protections; one or two current finance news stories *(verify)*.
   - SimpleStudy: Financial Regulation.

### ch19 — Being an Informed Employee [4.3]

Glossary: gig economy. Footnote 3 of the specification: use current employment legislation.

1. **Employee rights and responsibilities: legislative and non-legislative protection** [4.3.1,
   4.3.2]
   - Syllabus: the rights and responsibilities of employees in legislation (pay, conditions,
     health and safety, discrimination, security of employment and dismissal) and how employees
     have both legislative and non-legislative protection; examine both; investigate how current
     employment legislation sets out the rights and responsibilities of employees and employers.
   - Cover *(verify every Act and figure)*: pay (National Minimum Wage Act 2000 and current
     rate; Payment of Wages Act 1991); conditions (Organisation of Working Time Act 1997,
     Terms of Employment (Information) Acts, Employment (Miscellaneous Provisions) Act 2018,
     Sick Leave Act 2022, Work Life Balance and Miscellaneous Provisions Act 2023); health and
     safety (Safety, Health and Welfare at Work Act 2005; employer and employee duties; the HSA);
     discrimination (Employment Equality Acts 1998–2015: the nine grounds — gender, civil
     status, family status, sexual orientation, religion, age, disability, race, membership of
     the Traveller community); security of employment and dismissal (Unfair Dismissals Acts:
     fair and unfair grounds, constructive dismissal, redress); redress through the WRC and the
     Labour Court; employees' responsibilities; non-legislative protection (contracts,
     collective agreements, trade unions, HR policies, codes of practice, grievance procedures).
   - Exam: S2 Q4(a) list three grounds, apart from gender, on which discrimination is illegal.
   - SimpleStudy: Employee Protections; Employee Governance.
2. **Trade unions and the gig economy** [4.3.3, 4.3.4]
   - Syllabus: the function of trade unions in supporting employees; describe their role; the
     impact on workers of on-demand, freelance jobs paid "per piece"; discuss the gig economy and
     its opportunities and challenges for workers.
   - Cover: what a trade union is and its functions (collective bargaining, representation,
     advice, protecting jobs, lobbying); the shop steward; ICTU; types of union as assumed
     knowledge; the gig economy (glossary) with examples (delivery, ride-hailing, freelance
     platforms); opportunities (flexibility, extra income, entry to work) and challenges
     (insecure income, no sick pay or pension, employment-status disputes, algorithmic
     management); the EU Platform Work Directive and Irish developments *(verify)*.
   - Exam: S1 Q5(a) explain the gig economy and identify three challenges for gig workers.
   - SimpleStudy: Employee Governance.
3. **The annual Budget and workers; informed decisions as an employee** [4.3.5, 4.3.6]
   - Syllabus: how government decisions affect people in employment; investigate how the annual
     Budget affects workers; appreciate informed decisions as an employee and discuss workplace
     news.
   - Cover: what the Budget is and when it happens; measures that affect workers *(verify against
     the latest Budget)*: income tax bands and credits, USC, PRSI, minimum-wage decisions, social
     welfare and childcare supports, housing supports, auto-enrolment pensions, cost-of-living
     measures; reading a simple payslip (gross pay, deductions, net pay) as assumed knowledge;
     one or two current workplace news stories *(verify)*.
   - SimpleStudy: Employee Protections.

---

## Appendix C — Coverage check

Every section and learning outcome of the specification has a home:

| Spec section | Outcomes | Subsection(s) |
|---|---|---|
| U1 Developing questions to research | 1 | ch0-s1 |
| U2 Managing information | 6 | ch0-s1 |
| U3 Project planning | 3 | ch0-s2 |
| U4 Analysing and evaluating information | 5 | ch0-s3 |
| U5 Presenting findings and perspectives | 4 | ch0-s3 |
| U6 Acknowledging sources | 1 | ch0-s1 |
| 1.1 Key stakeholders | 4 | ch1-s1, s2, s3 |
| 1.2 Forms of business, regulation, governance | 5 | ch2-s1, s2, s3 |
| 1.3 Business and the economy | 2 | ch3-s1, s2 |
| 1.4 National and EU policy | 6 | ch4-s1, s2, s3 |
| 1.5 Irish business globally | 11 | ch5-s1 to s4 |
| 1.6 Applying my learning | 1 | ch5-s4, and news examples throughout |
| 2.1 Enterprise in its broadest sense | 3 | ch6-s1, s2 |
| 2.2 Idea development | 3 | ch7-s1, s2, s3 |
| 2.3 Business planning | 7 | ch8-s1 to s4 |
| 2.4 The target market | 8 | ch9-s1 to s5 |
| 2.5 Operations and finance | 3 | ch10-s1 to s4 |
| 2.6 Growth, development and expansion | 6 | ch11-s1 to s4 |
| 2.7 Managing risk | 3 | ch12-s1, s2 |
| 2.8 Applying my learning | 1 | ch6-s1 |
| 3.1 Leading and managing an organisation | 6 | ch13-s1, s2 |
| 3.2 Leading and managing people | 15 | ch14-s1 to s6 |
| 3.3 The importance of communication | 4 | ch15-s1, s2 |
| 3.4 The rationale for planning | 9 | ch16-s1, s2, s3 |
| 3.5 Applying my learning | 1 | ch13-s1 |
| 4.1 Making informed decisions as a consumer | 5 | ch17-s1, s2, s3 |
| 4.2 Making informed financial decisions | 9 | ch18-s1 to s4 |
| 4.3 Being an informed employee | 6 | ch19-s1, s2, s3 |
| **Total** | **138** | **66 subsections: 33 in the original chapters + 33 in the added ones** |

Outcomes in the original 10 chapters: 52 of 138 (sections 1.1, 2.1–2.8, 3.4, 4.1).
Outcomes in the 10 added chapters: 86 of 138 (the Unifying Strand, 1.2–1.6, 3.1–3.3, 3.5,
4.2, 4.3).

## Appendix D — SimpleStudy structure as recorded (2026-08-07)

From `pipeline/resources/business/guide-simplestudy.md`; 22 units, 35 topics.

1. Investigating Business — Developing Questions to Research; Managing Information; Project
   Planning; Analysing and Evaluating Information; Presenting Findings and Perspectives
2. People in Business — Key Stakeholders in Business
3. Conflict Resolution: The Consumer — Consumer Rights; Making Informed Consumer Decisions
4. Conflict Resolution: Industrial Relations — Employee Protections; Employee Governance
5. Enterprise — Enterprise
6. Management Skills: Leading and Motivating — Leading and Managing an Organisation; Leading and
   Managing People
7. Management Skills: Communication — The Importance of Communication
8. Management Activities: Planning, Organising and Controlling — The Rationale for Planning;
   Force Field Analysis and Strategic Planning
9. Sources of Finance and Cash Flow Management — Operations and Finance; Making Informed
   Financial Decisions; Financial Regulation
10. Insurance and Managing Risk — Risk Management and Insurance
11. Human Capital Management — Human Capital Management
12. Identifying Business Opportunities — Idea Development
13. Getting Started in Business — Business Planning
14. Market Research and Market Segmentation — Market Research and Market Analysis
15. Marketing Mix — The Marketing Mix
16. Business Expansion — Growth, Development, and Expansion
17. Ownership Structures — Forms of Business; Business Regulation and Governance
18. Business, Government and the Economy — Key Economic Indicators; National Policy and Business
19. International Trade — International Business
20. The European Union — The European Union
21. Global Business — Internationalisation and Globalisation
22. Assessment — Investigative Study; Written Exam
