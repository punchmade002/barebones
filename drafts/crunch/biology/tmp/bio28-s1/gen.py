import json, re
P = '/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
E, H = 'essential', 'helpful'
def L(i, s, w, c='high'): return {"id": i, "strength": s, "why": w, "confidence": c}
S = 'bio28-s1.'
spec = {
'0.b': (1, []),
'0.0': (1, [L('bio15-s1.1.0', H, 'aerobic respiration uses oxygen')]),
'0.1': (1, []),
'0.2': (1, [L('bio15-s1.0.0', H, 'respiration definition')]),
'0.3': (2, [L('bio25-s1.1.0', H, 'diffusion as transport')]),
'0.4': (1, [L(S+'0.3', E, 'why diffusion alone is not enough')]),
'1.b': (1, []), '1.0': (1, []),
'1.1': (1, [L(S+'1.0', E, 'nose filters, warms, moistens')]),
'1.2': (1, []),
'1.3': (1, [L(S+'1.2', H, 'pharynx shared by air and food')]),
'1.4': (1, [L(S+'1.3', E, 'epiglottis closes airway')]),
'1.5': (1, []),
'2.b': (1, []),
'2.0': (1, [L(S+'4.0', H, 'pressure falls in inhalation', 'low')]),
'2.1': (1, [L(S+'2.0', E, 'C-shaped cartilage rings')]),
'2.2': (2, [L(S+'2.4', H, 'bronchi')]),
'2.3': (1, [L(S+'2.2', E, 'ciliated, mucus-secreting lining')]),
'2.4': (1, [L(S+'2.0', H, 'trachea')]),
'2.5': (2, [L(S+'2.4', E, 'bronchi branching')]),
'2.6': (1, [L(S+'2.5', E, 'bronchioles end in alveoli')]),
'3.b': (1, []), '3.0': (2, []), '3.1': (1, []),
'3.2': (1, [L(S+'3.1', E, 'pleural fluid between membranes')]),
'3.3': (1, []),
'3.4': (1, [L(S+'3.0', H, 'rib cage')]),
'3.5': (2, [L(S+'2.6', H, 'alveoli wrapped in capillaries')]),
'4.b': (1, []),
'4.0': (2, [L(S+'3.2', H, 'lungs follow thorax')]),
'4.1': (1, [L(S+'4.0', E, 'pressure and volume principle')]),
'4.2': (1, [L(S+'7.0', H, 'brain controls breathing muscles', 'low')]),
'4.3': (1, [L(S+'3.3', E, 'diaphragm')]),
'4.4': (1, [L(S+'3.4', E, 'intercostal muscles')]),
'4.5': (1, []),
'4.6': (1, [L(S+'4.0', E, 'pressure fall draws air in')]),
'4.7': (1, [L('bio15-s1.0.4', H, 'ATP powers muscle contraction')]),
'5.b': (1, []),
'5.0': (2, [L(S+'4.3', H, 'diaphragm and intercostal action')]),
'5.1': (1, [L(S+'3.3', H, 'diaphragm dome')]),
'5.2': (1, [L(S+'9.5', H, 'elastic recoil', 'low')]),
'5.3': (1, [L(S+'4.1', E, 'volume change alters pressure')]),
'5.4': (1, []),
'5.5': (2, [L(S+'3.4', E, 'intercostal muscles')]),
'5.6': (1, [L(S+'5.0', H, 'passive exhalation contrast')]),
'6.b': (1, []),
'6.0': (1, [L(S+'4.3', E, 'diaphragm in inhalation')]),
'6.1': (1, [L(S+'4.4', E, 'external intercostals in inhalation')]),
'6.2': (2, [L(S+'4.0', E, 'volume and pressure principle')]),
'6.3': (1, [L(S+'5.0', H, 'passive exhalation')]),
'6.4': (1, [L(S+'4.0', E, 'volume and pressure principle')]),
'6.5': (1, [L(S+'3.5', H, 'breathing system labels', 'low')]),
'7.b': (1, []), '7.0': (1, []),
'7.1': (1, [L(S+'7.0', H, 'automatic control contrast')]),
'7.2': (2, [L(S+'7.0', E, 'breathing centre'), L('bio15-s1.1.0', H, 'respiration produces CO2')]),
'7.3': (1, [L(S+'7.2', E, 'CO2 controls breathing')]),
'7.4': (1, []),
'7.5': (1, [L(S+'7.4', E, 'rate and tidal volume')]),
'8.b': (1, []),
'8.0': (2, [L('bio25-s1.1.0', E, 'diffusion down concentration gradient')]),
'8.1': (1, [L(S+'8.0', E, 'diffusion across alveolus')]),
'8.2': (2, [L(S+'8.0', E, 'diffusion across alveolus'), L(S+'9.2', H, 'moist lining dissolves gas')]),
'8.3': (1, [L(S+'8.0', E, 'diffusion across alveolus')]),
'8.4': (1, [L(S+'8.2', H, 'oxygenated blood leaving lungs')]),
'8.5': (1, [L('bio25-s1.1.6', E, 'steep gradient speeds diffusion')]),
'8.6': (1, [L('bio25-s1.1.7', H, 'blood flow keeps gradient steep')]),
'9.b': (1, []),
'9.0': (1, [L('bio25-s1.1.6', H, 'larger surface area speeds diffusion')]),
'9.1': (1, [L('bio25-s1.1.6', H, 'shorter distance speeds diffusion')]),
'9.2': (1, [L(S+'8.2', H, 'oxygen dissolves in moisture')]),
'9.3': (1, [L(S+'8.6', E, 'blood flow steepens gradient')]),
'9.4': (1, [L('bio29-s5.3.2', H, 'narrow capillary lumen')]),
'9.5': (1, [L(S+'5.2', H, 'elastic recoil')]),
'9.6': (2, [L(S+'8.2', H, 'oxygen moves into blood')]),
'10.b': (1, []), '10.0': (1, []),
'10.1': (1, [L(S+'10.0', H, 'compare with inhaled air')]),
'10.2': (1, []),
'10.3': (1, [L(S+'10.1', E, 'oxygen content of exhaled air')]),
'10.4': (1, [L(S+'10.1', E, 'CO2 content of exhaled air')]),
'11.b': (1, []),
'11.0': (2, [L(S+'2.2', E, 'cilia and mucus lining')]),
'11.1': (2, [L(S+'9.0', E, 'large alveolar surface area')]),
'11.2': (1, [L(S+'8.2', H, 'haemoglobin carries oxygen')]),
'11.3': (2, [L(S+'2.5', E, 'bronchiole smooth muscle')]),
}
txt = open(P+'points/bio28-s1.txt').read()
tgt, cand = txt.split('\nCANDIDATES', 1)
tids = re.findall(r'^\[([^\]]+)\]', tgt, re.M)
allids = set(tids) | set(re.findall(r'^\[([^\]]+)\]', cand, re.M))
out = {}
for t in tids:
    c, n = spec[t.replace(S, '')]
    out[t] = {"cost": c, "needs": n}
assert set(spec) == {t.replace(S, '') for t in tids}
for t, v in out.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id'] != t, (t, n)
json.dump(out, open(P+'point-links/bio28-s1.json', 'w'), indent=1)
d = json.load(open(P+'point-links/bio28-s1.json'))
links = [n for v in d.values() for n in v['needs']]
print(len(d), len(links), sum(v['cost'] == 2 for v in d.values()), sum(n['confidence'] == 'low' for n in links))
