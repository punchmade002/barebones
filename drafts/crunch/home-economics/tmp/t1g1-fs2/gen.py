import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
def build(name,spec):
    src=open(D+'packs/'+name+'.t1g1.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',src,re.M))
    tid=[]; sec=None
    for ln in src.split('\n'):
        if ln.startswith('TARGET'): sec='t'
        elif ln.startswith('CANDIDATES'): sec='c'
        m=re.match(r'\[([^\]]+)\]',ln)
        if m and sec=='t': tid.append(m.group(1))
    p=name.rsplit('-',1)[0]+'.'  # unused
    pre=name.split('.')[0]+'.'
    out={}
    for k,(c,n) in spec.items(): out[pre+k]={"cost":c,"needs":n}
    assert list(out)==tid,(set(tid)^set(out),name)
    for v in out.values():
        for n in v['needs']: assert n['id'] in ids,n
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
def seq(keys,costs2=(),needs={}):
    return {k:(2 if k in costs2 else 1,needs.get(k,[])) for k in keys}
f='hom-family-society-s2.'
k2="0.b 0.0 0.1 0.2 0.3 0.4 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 2.b 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.b 3.0 3.1 3.2 3.3 3.4 3.5 4.b 4.0 4.1 4.2 4.3 4.4 4.5 5.b 5.0 5.1 5.2 5.3".split()
build('hom-family-society-s2',seq(k2,{'0.3','0.4','1.4','1.6','2.5','3.2','4.2','4.4'},{
 '0.4':[L(f+'1.3','helpful','uses patriarchal authority')],
 '2.1':[L(f+'0.1','helpful','uses nuclear family')],
 '3.2':[L(f+'3.1','helpful','divorce referendum introduces divorce')],
 '3.3':[L(f+'3.2','essential','amends the divorce living-apart condition')],
 '4.1':[L(f+'1.4','helpful','contrasts segregated gender roles')],
 '4.3':[L(f+'3.2','helpful','uses legal divorce')]}))
g='hom-food-safety-s3.'
k3="0.b 0.0 0.1 0.2 0.3 0.4 0.5 0.6 1.b 1.0 1.1 1.2 1.3 2.b 2.0 2.1 2.2 2.3 2.4 3.b 3.0 3.1 3.2 3.3 3.4 3.5 4.b 4.0 4.1 4.2 4.3 5.b 5.0 5.1 5.2 5.3 5.4 5.5".split()
build('hom-food-safety-s3',seq(k3,{'3.2','3.3','4.0','4.3','5.1','5.4'},{
 '1.2':[L('hom-food-safety-s2.7.3','helpful','toxic poisoning from bacterial toxins','low')],
 '2.2':[L('hom-food-safety-s1.8.3','helpful','yeast fermentation of sugar')],
 '2.3':[L('hom-food-safety-s1.3.3','helpful','moulds are aerobic')],
 '2.4':[L('hom-food-safety-s1.3.4','helpful','moulds prefer acidic pH')],
 '3.5':[L('hom-food-safety-s1.9.6','helpful','binary fission')],
 '5.0':[L(g+'3.2','helpful','uses temperature and danger zone')],
 '5.1':[L(g+'3.1','helpful','moisture need of micro-organisms')],
 '5.2':[L(g+'3.4','helpful','uses pH tolerance')],
 '5.3':[L(g+'3.3','helpful','aerobic oxygen requirement')],
 '5.5':[L(g+'5.1','helpful','uses sugar to remove moisture'),L(g+'5.2','helpful','uses acid to lower pH'),L(g+'4.0','helpful','uses heat treatment','low')]}))
h='hom-family-society-s3.'
k4="0.b 0.0 0.1 0.2 0.3 0.4 0.5 0.6 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 2.b 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.b 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 4.b 4.0 4.1 4.2 4.3 5.b 5.0 5.1 5.2 5.3 5.4 5.5 5.6".split()
build('hom-family-society-s3',seq(k4,{'1.4','3.1'},{
 '1.6':[L(h+'3.b','helpful','blended family formed by new partner')],
 '2.b':[L(h+'0.b','helpful','extended adds to nuclear family')],
 '5.0':[L(h+'0.b','helpful','nuclear structure'),L(h+'1.b','helpful','lone-parent structure'),L(h+'2.b','helpful','extended structure'),L(h+'3.b','helpful','blended structure')],
 '5.5':[L(h+'0.b','helpful','nuclear family most common')]}))
