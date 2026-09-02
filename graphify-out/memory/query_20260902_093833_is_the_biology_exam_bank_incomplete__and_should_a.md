---
type: "query"
date: "2026-09-02T09:38:33.524733+00:00"
question: "Is the Biology exam bank incomplete, and should a partial pipeline run expand it without replacing existing questions?"
contributor: "graphify"
source_nodes: ["segment.py", "biology_repair.py", "model_answers.py", "schemes.py"]
---

# Q: Is the Biology exam bank incomplete, and should a partial pipeline run expand it without replacing existing questions?

## Answer

Yes. The live canonical Biology bank contains 28 questions and 66 parts, all Higher Level, while the 36 digested official components represent 22 Higher and Ordinary exams and 350 numbered questions for 2015 through 2025. A targeted expansion should reuse the existing digests, scaffold, and 28 curated rows; run segmentation for all components; reconcile by year, level, and question identity; fill official scheme answers first and AI answers only for residual gaps; crop required figures; validate; and publish additively. The current default resume path is not sufficient because it considers a paper complete when any row from that paper exists, which skips 11 partially represented Higher components. Force mode is also unsafe because collection replaces the base canonical set. All new sources must retain the LEGACY pre-2027 label.

## Source Nodes

- segment.py
- biology_repair.py
- model_answers.py
- schemes.py