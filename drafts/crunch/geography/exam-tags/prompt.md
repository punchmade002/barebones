You are tagging past Leaving Certificate Geography exam answers to the exact note points a student must have learned to earn the marks. This is for a feature that hides the least valuable note points from a student's course, so a wrong tag either wastes the student's time or costs them marks.

Read ONLY the batch file you are given, with the Read tool, every line to the end (page through it with offset/limit if the Read is cut off). It holds several questions separated by lines of "=". Each question has:
- QUESTION: the question id.
- PART blocks: a part label, its marks and the MODEL ANSWER (written from these notes and checked against the marking scheme).
- CANDIDATES (shortlist): the note points you may tag, each as `[point-id] text`. A script picked them because they share words with the model answer, so many are near misses. Tag only the ones that really state what the answer uses.

For EVERY part, list its marking points. A marking point is one thing the examiner gives marks for:
- Short parts: usually one marking point per fact asked for (a definition, a named feature, a reason).
- Long answers (20 and 30 marks) are marked in SRPs (significant relevant points) of 2 marks each, so a 30-mark answer has up to about 15. Each SRP is one marking point. Headings like "Option chosen – …" or "Process – Carbonation:" are not SRPs.
For each marking point, give the note points that let a student write it:
- {"k": 1, "of": ["id"]}: the student needs that one point.
- {"k": 1, "of": ["id1", "id2"]}: any ONE of these points earns it (the same fact is stated in two places).
- {"k": 2, "of": ["id1", "id2", "id3"]}: the part asks for, e.g., two examples and the notes give three acceptable ones. The student needs any two.

Rules:
- Tag the point that actually STATES the fact used. Don't tag a point just because it mentions the topic or shares words.
- At most 2 ids in "of" unless the part asks for "any k of several" examples.
- If no candidate states a marking point's fact, leave that marking point out. Never put in a loosely related point instead.
- If the answer is read off a map, photograph, graph or figure printed in the question, or the model answer is "(none)", tag only a method the notes teach (e.g. how to give a six-figure grid reference), or give the part an empty list [].
- Use only ids printed in that question's CANDIDATES. Never invent or shorten ids.
- You may give one note point to two marking points when it states both facts.

Write ONE file per question, ONLY this JSON, to the output folder you are given, named <question id>.json, with one key per part label exactly as printed, in order:
{"2A(i)": [{"k": 1, "of": ["geo-rivers-s4.3.1"]}], "2A(ii)": [], "2B": [{"k": 1, "of": ["geo-rocks-weathering-s5.2.0"]}, {"k": 1, "of": ["geo-rocks-weathering-s5.2.1", "geo-rocks-weathering-s5.6.0"]}]}

Then check every file: it must parse, have every part label exactly once, every "k" must be between 1 and the length of its "of" list, and every id must be in that question's CANDIDATES.
If you write any helper script, put it ONLY in /Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/tmp/<batch name>/ (create it). Other agents run at the same time: never use /tmp or a shared scratchpad, and never run a script you didn't write. Decide EVERY marking point yourself; never fill parts with a default.

Reply with just this, per question: question id, part count, marking-point count, empty parts.
