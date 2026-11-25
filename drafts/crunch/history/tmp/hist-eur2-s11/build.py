import json,re,sys
H,E,L='helpful','essential','low'
def mk(pack,out,pre,data):
    txt=open(pack).read()
    tgt=[]
    for l in txt.split('CANDIDATES')[0].splitlines():
        m=re.match(r'\[(\S+?)\]',l)
        if m: tgt.append(m.group(1))
    allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
    res={}
    for k,(c,ns) in data.items():
        kid=k if k.startswith('hist-') else pre+k
        res[kid]={"cost":c,"needs":[{"id":(i if i.startswith('hist-') else pre+i),"strength":s,"why":w,"confidence":('low' if f else 'high')} for (i,s,w,f) in ns]}
    assert list(res)==tgt,(set(tgt)-set(res),set(res)-set(tgt))
    for k,v in res.items():
        for n in v['needs']:
            assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(res,open(out,'w'),indent=1)
    nl=sum(len(v['needs']) for v in res.values())
    print(len(res),nl,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
def n(i,s,w,f=0): return (i,s,w,f)
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(2,[n('0.1',H,'her radioactivity research')]),
'0.3':(1,[n('0.2',H,'uses radium discovery')]),
'0.4':(1,[n('0.1',H,'Becquerel and radioactivity')]),
'0.5':(1,[]),
'0.6':(1,[n('0.2',H,'polonium and radium discovery')]),
'0.7':(1,[]),
'0.8':(1,[n('2.0',H,'uses X-rays')]),
'0.9':(1,[]),'0.10':(2,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[n('1.0',H,'microbes cause disease idea')]),
'1.2':(1,[n('1.1',H,'Pasteur vaccines')]),
'1.3':(2,[n('1.0',H,'germ theory of disease',1)]),
'1.4':(2,[]),'1.5':(1,[]),
'1.6':(1,[n('1.0',H,'microbes cause infection',1)]),
'1.7':(2,[n('1.6',H,'antiseptic surgery contrast')]),
'1.8':(1,[]),
'2.0':(1,[]),
'2.1':(1,[n('0.8',E,'Curie mobile X-ray units'),n('2.0',E,'uses X-rays')]),
'2.2':(1,[]),'2.3':(2,[]),'2.4':(2,[]),
'2.5':(1,[n('2.4',E,'uses Marconi wireless')]),
'2.6':(1,[]),
'3.0':(2,[]),
'3.1':(1,[n('3.0',H,'Wright brothers flight')]),
'3.2':(1,[n('3.0',H,'early powered flight')]),
'3.3':(1,[]),'3.4':(2,[]),'3.5':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(2,[n('4.0',E,"Otto's four-stroke engine")]),
'4.2':(2,[n('4.0',H,'internal combustion engine')]),
'4.3':(1,[n('4.1',E,'Daimler engine work'),n('4.2',E,"Benz's Motorwagen")]),
'4.4':(2,[n('4.2',E,"Benz's Motorwagen")]),
'4.5':(2,[n('4.1',E,'Daimler engines')]),
'4.6':(1,[]),'4.7':(1,[]),
'4.8':(1,[n('4.1',H,'Daimler and his engine')]),
'4.9':(1,[]),
'5.0':(1,[]),
'5.1':(1,[n('5.0',E,"Ford's cheap car aim")]),
'5.2':(2,[n('5.1',H,'Model T production')]),
'5.3':(1,[n('5.2',E,'moving assembly line')]),
'5.4':(1,[n('5.2',H,'Ford mass production')]),
'5.5':(2,[]),
'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),
'6.3':(2,[n('hist-eur2-s5.2.1',E,'Verdun supply'),n('hist-eur2-s5.0.2',E,'Battle of the Marne')]),
'6.4':(1,[n('hist-eur2-s5.1.5',H,'tanks in the war')]),
'6.5':(1,[]),
'6.6':(1,[n('5.1',H,'Model T in USA')]),
'7.0':(1,[n('1.0',H,'germ theory'),n('2.0',H,'X-ray diagnosis')]),
'7.1':(1,[n('0.9',E,'Curie died of radiation')]),
'7.2':(1,[n('2.3',H,'Edison and electricity'),n('2.4',H,'Marconi wireless')]),
'7.3':(1,[n('3.2',H,'aircraft in the war'),n('6.3',H,'motor vehicles in war')]),
'7.4':(2,[n('4.2',H,"Benz's early car"),n('5.1',E,'Model T mass product')]),
'7.5':(2,[n('0.6',H,'Curie recognition',1)]),
}
mk(P+'packs/hist-eur2-s11.t1g1.txt',P+'point-links/hist-eur2-s11.t1g1.json','hist-eur2-s11.',d)
