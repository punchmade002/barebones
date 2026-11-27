import json, re
P = '/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i, s, w, c='high'): return {'id': 'chem1-s2.'+i, 'strength': s, 'why': w, 'confidence': c}
E, H = 'essential', 'helpful'
ids = ['0.b','0.0','0.1','0.2','1.b','1.0','1.1','1.2','2.b','2.0','2.1','2.2','2.3','3.b','3.0','3.1','3.2','3.3','3.4','3.5','3.6','4.b','4.0','4.1','4.2','5.b','5.0','5.1','5.2','5.3','6.b','6.0','6.1','6.2','7.b','7.0','7.1','7.2','7.3','7.4','7.5','8.b','8.0','8.1','8.2','8.3','8.4','8.5']
cost = {i: 1 for i in ids}
for i in ['1.2','2.1','5.2']: cost[i] = 2
d = {
 '1.0': [L('0.2', H, 'results published in journals')],
 '1.1': [L('1.0', H, 'evidence others can examine')],
 '1.2': [L('2.1', H, 'SI units')],
 '2.2': [L('2.1', H, 'SI base units')],
 '3.3': [L('3.0', H, 'what peer review is')],
 '3.5': [L('3.0', E, 'what peer review is')],
 '3.6': [L('4.1', H, 'reproducing results', 'low')],
 '4.2': [L('4.1', E, 'reproducible results')],
 '6.2': [L('6.0', E, 'primary data'), L('6.1', E, 'secondary data')],
 '7.0': [L('3.0', E, 'peer review')],
 '7.4': [L('7.0', H, 'compare source reliability', 'low')],
 '8.3': [L('7.5', H, 'sources written to sell or persuade')],
}
txt = open(P + 'packs/chem1-s2.t1g1.txt').read()
allids = set(re.findall(r'^\[([^\]]+)\]', txt, re.M))
tgt = re.findall(r'^\[([^\]]+)\]', txt, re.M)
assert [t.replace('chem1-s2.', '') for t in tgt] == ids, 'ids'
o = {}
for k in tgt:
    s = k.replace('chem1-s2.', '')
    n = d.get(s, [])
    for x in n: assert x['id'] in allids and x['id'] != k, x
    o[k] = {'cost': cost[s], 'needs': n}
json.dump(o, open(P + 'point-links/chem1-s2.t1g1.json', 'w'), ensure_ascii=False, indent=1)
j = json.load(open(P + 'point-links/chem1-s2.t1g1.json'))
print(len(j), sum(len(v['needs']) for v in j.values()), sum(v['cost'] == 2 for v in j.values()), sum(n['confidence'] == 'low' for v in j.values() for n in v['needs']))
