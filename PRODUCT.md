# bare bones — Product Context

## Product Purpose
A browser-based study tool built for a small group of Irish Leaving Certificate students. Strips away noise and gamification — just the content, the test, and your progress. The name says it all.

## Register
product — design serves the studying, not the other way around

## Users
Irish LC students (16–18), a named cohort of ~13 people. They know each other. The tool is invite-only (approved usernames). They study Business, PE, Biology, Geography, and Maths.

**Mental model:** a student sitting down to grind through a chapter before an exam. They want to flip cards, test themselves, read model answers, and see how far along they are. Nothing more.

## Brand Tone
Focused. Warm but no-nonsense. Slightly editorial — the ASCII logo gives it personality without being loud. Orange is the energy; everything else is calm.

**Not:** gamified, patronising, corporate EdTech, cluttered, generic SaaS dashboard.

## Core Features
- Subject/chapter picker sidebar (left column, sticky scroll)
- Flashcard study mode — concept cards with flip, mark-learned, keyword chips
- Written test — 3-question sample, scored with keyword matching + semantic overlap
- Exam Qs — past LC paper questions with model answers (show/hide)
- Subject overview — per-chapter progress bars when clicking a subject header
- Full Notes overlay — all chapter content in a reading view
- Progress screen — overall % + per-subject breakdown with chapter bars
- Multi-account support (localStorage, invite-only usernames)

## Strategic Principles
- No build step. No bundler. Open index.html and it works.
- Every feature should feel like less, not more.
- Progress data is the student's — stored locally, not phoned home.
- Exam Qs and model answers are the highest-value content. Protect their clarity.
