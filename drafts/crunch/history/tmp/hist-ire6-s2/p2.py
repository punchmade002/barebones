import json,re
P='hist-ire6-s2.'
E,H='essential','helpful'
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(2,[('s1:5.3',H,'1955-56 crisis met by deflation','high'),('s1:4.1',H,'1952 deflationary budget','high')]),
'0.5':(1,[('s1:7.0',H,'1957 Fianna Fail election win','high')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[('1.0',H,'Whitaker at Finance','high')]),
'1.2':(2,[('0.0',H,'protection and its failings','high')]),
'1.3':(2,[]),
'1.4':(2,[('0.1',E,'Control of Manufactures Acts','high')]),
'1.5':(1,[('1.1',E,'Economic Development report','high')]),
'2.b':(1,[]),
'2.0':(1,[('0.3',H,'emigration problem','high')]),
'2.1':(1,[]),
'2.2':(2,[('0.1',E,'rule on Irish shareholding','high')]),
'2.3':(2,[]),
'2.4':(1,[('s1:1.4',H,'the IDA','high')]),
'2.5':(1,[]),'2.6':(1,[]),
'2.7':(1,[('1.3',H,'productive over social investment','high')]),
'3.b':(1,[('2.1',H,'the growth target','high')]),
'3.0':(1,[('2.1',E,'the 2 per cent target','high')]),
'3.1':(1,[('2.2',H,'foreign-owned firms','high')]),
'3.2':(1,[('0.3',H,'1950s emigration figures','high')]),
'3.3':(1,[('3.2',H,'falling emigration and population','low')]),
'3.4':(1,[]),
'3.5':(1,[('0.4',H,'balance of payments crises','high')]),
'3.6':(1,[('3.0',H,'growth against target','low')]),
'4.0':(1,[]),
'4.1':(1,[('0.3',H,'pessimism of the 1950s','low')]),
'4.2':(2,[('2.2',H,'openness to foreign investment','high')]),
'4.3':(2,[('2.3',E,'Export Profits Tax Relief','high'),('3.6',H,'world boom helping exports','high')]),
'4.4':(2,[('2.2',H,'foreign firms in Ireland','high')]),
'4.5':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(2,[]),
'5.2':(2,[('4.0',H,'the First Programme and planning','high'),('0.4',H,'balance of payments deficit','low')]),
'5.3':(2,[('6.2',H,'free trade with Britain','high')]),
'5.4':(1,[('6.3',H,'lower tariffs','low')]),
'5.5':(1,[]),
'5.6':(1,[('6.6',E,'Lemass-O Neill meetings','high')]),
'6.b':(1,[('0.0',H,'protection','high')]),
'6.0':(1,[]),
'6.1':(2,[('6.0',E,'Irelands EEC application','high')]),
'6.2':(2,[('6.1',E,'EEC entry delayed','high')]),
'6.3':(1,[('6.2',E,'the Free Trade Agreement','high')]),
'6.4':(1,[('6.3',E,'free trade removing tariffs','high')]),
'6.5':(1,[('6.4',H,'effects of free trade','low')]),
'6.6':(2,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(2,[('1.5',H,'Economic Development and the First Programme','high')]),
'7.2':(1,[('7.1',H,'Whitaker at Finance','high')]),
'7.3':(2,[]),'7.4':(1,[]),
'7.5':(2,[('7.1',H,'Whitakers role in planning','high'),('5.0',H,'Lemass political will','low')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(2,[]),
'8.2':(1,[('0.0',E,'the protectionist policy of the 1930s','high')]),
'8.3':(1,[('1.5',H,'the First Programme','high'),('6.0',H,'the EEC application','high'),('6.3',H,'the Free Trade Agreement','high')]),
'8.4':(1,[]),
'8.5':(2,[('5.6',H,'partition and Northern Ireland meetings','low')]),
'9.0':(1,[('7.1',H,'Whitaker as author','high'),('8.3',H,'Lemass as Taoiseach','high')]),
'9.1':(1,[('5.2',E,'the Second Programme','high')]),
'9.2':(1,[('3.0',E,'growth against target','high'),('3.2',H,'falling emigration','high')]),
'9.3':(1,[('3.4',H,'employment and unemployment','high')]),
'9.4':(1,[]),
'9.5':(2,[('3.6',H,'European boom','high')]),
}
def full(t): return 'hist-ire6-s1.'+t[3:] if t.startswith('s1:') else P+t
f='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
txt=open(f+'packs/hist-ire6-s2.t1g1.txt').read()
tg=re.findall(r'^\[(hist-ire6-s2\.[^\]]+)\]',txt,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert set(D)=={t[len(P):] for t in tg}
out={}
for t in tg:
    c,n=D[t[len(P):]]
    out[t]={'cost':c,'needs':[{'id':full(x),'strength':s,'why':w,'confidence':q} for x,s,w,q in n]}
for k,v in out.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=k,n
json.dump(out,open(f+'point-links/hist-ire6-s2.t1g1.json','w'),indent=0)
json.load(open(f+'point-links/hist-ire6-s2.t1g1.json'))
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
