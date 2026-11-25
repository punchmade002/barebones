import json,re
def L(t,s,why,c='h'):
    return {"id":'hist-ire1-s1.'+t,"strength":{'E':'essential','H':'helpful'}[s],"why":why,"confidence":{'h':'high','l':'low'}[c]}
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[L('0.5','H','Peel as Chief Secretary')]),
'1.4':(1,[]),
'1.5':(1,[L('1.4','H','earlier county constabulary')]),
'1.6':(1,[L('1.5','H','the central armed Irish Constabulary')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[L('2.1','E','forty-shilling freeholders voting')]),
'2.3':(1,[]),'2.4':(1,[]),
'2.5':(1,[L('0.3','H','Catholic Emancipation')]),
'2.6':(2,[L('2.5','E','the veto controversy')]),
'2.7':(1,[L('2.6','E','the dispute over the veto')]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L('3.0','E','the Catholic Association')]),
'3.2':(1,[L('3.1','E','the Catholic Rent')]),
'3.3':(1,[L('3.1','H','funds from the Catholic Rent')]),
'3.4':(1,[L('3.2','H','parish network used by the Association')]),
'3.5':(1,[L('1.0','H','the grand jury system'),L('0.2','H','established Church of Ireland','l')]),
'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(1,[L('3.0','E','the growing Catholic Association')]),
'4.1':(1,[L('4.0','E','the Unlawful Societies Act')]),
'4.2':(1,[]),
'4.3':(1,[L('3.2','H','Rent organisation as election committees')]),
'4.4':(1,[L('4.3','E','the 1826 Waterford election'),L('2.1','H','forty-shilling freeholders')]),
'4.5':(1,[L('4.4','H','tenants defying landlords in Waterford')]),
'4.6':(1,[L('2.2','H','open voting and landlord control','l')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L('3.0','H','the Association deciding policy')]),
'5.2':(1,[L('2.3','E','Catholics barred by the oath')]),
'5.3':(1,[L('3.4','H','priests leading the movement')]),
'5.4':(1,[L('5.0','E','the Clare by-election')]),
'5.5':(1,[L('5.4','E','O\'Connell\'s Clare victory'),L('2.3','H','Catholics unable to take seats')]),
'5.6':(2,[L('7.4','H','Relief Act not retrospective')]),
'6.b':(1,[L('0.3','H','Catholic Emancipation')]),
'6.0':(1,[L('5.5','E','prospect after Clare')]),
'6.1':(1,[L('0.4','H','the Lord Lieutenant')]),
'6.2':(1,[L('4.2','H','Commons voting for relief','l')]),
'6.3':(1,[]),
'6.4':(2,[L('6.0','H','fear of civil strife')]),
'6.5':(1,[L('4.0','H','government suppressing the Association','l')]),
'7.b':(1,[L('6.4','H','Wellington and Peel conceding')]),
'7.0':(1,[L('2.3','E','the oath Catholics could not take')]),
'7.1':(1,[L('0.4','H','Lord Lieutenant office')]),
'7.2':(1,[]),
'7.3':(2,[L('2.1','E','forty-shilling freeholders')]),
'7.4':(1,[L('5.6','H','O\'Connell refused his Clare seat')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L('6.4','H','Peel reversing his position')]),
'8.2':(1,[]),'8.3':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),
'9.3':(1,[L('0.b','H','the Union he opposed'),L('2.5','H','anti-veto party')]),
'9.4':(1,[L('1.2','H','Dublin Corporation closed to Catholics')]),
'9.5':(1,[L('3.0','H','founding the Association'),L('3.1','H','devising the Rent'),L('5.2','H','standing in Clare')]),
'9.6':(1,[L('3.6','H','legal moral-force methods')]),
'9.7':(1,[]),
'9.8':(2,[L('7.3','H','loss of the forty-shilling vote')]),
'10.b':(1,[]),
'10.0':(2,[L('3.1','H','the Rent'),L('5.2','H','Clare candidacy')]),
'10.1':(2,[L('3.4','H','clergy organising'),L('4.3','H','Wyse winning Waterford')]),
'10.2':(1,[L('7.0','H','Catholics entering Parliament')]),
'10.3':(1,[L('7.3','E','the 10 pound franchise'),L('1.0','H','Protestant control of grand juries')]),
'10.4':(1,[]),
'10.5':(1,[L('3.5','H','tithes grievance')]),
'10.6':(1,[]),
'10.7':(2,[L('0.b','H','Repeal meaning undoing the Union')]),
}
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
txt=open(P+'packs/hist-ire1-s1.t1g1.txt').read()
tg=re.findall(r'^\[([^\]]+)\]',txt,re.M)
out={}
for t in tg:
    c,l=D[t[len('hist-ire1-s1.'):]]; out[t]={"cost":c,"needs":l}
assert len(D)==len(tg)==len(out),(len(D),len(tg))
for t,v in out.items():
    for n in v['needs']: assert n['id'] in out and n['id']!=t,(t,n)
json.dump(out,open(P+'point-links/hist-ire1-s1.t1g1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
