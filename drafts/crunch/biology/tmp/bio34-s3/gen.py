import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio34-s3.txt').read()
tg=txt.split('CANDIDATES')[0]
targets=re.findall(r'^\[([^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
H,E='helpful','essential'
# id: (cost, [(need,strength,why,conf)])
S={
'0.0':(1,[('bio34-s1.0.3',H,'carbon stores','high')]),
'0.2':(2,[('bio34-s3.0.1',H,'ethical issue meaning','high')]),
'0.3':(1,[('bio34-s3.0.1',H,'ethical issue meaning','low')]),
'1.0':(1,[('bio34-s2.5.3',H,'nitrate leaching','high')]),
'1.3':(1,[('bio34-s3.1.b',H,'eutrophication','high')]),
'2.b':(1,[('bio34-s1.4.0',H,'decomposers respire','high')]),
'2.1':(1,[('bio34-s3.2.0',H,'previous step','high')]),
'2.2':(1,[('bio34-s3.2.1',H,'algal bloom','high')]),
'2.3':(1,[('bio34-s3.2.2',H,'previous step','high')]),
'2.4':(2,[('bio34-s1.4.0',E,'aerobic decomposers respire','high'),('bio34-s3.2.3',H,'dead algae','high')]),
'2.5':(1,[('bio34-s3.2.4',E,'oxygen used by decomposers','high')]),
'2.6':(2,[('bio34-s3.2.5',H,'dead fish','high'),('bio34-s1.4.5',H,'anaerobic decomposition','high')]),
'2.7':(2,[('bio34-s3.2.4',H,'decomposer step of chain','low')]),
'3.b':(1,[('bio34-s3.2.5',H,'oxygen loss','high')]),
'3.1':(1,[('bio34-s3.3.0',H,'blue-green algal blooms','high')]),
'4.b':(1,[('bio34-s3.0.2',H,'who gains and pays','low')]),
'4.0':(2,[('bio34-s2.0.2',H,'plants absorb nitrate','high')]),
'4.1':(1,[('bio34-s2.2.1',E,'Haber process','high')]),
'5.b':(1,[('bio34-s3.1.b',H,'eutrophication','high')]),
'5.0':(1,[('bio34-s3.1.b',H,'eutrophication','high')]),
'5.2':(1,[('bio34-s3.5.1',H,'nitrate limit','high')]),
'6.0':(1,[('bio34-s2.2.1',E,'Haber process','high')]),
'6.1':(2,[('bio34-s2.6.0',E,'denitrification','high')]),
'6.2':(1,[('bio34-s3.1.1',H,'slurry','low')]),
'6.3':(2,[('bio34-s3.6.2',H,'ammonia emissions','high')]),
'6.4':(1,[('bio34-s3.6.2',H,'ammonia emissions','high')]),
'7.b':(1,[('bio34-s3.0.1',H,'ethical issue','high')]),
'7.0':(1,[('bio34-s3.0.2',H,'who benefits and pays','high')]),
'7.1':(1,[('bio34-s3.0.2',E,'polluter pays principle','high')]),
'7.2':(1,[('bio34-s3.7.1',H,'polluter pays argument','high')]),
'7.3':(1,[('bio34-s3.7.1',H,'cost of prevention','low')]),
'7.4':(2,[('bio34-s3.0.3',H,'justice','high')]),
'8.1':(2,[('bio34-s3.8.0',E,'Nitrates Directive','high')]),
'8.2':(1,[('bio34-s3.8.0',H,'Nitrates Directive','high')]),
'8.3':(1,[('bio34-s3.8.0',E,'Nitrates Directive','high')]),
'9.0':(1,[('bio34-s3.1.0',H,'nitrate lost to water','high')]),
'9.1':(2,[('bio34-s2.1.1',E,'nitrogen fixation in legumes','high')]),
'9.2':(1,[('bio34-s3.1.0',H,'nutrient runoff','low')]),
'9.3':(1,[('bio34-s3.6.2',E,'ammonia loss from slurry','high')]),
'9.4':(2,[('bio34-s2.6.4',E,'denitrification removes nitrate','high')]),
'9.5':(2,[('bio34-s3.4.1',H,'fertiliser feeds world','high')]),
'9.6':(1,[('bio34-s3.9.5',H,'the judgement','high')]),
'10.1':(1,[('bio34-s1.4.0',H,'decomposers','high')]),
'10.2':(2,[('bio34-s1.4.5',H,'anaerobic breakdown','low')]),
'10.3':(1,[('bio34-s3.10.2',E,'anaerobic digestion','high')]),
'11.b':(1,[('bio34-s3.10.0',H,'recycling methods','high')]),
'11.0':(1,[('bio34-s3.6.0',H,'energy to make fertiliser','high')]),
'11.1':(1,[('bio34-s1.4.5',H,'anaerobic methane release','high')]),
'11.2':(1,[('bio34-s1.0.3',H,'soil carbon store','low')]),
'11.3':(1,[('bio34-s3.10.2',H,'sludge and manure use','low')]),
'11.4':(1,[('bio34-s3.1.1',H,'slurry washed off','low')]),
'11.5':(1,[('bio34-s3.10.3',H,'biogas methane','high')]),
'11.7':(1,[('bio34-s3.10.0',H,'recycling methods','high')]),
'12.b':(1,[('bio34-s1.6.0',H,'sink and source','high')]),
'12.1':(2,[('bio34-s1.6.0',E,'sink and source','high')]),
'12.3':(1,[('bio34-s3.12.1',H,'effects of deforestation','high')]),
'12.4':(1,[('bio34-s3.12.0',H,'beef, soya, palm oil','high')]),
'13.b':(1,[('bio34-s1.6.1',H,'bog as sink or source','high')]),
'13.1':(2,[('bio34-s1.7.4',E,'draining bog releases CO2','high')]),
'13.2':(1,[('bio34-s3.13.0',H,'turf cutting','high')]),
'13.3':(1,[('bio34-s3.13.1',H,'carbon lost from peat','high')]),
'14.0':(1,[('bio34-s3.13.0',H,'Bord na Mona','high')]),
'14.1':(1,[('bio31-s2.3.0',H,'SACs on raised bogs','high')]),
'14.2':(1,[('bio31-s2.3.1',H,'rewetting bogs','high')]),
'14.3':(1,[('bio34-s3.14.2',H,'people losing income','low')]),
'14.4':(2,[('bio34-s1.5.4',E,'fossil fuel CO2 release','high')]),
'14.5':(1,[('bio34-s3.14.4',H,'climate harm to others','high')]),
}
out={}
for t in targets:
    k=t.replace('bio34-s3.','')
    c,ns=S.get(k,(1,[]))
    out[t]={"cost":c,"needs":[{"id":i,"strength":s,"why":w,"confidence":f} for i,s,w,f in ns]}
for k in S: assert 'bio34-s3.'+k in out,k
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open(P+'point-links/bio34-s3.json','w'),indent=1)
d=json.load(open(P+'point-links/bio34-s3.json'))
assert list(d)==targets
L=[n for v in d.values() for n in v['needs']]
print(len(d),len(L),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for n in L))
