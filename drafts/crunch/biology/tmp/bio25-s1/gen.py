import json,re
P='bio25-s1.'
E,H='essential','helpful'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[]),
'0.0':(1,[n('bio7-s3.0.3',H,'cell membrane structure')]),
'0.1':(1,[]),
'0.2':(1,[n(P+'0.0',H,'phospholipid bilayer')]),
'0.3':(2,[n(P+'0.0',E,'bilayer and proteins')]),
'0.4':(2,[n('bio7-s3.0.0',H,'plant cell wall example','low')]),
'0.5':(1,[n(P+'0.4',H,'contrast with other barrier types')]),
'0.6':(1,[]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[n('bio7-s3.2.2',H,'ATP as cell energy carrier')]),
'1.2':(1,[n(P+'1.0',H,'net movement down gradient')]),
'1.3':(1,[n(P+'1.0',H,'diffusion of gases')]),
'1.4':(1,[n(P+'1.0',H,'diffusion examples','low')]),
'1.5':(2,[n(P+'0.3',E,'channel and carrier proteins')]),
'1.6':(2,[n(P+'1.0',E,'diffusion and gradient')]),
'1.7':(2,[n(P+'1.6',E,'factors affecting diffusion rate')]),
'2.b':(1,[]),
'2.0':(1,[n(P+'1.0',E,'diffusion definition'),n(P+'0.4',H,'semi-permeable membrane')]),
'2.1':(1,[n(P+'1.0',E,'diffusion')]),
'2.2':(2,[n(P+'0.6',E,'solute and water concentration')]),
'2.3':(1,[n(P+'2.2',E,'why water moves'),n('bio7-s3.0.1',H,'cell wall resists osmotic uptake','low')]),
'2.4':(1,[n(P+'2.0',E,'osmosis definition')]),
'3.b':(1,[]),
'3.0':(2,[n(P+'2.0',E,'osmosis water movement')]),
'3.1':(2,[n(P+'3.0',E,'hypotonic and hypertonic')]),
'3.2':(1,[n(P+'3.0',E,'hypertonic solution')]),
'3.3':(2,[n(P+'3.0',E,'hypotonic solution'),n('bio7-s3.1.2',H,'vacuole structure')]),
'3.4':(2,[n(P+'3.3',E,'turgid cell and wall')]),
'3.5':(1,[n(P+'3.4',E,'plasmolysis'),n(P+'0.4',H,'cell wall fully permeable')]),
'3.6':(2,[n(P+'3.4',E,'turgid, flaccid, plasmolysed'),n(P+'3.2',H,'crenated red blood cells')]),
'4.b':(1,[]),
'4.0':(1,[n(P+'1.0',E,'concentration gradient'),n('bio7-s3.2.2',H,'ATP energy')]),
'4.1':(1,[n(P+'4.0',E,'active transport needs ATP')]),
'4.2':(1,[n('bio7-s3.2.2',E,'mitochondria make ATP')]),
'4.3':(1,[n(P+'4.0',E,'against gradient uptake')]),
'4.4':(1,[n(P+'4.0',E,'against gradient absorption')]),
'5.b':(1,[]),
'5.0':(1,[n(P+'0.3',H,'carrier proteins in membrane')]),
'5.1':(1,[n(P+'5.0',E,'carrier protein pump'),n('bio7-s3.2.2',H,'ATP releases energy')]),
'5.2':(1,[n(P+'5.1',E,'shape change of carrier')]),
'5.3':(1,[n(P+'5.2',E,'carrier shape change')]),
'5.4':(2,[n(P+'5.0',H,'four-step pump process')]),
'6.b':(1,[]),
'6.0':(2,[n(P+'4.0',E,'active transport against gradient'),n(P+'5.0',H,'carrier protein pump')]),
'6.1':(1,[n(P+'6.0',E,'Na+ and K+ pumping')]),
'7.b':(1,[]),
'7.0':(1,[n(P+'1.1',E,'diffusion is passive'),n(P+'4.1',H,'active transport needs ATP')]),
'7.1':(1,[n(P+'1.0',E,'diffusion down gradient'),n(P+'4.0',E,'active transport against gradient')]),
'7.2':(1,[n(P+'2.1',H,'osmosis moves water only')]),
'7.3':(2,[n(P+'2.1',H,'osmosis needs membrane'),n(P+'5.0',H,'carrier proteins')]),
'7.4':(1,[n(P+'4.1',E,'depends on respiration')]),
}
out={P+k:{"cost":c,"needs":v} for k,(c,v) in d.items()}
open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio25-s1.json','w').write(json.dumps(out,indent=1))
pk=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio25-s1.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
t=pk.split('CANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',t,re.M)
r=json.load(open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio25-s1.json'))
assert list(r)==tids,(set(tids)^set(r))
L=[x for v in r.values() for x in v['needs']]
assert all(x['id'] in allids for x in L)
assert all(k!=x['id'] for k,v in r.items() for x in v['needs'])
print(len(r),len(L),sum(v['cost']==2 for v in r.values()),sum(x['confidence']=='low' for x in L))
