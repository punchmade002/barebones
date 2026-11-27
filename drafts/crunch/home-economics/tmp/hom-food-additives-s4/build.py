import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics'
def L(i,s,w,c='high'): return {"id":i,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":c}
def run(name,pre,items):
    out={}
    for k,(cost,links) in items.items():
        assert k not in out; out[pre+k]={"cost":cost,"needs":[ {**l,"id":l["id"] if l["id"].startswith("hom-") else pre+l["id"]} for l in links]}
    txt=open(f'{D}/packs/{name}.txt').read()
    tgt=[];sec=None
    for line in txt.split('\n'):
        if line.startswith('TARGET'): sec='T'
        elif line.startswith('CANDIDATES'): sec='C'
        m=re.match(r'\[([^\]]+)\]',line)
        if m and sec=='T': tgt.append(m.group(1))
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(out)==tgt,(set(tgt)^set(out))
    for k,v in out.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
        assert all(len(n['why'].split())<=8 for n in v['needs'])
    json.dump(out,open(f'{D}/point-links/{name}.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values()); c2=sum(v['cost']==2 for v in out.values())
    lo=sum(n['confidence']=='low' for v in out.values() for n in v['needs'])
    print(name,len(out),nl,c2,lo)

P='hom-food-preservation-s5.'; LI='hom-lipids-s4.'
run('hom-food-additives-s4.t1g1','hom-food-additives-s4.',{
'0.b':(2,[]),'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(2,[L('0.0','e','classes of additive')]),
'0.4':(2,[]),
'0.5':(1,[L('4.6','h','polyols are bulk sweeteners'),L('3.3','h','sulphur dioxide destroys thiamine')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(2,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[L('1.2','h','tartrazine example')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(2,[]),'2.2':(2,[]),'2.3':(1,[]),
'2.4':(1,[L('2.3','e','monosodium glutamate introduced')]),
'2.5':(1,[L('2.3','h','flavour enhancers have E numbers')]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L(P+'0.3','h','traditional natural preservatives')]),
'3.2':(2,[L(P+'6.3','h','sulphur dioxide as preservative'),L(P+'6.1','h','potassium sorbate as preservative')]),
'3.3':(1,[L('3.2','e','sulphur dioxide preservative')]),
'3.4':(1,[L(P+'6.5','h','allergens emphasised on labels')]),
'4.b':(2,[]),'4.0':(1,[]),'4.1':(1,[]),
'4.2':(2,[L('4.1','h','intense sweeteners defined')]),
'4.3':(2,[L('4.1','h','intense sweeteners used in small amounts')]),
'4.4':(1,[L('4.1','h','intense sweeteners')]),
'4.5':(1,[L('4.2','h','aspartame example')]),
'4.6':(2,[]),
'4.7':(1,[L('4.6','e','polyols are bulk sweeteners')]),
'5.b':(1,[]),
'5.0':(1,[L('4.1','h','intense sweeteners reduce sugar')]),
'5.1':(1,[]),
'6.b':(1,[]),
'6.0':(1,[L(LI+'7.0','h','oxidative rancidity of fats')]),
'6.1':(1,[]),'6.2':(1,[]),'6.3':(2,[]),
'6.4':(1,[L('6.0','h','antioxidants prevent rancidity')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L('7.0','h','nutritional supplements defined')]),
'7.2':(1,[L('0.0','h','other additive classes',"low")]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(2,[L('8.0','h','emulsifier holds liquids together')]),
'8.2':(1,[L('8.0','h','emulsifier examples')]),
'8.3':(1,[L('8.0','h','emulsifier uses')]),
'8.4':(2,[L('8.0','h','emulsion held by emulsifier'),L(LI+'2.0','h','what an emulsion is')]),
'8.5':(2,[L('8.1','e','emulsifier molecule structure')]),
'9.b':(1,[]),
'9.0':(1,[L('4.6','h','sorbitol and mannitol are polyols')]),
'9.1':(1,[L('9.0','e','humectant function')]),
'9.2':(2,[]),'9.3':(1,[]),'9.4':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[]),'10.2':(1,[]),'10.3':(1,[]),'10.4':(1,[]),
})
