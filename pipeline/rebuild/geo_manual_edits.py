"""Hand corrections to Geography fill answers, applied after fill_collect / geo_thirty_collect.

    python3 pipeline/rebuild/geo_manual_edits.py

Each edit is (fill file, part id, old text, new text). The old text must occur in the answer, or the
script stops; edited answers keep their 'by' and gain 'edited': true. Rerun after any re-collect.
These are slips the long-answer checker caught in one answer and that recur, unchecked or missed,
in others (grep-found, Nov 2026).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fill_packages import BASE  # noqa: E402

FILL = BASE / 'geography' / 'fill'

KURD_OLD = 'banned Kurdish in public life and broadcasting until the early 1990s'
KURD_NEW = 'banned Kurdish in public life until 1991 and in broadcasting until the early 2000s'
BIRTH_OLD = 'Natural increase adds to the population, because birth rates are high and death rates have fallen.'
BIRTH_NEW = 'Natural increase adds to the population, because many of the migrants are young adults who start families in the city.'

EDITS = [
    # Mary Manning refused to handle South African grapefruit (Outspan), not grapes
    ('long.json', '2020-higher-q115|15', 'South African grapes', 'South African grapefruit'),
    ('long.json', '2023-higher-q115|15', 'South African grapes', 'South African grapefruit'),
    ('long.json', '2025-higher-q113|13', 'South African grapes', 'South African grapefruit'),
    # Switzerland had 22 cantons in 1848; 26 only after Jura (1979)
    ('long.json', '2026-higher-q121|21', 'created the modern federal state of 26 cantons',
     'created the modern federal state, now of 26 cantons,'),
    # Banaue terraces: the 2,000-year age is disputed
    ('long.json', '2024-higher-q118|18', 'which are over 2,000 years old', 'which have been farmed for centuries'),
    # Kurdish: public use allowed 1991, broadcasting only from the 2000s
    ('long.json', '2017-higher-q119|19', KURD_OLD, KURD_NEW),
    ('long.json', '2019-higher-q120|20', KURD_OLD, KURD_NEW),
    ('long.json', '2021-higher-q119|19', KURD_OLD, KURD_NEW),
    ('long.json', '2022-higher-q120|20', KURD_OLD, KURD_NEW),
    ('long.json', '2023-higher-q119|19', KURD_OLD, KURD_NEW),
    ('long.json', '2024-higher-q119|19', KURD_OLD, KURD_NEW),
    ('long.json', '2021-higher-q120|20', 'Kurdish was banned in public life and broadcasting in Turkey until the early 1990s.',
     'Kurdish was banned in public life in Turkey until 1991 and in broadcasting until the early 2000s.'),
    ('long.json', '2026-higher-q120|20', 'Turkey banned Kurdish in public life and broadcasting until the early 1990s.',
     'Turkey banned Kurdish in public life until 1991 and in broadcasting until the early 2000s.'),
    # Kolkata and Mumbai have low birth rates; growth from natural increase comes from young migrants
    ('long.json', '2019-ordinary-q111|11B', BIRTH_OLD, BIRTH_NEW),
    ('thirty.json', '2018-higher-q106|6B', BIRTH_OLD.replace(',', ''), BIRTH_NEW.replace(',', '')),
    ('long.json', '2026-ordinary-q112|12B', 'Natural increase adds to the growth because many migrants are young and birth rates are high.',
     'Natural increase adds to the growth because many migrants are young adults who start families in the city.'),
]


R = 'replace'
A = 'after'   # insert a new line after the line containing old

# The 12 30-mark essays still failing after the fix round (fill/thirty-flagged.json), fixed by hand
# from the checker's findings (Nov 2026). They ship as sonnet-thirty-manual.
FLAGGED_FIXES = {
    '2023-higher-q111|11B': [
        (R, 'The World Health Organization declared smallpox eradicated in 1980.',
         'The World Health Organization declared smallpox eradicated in 1980, which removed a major killer of children and lowered death rates.'),
        (R, 'The core areas were Punjab, Haryana and western Uttar Pradesh.',
         'Higher yields in Punjab, Haryana and western Uttar Pradesh ended the famines that had checked population growth, such as the Bengal famine of 1943.'),
        (R, 'Second impact – technology lowers birth rates:', 'Impact 2 – Technology lowers birth rates:'),
        (A, 'Desertification and drought there cause famine and an overpopulated environment.',
         'Without irrigation, fertiliser or high-yield seeds, food output cannot keep pace with population growth of about 3% a year, so famine raises death rates.'),
    ],
    '2017-higher-q106|6B': [
        (R, 'Mumbai and Pune on the west coast and Bengaluru on the southern Deccan.',
         'Mumbai on the west coast, Pune inland from it on the Deccan and Bengaluru on the southern Deccan.'),
    ],
    '2017-ordinary-q112|12B': [
        (A, 'Trade and traffic travelling between the surrounding districts passed through the town',
         'Market days and fairs drew farmers from the surrounding countryside into the town along these roads.'),
        (A, 'People settled around the castle for protection, so the town grew up under its shelter.',
         'A defended site attracted merchants and craftsmen, who felt safe to trade there.'),
    ],
    '2018-higher-q111|11B': [
        (A, 'Gently sloping, well-drained lowland with better soils',
         'Upland land is used for rough grazing and forestry, which support few people, so houses there are widely spaced.'),
        (A, 'Few roads climb the uplands, so there are few houses there.',
         'Ribbon development along roads such as the N15 north of Sligo is cheaper because road access, water and electricity are already in place.'),
    ],
    '2021-higher-q111|11B': [
        (R, 'Air pollution from vehicles and industry adds to the city\'s environmental problems.',
         'Narrow streets in the old centre were not built for the volume of modern traffic, so they jam easily.'),
        (R, 'Poor and rich districts sit side by side, as Paraisópolis favela borders the wealthy district of Morumbi.',
         'Better-off families move out to gated condominiums such as Alphaville on the edge of the metropolitan region, which spreads the city further.'),
        (R, 'Sprawling informal settlements lack piped water and sewers, which spreads disease, and the Tietê river floods in heavy summer rain.',
         'Sprawling informal settlements lack piped water and sewers, which spreads disease.'),
        (A, 'New housing on the edge of the city takes over farmland and green space',
         'Building on floodplains and steep slopes at the edge removes vegetation, so heavy summer rain brings floods and landslides to the outer districts.'),
    ],
    '2021-ordinary-q108|8C': [
        (R, 'Named developed economy – Ireland:', 'Financial services – Ireland:'),
    ],
    '2023-ordinary-q106|6C': [
        (A, 'Rich-country cotton subsidies allow surplus cotton',
         'Mali, Niger and Burkina Faso are landlocked, so their trade must cross other countries to reach a port, which raises costs.'),
    ],
    '2024-ordinary-q107|7C': [
        (A, 'Named policy – Common Agricultural Policy (CAP):', 'The CAP is the EU policy that supports farmers and rural areas.'),
        (R, 'The MacSharry reform of 1992 and the Fischler reform of 2003 decoupled payments from production, so',
         'The MacSharry reform of 1992 cut guaranteed prices and paid farmers directly instead, and the Fischler reform of 2003 decoupled payments from production, so'),
    ],
    '2025-higher-q106|6C': [
        (R, 'Heliópolis is the largest favela, so inequality is visible from one street to the next.',
         'Heliópolis, the city\'s largest favela, grew on unused land as migrants arrived faster than housing could be built.'),
    ],
    '2025-ordinary-q105|5C': [
        (R, 'Coal was replaced by oil and gas, and out-of-date plant added to the decline.',
         'Coal was replaced by oil and gas as fuels, so demand for Ruhr coal fell.\nOut-of-date plant made Ruhr steel less competitive.'),
        (R, 'This caused out-migration, as young people left for better jobs, and services fell as the population dropped.',
         'This caused out-migration, as young people left for better jobs elsewhere.\nServices such as shops and schools closed as the population fell.'),
        (R, 'Responses include clearing and cleaning land, retraining workers, and attracting new light industry and services.',
         'Rivers such as the Emscher were used as open sewers for industrial waste, which polluted the water.'),
        (R, '\nThe Zollverein coal mine complex in Essen became a UNESCO World Heritage Site in 2001 and is now a cultural centre.', ''),
    ],
    '2026-higher-q109|9C': [
        (R, 'Factor 1 – Road transport:', 'Factor 1 – Road and rail transport:'),
        (R, '\nDundalk lies on the Dublin to Belfast railway line, which carries freight and commuters.', ''),
        (A, 'The N53 links junction 17', 'Dundalk lies on the Dublin to Belfast railway line, which carries freight and commuters.'),
        (A, 'The estates lie beside the R132 and R172',
         'Grouping firms on estates lets them share services such as roads, water and power.'),
        (A, 'Shops, schools and offices in the town serve a large catchment',
         'The bus station and post offices make the town convenient for workers and visiting business people.\nThe tourist information office shows that tourism is also an economic activity in the town.'),
    ],
    '2026-higher-q112|12C': [
        (R, '\nThe industrial estate at 066 073 shows the town processes and supplies goods for this wider hinterland.',
         '\nThe town became the main market and service centre for the farms of north Louth, which helped it grow.'),
        (R, 'and many scattered farm buildings between 02 and 08 east.', 'and many scattered farm buildings on the low ground around the town.'),
        ('grid', 'J', ''),   # this answer gave grid references without the letter
    ],
}


def fix_flagged():
    import re
    tf, ff = FILL / 'thirty.json', FILL / 'thirty-flagged.json'
    thirty, flagged = json.loads(tf.read_text()), json.loads(ff.read_text())
    left = []
    for f in flagged['flagged']:
        ops = FLAGGED_FIXES.get(f.get('id'))
        if ops is None:
            left.append(f)
            continue
        m = f['model']
        for op, old, new in ops:
            if op == 'grid':
                m = re.sub(r'(?<![A-Z] )\b(\d{3} \d{3})\b', old + r' \1', m)
                continue
            if old not in m:
                sys.exit(f'{f["id"]}: text not found: {old!r}')
            if op == R:
                m = m.replace(old, new)
            else:
                lines = m.split('\n')
                k = next(i for i, line in enumerate(lines) if old in line)
                lines.insert(k + 1, new)
                m = '\n'.join(lines)
        thirty[f['id']] = {'model': m, 'by': 'sonnet-thirty-manual', 'issue': f.get('issue', '')}
    flagged['flagged'] = left
    tf.write_text(json.dumps(thirty, ensure_ascii=False, indent=1))
    ff.write_text(json.dumps(flagged, ensure_ascii=False, indent=1))
    print(f'{len(FLAGGED_FIXES)} flagged essays fixed by hand; {len(left)} still flagged')


def main():
    fix_flagged()
    files = {}
    for name, pid, old, new in EDITS:
        d = files.setdefault(name, json.loads((FILL / name).read_text()))
        a = d[pid]
        if old not in a['model']:
            if new in a['model']:
                continue
            sys.exit(f'{name} {pid}: text not found: {old!r}')
        a['model'] = a['model'].replace(old, new)
        a['edited'] = True
    for name, d in files.items():
        (FILL / name).write_text(json.dumps(d, ensure_ascii=False, indent=1))
    print(f'{len(EDITS)} edits applied to {", ".join(files)}')


if __name__ == '__main__':
    main()
