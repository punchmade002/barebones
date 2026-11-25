import json, os, re

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-53.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out'
G = 'geo-option-geoecology-'

def mp(k, *ids):
    return {"k": k, "of": [G + i for i in ids]}

# Marking points per question, per part. Comments give the model-answer sentence.
DATA = {
 "geography-pp-2020-higher-q116": {
  "16": [
   mp(1, 's3.1.0'),                 # overcropping definition
   mp(1, 's3.1.1'),                 # nutrients removed faster, humus falls
   mp(2, 's3.1.1', 's3.1.2'),       # crumb breakdown; dusty/compacted, less water
   mp(1, 's3.1.3'),                 # monoculture same nutrients, pests
   mp(2, 's3.2.0', 's3.2.1'),       # 1930s Great Plains ploughed for wheat
   mp(1, 's3.2.2'),                 # drought, dust storms, families left
   mp(1, 's3.2.4'),                 # Soil Conservation Service 1935, measures
   mp(2, 's3.3.0', 's3.3.1'),       # overgrazing definition + exposure
   mp(1, 's3.3.2'),                 # trampling compacts, poaching, runoff
   mp(1, 's3.4.0'),                 # EU headage payments, sheep rise
   mp(2, 's3.4.2', 's3.4.3'),       # heather/peat stripped, silt harms salmon
   mp(2, 's3.8.0', 's3.8.3'),       # Sahel livestock/fallow/fuelwood + drought
   mp(2, 's3.6.0', 's3.6.4'),       # desertification: topsoil loss, falling yields, migration
   mp(1, 's3.9.1'),                 # Lake Chad shrinkage
   mp(1, 's3.15.0'),                # contour ploughing
   mp(1, 's3.15.1'),                # terracing, Banaue
   mp(1, 's3.15.3'),                # shelter belts
   mp(1, 's3.16.0'),                # rotation, fallow, cover crops, clover
   mp(2, 's3.12.0', 's3.12.1'),     # Niger FMNR, 5 million ha
   mp(2, 's3.11.0', 's3.11.1'),     # Yatenga zai pits
   mp(1, 's3.12.2'),                # trees shade, wind, Faidherbia nitrogen
   mp(2, 's3.19.0', 's3.19.1'),     # liming; drainage improves gleys
   mp(1, 's3.19.1'),                # Arterial Drainage Act 1945
   mp(1, 's3.19.4'),                # Aran Islands soil building
   mp(2, 's3.23.0', 's3.23.3'),     # BurrenLIFE; pay by results scoring
   mp(2, 's3.26.0', 's3.26.1'),     # Iceland 1907 service; fencing, lyme grass
   mp(2, 's3.26.4', 's3.26.5'),     # Farmers Heal the Land 1990; sheep fall
   mp(2, 's3.24.3', 's3.26.6'),     # Iceland sheep prevented regrowth; both sides
  ],
 },
 "geography-pp-2020-higher-q117": {
  "17": [
   mp(1, 's2.16.0'),                # most widespread lowland soil
   mp(1, 's2.16.1'),                # Golden Vale, south-east
   mp(2, 's2.16.3', 's2.16.4'),     # mild wet climate; rainfall 750-1000 mm east
   mp(1, 's2.16.3'),                # deciduous woodland after Ice Age
   mp(2, 's1.2.0', 's2.16.5'),      # glacial till, glaciation ended 10,000 yrs ago
   mp(1, 's2.16.6'),                # mild leaching carries iron and clay down
   mp(1, 's2.17.b'),                # earthworms mix, no bleached layer
   mp(1, 's2.17.0'),                # O horizon
   mp(1, 's2.17.1'),                # A horizon
   mp(1, 's2.17.2'),                # B horizon
   mp(1, 's2.17.2'),               # gradual A-B boundary (earthworms)
   mp(1, 's2.17.3'),                # C horizon
   mp(2, 's2.17.4', 's2.5.3'),      # no bleached E; mild leaching not podzol
   mp(1, 's1.16.1'),                # brown colour from humus and iron
   mp(1, 's1.4.0'),                 # good loam composition
   mp(1, 's1.5.0'),                 # mineral matter
   mp(1, 's1.5.1'),                 # mineral matter releases nutrients
   mp(2, 's1.6.0', 's1.6.1'),       # organic matter; decomposers to humus
   mp(2, 's1.7.0', 's1.6.2'),       # mull humus; humus binds, holds nutrients
   mp(1, 's1.6.3'),                 # earthworms mix and aerate
   mp(2, 's1.4.2', 's1.13.2'),      # water and air share pores; drains, holds moisture
   mp(1, 's1.13.2'),                # loamy texture
   mp(2, 's1.14.0', 's1.11.0'),     # crumb structure, pores for air and water
   mp(1, 's2.16.5'),                # slightly acidic pH 5.5-6.5
   mp(1, 's1.20.0'),                # clay-humus complex holds nutrients
   mp(1, 's2.17.6'),                # uses in Golden Vale and south-east
   mp(2, 's1.19.4', 's1.19.5'),     # Teagasc pH targets; farmers spread lime
   mp(1, 's2.16.2'),                # grey-brown podzolics, east Midlands
  ],
 },
 "geography-pp-2020-higher-q118": {
  "18": [
   mp(1, 's4.18.0'),                # 26-28 C all year
   mp(1, 's4.18.1'),                # annual range 2-3 C
   mp(1, 's4.19.0'),                # over 2000 mm, Manaus 2300 mm
   mp(1, 's4.19.b', 's4.19.0'),     # rain every month, no dry season
   mp(2, 's4.19.1', 's4.19.2'),     # morning heating, cumulonimbus build-up
   mp(1, 's4.19.3'),                # afternoon thunderstorms daily
   mp(1, 's4.19.4'),                # ITCZ drives convectional rain
   mp(1, 's4.19.5'),                # humidity over 80%
   mp(1, 's4.19.6'),                # evapotranspiration recycling
   mp(1, 's4.20.0'),                # latosols deep
   mp(1, 's4.20.0'),                # heavy rain leaches silica and bases (laterisation)
   mp(1, 's4.20.0'),                # iron and aluminium left, red or yellow
   mp(1, 's4.20.0'),                # acidic, infertile
   mp(2, 's4.20.1', 's4.20.0'),     # litter decomposes fast, little humus
   mp(1, 's4.20.2'),                # shallow roots and mycorrhiza
   mp(1, 's4.20.3'),                # nutrients held in vegetation, closed cycle
   mp(1, 's4.24.4'),                # clearing loses nutrients stored in species
   mp(2, 's4.17.0', 's4.22.5'),     # dense evergreen broadleaved; leaves all year
   mp(1, 's4.24.0'),                # hundreds of species per hectare
   mp(1, 's4.21.0'),                # emergents 45-60 m
   mp(1, 's4.21.1'),                # canopy 25-40 m, intercepts light and rain
   mp(1, 's4.21.4'),                # 2 per cent light on forest floor
   mp(1, 's4.22.3'),                # large understorey leaves
   mp(1, 's4.22.2'),                # drip tips and waxy leaves
   mp(2, 's4.22.0', 's4.22.1'),     # buttress roots, shallow roots near surface
   mp(2, 's4.23.0', 's4.23.1'),     # lianas and epiphytes
  ],
 },
}

def candidates(block):
    ids = set()
    in_c = False
    for line in block.splitlines():
        if line.startswith('CANDIDATES'):
            in_c = True
            continue
        if in_c:
            m = re.match(r'^\[([^\]]+)\]', line)
            if m:
                ids.add(m.group(1))
    return ids

def labels(block):
    return re.findall(r'^PART "([^"]+)"', block, flags=re.M)

text = open(BATCH, encoding='utf-8').read()
blocks = text.split('\n====')
qblocks = {}
for b in blocks:
    m = re.search(r'^QUESTION (\S+)', b, flags=re.M)
    if m:
        qblocks[m.group(1)] = b

os.makedirs(OUT, exist_ok=True)
ok = True
for qid, parts in DATA.items():
    block = qblocks[qid]
    cands = candidates(block)
    labs = labels(block)
    assert set(parts.keys()) == set(labs) and len(labs) == len(parts), (qid, labs, list(parts))
    for lab, pts in parts.items():
        for p in pts:
            assert 1 <= p['k'] <= len(p['of']), (qid, lab, p)
            for i in p['of']:
                assert i[len(G):] in {c[len(G):] for c in cands if c.startswith(G)} , (qid, lab, i)
    out = {lab: parts[lab] for lab in labs}
    path = os.path.join(OUT, qid + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False)
    # re-read check
    with open(path, encoding='utf-8') as f:
        chk = json.load(f)
    assert list(chk.keys()) == labs
    total = sum(len(v) for v in chk.values())
    empty = [k for k, v in chk.items() if not v]
    print(qid, 'parts=', len(chk), 'points=', total, 'empty=', empty)
