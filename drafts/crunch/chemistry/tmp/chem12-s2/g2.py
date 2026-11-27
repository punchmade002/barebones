import json, re
P = '/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i, s, w, c='high'): return {'id': i, 'strength': s, 'why': w, 'confidence': c}
E, H = 'essential', 'helpful'
d = {
 '4.b': [L('chem18-s1.1.0', H, 'chemical equilibrium')],
 '4.1': [L('chem18-s1.0.1', H, 'reversible reaction sign')],
 '5.0': [L('chem18-s1.0.1', H, 'reversible reaction sign')],
 '7.0': [L('chem8-s2.2.3', E, 'standard solution')],
 '7.2': [L('chem8-s2.5.2', E, 'NaOH is not a primary standard'), L('chem8-s2.4.0', H, 'primary standard')],
 '8.0': [L('chem8-s2.8.2', H, 'diluting with pipette and flask')],
 '8.5': [L('chem8-s2.7.1', H, 'volumetric flask diagram')],
 '10.b': [L('chem8-s2.10.2', H, '%w/v')],
 '10.1': [L('chem8-s2.2.1', E, 'n = c x V')],
 '10.2': [L('chem8-s2.2.1', E, 'c = n / V')],
 '10.3': [L('chem8-s2.8.0', E, 'dilution keeps moles of solute')],
 '10.4': [L('chem8-s2.11.0', E, 'mol/L to g/L')],
 '10.5': [L('chem8-s2.11.2', E, 'g/L to %w/v')],
}
txt = open(P + 'packs/chem12-s2.t1g2.txt').read()
allids = set(re.findall(r'^\[([^\]]+)\]', txt, re.M))
tg = txt.split('CANDIDATES')[0]
tgt = re.findall(r'^\[([^\]]+)\]', tg, re.M)
o = {}
for k in tgt:
    n = d.get(k.replace('chem12-s2.', ''), [])
    for x in n: assert x['id'] in allids and x['id'] != k
    o[k] = {'needs': n}
json.dump(o, open(P + 'point-links/chem12-s2.t1g2.json', 'w'), ensure_ascii=False, indent=1)
j = json.load(open(P + 'point-links/chem12-s2.t1g2.json'))
print(len(j), sum(len(v['needs']) for v in j.values()), 0, sum(n['confidence'] == 'low' for v in j.values() for n in v['needs']))
