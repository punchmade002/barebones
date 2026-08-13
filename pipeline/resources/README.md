# Pipeline resource contract

These folders are editorial inputs to the pipeline. They do not change app course content by
themselves.

Every subject listed in `resources.SUPPORTED_SUBJECTS` must contain exactly the same core resource
set:

1. `manifest.json` - machine-readable provenance, level, coverage counts, alignment status,
   source profile and first examination year.
2. `spec-syllabus.pdf` - the official NCCA syllabus or current curriculum specification.
3. `guide-simplestudy.md` - the complete Higher Level SimpleStudy unit/topic taxonomy plus
   subject-specific pipeline guidance.
4. `worked-example-guidance.md` - the answer pattern the pipeline should follow and one original
   model illustrating that pattern.

The source policy is fixed:

- NCCA is the authority for course scope and assessment.
- SimpleStudy is the single secondary research source for structure, sequencing and teaching
  presentation. The authenticated course is preferred; when an older account picker does not list
  a subject, use SimpleStudy's current public subject catalogue and record that access surface in
  the manifest.
- SEC papers and marking schemes remain the authority for real exam questions and official
  answers.
- SimpleStudy subscription prose and worked answers must not be copied into app content.

`resources.require_bundle(subject)` enforces the contract before Stage 0. A subject with missing
files, mixed research providers, missing headings, an implausible exam cutoff or empty coverage
counts cannot enter the pipeline. The cutoff is the first examination year, not the date teaching
began, so the acquisition stage does not pull papers from the wrong syllabus.

Run:

```sh
python3 pipeline/resources.py <subject> --force
python3 pipeline/tests/run_tests.py resources
```

| Subject | SimpleStudy units | Topics | First exam year | Alignment |
|---|---:|---:|---:|---|
| Accounting | 17 | 17 | 2002 | aligned; current syllabus through June 2028 |
| Art | 36 | 53 | 2023 | aligned; catalogue taxonomy mapped to NCCA strands |
| Biology | 32 | 53 | 2027 | aligned |
| Business | 22 | 35 | 2027 | aligned |
| Chemistry | 15 | 54 | 2027 | aligned |
| Computer Science | 21 | 27 | 2025 | aligned to updated specification |
| DCG | 22 | 153 | 2009 | aligned; repeated catalogue cards de-duplicated |
| Economics | 16 | 20 | 2021 | aligned |
| English | 31 | 85 | 2001 | aligned; prescribed texts remain year-bound |
| Geography | 23 | 63 | 2028 | transitional; map outgoing taxonomy to the new NCCA spec |
| History | 6 | 66 | 2006 | aligned |
| Home Economics | 12 | 32 | 2004 | aligned |
| Mathematics | 27 | 156 | 2015 | aligned |
| Music | 9 | 10 | 1999 | aligned; prescribed works remain cycle-bound |
| Physical Education | 12 | 25 | 2022 | aligned |
| Politics and Society | 10 | 57 | 2021 | aligned to updated specification |
