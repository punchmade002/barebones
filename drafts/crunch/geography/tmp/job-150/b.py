import json,re
P='geo-weather-climate-s2'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
S1='geo-weather-climate-s1.'
R={}
def a(k,c,*n): R[P+'.'+k]=(c,list(n))
a('0.b',1); a('0.0',1)
a('0.1',1,L(P+'.0.0','helpful','uses wavebands'))
a('0.2',1,L(P+'.0.1','essential','uses pixel'))
a('0.3',1); a('0.4',1)
a('1.b',1); a('1.0',2); a('1.1',1)
a('1.2',1); a('1.3',2,L(P+'.0.2','helpful','detail means resolution'))
a('2.b',1)
a('2.0',1,L(P+'.0.0','helpful','uses wavebands'))
a('2.1',1,L(P+'.0.0','helpful','uses infrared waveband'))
a('2.2',1,L(P+'.0.0','helpful','uses near-infrared waveband'))
a('2.3',1,L(P+'.0.0','helpful','uses microwave waveband'))
a('3.b',1)
a('3.0',1,L(P+'.2.b','helpful','image types: colour meanings'))
a('3.1',1); a('3.2',1,L(P+'.4.b','helpful','colour and tone clues','low')); a('3.3',1); a('3.4',1)
a('4.b',1); a('4.0',1); a('4.1',1); a('4.2',1); a('4.3',1)
a('4.4',1); a('4.5',1)
a('5.b',1)
a('5.0',1,L(S1+'3.0','essential','depression'),L(S1+'6.b','helpful','fronts'))
a('5.1',1); a('5.2',1,L(S1+'3.2','essential','anticyclone'))
a('5.3',2); a('5.4',1)
a('6.b',1); a('6.0',1); a('6.1',1); a('6.2',1); a('6.3',1); a('6.4',1); a('6.5',1)
a('7.b',1); a('7.0',2); a('7.1',2); a('7.2',1); a('7.3',2); a('7.4',1); a('7.5',1)
a('8.b',1); a('8.0',2); a('8.1',1); a('8.2',1); a('8.3',1); a('8.4',1)
a('9.b',1)
a('9.0',2,L(S1+'3.0','helpful','depressions','low'),L(S1+'6.b','helpful','fronts','low'))
a('9.1',1); a('9.2',1); a('9.3',1); a('9.4',2)
a('10.b',1); a('10.0',1); a('10.1',1); a('10.2',1); a('10.3',1); a('10.4',1)
a('11.b',1); a('11.0',1); a('11.1',1); a('11.2',1)
a('12.b',1); a('12.0',1); a('12.1',1)
a('12.2',1,L(P+'.0.0','helpful','uses wavebands'))
a('12.3',1)
a('12.4',1,L(P+'.2.1','helpful','infrared images blocked by cloud'))
a('12.5',1,L(P+'.0.2','helpful','uses resolution'))
a('12.6',1); a('12.7',1)
out={k:{"cost":c,"needs":n} for k,(c,n) in R.items()}
txt=open('packs/%s.t1g1.txt'%P).read()
tgt=[]
for l in txt.split('CANDIDATES')[0].splitlines():
    m=re.match(r'\[([^\]]+)\]',l)
    if m: tgt.append(m.group(1))
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert tgt==list(out),(set(tgt)^set(out))
for v in out.values():
    for n in v['needs']: assert n['id'] in allids
json.dump(out,open('point-links/%s.t1g1.json'%P,'w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
