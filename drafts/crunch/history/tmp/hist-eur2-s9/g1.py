import json,re
P='hist-eur2-s9.'
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
E='essential';H='helpful'
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[L('hist-eur2-s5.2.0',H,'the 1915 shell shortages')]),
'0.3':(1,[]),'0.4':(1,[]),
'0.5':(1,[L('hist-eur2-s5.5.3',H,'the submarine campaign cutting supplies')]),
'0.6':(1,[]),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'1.3':(2,[L('hist-eur2-s5.5.0',E,'the British blockade of Germany')]),
'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),
'2.0':(2,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(2,[]),'3.4':(1,[]),
'4.0':(1,[L(P+'0.2',E,'the shell shortage and Munitions Ministry')]),
'4.1':(2,[L(P+'4.0',H,'the Ministry of Munitions')]),
'4.2':(1,[L(P+'4.0',H,'women filling munitions work')]),
'4.3':(2,[L(P+'4.2',H,'women munitions workers')]),
'4.4':(1,[L(P+'4.2',H,'women munitions workers')]),
'4.5':(1,[L(P+'4.3',H,'poor munitions working conditions')]),
'5.0':(1,[]),
'5.1':(1,[L(P+'4.2',H,'British munitionettes parallel','low')]),
'5.2':(1,[]),'5.3':(1,[]),
'5.4':(2,[L(P+'0.3',E,'the Hindenburg Programme')]),
'5.5':(1,[L(P+'1.3',H,'German food shortages')]),
'6.0':(1,[]),'6.1':(1,[]),
'6.2':(1,[L('hist-eur2-s5.5.3',H,'the submarine campaign threatening food')]),
'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),
'7.0':(1,[]),
'7.1':(1,[L(P+'4.1',E,'the dilution agreement')]),
'7.2':(1,[]),
'7.3':(1,[L(P+'7.2',E,'the WSPU suspending militancy')]),
'7.4':(1,[L(P+'7.3',H,'the Pankhursts and the war')]),
'7.5':(1,[L(P+'8.0',H,'the 1918 vote for women')]),
'8.0':(2,[L(P+'3.3',H,'women lacking the vote before the war')]),
'8.1':(1,[L(P+'8.0',E,'the 1918 limited franchise')]),
'8.2':(1,[]),'8.3':(1,[]),
'8.4':(2,[L(P+'7.1',H,'restoring pre-war practices')]),
'8.5':(1,[]),
'9.0':(1,[L(P+'8.0',H,'women winning the vote')]),
'9.1':(1,[L(P+'8.4',H,'women losing jobs after 1918')]),
'9.2':(1,[]),
'9.3':(2,[L(P+'9.2',H,'Marwick thesis it challenges')]),
'9.4':(1,[]),
'9.5':(2,[L(P+'8.0',H,'British women gaining the vote'),L(P+'8.3',H,'French women denied the vote')]),
}
out={P+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur2-s9.t1g1.json','w'),indent=1)
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur2-s9.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith(P)]
assert list(out)==tg,(set(tg)^set(out))
assert all(n['id'] in ids and n['id']!=k for k,v in out.items() for n in v['needs'])
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
