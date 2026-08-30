---
type: "query"
date: "2026-08-30T12:33:53.790099+00:00"
question: "Why was generated PE content missing from index.html and the live app after deployment?"
contributor: "graphify"
source_nodes: ["app.js", "buildSubjectChapters", "renderGraph", "index.html"]
---

# Q: Why was generated PE content missing from index.html and the live app after deployment?

## Answer

The deployment was current, but index.html only contained seven-subject marketing copy and app.js built PE from legacy pe1-to-pe9 COURSE_DATA ids. The generated pe-flashcards.js and pe-exam-questions.js use sixteen pe-* chapter ids, so their data had no visible chapter mapping. The fix adds a pre-app adapter that replaces the legacy PE chapter shell with the sixteen pipeline ids, updates the landing copy, and cache-busts the PE assets.

## Source Nodes

- app.js
- buildSubjectChapters
- renderGraph
- index.html