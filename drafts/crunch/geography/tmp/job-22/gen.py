import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P_='geo-economic-globalisation-s1.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful';E='essential'
S1='geo-economic-globalisation-s1.'
S2='geo-economic-activities-s2.'
A1='geo-economic-activities-s1.'
M1='geo-mapwork-s1.'
# explicit target list: id -> cost (1 default stated explicitly via list below)
ids=[]
counts={0:5,1:2,2:8,3:5,4:4,5:4,6:2,7:3,8:4,9:4,10:7,11:2,12:2,13:3,14:2,15:3,16:1,17:1,18:6,19:5,20:2}
for k in range(21):
    ids.append(f'{S1}{k}.b')
    for j in range(counts[k]+1): ids.append(f'{S1}{k}.{j}')
cost2={'0.2','0.3','2.0','3.3','4.2','4.4','7.3','8.1','10.0','10.5','10.7','18.0','18.1','18.2','19.1','19.5'}
cost={i:(2 if i[len(S1):] in cost2 else 1) for i in ids}
def R(d): return {S1+k:v for k,v in d.items()}
n1=R({
'0.1':[L(S1+'0.0','essential','uses HQ, home and host country')],
'0.2':[L(S1+'0.1','helpful','headquarters and branch plants')],
'0.3':[L(S1+'0.1','helpful','core and branch placement')],
'1.0':[L(S1+'1.b','essential','uses foreign direct investment')],
'1.1':[L(S1+'1.0','helpful','uses IDA Ireland')],
'1.2':[L(S1+'0.0','helpful','uses MNC definition')],
'2.4':[L(S1+'1.0','essential','IDA role')],
'2.6':[L(S2+'1.5','helpful','cluster or agglomeration meaning')],
'3.b':[L(S1+'0.1','helpful','home-country core, branch plants')],
'3.1':[L(S1+'6.0','helpful','what a microprocessor does','low')],
'4.b':[L(S2+'1.1','helpful','branch plant meaning')],
'4.2':[L(S1+'6.1','helpful','wafers and chip making')],
'4.3':[L(S1+'4.2','helpful','Fab 34 introduced there')],
'4.4':[L(S1+'4.2','helpful','Fab 34 introduced there')],
'5.b':[L(S1+'3.3','helpful','what a fab is')],
'5.0':[L(S2+'3.7','helpful','motorways as a transport factor','low')],
'5.1':[L(S2+'1.3','helpful','greenfield site meaning')],
'5.3':[L(S2+'2.2','helpful','labour as location factor','low')],
'5.4':[L(S2+'2.1','helpful','energy as location factor','low')],
'6.2':[L(S1+'6.1','helpful','wafers and tiny circuits')],
'7.0':[L(S1+'6.1','helpful','silicon wafers')],
'7.3':[L(S1+'4.2','helpful','EUV lithography')],
'8.0':[L(S1+'3.3','essential','fab locations')],
'8.1':[L(S1+'3.4','essential','assembly and test plants'),L(S1+'8.0','helpful','stage 1 precedes it')],
'8.3':[L(S2+'3.4','essential','air freight suits light valuable goods')],
'8.4':[L(S1+'8.1','helpful','cutting and testing stage')],
'9.1':[L(S2+'15.b','helpful','data centres explained','low')],
'9.4':[L(S1+'9.3','helpful','markets by region')],
'10.1':[L(S1+'9.0','helpful','Apple was a customer','low')],
'10.5':[L(S1+'2.0','essential','15% minimum tax rate')],
'10.6':[L(S1+'5.4','helpful','fabs need power')],
'10.7':[L(S1+'3.4','helpful','Asian assembly and test plants','low')],
'11.1':[L(S1+'2.0','helpful','corporation tax rate','low')],
'11.2':[L(S1+'5.2','helpful','university links')],
'12.2':[L(S1+'0.1','helpful','core of the company')],
'13.b':[L(S1+'0.1','helpful','regional headquarters')],
'13.3':[L(S1+'13.2','helpful','what the campus does')],
'14.1':[L(S1+'14.0','helpful','contract manufacturer outsourcing')],
'15.0':[L(S1+'10.0','helpful','TSMC identified there','low')],
'15.3':[L(S1+'15.2','helpful','cobalt as raw material')],
'16.0':[L(S1+'14.1','helpful','Foxconn contract maker')],
'16.1':[L(S1+'16.0','helpful','assembly in China first')],
'18.0':[L(S1+'18.2','helpful','what state aid means')],
'18.1':[L(S1+'18.0','essential','the 2016 ruling reinstated')],
'18.2':[L(S1+'18.0','helpful','the tax case')],
'18.3':[L(S1+'16.0','helpful','assembly in China')],
'18.6':[L(S2+'15.b','helpful','data centres explained','low')],
'19.b':[L(S2+'29.b','helpful','map evidence question structure')],
'19.0':[L(S2+'30.1','helpful','roads, rail, port for moving goods')],
'19.1':[L(S2+'30.0','helpful','flat land for a factory','low')],
'19.2':[L(S2+'1.4','helpful','industrial estate meaning')],
'19.3':[L(S2+'30.3','helpful','water supply for industry','low')],
'19.4':[L(S2+'33.1','helpful','flood-prone land as a reason against','low')],
'19.5':[L(S1+'19.0','helpful','map features listed there')],
})
n2=R({
'2.0':[L(A1+'5.2','helpful','12.5% corporation tax')],
'2.2':[L(A1+'5.0','helpful','EU single market')],
'2.3':[L(A1+'23.4','helpful','Brexit and UK leaving EU')],
'2.4':[L(A1+'3.0','helpful','IDA set up to attract firms')],
'2.6':[L(A1+'19.4','helpful','clusters of similar firms','low')],
'3.0':[L(A1+'30.0','helpful','Silicon Valley described')],
'9.1':[L(A1+'28.b','helpful','data centres explained','low')],
'10.5':[L(A1+'23.1','helpful','15% minimum tax reduces advantage')],
'10.6':[L(A1+'23.6','helpful','grid and energy constraints')],
'11.1':[L(A1+'9.1','helpful','tax from few multinationals','low')],
'18.0':[L(A1+'23.2','helpful','Apple tax back-payment ruling')],
})
n3=R({
'19.b':[L(M1+'35.b','helpful','site choice with map evidence')],
'19.0':[L(M1+'14.0','helpful','roads and railways in the legend','low')],
'19.1':[L(M1+'9.0','essential','contour spacing shows slope')],
'19.2':[L(M1+'14.0','helpful','industrial estate symbol in legend','low')],
'19.4':[L(M1+'9.0','helpful','close contours mean steep slope')],
})
def build(out,src,nd,withcost):
    d={}
    for i in ids:
        e={}
        if withcost: e['cost']=cost[i]
        e['needs']=nd.get(i,[])
        d[i]=e
    for k,v in nd.items(): assert k in ids,k
    txt=open(P+'packs/'+src).read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=set(re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M))
    assert tg==set(ids),(tg^set(ids))
    for e in d.values():
        for n in e['needs']:
            assert n['id'] in pk,n['id']; 
    for k,e in d.items():
        for n in e['needs']: assert n['id']!=k
    json.dump(d,open(P+'point-links/'+out,'w'),indent=1)
    d2=json.load(open(P+'point-links/'+out))
    links=sum(len(e['needs']) for e in d2.values())
    low=sum(n['confidence']=='low' for e in d2.values() for n in e['needs'])
    print(out,len(d2),links,sum(e.get('cost')==2 for e in d2.values()),low)
for t,nd,wc in(('t1g1',n1,1),('t1g2',n2,0),('t1g3',n3,0)):
    build(f'geo-economic-globalisation-s1.{t}.json',f'geo-economic-globalisation-s1.{t}.txt',nd,wc)
