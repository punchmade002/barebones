# Leaving Cert Business (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format
  and a worked example). This outline says what to cover; that file says how to write it.
- **The specification:** the NCCA *Curriculum Specification for Leaving Certificate Business*,
  for introduction to schools in September 2025, published August 2024. It is first examined in
  **June 2027**, so it is the course the app's students sit. The official PDF is
  `pipeline/resources/business/spec-syllabus.pdf` (also in `relevant-resources/syllabi/business.pdf`),
  downloaded from curriculumonline.ie on 2026-10-19. The curriculumonline.ie Business page labels
  it "LC Business Specification (for introduction in September 2025)".
- **Do not use the old 1997 syllabus** (curriculumonline.ie: "LC Business Syllabus (for examination
  to June 2026)", © 1996, seven units: People in Business, Enterprise, Managing 1 and 2, Business
  in Action, Domestic Environment, International Environment). It is a different course and is no
  longer examined. Pre-2027 past papers, older textbooks and most online notes follow it. Appendix
  A lists the old-syllabus topics the specification dropped; leave them out.
- **References** in brackets are the specification's own numbering: **[S1.4 LO5]** means Strand 1,
  section 4 ("The influence of national and EU policy"), learning outcome 5 in the "Students
  should be able to" column. **[U2]** is section 2 of the Unifying Strand.
- **Chapters** are the app's 10 business chapter IDs (`data.js`; there is no
  `pipeline/scaffold/business.json`). Keep every ID exactly as written. Nine specification sections
  and the whole Unifying Strand have **no chapter yet**. Their outlines are in **Appendix B**,
  with proposed IDs. They are not app chapters until the user approves them.
- **What each subsection contains:**
  - **Syllabus**: what the specification says students learn about and should be able to do,
    close to its own wording. This is the required scope, and every item must be covered. Lists
    introduced by "including" are required content, not examples.
  - **Glossary**: the specification's Appendix 2 definition for terms it marks with an asterisk.
    Notes must teach the term consistently with this definition.
  - **App slot**: the existing `learningOutcomes` entry in `data.js` the notes belong in. "New
    slot" means the subsection has no entry yet.
  - **SimpleStudy**: the matching topic(s) in SimpleStudy's Higher Level course (recorded
    2026-08-07, `pipeline/resources/business/guide-simplestudy.md`). Use for structure and pacing
    only; write all prose in your own words.
- **Settings:** unlike the geography syllabus, the specification gives no example businesses or
  places. Notes must still use specific, real, named examples, preferably Irish (NOTES_STANDARD
  rule 7). Where the specification says "current legislation", use the law in force when the
  notes are written, and never invent figures.
- **Higher vs Ordinary level:** the specification marks **no** learning outcome as Higher Level
  only. Both levels study all content; Higher Level expects "knowledge of significant complexity",
  creative and critical analysis, evaluation, and application to unfamiliar problems (Table 1).
  The old syllabus's "(HL)" outcomes don't apply.
- **Where the specification sets a choice, write content for several options,** so students can
  pick:
  - three Irish government policies affecting three different sectors [S1.4 LO1]
  - one EU regulation and one EU directive of the student's choice [S1.4 LO6]. Footnote 1: these
    must be **different from any legislation explored in Strand 4 sections 1 and 3**, so GDPR
    (used in [S4.1 LO4]) and the consumer and employment laws there can't be used
  - a marketing mix with a USP analysis for a product **and** a service of choice [S2.4 LO3]
- **Cross-cutting themes** run through every strand, and the written exam assesses applying them:
  **ethics and sustainability, entrepreneurial thinking, business and financial literacy,
  digital transformation** (including digitalisation, AI and big data). Notes should bring them
  in wherever the learning outcome does.
- **"Applying my learning"** sections close each strand: analyse business news and give an
  informed opinion. The exam assesses "students' capacity to engage with the world of business
  and business in the media", so recent, named Irish business stories belong in the notes.
- **Assessment** (Table 2), both components set and marked by the SEC:
  - **Business Alive Investigative Study (AAC), 40%:** common brief at a common level, issued
    by the SEC in term two of fifth year. Up to 20 hours of work; a report submitted digitally
    in sixth year. Judged on the Descriptors of Quality: planning, investigating, applying and
    communicating. It applies the Unifying Strand to one or more contextual strands or
    cross-cutting themes.
  - **Written examination, 60%,** at Higher and Ordinary level. "A range of question types"
    assessing the four contextual strands, the Unifying Strand, the cross-cutting themes, and
    business in the media. Differentiation comes from the stimulus material and the amount of
    structured support. The app has no sample or past paper for this specification yet
    (`exam-breakdown.js`).
  - Grading uses H1–H8 / O1–O8 in 10% bands (H1 = 90–100).
- **Command words** follow the specification's Appendix 1 glossary of action verbs (e.g.
  outline = main points only; discuss = balanced review with evidence; evaluate = judgement
  supported by evidence, with limitations). Learning outcomes that say "calculate" [S1.5 LO6],
  "conduct" [S1.1 LO4, S2.4 LO8, S2.6 LO5] or "use" [S2.4 LO7, S2.6 LO2] need a worked method
  in the notes.

---

## Strand 1 — Exploring the Business Environment

Ireland as a small, open economy; forms of business; stakeholders; government, EU and
international influences on business. Sections 1.2–1.5 have no chapter yet (Appendix B: proposed
ch2–ch5).

### ch1 — Key Stakeholders in Business [S1.1, S1.6]
1. **Internal and external stakeholders and their importance** [S1.1 LO1]: key stakeholders
   (business owners, investors, employees, consumers, suppliers, local community, government);
   which are internal and which external; their importance in the business environment; their
   needs and wants at different stages of business development.
   - App slot: `lo1-1`.
   - SimpleStudy: Key Stakeholders in Business.
2. **How stakeholders interact and where conflict arises** [S1.1 LO2]: interdependencies
   between stakeholders; how they interact; potential conflicts between them.
   App slot: `lo1-2`.
3. **Avoiding and resolving stakeholder conflict** [S1.1 LO3]: appropriate ways to avoid and
   resolve conflict between stakeholders.
   App slot: `lo1-3`.
4. **Stakeholder mapping and prioritising interests** [S1.1 LO4]: conduct stakeholder mapping;
   explain why prioritising different stakeholder interests matters.
   - Glossary: stakeholder mapping considers the main stakeholders and their power and
     influence. It can be written or visual and should show the stakeholders, their
     interdependencies and inter-relationships, and their power and influence on decisions.
   - App slot: `lo1-4`.
5. **Applying my learning: the business environment in the news** [S1.6 LO1]: analyse news and
   media stories about the business environment and give an informed opinion or perspective.
   - App slot: new slot. If ch2–ch5 are approved, this could move to ch5.
   - SimpleStudy: none.

---

## Strand 2 — Understanding Enterprise

Enterprise and intrapreneurship, idea development, business planning and models, the target
market, operations and finance, growth, and risk.

### ch6 — Enterprise in Action [S2.1, S2.8]
1. **Enterprise, innovation, intrapreneurship and entrepreneurship** [S2.1 LO1]: the range of
   reasons for starting an enterprise; how enterprise and innovation are present in, and important
   for, government, society, business, the community and students' own lives; identify examples of
   innovation, intrapreneurship and entrepreneurship locally, nationally and internationally;
   explain the importance of innovation for business, the economy and society.
   - App slot: `lo6-1`.
   - SimpleStudy: Enterprise.
2. **Competencies of innovators** [S2.1 LO2]: the competencies that support innovation and
   enterprise development, and why they matter when starting a business.
   - Glossary: competencies (of entrepreneurs) are the integration of knowledge, skills, values
     and dispositions that support and foster innovation.
   - App slot: `lo6-2`.
3. **The government's role in fostering enterprise** [S2.1 LO3]: how the Irish government
   supports business and enterprise locally and nationally, and supports development and growth.
   App slot: `lo6-3`.
4. **Applying my learning: enterprise and innovation in the news** [S2.8 LO1]: analyse news and
   media stories about enterprise and innovation and give an informed opinion or perspective.
   App slot: new slot.

### ch7 — Idea Development [S2.2]
1. **How business ideas are developed** [S2.2 LO1]: determine the factors that affect the
   development of business ideas.
   - App slot: `lo7-1`.
   - SimpleStudy: Idea Development.
2. **Design thinking** [S2.2 LO2]: the four phases (**clarify, ideate, develop, implement**); design
   thinking as an innovative approach to idea development that is iterative and both solution-
   and person-centred.
   - Glossary: design thinking is an innovative, non-linear approach to developing products and
     services that focuses on solutions for the end user.
   - App slot: `lo7-2`.
3. **The feasibility study** [S2.2 LO3]: why evaluating a business idea with a feasibility study
   matters for judging the future viability of the business.
   App slot: `lo7-3`.

### ch8 — Business Planning [S2.3]
1. **The business plan and its functions** [S2.3 LO1]: why a coherent business plan matters at
   different stages of business development; how it supports start-up, operations, funding and
   development; the key functions of a business plan.
   - App slot: `lo8-1`.
   - SimpleStudy: Business Planning.
2. **Ethics and sustainability in business planning** [S2.3 LO2].
   App slot: `lo8-2`.
3. **What a business model is** [S2.3 LO3]: the role of business models in generating income
   and in creating, delivering and capturing value for both the enterprise and its customers; the
   business model's role within the business plan.
   - Glossary: a business model is an element within the business plan which outlines how a
     company will operate, create, deliver and capture value in economic, social and cultural
     contexts.
   - App slot: `lo8-3`.
4. **The business model canvas** [S2.3 LO4]: the key elements of the canvas; the role of business
   models in successful enterprises.
   - Glossary: the canvas includes the key partners, key activities and key resources; the value
     proposition (why the customer would choose the product or service); customers, customer
     relations and channels; costs; and revenues.
   - App slot: `lo8-4`.
5. **Common business models** [S2.3 LO5]: identify and compare **retail, manufacturing,
   subscription, franchise and affiliate** models.
   App slot: `lo8-5`.
6. **Digital technology as a driver of change** [S2.3 LO6]: how digital technology drives change in
   business; how businesses have adapted to, or developed from, the digital economy and other
   internal or external drivers.
   App slot: `lo8-6`.
7. **Technology-driven business models** [S2.3 LO7]: **marketplace, subscription, crowdfunding and
   advertising-supported** models: the key characteristics of each, and how they are similar to
   and different from non-digital models.
   App slot: `lo8-7`.

### ch9 — The Target Market [S2.4]
1. **Market research and the target market** [S2.4 LO1]: why identifying the target market
   matters; why market research matters in identifying it; how businesses conduct market research.
   - App slot: `lo9-1`.
   - SimpleStudy: Market Research and Market Analysis.
2. **The marketing mix** [S2.4 LO2]: the seven elements as the specification lists them:
   **product/service, pricing, promotion, people, packaging, process and place**. Explain each
   element's significance and how the target market influences it. The specification's seventh
   P is **packaging**, not "physical evidence".
   - App slot: `lo9-2`.
   - SimpleStudy: The Marketing Mix.
3. **USP and developing a marketing mix** [S2.4 LO3]: identifying the unique selling point;
   developing a marketing mix with a USP analysis for **a product and a service** of choice. This
   is a choice, so write worked mixes for at least two products and two services.
   App slot: `lo9-3`.
4. **Evaluating and improving a marketing mix** [S2.4 LO4]: modifying an existing marketing mix
   and suggesting improvements.
   App slot: `lo9-4`.
5. **Digital technology's disruptive impact on market research and marketing** [S2.4 LO5].
   - Glossary: disruptive impact describes how digital technology can change the way businesses
     operate (including in the workplace) and how consumers interact with business. It can be
     positive or negative.
   - App slot: `lo9-5`.
6. **Ethics and sustainability in marketing** [S2.4 LO6]: their influence on marketing, on
   marketing companies and on different marketing strategies.
   App slot: `lo9-6`.
7. **The power-interest grid** [S2.4 LO7]: use a power-interest grid to analyse customer interest
   and adjust the marketing mix as necessary.
   - Glossary: a form of stakeholder mapping. It considers stakeholders' motivations and their
     ability to exert positive or negative influence, and maps them by relative power and
     interest.
   - App slot: `lo9-7`.
8. **STEEPLE analysis** [S2.4 LO8]: conduct a STEEPLE analysis to understand the external
   environment and identify issues of concern for a business.
   - Glossary: social, technological, economic, environmental, political, legal and ethical
     factors.
   - App slot: `lo9-8`.

### ch10 — Operations and Finance [S2.5]
1. **The operational model** [S2.5 LO1]: the key partners, key activities and key resources of a
   business, and why they may change over time.
   - App slot: `lo10-1`.
   - SimpleStudy: Operations and Finance.
2. **Costs, revenue streams and sources of finance** [S2.5 LO2]: key costs (**variable and
   fixed**); potential revenue streams (**single transactions or recurring sales**); sources of
   finance; why these may change over the lifecycle of the product or service.
   - App slot: `lo10-2`.
   - SimpleStudy: Operations and Finance.
3. **Cashflow analysis** [S2.5 LO3]: analyse a business's cashflow and recommend a suitable
   course of action for the issues the analysis reveals. Include a worked cashflow example.
   App slot: `lo10-3`.

### ch11 — Growth, Development and Expansion [S2.6]
1. **Identifying competition** [S2.6 LO1]: why identifying potential competition and competitors
   matters; competitive advantage and how a business can capitalise on it.
   - App slot: `lo11-1`.
   - SimpleStudy: Growth, Development, and Expansion.
2. **Porter's five forces** [S2.6 LO2]: use the model to identify and analyse competition and
   find a business's competitive advantage.
   - Glossary: threat of new entrants, bargaining power of suppliers, bargaining power of
     customers, threat of substitutes, competitive rivalry.
   - App slot: `lo11-2`.
3. **Strategies to adapt or expand** [S2.6 LO3]: enterprise is not static; strategies a business
   uses to adapt or expand.
   App slot: `lo11-3`.
4. **Technology supporting adaptation and expansion** [S2.6 LO4].
   App slot: `lo11-4`.
5. **Cost-benefit analysis of expansion** [S2.6 LO5]: weigh potential benefits and costs when
   making business decisions; conduct a cost-benefit analysis of a business expansion. Include a
   worked example.
   App slot: `lo11-5`.
6. **Adapting to external drivers** [S2.6 LO6]: adapting to customer demographics, competition
   and economic factors to improve financial sustainability, through the product/service,
   pricing, promotion, people, packaging, process and place and/or the business model.
   App slot: `lo11-6`.

### ch12 — Managing Risk [S2.7]
1. **Challenges and risks of enterprise** [S2.7 LO1]: the nature of risk in entrepreneurship.
   - App slot: `lo12-1`.
   - SimpleStudy: Risk Management and Insurance.
2. **Why assessing and managing risk matters** [S2.7 LO2].
   App slot: `lo12-2`.
3. **Risk management strategies and insurance** [S2.7 LO3]: analyse risk management strategies,
   including **avoidance, spread and prevention**, and the importance of choosing suitable
   insurance products.
   App slot: `lo12-3`.

---

## Strand 3 — Leading in Business

Leadership and management, people, communication, and planning for change. Sections 3.1–3.3
have no chapter yet (Appendix B: proposed ch13–ch15).

### ch16 — The Rationale for Planning [S3.4, S3.5]
1. **Internal and external changes** [S3.4 LO1]: the changes organisations encounter through
   their lifetime.
   - App slot: `lo16-1`.
   - SimpleStudy: The Rationale for Planning.
2. **Resistance to change** [S3.4 LO2]: analyse why resistance to change arises in an
   organisation.
   App slot: `lo16-2`.
3. **Practices that promote innovation** [S3.4 LO3]: practices that foster innovation and
   entrepreneurial or intrapreneurial thinking.
   App slot: `lo16-3`.
4. **Overcoming resistance to change** [S3.4 LO4]: a range of approaches.
   App slot: `lo16-4`.
5. **Strategic planning** [S3.4 LO5]: what it is; why it is an ongoing process; how it supports
   leading and managing change.
   - App slot: `lo16-5`.
   - SimpleStudy: Force Field Analysis and Strategic Planning.
6. **Benefits of strategic planning** [S3.4 LO6].
   App slot: `lo16-6`.
7. **Planning for change and force-field analysis** [S3.4 LO7]: why planning for change matters;
   how a force-field analysis supports strategic planning for change and strategic decisions.
   Include a worked analysis.
   - Glossary: identifies and analyses the internal and external forces that drive and inhibit
     change.
   - App slot: `lo16-7`.
   - SimpleStudy: Force Field Analysis and Strategic Planning.
8. **Contingency planning and crisis management** [S3.4 LO8]: what contingency planning means for
   crisis management; crises may arise locally or nationally.
   App slot: `lo16-8`.
9. **Developing a contingency plan** [S3.4 LO9]: the factors to consider, including **cost, time
   and risk**.
   App slot: `lo16-9`.
10. **Applying my learning: leadership in the news** [S3.5 LO1]: analyse news and media stories
    about leadership in business and give an informed opinion or perspective.
    - App slot: new slot. If ch13 is approved, this could move there.
    - SimpleStudy: none.

---

## Strand 4 — Being Informed and Making Informed Decisions

Students as consumers, financial decision-makers and employees. Sections 4.2 and 4.3 have no
chapter yet (Appendix B: proposed ch18–ch19). Footnotes 2 and 3: students must engage with
**current** legislation. Where legislation changes during the two years, either the existing or
the newer law may be used.

### ch17 — Making Informed Decisions as a Consumer [S4.1]
1. **Consumer rights and responsibilities** [S4.1 LO1]: investigate consumers' rights and
   responsibilities using current consumer legislation, covering products, services, digital
   services and their promotion, and how rights change when buying from outside the EU.
   - App slot: `lo17-1`.
   - SimpleStudy: Consumer Rights.
2. **Ethical and sustainable consumer behaviour** [S4.1 LO2]: how ethics and sustainability can
   inform consumer behaviour; the consequences of taking part in the shadow economy for the
   consumer, the business and the economy; how consumers contribute to the circular economy.
   - Glossary: the **shadow economy** is business and economic transactions deemed illegal in a
     jurisdiction, because the goods or services are unlawful or the transaction breaks
     legislation or government reporting requirements. The **circular economy** is a model of
     production and consumption that extends product life cycles, reduces waste and creates
     further value.
   - App slot: `lo17-2`.
   - SimpleStudy: Making Informed Consumer Decisions.
3. **Digital technology and consumer behaviour** [S4.1 LO3]: positive and negative impacts on
   the consumer.
   App slot: `lo17-3`.
4. **Protecting personal data** [S4.1 LO4]: how European regulation (GDPR) protects personal
   data. Because GDPR is used here, it can't be the student's chosen EU regulation in [S1.4 LO6].
   App slot: `lo17-4`.
5. **Applying my learning: informed consumer decisions** [S4.1 LO5]: why informed consumer
   decisions matter; using this to discuss consumer stories in the news and media.
   App slot: `lo17-5`.

---

## Appendix A — Where the specification differs from SimpleStudy, the old syllabus and the repo

- **In the specification but missing from SimpleStudy's topic list:** acknowledging sources
  [U6] (SimpleStudy may fold it into "Managing Information"); all four "Applying my learning"
  sections [S1.6, S2.8, S3.5, and the news items in S4.1–S4.3]. SimpleStudy has no topic for
  balance of payments or balance of trade calculations [S1.5 LO6], CBDC and stablecoins
  [S4.2 LO8], the gig economy [S4.3 LO4] or the annual budget's effect on workers [S4.3 LO5],
  though its broader topics may include them. Treat the specification as the full list.
- **SimpleStudy unit names use old-syllabus headings** ("Conflict Resolution: Industrial
  Relations", "Management Skills", "Management Activities: Planning, Organising and Controlling",
  "Sources of Finance and Cash Flow Management", "Ownership Structures"). The topics under them
  follow the specification. Don't let the unit names pull old-syllabus content back in.
- **Old-syllabus content the specification dropped.** Leave all of this out of notes,
  flashcards and test questions unless a learning outcome above asks for it:
  - elements of contract law
  - managing a household and comparing it with a business; household budgets; basic tax
    computations and tax forms
  - final accounts, balance sheets, and profitability, liquidity and debt/equity ratios
  - the planning–organising–controlling framework; formal and informal organisation structures;
    span of control
  - "classic motivation theories" as a named requirement. [S3.2 LO4] asks for factors that
    affect motivation, and theories may support that.
  - empowerment and total quality management
  - memos, reports and business letters; chairperson and secretary duties; agendas and minutes
  - categories of industry; community development
- **No Higher Level-only content.** The old syllabus marked outcomes "(HL)"; the specification
  marks none.
- **New in the specification:** ESG, governance, audit, risk management and compliance [S1.2];
  stakeholder mapping and power-interest grids; design thinking; the business model canvas and
  digital business models; STEEPLE and Porter's five forces; cost-benefit and force-field
  analysis; remote and blended work and corporate wellness [S3.2]; fintech, credit ratings,
  financial fraud, crypto-finance and CBDC [S4.2]; the gig economy [S4.3]; the circular and shadow
  economies [S4.1]; FDI [S1.5]; the 40% Investigative Study.
- **The marketing mix has seven elements** [S2.4]: product/service, pricing, promotion, people,
  packaging, process and place. Packaging replaces the "physical evidence" of the usual services
  7 Ps.
- **Corrections to the repo:**
  - `pipeline/config.py` gave business a cutoff of 1999 as an unverified estimate. 1999 is the
    old syllabus's first exam: it was introduced in 1997 (Department of Education circular
    0033/2018). Papers from 1999 to 2026 are old-syllabus legacy practice, not on-course
    papers. The entry now says so.
  - The app has 10 chapters for 19 specification sections plus the Unifying Strand. The missing
    sections hold about half the learning outcomes (Appendix B).
  - `app.js` fallback vocabulary for chapter "10" (break-even point, working capital) and chapter
    "14" (delegation) leans on old-syllabus terms. It only shows if `data.js` fails to load, so
    it was left alone.

## Appendix B — Specification content with no chapter yet (proposed placement; needs user approval)

The app numbers chapters by specification section across strands (ch1 = S1.1, ch6–ch12 =
S2.1–S2.7, ch16 = S3.4, ch17 = S4.1). The proposed IDs fill the gaps in that numbering. The
Unifying Strand needs an ID outside the sequence. 84 of the specification's 138 learning
outcomes are here.

### ch2 (proposed) — Forms of Business, Regulation and Governance [S1.2]
1. **Public, private, semi-state and not-for-profit enterprises** [S1.2 LO1]: distinguish them
   and analyse the contribution of each type locally and nationally.
   - Glossary: not-for-profit enterprises are motivated by broader social objectives, including
     charities, social enterprises and NGOs.
   - SimpleStudy: Forms of Business.
2. **Ownership and how it changes** [S1.2 LO2]: how ownership differs between **sole traders,
   partnerships, private limited companies, public listed companies, franchises, co-operatives
   and public sector organisations**; how ownership evolves over a business's lifecycle,
   including **nationalisation and privatisation**.
   SimpleStudy: Forms of Business.
3. **Regulation** [S1.2 LO3]: the purpose of regulation in business; how organisations are
   regulated internally and externally, including **audit, risk management and compliance**.
   SimpleStudy: Business Regulation and Governance.
4. **Governance** [S1.2 LO4]: what governance in an organisation means.
5. **ESG** [S1.2 LO5]: the significance of environmental, social and governance factors in
   business governance; the three factors considered in an ESG report.
   Glossary: these three pillars form ESG frameworks, and businesses may be expected to report
   their performance and progress under them.

### ch3 (proposed) — Business and the Economy [S1.3]
1. **Economic indicators** [S1.3 LO1]: how **inflation, employment rates, interest rates, economic
   growth and development, exchange rates and consumer confidence** affect business development
   and growth.
   SimpleStudy: Key Economic Indicators.
2. **The value of the business economy in Ireland** [S1.3 LO2]: including turnover and employment
   patterns. Use current CSO figures and don't invent statistics.

### ch4 (proposed) — The Influence of National and EU Policy [S1.4]
1. **Irish government policy across sectors** [S1.4 LO1]: three Irish government policies that
   affect three different sectors of the economy. This is a choice, so write more than three.
   - Glossary: Irish government policy means actions or statements of guidance adopted by
     the government and used as a basis for decision-making. Sectors of the economy are those
     published by the CSO.
   - SimpleStudy: National Policy and Business.
2. **Policy vs legislation** [S1.4 LO2]: the difference between government policy and
   legislation.
3. **Business and national policy** [S1.4 LO3]: the role business plays in developing national
   policy; how stakeholders can inform and influence policy, including **interest groups and
   lobbying**.
4. **EU decision-makers** [S1.4 LO4]: the **Council of the European Union, the European
   Commission, the European Parliament and the European Central Bank**.
   SimpleStudy: The European Union.
5. **Regulations, directives and opinions** [S1.4 LO5]: distinguish them by how the Irish
   government must respond at national level.
6. **One EU regulation and one EU directive** [S1.4 LO6]: evaluate their effect on business in
   Ireland: purpose, implementation in Ireland, positive and negative effects on different
   stakeholders, and whether each fosters ethical and sustainable practice and/or technology use.
   Choice: write at least two regulations and two directives. **Exclude GDPR and the consumer and
   employment law used in [S4.1] and [S4.3]** (footnote 1).

### ch5 (proposed) — Irish Business Globally and Internationally [S1.5]
1. **Trading blocs** [S1.5 LO1–2]: what a trading bloc is; why trading blocs matter to
   businesses in the Irish economy; the blocs most relevant to Irish business.
   SimpleStudy: International Business; The European Union.
2. **Ireland's EU membership** [S1.5 LO3]: evaluate it from the perspective of the economy,
   businesses and consumers.
3. **Trading internationally** [S1.5 LO4–5]: why Irish-based organisations expand
   internationally; factors to consider: **taxes and tariffs, costs, exchange rates, regulation,
   competition, language/culture**; why Irish businesses trade globally, with reference to
   Ireland's open economy; the challenges and benefits compared.
   - Glossary: international trade is the movement or exchange of goods or services between two
     jurisdictions or across borders, including trade on the island of Ireland between the
     Republic and Northern Ireland.
   - SimpleStudy: International Business; Internationalisation and Globalisation.
4. **Balance of payments and balance of trade** [S1.5 LO6]: distinguish them and calculate both
   from given figures. Include worked calculations.
5. **Globalisation's impact** [S1.5 LO7–8]: the social and environmental consequences of
   globalisation, including **political risks, financial risks and cultural barriers**; positive
   and negative impacts of Irish organisations trading internationally; how globalisation
   increases interdependence, and the consequences for businesses and consumers.
   - Glossary: globalisation is the growing interdependence and interconnectedness of the
     world's economies, cultures and populations, from cross-border trade in goods, services and
     digital technology and the movement of investment, people, data and information.
     Interdependence arises when one group depends on another to supply necessary goods and
     services.
   - SimpleStudy: Internationalisation and Globalisation.
6. **Technology in globalisation** [S1.5 LO9]: technology's role in trade, work practices and how
   businesses operate.
7. **Foreign Direct Investment** [S1.5 LO10–11]: what FDI is; how Ireland attracts it (**human
   capital development, pro-enterprise policy, access to markets, research**) and how the
   government promotes it; its contribution and challenges for Ireland in **employment, revenue,
   research, infrastructure and innovation**.
   Glossary: human capital is the competencies embodied in people, invested in and developed to
   help them be more productive and realise their potential.

### ch13 (proposed) — Leading and Managing an Organisation [S3.1]
1. **Leadership vs management** [S3.1 LO1]: the roles of leaders and managers; distinguish
   between leadership and management.
   SimpleStudy: Leading and Managing an Organisation.
2. **Organisational culture and innovation** [S3.1 LO2]: their significance in successful
   organisations; applying innovative approaches.
3. **Leadership styles** [S3.1 LO3]: how leadership styles influence organisations and foster
   organisational culture and innovation.
4. **Conflict in the workplace** [S3.1 LO4]: the range of reasons for workplace conflict and its
   impact on the workplace.
5. **Dealing with conflict internally** [S3.1 LO5]: how employees and employers deal with conflict
   internally.
6. **External conflict resolution** [S3.1 LO6]: external approaches, including **conciliation and
   arbitration**. This overlaps ch1 subsection 3 (stakeholder conflict); state each fact once
   and cross-reference.

### ch14 (proposed) — Leading and Managing People [S3.2]
1. **Workforce planning** [S3.2 LO1]: internal and external factors affecting workforce
   planning.
   SimpleStudy: Leading and Managing People; Human Capital Management.
2. **Recruitment and ethics** [S3.2 LO2]: key stages in recruitment (**identification, application,
   selection**); ethical recruitment, including **equality, diversity and inclusion**.
3. **Digital recruitment and selection** [S3.2 LO3]: evaluate how digital technologies influence
   recruitment and selection.
4. **Motivation** [S3.2 LO4]: factors that affect employee motivation.
5. **Appraisal** [S3.2 LO5–6]: what effective appraisal is; approaches, including
   **self-appraisal, formative, summative and 360-degree**; how they contribute to motivation.
6. **Human capital management** [S3.2 LO7]: what it is; how the organisational environment
   affects its development; **induction**; how employees learn from experience.
   SimpleStudy: Human Capital Management.
7. **Training and professional development** [S3.2 LO8]: types offered; why ongoing training and
   development matter to human capital management.
8. **Teamwork** [S3.2 LO9]: opportunities and challenges of teams for employees and employers.
9. **Sustainable workplaces** [S3.2 LO10]: how employers and employees can work together to make
   the workplace more sustainable.
10. **Digital technology in the workplace** [S3.2 LO11]: how digital technology affects the
    workplace.
11. **Remote and blended work** [S3.2 LO12–13]: opportunities and challenges for employees and
    employers; the ethical and sustainability issues involved.
12. **Corporate wellness** [S3.2 LO14–15]: its importance; its effect on motivation and
    organisational culture; the leader's role in promoting it.
    Glossary: corporate wellness is an organisational focus on equality, diversity, inclusivity
    and the overall wellbeing of the workforce, to nurture a diverse, inclusive and healthy
    workplace.

### ch15 (proposed) — The Importance of Communication [S3.3]
1. **Why communication matters** [S3.3 LO1]: it supports collaboration, avoids conflict,
   increases engagement, promotes a positive culture, manages change and promotes innovation.
   SimpleStudy: The Importance of Communication.
2. **Modes of communication** [S3.3 LO2]: verbal and non-verbal modes and how effective each is
   in an organisation.
3. **Technology and communication** [S3.3 LO3]: its effect on **modes, speed, cost, access,
   collaboration, sustainable business practices, productivity and security**.
4. **Improving communication** [S3.3 LO4]: including **setting clear goals, listening actively,
   ensuring ongoing engagement, and choosing the correct mode**.

### ch18 (proposed) — Making Informed Financial Decisions [S4.2]
1. **Saving, investing and borrowing** [S4.2 LO1]: factors to consider: **inflation, risk, interest
   rates, taxes and charges, short/medium/long term, return on investment**.
   SimpleStudy: Making Informed Financial Decisions.
2. **Risk tolerance and reliable information** [S4.2 LO2]: risk tolerance from a consumer's
   perspective; risks facing consumers of financial products; finding reliable sources of
   financial information.
3. **Switching providers** [S4.2 LO3]: why consumers should consider switching financial
   product providers.
4. **Fintech** [S4.2 LO4]: how technology affects the provision of financial products; benefits
   and challenges of fintech for consumers.
   Glossary: fintech is the use of technology to deliver financial services and products to
   consumers.
5. **Credit ratings** [S4.2 LO5]: the criteria for creditworthiness; how a credit rating is
   established; factors affecting it; the consequences of a poor rating; how a rating stays with
   a person over time.
6. **Regulating financial services** [S4.2 LO6]: regulation by the Irish government and the EU;
   managing risk in **pensions, mortgages, credit-based products and crypto-finance**; the
   consequences of under-regulation.
   SimpleStudy: Financial Regulation.
7. **Financial fraud** [S4.2 LO7]: a range of fraud activities and how consumers can protect
   themselves.
8. **Central Bank Digital Currency** [S4.2 LO8]: CBDC as an electronic equivalent of cash; its
   advantages and disadvantages; how it differs from stablecoins and crypto assets; its potential
   effect on consumers and businesses.
   Glossary: CBDC lets consumers use central bank money in digital form alongside notes and
   coins. A stablecoin's stability depends on the issuer and its pledge to maintain the value. No
   single identifiable entity is liable for crypto assets.
9. **Applying my learning: finance in the news** [S4.2 LO9].

### ch19 (proposed) — Being an Informed Employee [S4.3]
1. **Employee protection** [S4.3 LO1]: how employees are protected legislatively and
   non-legislatively.
   SimpleStudy: Employee Protections.
2. **Employment legislation** [S4.3 LO2]: the rights and responsibilities of employees and
   employers under current employment legislation, covering **pay, conditions, health and safety,
   discrimination, security of employment and dismissal**.
   SimpleStudy: Employee Protections.
3. **Trade unions** [S4.3 LO3]: their role in supporting employees in the workplace.
   SimpleStudy: Employee Governance.
4. **The gig economy** [S4.3 LO4]: on-demand, freelance and "per piece" work; opportunities and
   challenges for workers.
   Glossary: the part of the labour market that relies on temporary positions, part-time workers
   or freelancers.
5. **The budget and workers** [S4.3 LO5]: how the annual government budget affects workers. Use
   the most recent budget.
6. **Applying my learning: the workplace in the news** [S4.3 LO6].

### Investigating Business (proposed ID, e.g. `ch20`) — Unifying Strand [U1–U6] and the Investigative Study
The Unifying Strand is woven through all four contextual strands. It is also the main content of
the 40% Business Alive Investigative Study, and the written exam assesses it. It needs a chapter
of its own, or a non-chapter assessment page; SimpleStudy treats it as its first unit.
1. **Developing questions to research** [U1 LO1]: develop and refine questions so they are clear
   and have sufficient quality information or data, using SMART objectives.
   - Glossary: SMART means specific, measurable, achievable, relevant and timebound.
   - SimpleStudy: Developing Questions to Research.
2. **Managing information** [U2 LO1–6]: identify relevant data, evidence and information from a
   range of sources; assess accuracy, credibility, reliability, bias and value; record and
   acknowledge sources; identify the key points in each; analyse how important an issue is to
   different individuals and groups; ensure data are representative and comprehensive; identify
   gaps and their effect on drawing conclusions.
   - Glossary: primary sources are original documents or first-hand information, such as
     interviews and surveys. Secondary sources often interpret primary information.
   - SimpleStudy: Managing Information.
3. **Project planning** [U3 LO1–3]: clearly defined purpose, goals and criteria for success; the
   elements of a project plan: **roles and responsibilities, resources, objectives, a detailed time
   schedule, risk assessment, monitoring and evaluation**; monitoring and evaluating progress.
   SimpleStudy: Project Planning.
4. **Analysing and evaluating information** [U4 LO1–5]: analyse and interpret data; evaluate the
   range of perspectives; synthesise findings; appraise the value of information; reach informed
   decisions, conclusions or recommendations.
   SimpleStudy: Analysing and Evaluating Information.
5. **Presenting findings and perspectives** [U5 LO1–4]: oral, visual, written and multimodal
   forms for different purposes and audiences; graphs, charts, diagrams and graphics; how and why
   one's perspective changed; presenting conclusions clearly using business terminology.
   SimpleStudy: Presenting Findings and Perspectives.
6. **Acknowledging sources** [U6 LO1]: record and acknowledge every primary and secondary source,
   whatever its format.
7. **The Business Alive Investigative Study**: the brief and its timeline, the stages, the report,
   and the four Descriptors of Quality (planning, investigating, applying, communicating). Use the
   specification's pages 32–35 and the NCCA *Guidelines to Support the Business Alive
   Investigative Study* (November 2024).
   SimpleStudy: Investigative Study.

## Appendix C — SimpleStudy structure as recorded (2026-08-07)

For reference only. Names are as given in `pipeline/resources/business/guide-simplestudy.md`.

| # | SimpleStudy unit — topics | Chapter |
|---:|---|---|
| 1 | Investigating Business — Developing Questions to Research; Managing Information; Project Planning; Analysing and Evaluating Information; Presenting Findings and Perspectives | Appendix B (Unifying) |
| 2 | People in Business — Key Stakeholders in Business | ch1 |
| 3 | Conflict Resolution: The Consumer — Consumer Rights; Making Informed Consumer Decisions | ch17 |
| 4 | Conflict Resolution: Industrial Relations — Employee Protections; Employee Governance | ch19 (proposed) |
| 5 | Enterprise — Enterprise | ch6 |
| 6 | Management Skills: Leading and Motivating — Leading and Managing an Organisation; Leading and Managing People | ch13, ch14 (proposed) |
| 7 | Management Skills: Communication — The Importance of Communication | ch15 (proposed) |
| 8 | Management Activities: Planning, Organising and Controlling — The Rationale for Planning; Force Field Analysis and Strategic Planning | ch16 |
| 9 | Sources of Finance and Cash Flow Management — Operations and Finance; Making Informed Financial Decisions; Financial Regulation | ch10; ch18 (proposed) |
| 10 | Insurance and Managing Risk — Risk Management and Insurance | ch12 |
| 11 | Human Capital Management — Human Capital Management | ch14 (proposed) |
| 12 | Identifying Business Opportunities — Idea Development | ch7 |
| 13 | Getting Started in Business — Business Planning | ch8 |
| 14 | Market Research and Market Segmentation — Market Research and Market Analysis | ch9 |
| 15 | Marketing Mix — The Marketing Mix | ch9 |
| 16 | Business Expansion — Growth, Development, and Expansion | ch11 |
| 17 | Ownership Structures — Forms of Business; Business Regulation and Governance | ch2 (proposed) |
| 18 | Business, Government and the Economy — Key Economic Indicators; National Policy and Business | ch3, ch4 (proposed) |
| 19 | International Trade — International Business | ch5 (proposed) |
| 20 | The European Union — The European Union | ch4, ch5 (proposed) |
| 21 | Global Business — Internationalisation and Globalisation | ch5 (proposed) |
| 22 | Assessment — Investigative Study; Written Exam | Appendix B (Unifying); Read this first |
