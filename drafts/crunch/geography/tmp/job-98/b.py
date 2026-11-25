import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-continental-s1.'
costs="""58.0=2 58.1=1 58.2=1 59.b=1 59.0=1 59.1=1 59.2=1 60.b=1 60.0=1 60.1=1 61.b=1 61.0=1 61.1=1 61.2=1 61.3=1 62.b=1 62.0=1 62.1=1
63.b=1 63.0=1 63.1=1 63.2=1 63.3=1 63.4=1 63.5=1 63.6=1 64.b=1 64.0=1 64.1=1 64.2=2 64.3=2 64.4=1 64.5=1
65.b=1 65.0=1 65.1=2 65.2=1 65.3=1 65.4=1 65.5=1 65.6=1 66.b=1 66.0=1 66.1=1 67.b=1 67.0=1 67.1=1 67.2=1 67.3=1 67.4=1 67.5=1
68.b=1 68.0=1 68.1=1 68.2=1 68.3=1 68.4=1 68.5=1 69.b=1 69.0=2 69.1=1 69.2=1 69.3=1 69.4=1 69.5=1
70.b=1 70.0=1 70.1=2 70.2=1 70.3=1 71.b=1 71.0=1 71.1=1 71.2=1 71.3=1 71.4=1 72.b=1 72.0=1 72.1=1 72.2=1 72.3=1 72.4=1
73.b=1 73.0=1 73.1=1 73.2=1 73.3=1 74.b=1 74.0=1 74.1=1 74.2=1 74.3=1 74.4=1 74.5=1
75.b=1 75.0=1 75.1=1 75.2=1 75.3=1 75.4=2 76.b=1 76.0=1 76.1=1 76.2=1 77.b=1 77.0=1 77.1=1 77.2=1 77.3=1 78.b=1 78.0=1 78.1=1 78.2=1
79.b=1 79.0=1 79.1=1 79.2=1 79.3=1 80.b=1 80.0=2 80.1=2 80.2=1 81.b=1 81.0=1 81.1=1 81.2=1 82.b=1 82.0=1 82.1=1 82.2=1
83.b=1 83.0=1 83.1=1 83.2=1 83.3=1 83.4=1 84.b=1 84.0=1 84.1=1 84.2=1 85.b=1 85.0=2 85.1=1
86.b=1 86.0=1 86.1=1 86.2=1 86.3=1 87.b=1 87.0=1 87.1=1"""
costs=[(S+a.split('=')[0],int(a.split('=')[1])) for a in costs.split()]
def L(i,s,w,c='high'): return {"id":i if '-s' in i and not i.startswith('.') else i,"strength":s,"why":w,"confidence":c}
s=lambda n:S+n
PM='geo-population-migration-s1.'
g1={'58.0':[(s('50.1'),'essential','Chota Nagpur coal and iron ore')],
'58.1':[(s('11.3'),'helpful','cotton on black soils')],
'58.2':[(s('27.5'),'helpful','Ganges delta')],
'60.1':[(s('56.3'),'helpful','export markets opened after 1991')],
'62.0':[(s('55.3'),'helpful','licensing (Licence Raj)')],
'62.1':[(s('57.1'),'helpful','Special Economic Zones')],
'63.3':[(s('50.1'),'helpful','Chota Nagpur minerals')],
'63.2':[(s('54.2'),'helpful','Hooghly jute mills','low')],
'65.5':[(s('54.1'),'helpful','Bombay cotton textile industry')],
'68.4':[(s('56.1'),'helpful','1991 liberalisation')],
'69.0':[(s('27.3'),'helpful','Yamuna river','low')],
'69.5':[(s('27.2'),'helpful','Ganges and Varanasi','low')],
'71.2':[(s('2.4'),'helpful','cool dry season')],
'74.4':[(s('71.2'),'helpful','dry winter tourist season')],
'80.b':[],
'80.0':[(s('80.b'),'helpful','demographic transition model'),(s('42.1'),'helpful','Green Revolution food supply')],
'80.2':[(s('80.b'),'essential','demographic transition model stages')],
'81.0':[(s('80.1'),'helpful','total fertility rate')],
'81.1':[(s('80.1'),'helpful','total fertility rate')],
'81.2':[(s('85.b'),'helpful','female literacy','low')],
'83.0':[(s('83.b'),'essential','sex ratio definition')],
'83.1':[(s('83.b'),'essential','sex ratio definition')],
'84.2':[(s('84.0'),'helpful','young population structure')],
'86.0':[(s('10.0'),'helpful','fertile alluvial soils')],
'87.0':[(s('5.4'),'helpful','Thar Desert aridity','low')],
'87.1':[(s('14.0'),'helpful','thin Himalayan soils','low')]}
g2={'58.2':[('geo-rivers-s1.13.b','helpful','delta formation','low')],
'63.2':[(s('107.2'),'helpful','Hooghly port and jute mills')],
'63.4':[(s('109.2'),'helpful','National Capital Region')],
'65.5':[(s('105.2'),'helpful','Mumbai cotton mills')],
'68.0':[(s('95.0'),'helpful','English as link language')],
'71.0':[(s('98.0'),'helpful','religion and holy places','low')],
'81.0':[(s('115.0'),'helpful','Kerala literacy and fertility','low')],
'86.b':[(s('88.b'),'helpful','density figures')]}
g3={'80.b':[(PM+'15.b','essential','demographic transition model')],
'80.0':[(PM+'16.0','helpful','stage 2 falling death rate')],
'80.1':[(PM+'0.5','helpful','replacement level')],
'80.2':[(PM+'17.0','essential','stage 3 of the model')],
'81.0':[(PM+'0.4','helpful','total fertility rate')],
'81.1':[(PM+'0.4','helpful','total fertility rate')],
'81.2':[(PM+'32.1','helpful','women status and education')],
'84.b':[(PM+'25.b','helpful','population pyramid')],
'84.0':[(PM+'26.0','helpful','wide-based pyramid')],
'84.1':[(PM+'31.1','helpful','demographic dividend')],
'84.2':[(PM+'31.0','helpful','pressure from many young people')],
'86.b':[(PM+'4.b','helpful','distribution and density')],
'86.0':[(PM+'5.2','helpful','soils and water supply')],
'86.2':[(PM+'6.2','helpful','cities attract people')],
'86.3':[(PM+'6.b','helpful','human factors')],
'87.b':[(PM+'7.b','helpful','low-density areas')],
'87.0':[(PM+'7.1','helpful','deserts sparse')],
'87.1':[(PM+'7.0','helpful','high cold land sparse')]}
def mk(links,withcost):
    out={}
    for i,c in costs:
        k=i[len(S):]
        n=[{"id":x[0],"strength":x[1],"why":x[2],"confidence":(x[3] if len(x)>3 else 'high')} for x in links.get(k,[])]
        out[i]={"cost":c,"needs":n} if withcost else {"needs":n}
    return out
for name,lk,wc in [('t3g1',g1,True),('t3g2',g2,False),('t3g3',g3,False)]:
    pk=S[:-1]+'.'+name
    txt=open(P+'packs/'+pk+'.txt').read()
    tl=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tl,re.M)
    cand=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    o=mk(lk,wc)
    assert list(o)==tids,(name,set(o)^set(tids))
    for k in lk: assert S+k in o,k
    n=0;lo=0
    for v in o.values():
        for x in v['needs']:
            assert x['id'] in cand,x['id']; n+=1; lo+=x['confidence']=='low'
            if not wc: assert x['id'] not in tids
    json.dump(o,open(P+'point-links/'+pk+'.json','w'),indent=1)
    print(name,len(o),n,sum(v.get('cost')==2 for v in o.values()),lo)
