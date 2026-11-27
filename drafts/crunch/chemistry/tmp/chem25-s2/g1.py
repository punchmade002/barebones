import json,re
# line: id|cost|ref;ref  ref=id,E/H,why[,L]   prefixes: a=chem24-s1 b=chem25-s1 c=chem23-s2 ; bare = chem25-s2
P={'a':'chem24-s1','b':'chem25-s1','c':'chem23-s2'}
def full(x):
    m=re.match(r'^([abc]):(.*)$',x)
    return P[m.group(1)]+'.'+m.group(2) if m else 'chem25-s2.'+x
D="""
0.b|1|
0.0|1|a:2.2,H,aldehyde group -CHO
0.1|1|a:2.3,H,ketone group C=O between carbons
0.2|1|0.0,E,hydrogen on carbonyl carbon;b:3.0,H,oxidation as gain of oxygen
0.3|1|0.1,E,ketone carbonyl has no hydrogen
0.4|1|0.2,E,aldehyde oxidised easily;0.3,E,ketone not oxidised
1.b|1|
1.0|2|
1.1|1|1.0,H,Fehling's A and B mixture
1.2|1|1.0,H,Fehling's reagent contents
2.b|1|0.4,H,colour change tells aldehyde from ketone
2.0|1|1.0,E,Fehling's reagent
2.1|1|2.0,E,tube set-up with Fehling's
2.2|1|2.1,H,tubes containing liquids
2.3|1|2.2,E,warm tubes in water bath
2.4|1|2.2,E,warmed tubes
2.5|1|2.3,E,ethanal result;2.4,E,propanone result
3.b|1|
3.0|1|1.0,H,Fehling's B contains sodium hydroxide
3.1|1|2.2,H,water bath heating
3.2|1|2.2,E,test tube set-up
4.b|1|b:3.0,H,oxidation and reduction
4.0|1|1.1,E,Cu2+ ions in reagent;b:3.0,H,oxidation meaning
4.1|1|4.0,E,aldehyde oxidation by reagent;a:3.0,H,carboxylic acid
4.2|1|4.0,E,Cu2+ reduced;b:3.2,H,oxidation number change
4.3|2|4.2,E,reduction half-equation
4.4|2|4.3,E,reduction half-equation;4.1,E,aldehyde to ethanoate
4.5|1|0.2,H,aldehydes easily oxidised;4.0,H,mild oxidising agent
5.b|1|
5.0|1|b:4.0,H,acid behaviour
5.1|1|5.0,H,showing acid behaviour
5.2|2|5.0,E,tests of acid behaviour
6.b|1|
6.0|1|5.0,H,reaction with metal test
6.1|1|6.0,E,gas from magnesium reaction
6.2|1|6.0,H,magnesium and ethanoic acid;6.1,H,hydrogen product
6.3|2|6.0,E,magnesium reaction rate
6.4|1|6.0,E,magnesium test;6.1,H,lighted taper test
7.b|1|
7.0|1|5.0,H,carbonate test
7.1|1|7.0,E,gas from carbonate reaction
7.2|1|7.0,H,carbonate reaction;b:4.2,H,same equation
7.3|1|7.1,E,limewater test
8.b|1|
8.0|1|b:4.1,H,acid with base equation
8.1|1|8.0,E,neutralisation with no visible change
9.b|1|
9.0|1|
9.1|1|6.1,H,hydrogen pop test
10.b|1|
10.0|1|
10.1|1|10.0,E,reaction scheme
10.2|1|10.0,E,reaction scheme;a:0.0,H,functional group
10.3|1|10.2,E,comparing formulae at arrows
10.4|2|b:3.0,E,oxidation;b:3.1,E,reduction;b:0.0,H,addition
10.5|2|b:2.0,E,elimination;b:1.0,E,substitution
10.6|1|b:4.1,E,carboxylic acid with base
11.b|1|a:1.4,H,alkene double bond
11.0|1|b:1.2,E,ethane to chloroethane substitution
11.1|1|b:0.6,E,hydrogenation of ethene
11.2|1|b:0.4,E,ethene and HCl
11.3|1|b:0.3,E,ethene and chlorine
11.4|1|b:0.2,E,ethene and bromine
11.5|1|b:0.5,E,ethene and water
11.6|1|b:2.1,E,dehydration of ethanol
11.7|1|b:2.4,E,loss of HCl from haloalkane
12.b|1|
12.0|1|b:3.3,E,oxidation of ethanol
12.1|1|b:3.4,E,ethanal reduced to ethanol
12.2|1|b:1.3,E,esterification
12.3|1|b:1.6,E,ester hydrolysis
12.4|1|b:4.1,E,acid with base;b:4.2,H,acid with carbonate
13.b|1|
13.0|1|b:8.0,E,addition polymerisation
13.1|1|b:2.5,E,1,2-dichloroethane loses HCl;b:10.0,H,chloroethene monomer
13.2|2|11.b,H,ethene reactions;12.b,H,ethanol reactions;13.0,H,polymerisation
14.b|1|a:7.0,H,primary and secondary alcohols
14.0|1|12.0,E,two-step oxidation;a:7.0,E,primary alcohol
14.1|1|a:7.2,E,secondary alcohol;12.0,H,oxidation with KMnO4
14.2|1|12.1,E,reduction with H2 and nickel
14.3|1|b:2.3,E,propan-2-ol dehydration
14.4|1|11.1,E,hydrogenation of alkene
14.5|1|b:3.0,H,oxidation,L
15.b|1|
15.0|1|14.0,H,primary alcohol gives aldehyde;14.1,H,secondary gives ketone
15.1|1|11.6,H,alcohol to alkene;11.5,H,alkene to alcohol
15.2|1|12.2,H,esterification joins molecules;12.3,H,hydrolysis splits
16.b|1|
16.0|1|a:0.3,H,functional group reactions
16.1|1|b:0.0,E,addition
16.2|2|12.0,E,alcohol oxidation;12.2,E,ester formation;12.3,E,ester with NaOH
16.3|2|11.5,E,ethene to ethanol;12.0,E,oxidation of ethanol
16.4|2|12.1,E,reduction of ethanal;12.0,E,oxidation to acid;12.2,E,esterification
16.5|1|11.7,E,elimination to ethene;11.5,E,addition of water
16.6|1|12.2,E,esterification;a:13.3,E,naming esters
17.b|1|a:17.0,H,tetrahedral carbon
17.0|1|a:17.0,H,tetrahedral geometry
17.1|1|a:17.2,H,planar geometry
17.2|1|17.0,E,tetrahedral carbon;17.1,E,planar carbon;a:18.1,H,counting carbons
17.3|1|17.0,E,tetrahedral carbon
18.b|1|17.b,H,planar and tetrahedral carbons
18.0|1|17.1,E,planar C=C carbon;11.1,H,addition to ethene
18.1|1|17.0,E,tetrahedral carbon;11.6,H,elimination
18.2|1|12.0,E,alcohol oxidation;17.1,H,planar carbon
18.3|1|12.1,E,reduction of ethanal;17.0,H,tetrahedral carbon
18.4|1|12.2,H,esterification;17.1,E,planar carbonyl carbon
19.b|1|
19.0|1|a:7.3,E,tertiary alcohol;12.0,H,oxidation with KMnO4
19.1|1|19.0,E,tertiary alcohols not oxidised
19.2|1|0.3,E,ketone not oxidised
19.3|2|b:0.1,E,saturated compounds;b:0.2,E,bromine water test
19.4|1|b:2.0,H,elimination makes C=C
19.5|1|a:1.6,E,benzene delocalised electrons
19.6|1|12.0,E,oxidation to ethanoic acid
20.b|1|a:13.0,H,ester from acid and alcohol
20.0|1|a:13.0,H,ester formation;b:1.3,H,esterification
20.1|1|20.0,H,ester preparation;b:1.3,H,esterification equation
20.2|1|
20.3|1|b:1.3,H,esterification
20.4|1|a:13.6,H,monocarboxylic acids and primary alcohols
21.b|1|
21.0|2|b:1.3,E,esterification
21.1|1|21.0,E,reversible reaction mixture
21.2|2|20.1,H,esterification equation
21.3|2|21.2,E,oxygen-18 evidence
22.b|1|
22.0|1|20.0,H,reactants of preparation
22.1|1|22.0,H,flask contents
22.2|1|
22.3|1|
22.4|1|22.3,H,condenser fitted for reflux
22.5|2|22.3,E,reflux condenser setup;22.4,E,reflux heating
23.b|1|
23.0|1|22.4,H,mixture after reflux
23.1|1|23.0,E,separating funnel layers
23.2|2|23.1,E,layers in funnel;7.2,H,acid with carbonate
23.3|1|23.2,E,carbonate wash
23.4|1|
23.5|1|23.4,H,dry ester
23.6|1|23.5,H,distilled product
23.7|1|23.1,E,layers;23.0,H,separating funnel
24.b|1|
24.0|1|22.3,E,reflux condenser
24.1|2|21.0,E,equilibrium shifted;22.1,H,sulfuric acid added
24.2|1|22.4,H,water bath heating
24.3|1|22.2,E,anti-bumping granules
24.4|1|22.3,E,open condenser
24.5|1|23.2,E,carbonate wash;7.2,H,carbonate and acid
24.6|1|23.2,E,carbon dioxide released in funnel
24.7|1|23.5,E,distillation
25.b|1|
25.0|1|22.1,H,adding concentrated sulfuric acid
25.1|1|22.0,H,propanoic acid and methanol
25.2|1|21.0,E,equilibrium
25.3|1|23.0,H,aqueous layers
25.4|1|
25.5|1|23.4,E,drying the ester
25.6|1|23.2,E,pressure release in funnel;24.6,H,carbon dioxide produced
25.7|1|22.4,H,heating under reflux;22.3,H,condenser
"""
out={}
for ln in D.strip().split('\n'):
    k,c,r=ln.split('|')
    needs=[]
    if r:
        for ref in r.split(';'):
            p=ref.split(',')
            conf='low' if p[-1]=='L' else 'high'
            if p[-1]=='L': p=p[:-1]
            needs.append({"id":full(p[0]),"strength":'essential' if p[1]=='E' else 'helpful',"why":p[2],"confidence":conf})
    out['chem25-s2.'+k]={"cost":int(c),"needs":needs}
import sys
json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,indent=0)
# check
txt=open(sys.argv[2]).read().split('\n')
tgt=[];ids=set()
sec=None
for l in txt:
    if l.startswith('TARGET'): sec='T'
    elif l.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[([^\]]+)\]',l)
    if m:
        ids.add(m.group(1))
        if sec=='T': tgt.append(m.group(1))
print(len(tgt),list(out)==tgt,len(set(tgt)-set(out)),len(set(out)-set(tgt)))
bad=[n['id'] for v in out.values() for n in v['needs'] if n['id'] not in ids]
print('bad',bad)
selfl=[k for k,v in out.items() if any(n['id']==k for n in v['needs'])]
print('self',selfl)
print('links',sum(len(v['needs']) for v in out.values()),'c2',sum(v['cost']==2 for v in out.values()),'low',sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
