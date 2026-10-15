# Leaving Cert Geography (Higher Level) — course outline for the content overhaul

## Read this first (instructions for the content model)

- **The syllabus:** the Leaving Certificate Geography syllabus first examined in 2006 and
  examined up to June 2027. This is **not** the 2026 specification (first exam 2028). Do not
  use `relevant-resources/syllabi/geography-2026-spec.pdf`; it is the new course.
- **The chapters** are the 25 chapter IDs already in the app (`data.js`) and the pipeline
  scaffold (`pipeline/scaffold/geography.json`). Past exam questions are tagged to these IDs,
  so keep every ID exactly as written.
- **The subsections** follow SimpleStudy's Higher Level Geography course, transcribed from a
  screen recording on 2026-10-15. Topic names in quotes are SimpleStudy's own. Use them for
  structure and depth only; write all prose in your own words.
- **"Cover"** lists the content each subsection must include, to Leaving Cert Higher Level
  standard. Items marked **[HL]** are Higher Level only.
- **Paper structure:** one paper per level, 80% of the grade. The Geographical Investigation
  report is the other 20%.
  - Part One: 12 short questions; answer 10.
  - Section 1: Physical (Core Unit 1).
  - Section 2: Regional (Core Unit 2).
  - Section 3: Electives. Students answer **one** elective: Economic (Q7–9) **or** Human
    (Q10–12).
  - Section 4: Options, **Higher Level only**. Students answer **one** option.
  - Ordinary Level has no Section 4.
- Every chapter needs named Irish and international examples and case studies. Higher Level
  answers are marked on detailed "significant relevant points" (SRPs), so notes should be
  dense with specific facts.

---

## Core Unit 1 — Patterns and Processes in the Physical Environment (Section 1)

### geo-plate-tectonics — Plate Tectonics
1. **The Earth's Structure:** crust (oceanic vs continental), mantle, outer and inner core;
   lithosphere vs asthenosphere.
2. **Continental Drift:** Wegener; Pangaea; evidence from fossils, matching rocks and
   mountains, the jigsaw fit, and past climates.
3. **Sea-Floor Spreading:** Hess; the Mid-Atlantic Ridge; palaeomagnetism and magnetic
   striping; the age of oceanic crust.
4. **Plate Boundaries:** constructive (divergent), destructive (convergent: oceanic–continental,
   oceanic–oceanic, continental–continental) and passive (conservative/transform), with an
   example of each. Covers subduction, ocean trenches, island arcs and rift valleys.
5. **The Pacific Ring of Fire:** the global distribution of volcanoes and earthquakes along
   plate boundaries.
6. **The Theory of Plate Tectonics:** driving forces (convection currents, slab pull, ridge
   push); how the evidence came together into one theory.

### geo-volcanoes-earthquakes — Earthquakes and Volcanoes
1. **Folding and Faulting Activity:** fold mountains (Alps, Himalayas, Andes; Ireland's
   Caledonian and Armorican/Hercynian folding, e.g. the MacGillycuddy's Reeks); fold types
   (simple, overfold, overthrust, nappe); faults (normal, reverse, tear); rift valleys and
   block mountains.
2. **Earthquake Activity:** causes (plate movement, the build-up and release of stress); focus
   and epicentre; P, S and L waves; measurement (seismograph, Richter scale, moment magnitude,
   Mercalli scale); effects (tsunamis, liquefaction, landslides); prediction and preparation;
   case studies (e.g. Japan 2011, Haiti 2010, Turkey–Syria 2023).
3. **Volcanic Activity:** volcanic activity at plate boundaries and hotspots (Hawaii, Iceland);
   lava types and eruption styles; extrusive landforms (volcanic cones, lava plateaus,
   calderas, geysers); intrusive landforms (batholiths, dykes, sills, laccoliths); positive and
   negative impacts; prediction; Irish examples (Giant's Causeway, Antrim Plateau).
4. **[HL] Human interaction with tectonic processes:** prediction and planning for volcanoes
   and earthquakes; benefits such as geothermal energy (Iceland), fertile soils and tourism.

### geo-rocks-weathering — Rocks, Weathering and Mass Movement
1. **Rocks:** igneous (granite, basalt), sedimentary (limestone, sandstone, shale) and
   metamorphic (marble, quartzite, slate). For each: formation, characteristics and an Irish
   location. Includes the rock cycle.
2. **[HL] Human interaction with the rock cycle:** quarrying and mining (e.g. Tara Mines,
   limestone quarries); oil and gas extraction (Corrib); geothermal energy; impacts and
   management.
3. **Weathering Processes and Landforms:** mechanical weathering (freeze-thaw, exfoliation);
   chemical weathering (carbonation, oxidation, hydrolysis). **Karst** landscape (the Burren):
   limestone pavement, clints and grikes, swallow holes, dolines, caverns, stalactites,
   stalagmites and pillars; human activity in karst regions.
4. **Mass Movement:** factors (gradient, water, vegetation, human activity); types: soil creep,
   solifluction, landslides, rockfalls, mudflows, bogbursts, lahars; examples (e.g. Pollatomish
   2003, Derrybrien 2003).
5. **[HL] Human interaction with mass movement:** overgrazing, deforestation, road building,
   wind-farm construction; prevention measures.

### geo-glaciation — Glaciation and Isostasy
1. **Glaciation and Glacial Processes:** ice ages and Ireland's glaciations; glacial erosion
   (plucking, abrasion). Erosional landforms: cirque/corrie, arête, pyramidal peak, U-shaped
   valley, hanging valley, ribbon lake, fjord. Depositional landforms: boulder clay,
   drumlins, moraines, erratics. Fluvioglacial landforms: eskers, outwash plains, kames.
   Irish examples throughout (e.g. Glendalough, Coumshingaun, Clew Bay, Esker Riada).
2. **Isostasy:** isostatic uplift after the ice melted; raised beaches; drowned features (rias,
   fjords, drowned drumlins); **[HL]** landforms resulting from the interaction of processes
   over time.
3. **[HL] Rejuvenation and the cycle of erosion:** base level change; knick points, incised
   meanders, paired terraces; Davis's cycle of erosion (youth, maturity, old age).

### geo-rivers — Rivers
1. **River Action:** river processes: erosion (hydraulic action, abrasion, attrition,
   solution), transport and deposition. Long profile. Landforms: V-shaped valley, interlocking
   spurs, waterfall, gorge, meanders, oxbow lake, floodplain, levees, delta. Irish examples
   (e.g. the River Shannon, Torc Waterfall, Powerscourt).
2. **[HL] Human interaction with river processes:** dams and hydroelectricity (e.g.
   Ardnacrusha); canalisation; flood control and flooding (e.g. the OPW CFRAM programme, the
   Mississippi); impacts on the natural river system.

### geo-sea — Coasts and the Sea
1. **Coasts and the Sea:** wave types (constructive, destructive), refraction, fetch; erosion
   (hydraulic action, compression, abrasion, attrition, solution); longshore drift. Erosional
   landforms: cliffs, wave-cut platforms, bays and headlands, caves, arches, sea stacks,
   blowholes. Depositional landforms: beaches, sand spits, tombolos, lagoons, sand dunes. Irish
   examples (e.g. the Cliffs of Moher, Bull Island, Inch, Lady's Island Lake).
2. **[HL] Human interaction with coastal processes:** coastal defences (rock armour, groynes,
   sea walls, gabions, dune stabilisation); their effects on deposition and erosion elsewhere;
   managed retreat (e.g. Rosslare, Courtown).

---

## Core Unit 3 — Geographical Investigation and Skills (Part One short questions + 20% report)

### geo-mapwork — Mapwork (Ordnance Survey maps)
1. **Scale, Grid References, and Direction:** scale types; four- and six-figure grid
   references; compass direction.
2. **Distance and Area:** straight-line and curved distance; area calculation.
3. **Height and Slope:** contours, spot heights, triangulation pillars; gradient calculation;
   steep, gentle, concave, convex and even slopes.
4. **Sketch Maps and Cross-Sections:** drawing a sketch map with features to scale; drawing a
   cross-section.
5. **Drainage Patterns: Physical Landscape:** dendritic, trellised, radial and deranged
   patterns; identifying physical landforms on OS maps.
6. **Other Landscapes and Settlements:** historic settlement (pre-Christian, early Christian,
   Norman, plantation); site, situation and function of towns; nucleated, dispersed and linear
   settlement; central place theory; transport routes; planning a new road, factory or
   development on an OS map.
7. **The Geographical Investigation (20% report):** choosing a topic from the SEC list;
   objectives and hypothesis; planning; gathering data; results; conclusions; evaluation;
   presenting results.

### geo-aerial-photographs — Aerial Photographs
1. **Aerial Photographs:** vertical vs oblique (low and high) photographs; locating features
   (background, middle ground, foreground; left, centre, right); dating a photograph and
   identifying the season; sketch maps; urban and rural land use; functions; traffic
   management; planning and development decisions; comparing aerial photographs with OS maps.

### geo-weather-climate — Weather Maps and Satellite Imagery
1. **Weather Maps:** isobars, highs and lows (anticyclones and depressions), warm, cold and
   occluded fronts; weather symbols; Met Éireann synoptic charts.
2. **Satellite Imagery:** interpreting satellite images (cloud, land use, fires, floods);
   satellite vs aerial photographs; uses of remote sensing.
3. **Geographic Information Systems:** what GIS is; layers; uses in planning, emergency
   services and the environment.

### geo-graph-skills — Graphs, Charts and Data Skills
1. **Graphs and Charts:** bar charts, line graphs, pie charts, population pyramids, climate
   graphs, triangular graphs, scatter graphs. Drawing, reading and interpreting them;
   calculating percentages and change.

---

## Core Unit 2 — Regional Geography (Section 2)

### geo-region-concept — The Concept of a Region
1. **The Concept of a Region:** types of region: climatic (e.g. cool temperate oceanic,
   Mediterranean); geomorphological (the Burren, Central Lowlands); administrative (counties,
   regional assemblies, NUTS regions, the Paris region); socio-economic (core, peripheral,
   regions of industrial decline such as Wallonia or Sambre-Meuse); cultural (language
   regions, the Gaeltacht, Belgium; religion, Northern Ireland); urban regions (the Greater
   Dublin Area, the Paris city region).

### geo-region-ireland — Irish Regions
1. **A Core Irish Region:** (e.g. the Greater Dublin Area) covering physical processes
   (relief, climate, soils, drainage); primary activities (agriculture, fishing, forestry);
   secondary activities (manufacturing); tertiary activities (services, tourism, transport);
   human processes (population, language, urban development).
2. **A Peripheral Irish Region:** (e.g. the Western Region or BMW region) covering the same
   headings, contrasted with the core region.

### geo-region-european — European Regions
1. **A Core European Region: The Paris Basin**
   - Physical Processes: relief, climate, soils, drainage.
   - Primary Economic Activities: agriculture (Beauce cereals) and the CAP.
   - Secondary Economic Activities: manufacturing in Paris; industrial decentralisation.
   - Tertiary Economic Activities: tourism, transport (TGV), services.
   - Human Processes: population and migration.
   - Urban Development: the growth of Paris; new towns; planning (SDRIF, Grand Paris).
2. **A Peripheral European Region: The Mezzogiorno**
   - Physical Processes: relief, climate (Mediterranean), soils, drainage.
   - Primary Economic Activities: latifundia and minifundia; land reform; the Cassa per il
     Mezzogiorno.
   - Secondary Economic Activities: "cathedrals in the desert" (Taranto); limited success.
   - Tertiary Economic Activities: tourism, transport.
   - Human Processes: population, out-migration to the north, Naples.
3. **[HL] The Complexity of Regions** (Higher Level only)
   - The Interaction of Economic, Political, and Cultural Activities: e.g. Belgium (language
     divide and economy), the Basque Country.
   - The Interaction of Different Cultural Groups and Political Regions: e.g. Northern
     Ireland, Belgium, Catalonia.
   - Development and Expansion of the European Union: from the EEC in 1957 to today;
     enlargement rounds.
   - The Future of Europe and the European Union: further enlargement; sovereignty; Brexit.
   - The Impact of EU Enlargement on Ireland: markets, migration, funding, competition.
   - Changes in the Boundaries and Extent of Language Regions: the Gaeltacht (Irish-language
     regions) over time.
   - Urban Growth and the Expansion of City Regions: e.g. Dublin and the Greater Dublin Area,
     Paris.
   - Changes in Political Boundaries and Their Impact on Cultural Groups: e.g. Partition of
     Ireland 1921, the break-up of Yugoslavia, the USSR, Germany.

### geo-region-continental — A Continental / Subcontinental Region
1. **A Continental or Subcontinental Region: India**
   - Physical Processes: relief (Himalayas, Ganges plain, Deccan plateau); the monsoon climate;
     soils; drainage.
   - Primary Economic Activities: agriculture, the Green Revolution, irrigation.
   - Secondary Economic Activities: manufacturing; growth since liberalisation in 1991.
   - Tertiary Economic Activities: IT and services (Bangalore), outsourcing; tourism.
   - Human Processes: population growth and structure; caste; religion and language; urban
     growth (Mumbai, Kolkata) and slums.

---

## Elective Unit 4 — Patterns and Processes in Economic Activities (Section 3, Q7–9)

Students choose either this elective or Elective 5 (Human).

### geo-economic-development — Economic Development
1. **Measuring Economic Development**
   - Gross National Product (GNP)
   - Gross Domestic Product (GDP)
   - The Human Development Index (HDI): its components and its strengths and weaknesses vs
     GNP/GDP.
2. **The Distribution of Economic Wealth**
   - Economic Development in Ireland: Case Study (e.g. from the 1950s to the Celtic Tiger,
     the crash and recovery).
   - Economic Development in India: Case Study.
   - Colonialism: A Development Issue (e.g. Brazil, India, Sudan).
   - Includes: the north–south divide; core–periphery at global, European and Irish scales;
     the role of NGOs (e.g. Trócaire, Concern).

### geo-economic-activities — Location of Economic Activities
1. **The Location of Economic Activities**
   - Factors Influencing the Development of an Industry or Activity: raw materials, markets,
     transport, labour, capital, government and EU policy, technology. Covers the changing
     location of industry over time (e.g. the Irish steel industry, the EU car industry).
     Uses Irish and EU examples, e.g. a specific industry such as a named MNC in Ireland.
   - Factors Influencing the Development of Tourism in an Area: physical attractions,
     climate, cultural factors, access, infrastructure, policy (e.g. tourism in the West of
     Ireland, the Mediterranean, Spain).

### geo-economic-environment — Economic Activity and Environmental Impact
1. **Environmental Impact**
   - Renewable vs non-renewable resources: fossil fuels, peat (Bord na Móna), wind, wave and
     solar energy.
   - Pollution from economic activity: acid rain, the greenhouse effect and global warming,
     water pollution.
   - Sustainable development; environmental impact assessments.
   - [HL] Conflicts of interest between economic development and the environment (e.g. the
     Corrib gas pipeline, wind farms, Amazon deforestation).

### geo-economic-eu — Ireland and the European Union
1. **Ireland and the European Union**
   - The Common Agricultural Policy (CAP): reforms and impact on Irish farming.
   - The Common Fisheries Policy (CFP): quotas, conservation and impact on Irish fishing.
   - Regional/structural and cohesion funds: impact on Irish infrastructure.
   - Trade, markets, the euro; Ireland's changing role (net recipient to net contributor).

### geo-economic-globalisation — Multinationals and Globalisation
1. **The Global Economy**
   - Globalisation: causes (technology, transport, trade liberalisation).
   - Multinational corporations (MNCs): reasons for locating in Ireland; a case study (e.g.
     Intel, Apple, Google).
   - The changing global economy: the rise of China, India and Brazil (BRICS); the global
     division of labour; outsourcing; world trade (WTO).

---

## Elective Unit 5 — Patterns and Processes in the Human Environment (Section 3, Q10–12)

Students choose either this elective or Elective 4 (Economic).

### geo-population-migration — Population and Migration
1. **The Dynamics of Population:** population distribution and density (Ireland, Europe,
   world); the demographic transition model (stages 1–5); population structure and pyramids
   (Ireland, Brazil or India); factors affecting fertility and mortality; the changing status
   of women; Ireland's population over time (the Famine).
2. **Overpopulation:** causes; the relationship between population and resources; the impact
   of income levels; case studies (e.g. the Sahel, Kolkata/India, Brazil's North-East);
   solutions.
3. **Migration:** types and push–pull factors; Irish emigration and immigration over time;
   rural–urban migration in developing countries (e.g. Brazil, India); impacts on donor and
   receiving areas; EU migration policy; refugees; multicultural issues and racial/ethnic
   issues.

### geo-urban — Urban Geography
1. **The Dynamics of Settlement:** the site, situation and function of settlements; settlement
   hierarchy and central place theory (Christaller); changing functions over time; the
   historical development of Irish towns; rural settlement patterns and planning (one-off
   housing).
2. **Urban Land Use and Planning:** land-use zones (CBD, residential, industrial);
   urban models (Burgess concentric zone, Hoyt sector); land values; Dublin as a case study;
   urban planning and new towns (e.g. Tallaght, Adamstown); expansion of city boundaries.
3. **Urban Problems:** traffic congestion, urban sprawl, urban decline and regeneration (e.g.
   Ballymun, Dublin Docklands), the inner city; urban problems in developing world cities
   (e.g. Kolkata, São Paulo slums); urban growth and sustainability.

---

## Options — Higher Level only, choose one (Section 4)

### geo-option-atmosphere-ocean — The Atmosphere-Ocean Environment
1. **The Atmosphere and Ocean Environments:** the composition and structure of the atmosphere.
2. **Solar Energy and Global Temperatures:** insolation; its uneven distribution
   (latitude, the atmosphere, land/sea); the heat budget; atmospheric circulation (Hadley,
   Ferrel and polar cells); pressure belts and winds; the Coriolis effect.
3. **Moisture in the Atmosphere:** the hydrological cycle; humidity; condensation; types of
   rainfall (relief, convectional, cyclonic); cloud types.
4. **Oceans, Atmosphere, Weather and Climate:** ocean currents (the Gulf Stream/North
   Atlantic Drift); El Niño; air masses; depressions and anticyclones; Irish weather.
5. **Climatic Environments:** world climate types; Ireland's climate (cool temperate
   oceanic); one other climate (e.g. hot desert, Mediterranean).
6. **Climate Characteristics and Economic Development:** how climate affects economic activity
   (e.g. tourism, agriculture); climate change (causes, evidence, impacts, responses).

### geo-option-culture-identity — Culture and Identity
1. **Physical Indicators of Identity:** racial groups; issues of racism; mixing of races (e.g.
   Brazil, the USA).
2. **Cultural Indicators of Identity:** language (the Gaeltacht, Irish-language decline and
   revival); religion (e.g. Islam, the Indian subcontinent and its partition); culture and
   identity in Ireland.
3. **Nationality and the Nation State:** nation vs state; nationalism; cultural conflict (e.g.
   the Basque Country, Northern Ireland, the former Yugoslavia).
4. **Case Study: Identity in Switzerland:** languages, religion and federal structure.

### geo-option-geoecology — Geoecology
1. **The Development of Soil:** soil composition; soil-forming factors (parent material,
   climate, organisms, topography, time); soil processes (humification, leaching,
   podzolisation, laterisation, salinisation, calcification); soil characteristics; soil
   classification (brown earth, podzol, gley, latosol); human interference with soils (e.g.
   the Sahel, desertification).
2. **Hot Desert Biome:** climate, soils, flora and fauna adaptations; human activity and its
   impact (e.g. desertification in the Sahel).
3. **Tropical Rainforest Biome:** climate, soils (latosols), flora and fauna; human activity
   and its impact (e.g. deforestation in the Amazon).

### geo-option-global-interdependence — Global Interdependence
1. **Models of Development:** Rostow's model; the Core–Periphery (Wallerstein) model;
   dependency theory; sustainable development models.
2. **An Interdependent Global Economy:** world trade; debt; aid (types and impacts);
   multinationals; fair trade; the impact of colonialism.
3. **Empowering Economic and Human Development:** local self-help; NGOs; micro-finance (e.g.
   Grameen Bank); women's empowerment; Irish Aid and development education.
4. **Sustainable Development:** definition and principles; examples of sustainable and
   unsustainable development (e.g. deforestation, fishing, renewable energy).

---

## Appendix — SimpleStudy structure as recorded (2026-10-15)

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
10. Regions - European — A Core European Region [The Paris Basin; Physical Processes; Primary,
    Secondary, Tertiary Economic Activities; Human Processes; Urban Development]; A Peripheral
    European Region [The Mezzogiorno; Physical Processes; Primary, Secondary, Tertiary Economic
    Activities; Human Processes]
11. Regions - Continental or Subcontinental — A Continental or Subcontinental Region [India;
    Physical Processes; Primary, Secondary, Tertiary Economic Activities; Human Processes]
12. Complexities of Regions — The Complexity of Regions [8 topics, listed under
    geo-region-european]
13. Mapwork — Ordnance Survey Maps [6 topics, listed under geo-mapwork]
14. Aerial Photographs — Aerial Photographs
15. Weather Maps, Graphs, Charts, Satellite Imagery, and GIS — [Weather Maps; Graphs and Charts;
    Satellite Imagery; Geographic Information Systems]
16. Economic - Economic Development — Measuring Economic Development [GNP; GDP; HDI]; The
    Distribution of Economic Wealth [Ireland case study; India case study; Colonialism]
17. Economic - Location of Activites — The Location of Economic Activities [Industry or
    Activity; Tourism in an Area]
18. Economic - Environmental Impact — Environmental Impact
19. Economic - European Union — Ireland and the European Union
20. Economic - Multinationals and Globalisation — The Global Economy
21. Human - Population and Migration — The Dynamics of Population; Overpopulation; Migration
22. Human - Urban Geography — The Dynamics of Settlement; Urban Land Use and Planning; Urban
    Problems
23. Option - Atmosphere and Ocean — 6 topics (see geo-option-atmosphere-ocean)
24. Option - Culture and Identity — 4 topics (see geo-option-culture-identity)
25. Option - Geoecology — 3 topics (see geo-option-geoecology)
26. Option - Global Interdependence — 4 topics (see geo-option-global-interdependence)
27. Assessment — Written Exam; Geographical Investigation
