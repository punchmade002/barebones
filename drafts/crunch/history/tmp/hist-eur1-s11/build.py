import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
H,E='essential','helpful'
def L(i,s,w,c='high'): return dict(id=i,strength=s,why=w,confidence=c)
p='hist-eur1-s11.'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[L('hist-eur1-s1.0.9',H,'nations without states after 1815')]),
'0.4':(1,[]),
'0.5':(1,[L(p+'0.0',H,'Romantic movement','low')]),
'1.0':(1,[L('hist-eur1-s1.4.7',H,'Polish uprising of 1830-31')]),
'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[L(p+'1.2',E,'uses Verdi and Nabucco')]),
'1.4':(1,[]),
'1.5':(1,[L('hist-eur1-s1.4.5',H,'July Revolution of 1830')]),
'1.6':(1,[]),'1.7':(1,[]),'1.8':(1,[]),
'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'2.4':(2,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),
'3.5':(1,[L(p+'3.0',H,'Hernani and the Romantic dispute','low')]),
'3.6':(1,[]),
'4.0':(1,[]),'4.1':(1,[]),
'4.2':(1,[L(p+'4.1',E,'condemns Lamennais\'s ideas')]),
'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'4.6':(2,[]),
'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),
'5.6':(1,[]),'5.7':(1,[]),
'6.0':(1,[]),
'6.1':(1,[L(p+'6.0',H,'Faraday\'s earlier discovery','low')]),
'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),
'6.5':(1,[L(p+'6.2',H,'telegraph technology'),L(p+'6.3',H,'Morse telegraph system','low')]),
'6.6':(1,[L(p+'6.0',H,'electromagnetic induction and generators')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),
'7.2':(1,[L(p+'7.1',H,'Beagle voyage observations')]),
'7.3':(1,[L(p+'7.2',H,'the Origin of Species')]),
'7.4':(1,[L(p+'7.3',H,'theory applied to humans')]),
'7.5':(1,[L(p+'7.2',E,'reaction to the Origin')]),
'7.6':(2,[L(p+'7.3',H,'evolutionary theory'),L(p+'8.0',H,'Mendel and genetics')]),
'8.0':(1,[]),'8.1':(1,[]),
'8.2':(1,[L(p+'8.1',H,'Pasteur\'s micro-organism work')]),
'8.3':(1,[]),
'8.4':(1,[L(p+'6.2',H,'telegraph')]),
'8.5':(1,[]),'8.6':(1,[]),
'9.0':(2,[L(p+'0.b',H,'Romanticism giving nationalists symbols')]),
'9.1':(2,[L(p+'9.0',H,'cultural nationalism achievement')]),
'9.2':(2,[L(p+'4.0',H,'Catholic revival'),L(p+'5.5',H,'church social work')]),
'9.3':(2,[L(p+'9.2',H,'church social work')]),
'9.4':(2,[L(p+'7.b',H,'Darwin'),L(p+'8.0',H,'Mendel'),L(p+'8.1',H,'Pasteur')]),
'9.5':(2,[L(p+'9.0',H,'cultural achievements summarised')]),
}
pk=P+'packs/hist-eur1-s11.t1g1.txt'
txt=open(pk).read()
tgt=re.findall(r'^\[(hist-eur1-s11\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert len(D)==len(tgt)
out={t:{'cost':D[t[len(p):]][0],'needs':D[t[len(p):]][1]} for t in tgt}
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t and len(n['why'].split())<=8,(t,n)
json.dump(out,open(P+'point-links/hist-eur1-s11.t1g1.json','w'),indent=1)
r=json.load(open(P+'point-links/hist-eur1-s11.t1g1.json'))
ln=[n for v in r.values() for n in v['needs']]
print(len(r),len(ln),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for n in ln))
