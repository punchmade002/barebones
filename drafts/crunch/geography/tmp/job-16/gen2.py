import re, json
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-economic-environment-s4.t1g%d'
E='geo-economic-environment-s4.'
S1='geo-economic-activities-s1.'; EU='geo-economic-eu-s3.'; R='geo-rocks-weathering-s2.'
V='geo-economic-environment-s'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def h(i,w,c='high'): return L(i,'helpful',w,c)
def e(i,w,c='high'): return L(i,'essential',w,c)
# every key: (cost, g1 links, g2 links, g3 links)  -- all 147 listed explicitly
T={}
def A(k,cost,a=(),b=(),c=()): T[k]=(cost,list(a),list(b),list(c))
for k in '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31'.split(): A(k+'.b',1)
A('0.0',1); A('0.1',2,[h(E+'0.0','sustainable development defined')])
A('1.0',1,[h(V+'1.0.3','renewable only if used sustainably')])
A('1.1',1,[h(V+'1.0.1','non-renewable resource meaning')])
A('1.2',1,[h(V+'3.0.0','what counts as pollution')])
A('1.3',1); A('1.4',1)
A('2.0',1,[h(E+'0.0','sustainable development aim')]); A('2.1',1,[h(E+'0.0','sustainable development aim')])
A('3.0',1); A('3.1',1)
A('4.0',2); A('4.1',1,[h(E+'4.0','licence requirement idea')]); A('4.2',2,[h(E+'4.0','what an EPA licence is')])
A('5.0',1); A('5.1',1,[h(V+'3.2.0','greenhouse gases counted','low')]); A('5.2',1); A('5.3',1); A('5.4',1); A('5.5',1)
A('6.0',1,[e(E+'4.1','emission limits in licence')]); A('6.1',1); A('6.2',1)
A('7.0',1,[h(E+'6.0','inspections of licensed activities')])
A('7.1',1,[h(V+'3.1.1','diffuse sources')]); A('7.2',1,[h(E+'6.2','local authority environmental work')])
A('8.0',1); A('8.1',1,[e(E+'8.0','what an impact assessment is')])
A('9.0',1,[h(E+'8.0','impact assessment meaning')]); A('9.1',2,[h(E+'8.0','impact assessment meaning')])
A('10.0',1); A('10.1',2); A('10.2',1); A('10.3',1)
A('10.4',1,[h(E+'8.1','EIAR and developer role')])
A('11.0',1,[e(E+'8.1','EIAR is prepared')]); A('11.1',1,[h(E+'11.0','step before submissions')]); A('11.2',1,[h(E+'11.1','submissions weighed in decision')])
A('12.0',1,[h(E+'8.0','impact assessment purpose')]); A('12.1',1,[h(E+'10.2','alternatives considered')])
A('12.2',1,[h(E+'11.1','public submissions')]); A('12.3',1)
A('12.4',2,[h(E+'8.0','impact assessment missing at Derrybrien')])
A('13.0',1,[h(V+'1.0.3','fish renewable if managed')]); A('13.1',2,[e(E+'13.0','stock breeding rate idea')])
A('14.0',2,[h(E+'13.0','catch rate versus stock recovery')]); A('14.1',1,[h(E+'13.0','stock replacement rate')])
A('14.2',1); A('14.3',1,[e(E+'13.0','stock must breed to renew')]); A('14.4',1); A('14.5',1,[],[],[h(EU+'14.0','national quotas from TACs')])
A('15.0',1); A('15.1',2,[h(E+'14.0','factory ships and technology')]); A('15.2',1,[h(E+'15.1','stock collapse before ban')]); A('15.3',1); A('15.4',1)
A('16.0',1); A('16.1',1,[h(E+'13.0','time to breed','low')]); A('16.2',1,[],[],[h(EU+'14.0','quotas after recovery','low')])
A('17.0',2,[],[h(S1+'16.0','CFP quotas')],[h(EU+'13.0','Common Fisheries Policy aims')])
A('17.1',2,[],[],[h(EU+'14.2','mesh sizes and closed areas')])
A('17.2',2,[e(E+'13.1','maximum sustainable yield'),e(E+'14.4','discards')],[],[h(EU+'18.0','2013 reform and landing obligation')])
A('17.3',2); A('17.4',1); A('17.5',1)
A('18.0',1,[],[h(S1+'15.3','Killybegs pelagic port')],[h(EU+'15.0','Killybegs pelagic port')])
A('18.1',1,[],[h(S1+'15.3','Killybegs pelagic fleet')])
A('18.2',2,[],[h(S1+'15.2','six fishery harbour centres')],[h(EU+'15.1','Fishery Harbour Centres')])
A('18.3',1,[h(E+'17.0','quotas and conservation limits','low')])
A('19.0',1,[],[h(R+'3.2','acid mine drainage at Avoca')])
A('19.1',1,[e(E+'19.0','acid mine drainage')],[h(R+'3.2','acid mine drainage at Avoca')])
A('20.0',2,[],[h(R+'2.2.0'.replace('2.2.0','2.0') if False else R+'2.0','Tara Mines facts')])
A('20.1',1,[h(E+'4.1','licence emission limits')],[h(R+'4.0','licensing and monitoring of mines','low')])
A('20.2',1,[],[h(R+'4.1','lined tailings ponds')]); A('20.3',1,[],[h(R+'4.2','mine rehabilitation','low')])
A('21.0',1,[],[h(R+'4.2','Lisheen rehabilitation')]); A('21.1',2,[e(E+'8.1','EIAR')])
A('22.0',1,[],[h(S1+'18.3','peat harvesting by Bord na Mona','low')]); A('22.1',1)
A('23.0',1,[],[h(S1+'18.2','peat stations closed')]); A('23.1',1,[h(E+'22.1','bogs harvested for peat')])
A('23.2',1,[e(E+'23.1','cutaway bog rehabilitation')]); A('23.3',1,[h(E+'23.1','cutaway bog reuse')])
A('23.4',1,[],[],[h(EU+'25.1','Just Transition Fund for Midlands')])
A('24.0',2); A('24.1',1); A('24.2',1,[h(E+'24.1','sea shrinking')]); A('24.3',1); A('24.4',1,[h(E+'24.1','northern sea shrank')])
A('25.0',1,[h(V+'1.0.2','renewable energy sources')])
A('26.0',1,[],[],[h(EU+'8.0','REPS scheme')]); A('26.1',1)
A('26.2',1,[h(V+'3.15.0','nitrates rules to stop runoff')],[],[h(EU+'12.0','Nitrates Directive limits')])
A('26.3',2); A('26.4',1,[h(E+'26.3','Burren farming scheme')])
A('27.0',1); A('27.1',1); A('27.2',1)
A('27.3',1,[h(E+'27.2','visitor limits')],[],[L(S1+'43.4','helpful','Skellig Michael visitors','low')])
A('28.0',1); A('28.1',1,[h(E+'1.3','levies make polluters pay','low')]); A('28.2',1)
A('29.0',1,[e(E+'1.3','polluter pays principle')]); A('29.1',1,[h(E+'1.3','polluter pays principle')])
A('29.2',1,[h(E+'1.3','polluter pays principle')]); A('29.3',1,[h(V+'3.9.0','emissions trading system')])
T['29.b']=(1,[e(E+'1.3','polluter pays principle')],[],[])
A('30.0',1); A('30.1',1); A('30.2',2,[h(V+'3.9.5','retrofit homes target')]); A('30.3',1,[h(E+'28.2','circular economy','low')]); A('30.4',1)
A('31.0',1); A('31.1',1); A('31.2',1,[],[],[h(EU+'25.1','peat jobs and Just Transition','low')]); A('31.3',1)
new={}
for n in (1,2,3):
    txt=open(G+'packs/'+P%n+'.txt').read()
    ids=re.findall(r'^\[(geo-economic-environment-s4\.[^\]]+)\]',txt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert len(ids)==len(set(ids))==147
    miss=[i for i in ids if i[len(E):] not in T]; assert not miss,miss
    out={};cnt=low=0
    for i in ids:
        c,*gl=T[i[len(E):]]; nd=gl[n-1]
        for x in nd: assert x['id'] in allids and x['id']!=i,(i,x['id']); cnt+=1; low+=x['confidence']=='low'
        out[i]=({'cost':c} if n==1 else {})|{'needs':nd}
    new[n]=out
    old=json.load(open(G+'tmp/job-16/old/'+P%n+'.json'))
    ch=sum(old[i]!=out[i] for i in ids)
    json.dump(out,open(G+'point-links/'+P%n+'.json','w'),ensure_ascii=False); json.load(open(G+'point-links/'+P%n+'.json'))
    print(n,len(out),cnt,sum(d.get('cost')==2 for d in out.values()),low,'changed',ch)
# defaulted = items with no entry in old script's tables = old items with cost1 & no needs in all 3
old=[json.load(open(G+'tmp/job-16/old/'+P%n+'.json')) for n in (1,2,3)]
d=[i for i in old[0] if old[0][i]['cost']==1 and not any(o[i]['needs'] for o in old)]
print('defaulted',len(d),'changed',sum(any(new[n][i]!=old[n-1][i] for n in (1,2,3)) for i in d))
