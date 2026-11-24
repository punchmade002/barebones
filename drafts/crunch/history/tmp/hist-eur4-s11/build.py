import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
pk=open(P+'packs/hist-eur4-s11.t1g1.txt').read()
targets=re.findall(r'^\[(hist-eur4-s11\.[^\]]+)\]',pk,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
E,H='essential','helpful'
def n(i,s,w,c='high'):return dict(id=('hist-eur4-' if i[0]=='s' else 'hist-eur4-s11.')+i,strength=s,why=w,confidence=c)
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[n('0.0',H,'John XXIII as pope')]),
'0.2':(1,[]),'0.3':(1,[]),'0.4':(2,[]),
'0.5':(1,[n('0.1',H,'the Council announced','low')]),
'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[n('0.0',H,'John XXIII as pope')]),
'1.2':(1,[n('1.1',E,'Paul VI becoming pope')]),
'1.3':(1,[]),
'1.4':(2,[n('0.7',H,'prepared drafts from the Curia')]),
'1.5':(1,[]),
'1.6':(2,[n('2.1',H,'Lumen Gentium'),n('2.4',H,'ecumenism decree')]),
'1.7':(2,[n('2.6',H,'religious liberty declaration'),n('2.5',H,'Nostra Aetate'),n('2.3',H,'Gaudium et Spes')]),
'1.8':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[]),
'3.b':(1,[]),
'3.0':(2,[n('2.0',H,'liturgy reform of Sacrosanctum Concilium')]),
'3.1':(1,[n('2.1',H,'larger role for the laity')]),
'3.2':(1,[n('2.4',H,'ecumenism commitment')]),
'3.3':(1,[n('2.5',E,'Nostra Aetate')]),
'3.4':(1,[n('3.3',H,'improved Catholic-Jewish dialogue')]),
'3.5':(1,[]),'3.6':(1,[]),
'3.7':(1,[n('2.6',H,'Dignitatis Humanae on religious liberty')]),
'4.b':(1,[]),
'4.0':(2,[n('2.6',H,'religious liberty teaching'),n('3.0',H,'the new liturgy')]),
'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),
'4.4':(2,[n('4.2',E,'Humanae Vitae encyclical')]),
'4.5':(1,[n('4.2',E,'Humanae Vitae')]),
'4.6':(2,[n('4.2',E,'Humanae Vitae ban on contraception'),n('4.4',H,'the 1966 commission and shock')]),
'4.7':(1,[]),
'5.b':(1,[]),
'5.0':(1,[n('2.3',H,'Gaudium et Spes')]),
'5.1':(1,[]),
'5.2':(1,[n('s4.1.1',H,'1979 visit to Poland')]),
'5.3':(1,[]),
'5.4':(1,[n('4.2',H,'contraception teaching')]),
'5.5':(2,[]),
'5.6':(1,[n('s4.4.b',H,'Solidarity union')]),
'5.7':(1,[]),'5.8':(2,[]),'5.9':(2,[]),'5.10':(1,[]),
'5.11':(1,[n('s4.0.b',H,'Gorbachev')]),
'6.b':(1,[]),'6.0':(2,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(2,[]),'6.4':(1,[]),
'7.b':(2,[]),
'7.0':(1,[n('3.0',H,'vernacular liturgy'),n('3.2',H,'ecumenical dialogue')]),
'7.1':(1,[n('6.0',H,'falling Mass attendance')]),
'7.2':(1,[]),
'7.3':(2,[n('6.0',H,'decline in practice')]),
'7.4':(2,[n('4.6',H,'Humanae Vitae authority gap','low'),n('1.5',H,'collegiality')]),
}
out={}
for t in targets:
    k=t.replace('hist-eur4-s11.','')
    assert k in D,k
    c,l=D[k]
    for x in l: assert x['id'] in allids and x['id']!=t,(t,x['id'])
    out[t]={'cost':c,'needs':l}
assert len(out)==len(D)==len(targets),(len(out),len(D),len(targets))
json.dump(out,open(P+'point-links/hist-eur4-s11.t1g1.json','w'),indent=1)
chk=json.load(open(P+'point-links/hist-eur4-s11.t1g1.json'))
ls=[x for v in chk.values() for x in v['needs']]
print(len(chk),len(ls),sum(v['cost']==2 for v in chk.values()),sum(x['confidence']=='low' for x in ls))
