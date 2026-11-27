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

S6='hom-food-safety-s6.'; S2='hom-appliances-equipment-s2.'
run('hom-appliances-equipment-s5.t1g1','hom-appliances-equipment-s5.',{
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[L(S6+'0.0','h','defines the danger zone')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),
'2.b':(1,[]),
'2.0':(2,[L('2.4','h','uses refrigerant')]),
'2.1':(2,[L('2.4','h','uses refrigerant')]),
'2.2':(1,[L('2.4','h','acts on liquid refrigerant')]),
'2.3':(2,[L('2.4','h','uses refrigerant')]),
'2.4':(1,[]),
'2.5':(1,[L('2.0','h','switches the compressor motor')]),
'2.6':(2,[]),
'2.7':(2,[L('3.b','h','order of refrigerant flow')]),
'3.b':(1,[]),
'3.0':(2,[L('2.0','h','compressor function')]),
'3.1':(1,[L('2.1','h','condenser function')]),
'3.2':(1,[L('2.2','h','expansion valve function'),L('4.1','h','pressure fall lowers boiling point')]),
'3.3':(1,[L('2.3','h','evaporator function')]),
'3.4':(1,[L('2.5','h','thermostat switches motor off')]),
'3.5':(1,[]),
'4.b':(1,[]),
'4.0':(1,[L('2.0','h','compressor does work')]),
'4.1':(1,[L('2.2','h','expansion valve lowers pressure')]),
'4.2':(1,[L('2.1','h','condenser releases heat')]),
'4.3':(2,[L('2.3','h','evaporator absorbs the heat')]),
'4.4':(1,[L('4.3','e','uses latent heat')]),
'4.5':(1,[L('2.3','h','evaporator walls')]),
'5.b':(1,[]),
'5.0':(2,[L('2.1','h','air circulates around condenser')]),
'5.1':(1,[L('0.2','h','danger zone 5 to 63')]),
'5.2':(1,[]),'5.3':(1,[]),
'5.4':(2,[L(S6+'0.1','h','cross-contamination from drips')]),
'5.5':(1,[]),'5.6':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L(S6+'1.5','h','use-by and best-before dates')]),
'6.2':(1,[L(S6+'2.1','h','thawing safely')]),
'6.3':(2,[]),
'6.4':(1,[L('2.1','h','condenser grille')]),
'6.5':(2,[]),'6.6':(1,[]),
'7.b':(1,[]),
'7.0':(1,[L(S2+'4.0','h','A to G energy label')]),
'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'7.4':(1,[L('9.2','h','inverter compressor feature')]),
'7.5':(1,[L(S2+'5.0','h','star rating applies to freezer')]),
'8.b':(1,[]),
'8.0':(2,[L('2.3','h','frost forms on evaporator')]),
'8.1':(1,[]),'8.2':(1,[]),'8.3':(1,[]),'8.4':(1,[]),'8.5':(1,[]),'8.6':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),
'9.2':(1,[L('2.0','h','compressor speed')]),
'9.3':(1,[]),'9.4':(1,[]),
})
