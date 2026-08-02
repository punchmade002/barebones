# Graph Report - barebones  (2026-06-14)

## Corpus Check
- 39 files · ~5,593,278 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 484 nodes · 699 edges · 42 communities (40 shown, 2 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 56 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d2df1c12`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

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
- [[_COMMUNITY_Mitochondrion Ultrastructure|Mitochondrion Ultrastructure]]
- [[_COMMUNITY_Bacterial Growth Phases|Bacterial Growth Phases]]
- [[_COMMUNITY_Root Zones & Structure|Root Zones & Structure]]
- [[_COMMUNITY_Course Data Access|Course Data Access]]
- [[_COMMUNITY_Notes & Persistence|Notes & Persistence]]
- [[_COMMUNITY_Outcomes & Vocabulary|Outcomes & Vocabulary]]
- [[_COMMUNITY_Course Data Store|Course Data Store]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]

## God Nodes (most connected - your core abstractions)
1. `run()` - 18 edges
2. `getCurrentUser()` - 17 edges
3. `renderAll()` - 14 edges
4. `Handoff: barebones — Landing Page` - 14 edges
5. `Approved Usernames List` - 14 edges
6. `bare bones App (index.html)` - 13 edges
7. `run_batch()` - 12 edges
8. `buildPrompt()` - 11 edges
9. `2. The pipeline — eight stages` - 11 edges
10. `Key Components` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Auth Panel` --conceptually_related_to--> `Approved Usernames List`  [INFERRED]
  index.html → approved_usernames.txt
- `Account Switcher Select` --conceptually_related_to--> `Approved Usernames List`  [INFERRED]
  index.html → approved_usernames.txt
- `buildPrompt()` --calls--> `run_batch()`  [EXTRACTED]
  app.js → pipeline/segment.py
- `buildPrompt()` --calls--> `pages_text()`  [EXTRACTED]
  app.js → pipeline/segment.py
- `_part_line()` --calls--> `recommended_words()`  [INFERRED]
  pipeline/model_answers.py → pipeline/config.py

## Communities (42 total, 2 thin omitted)

### Community 0 - "Approved User Accounts"
Cohesion: 0.06
Nodes (60): buildPrompt(), isPersonTerm(), isPluralTerm(), needsDefiniteArticle(), shouldAskForExamples(), termForSentence(), build_prompt(), _chapters() (+52 more)

### Community 1 - "Core App Logic"
Cohesion: 0.06
Nodes (23): APPROVED_USERNAMES, AVATAR_COLORS, bindEvents(), BIOLOGY_SUBJECT, buildOutcomes(), BUSINESS_SUBJECT, chapterVocabulary(), CHEMISTRY_SUBJECT (+15 more)

### Community 2 - "App Bootstrap & Config"
Cohesion: 0.09
Nodes (26): archive_url(), download(), discover_and_download(), Stage 1 — ACQUIRE via the SEC archive form.  (Playwright)  Verified against the, Set a cascade <select> and wait for the postback that reveals the next one., run(), _select(), _subject_label() (+18 more)

### Community 3 - "Plant Vascular Tissue"
Cohesion: 0.07
Nodes (32): Username: david, Username: ellie, Username: gabriel, Username: harmony, Username: irial, Username: james, Username: jeffery, Username: kevine (+24 more)

### Community 4 - "AI Answer Evaluation"
Cohesion: 0.08
Nodes (25): bare bones — Design System, Buttons, Cards, code:block1 (--r-xs:   8px), code:block2 (--s0: 0 1px 3px rgba(0,0,0,0.04)    subtle), code:block3 (--t:    180ms), Color Tokens, Exam Groups (+17 more)

### Community 5 - "Bacterial Cell Structure"
Cohesion: 0.15
Nodes (22): applyAccentColor(), buildProgressSubjectStats(), computeUserProgress(), getCurrentUser(), getEnabledSubjectIds(), getEnabledSubjects(), getLearnedByOutcome(), hasViewedNotesForChapter() (+14 more)

### Community 6 - "Digestive System"
Cohesion: 0.09
Nodes (21): 0. Sticky nav (`header.nav`), 1. Hero — pick ONE direction, 2. Method — "Two steps. That's it." (`#method`, `.band` background), 3. Features — "Less app. More marks." (`#features`), 4. Product — "Open it. Start studying." (`#product`, `.band`), 5. Sign-up CTA (`#start`)  ← all CTAs scroll here, 6. Footer (`footer.site`), About the Design Files (+13 more)

### Community 7 - "Seed Germination & pH"
Cohesion: 0.1
Nodes (19): 0. The key insight, 1. Target output (what the pipeline must produce), 2. The pipeline — eight stages, 3. Architecture decisions that matter, 4. Rollout for all 26 subjects, 5. Realistic expectations, 6. One caution, bare bones — Exam Data Pipeline (+11 more)

### Community 8 - "Photosynthesis Pigments"
Cohesion: 0.19
Nodes (15): buildFullNotesHtml(), cardsForOutcome(), getProgressByOutcome(), getSelectedChapter(), getSelectedOutcome(), markNotesViewed(), openFullNotes(), persist() (+7 more)

### Community 9 - "Cell Membrane Structure"
Cohesion: 0.15
Nodes (14): derive_flashcards(), load_to_app(), pair_marking_scheme(), Part, qa(), Question, Stages 3–8 — typed stubs with the contract each must satisfy.  These are deliber, pages[] -> Question[] with parts. Owns: where one question ends and the next beg (+6 more)

### Community 11 - "Mitochondrion Ultrastructure"
Cohesion: 0.26
Nodes (9): confetti(), hideCustomInput(), pad(), renderFill(), renderText(), start(), startCustom(), stop() (+1 more)

### Community 12 - "Bacterial Growth Phases"
Cohesion: 0.15
Nodes (12): code:block1 (run.py           ⭐ one command: input a subject -> all relev), code:bash (pip install anthropic --break-system-packages), code:bash (p2), code:block4 (_data/raw/history/2023-higher-EV-papers.pdf, …-scheme.pdf, 2), code:bash (pip install playwright --break-system-packages), code:bash (pip install pymupdf --break-system-packages), ⭐ One command per subject, pipeline/ — exam data extraction (+4 more)

### Community 14 - "Course Data Access"
Cohesion: 0.17
Nodes (11): 1. Where things live, 2. Chapter shape (canonical), 3. Runtime flattening (important caveat), 4. Adding a new subject — step by step, 5. Cross-applicability (`appliesTo`), 6. Reference example, code:block1 (data.js                  Source of truth: chapter list, lear), code:js ({) (+3 more)

### Community 15 - "Notes & Persistence"
Cohesion: 0.24
Nodes (12): Assimilate/Sucrose Transport (Bidirectional), Companion Cell, Xylem and Phloem Diagram, Phloem, Plant, Sieve Plate, Sieve Tube Element, Spiral Thickening (Lignified Wall) (+4 more)

### Community 16 - "Outcomes & Vocabulary"
Cohesion: 0.2
Nodes (10): buildSubjectChapters(), ensureMinimumConcepts(), getExamDisclaimer(), getExamQuestionsForChapter(), getExternalCourseData(), getOriginalChapter(), questionsForChapter(), renderExamSection() (+2 more)

### Community 17 - "Course Data Store"
Cohesion: 0.33
Nodes (9): Bacterial Cell, Cell Membrane, Cell Wall, Cytoplasm, TEM Image of Bacterial Cell, Label X (Annotated Region), Nucleoid Region, Ribosomes (+1 more)

### Community 18 - "Community 18"
Cohesion: 0.39
Nodes (9): Bell-Curve Germination Trend, Percentage Germination of Grass Seeds, Germination Process, Grass Seeds, High pH Germination Inhibition (pH > 8), Germination Graph Image, Low pH Germination Inhibition (pH < 2), Optimal Soil pH for Germination (~6–6.5) (+1 more)

### Community 19 - "Community 19"
Cohesion: 0.32
Nodes (8): compactText(), evaluateAnswerDetailed(), extractKeywords(), findKeywordHits(), getKeywordStopwords(), sanitize(), splitExpectedParts(), tokenize()

### Community 20 - "Community 20"
Cohesion: 0.25
Nodes (7): bare bones — Product Context, Brand Tone, Core Features, Product Purpose, Register, Strategic Principles, Users

### Community 21 - "Community 21"
Cohesion: 0.43
Nodes (8): Cell Membrane Ultrastructure Diagram, Fluid Mosaic Model, Hydrophilic Head (Phosphate Group), Hydrophobic Tail (Fatty Acid Chain), Phospholipid Molecule, Phospholipid Bilayer, Labeled Component X (Peripheral/Intrinsic Protein or Glycoprotein), Labeled Component Y (Transmembrane/Intrinsic Protein)

### Community 22 - "Community 22"
Cohesion: 0.5
Nodes (8): Alimentary Canal, Large Intestine, Liver (Label B), Mouth / Oral Cavity, Oesophagus (Label A), Probiotic Bacteria, Small Intestine, Stomach (Label C)

### Community 23 - "Community 23"
Cohesion: 0.57
Nodes (6): deleteUserProgressData(), getAllProgressUsernames(), getUserProgressData(), loadAllProgress(), saveAllProgress(), saveUserProgressData()

### Community 24 - "Community 24"
Cohesion: 0.29
Nodes (7): closeFullNotes(), escapeHtml(), examSectionBadge(), formatModelAnswer(), openExamBreakdown(), renderBreakdownModal(), renderBreakdownPie()

### Community 25 - "Community 25"
Cohesion: 0.52
Nodes (7): Absorption of Light, Blue-Violet Absorption Peak (~430-450 nm), Chlorophyll a, Photosynthesis Absorption Spectrum Diagram, Colour (Wavelength) of Light, Photosynthesis, Red Absorption Peak (~660-680 nm)

### Community 26 - "Community 26"
Cohesion: 0.48
Nodes (7): Cristae, Inner Membrane, Intermembrane Space, Mitochondrial Matrix, Matrix Granules / Ribosomes, Mitochondrion, Outer Membrane

### Community 27 - "Community 27"
Cohesion: 0.43
Nodes (7): Bacteria Growth Chart, Bacterial Growth Curve, Decline Phase (Death Phase), Population (Y-Axis Metric), Stage Z - Decline Phase, Stationary Phase, Time (X-Axis Metric)

### Community 28 - "Community 28"
Cohesion: 0.48
Nodes (7): Dashed Line Indicator for Cross-Section Plane, Plant Root Longitudinal Section Diagram, Region X - Root Hair Zone, Region Y - Elongation Zone, Region Z - Root Cap / Meristematic Zone, Transverse Section of Root at Dashed Line, Root Biology Worksheet

### Community 29 - "Community 29"
Cohesion: 0.5
Nodes (3): buildGlyph(), F, render()

## Ambiguous Edges - Review These
- `Labeled Component X (Peripheral/Intrinsic Protein or Glycoprotein)` → `Labeled Component Y (Transmembrane/Intrinsic Protein)`  [AMBIGUOUS]
  images/cell-membrane.png · relation: conceptually_related_to

## Knowledge Gaps
- **149 isolated node(s):** `COURSE_DATA`, `APPROVED_USERNAMES`, `FALLBACK_CHAPTERS`, `BUSINESS_SUBJECT`, `PE_SUBJECT` (+144 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Labeled Component X (Peripheral/Intrinsic Protein or Glycoprotein)` and `Labeled Component Y (Transmembrane/Intrinsic Protein)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `buildPrompt()` connect `Approved User Accounts` to `Core App Logic`, `Community 19`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Why does `run()` connect `App Bootstrap & Config` to `Approved User Accounts`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Why does `Approved Usernames List` connect `Plant Vascular Tissue` to `Core App Logic`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Approved Usernames List` (e.g. with `Auth Panel` and `Account Switcher Select`) actually correct?**
  _`Approved Usernames List` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `COURSE_DATA`, `APPROVED_USERNAMES`, `FALLBACK_CHAPTERS` to the rest of the system?**
  _149 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Approved User Accounts` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._