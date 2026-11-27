import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(spec):
    out=[]
    for s in spec.split(';'):
        s=s.strip()
        if not s: continue
        i,st,w=s.split('|'); c='high'
        if w.endswith('?'): w=w[:-1]; c='low'
        out.append({"id":i,"strength":{'e':'essential','h':'helpful'}[st],"why":w,"confidence":c})
    return out
def build(name,pre,costs,links):
    ids=[l[len(pre):] for l in [] ]
    res={}
    for k,c in costs.items():
        res[pre+k]={"cost":c,"needs":L(links.get(k,'').replace('@',pre))}
    pk=open(D+'packs/'+name+'.txt').read()
    targ=re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    assert targ==list(res),(set(targ)^set(res))
    for k,v in res.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(res,open(D+'point-links/'+name+'.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in res.values())
    print(name,len(res),nl,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
# food safety
p='hom-food-safety-s1.'
c={}
for k in "0.b 0.0 0.1 0.2 1.b 1.0 1.1 1.2 1.3 1.4 1.5 2.b 2.0 2.1 2.2 2.3 2.4 3.b 3.0 3.1 3.2 3.3 3.4 3.5 3.6 4.b 4.0 4.1 4.2 4.3 5.b 5.0 5.1 5.2 5.3 6.b 6.0 6.1 6.2 6.3 6.4 6.5 7.b 7.0 7.1 7.2 7.3 7.4 7.5 7.6 8.b 8.0 8.1 8.2 8.3 8.4 8.5 9.b 9.0 9.1 9.2 9.3 9.4 9.5 9.6 9.7".split(): c[k]=1
for k in "1.5 6.0 7.6 9.7".split(): c[k]=2
l={'1.1':'@1.0|h|uses hyphae','1.2':'@1.0|e|upright hypha','1.3':'@1.2|e|sits at tip of sporangiophore','1.4':'@1.3|h|contrasts with sporangium',
'1.5':'@1.0|e|hypha label;@1.1|e|mycelium label;@1.2|e|sporangiophore label;@1.3|e|sporangium label',
'3.5':'@1.1|h|mycelium spreading',
'4.0':'@1.4|h|conidia chains','4.2':'@6.4|h|zygospore','5.1':'@6.4|h|zygospore','5.3':'@1.4|h|conidia',
'6.0':'@1.2|e|sporangiophore;@1.4|h|conidia chains','6.1':'@1.3|h|sporangium','6.2':'@1.1|h|mycelium','6.3':'@1.0|h|hyphae','6.4':'@6.3|e|fused hyphae','6.5':'@6.4|e|zygospore',
'7.6':'@7.1|e|cell wall label;@7.2|e|cell membrane label;@7.3|e|nucleus label;@7.4|e|vacuole label;@7.5|e|granular cytoplasm label',
'8.5':'@8.3|h|fermentation',
'9.b':'@7.3|h|fungi have nucleus',
'9.7':'@9.0|e|cell wall label;@9.1|e|cell membrane label;@9.2|e|cytoplasm label;@9.3|e|ribosomes label;@9.4|e|flagella label;@9.5|e|nucleoid label'}
build('hom-food-safety-s1.t1g1',p,c,l)
# sociological
p='hom-sociological-concepts-s1.'
c={k:1 for k in "0.b 0.0 0.1 0.2 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 2.b 2.0 2.1 2.2 2.3 2.4 3.b 3.0 3.1 3.2 3.3 3.4 3.5 4.b 4.0 4.1 4.2 4.3 4.4 4.5 4.6 5.b 5.0 5.1 5.2 5.3 6.b 6.0 6.1 6.2 6.3 6.4".split()}
for k in "1.0 5.3 6.1".split(): c[k]=2
l={'0.2':'@0.0|h|uses definition of society','1.0':'@0.0|h|culture of a society','1.1':'@1.0|h|culture defined','1.2':'@1.0|h|culture divided','1.3':'@1.0|h|culture varies','1.4':'@1.0|h|uses culture examples','1.5':'@1.0|h|examples of culture','1.6':'@1.0|h|shares main culture','1.7':'@1.0|e|judging cultures',
'2.1':'@2.0|e|norms varying','2.2':'@2.0|e|more is a norm','2.3':'@2.0|e|customs are norms;@2.2|h|contrasted with mores','2.4':'@2.0|e|laws are norms;@2.2|h|mores becoming laws',
'3.0':'@2.0|e|enforces norms','3.1':'@3.0|e|type of sanction','3.2':'@3.0|e|type of sanction','3.3':'@3.0|e|sanction sources','3.4':'@2.0|e|following or breaking norms','3.5':'@3.4|e|deviance defined;@2.1|h|norms vary',
'4.b':'@2.0|h|contrasts with norm','4.1':'@4.0|e|value vs norm;@2.0|e|norms carry values','4.2':'@4.0|e|examples of values','4.3':'@4.0|e|types of values','4.4':'@4.0|e|how values are learned;@1.1|h|socialisation','4.5':'@4.0|e|values change','4.6':'@4.0|e|conflicting values',
'5.0':'@1.0|e|culture as umbrella;@4.0|h|values as part;@2.0|h|norms as part','5.1':'@4.0|e|values broad beliefs;@2.0|e|norms as rules','5.2':'@3.0|e|sanctions enforce;@2.4|e|laws formal norms','5.3':'@4.1|e|value leads to norm;@3.0|e|sanction','6.1':'@1.0|e|culture definition;@2.0|e|norm definition;@4.0|e|value definition','6.2':'@2.3|h|folkways vs mores;@4.1|h|norms vs values','6.4':'@4.1|h|values underpin norms;@3.0|h|norms enforced by sanctions'}
build('hom-sociological-concepts-s1.t1g1',p,c,l)
# proteins
p='hom-proteins-s6.'
c={k:1 for k in "0.b 0.0 0.1 0.2 1.b 1.0 1.1 1.2 1.3 1.4 2.b 2.0 2.1 2.2 2.3 2.4 2.5 2.6 3.b 3.0 3.1 3.2 4.b 4.0 4.1 4.2".split()}
for k in "1.2 4.1".split(): c[k]=2
S='hom-proteins-s1.'
l={'0.b':S+'0.2|h|amino acids as units','0.2':S+'2.0|e|essential amino acids','1.b':S+'0.2|h|amino acids','1.0':S+'0.2|e|amino acids as units','3.b':S+'0.2|h|amino acids','3.0':S+'2.0|e|essential amino acids','3.1':S+'0.2|e|amino acids make proteins','4.2':S+'2.0|h|essential amino acids'}
l={k:v.replace('@','') for k,v in l.items()}
build('hom-proteins-s6.t1g1',p,c,l)
