import json,re,sys
base='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def build(name,spec):
    txt=open(base+'packs/'+name+'.t1g1.txt').read()
    tg=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(spec)==tids,(set(tids)^set(spec))
    out={}
    for k,(c,n) in spec.items():
        for x in n: assert x['id'] in allids and x['id']!=k,x
        out[k]={"cost":c,"needs":n}
    json.dump(out,open(base+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
a='hom-food-safety-s4.'
build('hom-food-safety-s4',{
a+'0.b':(1,[]),a+'0.0':(1,[]),
a+'0.1':(2,[L(a+'0.0','helpful','uses fermentation')]),
a+'0.2':(1,[L(a+'0.0','helpful','uses fermentation')]),
a+'0.3':(1,[L(a+'0.0','helpful','uses fermentation')]),
a+'1.b':(1,[L(a+'0.2','helpful','lactic acid fermentation of lactose')]),
a+'1.0':(1,[L(a+'0.2','helpful','lactic acid fermentation of lactose')]),
a+'1.1':(2,[L(a+'1.0','helpful','uses lactic acid from starter cultures')]),
a+'1.2':(2,[L(a+'0.2','helpful','lactose to lactic acid fermentation')]),
a+'1.3':(1,[]),
a+'2.b':(1,[L('hom-food-safety-s1.0.0','helpful','moulds are filamentous fungi')]),
a+'2.0':(2,[L('hom-food-safety-s1.4.0','helpful','Penicillium mould features','low')]),
a+'2.1':(1,[]),
a+'2.2':(1,[L(a+'0.0','helpful','uses fermentation')]),
a+'3.b':(1,[L(a+'0.3','helpful','alcoholic fermentation by yeast')]),
a+'3.0':(1,[L(a+'0.3','helpful','yeast makes carbon dioxide')]),
a+'3.1':(1,[L(a+'3.0','helpful','alcohol made in dough')]),
a+'3.2':(1,[L(a+'0.3','helpful','yeast ferments sugars to alcohol')]),
a+'3.3':(1,[L(a+'0.3','helpful','yeast ferments sugars to alcohol')]),
a+'3.4':(1,[L(a+'0.1','helpful','acetic acid as fermentation product','low')]),
a+'4.b':(1,[]),
a+'4.0':(1,[L(a+'0.2','helpful','bacteria ferment sugars to lactic acid')]),
a+'4.1':(2,[]),
a+'4.2':(1,[]),a+'4.3':(1,[]),a+'4.4':(1,[]),
a+'5.b':(1,[]),
a+'5.0':(2,[L(a+'0.1','helpful','fermentation changes flavour and texture','low')]),
a+'5.1':(1,[L(a+'0.1','helpful','acids as fermentation by-products')]),
a+'5.2':(1,[L(a+'4.4','helpful','yeast extract B vitamins')]),
a+'5.3':(1,[]),
})
b='hom-food-safety-s5.'
build('hom-food-safety-s5',{
b+'0.b':(1,[]),b+'0.0':(1,[]),b+'0.1':(1,[]),b+'0.2':(1,[]),
b+'0.3':(1,[L(b+'0.1','essential','uses active site and substrate')]),
b+'0.4':(1,[]),
b+'1.b':(1,[]),
b+'1.0':(1,[L(b+'0.0','helpful','enzymes keep working after picking')]),
b+'1.1':(1,[L(b+'1.0','helpful','ripening enzyme changes')]),
b+'1.2':(1,[L(b+'1.0','helpful','enzymes soften and sweeten fruit')]),
b+'2.b':(1,[]),b+'2.0':(1,[]),
b+'2.1':(1,[L(b+'2.0','helpful','enzymes released from damaged cells')]),
b+'2.2':(1,[L(b+'2.1','helpful','polyphenol oxidase reaction')]),
b+'2.3':(1,[]),
b+'3.b':(1,[]),b+'3.0':(2,[]),b+'3.1':(1,[]),
b+'3.2':(1,[L(b+'4.0','helpful','blanching inactivates enzymes')]),
b+'3.3':(2,[L(b+'2.1','helpful','oxidase acts with oxygen')]),
b+'4.b':(1,[]),
b+'4.0':(1,[L(b+'0.3','helpful','heat denatures enzymes')]),
b+'4.1':(1,[L(b+'2.1','helpful','browning enzyme is oxidase')]),
b+'4.2':(1,[L(b+'0.4','helpful','cold slows but keeps enzymes')]),
b+'4.3':(1,[]),
b+'4.4':(2,[L(b+'2.1','helpful','oxidase needs oxygen to brown')]),
b+'4.5':(1,[L(b+'0.2','helpful','enzymes need water')]),
b+'4.6':(1,[]),
})
c='hom-fish-seafood-s2.'
f='hom-food-preservation-s2.'
build('hom-fish-seafood-s2',{
c+'0.b':(1,[]),c+'0.0':(1,[]),c+'0.1':(1,[]),c+'0.2':(1,[]),c+'0.3':(1,[]),c+'0.4':(1,[]),c+'0.5':(1,[]),
c+'0.6':(2,[]),c+'0.7':(2,[]),c+'0.8':(1,[]),
c+'1.b':(1,[]),c+'1.0':(1,[]),
c+'2.b':(1,[]),
c+'2.0':(1,[L('hom-food-safety-s3.0.4','helpful','rancidity is fat going off')]),
c+'2.1':(1,[]),
c+'2.2':(1,[L(c+'2.1','essential','uses glycogen stores')]),
c+'2.3':(1,[L('hom-food-safety-s3.1.0','helpful','bacterial putrefaction of protein')]),
c+'2.4':(1,[L('hom-food-safety-s3.0.1','helpful','enzyme action in food')]),
c+'3.b':(1,[]),
c+'3.0':(1,[L('hom-food-safety-s3.5.0','helpful','low temperature slows growth')]),
c+'3.1':(1,[]),c+'3.2':(1,[]),c+'3.3':(1,[]),c+'3.4':(1,[]),
c+'3.5':(1,[L(c+'2.0','helpful','rancidity of fish fats')]),
c+'4.b':(2,[L(f+'0.0','helpful','freezing stops enzymes and growth')]),
c+'4.0':(1,[]),
c+'4.1':(1,[L(f+'2.1.6'.replace('2.1.6','1.6'),'helpful','fast-freeze setting timing')]),
c+'4.2':(1,[]),
c+'4.3':(1,[L(f+'3.5','helpful','do not overload freezer')]),
c+'4.4':(1,[L(f+'4.0','helpful','freezer burn')]),
c+'4.5':(1,[]),c+'4.6':(1,[]),
c+'4.7':(1,[L(f+'4.3','helpful','no refreezing thawed food')]),
c+'5.b':(1,[]),c+'5.0':(1,[]),c+'5.1':(1,[]),
c+'5.2':(1,[L(f+'4.0','helpful','freezer burn')]),
c+'5.3':(2,[]),c+'5.4':(1,[]),
})
