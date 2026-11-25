import json,re,sys
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
# every target id judged; only these have links (all others judged: no needs from s2 candidates)
L={
'0.2':[('s2.0.2','H','NATO and Warsaw Pact formation','l')],
'0.3':[('s2.24.0','H','Khrushchev removed 1964','h'),('s2.0.5','H','Stalin died March 1953','h')],
'0.4':[('s2.8.3','E','Hungarian Uprising crushed 1956','h')],
'0.6':[('s2.19.2','H','Helsinki human rights commitments','h')],
'0.7':[('s2.22.0','H','Reagan evil empire and SDI','h'),('s2.20.0','H','Afghanistan invasion 1979','h')],
'1.3':[('s2.4.3','H','Polish October of 1956','h')],
'1.7':[('s2.8.3','E','Hungary 1956 crushed','h')],
'2.4':[('s2.8.3','H','Nagy and Hungary 1956','l')],
'3.1':[('s2.23.4','H','Brezhnev Doctrine as intervention claim','l')],
'3.5':[('s2.19.2','H','Helsinki human rights standard','h')],
'7.2':[('s2.0.4','H','General Secretary and Politburo roles','l')],
'7.4':[('s2.8.3','E','Khrushchev crushing Hungary 1956','h')],
'7.5':[('s2.22.4','H','arms agreements with Reagan','l')],
'8.0':[('s2.20.0','H','Afghanistan war','h')],
'10.0':[('s2.22.3','H','Reykjavik summit','h'),('s2.22.0','H','SDI','h')],
'10.1':[('s2.22.4','H','INF Treaty','h')],
'10.3':[('s2.20.0','H','Afghanistan invasion','h')],
'10.5':[('s2.16.3','H','earlier SALT arms limits','l')],
'11.4':[('s2.8.3','H','1956 uprising','h')],
'12.6':[('s2.12.0','H','the Berlin Wall','h')],
'18.3':[('s2.0.2','H','NATO','l')],
'18.5':[('s2.18.2','H','Oder-Neisse line','h')],
'21.1':[('s2.20.0','H','Afghanistan war','h')],
'21.6':[('s2.26.4','E','Khrushchev compared with Gorbachev','h'),('s2.24.0','H','Khrushchev removed','h')],
'22.4':[('s2.22.0','E','Reagan evil empire and SDI','h')],
'22.5':[('s2.8.3','H','force in 1956','l')],
}
txt=open(H+'packs/hist-eur4-s4.t1g2.txt').read()
tgt=[];cand=[];sec=None
for l in txt.splitlines():
    if l.startswith('TARGET'):sec='t'
    elif l.startswith('CANDIDATES'):sec='c'
    m=re.match(r'\[(\S+)\]',l)
    if m:(tgt if sec=='t' else cand).append(m.group(1))
ids=[t.replace('hist-eur4-s4.','') for t in tgt]
assert all(k in ids for k in L)
out={}
for i in ids:  # explicit decision for each: links from L else judged none
    out['hist-eur4-s4.'+i]={"needs":[{"id":"hist-eur4-"+a,"strength":"essential" if s=='E' else "helpful","why":w,"confidence":"high" if c=='h' else "low"} for a,s,w,c in L.get(i,[])]}
cs=set(cand)
for k,v in out.items():
    for n in v['needs']: assert n['id'] in cs,n
json.dump(out,open(H+'point-links/hist-eur4-s4.t1g2.json','w'),ensure_ascii=False,indent=0)
chk=json.load(open(H+'point-links/hist-eur4-s4.t1g2.json'))
assert list(chk)==tgt
print(len(chk),sum(len(v['needs']) for v in chk.values()),sum(n['confidence']=='low' for v in chk.values() for n in v['needs']))
