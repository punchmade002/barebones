import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
S='hist-ire6-s9.'
E='hist-ire6-s1.'
def L(i,st,why,c='high'): return {"id":i,"strength":st,"why":why,"confidence":c}
d={}
def a(k,cost,*n): d[S+k]=(cost,list(n))
a('0.b',1); a('0.0',1); a('0.1',1)
a('0.2',1,L(E+'4.0','helpful','Browne health scheme'))
a('0.3',1,L(E+'8.1','helpful','1950s emigration'))
a('1.b',1); a('1.0',1)
a('1.1',2)
a('1.2',1,L(E+'8.1','helpful','emigration from the Gaeltacht','low'))
a('1.3',1)
a('1.4',1,L(S+'1.0','helpful','compulsory Irish policy'))
a('1.5',1,L(S+'1.0','essential','compulsory pass in Irish'))
a('1.6',1,L(S+'1.5','essential','the 1973 change'))
a('2.b',1); a('2.0',1)
a('2.1',1,L(S+'2.0','helpful','pirate station before RnaG'))
a('2.2',1)
a('2.3',1,L(S+'1.2','essential','Gaeltarra Éireann'))
a('2.4',1)
a('3.b',1); a('3.0',1); a('3.1',1); a('3.2',2); a('3.3',2)
a('3.4',1,L(S+'1.4','helpful','move away from compulsion','low'))
a('3.5',1); a('3.6',1)
a('4.b',1); a('4.0',1)
a('4.1',2,L(S+'1.1','helpful','Gael Linn film Mise Éire'))
a('4.2',1,L(S+'5.1','helpful','Mass in the vernacular'),L(S+'4.1','helpful','Ó Riada'))
a('4.3',2); a('4.4',1)
a('5.b',1); a('5.0',1)
a('5.1',1,L(S+'5.0','helpful','the Council itself'))
a('5.2',1)
a('5.3',2)
a('5.4',1)
a('5.5',1,L(S+'5.1','helpful','loss of Latin Mass'))
a('5.6',1)
a('6.b',1)
a('6.0',1,L(S+'0.2','helpful','Mother and Child dispute'))
a('6.1',1,L(S+'5.0','helpful','Vatican II'))
a('6.2',1,L(S+'5.3','helpful','ecumenism'))
a('6.3',1,L(S+'8.1','helpful','McGahern ban case'))
a('6.4',1); a('6.5',1); a('6.6',1); a('6.7',1)
a('6.8',1,L(S+'6.7','helpful','the Cooney view'))
a('7.b',1); a('7.0',1)
a('7.1',1,L(S+'5.0','helpful','distinct from Vatican II','low'))
a('7.2',1); a('7.3',1); a('7.4',1); a('7.5',1)
a('7.6',2,L(S+'7.5','essential','the 1983 and 1986 referendums'))
a('8.b',1); a('8.0',1)
a('8.1',1,L(S+'8.0','helpful','censorship board bans'))
a('8.2',1,L(S+'8.0','essential','the censorship Acts'))
a('8.3',1)
a('8.4',1,L(S+'8.2','helpful','1967 relaxation'))
a('8.5',1)
a('9.b',1); a('9.0',1); a('9.1',1); a('9.2',1); a('9.3',1); a('9.4',1); a('9.5',1); a('9.6',1)
a('10.b',1); a('10.0',2)
a('10.1',1,L(S+'1.4','helpful','compulsion debates'))
a('10.2',1)
a('10.3',1,L(S+'7.5','helpful','secular pluralist society'))
txt=open(P+'packs/hist-ire6-s9.t1g1.txt').read()
tgt=[];allids=set();sec=None
for ln in txt.split('\n'):
    if ln.startswith('TARGET'): sec='t'
    elif ln.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[([^\]]+)\]',ln)
    if m:
        allids.add(m.group(1))
        if sec=='t': tgt.append(m.group(1))
assert tgt==list(d), (set(tgt)^set(d),len(tgt),len(d))
out={k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k
json.dump(out,open(P+'point-links/hist-ire6-s9.t1g1.json','w'),indent=1,ensure_ascii=False)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
