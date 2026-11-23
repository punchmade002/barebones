import json,re
P='points/bio22-s7.txt'
txt=open(P).read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=txt.split('CANDIDATES')[0]
targets=re.findall(r'^\[([^\]]+)\]',tg,re.M)
S='bio22-s7.';C='bio22-s6.'
H,L='high','low'
E,Hl='essential','helpful'
def n(i,s,w,c=H):return {"id":i,"strength":s,"why":w,"confidence":c}
d={
'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'1.0':(1,[n(S+'0.1',Hl,'animal-to-human transmission',L)]),
'1.1':(1,[]),
'1.2':(1,[n(C+'6.2',Hl,'symptom-free infectious carriers')]),
'1.3':(1,[]),
'1.4':(2,[n(C+'2.0',Hl,'droplet and aerosol spread')]),
'1.5':(1,[]),
'1.6':(1,[n(C+'8.4',Hl,'mutation producing SARS-CoV-2 variants')]),
'2.0':(2,[n(C+'4.5',Hl,'migrating birds carry avian influenza',L)]),
'2.1':(1,[n(C+'9.0',Hl,'mixing with human flu virus')]),
'2.2':(1,[]),
'2.3':(2,[]),
'2.4':(2,[]),
'2.5':(2,[n(S+'2.3',Hl,'fruit bats as reservoir',L)]),
'2.6':(1,[n(S+'2.5',E,'Nipah outbreak being controlled')]),
'2.7':(2,[n(C+'2.6',Hl,'biting midges as vectors')]),
'2.8':(1,[n(S+'2.7',E,'Schmallenberg virus')]),
'3.0':(1,[]),
'3.1':(1,[n(S+'3.0',E,'ToBRFV identity')]),
'3.2':(1,[n(C+'2.3',Hl,'indirect contact via hands and tools')]),
'3.3':(2,[n(C+'9.2',Hl,'mutation overcoming crop resistance')]),
'3.4':(2,[]),
'4.0':(2,[n(C+'13.0',Hl,'monoculture genetic uniformity')]),
'4.1':(2,[]),
'4.2':(1,[]),
'4.3':(1,[n(C+'13.2',Hl,'reliance on one crop: Great Famine',L)]),
'5.0':(1,[]),
'5.1':(2,[n(S+'5.0',Hl,'self versus non-self')]),
'5.2':(2,[n(S+'5.1',E,'tolerance of self antigens')]),
'6.0':(1,[n(S+'5.0',E,'autoimmune disease definition')]),
'6.1':(1,[n(S+'5.0',E,'autoimmune disease definition')]),
'6.2':(1,[n(S+'5.0',E,'autoimmune disease definition')]),
'6.3':(2,[n(S+'5.0',E,'autoimmune disease definition')]),
'6.4':(1,[n(S+'5.0',E,'autoimmune disease definition')]),
'7.0':(1,[]),
'7.1':(2,[n(S+'5.2',Hl,'antibodies attacking self antigen')]),
'7.2':(1,[n(S+'7.1',E,'cross-reacting antibodies after infection')]),
'7.3':(1,[n(S+'7.1',Hl,'infection triggering autoimmunity',L)]),
'8.0':(1,[]),
'8.1':(2,[n(S+'5.1',Hl,'immune regulation',L)]),
'8.2':(1,[n(S+'5.0',Hl,'autoimmune disease definition')]),
'8.3':(2,[n(S+'6.0',Hl,'insulin replacement example',L)]),
'9.0':(1,[]),
'9.1':(1,[]),
'9.2':(2,[n(C+'15.0',E,'R0 meaning'),n(C+'6.0',Hl,'infectious period length')]),
'9.3':(2,[n(C+'18.2',E,'bringing R below 1')]),
'9.4':(2,[n(C+'19.0',E,'herd-immunity threshold')]),
'9.5':(1,[n(C+'8.3',Hl,'vaccines updated for mutation')]),
'10.0':(2,[n(C+'14.5',Hl,'reducing mobility reduces spread')]),
'10.1':(2,[n(C+'4.2',Hl,'trade moves plant pathogens',L)]),
'10.2':(1,[n(C+'13.0',E,'genetic uniformity in monocultures')]),
'10.3':(2,[n(C+'11.0',Hl,'misuse of antibiotics speeds resistance')]),
'10.4':(1,[n(S+'0.2',E,'spillover from wildlife contact')]),
'10.5':(1,[]),
'11.0':(1,[n(C+'15.0',E,'R0 meaning')]),
'11.1':(1,[]),
'12.0':(1,[]),'12.1':(1,[]),
'12.2':(1,[n(C+'12.0',E,'herd immunity')]),
'12.3':(1,[]),
'12.4':(1,[n(C+'3.2',Hl,'2001 foot-and-mouth epidemic')]),
'12.5':(1,[n(C+'13.2',Hl,'Irish Great Famine')]),
'12.6':(1,[n(C+'5.1',Hl,'chytrid amphibian decline')]),
'12.7':(1,[]),
'13.0':(1,[]),'13.1':(1,[]),'13.2':(1,[]),'13.3':(1,[]),'13.4':(1,[]),'13.5':(1,[]),
}
out={}
for t in targets:
    k=t[len(S):]
    out[t]=({"cost":1,"needs":[]} if k.endswith('.b') else {"cost":d[k][0],"needs":d[k][1]})
json.dump(out,open('point-links/bio22-s7.json','w'),indent=1)
o=json.load(open('point-links/bio22-s7.json'))
assert list(o)==targets and len(set(targets))==len(targets)
nd=[x for v in o.values() for x in v['needs']]
assert all(x['id'] in ids and x['id'] not in () for x in nd)
assert all(x['id']!=k for k,v in o.items() for x in v['needs'])
print(len(o),len(nd),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in nd))
