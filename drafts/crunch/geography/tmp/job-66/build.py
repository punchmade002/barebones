import json,re,sys
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-global-interdependence-s2.'
PRE={'S.':S,'G1.':'geo-economic-globalisation-s1.','G3.':'geo-economic-globalisation-s3.','EN.':'geo-economic-environment-s3.','GE.':'geo-option-geoecology-s3.','PM.':'geo-population-migration-s3.'}
def ex(r):
    for k,v in PRE.items():
        if r.startswith(k): return v+r[len(k):]
    raise Exception(r)
def parse(spec,withcost):
    out={}
    for line in spec.strip().splitlines():
        id_,cost,links=line.split('|')
        needs=[]
        for l in filter(None,links.split(';')):
            r,s,c,w=l.split(',')
            assert len(w.split())<=8
            needs.append({'id':ex(r),'strength':{'e':'essential','h':'helpful'}[s],'why':w,'confidence':{'h':'high','l':'low'}[c]})
        d={'needs':needs}
        if withcost: d={'cost':int(cost),'needs':needs}
        assert S+id_ not in out
        out[S+id_]=d
    return out
S1='''0.b|1|
0.0|1|
0.1|1|
0.2|1|
1.b|1|
1.0|1|
1.1|1|
1.2|2|S.1.1,h,h,consumer regions capture value
2.b|1|
2.0|1|
2.1|1|
2.2|2|
2.3|1|
2.4|2|
2.5|2|S.2.4,h,h,Foxconn assembly in China
2.6|1|
3.b|1|
3.0|1|S.2.4,h,l,assembly jobs in China
3.1|1|S.2.2,h,h,TSMC as supplier;S.2.4,h,h,Foxconn as supplier
3.2|2|S.1.2,e,h,value added shared unequally
3.3|2|S.2.4,h,h,Foxconn Shenzhen factories
3.4|1|S.2.4,h,h,Foxconn Zhengzhou plant
3.5|1|S.2.5,e,h,assembly shifting to India
3.6|1|S.2.3,e,h,cobalt mined in DR Congo
4.b|1|
4.0|1|S.1.2,h,l,cheap assembly versus value added
4.1|1|S.1.2,h,h,design and branding capture value
4.2|1|
5.b|1|
5.0|1|
5.1|1|S.2.4,h,h,Chinese iPhone assembly chain
5.2|2|S.12.6,h,l,corporation tax and tax benefits
5.3|2|S.5.2,e,h,the 2016 State aid ruling
5.4|1|S.5.2,e,h,Brussels decision on Apple tax
5.5|1|S.2.5,h,h,assembly moving to India
6.b|1|
6.0|1|
6.1|2|
6.2|1|S.6.1,e,h,Mondelez takeover of Cadbury
6.3|1|
6.4|1|S.6.3,e,h,Rathmore plant
7.b|1|
7.0|1|
7.1|1|
7.2|2|S.7.1,h,l,low farm incomes of small farmers
7.3|1|S.7.0,h,h,cocoa in Côte d'Ivoire and Ghana
7.4|1|S.7.3,h,l,child labour in cocoa
7.5|1|S.6.4,e,h,Rathmore uses Irish milk;S.1.0,e,h,producer region term
8.b|1|
8.0|1|S.7.0,h,h,cocoa farms in Côte d'Ivoire;S.13.b,h,l,deforestation meaning
8.1|1|S.7.0,h,l,dependence on one crop
8.2|1|S.8.1,e,h,2024 price record
8.3|1|S.1.2,h,h,value added outside producer region
9.b|1|
9.0|1|
9.1|1|S.6.1,h,l,Mondelez company
9.2|1|S.9.0,e,h,Fairtrade Mark;S.9.1,e,h,Cocoa Life programme
10.b|1|
10.0|1|S.1.2,h,h,brands take value added
10.1|1|S.1.1,h,h,consumer region pressure
10.2|2|S.13.b,h,h,deforestation definition
11.b|1|
11.0|1|
11.1|2|
11.2|2|S.11.1,h,h,wafer fabs stage before assembly
11.3|1|
11.4|1|S.11.1,h,h,Leixlip fab
11.5|1|S.11.4,e,h,Fab 34 at Leixlip
11.6|2|
12.b|1|S.1.0,h,h,producer region
12.0|1|
12.1|1|S.12.0,h,l,exports mainly to USA
12.2|2|S.1.0,h,h,producer region
12.3|1|G1.1.0,h,l,IDA role attracting foreign firms
12.4|1|S.12.0,h,h,dependence on US market
12.5|1|
12.6|1|G1.2.0,h,l,low tax attracts firms
13.b|1|
13.0|1|
13.1|1|
13.2|1|
13.3|1|
14.b|1|S.13.3,h,h,demand from other regions
14.0|1|
14.1|1|S.14.0,h,h,Amazon rainforest
14.2|1|S.13.3,h,h,soya as deforestation driver
14.3|1|S.14.1,h,h,clearance in Amazon
14.4|2|S.14.1,h,l,clearance in Brazilian Amazon
15.b|1|
15.0|2|S.24.b,h,h,carbon and global warming
15.1|1|S.14.1,h,l,share of forest cleared
15.2|1|S.14.1,h,l,clearing of Amazon holdings
15.3|1|
15.4|2|S.10.2,h,h,EU Deforestation Regulation;S.14.2,h,l,soya trade
16.b|1|
16.0|1|S.13.3,h,l,palm oil driving clearance
16.1|1|S.16.0,h,l,oil palm plantations
16.2|1|S.16.1,e,h,clearing and burning peat
16.3|1|S.16.1,h,l,forest loss
17.b|1|
17.0|1|
17.1|1|
17.2|2|
17.3|1|
18.b|1|
18.0|1|S.17.3,h,l,foreign buyers of timber
18.1|1|
18.2|1|S.18.1,e,h,clear-felling
18.3|1|S.18.1,e,h,clear-felling
18.4|1|S.17.2,h,h,sustainable yield
19.b|1|
19.0|1|
19.1|1|
19.2|1|S.19.0,h,h,current forest cover
19.3|1|S.13.3,h,l,palm oil and beef drivers
20.b|1|
20.0|1|
20.1|1|S.20.0,h,l,drylands
20.2|1|S.20.0,e,h,desertification
21.b|1|
21.0|1|
21.1|1|S.21.0,h,h,unreliable rainfall
21.2|2|S.20.0,h,l,causes of desertification
21.3|1|S.24.b,h,h,global warming
21.4|1|
21.5|1|S.20.0,h,l,restoring degraded land
21.6|1|S.21.0,h,l,low rainfall
21.7|1|
22.b|1|
22.0|1|
22.1|1|S.22.0,h,h,Aral Sea'''
S2={ '1.0':'G3.16.0,h,h,assembly moved to low-wage countries','1.2':'G3.16.1,h,h,core keeps design and marketing','2.1':'G3.16.1,h,h,design kept in core','2.5':'G3.17.2,h,h,assembly spreading to other countries','3.0':'G3.2.4,h,l,exports bring earnings and jobs','3.5':'G3.17.2,h,h,assembly moving to cheaper places','4.1':'G3.16.1,h,h,core keeps design and marketing','5.5':'G3.8.5,h,h,US tariffs on Chinese goods;G3.8.6,h,h,2025 US tariff rises','7.0':'G3.15.3,h,h,cocoa colonial export pattern','8.3':'G3.15.3,h,h,cocoa exported unprocessed','9.0':'G3.4.6,h,h,fair trade minimum price','10.0':'G3.16.1,h,h,brands and marketing in core','10.2':'G3.4.1,h,l,regulations as trade barriers','11.6':'G3.4.1,h,l,subsidies as support','12.b':'G3.18.b,h,h,open economy and exports','12.1':'G3.0.3,h,h,trade surplus','12.2':'G3.18.2,h,h,main Irish goods exports','12.4':'G3.21.0,h,h,dependence on US MNCs','12.5':'G3.20.1,h,h,Brexit customs checks','15.0':'EN.3.0,h,h,CO2 from deforestation','16.2':'EN.0.3,h,h,transboundary pollution','21.3':'EN.2.1,h,h,enhanced greenhouse effect'}
S3={'0.2':'PM.0.4,h,l,refugees and economic migrants','21.0':'GE.7.1,h,h,one short wet season','21.2':'GE.3.0,h,h,overgrazing;GE.1.0,h,h,overcropping;GE.8.2,h,l,settled nomads concentrate grazing','21.4':'GE.9.1,h,h,Lake Chad shrinkage','21.6':'GE.11.1,h,h,zaï pits','21.7':'GE.12.0,h,h,farmer-managed natural regeneration'}
ids=[l.split('|')[0] for l in S1.splitlines()]
def mk(m): return '\n'.join(f'{i}|0|{m.get(i,"")}' for i in ids)
names=['geo-option-global-interdependence-s2.t1g%d'%i for i in (1,2,3)]
res=[parse(S1,True),parse(mk(S2),False),parse(mk(S3),False)]
for n,r in zip(names,res):
    pack=open(P+'packs/%s.txt'%n).read()
    tgt=pack.split('CANDIDATES')[0]
    tids=re.findall(r'^\[(\S+?)\]',tgt,re.M)
    allids=set(re.findall(r'^\[(\S+?)\]',pack,re.M))
    assert list(r)==tids,(n,len(r),len(tids))
    for k,v in r.items():
        for x in v['needs']: assert x['id'] in allids and x['id']!=k,(n,k,x)
    json.dump(r,open(P+'point-links/%s.json'%n,'w'),ensure_ascii=False,indent=0)
    json.load(open(P+'point-links/%s.json'%n))
    print(n,len(r),sum(len(v['needs']) for v in r.values()),sum(v.get('cost')==2 for v in r.values()),sum(x['confidence']=='low' for v in r.values() for x in v['needs']))
