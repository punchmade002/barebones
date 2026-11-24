import json,re,sys
P='geo-economic-activities-s1.'
S2='geo-economic-eu-s3.'
G='geo-economic-globalisation-s1.'
def L(i,s,w,c='high'):
    for p in (S2,G):
        pass
    return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={}
def a(i,*n): d[P+i]=list(n)
def s(i,*a_): return a_
a('40.1'); a('40.2'); a('40.3')
for i in ['41.b','41.0','41.1','41.2','41.3','42.b','42.0','42.1','42.2','43.b','43.0','43.1','43.2','43.3','43.4','43.5','44.b','44.0','44.1','44.2','45.b','45.0','45.1','45.2','45.3','45.4','46.b','46.0','46.1','46.2','46.3','47.b','47.0','47.1','47.2','47.3','48.b','48.0','48.1','48.2','48.3','48.4','49.b','49.0','49.1','50.b','50.0','50.1','51.b']: a(i)
a('51.0',L(S2+'1.0',H,'single market access'))
a('51.1'); a('51.2'); a('51.3'); a('51.4'); a('51.5')
for i in ['52.b','52.0','52.1','52.2','53.b','53.0']: a(i)
a('53.1',L(S2+'3.2',H,'CAP surpluses behind sugar reform','low'))
a('53.2'); a('53.3',L(S2+'30.1',H,'Dell EGF support same event','low'))
a('54.b'); a('54.0'); a('54.1'); a('55.b'); a('55.0'); a('55.1'); a('55.2'); a('55.3'); a('56.b'); a('56.0')
a('56.1'); a('56.2'); a('56.3',L(S2+'30.2',H,'Waterford Crystal workers EGF','low'))
a('56.4',L(S2+'28.0',H,'ESF retraining of workers'))
a('56.5',L(S2+'25.1',E,'Just Transition Fund for peat'))
a('57.b'); a('57.0'); a('58.b',L(S2+'20.0',H,'regional inequality in Ireland and EU'))
a('58.0'); a('58.1')
a('58.2',L(S2+'22.0',E,'BMW region and Objective 1'),L(S2+'21.0',H,'Objective 1 funding status'))
a('58.3')
d={k:{"needs":v} for k,v in d.items()}
out='/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-activities-s1.t2g3.json'
json.dump(d,open(out,'w'),ensure_ascii=False,indent=0)
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-activities-s1.t2g3.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert list(d)==tg,(set(tg)^set(d))
n=l=lo=0
for k,v in d.items():
    n+=1
    for x in v['needs']:
        l+=1;lo+=x['confidence']=='low';assert x['id'] in allids and x['id']!=k,x
print(n,l,lo)
