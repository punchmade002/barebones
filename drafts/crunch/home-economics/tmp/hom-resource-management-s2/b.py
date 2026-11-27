import json,re
P='hom-resource-management-s2.'
Q='hom-resource-management-s1.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful';E='essential'
d={
'0.b':(1,[n(Q+'0.1',H,'uses resources')]),
'0.0':(1,[]),
'0.1':(1,[n(P+'0.0',H,'contrast with needs')]),
'0.2':(1,[n(Q+'0.3',H,'goals defined')]),
'0.3':(1,[n(P+'0.2',H,'values shape goals')]),
'0.4':(2,[n(Q+'2.0',H,'human resources type')]),
'0.5':(2,[n(Q+'2.1',H,'material resources type')]),
'0.6':(1,[n(P+'0.2',H,'uses goals')]),
'1.b':(1,[n(P+'0.b',H,'inputs become outputs')]),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[n(P+'1.2',H,'implementing defined')]),
'1.4':(1,[]),'1.5':(1,[]),
'2.b':(1,[n(P+'0.2',H,'judged against goals')]),
'2.0':(1,[n(P+'0.2',H,'uses goals')]),
'2.1':(1,[n(P+'0.3',H,'uses values')]),
'2.2':(1,[]),'2.3':(2,[]),
'2.4':(1,[n(Q+'3.5',H,'feedback cycle')]),
'3.b':(1,[n(Q+'3.2',H,'one-off events use system')]),
'3.0':(2,[n(P+'0.b',H,'inputs components')]),
'3.1':(2,[n(P+'1.b',E,'throughputs components')]),
'3.2':(1,[n(P+'2.b',H,'outputs defined')]),
'3.3':(1,[n(P+'2.4',E,'feedback into next cycle')]),
'4.b':(1,[]),
'4.0':(2,[n(P+'0.2',H,'weigh against goals')]),
'4.1':(1,[n(P+'4.0',H,'review step')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'4.6':(1,[n(P+'0.3',H,'uses values')]),
'5.b':(1,[]),
'5.0':(2,[n(P+'1.b',H,'uses throughput stages')]),
'5.1':(1,[n(P+'2.4',H,'feedback evaluates outputs')]),
'5.2':(1,[]),'5.3':(1,[]),
'6.b':(1,[]),'6.0':(2,[]),'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[n(P+'6.2',H,'responsibility for tasks')]),
'6.4':(1,[]),'6.5':(1,[]),'6.6':(1,[]),
'7.b':(1,[n(Q+'0.1',H,'resource defined')]),
'7.0':(1,[]),
'7.1':(1,[n(P+'0.4',H,'human resources')]),
'7.2':(1,[]),
'7.3':(1,[n(P+'0.5',H,'material resources')]),
'7.4':(1,[n(P+'0.4',H,'human resources')]),
}
out={P+k:{"cost":c,"needs":v} for k,(c,v) in d.items()}
f='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
txt=open(f+'packs/hom-resource-management-s2.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert list(out)==tg,(set(tg)^set(out))
for v in out.values():
  for x in v['needs']: assert x['id'] in ids,x
json.dump(out,open(f+'point-links/hom-resource-management-s2.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),0)
