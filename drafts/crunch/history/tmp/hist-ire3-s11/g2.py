import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-ire3-s11.'
Hp='helpful'
ids="0.b 0.0 0.1 0.2 0.3 0.4 0.5 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 2.b 2.0 2.1 2.2 2.3 2.4 3.b 3.0 3.1 3.2 3.3 3.4 3.5 3.6 4.b 4.0 4.1 4.2 4.3 4.4 4.5 4.6 5.b 5.0 5.1 5.2 5.3 5.4 6.b 6.0 6.1 6.2 6.3 6.4 6.5 6.6 6.7 7.b 7.0 7.1 7.2 7.3 7.4 7.5".split()
L={
'0.5':[('hist-ire3-s10.3.0',Hp,'Church managed schools','high')],
'1.4':[('hist-ire3-s10.5.2',Hp,'state radio 2RN and Athlone','high')],
'3.4':[('hist-ire3-s10.5.2',Hp,'state radio station','high')],
'4.1':[('hist-ire3-s10.5.2',Hp,'state radio station','high')],
'4.6':[('hist-ire3-s10.5.2',Hp,'Athlone and Radio Éireann','high')],
'5.3':[('hist-ire3-s10.7.0',Hp,'Orange Order parades and culture','low')],
'6.0':[('hist-ire3-s10.4.b',Hp,'Catholic ethos of social legislation','high')],
'6.1':[('hist-ire3-s10.0.3',Hp,'conformity and censorship','high')],
'6.6':[('hist-ire3-s10.0.3',Hp,'conformity of the 1930s','high')],
}
txt=open(H+'packs/hist-ire3-s11.t1g2.txt').read()
tg=[];sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'):sec='t'
    elif l.startswith('CANDIDATES'):sec='c'
    m=re.match(r'\[(hist-[^\]]+)\]',l)
    if m and sec=='t':tg.append(m.group(1))
allid=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
assert tg==[P+k for k in ids]
out={P+k:{'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in L.get(k,[])]} for k in ids}
for v in out.values():
    for x in v['needs']: assert x['id'] in allid
json.dump(out,open(H+'point-links/hist-ire3-s11.t1g2.json','w'),ensure_ascii=False,indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
