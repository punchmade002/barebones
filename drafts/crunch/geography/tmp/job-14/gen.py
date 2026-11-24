import json,re
B='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-economic-environment-s2.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful'; E='essential'
two={'0.0','0.1','4.1','4.3','4.4','5.0','5.2','7.1','7.2','10.0','10.4','11.3','11.7','14.0','20.1'}
n1={
'1.2':[L(P+'2.0',H,'CO2 as greenhouse gas','low')],
'2.0':[L(P+'3.0',H,'CO2 causes global warming')],
'2.1':[L(P+'4.1',H,'SO2 forms acid rain')],
'2.2':[L(P+'4.1',H,'NOx forms acid rain')],
'4.1':[L(P+'2.1',H,'uses SO2 and NOx')],
'4.2':[L(P+'2.1',H,'sulphur-bearing fuels give SO2')],
'4.3':[L(P+'4.b',H,'transboundary pollution idea')],
'5.0':[L(P+'4.1',H,'acid deposition harms soil')],
'5.1':[L(P+'4.1',H,'acid deposition acidifies lakes')],
'5.2':[L(P+'4.1',H,'acids dissolve limestone')],
'6.2':[L(P+'2.1',H,'scrubbers remove SO2'),L('geo-economic-environment-s1.6.1',H,'Moneypoint station','low')],
'6.3':[L(P+'2.2',H,'catalytic converters cut NOx')],
'6.5':[L(P+'2.1',H,'low SO2 fuels')],
'7.2':[L(P+'7.1',E,'temperature inversion')],
'8.1':[L(P+'8.0',H,'Great Smog led to law')],
'8.3':[L(P+'8.2',H,'Dublin smog led to ban','low')],
'8.4':[L(P+'8.3',E,'the Dublin smoky coal ban')],
'10.0':[L(P+'10.b',H,'onshore versus offshore')],
'11.4':[L(P+'11.2',E,'pumped storage at peak')],
'14.2':[L(P+'14.0',H,'Iceland hot crust example')],
'15.3':[L(P+'2.0',H,'CO2 released when burned')],
'17.2':[L(P+'16.3',H,'Chernobyl fears')],
'18.1':[L(P+'2.1',H,'SO2 and NOx emissions','low')],
'18.2':[L('geo-economic-environment-s1.2.4',H,'import bill and exposure')],
'18.5':[L('geo-economic-environment-s1.11.b',H,'renewable targets')],
'20.0':[L('geo-economic-environment-s1.3.1',H,'Ireland energy imports')],
'20.1':[L('geo-economic-environment-s1.11.2',H,'Climate Action Plan targets')],
'20.2':[L('geo-economic-environment-s1.13.b',H,'interconnectors')],
'21.b':[L('geo-mapwork-s1.0.b',H,'OS map reading')],
'21.1':[L(P+'10.3',H,'shadow flicker and noise')],
'21.2':[L(P+'19.3',H,'grid connection need','low')],
'21.3':[L(P+'10.4',H,'peat slide risk')],
}
n2={
'0.1':[L('geo-rocks-weathering-s2.14.0',H,'fracking of shale')],
'9.0':[L('geo-rocks-weathering-s2.13.0',H,'oil spill example','low')],
'10.4':[L('geo-rocks-weathering-s2.2.4',H,'slide as mass movement','low')],
'11.b':[L('geo-rivers-s4.1.b',H,'falling water drives turbines')],
'11.0':[L('geo-rivers-s4.1.0',H,'reservoir releasing water through turbines')],
'11.3':[L('geo-rivers-s4.4.b',H,'Ardnacrusha and Shannon Scheme')],
'11.7':[L('geo-rivers-s4.8.b',H,'Three Gorges effects')],
'14.b':[L('geo-rocks-weathering-s2.15.b',H,'earth heat as energy')],
'14.0':[L('geo-rocks-weathering-s2.18.0',H,'Iceland geothermal case')],
'14.1':[L('geo-rocks-weathering-s2.19.2',H,'ground-source heat pumps')],
'14.2':[L('geo-rocks-weathering-s2.15.2',H,'heat near plate boundaries')],
'19.4':[L('geo-rivers-s4.3.5',H,'dams harm habitats','low')],
'21.b':[L('geo-mapwork-s1.35.b',H,'site choice method')],
'21.0':[L('geo-mapwork-s1.35.3',H,'wind farm site needs')],
'21.4':[L('geo-mapwork-s1.35.4',H,'site disadvantages conflict')],
}
def targets(f):
    t=open(B+'packs/'+f+'.txt').read().split('CANDIDATES')[0]
    return re.findall(r'^\[(geo-[^\]]+)\]',t,re.M)
def run(f,links,cost):
    ids=targets(f); full=set(re.findall(r'^\[(geo-[^\]]+)\]',open(B+'packs/'+f+'.txt').read(),re.M))
    out={}
    for i in ids:
        k=i[len(P):]
        d={}
        if cost: d['cost']=2 if k in two else 1
        d['needs']=links.get(k,[])
        out[i]=d
    nl=sum(len(v['needs']) for v in out.values()); low=sum(n['confidence']=='low' for v in out.values() for n in v['needs'])
    for v in out.values():
        for n in v['needs']: assert n['id'] in full,n
    json.dump(out,open(B+'point-links/'+f+'.json','w'),indent=1)
    print(f,len(ids),nl,sum(v.get('cost')==2 for v in out.values()),low)
run('geo-economic-environment-s2.t1g1',n1,True)
run('geo-economic-environment-s2.t1g2',n2,False)
