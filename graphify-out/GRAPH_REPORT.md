# Graph Report - /Users/gabrielwhelan/barebones  (2026-05-18)

## Corpus Check
- 13 files · ~110,733 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 199 nodes · 330 edges · 18 communities (17 shown, 1 thin omitted)
- Extraction: 85% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 47 edges (avg confidence: 0.87)
- Token cost: 1,800 input · 1,200 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Approved User Accounts|Approved User Accounts]]
- [[_COMMUNITY_Core App Logic|Core App Logic]]
- [[_COMMUNITY_App Bootstrap & Config|App Bootstrap & Config]]
- [[_COMMUNITY_Plant Vascular Tissue|Plant Vascular Tissue]]
- [[_COMMUNITY_AI Answer Evaluation|AI Answer Evaluation]]
- [[_COMMUNITY_Bacterial Cell Structure|Bacterial Cell Structure]]
- [[_COMMUNITY_Digestive System|Digestive System]]
- [[_COMMUNITY_Seed Germination & pH|Seed Germination & pH]]
- [[_COMMUNITY_Photosynthesis Pigments|Photosynthesis Pigments]]
- [[_COMMUNITY_Cell Membrane Structure|Cell Membrane Structure]]
- [[_COMMUNITY_Study Tabs & Navigation|Study Tabs & Navigation]]
- [[_COMMUNITY_Mitochondrion Ultrastructure|Mitochondrion Ultrastructure]]
- [[_COMMUNITY_Bacterial Growth Phases|Bacterial Growth Phases]]
- [[_COMMUNITY_Root Zones & Structure|Root Zones & Structure]]
- [[_COMMUNITY_Course Data Access|Course Data Access]]
- [[_COMMUNITY_Notes & Persistence|Notes & Persistence]]
- [[_COMMUNITY_Outcomes & Vocabulary|Outcomes & Vocabulary]]
- [[_COMMUNITY_Course Data Store|Course Data Store]]

## God Nodes (most connected - your core abstractions)
1. `getCurrentUser()` - 16 edges
2. `Approved Usernames List` - 15 edges
3. `bare bones App (index.html)` - 13 edges
4. `renderAll()` - 11 edges
5. `renderOutcomes()` - 10 edges
6. `submitTest()` - 8 edges
7. `Bacterial Cell` - 8 edges
8. `renderTestOverview()` - 7 edges
9. `Alimentary Canal` - 7 edges
10. `Phloem` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Auth Panel` --conceptually_related_to--> `Approved Usernames List`  [INFERRED]
  index.html → approved_usernames.txt
- `Account Switcher Select` --conceptually_related_to--> `Approved Usernames List`  [INFERRED]
  index.html → approved_usernames.txt

## Hyperedges (group relationships)
- **Subject Study Flow (Graph → Workbench → Tabs)** — index_subject_graph, index_subject_workbench, index_flashcards_tab, index_test_tab, index_exam_tab [INFERRED 0.85]
- **Account Authentication Flow (Avatar → Menu → Auth Panel → Usernames)** — index_profile_avatar, index_profile_menu, index_auth_panel, approved_usernames_list [INFERRED 0.75]
- **App Script Dependencies (index.html loads data.js and app.js)** — index_app, index_data_js, index_app_js [EXTRACTED 1.00]
- **Bacterial Cell Ultrastructure Components** — bacteria_tem_bacterial_cell, bacteria_tem_cell_wall, bacteria_tem_cell_membrane, bacteria_tem_cytoplasm, bacteria_tem_nucleoid, bacteria_tem_ribosomes [INFERRED 0.85]
- **Chlorophyll Pigments Absorb Light at Blue-Violet and Red Wavelengths** — photosynthesis_spectrum_chlorophyll_a, photosynthesis_spectrum_chlorophyll_b, photosynthesis_spectrum_blue_violet_peak, photosynthesis_spectrum_red_peak, photosynthesis_spectrum_absorption [EXTRACTED 1.00]
- **Chlorophyll a and b Are Photosynthetic Pigments** — photosynthesis_spectrum_chlorophyll_a, photosynthesis_spectrum_chlorophyll_b, photosynthesis_spectrum_photosynthesis [EXTRACTED 1.00]
- **Phospholipid Bilayer Structure Components** — cell_membrane_phospholipid_bilayer, cell_membrane_hydrophilic_head, cell_membrane_hydrophobic_tail, cell_membrane_phospholipid [INFERRED 0.95]
- **Fluid Mosaic Model Membrane Components** — cell_membrane_fluid_mosaic_model, cell_membrane_phospholipid_bilayer, cell_membrane_protein_x, cell_membrane_protein_y [INFERRED 0.85]
- **Alimentary Canal Organ Sequence** — alimentary_mouth, alimentary_oesophagus, alimentary_stomach, alimentary_small_intestine, alimentary_large_intestine [EXTRACTED 1.00]
- **Accessory Digestive Organs** — alimentary_liver, alimentary_stomach, alimentary_small_intestine [INFERRED 0.85]
- **Plant Vascular System** — xylem_phloem_xylem, xylem_phloem_phloem, xylem_phloem_vascular_tissue, xylem_phloem_plant [INFERRED 0.95]
- **Phloem Structural Components** — xylem_phloem_phloem, xylem_phloem_sieve_tube, xylem_phloem_sieve_plate, xylem_phloem_companion_cell [EXTRACTED 1.00]
- **Xylem Structural Components** — xylem_phloem_xylem, xylem_phloem_xylem_vessel, xylem_phloem_spiral_thickening [EXTRACTED 1.00]
- **Mitochondrial Membrane System** — mitochondrion_outer_membrane, mitochondrion_inner_membrane, mitochondrion_cristae, mitochondrion_intermembrane_space [INFERRED 0.95]
- **Mitochondrial Internal Compartments** — mitochondrion_matrix, mitochondrion_cristae, mitochondrion_matrix_granules [INFERRED 0.85]
- **Soil pH Influence on Grass Seed Germination** — germination_graph_soil_ph, germination_graph_germination_percentage, germination_graph_grass_seeds, germination_graph_germination_process [EXTRACTED 1.00]
- **Bell-Curve pH Optimum Pattern** — germination_graph_bell_curve_trend, germination_graph_optimal_ph, germination_graph_low_ph_inhibition, germination_graph_high_ph_inhibition [EXTRACTED 1.00]
- **Bacterial Growth Phase Transition: Stationary to Decline** — bacteria_growth_stationary_phase, bacteria_growth_decline_phase, bacteria_growth_stage_z [INFERRED 0.85]
- **Chart Axes Define Population Over Time** — bacteria_growth_chart, bacteria_growth_population, bacteria_growth_time, bacteria_growth_curve [EXTRACTED 1.00]
- **Root Structural Zones X Y Z** — root_region_x, root_region_y, root_region_z [EXTRACTED 1.00]
- **Root Diagram and Worksheet Educational Context** — root_diagram, root_worksheet, root_transverse_section, root_dashed_line [INFERRED 0.85]

## Communities (18 total, 1 thin omitted)

### Community 0 - "Approved User Accounts"
Cohesion: 0.07
Nodes (34): Username: david, Username: ellie, Username: elliot, Username: gabriel, Username: harmony, Username: irial, Username: james, Username: jeffery (+26 more)

### Community 1 - "Core App Logic"
Cohesion: 0.12
Nodes (29): applyAccentColor(), buildProgressSubjectStats(), cardsForOutcome(), computeUserProgress(), escapeHtml(), formatModelAnswer(), getCurrentUser(), getEnabledSubjectIds() (+21 more)

### Community 2 - "App Bootstrap & Config"
Cohesion: 0.07
Nodes (16): APPROVED_USERNAMES, AVATAR_COLORS, bindEvents(), BIOLOGY_SUBJECT, BUSINESS_SUBJECT, els, FALLBACK_CHAPTERS, GEOGRAPHY_SUBJECT (+8 more)

### Community 3 - "Plant Vascular Tissue"
Cohesion: 0.24
Nodes (12): Assimilate/Sucrose Transport (Bidirectional), Companion Cell, Xylem and Phloem Diagram, Phloem, Plant, Sieve Plate, Sieve Tube Element, Spiral Thickening (Lignified Wall) (+4 more)

### Community 4 - "AI Answer Evaluation"
Cohesion: 0.24
Nodes (10): buildPrompt(), compactText(), evaluateAnswerDetailed(), extractKeywords(), findKeywordHits(), getKeywordStopwords(), sanitize(), shouldAskForExamples() (+2 more)

### Community 5 - "Bacterial Cell Structure"
Cohesion: 0.33
Nodes (9): Bacterial Cell, Cell Membrane, Cell Wall, Cytoplasm, TEM Image of Bacterial Cell, Label X (Annotated Region), Nucleoid Region, Ribosomes (+1 more)

### Community 6 - "Digestive System"
Cohesion: 0.42
Nodes (9): Alimentary Canal, Alimentary Canal Diagram, Large Intestine, Liver (Label B), Mouth / Oral Cavity, Oesophagus (Label A), Probiotic Bacteria, Small Intestine (+1 more)

### Community 7 - "Seed Germination & pH"
Cohesion: 0.39
Nodes (9): Bell-Curve Germination Trend, Percentage Germination of Grass Seeds, Germination Process, Grass Seeds, High pH Germination Inhibition (pH > 8), Germination Graph Image, Low pH Germination Inhibition (pH < 2), Optimal Soil pH for Germination (~6–6.5) (+1 more)

### Community 8 - "Photosynthesis Pigments"
Cohesion: 0.61
Nodes (8): Absorption of Light, Blue-Violet Absorption Peak (~430-450 nm), Chlorophyll a, Chlorophyll b, Photosynthesis Absorption Spectrum Diagram, Colour (Wavelength) of Light, Photosynthesis, Red Absorption Peak (~660-680 nm)

### Community 9 - "Cell Membrane Structure"
Cohesion: 0.43
Nodes (8): Cell Membrane Ultrastructure Diagram, Fluid Mosaic Model, Hydrophilic Head (Phosphate Group), Hydrophobic Tail (Fatty Acid Chain), Phospholipid Molecule, Phospholipid Bilayer, Labeled Component X (Peripheral/Intrinsic Protein or Glycoprotein), Labeled Component Y (Transmembrane/Intrinsic Protein)

### Community 10 - "Study Tabs & Navigation"
Cohesion: 0.33
Nodes (7): getExamDisclaimer(), getSelectedChapter(), getSelectedOutcome(), renderExamSection(), shuffleArray(), startTest(), switchTab()

### Community 11 - "Mitochondrion Ultrastructure"
Cohesion: 0.48
Nodes (7): Cristae, Inner Membrane, Intermembrane Space, Mitochondrial Matrix, Matrix Granules / Ribosomes, Mitochondrion, Outer Membrane

### Community 12 - "Bacterial Growth Phases"
Cohesion: 0.43
Nodes (7): Bacteria Growth Chart, Bacterial Growth Curve, Decline Phase (Death Phase), Population (Y-Axis Metric), Stage Z - Decline Phase, Stationary Phase, Time (X-Axis Metric)

### Community 13 - "Root Zones & Structure"
Cohesion: 0.48
Nodes (7): Dashed Line Indicator for Cross-Section Plane, Plant Root Longitudinal Section Diagram, Region X - Root Hair Zone, Region Y - Elongation Zone, Region Z - Root Cap / Meristematic Zone, Transverse Section of Root at Dashed Line, Root Biology Worksheet

### Community 14 - "Course Data Access"
Cohesion: 0.4
Nodes (5): buildSubjectChapters(), getExamQuestionsForChapter(), getExternalCourseData(), getOriginalChapter(), questionsForChapter()

### Community 15 - "Notes & Persistence"
Cohesion: 0.5
Nodes (4): buildFullNotesHtml(), markNotesViewed(), openFullNotes(), persist()

### Community 16 - "Outcomes & Vocabulary"
Cohesion: 0.67
Nodes (3): buildOutcomes(), chapterVocabulary(), t()

## Ambiguous Edges - Review These
- `Labeled Component X (Peripheral/Intrinsic Protein or Glycoprotein)` → `Labeled Component Y (Transmembrane/Intrinsic Protein)`  [AMBIGUOUS]
  images/cell-membrane.png · relation: conceptually_related_to

## Knowledge Gaps
- **41 isolated node(s):** `COURSE_DATA`, `AVATAR_COLORS`, `APPROVED_USERNAMES`, `FALLBACK_CHAPTERS`, `BUSINESS_SUBJECT` (+36 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Labeled Component X (Peripheral/Intrinsic Protein or Glycoprotein)` and `Labeled Component Y (Transmembrane/Intrinsic Protein)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Are the 2 inferred relationships involving `Approved Usernames List` (e.g. with `Auth Panel` and `Account Switcher Select`) actually correct?**
  _`Approved Usernames List` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `COURSE_DATA`, `AVATAR_COLORS`, `APPROVED_USERNAMES` to the rest of the system?**
  _41 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Approved User Accounts` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `Core App Logic` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._
- **Should `App Bootstrap & Config` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._