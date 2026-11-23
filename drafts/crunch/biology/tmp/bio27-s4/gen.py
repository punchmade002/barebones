import json,re
H,L='high','low'
def n(i,s,w,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
E,P='essential','helpful'
d={
"bio27-s4.0.b":(1,[]),
"bio27-s4.0.0":(1,[n("bio27-s3.0.1",P,"digested food becomes small units")]),
"bio27-s4.0.1":(1,[n("bio25-s1.1.7",P,"large surface area speeds diffusion")]),
"bio27-s4.0.2":(1,[n("bio27-s4.0.1",E,"surface area increase")]),
"bio27-s4.0.3":(1,[n("bio25-s1.1.6",E,"short distance speeds diffusion")]),
"bio27-s4.0.4":(2,[n("bio25-s1.1.0",E,"concentration gradient and diffusion")]),
"bio27-s4.0.5":(1,[n("bio27-s4.0.4",E,"keeping gradient steep")]),
"bio27-s4.1.b":(1,[]),
"bio27-s4.1.0":(1,[n("bio27-s4.0.2",P,"villus structure")]),
"bio27-s4.1.1":(2,[n("bio25-s1.4.2",E,"mitochondria supply ATP for active transport"),n("bio25-s1.4.0",P,"active transport definition",L)]),
"bio27-s4.1.2":(1,[n("bio27-s4.0.2",P,"villus lining cells")]),
"bio27-s4.1.3":(2,[n("bio27-s4.0.2",E,"villus and microvilli"),n("bio27-s4.1.0",E,"lacteal"),n("bio27-s4.3.0",P,"hepatic portal vein",L)]),
"bio27-s4.2.b":(1,[]),
"bio27-s4.2.0":(2,[n("bio25-s1.4.0",E,"active transport against gradient"),n("bio25-s1.1.0",E,"diffusion"),n("bio27-s3.0.1",P,"digestion products")]),
"bio27-s4.2.1":(2,[n("bio27-s3.0.1",E,"fatty acids and glycerol products"),n("bio27-s4.1.0",E,"lacteal absorbs fats"),n("bio25-s1.0.2",P,"lipid membrane permeability",L)]),
"bio27-s4.2.2":(1,[n("bio27-s4.1.0",E,"lymph and lacteal"),n("bio27-s4.2.1",P,"fats enter lacteal")]),
"bio27-s4.2.3":(1,[n("bio25-s1.2.0",E,"osmosis"),n("bio27-s4.7.1",P,"large intestine water absorption",L)]),
"bio27-s4.2.4":(1,[n("bio25-s1.4.0",P,"active transport"),n("bio25-s1.1.0",P,"diffusion")]),
"bio27-s4.3.b":(1,[]),
"bio27-s4.3.0":(1,[n("bio27-s4.0.2",P,"villi capillaries"),n("bio29-s2.6.0",P,"portal system",L)]),
"bio27-s4.3.1":(2,[n("bio29-s2.6.0",E,"portal system definition"),n("bio27-s4.3.0",E,"hepatic portal vein")]),
"bio27-s4.3.2":(1,[n("bio27-s4.3.0",E,"hepatic portal vein blood")]),
"bio27-s4.3.3":(2,[n("bio27-s4.3.0",E,"portal vein to liver"),n("bio27-s4.4.0",P,"liver stores glucose as glycogen",L)]),
"bio27-s4.3.4":(1,[n("bio27-s4.3.0",E,"hepatic portal vein route"),n("bio29-s2.5.5",P,"liver blood supply")]),
"bio27-s4.3.5":(1,[n("bio27-s4.2.1",E,"fats absorbed into lacteal"),n("bio27-s4.3.0",P,"hepatic portal vein")]),
"bio27-s4.4.b":(1,[]),
"bio27-s4.4.0":(2,[n("bio27-s4.3.3",P,"liver processes absorbed glucose",L),n("bio8-s3.0.4",E,"glycogen storage polysaccharide")]),
"bio27-s4.4.1":(1,[n("bio27-s4.4.0",E,"glycogen stored in liver")]),
"bio27-s4.4.2":(1,[n("bio27-s4.4.0",E,"glycogen storage"),n("bio8-s3.1.2",P,"fat stored in adipose tissue")]),
"bio27-s4.4.3":(1,[]),
"bio27-s4.5.b":(1,[]),
"bio27-s4.5.0":(1,[n("bio27-s4.2.0",P,"amino acids absorbed"),n("bio8-s3.3.0",P,"proteins as enzymes",L)]),
"bio27-s4.5.1":(2,[n("bio27-s4.5.0",E,"amino acids"),n("bio8-s3.3.6",P,"deamination and urea")]),
"bio27-s4.5.2":(1,[n("bio27-s4.5.1",E,"amino group removed")]),
"bio27-s4.5.3":(1,[n("bio27-s4.5.2",E,"ammonia")]),
"bio27-s4.5.4":(1,[n("bio27-s4.5.3",E,"urea formed in liver")]),
"bio27-s4.5.5":(1,[n("bio27-s4.5.1",E,"deamination leaves non-nitrogen part"),n("bio8-s3.0.0",P,"glucose respired for energy",L)]),
"bio27-s4.5.6":(1,[n("bio27-s4.5.4",E,"urea excreted by kidneys"),n("bio27-s4.5.1",E,"deamination")]),
"bio27-s4.6.b":(1,[]),
"bio27-s4.6.0":(1,[n("bio27-s3.3.0",P,"bile made in liver"),n("bio27-s3.3.4",P,"bile pigments from red blood cells",L)]),
"bio27-s4.7.b":(1,[]),
"bio27-s4.7.0":(1,[n("bio27-s4.0.0",P,"small intestine absorbs most food")]),
"bio27-s4.7.1":(1,[n("bio25-s1.2.0",E,"osmosis"),n("bio27-s4.7.0",P,"watery material entering colon")]),
"bio27-s4.7.2":(1,[n("bio27-s4.7.0",P,"undigested fibre in colon")]),
"bio27-s4.7.3":(2,[n("bio27-s4.7.1",E,"faeces formed in colon"),n("bio27-s4.0.5",P,"peristalsis")]),
"bio27-s4.7.4":(1,[n("bio27-s4.7.1",E,"water absorption in colon"),n("bio27-s4.7.3",P,"faeces movement")]),
"bio27-s4.7.5":(1,[n("bio27-s4.7.1",E,"water absorption in colon")]),
}
out={k:{"cost":c,"needs":v} for k,(c,v) in d.items()}
p='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(p+'points/bio27-s4.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith('bio27-s4.')]
assert list(out)==tg,(set(tg)^set(out))
idset=set(ids)
for k,v in out.items():
    for x in v['needs']:
        assert x['id'] in idset and x['id']!=k,(k,x['id'])
json.dump(out,open(p+'point-links/bio27-s4.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
