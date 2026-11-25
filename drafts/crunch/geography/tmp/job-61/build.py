import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
T='geo-option-geoecology-s4.'
A5='geo-option-atmosphere-ocean-s5.'; A4='geo-option-atmosphere-ocean-s4.'; S2='geo-option-geoecology-s2.'
# subsection -> (item suffixes, costs in same order); 'b' first
C={0:'1 1 2 1 2 1',1:'1 1 2 2 1',2:'1 2 1 2 2 2 1 1',3:'1 1 1 1 1 1',4:'1 1 1 1 1 1',5:'1 1 2 1 1',
6:'1 1 1 2 2 1 2 1 1',7:'1 1 1 1 1',8:'1 1 2 1 2 1',9:'1 2 1 1 1 1 2 1',10:'1 1 1 1',11:'1 1 1 1 1',
12:'1 2 2 1 1 2 1 1',13:'1 1 1 1',14:'1 1 1 1 1',15:'1 1 1 1',16:'1 1 2 1 1',17:'1 1 1 1 1 2 1 1',
18:'1 1 1 1 1',19:'1 1 1 1 1 1 1 2',20:'1 2 1 1 1 1',21:'1 1 1 1 1 1 1',22:'1 1 1 1 1 1 1',
23:'1 1 1 1 1 1',24:'1 1 1 1 2 1',25:'1 1 2 1 1 1',26:'1 1 1 2 1 1 1 1',27:'1 1 2 1 2',
28:'1 1 1 1',29:'1 1',30:'1 1 1 1'}
cost={}
for s,v in C.items():
    c=v.split(); 
    for i,x in enumerate(c): cost[T+f"{s}."+('b' if i==0 else str(i-1))]=int(x)
def L(t,s,w,c='high'): return {"id":t,"strength":s,"why":w,"confidence":c}
t=lambda x:T+x
p1={
'0.3':[L(A5+'0.2','helpful','biome belts follow climate belts')],
'0.4':[L(A5+'18.3','helpful','vertical zones with altitude')],
'1.3':[L(t('1.0'),'essential','desert latitudes and belts')],
'2.3':[L(t('2.2'),'helpful','cold currents cause aridity')],
'2.5':[L(t('2.4'),'essential','rain shadow mechanism')],
'3.2':[L(t('3.1'),'essential','diurnal range explained')],
'4.3':[L(t('2.2'),'helpful','cold current causes coastal fog')],
'6.3':[L(t('6.2'),'essential','salts from capillary rise')],
'6.5':[L(t('6.2'),'helpful','no leaching keeps nutrients')],
'6.7':[L(t('20.0'),'helpful','rainforest soils infertile')],
'7.1':[L(t('0.2'),'helpful','competition for scarce water')],
'7.3':[L(t('5.2'),'helpful','wadis are dry river beds')],
'8.1':[L(t('8.0'),'essential','succulent water storage')],
'8.2':[L(t('8.1'),'essential','refers to saguaro')],
'8.3':[L(t('8.0'),'helpful','cacti as succulents','low')],
'9.5':[L(t('4.3'),'helpful','fog as desert moisture')],
'9.6':[L(t('6.2'),'helpful','salts rise by capillary rise')],
'10.1':[L(t('10.0'),'essential','desert bloom ephemerals'),L(A5+'31.b','helpful','El Nino warm Pacific pattern')],
'10.2':[L(t('10.0'),'essential','superbloom of ephemerals')],
'12.2':[L(t('4.3'),'helpful','Namib fog from cold current')],
'13.0':[L(t('8.1'),'helpful','saguaro pollination')],
'13.1':[L(t('8.1'),'essential','nests in saguaros')],
'13.2':[L(t('0.1'),'helpful','food chains and producers')],
'14.1':[L(t('9.1'),'helpful','roots reach groundwater','low')],
'14.2':[L(t('2.4'),'helpful','rain shadow')],
'14.3':[L(t('14.2'),'essential','Tabernas Desert')],
'15.0':[L(t('3.3'),'helpful','annual range')],
'15.1':[L(t('1.0'),'essential','under 250 mm desert limit')],
'16.2':[L(t('0.3'),'helpful','biome belts','low')],
'16.3':[L(t('0.4'),'helpful','vertical zones')],
'17.0':[L(A5+'1.b','helpful','equatorial climate')],
'17.6':[L(t('17.1'),'helpful','main basins','low')],
'18.1':[L(A5+'1.2','helpful','high sun, constant day length')],
'18.2':[L(A5+'1.2','helpful','overhead sun at equinoxes')],
'18.3':[L(A5+'1.1','helpful','daily versus annual range')],
'19.1':[L(A5+'2.2','helpful','convectional rain process')],
'19.2':[L(t('19.1'),'essential','follows stage 1')],
'19.3':[L(t('19.2'),'essential','follows stage 2')],
'19.4':[L(A5+'1.4','helpful','ITCZ low-pressure belt')],
'19.6':[L(A5+'2.2','helpful','transpiration moistens air','low')],
'20.3':[L(t('20.1'),'helpful','fast decomposition recycles nutrients')],
'20.4':[L(t('6.5'),'helpful','irrigated desert soils fertile')],
'21.4':[L(t('21.1'),'helpful','canopy blocks sunlight')],
'21.5':[L(t('21.0'),'essential','layers and heights','low')],
'22.0':[L(t('21.0'),'helpful','emergent trees')],
'22.1':[L(t('20.2'),'helpful','shallow roots take nutrients')],
'22.3':[L(t('21.4'),'helpful','little light reaches floor')],
'22.4':[L(t('23.1'),'helpful','epiphytes','low')],
'23.2':[L(t('23.1'),'essential','starts as epiphyte')],
'24.1':[L(t('24.0'),'helpful','many species per hectare')],
'24.3':[L(t('21.0'),'helpful','forest layers create niches')],
'24.4':[L(t('20.3'),'essential','closed nutrient cycle')],
'25.0':[L(t('21.1'),'helpful','canopy animal life','low')],
'25.4':[L(t('21.1'),'helpful','hunts in canopy','low')],
'27.1':[L(t('27.b'),'essential','mutualism defined')],
'27.3':[L(t('27.0'),'helpful','pollination and seed dispersal')],
'28.1':[L(t('28.0'),'helpful','peoples using these methods','low')],
}
p2={
'2.0':[L(A4+'3.1','essential','subtropical high sinking air')],
'2.1':[L(A4+'4.0','essential','trade winds')],
'2.2':[L(A4+'14.3','helpful','cold water chills air, fog')],
'2.3':[L(A4+'13.1','helpful','cold eastern-boundary currents')],
'4.3':[L(A4+'14.3','helpful','cold current fog')],
'19.4':[L(A4+'3.0','essential','ITCZ'),L(A4+'6.0','helpful','ITCZ shifts seasonally')],
}
p3={
'6.b':[L(S2+'13.5','helpful','aridisol is desert soil')],
'6.0':[L(S2+'3.2','helpful','weathering rate sets depth')],
'6.1':[L(S2+'6.0','helpful','humus from decomposition','low')],
'6.2':[L(S2+'5.0','helpful','leaching process'),L(S2+'11.0','helpful','capillary rise leaves salts')],
'6.3':[L(S2+'9.b','helpful','calcification process')],
'6.4':[L(S2+'4.2','helpful','wind deflation')],
'6.6':[L(S2+'12.2','helpful','alluvium as azonal soil','low')],
'20.b':[L(S2+'23.b','helpful','nutrients in plants, not soil')],
'20.0':[L(S2+'8.b','essential','laterisation process')],
'20.1':[L(S2+'6.1','helpful','fast humification when warm, moist')],
'20.3':[L(S2+'23.3','helpful','nutrients held in vegetation')],
'23.3':[L(S2+'23.b','helpful','nutrient-poor tropical soils','low')],
}
def run(name,links,withcost):
    txt=open(P+f'packs/{name}.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={}
    for k in cost:
        l=[x for x in links.get(k[len(T):],[])]
        out[k]={"cost":cost[k],"needs":l} if withcost else {"needs":l}
    for kk in links: assert T+kk in out,kk
    n=0;low=0
    for k,v in out.items():
        for x in v['needs']:
            assert x['id'] in ids and x['id']!=k,(k,x); n+=1; low+= x['confidence']=='low'
    tg=[i for i in ids if i.startswith(T)]
    assert set(tg)==set(out) and len(out)==len(cost),(len(tg),len(out))
    json.dump(out,open(P+f'point-links/{name}.json','w'),indent=1)
    print(name,len(out),n,sum(v.get('cost',1)==2 for v in out.values()) if withcost else '-',low)
run('geo-option-geoecology-s4.t1g1',p1,True)
run('geo-option-geoecology-s4.t1g2',p2,False)
run('geo-option-geoecology-s4.t1g3',p3,False)
