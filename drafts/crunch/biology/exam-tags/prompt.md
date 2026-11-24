You are tagging past Leaving Certificate Biology exam answers to the exact note points a student must have learned to earn the marks. This is for a feature that hides the least valuable note points from a student's course, so a wrong tag either wastes the student's time or costs them marks.

Read ONLY the package files you are given, using the Read tool. Each package has:
- QUESTION: the question id.
- PART blocks: a part label, its marks, the subsections it was tagged to, and the MODEL ANSWER (written from these notes and checked against the marking scheme).
- CANDIDATES <subsection>: the note points you may tag, each as `[point-id] text`.

For EVERY part, list its marking points. A marking point is one thing the examiner gives marks for. For each one, give the note points that let a student write it:
- {"k": 1, "of": ["id"]}: the student needs that one point.
- {"k": 1, "of": ["id1", "id2"]}: any ONE of these points earns it, e.g. the model answer says "Haemophilia (or colour-blindness)" and each is a separate point, or the same fact is stated in two places.
- {"k": 2, "of": ["id1", "id2", "id3", "id4"]}: the part asks for, e.g., two examples and the notes give four acceptable ones. The student needs any two.

Rules:
- Tag the point that actually STATES the fact or method used. Don't tag a point just because it mentions the topic.
- Prefer the most specific point. Don't add background points the answer doesn't use; prerequisites are handled separately.
- Count marking points from the model answer: "1. … 2. …" or three facts for 9 marks means separate marking points. One definition is one marking point.
- If the answer is worked out from information printed in the question (reading a graph, or a genotype given in the question), tag only the method the student must know (e.g. how to set out a dihybrid cross). If it needs nothing from the notes, give that part an empty list [].
- If the notes don't cover the answer at all, give an empty list [].
- Use only ids that appear in the package. Never invent or shorten ids.

Write ONLY this JSON to the output path you are given, one key per part label exactly as printed, in order:
{"(a)(i)": [{"k": 1, "of": ["bio17-s3.0.0"]}], "(a)(ii)": [{"k": 2, "of": ["bio17-s3.2.1", "bio17-s3.2.2", "bio17-s3.2.3"]}], "(b)(ii)1": []}

Then check it: it must parse, have every part label exactly once, every "k" must be between 1 and the length of its "of" list, and every id must appear in the package.

If you write any helper script, put it ONLY in /Users/gabrielwhelan/barebones/drafts/crunch/biology/tmp/<question id>/ (create it). Other agents run at the same time: never use /tmp or a shared scratchpad, and never run a script you didn't write.
Read the full text of the candidates before deciding. Never shorten or truncate text when printing it. Decide EVERY part explicitly, never with a default.

Reply with just this, per question: part count, marking-point count, empty parts, and any part you were unsure about (label and one line why).
