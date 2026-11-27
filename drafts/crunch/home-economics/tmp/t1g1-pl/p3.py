import json
P='hom-marriage-s4.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
ids=['0.b']+['0.%d'%i for i in range(6)]+['1.b']+['1.%d'%i for i in range(6)]+['2.b']+['2.%d'%i for i in range(6)]+['3.b']+['3.%d'%i for i in range(7)]+['4.b']+['4.%d'%i for i in range(7)]
c2={'1.2','3.2','3.3','4.5'}
links={
'2.2':[L('hom-marriage-s4.1.1','helpful','mediator helping reach terms','low')],
'2.4':[L(P+'3.0','helpful','nullity allows remarriage'),L(P+'4.b','helpful','divorce allows remarriage')],
'2.5':[L('hom-family-law-s4.0.b','essential','judicial separation court decree')],
'3.1':[L(P+'3.0','helpful','legal nullity decree')],
'3.2':[L('hom-marriage-s1.3.0','essential','void marriage meaning')],
'3.3':[L('hom-marriage-s1.3.1','essential','voidable marriage meaning')],
'3.5':[L(P+'3.4','helpful','church annulment meaning')],
'3.6':[L(P+'4.b','helpful','divorce ends valid marriage')],
'4.0':[L(P+'4.b','helpful','divorce Act 1996')],
'4.3':[L('hom-family-law-s1.0.b','helpful','maintenance for dependants','low')],
'4.5':[L('hom-family-law-s4.2.b','helpful','court orders on money, property, children')],
}
d={P+i:{"cost":2 if i in c2 else 1,"needs":links.get(i,[])} for i in ids}
json.dump(d,open('../../point-links/hom-marriage-s4.t1g1.json','w'),indent=1)
