# Package: geo-weather-climate-s3 — Geographical information systems (GIS)

- **loId:** `geo-weather-climate-s3` · **chapterId:** `geo-weather-climate` · **syllabusRef:** 3 (Skills, Higher Level 7)
- **Syllabus:** Higher Level, "7. Geographical information systems (GIS). GIS, as a specialised
  investigative tool, can be used to combine data sources in the study of particular areas or
  geographical problems. Studies should involve a combination of skills in the study of one of
  the following:
  • the use of aerial photographs, census material, and maps in the study of urban sprawl
  • the use of satellite images and statistical information in the study of changing
    agricultural land use
  • the use of aerial photographs, maps, and statistical information in the study of forestry
    development
  • the use of maps, aerial photographs, and the record of monuments and places in the study of
    the destruction of archaeological sites." GIS is not in the Ordinary Level skills list; the
  general aims list "GIS and satellite imagery" as information sources.
- **Students study one of the four; the notes cover all four** (G-block first, then one block
  per study: U, A, F, R). Each study names the data sources the syllabus lists, shows how they
  are layered and analysed in a GIS, and gives the findings and issues with checked facts.
- **Prepared by:** a higher model, 2026-10-20. The writer works only from this package and
  `course-outlines/NOTES_STANDARD.md`.

## 1. Must cover (one bullet or block for every item; tick each off)

GIS: what it is and how it works (all students)
- [ ] G1 Definition: a GIS is a computer system for capturing, storing, analysing and displaying data that is linked to locations on the earth's surface (spatial or geo-referenced data). It combines data sources (maps, aerial photographs, satellite images, census and other statistics, field surveys) for one area so they can be studied together.
- [ ] G2 Layers: each data set is stored as a separate layer (e.g. roads, rivers, land use, population, protected sites) over the same base map; layers can be switched on and off and overlaid to reveal relationships.
- [ ] G3 Geo-referencing: every item is tied to a location by coordinates (latitude and longitude, or a national grid such as the Irish Transverse Mercator grid used on Irish maps), so layers from different sources line up.
- [ ] G4 Two kinds of spatial data: vector (points, lines and polygons, e.g. a monument as a point, a road as a line, a forest as a polygon) and raster (a grid of cells or pixels, e.g. a satellite image or an aerial photograph). Each feature can carry attribute data (a table of information, e.g. a house's year of building, a field's crop).
- [ ] G5 What GIS analysis does, one bullet each: overlay (combining layers to see where things coincide, e.g. new housing on former farmland); buffering (a zone of set distance around a feature, e.g. 100 m around a river or monument); querying (selecting features that meet conditions, e.g. all Small Areas whose population grew by over a set amount); change detection (comparing the same layer at different dates); network analysis (shortest or fastest route, e.g. for ambulances); thematic and statistical maps (choropleth maps of census data).
- [ ] G6 Steps in a GIS study (the structure for every option): define the problem and area; collect data layers; geo-reference them to one base map; overlay and analyse (overlay, buffer, change detection, statistics); map and present results; draw conclusions and recommend planning action.
- [ ] G7 Wider uses of GIS, one short bullet: local authority planning and zoning, flood-risk mapping, emergency services, utilities (water, electricity networks), retail and service location, environmental monitoring, census mapping.
- [ ] G8 Advantages and limitations: advantages (handles very large data sets; combines many sources; fast analysis and re-analysis; easy updating; clear map output; models "what if" scenarios); limitations (cost of software and data; needs training; results only as good as the data, which may be out of date or inaccurate; layers at different scales or dates may not match; privacy of personal data).
- [ ] G9 Irish data sources, one bullet: Tailte Éireann (which absorbed Ordnance Survey Ireland) for maps and aerial photography; the Central Statistics Office (CSO) for census data by area; satellite images (e.g. Landsat, Copernicus Sentinel); government departments and agencies for sector statistics.

Study 1: urban sprawl (aerial photographs, census material, maps)
- [ ] U1 Urban sprawl: the uncontrolled outward spread of low-density urban development (housing estates, retail parks, business parks) into the surrounding countryside, often along roads, leapfrogging into commuter towns and villages. One-sentence definition; the issue itself is in `geo-urban-s5`.
- [ ] U2 Aerial photographs: photos of the same area at different dates show farmland replaced by housing estates, new roads, roundabouts and business parks; ribbon development along approach roads. Overlaying them shows exactly where and when land changed.
- [ ] U3 Census material: population and housing counts by small area at each census show where population grew fastest, the age of housing stock, household size and commuting (travel to work, distance and mode). Mapping the change between censuses shows growth on the city edge and in commuter towns.
- [ ] U4 Maps: OS maps and historic maps of different editions show the built-up area expanding; development plan zoning maps show land zoned for housing; transport maps show new motorways and rail lines that encouraged growth.
- [ ] U5 GIS analysis: overlay the built-up area at each date to measure how much land was urbanised; overlay census growth on it; buffer motorways and rail stations to test whether growth followed transport; link commuting data to show dependence on the car.
- [ ] U6 Findings for Dublin (case study): the city and its suburbs spread into the surrounding counties; commuter towns in Meath, Kildare, Wicklow and Louth grew rapidly; many residents commute long distances to Dublin. Use only section 2 facts.
- [ ] U7 Problems of sprawl shown by the study, one bullet each: loss of farmland and green space; car dependence, long commutes and traffic congestion; services (schools, transport, shops) lagging behind new housing; high cost of extending water, sewerage and public transport to low-density areas; weakened community life in dormitory settlements.
- [ ] U8 Planning responses the study informs: compact growth and higher density near public transport (the National Planning Framework, 2018); planned new communities with services built alongside housing (e.g. Adamstown); greenbelts.

Study 2: changing agricultural land use (satellite images, statistics)
- [ ] A1 Satellite images: false-colour images from different years show changes in crops and grassland, field size, drainage and reclamation of marginal land, land lost to housing or forestry; Sentinel and Landsat images repeat regularly, so changes in a single season can be tracked.
- [ ] A2 Land-cover maps from satellites: CORINE land cover, an EU inventory mapped from satellite images for several dates, shows agricultural, forest, wetland and urban land at each date, so change can be measured.
- [ ] A3 Statistical information: the CSO Census of Agriculture and annual crop and livestock surveys give farm numbers, farm size, crop areas and livestock numbers by county; Department of Agriculture data on farm payments.
- [ ] A4 GIS analysis: overlay satellite-derived land use from two dates to map where tillage, grassland, forestry and built land changed; join county statistics to the map; relate change to soils, relief and rainfall layers (e.g. tillage concentrated on the drier, flatter, better-drained land of the east and south-east).
- [ ] A5 Findings for Ireland: most farmland is grassland for cattle and sheep; tillage is concentrated in the east and south-east; dairy farming expanded after EU milk quotas ended in 2015; some marginal land in the west has been planted with forestry; farmland on the edge of cities has been lost to urban growth. Use only section 2 facts.
- [ ] A6 Uses: checking farmers' land-use claims under the Common Agricultural Policy (CAP) by satellite; monitoring crop health and forecasting yields; environmental monitoring (drainage of wetlands, hedgerow loss, nitrate pressure on water).
- [ ] A7 International illustration, one bullet: satellite images of irrigated desert farming (centre-pivot circles) and of Amazon clearance for cattle and soya show agricultural change on a large scale. Use the checked facts in `geo-weather-climate-s2` only.

Study 3: forestry development (aerial photographs, maps, statistics)
- [ ] F1 Aerial photographs: photos of different dates show new plantations (dark, uniform blocks with straight edges and firebreaks), clear-felled areas (bare brown patches with brash), and replanting; species and age can be distinguished by tone and texture.
- [ ] F2 Maps: OS maps show forest areas by symbol (coniferous, deciduous, mixed) and can be compared across editions; soil, peat and relief maps show where planting took place (marginal upland, wet mineral soils and peat); maps of protected areas (Special Areas of Conservation, Special Protection Areas) show conflicts.
- [ ] F3 Statistical information: the Forest Service's National Forest Inventory (forest area, species, ownership, age by county), annual afforestation and felling figures, grant data.
- [ ] F4 GIS analysis: overlay forest cover at successive dates to map expansion; overlay with soils, slope and altitude to explain where planting happened; overlay protected sites, rivers and archaeological sites, with buffers, to identify conflicts; query which counties had the largest increase.
- [ ] F5 Findings for Ireland: forest cover was about 1% at the start of the 20th century and is now about 11% of the land area; most planting has been of conifers, mainly Sitka spruce (about half of all forest area), on marginal land; Coillte, the state forestry company set up in 1988, manages most public forest; private (largely farm) planting grew with grants.
- [ ] F6 Issues the study identifies, one bullet each: benefits (timber and jobs, farm income diversification, carbon storage, recreation); problems (dense conifer blocks change the landscape and reduce biodiversity; acidification and sediment in streams, harming fish and the freshwater pearl mussel; loss of open upland habitat for birds such as the hen harrier; planting on peat releases carbon; clear-felling causes erosion; local opposition where forestry replaces farms, e.g. in Co. Leitrim; disease such as ash dieback, first found in Ireland in 2012); management (more broadleaf planting, buffer zones along rivers, environmental assessment of planting, continuous-cover forestry).

Study 4: destruction of archaeological sites (maps, aerial photographs, the Record of Monuments and Places)
- [ ] R1 The Record of Monuments and Places (RMP): the statutory list of known archaeological monuments in each county, set up under the National Monuments (Amendment) Act 1994. It is published as a written list with OS maps on which each site is marked (circled). Anyone intending to carry out works at or near a recorded monument must give the Minister two months' notice. The underlying database (the Sites and Monuments Record) is viewable online in the National Monuments Service's Historic Environment Viewer.
- [ ] R2 Types of site: ringforts (the most numerous field monument in Ireland), megalithic tombs, standing stones, ecclesiastical sites, castles and tower houses, crannógs, fulachta fiadh, buried sites known only from below-ground remains.
- [ ] R3 Maps: early OS six-inch maps (first edition, 1830s–1840s) and later editions record sites (e.g. ringforts drawn as circles); comparing old maps with modern maps and the RMP shows which sites have disappeared.
- [ ] R4 Aerial photographs: reveal sites not visible on the ground: cropmarks (crops over buried ditches grow taller and greener because of extra moisture; over buried walls they are stunted and parched), parchmarks in dry summers, soil marks in ploughed fields, shadow marks (low sun shows earthworks); comparing photos from different dates shows sites levelled. LiDAR (laser scanning from aircraft) reveals earthworks under trees.
- [ ] R5 GIS analysis: overlay the RMP point layer on old and new maps and aerial photographs to record which sites survive, are damaged or are destroyed; overlay development layers (new roads, housing, quarries, forestry, land drainage) and buffer each monument to predict threats; map destruction rates by area.
- [ ] R6 Causes of destruction, one bullet each: agricultural improvement (land reclamation, drainage, ploughing, removing field boundaries); road building and infrastructure; urban and housing development; quarrying; afforestation (ploughing, drains, tree roots); natural erosion (coastal erosion of promontory forts and middens).
- [ ] R7 Case studies (checked facts only): Wood Quay, Dublin (Viking-age remains excavated and largely removed for Dublin Corporation's civic offices after protests in the late 1970s); the M3 motorway through the Tara–Skryne valley near the Hill of Tara, Co. Meath (opened 2010; a henge was found at Lismullin during construction in 2007); Carrickmines Castle on the M50 route, Co. Dublin (early 2000s); discoveries by aerial survey in the 2018 drought, including a previously unknown henge at Brú na Bóinne, Co. Meath.
- [ ] R8 Protection the study supports: the RMP and notification system; archaeological assessment and excavation before development (preservation by record vs preservation in situ); planning conditions; rerouting roads; public awareness; farm schemes that protect monuments.

## 2. Checked facts and examples (the only named places, dates and figures you may use)

| Item | Fact |
|---|---|
| G3 | Irish maps use the Irish Transverse Mercator (ITM) grid (and the older Irish Grid). |
| G9 | Tailte Éireann was set up in 2023, bringing together Ordnance Survey Ireland, the Property Registration Authority and the Valuation Office. |
| U3 | Ireland's recent censuses: 2011, 2016 and 2022 (the 2021 census was postponed to 2022 because of COVID-19). Census 2022: Ireland's population about 5.1 million; Dublin county about 1.45 million. The CSO publishes census results for Small Areas (each generally of 50–200 dwellings). |
| U6 | The Greater Dublin Area = Dublin, Meath, Kildare and Wicklow. Commuter towns include Navan, Drogheda, Naas, Newbridge and Portlaoise. Give no growth rates or commuting figures. |
| U8 | National Planning Framework (2018, part of Project Ireland 2040) promotes compact growth. Adamstown, Co. Dublin, is a planned Strategic Development Zone (SDZ) community. Give no percentages. |
| A2 | CORINE land cover is an EU land-cover inventory mapped from satellite images; Ireland has been mapped for 1990, 2000, 2006, 2012 and 2018. |
| A3, A5 | The CSO Census of Agriculture 2020 counted about 135,000 farms. Most Irish farmland is grassland. EU milk quotas ended in 2015, after which dairy farming expanded. |
| A6 | The EU's Common Agricultural Policy (CAP); satellite images are used to check farm land-use claims. Give no dates. |
| F5 | Forest cover about 1% of Ireland at the start of the 20th century; about 11% today (National Forest Inventory, 2022). Coillte set up in 1988. Sitka spruce is the most planted species, about half of all forest area. |
| F6 | Ash dieback was first found in Ireland in 2012. Co. Leitrim has seen local opposition to forestry replacing farmland (give no figures). |
| R1 | Record of Monuments and Places set up under section 12 of the National Monuments (Amendment) Act 1994; two months' notice required before works at a recorded monument. The National Monuments Service runs the online Historic Environment Viewer. |
| R2 | There are about 45,000 ringforts in Ireland, the most common field monument. |
| R3 | First edition OS six-inch maps of Ireland date from the 1830s–1840s. |
| R7 | Wood Quay, Dublin: Viking-age site; civic offices built after protests in the late 1970s. M3 motorway, Tara–Skryne valley, Co. Meath: opened 2010; Lismullin henge found 2007. Carrickmines Castle, M50 route, Co. Dublin: dispute in the early 2000s. July 2018 drought: a henge was spotted from the air (by drone) at Brú na Bóinne, Co. Meath. |
| All other items | No checked example. Do not name one. |

## 3. Traps

- **Cover all four studies**, each built on the data sources the syllabus names for it: urban
  sprawl (aerial photographs, census, maps); agricultural land use (satellite images,
  statistics); forestry (aerial photographs, maps, statistics); archaeology (maps, aerial
  photographs, RMP). Don't swap the sources between studies.
- GIS is the **combining** of layers; a single map or photo is not a GIS. Every study must show
  overlay or analysis, not just list sources.
- "RMP" = Record of Monuments and Places (not "Register"). The Act is the National Monuments
  (Amendment) Act **1994**.
- Ordnance Survey Ireland is now part of Tailte Éireann (2023); either name is acceptable, but
  don't call Tailte Éireann a census body.
- Census 2021 did not happen; the census was held in 2022.
- Don't give sprawl growth rates, commuting distances, forest planting rates, archaeological
  destruction percentages, CORINE change figures or farm-size figures: none are checked.
- Don't say the M3 "destroyed the Hill of Tara": the motorway passes through the valley near it.
- Urban sprawl as an urban problem, urban renewal and planning case studies belong to
  `geo-urban-s5` and `geo-urban-s6`; here sprawl is the subject of a GIS study, so focus on data
  and method, with problems and responses in one bullet each.
- Forestry as a primary economic activity and EU agricultural policy (CAP detail) belong to
  `geo-economic-activities` and `geo-economic-eu`; prehistoric and historic settlement belong to
  `geo-urban-s1`. Don't re-teach them.
- Reading aerial photographs (location notation, sketch maps) is in `geo-aerial-photographs-s1`;
  satellite image types and recognition are in `geo-weather-climate-s2`. Refer, don't repeat.

## 4. What exams ask (topics only)

- No short questions in the tagged past papers test GIS directly. It supports the Higher Level
  skills requirement and can be drawn on in Geographical Investigation and longer answers on
  urban sprawl, land use change and heritage.
- Expected knowledge: a definition of GIS; layers and overlay; data sources; how GIS is used in
  the chosen study, with an Irish case study; advantages and limitations.

## 5. Practice questions to write

1. 30 marks, Higher: "Examine how GIS, using aerial photographs, census material and maps, can be
   used in the study of urban sprawl." Model answer: G1–G2 briefly, then each source (U2–U4),
   the GIS analysis (U5), Dublin findings (U6, section 2 facts only), problems and responses
   (U7–U8). About 15 SRPs.
2. 30 marks, Higher: "Examine how maps, aerial photographs and the Record of Monuments and Places
   can be used in a GIS to study the destruction of archaeological sites." Model answer: RMP
   (R1), maps (R3), aerial photographs and cropmarks (R4), GIS analysis (R5), causes (R6), two
   case studies from R7, protection (R8). About 15 SRPs.
3. 8 marks: (a) define GIS; (b) explain layers and overlay; (c) distinguish vector and raster
   data; (d) one advantage and one limitation of GIS. Model answer: G1, G2, G4, G8 only.

Each model answer uses only section 2 facts; no invented statistics.
