import json,re
P='geo-option-atmosphere-ocean-s2.'
S1='geo-option-atmosphere-ocean-s1.'
def L(i,s,w,c='high'):
    return {"id":(S1+i[1:] if i.startswith('+') else P+i),"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
D={}
def a(k,cost,*n): D[P+k]={"cost":cost,"needs":list(n)}
a('0.b',1); a('0.0',1)
a('0.1',1,L('0.0',H,'short-wave in versus long-wave out'))
a('0.2',1)
a('1.b',1); a('1.0',1)
a('1.1',1,L('+0.1',H,'evaporation','low'))
a('1.2',1,L('+0.3',H,'wind drives currents','low'))
a('1.3',1)
a('2.b',1); a('2.0',1); a('2.1',1); a('2.2',1); a('2.3',1)
a('2.4',2 if False else 1)
D[P+'2.4']['cost']=1
