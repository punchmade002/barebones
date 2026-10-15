# Leaving Cert Geography (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **How to write the notes:** follow `course-outlines/NOTES_STANDARD.md` (rules, output format,
  and a fully worked example for `geo-rivers`). This outline says what to cover; that file says
  how to write it.
- **The syllabus:** the NCCA *Leaving Certificate Geography Syllabus (Ordinary and Higher
  Levels)*, © 2003, first examined 2006 and examined to June 2027. The official PDF is
  `pipeline/resources/geography/spec-syllabus.pdf` (also in
  `relevant-resources/syllabi/geography.pdf`). Section numbers in brackets, e.g. **[1.5]**, are
  the syllabus's own numbers.
- **Do not use the 2026 specification**
  (`relevant-resources/syllabi/geography-2026-spec.pdf`). It is a different course, first
  examined in 2028.
- **Chapters** are the app's 25 geography chapter IDs (`data.js`,
  `pipeline/scaffold/geography.json`). Past exam questions are tagged to these IDs, so keep
  every ID exactly as written.
- **What each subsection contains:**
  - **"Syllabus"** is what the syllabus says students should study, often in its own words.
    This is the required scope; every item must be covered.
  - **"Settings"** are the syllabus's own example places. They're suggestions, not
    requirements, but they're a good default.
  - **"SimpleStudy"** names the matching topic(s) in SimpleStudy's Higher Level course
    (recorded 2026-10-15). Use them for structure and pacing only; write all prose in your own
    words.
- **Higher vs Ordinary level:** the syllabus doesn't mark individual core or elective topics as
  Higher Level only. Both levels study the same content; Higher Level outcomes demand more
  detail, evaluation and assessment. Only the four **Optional Units are Higher Level only**.
- **Where the syllabus sets a choice, write content for every option,** so students can pick.
  The choices are: one human interaction with the rock cycle [1.2]; detail on one surface
  process [1.5]; one human interaction with surface processes [1.7]; one GIS study [skills];
  one biome [7.3]; one European case-study region [8.3]; one climate [9.5].
- **Students take one elective:** Unit 4 (Economic) **or** Unit 5 (Human).
- **Assessment:** written exam 80% (Higher and Ordinary papers); Geographical Investigation
  report 20%. Short-answer and multi-part questions throughout; longer essay-style answers only
  in the Optional Units. Higher Level 30-mark answers are marked as about 15 significant relevant
  points (SRPs), so notes must be dense with distinct, specific facts.

---

## Core Unit 1 — Patterns and Processes in the Physical Environment (Section 1)

All students. The aim is to examine the relationship between the tectonic cycle, the rock cycle
and the processes of landform development. Higher Level outcomes add: show how landforms are a
balance through time between endogenic (internal) and exogenic (external) forces, and assess
the impact of human activity on physical processes at different scales.

### geo-plate-tectonics — Plate Tectonics [1.1]
1. **The internal structure of the earth:** crust, mantle, core.
   SimpleStudy: The Earth's Structure.
2. **The plate tectonics model:** how the theory developed (continental drift, sea-floor
   spreading); the global geography of lithospheric plates; the mobility of the crust producing
   endogenic forces.
   - Settings: the position of Ireland in relation to plate boundaries now and in past geological
     periods; the global geography of lithospheric plates.
   - SimpleStudy: Continental Drift; Sea-Floor Spreading; The Theory of Plate Tectonics.
3. **Plate boundaries as zones of crustal construction and destruction:** constructive,
   destructive and passive/transform boundaries; how crustal structures are created, modified
   and destroyed in the tectonic cycle.
   SimpleStudy: Plate Boundaries; The Pacific Ring of Fire.

### geo-volcanoes-earthquakes — Volcanoes, Earthquakes and Tectonic Landforms [1.1, 1.3]
1. **The geography of volcanoes** [1.1]: the global distribution of volcanic activity; how
   eruptions and their effects may be predicted.
   - Settings: Antrim basalt extrusion and the opening of the Atlantic; the global geography of
     volcanic activity.
   - SimpleStudy: Volcanic Activity.
2. **The geography of earthquakes** [1.1]: the global distribution of seismic activity; how
   earthquakes and their effects may be predicted.
   SimpleStudy: Earthquake Activity.
3. **Landforms from volcanic and plutonic structures** [1.3]: lava flows, volcanoes, joints.
   - Settings: the Antrim plateau and the Leinster batholith; Hawaii, Iceland, Devon and
     Cornwall.
   - SimpleStudy: Volcanic Activity.
4. **Landforms from sedimentary structures** [1.3]: bedding planes, joints.
   Settings: the Dartry–Cuilcagh upland; the Paris Basin, the Brecon Beacons.
5. **Landforms from structures of deformation** [1.3]: folding, doming, and faulting by both
   vertical and horizontal displacement.
   - Settings: the South Ireland ridge-and-valley province, the Armorican thrust front, Donegal
     thrust and tear faults; the Appalachians, the Weald, the Alps.
   - SimpleStudy: Folding and Faulting Activity.

### geo-rocks-weathering — Rocks, Weathering and Mass Movement [1.2, 1.4, 1.5, 1.7]
1. **The rock cycle and rock formation** [1.2]: the geotectonic setting of how igneous (both
   plutonic and volcanic), metamorphic and sedimentary rocks form; rocks continually formed,
   modified, destroyed and reconstituted.
   - Settings: Irish rock types as illustrations of plutonic, volcanic, metamorphic and
     sedimentary settings; the North American continent with its active and trailing plate
     margins.
   - SimpleStudy: Rocks.
2. **Human interaction with the rock cycle** [1.2]: the syllabus says to pay particular
   attention to **one of** mining, extraction of building materials, oil/gas exploitation, or
   geothermal energy production. Write one section for each. Settings: appropriate national and
   international examples.
3. **Weathering processes** [1.2]: physical (mechanical) and chemical weathering.
   SimpleStudy: Weathering Processes and Landforms.
4. **Landforms associated with particular rock types** [1.4]: e.g. karst landforms on
   limestone; granite landscapes; how spatial variations in rock type influence the physical
   landscape.
   - Settings: the Burren, the Marble Arch upland, the Mask–Corrib lowland, Wicklow granite
     landscapes; Slovenia, S.W. China, Kentucky, Jamaica, Dartmoor.
   - SimpleStudy: Weathering Processes and Landforms.
5. **Mass movement (mass wasting) processes and the factors governing them** [1.2, 1.5].
   - Settings: Antrim coastal landslides, bog bursts in N.W. Ireland; mudslides in Italy, the
     Middle East, South America.
   - SimpleStudy: Mass Movement.
6. **Erosion by wind** [1.2]: aeolian processes. This is listed in the syllabus but SimpleStudy
   has no topic for it.
7. **Human interaction: mass movement** [1.7, one of three]: the impact of overgrazing,
   overcropping and deforestation on mass movement processes. Settings: appropriate Irish and
   international examples.

### geo-glaciation — Glaciation and Isostasy [1.5, 1.6]
1. **Glacial processes, patterns and associated landforms** [1.5]: erosion, transport and
   deposition by ice, and the landforms of each. Settings: appropriate Irish examples.
   SimpleStudy: Glaciation and Glacial Processes.
2. **Isostasy** [1.6]: crustal uplift in response to isostatic readjustment; landscapes that
   show uplift and denudation temporarily out of balance.
   SimpleStudy: Isostasy.

### geo-rivers — Rivers [1.5, 1.6, 1.7]
1. **Fluvial processes, patterns and associated landforms** [1.5]. Settings: appropriate Irish
   examples.
   SimpleStudy: River Action.
2. **Fluvial adjustment to base level** [1.6]: rejuvenation and its landforms.
   Settings: rivers of N.W. Ireland.
3. **Cyclic landscape development and peneplains** [1.6]: the balance between endogenic and
   exogenic forces through time. Settings: planation surfaces in Munster.
4. **Human interaction: river processes** [1.7, one of three]: the impact of hydro-electric
   dams, canalisation and flood control measures. Settings: appropriate Irish and international
   examples.

### geo-sea — Coasts and the Sea [1.5, 1.7]
1. **Coastal processes, patterns and associated landforms** [1.5]. Settings: appropriate Irish
   examples.
   SimpleStudy: Coasts and the Sea.
2. **Human interaction: coastal processes** [1.7, one of three]: the impact of recreational
   pressures, coastal defence work, and conservation and management measures. Settings:
   appropriate Irish and international examples.

Note for [1.5]: students study all four surface processes (mass movement, fluvial, coastal,
glacial) and one in detail. Write all four in full.

---

## Core Unit 3 — The Geographical Investigation and Skills Unit (Part One + 20% report)

All students. The syllabus says skills should be taught throughout the core, elective and
optional units, not in isolation.

### geo-mapwork — Map Skills and the Geographical Investigation
1. **Map interpretation:** coordinate systems (latitude and longitude); grid references;
   scale, distance and direction; altitude and slope; sketch maps; symbol recognition;
   cross-sections; pattern recognition; statistical mapping; absolute and relative location.
   - SimpleStudy: Ordnance Survey Maps: Scale, Grid References, and Direction; Distance and
     Area; Height and Slope; Sketch Maps and Cross-Sections; Drainage Patterns: Physical
     Landscape; Other Landscapes and Settlements.
2. **Textual sources:** using a range of textual and secondary sources, past and present,
   especially for the investigation.
3. **The Geographical Investigation (20%):** a topic from the SEC's annual list (issued in
   Leaving Cert Year 1); an individual report due at the end of term one of Year 2; no group
   projects; sources at about 60% primary and 40% secondary; authenticity verified by teacher
   and principal.
   - **Stages:**
     - Introduction: topic, hypothesis or aim, objectives, the information needed.
     - Planning: collection methods, questionnaire or recording-sheet design, locations.
     - Collection of data: instruments and measurements, field observations, questionnaires
       and surveys, documentary sources, problems encountered.
     - Preparation of the report: organising data; illustrations, graphs, maps and tables; ICT.
     - Conclusion and evaluation: analysis, valid conclusions, comparison with established
       theory, evaluating hypotheses, validity and improvements.
   - SimpleStudy: Assessment: Geographical Investigation.

### geo-aerial-photographs — Aerial Photograph Interpretation
1. **Aerial photograph interpretation:** the same spatial concepts as maps (location, scale,
   direction, sketch maps, pattern recognition, absolute and relative location), applied to
   vertical and oblique photographs; comparing photographs with maps.
   SimpleStudy: Aerial Photographs.

### geo-weather-climate — Weather Maps, Satellite Imagery and GIS
1. **Weather maps and weather data:** daily weather maps, their information and symbols; media
   weather reports; interpreting synoptic weather maps.
   SimpleStudy: Weather Maps.
2. **Satellite imagery:** examining large areas of the physical and cultural landscape; using
   it alongside the core and elective units.
   SimpleStudy: Satellite Imagery.
3. **Geographical information systems (GIS):** GIS as a tool combining data sources. The
   syllabus requires a study of **one of:**
   - aerial photographs, census material and maps in the study of urban sprawl
   - satellite images and statistics in the study of changing agricultural land use
   - aerial photographs, maps and statistics in the study of forestry development
   - maps, aerial photographs and the Record of Monuments and Places in the study of the
     destruction of archaeological sites.
   
   Write a section for each. SimpleStudy: Geographic Information Systems.

### geo-graph-skills — Figure Interpretation and Census Data
1. **Figure interpretation:** analysing and evaluating information in figures, graphs and
   tables; figure drawing; statistical analysis.
   SimpleStudy: Graphs and Charts.
2. **Census of population data:** recent Irish census returns; the demographic structure of a
   population; population trends in the local area.

---

## Core Unit 2 — Regional Geography (Section 2)

All students. Study five regions: two contrasting Irish regions, two contrasting European
regions, and one continental or subcontinental region outside Europe. The syllabus wants these
regions reused as settings for Unit 1, the chosen elective and the chosen Option.

### geo-region-concept — The Concept of a Region [2.1]
1. **Physical regions:**
   - Climatic regions, in particular the cool temperate oceanic. Settings: Irish climate; North
     West Europe.
   - Geomorphological regions, including karst landscapes (the Burren), Munster ridge and valley
     (South Munster) and the Northern European Plain.
2. **Administrative regions at different scales.**
   Settings: local councils/corporations, constituency boundaries, county divisions; French
   départements.
3. **Cultural regions:**
   - Regions associated with language. Settings: Irish examples; Belgium.
   - Regions associated with religion. Settings: Irish examples; the Islamic world, European
     examples.
4. **Socio-economic regions:** less-developed regions, core regions, peripheral regions,
   regions of industrial decline. Link the examples to the Irish and European regions in [2.2].
5. **Nodal/city/urban regions:** urban areas and their hinterlands. Settings: Irish cities;
   European cities.

SimpleStudy: The Concept of a Region.

### geo-region-ireland — Two Contrasting Irish Regions [2.2]
1. **A Core Irish Region** (e.g. the Greater Dublin Area).
2. **A Peripheral Irish Region** (e.g. the West of Ireland / Western Region).

Each region covers:
- Physical processes: climate, soils, relief, drainage.
- Economic processes: primary activities (agriculture, forestry, fishing, mining/energy);
  secondary activities (patterns in manufacturing); tertiary activities (tourism and transport).
- Human processes: language, religion, urban and rural development, population dynamics.

SimpleStudy: A Core Irish Region; A Peripheral Irish Region.

### geo-region-european — Two Contrasting European Regions and the Complexity of Regions [2.2–2.4]
1. **A Core European Region: the Paris Basin.** Same headings as the Irish regions: physical
   processes; primary, secondary and tertiary activities; human processes (including urban
   development).
   SimpleStudy: The Paris Basin; Physical Processes; Primary, Secondary and Tertiary Economic
   Activities; Human Processes; Urban Development.
2. **A Peripheral European Region: the Mezzogiorno.** Same headings.
   SimpleStudy: The Mezzogiorno; Physical Processes; Primary, Secondary and Tertiary Economic
   Activities; Human Processes.

   The syllabus lets students choose regions from Scandinavia, western/central Europe (including
   the UK) and/or the Mediterranean. The Paris Basin and the Mezzogiorno are the standard
   pairing and match SimpleStudy.
3. **The complexity of regions (i)** [2.3]: the interaction of economic, cultural and physical
   processes.
   - The interaction of economic, political and cultural activities. Settings: the Republic of
     Ireland and Northern Ireland; European examples.
   - The interaction of different cultural groups and political regions.
   - The future of Europe and the European Union, with particular reference to political
     union, economic union and sovereignty.
   - SimpleStudy: the first two topics above have SimpleStudy topics of the same name; the
     third matches The Future of Europe and the European Union.
4. **The complexity of regions (ii)** [2.4]: the boundaries and extent of regions change over
   time.
   - Changes in the boundaries and extent of language regions. Settings: Gaeltacht areas from
     1850.
   - Urban growth and the expansion of city regions. Settings: Dublin council structures.
   - European Union development and expansion. Settings: post-war development, eastern
     European expansion.
   - Changes in political boundaries and their impact on cultural groups.
   - SimpleStudy: Changes in the Boundaries and Extent of Language Regions; Urban Growth and the
     Expansion of City Regions; Development and Expansion of the European Union; The Impact of
     EU Enlargement on Ireland; Changes in Political Boundaries and Their Impact on Cultural
     Groups.

### geo-region-continental — A Continental/Subcontinental Region [2.2]
1. **India** (a non-European region; SimpleStudy's choice). Covers:
   - Physical processes: climate, soil, relief, drainage.
   - Economic processes: primary, secondary and tertiary activities.
   - Human processes: language, religion, urban and rural development, population dynamics.
   
   SimpleStudy: India; Physical Processes; Primary, Secondary and Tertiary Economic Activities;
   Human Processes.

---

## Elective Unit 4 — Patterns and Processes in Economic Activities (Section 3, Q7–9)

Students take this elective **or** Elective Unit 5, not both.

### geo-economic-development — Economic Development [4.1, 4.2]
1. **Measuring economic development** [4.1]: gross national product (GNP) as a measure of
   economic development; the human development index (HDI) as a broad measure of development.
   - Settings: Ireland; European and global examples.
   - SimpleStudy: GNP; GDP (not named in the syllabus; useful context); HDI.
2. **Spatial variations in development** [4.2]: levels of development vary in space and over
   time, through the interaction of physical, social, cultural and political factors.
   SimpleStudy: The Distribution of Economic Wealth.
3. **Case study of a developing economy** [4.2]: the impact of colonialism, and adjustments to
   a global economy.
   SimpleStudy: Economic Development in India: Case Study; Colonialism: A Development Issue.
4. **Global issues and a justice perspective** [4.2] on these patterns.

### geo-economic-activities — A Developed Economy and the Location of Activities [4.2, 4.3]
1. **Case study of a developed economy** [4.2]: Ireland, including regions dominated by service
   and footloose industries, financial services and/or mass-tourism regions, and evidence of
   industrial decline.
   - Settings: Ireland; European and global examples.
   - SimpleStudy: Economic Development in Ireland: Case Study.
2. **The mobility of modern economic activities and factors in their location** [4.3]: why
   activities locate where they do; how corporate strategies open and close branch plants; how
   the product life cycle changes location.
   - SimpleStudy: The Location of Economic Activities: Factors Influencing the Development of
     an Industry or Activity; Factors Influencing the Development of Tourism in an Area.
   - SimpleStudy's tourism topic fits under the developed economy's mass-tourism regions in
     [4.2].

### geo-economic-globalisation — The Global Economy [4.3]
1. **One multinational company (MNC):** its structure and organisation. For one product: the
   sourcing of raw materials and components, the location of basic processing units, and the
   location of markets. Settings: an Irish-based MNC.
2. **The MNC and change:** the mobility of modern economic activities; corporate strategies and
   branch-plant openings and closures; product life cycle and changes in location; the future of
   economic activities (teleservices, information technology, e-commerce).
3. **Patterns in world trade:** economies linked in a global framework; the trading triad of
   the USA, Europe and the Pacific Rim; the international division of labour.
4. **How the global economy is organised:** how basic processing units are widely spread; how
   core and peripheral regions have developed; why some regions are excluded from world
   manufacturing; how globalisation has affected world trade.

SimpleStudy: The Global Economy.

### geo-economic-eu — Ireland and the European Union [4.4]
1. **EU trading patterns:** trade within the single market, and external EU trade.
2. **Irish trading patterns with the EU.**
3. **How the EU influences the Irish economy:**
   - the Common Agricultural Policy
   - the Common Fisheries Policy
   - regional development funds
   - social funding.

SimpleStudy: Ireland and the European Union.

### geo-economic-environment — Environmental Impact [4.5]
1. **Renewable and non-renewable resources in the economy.**
   Settings: national energy resources; European energy production and consumption.
2. **Burning fossil fuels and using alternative energy sources.**
   Settings: smoke-free zones; patterns of production and consumption; acid rain as a European
   issue.
3. **Environmental pollution** at local/national and global scales. Settings: global warming.
4. **Sustainable economic development** to control environmental impact: past experiences,
   future prospects, and why environmental impact studies are needed.
   Settings: the role of the EPA; depletion of fish stocks; mining sites.
5. **Conflicts between economic interests and environmental interests,** local and global. The
   syllabus requires at least two examples; write at least two.
   Settings: Irish fish stocks, tourism, heritage; global examples.

SimpleStudy: Environmental Impact.

---

## Elective Unit 5 — Patterns and Processes in the Human Environment (Section 3, Q10–12)

Students take this elective **or** Elective Unit 4, not both.

### geo-population-migration — The Dynamics of Population [5.1–5.3]
1. **Changing population characteristics** [5.1]: changes in population distribution,
   population density, growth patterns, and population structure (changing fertility and
   mortality rates).
   - Settings: census material showing change in Ireland; European and global examples.
   - SimpleStudy: The Dynamics of Population.
2. **Overpopulation** [5.2]: causes and effects, with particular attention to the development
   of resources, the influence of society and culture, the impact of income levels, and the
   impact of technology on population growth. Also the impact of growth rates on development.
   SimpleStudy: Overpopulation.
3. **Changing migration patterns in Ireland** [5.3]. Settings: the 20th-century Irish census;
   migration to and from Ireland since 1950.
4. **Migration policy in Ireland and the EU** [5.3].
5. **Ethnic, racial and religious issues arising from migration** [5.3]. Settings: government
   policy.
6. **Rural-to-urban migration in developed and developing regions** [5.3]: contrasting impacts
   on donor and receiver regions. Settings: growth in Irish cities.

SimpleStudy (items 3–6): Migration.

### geo-urban — The Dynamics of Settlement [5.4–5.6]
1. **Pre-historic and historic settlement** [5.4]: locational characteristics; the historic
   development of Irish towns.
2. **Rural settlement** [5.4]: rural settlement patterns; dispersed and clustered settlement;
   ribbon development; planning strategies in rural areas.
   Settings: county and national development plans.
3. **Urban settlement: site, hierarchy, hinterland and central place theory** [5.4]; how the
   functions and services of urban centres change over time.
   - Settings: appropriate Irish towns and cities.
   - SimpleStudy (items 1–3): The Dynamics of Settlement.
4. **Urban land use and planning** [5.5]: land-use zones in the modern city; changes in land
   use and planning issues (industrial, residential and commercial land use moving); land values
   and social stratification within cities; the expansion of cities and pressure on rural land
   use.
   - Settings: an Irish city; appropriate world cities.
   - SimpleStudy: Urban Land Use and Planning.
5. **Urban problems in developed-world cities** [5.6]: traffic movement and congestion; urban
   decay, urban sprawl and the absence of community; heritage issues; environmental quality.
   Settings: Irish towns and cities; case studies from developed-world cities.
6. **Urban planning and renewal** [5.6]: how effective urban planning strategies and urban
   renewal are at solving urban problems. Settings: strategic urban plans.
7. **Developing-world cities** [5.6]: their expansion and problems, using case studies.
8. **The future of urbanism** [5.6]: issues for the cities of the future.

SimpleStudy (items 5–8): Urban Problems.

---

## Optional Units — Higher Level only; students take one (Section 4)

### geo-option-global-interdependence — Global Interdependence [Unit 6]
1. **Views of development and underdevelopment** [6.1]: challenging all views of development;
   contrasting models and approaches, including determinist and modernisation approaches;
   images and language associated with developing societies; a critical examination of "first
   world/third world" and north/south; Eurocentric thinking.
   SimpleStudy: Models of Development.
2. **An interdependent global economy** [6.2]:
   - A case study of one MNC: the impact of global trading patterns on producer and consumer
     regions. Settings: Irish trade, MNCs in Ireland.
   - Global environmental issues: deforestation, desertification, global warming. Settings:
     managed forests in Scandinavia.
   - The impact of social and political decisions: economic and political refugees, migration
     patterns, human rights issues.
   - SimpleStudy: An Interdependent Global Economy.
3. **Empowering people: linking economic growth with human development** [6.3]: the weight of
   national debt and the cycle of poverty; the "aid" debate (who benefits?); the role of NGOs;
   land-ownership patterns and their impact on development; decision-making and levels of
   participation; levels of exploitation at local and global scales; differing gender roles in
   society.
   - Settings: Irish aid programmes, Irish NGOs, 19th-century Ireland, co-operatives, local
     enterprise boards; EU aid programmes.
   - SimpleStudy: Empowering Economic and Human Development.
4. **Sustainable development as a model for the future** [6.4]: sustainable use of resources;
   fair trade and its potential impact; justice issues, especially for minority groups;
   self-reliance and development as self-help.
   SimpleStudy: Sustainable Development.

### geo-option-geoecology — Geoecology [Unit 7]
1. **Soil composition and characteristics** [7.1]: mineral matter, organic matter, water and
   air; texture, colour, structure, water content, organic content, water retention.
   SimpleStudy: The Development of Soil.
2. **Soil processes and the global pattern of soils** [7.2]: the global pattern of soils;
   weathering, soil erosion, leaching, humification, podzolisation, laterisation,
   calcification.
   - Settings: a soil profile of one Irish soil type; one soil type from a continental or
     subcontinental region.
   - SimpleStudy: The Development of Soil.
3. **Human interference with soils** [7.2]: overcropping and overgrazing; desertification and
   conservation. Settings: the Burren; the Sahel, Iceland.
4. **One major biome in detail** [7.3]: its climate and soil characteristics, and the related
   patterns of plant and animal distribution and adaptation. The syllabus requires one biome;
   write both SimpleStudy options.
   SimpleStudy: Hot Desert Biome; Tropical Rainforest Biome.
5. **Human alteration of biomes** [7.4]: the impact of early settlement and forest clearance;
   the felling of tropical rainforests; intensive agriculture; industrial development.

### geo-option-culture-identity — Culture and Identity [Unit 8]
1. **Racial groupings** [8.1]: characteristics and locational patterns; multi-racial
   societies; racial mixing; racial conflict; the impact of colonialism and migration on racial
   patterns.
   - Settings: asylum seekers and refugees.
   - SimpleStudy: Physical Indicators of Identity.
2. **Language as a cultural indicator** [8.1]: major language groups; European languages and
   the influence of mass media; minority languages and policies for their survival.
   - Settings: Irish-language Gaeltacht areas; Welsh.
   - SimpleStudy: Cultural Indicators of Identity.
3. **Religion as a cultural indicator** [8.1]: the distribution of major world religions;
   church–state relationships; religious conflict.
   - Settings: the Irish constitution; Northern Ireland.
   - SimpleStudy: Cultural Indicators of Identity.
4. **Everyday expressions of culture and identity** [8.1]: sports, traditions, costume, food,
   music, art and festivals. Settings: Irish and European examples.
5. **Nationality and the nation state** [8.2]: physical and political boundaries; cultural
   groups within nation states; cultural groups without nationality; conflicts between
   political structures and cultural groups.
   - Settings: the island of Ireland and partition; Northern Ireland.
   - SimpleStudy: Nationality and the Nation State.
6. **A European regional case study of identity** [8.3]: historical developments (physical
   and political boundaries); ethnicity and race; religion; music, art and festivals; the role
   of migration; new boundaries. The syllabus suggests Celtic regions, the Balkans or
   Switzerland.
   SimpleStudy: Case Study: Identity in Switzerland.

### geo-option-atmosphere-ocean — The Atmosphere–Ocean Environment [Unit 9]
1. **The atmosphere and oceans as linked systems** [9.1]: the composition and structure of the
   atmosphere and oceans; measuring pressure, temperature, wind and humidity, including weather
   instrument readings.
   SimpleStudy: The Atmosphere and Ocean Environments.
2. **Solar energy and its redistribution** [9.2]: energy flows in the atmosphere–ocean
   environment; the earth's heat budget and the geographical distribution of temperature.
   SimpleStudy: Solar Energy and Global Temperatures.
3. **Exchanges of water between oceans and atmosphere** [9.3]: the hydrological cycle;
   humidity, evaporation and condensation; cloud formation and classification; precipitation
   and its distribution.
   SimpleStudy: Moisture in the Atmosphere.
4. **Atmospheric and oceanic circulation** [9.4]: the forces governing the movement of air
   and water (e.g. the Coriolis force); the general circulation of atmosphere and ocean (e.g.
   the North Atlantic); mid-latitude depressions and anticyclones; land and sea breezes;
   mountain and valley winds; thunderstorms.
   SimpleStudy: Oceans, Atmosphere, Weather and Climate.
5. **Climatic environments and climate change** [9.5]: one distinctive global climate (the
   syllabus suggests equatorial, monsoon, mid-latitude west coast, Mediterranean or
   continental); examples of climate change (e.g. the Ice Ages, 20th-century global warming,
   El Niño).
   SimpleStudy: Climatic Environments.
6. **Climate and economic development** [9.6]: the influence of rainfall on agriculture and
   domestic water supply; the impact of drought and desertification; the impact of climate on
   tourism.
   - Settings: Irish agriculture; global examples.
   - SimpleStudy: Climate Characteristics and Economic Development.

---

## Appendix A — Where the syllabus differs from the earlier draft and from SimpleStudy

- **No Higher Level-only topics in the core or electives.** The earlier draft tagged human
  interaction, rejuvenation and the complexity of regions as Higher Level only. The syllabus
  doesn't; all students study them. Only the Options are Higher Level only.
- **In the syllabus but missing from SimpleStudy:** erosion by wind [1.2]; human interaction
  with the rock cycle [1.2]; doming and sedimentary structures [1.3]; fluvial adjustment to
  base level, cyclic landscapes and peneplains [1.6]; human interaction with surface processes
  [1.7]; latitude and longitude, statistical mapping, census data and the GIS studies [skills];
  the justice perspective [4.2]; product life cycle, world trade patterns and the division of
  labour [4.3]; social funding and EU trade patterns [4.4]; migration policy and ethnic, racial
  and religious issues [5.3]; heritage, environmental quality and the future of urbanism [5.6];
  images of development and Eurocentric thinking [6.1]; refugees, human rights, debt, land
  ownership and gender roles [6.2–6.3]; human alteration of biomes [7.4]; racial groupings and
  everyday expressions of culture [8.1]; local winds and thunderstorms [9.4]; drought,
  desertification and tourism [9.6].
- **In SimpleStudy but not named in the syllabus:** GDP [4.1] (keep it as context next to GNP);
  "Location of Economic Activities" as a separate unit (folded into [4.2]/[4.3]); "Impact of EU
  Enlargement on Ireland" (folded into EU expansion in [2.4]). SimpleStudy covers two biomes,
  but the syllabus requires only one.

## Appendix B — SimpleStudy structure as recorded (2026-10-15)

For reference only. Names are exactly as SimpleStudy shows them, including their spelling
"Activites". Items in brackets are third-level topics shown where the recording opened them.

1. Plate Tectonics — The Earth's Structure; Continental Drift; Sea-Floor Spreading; The Pacific
   Ring of Fire; Plate Boundaries; The Theory of Plate Tectonics
2. Earthquakes and Volcanoes — Folding and Faulting Activity; Earthquake Activity; Volcanic
   Activity
3. Rocks, Weathering, and Mass Movement — Rocks; Weathering Processes and Landforms; Mass
   Movement
4. Rivers — River Action
5. Coasts and the Sea — Coasts and the Sea
6. Glaciation — Glaciation and Glacial Processes
7. Isostasy — Isostasy
8. The Concept of a Region — The Concept of a Region
9. Regions - Ireland — A Core Irish Region; A Peripheral Irish Region
10. Regions - European — A Core European Region [The Paris Basin + 6 topics]; A Peripheral
    European Region [The Mezzogiorno + 5 topics]
11. Regions - Continental or Subcontinental — [India + 5 topics]
12. Complexities of Regions — The Complexity of Regions [8 topics]
13. Mapwork — Ordnance Survey Maps [6 topics]
14. Aerial Photographs — Aerial Photographs
15. Weather Maps, Graphs, Charts, Satellite Imagery, and GIS — [4 topics]
16. Economic - Economic Development — Measuring Economic Development [GNP; GDP; HDI]; The
    Distribution of Economic Wealth [Ireland case study; India case study; Colonialism]
17. Economic - Location of Activites — The Location of Economic Activities [2 topics]
18. Economic - Environmental Impact — Environmental Impact
19. Economic - European Union — Ireland and the European Union
20. Economic - Multinationals and Globalisation — The Global Economy
21. Human - Population and Migration — The Dynamics of Population; Overpopulation; Migration
22. Human - Urban Geography — The Dynamics of Settlement; Urban Land Use and Planning; Urban
    Problems
23. Option - Atmosphere and Ocean — 6 topics
24. Option - Culture and Identity — 4 topics
25. Option - Geoecology — 3 topics
26. Option - Global Interdependence — 4 topics
27. Assessment — Written Exam; Geographical Investigation
