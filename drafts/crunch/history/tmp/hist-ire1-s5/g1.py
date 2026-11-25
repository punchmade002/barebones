import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-ire1-s5.'
E,H='essential','helpful'
def L(i,s,w,c='high'):
    if not i.startswith('hist-'): i=P+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
S4='hist-ire1-s4.'
d={
'0.b':(2,[]),'3.b':(1,[]),'5.b':(1,[]),'8.b':(1,[]),'12.b':(1,[]),
'0.0':(2,[]),
'0.1':(2,[]),
'0.2':(1,[L('0.1',E,'pasture economy')]),
'0.3':(1,[L(S4+'8.1',H,'cottiers died or emigrated')]),
'0.4':(1,[L('0.1',H,'pasture needed fewer hands')]),
'1.b':(1,[]),
'1.0':(1,[L('0.1',E,'rising livestock prices')]),
'1.1':(1,[L('1.0',E,'uses stronger farmers')]),
'1.2':(2,[L(S4+'8.3',H,'Encumbered Estates Act sales')]),
'1.3':(1,[L('1.2',E,'buyers at estate sales')]),
'1.4':(1,[]),
'1.5':(1,[L('1.4',H,'no legal security of tenure')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L('2.0',H,'bride with a dowry')]),
'2.2':(1,[L('2.1',H,'land and dowry in marriage')]),
'2.3':(1,[L('2.1',E,'waiting to inherit the farm')]),
'2.4':(1,[L('2.1',E,'single-heir inheritance')]),
'2.5':(1,[L('2.3',E,'late marriage and celibacy')]),
'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'3.4':(1,[L('3.3',E,'uses chain migration')]),
'3.5':(2,[L('3.2',H,'who emigrated')]),
'4.b':(1,[]),'4.0':(2,[]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(2,[L('4.1',H,'aim of mixed education')]),
'4.4':(1,[L('4.1',H,'Catholic reaction to plan')]),
'4.5':(2,[L('4.4',H,'Cullen and Catholic bishops','low')]),
'5.0':(1,[]),
'5.1':(1,[L('5.0',E,'Christian Brothers schools'),L('4.0',H,'national school system of 1831')]),
'5.2':(1,[]),'5.3':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L('6.0',E,'uses the Queen\'s Colleges')]),
'6.2':(2,[L('6.1',E,'why colleges were condemned')]),
'6.3':(2,[L('6.2',E,'Catholic alternative to Queen\'s Colleges')]),
'6.4':(1,[]),
'6.5':(1,[L('6.0',H,'uses Queen\'s College Belfast')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(2,[]),
'7.3':(1,[L('7.2',H,'rail links between cities')]),
'7.4':(1,[]),
'8.0':(1,[L('0.2',H,'cattle exports to Britain')]),
'8.1':(1,[L('7.1',H,'railway network growth')]),
'8.2':(1,[]),'8.3':(1,[]),
'8.4':(1,[L('7.2',H,'Killarney line of 1853')]),
'9.b':(1,[]),'9.0':(1,[]),
'9.1':(2,[L('7.0',E,'Dublin and Kingstown Railway')]),
'9.2':(1,[L('10.3',H,'Harland and Wolff site')]),
'9.3':(1,[]),
'9.4':(1,[L('9.3',E,'uses the Dublin Exhibition')]),
'9.5':(1,[]),
'9.6':(1,[L('9.3',H,'Dargan testimonial and exhibition','low')]),
'9.7':(2,[L('9.1',H,'his railway work')]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(2,[L('10.0',H,'linen industry demand')]),
'10.2':(1,[L('9.2',H,'Dargan Victoria Channel')]),
'10.3':(2,[L('9.2',H,'Queen\'s Island origin')]),
'10.4':(1,[]),'10.5':(1,[]),'10.6':(1,[]),
'11.b':(1,[]),'11.0':(1,[]),
'11.1':(1,[L('10.6',H,'migrants to Belfast')]),
'11.2':(1,[L('11.1',H,'Catholic migrants in Belfast')]),
'12.0':(1,[L('1.0',H,'stronger farmers'),L('8.0',H,'railways opened markets')]),
'12.1':(1,[L('0.0',E,'population fall'),L('3.0',H,'continued emigration')]),
'12.2':(1,[L('4.0',H,'national school system')]),
'12.3':(1,[L('5.2',E,'schooling in English')]),
'12.4':(1,[L('10.0',H,'Belfast industrialisation')]),
'12.5':(1,[L('11.0',H,'southern industry declined')]),
'12.6':(1,[L('12.0',H,'prosperity of stronger farmers'),L('8.0',H,'railways as improvement')]),
'12.7':(2,[L('1.0',H,'prosperous farmer class'),L('3.0',H,'emigrant society')]),
}
txt=open(D+'packs/hist-ire1-s5.t1g1.txt').read()
tgt=[];sec=None;allids=set()
for ln in txt.splitlines():
    if ln.startswith('TARGET'): sec='t'
    elif ln.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[([^\]]+)\]',ln)
    if m:
        allids.add(m.group(1))
        if sec=='t': tgt.append(m.group(1))
assert set(d)=={t[len(P):] for t in tgt},set(d)^{t[len(P):] for t in tgt}
out={t:{"cost":d[t[len(P):]][0],"needs":d[t[len(P):]][1]} for t in tgt}
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open(D+'point-links/hist-ire1-s5.t1g1.json','w'),indent=1)
r=json.load(open(D+'point-links/hist-ire1-s5.t1g1.json'))
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for v in r.values() for n in v['needs']))
