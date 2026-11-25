import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
P='hist-ire5-s8.'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[L('hist-ire5-s4.10.4','helpful','why 1972 was deadliest','low')]),
'0.2':(1,[L('hist-ire5-s7.0.0','helpful','republicans and loyalists defined')]),
'0.3':(1,[]),
'0.4':(2,[]),
'0.5':(1,[L('hist-ire5-s7.6.1','helpful','Dublin and Monaghan bombings')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'2.b':(2,[]),
'2.0':(1,[]),
'2.1':(1,[L(P+'2.0','helpful','the manufacturing decline')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(2,[L('hist-ire5-s4.2.7','helpful','formation of the UDR')]),
'2.5':(1,[]),
'2.6':(1,[L(P+'2.5','essential','British subvention')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),
'3.2':(1,[L(P+'3.0','helpful','the DeLorean company and car')]),
'3.3':(1,[L(P+'3.2','helpful','the company failure','low')]),
'3.4':(2,[L(P+'3.2','helpful','the company collapse')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(2,[]),
'4.2':(1,[L(P+'4.1','helpful','employment discrimination against Catholics')]),
'4.3':(2,[L(P+'4.2','essential','the 1976 Act and Agency replaced')]),
'4.4':(1,[]),'4.5':(1,[]),
'4.6':(2,[L('hist-ire5-s7.1.b','helpful','paramilitary recruitment, Provisional IRA','low')]),
'5.b':(1,[]),
'5.0':(1,[L('hist-ire5-s4.3.2','helpful','Housing Executive created in 1971','low')]),
'5.1':(1,[L('hist-ire5-s4.0.2','helpful','Catholic housing discrimination complaints'),L(P+'5.0','helpful','the Housing Executive')]),
'5.2':(1,[]),'5.3':(1,[]),
'5.4':(1,[L(P+'5.2','helpful','segregation created by intimidation')]),
'5.5':(1,[L(P+'5.2','helpful','segregation by intimidation','low')]),
'5.6':(1,[L(P+'5.1','essential','the Executive allocation policy'),L(P+'5.2','helpful','families moving from mixed areas')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),
'6.5':(1,[L(P+'6.4','helpful','integrated schools','low')]),
'6.6':(1,[L(P+'6.0','helpful','separate school system')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),'7.4':(1,[]),'7.5':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L(P+'1.2','helpful','security gates sealing the city centre')]),
'8.2':(1,[]),'8.3':(1,[]),'8.4':(1,[]),
'9.b':(1,[]),
'9.0':(1,[L(P+'2.5','helpful','reliance on public money')]),
'9.1':(1,[L(P+'5.5','helpful','housing segregation'),L(P+'6.0','helpful','divided schooling')]),
'9.2':(1,[L(P+'5.0','helpful','the Housing Executive'),L(P+'4.3','helpful','the Fair Employment Acts'),L(P+'6.5','helpful','integrated schools support')]),
'9.3':(1,[L(P+'4.1','helpful','Catholic-Protestant unemployment gap'),L(P+'6.6','helpful','few integrated schools')]),
'9.4':(1,[L(P+'2.5','essential','British subvention')]),
'9.5':(1,[L(P+'4.1','helpful','discrimination and unemployment')]),
'9.6':(2,[]),
'9.7':(1,[L(P+'0.4','helpful','where violence was concentrated','low')]),
}
txt=open(H+'packs/hist-ire5-s8.t1g1.txt').read()
tgt=[]
sec=None
for ln in txt.split('\n'):
    if ln.startswith('TARGET'): sec='T'
    elif ln.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[(hist-[^\]]+)\]',ln)
    if m and sec=='T': tgt.append(m.group(1))
allids=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
out={}
for t in tgt:
    k=t.replace('hist-ire5-s8.','')
    c,n=D[k]; out[t]={"cost":c,"needs":n}
assert set(D)=={t.replace('hist-ire5-s8.','') for t in tgt}
for v in out.values():
    for n in v['needs']: assert n['id'] in allids
json.dump(out,open(H+'point-links/hist-ire5-s8.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
