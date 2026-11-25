import json,re
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-economic-globalisation-s3.'
GS='geo-graph-skills-s1.'; EU='geo-economic-eu-s1.'; D='geo-economic-development-s2.'
E,H='essential','helpful'
# suffix: (cost, [(id,strength,why,conf)]) ; ids starting with '.' are local targets
T={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[('.0.2',E,'uses balance of trade','high')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[('.1.0',H,'items in balance of payments','high')]),
'1.2':(1,[('.0.2',E,'compares with balance of trade','high')]),
'2.b':(1,[]),
'2.0':(1,[('.0.3',E,'uses trade deficit','high')]),
'2.1':(1,[('.2.0',H,'extra imports from deficit','high')]),
'2.2':(1,[]),
'2.3':(1,[('.2.0',H,'persistent deficit weakens currency','low')]),
'2.4':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[('.3.0',E,'uses many export partners','high'),('.4.1',H,'uses tariff','high')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(2,[('.4.0',H,'barriers serve protectionism','high')]),
'4.2':(1,[('.4.1',H,'removes barriers between members','high')]),
'4.3':(1,[('.4.1',H,'uses tariffs','high')]),
'4.4':(1,[]),
'4.5':(1,[('.4.4',E,'WTO is the body','high')]),
'4.6':(1,[]),
'5.b':(1,[]),
'5.0':(1,[('.4.3',H,'GATT cut tariffs','high'),('.4.4',H,'WTO rules','high')]),
'5.1':(2,[]),'5.2':(1,[('.5.1',H,'container port','high')]),
'5.3':(2,[]),'5.4':(1,[]),'5.5':(1,[]),
'6.b':(1,[('.7.b',H,'uses trading triad','high')]),
'6.0':(2,[('.5.4',H,'MNC trading components','low')]),
'6.1':(1,[('.7.b',H,'triad shipping routes','high')]),
'6.2':(1,[('.6.1',E,'Suez Canal chokepoint','high')]),
'6.3':(1,[('.6.1',H,'Suez shipping route','low')]),
'6.4':(1,[]),
'6.5':(1,[('.6.0',H,'uses supply chains','high')]),
'7.b':(1,[]),
'7.0':(1,[('.7.b',H,'triad areas','high')]),
'7.1':(1,[('.5.4',H,'uses MNCs','high'),('.7.b',H,'triad areas','high')]),
'7.2':(1,[('.7.b',E,'three triad areas','high')]),
'8.b':(1,[('.7.b',H,'USA as triad member','high')]),
'8.0':(1,[]),
'8.1':(1,[('.0.3',E,'uses trade deficit','high')]),
'8.2':(1,[('.4.2',H,'trade bloc idea','high')]),
'8.3':(1,[('.8.2',E,'replaced NAFTA','high')]),
'8.4':(1,[]),'8.5':(1,[]),
'8.6':(1,[('.8.5',H,'earlier US tariffs','low')]),
'9.b':(1,[('.7.b',H,'Europe as triad area','high')]),
'9.0':(1,[('.4.2',H,'trade bloc','high')]),
'9.1':(1,[('.9.0',H,'single market','high')]),
'9.2':(1,[('.4.2',H,'trading bloc','high')]),
'9.3':(1,[]),
'9.4':(1,[('.8.6',H,'US tariffs 2025','low')]),
'10.b':(1,[('.7.b',H,'Pacific Rim as triad area','high')]),
'10.0':(1,[('.10.b',H,'Pacific Rim definition','high')]),
'10.1':(1,[]),'10.2':(1,[]),
'10.3':(2,[('.10.0',H,'member countries','high')]),
'10.4':(2,[('.10.3',E,'RCEP is the bloc','high')]),
'10.5':(1,[('.10.0',H,'Pacific Rim members','low')]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[]),
'11.2':(2,[('.12.4',H,'China overtook Japan','low')]),
'11.3':(1,[]),'11.4':(1,[]),
'11.5':(2,[('.4.1',H,'avoiding trade barriers','high')]),
'11.6':(1,[('.11.0',H,'earlier growth','high')]),
'12.b':(1,[]),'12.0':(1,[]),
'12.1':(1,[('.12.0',H,'reforms opened economy','high')]),
'12.2':(1,[('.12.1',E,'Shenzhen is an SEZ','high')]),
'12.3':(1,[('.4.4',H,'what the WTO is','high')]),
'12.4':(1,[('.11.2',H,'Japan economy ranking','low')]),
'12.5':(1,[('.0.3',E,'uses trade surplus','high')]),
'12.6':(1,[]),
'12.7':(1,[('.8.5',H,'US tariffs trade war','high')]),
'13.b':(1,[]),'13.0':(1,[]),
'13.1':(1,[('.13.0',H,'poor starting point','high')]),
'13.2':(1,[]),'13.3':(1,[]),'13.4':(1,[]),
'13.5':(1,[('.10.5',H,'Asian Tigers','high')]),
'14.b':(1,[]),
'14.0':(1,[('.7.b',H,'contrast with triad','high')]),
'15.b':(1,[]),'15.0':(1,[]),
'15.1':(1,[('.15.0',H,'colonial raw material pattern','high')]),
'15.2':(1,[('.15.0',H,'colonial raw material pattern','high')]),
'15.3':(2,[('.15.0',H,'colonial raw material pattern','high')]),
'16.b':(1,[('.15.b',H,'earlier pattern changed','high')]),
'16.0':(1,[('.13.b',H,'uses NICs','high'),('.5.4',H,'uses MNCs','high')]),
'16.1':(1,[]),
'16.2':(1,[('.16.1',H,'core versus periphery','high')]),
'16.3':(1,[('.16.1',H,'core keeps design','high')]),
'16.4':(2,[('.16.1',H,'core keeps R&D','high')]),
'17.b':(1,[]),
'17.0':(2,[('.16.0',H,'services split like production','low')]),
'17.1':(1,[('.16.0',H,'low-cost assembly','high')]),
'17.2':(1,[('.16.0',H,'assembly moves to low-wage places','high')]),
'18.b':(1,[]),'18.0':(1,[]),
'18.1':(1,[('.18.0',H,'export value','low')]),
'18.2':(2,[('.0.0',H,'visible trade goods','low')]),
'18.3':(1,[('.0.1',H,'invisible trade services','high')]),
'18.4':(1,[('.18.3',H,'aircraft leasing service export','high')]),
'18.5':(1,[('.0.3',E,'uses trade surplus','high')]),
'19.b':(1,[]),'19.0':(1,[]),'19.1':(1,[]),
'19.2':(1,[('.18.1',H,'MNC-made exports','high')]),
'19.3':(1,[('.8.6',H,'new US tariffs','low')]),
'20.b':(1,[]),'20.0':(1,[]),
'20.1':(1,[('.9.0',H,'single market','high')]),
'20.2':(1,[]),
'20.3':(1,[('.3.0',H,'many export partners','high')]),
'21.b':(1,[]),
'21.0':(1,[('.18.1',H,'MNC-driven exports','high')]),
'21.1':(1,[('.8.6',H,'US tariffs 2025','high')]),
'22.b':(1,[]),
'22.0':(1,[(GS+'0.0',H,'check labels and units','high'),(GS+'0.1',H,'reading values from charts','high')]),
'22.1':(1,[('.0.2',E,'uses balance of trade','high')]),
'22.2':(1,[(GS+'3.1',H,'method for difference','high')]),
'22.3':(1,[(GS+'3.0',H,'method for total','high')]),
'22.4':(1,[(GS+'8.0',H,'choosing graph type','high')]),
}
# package 2: links only, to development-s2 candidates
L2={'5.5':[(D+'13.0',H,'China opened to trade','low')],
'11.2':[(D+'13.4',H,'China overtook Japan 2010','high')],
'14.0':[(D+'0.2',H,'rich North, poorer South','low')],
'15.0':[(D+'10.3',H,'colonial history left export economies','low')],
'16.1':[(D+'2.2',H,'core and periphery','high')],
'16.2':[(D+'2.2',H,'periphery meaning','high')]}
def ids(f,mode):
    out=[]
    for l in open(G+'packs/'+f):
        if l.startswith('CANDIDATES'):break
        m=re.match(r'\[(\S+)\]',l)
        if m:out.append(m.group(1))
    return out
def conv(x): return x if not x.startswith('.') else P[:-1]+x
def mk(links): return [{'id':conv(i),'strength':s,'why':w,'confidence':c} for i,s,w,c in links]
for f,mode in(('t1g1','c'),('t1g2','l')):
    tids=ids('geo-economic-globalisation-s3.%s.txt'%f,mode)
    assert [P+k for k in T]==tids,(set(tids)^set(P+k for k in T))
    out={}
    for k,(c,l) in T.items():
        if mode=='c': out[P+k]={'cost':c,'needs':mk(l)}
        else: out[P+k]={'needs':mk(L2.get(k,[]))}
    # validate ids
    txt=open(G+'packs/geo-economic-globalisation-s3.%s.txt'%f).read()
    for v in out.values():
        for n in v['needs']: assert '['+n['id']+']' in txt,n['id']
        for n in v['needs']: pass
    json.dump(out,open(G+'point-links/geo-economic-globalisation-s3.%s.json'%f,'w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values())
    lo=sum(n['confidence']=='low' for v in out.values() for n in v['needs'])
    print(f,len(out),nl,sum(v.get('cost')==2 for v in out.values()),lo)
