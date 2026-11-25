import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-ire3-s11.'
E,Hp='essential','helpful'
# id: (cost, [(id,strength,why,conf)])
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[('hist-ire3-s5.8.0',Hp,'Cumann na nGaedheal and Cosgrave','high')]),
'0.3':(1,[]),
'0.4':(1,[('hist-ire3-s5.0.b',Hp,'Treaty and Civil War background','high')]),
'0.5':(1,[]),
'1.b':(1,[('hist-ire3-s5.15.3',Hp,'de Valera took office March 1932','high')]),
'1.0':(1,[('hist-ire3-s5.14.1',Hp,'founding of Fianna Fáil','low')]),
'1.1':(1,[('hist-ire3-s11.0.2',Hp,'invitation came under Cosgrave','high')]),
'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),'1.7':(1,[]),
'2.b':(1,[('hist-ire3-s5.8.4',Hp,'Governor-General as Crown representative','high')]),
'2.0':(1,[('hist-ire3-s11.0.3',Hp,'Lauri and Byrne introduced','high')]),
'2.1':(1,[('hist-ire3-s5.8.4',E,'Governor-General and the oath','high')]),
'2.2':(1,[('hist-ire3-s6.2.0',Hp,'McNeill removed as Governor-General','high')]),
'2.3':(2,[('hist-ire3-s6.0.b',Hp,'sovereignty and Crown under Treaty','high')]),
'2.4':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'3.4':(1,[('hist-ire3-s11.1.4',Hp,'Athlone radio station','high')]),
'3.5':(1,[]),'3.6':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[('hist-ire3-s11.1.4',Hp,'radio and loudspeaker arrangements','high')]),
'4.2':(1,[]),
'4.3':(1,[('hist-ire3-s5.0.b',Hp,'the Civil War','high')]),
'4.4':(1,[]),'4.5':(1,[]),
'4.6':(1,[('hist-ire3-s11.1.4',Hp,'Athlone station','high')]),
'5.b':(1,[('hist-ire3-s3.0.b',Hp,'unionists and partition','high')]),
'5.0':(1,[]),'5.1':(1,[]),
'5.2':(1,[('hist-ire3-s3.0.b',Hp,'partition','high')]),
'5.3':(1,[]),'5.4':(1,[]),
'6.b':(2,[]),
'6.0':(2,[('hist-ire3-s6.5.b',Hp,'1937 constitution','high')]),
'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[('hist-ire3-s11.2.1',Hp,'Governor-General dispute','high')]),
'6.4':(1,[('hist-ire3-s11.5.2',Hp,'unionist fear of Catholic state','high')]),
'6.5':(1,[]),'6.6':(2,[]),
'6.7':(1,[('hist-ire3-s11.0.2',Hp,'Congress planned under Cosgrave','high')]),
'7.b':(1,[]),'7.0':(1,[('hist-ire3-s5.0.b',Hp,'the Civil War','high')]),
'7.1':(1,[]),'7.2':(1,[]),
'7.3':(1,[('hist-ire3-s11.5.2',Hp,'unionist reaction to Congress','high')]),
'7.4':(1,[]),'7.5':(1,[]),
}
txt=open(H+'packs/hist-ire3-s11.t1g1.txt').read()
tg=[]
sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='t'
    elif l.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[(hist-[^\]]+)\]',l)
    if m and sec=='t': tg.append(m.group(1))
allid=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
assert tg==[P+k for k in d],(set(tg)^set(P+k for k in d))
out={}
for k,(c,ns) in d.items():
    out[P+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in ns]}
    for i,*_ in ns: assert i in allid and i!=P+k,i
json.dump(out,open(H+'point-links/hist-ire3-s11.t1g1.json','w'),ensure_ascii=False,indent=1)
n=sum(len(v['needs']) for v in out.values())
print(len(out),n,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
