import json,re
B='drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
def run(name,items):
    # items: id -> (cost, [links])
    txt=open(f'packs/{name}.txt').read()
    tgt=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(items)==tgt,(set(tgt)^set(items))
    out={k:{"cost":c,"needs":n} for k,(c,n) in items.items()}
    for v in out.values():
        for n in v["needs"]: assert n["id"] in allids
    json.dump(out,open(f'drafts/crunch/home-economics/point-links/{name}.json'.replace('drafts/crunch/home-economics/','') ,'w'),indent=1)
    nl=sum(len(v["needs"]) for v in out.values()); c2=sum(v["cost"]==2 for v in out.values()); lo=sum(n["confidence"]=="low" for v in out.values() for n in v["needs"])
    print(name,len(out),nl,c2,lo)
p='hom-personal-finance-s5.'
run('hom-personal-finance-s5.t1g1',{
p+'0.b':(1,[]),p+'0.0':(1,[]),p+'0.1':(1,[]),
p+'0.2':(1,[L(p+'1.1','helpful' and H,'policy as the contract')]),
p+'0.3':(1,[]),p+'0.4':(2,[]),
p+'1.b':(1,[]),p+'1.0':(1,[]),p+'1.1':(1,[]),p+'1.2':(1,[]),p+'1.3':(1,[]),p+'1.4':(2,[]),
p+'1.5':(2,[L(p+'1.4',H,'uses excess'),L(p+'1.0',H,'premium being set')]),
p+'2.b':(1,[]),
p+'2.0':(2,[L('hom-personal-finance-s1.4.3',H,'PRSI as compulsory contribution')]),
p+'2.1':(1,[L(p+'2.0',H,'PRSI as State scheme')]),
p+'2.2':(2,[L('hom-personal-finance-s1.6.0',H,'social insurance payments earned by PRSI')]),
p+'2.3':(1,[L(p+'2.0',H,'PRSI contributions protect income')]),
p+'2.4':(1,[L('hom-personal-finance-s1.4.4',H,'PRSI classes and exemption')]),
p+'3.b':(1,[]),p+'3.0':(1,[]),p+'3.1':(1,[]),p+'3.2':(2,[]),p+'3.3':(1,[]),
p+'3.4':(2,[L(p+'1.4',H,'excess when comparing plans')]),
p+'3.5':(1,[]),p+'3.6':(1,[]),
p+'4.b':(1,[]),p+'4.0':(1,[]),p+'4.1':(1,[]),
p+'4.2':(1,[L(p+'4.0',E,'buildings cover combined'),L(p+'4.1',E,'contents cover combined')]),
p+'4.3':(2,[]),p+'4.4':(2,[]),
p+'4.5':(2,[L(p+'4.1',H,'inventory of contents','low')]),
p+'5.b':(1,[]),p+'5.0':(1,[]),
p+'5.1':(1,[L(p+'5.0',H,'life assurance payout on death')]),
p+'5.2':(1,[L(p+'5.0',H,'life assurance payout on death')]),
p+'5.3':(1,[]),
p+'5.4':(2,[L(p+'5.1',E,'is term assurance')]),
p+'5.5':(2,[L(p+'5.1',E,'term assurance converted'),L(p+'5.2',H,'whole-of-life policy')]),
p+'5.6':(1,[L(p+'5.4',H,'mortgage protection policy','low')]),
})
q='hom-lipids-s3.'
run('hom-lipids-s3.t1g1',{
q+'0.b':(1,[]),q+'0.0':(1,[]),q+'0.1':(1,[]),q+'0.2':(1,[]),q+'0.3':(1,[]),q+'0.4':(1,[]),q+'0.5':(1,[]),q+'0.6':(1,[]),q+'0.7':(1,[]),
q+'1.b':(1,[]),q+'1.0':(1,[]),q+'1.1':(1,[]),q+'1.2':(1,[]),q+'1.3':(1,[]),q+'1.4':(1,[]),q+'1.5':(1,[]),q+'1.6':(1,[]),q+'1.7':(1,[]),
q+'2.b':(1,[]),
q+'2.0':(2,[L('hom-lipids-s1.1.3',H,'omega-3 as polyunsaturated')]),
q+'2.1':(1,[L(q+'0.2',H,'fat-soluble vitamins A and D')]),
q+'2.2':(1,[]),q+'2.3':(1,[]),
q+'3.b':(1,[L('hom-lipids-s1.0.b',H,'saturated, mono, polyunsaturated classes')]),
q+'3.0':(2,[L('hom-lipids-s1.0.1',E,'saturated fatty acids'),L('hom-lipids-s1.5.1',H,'LDL cholesterol harm')]),
q+'3.1':(1,[L('hom-lipids-s1.0.1',H,'saturated fatty acids')]),
q+'3.2':(2,[L('hom-lipids-s1.0.2',E,'monounsaturated fatty acids')]),
q+'3.3':(2,[L('hom-lipids-s1.0.3',E,'polyunsaturated fatty acids'),L('hom-lipids-s1.5.2',H,'HDL cholesterol protects')]),
q+'3.4':(1,[]),
q+'3.5':(2,[L('hom-lipids-s2.4.4',H,'classification by predominant type')]),
q+'3.6':(1,[L('hom-lipids-s1.5.4',H,'unsaturated fats benefit heart')]),
q+'3.7':(2,[L('hom-lipids-s1.2.4',H,'trans fats from hydrogenation')]),
q+'4.b':(1,[]),q+'4.0':(1,[]),
q+'4.1':(1,[L('hom-lipids-s2.4.0',H,'predominant fatty acid type')]),
q+'4.2':(1,[L('hom-lipids-s1.4.0',H,'omega-3 health benefits')]),
q+'4.3':(1,[]),
})
f='hom-family-law-s1.'
run('hom-family-law-s1.t1g1',{
f+'0.b':(1,[]),f+'0.0':(1,[]),f+'0.1':(1,[]),f+'0.2':(1,[]),f+'0.3':(1,[]),f+'0.4':(1,[]),f+'0.5':(1,[]),
f+'1.b':(1,[]),f+'1.0':(2,[]),f+'1.1':(1,[]),f+'1.2':(1,[]),f+'1.3':(1,[]),
f+'2.b':(1,[]),f+'2.0':(1,[]),f+'2.1':(1,[]),
f+'2.2':(1,[L(f+'2.1',H,'application to court')]),
f+'2.3':(1,[L(f+'2.0',H,'informal maintenance agreement')]),
f+'2.4':(1,[]),
f+'3.b':(1,[]),f+'3.0':(1,[]),f+'3.1':(1,[]),f+'3.2':(1,[]),f+'3.3':(1,[]),
f+'3.4':(1,[L(f+'2.2',H,'maintenance order enforced')]),
f+'4.b':(1,[]),
f+'4.0':(1,[L('hom-marriage-s4.2.b',H,'legal separation')]),
f+'4.1':(1,[L('hom-marriage-s4.4.b',H,'divorce Act 1996')]),
f+'4.2':(1,[L(f+'4.0',H,'separation'),L(f+'4.1',H,'divorce')]),
f+'4.3':(1,[]),f+'4.4':(1,[]),
})
