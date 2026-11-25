import json,re
P='hist-eur5-s7.'
def L(i,s,w,c='high'):
    if not i.startswith('hist-'): i=P+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(2,[]),
'0.4':(1,[L('0.3',H,'terms of trade, commodity prices')]),
'0.5':(1,[]),
'0.6':(1,[L('0.2',H,'colonial control of trade')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[L('1.0',E,'EEC association of colonies')]),
'1.2':(2,[L('1.1',H,'earlier Yaoundé trade agreement')]),
'1.3':(1,[L('1.2',E,'Lomé I terms')]),
'1.4':(1,[L('1.2',E,'Lomé I fund')]),
'1.5':(1,[L('1.2',E,'Lomé I and later Conventions')]),
'1.6':(2,[L('1.2',E,'Lomé I and II')]),
'2.0':(1,[]),
'2.1':(1,[]),
'2.2':(1,[L('2.1',E,'1970s borrowing and oil costs')]),
'2.3':(2,[L('2.0',H,'IMF and World Bank lending')]),
'2.4':(2,[L('2.3',E,'structural adjustment programmes')]),
'2.5':(1,[L('2.3',H,'IMF-backed adjustment programme')]),
'3.0':(1,[]),
'3.1':(1,[L('3.0',H,'bilateral aid')]),
'3.2':(1,[]),
'3.3':(1,[L('hist-eur5-s5.4.0',H,'Mobutu in Zaire','low')]),
'3.4':(1,[]),
'3.5':(1,[L('3.0',H,'aid given by rich countries')]),
'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(2,[L('hist-eur5-s5.1.4',E,'Biafran War')]),
'4.1':(2,[L('4.0',E,'Biafran famine relief')]),
'4.2':(2,[]),
'4.3':(2,[]),
'4.4':(2,[L('4.3',E,'Ethiopian famine 1984')]),
'4.5':(1,[L('3.0',H,'food aid','low')]),
'4.6':(1,[L('4.3',E,'Ethiopian famine and government')]),
'5.0':(1,[]),
'5.1':(1,[L('5.0',H,'what NGOs are')]),
'5.2':(1,[L('hist-eur5-s5.1.4',E,'Biafran famine')]),
'5.3':(1,[L('5.0',H,'what NGOs are')]),
'5.4':(1,[L('5.0',H,'what NGOs are')]),
'5.5':(1,[L('5.3',H,'Trocaire founding')]),
'5.6':(1,[L('hist-eur5-s5.1.4',H,'Biafra relief')]),
'6.b':(1,[L('hist-eur5-s5.5.b',H,'Nyerere and Tanzania')]),
'6.0':(2,[L('hist-eur5-s5.5.4',H,'Tanzania formed 1964')]),
'6.1':(1,[L('6.0',E,'Arusha Declaration and ujamaa')]),
'6.2':(2,[L('6.0',E,'ujamaa policy')]),
'6.3':(2,[L('6.2',E,'villagisation')]),
'6.4':(1,[]),
'6.5':(1,[L('6.3',H,'collapse of socialist policies'),L('2.3',H,'IMF programme conditions','low')]),
'6.6':(2,[L('6.3',H,'collapse of farm output')]),
'6.7':(1,[]),'6.8':(1,[]),
'7.b':(1,[]),
'7.0':(1,[L('5.0',H,'NGOs such as Concern')]),
'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'7.4':(1,[L('5.0',H,'NGO campaigns')]),
'7.5':(1,[]),'7.6':(1,[]),'7.7':(1,[]),
'8.0':(1,[L('1.3',E,'Lomé preferential access')]),
'8.1':(1,[L('8.0',E,'Lomé trade preferences'),L('0.4',H,'commodity dependence and price falls')]),
'8.2':(1,[]),
'8.3':(1,[L('2.3',H,'structural adjustment cuts')]),
'8.4':(1,[L('6.4',E,'Tanzania literacy gains')]),
'8.5':(1,[L('6.2',E,'villagisation')]),
'8.6':(2,[L('0.3',H,'colonial economic structures'),L('2.4',H,'the Berg Report')]),
}
out={P+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
json.dump(out,open('point-links/hist-eur5-s7.t1g1.json','w'),indent=1)
pk=open('packs/hist-eur5-s7.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=re.findall(r'^\[(hist-eur5-s7\.[^\]]+)\]',pk,re.M)
assert list(out)==tg,set(tg)^set(out)
for k,v in out.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=k,n
a=[n for v in out.values() for n in v['needs']]
print(len(out),len(a),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in a))
