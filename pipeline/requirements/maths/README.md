# Maths skills database

Every skill the Leaving Cert Maths syllabus (examined from 2015) can ask for. A skill is one way of treating numbers that turns a given input into a definite output, for example "cubic with an integer root → all three roots". Scope comes from `pipeline/resources/maths/spec-syllabus.pdf` (strands 1–5, the trig formulae appendix, and the Geometry for Post-primary School Mathematics constructions and theorems), **not** from past papers.

- `skills.py`: the hand-authored rows. Edit this file.
- `skills.json` / `skills.md`: generated. Each skill has `id`, `level`, `syllabus` (topic 1.1–5.2), `chapter` (app chapter `mathsN`), `paper`, `input`, `output`, `example`, `prereqs` (the smaller skills it needs) and `usedBy` (the reverse).
- Levels: `JC` is Junior Cycle knowledge the syllabus assumes and may examine. `OL` is required at Ordinary and Higher, because OL is a subset of HL. `HL` is Higher only. Constructions 3 and 7, Theorem 19 and Corollaries 1, 2 and 5 are tagged HL, because the syllabus assumes them only from JC Higher.

Run `python3 pipeline/requirements/maths/build.py` to rebuild. It exits non-zero if an id is duplicated, a prereq is unknown, the prereq graph has a cycle, an OL or JC skill depends on a higher-level skill, or any syllabus topic or app chapter has no skills.

Keep ids stable. Questions and progress will key off them.

Judgement calls that need a teacher's review:
- `diff-inverse-trig`: reads "inverse functions" in 5.2 as sin⁻¹ and tan⁻¹.
- `int-reciprocal` (∫1/x): reads 5.2's xᵃ, a ∈ Q as including a = −1.
- Decomposition skills the syllabus does not name word for word: `eq-surd`, `ineq-prove`, `seq-sigma`, `quad-discriminant` (HL), `diff-inflection` (HL), `fin-rate-conversion`, `fin-amortisation`, `circ-common-chord`, `circ-tangent-length`, `trig-sine-ambiguous`, `fn-transformations`.
