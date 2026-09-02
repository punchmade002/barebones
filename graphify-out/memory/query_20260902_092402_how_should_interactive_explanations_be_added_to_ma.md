---
type: "query"
date: "2026-09-02T09:24:02.062950+00:00"
question: "How should interactive explanations be added to maths worked answers?"
contributor: "graphify"
source_nodes: ["app.js", "exam-questions-db.js", "renderExamSection", "formatModelAnswer"]
---

# Q: How should interactive explanations be added to maths worked answers?

## Answer

Represent each maths solution as structured steps with stable IDs, an equation, the operation performed, why it is valid, the rule used, and common mistakes. Render the steps as selectable cards with KaTeX. Clicking a step or selecting text opens an anchored explanation panel. Keep the current model string as a fallback for non-maths subjects and migrate maths incrementally. Use curated explanations first, with optional contextual AI follow-up only after the deterministic version is reliable.

## Source Nodes

- app.js
- exam-questions-db.js
- renderExamSection
- formatModelAnswer