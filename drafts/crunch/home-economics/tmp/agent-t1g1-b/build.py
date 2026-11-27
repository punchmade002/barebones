import json,re,sys
H='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def run(name, items):
    txt=open(H+'packs/'+name+'.txt').read()
    tgt=[]; allids=set(); intgt=True
    for line in txt.split('\n'):
        if line.startswith('CANDIDATES'): intgt=False
        m=re.match(r'\[([^\]]+)\]',line)
        if m:
            allids.add(m.group(1))
            if intgt: tgt.append(m.group(1))
    assert list(items.keys())==tgt,(set(tgt)-set(items),set(items)-set(tgt))
    out={};nl=0;c2=0;lo=0
    for k,(c,n) in items.items():
        for x in n: assert x['id'] in allids and x['id']!=k,(k,x)
        out[k]={"cost":c,"needs":n};nl+=len(n);c2+=c==2;lo+=sum(x['confidence']=='low' for x in n)
    json.dump(out,open(H+'point-links/'+name+'.json','w'),indent=1)
    json.loads(open(H+'point-links/'+name+'.json').read())
    print(name,len(out),nl,c2,lo)
def mk(spec):
    d={}
    for line in spec.strip().split('\n'):
        k,c,*rest=line.split('|')
        n=[]
        for r in rest:
            if r.strip():
                i,s,w,cf=r.split(';'); n.append(L(i,s,w,cf))
        d[k]=(int(c),n)
    return d
P='hom-energy-nutrition-s6.'
S=P
a=mk(f"""
{P}0.b|1
{P}0.0|1
{P}0.1|1
{P}0.2|2
{P}0.3|1
{P}0.4|1
{P}0.5|1
{P}0.6|1|hom-vitamins-minerals-s4.1.b;helpful;uses calcium as a mineral;low
{P}0.7|1
{P}1.b|1|{P}0.2;helpful;water as solvent;high
{P}1.0|1
{P}1.1|2
{P}1.2|1
{P}1.3|2
{P}1.4|2|{P}0.2;helpful;water dissolving substances;high
{P}1.5|1|{P}0.2;essential;water as a solvent;high
{P}1.6|1
{P}2.b|1
{P}2.0|1
{P}2.1|1|{P}0.3;helpful;water retains heat well;high
{P}2.2|1|{P}2.0;helpful;sweating cools the body;high
{P}3.b|1
{P}3.0|1
{P}3.1|1
{P}3.2|1|{P}3.0;helpful;kidneys remove waste in urine;high
{P}4.b|1
{P}4.0|2
{P}4.1|1
{P}4.2|1
{P}5.b|1
{P}5.0|1|hom-vitamins-minerals-s4.0.0;helpful;minerals the body needs;high
{P}5.1|1|{P}0.6;helpful;hard water has dissolved calcium;high|hom-vitamins-minerals-s4.1.b;helpful;calcium as a mineral;low
{P}5.2|1|hom-vitamins-minerals-s4.3.1;helpful;fluoride is a trace mineral;low
{P}5.3|1|{P}5.2;helpful;fluoride in water supplies;low
{P}6.b|1
{P}6.0|1
{P}6.1|2|{P}6.0;helpful;thirst signals water loss;low
{P}6.2|2|{P}6.1;helpful;dehydration;high
{P}6.3|2|{P}6.2;helpful;dehydration;high
{P}6.4|1
{P}6.5|2
{P}7.b|1
{P}7.0|1|{P}0.7;helpful;water has no energy value;high
{P}7.1|1
{P}8.b|1
{P}8.0|2|{P}1.4;helpful;water carries nutrients and waste;high
{P}8.1|1
{P}8.2|1|{P}4.2;helpful;water prevents constipation;high
{P}8.3|1
{P}9.b|1|{P}2.0;helpful;sweating cools the body;high
{P}9.0|1|{P}2.0;helpful;sweating cools the body;high|hom-vitamins-minerals-s4.6.b;helpful;sodium and potassium;low
{P}9.1|1
{P}9.2|2|{P}6.1;helpful;dehydration;high
{P}9.3|1
{P}9.4|2|hom-vitamins-minerals-s4.6.b;helpful;sodium and potassium roles;low|{P}9.0;helpful;salts lost in sweat;high
{P}9.5|1
""")
run('hom-energy-nutrition-s6.t1g1',a)
P='hom-cereals-grains-s2.'
b=mk(f"""
{P}0.b|1
{P}0.0|2
{P}0.1|2
{P}0.2|2
{P}0.3|2
{P}0.4|2
{P}0.5|1
{P}0.6|1
{P}1.b|1
{P}1.0|1
{P}1.1|1
{P}1.2|1
{P}1.3|1
{P}1.4|1
{P}1.5|1|{P}2.b;helpful;fortification;high
{P}1.6|1
{P}1.7|1|hom-cereals-grains-s1.4.0;helpful;wholegrain means all three grain parts;low
{P}2.b|1
{P}2.0|1|hom-cereals-grains-s1.1.5;essential;refining removes bran and germ nutrients;high
{P}2.1|1
{P}2.2|2
{P}2.3|1|{P}2.0;helpful;nutrients added to cereals;low
{P}2.4|1
{P}2.5|2
{P}2.6|1|{P}1.6;helpful;sugar and salt levels vary;low
{P}3.b|1|hom-cereals-grains-s1.5.0;helpful;coeliac disease and gluten;high|hom-proteins-s4.4.0;helpful;gluten is the wheat protein;high
{P}3.0|1|hom-proteins-s4.4.0;helpful;gluten in wheat;low
{P}3.1|2
{P}3.2|1
{P}3.3|2
{P}3.4|1
{P}4.b|1
{P}4.0|1
{P}4.1|1
{P}4.2|1
{P}4.3|2|hom-cereals-grains-s1.0.2;essential;germ holds unsaturated fat;high
{P}4.4|1
{P}4.5|1
{P}5.b|1
{P}5.0|1|{P}1.7;helpful;ingredients in descending weight;high|hom-cereals-grains-s1.4.0;helpful;wholegrain definition;low
{P}5.1|1|hom-cereals-grains-s1.2.3;helpful;fibre from cereals;low
{P}5.2|1|{P}4.2;helpful;best-before date;low
""")
run('hom-cereals-grains-s2.t1g1',b)
P='hom-food-safety-s2.'
c=mk(f"""
{P}0.b|1
{P}0.0|2
{P}0.1|1
{P}0.2|1|hom-food-safety-s1.9.6;helpful;bacteria reproduce by binary fission;high
{P}0.3|1
{P}1.b|1|{P}0.3;helpful;danger zone;high
{P}1.0|1
{P}1.1|1
{P}1.2|1|{P}1.1;helpful;mesophile growth temperature;high
{P}1.3|1
{P}1.4|1|{P}1.1;essential;mesophiles;high
{P}2.b|1
{P}2.0|1|hom-food-safety-s1.3.3;helpful;moulds need oxygen;low
{P}2.1|1
{P}2.2|2|hom-food-safety-s1.8.2;helpful;yeast facultative respiration;low
{P}3.b|1|{P}7.0;helpful;infectious food poisoning;high
{P}3.0|2|hom-food-safety-s1.9.b;helpful;bacterial cell structure;low
{P}3.1|1
{P}3.2|1
{P}3.3|2|{P}1.1;helpful;mesophile;high|{P}2.2;helpful;facultative;high
{P}3.4|1|{P}7.b;helpful;incubation period defined;high
{P}3.5|1
{P}4.b|1|{P}7.3;helpful;toxic food poisoning;high
{P}4.0|2|hom-food-safety-s1.9.b;helpful;bacterial structure;low
{P}4.1|1
{P}4.2|2
{P}4.3|2|{P}1.1;helpful;mesophile;high|{P}2.2;helpful;facultative;high
{P}4.4|2|{P}7.3;helpful;exotoxin in toxic poisoning;high
{P}4.5|1|{P}7.b;helpful;incubation period defined;high
{P}4.6|1
{P}5.b|1|{P}7.3;helpful;toxic food poisoning;high
{P}5.0|2|{P}2.1;essential;anaerobic;high
{P}5.1|1
{P}5.2|2
{P}5.3|1|{P}2.1;essential;anaerobic growth;high
{P}5.4|2|{P}7.4;helpful;exotoxins hard to destroy;high
{P}5.5|1|{P}7.b;helpful;incubation period defined;high
{P}5.6|2
{P}6.b|1
{P}6.0|2|{P}7.0;helpful;infectious food poisoning;high
{P}6.1|1|{P}7.0;helpful;infectious food poisoning;high
{P}6.2|1|{P}7.0;helpful;infectious food poisoning;high
{P}6.3|1
{P}6.4|1|{P}7.3;helpful;toxic food poisoning;high
{P}7.b|1
{P}7.0|1
{P}7.1|1|{P}7.0;essential;infectious food poisoning;high
{P}7.2|2|{P}7.0;helpful;infectious type;high
{P}7.3|1
{P}7.4|2|{P}7.3;essential;toxic food poisoning;high
{P}7.5|2|{P}7.2;helpful;infectious summary;high|{P}7.4;helpful;toxic summary;high
{P}8.b|1|{P}0.0;helpful;growth conditions;high
{P}8.0|1|{P}0.3;helpful;heat above 63 destroys bacteria;high
{P}8.1|1|{P}0.3;essential;danger zone;high
{P}8.2|1
{P}8.3|1
{P}8.4|1
{P}8.5|1|{P}0.2;helpful;bacteria multiply quickly with time;high
""")
run('hom-food-safety-s2.t1g1',c)
