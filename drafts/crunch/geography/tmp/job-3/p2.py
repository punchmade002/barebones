import json,re,sys
P='geo-economic-activities-s1.'
S2='geo-economic-activities-s2.'
G='geo-economic-globalisation-s1.'
def L(i,s,w,c='high'):
    for p in (S2,G):
        pass
    return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={}
def a(i,*n): d[P+i]=list(n)
def s(i,*a_): return a_
a('40.1'); a('40.2'); a('40.3',L(S2+'3.6',H,'road and rail freight/transport links','low'))
for i in ['41.b','41.0','41.1','41.2','41.3','42.b','42.0','42.1','42.2']: a(i)
a('43.b'); a('43.0'); a('43.1'); a('43.2'); a('43.3'); a('43.4'); a('43.5')
a('44.b'); a('44.0'); a('44.1'); a('44.2')
a('45.b'); a('45.0'); a('45.1'); a('45.2'); a('45.3'); a('45.4')
a('46.b'); a('46.0'); a('46.1'); a('46.2'); a('46.3'); a('47.b'); a('47.0'); a('47.1'); a('47.2'); a('47.3')
a('48.b'); a('48.0'); a('48.1'); a('48.2'); a('48.3'); a('48.4'); a('49.b'); a('49.0'); a('49.1')
a('50.b'); a('50.0'); a('50.1')
a('51.b'); a('51.0'); a('51.1',L(S2+'18.2',H,'lower costs relocation','low'),L(S2+'19.1',H,'relocation to lower-cost countries'))
a('51.2'); a('51.3',L(S2+'19.3',E,'automation replacing workers'))
a('51.4'); a('51.5',L(S2+'21.1',E,'Dell move to Poland'),L(S2+'19.1',H,'relocation to lower-cost countries'))
a('52.b'); a('52.0'); a('52.1'); a('52.2')
a('53.b'); a('53.0'); a('53.1'); a('53.2'); a('53.3',L(S2+'21.1',E,'same Dell Poland move','low'))
a('54.b'); a('54.0',L(S2+'10.0',H,'Moneypoint on Shannon estuary','low')); a('54.1',L(S2+'10.1',H,'same Moneypoint coal end','low'))
a('55.b'); a('55.0'); a('55.1'); a('55.2'); a('55.3')
a('56.b'); a('56.0',L(S2+'4.1',H,'IDA grants and sites')); a('56.1'); a('56.2'); a('56.3'); a('56.4'); a('56.5')
a('57.b'); a('57.0'); a('58.b'); a('58.0',L(S2+'6.0',H,'agglomeration explains Dublin concentration','low'))
a('58.1'); a('58.2',L(S2+'4.4',H,'regional policy and EU funds','low')); a('58.3',L(S2+'4.4',H,'regional policy steers growth','low'))
d={k:{"needs":v} for k,v in d.items()}
out='/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-activities-s1.t2g2.json'
json.dump(d,open(out,'w'),ensure_ascii=False,indent=0)
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-activities-s1.t2g2.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert list(d)==tg,(set(tg)^set(d))
n=l=lo=0
for k,v in d.items():
    n+=1
    for x in v['needs']:
        l+=1;lo+=x['confidence']=='low';assert x['id'] in allids and x['id']!=k,x
print(n,l,lo)
