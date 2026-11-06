# Leaving Cert History (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format,
  worked example). This outline says **what** to cover; that file says **how** to write it. An
  information package (`course-outlines/packages/history/<loId>.md`, see `packages/README.md`)
  must be written for each subsection before its notes. None exist yet for history.
- **The syllabus:** the NCCA *Leaving Certificate History Syllabus (Ordinary and Higher Levels)*,
  Government of Ireland © 2003, introduced in 2004 and first examined in 2006. curriculumonline.ie
  labels it **"LC Syllabus (for examination to June 2028)"**, so it is the correct document for
  June 2027 candidates. The official PDF is `pipeline/resources/history/spec-syllabus.pdf` (also
  `relevant-resources/syllabi/history.pdf`). On 2026-11-05 both were checked byte for byte
  against the copy on curriculumonline.ie. The Guidelines for Teachers (same page, same status)
  fill in the documents-based and research studies.
- **Do not use the new *Curriculum specification for Leaving Certificate History*** ("for
  introduction to schools in September 2027", kept as
  `relevant-resources/syllabi/history-2027-spec.pdf`), or the NCCA's March 2026 consultation
  draft. It is a different course: Strands 1–4, "Ireland 1879–2009" and "The World 1917–2009",
  no fields of study and no prescribed case studies. The first cohort sits the exam in 2029 at
  the earliest. Nothing in it is examined in June 2027.
- **The field of study:** the syllabus has two alternative fields: **Early Modern, 1492–1815**
  and **Later Modern, 1815–1993**. Each has 12 topics: 6 Irish and 6 from Europe and the wider
  world. Each student takes one field. **The app covers only the Later Modern field**: its 12
  chapter IDs are the 12 Later Modern topics in syllabus order. Every past paper in the app is
  the Later Modern paper. The Early Modern field has no chapters (Appendix B).
- **The documents-based topic for June 2027 is prescribed by the SEC.** Circular **S09/24**
  (February 2024) sets **Later Modern, Ireland, Topic 2: Movements for political and social
  reform, 1870–1914 (`hist-ire2`)** for the 2026 and 2027 examinations (copy:
  `relevant-resources/syllabi/history-2026-2027-prescribed-topics.pdf`). The Early Modern
  topic is Ireland Topic 1, Reform and Reformation in Tudor Ireland. This means, for every
  Later Modern candidate in 2027:
  - `hist-ire2` is **compulsory**. It is examined only through Question 1, the documents-based
    question (DBQ). The paper sets no Section 2 essay on it.
  - Because the prescribed topic is Irish, each student studies **one more Irish topic** (from
    `hist-ire1`, `hist-ire3`–`hist-ire6`) and **two Europe topics** (from `hist-eur1`–`hist-eur6`).
    Students choose, so all 12 chapters need full notes.
  - For reference, SEC circular S25/26 prescribes **Europe Topic 6 (`hist-eur6`)** for 2028.
    That doesn't affect 2027.
- **References** in square brackets: **[I2]** = Later Modern Ireland Topic 2; **[E3]** = Europe
  and the wider world Topic 3. A letter after the topic names the syllabus perspective:
  **P** = politics and administration; **S** = society and economy (I4's row is "economy and
  society"); **C** = culture, religion (and science). **CS** = the case study in that
  perspective's row, e.g. **[I2 S-CS]** = Dublin 1913.
- **How the syllabus sets out each topic** (pp. 11, 18–47): date limits; elements listed under
  each perspective; **three case studies**; **ten key personalities**; and a list of **key
  concepts**. Students study what the elements list, not everything that happened between the
  dates. Every element, every case study, every key personality and every key concept is
  required. **There are no choices inside a topic.**
- **What each subsection contains:**
  - **Syllabus:** the elements, close to the syllabus's wording. This is the required scope.
  - **Case study:** named when the subsection holds one. Case studies need a full discursive
    account: background, causes, sequence of events with dates, people involved, outcomes,
    significance, and the differing views of contemporaries.
  - **Key personalities:** the ones whose main profile belongs here. Each gets one note block:
    who they were; their role in the listed elements; what they did with dates; how they
    influenced events or were influenced by them; whether they were a participant or a witness;
    contemporary attitudes to them; current (historians') attitudes to them. The Higher Level
    outcomes on p. 13 require the last two.
  - **Key concepts:** the syllabus's key concepts for this subsection. Each one goes into
    `keyTerms`, defined and tied to its use in the topic.
  - **Cover:** what the notes should contain, including the assumed knowledge
    (NOTES_STANDARD rule 9) the elements rest on. **Every name, date and figure in Cover points
    the package writer at what to check. None of them is a checked fact.** The package must
    verify each one before notes use it; items marked *(verify)* are ones where sources often
    disagree.
  - **Exam:** how SEC Higher Level papers, 2006–2025, have tested it, paraphrased (the app's
    bank, `history-exam-questions.js`). Never copy question wording into notes.
  - **SimpleStudy:** the matching unit in SimpleStudy's Higher Level course (recorded
    2026-08-07, `pipeline/resources/history/guide-simplestudy.md`). It covers only 5 of the 12
    topics; "none" means it has no unit.
- **Higher vs Ordinary level** (syllabus p. 7, p. 13): both levels study the same topics. Ordinary
  Level puts "particular emphasis" on the key personalities and case studies. Higher Level
  studies "all aspects of topics to a greater depth". The Higher Level outcomes add: a good
  understanding of causes and consequences; a *discursive* (not just narrative) account of each
  case study; evaluating each key personality, with contemporary and current attitudes; and the
  relevance of the key concepts. **The syllabus marks no topic, element or case study as Higher
  Level only, so mark nothing HL only.**
- **What the exam needs from the notes:** Higher Level essays (100 marks each) are marked on
  cumulative points plus an overall evaluation of how well the answer argues (the app's paper
  guide, `exam-breakdown.js`). The recurring question shapes are: "contribution of X and/or Y",
  "strengths and weaknesses", "successes and failures", "to what extent", "which was more
  effective, A or B", "why and how", "impact on…", and "main events and significance" of a case
  study. So every subsection needs: causes → events → results, with dates; evidence a student
  can use for judgement (achievements vs limits, contemporary vs later views); and the links
  between elements that questions often join (e.g. "Fenianism or Liberal reforms").
- **Assessment** (syllabus pp. 14–15; Guidelines pp. 13–15; SEC circulars):
  - **Research study report, 20% (100 marks)**, pre-submitted to the SEC: outline plan 3%,
    evaluation of sources 5%, extended essay 12%. Higher Level uses at least three primary or
    specialist secondary sources. The extended essay is about 2,000 words at Higher Level
    (Guidelines). See Appendix B.
  - **Terminal examination, 80% (400 marks).** Higher Level 2 h 50 min; four questions of
    equal value, one per topic studied. **Question 1 is the DBQ on the prescribed topic:**
    (a) comprehension 20, (b) comparison 20, (c) criticism 20, (d) contextualisation 40.
    Documents relate to one of the topic's three case studies. Part (d) is a short essay
    that places the documents in their historical context. In every Higher Level paper from
    2006 to 2025 it asked about the case study's own subject (e.g. 2015: the significance of
    the Eucharistic Congress; 2025: whether the Jarrow March was a total failure). The other
    three answers are essays, one from each of the student's other topics, chosen from four
    questions per topic. At least two of the three perspectives are
    examined in each topic each year.
- **Subsection ids:** notes use `<chapter-id>-s<n>` (e.g. `hist-ire2-s9`), numbered in the order
  below; `data.js` has these outcomes, after each chapter's review outcome (`hist-ire1-1` etc.),
  which holds the test questions in `history-test-questions.js`. Notes live in
  `content/history/<loId>.json` and build to `history-notes.js`.
- **Status (2026-11-06):** all 128 subsections have notes, key terms and fact cards. Haiku
  drafted them from this outline, and Sonnet reviewers then fact-checked and expanded every file
  (about 530 factual corrections). No information packages were written first, so facts rest on
  the reviewers' checks, not on a package's checked-facts table. The old `history-content.js`
  notes and `history-flashcards.js` deck are retired to `archive/history-2026-11-06/`.

---

## Later Modern Ireland, 1815–1993

### hist-ire1 — Ireland and the Union, 1815–1870 [I1]

Key personalities: Daniel O'Connell; Thomas Davis; Charles Trevelyan; Charles Kickham; James
Stephens; Asenath Nicholson; Mother Mary Aikenhead; Cardinal Paul Cullen; William Carleton;
William Dargan. Key concepts: the Union; sectarianism; Catholic Emancipation; physical force
republicanism; laissez-faire; economic depression; dowry; landlordism; famine; nation;
ultramontanism; evangelicalism.

1. **The government of Ireland under the Union and the campaign for Catholic Emancipation,
   1815–1829** [I1 P; P-CS]
   - Syllabus: administrative and political structures under the Act of Union; O'Connell — the
     campaign for Emancipation. Case study: **the campaign for Catholic Emancipation,
     1823–1829**.
   - Key personalities: Daniel O'Connell (profile, part 1: background, the Catholic question,
     methods).
   - Key concepts: the Union; Catholic Emancipation; sectarianism.
   - Cover: Act of Union 1801 (assumed); Westminster and the 100 Irish MPs; Lord Lieutenant,
     Chief Secretary, Under-Secretary and Dublin Castle; local government (grand juries,
     magistrates); policing (Peace Preservation Force, county constabulary, the 1836 Irish
     Constabulary); the forty-shilling freeholder franchise; the disabilities Catholics still
     faced in 1815 (could not sit in Parliament or hold high office) and the veto controversy.
     Case study in depth: the Catholic Association (1823); the Catholic Rent (1824) and its
     collection through parishes; the role of the clergy; the Association's suppression (1825)
     and re-formation; the Waterford election (1826); the Clare election (1828); Wellington's
     and Peel's reasons for conceding; the Relief Act (April 1829) and what it did and did not
     grant; the raising of the county franchise to £10; how far it was O'Connell's victory;
     its political and religious dimensions; British and Protestant reactions.
   - Exam: Emancipation's political and religious dimensions (2020); why O'Connell won
     Emancipation but not Repeal (2006, 2010, 2021); how far his leadership explains success
     and failure (2019); changes in political structures, 1815–1870 (2011).
   - SimpleStudy: none.
2. **O'Connell after 1829, the Tithe War, the Poor Law and Young Ireland, 1830–1848** [I1 P]
   - Syllabus: O'Connell — the campaign for Repeal, achievements; the Tithe War; the Poor Law;
     Young Ireland.
   - Key personalities: Daniel O'Connell (profile, part 2: Repeal, his achievements and an
     overall evaluation); Thomas Davis.
   - Key concepts: nation; physical force republicanism (as Young Ireland's legacy).
   - Cover: O'Connell at Westminster in the 1830s; the Lichfield House Compact (1835) and the
     Whig alliance (Drummond's reforms, municipal reform 1840, O'Connell Lord Mayor of Dublin);
     the Repeal Association (1840); 1843 "Repeal Year", the monster meetings, the Clontarf
     cancellation, his arrest and trial; the split with Young Ireland (the peace resolutions,
     1846); his death (1847). O'Connell's strengths and weaknesses, and contemporary and later
     views of him. The Tithe War: tithe as a grievance, the 1830s campaign of non-payment and
     violent clashes (e.g. Carrickshock 1831), and the Tithe Rentcharge Act (1838). The Poor
     Law (1838): the rejected Whately inquiry, George Nicholls, unions, boards of guardians,
     workhouses, the poor rate. Young Ireland: The Nation (1842); Davis, Gavan Duffy, Dillon,
     Mitchel; cultural nationalism; the Irish Confederation (1847); the 1848 rising at
     Ballingarry, and why it failed.
   - Exam: O'Connell's aims and achievement, strengths and weaknesses (2008, 2009, 2012, 2013,
     2016, 2024); why Repeal failed (2015); Young Ireland's aims and achievements and its
     contribution to nationalism (2007, 2008, 2010, 2018, 2025); Davis (2009, 2016); the Tithe
     War (2020); the Poor Law in relief of distress (2016).
   - SimpleStudy: none.
3. **The Irish countryside, economic crisis and the Great Famine: causes, course and government
   responses, 1815–1850** [I1 S; P]
   - Syllabus: the Irish countryside, 1815; economic crisis, 1815–1850; the Famine;
     government responses to Famine.
   - Key personalities: Charles Trevelyan.
   - Key concepts: landlordism; economic depression; laissez-faire; famine.
   - Cover: the social structure of the countryside in 1815 (landlords, absentees, middlemen,
     strong farmers, cottiers, labourers, conacre); population growth, subdivision and
     dependence on the potato; the post-1815 price collapse, the decline of rural industry and
     the partial famines before 1845; the Devon Commission. The Famine: blight (1845) and its
     spread; 1846–47 ("Black '47"); 1848–49; regional variation (west and south-west worst);
     fever; mortality and emigration *(verify figures)*. Government responses: Peel's Indian
     corn purchases and Relief Commission; public works; Russell's Whig government and
     laissez-faire; Trevelyan at the Treasury; the soup kitchens (1847); the Poor Law Extension
     Act (1847), the Gregory (quarter-acre) clause and evictions; the rate-in-aid (1849);
     exports of food during the Famine; how effective the responses were and why.
   - Exam: how effective government and/or private responses were (2007, 2012, 2015, 2018,
     2019, 2021, 2022); how the Famine began and why it lasted (2011); social and economic
     developments 1815–1850 (2009, 2013); Trevelyan and/or Nicholson (2008, 2017, 2020, 2023);
     landlords' fortunes 1815–1870 (2023).
   - SimpleStudy: none.
4. **Private responses to Famine and the Famine's impact** [I1 S-CS]
   - Syllabus: case study **private responses to Famine, 1845–1849**; emigration (Famine
     emigration).
   - Key personalities: Asenath Nicholson.
   - Cover: case study in depth: the Society of Friends (the Central Relief Committee, soup
     kitchens, later reports on conditions); the British Relief Association; other charities
     and international giving; the churches (including "souperism" and its legacy); landlord
     responses, from relief to clearances and assisted emigration; local committees; Asenath
     Nicholson's travels, relief work and writings; what private relief could and couldn't
     achieve, and why it shrank after 1847. Impact of the Famine to 1870: population fall,
     the end of the cottier class, consolidation of holdings, the Encumbered Estates Act
     (1849) and new landlords, the shift to pasture, late marriage and the dowry, emigration
     as a habit, the decline of the Irish language, and the political memory of the Famine.
   - Exam: effectiveness of private responses (as for s3); impact of the Famine during and
     after, to 1870 (2006, 2025).
   - SimpleStudy: none.
5. **Post-Famine Ireland: economy and society, 1850–1870** [I1 S]
   - Syllabus: the post-Famine economy; emigration; education; impact of the railways;
     industrial development in Belfast.
   - Key personalities: William Dargan.
   - Key concepts: dowry; landlordism (post-Famine).
   - Cover: post-Famine agriculture (cattle and dairy, rising prices, the stronger farmer
     class); emigration after 1850 (destinations, chain migration, remittances, effects on
     those who stayed) — treat briefly here; `hist-ire4` covers it in depth. Education: the
     national school system (1831) and its aims; Catholic and Protestant attitudes; the
     Christian Brothers; the Queen's Colleges (1845); the Catholic University (1854); effects
     on literacy and on the Irish language. Railways: the Dublin and Kingstown (1834); Dargan's
     career and projects, including the 1853 Dublin Exhibition; network growth; effects on
     trade, agriculture, towns, the press and tourism. Belfast: linen mechanisation;
     engineering; the start of shipbuilding (Harland and Wolff); population growth;
     sectarian geography and riots; why the Belfast region developed differently from the
     rest of Ireland.
   - Exam: railways and/or Belfast industry (2006, 2007, 2010, 2012, 2017, 2022); emigration
     and education (2010, 2012, 2017); Belfast's different development (2016); Dargan (2018,
     2021).
   - SimpleStudy: none.
6. **Electoral reform, sectarianism in politics, Fenianism and Liberal reforms, 1850–1870**
   [I1 P]
   - Syllabus: electoral reform; sectarianism in politics; Fenianism; Liberal reforms.
   - Key personalities: James Stephens; Charles Kickham.
   - Key concepts: physical force republicanism; sectarianism.
   - Cover: electoral reform (the 1829 franchise, the 1832 Reform Act, the Irish Franchise
     Act 1850, and their effect on the electorate); sectarianism in politics (the Orange Order,
     Dolly's Brae 1849, the Ecclesiastical Titles Act 1851, the Tenant League and Independent
     Irish Party, and the Sadleir–Keogh betrayal); Fenianism: the IRB (1858) and the Fenian
     Brotherhood in the USA; Stephens's organisation and leadership; the Irish People and
     Kickham; Church opposition (Cullen); the 1865 arrests; the 1867 rising; the Manchester
     Martyrs; Clerkenwell; the Canadian raids; Fenianism's Irish and international
     dimensions, strengths and weaknesses, and long-term legacy. Liberal reforms: Gladstone's
     1868 mission; the Irish Church Act (1869, disestablishment); the Land Act (1870) and its
     limits.
   - Exam: Fenianism's effectiveness, strengths and weaknesses, international dimension
     (2013, 2017, 2022, 2024); Stephens and/or Kickham (2009, 2011, 2019, 2023); Fenianism or
     Liberal reforms (2013, 2020).
   - SimpleStudy: none.
7. **Culture, religion and science: identities, the Synod of Thurles, the creative arts and
   science** [I1 C; C-CS]
   - Syllabus: developments in the creation of cultural and religious identities; the creative
     arts; developments in science and technology. Case study: **the Synod of Thurles, 1850,
     and the Romanisation of the Catholic Church**.
   - Key personalities: Cardinal Paul Cullen; Mother Mary Aikenhead; William Carleton; Thomas
     Davis (cultural role; cross-refer to s2).
   - Key concepts: ultramontanism; evangelicalism; nation; sectarianism.
   - Cover: Catholic identity (church building, religious orders, the "devotional revolution");
     Protestant identity (evangelicalism, the "Second Reformation", the Orange Order); the
     nationalist "nation" of Young Ireland; the decline of the Irish language. Case study in
     depth: Cullen's background in Rome; his appointment as Archbishop of Armagh and apostolic
     delegate; the Synod (1850) — the first national synod in about two centuries *(verify)*,
     its decrees (condemning the Queen's Colleges, regulating sacraments and clergy) and
     opposition to it; Cullen in Dublin from 1852; Romanisation of practice and devotion;
     the Catholic University; Cullen's attitude to Fenianism; his influence on political
     attitudes and religious practice. Mary Aikenhead: the Religious Sisters of Charity
     (1815) and St Vincent's Hospital (1834). The creative arts: Carleton (Traits and Stories
     of the Irish Peasantry), Thomas Moore, Mangan, and painters and antiquarians such as
     Petrie and the Ordnance Survey scholars O'Donovan and O'Curry *(verify the selection in
     the package)*. Science and technology: William Rowan Hamilton, Lord Rosse's telescope at
     Birr, Nicholas Callan's induction coil, George Boole at Cork, Robert Kane *(verify)*.
   - Exam: Cullen's influence on political attitudes and religious practice (2007, 2009,
     2015, 2025); Cullen and/or Aikenhead (2013, 2022); Carleton, Dargan, Aikenhead, Davis
     (2011, 2018, 2021, 2024); creative arts and/or science (2008, 2012, 2017, 2025);
     development of cultural and religious identities (2019, 2020).
   - SimpleStudy: none.

### hist-ire2 — Movements for political and social reform, 1870–1914 [I2] — the 2026–2027 documents-based topic

**This chapter is compulsory for every 2027 student and is examined only by Question 1.**
Documents (written or visual, including cartoons and photographs) come from one of the three
case studies: s3, s7 or s9. Notes for those three must be detailed enough to put any document
in context: names, dates, places, organisations, numbers and the views of each side.
Part (d) (40 marks) is a short essay on the subject of the case study the documents come from,
drawing on the rest of the topic for context. This topic was last prescribed for 2006 and 2007.
In 2006 the documents were on the 1885–1886 elections and Home Rule, and part (d) asked for
Parnell's strengths and weaknesses. In 2007 they were on the GAA, and part (d) asked how the
GAA dealt with its difficulties, 1884–1891. Dublin 1913 has not yet been the DBQ case study.
The June 2026 paper is not in the app's bank yet; add it when it is. Prepare all three case
studies equally. The rest of the chapter matters too: it supplies the context that parts (c)
and (d) reward, and SEC questions name its key personalities. The skills subsection (s11) is
part of this chapter for 2027.

Key personalities: Charles Stewart Parnell; John Redmond; Edward Carson; Isabella Tod; Hanna
Sheehy-Skeffington; James Connolly; Michael Davitt; James Larkin; Douglas Hyde; W.B. Yeats.
Key concepts: democracy; Home Rule; separatism; militarism; socialism; feminism; political
agitation; anglicisation/de-anglicisation; Irish Ireland; Anglo-Irish; suffragette.

1. **The Home Rule movement: origins, Butt and the rise of Parnell, 1870–1885** [I2 P]
   - Syllabus: the Home Rule movement: origins; development; leadership — Butt, Parnell.
   - Key personalities: Charles Stewart Parnell (profile, part 1: background and rise).
   - Key concepts: Home Rule; democracy; political agitation.
   - Cover: Isaac Butt's background and federal idea; the Home Government Association (1870)
     and Home Rule League (1873); the 1872 Ballot Act and the 1874 election; why Butt failed;
     obstruction (Biggar, Parnell); the New Departure (1878–79, Devoy, Davitt, Parnell);
     Parnell as League president and party chairman (1880); Kilmainham (1881–82); the Phoenix
     Park murders; the Irish National League (1882); turning the party into a disciplined
     machine (the pledge, constituency conventions, funding from America); Butt vs Parnell as
     leaders.
   - Exam: development of Home Rule 1870–1886 (2011, 2013, 2017); Butt or Parnell (2009, 2015);
     successes and failures of Home Rule 1870–1891 (2024).
   - SimpleStudy: Home Rule and Advanced Nationalism; Rise of Parnell.
2. **Land agitation and land reform, 1870–1914** [I2 S]
   - Syllabus: land agitation and land reform.
   - Key personalities: Michael Davitt.
   - Key concepts: political agitation.
   - Cover: tenant grievances and the "Three Fs"; the 1870 Act's limits (cross-refer to
     `hist-ire1-s6`); the agricultural depression of 1877–79; Irishtown and the Land League of
     Mayo (1879); the Irish National Land League (Oct 1879); Davitt's background and aims;
     the Land War: rent strikes, boycotting (Captain Boycott 1880), evictions, the Ladies' Land
     League (Anna Parnell); coercion; the 1881 Land Act (the Three Fs, the Land Courts); the No
     Rent Manifesto; the Arrears Act (1882); the Plan of Campaign (1886); Conservative
     "constructive unionism" (Ashbourne 1885, Balfour 1891, the Congested Districts Board); the
     Land Conference and Wyndham Act (1903); the Birrell Act (1909); outcome: tenant
     proprietorship and the end of landlordism as a power. Davitt's later career (Labour,
     opposition to Parnell in 1890).
   - Exam: land agitation and land reform (2008, 2015, 2017, 2018, 2021, 2024); Davitt and/or
     Parnell on land (2010, 2016, 2020, 2022); Davitt's contribution (2009); land agitation or
     1913 (2013, 2019); Davitt or Larkin as campaigners (2025).
   - SimpleStudy: Home Rule and Advanced Nationalism (land).
3. **Case study: the elections of 1885 and 1886 — issues and outcomes** [I2 P-CS; DBQ source]
   - Syllabus: case study **the elections of 1885 and 1886: issues and outcomes**.
   - Key personalities: Parnell (role in the case study).
   - Key concepts: Home Rule; democracy.
   - Cover: the Third Reform Act (1884) and redistribution (1885), and their effect on the
     Irish electorate; Parnell's balance-of-power strategy and the "Maamtrasna" alliance with
     the Conservatives; the clergy and the National League in candidate selection; the
     November–December 1885 election: the Irish Party's sweep outside east Ulster, the hung
     Parliament *(verify seat figures: Liberal 335, Conservative 249, Irish Party 86)*; the
     Hawarden Kite; Gladstone's conversion; the fall of Salisbury's government; the First Home
     Rule Bill (April 1886): its terms, debates, Chamberlain and the Liberal Unionists, its
     defeat in the Commons (June 1886); the "Orange card" (Lord Randolph Churchill) and
     unionist mobilisation; the Belfast riots of 1886; the July 1886 election and the
     Conservative–Liberal Unionist majority. Outcomes: the Liberal–Nationalist alliance, Home
     Rule tied to the Liberals, the birth of organised unionism, Parnell at his peak.
     Document types the SEC used in 2006: speeches, newspaper reports and pro- and anti-Home
     Rule cartoons (e.g. Punch).
   - Exam: the 2006 DBQ (documents on Home Rule and land; part (d) Parnell's strengths and
     weaknesses); issues and outcomes of the elections (2016).
   - SimpleStudy: 1885–1886 Elections case study.
4. **Parnell's fall, Redmond's leadership and Home Rule's rivals, 1886–1914** [I2 P]
   - Syllabus: the Home Rule movement: development; leadership — Parnell, Redmond; the first
     Sinn Féin party; the Irish Volunteers.
   - Key personalities: Parnell (profile, part 2: 1886–91 and overall evaluation); John
     Redmond.
   - Key concepts: separatism; militarism; Home Rule.
   - Cover: the Plan of Campaign and Parnell's distance from it; the Pigott forgeries and the
     Special Commission (1887–90); the O'Shea divorce (1890); Gladstone's letter, the Catholic
     hierarchy and Committee Room 15; the split; Parnell's death (1891); the Second Home Rule
     Bill (1893) and the Lords; the divided party in the 1890s; reunion under Redmond (1900);
     the United Irish League; the 1910 elections, the Parliament Act (1911) and the Third Home
     Rule Bill (1912), with its passage treated in `hist-ire3-s1`; Redmond's strengths and
     weaknesses to 1914. The first Sinn Féin: Arthur Griffith, the United Irishman, Cumann na
     nGaedheal (1900), The Resurrection of Hungary (1904) and dual monarchy, abstention and
     economic self-sufficiency, the founding of Sinn Féin (1905–08), the North Leitrim
     by-election (1908) and decline. The IRB revival (Tom Clarke, Bulmer Hobson, Seán Mac
     Diarmada). The Irish Volunteers: MacNeill's "The North Began" (1913); founding (November
     1913); Cumann na mBan (1914); Howth gun-running (July 1914); Redmond's control and the
     September 1914 split.
   - Exam: Parnell's achievements and failures, strengths and weaknesses (2012, 2018, 2021,
     2023); Carson or Redmond (2008, 2024); first Sinn Féin (2015).
   - SimpleStudy: Home Rule and Advanced Nationalism.
5. **Unionism and the Ulster Question, 1870–1914** [I2 P; S]
   - Syllabus: unionism and the Ulster Question.
   - Key personalities: Edward Carson.
   - Key concepts: militarism; democracy.
   - Cover: who unionists were (Ulster Protestants of all classes; southern unionists,
     landlords and business); reasons for opposition: religion ("Home Rule is Rome Rule"), the
     economy (Belfast's industries and the imperial market), and identity and empire; the
     Orange Order revival; the Irish Loyal and Patriotic Union (1885) and Ulster organisation
     (1886); opposition to the 1893 Bill (the Ulster Convention 1892); the Ulster Unionist
     Council (1905); Carson becomes leader (1910) and James Craig is his organiser; the
     Conservative alliance (Bonar Law's Blenheim speech, 1912); the Solemn League and Covenant
     (28 September 1912) *(verify signatory numbers)*; the Ulster Volunteer Force (1913); the
     Larne gun-running (April 1914); the Curragh incident (March 1914); exclusion proposals and
     the Buckingham Palace Conference (July 1914); Carson's successes and failures.
   - Exam: why and how unionism developed and opposed Home Rule (2009, 2011, 2012, 2015, 2021,
     2022); how effective unionism was in resisting Home Rule (2016, 2025); unionist
     achievements (2020); Carson (2010, 2017, 2019, 2023); Carson or Redmond (2008, 2024).
   - SimpleStudy: Unionism and the Ulster Question.
6. **The suffrage movement and educational reforms** [I2 P; S]
   - Syllabus: the Suffrage movement; educational reforms: schools and universities.
   - Key personalities: Isabella Tod; Hanna Sheehy-Skeffington.
   - Key concepts: feminism; suffragette; democracy.
   - Cover: Isabella Tod (the Belfast suffrage society of 1872, married women's property,
     girls' education, unionism); Anna and Thomas Haslam and the Dublin women's suffrage
     association (1876); women poor law guardians and the Local Government Act (1898); the
     Irish Women's Franchise League (1908, Hanna Sheehy-Skeffington and Margaret Cousins);
     the Irish Citizen; militancy in 1912 (window-breaking, Asquith's Dublin visit, prison and
     hunger strike); the Irish Party's opposition (Redmond and Dillon); suffragists divided
     over nationalism and unionism. Educational reforms: the Intermediate Education Act (1878)
     and the payment-by-results system; the Royal University (1879) and women graduates;
     Alexandra College and convent schools; the Irish Universities Act (1908: NUI and Queen's
     University Belfast); Irish compulsory for NUI matriculation (decided 1910, applied from
     1913 *(verify)*); the 1900 revised primary programme.
   - Exam: the history of women: suffrage, Tod, Sheehy-Skeffington (2012, 2015, 2017, 2019,
     2021, 2025); suffrage as controversy (2013); education (2024).
   - SimpleStudy: suffrage; education and Catholic identity.
7. **Unionisation of the working classes and the Dublin strike and lockout, 1913** [I2 S;
   S-CS; DBQ source]
   - Syllabus: unionisation of the working classes. Case study: **Dublin 1913 — strike and
     lockout**.
   - Key personalities: James Larkin; James Connolly.
   - Key concepts: socialism.
   - Cover: Dublin's urban poverty (tenements, death rates, unskilled casual labour; the
     Church Street collapse, September 1913); craft unions vs "new unionism"; the Irish Trades
     Union Congress (1894); Connolly's Irish Socialist Republican Party (1896) and writings;
     Larkin's 1907 Belfast dock strike; the ITGWU (1909); the sympathetic strike and
     "Larkinism"; the Irish Labour Party (1912). Case study in depth: William Martin Murphy and
     the Dublin Employers' Federation; the tram strike (26 August 1913, Horse Show week); the
     O'Connell Street meeting and baton charges ("Bloody Sunday", 31 August); the employers'
     "document" and the lockout *(verify numbers locked out)*; British TUC food ships; the
     "Save the Kiddies" scheme and Archbishop Walsh; the Askwith inquiry; the Irish Citizen
     Army (November 1913); the drift back to work (early 1914); outcomes and significance;
     views of Murphy, Larkin, the Church, nationalists and the press (e.g. Yeats's
     "September 1913" and press cartoons as document types).
   - Exam: why 1913 happened, how it ran and its outcome (2009, 2016, 2022, 2023); land
     agitation or 1913 (2013, 2019); Larkin and/or Connolly (2011, 2018, 2021, 2025); urban
     poverty (2008, 2010).
   - SimpleStudy: working-class unionisation; Dublin 1913 Strike and Lockout case study.
8. **The co-operative movement and industrial Belfast: the shipyards** [I2 S]
   - Syllabus: the Co-operative Movement; industrial development in Belfast: the shipyards.
   - Cover: Horace Plunkett, the first co-operative creamery (Dromcollogher, 1889 *(verify)*),
     the IAOS (1894), credit societies, the Recess Committee and the Department of
     Agriculture and Technical Instruction (1899), nationalist and unionist suspicion, and
     results; Belfast: Harland and Wolff (Edward Harland, Gustav Wolff, William Pirrie) and
     Workman Clark; the Olympic-class liners (Titanic 1911–12); linen, ropeworks, engineering,
     tobacco; population growth to the largest city in Ireland *(verify date)*; working
     conditions; sectarian employment and the shipyard expulsions; links to unionism; Belfast
     vs Dublin.
   - Exam: Belfast industry and/or the co-operative movement (2009, 2010, 2013, 2017, 2018,
     2020, 2021).
   - SimpleStudy: society and economy.
9. **Case study: the GAA to 1891** [I2 C-CS; DBQ source]
   - Syllabus: the GAA. Case study: **the GAA to 1891**.
   - Key concepts: anglicisation/de-anglicisation; Irish Ireland.
   - Cover: the state of Irish sport before 1884 (athletics under English rules, the decline
     of hurling); Michael Cusack and Maurice Davin; Hayes' Hotel, Thurles (1 November 1884);
     the patrons Archbishop Croke, Parnell and Davitt, and Croke's letter; the first rules;
     the ban on "foreign" games and on RIC members; clubs based on parishes; IRB infiltration
     and the clerical reaction; Cusack's removal (1886); the 1887 Thurles convention split;
     the first All-Ireland championships; the American "invasion" tour (1888); the Parnell
     split and the collapse in membership by 1891; why the GAA survived. Document types the
     SEC used in 2007: Davitt's and others' letters and speeches of support, reports of
     meetings.
   - Exam: the 2007 DBQ (part (d) how the GAA dealt with its difficulties 1884–1891); the GAA
     1884–1891 (2015); GAA vs Gaelic League (2010, 2023); GAA and/or other movements (2017,
     2018, 2020, 2022, 2024, 2025).
   - SimpleStudy: GAA to 1891 case study.
10. **Cultural revivals and the consolidation of Catholic identity** [I2 C]
    - Syllabus: cultural revivals — the Gaelic League, the Anglo-Irish Literary Revival; the
      consolidation of Catholic identity. (The GAA after 1891 belongs here too.)
    - Key personalities: Douglas Hyde; W.B. Yeats.
    - Key concepts: anglicisation/de-anglicisation; Irish Ireland; Anglo-Irish.
    - Cover: Hyde's 1892 lecture on de-anglicising Ireland; the Gaelic League (1893, Hyde and
      MacNeill), its activities (classes, timirí, feiseanna, An Claidheamh Soluis), its
      successes (Irish in schools, St Patrick's Day, NUI matriculation) and politicisation
      (Pearse; Hyde's 1915 resignation as later context); D.P. Moran and "Irish Ireland";
      the Anglo-Irish Literary Revival: Yeats, Lady Gregory, Synge, the Irish Literary
      Theatre (1899), the Abbey (1904), The Playboy of the Western World riots (1907), the
      Hugh Lane gallery dispute; tensions between "Anglo-Irish" and "Irish Ireland" visions;
      the GAA's recovery after 1891 and its links to the IRB. Consolidation of Catholic
      identity: church building and devotional life; control of schools; Maynooth and the
      clergy's social position; confraternities and sodalities; the Pioneer Total Abstinence
      Association (1898); the Ne Temere decree (1908); the Catholic middle class; how Catholic
      and nationalist identity merged, and the unionist reaction.
    - Exam: GAA, Gaelic League and Literary Revival as controversy or contribution (2008,
      2011, 2013, 2016, 2020); Hyde and/or Yeats (2011, 2018); cultural and religious
      identities (2019); GAA or Gaelic League (2010, 2023, 2025).
    - SimpleStudy: cultural nationalism; Literary Revival; education and Catholic identity.
11. **Working with evidence: history, the historian and the documents-based question** [Part I
    A–B, pp. 8–10, 15; Guidelines pp. 12–13, 24–32]
    - Syllabus: what is history (the past itself, surviving evidence, written histories); the
      provisional nature of historical knowledge; the role of evidence; the main varieties of
      evidence (public records, private institutions' records, letters, memoirs, eyewitness
      accounts, maps, photographs, political cartoons, oral testimony, radio and TV
      transcripts); repositories (archives, libraries, museums; which sources each holds);
      how the historian interrogates evidence (who, why, when, in what circumstances, for what
      audience); stages of research; objectivity; revising views in the light of new
      evidence; source vs evidence; fact vs opinion; bias and objectivity; propaganda;
      strengths and limitations of sources; primary vs secondary. The DBQ format:
      comprehension, comparison, criticism, contextualisation.
    - Cover: each concept defined with an example drawn from the three `hist-ire2` case
      studies; a method for each DBQ part (comprehension: answer from the named document only;
      comparison: a specific similarity or difference in both; criticism: provenance, purpose,
      viewpoint, reliability, bias and propaganda, with a cited line; how to read a cartoon or
      photograph); how part (d) differs (own knowledge of the topic, not retelling the
      documents); typical questions on usefulness, primary/secondary, fact/opinion and
      propaganda. Use no past-paper document text. Keep it to what the DBQ tests; the
      research study is outlined in Appendix B.
    - Exam: every DBQ's parts (a)–(c), 2006–2025, e.g. strengths and weaknesses of a document
      as a source (2006), whether a cartoon is anti-Irish (2006), fact vs opinion (2015).
    - SimpleStudy: Assessment (Written Exam).

### hist-ire3 — The pursuit of sovereignty and the impact of partition, 1912–1949 [I3]

Key personalities: Patrick Pearse; Éamon de Valera; Arthur Griffith; Michael Collins; Countess
Markievicz; W.T. Cosgrave; James J. McElligott; James Craig; Richard Dawson Bates; Evie Hone.
Key concepts: sovereignty; partition; Ulster Unionism; allegiance; physical force; IRB/IRA;
"blood sacrifice"; dominion status; republic; free trade; protectionism; neutrality;
discrimination; conformity/censorship.

1. **The Home Rule Bill, World War I and the 1916 Rising, 1912–1916** [I3 P]
   - Syllabus: the Home Rule Bill, 1912–1914; the impact of World War I; the 1916 Rising.
   - Key personalities: Patrick Pearse; Countess Markievicz (part 1).
   - Key concepts: physical force; IRB/IRA; "blood sacrifice".
   - Cover: the Third Home Rule Bill's terms and passage under the Parliament Act;
     unionist and nationalist mobilisation (cross-refer to `hist-ire2-s4`, `hist-ire2-s5`
     for detail); suspension in September 1914 and the Amending Bill; World War I: Redmond's
     Woodenbridge speech and the split, recruitment, the 10th, 16th and 36th Divisions, the
     Somme, economic effects; the IRB Military Council, Casement and Germany, the Aud,
     MacNeill's countermand; Easter Week in Dublin (GPO and garrisons, the Proclamation,
     Markievicz at St Stephen's Green), surrender, casualties and damage; the executions
     (May 1916), martial law and the shift in opinion; Pearse's ideas ("blood sacrifice") and
     career; contemporary and later views of the Rising.
   - Exam: the Rising's events and whether Ireland was "changed utterly" (2016); military and
     political significance (2019); Pearse's aims and achievements (2007, 2011, 2021);
     tensions from the Bill, WWI and 1918 (2023); a decade of revolutionary change (2024).
   - SimpleStudy: 1912 to Easter 1916.
2. **The second Sinn Féin, the 1918 election and the War of Independence, 1917–1921** [I3 P]
   - Syllabus: the rise of the second Sinn Féin party; the 1918 election; the War of
     Independence.
   - Key personalities: Michael Collins; Éamon de Valera (part 1); Markievicz (part 2).
   - Key concepts: republic; sovereignty; IRB/IRA.
   - Cover: the 1917 by-elections; the October 1917 Ard Fheis and de Valera's presidency; the
     conscription crisis (1918) and the "German Plot"; the December 1918 election, its
     results and Markievicz's election; the First Dáil (21 January 1919), the Declaration of
     Independence and the Democratic Programme; Soloheadbeg; the Dáil courts, the Dáil loan,
     the counter-state; Collins's intelligence network and the Squad; the RIC, Black and Tans
     and Auxiliaries; Bloody Sunday (November 1920); Kilmichael and flying columns; the burning
     of Cork; reprisals and British opinion; the truce (July 1921); de Valera in America
     (cross-refer to `hist-ire4-s5`); why the British negotiated.
   - Exam: the fortunes and development of Sinn Féin 1912–1923 (2013, 2018); the rise of SF and
     decline of Home Rule (2025); the threat and use of physical force (2012); attempts to win
     self-government 1912–1921 (2020).
   - SimpleStudy: path towards independence.
3. **Partition and Northern Ireland under the Unionist Party, 1912–1949** [I3 P; S]
   - Syllabus: Partition; Northern Ireland — the Unionist Party in power; impact of partition on
     economy and society.
   - Key personalities: James Craig; Richard Dawson Bates.
   - Key concepts: partition; Ulster Unionism; discrimination.
   - Cover: the factors behind partition (unionist resistance, exclusion debates 1914–16,
     1918 results, British policy); the Government of Ireland Act (1920); the first Northern
     Ireland parliament (1921) and Craig; violence in 1920–22, the Special Constabulary and the
     Special Powers Act (1922); the Boundary Commission (1924–25); abolition of PR (local 1922,
     Stormont 1929), gerrymandering and discrimination in housing and jobs; nationalist
     abstention; Dawson Bates at Home Affairs; Craig's "Protestant parliament and a Protestant
     state" speech; the effect of partition on the economy and society, North and South; the
     inter-war depression in Northern Ireland (shipbuilding and linen, unemployment, the 1932
     Outdoor Relief riots); Craig's strengths and weaknesses.
   - Exam: factors in partition (2006, 2010, 2017, 2022); how the Unionist government dealt
     with challenges, the nationalist minority, the economy and security (2008, 2009, 2010,
     2012, 2022, 2023, 2024); Craig (2016).
   - SimpleStudy: establishment of Northern Ireland.
4. **Case study: the Treaty negotiations, October–December 1921** [I3 P-CS]
   - Syllabus: case study **the Treaty negotiations, October–December 1921**; Treaty.
   - Key personalities: Arthur Griffith; Collins (role in the negotiations); de Valera (role).
   - Key concepts: dominion status; allegiance; sovereignty.
   - Cover: the July 1921 de Valera–Lloyd George talks; external association; why de Valera
     stayed at home; the delegation (Griffith, Collins, Barton, Duggan, Gavan Duffy; Childers as
     secretary) and the plenipotentiary issue; the British team; the issues (Crown and oath,
     Ulster and the Boundary Commission offer, defence and ports, finance); key moments
     (Griffith's letter of assurance; the final ultimatum and the threat of "immediate and
     terrible war"); the signing (6 December 1921); the terms; the Dáil debates and the vote
     (64–57, 7 January 1922); Griffith's role and character; the views of both sides then and
     of historians since.
   - Exam: why the negotiations and terms were controversial (2009, 2016, 2018, 2021); Treaty
     and Civil War (2008); de Valera in the negotiations and the Civil War (2025).
   - SimpleStudy: Treaty and Civil War.
5. **The Civil War, state building and the consolidation of democracy, 1922–1932** [I3 P]
   - Syllabus: Treaty and Civil War; state building and the consolidation of democracy.
   - Key personalities: W.T. Cosgrave.
   - Key concepts: republic; physical force; dominion status.
   - Cover: the split; the Provisional Government; the Four Courts and the start of the Civil
     War (June 1922); the course of the war; the deaths of Griffith and Collins; the
     Emergency Powers Act and the executions *(verify number)*; the ceasefire (May 1923);
     legacy. State building under Cosgrave: the 1922 Constitution; the unarmed Garda
     Síochána; the courts and civil service; the Army Mutiny (1924); the Boundary Commission
     crisis (1925); Kevin O'Higgins and the Public Safety Acts; the Electoral Amendment Act and
     Fianna Fáil entering the Dáil (1927); the Shannon Scheme and ESB; the peaceful transfer of
     power in 1932; Cosgrave's strengths and weaknesses.
   - Exam: the Cosgrave governments' foundations (2006); consolidating democracy (2008, 2011);
     threats to the state (2018).
   - SimpleStudy: Cumann na nGaedheal.
6. **De Valera in power, Anglo-Irish relations and from Free State to Republic, 1932–1949**
   [I3 P]
   - Syllabus: from Free State to Republic; Anglo-Irish relations.
   - Key personalities: Éamon de Valera (part 2 and overall evaluation).
   - Key concepts: sovereignty; republic; dominion status; allegiance.
   - Cover: Anglo-Irish relations under Cosgrave (the Commonwealth, imperial conferences, the
     Statute of Westminster 1931); Fianna Fáil's founding (1926) and 1932 victory;
     dismantling the Treaty (removing the oath, downgrading the Governor-General, the External
     Relations Act 1936); the Economic War over land annuities; the Blueshirts; Bunreacht na
     hÉireann (1937), with articles 2–3, 41, 44 and the President; the 1938 Anglo-Irish
     Agreements (ports, annuity settlement, trade); wartime relations (cross-refer to s8); the
     inter-party government, the Republic of Ireland Act (1948, in force 1949) and the
     Ireland Act (1949); de Valera's successes and failures; Cosgrave or de Valera in
     Anglo-Irish relations.
   - Exam: Anglo-Irish relations 1923–1949 (2007, 2012, 2019); under de Valera (2013);
     Cosgrave or de Valera (2010, 2017, 2023); de Valera's strengths, weaknesses, successes and
     failures (2011, 2020, 2024).
   - SimpleStudy: Fianna Fáil 1932–1939; Free State to Republic.
7. **Economy and society: world crisis and from free trade to protectionism, 1922–1945** [I3 S]
   - Syllabus: impact of world economic crisis; from free trade to protectionism; impact of
     partition on economy (South).
   - Key personalities: James J. McElligott.
   - Key concepts: free trade; protectionism.
   - Cover: the Free State's inheritance; Cumann na nGaedheal's free-trade, agriculture-led
     policy (Patrick Hogan); fiscal conservatism (the 1924 pension cut); McElligott at
     Finance and his influence; the Tariff Commission; the Wall Street Crash and depression;
     Fianna Fáil's protectionism (tariffs, the Control of Manufactures Acts, the Industrial
     Credit Company, semi-state bodies); the Economic War's effect on cattle farmers; housing
     and social policy; emigration; results by 1939; why economic success was hard to achieve.
   - Exam: governments and economic or social problems, 1922–1945 (2013, 2016, 2020, 2022);
     de Valera's economy vs Anglo-Irish relations (2009); McElligott (2021).
   - SimpleStudy: Cumann na nGaedheal; Fianna Fáil 1932–1939.
8. **The impact of World War II on independent Ireland** [I3 P; S]
   - Syllabus: the impact of World War II (South); impact of World War II on economy and
     society.
   - Key concepts: neutrality; conformity/censorship.
   - Cover: neutrality and its reasons; the Emergency Powers Act (1939); censorship; the
     Defence Forces and LDF; Lemass and the Department of Supplies; rationing and shortages;
     Irish Shipping; turf; internment of the IRA; relations with Britain (Churchill, the ports,
     the 1940 unity offer) and the USA (the American Note, 1944); help to the Allies; the North
     Strand bombing (1941); de Valera's condolences on Hitler's death and the Churchill
     exchange (May 1945); emigration and war work in Britain; the effects on the economy and
     society.
   - Exam: impact of WWII North and South (2006, 2013, 2017, 2021).
   - SimpleStudy: WWII in the South.
9. **Northern Ireland during World War II and case study: Belfast during World War II** [I3 P;
   S-CS]
   - Syllabus: the impact of World War II (North). Case study: **Belfast during World War II**.
   - Key concepts: neutrality (as seen from the North); Ulster Unionism.
   - Cover: Northern Ireland's war role (shipbuilding, aircraft at Short Brothers, munitions,
     linen, agriculture); conscription not applied (1941); poor air-raid preparation;
     the Belfast Blitz (April and May 1941): targets, casualties and damage *(verify)*,
     Dublin's fire brigades; evacuation and what it revealed about poverty; American troops
     (from 1942); the Andrews and Brooke governments; unemployment and industrial unrest;
     social and political effects (housing, the welfare state's origins, the Labour vote);
     how far Belfast in 1945 differed from 1939.
   - Exam: Belfast 1939 vs 1945 (2007); WWII's effect on Northern Ireland (2011, 2019, 2025).
   - SimpleStudy: Belfast in WWII case study.
10. **State and culture, North and South: language, religion, education and cultural identity,
    1920–1949** [I3 C]
    - Syllabus: state and culture, North and South — language, religion and education;
      promotion of cultural identity.
    - Key personalities: Evie Hone.
    - Key concepts: conformity/censorship; discrimination.
    - Cover: the South: compulsory Irish in schools and the civil service; the Gaeltacht
      Commission (1926); An Gúm; the Irish Folklore Commission (1935); the Catholic ethos
      (the divorce ban 1925, the Censorship of Films Act 1923, the Censorship of Publications
      Act 1929, the ban on contraceptives 1935, Article 44); the Tailteann Games (1924); 2RN
      (1926); the Abbey; Evie Hone's stained glass (An Túr Gloine) as an expression of Irish
      identity; the results of the language policy. The North: the Lynn Committee and the
      Londonderry Education Act (1923), Church opposition and the 1925 and 1930 amendments;
      the Protestant ethos; Orange and loyalist culture; the Irish language and nationalist
      culture in the North.
    - Exam: attempts to promote cultural identity North and South (2006, 2007, 2009, 2020,
      2025); a Gaelic and Catholic society (2018); language policy (2010, 2017, 2023); Hone
      (2021).
    - SimpleStudy: cultural identity North and South.
11. **Case study: the Eucharistic Congress, 1932** [I3 C-CS]
    - Syllabus: case study **the Eucharistic Congress, 1932**.
    - Key concepts: conformity/censorship; sovereignty (international standing).
    - Cover: what a Eucharistic Congress is; why Dublin (the 1,500th anniversary of Patrick's
      mission); the preparations under Cosgrave and the change of government in 1932;
      de Valera's handling, and the snub to the Governor-General; the papal legate
      (Cardinal Lauri) and his arrival; the events of 21–26 June 1932 (the children's mass,
      the Phoenix Park mass, John McCormack, the O'Connell Bridge benediction); attendance and
      organisation (radio, the loudspeaker system, decorations in the slums); the attacks on
      northern pilgrims; significance for Church–state relations, Catholic identity, the
      Free State's image abroad, and unionist perceptions. The 2015 DBQ used it.
    - Exam: the 2015 DBQ (part (d) its significance); main events and significance (2008,
      2012, 2019, 2021, 2022, 2024); the Congress and/or language policy (2010, 2017, 2023).
    - SimpleStudy: Eucharistic Congress case study.

### hist-ire4 — The Irish diaspora, 1840–1966 [I4]

Key personalities: John Devoy; Andrew Bonar Law; Joe Kennedy; Boss Croker; Archbishop Mannix;
Domhnall Mac Amhlaigh; Paul O'Dwyer; Bishop Edward Galvin; Maureen O'Hara; Mother Mary Martin.
Key concepts: pre-paid passages; chain-emigration; emigrants' remittances; discrimination;
assimilation; "Ireland's spiritual empire".

1. **Emigration before and during the Famine, 1840–1855, and case study: Grosse Isle** [I4 S;
   S-CS]
   - Syllabus: the main trends in Irish emigration by origin, destination and type of
     emigrant, their occupations and where they settled: pre-1845; the Famine decade,
     1845–1855. Case study: **Grosse Isle**.
   - Key concepts: pre-paid passages; chain-emigration.
   - Cover: pre-Famine emigration (Ulster Presbyterians, then Catholics from the south;
     destinations in British North America, the USA and Britain; seasonal migration); Famine
     emigration: numbers *(verify)*, assisted emigration by landlords, routes via Liverpool,
     "coffin ships", fares and conditions, ports of arrival; the push and pull factors.
     Grosse Isle in depth: the quarantine station near Quebec (opened 1832); the 1847 season
     (the queue of ships, fever and sheds, deaths, Dr Douglas, clergy who died), orphans
     adopted by French-Canadian families, comparison with Partridge Island and New York, the
     Celtic cross memorial (1909), and its place in memory and heritage.
   - Exam: factors at home and abroad in emigration, 1840–1914 (2006, 2009, 2024); main
     trends 1840–1920 (2007); Grosse Isle (2008, 2010, 2012, 2015, 2019, 2024).
   - SimpleStudy: none.
2. **Emigration, 1855–1914 and 1920–1966; restriction and regulation after 1920** [I4 S]
   - Syllabus: main trends 1855–1914 and 1920–1966; increased restriction and regulation of
     emigration after 1920.
   - Key personalities: Domhnall Mac Amhlaigh.
   - Key concepts: emigrants' remittances; chain-emigration; assimilation.
   - Cover: post-Famine emigration as a way of life (the "American wake", young single women,
     emigration from the west); occupations and settlement in the USA (cities of the
     north-east, labour, domestic service, police, politics), Britain (Liverpool, Glasgow,
     London, Manchester) and Australia; assisted passages; remittances; US restriction after
     1920 (quota acts of 1921 and 1924); the shift to Britain from the 1930s; wartime travel
     permits; post-war reconstruction work (building, nursing, factories); the Commission on
     Emigration (1948–54); 1950s emigration; Irish centres and welfare; Mac Amhlaigh's
     Dialann Deoraí (1960; translated as An Irish Navvy) as a source on navvy life;
     assimilation in Britain vs the USA.
   - Exam: trends 1920–1966 (2006, 2010, 2013); why Britain and how far assimilated (2009,
     2016, 2019, 2021, 2023); the Irish in Britain (2011, 2020); how emigration changed lives
     (2022, 2023); Mac Amhlaigh (2008, 2012, 2022).
   - SimpleStudy: none.
3. **The Irish in the USA and Britain: anti-Irish sentiment and political participation** [I4 P]
   - Syllabus: anti-Irish sentiment in both the US and Britain in the 19th century; Irish
     participation in politics in the USA and in Britain; the Molly Maguires.
   - Key personalities: Boss Croker; Joe Kennedy; Paul O'Dwyer.
   - Key concepts: discrimination; assimilation.
   - Cover: anti-Irish sentiment and its causes (religion, poverty, disease, crime, competition
     for work, racial stereotypes) in the USA (nativism, the Know-Nothings, Thomas Nast's
     cartoons, "No Irish Need Apply") and Britain (Punch caricatures, the Stockport riots 1852,
     Murphy riots, Fenian scares); Irish political participation in the USA (the Democratic
     Party, ward politics, Tammany Hall, Croker's career, Irish mayors, the Kennedys: Joe
     Kennedy as businessman and ambassador to Britain, 1938–40) and in Britain (Irish voters,
     T.P. O'Connor in Liverpool, Labour); Paul O'Dwyer (New York lawyer, civil rights, Irish
     causes); the Molly Maguires in the Pennsylvania anthracite fields (1870s, the Pinkerton
     informer, the trials and hangings, labour vs nationalist interpretations).
   - Exam: anti-Irish sentiment (2006, 2009, 2010, 2018); participation in politics (2007);
     the Molly Maguires, Croker, Kennedy (2012, 2015, 2020, 2022, 2023); challenges and
     opportunities in North America (2013, 2017, 2021).
   - SimpleStudy: none.
4. **Irish nationalism and Ulster Unionism as international forces** [I4 P]
   - Syllabus: Irish nationalism as an international force from the Famine to independence;
     the anti-partition campaign; Ulster Unionist efforts to lobby for international support
     among Ulster emigrants.
   - Key personalities: John Devoy; Andrew Bonar Law.
   - Cover: the Fenian Brotherhood and the Canadian raids; Clan na Gael; Devoy's career (Fenian
     prisoner, exile, the Catalpa rescue 1876, the New Departure, the Gaelic American, 1916
     funding, the split with de Valera); Parnell's and Davitt's American tours and Land League
     funds; Irish-America and the Rising; the Friends of Irish Freedom; Irish nationalism in
     Britain and Australia; the anti-partition campaign after 1945 (the Anti-Partition League,
     de Valera's 1948 world tour, Irish-American lobbying); Ulster Unionist lobbying: the
     Scotch-Irish/Ulster-Scots identity in North America, Canadian and Australian Orange
     support; Bonar Law (born in New Brunswick to an Ulster Presbyterian father; Conservative
     leader 1911; Blenheim speech 1912; his role in Home Rule and partition).
   - Exam: Irish nationalists and/or unionists seeking support abroad (2008, 2016, 2018,
     2019); Devoy and/or Bonar Law (2012, 2016, 2024).
   - SimpleStudy: none.
5. **Case study: de Valera in America, June 1919–December 1920** [I4 P-CS]
   - Syllabus: case study **de Valera in America, June 1919–December 1920**.
   - Cover: why he went (recognition of the Republic, funds, influencing the Paris Peace
     Conference and the 1920 presidential election); his escape from Lincoln jail and arrival;
     the tour of cities and its reception; the Dáil bond drive *(verify the sum raised)*;
     approaches to the Republican and Democratic conventions (1920); the conflict with Devoy
     and Judge Cohalan and the Friends of Irish Freedom; the Westminster Gazette "Cuba"
     interview (February 1920); the American Association for the Recognition of the Irish
     Republic (November 1920); what happened in Ireland while he was away; success or failure,
     and views of it then and since.
   - Exam: success, importance, controversy, aims achieved (2006, 2007, 2011, 2020, 2023).
   - SimpleStudy: none.
6. **The Catholic Church, the GAA, Protestant churches and the Orange Order abroad** [I4 C]
   - Syllabus: role of the Catholic Church and GAA in sustaining a sense of Irishness among
     emigrants; role of Protestant churches in fostering an Ulster-Scottish identity; the
     Orange Order in Canada and Australia.
   - Key personalities: Archbishop Mannix.
   - Cover: the Catholic Church abroad (Irish priests and bishops in the USA, Britain and
     Australia; parishes, schools, hospitals, social organisations; Irish dominance of the
     American hierarchy); Mannix's career in Melbourne (the 1916–17 conscription referendums,
     support for Irish independence, his 1920 removal from a ship to stop him landing in
     Ireland); the GAA abroad (clubs, the 1888 American tour, New York GAA); Protestant churches
     (Presbyterian and Methodist congregations, Ulster-Scots identity in the USA and Canada);
     the Orange Order in Canada (Toronto, political power) and Australia; assimilation vs
     preservation of identity.
   - Exam: Church and GAA in sustaining Irishness (2007); the Church in the diaspora (2010,
     2018); Protestant churches, the Orange Order, Ulster-Scots identity (2015, 2021);
     Mannix (2016, 2017, 2019, 2022).
   - SimpleStudy: none.
7. **Irish missionaries in Africa and Asia; case study: the Holy Ghost mission to Nigeria,
   1945–1966** [I4 C; C-CS]
   - Syllabus: Irish missionaries in Africa and Asia. Case study: **the Holy Ghost mission to
     Nigeria, 1945–1966**.
   - Key personalities: Bishop Edward Galvin; Mother Mary Martin.
   - Key concepts: "Ireland's spiritual empire".
   - Cover: the missionary movement and why Ireland supplied so many (vocations, the
     "spiritual empire" idea); Galvin and the Maynooth Mission to China (the Columbans),
     Hanyang, wars, and expulsion by the Communists *(verify dates)*; Mary Martin and the
     Medical Missionaries of Mary (Nigeria, Drogheda); other orders (Kiltegan, SMA, the Holy
     Rosary Sisters). Case study in depth: the Holy Ghost Fathers (Spiritans) in south-eastern
     Nigeria — the earlier work of Bishop Shanahan as background; the 1945–1966 expansion of
     schools, teacher training, hospitals and parishes; numbers of Irish priests and sisters;
     relations with the colonial government and with Nigerian independence (1960); the
     education emphasis; achievements and criticisms; the eve of the Biafran war (1967) as
     the end point.
   - Exam: missionaries' impact and success (2008, 2011, 2017, 2021, 2024); the Holy Ghost
     mission (2009, 2013, 2016, 2020); spiritual empire (2019); Martin or Galvin (2010, 2013,
     2022).
   - SimpleStudy: none.
8. **Images of Ireland: film, music, tourism and heritage, and John F. Kennedy** [I4 C]
   - Syllabus: the creation of Irish images through film and music; links between Ireland and
     the wider Irish community through tourism and heritage; the impact of John F. Kennedy.
   - Key personalities: Maureen O'Hara.
   - Cover: Hollywood's Irish (stereotypes; John Ford; The Quiet Man, 1952, and its effect on
     tourism; O'Hara's career and image); music (Irish-American song, John McCormack,
     céilí bands, the Clancy Brothers and the 1960s folk boom); tourism and heritage (Bord
     Fáilte, An Tóstal 1953, Shannon airport, "roots" tourism, genealogy); JFK: his Irish
     ancestry, the 1960 election as acceptance of Irish Catholics, his June 1963 visit to
     Ireland, his impact on Irish self-image and Irish-America. Joe Kennedy's profile is in s3.
   - Exam: film and music and/or tourism and heritage (2017, 2018); JFK (2013, 2022); O'Hara
     (2020, 2022, 2023).
   - SimpleStudy: none.

### hist-ire5 — Politics and society in Northern Ireland, 1949–1993 [I5]

Key personalities: Terence O'Neill; Conn and Patricia McCluskey; Bernadette Devlin; Ian
Paisley; Brian Faulkner; John Hume; James Molyneaux; Margaret Thatcher; Gerry Adams; Seamus
Heaney. Key concepts: Civil Rights; gerrymandering; terrorism; power sharing; sectarianism;
bigotry; tolerance and intolerance; cultural traditions; cultural identity; ecumenism;
propaganda.

1. **Brookeborough's Northern Ireland and the welfare state, 1949–1963** [I5 P; S]
   - Syllabus: from Brookeborough (to O'Neill); impact of the Welfare State: education, health,
     housing; social and economic developments prior to 1969.
   - Key concepts: gerrymandering; sectarianism; discrimination (as context).
   - Cover: the Ireland Act (1949) guarantee; Brookeborough's premiership (1943–63) and his
     attitudes; the welfare state: the NHS (1948), the Education Act (Northern Ireland) 1947
     and the eleven-plus, the Housing Trust and council housing; their effect on the
     Catholic minority (the new educated middle class); the decline of shipbuilding and linen;
     unemployment; new industry and its location east of the Bann; the IRA border campaign
     (1956–62); discrimination in housing, jobs and local voting; Brookeborough's successes and
     failures.
   - Exam: welfare state and social/economic developments (2006, 2007, 2008, 2013, 2015, 2017,
     2018, 2020, 2021); Brookeborough or O'Neill (2009, 2019); Brookeborough (2024).
   - SimpleStudy: emergence of Northern Ireland; welfare state and Brookeborough.
2. **O'Neill and the Civil Rights movement, 1963–1969** [I5 P]
   - Syllabus: (from Brookeborough) to O'Neill; the Civil Rights movement.
   - Key personalities: Terence O'Neill; Conn and Patricia McCluskey; Bernadette Devlin; Ian
     Paisley (part 1).
   - Key concepts: Civil Rights; gerrymandering; tolerance and intolerance.
   - Cover: O'Neill's modernisation (economic planning, the Matthew and Wilson plans,
     bridge-building gestures, the 1965 Lemass meetings); unionist critics; Paisley's
     background, the Free Presbyterian Church and the "O'Neill must go" campaign; the
     Campaign for Social Justice (1964, the McCluskeys, Dungannon housing); NICRA (1967) and
     its demands; Caledon (June 1968); Derry, 5 October 1968; O'Neill's five-point reform
     package and "Ulster at the crossroads" speech; People's Democracy and Burntollet
     (January 1969); the February 1969 election; Devlin's election (April 1969); O'Neill's
     resignation; how successful O'Neill and the movement were; contemporary and later views.
   - Exam: O'Neill's contribution, success or failure (2006, 2012, 2015, 2017, 2018, 2019,
     2021); why the Civil Rights movement emerged and whether it succeeded (2008, 2017);
     Paisley (2015, 2017, 2020); Devlin (2012, 2016, 2018).
   - SimpleStudy: O'Neill years.
3. **Case study: the Coleraine University controversy** [I5 S-CS]
   - Syllabus: case study **the Coleraine University controversy**.
   - Key personalities: John Hume (part 1: the University for Derry campaign).
   - Key concepts: discrimination; propaganda.
   - Cover: Magee College's position; the Lockwood Committee (1963–65) and its terms; the
     University for Derry Committee (Hume as chair; cross-community support); the motorcade
     to Stormont (February 1965); the report choosing Coleraine (February 1965); the "faceless
     men" allegation; the Stormont debate and vote; the New University of Ulster (opened
     1968); related "west of the Bann" grievances (the Benson rail closures, Craigavon new
     city, Derry's economic decline); significance for Derry, for Hume's career and for the
     civil rights movement.
   - Exam: the 2022 DBQ (documents on the University for Derry campaign; part (d) how
     Coleraine and other issues raised tension in Derry); the controversy (2008, 2009, 2012,
     2016, 2019, 2024).
   - SimpleStudy: Coleraine University controversy case study.
4. **The outbreak of the Troubles: from 1969 to Direct Rule, 1972** [I5 P]
   - Syllabus: emergence of the Provisional IRA; the fall of Stormont; Direct Rule; Republican
     and Loyalist terrorism (beginning).
   - Key personalities: Brian Faulkner (part 1: as Prime Minister).
   - Key concepts: terrorism; sectarianism.
   - Cover: August 1969 (the Battle of the Bogside, the Belfast riots, British troops
     deployed); the Hunt Report, disbanding the B Specials, RUC reform; the IRA split and the
     Provisionals (1969–70); the Falls curfew (1970); the SDLP (1970) and Alliance; Loyalist
     paramilitaries (the UVF, the UDA 1971); Chichester-Clark; Faulkner's premiership (1971–72);
     internment (August 1971); Bloody Sunday (30 January 1972); the suspension of Stormont and
     Direct Rule (March 1972) and why it lasted; Bloody Friday and Operation Motorman (July
     1972); why the Troubles erupted and why they lasted so long.
   - Exam: why Direct Rule was introduced and lasted (2006); fall of Stormont (2007); how the
     Troubles erupted and lasted (2018); Faulkner (2013, 2016, 2018).
   - SimpleStudy: beginning of the Troubles.
5. **Case study: the Sunningdale Agreement and the power-sharing executive, 1973–1974** [I5
   P-CS]
   - Syllabus: case study **the Sunningdale Agreement and the power-sharing executive,
     1973–1974**.
   - Key personalities: Faulkner (part 2 and overall evaluation); Hume (part 2).
   - Key concepts: power sharing.
   - Cover: the 1973 White Paper; the border poll (1973); the Assembly election (June 1973);
     forming the executive (Faulkner, Fitt, Hume, Napier); the Sunningdale conference
     (December 1973): the Council of Ireland, the status of Northern Ireland, policing; the
     UUUC and Paisley; the Boland case; the February 1974 Westminster election; the Ulster
     Workers' Council strike (May 1974) and Wilson's "spongers" broadcast; the collapse
     (28 May 1974); why it failed and its legacy (compared with later agreements up to 1993).
   - Exam: the 2010 DBQ (difficulties of implementing it) and 2023 DBQ (why divisive); what it
     was and why it collapsed (2007, 2015, 2020, 2021); importance (2009, 2019, 2024).
   - SimpleStudy: Direct Rule and Sunningdale; Sunningdale Agreement case study.
6. **Direct Rule and the search for a settlement, 1974–1993** [I5 P]
   - Syllabus: Direct Rule; Republican and Loyalist terrorism; the Anglo-Irish Agreement,
     1985; the Downing Street Declaration, 1993.
   - Key personalities: Margaret Thatcher; James Molyneaux; Gerry Adams; John Hume (part 3:
     SDLP leader and the Hume–Adams talks).
   - Key concepts: terrorism; power sharing; propaganda.
   - Cover: the Constitutional Convention (1975); "Ulsterisation" and criminalisation; the
     Peace People (1976); the H-Blocks, the blanket protest and the 1981 hunger strikes (Bobby
     Sands' election and death); Sinn Féin's electoral strategy ("the Armalite and the ballot
     box"); Adams's rise; the New Ireland Forum (1983–84) and Thatcher's "out, out, out";
     the Brighton bomb (1984); the Anglo-Irish Agreement (15 November 1985): the
     Intergovernmental Conference and Maryfield secretariat, unionist "Ulster says No",
     Molyneaux and Paisley's campaign; Thatcher's motives; Enniskillen (1987); the Hume–Adams
     dialogue (1988, 1993); the Brooke–Mayhew talks; the Downing Street Declaration
     (15 December 1993): consent and self-determination; how far each step moved towards a
     peaceful settlement.
   - Exam: moves towards a peaceful resolution 1973–1993 (2008, 2012); importance of the AIA
     and DSD (2007, 2009, 2019, 2024); Hume, Paisley, Heaney, Devlin (2012, 2016).
   - SimpleStudy: stalemate and the search for peace; peace developments 1985–1994.
7. **Republican and Loyalist terrorism and the Republic's responses to the Troubles,
   1969–1993** [I5 P]
   - Syllabus: Republican and Loyalist terrorism; the Republic — responses to the "Troubles".
   - Key concepts: terrorism; sectarianism; propaganda.
   - Cover: the main paramilitary groups, their aims, campaigns and casualties *(verify
     figures)*; bombings in Britain; Loyalist sectarian killings (the Shankill Butchers) and
     the Dublin and Monaghan bombings (1974); propaganda on all sides; the Republic's
     responses: Lynch's "can no longer stand by" broadcast (August 1969), field hospitals and
     refugees; the Arms Crisis (1970); the burning of the British embassy (1972); the Offences
     against the State (Amendment) Act 1972 and the Special Criminal Court; Section 31;
     Sunningdale (Cosgrave government); FitzGerald, Haughey and the AIA; extradition debates.
   - Exam: impact of terrorism (2013).
   - SimpleStudy: the Republic's response.
8. **The impact of the Troubles on the economy and society** [I5 S]
   - Syllabus: impact of the "Troubles": (a) the economy; (b) society — education, health,
     housing.
   - Cover: deaths and injuries *(verify)*; loss of investment and tourism; the decline of
     manufacturing; growth of public-sector and security jobs; British subvention; the De
     Lorean episode; unemployment differentials; housing (the Northern Ireland Housing
     Executive 1971, population movement and segregation, peace walls); education (segregated
     schooling, the first integrated school, Lagan College 1981); health (trauma and the
     Royal Victoria Hospital's expertise); everyday life (security checks, divided towns).
   - Exam: social and economic effects of the Troubles (2009, 2015).
   - SimpleStudy: society and culture.
9. **Religious affiliation, cultural identity, ecumenism and cultural responses to the
   Troubles** [I5 C]
   - Syllabus: religious affiliation and cultural identity; ecumenism; cultural responses to
     the "Troubles".
   - Key personalities: Seamus Heaney; Ian Paisley (part 2: religion and politics, opposition
     to ecumenism).
   - Key concepts: cultural traditions; cultural identity; ecumenism; bigotry; tolerance and
     intolerance.
   - Cover: how religion and identity overlapped (unionist/Protestant/British; nationalist/
     Catholic/Irish); the Orange Order and marching; the GAA and Irish language in the North;
     ecumenism: Vatican II's effect, Corrymeela (1965), the Irish School of Ecumenics (1970),
     clergy peace initiatives, and the problems ecumenism faced; cultural responses: Heaney's
     life and poetry (North, 1975), other poets (Mahon, Longley, Montague), Field Day (Friel's
     Translations, 1980), drama, novels, music, murals, film and TV; the Cultural Traditions
     Group (1988).
   - Exam: ecumenism's problems and opportunities (2007); religion, culture and identity
     (2013, 2017, 2019, 2024); Heaney and/or cultural responses (2015, 2016, 2020); divided
     societies being culturally productive (2021).
   - SimpleStudy: society and culture.
10. **Case study: the Apprentice Boys of Derry** [I5 C-CS]
    - Syllabus: case study **the Apprentice Boys of Derry**.
    - Key concepts: cultural traditions; cultural identity; sectarianism; tolerance and
      intolerance.
    - Cover: the siege of Derry: the shutting of the gates (December 1688), Lundy, the relief
      (1689); the founding of Apprentice Boys clubs and the parent club; the Memorial Hall;
      the August (relief) and December (shutting/Lundy) parades and their rituals; the walls
      and the Bogside; the meaning for unionists (siege mentality, "No Surrender") and for
      nationalists (triumphalism); the 12 August 1969 parade and the Battle of the Bogside;
      parades banned and restored in the 1970s; the organisation's relationship with Derry.
    - Exam: the 2011 DBQ (significance for unionists and nationalists); contribution to
      celebrating identity (2006); controversy (2009, 2012, 2016, 2018).
    - SimpleStudy: Apprentice Boys of Derry case study.

### hist-ire6 — Government, economy and society in the Republic of Ireland, 1949–1989 [I6]

Key personalities: T.K. Whitaker; Seán Lemass; Archbishop J.C. McQuaid; Jack Lynch; Charles
Haughey; Garret FitzGerald; Sylvia Meehan; Mary Robinson; Breandán Ó hEithir; Gay Byrne. Key
concepts: economic planning; free trade; common market; equality of opportunity; ecumenism;
secularisation; balance of payments; discrimination; censorship; pluralism; liberalisation.

1. **Alternating governments and their economic and social policies, 1948–1959** [I6 P]
   - Syllabus: alternating governments and their economic and social policies, 1948–1959.
   - Key personalities: Archbishop J.C. McQuaid (part 1: Church power and the Mother and Child
     Scheme).
   - Key concepts: balance of payments.
   - Cover: the First Inter-Party Government (1948–51: Costello, MacBride and Clann na
     Poblachta, the Republic of Ireland Act, the IDA 1949, Marshall Aid, Browne's TB campaign,
     the Mother and Child Scheme crisis, 1951); Fianna Fáil 1951–54 (MacEntee's deflationary
     budget, 1952); the Second Inter-Party Government (1954–57: Sweetman, the 1956 balance of
     payments crisis, the Capital Investment Advisory Committee); stagnation, unemployment and
     1950s emigration *(verify figures)*; Fianna Fáil's return (1957); the "wasted years"
     debate.
   - Exam: instability and economic problems 1949–59 (2006, 2008, 2010, 2016, 2020, 2024);
     the "wasted years" (2013).
   - SimpleStudy: none.
2. **Economic planning and the move to free trade; case study: the First Programme for
   Economic Expansion, 1958–1963** [I6 P; P-CS]
   - Syllabus: economic planning; the move to free trade. Case study: **the First Programme
     for Economic Expansion, 1958–1963**.
   - Key personalities: T.K. Whitaker; Seán Lemass.
   - Key concepts: economic planning; free trade.
   - Cover: Whitaker's background and Economic Development (1958); the First Programme's aims,
     measures (grants and tax relief for exporters, foreign investment, ending the Control of
     Manufactures Acts, productive public investment) and results against targets *(verify)*;
     Lemass as Taoiseach (1959–66): style, modernisation, the Second Programme, the first EEC
     application (1961), the Anglo-Irish Free Trade Agreement (1965), the 1965 meetings with
     O'Neill; what Lemass achieved and left undone; Whitaker and Lemass compared.
   - Exam: the 2019 DBQ (part (d) whether the First Programme achieved its aims); the
     Programme's features and success (2007); Whitaker and/or Lemass (2009, 2011, 2015, 2022);
     Lemass as Taoiseach (2006, 2010, 2012, 2016, 2020, 2021, 2023); First Programme or EEC
     (2024).
   - SimpleStudy: none.
3. **Changes in education, health and social welfare provision** [I6 P; S]
   - Syllabus: changes in education, health and social welfare provision; social change —
     housing, schools, amenities.
   - Key concepts: equality of opportunity.
   - Cover: Investment in Education (1965); Hillery and comprehensive schools; Donogh
     O'Malley and free secondary education (announced 1966, from 1967) with free transport;
     community schools; Regional Technical Colleges; third-level grants; the new primary
     curriculum (1971); health: the 1953 Health Act, the Voluntary Health Insurance Board, the
     1970 health boards, hospital building; social welfare (children's allowance, pensions,
     unemployment and new benefits such as unmarried mothers' allowance 1973); housing
     (local authority building, Ballymun, suburban growth, rural electrification and water
     schemes).
   - Exam: developments in education, health, housing, welfare (2007, 2011, 2015, 2022).
   - SimpleStudy: none.
4. **Economic and social challenges of the 1970s and 1980s: Lynch, Haughey and FitzGerald** [I6
   P]
   - Syllabus: economic and social challenges of the 1970s and 1980s.
   - Key personalities: Jack Lynch; Charles Haughey; Garret FitzGerald.
   - Key concepts: balance of payments; liberalisation; pluralism.
   - Cover: Lynch's first government (1966–73), the Arms Crisis (1970) and his handling of the
     North; the oil crises (1973, 1979), inflation and unemployment; the 1977 Fianna Fáil
     manifesto and borrowing; Haughey's 1980 address on "living beyond our means", spending
     and the national debt; the instability of 1981–82 (three elections, GUBU); FitzGerald's
     coalitions (1981–82, 1982–87), the "constitutional crusade", the New Ireland Forum and the
     AIA; the 1983 and 1986 referendums; unemployment and 1980s emigration *(verify)*; Haughey's
     1987 government and the Programme for National Recovery. Each leader's strengths and
     weaknesses.
   - Exam: the challenges of the 1970s and 1980s (2010, 2017); Lynch (2008, 2012, 2017, 2021,
     2023); Haughey and/or FitzGerald (2011, 2013, 2017, 2021, 2023).
   - SimpleStudy: none.
5. **Anglo-Irish relations, 1949–1989** [I6 P]
   - Syllabus: Anglo-Irish relations, 1949–1989.
   - Cover: the Republic of Ireland Act and the Ireland Act (1949); the anti-partition
     campaign; trade dependence on Britain; Lemass–O'Neill (1965) and the Free Trade Agreement;
     Lynch and the Troubles (Heath, Bloody Sunday, the embassy burning); Sunningdale (1973);
     joint EEC entry (1973); Haughey–Thatcher summits (1980, "totality of relationships") and
     the Falklands rift (1982); FitzGerald and the AIA (1985); the state of relations in 1989.
   - Exam: Anglo-Irish relations 1949–1989 (2012, 2015, 2020); Haughey and/or FitzGerald on
     Anglo-Irish relations (2023).
   - SimpleStudy: none.
6. **Increasing international involvement: the UN and the EEC** [I6 P]
   - Syllabus: increasing international involvement — the UN and the EEC.
   - Key concepts: common market.
   - Cover: UN membership (1955) and Frank Aiken's independent line (the non-proliferation
     resolution); peacekeeping (Congo 1960–64, Niemba and Jadotville, cross-refer to
     `hist-eur5-s6`; Cyprus 1964; Lebanon from 1978); Boland as President of the General
     Assembly (1960); the EEC: the 1961 application and de Gaulle's veto, the 1967 application,
     negotiations, the 1972 referendum and entry (1 January 1973); the Single European Act
     (1987) and the Crotty case. UN or EEC: which mattered more.
   - Exam: UN and/or EEC (2009, 2011, 2021).
   - SimpleStudy: none.
7. **The impact of EEC membership; case study: the impact of the EEC on fisheries** [I6 S;
   S-CS]
   - Syllabus: economic change and its social consequences; the impact of EEC membership.
     Case study: **the impact of the EEC on fisheries**.
   - Key concepts: common market.
   - Cover: CAP and farm incomes; regional and social funds; foreign investment and new
     industry; the decline of protected industries; equality directives and their effect on
     women's rights; changes in attitudes and sovereignty. Case study in depth: the state of
     the Irish fishing industry before 1973; the accession terms and the Common Fisheries
     Policy (exclusive limits, later quotas, the 1983 settlement); Bord Iascaigh Mhara and
     fleet development; ports such as Killybegs and Castletownbere; foreign fleets in Irish
     waters; the benefits and costs for coastal communities; conflicting views of fishermen and
     government.
   - Exam: effects of EEC membership (2006, 2007, 2015, 2016, 2020, 2022, 2024); fisheries
     and/or TV (2012).
   - SimpleStudy: none.
8. **Demographic and social change: the status of women and social change, 1949–1989** [I6 S]
   - Syllabus: demographic change; social change — status of women (housing, schools and
     amenities are in s3).
   - Key personalities: Sylvia Meehan; Mary Robinson.
   - Key concepts: discrimination; liberalisation; equality of opportunity.
   - Cover: population decline to 1961 and growth after *(verify figures)*; the reversal of
     emigration in the 1970s and its return in the 1980s; urbanisation; marriage and birth
     rates; women: the marriage bar (removed 1973), the Commission on the Status of Women
     (1970–72), the Irish Women's Liberation Movement and the 1971 "contraceptive train",
     the McGee case (1973), the Anti-Discrimination (Pay) Act 1974, the Employment Equality
     Act 1977 and the Employment Equality Agency (Meehan as its first chair), the Health
     (Family Planning) Act 1979, women in politics; Mary Robinson's career as senator and
     lawyer to 1989 (private member's bills, landmark cases); the extent of change.
   - Exam: the status/role of women (2008, 2012, 2017, 2024); Meehan and/or Robinson (2008,
     2009, 2016, 2021); social and economic change 1949–89 (2013).
   - SimpleStudy: none.
9. **Culture and religion: the Irish language, Vatican II and the communications revolution**
   [I6 C]
   - Syllabus: changing attitudes towards Irish language and culture; the impact of Vatican
     II; the impact of the communications revolution (television itself is s10).
   - Key personalities: Archbishop J.C. McQuaid (part 2 and overall evaluation); Breandán Ó
     hEithir.
   - Key concepts: ecumenism; secularisation; censorship; pluralism.
   - Cover: the Irish language (Gael Linn 1953; the Language Freedom Movement 1966; the end of
     compulsory Irish for the Leaving Cert pass (1973); Bord na Gaeilge; Raidió na Gaeltachta
     1972; Ó hEithir as writer and broadcaster); traditional music revival (Comhaltas, Seán Ó
     Riada); Vatican II and McQuaid's reaction; the vernacular mass, lay roles and ecumenism;
     the decline of vocations and changes in practice; censorship relaxed (1967); the
     communications revolution (telephones, newspapers, transport, computers); pluralism
     debates and the 1983 and 1986 referendums; secularisation.
   - Exam: Irish language and culture (2006, 2009, 2017, 2021, 2023); TV and/or Vatican II
     (2010, 2013, 2016); McQuaid and Vatican II (2022, 2023); McQuaid, Gay Byrne, Ó hEithir
     (2007, 2009); the communications revolution (2008).
   - SimpleStudy: none.
10. **Case study: the impact of RTÉ, 1962–1972** [I6 C-CS]
    - Syllabus: the impact of television. Case study: **the impact of RTÉ, 1962–1972**.
    - Key personalities: Gay Byrne.
    - Key concepts: censorship; liberalisation; secularisation.
    - Cover: the Broadcasting Authority Act (1960) and Telefís Éireann's launch (31 December
      1961); imported vs home programmes; the Late Late Show (1962), Byrne's style and famous
      controversies (the "Bishop and the Nightie", 1966); current affairs (Seven Days) and
      clashes with government; Lemass's view of RTÉ as an instrument of public policy;
      Telefís Scoile; Irish-language programming; the effect on rural life and politics;
      Section 31 (1971) and the sacking of the RTÉ Authority (1972); whether RTÉ entertained,
      challenged or changed its viewers.
    - Exam: the 2018 DBQ (part (d) whether RTÉ both entertained and challenged); impact of RTÉ
      or TV (2010, 2012, 2013, 2020).
    - SimpleStudy: none.

---

## Later Modern Europe and the wider world, 1815–1992

### hist-eur1 — Nationalism and state formation in Europe, 1815–1871 [E1]

Key personalities: Clemens Metternich; Giuseppe Mazzini; Karl Marx; Mikhail Bakunin; Feargus
O'Connor; Napoleon III; Victor Hugo; Charles Darwin; Otto von Bismarck; Robert Peel. Key
concepts: nationalism; autocracy; democracy; liberalism; serfdom; industrialisation/"Industrial
Revolution"; laissez-faire; Chartism; socialism; romanticism.

1. **The Vienna settlement and the system of Metternich under attack, 1815–1848** [E1 P]
   - Syllabus: the Germanic lands from Confederation…: the system of Metternich under attack.
   - Key personalities: Clemens Metternich.
   - Key concepts: liberalism; nationalism; autocracy.
   - Cover: the Congress of Vienna (1815): aims, territorial settlement, legitimacy and the
     balance of power; the German Confederation (Bund) and its Diet; the Quadruple Alliance
     and the Congress System (Aix-la-Chapelle, Troppau, Laibach, Verona); the Holy Alliance;
     Metternich's aims and methods (censorship, police, the Carlsbad Decrees 1819, the Six
     Articles 1832); challenges: the 1820–21 revolutions (Spain, Naples, Piedmont), Greece,
     the 1830 revolutions (France, Belgium, Poland, central Italy), liberal and nationalist
     movements in Germany (the Burschenschaften, the Wartburg and Hambach festivals), the
     Zollverein (1834) as Prussia's challenge; the fall of Metternich (March 1848); how
     successful his system was, and contemporary and later views of him.
   - Exam: Metternich's system and its success (2006, 2009, 2010, 2012, 2013, 2015, 2017, 2018,
     2020); Metternich vs Marx (2025).
   - SimpleStudy: none.
2. **Case study: the 1848 Revolution in Germany** [E1 P-CS]
   - Syllabus: case study **the 1848 Revolution in Germany**.
   - Key concepts: liberalism; nationalism; democracy.
   - Cover: 1848 across Europe ("the year of revolutions") and why; German causes (the
     1846–47 crop failures and depression, liberal demands, nationalism, the Paris February
     revolution); the March days (Baden, Berlin barricades, Frederick William IV's concessions);
     the Vorparlament and Frankfurt Parliament (May 1848): its members, the Basic Rights, the
     Grossdeutsch vs Kleindeutsch debate, Schleswig-Holstein; the recovery of Austria and
     Prussia (late 1848); the constitution and the crown refused (April 1849); the rump
     parliament and the 1849 risings; why the revolution failed; results (the Erfurt Union,
     Olmütz 1850, lessons for liberals and for Bismarck).
   - Exam: why there was revolution in Germany and why it failed (2008, 2012, 2016, 2023).
   - SimpleStudy: none.
3. **The Germanic lands from Confederation to Empire, 1850–1871** [E1 P]
   - Syllabus: the Germanic lands from Confederation to Empire.
   - Key personalities: Otto von Bismarck (part 1: unification; his later career is
     `hist-eur2-s1`).
   - Key concepts: nationalism; autocracy.
   - Cover: Prussia's economic strength (the Zollverein, coal, iron, railways); Austria's
     weakness after 1859; the constitutional crisis and Bismarck's appointment (1862, "blood and
     iron"); Roon, Moltke and army reform; the Danish War (1864); the Austro-Prussian War
     (1866, Königgrätz/Sadowa) and the Treaty of Prague; the North German Confederation (1867);
     the Hohenzollern candidature, the Ems telegram and the Franco-Prussian War (1870–71,
     Sedan); the proclamation of the German Empire at Versailles (18 January 1871) and its
     constitution; Bismarck's methods (Realpolitik); plan or opportunism; Germany vs Italy.
   - Exam: Confederation to Empire (2019, 2024); Italy and/or Germany towards unity (2009,
     2013, 2017, 2021); Mazzini or Bismarck (2018, 2022, 2025).
   - SimpleStudy: none.
4. **Italy moves towards unity, 1815–1871** [E1 P]
   - Syllabus: Italy moves towards unity.
   - Key personalities: Giuseppe Mazzini.
   - Key concepts: nationalism; liberalism.
   - Cover: Italy after 1815 (Austrian dominance, the states, the Papacy); the Carbonari and
     the risings of 1820–21 and 1831; Mazzini's ideas and Young Italy (1831), failed risings,
     exile; 1848–49 (Charles Albert, Custoza and Novara, the Roman Republic, Garibaldi's
     defence); Piedmont under Victor Emmanuel II and Cavour (economic reform, the Crimean War,
     Plombières 1858); the war of 1859 (Magenta, Solferino, Villafranca); central Italy's
     annexation; Garibaldi and the Thousand (1860); the Kingdom of Italy (1861); Venetia (1866)
     and Rome (1870); obstacles to unification and why attempts after 1852 succeeded; Mazzini's
     contribution and his disappointment.
   - Exam: progress towards Italian unity (2007, 2011); obstacles and how they were overcome
     (2015); why post-1852 attempts succeeded (2024); Mazzini (2018, 2022, 2025).
   - SimpleStudy: none.
5. **Autocracy in the East: Balkan nationalism (Greece and Serbia) and serfdom in Russia** [E1
   P; S]
   - Syllabus: autocracy in the East: Balkan nationalism; Greece and Serbia; serfdom in Russia.
   - Key concepts: autocracy; nationalism; serfdom.
   - Cover: the Ottoman Empire and the Eastern Question (assumed); Serbia: the risings of 1804
     and 1815 (Karadjordje, Miloš Obrenović), autonomy (1830), internal rivalry; Greece: the
     Philiki Etaireia, the 1821 rising, atrocities and philhellenism (Byron), the Great Powers'
     intervention, Navarino (1827), the London Protocol (1830) and the kingdom under Otto; the
     Crimean War (1853–56) as background; Romania's formation (1859–62) briefly; how far
     Balkan nationalism threatened European stability. Russia: tsarist autocracy (Alexander I,
     Nicholas I, the Decembrists 1825); serfdom: its extent, obligations and economic effects;
     Alexander II's emancipation edict (1861), its terms, redemption payments and the mir;
     results for peasants and the economy.
   - Exam: Balkan nationalism (2007, 2016, 2019).
   - SimpleStudy: none.
6. **The State in France: monarchy, republic and Empire, 1815–1871** [E1 P]
   - Syllabus: the State in France: monarchy, republic and Empire.
   - Key personalities: Napoleon III; Victor Hugo (political role: opponent and exile;
     literary role is s11).
   - Key concepts: liberalism; democracy; autocracy.
   - Cover: the restored Bourbons (Louis XVIII and the Charter; Charles X, the July Ordinances,
     the 1830 revolution); the July Monarchy of Louis-Philippe (Guizot, the restricted
     franchise, the banquet campaign); the February 1848 revolution, the Second Republic, the
     National Workshops and June Days; Louis-Napoleon's election (December 1848), the coup
     (December 1851) and the Second Empire (1852); Napoleon III's domestic policy (the
     authoritarian and liberal empire, economic growth, Paris) and foreign policy (Crimea,
     Italy 1859, Mexico, the 1870 war); Sedan and the Third Republic (September 1870); the
     Paris Commune (1871); why France was unstable.
   - Exam: regime changes and instability (2006, 2008, 2010); Napoleon III (2011, 2023, 2025);
     France politically unstable but culturally productive (2022).
   - SimpleStudy: none.
7. **The changing economy and society: agriculture, industrialisation, urban growth and
   education** [E1 S]
   - Syllabus: the changing agricultural economy in the West; industrialisation; urban growth
     and migration; primary education: increased literacy.
   - Key concepts: industrialisation/"Industrial Revolution"; laissez-faire.
   - Cover: agricultural change in Britain, France and the German lands (enclosure, new crops
     and fertilisers, machinery, the 1840s crisis, emigration); industrialisation (coal, iron
     and steel, textiles, steam, railways; Britain first, then Belgium, France and Germany);
     the factory system and working conditions; laissez-faire ideas; urban growth (Manchester,
     Paris, the Ruhr), migration from the countryside, slums, cholera and public health; primary
     education (the Guizot Law 1833, Prussian compulsory schooling, British grants and the
     1870 Act) and rising literacy.
   - Exam: changes in agriculture and industry (2015, 2018, 2021, 2023, 2025); harsh life for
     workers (2008); industrialisation, urbanisation or education (2007).
   - SimpleStudy: none.
8. **Responses to industrial society: trade unionism, socialism, Chartism, mass politics and
   Peel** [E1 S]
   - Syllabus: industrialisation: trade unionism and socialism; mass politics.
   - Key personalities: Karl Marx; Mikhail Bakunin; Feargus O'Connor; Robert Peel.
   - Key concepts: socialism; Chartism; democracy; laissez-faire.
   - Cover: early trade unions (the Combination Acts and their repeal, Tolpuddle 1834, the
     GNCTU, the New Model Unions such as the ASE 1851); utopian socialism (Owen, Fourier, Saint-
     Simon) as background; Marx (with Engels, the Communist Manifesto 1848, Das Kapital 1867,
     historical materialism, the First International 1864); Bakunin (anarchism, the split with
     Marx); mass politics: the 1832 Reform Act, Chartism (the People's Charter 1838, the
     petitions, O'Connor and the Northern Star, Kennington Common 1848, the Land Company, why
     it failed); manhood suffrage in France (1848) and the North German Confederation; Peel's
     reforms (the Metropolitan Police 1829, the Tamworth Manifesto, income tax and free trade
     budgets, the 1844 Factory Act, repeal of the Corn Laws 1846); Owen vs Peel as reformers.
   - Exam: Marx, Bakunin, O'Connor (2011, 2013, 2020, 2021, 2022); Owen and/or Peel (2009,
     2012, 2016, 2019, 2024); trade unionism or socialism (2017).
   - SimpleStudy: none.
9. **Case study: Robert Owen's model village at New Lanark** [E1 S-CS]
   - Syllabus: case study **Robert Owen's model village at New Lanark**.
   - Cover: Owen's background; the New Lanark mills (David Dale; Owen as manager from 1800
     *(verify)*); conditions he found; his reforms: hours, child labour, housing, the
     "silent monitor", the village store, sanitation, the Institute for the Formation of
     Character (1816) and infant school; profits and partners' disputes; A New View of Society;
     Owen's campaign for factory legislation (1819 Act); New Harmony (1825); co-operation and
     the GNCTU; why the model was not widely copied; its reputation then and since.
   - Exam: New Lanark's characteristics and why not adopted (2006, 2011); Owen as reformer
     (2009, 2012, 2013, 2016, 2019, 2022, 2024).
   - SimpleStudy: none.
10. **Case study: Haussmann's Paris, and city planning** [E1 C; C-CS]
    - Syllabus: city planning. Case study: **Haussmann's Paris**.
    - Cover: why cities needed planning (overcrowding, disease, traffic, revolution); Paris
      before 1853; Napoleon III's aims; Haussmann as Prefect of the Seine (1853–70); the
      boulevards and grands travaux; Belgrand's water supply and sewers; parks (Bois de
      Boulogne, Bois de Vincennes, Buttes-Chaumont); new buildings (the Opéra, Les Halles,
      railway stations); the annexation of the suburbs (1860); financing and Haussmann's fall;
      social effects (displacement, the east–west divide); criticisms (Hugo and others);
      other examples of city planning (Vienna's Ringstrasse; British sanitary reform).
    - Exam: Haussmann's success (2009, 2010, 2013, 2015, 2017, 2018, 2020, 2021, 2023).
    - SimpleStudy: none.
11. **Cultural nationalism, the churches and social change, and developments in science** [E1 C]
    - Syllabus: cultural nationalism: music, art, literature and language; the churches and
      social change: France and Great Britain; developments in science: electricity, biology
      and technology.
    - Key personalities: Victor Hugo (literary role); Charles Darwin.
    - Key concepts: romanticism; nationalism.
    - Cover: romanticism; music (Verdi, Wagner, Chopin, Liszt, Smetana *(verify the selection
      in the package)*); art (Delacroix's Liberty Leading the People); literature and language
      (the Grimm brothers, Pushkin, Manzoni, Mickiewicz; standardising national languages);
      Hugo (Les Misérables 1862, exile in Guernsey); the churches in France (Catholic revival,
      Lamennais, Ozanam and the Society of St Vincent de Paul 1833, the Falloux Law 1850) and
      Britain (Methodism, the Oxford Movement, Christian Socialism, Sunday schools, temperance;
      responses to urban poverty); science: electricity (Faraday, the telegraph), biology
      (Darwin's voyage, On the Origin of Species 1859, the controversy, Pasteur, Mendel),
      technology (steam, railways, photography).
    - Exam: cultural nationalism (2006, 2010, 2012, 2017, 2020, 2023); Darwin and/or Hugo
      (2007, 2013, 2016, 2018, 2021, 2024); science and technology (2019, 2020); churches and
      social change (2022).
    - SimpleStudy: none.

### hist-eur2 — Nation states and international tensions, 1871–1920 [E2]

Key personalities: Otto von Bismarck; Wilhelm II; Douglas Haig; Woodrow Wilson; the Krupp
family; Rosa Luxemburg; Wilfred Owen; Leo XIII; Marie Curie; Karl Benz. Key concepts: balance
of power; nationalism; the New Imperialism; world war; war of attrition; conscription;
self-determination; war guilt; anti-Semitism.

1. **The Second Reich, Bismarck's foreign policy and the changing balance of power,
   1871–1890** [E2 P]
   - Syllabus: the Second Reich and the changing balance of power; Anglo- and Franco-German
     tensions; Bismarck's foreign policy.
   - Key personalities: Otto von Bismarck (part 2: Chancellor 1871–90 and overall evaluation).
   - Key concepts: balance of power.
   - Cover: the Reich's constitution (Kaiser, Chancellor, Bundesrat, Reichstag); Bismarck's
     domestic policy (the Kulturkampf is s10; the anti-socialist laws 1878; state social
     insurance 1883–89; tariffs 1879); French revanche and Alsace-Lorraine; the War-in-Sight
     crisis (1875); the Three Emperors' League (1873, 1881); the Congress of Berlin (1878); the
     Dual Alliance (1879); the Triple Alliance (1882); the Reinsurance Treaty (1887); colonies
     (1884–85) and relations with Britain; Bismarck's dismissal (1890); his domestic vs
     foreign record.
   - Exam: Bismarck's foreign and domestic policies (2008, 2010, 2013, 2018, 2024, 2025);
     Bismarck or Wilhelm II (2009, 2016).
   - SimpleStudy: none.
2. **The structures of European diplomacy, the New Imperialism and colonial rivalries** [E2 P]
   - Syllabus: the structures of European diplomacy; the New Imperialism and colonial
     rivalries.
   - Key concepts: the New Imperialism; balance of power; nationalism.
   - Cover: the alliance system after 1890 (the Franco-Russian Alliance 1894, the Entente
     Cordiale 1904, the Anglo-Russian Entente 1907, the Triple Entente); the causes of the New
     Imperialism (economic, strategic, nationalist, missionary, "Social Darwinist"); the
     Berlin Conference (1884–85) and the Scramble for Africa; Leopold II and the Congo; Asian
     rivalry (China); Fashoda (1898); the Boer War; the Moroccan crises (1905–06 Algeciras,
     1911 Agadir); how imperialism affected Europe and international tension.
   - Exam: why colonies were sought (2006); causes and effects of the New Imperialism (2009,
     2017, 2023); colonial rivalries and tension (2013, 2015); main tensions 1871–1914 (2011,
     2019).
   - SimpleStudy: none.
3. **Wilhelm II and Weltpolitik; case study: the naval policy of Wilhelm II** [E2 P; P-CS]
   - Syllabus: Wilhelm II and Weltpolitik. Case study: **the naval policy of Wilhelm II**.
   - Key personalities: Wilhelm II.
   - Key concepts: balance of power; nationalism.
   - Cover: Wilhelm II's personality and the "new course"; Weltpolitik (Bülow, the "place in
     the sun", colonies, the Kruger telegram 1896, the Berlin–Baghdad railway); naval case
     study in depth: Mahan's influence, Tirpitz, the Navy Laws (1898, 1900, and later
     supplements), the Navy League, the risk theory, Britain's response (the Dreadnought 1906,
     the arms race, "We want eight"), the Haldane mission (1912), costs and domestic politics,
     effects on Anglo-German relations and on the outbreak of war.
   - Exam: problems caused by the naval policy (2006, 2007, 2020); Weltpolitik's effect (2012);
     German foreign policy and the balance of power (2010, 2016, 2024).
   - SimpleStudy: none.
4. **Serbia, the Second International and the outbreak of war in 1914** [E2 P]
   - Syllabus: Serbia as a fulcrum of Great Power rivalry; the Second International; the
     outbreak of war in 1914.
   - Key personalities: Rosa Luxemburg.
   - Key concepts: nationalism; balance of power.
   - Cover: Serbia after 1878; the 1903 coup and the Karadjordjević turn towards Russia; the
     Pig War (1906); the Bosnian annexation crisis (1908–09); the Balkan Wars (1912–13); the
     Black Hand; Sarajevo (28 June 1914); the July crisis, the "blank cheque", the ultimatum,
     mobilisations, the Schlieffen Plan and Belgium; long- and short-term causes; the war-guilt
     debate (cross-refer to s6). The Second International (1889): its parties, anti-war
     resolutions (Stuttgart 1907, Basel 1912), and its collapse in August 1914; Luxemburg's
     career (Polish-born, the SPD left, anti-war campaigning, prison, the Spartacists, her
     murder in January 1919).
   - Exam: causes of WWI (2008, 2018, 2021); Luxemburg (2012, 2020).
   - SimpleStudy: none.
5. **The conduct of war, 1914–1918** [E2 P]
   - Syllabus: the conduct of war.
   - Key personalities: Douglas Haig.
   - Key concepts: world war; war of attrition; conscription.
   - Cover: the Western Front (the Marne 1914, trench warfare, Verdun 1916, the Somme 1916,
     Passchendaele 1917, the German spring offensive and the Hundred Days 1918); weapons and
     tactics; the Eastern Front (Tannenberg, Brusilov, Russia's exit); other fronts (Gallipoli,
     Italy); war at sea (blockade, Jutland 1916, unrestricted submarine warfare); the USA's
     entry (1917); conscription; the armistice (11 November 1918); Haig's command and the
     "lions led by donkeys" debate.
   - Exam: WWI through Haig, Owen, women, the conduct of war (2009, 2012, 2016, 2019, 2023).
   - SimpleStudy: none.
6. **War and revolution in Germany, and the Peace Settlement, 1918–1920** [E2 P]
   - Syllabus: war and revolution; the Peace Settlement.
   - Key personalities: Woodrow Wilson.
   - Key concepts: self-determination; war guilt.
   - Cover: the collapse of the Central Powers; the German revolution (the Kiel mutiny,
     abdication, the Weimar republic proclaimed, the Spartacist rising January 1919);
     Austria-Hungary's break-up; Wilson's Fourteen Points; the Paris Peace Conference (the Big
     Four, aims); the Treaty of Versailles (territory, reparations, disarmament, Article 231);
     the treaties of St Germain, Trianon, Neuilly and Sèvres; the League of Nations and the US
     Senate's rejection; self-determination applied and denied; the problems Europe faced
     after the war.
   - Exam: Wilson's role (2007, 2020); WWI and the Peace Settlement (2017, 2018); post-war
     problems (2024).
   - SimpleStudy: none.
7. **Economic growth and social tensions: industrialisation in Germany and the Krupp family**
   [E2 S]
   - Syllabus: economic growth and social tensions: industrialisation in Germany and its
     impact on society.
   - Key personalities: the Krupp family.
   - Cover: why Germany industrialised fast after 1871 (coal and iron, railways, banks,
     education, cartels); the second industrial revolution (steel, chemicals, electricals:
     Siemens, AEG); the Krupp firm at Essen (Alfred Krupp, Friedrich Alfred, Bertha and Gustav
     Krupp von Bohlen und Halbach; armaments, worker housing and welfare, "Big Bertha");
     urbanisation and the working class; the growth of the SPD and trade unions; social
     tensions (Junkers vs industrialists vs workers); state welfare as a response.
   - Exam: German industrialisation and its impact (2016, 2017, 2018, 2020, 2021, 2024);
     church–state and other tensions in Germany (2022).
   - SimpleStudy: none.
8. **Industrialisation, economic crisis and revolution in Tsarist Russia, 1871–1920** [E2 S; P]
   - Syllabus: industrialisation and economic crisis in Tsarist Russia; war and revolution
     (Russia).
   - Key concepts: world war; self-determination.
   - Cover: Russian backwardness in 1871; Witte's industrialisation (foreign loans, the gold
     standard, the Trans-Siberian railway); peasant conditions and the 1891 famine; the
     Russo-Japanese war (1904–05); the 1905 revolution (Bloody Sunday, the October Manifesto,
     the Dumas); Stolypin's reforms; the impact of World War I (defeats, shortages, Rasputin);
     the February and October 1917 revolutions; Brest-Litovsk (1918); the civil war to 1920 in
     outline.
   - Exam: crisis in Tsarist Russia (2006, 2007, 2015, 2018, 2023, 2025); war and revolution
     (2010, 2012, 2017, 2021); industrialisation in Tsarist Russia (2019).
   - SimpleStudy: none.
9. **The impact of war on society and economy; case study: women in the workforce during World
   War I** [E2 S; S-CS]
   - Syllabus: the impact of war on society and economy. Case study: **women in the workforce
     during World War I**.
   - Key concepts: world war; conscription.
   - Cover: total war (state control, DORA, rationing, propaganda, war economies and debt,
     inflation, casualties, the 1918 influenza); case study in depth: women before 1914;
     munitions work (the "munitionettes", TNT poisoning), transport, offices, farms (the Women's
     Land Army), nursing (VADs) and auxiliary services, in Britain, France and Germany; pay and
     trade union attitudes; Pankhurst's wartime campaigning; what changed after 1918 (the
     vote in Britain and Germany, women's return to the home).
   - Exam: impact of WWI on economy and society (2010); women in the workforce (2012, 2021,
     2022, 2023).
   - SimpleStudy: none.
10. **Culture and religion: national identity, the literature of WWI, church–state tensions and
    anti-Semitism** [E2 C]
    - Syllabus: expression of national identity through literature and the arts; the
      literature of World War I; Church/State tensions in Germany and Italy; anti-Semitism in
      France and Russia.
    - Key personalities: Wilfred Owen; Leo XIII.
    - Key concepts: anti-Semitism; nationalism.
    - Cover: national identity in the arts (e.g. Kipling, Elgar, Sibelius, Wagner's legacy
      *(verify the selection in the package)*); WWI literature: early patriotism (Brooke), the
      later protest poets (Owen: Craiglockhart, Sassoon, "Dulce et Decorum Est", death in
      November 1918, posthumous fame), Barbusse, Remarque as the post-war view; the Kulturkampf
      (Falk, the May Laws 1873, the Centre Party, why Bismarck ended it); Italy and the Roman
      Question (the Law of Guarantees 1871, non expedit); Leo XIII (ending the Kulturkampf,
      Rerum Novarum 1891, ralliement in France); anti-Semitism in France (Drumont, the Dreyfus
      Affair 1894–1906, Zola's J'accuse) and Russia (the 1881–82 pogroms, the May Laws, the
      Pale of Settlement, Kishinev 1903, the Protocols, emigration).
    - Exam: literature of WWI (2006, 2007, 2011, 2020, 2022, 2025); national identity in the
      arts (2010); church–state and/or anti-Semitism (2008, 2009, 2011, 2015, 2019, 2022,
      2024); Leo XIII (2012, 2016).
    - SimpleStudy: none.
11. **Science, technology and medicine; case study: the invention and early history of the
    motor car** [E2 C; C-CS]
    - Syllabus: key developments in science, technology and medicine. Case study: **the
      invention and early history of the motor car**.
    - Key personalities: Marie Curie; Karl Benz.
    - Cover: Curie (radioactivity, polonium and radium, Nobel prizes 1903 and 1911, mobile
      X-ray units in WWI); Röntgen's X-rays (1895); Pasteur and Koch (germ theory, vaccines);
      anaesthetics and antiseptics; electricity and communications (Edison, Marconi's
      wireless); flight (1903). Motor car case study in depth: the internal combustion engine
      (Otto, Daimler and Maybach); Benz's Motorwagen (patented 1886) and Bertha Benz's 1888
      drive; Peugeot, Panhard, Renault; Dunlop's pneumatic tyre; Ford's Model T (1908) and the
      moving assembly line (1913); economic and social effects (industry, roads, leisure, war
      transport).
    - Exam: the motor car (2013, 2023, 2025); science, technology and medicine (2008, 2011,
      2015, 2022); Curie (2016, 2020); industry including the motor car (2020, 2024).
    - SimpleStudy: none.

### hist-eur3 — Dictatorship and democracy in Europe, 1920–1945 [E3]

Key personalities: J.M. Keynes; Adolf Hitler; Benito Mussolini; Vladimir Ilyich Lenin; Josef
Stalin; Winston Churchill; Joseph Goebbels; Leni Riefenstahl; Bing Crosby; Charlie Chaplin. Key
concepts: inflation; the Depression; protectionism; collectivisation; communism; fascism;
dictatorship; personality cult; totalitarianism; democracy; propaganda; anti-Semitism;
herrenvolk; Reichskirche; the Holocaust; collaboration; resistance; lebensraum; blitzkrieg.

1. **Origins and growth of the fascist regimes: Mussolini's Italy** [E3 P]
   - Syllabus: origins and growth of the fascist regimes in Europe.
   - Key personalities: Benito Mussolini.
   - Key concepts: fascism; dictatorship; personality cult; totalitarianism.
   - Cover: the general conditions favouring fascism (the war's legacy, fear of communism,
     economic crisis, weak democracies); the characteristics of fascism; Italy: the "mutilated
     victory", the Fasci di Combattimento (1919), the squadristi, the March on Rome (1922),
     the Acerbo Law, Matteotti's murder (1924), the totalitarian state, the corporate state,
     the battles for grain, births and the lira, youth and propaganda, foreign policy (Corfu,
     Abyssinia 1935–36, the Axis), and his fall (1943) and the Salò republic; other
     authoritarian regimes of the period as comparison only. (Spain is not named in the
     syllabus; Appendix A notes the app's existing Spanish Civil War content.)
   - Exam: conditions for fascism and its characteristics (2006, 2013, 2019, 2023); why Italy
     and/or Germany embraced dictatorship (2022); Mussolini's policies and Italian fascism
     (2011, 2021); propaganda and terror (2009, 2015).
   - SimpleStudy: growth of fascism.
2. **Weimar Germany and the rise of Hitler, 1920–1933** [E3 P; S]
   - Syllabus: origins and growth of the fascist regimes (Germany); economic and social
     problems of the inter-war years (Germany).
   - Key concepts: inflation; the Depression; democracy.
   - Cover: the Weimar constitution's weaknesses (Article 48, PR); Versailles resentment; the
     Kapp Putsch; the Ruhr occupation and hyperinflation (1923); the Munich Putsch and Mein
     Kampf; Stresemann (the Rentenmark, Dawes 1924, Locarno, Young 1929); the Depression's
     effect on German unemployment; the Nazi breakthrough (1930, 1932 elections); propaganda
     and the SA; Brüning, Papen, Schleicher; Hitler appointed Chancellor (30 January 1933);
     how German governments dealt with economic and social problems.
   - Exam: German governments and economic/social problems (2010, 2015); Britain or Germany
     (2008, 2020); Hitler's route to absolute control (2018).
   - SimpleStudy: interwar Germany.
3. **The Nazi state in peace, 1933–1939, and Hitler's foreign policy** [E3 P]
   - Syllabus: the Nazi state in peace (and war).
   - Key personalities: Adolf Hitler.
   - Key concepts: totalitarianism; herrenvolk; lebensraum; dictatorship.
   - Cover: the Reichstag fire and Enabling Act (1933); Gleichschaltung; the Night of the Long
     Knives (1934); Hitler as Führer; the SS, Gestapo and camps; the economy (Schacht, public
     works, autobahns, the Four Year Plan, rearmament, autarky); youth, women and the
     Volksgemeinschaft; Hitler's foreign policy (leaving the League, the Saar, conscription
     1935, the Rhineland 1936, the Anschluss and the Sudetenland 1938, Munich, Prague, the
     Nazi-Soviet Pact, Poland 1939), appeasement, and how far he caused the war; the Nazi
     state in war (Speer, total war, the July 1944 plot) briefly here, with the course of the
     war in s9.
   - Exam: characteristics of the Nazi state (2007, 2011); Hitler's foreign policy and the
     outbreak of war (2012, 2015, 2021).
   - SimpleStudy: interwar Germany; Hitler's foreign policy.
4. **Communism in Russia: Lenin, Stalin and the Soviet alternative** [E3 P; S]
   - Syllabus: communism in Russia: the regimes of Lenin and Stalin; the Stalinist state in
     peace and war; the Soviet alternative.
   - Key personalities: Vladimir Ilyich Lenin; Josef Stalin.
   - Key concepts: communism; collectivisation; personality cult; totalitarianism.
   - Cover: Lenin's regime (the Bolshevik seizure of power is background from `hist-eur2-s8`;
     the Cheka, the civil war and War Communism, the Kronstadt rising, the NEP 1921, the USSR
     1922); the struggle for succession (Trotsky, the left and right oppositions); Stalin's
     Five-Year Plans (Magnitogorsk, Stakhanov, results and costs); collectivisation, the kulaks
     and the 1932–33 famine; the cult of personality; Soviet society (education, women,
     religion, the arts); the "Soviet alternative" as seen from the West in the Depression;
     the Stalinist state in war (Barbarossa, Stalingrad, the war economy, Stalin as war
     leader); his internal and external policies evaluated.
   - Exam: Lenin and Stalin's contribution (2008, 2011); Stalin's transformation of economy
     and society (2006, 2013, 2021, 2023); Stalin's rule and leadership in peace and war
     (2010, 2012, 2018, 2019, 2020, 2022); Soviet role in WWII (2007).
   - SimpleStudy: Communism in Russia.
5. **Case study: Stalin's show trials** [E3 P-CS]
   - Syllabus: case study **Stalin's show trials**.
   - Key concepts: totalitarianism; propaganda; personality cult.
   - Cover: why Stalin purged (paranoia, rivals, scapegoats for economic failure); the Kirov
     murder (December 1934); the trials: Zinoviev and Kamenev (August 1936), Pyatakov and
     Radek (January 1937), Bukharin, Rykov and Yagoda (March 1938); Vyshinsky as prosecutor;
     how confessions were obtained; the military purge (Tukhachevsky, 1937); the wider Terror
     (Yezhov, the NKVD, the Gulag, numbers *(verify)*); foreign reactions (diplomats,
     journalists, the Dewey Commission); the impact on the Party, army, economy and society.
   - Exam: the 2024 DBQ (part (d) the trials' impact on Soviet Russia); Stalin's economy and/or
     show trials (2013, 2023); Stalin's leadership (2019).
   - SimpleStudy: Stalin's Show Trials case study.
6. **France: the Third Republic, 1920–1940, and the Vichy state** [E3 P]
   - Syllabus: France: the Third Republic, 1920–1940, and the Vichy state.
   - Key concepts: democracy; collaboration; resistance.
   - Cover: post-war France (reconstruction, the Bloc National, Poincaré, the Ruhr
     occupation, the Cartel des Gauches); political instability (frequent changes of
     government) and the economy; the Depression's late arrival; the Stavisky affair and the
     6 February 1934 riots; the leagues; the Popular Front (Blum 1936, the Matignon
     Agreements); the Maginot Line and defence policy; the fall of France (1940); Pétain and
     Vichy (the National Revolution, "Travail, Famille, Patrie", Laval, collaboration, the
     Milice, anti-Jewish laws and deportations, the Vel' d'Hiv round-up 1942); de Gaulle and
     the Free French; the Resistance; liberation (1944).
   - Exam: France's problems and instability 1920–1945 (2007, 2009, 2012, 2018, 2023).
   - SimpleStudy: France from Third Republic to Vichy.
7. **Economic and social problems of inter-war Britain, and Keynes** [E3 S]
   - Syllabus: economic and social problems of the inter-war years, with particular reference
     to Britain (Germany is s2).
   - Key personalities: J.M. Keynes.
   - Key concepts: the Depression; protectionism; democracy.
   - Cover: the post-war boom and slump; the decline of the staple industries (coal, cotton,
     shipbuilding, steel); regional unemployment (the "distressed areas") vs the prosperous
     south-east; the return to gold (1925); the General Strike (1926); the 1929–31 crisis, the
     May Report, the National Government, abandoning gold and adopting protection (1931–32);
     the means test and the unemployed (the NUWM, hunger marches); the Special Areas Act
     (1934); housing and new industries; Keynes's career and ideas (The Economic Consequences
     of the Peace 1919, the General Theory 1936, his wartime role); how effectively problems
     were dealt with.
   - Exam: Britain's inter-war problems and responses (2006, 2009, 2013, 2015, 2019, 2022);
     Britain or Germany (2008, 2020); Keynes and others (2011, 2021, 2023).
   - SimpleStudy: interwar Britain.
8. **Case study: the Jarrow March, October 1936** [E3 S-CS]
   - Syllabus: case study **the Jarrow March, October 1936**.
   - Key concepts: the Depression; democracy.
   - Cover: Jarrow and Palmer's shipyard; its closure by National Shipbuilders' Security
     (1933–34) and the steelworks refusal; unemployment levels *(verify)*; Ellen Wilkinson MP
     and the town council; the organisation of the crusade (the 200 marchers, the cross-party
     approach, the Labour and TUC attitudes, the churches); the march (5 October–31 October
     1936), the route and reception; the petition; Baldwin's refusal to meet them; outcome
     (the return home, the dole cut); later effects (new industries, Wilkinson's The Town
     That Was Murdered 1939, rearmament); its place in memory; success or failure.
   - Exam: the 2017 DBQ (part (d) aims and how far achieved) and 2025 DBQ (part (d) whether a
     total failure); causes and consequences (2007).
   - SimpleStudy: Jarrow March case study.
9. **The Second World War: blitzkrieg, wartime alliances, the technology of warfare and
   Churchill** [E3 P; C]
   - Syllabus: wartime alliances, 1939–1945; the technology of warfare.
   - Key personalities: Winston Churchill.
   - Key concepts: blitzkrieg.
   - Cover: the course of the war in outline (Poland, the Phoney War, the fall of France,
     the Battle of Britain, Barbarossa, Pearl Harbor, El Alamein, Stalingrad, Kursk, D-Day,
     the fall of Berlin); the Axis (the Pact of Steel 1939, the Tripartite Pact 1940); the
     Grand Alliance (the Atlantic Charter 1941, Lend-Lease, Tehran 1943, Yalta 1945) and its
     tensions; Churchill's career and war leadership; the technology of warfare (tanks and
     blitzkrieg, aircraft and strategic bombing, radar, Enigma and Ultra, submarines and
     convoys, rockets, jet aircraft, the atomic bomb); the technology between the wars.
   - Exam: technology of warfare (2006, 2019); wartime alliances (2009, 2020); Churchill or
     Stalin (2018).
   - SimpleStudy: Second World War; wartime alliances.
10. **Society during World War II: the Home Front, rationing, evacuees, refugees,
    collaboration and resistance** [E3 S]
    - Syllabus: society during World War II: the Home Front; rationing/evacuees; refugees;
      collaboration/resistance.
    - Key concepts: collaboration; resistance.
    - Cover: Britain's Home Front (the Blitz, evacuation in 1939–40, rationing, women's war
      work, conscription of women 1941, the Beveridge Report); Germany's Home Front (rationing,
      bombing, foreign labour, total war); refugees and displaced people; collaboration
      (Vichy, Quisling in Norway, other occupied states) and resistance (France, Poland, the
      Yugoslav partisans, the White Rose); civilian populations in Britain and/or France.
    - Exam: civilian populations in Britain and/or France (2008); the Home Front among WWII
      topics (2009, 2020).
    - SimpleStudy: wartime society.
11. **Anti-Semitism and the Holocaust** [E3 S]
    - Syllabus: anti-Semitism and the Holocaust.
    - Key concepts: anti-Semitism; the Holocaust; herrenvolk.
    - Cover: the roots of anti-Semitism (cross-refer to `hist-eur2-s10`); Nazi racial ideology;
      the boycott (1933) and exclusion laws; the Nuremberg Laws (1935); Kristallnacht (1938);
      emigration and the Évian conference; ghettos (Warsaw, Łódź); the Einsatzgruppen; the
      Wannsee Conference (1942) and the "Final Solution"; the death camps (Auschwitz-Birkenau,
      Treblinka and others); victims *(verify figures)*; Jewish resistance (the Warsaw
      uprising 1943); bystanders, rescuers and collaborators across Europe; liberation and
      the Nuremberg trials.
    - Exam: how anti-Semitism and the Holocaust affected Europe (2012, 2020).
    - SimpleStudy: anti-Semitism and the Holocaust.
12. **Nazi propaganda; case study: the Nuremberg Rallies** [E3 C; C-CS]
    - Syllabus: Nazi propaganda — state control and use of mass media. Case study: **the
      Nuremberg Rallies**.
    - Key personalities: Joseph Goebbels; Leni Riefenstahl.
    - Key concepts: propaganda; personality cult; totalitarianism.
    - Cover: Goebbels's career (Berlin Gauleiter, election campaigns, the Ministry of Public
      Enlightenment and Propaganda 1933, the Reich Chamber of Culture, total war speech 1943);
      press, radio (the People's Receiver), cinema, posters, book burning (May 1933),
      degenerate art, the 1936 Olympics; Riefenstahl (Triumph of the Will 1935, Olympia 1938,
      her later claims and reputation). Nuremberg Rallies in depth: why Nuremberg; the rally
      grounds (Zeppelin Field, Speer's design and the "cathedral of light"); the 1933–1938
      rallies and their themes; the 1934 rally and Triumph of the Will; the Nuremberg Laws
      announced at the 1935 rally; the experience of participants; purpose and effect.
    - Exam: the 2016 DBQ (part (d) the rallies and/or Goebbels); Goebbels and/or Riefenstahl
      (2008); propaganda and terror (2009); cinema (2018).
    - SimpleStudy: Nuremberg Rallies case study.
13. **Church–state relations under Mussolini and Hitler; Anglo-American popular culture: radio
    and cinema** [E3 C]
    - Syllabus: church–state relations under Mussolini and Hitler; Anglo-American popular
      culture in peace and war: radio and cinema.
    - Key personalities: Charlie Chaplin; Bing Crosby.
    - Key concepts: Reichskirche.
    - Cover: Mussolini and the Church (the Lateran Treaties 1929; disputes over Catholic
      Action 1931; the racial laws 1938); Hitler and the churches (the Concordat 1933; the
      Reichskirche and the German Christians, Ludwig Müller; the Confessing Church, Niemöller,
      Bonhoeffer; Mit brennender Sorge 1937; Galen and euthanasia); radio (the BBC and Reith,
      American networks, Roosevelt's fireside chats, wartime radio); cinema (Hollywood's
      studio system, talkies from 1927, newsreels, British cinema, wartime films); Chaplin
      (the Tramp, Modern Times 1936, The Great Dictator 1940); Bing Crosby (radio, records,
      films, "White Christmas", entertaining troops); the spread of American culture in
      Europe and reactions to it.
    - Exam: church–state relations (2010); popular culture's impact (2010, 2022); radio and
      cinema through Chaplin, Crosby, Riefenstahl (2013, 2018).
    - SimpleStudy: Anglo-American popular culture.

### hist-eur4 — Division and realignment in Europe, 1945–1992 [E4]

Key personalities: Imre Nagy; Nikita Khrushchev; Pope John Paul II; Mikhail Gorbachev; Jean
Monnet; Jacques Delors; Margaret Thatcher; Alexander Solzhenitsyn; Simone de Beauvoir; John
Lennon. Key concepts: capitalism; communism; Sovietisation; Cold War; Iron Curtain; nuclear
deterrence; détente; satellite state; glasnost; common market; federal Europe; welfare state;
feminism; dissident writer; ecumenical movement; mass media; information technology; pop star;
teenager.

1. **Origins of the Cold War, the division of Germany and the Sovietisation of Eastern
   Europe, 1945–1949** [E4 P]
   - Syllabus: origins of Cold War; division of Germany; "Sovietisation" of Eastern Europe;
     military alliances.
   - Key concepts: Cold War; Iron Curtain; Sovietisation; satellite state; capitalism;
     communism.
   - Cover: wartime tensions; Yalta and Potsdam; the occupation zones and Berlin; Soviet
     security aims; Churchill's "Iron Curtain" speech (1946); "salami tactics" and the
     takeovers in Poland, Hungary, Romania, Bulgaria and Czechoslovakia (February 1948);
     Cominform; the Tito split (1948); the Truman Doctrine and Marshall Plan (1947); the
     Berlin Blockade and airlift (1948–49); the FRG and GDR (1949); NATO (1949) and the Warsaw
     Pact (1955).
   - Exam: origin and development of the Cold War (2013, 2019, 2022); division of Germany and
     Berlin (2018); Sovietisation (2006, 2007, 2010); Soviet control of Eastern Europe (2011,
     2016, 2020); the Berlin Blockade, alliances and tensions (2021, 2023).
   - SimpleStudy: none.
2. **The main crises of the Cold War, Khrushchev and détente** [E4 P]
   - Syllabus: main crises of Cold War; military alliances.
   - Key personalities: Nikita Khrushchev.
   - Key concepts: nuclear deterrence; détente; Cold War.
   - Cover: Khrushchev's rise; the 1956 "secret speech" and de-Stalinisation; peaceful
     coexistence; his domestic reforms (the Virgin Lands, decentralisation) and failures;
     Berlin (the 1958 ultimatum, the Wall 1961); the U-2 incident; Cuba (1962) as seen from
     Europe; his fall (1964); nuclear deterrence and arms control; détente (Ostpolitik,
     Helsinki 1975); the "second Cold War" (Afghanistan 1979, the Euromissiles); the key
     turning points to 1989.
   - Exam: Khrushchev's policies and success (2009, 2012, 2017); Khrushchev and/or Gorbachev
     (2015, 2019, 2025); main crises of the Cold War (2009); turning points (2024).
   - SimpleStudy: none.
3. **Case study: the Hungarian Uprising, 1956** [E4 P-CS]
   - Syllabus: case study **the Hungarian Uprising, 1956**.
   - Key personalities: Imre Nagy.
   - Key concepts: satellite state; Sovietisation.
   - Cover: Rákosi's Stalinist rule; Nagy's first premiership (1953–55); the effect of the
     secret speech and the Polish October; the 23 October 1956 student demonstration, the
     Stalin statue and the radio station; Nagy's return; the fighting and the Soviet
     withdrawal; multi-party government and withdrawal from the Warsaw Pact (1 November); the
     second Soviet intervention (4 November) and Kádár; casualties and refugees *(verify)*;
     the West's response (Suez, Radio Free Europe, the UN); Nagy's trial and execution (1958);
     why it failed; its significance.
   - Exam: reasons for the uprising and why it failed or was crushed (2008, 2018); Berlin and/or
     Hungary and international tension (2021).
   - SimpleStudy: none.
4. **Reform movements in Eastern Europe, the collapse of the Soviet Union, and fragmentation and
   realignment, 1953–1992** [E4 P]
   - Syllabus: emergence of reform movements in Eastern Europe; collapse of Soviet Union;
     fragmentation and realignment in Europe.
   - Key personalities: Mikhail Gorbachev; Pope John Paul II (political role; religious role
     in s11).
   - Key concepts: glasnost; communism.
   - Cover: East Berlin (1953); Poland (1956); the Prague Spring (1968, Dubček) and the
     Brezhnev Doctrine; Solidarity (1980, Wałęsa) and martial law (1981); John Paul II's
     election (1978) and his 1979 visit to Poland; Gorbachev's background, glasnost,
     perestroika, the Sinatra Doctrine, Chernobyl and arms control; 1989 (Poland, Hungary,
     the Berlin Wall on 9 November, Czechoslovakia, Romania); German reunification (October
     1990); the August 1991 coup and the dissolution of the USSR (December 1991); the break-up
     of Yugoslavia (1991–92); Gorbachev's successes and failures; why communism collapsed.
   - Exam: Gorbachev (2008, 2021, 2023); Khrushchev and/or Gorbachev as reformers (2015, 2019,
     2025); the collapse of communism (2010); how the Cold War ended (2019); Soviet control of
     Eastern Europe (2011, 2016, 2020).
   - SimpleStudy: none.
5. **Moves towards European unity and the EEC, 1945–1992** [E4 P]
   - Syllabus: moves towards European unity, 1945–1957; establishment and evolution of the EEC.
   - Key personalities: Jean Monnet; Jacques Delors.
   - Key concepts: common market; federal Europe.
   - Cover: reasons for unity (war, the Soviet threat, economic recovery); the Council of
     Europe (1949); Monnet's career (the Monnet Plan, the Schuman Declaration 1950, the ECSC
     1951–52 and its High Authority, the Action Committee); the failure of the EDC (1954);
     Messina (1955) and the Treaties of Rome (1957): the EEC and Euratom; the CAP; EFTA;
     de Gaulle's vetoes (1963, 1967) and the empty chair crisis (1965); enlargement (1973,
     1981, 1986); the EMS (1979); Delors's presidency (from 1985), the Single European Act
     (1986) and Maastricht (1992); Thatcher's attitude (cross-refer to s7); federalists vs
     intergovernmentalists.
   - Exam: the EEC's establishment and evolution (2006, 2007, 2022); why and how far Europe
     moved to unity (2012, 2018, 2025); attitudes to unity of Monnet, Thatcher and others
     (2009); Monnet, Delors, de Beauvoir, Thatcher (2013, 2015); effects of unity (2011, 2015,
     2016, 2019, 2021).
   - SimpleStudy: none.
6. **The Western economies, 1945–1973: growth, Marshall Aid, free trade, immigration and the
   welfare state** [E4 S]
   - Syllabus: the Western economies, 1945–1973: the era of economic growth; Marshall Aid;
     moves towards free trade; immigration; the Welfare State.
   - Key concepts: welfare state; capitalism; common market.
   - Cover: post-war devastation; Marshall Aid (1948–52) and the OEEC; Bretton Woods, GATT;
     the German "economic miracle" (Erhard), the French trente glorieuses and planning, Italy;
     the factors that helped and hindered growth; free-trade moves (Benelux, the ECSC, the
     EEC, EFTA); labour shortages and immigration (guest workers in West Germany, colonial
     migrants to Britain and France); the welfare state (Beveridge, the NHS 1948, other
     European systems).
   - Exam: what helped and hindered growth (2008); Marshall Aid and free trade (2016, 2020);
     growth 1945–1973 and the oil crisis (2023); strengths and weaknesses of the Western
     economies (2017).
   - SimpleStudy: none.
7. **Case study: the Oil Crisis, 1973, and the Western economies, 1973–1990; Margaret
   Thatcher** [E4 S; S-CS]
   - Syllabus: the Western economies, 1973–1990: impact of the Oil Crisis; recession and the
     rise in unemployment. Case study: **the Oil Crisis, 1973**.
   - Key personalities: Margaret Thatcher.
   - Key concepts: capitalism; welfare state.
   - Cover: the Yom Kippur War and the OPEC embargo and price rises (October 1973); immediate
     effects (fuel rationing, car-free Sundays, inflation, balance of payments); stagflation;
     the 1979 second oil shock; recession and unemployment in the 1980s; deindustrialisation;
     energy responses (North Sea oil, nuclear power in France); how lasting the impact was.
     Thatcher: her rise; monetarism, privatisation, trade union laws, the miners' strike
     (1984–85); the Falklands (1982); relations with the USA and USSR; her attitude to Europe
     (the budget rebate 1984, the Bruges speech 1988); her fall (1990); successes and
     failures.
   - Exam: the oil crisis's impact (2006, 2012, 2015, 2021, 2023); developments 1973–1992
     (2010); prosperity and recession (2024); Thatcher (2011, 2013, 2015, 2017, 2020, 2021,
     2022, 2024).
   - SimpleStudy: none.
8. **The communist economies: problems and outcomes** [E4 S]
   - Syllabus: the communist economies: problems and outcomes.
   - Key concepts: communism; Sovietisation.
   - Cover: the Soviet planning model exported to the satellites; Comecon (1949);
     collectivisation and heavy industry; living standards and shortages; Khrushchev's and
     Kosygin's reforms; the Brezhnev era of stagnation; Hungary's "goulash communism"; Poland's
     price rises and protests (1970, 1976, 1980) and Western debt; the arms burden; the
     failure of perestroika; the East–West gap by 1989.
   - Exam: communist governments and their economic challenges (2013).
   - SimpleStudy: none.
9. **Marriage, the family and the changing role of women; affluence, leisure time and the
   consumer society** [E4 S]
   - Syllabus: marriage, the family and the changing role of women; affluence, leisure time and
     the consumer society.
   - Key personalities: Simone de Beauvoir (part 1: The Second Sex and feminism).
   - Key concepts: feminism.
   - Cover: post-war family life and the baby boom; women in the workforce; de Beauvoir's The
     Second Sex (1949); second-wave feminism; the contraceptive pill; reforms in divorce,
     abortion (e.g. the Veil law 1975) and equal pay (EEC Article 119); differences between
     West and East; affluence (consumer durables, cars, television, supermarkets, credit);
     more leisure time and package holidays; criticism of consumerism.
   - Exam: marriage, the family and women (2007, 2009, 2020); affluence and the consumer society
     (2016).
   - SimpleStudy: none.
10. **Literature and social criticism, East and West; changing patterns in religious
    observance** [E4 C]
    - Syllabus: literature and social criticism, East and West; changing patterns in religious
      observance.
    - Key personalities: Alexander Solzhenitsyn; Simone de Beauvoir (part 2: writer and
      critic).
    - Key concepts: dissident writer; ecumenical movement.
    - Cover: Eastern dissident writing (Solzhenitsyn: the Gulag, One Day in the Life of Ivan
      Denisovich 1962, The Gulag Archipelago 1973, the Nobel prize 1970, expulsion 1974;
      Pasternak; Havel; samizdat); Western social criticism (Orwell, Camus, Sartre, Grass,
      Böll, de Beauvoir); religious observance: secularisation in the West, the decline in
      practice, the churches under communism, the ecumenical movement (the World Council of
      Churches 1948, Taizé), Islam in Western Europe.
    - Exam: Solzhenitsyn and/or de Beauvoir (2006, 2016, 2018, 2024, 2025); religious practice
      (2009, 2012, 2015).
    - SimpleStudy: none.
11. **Case study: the Second Vatican Council** [E4 C-CS]
    - Syllabus: case study **the Second Vatican Council**.
    - Key personalities: Pope John Paul II (religious role).
    - Key concepts: ecumenical movement.
    - Cover: John XXIII's reasons for calling it (aggiornamento); the sessions (1962–65) and
      Paul VI; the main documents (on the liturgy, the Church, revelation, and the Church in
      the modern world; on ecumenism, religious liberty and non-Christian religions);
      changes (the vernacular mass, lay participation, ecumenism, relations with Judaism);
      reactions (traditionalists, Lefebvre; progressives; Humanae Vitae 1968 as a turning
      point); John Paul II (election 1978, travels, conservative teaching, role in Poland and
      in the fall of communism); its influence on religious practice.
    - Exam: Vatican II and/or John Paul II (2007, 2011, 2017, 2025).
    - SimpleStudy: none.
12. **Youth and popular culture (including sport) and the mass media** [E4 C]
    - Syllabus: youth and popular culture (including sport) and the mass media.
    - Key personalities: John Lennon.
    - Key concepts: teenager; pop star; mass media.
    - Cover: the "teenager" and youth spending; rock 'n' roll and American influence; the
      Beatles and Lennon (Liverpool, Beatlemania, the 1960s, the peace campaign, his solo
      career and death 1980); 1968 student protests (Paris); fashion and subcultures; sport
      (the European Cup, the World Cup, the Olympics, television and money, Cold War
      sport); mass media (television's spread, Eurovision, commercial vs public broadcasting).
    - Exam: youth and popular culture, including sport (2008, 2012, 2015, 2019, 2022); Lennon
      (2016, 2018, 2021, 2025).
    - SimpleStudy: none.
13. **The impact of advances in the biological sciences, nuclear power and the computer** [E4 C]
    - Syllabus: the impact of (a) advances in the biological sciences, (b) nuclear power and
      (c) the computer.
    - Key concepts: information technology.
    - Cover: biology and medicine (antibiotics in mass use, the polio vaccine, the structure
      of DNA 1953, the pill, transplants, IVF 1978, genetic engineering); nuclear power
      (Calder Hall 1956, the French programme, the anti-nuclear movement, Three Mile Island,
      Chernobyl 1986); the computer (Colossus and early machines, the transistor and the
      microchip, mainframes, personal computers in the 1980s, effects on work and society).
    - Exam: biology, nuclear power and/or the computer (2010, 2020, 2023).
    - SimpleStudy: none.

### hist-eur5 — European retreat from empire and the aftermath, 1945–1990 [E5]

Key personalities: Mohandas Gandhi; Ho Chi Minh; Achmad Sukarno; David Ben-Gurion; Gamal Abdul
Nasser; Charles de Gaulle; Sese Seko Mobutu; a development worker in Africa; Nadine Gordimer;
Chinua Achebe. Key concepts: colonial rule; assimilation; de-colonisation; Zionism; terrorism;
tribalism; racism; (British) Commonwealth; (French) Union and Community; IMF; World Bank;
transnational economy; NGO (non-governmental organisation); cultural diversity; identity.

1. **World War II and Asia; case study: British withdrawal from India, 1945–1947** [E5 P;
   P-CS]
   - Syllabus: implications of World War II for European role in Asia; independence struggles
     and the reactions of the European powers (India); post-independence relations with the
     colonial power. Case study: **British withdrawal from India, 1945–1947**.
   - Key personalities: Mohandas Gandhi.
   - Key concepts: colonial rule; de-colonisation; (British) Commonwealth.
   - Cover: the war's effect on European prestige in Asia (Japanese conquests, the fall of
     Singapore); the Indian National Congress and Gandhi (satyagraha, the Salt March 1930,
     Quit India 1942); Jinnah and the Muslim League (the Pakistan demand); Labour's 1945
     victory and Attlee; the Cabinet Mission (1946); Direct Action Day (16 August 1946);
     Attlee's February 1947 deadline; Mountbatten; the Indian Independence Act and partition
     (15 August 1947); the Radcliffe line; violence and migration *(verify figures)*; Kashmir;
     Gandhi's assassination (January 1948); India and Pakistan in the Commonwealth; the
     importance of withdrawal for Britain and India; Gandhi's aims and achievements.
   - Exam: the 2012 DBQ (part (d) difficulties of withdrawal); causes, consequences,
     difficulties and importance of withdrawal (2008, 2010, 2015, 2017, 2018, 2020, 2021, 2023);
     Gandhi (2009, 2011, 2019, 2022, 2024).
   - SimpleStudy: none.
2. **Independence struggles in Indochina and the East Indies** [E5 P]
   - Syllabus: independence struggles and reactions of the European powers (Indochina and the
     East Indies); post-independence relations.
   - Key personalities: Ho Chi Minh; Achmad Sukarno.
   - Key concepts: colonial rule; de-colonisation; (French) Union.
   - Cover: French Indochina; Ho Chi Minh's career, the Viet Minh, the declaration of
     independence (2 September 1945); France's return and the French Union; the war
     (1946–54); Dien Bien Phu (1954); the Geneva Accords and the division of Vietnam; Laos
     and Cambodia briefly. The Dutch East Indies: the Japanese occupation; Sukarno's
     declaration of independence (17 August 1945); the Dutch "police actions" (1947–49); UN
     and US pressure; the transfer of sovereignty (1949); Sukarno's Indonesia (Bandung 1955,
     Guided Democracy, West New Guinea, Konfrontasi, the 1965 coup and his fall); internal and
     external problems.
   - Exam: Ho Chi Minh and/or Sukarno (2008, 2009, 2011, 2021, 2024); Sukarno's Indonesia (2017,
     2022).
   - SimpleStudy: none.
3. **British withdrawal from Palestine, the origins of the Arab–Israeli conflict and the Suez
   Crisis, 1956** [E5 P]
   - Syllabus: British withdrawal from Palestine and origins of Arab-Israeli conflict; the Suez
     Crisis, 1956.
   - Key personalities: David Ben-Gurion; Gamal Abdul Nasser.
   - Key concepts: Zionism; terrorism.
   - Cover: Zionism and the Balfour Declaration (1917); the Mandate; Jewish immigration and
     Arab opposition; the 1939 White Paper; the Holocaust's effect; Jewish armed groups (the
     Haganah, Irgun, the King David Hotel 1946); Britain's referral to the UN; the partition
     plan (November 1947); Israel's declaration (14 May 1948) and Ben-Gurion; the 1948–49 war
     and Palestinian refugees; Nasser's rise (1952 Free Officers), Arab nationalism and the
     Aswan Dam; nationalising the Suez Canal (26 July 1956); the Sèvres plan; the invasion
     (October–November 1956); US and Soviet pressure; UNEF; results for Britain, France,
     Nasser and Israel; how far Britain contributed to Middle East tensions.
   - Exam: Britain and Middle East tensions (2006, 2009, 2016); Palestine and/or Suez (2011,
     2020); origins of the Arab–Israeli conflict (2018); Europe's role in it (2021); Ben-Gurion
     and/or Nasser (2010, 2015, 2019, 2022, 2023); Suez (2007, 2020, 2024, 2025).
   - SimpleStudy: none.
4. **Africa and the "winds of change": Algeria and de Gaulle** [E5 P]
   - Syllabus: Africa — the "winds of change" (Algeria); post-independence relations with the
     colonial power.
   - Key personalities: Charles de Gaulle.
   - Key concepts: (French) Union and Community; assimilation; terrorism.
   - Cover: Macmillan's "wind of change" speech (1960) and the wave of independence in 1960;
     Algeria as part of France, the pieds-noirs; the FLN rising (1954); the war, torture and
     the Battle of Algiers; the May 1958 crisis and de Gaulle's return; the Fifth Republic;
     the French Community (1958); de Gaulle's path to self-determination; the OAS; the Évian
     Accords and independence (1962); the pieds-noirs' exodus and the harkis; post-independence
     relations; de Gaulle's handling of French colonialism.
   - Exam: de Gaulle and French colonialism (2025); why European countries retreated (2022,
     2025).
   - SimpleStudy: none.
5. **Africa: Nigeria, the Congo, Tanzania and Angola** [E5 P]
   - Syllabus: Africa — the "winds of change" (with particular reference to Nigeria, the
     Congo, Tanzania and Angola); post-independence relations with the colonial power.
   - Key concepts: tribalism; (British) Commonwealth; colonial rule.
   - Cover: Nigeria (federal structure and regions, independence 1960, ethnic and regional
     tensions, the coups of 1966, the Biafran war 1967–70); the Belgian Congo (Belgian rule,
     sudden independence June 1960, Lumumba, the army mutiny; the Katanga case study is s6);
     Tanganyika/Tanzania (peaceful independence under Nyerere 1961, the union with Zanzibar
     1964; ujamaa is s7); Angola (Portuguese rule, the MPLA, FNLA and UNITA, the war from
     1961, the Carnation Revolution 1974, independence 1975, civil war and Cold War
     involvement); relations with the former colonial powers (the Commonwealth, French
     networks, Belgium and Portugal); problems and opportunities of independence.
   - Exam: problems caused by British, Belgian or Portuguese withdrawal (2018); problems and
     opportunities of independence (2008); whether decolonisation was positive (2019); whether
     the colonial powers helped or hindered (2006).
   - SimpleStudy: none.
6. **Case study: the secession of Katanga, 1960–1965** [E5 S-CS]
   - Syllabus: case study **the secession of Katanga, 1960–1965**.
   - Key personalities: Sese Seko Mobutu.
   - Key concepts: tribalism; transnational economy.
   - Cover: Katanga's mineral wealth and Union Minière; Moïse Tshombe; the secession (11 July
     1960) and Belgian backing; Lumumba's appeal to the UN; ONUC; Irish troops (Niemba,
     November 1960; Jadotville, September 1961); Lumumba's overthrow and murder (January
     1961); Conor Cruise O'Brien and Operation Morthor; Hammarskjöld's death (September 1961);
     the end of secession (January 1963); Tshombe as Congo's Prime Minister (1964); Mobutu's
     career (army chief, the 1960 and 1965 coups, Zaire, rule to 1990); national and
     international significance.
   - Exam: the 2013 DBQ (part (d) why Katanga seceded and why it drew international
     involvement); why it seceded and its results (2006, 2007, 2011, 2016, 2019); Suez and/or
     Katanga internationally (2020, 2024).
   - SimpleStudy: none.
7. **Economic consequences of decolonisation: the Lomé Conventions, trade, aid and famine,
   and Nyerere's ujamaa** [E5 S]
   - Syllabus: economic consequences of the process of de-colonisation; the Lomé Conventions;
     trade, aid and famine in post-colonial Africa; Julius Nyerere and the policy of ujamaa.
   - Key personalities: a development worker in Africa (a named, documented example, chosen
     in the package, e.g. an Irish aid worker or missionary doctor *(verify)*).
   - Key concepts: IMF; World Bank; transnational economy; NGO.
   - Cover: colonial economies (cash crops, minerals, infrastructure geared to export); terms
     of trade and dependence on a few commodities; the Yaoundé and Lomé Conventions (Lomé I
     1975: preferential access, STABEX, aid); debt and the IMF and World Bank's structural
     adjustment (1980s); aid (bilateral and multilateral, its benefits and criticisms); famine
     (Biafra 1968, the Sahel in the 1970s, Ethiopia 1984–85 and Band Aid/Live Aid); NGOs
     (Concern, Trócaire, Oxfam); Nyerere (the Arusha Declaration 1967, ujamaa villages,
     villagisation, education and health results, economic failure, his reputation).
   - Exam: social and economic effects on Africa (2009, 2020, 2023, 2024); Nyerere, ujamaa
     and/or Lomé (2007, 2010, 2015, 2017); development workers' problems (2010).
   - SimpleStudy: none.
8. **Immigration patterns and policies in Britain and France; multi-racial Britain** [E5 S; C]
   - Syllabus: immigration patterns and policies in different European states — Britain,
     France; cultural diversity in multi-racial Britain (and France).
   - Key concepts: racism; cultural diversity; identity; assimilation.
   - Cover: Britain: the British Nationality Act (1948); the Empire Windrush (1948); migration
     from the Caribbean and South Asia; labour recruitment; the Notting Hill riots (1958); the
     Commonwealth Immigrants Acts (1962, 1968) and the Immigration Act (1971); Enoch Powell's
     1968 speech; the Race Relations Acts (1965, 1968, 1976); discrimination in housing and
     jobs; Brixton and other 1981 riots, the Scarman Report; multicultural Britain (music,
     food, religion, politics). France: North African and West African immigration, the
     bidonvilles, the 1974 halt to labour migration and family reunification; the French
     assimilation model vs British multiculturalism.
   - Exam: race relations in Britain and/or France (2006, 2009, 2021, 2023); multi-racial
     societies (2015, 2024); Britain or France (2010, 2016); similarities and differences
     (2019); cultural diversity in Britain (2007).
   - SimpleStudy: none.
9. **Case study: race relations in France in the 1980s** [E5 C-CS]
   - Syllabus: case study **race relations in France in the 1980s**.
   - Key concepts: racism; assimilation; identity; cultural diversity.
   - Cover: the banlieues and the second generation ("beurs"); unemployment and policing; the
     Minguettes unrest (1981); the March for Equality and Against Racism (1983); SOS Racisme
     (1984, "Touche pas à mon pote"); the Front National's rise (Le Pen; Dreux 1983; the 1984
     European elections and 1986 parliamentary seats); the 1986 Pasqua laws; the 1989
     headscarf affair; government responses and the link with France's colonial past and
     Algeria; similarities with and differences from Britain.
   - Exam: how France became multi-racial and race relations in the 1980s (2011); France's loss
     of empire and 1980s racial tension (2018).
   - SimpleStudy: none.
10. **Culture and religion: indigenous and colonial culture, Islam and Christianity, English as
    a world language and post-colonial literature** [E5 C]
    - Syllabus: tensions between indigenous culture and colonial culture; the spread of Islam
      and Christianity in Africa; the Islamic faith in Europe; English as a world language;
      post-colonial literature.
    - Key personalities: Nadine Gordimer; Chinua Achebe.
    - Key concepts: identity; cultural diversity; assimilation.
    - Cover: colonial education and the "civilising mission"; négritude (Senghor) and
      cultural nationalism; missions and African churches; the spread of Islam in West and East
      Africa; Islam in Europe (mosques, communities in Britain and France, the Rushdie affair
      1989); English as a world language (colonial legacy, the Commonwealth, American power,
      media); post-colonial literature: Achebe (Things Fall Apart 1958, the language debate),
      Gordimer (apartheid South Africa in her novels, censorship, the Nobel prize 1991),
      Ngũgĩ, Soyinka.
    - Exam: Islam and Christianity in Africa and/or Islam in Europe (2017, 2020, 2022);
      colonialism's legacy in literature and language (2008); Gordimer and/or Achebe (2011,
      2015, 2016, 2025).
    - SimpleStudy: none.

### hist-eur6 — The United States and the world, 1945–1989 [E6]

Key personalities: Harry Truman; Joe McCarthy; Martin Luther King; Lyndon Johnson; the
"Organization Man"; Betty Friedan; Norman Mailer; Muhammad Ali; Billy Graham; Marilyn Monroe.
Key concepts: corporate capitalism; globalisation; internationalism; imperialism; consumerism;
technological development; the military-industrial complex; discrimination; liberalism;
presidential bureaucracy; mass media; public opinion; fundamentalism; moral majority;
feminism.

1. **US politics: structures and tensions, and the Presidency from Roosevelt to Reagan** [E6 P]
   - Syllabus: US politics: structures and tensions — federal government and the states; the
     separation of powers; the Presidency from Roosevelt to Reagan.
   - Key personalities: Harry Truman (part 1: domestic record).
   - Key concepts: liberalism; presidential bureaucracy; public opinion.
   - Cover: the Constitution, federalism and states' rights (the civil rights conflicts); the
     separation of powers and checks and balances (the Supreme Court, Congress vs President);
     the growth of the executive (presidential bureaucracy); each president's main record:
     Roosevelt's legacy, Truman (the Fair Deal, the Taft-Hartley conflict, 1948), Eisenhower,
     Kennedy (the New Frontier, assassination 1963), Johnson (the Great Society; s3 covers
     Vietnam), Nixon (Watergate and resignation 1974), Ford, Carter, Reagan (Reaganomics,
     Iran-Contra); whether presidents acted for the good of America.
   - Exam: the Presidency from Roosevelt to Reagan (2011, 2017); Truman (2018, 2024); Truman or
     Johnson (2012, 2013, 2016); Reagan (2006).
   - SimpleStudy: US politics.
2. **US foreign policy, 1945–1972: Berlin, Korea, Cuba and Vietnam** [E6 P]
   - Syllabus: US foreign policy, 1945–1972: Berlin, Korea, Cuba, Vietnam.
   - Key personalities: Truman (part 2: foreign policy and overall evaluation).
   - Key concepts: internationalism; imperialism.
   - Cover: containment, the Truman Doctrine, the Marshall Plan, NATO; Berlin (the airlift
     1948–49, the Wall 1961, Kennedy's 1963 visit); Korea (1950–53: causes, the UN, Inchon,
     Chinese intervention, MacArthur's dismissal, the armistice); Cuba (the revolution 1959,
     the Bay of Pigs 1961, the missile crisis October 1962 and its resolution); Vietnam to
     1972 (from aid to France, through Eisenhower's advisers, Kennedy, Johnson's escalation
     (s3), to Nixon's Vietnamisation and expansion into Cambodia); how successful US leaders
     were.
   - Exam: Berlin, Korea, Cuba (2010, 2015, 2025); Korea, Cuba, Vietnam (2022); Korea or Vietnam
     (2006); Korea or Cuba (2023); Korea and/or Vietnam (2019); Korea, Cuba, SALT and Star Wars
     (2012).
   - SimpleStudy: foreign policy 1945–1972.
3. **Case study: Lyndon Johnson and Vietnam, 1963–1968** [E6 P-CS]
   - Syllabus: case study **Lyndon Johnson and Vietnam, 1963–1968**.
   - Key personalities: Lyndon Johnson.
   - Key concepts: imperialism; public opinion; the military-industrial complex.
   - Cover: Johnson's background and political skills; what he inherited in Vietnam; the Gulf
     of Tonkin incidents and resolution (August 1964); the 1964 election; Rolling Thunder and
     the first combat troops (March 1965); escalation and troop numbers *(verify)*;
     Westmoreland's strategy; the "credibility gap"; the anti-war movement and Congress
     (Fulbright's hearings); the costs to the Great Society; the Tet Offensive (January
     1968) and its effect on opinion; Johnson's 31 March 1968 speech; why he could not win;
     his successes and failures overall.
   - Exam: the 2008 DBQ (part (d) why Johnson couldn't win) and 2020 DBQ (part (d) how Vietnam
     affected his presidency); Johnson's presidency and leadership (2010, 2025); Vietnam's
     importance for both countries (2018); why the US lost (2011).
   - SimpleStudy: LBJ and Vietnam case study.
4. **Domestic factors in US foreign policy: McCarthyism, the anti-war movement and race
   relations** [E6 P]
   - Syllabus: domestic factors in US foreign policy: McCarthyism, the anti-war movement, race
     relations.
   - Key personalities: Joe McCarthy.
   - Key concepts: public opinion; mass media; liberalism.
   - Cover: the Red Scare (HUAC, the Hollywood Ten, Hiss, the Rosenbergs); McCarthy's Wheeling
     speech (February 1950), his methods, the Army–McCarthy hearings (1954), his censure; the
     effect on foreign policy and US society; the anti-war movement (teach-ins, the draft,
     students and SDS, Martin Luther King's 1967 opposition, Ali's refusal, 1968 Chicago, Kent
     State 1970, the Pentagon Papers 1971); race relations and the Cold War image of the USA.
   - Exam: McCarthyism and/or the anti-war movement (2006, 2007, 2016, 2023); McCarthy (2019).
   - SimpleStudy: domestic factors in foreign policy.
5. **The decline of Cold War certainties, 1973–1989: withdrawal from Vietnam, détente, SALT
   and Star Wars** [E6 P]
   - Syllabus: decline of Cold War certainties, 1973–1989: withdrawal from Vietnam, détente,
     SALT and Star Wars.
   - Key concepts: internationalism; technological development.
   - Cover: the Paris Peace Accords (1973) and the fall of Saigon (1975); the War Powers
     Resolution (1973); Nixon and Kissinger's détente (Moscow 1972, the opening to China);
     SALT I (1972) and SALT II (1979, unratified); Carter (human rights, the Iran hostages,
     Afghanistan 1979, the Olympic boycott); Reagan's build-up, the "evil empire", the
     Strategic Defense Initiative ("Star Wars", 1983); the Reagan–Gorbachev summits and the
     INF Treaty (1987); the end of the Cold War.
   - Exam: foreign policy 1973–1989 (2007); SALT and Star Wars (2012); the moon landing and/or
     Star Wars (2016, 2024).
   - SimpleStudy: decline of Cold War certainties.
6. **The US economy, 1945–1968: sources of the boom and the multinational corporation** [E6 S]
   - Syllabus: sources of the US economic boom: the war, public investment and international
     financing, 1945–1968; the development of the US industrial structure: the multinational
     corporation, 1945–1968.
   - Key personalities: the "Organization Man".
   - Key concepts: corporate capitalism; globalisation; the military-industrial complex.
   - Cover: wartime production and savings; the GI Bill; public investment (defence spending,
     the Interstate Highway Act 1956, space and research); international financing (Bretton
     Woods, the dollar, the IMF, the World Bank, Marshall Aid); the military-industrial
     complex (Eisenhower's 1961 warning); the multinational corporation (General Motors, IBM,
     Coca-Cola, ITT), and how it spread abroad; William H. Whyte's The Organization Man (1956)
     as a portrait of corporate life and conformity.
   - Exam: why the boom happened and its impact (2010); multinationals and the military-
     industrial complex (2013); achievements 1945–1968 (2017).
   - SimpleStudy: postwar economic boom.
7. **The US economy, 1968–1989: Vietnam, the federal deficit, recession and international
   competition** [E6 S]
   - Syllabus: the Vietnam War; the federal deficit; domestic recession; international
     competition from Japan and Europe, 1968–1989.
   - Key concepts: globalisation; corporate capitalism.
   - Cover: the cost of the war and the Great Society together; inflation; the end of the
     Bretton Woods system (1971); the oil shocks (1973, 1979) and stagflation; the decline of
     the "rust belt" (steel and cars) and Japanese and European competition; Reaganomics (tax
     cuts, defence spending, deficits, deregulation), the 1982 recession and recovery; the
     trade deficit and debt by 1989.
   - Exam: success and decline (2012); strengths and weaknesses 1945–1989 (2016, 2022); what
     limited growth 1968–1989 (2017).
   - SimpleStudy: affluence and economic decline.
8. **Demographic growth and affluence: consumerism, leisure, work, women and the family** [E6 S]
   - Syllabus: demographic growth; affluence — consumerism, leisure, the role of work, the
     changing role of women and the family.
   - Key personalities: Betty Friedan; Marilyn Monroe (as an image of women; career in s11).
   - Key concepts: consumerism; feminism.
   - Cover: the baby boom and population shifts (to the suburbs and the Sun Belt); Levittown
     and suburban life; consumer goods, credit, advertising and television; leisure; the role
     of work (white-collar growth, corporate culture); women (the post-war return to the home,
     rising employment, Friedan's The Feminine Mystique 1963, NOW 1966, the ERA, Roe v. Wade
     1973) and the changing family; the American Dream as ideal and reality.
   - Exam: the American Dream and reality (2015, 2025); Friedan and/or Monroe and women's
     changing role (2024); Friedan and others (2007, 2017, 2022).
   - SimpleStudy: age of consensus.
9. **Troubled affluence: racial conflict and the civil rights movement, urban poverty, drugs and
   crime** [E6 S]
   - Syllabus: troubled affluence: racial conflict, urban poverty, drugs and crime.
   - Key personalities: Martin Luther King (overall career; his role in Montgomery is s10).
   - Key concepts: discrimination; liberalism.
   - Cover: segregation and Jim Crow; Brown v. Board of Education (1954) and Little Rock
     (1957); the sit-ins and Freedom Rides (1960–61); Birmingham and the March on Washington
     (1963); the Civil Rights Act (1964) and Voting Rights Act (1965); Malcolm X and Black
     Power; King's career, methods, later campaigns and assassination (1968); the urban riots
     (Watts 1965, Detroit 1967) and the Kerner Report (1968); urban poverty (Harrington's
     The Other America 1962, the War on Poverty); drugs (heroin, the 1980s crack epidemic,
     the "war on drugs") and crime; how far racial equality was achieved by 1989.
   - Exam: race relations and racial equality (2006, 2013, 2019, 2022, 2023); King (2011, 2017).
   - SimpleStudy: racial conflict and early desegregation; Civil Rights Movement.
10. **Case study: the Montgomery bus boycott, 1956** [E6 S-CS]
    - Syllabus: case study **the Montgomery bus boycott, 1956**.
    - Key personalities: Martin Luther King (role in the boycott).
    - Key concepts: discrimination.
    - Cover: segregation on Montgomery's buses; earlier protests (Claudette Colvin); Rosa
      Parks' arrest (1 December 1955) and her background in the NAACP; E.D. Nixon, Jo Ann
      Robinson and the Women's Political Council; the Montgomery Improvement Association and
      King's leadership; the car pools and the churches; white resistance (the White
      Citizens' Council, bombings, arrests, the injunction against car pools); Browder v.
      Gayle and the Supreme Court ruling (November 1956); desegregated buses (21 December
      1956), after 381 days; the significance for the civil rights movement, King and
      non-violence.
    - Exam: the 2009 DBQ (part (d) its importance) and 2021 DBQ (part (d) how far it brought
      change); why it happened, how it was run and how it advanced civil rights (2007, 2012,
      2015, 2017, 2024).
    - SimpleStudy: Montgomery Bus Boycott case study.
11. **Culture: consensus and its collapse — Hollywood, the red scare, youth culture,
    counter-culture and multiculturalism** [E6 C]
    - Syllabus: Consensus? 1945–1968: Hollywood — the American Dream; the "red scare".
      Collapse of consensus, 1968–1989: youth culture, "counter-culture", and
      multiculturalism.
    - Key personalities: Marilyn Monroe; Norman Mailer; Muhammad Ali.
    - Key concepts: liberalism; mass media.
    - Cover: Hollywood's studio system and the American Dream on screen; the red scare in
      Hollywood (blacklists); Monroe's career, image and death (1962); 1950s youth (rock 'n'
      roll, Elvis, James Dean, the Beats); Mailer's career (The Naked and the Dead 1948,
      "The White Negro" 1957, The Armies of the Night 1968, his public persona); the 1960s
      counter-culture (hippies, Haight-Ashbury, Woodstock 1969, drugs, music, protest);
      multiculturalism (Black Power, the Chicano and Native American movements, gay rights
      and Stonewall 1969, women's liberation); Ali's career (Olympic gold 1960, the title
      1964, the Nation of Islam and his name change, his draft refusal 1967 and the 1971
      Supreme Court ruling, comeback).
    - Exam: Hollywood 1945–1968 (2012); Monroe, Ali, Mailer and others (2007, 2011, 2017, 2018,
      2019, 2022).
    - SimpleStudy: collapse of consensus.
12. **Religion, the mass media and mass higher education in modern American culture** [E6 C]
    - Syllabus: religion in modern American culture; the mass media in modern American
      culture; mass higher education.
    - Key personalities: Billy Graham.
    - Key concepts: fundamentalism; moral majority; mass media; public opinion.
    - Cover: post-war religious revival ("In God We Trust", 1956); Graham's career (the 1949
      Los Angeles crusade, crusades, presidents, television); Catholic America and JFK
      (1960); the Black churches and civil rights; evangelicalism and fundamentalism;
      televangelism; the Moral Majority (Falwell, 1979) and the religious right in the 1980
      election; the mass media (network television, news and Vietnam, Watergate and the
      press, advertising); mass higher education (the GI Bill, state universities, Berkeley's
      Free Speech Movement 1964, campus protest).
    - Exam: religion and/or mass media (2013); religion as a growing force (2025); Graham (2011,
      2018, 2019, 2022).
    - SimpleStudy: religion in American culture.
13. **Advances in military, space and information technology; case study: the Moon landing,
    1969** [E6 C; C-CS]
    - Syllabus: advances in military, space and information technology. Case study: **the
      Moon landing, 1969**.
    - Key concepts: technological development; the military-industrial complex.
    - Cover: military technology (the H-bomb, ICBMs and submarine missiles, jets, satellites,
      SDI); the space race (Sputnik 1957, NASA 1958, Mercury, Gagarin 1961, Kennedy's 1961
      pledge, Gemini); Moon landing case study in depth: Apollo's organisation and cost
      *(verify)*, the Apollo 1 fire (1967), Apollo 8, Apollo 11 (Armstrong, Aldrin, Collins;
      20 July 1969), worldwide television coverage, significance at home and abroad, later
      missions and declining interest, the Shuttle (1981) and Challenger (1986); information
      technology (ENIAC, the transistor, IBM, the integrated circuit and microprocessor,
      ARPANET 1969, Apple and the IBM PC, Silicon Valley).
    - Exam: the moon landing (2010, 2011, 2016, 2019, 2023, 2024); military, space and
      information technology (2006, 2015, 2018).
    - SimpleStudy: technology; Moon Landing case study.

---

## Appendix A — Where the syllabus differs from SimpleStudy and from the repo's earlier assumptions

### A1. SimpleStudy covers only 5 of the 12 Later Modern topics

SimpleStudy's history course (`guide-simplestudy.md`) has units for `hist-ire2`, `hist-ire3`,
`hist-ire5`, `hist-eur3` and `hist-eur6`, plus an assessment unit. It has **nothing** for
`hist-ire1`, `hist-ire4`, `hist-ire6`, `hist-eur1`, `hist-eur2`, `hist-eur4` or `hist-eur5`.
Those seven chapters must be built from the syllabus alone. Within the units it has, its topic
lists also leave out several elements:

- `hist-ire2`: the co-operative movement and educational reforms (it has only "education and
  Catholic identity"); the first Sinn Féin and the Irish Volunteers are not named.
- `hist-ire3`: impact of partition on economy and society; Anglo-Irish relations as a theme;
  Northern Ireland's Unionist government after 1921 is only "establishment of Northern
  Ireland".
- `hist-ire5`: the impact of the Troubles on the economy; ecumenism.
- `hist-eur3`: church–state relations; the technology of warfare; the Soviet alternative.
- `hist-eur6`: US political structures (federal government and the states; the separation of
  powers); mass higher education; the multinational corporation.

SimpleStudy has nothing that falls outside the syllabus. Its "Assessment — Research Study" unit
matches Part I C (Appendix B).

### A2. Corrections to the repo's earlier assumptions (made in this restructure)

- `pipeline/scaffold/history.json` said the documents-based question is "on a rotating Ireland
  case-study topic". **Wrong:** the SEC rotates the prescribed topic between Irish and Europe
  topics (2024–2025 were `hist-eur3`; 2028 is `hist-eur6`). The note now says so and names the
  2026–2027 topic.
- `relevant-resources/relevant-resources.js` called the document "Published syllabus" and
  mentioned a draft under consultation. It now gives the curriculumonline.ie label ("for
  examination to June 2028") and points to the 2027 specification as a separate, later course.
- `pipeline/resources/history/manifest.json` and `pipeline/resources/README.md` now record the
  exam window and the prescribed topic. The cutoff (first examined 2006) was already correct.

### A3. Wrong-course content removed from the app (2026-11-05)

- **156 exam-bank entries from the 2005 papers** (Higher and Ordinary), which were set on the
  syllabus before this one (different periods: Irish history 1477–1625 and 1868–1966, European
  history 1453–1618 and 1870–1966; a "research topic" essay; no documents-based question). They
  were pulled as a "REFERENCE" year, and the tagger had filed Early Modern questions (e.g. the
  Plantation of Ulster, Zwingli and Calvin, Florence in the Renaissance) under Later Modern
  chapters `hist-ire1`, `hist-eur1`, `hist-eur2` and `hist-eur5`. Fourteen more were
  untaggable. The pipeline no longer pulls the reference year by default.
- **Three note blocks in `history-content.js` (`hist-eur5`)** on topics the syllabus doesn't
  list: "Kenya and the Mau Mau", "Apartheid in South Africa" and "Soweto, sanctions and the end
  of apartheid". Rhodesia was cut from "The Portuguese empire and Rhodesia", leaving Angola and
  the Portuguese wars, which the syllabus names.
- **One test question (`hist-eur5-1`)** on the end of apartheid.
- **Three flashcards:** "League of Nations Union" (`hist-ire2`: not in the syllabus, and the
  card was wrong); "Ceasefire (1994–1997)" and "Good Friday Agreement (1998)" (`hist-ire5`:
  after the topic's 1993 end date).

### A4. Kept, but needing a decision

- **The Spanish Civil War** has a note block in `history-content.js` and a test question
  (`hist-eur3-1`, Franco's victory). The syllabus says "origins and growth of the fascist
  regimes in Europe" but names no Spanish element, case study or personality. No Higher Level
  question 2006–2025 asked about Spain. The new notes should mention Spain only as comparison
  (s1); whether to keep the old block and question until then is the user's call.
- **Early Modern field:** see Appendix B.

## Appendix B — Syllabus content with no home in an existing chapter

1. **Part I A–B, "Introduction: history and the historian" and the documents-based study
   skills.** Placed in **`hist-ire2-s11`** for 2027, because `hist-ire2` is the prescribed
   topic and every student takes it. Rotating topics will move the DBQ: from 2028 it is
   `hist-eur6`, so this subsection would need to move or be copied. **Proposal (needs
   approval):** a dedicated chapter, e.g. `hist-skills`, holding Part I A–B and the research
   study, so it doesn't depend on the year's prescribed topic.
2. **Part I C, the research study (20%).** No chapter. The syllabus and Guidelines require:
   choosing a narrow, significant, verifiable subject (local history and historiography
   allowed); primary or specialist secondary sources, at least three at Higher Level; the
   outline plan (defining and justifying the subject, aims, approach, sources; about one A4
   page); the evaluation of sources (relevance, strengths and weaknesses; about one A4 page);
   the extended essay (findings, a review of the process, coherent structure; about 2,000
   words at Higher Level); authentication and the internet protocol. For June 2027 candidates
   the report is likely submitted before most of the app's notes ship *(check the SEC's 2027
   date)*, so its priority is low. **Proposal:** put it in the `hist-skills` chapter above.
3. **The Early Modern field (12 topics, 1492–1815)** has no chapters. Students who take it sit a
   different paper; its 2026–2027 DBQ topic is Ireland Topic 1, Reform and Reformation in Tudor
   Ireland. Adding it would mean 12 new chapters and their own exam bank, which the user must
   approve. The app currently presents history as the Later Modern course only.

## Appendix C — Coverage check

- **Chapters:** all 12 history chapter IDs in `data.js` and `pipeline/scaffold/history.json`
  appear above, unchanged.
- **Subsections:** 128 in total (the app currently has one outcome per chapter): `hist-ire1` 7,
  `hist-ire2` 11, `hist-ire3` 11, `hist-ire4` 8, `hist-ire5` 10, `hist-ire6` 10, `hist-eur1` 11,
  `hist-eur2` 11, `hist-eur3` 13, `hist-eur4` 13, `hist-eur5` 10, `hist-eur6` 13. A 2027
  student studies `hist-ire2` (11) plus three other chapters.
- **Syllabus items mapped:** about 197 listed elements (counting each element sentence once;
  some combine several items), 36 case studies, 120 key personalities and 152 key concepts
  across the 12 topics. Every element, case study, key personality and key concept is assigned
  to exactly one subsection above. Key personalities split across subsections (e.g. O'Connell,
  Parnell, de Valera, Bismarck) say which part goes where. Part I (working with evidence) is in
  `hist-ire2-s11`; the research study is in Appendix B.
- **Coverage before the 2026-11-06 notes** (kept for the record; all 128 subsections now have
  authored notes, see "Read this first"):
  (`history-content.js`: one or two paragraphs per heading, written
  before this outline; flashcards in `history-flashcards.js`): **no subsection is covered
  fully.** About **91 are covered thinly** (one paragraph or a few flashcards touch the topic)
  and about **37 not at all**. The gaps are biggest in `hist-eur4` (8 of 13 not covered: the
  economies, society, culture, Vatican II and science), `hist-eur1` (4), `hist-eur5` (4),
  `hist-eur6` (4), `hist-ire3` (3), `hist-ire4` (3), `hist-ire5` (3) and `hist-eur3` (3). In the
  compulsory 2027 chapter, `hist-ire2`, the three case studies are covered only thinly and the
  skills subsection (s11) not at all.
