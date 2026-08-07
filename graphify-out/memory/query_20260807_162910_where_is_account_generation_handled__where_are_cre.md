---
type: "query"
date: "2026-08-07T16:29:10.053934+00:00"
question: "Where is account generation handled, where are credential emails processed, and what persistent storage patterns should a mailing list use?"
contributor: "graphify"
source_nodes: ["Auth Panel", "app.js", "Approved Usernames List"]
---

# Q: Where is account generation handled, where are credential emails processed, and what persistent storage patterns should a mailing list use?

## Answer

The existing graph places the account UI in the Auth Panel and connects it to app.js. The approved_usernames.txt file is a historical cohort manifest conceptually related to authentication, not the current credential store. The code therefore needed a protected persistence layer attached to account creation, with the root mailing-list file serving only as an administrative export.

## Source Nodes

- Auth Panel
- app.js
- Approved Usernames List