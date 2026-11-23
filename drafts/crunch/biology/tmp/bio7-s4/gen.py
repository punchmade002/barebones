import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio7-s4.txt').read()
tgt=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
E,H='essential','helpful'
# id: (cost, [(need, strength, why, conf)])
S={
'0.b':(1,[]),
'0.0':(1,[('bio7-s2.6.3',H,'SEM as a microscope type','high')]),
'0.1':(1,[('bio7-s3.9.1',H,'plant-only cell structures','high')]),
'0.2':(1,[('bio2-s2.0.1',E,'independent variable definition','high')]),
'0.3':(1,[('bio2-s2.0.2',E,'dependent variable definition','high')]),
'0.4':(1,[('bio2-s2.0.3',E,'controlled variables','high')]),
'0.5':(2,[('bio2-s2.2.1',E,'control experiment idea','high'),('bio7-s2.5.0',H,'wet mount technique','high')]),
'1.b':(1,[]),
'1.0':(2,[('bio7-s2.5.0',H,'slides, coverslips, wet mount','low')]),
'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[('bio7-s2.5.0',H,'coverslip and slide','low')]),
'1.5':(1,[('bio7-s2.4.3',H,'sunlight hazard to eye','high')]),
'2.b':(1,[('bio7-s2.5.3',H,'lowering the coverslip','high')]),
'2.0':(1,[('bio7-s2.5.0',H,'wet mount','high')]),
'2.1':(1,[]),'2.2':(1,[]),
'2.3':(1,[('bio7-s2.5.1',H,'specimen one cell thick','high')]),
'2.4':(1,[('bio7-s2.5.2',H,'iodine stain for plant cells','high')]),
'2.5':(1,[('bio7-s2.5.3',E,'45 degree coverslip technique','high')]),
'2.6':(1,[('bio2-s2.2.1',H,'control set-up','high')]),
'2.7':(2,[('bio7-s2.3.7',H,'change objective, fine focus','high'),('bio7-s2.0.3',H,'total magnification','high')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(1,[('bio7-s2.5.2',H,'methylene blue for animal cells','high')]),
'3.4':(1,[('bio7-s2.5.3',H,'lowering the coverslip','high')]),
'3.5':(1,[('bio2-s2.2.1',H,'control set-up','high')]),
'3.6':(1,[('bio7-s2.3.7',H,'switching to high power','high')]),
'3.7':(1,[]),
'4.b':(1,[('bio7-s3.3.0',E,'chloroplast structure and function','high')]),
'4.0':(1,[('bio7-s2.5.1',H,'thin specimen for light','high')]),
'4.1':(1,[('bio7-s3.3.6',H,'chloroplasts visible as green discs','high')]),
'5.b':(1,[]),
'5.0':(1,[('bio7-s3.0.2',H,'cell wall in plants','high')]),
'5.1':(2,[('bio7-s3.1.2',E,'large central vacuole','high'),('bio7-s2.5.2',H,'iodine stains nucleus','high')]),
'5.2':(1,[('bio7-s3.3.5',E,'no chloroplasts in onion bulb','high')]),
'5.3':(1,[('bio7-s3.0.3',H,'cell membrane','high')]),
'5.4':(1,[('bio7-s2.5.2',H,'methylene blue stains nucleus','high')]),
'5.5':(2,[('bio7-s2.5.2',H,'stains add contrast','high'),('bio7-s4.0.5',H,'unstained control','high')]),
'5.6':(2,[('bio7-s2.7.3',E,'structures needing electron microscope','high')]),
'5.7':(1,[('bio7-s3.9.6',H,'labelled plant cell structures','low')]),
'6.b':(1,[('bio7-s2.6.3',H,'SEM','high')]),
'6.0':(1,[('bio7-s2.6.3',H,'SEM images','high')]),
'6.1':(1,[('bio7-s2.0.1',E,'resolution','high'),('bio7-s2.6.3',H,'SEM gives 3D surfaces','high')]),
'6.2':(1,[('bio7-s2.6.3',H,'SEM surface images','low')]),
'6.3':(2,[('bio7-s2.6.2',H,'TEM shows internal structure','high'),('bio7-s2.6.1',E,'dead specimens, false colour','high')]),
'6.4':(2,[('bio7-s2.0.0',E,'magnification definition','high')]),
'6.5':(2,[('bio7-s4.6.4',E,'size formula','high')]),
'6.6':(2,[('bio7-s4.6.4',H,'size calculation from image','high')]),
'6.7':(2,[('bio7-s2.7.5',H,'light vs electron microscope trade-offs','high')]),
'7.b':(1,[]),
'7.0':(1,[('bio7-s3.2.3',H,'eukaryotic cells have nucleus','high')]),
'7.1':(2,[('bio7-s3.0.1',E,'wall gives shape, turgor','high'),('bio7-s3.1.3',E,'vacuole keeps cell turgid','high')]),
'7.2':(1,[]),'7.3':(1,[]),
'7.4':(1,[('bio7-s3.3.5',H,'bulb cells lack chloroplasts','high')]),
'8.b':(1,[]),
'8.0':(1,[('bio7-s2.5.3',E,'45 degree coverslip technique','high')]),
'8.1':(1,[('bio7-s2.5.1',H,'thin specimen needed','high')]),
'8.2':(1,[('bio7-s2.5.2',H,'stains add contrast','high')]),
'8.3':(1,[('bio7-s2.5.4',H,'coverslip stops drying out','low')]),
'8.4':(1,[('bio7-s2.2.2',H,'diaphragm controls light','high'),('bio7-s2.1.4',H,'fine focus at high power','high')]),
'8.5':(2,[('bio2-s2.5.3',H,'sample size and variation','low')]),
}
out={}
for i in tids:
    k=i.replace('bio7-s4.','')
    c,n=S[k]
    out[i]={'cost':c,'needs':[{'id':a,'strength':s,'why':w,'confidence':f} for a,s,w,f in n]}
json.dump(out,open(P+'point-links/bio7-s4.json','w'),indent=1)
d=json.load(open(P+'point-links/bio7-s4.json'))
assert list(d)==tids and len(S)==len(tids)
for v in d.values():
    for n in v['needs']: assert n['id'] in allids and n['id'] not in d.get('x',{})
ln=sum(len(v['needs']) for v in d.values())
print(len(d),ln,sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
