import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-weather-climate-s3.'
cnt={0:6,1:7,2:6,3:5,4:7,5:5,6:7,7:7,8:8,9:4,10:6,11:8}
ids=[]
for n,k in cnt.items():
    ids.append(f'{n}.b'); ids+= [f'{n}.{i}' for i in range(k)]
cost2={'1.6','3.3','4.2','4.6','5.2','6.5','7.0','8.4','8.5','8.7','9.1','9.3','10.1','11.3','11.6'}
def L(i,s,w,c='high'): return {'id':i,'strength':s,'why':w,'confidence':c}
l1={'0.2':[L('geo-mapwork-s1.1.0','helpful','uses the Irish Grid system')],
'2.3':[L('geo-mapwork-s1.0.0','helpful','Ordnance Survey maps','low')],
'7.1':[L('geo-mapwork-s1.14.2','helpful','OS forest symbols coniferous deciduous mixed')],
'7.2':[L('geo-mapwork-s1.8.0','helpful','reading relief from contours','low')],
'9.1':[L('geo-mapwork-s1.0.0','helpful','OS map extracts and legend','low')],
'9.3':[L('geo-mapwork-s1.28.1','helpful','ringforts as early Christian farmsteads')],
'10.0':[L('geo-mapwork-s1.28.1','helpful','ringfort monument type')],
'11.1':[L('geo-mapwork-s1.27.1','helpful','promontory forts defined','low')]}
l2={'0.0':[L('geo-weather-climate-s2.0.0','helpful','satellite image data','low')],
'0.4':[L('geo-weather-climate-s2.0.1','helpful','pixels in satellite images')],
'2.5':[L('geo-weather-climate-s2.1.3','helpful','Landsat and Sentinel satellites')],
'3.0':[L('geo-aerial-photographs-s1.28.0','helpful','land-use change from photographs')],
'3.b':[L('geo-aerial-photographs-s1.29.4','helpful','sprawl into the countryside','low')],
'5.0':[L('geo-weather-climate-s2.9.2','helpful','satellite monitoring of agriculture')],
'5.1':[L('geo-weather-climate-s2.12.1','helpful','regular repeat satellite coverage')],
'6.5':[L('geo-weather-climate-s2.9.2','helpful','satellite crop monitoring')],
'6.6':[L('geo-weather-climate-s2.7.0','essential','centre-pivot irrigation appearance')],
'10.b':[L('geo-aerial-photographs-s1.12.3','helpful','photograph and map dates reveal change')],
'10.1':[L('geo-aerial-photographs-s1.0.0','helpful','vertical aerial photographs','low')],
'10.2':[L('geo-aerial-photographs-s1.32.0','helpful','shadows and low sun direction','low')],
'10.3':[L('geo-aerial-photographs-s1.28.0','helpful','comparing photographs for change','low')]}
l3={'4.2':[L('geo-urban-s5.12.0','helpful','Dublin sprawl into commuter counties')],
'4.3':[L('geo-urban-s5.11.0','helpful','long commutes and car dependence')],
'4.4':[L('geo-urban-s5.11.2','helpful','costly services over large area')],
'4.5':[L('geo-urban-s5.13.1','helpful','compact growth and density')],
'4.6':[L('geo-urban-s5.13.3','helpful','planned new self-contained towns')],
'9.3':[L('geo-urban-s1.5.0','helpful','ringforts as dispersed farmsteads')],
'10.0':[L('geo-urban-s1.5.0','helpful','ringforts drawn as circles','low')],
'11.1':[L('geo-urban-s1.4.2','helpful','promontory forts defined')],
'11.2':[L('geo-urban-s5.19.1','helpful','Wood Quay Viking site and civic offices')],
'11.5':[L('geo-urban-s1.3.2','helpful','Brú na Bóinne location','low')]}
def build(links,withcost):
    o={}
    for i in ids:
        d={}
        if withcost: d['cost']=2 if i in cost2 else 1
        d['needs']=links.get(i,[])
        o[S+i]=d
    return o
for name,links,wc,cands in [('t1g1',l1,True,'geo-mapwork-s1.'),('t1g2',l2,False,None),('t1g3',l3,False,None)]:
    o=build(links,wc)
    json.dump(o,open(P+f'point-links/geo-weather-climate-s3.{name}.json','w'),ensure_ascii=False)
    txt=open(P+f'packs/geo-weather-climate-s3.{name}.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=set(re.findall(r'^\[(geo-weather-climate-s3\.[^\]]+)\]',txt,re.M))
    assert tg==set(o),(name,tg^set(o))
    nl=sum(len(v['needs']) for v in o.values())
    assert all(n['id'] in pk and n['id'] not in tg for v in o.values() for n in v['needs'])
    print(name,len(o),nl,sum(v.get('cost')==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
