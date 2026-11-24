import json,re
P='geo-graph-skills-s2.'
src=open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-graph-skills-s2.t1g1.txt').read()
tg=src.split('CANDIDATES')[0]
tids=re.findall(r'^\[(geo-graph-skills-s2\.[^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',src,re.M))
def L(i,s,w,c='high'):return {"id":i if i.startswith('geo-') else P+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={}
def s(k,cost,*n):d[P+k]=(cost,list(n))
for k in "0.b 0.0 0.2 0.3 0.4 0.5 1.b 1.0 1.1 1.2 1.3 2.b 2.0 2.1 2.3 2.4 2.5 3.b 3.0 3.1 3.2 3.4 4.b 4.0 4.3 5.b 5.0 5.1 5.2 5.3 5.5 5.6 5.7 6.b 6.0 6.1 6.2 6.3 7.b 7.0 7.1 7.2 7.3 8.b 8.0 8.3 9.b 9.0 9.1 9.2 10.b 10.0 10.1 10.2 10.4 11.b 11.1b 12.b 12.0 12.1 12.2 12.3 12.4 12.5 13.b 13.0 13.1 13.2 13.5 14.b 14.1 14.2 14.4 15.b 15.0 15.1".split():
    if k!='11.1b': s(k,1)
s('0.1',2); s('1.4',1,L('1.3',H,'records closed for 100 years'))
s('2.2',2); s('3.3',1,L('s1.4.1',H,'uses percentage change formula'))
s('3.5',1,L('3.4',H,'Northern Ireland census details'))
s('4.1',2); s('4.2',1,L('4.1',H,'Small Areas in the units list'))
s('5.4',1,L('8.0',H,'uses age structure groups'))
s('7.4',1,L('4.1',H,'uses Electoral Divisions and Small Areas'))
s('7.5',2)
s('8.1',2,L('8.0',E,'uses the three age groups'))
s('8.2',1,L('8.0',E,'uses young and old dependents'))
s('8.4',1,L('8.1',E,'applies dependency ratio formula'),L('8.3',E,'uses the age figures'))
s('8.5',1,L('8.3',E,'uses the age figures'),L('s1.4.0',H,'percentage of a total formula'))
s('8.6',1,L('s1.12.1',E,'population pyramid drawing'))
s('9.3',1,L('9.0',E,'applies sex ratio formula'))
s('10.3',2,L('10.0',E,'population change formula'),L('10.1',H,'natural increase from births, deaths'))
s('10.5',1,L('10.4',E,'uses the population change figures'),L('s1.4.1',H,'percentage change formula'))
s('10.6',2,L('10.3',E,'net migration = change minus natural increase'),L('10.4',H,'uses the change of +630'))
s('11.0',1,L('s1.5.0',H,'rate per 1,000 method'))
s('11.1',1,L('s1.5.1',H,'density = number per area'))
s('11.2',1,L('s1.4.0',H,'percentage of a total'))
s('11.3',1,L('11.0',E,'crude birth rate formula'))
s('13.3',2,L('8.1',E,'dependency ratio calculation'),L('9.0',E,'sex ratio calculation'),L('s1.4.1',H,'percentage change calculation'))
s('13.4',2,L('s1.10.1',H,'line graph of trends'),L('s1.12.1',H,'population pyramid'),L('s1.16.0',H,'choropleth map'))
s('13.6',1,L('13.4',H,'graph types from step 5'))
s('14.0',1,L('8.2',H,'young dependency ratio meaning'))
s('14.3',2,L('14.0',E,'new estates bring young dependents'),L('10.2',H,'positive net migration'))
out={}
for t in tids:
    assert t in d,t
    c,n=d[t]; out[t]={"cost":c,"needs":n}
assert set(d)==set(tids),set(d)^set(tids)
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-graph-skills-s2.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
