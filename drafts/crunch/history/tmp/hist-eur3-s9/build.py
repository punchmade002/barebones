import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
costs={0:"1112",1:"111111",2:"11111112",3:"11111111",4:"12211",5:"1112",6:"1111",7:"1111",8:"11111",9:"12112",10:"11111111",11:"1111111",12:"1111",13:"111112",14:"11111211",15:"111111211",16:"1111111",17:"12111",18:"1111111",19:"1112121",20:"112111112",21:"1211221",22:"1111111",23:"111121",24:"12211111",25:"112",26:"1111221",27:"1111111",28:"111111"}
P='hist-eur3-s9.'
def i(x): return P+x
# links: item|need|strength|why|conf   (strength h=helpful e=essential; conf H/L)
L1="""
0.0|s3.14.3|h|Hitler's demands and Polish guarantee|H
0.1|s3.14.4|h|Nazi-Soviet Pact explained|H
1.1|9.1.0|h|tanks the air support accompanies|H
1.2|9.1.0|h|Panzer armour and motorised infantry|H
1.4|9.2.1|h|Poland campaign of 1939|H
2.0|9.0.0|h|Anglo-French guarantee to Poland|H
2.1|9.0.1|e|Nazi-Soviet Pact division of Poland|H
2.2|9.2.0|h|Britain and France at war|H
2.4|9.2.3|e|German invasion of Norway|H
2.5|9.2.4|h|German victory in Norway|H
2.6|9.2.4|e|failure in Norway|H
3.1|9.3.0|e|Ardennes thrust|H
3.2|9.3.0|e|Ardennes armoured thrust|H
3.3|9.3.2|h|sickle cut through the Ardennes|L
3.4|9.3.3|e|forces cut off in the north|H
4.1|9.4.0|e|attempt to win air superiority|H
4.2|9.4.0|e|Operation Sea Lion|H
4.3|9.4.0|h|failure to win air superiority|L
5.1|9.5.0|e|Italian defeats needing rescue|H
5.2|9.5.1|e|German intervention in Balkans/Africa|H
6.b|0.1|h|Nazi-Soviet Pact|H
6.0|9.2.1|e|partition of Poland|H
7.0|9.6.2|h|Operation Barbarossa|H
7.1|9.7.0|h|Barbarossa advance|H
7.2|1.b|h|blitzkrieg aim of quick victory|H
8.1|9.8.0|e|Japanese occupation of Indochina|H
8.2|9.8.1|h|embargo pushing Japan to attack|L
8.3|9.8.2|e|Pearl Harbor|H
9.0|9.8.2|h|Pearl Harbor then conquests|L
9.1|9.9.0|h|Japanese advance halted|H
9.2|9.9.1|h|American counter-offensive|H
9.3|21.4|h|atomic bombs on Hiroshima, Nagasaki|H
10.0|5.1|h|Rommel and the Afrika Korps|H
10.1|10.0|h|El Alamein in North Africa|H
10.2|7.0|h|Eastern Front invasion|H
10.3|10.2|h|German offensives in the east|H
10.4|10.1|h|Axis expelled from North Africa|L
10.6|10.5|e|Battle of the Atlantic|H
11.0|10.0|h|Montgomery at El Alamein|L
11.1|11.0|e|D-Day landings|H
11.2|11.0|e|Normandy beachheads|H
11.4|11.3|h|Soviet offensive on Berlin|H
11.5|11.4|h|Hitler's death|H
12.1|8.3|e|German declaration on the US|H
12.2|18.0|h|radar|H
13.0|3.5|h|Italy entering the war|H
13.1|13.0|h|Axis alliance background|L
13.2|13.1|e|Tripartite Pact|H
13.3|5.0|e|Italian defeats in Greece and Africa|H
13.4|8.2|h|Pearl Harbor|H
14.0|7.0|h|Barbarossa|H
14.0|8.2|h|Pearl Harbor|H
14.5|14.4|e|Atlantic Charter|H
14.6|8.3|h|global war|L
15.1|11.0|h|Overlord|H
15.5|15.2|h|Curzon Line|H
15.5|16.3|h|Lublin government|L
15.6|15.4|e|Yalta conference|H
15.7|25.0|h|Churchill replaced by Attlee|H
16.1|16.0|h|second front|H
16.3|16.2|h|Polish government in London|H
16.4|11.3|h|Red Army advance into Poland|H
17.0|1.0|h|Panzer divisions|H
17.1|19.2|h|strategic bombing|H
17.2|s3.12.3|h|Condor Legion|H
17.3|4.1|h|Hurricane and Spitfire|L
18.1|18.0|e|Chain Home radar|H
19.0|1.0|h|Panzer divisions|H
19.1|19.0|h|tanks the guns answer|H
19.3|19.2|h|strategic bombing|H
19.4|19.2|h|strategic bombing|H
19.5|19.2|e|strategic bombing|H
20.0|18.0|e|Chain Home|H
20.1|18.0|h|radar|H
20.2|20.1|h|small radar sets|H
20.3|18.2|e|Enigma|H
20.4|20.3|e|decrypting Enigma|H
20.5|20.3|h|Bletchley codebreaking|L
20.6|10.5|h|Battle of the Atlantic|H
20.7|20.6|e|U-boat wolf packs|H
20.7|20.4|h|Ultra|H
21.0|18.4|h|V-2 rocket development|H
21.1|21.0|e|V-weapons|H
21.4|21.3|h|Manhattan Project|H
21.5|21.4|h|atomic bombs|H
22.4|s3.16.0|h|appeasement|H
22.5|s3.13.3|e|Munich agreement|H
23.0|2.6|e|Norway debate|H
23.2|3.6|h|fall of France|L
23.3|3.4|h|Dunkirk|H
23.3|4.3|h|the Blitz|H
23.4|4.0|e|Battle of Britain|H
24.0|14.1|e|destroyers-for-bases deal|H
24.0|14.2|e|Lend-Lease|H
24.0|14.4|e|Atlantic Charter|H
24.0|14.6|h|Germany first policy|H
24.1|14.4|h|Placentia Bay meeting|H
24.1|15.0|h|Casablanca|H
24.1|15.1|h|Tehran|H
24.1|15.4|h|Yalta|H
24.2|15.3|e|percentages agreement|H
24.3|15.7|e|Potsdam conference|H
24.4|16.1|h|Mediterranean strategy|H
24.4|19.2|h|strategic bombing|H
24.5|9.0|h|fall of Singapore|H
24.5|10.0|h|Rommel's North African campaign|L
24.6|12.0|h|US and Soviet production|H
25.0|15.7|h|Potsdam|H
25.1|25.0|h|1945 election defeat|H
26.0|22.2|h|Gallipoli|H
26.0|22.3|h|return to the gold standard|H
26.4|19.4|h|bombing of Dresden|H
27.0|23.2|e|refusal of negotiated peace|H
27.1|9.0|h|losses of Hong Kong, Singapore|H
27.1|14.2|h|American resources|L
27.2|14.b|h|Grand Alliance|H
27.3|16.5|h|Allied divisions|H
27.4|26.0|h|contemporary views of Churchill|L
28.1|20.0|h|radar in 1940|H
28.1|20.7|h|Atlantic convoys and Ultra|H
28.2|21.1|h|V-weapons too late|H
28.2|21.2|h|Me 262 too late|H
28.3|19.0|e|Sherman and T-34 mass production|H
28.4|19.5|h|strategic bombing debate|H
28.4|21.4|h|atomic bombs|H
"""
L2="""
0.1|s4.14.4|h|Nazi-Soviet Pact, Soviet side|H
2.1|s4.14.5|h|Red Army entering eastern Poland|H
6.0|s4.14.5|h|Soviet share of Poland|H
6.1|s4.14.4|h|Nazi-Soviet Pact|L
6.2|s4.15.0|h|Barbarossa and Soviet losses|H
7.1|s4.15.0|h|siege of Leningrad|H
7.2|s4.15.2|h|Soviet counter-offensive December 1941|H
10.2|s4.16.0|h|Stalingrad encirclement|H
10.3|s4.16.1|h|Kursk and Soviet initiative|H
11.3|s4.16.1|h|Red Army advance to Berlin|H
12.0|s4.15.4|h|Soviet tank and aircraft output|H
13.2|s4.14.6|h|Soviet war with Finland|L
14.0|s4.15.0|h|Soviet entry after Barbarossa|H
14.2|s4.16.3|h|Lend-Lease to Soviet Union|H
15.2|s4.17.2|h|Stalin at Tehran|H
16.2|s4.14.5|e|NKVD killing Polish officers|H
16.5|s4.17.0|h|Soviet control of eastern Europe|H
19.0|s4.15.4|h|T-34 tank|H
24.0|s4.0.1|h|Marxist anti-communism context|L
27.3|s4.17.0|h|Soviet control of eastern Europe|H
28.3|s4.15.4|h|Soviet T-34 production|H
"""
def ids_of(pack):
    out=[]
    for l in open(D+'packs/'+pack):
        if l.startswith('CANDIDATES'): break
        m=re.match(r'\[(\S+)\]',l)
        if m: out.append(m.group(1))
    return out
def allids(pack):
    return {m.group(1) for l in open(D+'packs/'+pack) for m in [re.match(r'\[(\S+)\]',l)] if m}
def parse(L):
    d={}
    for l in L.strip().splitlines():
        a,n,s,w,c=l.split('|')
        nid=n if n.startswith('s3.') or n.startswith('s4.') else None
        nid=(P[:-1]+'-'+n) if False else None
        d.setdefault(a,[]).append((n,s,w,c))
    return d
def fullid(n):
    if n.startswith('s'): return 'hist-eur3-'+n
    if n.count('.')==2: return 'hist-eur3-s'+n
    return P+n
def build(pack,L,withcost):
    t=ids_of(pack); ok=allids(pack)
    # expected explicit ids from cost table
    exp=[]
    for s,cs in costs.items():
        exp.append((i(f'{s}.b'),int(cs[0])))
        for k,ch in enumerate(cs[1:]): exp.append((i(f'{s}.{k}'),int(ch)))
    assert [e[0] for e in exp]==t,(len(exp),len(t))
    links=parse(L); res={}
    for iid,c in exp:
        short=iid[len(P):]
        needs=[]
        for n,s,w,cf in links.get(short,[]):
            nid=fullid(n)
            assert nid in ok and nid!=iid,(iid,nid)
            if not withcost: assert nid.startswith('hist-eur3-s4.'),nid
            needs.append({"id":nid,"strength":"essential" if s=='e' else "helpful","why":w,"confidence":"high" if cf=='H' else "low"})
        d={}
        if withcost: d['cost']=c
        d['needs']=needs; res[iid]=d
    assert set(links)<={e[0][len(P):] for e in exp}
    return res
for pack,L,wc,out in [('hist-eur3-s9.t1g1.txt',L1,True,'hist-eur3-s9.t1g1.json'),('hist-eur3-s9.t1g2.txt',L2,False,'hist-eur3-s9.t1g2.json')]:
    r=build(pack,L,wc)
    json.dump(r,open(D+'point-links/'+out,'w'),indent=1,ensure_ascii=False)
    chk=json.load(open(D+'point-links/'+out))
    nl=sum(len(v['needs']) for v in chk.values())
    low=sum(1 for v in chk.values() for n in v['needs'] if n['confidence']=='low')
    c2=sum(1 for v in chk.values() if v.get('cost')==2)
    print(pack,len(chk),nl,c2 if wc else '-',low)
