import json,re
P='bio20-s1.'
ids=re.findall(r'^\[(bio\d+-s\d+\.[\w.]+)\]',open('points/bio20-s1.txt').read(),re.M)
tg=[i for i in ids if i.startswith(P)]
cost2={'0.4','2.0','2.1','2.3','4.2','5.3'}
# k: (target, strength, why, conf)
L={
'0.1':[('0.0','helpful','hormone definition','high')],
'0.2':[('0.1','helpful','contrast with endocrine glands','high')],
'0.3':[('0.2','essential','exocrine gland meaning','high'),('0.1','essential','endocrine gland meaning','high')],
'1.0':[('1.b','helpful','pituitary controls other glands','high'),('3.1','helpful','thyroxine function','low')],
'1.2':[('1.1','essential','oxytocin','high')],
'2.0':[('8.1','helpful','oestrogen','low')],
'2.1':[('2.0','helpful','follicle','high')],
'2.2':[('2.0','essential','FSH action on testes','high'),('7.b','helpful','testosterone','high')],
'2.4':[('1.2','essential','made in hypothalamus, released from pituitary','high'),('2.3','essential','ADH action','high')],
'4.2':[('4.1','essential','parathyroid hormone raises calcium','high')],
'5.2':[('5.1','helpful','adrenaline fight or flight','high')],
'5.3':[('6.3','helpful','glycogen and glucose conversion','low')],
'5.4':[('5.1','helpful','adrenaline fight or flight','high')],
'6.1':[('0.1','helpful','secrete directly into blood','low')],
'6.2':[('6.1','helpful','insulin secreted by islets','high')],
'6.3':[('6.2','helpful','insulin lowers blood glucose','high')],
'7.1':[('7.b','helpful','testosterone','high')],
'7.2':[('7.1','helpful','puberty','high')],
'8.1':[('8.b','helpful','oestrogen','high')],
'8.3':[('8.2','essential','endometrium','high')],
'9.0':[('2.0','helpful','FSH functions','high')],
'9.1':[('2.1','helpful','LH functions','high')],
'9.2':[('1.1','helpful','oxytocin functions','high')],
'9.3':[('1.0','helpful','TSH function','high')],
'9.4':[('2.3','helpful','ADH function','high')],
'10.0':[('5.1','helpful','adrenaline function','high')],
'10.1':[('3.1','helpful','thyroxine metabolic rate','high')],
'10.2':[('4.1','helpful','parathyroid hormone','high')],
'10.3':[('6.2','helpful','insulin lowers glucose','high')],
'10.4':[('7.2','helpful','testosterone effects','high')],
'10.5':[('8.1','helpful','oestrogen effects','high')],
'10.6':[('8.3','helpful','progesterone effects','high')],
}
out={}
for t in tg:
    k=t[len(P):]
    out[t]={"cost":2 if k in cost2 else 1,"needs":[{"id":P+a,"strength":s,"why":w,"confidence":c} for a,s,w,c in L.get(k,[])]}
for v in out.values():
    for n in v['needs']: assert n['id'] in ids,n
json.dump(out,open('point-links/bio20-s1.json','w'),indent=1)
d=json.load(open('point-links/bio20-s1.json'))
assert list(d)==tg
n=[x for v in d.values() for x in v['needs']]
print(len(d),len(n),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for x in n))
