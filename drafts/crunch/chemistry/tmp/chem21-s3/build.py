import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
E='e';H='h'
def L(i,s,w,c='H'): return {"id":i,"strength":'essential' if s=='e' else 'helpful',"why":w,"confidence":'high' if c=='H' else 'low'}
def build(pack,out,data):
    txt=open(D+'packs/'+pack).read()
    ids=[];allids=set();inT=False
    for ln in txt.split('\n'):
        if ln.startswith('TARGET'): inT=True
        elif ln.startswith('CANDIDATES'): inT=False
        m=re.match(r'\[([^\]]+)\]',ln)
        if m:
            allids.add(m.group(1))
            if inT: ids.append(m.group(1))
    assert list(data.keys())==ids,(set(ids)-set(data),set(data)-set(ids))
    res={}
    for k,(c,needs) in data.items():
        for n in needs: assert n['id'] in allids and n['id']!=k,(k,n)
        res[k]={"cost":c,"needs":needs}
    json.dump(res,open(D+'point-links/'+out,'w'),ensure_ascii=False,indent=1)
    nl=sum(len(v['needs']) for v in res.values())
    print(out,len(res),nl,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))

p='chem21-s3.'
def a(s):return p+s
d={}
def A(k,c,*n): d[a(k)]=(c,[L(*x) for x in n])
A('0.b',1,('chem21-s1.2.0',H,'bond enthalpy definition'))
A('0.0',2,(a('0.b'),H,'average bond enthalpy values'))
A('0.1',1,('chem5-s1.2.2',H,'double bonds','L'),(a('0.b'),H,'average bond enthalpy values'))
A('0.2',1,('chem5-s1.2.3',H,'triple bond in nitrogen','L'))
A('1.b',1,('chem21-s1.3.0',E,'bonds broken then made'))
A('1.0',1,('chem10-s2.7.1',H,'balanced equation'),('chem5-s1.2.1',H,'drawing bonds','L'))
A('1.1',1,(a('1.0'),E,'bonds shown in structural formulae'),('chem10-s2.7.3',E,'coefficients multiply bonds'),('chem21-s1.2.0',H,'bond enthalpy'))
A('1.2',1,(a('1.1'),E,'same method as bonds broken'),('chem21-s1.3.2',H,'bond making releases energy'))
A('1.3',2,(a('1.1'),E,'sum of bonds broken'),(a('1.2'),E,'sum of bonds formed'),('chem21-s1.1.1',H,'definition of delta H'))
A('1.4',1,(a('1.3'),E,'sign of delta H'),('chem21-s1.6.0',E,'exothermic and endothermic meanings'))
A('1.5',1,(a('1.3'),E,'sums of bonds broken and formed'))
A('2.b',1)
A('2.0',1,(a('1.0'),E,'drawing every bond'),('chem10-s2.9.1',H,'methane combustion equation'))
A('2.1',1,(a('1.1'),E,'bonds broken sum'),(a('0.0'),E,'bond enthalpy values'))
A('2.2',1,(a('1.2'),E,'bonds formed sum'),(a('0.0'),E,'bond enthalpy values'))
A('2.3',1,(a('1.3'),E,'delta H formula'),(a('2.1'),E,'bonds broken total'),(a('2.2'),E,'bonds formed total'))
A('2.4',2,(a('2.3'),E,'calculated delta H'),('chem21-s1.7.0',H,'standard methane combustion value'))
A('2.5',2,(a('2.4'),E,'steam versus liquid water difference'),('chem21-s1.5.4',H,'condensing releases energy'))
A('3.b',1)
A('3.0',1)
A('3.1',1,(a('1.5'),E,'leave out unchanged bonds'),(a('0.0'),E,'bond enthalpy values'),(a('0.1'),E,'C=C value'))
A('3.2',1,(a('3.1'),E,'new bonds formed'),(a('0.0'),E,'bond enthalpy values'))
A('3.3',1,(a('3.1'),E,'bonds broken sum'),(a('3.2'),E,'bonds formed sum'))
A('4.b',1)
A('4.0',1)
A('4.1',1,(a('0.0'),E,'H-H and Cl-Cl values'),(a('1.1'),H,'bonds broken sum'))
A('4.2',1,(a('0.0'),E,'H-Cl value'),(a('1.2'),H,'bonds formed sum'))
A('4.3',1,(a('4.1'),E,'bonds broken'),(a('4.2'),E,'bonds formed'),(a('1.3'),E,'delta H formula'))
A('4.4',1,(a('4.3'),E,'calculated delta H'),('chem21-s1.2.3',H,'average bond enthalpies'))
A('5.b',1)
A('5.0',1)
A('5.1',1,(a('0.0'),E,'C-H and Cl-Cl values'),(a('1.5'),E,'leave out unchanged bonds'))
A('5.2',1,(a('0.0'),E,'C-Cl and H-Cl values'),(a('1.2'),H,'bonds formed sum'))
A('5.3',1,(a('5.1'),E,'bonds broken'),(a('5.2'),E,'bonds formed'),(a('1.3'),E,'delta H formula'))
A('6.b',1)
A('6.0',1,('chem21-s1.2.3',E,'average bond enthalpies'))
A('6.1',1,('chem21-s1.2.0',E,'bond enthalpy refers to gaseous state'))
A('6.2',1,(a('6.0'),H,'estimates are approximate'))
A('6.3',1,('chem21-s1.3.3',E,'exothermic when bonds formed release more'))
A('7.b',1)
A('7.0',1,(a('0.0'),E,'C-C, C=C, C triple bond values'),(a('0.1'),E,'multiple bond values'),('chem5-s1.2.3',H,'single double triple bonds','L'))
A('7.1',2,(a('7.0'),E,'multiple bond values'),('chem5-s1.12.4',E,'double bond is sigma plus pi'))
A('7.2',2,('chem5-s1.12.0',E,'sigma bond head-on overlap'),('chem5-s1.12.2',E,'pi bond sideways overlap'),('chem5-s1.12.5',H,'pi weaker than sigma'))
A('7.3',1,(a('0.0'),E,'C-halogen values'))
A('7.4',2,(a('7.3'),E,'trend down group'),('chem5-s1.2.0',H,'shared pair held by nuclei','L'))
A('7.5',1,(a('0.2'),E,'N triple bond value'))
build('chem21-s3.t1g1.txt','chem21-s3.t1g1.json',d)
