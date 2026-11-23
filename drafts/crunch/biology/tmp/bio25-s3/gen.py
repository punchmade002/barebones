import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio25-s3.txt').read()
tgt,_,cand=txt.partition('\nCANDIDATES')
ids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
E,H='essential','helpful'
# id: (cost, [(need,strength,why,conf)])
D={
'0.0':(1,[('bio25-s1.2.0',E,'osmosis definition','high')]),
'0.1':(1,[('bio25-s1.2.0',E,'water movement by osmosis','high')]),
'0.2':(1,[('bio25-s3.0.1',H,'percentage change in mass','high')]),
'0.3':(1,[('bio25-s3.3.0',H,'Visking tubing semi-permeable','high')]),
'1.3':(2,[]),
'1.4':(2,[('bio25-s3.1.3',E,'making 1.0 M solution','high')]),
'1.5':(1,[('bio2-s2.5.1',H,'replicates','high')]),
'1.6':(1,[('bio2-s2.5.2',H,'repeats','high')]),
'2.3':(1,[('bio2-s2.2.0',H,'fair test','low')]),
'3.0':(1,[('bio25-s1.0.4',H,'semi-permeable definition','high')]),
'3.1':(1,[('bio25-s3.3.0',E,'semi-permeable pores','high')]),
'3.2':(1,[('bio25-s1.0.5',E,'selectively permeable living membrane','high')]),
'3.3':(2,[('bio25-s3.3.0',H,'Visking tubing properties','low')]),
'4.b':(1,[('bio25-s1.1.0',H,'concentration gradient','high')]),
'4.0':(2,[('bio25-s1.1.0',E,'concentration gradient','high'),('bio25-s1.2.0',E,'net water movement','high')]),
'4.1':(1,[('bio2-s2.0.1',E,'independent variable','high'),('bio2-s2.0.2',E,'dependent variable','high')]),
'4.2':(1,[('bio2-s2.0.3',E,'controlled variables','high')]),
'4.3':(1,[('bio2-s2.2.1',E,'control experiment','high')]),
'5.0':(1,[('bio25-s3.2.0',E,'steps for making bag','high')]),
'5.3':(1,[('bio25-s3.2.5',H,'blotting method','high')]),
'5.4':(1,[('bio25-s3.11.0',E,'change in mass and rate','high')]),
'6.b':(1,[('bio25-s1.0.5',H,'living membrane permeability','low')]),
'6.0':(1,[('bio25-s3.1.2',H,'cork borer equipment','high')]),
'6.2':(1,[('bio25-s3.1.4',H,'making sucrose range','high')]),
'6.3':(1,[('bio25-s3.11.1',E,'percentage change formula','high')]),
'6.4':(1,[('bio25-s3.6.3',H,'percentage change in mass','high')]),
'6.5':(2,[('bio25-s1.2.0',H,'osmosis direction','high')]),
'6.6':(1,[('bio25-s3.6.5',E,'egg method','high')]),
'7.0':(2,[('bio25-s1.1.6',E,'temperature raises diffusion rate','high'),('bio25-s1.1.1',H,'kinetic energy of particles','low')]),
'7.1':(1,[('bio2-s2.0.1',E,'independent variable','high'),('bio2-s2.0.2',E,'dependent variable','high')]),
'7.2':(1,[('bio2-s2.0.3',E,'controlled variables','high')]),
'7.3':(1,[('bio2-s2.2.1',E,'control experiment','high')]),
'7.4':(2,[('bio25-s3.3.2',H,'Visking versus living membranes','low')]),
'8.2':(1,[('bio25-s3.2.0',E,'steps for making bag','high')]),
'8.4':(1,[('bio25-s3.5.3',H,'weighing procedure','high')]),
'8.5':(1,[('bio25-s3.11.0',E,'rate calculation','high')]),
'9.b':(1,[('bio25-s1.1.7',H,'surface area and diffusion','low')]),
'9.0':(2,[('bio25-s1.1.6',E,'surface area raises rate','high')]),
'9.1':(1,[('bio2-s2.0.1',E,'independent variable','high'),('bio2-s2.0.2',E,'dependent variable','high')]),
'9.2':(1,[('bio2-s2.0.3',E,'controlled variables','high')]),
'9.3':(2,[]),
'9.4':(1,[('bio25-s3.9.3',H,'surface area calculation','high')]),
'9.5':(2,[('bio25-s3.9.3',H,'surface area calculation','high')]),
'9.6':(1,[('bio2-s2.2.0',H,'fair test','high')]),
'9.7':(1,[('bio2-s2.2.1',H,'control experiment','high')]),
'10.0':(1,[('bio25-s3.6.0',H,'cutting potato pieces','high')]),
'10.4':(1,[('bio25-s3.11.1',E,'percentage change formula','high')]),
'11.1':(1,[('bio25-s3.11.0',H,'change in mass','high')]),
'11.2':(2,[('bio25-s3.11.1',E,'rate and percentage formulas','high')]),
'11.3':(2,[('bio25-s3.11.1',E,'percentage change formula','high')]),
'11.4':(1,[('bio25-s3.11.1',E,'percentage change formula','high')]),
'11.5':(2,[('bio2-s2.0.1',E,'independent and dependent variables','high')]),
'11.6':(1,[('bio25-s3.11.5',H,'plotting graphs','low')]),
'12.0':(1,[('bio2-s2.7.0',H,'hazards and control measures','low')]),
'12.1':(1,[('bio2-s2.7.2',H,'hot water hazard','high')]),
'13.0':(2,[('bio25-s3.4.0',E,'concentration gradient hypothesis','high')]),
'13.1':(2,[('bio25-s1.1.0',H,'concentration gradient','high')]),
'13.2':(2,[('bio25-s1.3.3',E,'turgid and flaccid cells','high'),('bio25-s1.3.0',H,'hypotonic and hypertonic','low')]),
'13.3':(2,[('bio25-s1.3.0',E,'isotonic meaning','high')]),
'13.4':(1,[('bio25-s3.7.0',H,'temperature hypothesis','high')]),
'13.5':(2,[('bio25-s3.7.4',H,'tubing not living tissue','low')]),
'13.6':(1,[('bio25-s3.9.0',H,'surface area hypothesis','high')]),
'14.0':(1,[('bio25-s3.2.5',H,'blotting method','high')]),
'14.1':(1,[('bio25-s3.3.1',H,'sucrose slowly passing tubing','high')]),
'14.2':(1,[('bio25-s3.2.3',H,'same volume in each bag','high')]),
'14.3':(1,[('bio25-s3.8.4',H,'checking bath temperature','high')]),
'14.4':(1,[('bio2-s2.4.3',E,'balance resolution','high')]),
'14.5':(1,[('bio2-s2.5.1',H,'replicates','high')]),
'14.6':(1,[('bio25-s1.0.5',E,'selectively permeable membranes','high')]),
}
out={}
for i in ids:
    k=i.split('s3.',1)[1]
    c,n=D.get(k,(1,[]))
    out[i]={"cost":c,"needs":[{"id":a,"strength":s,"why":w,"confidence":f} for a,s,w,f in n]}
json.dump(out,open(P+'point-links/bio25-s3.json','w'),indent=1)
o=json.load(open(P+'point-links/bio25-s3.json'))
assert list(o)==ids and len(set(ids))==len(ids)
bad=[k for v in o.values() for n in v['needs'] for k in [n['id']] if k not in allids]
selfl=[i for i,v in o.items() for n in v['needs'] if n['id']==i]
unk=[k for k in D if 'bio25-s3.'+k not in ids]
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']),bad,selfl,unk)
