import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-education-s3.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[L(P+'0.1','helpful','uses Early Start programme')]),
'0.3':(1,[L(P+'0.0','helpful','free pre-school programme (ECCE)','low')]),
'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(2,[]),
'1.3':(1,[L(P+'1.2','helpful','state-funded versus private schools')]),
'1.4':(2,[]),'1.5':(1,[]),
'2.b':(1,[]),'2.0':(2,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(2,[]),'2.4':(2,[]),'2.5':(1,[]),
'3.b':(1,[]),
'3.0':(1,[L(P+'2.5','helpful','LCVP link module'),L(P+'2.1','helpful','Transition Year')]),
'3.1':(1,[]),'3.2':(1,[]),'3.3':(2,[]),'3.4':(1,[]),'3.5':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L(P+'2.3','helpful','grades converted to points')]),
'4.2':(2,[]),'4.3':(1,[]),'4.4':(1,[]),
'4.5':(1,[L(P+'4.1','helpful','points-based CAO entry')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),'6.6':(1,[]),'6.7':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),
}
txt=open(B+'packs/hom-education-s3.t1g1.txt').read()
ids=re.findall(r'^\[(hom-education-s3\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    c,n=D[i[len(P):]]; out[i]={"cost":c,"needs":n}
assert len(D)==len(ids)==len(out)
for v in out.values():
    for n in v['needs']: assert n['id'] in allids
json.dump(out,open(B+'point-links/hom-education-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
