import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio26-s1.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
targets=re.findall(r'^\[(bio26-s1\.[^\]]+)\]',txt,re.M)
E,H='essential','helpful'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[n('bio26-s1.0.0',E,'excretion of metabolic wastes')]),
'0.2':(2,[n('bio26-s1.0.0',H,'urea as a metabolic waste','low')]),
'0.3':(1,[n('bio26-s1.0.2',E,'urea production')]),
'0.4':(1,[n('bio26-s1.0.1',H,'wastes kidneys remove into urine')]),
'0.5':(1,[n('bio26-s1.0.4',H,'kidneys transfer between blood and urine','low')]),
'0.6':(2,[n('bio26-s1.0.0',E,'excretion defined'),n('bio21-s2.0.b',H,'homeostasis meaning')]),
'0.7':(2,[n('bio26-s1.0.6',H,'the two kidney roles')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[n('bio26-s1.1.0',H,'kidney position')]),
'1.2':(1,[n('bio26-s1.1.0',H,'kidney location')]),
'1.3':(1,[n('bio26-s1.1.0',H,'kidney position')]),
'1.4':(1,[n('bio26-s1.0.7',H,'filtration needs pressure')]),
'1.5':(1,[n('bio26-s1.1.4',H,'renal artery counterpart')]),
'1.6':(2,[n('bio26-s1.1.4',E,'renal artery blood'),n('bio26-s1.0.7',H,'filtration and reabsorption removing substances','low')]),
'1.7':(2,[n('bio26-s1.1.4',H,'renal artery from aorta'),n('bio26-s1.2.0',H,'ureters'),n('bio26-s1.2.4',H,'sphincter muscles')]),
'2.b':(1,[]),
'2.0':(1,[n('bio26-s1.3.3',H,'renal pelvis','low')]),
'2.1':(2,[n('bio26-s1.2.0',E,'ureter structure')]),
'2.2':(1,[]),
'2.3':(1,[n('bio26-s1.2.2',E,'bladder')]),
'2.4':(2,[n('bio26-s1.2.2',E,'bladder outlet')]),
'2.5':(1,[n('bio26-s1.2.2',H,'bladder as urine source')]),
'2.6':(1,[n('bio26-s1.2.5',E,'urethra')]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[n('bio26-s1.3.0',E,'kidney regions'),n('bio26-s1.1.2',H,'renal capsule','low')]),
'3.2':(1,[n('bio26-s1.3.0',E,'kidney regions')]),
'3.3':(1,[n('bio26-s1.3.0',E,'kidney regions'),n('bio26-s1.2.0',H,'ureter')]),
'4.b':(1,[]),
'4.0':(1,[n('bio26-s1.3.0',H,'cortex and medulla')]),
'4.1':(1,[n('bio26-s1.4.0',E,'nephron tubules'),n('bio26-s1.3.3',H,'renal pelvis')]),
'4.2':(2,[n('bio26-s1.4.0',E,'nephron structure'),n('bio26-s1.1.4',H,'high-pressure renal blood supply')]),
'4.3':(2,[n('bio26-s1.4.2',E,'filtration into capsule'),n('bio25-s1.0.2',H,'selective permeability and size','low')]),
'4.4':(2,[n('bio26-s1.4.0',E,'nephron regions'),n('bio25-s1.4.4',H,'reabsorption by active transport','low')]),
'4.5':(2,[n('bio26-s1.4.3',E,'filtrate contents'),n('bio26-s1.4.4',E,'reabsorption')]),
'4.6':(2,[n('bio26-s1.3.0',E,'kidney regions'),n('bio26-s1.4.0',E,'nephron structure')]),
'5.b':(1,[]),
'5.0':(1,[n('bio26-s1.0.1',H,'substances excreted in urine')]),
'5.1':(1,[n('bio26-s1.4.3',E,'protein not filtered'),n('bio26-s1.4.5',E,'glucose reabsorbed')]),
'5.2':(1,[n('bio26-s1.4.5',H,'water reabsorption')]),
'5.3':(1,[n('bio26-s1.4.5',H,'water reabsorption'),n('bio26-s1.5.2',H,'dilute urine contrast')]),
'5.4':(1,[n('bio21-s2.7.1',H,'ADH controls water reabsorption')]),
'6.b':(1,[]),
'6.0':(1,[n('bio26-s1.4.5',H,'salt reabsorption')]),
'6.1':(2,[n('bio25-s1.2.0',E,'osmosis definition'),n('bio25-s1.3.2',H,'animal cells shrink or swell','low')]),
'6.2':(1,[n('bio26-s1.0.1',H,'hydrogen ions excreted')]),
'6.3':(2,[n('bio21-s2.2.0',E,'negative feedback'),n('bio21-s2.0.b',E,'homeostasis defined')]),
'7.b':(1,[]),
'7.0':(1,[n('bio26-s1.4.1',E,'collecting ducts to renal pelvis'),n('bio26-s1.4.5',H,'urine formed','low')]),
'7.1':(1,[n('bio26-s1.2.1',E,'peristalsis in ureter')]),
'7.2':(2,[n('bio26-s1.2.3',E,'stretchy bladder wall')]),
'7.3':(2,[n('bio26-s1.2.4',E,'sphincter muscles'),n('bio26-s1.2.3',H,'bladder contracts')]),
'7.4':(1,[n('bio26-s1.2.5',E,'urethra')]),
'8.b':(1,[]),
'8.0':(1,[n('bio26-s1.1.2',E,'fat layer cushions kidney')]),
'8.1':(1,[n('bio26-s1.1.4',E,'renal artery supply')]),
'8.2':(1,[n('bio26-s1.4.0',E,'nephrons')]),
'8.3':(1,[n('bio26-s1.4.2',E,'filtration in cortex')]),
'8.4':(1,[n('bio26-s1.4.4',E,'reabsorption sites')]),
'8.5':(1,[n('bio26-s1.3.3',E,'renal pelvis')]),
'8.6':(1,[n('bio26-s1.2.1',E,'peristalsis in ureters')]),
'8.7':(1,[n('bio26-s1.2.3',E,'elastic bladder'),n('bio26-s1.2.4',E,'sphincters')]),
'9.b':(1,[]),
'9.0':(1,[n('bio26-s1.5.1',E,'no glucose in healthy urine'),n('bio26-s1.4.5',H,'glucose reabsorption')]),
'9.1':(1,[n('bio26-s1.5.1',E,'no protein in healthy urine'),n('bio26-s1.4.3',H,'filters keep protein back')]),
'9.2':(1,[]),
'10.b':(1,[]),
'10.0':(1,[n('bio26-s1.0.6',H,'kidney roles')]),
'10.1':(1,[n('bio26-s1.10.0',H,'kidney failure')]),
'10.2':(1,[n('bio26-s1.10.1',E,'transplant as treatment')]),
'11.b':(1,[n('bio25-s1.1.0',H,'diffusion')]),
'11.0':(2,[n('bio25-s1.0.4',E,'semi-permeable membrane'),n('bio26-s1.10.1',H,'dialysis treatment')]),
'11.1':(2,[n('bio25-s1.1.0',E,'diffusion down gradient'),n('bio26-s1.11.0',E,'dialysis setup')]),
'11.2':(2,[n('bio26-s1.11.1',H,'diffusion across membrane'),n('bio26-s1.4.3',H,'size limits what crosses','low')]),
'11.3':(1,[n('bio26-s1.11.0',H,'dialysis machine')]),
}
out={}
for t in targets:
    c,nd=D[t.split('s1.')[1]]
    out[t]={"cost":c,"needs":nd}
assert len(out)==len(targets)==len(D)
for t,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=t,(t,x)
json.dump(out,open(P+'point-links/bio26-s1.json','w'),indent=1)
l=sum(len(v['needs']) for v in out.values())
print(len(out),l,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
