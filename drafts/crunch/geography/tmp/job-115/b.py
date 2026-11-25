import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-ireland-s1.'
costs="""0.b:1 0.0:1 0.1:2 1.b:1 1.0:1 1.1:1 1.2:1 1.3:1 1.4:2
2.b:1 2.0:1 2.1:1 2.2:1 2.3:1 2.4:1
3.b:2 3.0:2 3.1:2 3.2:1 3.3:1 3.4:1 3.5:1 3.6:1
4.b:1 4.0:1 4.1:1
5.b:1 5.0:1 5.1:1 5.2:2 5.3:1 5.4:1 5.5:1 5.6:1
6.b:1 6.0:1 6.1:1 6.2:1 6.3:1
7.b:1 7.0:2 7.1:1 7.2:1 7.3:1 7.4:1 7.5:1 7.6:1
8.b:1 8.0:1 8.1:1 8.2:1 8.3:1 8.4:1 8.5:1 8.6:1 8.7:1
9.b:1 9.0:1 9.1:1 9.2:1 9.3:1 9.4:1 9.5:1
10.b:1 10.0:1 10.1:1 10.2:2 10.3:1 10.4:1
11.b:1 11.0:1 11.1:1 11.2:1 11.3:1 11.4:1 11.5:1
12.b:1 12.0:1 12.1:1 12.2:1 12.3:1 12.4:1 12.5:1
13.b:1 13.0:1 13.1:1 13.2:2 13.3:1 13.4:1 13.5:1 13.6:1
14.b:1 14.0:2 14.1:1 14.2:1 14.3:1 14.4:1
15.b:1 15.0:1 15.1:1 15.2:1 15.3:2 15.4:1 15.5:1 15.6:1
16.b:1 16.0:1 16.1:1 16.2:1 16.3:1 16.4:1
17.b:1 17.0:1 17.1:1 17.2:1 17.3:1 17.4:1
18.b:1 18.0:1 18.1:1 18.2:1 18.3:1 18.4:1
19.b:1 19.0:1 19.1:2 19.2:1 19.3:1 19.4:1"""
ids=[S+p.split(':')[0] for p in costs.split()]
cost={S+p.split(':')[0]:int(p.split(':')[1]) for p in costs.split()}
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
c1={
'1.4':[L('geo-region-concept-s4.0.3',H,'cumulative causation idea')],
'4.1':[L(S+'3.6',H,'heavy upland rainfall')],
'7.4':[L(S+'5.2',H,'granite uplands')],
'7.5':[L(S+'5.2',H,'granite uplands')],
'8.1':[L(S+'8.0',H,'River Liffey course')],
'9.0':[L(S+'4.0',H,'climate effect on farming')],
'9.1':[L(S+'5.6',H,'lowland relief effect')],
'9.2':[L(S+'7.0',H,'brown earth soils')],
'9.5':[L(S+'11.5',H,'what the CAP is')],
'10.1':[L(S+'7.0',H,'fertile lowland soils')],
'10.2':[L(S+'7.2',H,'the Curragh')],
'12.1':[L(S+'7.5',H,'poor upland soils')],
'14.2':[L(S+'6.1',H,'glacial deposits','low')],
'14.3':[L(S+'5.2',H,'Wicklow granite','low')],
'14.4':[L(S+'7.3',H,'Bog of Allen peat')],
'16.3':[L(S+'16.2',H,'high-tech plant locations')],
'16.4':[L(S+'16.1',H,'inner-city industry decline')],
'17.1':[L(S+'17.0',H,'Intel at Leixlip')],
'17.4':[L(S+'16.1',H,'older inner-city industry')],
'19.4':[L(S+'19.0',H,'skilled workforce')],
}
c2={
'1.1.2':None}
c2={
'3.b':[L('geo-region-concept-s1.4.b',H,'cool temperate oceanic climate causes')],
'3.0':[L('geo-region-concept-s1.5.2',H,'rain shadow')],
'3.5':[L('geo-region-concept-s1.6.2',H,'continental influence','low')],
'3.6':[L('geo-region-concept-s1.4.5',H,'relief rainfall')],
'5.2':[L('geo-region-concept-s1.13.3',H,'Leinster batholith granite','low')],
'7.0':[L('geo-region-concept-s1.7.1',H,'brown earth soil')],
'1.2':[L('geo-economic-activities-s2.1.7',H,'infrastructure meaning')],
'16.2':[L('geo-economic-activities-s2.1.4',H,'business park meaning')],
'16.4':[L('geo-economic-activities-s2.5.0',H,'site needs space','low')],
'17.1':[L('geo-economic-activities-s2.11.4',H,'Intel site motorway and airport')],
'17.4':[L('geo-economic-activities-s2.14.6',H,'industrial inertia')],
'18.3':[L('geo-economic-activities-s2.3.4',H,'air freight of high-value goods')],
'19.4':[L('geo-economic-activities-s2.6.0',H,'agglomeration of skilled labour','low')],
}
c3={
'5.1':[L('geo-glaciation-s1.15.0',H,'glacial deposits','low')],
'6.0':[L('geo-glaciation-s1.9.b',H,'U-shaped valley formation')],
'6.1':[L('geo-glaciation-s1.20.b',H,'how eskers form')],
'7.0':[L('geo-glaciation-s1.15.0',H,'boulder clay (till)')],
'7.2':[L('geo-glaciation-s1.21.b',H,'outwash plain')],
'8.7':[L('geo-urban-s5.27.0',H,'urban runoff and flooding')],
'11.0':[L('geo-urban-s5.10.b',H,'urban sprawl')],
'14.2':[L('geo-glaciation-s1.19.0',H,'glacial sand and gravel','low')],
'16.1':[L('geo-urban-s5.5.0',H,'inner-city industry loss','low')],
}
c2['1.2']=[L('geo-economic-activities-s2.1.7',H,'infrastructure meaning')]
c2.pop('1.1.2',None)
def build(name,links,withcost):
    out={}
    for i in ids:
        k=i[len(S):]
        d={}
        if withcost: d['cost']=cost[i]
        d['needs']=links.get(k,[])
        out[i]=d
    pk=open(P+'packs/'+name+'.txt').read()
    tgt=set(re.findall(r'^\[(geo-region-ireland-s1\.[^\]]+)\]',pk.split('CANDIDATES')[0],re.M))
    allp=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    assert tgt==set(ids),(tgt^set(ids))
    n=0;lo=0
    for v in out.values():
        for x in v['needs']:
            assert x['id'] in allp,x['id']; n+=1; lo+=x['confidence']=='low'
    json.dump(out,open(P+'point-links/'+name+'.json','w'),indent=1)
    json.loads(open(P+'point-links/'+name+'.json').read())
    print(name,len(out),n,sum(v.get('cost',1)==2 for v in out.values()) if withcost else '-',lo)
build('geo-region-ireland-s1.t1g1',c1,True)
build('geo-region-ireland-s1.t1g2',c2,False)
build('geo-region-ireland-s1.t1g3',c3,False)
