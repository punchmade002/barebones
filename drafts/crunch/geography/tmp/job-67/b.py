import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
T='geo-option-global-interdependence-s2.'
def h(i,w,s='helpful',c='high'): return (i,s,w,c)
E='geo-economic-development-s4.'; M='geo-population-migration-s4.'; G='geo-economic-globalisation-s2.'
ids="0.b 0.0 0.1 0.2 1.b 1.0 1.1 1.2 2.b 2.0 2.1 2.2 2.3 2.4 2.5 2.6 3.b 3.0 3.1 3.2 3.3 3.4 3.5 3.6 4.b 4.0 4.1 4.2 5.b 5.0 5.1 5.2 5.3 5.4 5.5 6.b 6.0 6.1 6.2 6.3 6.4 7.b 7.0 7.1 7.2 7.3 7.4 7.5 8.b 8.0 8.1 8.2 8.3 9.b 9.0 9.1 9.2 10.b 10.0 10.1 10.2 11.b 11.0 11.1 11.2 11.3 11.4 11.5 11.6 12.b 12.0 12.1 12.2 12.3 12.4 12.5 12.6 13.b 13.0 13.1 13.2 13.3 14.b 14.0 14.1 14.2 14.3 14.4 15.b 15.0 15.1 15.2 15.3 15.4 16.b 16.0 16.1 16.2 16.3 17.b 17.0 17.1 17.2 17.3 18.b 18.0 18.1 18.2 18.3 18.4 19.b 19.0 19.1 19.2 19.3 20.b 20.0 20.1 20.2 21.b 21.0 21.1 21.2 21.3 21.4 21.5 21.6 21.7 22.b 22.0 22.1".split()
assert len(ids)==131
p1={i:[] for i in ids}  # every id explicitly judged; empties reviewed
p1['0.2']=[h(M+'0.3','refugee definition',c='low')]
p1['1.0']=[h(E+'17.0','firms locate work in low-wage countries',c='low')]
p1['1.2']=[h(E+'3.2','most price goes to brands/retailers')]
p1['2.3']=[h(E+'19.2','cobalt from DR Congo')]
p1['3.0']=[h(E+'17.1','jobs and wages for workers',c='low')]
p1['3.2']=[h(E+'3.2','unequal share of final price')]
p1['3.3']=[h(E+'17.2','exploitation: long hours, pressure',c='low')]
p1['3.6']=[h(E+'19.3','same Amnesty cobalt child labour')]
p1['4.1']=[h(E+'3.2','profit captured by brands in rich countries')]
p1['7.0']=[h(E+'3.0','dependence on few primary commodities')]
p1['7.2']=[h(E+'6.0','guaranteed price floor to raise incomes',c='low')]
p1['7.3']=[h(E+'19.1','child labour in cocoa')]
p1['7.4']=[h(E+'19.1','child labour in cocoa',c='low')]
p1['8.1']=[h(E+'3.0','unstable commodity prices',c='low')]
p1['8.3']=[h(E+'3.2','value added far from growers')]
p1['9.0']=[h(E+'6.b','Fairtrade Mark')]
p1['9.2']=[h(E+'7.4','fair trade criticisms',c='low')]
p1['10.0']=[h(E+'3.2','brands and retail take most price')]
p1['10.1']=[h(E+'21.0','consumer campaigns pressure firms')]
p1['10.2']=[h(E+'21.1','due diligence rules on supply chains',c='low')]
p1['21.2']=[h(E+'3.0','cash crops for export',c='low')]
p1['21.3']=[h(E+'22.0','emissions from rich regions')]
for k in p1: assert k in ids
p2={i:[] for i in ids}
p2['0.1']=[h(G+'0.b','MNC and footloose firms',c='low')]
p2['1.0']=[h(G+'1.0','low labour costs attract production')]
p2['2.4']=[h(G+'4.3','contract manufacturers',c='low')]
p2['2.5']=[h(G+'2.2','Apple assembly in India')]
p2['3.5']=[h(G+'2.2','assembly shifting to India')]
p2['5.1']=[h(G+'12.1','Apple Cork customer support',c='low')]
p2['5.5']=[h(G+'2.2','assembly moving to India')]
p2['6.1']=[h(G+'4.0','mergers and takeovers',c='low')]
p2['11.1']=[h(G+'2.3','fab means chip factory',c='low')]
p2['11.4']=[h(G+'7.0','Leixlip investment')]
p2['11.5']=[h(G+'7.1','Fab 34 sale to Apollo')]
p2['11.6']=[h(G+'7.3','CHIPS Act and US stake'),h(G+'7.2','Intel job cuts')]
p2['12.2']=[h(G+'13.2','computer services exporter')]
p2['12.3']=[h(G+'12.0','IDA support attracting firms',c='low')]
p2['12.6']=[h(G+'16.3','global minimum tax')]
for k in p2: assert k in ids
def out(name,d):
    o={}
    for i in ids:
        o[T+i]={"needs":[{"id":x[0],"strength":x[1],"why":x[2],"confidence":x[3]} for x in d[i]]}
    json.dump(o,open(P+'point-links/'+name+'.json','w'),indent=1,ensure_ascii=False)
    txt=open(P+'packs/'+name+'.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M)); tg=[T+i for i in ids]
    r=json.load(open(P+'point-links/'+name+'.json'))
    assert list(r)==tg and set(tg)<=pk
    n=sum(len(v['needs']) for v in r.values()); lo=sum(x['confidence']=='low' for v in r.values() for x in v['needs'])
    assert all(x['id'] in pk and x['id']!=k for k,v in r.items() for x in v['needs'])
    print(name,len(r),n,lo)
out('geo-option-global-interdependence-s2.t1g4',p1)
out('geo-option-global-interdependence-s2.t1g5',p2)
