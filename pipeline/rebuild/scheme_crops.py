"""Crop each question's marking scheme out of the official scheme PDF, like crops.py does for the paper.

The app shows a question's scheme behind its Marking scheme button, as images of the SEC's own
scheme pages. A question starts at its heading at the left margin ("Question 7" in newer schemes,
a bare "7" in older ones) and runs to the next question's heading or the end of the scheme; the
front matter before Question 1 (marking notes, mark conversion tables) belongs to no question.

    python3 pipeline/rebuild/scheme_crops.py biology            # crop every year, then attach
    python3 pipeline/rebuild/scheme_crops.py biology attach     # only re-attach to the bank

Writes   exam-images/<subject>/<year>/<level>-q<N>-ms-<k>.webp   (public, shown in the app)
         <DATA>/<subject>/scheme-crops.json                       (manifest; assemble.py reads it)
and adds schemeImages[] to each matching question in <subject>-exam-questions.js.
Prints the questions in the bank that got no scheme crop, for review.
"""
import json
import re
import sys
from pathlib import Path

import fitz

sys.path.insert(0, str(Path(__file__).parent))
from crops import CROP_ZOOM, DATA, PAD, ROOT, content_box, footer_y, lines_of  # noqa: E402

# "Question 7", "QUESTION 7:", "QUESTION 10 : Answer any two"; not "Question 7 (continued)" or "Question 16 (a)"
# ("Question 13 - Answer any two", "Question 13.  Answer all parts" in PE; Chemistry 2014 HL misprints "QUSESTION 2")
HEADING = re.compile(r'^Qu[a-z]*tion\s+(?P<n>\d{1,2})\s*([:\-–.].*)?$', re.I)
BARE = re.compile(r'^Q?(?P<n>\d{1,2})\.?(\s*\(a\))?$')     # "7", "7.", "Q7", or "7 (a)" opening a question in parts
# Maths heads every page of a question "Q7", "Q2 Model Solution – 25" or "P1 Q7" (2023 OL drops the
# Q for a few: a lone "3"), and restarts at Q1 for Paper 2. Its contents table lists "Question 1"
# lines, so "Question N" only counts in a scheme with no Q headings (2015).
PAPER_HEADING = {'maths': re.compile(r'^(?:P(?P<p>[12])\s+)?(?:Q(?=\d)|(?=\d{1,2}$))(?P<n>\d{1,2})(\s|$)')}
# Headings sit left of this (PE indents them to ~94pt); bare numbers likewise (up to ~105pt).
# Maths heads sit at ~63pt and its working is full of lone numbers from ~90pt in.
MARGIN = {'maths': 75}
SECTION = re.compile(r'^Section\s+[A-C]\b', re.I)         # a section banner ends the question above it
# So do the pages between one paper's marking notes and the next (Maths), and the coursework
# rubrics after the last question (PE)
# ("Marking" and "Scheme – Paper 2" can fall on separate lines; a paper's cover starts "Mathematics";
# the Irish bonus-marks table "Marcanna Breise" follows the questions)
BREAK = re.compile(r'^((Marking\s+)?Scheme\s*[–-]\s*Paper|Structure of the marking scheme|Summary of mark allocations'
                   r'|Detailed marking notes|Instructions$|Paper\s+[12]$|Mathematics$|Coimisiún na Scrúduithe Stáit'
                   r'|Marcanna Breise|(Leaving Certificate\s+)?Physical Activity Project|Performance Assessment)', re.I)
BLANK = re.compile(r'\s*BLANK\s+PAGE\s*', re.I)
# Running heads some years print at the top of every page ("Higher Level Biology Marking Scheme 2020")
HEAD = re.compile(r'Marking Scheme|Leaving Certificate', re.I)
HEAD_ZONE = 90
TOP_Y = 20
CONTENTS_HEADINGS = 5
# Questions printed side by side in one box share its crop (2015 HL sets Q3 and Q4 in two columns).
SHARED = {'biology': {'2015-higher-q4': '2015-higher-q3'}}


# Older schemes' footers ("ATAL Chemistry Marking Scheme 2011 / Page 8", "page 10 of 16") that
# crops.py's paper footer rule doesn't know
SCHEME_FOOT = re.compile(r'Marking Scheme|ATAL Chemistry|^Page\s+\d+|page\s+\d+\s+of\s+\d+', re.I)
FOOT_ZONE = 70


def scheme_footer(page, lines):
    ys = [b[1] for b, t in lines if b[1] > page.rect.height - FOOT_ZONE and SCHEME_FOOT.search(t)]
    return min([footer_y(page, lines)] + [y - 2 for y in ys])


def find_questions(doc, subject=''):
    """[{number, paper, segments: [(page_index, y0, y1)]}] in scheme order; paper is 0 unless the
    subject's scheme holds two papers."""
    pages = [lines_of(page) for page in doc]
    margin = MARGIN.get(subject, 110)
    heading = PAPER_HEADING.get(subject, HEADING)
    if not any(heading.match(t) and not t.isdigit() for lines in pages for b, t in lines if b[0] < margin):
        heading = HEADING
    # A page listing five or more headings is a contents or mark-summary table, not the questions
    counts = [sum(bool(heading.match(t)) and not t.isdigit() for b, t in lines if b[0] < margin) for lines in pages]
    contents = {pno for pno, n in enumerate(counts) if n >= CONTENTS_HEADINGS}
    headed = any(n for pno, n in enumerate(counts) if pno not in contents)
    questions, current, last, paper, run = [], None, 0, 1 if subject in PAPER_HEADING else 0, 1
    for pno, (page, lines) in enumerate(zip(doc, pages)):
        footer = scheme_footer(page, lines)
        head = [b[3] for b, t in lines if b[1] < HEAD_ZONE and HEAD.search(t) and not BREAK.match(t)]
        cursor = max(head) + 2 if head else TOP_Y
        if headed and pno in contents:
            if current is not None:
                questions.append(current)
                current = None
            continue
        for (x0, y0, _, y1), text in lines:
            if y0 >= footer or y0 < cursor:
                continue
            if (SECTION.match(text) or BREAK.match(text)) and x0 < 300 and current is not None:
                current['segments'].append((pno, cursor, y0 - 3))
                questions.append(current)
                current = None
                continue
            if x0 >= margin:
                continue
            m = (heading if headed else BARE).match(text)
            if m and not headed and not paper and int(m.group('n')) == 1 and last >= 5:
                questions, current, last = [], None, 0   # that run was the scheme's numbered notes
            if m and paper:
                printed = int(m.groupdict().get('p') or 0)
                if printed and printed != paper:
                    paper, last = printed, 0
                elif not printed and int(m.group('n')) == 1 and last >= 5:
                    run, last = run + 1, 0     # the next paper (or pass) starts again at Q1
                    paper = run
            # Only the next number in sequence counts (a lone "3" at the margin is otherwise a
            # mark total); one may be skipped, as 2015 HL prints no "4."
            if not m or not last < int(m.group('n')) <= last + 2:
                continue
            # cut above the whole row: a number can sit a little below the text beside it
            cut = max(min(b[1] for b, t in lines if t.strip() and b[1] < y1 and b[3] > y0) - 3, cursor)
            if current is not None:
                current['segments'].append((pno, cursor, cut))
                questions.append(current)
            last = int(m.group('n'))
            current = {'number': last, 'paper': paper, 'segments': []}
            cursor = cut
        if current is not None:
            current['segments'].append((pno, cursor, footer))
    if current is not None:
        questions.append(current)
    if paper and run == 4:
        # 2015 Maths goes through each paper twice: model solutions, then detailed marking notes.
        # Runs 1-2 are Paper 1 and 3-4 Paper 2; a question's notes join its solution.
        merged = {}
        for q in questions:
            q['paper'] = (q['paper'] + 1) // 2
            key = (q['paper'], q['number'])
            if key in merged:
                merged[key]['segments'] += q['segments']
            else:
                merged[key] = q
        questions = list(merged.values())
    return questions


def has_text(text):
    """False for a blank page, or one holding only its page number and running head."""
    text = re.sub(r'Page\s+\d+|ATAL Chemistry', '', HEAD.sub('', BLANK.sub('', text)))
    return re.search(r'[A-Za-z]{3}', text) is not None


def crop(subject, wanted):
    manifest = {}
    for pdf in sorted((ROOT / 'exam-papers' / subject).glob('*-marking-scheme.pdf')):
        year, level = pdf.name.split('-')[:2]
        if f'{year}-{level}' not in wanted:
            continue                     # a year the bank has no questions from
        doc = fitz.open(pdf)
        img_dir = ROOT / 'exam-images' / subject / year
        img_dir.mkdir(parents=True, exist_ok=True)
        for old in img_dir.glob(f'{level}-*-ms-*.webp'):
            old.unlink()                 # a rerun may cut a question into fewer pieces
        for q in find_questions(doc, subject):
            qkey = f'p{q["paper"]}-q{q["number"]}' if q['paper'] else f'q{q["number"]}'
            images = []
            for pno, y0, y1 in q['segments']:
                page = doc[pno]
                box = content_box(page, y0, y1)
                if box is None or box.height < 2 * PAD + 14 or not has_text(page.get_text(clip=box)):
                    continue
                name = f'{level}-{qkey}-ms-{len(images) + 1}.webp'
                page.get_pixmap(matrix=fitz.Matrix(CROP_ZOOM, CROP_ZOOM), clip=box) \
                    .pil_save(img_dir / name, format='WEBP', quality=78, method=6)
                images.append(f'exam-images/{subject}/{year}/{name}')
            manifest[f'{year}-{level}-{qkey}'] = {
                'scheme': f'exam-papers/{subject}/{pdf.name}',
                'pages': sorted({p + 1 for p, _, _ in q['segments']}), 'images': images}
        print(f'{pdf.name:40} {sum(k.startswith(f"{year}-{level}-") for k in manifest):3} questions')
    path = DATA / subject / 'scheme-crops.json'
    path.write_text(json.dumps(manifest, indent=1))
    return manifest


def read_bank(subject):
    text = (ROOT / f'{subject}-exam-questions.js').read_text()
    head, sep, rest = text.partition('.concat(\n')
    return head + sep, json.loads(rest.rsplit('\n);', 1)[0])


def attach(subject, manifest):
    bank_path = ROOT / f'{subject}-exam-questions.js'
    head, bank = read_bank(subject)
    missing = []
    for q in bank:
        key = q['id'].split('-pp-', 1)[1]
        images = manifest.get(SHARED.get(subject, {}).get(key, key), {}).get('images')
        if images:
            q['schemeImages'] = images
        else:
            q.pop('schemeImages', None)
            missing.append(key)
    bank_path.write_text(head + json.dumps(bank, indent=1, ensure_ascii=False) + '\n);\n')
    print(f'{len(bank) - len(missing)}/{len(bank)} questions have scheme crops')
    if missing:
        print('no scheme crop:', ' '.join(missing))


if __name__ == '__main__':
    subject = sys.argv[1]
    if sys.argv[2:] == ['attach']:
        attach(subject, json.loads((DATA / subject / 'scheme-crops.json').read_text()))
    else:
        wanted = {f'{q["year"]}-{q["level"]}' for q in read_bank(subject)[1]}
        attach(subject, crop(subject, wanted))
