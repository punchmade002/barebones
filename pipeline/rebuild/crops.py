"""Crop each exam question straight out of the paper PDF.

The app shows students the original paper (question text, data, figures, tables), never a
transcription. This finds every question's start ("7." at the left margin), follows it across
pages until the next question or a stop page (answerbook instructions, acknowledgements, blank
page), trims the running footer, and writes one WebP per page segment.

    python3 pipeline/rebuild/crops.py biology 2025-higher-PA 2025-higher [...]

Writes   exam-images/<subject>/<year>/<level>-q<N>-<k>.webp      (public, shown in the app)
         <DATA>/<subject>/crops.json                              (manifest, internal)
         <DATA>/<subject>/pages/<paper>/p<NN>.png                 (full pages, for agents)
         <DATA>/<subject>/text/<year>-<level>-q<N>.txt            (text layer, internal only)

Boxes can be overridden per question in <DATA>/<subject>/crop-overrides.json:
    {"2025-higher-q4": [{"paper": "2025-higher-PA", "page": 6, "y0": 50, "y1": 700}]}
"""
import json
import re
import sys
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
RAW = Path.home() / 'barebones/pipeline/_data/raw'
DATA = Path.home() / 'barebones/pipeline/_data/rebuild'

FOOTER_ZONE = 90        # running footers ("Page 3 of 16", "[OVER]", "Leaving Certificate ...") sit in the bottom 90pt
TOP_Y = 20
PAD = 6
CROP_ZOOM = 2.0         # ~144 dpi: sharp on phones, small files
PAGE_DPI = 110
STOP_MARKERS = ('Answerbook for Section C', 'Acknowledg', 'Copyright notice', 'Blank Page',
                'Start each question on a new page', 'Do not write on this page',
                'There is no examination material on this page', 'Do not hand this question paper up',
                'supplied in a separate', 'is supplied separately',
                'Questions for Section C are supplied separately', 'Space for extra work',
                'Indicate clearly the question number', 'PART TWO are supplied separately',
                'Do not hand this up', 'This document will not be returned')
STOP_LINES = ('Instructions',)  # whole-line markers (the answerbook's Section C instructions page)
BACK_COVER = re.compile(r'Leaving Certificate\s*[–-]\s*(Higher|Ordinary)')  # "The Leaving Certificate – Ordinary Level"
ANCHOR = re.compile(r'^(\d{1,2})(\.?)(\s|$)')
# PE prints "Question 7" at the margin; its numbered answer lines ("1.", "2.") sit just inside it.
HEADED = re.compile(r'^Question\s+(\d{1,2})()(\s|$)')
# Subjects whose Section B opens with a case study before its one question: those pages belong to it.
PREAMBLE_SECTIONS = {'pe': {'B'}}
# Geography numbers Part One "1."-"12.", then Part Two "Question 1"-"Question 12" and the options
# "13."-"24." (2017-19 in one file; 2020+ as separate P1/P2 files). Part Two is keyed 100+N so the
# two parts never share a key; the printed number is kept as printedNumber.
GEO_PART_TWO = 100
# Instruction blocks between Geography's parts and sections: they end the question above them and
# belong to no question.
GEO_BREAK = re.compile(r'^(PART (ONE|TWO)\b|SECTION \d|PATTERNS AND PROCESSES|REGIONAL GEOGRAPHY|Questions \d+ to \d+'
                       r'|Note:\s+It is better|Attempt (ONE|any|TWO) question|You MUST attempt|Answerbook for PART TWO'
                       r'|(Global Interdependence|Geoecology|Culture and Identity|(The )?Atmosphere\s*[–-]\s*Ocean Environment)\s*$)')


def geo_section(number):
    if number < GEO_PART_TWO:
        return 'P1'
    n = number - GEO_PART_TWO
    return 'core' if n <= 6 else 'elective' if n <= 12 else 'option'
ANCHOR_SLACK = 8        # question numbers sit at the paper's left margin; numbered sub-items are indented
SECTION = re.compile(r'^Section\s+([ABC])\b')
FOOTER = re.compile(r'^(Page \d+ of \d+|\[OVER\]|Leaving Certificate Examination.*|Leaving Certificate,?\s*\d{4}.*|(Biology|Chemistry|Physical Education|Geography)\s*[–-].*[Ll]evel.*'
                    r'|Sections? [ABC].*|\d{1,2})$')


def paper_pdf(subject, paper):
    """Raw paper PDF; pre-syllabus reference papers are stored with a -REF suffix."""
    plain = RAW / subject / f'{paper}-EV-papers.pdf'
    return plain if plain.exists() else RAW / subject / f'{paper}-EV-papers-REF.pdf'


def lines_of(page):
    out = []
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            text = ''.join(s['text'] for s in line['spans']).replace('\xa0', ' ').strip()
            if text:
                out.append((line['bbox'], text))
    return sorted(out, key=lambda l: (round(l[0][1]), l[0][0]))


def footer_y(page, page_lines):
    """Top of the running footer; papers differ by year (2015-18 put it lower than 2019+)."""
    zone = page.rect.height - FOOTER_ZONE
    ys = [b[1] for b, t in page_lines
          if (b[1] > zone and FOOTER.match(t)) or (t == '[OVER]' and b[1] > page.rect.height * 0.85)]
    return min(ys) - 2 if ys else page.rect.height - 25


def stop_y(page_lines, footer):
    ys = [b[1] for b, t in page_lines
          if (any(m in t for m in STOP_MARKERS) or t in STOP_LINES or BACK_COVER.search(t)) and b[1] < footer]
    return min(ys) if ys else None


def content_box(page, y0, y1):
    """Tight box around everything painted between y0 and y1 (text, lines, images)."""
    xs0, ys0, xs1, ys1 = [], [], [], []
    text_rects = [fitz.Rect(b) for b, _ in lines_of(page)]
    words = [fitz.Rect(b) for b, t in lines_of(page) if re.search(r'[A-Za-z0-9]', t)
             and not any(m in t for m in STOP_MARKERS)]
    if not any(r.y0 >= y0 - 2 and r.y1 <= y1 + 2 for r in words):
        return None                      # rules, a frame or a header bar, but no question text
    # 2019+ answerbook pages carry a scanning barcode (a thin image) just above the footer.
    barcodes = [r for r in (fitz.Rect(i['bbox']) for i in page.get_image_info())
                if r.height < 25 and r.width > 3 * r.height and r.y0 > page.rect.height - 130]
    rects = text_rects + [d['rect'] for d in page.get_drawings()] + \
        [fitz.Rect(i['bbox']) for i in page.get_image_info() if fitz.Rect(i['bbox']) not in barcodes]
    for r in rects:
        if r.is_empty and not (r.width or r.height):
            continue
        if r.y1 <= y0 or r.y0 >= y1 or r.width > page.rect.width * 0.98:
            continue
        xs0.append(r.x0); ys0.append(max(r.y0, y0)); xs1.append(r.x1); ys1.append(min(r.y1, y1))
    if not ys0:
        return None
    # Padding never reaches past the segment, so it can't pick up the edge of the next
    # question or a footer mark like "[OVER]".
    return fitz.Rect(max(min(xs0) - PAD, 0), max(min(ys0) - PAD, y0 - 3, 0),
                     min(max(xs1) + PAD, page.rect.width), min(max(ys1) + PAD, y1, page.rect.height))


# History (Later Modern paper only): Section 1 is the documents-based question (q1), then each
# topic block is one question: Ireland topic N -> q(1+N), Europe topic N -> q(7+N). Headers are
# centred and can be split into several spans on one row. The DBQ's own topic is not set again
# in Section 2/3, so a paper has 12 or 13 questions.
HIST_SECTION = re.compile(r'^SECTION\s*(\d)\s*:')
HIST_TOPIC = re.compile(r'^(?:Later Modern\s+)?(Ireland|Europe and the wider world)\s*:?\s*Topic\s*(\d)\s*$', re.I)
# 2023-25 Ordinary papers add a Part A for the DBQ's own topic, for candidates on that year's
# alternative instructions; it takes the DBQ topic's otherwise unused question number.
HIST_ALTERNATIVE = re.compile(r'^Answer the questions below if you are following the Alternative', re.I)
# Topic titles decide the topic number (the 2010 OL paper prints "Topic 5" over Topic 6's title).
HIST_TITLES = {('IRL', 'Ireland and the Union'): 1, ('IRL', 'Movements for political'): 2,
               ('IRL', 'The pursuit of sovereignty'): 3, ('IRL', 'The Irish diaspora'): 4,
               ('IRL', 'Politics and society in Northern'): 5, ('IRL', 'Government, economy and society'): 6,
               ('EUR', 'Nationalism and state formation'): 1, ('EUR', 'Nation states and international'): 2,
               ('EUR', 'Dictatorship and democracy'): 3, ('EUR', 'Division and realignment'): 4,
               ('EUR', 'European retreat from empire'): 5, ('EUR', 'The United States and the world'): 6}
HIST_RUNNING = re.compile(r'^History\s*[–-]\s*Later Modern|^Leaving Certificate Examination|^\d{1,2}$')


def rows_of(page):
    """lines_of, with spans that share a baseline joined left to right."""
    out = []
    for b, t in lines_of(page):
        if out and abs(out[-1][0][1] - b[1]) < 4:
            pb, pt = out[-1]
            out[-1] = ((min(pb[0], b[0]), min(pb[1], b[1]), max(pb[2], b[2]), max(pb[3], b[3])),
                       f'{pt} {t}' if b[0] >= pb[0] else f'{t} {pt}')
        else:
            out.append((b, t))
    return [(b, re.sub(r'\s+', ' ', t)) for b, t in out]


def find_history(paper):
    doc = fitz.open(paper_pdf(SUBJECT, paper))
    questions, current, section, dbq_topic = [], None, None, None
    for pno, page in enumerate(doc):
        if pno == 0:
            continue                     # cover page
        rows = rows_of(page)
        footer = footer_y(page, rows)
        stop = stop_y(rows, footer)
        limit = min(stop if stop is not None else footer, footer)
        # the running head ("Leaving Certificate Examination 2025 / 4 / History – Later Modern –
        # Higher Level") is not part of any question
        head = [b[3] for b, t in rows if b[1] < 110 and HIST_RUNNING.match(t)]
        cursor = max(head) + 2 if head else TOP_Y
        for (x0, y0, x1, y1), text in rows:
            if y0 >= limit or y0 < cursor:
                continue
            s, t = HIST_SECTION.match(text), HIST_TOPIC.match(text)
            if t and section == 1 and dbq_topic is None:
                dbq_topic = t
            alt = HIST_ALTERNATIVE.match(text) and dbq_topic is not None
            if alt:
                t = dbq_topic
            if s:
                if current is not None:
                    current['segments'].append((pno, cursor, y0 - 3))
                    questions.append(current)
                    current = None
                section = int(s.group(1))
                if section == 1:
                    current = {'number': 1, 'section': 'DBQ', 'segments': []}
                cursor = y0 - 3 if section == 1 else y1 + 1
            elif t and section in (2, 3):
                if current is not None:
                    current['segments'].append((pno, cursor, y0 - 3))
                    questions.append(current)
                europe = t.group(1)[0] in 'Ee'
                topic = int(t.group(2))
                if not alt:
                    after = [r for b, r in rows if b[1] > y0 + 2][:1]
                    titled = [n for (sec, title), n in HIST_TITLES.items()
                              if sec == ('EUR' if europe else 'IRL') and after and after[0].lower().startswith(title.lower())]
                    if titled and titled[0] != topic:
                        print(f'  {paper} p{pno + 1}: printed Topic {topic}, title is Topic {titled[0]}')
                        topic = titled[0]
                current = {'number': (7 if europe else 1) + topic,
                           'section': 'EUR' if europe else 'IRL', 'segments': [],
                           **({'alternative': True} if alt else {})}
                cursor = y0 - 3
        if current is not None:
            current['segments'].append((pno, cursor, limit))
            if stop is not None:
                questions.append(current)
                current = None
    if current is not None:
        questions.append(current)
    return doc, questions


def find_questions(paper):
    """Return [{number, section, segments: [(page_index, y0, y1)]}] for one paper file."""
    if SUBJECT == 'history':
        return find_history(paper)
    doc = fitz.open(paper_pdf(SUBJECT, paper))
    anchor = HEADED if SUBJECT == 'pe' else ANCHOR
    margins = [min((b[0] for b, t in lines_of(page) if b[0] < 80 and (m := ANCHOR.match(t)) and m.group(2)),
                   default=None) for page in doc]
    doc_margin = min((m for m in margins if m is not None), default=57)
    questions, current, section, last = [], None, None, 0
    part_two = paper.endswith('-P2')
    for pno, page in enumerate(doc):
        lines = lines_of(page)
        # Question numbers hang at the page's left margin (37-57pt depending on the year and
        # page); numbered sub-items are indented ~28pt further, so a page holding only those
        # falls back to the paper's margin.
        margin = margins[pno] if margins[pno] is not None and margins[pno] <= doc_margin + 20 else doc_margin
        pictures = [fitz.Rect(i['bbox']) for i in page.get_image_info()]
        footer = footer_y(page, lines)
        stop = stop_y(lines, footer)
        limit = min(stop if stop is not None else footer, footer)
        events = []
        for (x0, y0, _, _), text in lines:
            if y0 >= limit:
                continue
            s = SECTION.match(text)
            if s and x0 < 300:
                events.append((y0, 'section', s.group(1)))
            if SUBJECT == 'geography' and GEO_BREAK.match(text):
                if not events or events[-1][1] != 'section':
                    events.append((y0, 'section', None))
                continue
            if SUBJECT == 'geography':
                if x0 > margin + ANCHOR_SLACK:
                    continue
                h, a = HEADED.match(text), ANCHOR.match(text)
                num = None
                if h:
                    part_two, num = True, GEO_PART_TWO + int(h.group(1))
                elif a and a.group(2):
                    n = int(a.group(1))
                    # inside Part Two a bare "3." is a list item; only the options (13-24) count
                    num = (GEO_PART_TWO + n if n >= 13 else None) if part_two else n
                if num is not None:
                    events.append((y0, 'anchor', num))
                    last = max(last, num)
                continue
            a = anchor.match(text)
            # A number with no full stop only counts if it is the next question (the 2022 OL
            # paper prints "12" without one); otherwise it is a table value or a label.
            if a and x0 <= margin + ANCHOR_SLACK and (a.group(2) or int(a.group(1)) == last + 1):
                events.append((y0, 'anchor', int(a.group(1))))
                last = max(last, int(a.group(1)))
        cursor = TOP_Y
        for y, kind, value in events:
            if kind == 'section':
                if current is not None:
                    current['segments'].append((pno, cursor, y))
                    questions.append(current)
                    current = None
                section = value
                cursor = y
                if value in PREAMBLE_SECTIONS.get(SUBJECT, ()):
                    current = {'number': None, 'section': section, 'segments': []}
                continue
            # A figure printed beside a question's first lines can start above its number;
            # move the boundary up so the figure goes with the question it belongs to.
            cut = min([r.y0 - 3 for r in pictures if r.y0 < y - 3 < r.y1 and r.y0 > cursor] + [y - 3])
            if current is not None and current['number'] is None:
                current['number'] = value    # the case study runs straight on into its question
                continue
            if current is not None:
                current['segments'].append((pno, cursor, cut))
                questions.append(current)
            current = {'number': value, 'section': section, 'segments': []}
            cursor = cut + 3 if cut < y - 3 else y
        if current is not None:
            current['segments'].append((pno, cursor, limit))
        if stop is not None and current is not None:
            questions.append(current)
            current = None
    if current is not None:
        questions.append(current)
    # A question number only counts once, in increasing order (rejects stray "2." list items).
    seen, clean = set(), []
    for q in questions:
        if q['number'] in seen or (clean and q['number'] < clean[-1]['number']):
            if clean:
                clean[-1]['segments'].extend(q['segments'])
            continue
        seen.add(q['number'])
        clean.append(q)
    for q in clean:                      # rejoin pieces of one page split at a stray number
        merged = []
        for seg in q['segments']:
            if merged and merged[-1][0] == seg[0] and seg[1] - merged[-1][2] <= 4:
                merged[-1] = (seg[0], merged[-1][1], seg[2])
            else:
                merged.append(seg)
        q['segments'] = merged
    return doc, clean


def render_pages(doc, paper):
    out = DATA / SUBJECT / 'pages' / paper
    out.mkdir(parents=True, exist_ok=True)
    for pno, page in enumerate(doc):
        target = out / f'p{pno + 1:02d}.png'
        if not target.exists():
            page.get_pixmap(dpi=PAGE_DPI).save(target)


def main(subject, papers):
    global SUBJECT
    SUBJECT = subject
    manifest_path = DATA / subject / 'crops.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    overrides_path = DATA / subject / 'crop-overrides.json'
    overrides = json.loads(overrides_path.read_text()) if overrides_path.exists() else {}
    (DATA / subject / 'text').mkdir(parents=True, exist_ok=True)

    for paper in papers:
        year, level = paper.split('-')[:2]
        doc, questions = find_questions(paper)
        # a question the detector missed can be supplied entirely by an override
        found = {q['number'] for q in questions}
        for okey in overrides:
            oy, ol, oq = okey.split('-')[:3]
            if (oy, ol) == (year, level) and int(oq[1:]) not in found:
                questions.append({'number': int(oq[1:]), 'section': None, 'segments': []})
        questions.sort(key=lambda q: q['number'])
        render_pages(doc, paper)
        img_dir = ROOT / 'exam-images' / subject / year
        img_dir.mkdir(parents=True, exist_ok=True)
        for q in questions:
            key = f'{year}-{level}-q{q["number"]}'
            segments = [{'paper': paper, 'page': p + 1, 'y0': round(a, 1), 'y1': round(b, 1)}
                        for p, a, b in q['segments']]
            segments = overrides.get(key, segments)
            images, text = [], []
            for k, seg in enumerate(segments, 1):
                page = fitz.open(paper_pdf(subject, seg['paper']))[seg['page'] - 1]
                box = content_box(page, seg['y0'], seg['y1'])
                if box is None or box.height < 2 * PAD + 14:
                    continue
                seg['box'] = [round(v, 1) for v in box]
                name = f'{level}-q{q["number"]}-{len(images) + 1}.webp'
                pix = page.get_pixmap(matrix=fitz.Matrix(CROP_ZOOM, CROP_ZOOM), clip=box)
                pix.pil_save(img_dir / name, format='WEBP', quality=82, method=6)
                images.append(f'exam-images/{subject}/{year}/{name}')
                text.append(page.get_text(clip=box))
            (DATA / subject / 'text' / f'{key}.txt').write_text('\n'.join(text))
            section = geo_section(q['number']) if subject == 'geography' else q['section']
            manifest[key] = {'year': int(year), 'level': level, 'paper': paper,
                             'number': q['number'], 'section': section,
                             'segments': segments, 'images': images,
                             **({'alternative': True} if q.get('alternative') else {})}
            print(f'{key:22} sec {q["section"]}  pages {[s["page"] for s in segments]}  '
                  f'{len(images)} image(s)')
    manifest_path.write_text(json.dumps(manifest, indent=1))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
