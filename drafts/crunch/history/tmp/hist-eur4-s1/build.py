import json,re,sys
P='hist-eur4-'
D='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
DATA='''
s1.0.b 1
s1.0.0 2
s1.0.1 1
s1.0.2 1 => s1.0.1,H,h,uses the Soviet zone
s1.0.3 1
s1.0.4 1
s1.0.5 2
s1.0.6 1 => s1.0.0,H,h,uses the Yalta Conference
s1.0.7 1
s1.0.8 1
s1.0.9 1
s1.0.10 1 => s1.0.0,H,h,uses Yalta's Polish government
s1.1.b 1
s1.1.0 1 => s1.0.3,H,h,uses the Potsdam Conference
s1.1.1 1 => s1.0.1,H,h,uses the occupation zones
s1.1.2 1 => s1.1.1,H,h,uses zonal reparations
s1.1.3 1 => s1.0.3,H,h,uses the German-Polish border dispute
s1.1.4 1 => s1.0.1,H,h,uses the four occupying powers
s1.1.5 1 => s1.1.0,H,h,uses the single economy aim
s1.2.b 1
s1.2.0 1
s1.2.1 1
s1.2.2 1 => s1.2.1,E,h,answers the Fulton speech
s1.2.3 1
s1.2.4 2 => s1.2.3,H,h,follows Britain's withdrawal from Greece
s1.2.5 1
s1.2.6 1 => s1.2.5,E,h,uses Marshall aid
s1.2.7 1
s1.2.8 1 => s1.2.4,E,h,tests the Truman Doctrine
s1.2.9 1 => s1.2.5,E,h,uses Marshall's offer
s1.2.10 1 => s1.2.5,E,h,uses Marshall aid
s1.3.b 1
s1.3.0 1
s1.3.1 1
s1.3.2 1
s1.3.3 1
s1.3.4 1
s1.3.5 1
s1.3.6 1
s1.3.7 1
s1.3.8 1 => s1.2.7,E,h,uses the Cominform
s1.3.9 2 => s1.3.1,H,h,uses Rakosi's salami tactics
s1.3.10 1
s1.3.11 1 => s1.3.4,H,h,uses the 1948 communist takeover
s1.3.12 1
s1.3.13 1
s1.4.b 1 => s1.2.6,H,h,uses refusal of Marshall aid
s1.4.0 1
s1.4.1 1 => s1.2.5,E,h,the alternative to Marshall aid
s1.4.2 1
s1.4.3 1 => s1.2.6,H,h,uses refusal of Marshall aid
s1.4.4 1 => s1.1.1,H,h,uses Soviet reparations
s1.5.b 1
s1.5.0 1 => s1.0.1,H,h,uses the Western zones
s1.5.1 1 => s1.5.0,H,h,uses the merged Western zones
s1.5.2 1 => s1.0.2,H,h,uses divided Berlin ;; s1.5.1,H,h,uses the currency reform
s1.5.3 1 => s1.5.2,E,h,uses the blockade
s1.5.4 1 => s1.5.0,H,h,uses the merged Western zones
s1.5.5 1 => s1.0.1,H,h,uses the Soviet zone
s1.5.6 1 => s1.0.2,E,h,uses divided Berlin ;; s1.5.4,H,h,uses the Federal Republic ;; s1.5.5,H,h,uses the German Democratic Republic
s1.5.7 1 => s1.5.2,E,h,uses the blockade ;; s1.5.1,H,h,uses the new currency
s1.5.8 1 => s1.5.2,E,h,uses the blockade
s1.5.9 1 => s1.5.3,H,h,uses the airlift
s1.6.b 1
s1.6.0 1
s1.6.1 1 => s1.6.0,H,h,uses the Brussels Treaty
s1.6.2 1 => s1.6.1,E,h,uses NATO ;; s1.5.4,H,h,uses West Germany
s1.6.3 1 => s1.6.2,H,h,uses West German NATO membership
s1.6.4 1 => s1.6.3,E,h,uses the Warsaw Pact
s1.6.5 1 => s1.6.1,H,h,uses NATO
s1.7.b 1
s1.7.0 1
s1.7.1 1 => s1.0.5,H,h,uses the atomic monopoly
s1.7.2 1 => s1.3.9,H,l,uses rigged elections and one-party rule
s1.7.3 1 => s1.5.1,E,h,uses the June 1948 currency reform
s1.7.4 1
s1.7.5 1 => s1.0.4,H,h,uses the buffer against invasion
'''
pk=open(D+'packs/hist-eur4-s1.t1g1.txt').read()
tg=pk.split('CANDIDATES')[0]
tids=re.findall(r'^\[(hist-eur4-s1\.[^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
out={}
for line in DATA.strip().split('\n'):
    h,_,l=line.partition(' => ')
    t,c=h.split(); needs=[]
    if l:
        for x in l.split(' ;; '):
            i,s,cf,w=x.split(',',3)
            needs.append({"id":P+i,"strength":"essential" if s=='E' else "helpful","why":w,"confidence":"high" if cf=='h' else "low"})
    assert P+t not in out
    out[P+t]={"cost":int(c),"needs":needs}
assert list(out)==tids,(set(tids)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open(D+'point-links/hist-eur4-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))

