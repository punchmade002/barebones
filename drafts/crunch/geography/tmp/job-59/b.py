import json,re,sys
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-option-geoecology-s2.'
def ids(path):
    t=open(G+'packs/'+path).read().split('\nCANDIDATES')[0]
    return re.findall(r'^\[(geo-option-geoecology-s2\.[^\]]+)\]',t,re.M)
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
S1='geo-option-geoecology-s1.';S3='geo-rocks-weathering-s3.';S5='geo-option-atmosphere-ocean-s5.'
c2={'0.3','1.4','4.1','7.0','7.2','8.6','10.0','10.2','12.1','12.2','13.1','13.2','13.5','15.3','16.3','23.1','23.5','24.1','26.3','27.0'}
n1={ # short id -> list of (id,strength,why,conf)
'0.0':[(S1+'12.b','helpful','uses texture'),(S1+'19.0','helpful','uses pH')],
'0.1':[(S3+'7.0','helpful','climate controls weathering type')],
'0.3':[(S1+'9.0','essential','precipitation versus evapotranspiration balance')],
'0.4':[(S1+'3.b','essential','uses soil horizons')],
'1.3':[(S1+'8.1','helpful','uses leaching')],
'1.4':[(S1+'7.0','helpful','mull and mor humus')],
'2.0':[(S1+'6.1','helpful','litter and humus')],
'2.1':[(S1+'6.1','helpful','litter and humus')],
'2.2':[(S1+'8.1','helpful','uses leaching')],
'2.5':[(P+'2.2','essential','E horizon'),(P+'2.3','essential','B horizon')],
'2.6':[(P+'2.b','helpful','uses horizon letters')],
'3.0':[(S3+'0.3','helpful','physical weathering')],
'3.1':[(S3+'6.0','helpful','hydrolysis forms clay')],
'3.2':[(S3+'7.1','helpful','chemical weathering fastest in warm wet')],
'4.4':[(P+'2.1','essential','A horizon topsoil')],
'4.5':[(S1+'14.b','helpful','soil structure')],
'5.0':[(S1+'9.0','essential','precipitation exceeds evapotranspiration')],
'5.1':[(S1+'20.0','helpful','nutrient bases held in soil','low')],
'5.2':[(S1+'19.1','helpful','acid soils from leaching')],
'5.3':[(P+'7.b','helpful','podzol formed by intense leaching')],
'6.0':[(S1+'6.1','essential','litter, decomposers and humus')],
'6.1':[(S1+'7.0','helpful','mull humus')],
'6.2':[(S1+'7.1','helpful','mor humus')],
'7.b':[(P+'5.b','essential','leaching')],
'7.0':[(P+'5.0','essential','precipitation exceeds evapotranspiration'),(S1+'7.1','helpful','mor humus')],
'7.2':[(P+'5.1','helpful','bases washed down')],
'7.3':[(P+'2.2','essential','E horizon')],
'7.4':[(P+'2.3','essential','B horizon')],
'8.b':[(P+'5.b','helpful','leaching')],
'8.0':[(S3+'7.1','helpful','chemical weathering in warm wet climates')],
'8.1':[(P+'5.b','helpful','leaching')],
'8.3':[(P+'6.0','helpful','humification')],
'8.5':[(P+'8.2','helpful','aluminium oxides left behind')],
'8.6':[(P+'8.5','helpful','bauxite')],
'8.7':[(P+'8.1','helpful','silica and bases leached')],
'9.b':[(S1+'9.1','helpful','evaporation exceeds precipitation')],
'9.0':[(P+'5.b','helpful','leaching')],
'9.2':[(S1+'8.2','helpful','capillary water')],
'10.b':[(S1+'10.4','helpful','iron reduced without oxygen')],
'10.0':[(S1+'9.2','helpful','waterlogging')],
'10.1':[(S1+'10.3','helpful','anaerobic soils')],
'10.2':[(S1+'10.4','essential','iron reduced in poor aeration')],
'10.3':[(P+'10.2','helpful','iron colour change')],
'11.0':[(S1+'8.2','helpful','capillary water')],
'12.2':[(S1+'0.3','helpful','alluvium and loess')],
'13.1':[(P+'7.b','helpful','podzolisation')],
'13.0':[(P+'10.b','helpful','gleying','low')],
'13.3':[(P+'9.b','helpful','calcification')],
'13.5':[(P+'11.b','helpful','salt crust formation')],
'13.6':[(P+'8.b','helpful','laterisation')],
'13.7':[(P+'13.b','helpful','soil belts')],
'14.0':[(P+'1.3','helpful','altitude and leaching')],
'15.1':[(P+'18.b','helpful','podzols in uplands')],
'15.2':[(P+'10.b','helpful','gleying')],
'15.3':[(P+'12.1','helpful','intrazonal soils')],
'16.5':[(S1+'19.0','helpful','pH scale')],
'16.6':[(S1+'6.3','helpful','earthworm mixing')],
'17.1':[(S1+'14.0','helpful','crumb structure')],
'17.2':[(P+'2.3','helpful','B horizon')],
'17.4':[(P+'2.2','helpful','E horizon')],
'17.7':[(S1+'19.4','helpful','Teagasc pH targets and liming')],
'18.1':[(S1+'7.1','helpful','mor humus')],
'18.2':[(P+'7.5','helpful','iron pan')],
'18.3':[(P+'7.b','essential','podzolisation steps')],
'19.2':[(P+'7.5','helpful','iron pan')],
'19.5':[(S1+'19.0','helpful','pH scale')],
'19.7':[(P+'7.5','helpful','iron pan')],
'20.0':[(P+'10.0','helpful','impermeable till and waterlogging')],
'20.2':[(P+'10.b','essential','gleying steps')],
'21.0':[(P+'10.4','helpful','gley colours')],
'21.1':[(S1+'15.2','helpful','poaching')],
'22.2':[(P+'8.b','essential','laterisation')],
'23.0':[(S3+'7.1','helpful','chemical weathering rate')],
'23.1':[(S1+'3.b','helpful','soil horizons')],
'23.2':[(P+'8.3','helpful','little humus')],
'23.5':[(P+'8.4','essential','laterite crust')],
'25.b':[(P+'9.b','essential','calcification')],
'25.0':[(P+'9.b','essential','calcification')],
'25.3':[(P+'24.3','helpful','grass roots add humus')],
'25.4':[(P+'9.1','helpful','calcium deposited in B horizon')],
'25.5':[(S1+'0.3','helpful','loess')],
'26.3':[(P+'4.2','helpful','wind erosion')],
'27.0':[(S1+'13.1','helpful','clay soils hold moisture')],
}
n2={
'0.1':[(S5+'0.3','helpful','climate controls','low')],
'1.3':[(S5+'18.3','helpful','temperature falls with altitude')],
'2.3':[(S5+'1.b','helpful','hot wet tropics','low')],
'8.b':[(S5+'1.b','helpful','equatorial climate')],
'9.b':[(S5+'14.b','helpful','continental dry climate')],
'11.0':[(S5+'17.0','helpful','hot desert dryness','low')],
'13.1':[(S5+'16.2','helpful','boreal forest belt','low')],
'13.2':[(S5+'8.0','helpful','temperate oceanic locations')],
'13.3':[(S5+'16.1','helpful','temperate grassland climate')],
'13.4':[(S5+'11.b','helpful','Mediterranean climate')],
'13.5':[(S5+'17.b','helpful','hot desert locations')],
'13.6':[(S5+'1.b','helpful','equatorial rainforest climate')],
'14.0':[(S5+'18.3','helpful','climate changes with altitude')],
'16.3':[(S5+'8.1','helpful','Irish mild climate')],
'16.4':[(S5+'9.1','helpful','Irish rainfall figures')],
'22.1':[(S5+'2.0','helpful','tropical rainfall')],
'24.2':[(S5+'15.0','helpful','continental precipitation')],
'25.0':[(S5+'15.1','helpful','winter snow and spring melt','low')],
'26.3':[(S5+'16.0','helpful','Dust Bowl')],
}
def build(pk,costmode,n,out):
    I=ids(pk); res={}
    for i in I:
        s=i[len(P):]; d={}
        if costmode: d['cost']=2 if s in c2 else 1
        d['needs']=[L(*x) for x in n.get(s,[])]
        res[i]=d
    allids=set(re.findall(r'^\[([^\]]+)\]',open(G+'packs/'+pk).read(),re.M))
    for d in res.values():
        for x in d['needs']: assert x['id'] in allids,x
    for s in n: assert P+s in res,s
    json.dump(res,open(G+'point-links/'+out,'w'),indent=1)
    lk=sum(len(d['needs']) for d in res.values())
    lo=sum(x['confidence']=='low' for d in res.values() for x in d['needs'])
    print(pk,len(res),lk,sum(d.get('cost')==2 for d in res.values()),lo)
build('geo-option-geoecology-s2.t1g1.txt',True,n1,'geo-option-geoecology-s2.t1g1.json')
build('geo-option-geoecology-s2.t1g2.txt',False,n2,'geo-option-geoecology-s2.t1g2.json')
