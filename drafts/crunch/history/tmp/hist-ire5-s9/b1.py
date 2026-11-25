import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
pk=open(P+'packs/hist-ire5-s9.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=[]
for l in pk.split('CANDIDATES')[0].splitlines():
    m=re.match(r'\[([^\]]+)\]',l)
    if m: tg.append(m.group(1))
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
p='hist-ire5-s9.'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(2,[]),'0.2':(2,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[]),'1.0':(2,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[L('hist-ire5-s2.0.0','helpful','uses Ulster Unionist Party and Stormont')]),
'1.5':(1,[L(p+'1.1','helpful','uses the Twelfth parades')]),'1.6':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L(p+'2.0','helpful','uses the GAA'),L('hist-ire5-s4.0.4','helpful','uses RUC',"low")]),
'2.2':(1,[L(p+'1.b','helpful','paralleled the Orange Order')]),
'2.3':(1,[]),'2.4':(1,[]),
'2.5':(1,[L('hist-ire5-s2.0.0','helpful','uses Stormont government')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(2,[]),
'3.2':(2,[L(p+'3.1','helpful','compared with Corrymeela')]),
'3.3':(1,[]),
'3.4':(1,[L(p+'3.3','helpful','contrast with Ballymascanlon'),L('hist-ire5-s4.4.0','helpful','uses the IRA','low')]),
'3.5':(1,[]),'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(1,[L(p+'5.0','helpful','Paisley and Free Presbyterian Church')]),
'4.1':(1,[L(p+'4.0','helpful','Paisley hostility to church contacts')]),
'4.2':(1,[]),
'4.3':(1,[L(p+'0.5','helpful','uses separation of communities')]),
'4.4':(2,[L(p+'4.3','helpful','mixed marriage disapproval')]),
'4.5':(1,[L(p+'0.6','helpful','uses sectarianism')]),
'4.6':(2,[L(p+'3.b','helpful','what ecumenism achieved')]),
'5.b':(1,[L(p+'4.0','helpful','Paisley opposed ecumenism')]),
'5.0':(1,[]),
'5.1':(2,[L('hist-ire5-s2.0.0','helpful','uses Stormont')]),
'5.2':(1,[L(p+'4.1','helpful','same 1966 march')]),
'5.3':(1,[L(p+'3.5','helpful','Pope John Paul II','low')]),
'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(2,[]),
'6.2':(2,[L(p+'6.1','helpful','North among his collections')]),
'6.3':(2,[]),
'6.4':(1,[L(p+'7.0','helpful','Field Day company')]),
'6.5':(1,[L(p+'6.2','essential','criticises the collection North')]),
'6.6':(1,[L(p+'7.0','helpful','Field Day pamphlet')]),
'6.7':(1,[L(p+'6.2','helpful','his Troubles poetry','low')]),
'7.b':(1,[]),'7.0':(2,[]),
'7.1':(2,[L(p+'7.0','helpful','Field Day first production')]),
'7.2':(1,[]),'7.3':(2,[]),'7.4':(1,[]),
'7.5':(1,[L('hist-ire5-s4.2.1','helpful','Free Derry barricades','low')]),
'7.6':(1,[]),
'7.7':(1,[L(p+'7.0','essential','criticises Field Day')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L(p+'0.4','helpful','cultural traditions defined')]),
'8.2':(1,[]),
'8.3':(1,[L(p+'8.1','helpful','Cultural Heritage themes')]),
'8.4':(1,[L(p+'8.1','helpful','equal recognition of traditions')]),
'9.b':(1,[]),
'9.0':(1,[L(p+'3.1','helpful','Corrymeela'),L(p+'3.3','helpful','Ballymascanlon'),L(p+'3.4','helpful','Feakle')]),
'9.1':(1,[L(p+'4.0','essential','Paisley hardline opposition')]),
'9.2':(1,[L(p+'6.b','helpful','Heaney poetry'),L(p+'7.0','helpful','Field Day')]),
'9.3':(1,[L(p+'6.b','helpful','uses Heaney')]),
'9.4':(1,[]),'9.5':(1,[L(p+'0.0','helpful','nationalists and united Ireland')]),'9.6':(1,[]),
}
out={}
for t in tg:
    k=t[len(p):]
    c,n=D[k]; out[t]={"cost":c,"needs":n}
assert set(D)=={t[len(p):] for t in tg},set(D)^{t[len(p):] for t in tg}
for v in out.values():
    for n in v['needs']: assert n['id'] in ids
json.dump(out,open(P+'point-links/hist-ire5-s9.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
