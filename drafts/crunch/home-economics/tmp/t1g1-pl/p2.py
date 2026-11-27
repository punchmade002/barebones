import json
P='hom-work-leisure-s7.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
ids=['0.b']+['0.%d'%i for i in range(7)]+['1.b']+['1.%d'%i for i in range(8)]+['2.b','2.0','2.1','2.2','3.b']+['3.%d'%i for i in range(5)]+['4.b']+['4.%d'%i for i in range(7)]+['5.b']+['5.%d'%i for i in range(6)]+['6.b']+['6.%d'%i for i in range(7)]+['7.b']+['7.%d'%i for i in range(8)]+['8.b']+['8.%d'%i for i in range(6)]+['9.b','9.0','9.1','9.2','10.b','10.0','10.1']+['11.b']+['11.%d'%i for i in range(7)]
c2={'0.1','6.4','7.1'}
links={
'0.1':[L(P+'0.0','helpful','uses residual time after essentials')],
'0.4':[L(P+'0.2','helpful','uses freely chosen leisure'),L('hom-work-leisure-s1.0.4','helpful','home activities as unpaid work','low')],
'1.7':[L('hom-work-leisure-s1.3.5','helpful','work-life balance conditions','low')],
'2.0':[L(P+'1.1','helpful','uses physical wellbeing benefit','low')],
'3.2':[L(P+'1.5','helpful','repeats family bonding benefit')],
'6.0':[L('hom-work-leisure-s1.3.1','helpful','socio-economic group and work','low')],
'7.2':[L(P+'7.0','helpful','uses disposable income')],
'7.6':[L('hom-work-leisure-s1.3.5','helpful','part-time, job-sharing, flexitime','low')],
'8.1':[L(P+'7.0','helpful','uses disposable income')],
'8.3':[L(P+'7.0','helpful','uses disposable income')],
'9.1':[L('hom-work-leisure-s1.0.3','helpful','unpaid household and caring work')],
'11.2':[L(P+'0.1','essential','uses essential activities list')],
'11.3':[L(P+'0.0','helpful','leisure as residual time')],
'11.4':[L(P+'7.1','helpful','uses cost of leisure items')],
'11.5':[L(P+'4.b','helpful','physical and social development'),L(P+'5.b','helpful','emotional and intellectual development')],
'11.6':[L(P+'8.b','essential','uses life cycle stages')],
}
d={P+i:{"cost":2 if i in c2 else 1,"needs":links.get(i,[])} for i in ids}
json.dump(d,open('../../point-links/hom-work-leisure-s7.t1g1.json','w'),indent=1)
