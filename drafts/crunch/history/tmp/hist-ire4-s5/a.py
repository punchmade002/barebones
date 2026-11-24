import json,re
P='hist-ire4-s5.'
E,H='essential','helpful'
def n(i,s,w,c='high'):return {"id":i if i.startswith('hist') else P+i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(2,[]),'0.3':(1,[]),
'0.4':(1,[n('0.3',E,'uses Lincoln Gaol imprisonment')]),
'0.5':(1,[n('0.2',H,'uses the Dáil')]),
'0.6':(2,[n('hist-ire4-s4.4.4',H,'Philadelphia Race Convention 1919')]),
'0.7':(1,[n('0.2',H,'uses the Dáil')]),
'0.8':(2,[]),
'1.b':(1,[]),'1.0':(1,[n('0.4',H,'introduces Harry Boland')]),
'1.1':(2,[n('1.0',H,'arrival in New York')]),
'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),
'1.5':(1,[n('0.2',H,'uses the Dáil')]),
'1.6':(1,[]),'1.7':(1,[]),'1.8':(1,[]),
'2.b':(1,[]),'2.0':(1,[n('0.2',H,'uses the Dáil')]),
'2.1':(1,[n('2.0',H,'the bond drive')]),
'2.2':(1,[]),
'2.3':(1,[n('3.1',H,'quarrel over control of funds','low')]),
'2.4':(2,[n('2.0',E,'the bond drive'),n('7.2',H,'Collins as Minister for Finance','low')]),
'2.5':(1,[n('2.1',H,'money raised by the drive')]),
'3.b':(1,[n('3.0',H,'Devoy and Cohalan')]),
'3.0':(1,[n('hist-ire4-s4.4.1',E,'founding of Friends of Irish Freedom')]),
'3.1':(1,[n('3.0',E,'Devoy, Cohalan, Friends of Irish Freedom')]),
'3.2':(1,[n('3.0',E,'Devoy and Cohalan organisation')]),
'3.3':(2,[n('3.0',H,'Devoy and Cohalan camp'),n('1.0',H,'Boland organised American side')]),
'3.4':(1,[n('3.1',H,'the split over control'),n('6.0',H,'de Valera\'s new organisation')]),
'3.5':(1,[]),
'4.b':(1,[]),'4.0':(2,[]),
'4.1':(2,[n('4.0',E,'the Westminster Gazette interview')]),
'4.2':(1,[n('4.0',E,'the interview'),n('3.0',H,'Cohalan and Devoy')]),
'4.3':(1,[n('4.0',E,'the interview')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[n('5.0',E,'the two conventions')]),
'5.2':(1,[n('5.1',H,'platform request at conventions')]),
'5.3':(1,[n('5.2',H,'failure at the conventions','low')]),
'5.4':(1,[n('0.7',E,'Wilson refused Irish self-determination')]),
'6.b':(1,[]),
'6.0':(1,[n('hist-ire4-s4.4.1',H,'Friends of Irish Freedom')]),
'6.1':(1,[n('6.0',E,'the AARIR')]),
'6.2':(1,[n('7.3',H,'British reprisals in Ireland')]),
'6.3':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[n('0.2',H,'the Dáil')]),
'7.2':(2,[n('7.0',H,'the Anglo-Irish War')]),
'7.3':(2,[n('7.0',H,'the Anglo-Irish War')]),
'7.4':(2,[n('7.0',H,'the Anglo-Irish War')]),
'7.5':(1,[n('7.3',H,'uses the Auxiliaries','low')]),
'7.6':(1,[n('hist-ire4-s4.5.0',H,'Government of Ireland Act and partition')]),
'7.7':(1,[n('7.6',E,'the Government of Ireland Act'),n('1.0',H,'Boland in America')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[n('2.b',H,'the bond drive')]),
'8.2':(1,[]),
'8.3':(1,[n('3.4',H,'the split'),n('6.0',E,'the AARIR')]),
'8.4':(2,[n('7.2',E,'Collins running the war')]),
'8.5':(2,[n('8.0',H,'no recognition won')]),
'8.6':(1,[n('6.0',E,'the AARIR')]),
'9.0':(2,[n('2.1',H,'five million dollars raised')]),
'9.1':(1,[n('8.0',H,'no recognition'),n('3.b',H,'the split in Irish America')]),
'9.2':(1,[]),'9.3':(1,[]),
'9.4':(2,[n('8.0',H,'recognition never granted','low')]),
}
src=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-ire4-s5.t1g1.txt').read()
tgt=re.findall(r'^\[(hist-ire4-s5\.[^\]]+)\]',src,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',src,re.M))
out={}
for t in tgt:
    c,nd=d[t[len(P):]]
    for x in nd:
        assert x['id'] in ids and x['id']!=t,(t,x)
    out[t]={"cost":c,"needs":nd}
assert len(out)==len(d)==len(tgt),(len(out),len(d),len(tgt))
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-ire4-s5.t1g1.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
