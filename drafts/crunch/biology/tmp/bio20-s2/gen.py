import json,re
P='bio20-s2'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
E_,H='essential','helpful'
d={
"0.b":(1,[n("bio20-s1.0.0",H,"hormone definition")]),
"0.0":(1,[n("bio20-s1.0.0",E_,"what a hormone is")]),
"0.1":(1,[n("bio20-s2.0.0",H,"manipulation definition")]),
"0.2":(1,[]),
"1.b":(1,[]),
"1.0":(1,[n("bio20-s1.7.2",H,"testosterone effects on muscle")]),
"1.1":(1,[n("bio20-s2.1.0",H,"what steroids are")]),
"1.2":(1,[n("bio20-s2.1.0",E_,"steroids as testosterone derivatives")]),
"1.3":(1,[n("bio20-s2.1.0",E_,"steroids as male hormone")]),
"1.4":(1,[n("bio20-s1.0.0",H,"hormone as messenger")]),
"1.5":(1,[n("bio20-s2.1.4",E_,"EPO raises red cells")]),
"1.6":(1,[n("bio20-s2.1.5",H,"extra red cells from EPO")]),
"1.7":(1,[]),
"2.b":(1,[]),
"2.0":(1,[n("bio20-s1.6.2",E_,"insulin lowers blood glucose")]),
"2.1":(2,[n("bio20-s2.2.0",E_,"insulin treatment")]),
"2.2":(1,[n("bio20-s1.8.1",H,"oestrogen as female hormone")]),
"2.3":(2,[n("bio20-s1.2.0",E_,"FSH function"),n("bio20-s1.2.1",E_,"LH causes ovulation"),n("bio20-s2.2.2",H,"pill hormones")]),
"2.4":(1,[n("bio20-s1.2.0",H,"FSH stimulates egg development")]),
"2.5":(2,[n("bio20-s1.8.1",E_,"oestrogen and its roles"),n("bio23-s6.12.0",H,"menopause definition")]),
"2.6":(1,[n("bio20-s2.2.5",E_,"what HRT is")]),
"2.7":(1,[n("bio20-s1.3.1",E_,"thyroxine function")]),
"3.b":(1,[]),
"3.0":(1,[n("bio20-s1.8.3",H,"progesterone as ovary hormone")]),
"3.1":(1,[]),
"3.2":(1,[n("bio20-s2.3.1",H,"growth hormone use in cattle")]),
"3.3":(1,[n("bio20-s2.3.2",E_,"BST use")]),
"3.4":(2,[]),
"3.5":(1,[]),
"3.6":(1,[]),
"4.b":(1,[]),
"4.0":(1,[n("bio20-s2.2.0",H,"insulin example")]),
"4.1":(2,[n("bio20-s2.1.1",H,"steroid side effects")]),
}
out={}
for k,v in d.items():
    out[f"{P}.{k}" if not k.endswith('.b') or True else k]={"cost":v[0],"needs":v[1]}
out={f"{P}.s{k}".replace(f"{P}.s",f"{P}.") if False else f"{P}.{k}":v for k,v in out.items()}
json.dump(out,open(f"/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/{P}.json","w"),indent=1)
pk=open(f"/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/{P}.txt").read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
t=[i for i in ids if i.startswith(P+'.')]
o=json.load(open(f"/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/{P}.json"))
print(list(o)==t,len(o),all(x['id'] in ids and x['id']!=k for k,v in o.items() for x in v['needs']))
print(sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for v in o.values() for x in v['needs']))
