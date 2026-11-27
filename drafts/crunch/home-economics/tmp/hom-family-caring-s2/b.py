import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-family-caring-s2.t1g1'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
F='hom-family-caring-s2.'
S='hom-sociological-concepts-s3.'
R='hom-family-caring-s1.'
# explicit: id -> (cost, needs)
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),
'2.b':(1,[]),
'2.0':(1,[n(F+'1.b','helpful','psychological needs being met')]),
'2.1':(1,[n(F+'1.3','helpful','uses self-esteem')]),
'3.b':(1,[]),'3.0':(2,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),'3.6':(1,[]),'3.7':(1,[]),
'4.b':(1,[]),
'4.0':(1,[n(F+'1.1','helpful','security from dependable caregiving')]),
'4.1':(1,[]),'4.2':(1,[]),
'4.3':(1,[n(F+'0.4','helpful','health care and check-ups')]),
'4.4':(1,[n(F+'1.2','helpful','attachment to caregiver')]),
'4.5':(1,[n(S+'3.1','helpful','primary socialisation process')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),'6.6':(1,[]),'6.7':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'7.4':(2,[n(F+'7.3','helpful','Child Care Act duty to protect'),n(F+'5.4','helpful','Tusla child-protection role')]),
'8.b':(1,[]),
'8.0':(1,[n(F+'3.2','helpful','adolescent need for independence')]),
'8.1':(1,[n(S+'0.7','helpful','peer group influence','low')]),
'8.2':(1,[]),'8.3':(1,[]),'8.4':(1,[]),'8.5':(1,[]),
'9.b':(1,[]),
'9.0':(1,[n(R+'1.6','helpful','disciplinarian role','low')]),
'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[]),'9.4':(1,[]),
'9.5':(1,[n(F+'3.2','helpful','independence and gradual freedom')]),
'10.b':(1,[]),
'10.0':(1,[n(F+'8.5','helpful','curfew as common flashpoint')]),
'10.1':(1,[n(F+'12.0','helpful','active listening without interrupting')]),
'10.2':(1,[]),
'10.3':(1,[n(F+'9.2','helpful','negotiation and compromise')]),
'10.4':(1,[n(F+'9.2','helpful','trial period compromise')]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[]),'11.2':(1,[]),'11.3':(1,[]),'11.4':(1,[]),'11.5':(1,[]),'11.6':(1,[]),'11.7':(1,[]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[]),'12.2':(1,[]),'12.3':(1,[]),
}
txt=open(H+'packs/'+P+'.txt').read()
tgt=[];allids=set()
sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='t'
    elif l.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[(\S+?)\]',l)
    if m:
        allids.add(m.group(1))
        if sec=='t': tgt.append(m.group(1))
out={}
for t in tgt:
    k=t[len(F):]
    assert k in d,k
    out[t]={"cost":d[k][0],"needs":d[k][1]}
assert len(d)==len(tgt)
for v in out.values():
    for x in v['needs']: assert x['id'] in allids,x
json.dump(out,open(H+'point-links/'+P.replace('.txt','')+'.json','w'),indent=1)
L=sum(len(v['needs']) for v in out.values())
print(len(out),L,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
