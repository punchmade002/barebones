import json,re
pkg=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio22-s5.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pkg,re.M)
tg=[i for i in ids if i.startswith('bio22-s5.')]
S='bio22-s5.'
# id: (cost, [(need,strength,why,conf)])
E,H='essential','helpful'
spec={
'0.1':(1,[('bio29-s4.0.4',H,'stem cells in red marrow','high')]),
'0.3':(1,[('bio22-s2.3.0',H,'phagocytosis definition','high')]),
'0.6':(2,[('bio22-s2.0.1',H,'self vs non-self markers','high')]),
'1.0':(1,[(S+'0.4',H,'lymphocyte appearance for contrast','high')]),
'1.1':(1,[(S+'0.3',H,'monocytes as phagocytes','low')]),
'1.2':(1,[('bio22-s2.3.0',E,'phagocytosis','high')]),
'1.3':(2,[('bio22-s2.11.4',E,'antigen presentation','high')]),
'1.4':(1,[('bio22-s2.4.0',H,'inflammation','low')]),
'1.5':(1,[(S+'1.0',E,'monocyte vs lymphocyte nuclei','high')]),
'2.0':(1,[('bio22-s2.0.2',H,'innate immunity','high')]),
'2.1':(1,[('bio22-s2.0.1',H,'self markers','high')]),
'2.2':(2,[(S+'2.1',E,'normal self-marker proteins','high')]),
'2.3':(1,[('bio22-s2.7.0',H,'antibody definition','high')]),
'2.5':(1,[(S+'2.4',E,'apoptosis after perforin/granzymes','high')]),
'3.0':(1,[('bio22-s2.7.0',E,'antibody structure and function','high')]),
'3.1':(1,[('bio22-s2.9.1',H,'B cell humoral response','high')]),
'3.2':(2,[('bio22-s2.9.5',H,'plasma cells from B cells','high')]),
'3.3':(1,[('bio22-s2.9.1',H,'antibodies act in fluids','low')]),
'4.0':(2,[('bio22-s2.11.3',E,'antigen presentation','high')]),
'4.1':(1,[(S+'3.2',H,'plasma cells make antibodies','high')]),
'4.3':(2,[('bio22-s2.12.1',H,'cytokines','high')]),
'4.4':(1,[(S+'4.3',E,'helper T cell role','high')]),
'5.1':(1,[('bio22-s2.11.3',H,'antigen presentation','low')]),
'5.2':(2,[(S+'2.4',E,'perforin and granzymes','high')]),
'5.3':(2,[(S+'2.4',E,'NK killing method','high')]),
'5.4':(1,[(S+'5.2',H,'killing mechanism','low')]),
'6.1':(1,[('bio22-s2.13.1',H,'switching off response','high')]),
'6.2':(1,[(S+'0.6',H,'self-reactive lymphocytes','high')]),
'6.3':(2,[('bio22-s2.9.4',H,'clone of identical cells','high')]),
'6.4':(2,[(S+'6.3',E,'memory T cell formation','high')]),
'6.5':(1,[(S+'6.4',E,'memory cells give faster response','high')]),
'7.0':(1,[('bio22-s2.0.2',H,'innate immunity','high')]),
'7.1':(1,[('bio22-s2.0.3',H,'adaptive immunity','high')]),
'7.2':(2,[(S+'5.2',H,'perforin killing','low')]),
'7.3':(1,[(S+'4.3',H,'helper T signalling','high')]),
'7.4':(1,[(S+'6.1',H,'suppressor T cells','high')]),
'8.0':(1,[(S+'3.3',H,'antibodies act outside cells','high')]),
'8.1':(1,[(S+'5.2',H,'killing infected cells','low')]),
'8.2':(2,[(S+'4.0',H,'T cells need presented antigen','high')]),
'8.3':(1,[(S+'2.2',E,'missing self pattern','high')]),
'8.4':(1,[(S+'1.2',H,'macrophage phagocytosis','low')]),
'9.0':(1,[(S+'1.3',H,'macrophage roles','low')]),
'9.1':(1,[(S+'2.2',H,'NK killing','low')]),
'9.2':(1,[(S+'3.0',H,'B cell antibodies','low')]),
'9.3':(2,[(S+'4.3',H,'helper T activation','low')]),
'9.4':(2,[(S+'5.2',H,'killer T killing','low')]),
'9.5':(1,[(S+'6.1',H,'suppressor T role','low')]),
'9.6':(1,[(S+'6.4',H,'memory cells','low')]),
'10.0':(2,[('bio22-s2.5.1',H,'interferons','high')]),
'10.1':(2,[(S+'5.2',H,'killer T killing','low')]),
'10.2':(1,[(S+'6.4',H,'memory cells','low')]),
}
out={}
for i in tg:
    k=i[len(S):]
    c,n=spec.get(k,(1,[]))
    out[i]={"cost":c,"needs":[{"id":a,"strength":b,"why":w,"confidence":f} for a,b,w,f in n]}
# cost 2 for multi-step/complex extras
for k in ['2.4','0.6']: out[S+k]['cost']=2
assert all(n['id'] in ids and n['id']!=i for i,v in out.items() for n in v['needs'])
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio22-s5.json','w'),indent=1)
d=json.load(open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio22-s5.json'))
assert list(d)==tg
L=[n for v in d.values() for n in v['needs']]
print(len(d),len(L),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for n in L))
