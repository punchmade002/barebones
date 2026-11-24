import json,re,sys
H,E,L='helpful','essential','low'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def run(pack,out,spec):
    txt=open(pack).read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tgt=[]
    sec=txt.split('\nCANDIDATES')[0]
    tgt=re.findall(r'^\[([^\]]+)\]',sec,re.M)
    assert [t for t,_,_ in spec]==tgt,(set(tgt)^set(t for t,_,_ in spec))
    d={}
    for t,c,nd in spec:
        for x in nd: assert x['id'] in ids and x['id']!=t,x
        d[t]={"cost":c,"needs":nd}
    json.dump(d,open(out,'w'),indent=1)
    links=sum(len(v['needs']) for v in d.values())
    print(len(d),links,sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
a='hist-eur2-s3.'
s1=[
(a+'0.b',1,[]),(a+'0.0',1,[]),
(a+'0.1',1,[n('hist-eur2-s1.7.4',H,'Bismarck resignation') ]),
(a+'0.2',1,[n('hist-eur2-s1.1.1',H,'Anti-Socialist Law')]),
(a+'0.3',1,[]),(a+'0.4',1,[]),
(a+'0.5',1,[n(a+'0.4',E,'Daily Telegraph affair')]),
(a+'0.6',1,[]),(a+'0.7',1,[]),(a+'0.8',1,[]),
(a+'0.9',1,[n('hist-eur2-s2.0.0',H,'Holstein and German foreign policy','low')]),
(a+'0.10',2,[]),
(a+'1.b',1,[]),(a+'1.0',1,[]),
(a+'1.1',1,[n('hist-eur2-s1.1.2',H,'growth of the SPD','low')]),
(a+'1.2',1,[]),
(a+'1.3',2,[n('hist-eur2-s2.5.1',H,'powers seizing Chinese concessions','low')]),
(a+'1.4',1,[n('hist-eur2-s2.6.4',E,'the Jameson Raid')]),
(a+'1.5',2,[]),(a+'1.6',1,[]),
(a+'1.7',1,[n('hist-eur2-s2.7.1',H,'the Moroccan crises')]),
(a+'2.b',1,[]),(a+'2.0',1,[]),(a+'2.1',1,[]),(a+'2.2',1,[]),
(a+'2.3',2,[n(a+'2.2',E,'Tirpitz and his battle fleet plan')]),
(a+'2.4',1,[n(a+'2.2',H,'Tirpitz and the fleet plan')]),
(a+'2.5',1,[]),(a+'2.6',1,[]),
(a+'3.0',2,[]),
(a+'3.1',2,[n(a+'3.0',E,'the First Navy Law'),n('hist-eur2-s2.6.4',H,'the Boer War','low')]),
(a+'3.2',1,[n(a+'2.3',E,'the risk theory')]),
(a+'3.3',2,[n(a+'3.1',H,'the German naval laws')]),
(a+'3.4',2,[n(a+'3.2',H,'the planned fleet ratio','low')]),
(a+'3.5',1,[n(a+'3.4',E,'HMS Dreadnought')]),
(a+'3.6',1,[n(a+'3.4',E,'dreadnoughts')]),
(a+'3.7',1,[n(a+'3.4',H,'dreadnought-class ships')]),
(a+'3.8',1,[n(a+'3.7',H,'the 1912 naval expansion','low')]),
(a+'4.0',1,[n('hist-eur2-s2.1.b',H,'Britain ending isolation')]),
(a+'4.1',1,[n(a+'3.3',H,'Admiral Fisher')]),
(a+'4.2',1,[]),
(a+'4.3',1,[n(a+'4.2',H,'the failed naval talks')]),
(a+'4.4',2,[n(a+'4.2',H,'neutrality versus limits on building')]),
(a+'4.5',2,[n('hist-eur2-s2.1.3',H,'the Anglo-French naval agreement')]),
(a+'4.6',1,[n(a+'1.5',H,'the Baghdad Railway')]),
(a+'5.0',1,[n(a+'2.3',E,'the risk theory aim')]),
(a+'5.1',1,[]),(a+'5.2',1,[]),(a+'5.3',1,[]),(a+'5.4',1,[]),(a+'5.5',1,[]),
(a+'6.0',1,[]),(a+'6.1',1,[]),(a+'6.2',1,[]),
(a+'6.3',2,[n(a+'1.b',H,'Weltpolitik','low')]),
(a+'6.4',2,[n(a+'2.4',H,'Tirpitz domestic motives')]),
(a+'6.5',1,[]),
(a+'7.0',1,[]),(a+'7.1',1,[]),
(a+'7.2',1,[n(a+'1.3',H,'Kiaochow and Samoa')]),
(a+'7.3',1,[n('hist-eur2-s2.7.1',H,'the Tangier crisis')]),
(a+'7.4',1,[]),
(a+'7.5',1,[n('hist-eur2-s2.1.7',H,'German sense of encirclement')]),
(a+'7.6',1,[]),
]
run(P+'packs/hist-eur2-s3.t1g1.txt',P+'point-links/hist-eur2-s3.t1g1.json',s1)
b='hist-eur4-s13.'
s2=[
(b+'0.b',1,[]),(b+'0.0',1,[]),
(b+'0.1',1,[n(b+'0.0',H,'penicillin and antibiotics')]),
(b+'0.2',1,[]),(b+'0.3',1,[]),(b+'0.4',2,[]),(b+'0.5',1,[]),(b+'0.6',1,[]),(b+'0.7',1,[]),(b+'0.8',2,[]),
(b+'1.b',1,[]),(b+'1.0',1,[]),
(b+'1.1',1,[n(b+'1.0',E,'the DNA double helix')]),
(b+'1.2',1,[]),(b+'1.3',1,[]),
(b+'1.4',1,[n(b+'1.0',H,'the double helix discovery')]),
(b+'1.5',1,[]),
(b+'1.6',1,[n(b+'1.2',E,'recombinant DNA techniques')]),
(b+'2.b',1,[]),(b+'2.0',2,[]),
(b+'2.1',2,[n(b+'1.3',H,'IVF')]),
(b+'2.2',1,[n(b+'1.0',H,'DNA','low')]),
(b+'2.3',1,[n(b+'2.1',H,'genetic and embryo ethics debate')]),
(b+'3.b',1,[]),(b+'3.0',1,[]),(b+'3.1',1,[]),
(b+'3.2',1,[n(b+'3.7',H,'oil crisis expansion of nuclear power','low')]),
(b+'3.3',1,[]),(b+'3.4',1,[]),(b+'3.5',1,[]),(b+'3.6',1,[]),(b+'3.7',1,[]),
(b+'3.8',1,[n(b+'4.2',H,'the Chernobyl reactors','low')]),
(b+'4.b',1,[]),(b+'4.0',1,[]),(b+'4.1',1,[]),(b+'4.2',1,[]),
(b+'4.3',1,[n(b+'4.2',E,'the Chernobyl explosion')]),
(b+'4.4',1,[n('hist-eur4-s2.7.1',H,'NATO missile deployments')]),
(b+'4.5',1,[]),(b+'4.6',1,[]),(b+'4.7',1,[]),
(b+'4.8',2,[n(b+'4.2',E,'the Chernobyl explosion')]),
(b+'4.9',1,[n(b+'4.3',H,'the Chernobyl exclusion zone')]),
(b+'4.10',1,[n(b+'4.8',H,'the Chernobyl accident and response')]),
(b+'5.b',1,[]),(b+'5.0',1,[]),(b+'5.1',1,[]),(b+'5.2',1,[]),
(b+'5.3',2,[n(b+'5.2',H,'the transistor','low')]),
(b+'5.4',1,[]),
(b+'5.5',1,[n(b+'5.3',H,'the microprocessor')]),
(b+'5.6',1,[]),
(b+'5.7',1,[n(b+'5.0',H,'wartime code-breaking at Bletchley','low')]),
(b+'5.8',1,[n(b+'5.4',H,'IBM mainframes','low')]),
(b+'5.9',1,[n(b+'5.3',H,'the microprocessor')]),
(b+'5.10',1,[]),
(b+'5.11',1,[n(b+'3.3',H,'CERN')]),
(b+'6.b',1,[]),(b+'6.0',1,[]),(b+'6.1',1,[]),
(b+'6.2',1,[n(b+'6.1',H,'Western export controls')]),
(b+'6.3',1,[]),(b+'6.4',1,[]),
(b+'6.5',1,[n(b+'6.0',H,'automation of work')]),
(b+'6.6',2,[n(b+'6.2',H,'the Soviet computing gap')]),
(b+'6.7',1,[]),
(b+'7.b',1,[]),(b+'7.0',1,[]),(b+'7.1',1,[]),(b+'7.2',1,[]),(b+'7.3',1,[]),
]
run(P+'packs/hist-eur4-s13.t1g1.txt',P+'point-links/hist-eur4-s13.t1g1.json',s2)
