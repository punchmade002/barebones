import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-urban-s5.'
# link spec: target:strength:why:conf ; separated by ';'
def mk(block, withcost):
    out={}
    for ln in block.strip().splitlines():
        parts=ln.split('|')
        i=S+parts[0]; k=1
        d={}
        if withcost: d['cost']=int(parts[k]); k+=1
        needs=[]
        if parts[k].strip():
            for l in parts[k].split(';'):
                t,s,w,c=l.split(':')
                needs.append({'id':t,'strength':{'e':'essential','h':'helpful'}[s],'why':w,'confidence':{'h':'high','l':'low'}[c]})
        d['needs']=needs
        assert i not in out; out[i]=d
    return out
ids='''0.b 0.0 0.1 0.2 0.3 0.4 0.5 0.6 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 2.b 2.0 2.1 2.2 2.3 3.b 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 4.b 4.0 4.1 4.2 4.3 4.4 5.b 5.0 5.1 5.2 5.3 5.4 5.5 6.b 6.0 6.1 6.2 6.3 6.4 6.5 6.6 7.b 7.0 7.1 7.2 8.b 8.0 8.1 8.2 9.b 9.0 9.1 9.2 9.3 9.4 9.5 10.b 10.0 10.1 10.2 10.3 11.b 11.0 11.1 11.2 11.3 11.4 12.b 12.0 12.1 13.b 13.0 13.1 13.2 13.3 13.4 14.b 14.0 14.1 14.2 14.3 14.4 14.5 15.b 15.0 15.1 15.2 16.b 16.0 16.1 16.2 16.3 16.4 17.b 17.0 17.1 17.2 18.b 18.0 18.1 18.2 18.3 18.4 19.b 19.0 19.1 19.2 19.3 20.b 20.0 20.1 20.2 20.3 20.4 21.b 21.0 22.b 22.0 22.1 22.2 22.3 23.b 23.0 23.1 23.2 23.3 24.b 24.0 24.1 24.2 24.3 25.b 25.0 25.1 25.2 26.b 26.0 26.1 26.2 26.3 27.b 27.0 27.1 27.2'''.split()
c2={'3.0','7.0','8.0','8.1','16.2','19.1','20.0','20.3'}
L1={ '0.1':'geo-urban-s4.0.3:h:suburbs zone:l','0.5':'geo-urban-s4.10.0:h:suburban shopping centres by motorway:h',
'2.0':'geo-urban-s5.10.b:h:urban sprawl:h','2.1':'geo-urban-s5.0.2:h:radial routes:h',
'3.1':'geo-urban-s5.3.0:h:Luas lines:h','3.7':'geo-urban-s5.0.4:h:heavy goods vehicles:h',
'4.0':'geo-urban-s4.1.7:h:pedestrian streets:h','4.4':'geo-urban-s4.11.4:h:mixed land use:l',
'5.b':'geo-urban-s4.0.1:h:inner city zone:h','7.1':'geo-urban-s4.9.0:h:tenements cleared:h',
'8.2':'geo-urban-s5.8.1:h:Fitzgerald report:h','10.2':'geo-urban-s4.11.1:h:greenfield and brownfield:h',
'11.1':'geo-urban-s4.15.1:h:loss of farmland:h','12.0':'geo-urban-s4.16.0:h:sprawl into Meath Kildare Wicklow:h',
'13.0':'geo-urban-s4.17.0:h:green belts:h','13.1':'geo-urban-s4.11.1:h:brownfield and greenfield:h',
'13.3':'geo-urban-s4.17.1:h:new towns:h','14.4':'geo-urban-s5.7.1:h:tenement clearance:h',
'14.5':'geo-urban-s4.13.b:h:segregation:h','16.1':'geo-urban-s5.12.1:h:ghost estates:h',
'16.2':'geo-urban-s4.7.5:h:banlieues and grands ensembles:h','20.4':'geo-urban-s5.20.3:h:UNESCO World Heritage listing:h',
'22.3':'geo-urban-s5.22.1:h:smoky coal ban:h','23.1':'geo-urban-s5.23.0:e:Ringsend plant:h',
'23.2':'geo-urban-s5.27.0:h:runoff from paved surfaces:l','25.2':'geo-urban-s5.5.2:h:dereliction:h',
'27.1':'geo-urban-s5.27.0:h:urban flooding:h'}
L2={'0.1':'geo-population-migration-s6.5.3:h:commuter towns:l','1.2':'geo-economic-environment-s3.24.0:h:urban air and noise pollution:l',
'4.3':'geo-population-migration-s6.3.1:h:remote working:h','11.4':'geo-economic-environment-s3.3.0:h:CO2 from fossil fuels:l',
'12.0':'geo-population-migration-s6.6.4:h:sprawl into commuter counties:h','18.3':'geo-economic-environment-s3.24.0:h:traffic air pollution:l',
'22.0':'geo-economic-environment-s3.24.0:h:town air pollution:h','22.1':'geo-economic-environment-s3.24.0:h:smoke-free zones:l',
'23.3':'geo-economic-environment-s3.1.1:h:diffuse runoff pollution:l','24.0':'geo-economic-environment-s3.21.0:h:landfill:l',
'24.1':'geo-economic-environment-s3.22.0:h:plastic bag levy:h','24.2':'geo-economic-environment-s3.22.2:h:waste hierarchy:l',
'24.3':'geo-economic-environment-s3.22.3:h:Poolbeg incinerator:h','25.0':'geo-economic-environment-s3.24.2:h:noise pollution:h',
'25.1':'geo-economic-environment-s3.24.2:h:visual pollution:h'}
L3={'0.2':'geo-region-ireland-s1.29.0:h:radial motorways:l','2.0':'geo-region-ireland-s1.30.1:h:long commutes into city:l',
'2.1':'geo-region-ireland-s1.29.0:h:radial routes:h','2.2':'geo-region-ireland-s1.29.3:h:Luas:h','2.3':'geo-region-ireland-s1.29.1:h:Port Tunnel:h',
'3.0':'geo-region-ireland-s1.29.2:h:DART:h;geo-region-ireland-s1.29.3:h:Luas:h;geo-region-ireland-s1.29.4:h:BusConnects:h;geo-region-ireland-s1.29.5:h:MetroLink:h',
'3.1':'geo-region-ireland-s1.29.3:h:Red and Green lines:h','3.6':'geo-region-ireland-s1.29.0:h:M50 orbital motorway:h',
'3.7':'geo-region-ireland-s1.29.1:h:Port Tunnel:h','12.0':'geo-region-ireland-s1.34.4:h:growth into commuter counties:h',
'16.0':'geo-region-ireland-s1.37.2:h:Ballymun high-rise flats:h','16.1':'geo-region-ireland-s1.37.5:h:commuter towns:l',
'19.3':'geo-region-ireland-s1.37.3:h:Temple Bar regeneration:h','24.3':'geo-region-ireland-s1.15.2:h:Poolbeg waste-to-energy:h',
'26.1':'geo-region-ireland-s1.8.5:h:Royal and Grand Canals:h','26.2':'geo-region-ireland-s1.6.3:h:North Bull Island:h',
'27.0':'geo-region-ireland-s1.8.7:h:paved surfaces runoff:h','27.1':'geo-region-ireland-s1.8.4:h:River Dodder:h'}
def blk(L,cost):
    return '\n'.join(i+'|'+(('2' if i in c2 else '1')+'|' if cost else '')+L.get(i,'') for i in ids)
for n,(L,cost) in enumerate([(L1,1),(L2,0),(L3,0)],1):
    r=mk(blk(L,cost),cost)
    pk=open(P+f'packs/geo-urban-s5.t1g{n}.txt').read()
    pids=set(re.findall(r'\[([^\]]+)\]',pk)); tgt={x for x in pids if x.startswith(S)}
    assert set(r)==tgt,(n,set(r)^tgt)
    for v in r.values():
        for x in v['needs']: assert x['id'] in pids
    if n>1:
        for v in r.values():
            for x in v['needs']: assert x['id'] not in tgt
    json.dump(r,open(P+f'point-links/geo-urban-s5.t1g{n}.json','w'),indent=0)
    print(n,len(r),sum(len(v['needs']) for v in r.values()),sum(v.get('cost')==2 for v in r.values()),sum(x['confidence']=='low' for v in r.values() for x in v['needs']))
