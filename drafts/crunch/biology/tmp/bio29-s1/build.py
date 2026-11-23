import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio29-s1.txt').read()
tgt,cand=txt.split('CANDIDATES')
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
E,H='essential','helpful'
# id -> (cost, [(need, strength, why, conf)])
d={
'0.4':(2,[('0.3',H,'ventricles pump blood out','high')]),
'1.0':(1,[('0.2',H,'atria receive blood','high')]),
'1.1':(1,[('0.2',H,'right atrium','high')]),
'1.2':(1,[('0.2',H,'left atrium','high')]),
'1.3':(1,[('0.3',H,'ventricles','high')]),
'1.4':(1,[('0.3',H,'left ventricle','high')]),
'1.5':(1,[('1.4',H,'aorta base','high')]),
'2.0':(2,[('0.2',H,'atria and ventricles','high')]),
'2.1':(1,[('2.0',E,'AV valves','high')]),
'2.2':(2,[('2.0',E,'AV valve flaps','high')]),
'2.3':(1,[('1.3',H,'pulmonary artery','low'),('1.4',H,'aorta','low')]),
'2.4':(1,[('2.3',E,'semilunar valve pockets','high')]),
'3.1':(1,[('3.0',E,'intercalated discs','high')]),
'3.2':(2,[('3.0',H,'cardiac muscle cells','high')]),
'3.4':(2,[('0.4',E,'thicker left ventricle wall','high'),('2.0',E,'AV valves','high'),('2.3',H,'semilunar valves','high'),('1.1',H,'venae cavae','high'),('1.3',H,'pulmonary artery','high')]),
'3.5':(2,[('3.0',E,'cardiac muscle structure','high')]),
'4.b':(1,[('bio2-s2.0.b',H,'types of variables','low')]),
'4.1':(1,[('0.4',H,'ventricle wall thickness','high')]),
'4.2':(1,[('1.3',H,'arteries thick-walled','high')]),
'4.3':(1,[('2.1',H,'valves one-way','high')]),
'4.4':(2,[('bio2-s2.0.1',E,'independent variable','high'),('bio2-s2.0.2',E,'dependent variable','high')]),
'4.5':(2,[('bio2-s2.0.3',E,'controlled variables','high')]),
'4.6':(1,[('bio2-s2.5.2',E,'repeats and mean','high')]),
'4.7':(2,[('4.0',E,'secondary data','high')]),
'5.0':(1,[('bio2-s2.7.1',H,'safety precautions','low')]),
'5.1':(2,[('1.3',H,'pulmonary artery','high'),('0.4',H,'left ventricle thicker','high')]),
'5.2':(2,[('0.2',H,'atria','high'),('1.5',H,'coronary arteries','high')]),
'5.3':(1,[('1.3',H,'arteries thick-walled','high')]),
'5.5':(1,[('1.1',H,'venae cavae to right atrium','high'),('1.4',H,'aorta from left ventricle','high')]),
'6.0':(1,[('0.3',H,'ventricles','high')]),
'6.1':(2,[('2.2',E,'chordae and papillary muscles','high'),('2.0',H,'tricuspid valve','high'),('2.3',H,'semilunar valve','high')]),
'6.2':(1,[('2.0',H,'bicuspid valve','high')]),
'6.3':(2,[('2.4',E,'semilunar valves closing','high')]),
'6.4':(1,[('2.1',H,'AV valves close','high')]),
'6.5':(1,[('0.5',H,'septum','high')]),
'6.6':(1,[('4.5',E,'controlled variables','high'),('4.6',H,'repeats and mean','high')]),
'6.7':(1,[('3.5',H,'cardiac muscle slide','high')]),
'7.0':(1,[('bio2-s2.7.4',H,'sharp scalpel precautions','low')]),
'7.1':(1,[('bio2-s2.7.1',H,'general control measures','low')]),
'7.4':(1,[('bio2-s2.9.0',H,'animal ethics','low')]),
'7.5':(1,[('bio2-s2.9.1',E,'the 3Rs','high')]),
'8.b':(1,[('4.0',H,'primary and secondary data','high')]),
'8.0':(2,[('0.4',H,'left ventricle thicker','high'),('0.5',H,'septum','high')]),
'8.1':(2,[('2.0',E,'AV valves','high'),('2.3',H,'semilunar valves','high')]),
'8.2':(1,[('1.5',H,'coronary arteries','high')]),
'8.4':(1,[('4.7',H,'secondary data model','high')]),
'8.5':(1,[('3.5',H,'cardiac muscle micrograph','high')]),
'9.0':(1,[('0.4',E,'ventricle wall thickness','high')]),
'9.1':(1,[('0.2',H,'atria thin walls','high')]),
'9.2':(1,[('2.1',H,'one-way valves','high')]),
'9.3':(1,[('0.5',H,'septum function','high')]),
'9.4':(1,[('1.3',H,'artery walls','high')]),
'9.5':(1,[('4.1',H,'hypotheses','high')]),
'10.1':(1,[('4.5',H,'controlled variables','high')]),
'10.3':(1,[('4.7',H,'model heart','high')]),
'10.4':(1,[('bio2-s2.5.4',H,'sample size','low')]),
}
# 2-cost for extra complex ones
for k in ['4.8']: d[k]=(2,[])
out={}
for t in tids:
    k=t.split('s1.')[1]
    c,ns=d.get(k,(1,[]))
    needs=[]
    for n,s,w,cf in ns:
        i=n if n.startswith('bio2') else 'bio29-s1.'+n
        assert i in allids and i!=t,(t,i)
        needs.append({'id':i,'strength':s,'why':w,'confidence':cf})
    out[t]=({'cost':c,'needs':needs})
json.dump(out,open(P+'point-links/bio29-s1.json','w'),indent=1)
o=json.load(open(P+'point-links/bio29-s1.json'))
assert list(o)==tids
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
