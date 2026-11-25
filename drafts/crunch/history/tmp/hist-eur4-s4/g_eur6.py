import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,st,w,c='high'): return {"id":i,"strength":st,"why":w,"confidence":c}
# (id suffix, cost, links)
rows=[
('0.b',1,[L('hist-eur6-s6.0.4','helpful','pent-up demand after the war')]),
('0.0',2,[]),('0.1',1,[]),('0.2',1,[]),('0.3',1,[]),('0.4',1,[]),
('0.5',1,[L('hist-eur6-s6.2.2','helpful','federal defence spending bringing jobs')]),
('0.6',1,[]),('0.7',1,[]),
('1.b',1,[L('hist-eur6-s6.0.6','helpful','GI Bill home loans, federal mortgages','low')]),
('1.0',1,[L('hist-eur6-s6.0.5','helpful','the GI Bill'),L('hist-eur6-s6.0.4','helpful','pent-up demand')]),
('1.1',2,[]),('1.2',1,[]),
('1.3',1,[L('hist-eur6-s6.0.5','helpful','veterans loan guarantees under GI Bill','low')]),
('1.4',2,[]),
('1.5',1,[L('hist-eur6-s6.2.0','helpful','Interstate highway system','low')]),
('1.6',1,[]),('1.7',2,[]),
('2.b',1,[]),('2.0',2,[]),('2.1',1,[]),('2.2',1,[]),('2.3',1,[]),('2.4',1,[]),('2.5',1,[]),('2.6',1,[]),('2.7',1,[]),
('3.b',1,[]),('3.0',1,[]),('3.1',1,[]),('3.2',1,[]),('3.3',1,[]),('3.4',1,[]),
('4.b',1,[]),('4.0',1,[]),('4.1',1,[]),('4.2',1,[]),('4.3',1,[]),('4.4',1,[]),('4.5',1,[]),
('5.b',1,[]),('5.0',1,[]),('5.1',1,[]),('5.2',1,[]),('5.3',1,[]),('5.4',1,[]),('5.5',2,[]),('5.6',1,[]),
('6.b',1,[]),('6.0',1,[]),('6.1',1,[]),('6.2',1,[]),('6.3',1,[]),('6.4',2,[]),('6.5',2,[]),('6.6',1,[]),('6.7',2,[]),
('7.b',1,[]),('7.0',1,[]),('7.1',2,[]),('7.2',1,[]),('7.3',2,[]),('7.4',1,[]),('7.5',1,[]),('7.6',1,[]),
('8.b',1,[]),('8.0',1,[]),('8.1',1,[]),('8.2',1,[]),('8.3',1,[]),
('8.4',2,[L('hist-eur6-s6.8.4','helpful','Galbraith, private affluence public squalor'),L('hist-eur6-s6.4.1','helpful','Whyte on conformity')]),
('8.5',1,[]),
]
out={'hist-eur6-s8.'+r[0]:{"cost":r[1],"needs":r[2]} for r in rows}
txt=open(D+'packs/hist-eur6-s8.t1g1.txt').read()
tg=re.findall(r'^\[(hist-eur6-s8\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert tg==list(out),(set(tg)^set(out))
for v in out.values():
    for n in v['needs']: assert n['id'] in allids and n['id'] not in tg
json.dump(out,open(D+'point-links/hist-eur6-s8.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
