import re, json
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-economic-environment-s4.t1g%d'
E='geo-economic-environment-s4.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# cost 2 items
c2={'0.1','4.0','4.2','13.1','14.0','15.1','17.0','17.1','17.2','17.3','18.2','21.1','24.0','26.3','12.4','30.2'}
g1={
'1.0':[L('geo-economic-environment-s1.0.3','helpful','renewable only if used sustainably')],
'1.1':[L('geo-economic-environment-s1.0.1','helpful','non-renewable resource meaning')],
'1.2':[L('geo-economic-environment-s3.0.0','helpful','what counts as pollution')],
'0.1':[L(E+'0.0','helpful','sustainable development defined')],
'4.1':[L(E+'4.0','helpful','licence requirement idea')],
'4.2':[L(E+'4.0','helpful','what an EPA licence is')],
'6.0':[L(E+'4.1','essential','emission limits in licence')],
'7.1':[L('geo-economic-environment-s3.1.1','helpful','diffuse sources')],
'8.1':[L(E+'8.0','essential','what an impact assessment is')],
'9.0':[L(E+'8.0','helpful','impact assessment meaning')],
'9.1':[L(E+'8.0','helpful','impact assessment meaning')],
'10.b':[L(E+'8.1','essential','EIAR is the report')],
'10.4':[L(E+'8.1','helpful','EIAR and developer role')],
'11.0':[L(E+'8.1','essential','EIAR is prepared')],
'12.4':[L(E+'8.0','helpful','impact assessment missing at Derrybrien')],
'13.0':[L('geo-economic-environment-s1.0.3','helpful','fish renewable if managed')],
'13.1':[L(E+'13.0','essential','stock breeding rate idea')],
'14.0':[L(E+'13.0','helpful','catch rate versus stock recovery')],
'14.1':[L(E+'13.0','helpful','stock replacement rate')],
'14.3':[L(E+'13.0','essential','stock must breed to renew')],
'17.2':[L(E+'13.1','essential','maximum sustainable yield'),L(E+'14.4','essential','discards')],
'18.3':[L(E+'17.0','helpful','quotas and conservation limits','low')],
'19.1':[L(E+'19.0','essential','acid mine drainage')],
'20.1':[L(E+'4.1','helpful','licence emission limits')],
'21.1':[L(E+'8.1','essential','EIAR')],
'23.1':[L(E+'22.1','helpful','bogs harvested for peat')],
'23.2':[L(E+'23.1','essential','cutaway bog rehabilitation')],
'23.3':[L(E+'23.1','helpful','cutaway bog reuse')],
'24.2':[L(E+'24.1','helpful','sea shrinking')],
'25.0':[L('geo-economic-environment-s1.0.2','helpful','renewable energy sources')],
'26.2':[L('geo-economic-environment-s3.15.0','helpful','nitrates rules to stop runoff')],
'26.4':[L(E+'26.3','helpful','Burren farming scheme')],
'27.3':[L(E+'27.2','helpful','visitor limits')],
'29.b':[L(E+'1.3','essential','polluter pays principle')],
'29.0':[L(E+'1.3','essential','polluter pays principle')],
'29.1':[L(E+'1.3','helpful','polluter pays principle')],
'29.2':[L(E+'1.3','helpful','polluter pays principle')],
'29.3':[L('geo-economic-environment-s3.9.0','helpful','emissions trading system')],
'30.2':[L('geo-economic-environment-s3.9.5','helpful','retrofit homes target')],
'30.3':[L(E+'28.2','helpful','circular economy','low')],
}
S1='geo-economic-activities-s1.'
g2={
'19.0':[L('geo-rocks-weathering-s2.3.2','helpful','acid mine drainage at Avoca')],
'19.1':[L('geo-rocks-weathering-s2.3.2','helpful','acid mine drainage at Avoca')],
'20.1':[L('geo-rocks-weathering-s2.4.0','helpful','licensing and monitoring of mines','low')],
'20.2':[L('geo-rocks-weathering-s2.4.1','helpful','lined tailings ponds')],
'21.0':[L('geo-rocks-weathering-s2.4.2','helpful','Lisheen rehabilitation')],
'18.0':[L(S1+'15.3','helpful','Killybegs pelagic port')],
'18.1':[L(S1+'15.3','helpful','Killybegs pelagic fleet')],
'18.2':[L(S1+'15.2','helpful','six fishery harbour centres')],
'17.0':[L(S1+'16.0','helpful','CFP quotas')],
}
EU='geo-economic-eu-s3.'
g3={
'14.5':[L(EU+'14.0','helpful','national quotas from TACs')],
'16.2':[L(EU+'14.0','helpful','quotas after stock recovery','low')],
'17.0':[L(EU+'13.0','helpful','Common Fisheries Policy aims')],
'17.1':[L(EU+'14.2','helpful','mesh sizes and closed areas')],
'17.2':[L(EU+'18.0','helpful','2013 reform and landing obligation')],
'18.0':[L(EU+'15.0','helpful','Killybegs pelagic port')],
'18.2':[L(EU+'15.1','helpful','Fishery Harbour Centres')],
'26.0':[L(EU+'8.0','helpful','REPS scheme')],
'26.2':[L(EU+'12.0','helpful','Nitrates Directive limits')],
'23.4':[L(EU+'25.1','helpful','Just Transition Fund for Midlands')],
'27.3':[L(S1+'43.4','helpful','Skellig Michael visitors','low')],
}
for n,links in ((1,g1),(2,g2),(3,g3)):
    ids=[m for m in re.findall(r'^\[(geo-economic-environment-s4\.[^\]]+)\]',open(G+'packs/'+P%n+'.txt').read(),re.M)]
    allids=set(re.findall(r'^\[([^\]]+)\]',open(G+'packs/'+P%n+'.txt').read(),re.M))
    out={}
    for i in ids:
        k=i[len(E):]
        d={}
        if n==1: d['cost']=2 if k in c2 else 1
        d['needs']=links.get(k,[])
        out[i]=d
    cnt=0;low=0
    for i,d in out.items():
        for x in d['needs']:
            assert x['id'] in allids and x['id']!=i,(i,x['id'])
            cnt+=1; low+=x['confidence']=='low'
    for k in links: assert E+k in out,k
    json.dump(out,open(G+'point-links/'+P%n+'.json','w'),ensure_ascii=False)
    json.load(open(G+'point-links/'+P%n+'.json'))
    print(n,len(out),cnt,sum(d.get('cost',0)==2 for d in out.values()),low)
