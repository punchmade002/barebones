import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c): return {"id":i,"strength":s,"why":w,"confidence":c}
P='hom-housing-s6.'
S2='hom-home-services-s2.'
S6='hom-home-services-s6.'
I='hom-home-interior-s1.'
g={
'0.b':(1,[]),
'0.0':(2,[L(I+'0.b','helpful','elements of design','high')]),
'0.1':(1,[]),
'0.2':(1,[L(S2+'9.1','helpful','passive solar gain','low')]),
'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),
'1.7':(2,[L(P+'1.5','helpful','flexibility for future needs','high'),L(P+'1.6','helpful','accessibility','high')]),
'2.b':(1,[]),
'2.0':(2,[L(S6+'0.0','helpful','how heat is lost','high')]),
'2.1':(2,[L(S2+'6.0','helpful','heating controls and zoning','high')]),
'2.2':(2,[L(P+'0.2','helpful','passive solar gain','high')]),
'2.3':(1,[L(P+'2.b','essential','uses BER','high')]),
'2.4':(2,[L(P+'2.3','helpful','BER rating scale','high')]),
'2.5':(2,[L(P+'2.3','helpful','BER rating','high')]),
'2.6':(1,[L(P+'2.0','helpful','insulation and glazing','high'),L(P+'2.3','helpful','BER rating','high')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'3.4':(2,[L(P+'2.1','helpful','zoned heating','high')]),
'3.5':(1,[]),'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(2,[]),
'4.1':(1,[]),
'4.2':(1,[L(P+'4.1','helpful','maintenance costs','high')]),
'4.3':(1,[L(P+'4.0','helpful','initial costs','high')]),
'4.4':(1,[L(P+'4.1','helpful','maintenance costs','low')]),
'5.b':(1,[]),
'5.0':(2,[]),
'5.1':(1,[L(P+'5.0','essential','Building Regulations','high')]),
'5.2':(1,[L(P+'5.0','essential','Building Regulations','high')]),
'5.3':(2,[L(P+'5.0','essential','Building Regulations','high')]),
'5.4':(2,[L(P+'5.3','essential','commencement notice and certifiers','high')]),
'5.5':(1,[]),
'5.6':(1,[L(P+'5.5','essential','structural defects warranty','high')]),
'5.7':(1,[L(P+'2.0','helpful','insulation measures','low')]),
'5.8':(1,[L(P+'5.0','helpful','Building Regulations','high')]),
}
f='hom-housing-s6.t1g1.txt'
t=open(B+'packs/'+f).read()
tid=re.findall(r'^\[([^\]]+)\]',t.split('\nCANDIDATES')[0],re.M)
allid=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
assert [P+k for k in g]==tid
res={P+k:{"cost":c,"needs":n} for k,(c,n) in g.items()}
for k,v in res.items():
    for n in v['needs']: assert n['id'] in allid and n['id']!=k,(k,n)
json.dump(res,open(B+'point-links/hom-housing-s6.t1g1.json','w'),indent=1)
print(len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
