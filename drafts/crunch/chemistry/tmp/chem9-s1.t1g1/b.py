import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
P='chem9-s1.'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {'id':i if '-' in i else P+i,'strength':s,'why':w,'confidence':c}
R={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[L('0.0',H,'particles in constant motion')]),
'0.2':(1,[L('0.0',H,'particles in constant motion')]),
'0.3':(1,[L('0.0',H,'particles in constant motion')]),
'0.4':(1,[L('0.1',H,'solid particle arrangement'),L('0.3',H,'gas particle arrangement')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[L('1.2',E,'compound has bonded elements')]),
'1.4':(1,[L('1.2',H,'compounds of different atoms')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'3.b':(1,[]),
'3.0':(1,[L('1.0',H,'pure substance has fixed melting point')]),
'3.1':(1,[L('3.0',E,'compare with sharp melting point')]),
'4.b':(1,[]),
'4.0':(1,[L('2.0',H,'mixture has variable composition')]),
'4.1':(1,[L('1.2',H,'compound elements chemically combined')]),
'4.2':(1,[L('1.3',H,'compound properties differ from elements')]),
'4.3':(1,[L('2.1',H,'mixtures separated physically')]),
'4.4':(1,[]),
'4.5':(1,[L('1.1',H,'element particle diagrams')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L('5.0',E,'particles in motion')]),
'5.2':(1,[L('5.1',E,'kinetic energy and temperature')]),
'5.3':(1,[L('5.0',H,'kinetic theory being tested'),L('chem1-s1.0.5',H,'evidence supports theory','low')][:1]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[L('6.2',H,'smoke cell')]),
'6.4':(1,[L('6.3',H,'lit smoke cell')]),
'6.5':(1,[L('6.1',H,'smoke particle experiment')]),
'7.b':(1,[]),
'7.0':(2,[L('6.5',E,'smoke jiggling observation')]),
'7.1':(1,[L('7.0',H,'air molecules move smoke')]),
'7.2':(1,[L('7.0',E,'explanation of smoke motion')]),
'7.3':(1,[L('6.2',H,'smoke cell set-up')]),
'8.b':(1,[]),
'8.0':(1,[L('5.0',H,'random motion of particles','low')]),
'8.1':(1,[L('0.3',H,'gas particles spread out')]),
'8.2':(1,[L('8.1',E,'bromine vapour spreading')]),
'8.3':(1,[]),
'9.b':(1,[L('8.b',H,'diffusion of gases')]),
'9.0':(1,[]),
'9.1':(1,[L('9.0',H,'ammonia and hydrochloric acid set-up')]),
'9.2':(1,[L('9.1',H,'white ring position')]),
'9.3':(2,[L('8.b',H,'diffusion of gases')]),
'9.4':(1,[]),
'9.5':(1,[L('9.0',H,'tube set-up')]),
'10.b':(1,[L('8.b',H,'diffusion')]),
'10.0':(1,[L('8.b',H,'diffusion')]),
'10.1':(1,[L('10.0',H,'diffusion in liquids')]),
}
txt=open(D+'packs/chem9-s1.t1g1.txt').read()
tids=re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
assert [i[len(P):] for i in tids]==list(R),set(tids)^{P+k for k in R}
out={}
for k,(c,n) in R.items():
    out[P+k]={'cost':c,'needs':n}
    for x in n: assert x['id'] in allids and x['id']!=P+k
json.dump(out,open(D+'point-links/chem9-s1.t1g1.json','w'),ensure_ascii=False)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
