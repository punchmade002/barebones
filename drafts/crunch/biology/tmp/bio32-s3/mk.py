import json,re
pk=open('points/bio32-s3.txt').read()
tgt,cand=pk.split('CANDIDATES',1)
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(tids)|set(re.findall(r'^\[([^\]]+)\]',cand,re.M))
P='bio32-s3.'
E,H='essential','helpful'
N={ # id: [(need,strength,why,conf)]
'3.6':[('s2.3.1',H,'gridded quadrat squares','high')],
'3.7':[('s2.6.0',E,'density calculation','high')],
'3.4':[('3.3',E,'aspect as slope direction','high')],
'4.4':[('4.3',H,'soil sample taken','high')],
'4.5':[('4.4',E,'mixture prepared in step 2','high')],
'4.6':[('4.5',E,'settled mixture','high')],
'4.7':[('0.6',H,'calibrating meters','high')],
'5.2':[('5.1',E,'empty dish mass','high')],
'5.3':[('5.2',E,'soil sample in dish','high')],
'5.4':[('5.3',E,'heated soil','high')],
'5.5':[('5.4',E,'cooled reweighed soil','high')],
'6.0':[('5.2',E,'fresh mass','high'),('5.5',E,'dry mass at constant mass','high')],
'6.1':[('6.0',E,'percentage water formula','high')],
'7.2':[('7.1',H,'can volume','high')],
'7.3':[('7.1',E,'can volume reused','high')],
'7.4':[('7.3',E,'water in cylinder','high')],
'7.5':[('7.4',E,'stirred soil and water','high')],
'7.6':[('7.5',E,'final reading','high')],
'7.7':[('7.6',E,'air volume formula','high')],
'8.2':[('5.5',E,'dry soil from water method','high'),('8.1',H,'weighed crucible','high')],
'8.3':[('8.2',E,'crucible with soil','high')],
'8.4':[('8.3',E,'burnt soil','high')],
'8.5':[('8.4',E,'cooled reweighed soil','high')],
'8.6':[('8.5',E,'loss in mass','high'),('5.5',H,'dry mass','high')],
'8.7':[('8.6',E,'percentage humus formula','high')],
'9.1':[('9.0',E,'settled soil in cylinder','high')],
'9.2':[('9.1',E,'layers of particles','high')],
'10.2':[('s1.2.4',H,'decomposers use up oxygen','low')],
'10.3':[('4.6',H,'pH measurement as for soil','high')],
'11.1':[('11.0',E,'timed float method','high')],
'11.2':[('11.1',E,'speed = distance ÷ time','high')],
'12.0':[('s2.8.0',H,'belt transect','high')],
'12.2':[('1.0',H,'light and photosynthesis','high')],
'12.3':[('s2.13.2',H,'independent variable','high')],
'12.4':[('s2.0.6',H,'abundance meaning','high')],
'12.5':[('s2.13.4',H,'controlled variables','high')],
'13.1':[('s2.13.7',H,'correlation not cause','high')],
'13.2':[('s2.3.1',H,'gridded quadrat','high')],
'14.1':[('s2.8.0',E,'interrupted belt transect','high')],
'14.2':[('s2.5.1',H,'counting squares for cover','high')],
'14.3':[('1.2',H,'light meter use','high')],
'14.4':[('0.3',H,'readings in short period','high')],
'15.1':[('14.1',E,'transect layout','high')],
'15.2':[('14.2',H,'counts recorded','high')],
'15.4':[('14.1',H,'quadrats every 2 m','high')],
'16.1':[('16.0',H,'sample data pattern','high')],
'16.3':[('13.1',H,'correlation meaning','high')],
'17.0':[('12.1',E,'hypothesis tested','high')],
'17.1':[('13.1',E,'correlation not proof','high')],
'17.2':[('13.0',H,'uncontrolled factors','low')],
'17.3':[('1.2',H,'light changes with cloud','high')],
'17.4':[('s2.14.0',H,'sampling errors','low')],
'18.1':[('18.0',H,'exposure causes zonation','high')],
'18.2':[('s2.8.0',H,'belt transect','high')],
'18.4':[('18.3',H,'light under canopy','high')],
'18.6':[('10.2',H,'oxygen and stoneflies','low')],
'13.3':[('4.2',H,'soil pH factor','low')],
}
C2={'0.0','0.1','3.1','4.4','6.0','7.6','7.7','12.5','18.1','11.0','8.3','5.3'}
def full(k):
    return k if k.startswith('s1.') or k.startswith('s2.') else None
out={}
for t in tids:
    k=t[len(P):]
    needs=[]
    for n,s,w,c in N.get(k,[]):
        nid=('bio31-' if n.startswith('s1.') else 'bio32-')+n if n[0]=='s' else P+n
        needs.append({"id":nid,"strength":s,"why":w,"confidence":c})
    out[t]={"cost":2 if k in C2 else 1,"needs":needs}
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open('point-links/bio32-s3.json','w'),indent=1,ensure_ascii=False)
d=json.load(open('point-links/bio32-s3.json'))
assert list(d)==tids
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
