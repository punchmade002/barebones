import json,re,sys
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
N='hom-unemployment-poverty-s7.t1g1'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
p='hom-personal-finance-s3.'; q='hom-consumer-rights-s1.'
q='hom-unemployment-poverty-s7.'
s4='hom-unemployment-poverty-s4.'
s6='hom-unemployment-poverty-s6.'
w='hom-work-leisure-s3.'
D={
'0.b':(1,[L(w+'2.b','helpful','voluntary work meaning','low')]),
'0.0':(1,[L(w+'2.b','helpful','volunteers','low')]),
'0.1':(1,[L(s6+'3.b','helpful','statutory body meaning')]),
'0.2':(1,[]),'0.3':(1,[]),
'1.b':(1,[L(s4+'0.b','helpful','risk of poverty')]),
'1.0':(1,[L(q+'0.0','helpful','voluntary organisation')]),
'1.1':(2,[]),'1.2':(1,[]),'1.3':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[L(s4+'5.b','helpful','groups at risk of poverty','low')]),
'2.3':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L(s6+'2.5','helpful','MABS service')]),
'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),
'4.2':(2,[L(s6+'3.7','helpful','Youthreach and VTOS')]),
'4.3':(1,[L(s6+'3.0','helpful','SOLAS role'),L(q+'4.2','helpful','ETBs')]),
'4.4':(1,[]),
'5.b':(1,[]),
'5.0':(1,[L(s6+'3.6','helpful','Community Employment scheme')]),
'5.1':(1,[]),'5.2':(1,[]),'5.3':(2,[]),
'5.4':(1,[L(s4+'0.2','helpful','social exclusion','low')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L(q+'6.b','helpful','surplus shared with members','low')]),
'6.2':(2,[]),
'6.3':(1,[L(q+'6.b','helpful','co-operative meaning')]),
'6.4':(1,[]),
'6.5':(1,[L(q+'6.b','helpful','member-owned business')]),
'6.6':(2,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),'7.4':(2,[]),'7.5':(1,[]),'7.6':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),
'8.2':(1,[L(q+'5.3','helpful','SICAP'),L(q+'1.b','helpful','SVP')]),
}
txt=open(P+'packs/'+N+'.txt').read().split('\n')
tg=[];cand=set();mode=None
for l in txt:
    if l.startswith('TARGET'):mode='t'
    elif l.startswith('CANDIDATES'):mode='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m: (tg.append(m.group(1)) if mode=='t' else cand.add(m.group(1)))
allids=set(tg)|cand
pre=tg[0].split('.')[0]+'.'
assert set(pre+k for k in D)==set(tg) and len(tg)==len(D),(set(tg)^set(pre+k for k in D))
out={}
for t in tg:
    c,n=D[t[len(pre):]]
    for x in n: assert x['id'] in allids and x['id']!=t,x
    out[t]={"cost":c,"needs":n}
json.dump(out,open(P+'point-links/'+N+'.json','w'),indent=1)
chk=json.load(open(P+'point-links/'+N+'.json'))
ls=[x for v in chk.values() for x in v['needs']]
print(len(chk),len(ls),sum(v['cost']==2 for v in chk.values()),sum(x['confidence']=='low' for x in ls))
