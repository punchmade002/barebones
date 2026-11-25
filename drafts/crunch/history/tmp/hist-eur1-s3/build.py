import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur1-s3.'
def L(i,s,w,c='high'): return (i,{'e':'essential','h':'helpful'}[s],w,{'H':'high','L':'low'}[c])
S3='hist-eur1-s3.'
def t(x): return S3+x
# pack 1: id -> (cost, links)
d1={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[L('hist-eur1-s2.5.0','h','the Frankfurt Parliament','H')]),
'0.2':(1,[L(t('0.1'),'e','Frankfurt failure and refused crown','H')]),
'0.3':(2,[L('hist-eur1-s2.11.1','h','Olmütz and the Erfurt Union','H')]),
'0.4':(1,[L(t('6.4'),'h','1866 exclusion of Austria','L')]),
'1.b':(1,[]),
'1.0':(1,[L('hist-eur1-s1.17.1','h','the Zollverein customs union','H')]),
'1.1':(1,[L(t('1.0'),'e','the Zollverein','H')]),
'1.2':(1,[]),
'1.3':(1,[L(t('1.2'),'h','Ruhr coal and iron','H')]),
'1.4':(2,[L(t('1.0'),'e','the Zollverein','H')]),
'1.5':(1,[]),
'1.6':(1,[L('hist-eur1-s1.4.0','h','Austria holding Lombardy-Venetia','H')]),
'1.7':(1,[]),
'1.8':(1,[L(t('2.0'),'h','William I','H'),L(t('0.0'),'h','the German Confederation','H')]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(2,[L(t('2.2'),'h','Roon as War Minister','H')]),
'2.2':(1,[]),
'2.3':(1,[L(t('2.1'),'e','the army reform being opposed','H')]),
'2.4':(1,[L(t('2.3'),'e','the budget deadlock','H')]),
'2.5':(1,[L(t('2.3'),'e','the deadlock Bismarck was to break','H')]),
'3.b':(1,[]),
'3.0':(1,[L(t('2.5'),'h','Bismarck as Minister-President','H'),L(t('0.1'),'h','the mistake of 1848-49','H')]),
'3.1':(1,[L(t('3.0'),'e','the blood and iron speech','H')]),
'3.2':(1,[L(t('3.0'),'e','the blood and iron speech','H'),L(t('2.1'),'h','the army reform','L')]),
'3.3':(2,[L(t('2.3'),'e','the budget refusal','H')]),
'3.4':(1,[L(t('3.3'),'e','the gap theory budget conflict','H'),L(t('7.0'),'h','the Indemnity Bill','H')]),
'4.b':(1,[]),
'4.0':(1,[L('hist-eur1-s2.7.0','h','Schleswig and Holstein','H'),L(t('0.0'),'h','the Confederation','L')]),
'4.1':(2,[L(t('4.0'),'e','Schleswig and Holstein','H'),L('hist-eur1-s2.7.6','h','London Protocol of 1852','L')]),
'4.2':(2,[L(t('4.1'),'h','the Danish crisis','H'),L(t('0.0'),'h','the Diet','L')]),
'4.3':(1,[L(t('4.1'),'e','the crisis causing invasion','H')]),
'4.4':(1,[L(t('4.3'),'e','the war with Denmark','H')]),
'4.5':(2,[L(t('4.4'),'e','joint rule of the duchies','H')]),
'5.b':(1,[]),
'5.0':(1,[L(t('1.7'),'e','Austria losing Russia in Crimea','H')]),
'5.1':(1,[]),
'5.2':(1,[L('hist-eur1-s1.4.0','h','Venetia held by Austria','H')]),
'5.3':(1,[L(t('4.5'),'e','the Gastein arrangements','H'),L(t('0.0'),'h','the Diet','L')]),
'5.4':(1,[L(t('5.3'),'h','the Diet mobilising','L')]),
'6.b':(1,[]),
'6.0':(1,[L(t('2.2'),'e','Moltke the chief of staff','H')]),
'6.1':(1,[L(t('5.4'),'h','the states fighting Prussia','L')]),
'6.2':(1,[L(t('5.2'),'e','Italy promised Venetia','H')]),
'6.3':(1,[L(t('6.1'),'e','the Königgrätz victory','H')]),
'6.4':(2,[L(t('0.0'),'h','the German Confederation','H'),L(t('5.2'),'h','Venetia for Italy','L')]),
'6.5':(1,[L(t('5.4'),'h','states that sided with Austria','H')]),
'6.6':(1,[L(t('5.4'),'h','southern states siding with Austria','L')]),
'7.b':(1,[]),
'7.0':(1,[L(t('3.4'),'e','years without an approved budget','H')]),
'7.1':(1,[L(t('7.0'),'e','the Indemnity Bill','H')]),
'7.2':(1,[L(t('7.1'),'e','the liberal split','H'),L(t('2.3'),'h','the Progressives','H')]),
'8.b':(1,[]),
'8.0':(1,[L(t('6.4'),'h','Prussia after 1866 settlement','L')]),
'8.1':(2,[L(t('8.0'),'e','the North German Confederation','H')]),
'8.2':(1,[L(t('8.0'),'e','the North German Confederation','H')]),
'8.3':(2,[L(t('8.0'),'e','North German Confederation north of Main','H'),L(t('6.6'),'h','southern states tied to Prussia','L')]),
'9.b':(1,[]),
'9.0':(2,[L(t('6.1'),'h','Sadowa (Königgrätz)','H')]),
'9.1':(1,[L(t('9.0'),'h','French fear of Prussia','L')]),
'9.2':(1,[L(t('9.1'),'e','Leopold\'s candidature','H')]),
'9.3':(1,[L(t('9.2'),'e','the guarantee demanded','H')]),
'9.4':(1,[L(t('9.3'),'e','the Ems meeting report','H')]),
'9.5':(1,[L(t('9.4'),'e','the Ems telegram','H'),L(t('6.6'),'h','the southern states\' treaties','H')]),
'9.6':(1,[L(t('9.3'),'h','Benedetti','H')]),
'10.b':(1,[]),
'10.0':(1,[L(t('9.5'),'e','the war with France','H')]),
'10.1':(1,[L(t('10.0'),'h','the early French defeats','L')]),
'10.2':(2,[L(t('10.1'),'e','Sedan and Napoleon III\'s surrender','H')]),
'10.3':(2,[L(t('10.0'),'e','Bazaine shut in Metz','H'),L(t('10.2'),'h','the Government of National Defence','H')]),
'10.4':(1,[L(t('6.0'),'h','Moltke\'s planning','H'),L(t('9.6'),'h','France without allies','L')]),
'11.b':(1,[]),
'11.0':(1,[L(t('6.6'),'h','the southern states\' alliances','L')]),
'11.1':(1,[L(t('11.0'),'e','Bavaria joining the union','H')]),
'11.2':(1,[L(t('11.1'),'e','the Kaiserbrief offer','H'),L(t('10.3'),'h','the siege of Paris context','L')]),
'11.3':(1,[L(t('11.2'),'e','the proclamation at Versailles','H')]),
'11.4':(2,[L(t('10.3'),'h','the end of the war','H')]),
'12.b':(1,[]),
'12.0':(1,[L(t('8.1'),'e','the 1867 constitution','H')]),
'12.1':(1,[L(t('8.1'),'h','Prussian king\'s powers in 1867','H')]),
'12.2':(1,[L(t('8.2'),'e','Reichstag and manhood suffrage','H')]),
'12.3':(2,[L(t('8.2'),'e','the Bundesrat','H')]),
'12.4':(2,[L('hist-eur1-s2.8.6','e','the three-class franchise','H')]),
'13.b':(1,[]),
'13.0':(1,[L('hist-eur1-s2.2.5','h','the United Diet of 1847','H')]),
'13.1':(2,[L('hist-eur1-s2.11.3','h','Bismarck as delegate at Frankfurt','H'),L(t('2.5'),'h','becoming Minister-President','H')]),
'13.2':(1,[L(t('3.0'),'e','the blood and iron speech','H'),L(t('3.3'),'e','the gap theory','H')]),
'13.3':(2,[L(t('4.3'),'e','the Danish War','H'),L(t('4.5'),'e','the Gastein settlement','H'),L(t('5.2'),'e','the alliance with Italy','H'),L(t('6.4'),'e','the Treaty of Prague','H'),L(t('8.0'),'e','the North German Confederation','H'),L(t('9.4'),'e','the Ems telegram','H')]),
'13.4':(1,[L(t('8.1'),'h','Chancellor of the Confederation','H'),L(t('12.0'),'h','the imperial constitution','L')]),
'13.5':(1,[L(t('7.2'),'e','the National Liberal Party','H')]),
'13.6':(2,[L(t('14.5'),'h','plan versus improviser debate','H')]),
'13.7':(1,[L(t('8.2'),'h','manhood suffrage','L')]),
'14.b':(1,[]),
'14.0':(1,[]),
'14.1':(1,[L(t('14.0'),'h','Realpolitik','L')]),
'14.2':(2,[L(t('5.0'),'e','the Alvensleben Convention','H'),L(t('5.1'),'e','Biarritz neutrality','H'),L(t('5.2'),'e','the Italian alliance','H'),L(t('9.6'),'e','France left with no ally','H')]),
'14.3':(1,[L(t('6.3'),'e','the moderate peace with Austria','H')]),
'14.4':(2,[L(t('4.1'),'e','the Danish succession crisis','H'),L(t('4.5'),'e','the Gastein arrangement','H'),L(t('9.1'),'e','the Hohenzollern candidature','H'),L(t('9.4'),'e','the Ems telegram','H')]),
'14.5':(2,[L(t('13.6'),'e','the Prussian school and Taylor','H')]),
'14.6':(1,[L(t('14.5'),'e','the plan versus improviser debate','H')]),
'15.b':(1,[]),
'15.0':(2,[L(t('5.2'),'h','Venetia added in 1866','L')]),
'15.1':(1,[L(t('15.0'),'h','Italian unification','L')]),
'15.2':(1,[L(t('6.2'),'e','Custoza and Lissa','H'),L(t('5.2'),'h','Venetia promised to Italy','H')]),
'15.3':(1,[L(t('5.1'),'h','Napoleon III\'s neutrality','H')]),
'15.4':(1,[L(t('11.1'),'h','the princes\' role','L')]),
'15.5':(1,[]),
'15.6':(2,[L(t('0.4'),'h','Kleindeutsch excluding Austria','H'),L(t('4.4'),'h','Schleswig and Denmark','L')]),
'16.b':(1,[]),
'16.0':(1,[L('hist-eur1-s2.2.3','h','liberals\' nation-state aim of 1848','L')]),
'16.1':(1,[L(t('0.1'),'e','failure of parliamentary unity','H')]),
'16.2':(1,[L(t('0.4'),'e','Kleindeutsch','H')]),
'16.3':(2,[L(t('12.2'),'e','Reichstag and Chancellor powers','H')]),
'16.4':(1,[L(t('16.0'),'h','achievement of unity','L')]),
'16.5':(1,[L(t('12.4'),'h','Prussian conservative dominance','L')]),
}
# pack 2: links to s4 only
d2={k:[] for k in d1}  # placeholder replaced below by explicit dict
d2={
'0.b':[],'0.0':[],'0.1':[],'0.2':[],'0.3':[],'0.4':[],
'1.b':[],'1.0':[],'1.1':[],'1.2':[],'1.3':[],'1.4':[],'1.5':[],
'1.6':[L('hist-eur1-s4.10.1','h','Magenta and Solferino 1859','H')],
'1.7':[L('hist-eur1-s4.8.6','h','Austria losing Russia in Crimea','H')],
'1.8':[],
'2.b':[],'2.0':[],'2.1':[],'2.2':[],'2.3':[],'2.4':[],'2.5':[],
'3.b':[],'3.0':[],'3.1':[],'3.2':[],'3.3':[],'3.4':[],
'4.b':[],'4.0':[],'4.1':[],'4.2':[],'4.3':[],'4.4':[],'4.5':[],
'5.b':[],
'5.0':[L('hist-eur1-s4.8.6','h','Austria lost Russian friendship','H')],
'5.1':[L('hist-eur1-s4.9.1','h','Napoleon III\'s aims','L')],
'5.2':[L('hist-eur1-s4.12.1','h','Italy allying with Prussia 1866','H')],
'5.3':[],'5.4':[],
'6.b':[],'6.0':[],'6.1':[],
'6.2':[L('hist-eur1-s4.12.1','h','Custoza, Lissa and Venetia','H')],
'6.3':[],
'6.4':[L('hist-eur1-s4.12.2','h','Venetia handed via Napoleon III','H')],
'6.5':[],'6.6':[],
'7.b':[],'7.0':[],'7.1':[],'7.2':[],
'8.b':[],'8.0':[],'8.1':[],'8.2':[],'8.3':[],
'9.b':[],'9.0':[],'9.1':[],'9.2':[],'9.3':[],'9.4':[],'9.5':[],'9.6':[],
'10.b':[],'10.0':[],'10.1':[],'10.2':[],'10.3':[],'10.4':[],
'11.b':[],'11.0':[],'11.1':[],'11.2':[],'11.3':[],'11.4':[],
'12.b':[],'12.0':[],'12.1':[],'12.2':[],'12.3':[],'12.4':[],
'13.b':[],'13.0':[],'13.1':[],'13.2':[],
'13.3':[L('hist-eur1-s4.12.1','h','the 1866 alliance with Italy','L')],
'13.4':[],'13.5':[],'13.6':[],'13.7':[],
'14.b':[],'14.0':[],'14.1':[],
'14.2':[L('hist-eur1-s4.12.1','h','the 1866 Italian alliance','L')],
'14.3':[],'14.4':[],'14.5':[],'14.6':[],
'15.b':[],
'15.0':[L('hist-eur1-s4.11.6','h','Kingdom of Italy proclaimed 1861','H'),L('hist-eur1-s4.12.2','h','Venetia added 1866','H'),L('hist-eur1-s4.12.4','h','capture of Rome 1870','H')],
'15.1':[L('hist-eur1-s4.13.4','h','Piedmont as leading state','H'),L('hist-eur1-s4.13.5','h','Piedmont\'s war and diplomacy','L')],
'15.2':[L('hist-eur1-s4.12.1','h','Custoza, Lissa and Venetia','H'),L('hist-eur1-s4.12.3','h','French garrison leaving Rome','H')],
'15.3':[L('hist-eur1-s4.9.3','h','French help against Austria 1859','H')],
'15.4':[L('hist-eur1-s4.11.2','h','Garibaldi\'s volunteers','H'),L('hist-eur1-s4.10.5','h','plebiscites','H')],
'15.5':[],'15.6':[],
'16.b':[],'16.0':[],'16.1':[],'16.2':[],'16.3':[],'16.4':[],'16.5':[],
}
def targets(f):
    ids=[]
    for l in open(B+'packs/'+f):
        if l.startswith('CANDIDATES'): break
        m=re.match(r'\[(hist-eur1-s3\.[^\]]+)\]',l)
        if m: ids.append(m.group(1))
    return ids
def allids(f):
    return set(re.findall(r'^\[([^\]]+)\]',open(B+'packs/'+f).read(),re.M))
def fmt(ls): return [{'id':i,'strength':s,'why':w,'confidence':c} for i,s,w,c in ls]
for name in ('t1g1','t1g2'):
    f='hist-eur1-s3.%s.txt'%name
    tg=targets(f); a=allids(f)
    out={}
    for i in tg:
        k=i.split('s3.')[1]
        if name=='t1g1': c,ls=d1[k]; out[i]={'cost':c,'needs':fmt(ls)}
        else: out[i]={'needs':fmt(d2[k])}
    assert set(d1)==set(k.split('s3.')[1] for k in tg)==set(d2), (set(d1)^set(d2))
    for i,v in out.items():
        for n in v['needs']:
            assert n['id'] in a and n['id']!=i,(i,n)
    json.dump(out,open(B+'point-links/hist-eur1-s3.%s.json'%name,'w'),ensure_ascii=False)
    j=json.load(open(B+'point-links/hist-eur1-s3.%s.json'%name))
    nl=sum(len(v['needs']) for v in j.values())
    lo=sum(n['confidence']=='low' for v in j.values() for n in v['needs'])
    c2=sum(v.get('cost')==2 for v in j.values())
    print(name,len(j),nl,c2 if name=='t1g1' else '-',lo)
