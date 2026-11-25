import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
E,H='essential','helpful'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
u=lambda x:'geo-urban-s4.'+x
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[n(u('0.0'),H,'CBD defined')]),
'1.0':(1,[n(u('12.0'),H,'accessibility drives land value')]),
'1.1':(1,[n(u('1.0'),H,'expensive land value','low')]),
'1.2':(1,[n(u('1.1'),H,'maximising use of costly sites','low')]),
'1.3':(1,[n(u('1.0'),H,'valuable sites, profitable uses')]),
'1.4':(1,[n(u('1.0'),H,'high land values')]),
'1.5':(1,[]),'1.6':(1,[]),'1.7':(1,[]),
'2.b':(1,[n(u('1.b'),H,'CBD features')]),
'2.0':(1,[]),
'2.1':(1,[n(u('1.7'),H,'pedestrian shopping streets')]),
'2.2':(1,[]),
'3.b':(1,[]),
'3.0':(1,[n(u('0.0'),H,'CBD at centre of rings')]),
'3.1':(2,[n(u('3.0'),E,'judges concentric model')]),
'3.2':(1,[n(u('3.0'),E,'rings of concentric model'),n(u('0.1'),H,'zone of transition label','low')]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(2,[n(u('4.0'),E,'judges sector model'),n(u('3.1'),H,'limitation answered by sectors','low')]),
'4.2':(1,[n(u('4.0'),E,'sector model drawn')]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(2,[n(u('5.0'),E,'judges multiple nuclei model')]),
'5.2':(1,[n(u('5.0'),E,'nuclei model drawn')]),
'5.3':(2,[n(u('5.0'),E,'multiple nuclei model'),n(u('4.0'),E,'sector model'),n(u('3.0'),E,'concentric model')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[n('geo-urban-s3.21.2',H,'Wide Streets Commissioners explained','low')]),
'6.2':(1,[n(u('0.1'),E,'zone in transition')]),
'6.3':(1,[n(u('0.2'),E,'inner residential zone')]),
'6.4':(2,[n(u('17.1'),H,'new towns defined','low')]),
'6.5':(2,[n(u('0.4'),H,'business parks and industrial zones')]),
'6.6':(1,[]),
'6.7':(2,[n(u('0.5'),H,'open space and recreation')]),
'7.b':(1,[]),
'7.0':(2,[]),
'7.1':(1,[n(u('0.0'),H,'CBD defined'),n(u('7.0'),H,'arrondissements explained')]),
'7.2':(1,[]),'7.3':(1,[]),'7.4':(1,[]),
'7.5':(2,[n(u('7.4'),E,'Périphérique ring road')]),
'7.6':(2,[n(u('17.1'),H,'new towns defined')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[n(u('8.0'),H,'these old inner-city sites')]),
'8.2':(2,[n(u('8.1'),H,'industry moving to the edge')]),
'8.3':(1,[]),
'8.4':(1,[n(u('8.0'),H,'old inner-city industry','low')]),
'8.5':(1,[n(u('8.3'),H,'brownfield site reused')]),
'8.6':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),
'9.2':(1,[n(u('9.1'),H,'trend reversed from suburban growth','low')]),
'9.3':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(2,[n(u('10.0'),H,'suburban shopping centres')]),
'10.2':(1,[n(u('10.0'),H,'same road-access logic','low')]),
'10.3':(1,[n(u('10.0'),H,'shoppers move to edge centres')]),
'10.4':(1,[n(u('10.3'),H,'effects being responded to')]),
'10.5':(1,[n(u('7.3'),E,'La Défense business district')]),
'11.b':(1,[]),'11.0':(1,[]),
'11.1':(1,[n(u('8.3'),H,'brownfield land defined')]),
'11.2':(1,[n(u('1.1'),H,'tall buildings in centre','low')]),
'11.3':(1,[]),'11.4':(1,[]),'11.5':(1,[]),
'12.b':(1,[]),
'12.0':(2,[n(u('12.b'),H,'bid-rent theory context')]),
'12.1':(1,[n(u('12.0'),E,'accessibility and land value')]),
'12.2':(2,[n(u('12.b'),E,'bid-rent definition')]),
'12.3':(1,[n(u('12.0'),E,'accessibility peaks')]),
'12.4':(1,[n(u('12.1'),H,'land values fall outwards')]),
'13.b':(1,[]),
'13.0':(2,[n(u('13.b'),H,'stratification and segregation')]),
'13.1':(1,[n(u('13.b'),H,'segregation of groups')]),
'13.2':(1,[]),
'14.b':(1,[n(u('13.b'),H,'segregation defined')]),
'14.0':(2,[n(u('13.1'),H,'affluent versus disadvantaged areas')]),
'14.1':(1,[]),
'14.2':(1,[n(u('13.2'),E,'gentrification defined')]),
'14.3':(1,[n(u('7.5'),H,'banlieues defined','low')]),
'14.4':(2,[n(u('7.5'),E,'grands ensembles defined')]),
'15.b':(1,[n(u('0.7'),H,'rural-urban fringe')]),
'15.0':(2,[]),
'15.1':(1,[n(u('0.7'),H,'fringe land competition','low')]),
'15.2':(1,[]),'15.3':(1,[]),'15.4':(1,[]),'15.5':(1,[]),'15.6':(1,[]),
'16.b':(1,[n(u('15.b'),H,'fringe pressures')]),
'16.0':(2,[n(u('9.1'),H,'sprawl defined')]),
'16.1':(2,[n('geo-urban-s3.2.3',H,'commuter towns defined')]),
'16.2':(1,[n(u('15.4'),H,'data centres on fringe')]),
'17.b':(1,[]),'17.0':(1,[]),
'17.1':(2,[]),
'17.2':(1,[n(u('17.1'),E,'new towns defined')]),
'17.3':(1,[n(u('17.1'),E,'new towns defined')]),
'17.4':(1,[n(u('8.3'),H,'brownfield land defined')]),
'17.5':(1,[n(u('11.0'),E,'zoning through development plans')]),
}
def run(pack,out,cost):
    txt=open(P+'packs/'+pack+'.txt').read()
    tgt=[]; ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M)); sec=None
    for l in txt.split('\n'):
        if l.startswith('TARGET'): sec=1
        elif l.startswith('CANDIDATES'): sec=0
        m=re.match(r'\[([^\]]+)\]',l)
        if m and sec: tgt.append(m.group(1))
    res={}
    for t in tgt:
        c,nd=D[t.replace('geo-urban-s4.','')]
        nd=[x for x in nd if x['id'] in ids and x['id']!=t]
        res[t]={"cost":c,"needs":nd} if cost else {"needs":[]}
    json.dump(res,open(P+'point-links/'+out+'.json','w'),indent=1,ensure_ascii=False)
    r=json.load(open(P+'point-links/'+out+'.json'))
    assert list(r)==tgt
    L=[x for v in r.values() for x in v['needs']]
    print(out,len(r),len(L),sum(v.get('cost')==2 for v in r.values()),sum(x['confidence']=='low' for x in L))
run('geo-urban-s4.t1g1','geo-urban-s4.t1g1',True)
run('geo-urban-s4.t1g2','geo-urban-s4.t1g2',False)
