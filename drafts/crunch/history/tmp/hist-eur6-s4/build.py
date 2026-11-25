import json,re,sys
P='hist-eur6-'
D='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
DATA='''
s4.0.b 1
s4.0.0 2
s4.0.1 1 => s4.0.0,H,h,Hollywood Ten and studio hearings
s4.0.2 2
s4.0.3 1
s4.0.4 1
s4.0.5 1
s4.0.6 1
s4.0.7 1
s4.0.8 1
s4.1.b 1 => s4.0.b,H,h,uses the Red Scare
s4.1.0 1
s4.1.1 2 => s4.1.6,E,h,uses the Wheeling speech ;; s4.0.2,H,h,uses the Hiss conviction ;; s4.0.7,H,h,uses Fuchs's arrest ;; s2.0.6,H,h,uses the loss of China
s4.1.2 1 => s4.1.6,H,h,investigates his Wheeling claims
s4.1.3 1
s4.1.4 1 => s4.1.7,H,l,his 1953 investigations as chairman
s4.1.5 1
s4.1.6 1
s4.1.7 1
s4.1.8 1 => s4.1.7,H,h,his 1954 inquiry into the army
s4.1.9 1
s4.1.10 1
s4.1.11 1
s4.1.12 1
s4.1.13 2 => s4.1.11,H,l,uses the Venona decrypts
s4.2.b 1
s4.2.0 1 => s2.0.6,H,h,uses the communist victory in China
s4.2.1 1
s4.2.2 1 => s4.2.0,H,h,uses the lost China charge
s4.2.3 1 => s2.3.b,H,l,uses the Korean War
s4.2.4 1 => s4.5.0,H,l,uses Eisenhower's security checks
s4.2.5 1 => s9.0.5,H,h,uses the Little Rock crisis
s4.3.b 1
s4.3.0 1
s4.3.1 1
s4.3.2 1
s4.3.3 1
s4.3.4 1
s4.3.5 1 => s2.5.13,E,h,uses the invasion of Cambodia
s4.3.6 1
s4.3.7 1 => s3.3.6,H,l,uses the draft
s4.3.8 1
s4.3.9 1
s4.3.10 1 => s3.1.3,E,h,uses the Gulf of Tonkin Resolution
s4.4.b 1
s4.4.0 1 => s9.0.3,H,h,uses the Brown ruling
s4.4.1 1 => s9.0.5,H,h,uses the Little Rock crisis
s4.4.2 1
s4.4.3 1 => s9.1.2,H,h,uses the Freedom Rides ;; s9.1.3,H,h,uses the Birmingham campaign
s4.4.4 1 => s9.4.5,H,h,uses Malcolm X ;; s9.3.13,H,l,uses King's Vietnam criticism
s4.4.5 1 => s9.2.0,H,h,uses the Civil Rights Act ;; s9.2.1,H,h,uses the Voting Rights Act
s4.4.6 1 => s9.0.3,H,h,uses the Brown case
s4.5.b 1 => s4.0.5,H,h,uses Truman's loyalty rules
s4.5.0 1 => s4.0.5,H,h,uses Truman's loyalty programme
s4.5.1 1 => s4.5.0,E,h,uses the new security criteria
s4.5.2 1 => s4.1.8,H,h,uses the Army hearings of 1954
s4.5.3 1 => s4.0.2,E,h,uses the Hiss investigation
s4.6.b 1
s4.6.0 1
s4.6.1 2 => s2.5.13,H,h,uses the Cambodia operations
s4.6.2 1
s4.6.3 1 => s4.3.6,H,h,uses the Pentagon Papers
s4.7.b 1
s4.7.0 1 => s4.1.11,H,h,uses the Venona decrypts
s4.7.1 1 => s4.2.2,H,h,uses weakened China expertise
s4.7.2 1 => s3.6.7,H,h,uses Johnson's 1968 decision not to run
s4.7.3 1
s4.7.4 1 => s4.0.b,H,h,uses the Red Scare
'''
pk=open(D+'packs/hist-eur6-s4.t1g1.txt').read()
tg=pk.split('CANDIDATES')[0]
tids=re.findall(r'^\[(hist-eur6-s4\.[^\]]+)\]',tg,re.M)
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
json.dump(out,open(D+'point-links/hist-eur6-s4.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
