import json
C='hom-family-society-s1.'
S='hom-marriage-s1.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={}
def a(k,c,*needs): d[S+k]={"cost":c,"needs":list(needs)}
a('0.b',1); a('0.0',1); a('0.1',1); a('0.2',1); a('0.3',1)
a('1.b',1)
a('1.0',1,n(C+'0.4','helpful','Article 41 protects the family'))
a('1.1',1); a('1.2',1); a('1.3',1)
a('1.4',1,n(S+'1.3','essential','civil partnership status'))
a('1.5',2)
a('2.b',1); a('2.0',1)
a('2.1',1,n(S+'0.1','helpful','marriage excludes all others'))
a('2.2',1); a('2.3',1,n(C+'3.5','helpful','blood and marriage relatives','low'))
a('2.4',1)
a('2.5',1,n(S+'2.4','essential','documents accompany notice'))
a('2.6',2,n(S+'1.5','helpful','civil or religious ceremony solemniser'))
a('2.7',1,n(S+'2.6','helpful','approved venue formalities'))
a('2.8',2,n(S+'2.6','helpful','ceremony and witnesses'))
a('3.b',1)
a('3.0',2,n(S+'2.1','helpful','free to marry condition'),n(S+'2.6','helpful','formalities requirement','low'))
a('3.1',1,n(S+'2.2','essential','free consent requirement'))
a('3.2',1,n(S+'3.1','helpful','voidable marriage annulled'))
a('3.3',1,n(S+'3.1','helpful','court annulment of voidable marriage','low'))
json.dump(d,open('../../point-links/hom-marriage-s1.t1g1.json','w'),indent=0)
