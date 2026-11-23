import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio24-s2.txt').read()
tgt_part=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tgt_part,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
C2={'0.0','0.1','0.5','1.0','1.1','2.2','2.3','3.2','3.4','4.1','4.6','4.7','5.1','6.0','7.1','7.0','8.0','3.6'}
N={
'0.b':[n('bio24-s1.5.0',H,'insect-pollinated flower structure')],
'0.0':[n('bio24-s1.1.2',E,'petal function'),n('bio24-s1.1.3',H,'nectar guides')],
'0.1':[n('bio24-s1.1.2',E,'petals attract insects'),n('bio24-s1.5.4',H,'wind-pollinated flower job')],
'0.2':[n('bio24-s1.1.4',E,'nectary and nectar')],
'0.3':[n('bio24-s1.1.4',E,'nectaries')],
'0.4':[n('bio24-s1.5.0',H,'insects attracted to flowers')],
'0.5':[n('bio24-s1.5.4',H,'wind-pollinated flower job')],
'0.6':[n('bio24-s1.5.4',H,'wind pollination of trees')],
'1.b':[n('bio24-s1.2.1',E,'anther produces pollen'),n('bio24-s1.3.1',E,'stigma receives pollen')],
'1.0':[n('bio24-s1.2.2',E,'filament holds anther')],
'1.1':[n('bio24-s1.2.2',E,'filament holds anther')],
'1.2':[n('bio24-s1.3.1',E,'sticky stigma catches pollen')],
'1.3':[n('bio24-s1.3.1',E,'feathery stigma catches pollen')],
'1.4':[n('bio24-s1.3.6',H,'half-flower diagram of insect flower')],
'2.0':[n('bio24-s2.0.b',H,'flower types differ by pollinator')],
'2.1':[n('bio24-s1.4.0',H,'pollen transfer to stigma')],
'2.2':[n('bio24-s1.2.1',H,'pollen made in anther')],
'2.3':[n('bio24-s1.4.0',H,'pollen transfer by wind')],
'3.b':[n('bio2-s2.2.0',H,'fair test, control group')],
'3.0':[n('bio24-s2.0.b',H,'structure related to pollination')],
'3.1':[n('bio24-s2.3.0',H,'aim and hypothesis link'),n('bio24-s2.0.2',H,'flower structure differences')],
'3.2':[n('bio2-s2.0.1',E,'independent variable'),n('bio2-s2.0.2',H,'recorded measurements')],
'3.3':[n('bio2-s2.0.2',H,'measured quantity')],
'3.4':[n('bio2-s2.5.4',E,'large sample reduces variation'),n('bio2-s2.0.3',H,'controlled variables')],
'3.5':[n('bio2-s2.0.3',E,'controlled variables')],
'3.6':[n('bio24-s1.1.1',H,'sepals and flower parts')],
'4.0':[n('bio24-s2.1.b',H,'anther and stigma positions')],
'4.1':[n('bio24-s1.1.1',E,'sepal, petal, stamen, carpel rings')],
'4.2':[n('bio24-s1.1.4',E,'nectary identification'),n('bio24-s1.3.1',E,'stigma')],
'4.3':[n('bio24-s1.2.2',H,'filament')],
'4.4':[n('bio24-s2.1.3',H,'feathery stigma')],
'4.5':[n('bio24-s1.3.6',E,'half-flower labelled diagram')],
'4.6':[n('bio24-s1.2.1',E,'anther releases pollen')],
'4.7':[n('bio24-s2.2.3',H,'wind pollen grains')],
'5.1':[n('bio24-s2.2.3',H,'wind pollen causes hay fever'),n('bio24-s1.5.7',H,'hay fever link')],
'5.2':[],
'5.0':[n('bio2-s2.7.4',H,'scalpel safety')],
'5.4':[],
'6.b':[],
'6.0':[n('bio24-s2.3.2',E,'recorded features'),n('bio24-s1.3.1',H,'stigma')],
'6.1':[n('bio24-s2.0.b',E,'insect flower adaptations')],
'6.2':[n('bio24-s2.0.5',E,'wind flower adaptations')],
'7.0':[n('bio24-s2.0.b',E,'adaptations relate structure to function'),n('bio24-s1.3.1',H,'stigma types')],
'7.1':[n('bio24-s2.2.2',H,'pollen grain surface')],
'7.2':[n('bio24-s2.2.1',H,'wind pollen amounts')],
'7.3':[],
'8.0':[n('bio2-s2.5.4',E,'sample size and representativeness')],
'8.1':[n('bio2-s2.0.3',H,'controlled variable')],
'8.2':[n('bio2-s2.4.3',H,'instrument resolution')],
'8.3':[n('bio2-s2.4.3',E,'precision and resolution')],
'8.4':[n('bio24-s2.7.1',H,'SEM images of pollen')],
'8.5':[n('bio2-s2.4.0',H,'measurement error and subjectivity')],
'8.6':[],
}
out={}
for i in ids:
    k=i.split('bio24-s2.')[1]
    out[i]={"cost":2 if k in C2 else 1,"needs":[x for x in N.get(k,[]) if x['id'] in allids and x['id']!=i]}
json.dump(out,open(P+'point-links/bio24-s2.json','w'),indent=0)
o=json.load(open(P+'point-links/bio24-s2.json'))
assert list(o)==ids and len(set(ids))==len(ids)
nd=[x for v in o.values() for x in v['needs']]
print(len(o),len(nd),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in nd))
