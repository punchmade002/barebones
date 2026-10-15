# Notes standard — instructions for the content model

This standard applies to every subject. Read it together with the subject's outline (e.g.
`course-outlines/geography.md`). The outline says **what** to cover; this file says **how**
to write it.

## The goal

Notes a student can read straight through and revise from, that contain **everything that
could be examined** in each subsection, **stated once**, with no padding.

## Rules

1. **Cover every syllabus point in the subsection.** Work through the outline's "Syllabus"
   list item by item. Every item gets its own note block or bullet. If a past exam question
   tagged to the chapter (`<subject>-exam-questions.js`) asks about something, the notes must
   contain the facts needed to answer it.
2. **Say each fact once.** Don't restate the overview in later blocks, repeat a definition in
   a second block, or summarise what you just said. Where a later block needs a term from an
   earlier one, use the term without redefining it.
3. **No filler or meta-text.** Banned: "These ideas should be used together…", "It is important
   to note…", "In conclusion…", "This topic is frequently examined…", "A complete answer
   should…". Every sentence must teach a fact, process or example.
4. **Never paste past-paper text.** Don't copy question wording or marking-scheme answers into
   the notes. Teach the content the question needs.
5. **Dense:** one distinct, specific, examinable fact per bullet (the equivalent of one
   significant relevant point, or SRP). A subsection that can carry a 30-mark answer needs at
   least 15 such bullets in total, and most need more. Use named places, dates, figures and
   processes rather than general statements.
6. **Readable:** short descriptive headings; plain language; define each technical term in
   bold-free plain text the first time it appears; bullets in a logical order (cause → process
   → result, or stage 1 → stage 2 → stage 3).
7. **Examples are specific and real.** Name the place (e.g. "Powerscourt Waterfall, River
   Dargle, Co. Wicklow"), not "a waterfall in Ireland". Use the syllabus's own settings where it
   gives them. Never invent statistics. If unsure of a figure, leave it out.
8. **Accurate before complete.** If you aren't confident a fact is correct, omit it rather than
   guess.

## Output format

Write each subsection as one JSON object. The app shows `h` as the heading, `b` as a short
lead paragraph, and `points` as a bulleted list. `b` is optional when `points` carries the
content.

```json
{
  "chapterId": "geo-rivers",
  "subsection": "1. Fluvial processes, patterns and associated landforms",
  "syllabusRef": "1.5",
  "notes": [
    { "h": "Heading", "b": "One or two sentence lead.", "points": ["Fact.", "Fact."] }
  ],
  "keyTerms": [
    { "term": "Hydraulic action", "definition": "One-sentence definition." }
  ]
}
```

- `notes`: usually 4–10 blocks per subsection, each with 3–10 points.
- `keyTerms`: the subsection's essential vocabulary for flashcards, one sentence each. These
  can overlap with the notes, because flashcards are a separate study mode.
- No markdown inside strings: no `**`, no headings, no line breaks. The app strips them.

## Block types to use

- **Process:** what drives it, then step-by-step how it works.
- **Landform / feature:** what it is; how it forms, in numbered stages; a named example; what
  to draw in a labelled diagram.
- **Case study:** place and context; specific facts, dates and figures; effects; responses or
  evaluation.
- **Comparison / evaluation:** advantages vs disadvantages, or A vs B, as paired points.
- **Skills:** the method step by step, with a worked example.

## Worked example (geography)

This is the target standard: dense, specific, non-repetitive and readable. It covers only the
first subsection of `geo-rivers`; real output must cover every subsection.

```json
{
  "chapterId": "geo-rivers",
  "subsection": "1. Fluvial processes, patterns and associated landforms",
  "syllabusRef": "1.5",
  "notes": [
    {
      "h": "How rivers erode",
      "b": "A river's energy depends on its volume and gradient. Energy not used to overcome friction is available to erode and transport.",
      "points": [
        "Hydraulic action: the force of moving water dislodges loose material and forces air into cracks in the bed and banks, widening them until rock breaks away.",
        "Abrasion: the load scrapes and grinds the bed and banks; pebbles swirled in hollows drill potholes into the bed.",
        "Attrition: pieces of load collide with each other and with the bed, becoming smaller and more rounded downstream.",
        "Solution: slightly acidic water dissolves soluble rock such as limestone, carrying it away in solution.",
        "Vertical erosion dominates in the upland (youthful) stage; lateral erosion dominates in the middle (mature) stage."
      ]
    },
    {
      "h": "How rivers transport and deposit",
      "points": [
        "Traction: the largest boulders are rolled along the bed, mainly during floods.",
        "Saltation: pebbles and sand bounce along the bed in a series of hops.",
        "Suspension: fine silt and clay are carried within the flow, giving the water its brown colour.",
        "Solution: dissolved minerals are carried invisibly in the water.",
        "Deposition happens when velocity falls: entering a lake or the sea, on the inside of a bend, when a flood recedes, or when the load becomes too great for the river's energy.",
        "The heaviest material is deposited first and the finest last, so deposits are sorted by size."
      ]
    },
    {
      "h": "Drainage patterns",
      "b": "The arrangement of a river and its tributaries reflects the underlying rock and relief.",
      "points": [
        "Dendritic: tree-like, with tributaries joining at acute angles; forms on rock of uniform resistance, e.g. much of the Shannon basin.",
        "Trellised: tributaries meet the main river at right angles; forms where bands of hard and soft rock alternate, e.g. the ridge-and-valley landscape of Munster.",
        "Radial: rivers flow outward from a central high point like spokes of a wheel, e.g. the rivers draining the Wicklow Mountains.",
        "Deranged: no clear pattern, with many lakes and marshes; forms on poorly drained glacial deposits, e.g. parts of the drumlin belt in Co. Cavan."
      ]
    },
    {
      "h": "V-shaped valley and interlocking spurs (erosion, upland stage)",
      "points": [
        "1. Steep gradient gives the river high energy, so it erodes vertically by hydraulic action and abrasion.",
        "2. Weathering and mass movement loosen the valley sides and move material into the channel, widening the top of the valley.",
        "3. The result is a narrow floor and steep sides in a V-shape.",
        "4. The river swings around areas of harder rock, leaving spurs that interlock like the teeth of a zip.",
        "Example: the upper course of the River Liffey in the Wicklow Mountains.",
        "Diagram: cross-section of a V-shaped valley; plan view of interlocking spurs with the river winding between them."
      ]
    },
    {
      "h": "Waterfall and gorge (erosion)",
      "points": [
        "1. A waterfall forms where a band of resistant rock lies over less resistant rock.",
        "2. The soft rock below is eroded faster by hydraulic action and abrasion, undercutting the hard rock and leaving an overhang.",
        "3. Falling water and its load scour a deep plunge pool at the base.",
        "4. The unsupported overhang collapses, and the waterfall retreats upstream.",
        "5. Repeated retreat leaves a steep-sided gorge downstream of the falls.",
        "Examples: Powerscourt Waterfall, River Dargle, Co. Wicklow (Ireland's highest at about 121 m); Torc Waterfall, near Killarney, Co. Kerry; Niagara Falls, USA–Canada.",
        "Diagram: cross-section showing hard rock cap, soft rock beneath, overhang, plunge pool and direction of retreat."
      ]
    },
    {
      "h": "Meanders and oxbow lakes (erosion and deposition, mature and old stages)",
      "points": [
        "1. Water flows fastest on the outside of a bend, where it erodes the bank by hydraulic action and abrasion, forming a steep river cliff.",
        "2. Water is slowest on the inside of the bend, where it deposits sand and gravel, forming a gently sloping point bar (slip-off slope).",
        "3. Corkscrew-shaped (helicoidal) flow carries eroded material from the outer bank to the inner bank of the next bend.",
        "4. Continued lateral erosion makes the bends more pronounced until only a narrow neck of land separates them.",
        "5. During a flood the river cuts through the neck and takes the straighter, shorter course.",
        "6. Deposition seals off the old bend, leaving a crescent-shaped oxbow lake that slowly fills with silt to become a meander scar.",
        "Examples: meanders on the River Shannon's floodplain (the Shannon Callows); oxbow lakes on the lower Mississippi, USA.",
        "Diagram: plan view of a meander with fastest flow line, river cliff and point bar; four-stage sequence of oxbow formation."
      ]
    },
    {
      "h": "Floodplain and levees (deposition, old stage)",
      "points": [
        "1. Lateral erosion by migrating meanders widens the valley floor.",
        "2. When the river floods, it spreads across the valley, loses velocity and deposits a layer of fine silt called alluvium.",
        "3. Repeated floods build a wide, flat, fertile floodplain.",
        "4. The coarsest material is dropped first, right beside the channel, so each flood raises the banks a little.",
        "5. Over time these build into natural embankments called levees, and the river bed itself may rise above the level of the floodplain.",
        "Examples: the Shannon Callows (floodplain); levees along the Mississippi, USA, which have been artificially raised for flood control.",
        "Diagram: cross-section of a floodplain showing alluvium layers, levees and the raised channel."
      ]
    },
    {
      "h": "Delta (deposition at the mouth)",
      "points": [
        "1. A delta forms where a river carrying a heavy load enters a sea or lake and its velocity drops sharply.",
        "2. In salt water, fine clay particles clump together (flocculation) and sink faster.",
        "3. Deposits build up until they block the channel, forcing the river to split into smaller channels called distributaries.",
        "4. Conditions needed: a large load; calm water with a small tidal range and weak currents, so deposits aren't removed.",
        "Types: arcuate (fan-shaped, e.g. the Nile, Egypt); bird's-foot (long fingers of deposits along distributaries, e.g. the Mississippi, USA); estuarine (filling a drowned river mouth).",
        "Irish example: the lake delta between the Upper and Lower Lakes at Glendalough, Co. Wicklow.",
        "Diagram: plan view of a delta with distributaries; cross-section showing topset, foreset and bottomset beds."
      ]
    }
  ],
  "keyTerms": [
    { "term": "Hydraulic action", "definition": "Erosion by the force of moving water, which dislodges material and forces air into cracks until rock breaks away." },
    { "term": "Abrasion", "definition": "Erosion caused by the river's load scraping and grinding against the bed and banks." },
    { "term": "Attrition", "definition": "The wearing down of the load as particles collide, making them smaller and rounder downstream." },
    { "term": "Plunge pool", "definition": "A deep hollow scoured at the foot of a waterfall by falling water and its load." },
    { "term": "Point bar", "definition": "A gently sloping deposit of sand and gravel on the inside of a meander bend." },
    { "term": "Levee", "definition": "A natural embankment of coarse alluvium built up along a river's banks by repeated flooding." },
    { "term": "Distributary", "definition": "A smaller channel that splits from the main river and flows across a delta." }
  ]
}
```

## Quality checks before finishing a chapter

- Every "Syllabus" item for the chapter in the outline has a block or bullet.
- No two blocks state the same fact.
- No sentence contains filler or meta-text (rule 3).
- Every landform has formation stages, a named example and a diagram cue.
- Every case study has specific facts.
- All strings are plain text.
