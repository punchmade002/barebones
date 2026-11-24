import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
A='geo-urban-s6.'
E,H='essential','helpful'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# package 1: id -> (cost, needs)
p1={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[]),
'0.3':(2,[n(A+'0.1',E,'renewal definition'),n(A+'0.2',E,'redevelopment definition')]),
'0.4':(1,[n('geo-urban-s4.13.2',H,'gentrification process','low')]),
'1.b':(1,[]),
'1.0':(1,[n(A+'0.0',H,'development plans and zoning')]),
'1.1':(1,[]),
'1.2':(2,[]),
'1.3':(1,[]),
'1.4':(1,[]),
'1.5':(2,[n(A+'1.4',E,'Part V share'),n(A+'1.3',H,'Strategic Development Zones')]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[]),
'2.2':(1,[]),
'2.3':(1,[]),
'3.b':(1,[]),
'3.0':(1,[n(A+'2.2',H,'new towns')]),
'3.1':(1,[n(A+'3.0',H,'the western new towns')]),
'3.2':(2,[n(A+'3.1',H,'services arriving late')]),
'3.3':(2,[n('geo-urban-s5.14.b',H,'community concept','low')]),
'4.b':(1,[]),
'4.0':(2,[]),
'4.1':(1,[]),
'4.2':(2,[n(A+'4.0',E,'designated gateways and hubs'),n(A+'4.1',E,'decentralisation programme')]),
'4.3':(1,[n(A+'4.0',H,'the aim of balancing growth'),n('geo-urban-s5.10.b',H,'sprawl','low')]),
'4.4':(1,[]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[]),
'5.2':(1,[n(A+'5.1',H,'Dublin growth share')]),
'5.3':(2,[n('geo-urban-s5.13.1',H,'compact growth and brownfield')]),
'5.4':(1,[]),
'5.5':(1,[]),
'5.6':(1,[n(A+'6.0',H,'housing targets','low')]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(1,[]),
'6.2':(1,[n(A+'1.4',E,'Part V requirement')]),
'6.3':(1,[n(A+'6.0',H,'level of need and targets','low')]),
'6.4':(1,[]),
'6.5':(1,[n(A+'6.1',H,'Rent Pressure Zones')]),
'7.b':(1,[n('geo-urban-s5.0.b',H,'congestion meaning')]),
'7.0':(2,[]),
'7.1':(1,[]),
'7.2':(1,[]),
'7.3':(1,[]),
'7.4':(2,[n(A+'7.0',E,'Luas rail capacity'),n(A+'7.1',E,'Port Tunnel and HGV ban')]),
'7.5':(2,[]),
'7.6':(2,[n('geo-urban-s5.0.5',E,'jobs and shops dispersed to suburbs')]),
'8.b':(1,[]),
'8.0':(1,[]),
'8.1':(1,[]),
'8.2':(1,[n('geo-urban-s5.23.0',H,'Ringsend treatment plant')]),
'8.3':(1,[]),
'8.4':(1,[n(A+'8.0',E,'the smoky coal ban')]),
'8.5':(2,[n('geo-urban-s5.22.0',H,'sources of air pollution')]),
'9.b':(1,[n(A+'0.2',H,'redevelopment definition'),n('geo-urban-s5.7.0',H,'containerisation job loss','low')]),
'9.0':(1,[n(A+'1.1',H,'tax incentives')]),
'9.1':(2,[n(A+'1.2',H,'development agencies')]),
'9.2':(1,[n(A+'1.2',H,'development agencies')]),
'9.3':(2,[]),
'9.4':(1,[n(A+'1.3',E,'Strategic Development Zones')]),
'9.5':(1,[]),
'9.6':(2,[n(A+'0.4',E,'gentrification and displacement')]),
'9.7':(2,[n(A+'1.2',H,'the DDDA')]),
'10.b':(1,[n(A+'0.1',H,'renewal definition')]),
'10.0':(1,[]),
'10.1':(1,[]),
'10.2':(1,[n(A+'10.0',E,'the bus station plan')]),
'10.3':(1,[]),
'10.4':(1,[]),
'10.5':(1,[]),
'11.b':(1,[n(A+'0.3',H,'renewal combined with redevelopment')]),
'11.0':(1,[]),
'11.1':(1,[]),
'11.2':(1,[n(A+'11.0',H,'the towers')]),
'11.3':(2,[]),
'11.4':(1,[n(A+'2.3',H,'community participation')]),
'11.5':(2,[n(A+'7.5',E,'Metro North shelved')]),
'12.b':(1,[]),
'12.0':(1,[]),
'12.1':(2,[]),
'12.2':(1,[]),
'12.3':(1,[]),
'12.4':(1,[]),
'13.b':(1,[n(A+'1.3',E,'Strategic Development Zones'),n(A+'3.1',H,'earlier new towns lacked services')]),
'13.0':(1,[n(A+'1.3',H,'fast-track SDZ planning')]),
'13.1':(1,[]),
'13.2':(1,[n(A+'13.1',H,'phased services')]),
'13.3':(1,[]),
'14.b':(1,[]),
'14.0':(2,[n(A+'1.1',H,'tax incentives')]),
'14.1':(1,[]),
'14.2':(1,[]),
'14.3':(1,[]),
'14.4':(1,[]),
'15.b':(1,[n(A+'1.2',H,'agency with planning powers')]),
'15.0':(1,[n(A+'1.2',H,'development agencies')]),
'15.1':(1,[n(A+'1.1',H,'tax incentives')]),
'15.2':(1,[]),
'15.3':(1,[]),
'15.4':(1,[]),
'15.5':(1,[]),
'15.6':(2,[n(A+'15.0',E,'unelected body with planning powers')]),
'15.7':(2,[n(A+'0.4',H,'residents priced out')]),
'16.b':(1,[n(A+'2.2',H,'new towns')]),
'16.0':(1,[n(A+'2.2',H,'new towns')]),
'16.1':(1,[n('geo-urban-s4.7.5',H,'banlieues and grands ensembles')]),
'16.2':(2,[n(A+'16.1',H,'banlieues problem estates')]),
'17.b':(1,[]),
'17.0':(2,[n(A+'13.2',E,'Adamstown phased services'),n(A+'2.3',H,'resident involvement')]),
'17.1':(2,[n(A+'9.6',E,'Docklands criticism')]),
'17.2':(2,[n(A+'4.2',E,'NSS undermined by decentralisation'),n(A+'1.1',H,'tax incentives')]),
}
G='geo-economic-activities-s1.'
R='geo-region-concept-s5.'
p2={k:[] for k in p1}
p2['4.2']=[n(G+'6.1',H,'property boom','low')]
p2['5.2']=[n(R+'6.0',H,'counterweight to Dublin')]
p2['9.1']=[n(G+'32.b',H,'IFSC')]
p2['9.5']=[n(G+'25.b',H,'Silicon Docks cluster')]
p2['9.7']=[n(G+'7.0',H,'property bubble and crash')]
p2['11.5']=[n(G+'7.0',H,'recession and property crash','low')]
p2['13.3']=[n(G+'7.0',H,'2008 property crash')]
p2['14.4']=[n(G+'56.2',H,'Cork Docklands regeneration')]
p2['15.2']=[n(G+'35.1',H,'Canary Wharf')]
p2['15.5']=[n(G+'35.b',H,'London financial centre')]
for k in p1:
    pass
def out(name,d):
    o={A+k:v for k,v in d.items()}
    json.dump(o,open(P+'point-links/'+name+'.json','w'),indent=1)
o1={A+k:{"cost":c,"needs":nd} for k,(c,nd) in p1.items()}
json.dump(o1,open(P+'point-links/geo-urban-s6.t1g1.json','w'),indent=1)
o2={A+k:{"needs":nd} for k,nd in p2.items()}
json.dump(o2,open(P+'point-links/geo-urban-s6.t1g2.json','w'),indent=1)
# validate
for name,o,cost in (('t1g1',o1,1),('t1g2',o2,0)):
    txt=open(P+'packs/geo-urban-s6.%s.txt'%name).read()
    tgt=re.findall(r'^\[(geo-urban-s6\.[^\]]+)\]',txt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(o)==tgt,(set(tgt)^set(o))
    links=[x for v in o.values() for x in v['needs']]
    for v in o.items():
        for x in v[1]['needs']:
            assert x['id'] in allids and x['id']!=v[0],(v[0],x['id'])
            if name=='t1g2': assert not x['id'].startswith('geo-urban-s6')
    print(name,len(o),len(links),sum(v.get('cost')==2 for v in o.values()),sum(x['confidence']=='low' for x in links))
