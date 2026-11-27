import json
C='hom-food-industry-s1.'
S='hom-food-industry-s3.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={}
def a(k,c,*needs): d[S+k]={"cost":c,"needs":list(needs)}
a('0.b',1)
a('0.0',1,n(C+'0.0','helpful','primary sector producers'))
a('0.1',2,n(C+'0.1','helpful','secondary sector processing'))
a('0.2',1,n(C+'0.1','helpful','secondary sector processing','low'))
a('0.3',1); a('0.4',1); a('0.5',1); a('0.6',1); a('0.7',1)
a('1.b',1); a('1.0',1); a('1.1',1); a('1.2',1); a('1.3',1); a('1.4',1)
a('1.5',1,n(C+'0.5','helpful','export markets','low'))
a('2.b',1)
a('2.0',2); a('2.1',1)
a('2.2',1,n(S+'2.0','helpful','contrast with protected dietitian title'))
a('2.3',1); a('2.4',2); a('2.5',1)
a('2.6',2,n(C+'1.4.8' if False else C+'4.8','helpful','Department of Agriculture role'))
a('3.b',1)
a('3.0',2)
a('3.1',2,n(C+'4.0','helpful','Bord Bia role','low'))
a('3.2',2); a('3.3',1)
a('3.4',2)
a('3.5',1,n(C+'5.4','helpful','careers a business offers'))
json.dump(d,open('../../point-links/hom-food-industry-s3.t1g1.json','w'),indent=0)
