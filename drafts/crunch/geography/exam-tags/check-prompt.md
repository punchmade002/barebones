You are checking another model's work: it tagged past Leaving Certificate Geography exam answers to the note points a student must have learned to earn the marks. The tagging rules are in /Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/prompt.md (read it first). For each batch you are given, read the whole batch file (page through it with offset/limit to the end) and the output file of every question in it (out/<question id>.json in the same exam-tags folder).

For every marking point, decide:
- WRONG: no tagged point states the fact (it only shares words or the topic). Remove the marking point, or swap in a candidate that does state it.
- MISSED: a sentence of the model answer whose fact a candidate states, with no marking point. Add it.
- TOO MANY: more marking points than the marks ÷ 2, or two marking points for one sentence of the answer. Merge them.
Leave correct tags alone. Use only ids from that question's CANDIDATES. Fix the output files in place, keeping the same JSON format, then check that each still parses, has every part label once, has every "k" between 1 and the length of its "of" list, and uses only candidate ids.
If you write a helper script, put it ONLY in /Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/tmp/check-<batch name>/. Never use /tmp, and never run a script you didn't write.

Reply with just this, per batch: marking points checked, how many were WRONG, MISSED and TOO MANY, and the one most common mistake in a line.
