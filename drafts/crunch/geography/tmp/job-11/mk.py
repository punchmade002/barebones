import re,json
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
txt=open(P+'packs/geo-economic-development-s3.t1g7.txt').read()
lines=txt.split('\n')
targets=[];allids=set()
inT=False
for l in lines:
    if l.startswith('TARGET'): inT=True
    elif l.startswith('CANDIDATES'): inT=False
    m=re.match(r'\[([^\]]+)\]',l)
    if m:
        allids.add(m.group(1))
        if inT: targets.append(m.group(1))
p='geo-economic-development-s3.'
c='geo-region-continental-s2.'
H,L='high','low'; E,Hp='essential','helpful'
L_={
'0.0':[(p+'0.b',E,'uses the term colonialism',H)],
'0.4':[(p+'0.b',Hp,'colony and colonial power',H)],
'0.5':[(p+'0.4',Hp,'colonies bought manufactured imports',H)],
'0.6':[(p+'0.4',Hp,'cheap raw materials for colonial power',L)],
'0.7':[(p+'0.6',Hp,'plantations growing one crop',L)],
'1.b':[(p+'0.b',Hp,'colonial rule',H)],
'1.0':[(p+'0.4',Hp,'raw materials exported to colonial power',H)],
'1.1':[(p+'1.0',Hp,'transport built to ports',H)],
'1.2':[(p+'1.0',Hp,'railways and ports as colonial infrastructure',H)],
'1.3':[(p+'1.2',E,'the debate about infrastructure benefits',H)],
'1.4':[(p+'0.3',Hp,'Europeans dividing Africa',L)],
'2.1':[(p+'0.4',Hp,'dependence on raw material exports',H)],
'2.3':[(p+'2.2',Hp,'privatising state firms',L)],
'2.4':[(p+'2.1',Hp,'dependence on few raw materials',H)],
'3.1':[(p+'3.0',E,'the East India Company',H)],
'3.2':[(p+'3.0',E,'rule transferred from the Company',H)],
'3.3':[(p+'3.2',Hp,'British rule ending',L)],
'4.b':[(p+'0.5',Hp,'colony losing its own manufacturing',H)],
'4.0':[(p+'0.5',Hp,'local industry destroyed by imports',H)],
'4.1':[(p+'4.0',E,'those Lancashire mills',H)],
'4.3':[(p+'0.7',E,'cash crops replacing food crops',H)],
'4.4':[(p+'4.3',Hp,'jute as a cash crop',H)],
'5.1':[(p+'5.0',E,'tax burden passed to peasants',H)],
'5.3':[(p+'5.2',E,'the Bengal famine',H)],
'6.b':[(p+'1.0',Hp,'colonial railways serving exports',H)],
'6.1':[(p+'1.0',Hp,'railways built for raw material export',H)],
'6.2':[(p+'6.1',Hp,'railways built for colonial needs',H)],
'6.3':[(p+'1.1',Hp,'ports growing into main cities',H)],
'6.4':[(p+'6.3',Hp,'Calcutta as colonial city',L)],
'7.3':[(p+'3.3',Hp,'Partition of 1947',H)],
'7.4':[(p+'7.3',E,'Partition as source of conflict',H)],
'7.5':[(p+'4.0',Hp,'cloth trade colonialism had built',L)],
'7.6':[(p+'7.5',Hp,'the independence movement',L)],
'8.1':[(p+'2.0',Hp,'import substitution and tariffs',H)],
'8.3':[(p+'8.0',Hp,'planned state-run economy',L)],
'8.4':[(p+'8.3',Hp,'effects of restricting competition',L)],
'9.b':[(p+'4.3',Hp,'cash crops replaced food crops',L)],
'9.1':[(p+'9.0',Hp,'Green Revolution raising output',H)],
'9.2':[(p+'9.1',Hp,'rising food-grain output',H)],
'10.b':[(p+'8.b',Hp,'state-led development',H)],
'10.1':[(p+'2.2',Hp,'IMF and debt crises',H)],
'10.2':[(p+'2.3',Hp,'liberalisation',H),(p+'8.3',Hp,'licences removed',H)],
'10.3':[(p+'2.5',Hp,'WTO',H)],
'11.b':[(p+'10.2',E,'the 1991 reforms',H)],
'11.1':[(p+'7.0',Hp,'English language aiding IT',L)],
'11.2':[(p+'10.2',Hp,'welcoming foreign investment',H)],
'11.4':[(p+'2.6',Hp,'remittances',H)],
'12.b':[(p+'11.0',Hp,'fast growth',L)],
'13.b':[(p+'0.b',Hp,'colonial rule',L)],
'13.1':[(p+'13.0',Hp,'Portuguese claim to Brazil',H)],
'13.2':[(p+'13.1',Hp,'Portuguese colonial rule',L)],
'13.4':[(p+'0.6',Hp,'plantations',L)],
'14.0':[(p+'0.6',Hp,'forced labour on plantations',H)],
'14.1':[(p+'14.0',Hp,'enslaved Africans',H)],
'14.2':[(p+'14.0',E,'legacy of slavery',H),(c+'113.0',Hp,'favelas',H)],
'14.4':[(p+'14.3',Hp,'indigenous peoples',H)],
'14.6':[(p+'14.5',E,'latifundia concentration of land',H)],
'14.7':[(p+'14.6',Hp,'unequal land ownership',H)],
'15.b':[(p+'13.b',Hp,'export cycles',H)],
'15.0':[(p+'13.4',E,'sugar as export cycle',H)],
'15.1':[(p+'13.6',Hp,'coffee wealth in South-East',L)],
'15.2':[(c+'94.0',Hp,'Northeast to Southeast migration',H)],
'15.3':[(p+'15.0',Hp,'poor North-East',L)],
'15.4':[(p+'13.6',Hp,'coffee exports',H)],
'16.b':[(p+'2.0',Hp,'import substitution',H)],
'16.1':[(p+'16.0',Hp,'state-led industrialisation',L)],
'16.3':[(c+'92.0',Hp,'Brasília opening the interior',H)],
'17.b':[(p+'16.b',Hp,'state-led industrialisation',L)],
'17.1':[(p+'2.2',Hp,'debt crisis and IMF programmes',H)],
'17.2':[(p+'17.1',E,'hyperinflation',H)],
'18.b':[(p+'2.3',Hp,'liberalisation',H)],
'18.0':[(p+'2.2',Hp,'privatising state firms',L)],
'18.1':[(p+'2.5',Hp,'regional trading blocs',H)],
'18.2':[(p+'18.b',Hp,'commodities boom',H)],
'18.3':[(p+'18.2',E,'commodity exports bought by China',H)],
'18.4':[(p+'18.2',Hp,'soya exports',H)],
'18.6':[(p+'2.4',Hp,'export diversification',H)],
'19.1':[(p+'19.0',Hp,'Bolsa Familia cutting hunger',H)],
'19.2':[(p+'12.4',Hp,'HDI definition',L)],
'19.5':[(p+'18.2',Hp,'commodity dependence',H)],
'19.6':[(p+'15.0',Hp,'North-East left poor',H)],
'20.2':[(p+'20.1',Hp,'the Mahdists',H)],
'20.3':[(p+'20.2',Hp,'British control after Omdurman',L)],
'20.4':[(p+'20.3',Hp,'rule until independence',L)],
'21.b':[(p+'0.7',Hp,'monoculture',L)],
'21.1':[(p+'21.0',E,'the Gezira Scheme',H)],
'21.2':[(p+'21.0',E,'the Gezira Scheme',H)],
'21.3':[(p+'21.0',Hp,'the Gezira Scheme',H)],
'21.4':[(p+'21.3',Hp,'cotton growing',H)],
'21.5':[(p+'21.3',Hp,'cotton export crop',H)],
'21.6':[(p+'21.0',Hp,'Gezira investment',L)],
'22.b':[(p+'20.3',Hp,'British rule of Sudan',L)],
'22.1':[(p+'22.0',E,'north and south ruled separately',H)],
'22.2':[(p+'22.0',Hp,'separate north and south',H)],
'22.3':[(p+'22.0',E,'two regions joined',H)],
'22.4':[(p+'1.4',Hp,'colonial boundaries enclosing groups',H)],
'23.b':[(p+'22.b',Hp,'colonial division',H)],
'23.3':[(p+'22.3',Hp,'north-south division',L)],
'24.b':[(p+'21.5',Hp,'dependence on cotton',H)],
'24.0':[(p+'21.5',E,'dependence on cotton',H)],
'24.2':[(p+'2.2',Hp,'IMF programmes after debt',H)],
'25.b':[(p+'23.3',Hp,'south separating',H)],
'25.2':[(p+'25.0',Hp,'oil exports',H)],
'25.3':[(p+'23.3',Hp,'South Sudan independence',H)],
'25.4':[(p+'25.3',E,'loss of oil production',H)],
'25.5':[(p+'25.0',E,'the pipeline to Port Sudan',H)],
'26.1':[(p+'2.2',Hp,'debt relief and IMF context',L)],
'27.1':[(p+'27.0',Hp,'2019 removal of al-Bashir',H)],
'27.3':[(p+'27.2',E,'the war causing displacement',H)],
'27.4':[(p+'27.3',Hp,'displacement crisis',L)],
'27.5':[(p+'27.2',Hp,'war reversing development',H)],
}
out={}
for t in targets:
    k=t[len(p):]
    out[t]={'needs':[{'id':i,'strength':s,'why':w,'confidence':cf} for i,s,w,cf in L_.get(k,[])]}
unk=set(L_)-{t[len(p):] for t in targets}
assert not unk,unk
json.dump(out,open(P+'point-links/geo-economic-development-s3.t1g7.json','w'),indent=1,ensure_ascii=False)
d=json.load(open(P+'point-links/geo-economic-development-s3.t1g7.json'))
assert list(d)==targets and len(set(targets))==len(targets)
n=lo=0
for t,v in d.items():
    for x in v['needs']:
        assert x['id'] in allids and x['id']!=t and len(x['why'].split())<=8
        n+=1; lo+=x['confidence']=='low'
print(len(d),n,lo)
