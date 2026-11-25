import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def h(i,w): return (i,'helpful',w,'high')
def e(i,w): return (i,'essential',w,'high')
def lo(t): return (t[0],t[1],t[2],'low')
def run(name,pref,own,data):
    out={}
    for k,(c,ls) in data.items():
        out[f'{pref}.{k}']={'cost':c,'needs':[{'id':(l[0] if l[0].startswith('hist-') else f'{own}.{l[0]}'),'strength':l[1],'why':l[2],'confidence':l[3]} for l in ls]}
    txt=open(B+f'packs/{name}.txt').read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[(hist-[^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
    assert list(out)==ids,(set(ids)^set(out))
    for k,v in out.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(out,open(B+f'point-links/{name}.json','w'),indent=0)
    print(name,len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
S6='hist-eur6-s6.';S3='hist-eur6-s3.'
d1={
'0.b':(1,[]),
'0.0':(1,[h(S6+'1.1','dollar tied to gold, Bretton Woods')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),
'1.b':(1,[h(S3+'9.1','guns and butter')]),
'1.0':(1,[h(S3+'0.5','the Great Society')]),
'1.1':(1,[]),
'1.2':(1,[h('1.1','spending outrunning output')]),
'1.3':(1,[h('1.0','Johnson not raising taxes')]),
'1.4':(1,[h('1.3','the delayed tax increase')]),
'1.5':(1,[h('0.2','budget deficit defined')]),
'1.6':(1,[]),
'1.7':(1,[e(S6+'1.1','dollar convertible to gold')]),
'2.b':(1,[h('1.7','strain on dollar and gold')]),
'2.0':(1,[e(S6+'1.1','dollar convertible to gold')]),
'2.1':(1,[h('2.0','the same 1971 measures')]),
'2.2':(1,[h('0.2','trade deficit defined')]),
'2.3':(1,[h('2.0','end of Bretton Woods')]),
'3.b':(1,[h('0.1','stagflation defined')]),
'3.0':(1,[]),
'3.1':(1,[e('3.0','the 1973 oil embargo')]),
'3.2':(2,[e('3.0','oil price rise from embargo'),h('0.1','stagflation defined')]),
'3.3':(1,[h('3.2','inflation and recession being fought')]),
'3.4':(1,[h('3.0','the first oil shock')]),
'3.5':(1,[e('0.1','stagflation defined')]),
'4.b':(1,[h('3.0','oil crises of the 1970s')]),
'4.0':(1,[h('3.0','dependence on imported oil')]),
'4.1':(1,[h('3.0','oil shortage and prices')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'5.b':(1,[h('0.3','globalisation'),h('0.5','rust belt')]),
'5.0':(1,[h('0.3','foreign competition')]),
'5.1':(1,[h('5.0','steel mills closing')]),
'5.2':(1,[h('3.0','oil shocks')]),
'5.3':(1,[h('5.2','Japanese car makers')]),
'5.4':(1,[]),
'5.5':(1,[h('5.3','Japanese car gains')]),
'6.b':(1,[]),
'6.0':(2,[h('0.3','global change and rivals')]),
'6.1':(1,[]),
'6.2':(1,[h('0.2','trade deficit defined')]),
'6.3':(1,[e('6.1','high dollar hurting exporters')]),
'6.4':(1,[e('0.5','rust belt and Sun Belt')]),
'6.5':(1,[h('6.4','manufacturing losses')]),
'7.b':(1,[]),
'7.0':(1,[h('0.1','inflation defined')]),
'7.1':(1,[e('7.0','Volcker\'s interest rate rises')]),
'7.2':(1,[]),
'7.3':(1,[h('7.2','supply-side tax theory')]),
'7.4':(1,[]),
'7.5':(1,[e('7.3','the tax cuts')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[h('0.4','deregulation defined')]),
'8.2':(1,[h('1.5','budget deficit')]),
'8.3':(1,[h('7.3','1981 tax cuts')]),
'8.4':(1,[h('0.1','inflation and unemployment')]),
'8.5':(1,[h('8.4','mid-1980s recovery')]),
'9.b':(1,[h('7.3','Reagan tax cuts')]),
'9.0':(1,[e('7.3','Reagan tax cuts')]),
'9.1':(1,[h('9.0','large deficits')]),
'9.2':(1,[e('6.1','strong dollar hurts exports')]),
'9.3':(1,[h('9.2','foreign capital financing deficits')]),
'9.4':(2,[h('6.3','Plaza Accord'),h('6.1','high dollar')]),
'9.5':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(1,[h('7.3','1981 tax cuts'),h('8.3','1986 tax reform')]),
'10.2':(1,[h('5.b','manufacturing decline')]),
'10.3':(1,[]),'10.4':(1,[]),
'10.5':(1,[h('6.4','urban areas losing industry')]),
'11.b':(1,[]),
'11.0':(1,[h('8.5','1980s job expansion')]),
'11.1':(1,[h('9.1','rising national debt')]),
'11.2':(2,[h('1.0','Vietnam and Great Society cost'),h('2.0','end of Bretton Woods'),h('3.0','oil shocks'),h('5.b','foreign competition')]),
'11.3':(2,[h('10.1','widening income gap'),h('3.2','1970s stagflation')]),
'11.4':(2,[h('6.1','high dollar'),h('5.b','manufacturing decline')]),
'11.5':(1,[]),
}
run('hist-eur6-s7.t1g1','hist-eur6-s7','hist-eur6-s7',d1)
