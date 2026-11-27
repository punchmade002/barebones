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

F3='hom-textiles-fibres-s3.'; F4='hom-textiles-fibres-s4.'; C1='hom-clothing-selection-s1.'
run('hom-textiles-fibres-s5.t1g1','hom-textiles-fibres-s5.',{
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[L('0.0','e','warp and weft yarns')]),
'0.2':(1,[L('0.0','e','warp and weft yarns')]),
'0.3':(1,[]),
'0.4':(1,[L('0.1','h','plain weave'),L('0.2','h','twill weave'),L('0.3','h','satin weave')]),
'0.5':(1,[L('0.0','h','weft turns back at edge')]),
'0.6':(2,[L('0.4','e','the three basic weaves')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L('1.0','h','loops formed across each row')]),
'1.2':(1,[]),
'1.3':(1,[L('1.1','h','reverse of plain knit')]),
'1.4':(1,[]),'1.5':(1,[]),'1.6':(2,[]),'1.7':(1,[]),
'2.b':(1,[]),
'2.0':(1,[L(C1+'1.1','h','wool scales interlock when felting')]),
'2.1':(1,[]),
'2.2':(1,[L('2.1','h','non-woven fibre web')]),
'2.3':(1,[L('2.0','h','felt made by felting'),L('2.1','h','bonded non-woven fabrics')]),
'2.4':(1,[]),
'3.b':(2,[]),
'3.0':(2,[L(C1+'3.4','h','resin finishes improve crease recovery')]),
'3.1':(1,[L(C1+'2.2','h','water-repellent finish coating')]),
'3.2':(1,[]),
'3.3':(1,[L(F3+'0.4','h','synthetic fibres defined','low')]),
'3.4':(1,[]),
'3.5':(1,[L(F4+'8.5','h','mercerising treatment of cotton')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L(C1+'1.5','h','shrink-resistant finish')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L(F3+'0.2','h','wool and silk are protein fibres')]),
'5.2':(1,[L(F3+'3.1','h','polyester fibre')]),
'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[]),'6.0':(2,[]),'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[L(F3+'3.1','h','polyester fibre')]),
'6.4':(1,[]),
'6.5':(2,[L('6.0','e','screen printing method')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),
'7.3':(1,[L('7.2','h','combined with quilting')]),
'7.4':(1,[]),'7.5':(1,[]),'7.6':(1,[]),
'7.7':(1,[L('6.b','h','printing methods')]),
'8.b':(1,[]),
'8.0':(2,[L(C1+'6.3','h','fair test conditions')]),
'8.1':(2,[L('8.0','h','fair test conditions')]),
'8.2':(1,[L('8.1','h','crease-recovery test')]),
'8.3':(1,[L('8.0','h','fair test conditions')]),
'8.4':(2,[L('8.0','h','fair test conditions')]),
'8.5':(1,[L(C1+'1.3','h','percentage shrinkage formula'),L('8.0','h','fair test conditions')]),
'8.6':(1,[]),'8.7':(1,[]),
})
