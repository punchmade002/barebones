---
type: "query"
date: "2026-09-01T10:42:07.788501+00:00"
question: "Can the Biology exam pipeline fill only missing marking-scheme answers, replace nonexistent or duplicated 2015-2017 papers, deduplicate images, and include orphan question pages without regenerating existing transcriptions?"
contributor: "graphify"
source_nodes: ["segment.py", "pair_marking_scheme()", "stages_3to8.py"]
---

# Q: Can the Biology exam pipeline fill only missing marking-scheme answers, replace nonexistent or duplicated 2015-2017 papers, deduplicate images, and include orphan question pages without regenerating existing transcriptions?

## Answer

The graph confirms that segmentation, marking-scheme pairing, and downstream answer work are separate stages, so a partial repair is architecturally possible. The graph is stale and does not establish the current cache controls, so current source inspection is required before choosing the exact entry point.

## Source Nodes

- segment.py
- pair_marking_scheme()
- stages_3to8.py