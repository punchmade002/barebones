import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
"bio14-s5.0.b":(1,[]),
"bio14-s5.0.0":(1,[n("bio25-s1.0.2",H,"selectively permeable membrane","low")]),
"bio14-s5.0.1":(1,[n("bio7-s3.3.0",H,"thylakoids as chloroplast membrane sacs")]),
"bio14-s5.0.2":(1,[n("bio14-s5.0.1",E,"thylakoid structure")]),
"bio14-s5.0.3":(2,[n("bio14-s3.0.2",E,"pigment clusters and reaction centres"),n("bio14-s5.1.0",H,"electron transport chain")]),
"bio14-s5.0.4":(1,[n("bio7-s3.6.1",H,"ribosomes make proteins","low")]),
"bio14-s5.0.5":(1,[n("bio14-s5.0.4",E,"chloroplast DNA and ribosomes")]),
"bio14-s5.0.6":(1,[n("bio14-s5.0.2",H,"grana and lamellae structure","low")]),
"bio14-s5.1.b":(1,[]),
"bio14-s5.1.0":(1,[]),
"bio14-s5.1.1":(1,[n("bio14-s5.1.0",E,"electron transport chain")]),
"bio14-s5.1.2":(1,[n("bio14-s3.0.4",E,"reaction centre loses electron")]),
"bio14-s5.1.3":(2,[n("bio14-s3.1.2",E,"NADP+ forming NADPH")]),
"bio14-s5.1.4":(2,[n("bio14-s5.1.1",H,"protein complexes in membrane"),n("bio25-s1.1.0",H,"concentration gradient","low")]),
"bio14-s5.2.b":(1,[]),
"bio14-s5.2.0":(2,[n("bio14-s5.0.1",E,"thylakoid space"),n("bio14-s3.1.3",E,"photolysis of water")]),
"bio14-s5.2.1":(2,[n("bio14-s3.1.3",E,"photolysis equation"),n("bio14-s5.2.0",H,"protons build up in thylakoid space")]),
"bio14-s5.2.2":(2,[n("bio14-s5.2.0",E,"proton build-up in thylakoid space"),n("bio14-s3.1.1",H,"ATP made from ADP and Pi")]),
"bio14-s5.2.3":(1,[]),
"bio14-s5.3.b":(1,[]),
"bio14-s5.3.0":(1,[n("bio14-s5.0.2",E,"stacked thylakoids in grana"),n("bio14-s5.0.3",H,"what thylakoid membranes hold")]),
"bio14-s5.3.1":(1,[n("bio14-s3.0.2",E,"antenna complexes around reaction centre")]),
"bio14-s5.3.2":(2,[n("bio14-s5.2.0",E,"proton concentration in thylakoid space"),n("bio25-s1.0.2",H,"selective permeability","low")]),
"bio14-s5.3.3":(1,[n("bio14-s5.0.4",H,"stroma hosts light-independent reactions")]),
"bio14-s5.3.4":(1,[n("bio14-s5.0.4",E,"stroma enzymes and starch")]),
"bio14-s5.3.5":(1,[n("bio14-s5.0.5",E,"chloroplast makes own proteins")]),
"bio14-s5.3.6":(1,[n("bio7-s3.3.4",H,"chloroplasts in palisade cells","low")]),
"bio14-s5.3.7":(2,[n("bio14-s5.2.2",H,"ATP synthase and proton flow"),n("bio14-s5.1.1",H,"protein complexes and carriers","low")]),
}
json.dump({k:{"cost":c,"needs":v} for k,(c,v) in d.items()},open(P+'point-links/bio14-s5.json','w'),ensure_ascii=False,indent=1)
txt=open(P+'points/bio14-s5.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M)); tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
o=json.load(open(P+'point-links/bio14-s5.json'))
assert list(o)==tg,(set(tg)^set(o))
bad=[x['id'] for v in o.values() for x in v['needs'] if x['id'] not in ids or x['id'] in o and False]
assert not bad,bad
for k,v in o.items(): assert all(x['id']!=k for x in v['needs'])
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for v in o.values() for x in v['needs']))
