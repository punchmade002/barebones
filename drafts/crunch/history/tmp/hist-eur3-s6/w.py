import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur3-s6.'
def L(i,s,w,c='h'): return {"id":i,"strength":{'E':'essential','H':'helpful'}[s],"why":w,"confidence":{'h':'high','l':'low'}[c]}
# ---- package 1: every id listed explicitly; links given where decided, [] otherwise
secs1={0:[0,1,2,3,4,5,6,7],1:[0,1,2,3,4,5],2:[0,1,2,3,4],3:[0,1,2,3,4],4:[0,1,2,3,4],5:[0,1,2,3,4,5],6:[0,1,2,3,4,5,6],7:[0,1,2,3,4,5,6],8:[0,1,2,3,4,5,6],9:[0,1,2,3,4,5,6],10:[0,1,2,3,4],11:[0,1,2,3,4,5,6],12:[0,1,2,3,4],13:[0,1,2,3,4],14:[0,1,2,3,4,5],15:[0,1,2],16:[0,1,2,3,4],17:[0,1,2,3,4,5,6],18:[0,1]}
ids1=[]
for s,l in secs1.items():
    ids1.append(f'{P}{s}.b'); ids1+= [f'{P}{s}.{k}' for k in l]
l1={
 '1.1':[L('hist-eur3-s3.0.2','H','Versailles terms Germany resented','l')],
 '12.2':[L('hist-eur3-s3.12.3','H','Spanish Civil War, Condor Legion','l')],
 '15.1':[L('hist-eur3-s3.12.0','E','Rhineland reoccupation of 1936')],
 '15.2':[L('hist-eur3-s3.13.3','E','Munich conference and agreement'),L('hist-eur3-s3.15.3','H','appeasement policy')],
 '16.0':[L('hist-eur3-s3.14.6','H','invasion of Poland, 1 September 1939')],
 '16.1':[L('hist-eur3-s3.14.4','E','Nazi-Soviet Pact')],
}
out1={i:{"needs":l1.get(i[len(P):],[])} for i in ids1}
# ---- package 2
def e(c,*l): return (c,list(l))
p2={
'18.2':e(1,L(P+'18.1','E','the 10 July vote')),
'18.3':e(1,L(P+'17.2','E','armistice of 22 June'),L(P+'18.1','H','the 10 July vote'),L(P+'18.2','E','Pétain made Head of State')),
'19.b':e(1),
'19.0':e(2,L(P+'14.3','E','Ardennes gamble, Maginot gaps'),L(P+'14.4','H','slow defensive doctrine')),
'19.1':e(1,L(P+'14.4','E','tanks spread among infantry')),
'19.2':e(1,L(P+'14.1','H','what the Maginot Line was'),L(P+'14.3','E','Line missed Belgium and Ardennes')),
'19.3':e(1,L(P+'19.0','H','military explanations')),
'19.4':e(1,L(P+'5.b','H','instability of governments','l')),
'19.5':e(1),
'19.6':e(1,L(P+'19.4','H','political decadence explanation'),L(P+'19.0','H','military failures')),
'20.b':e(1),
'20.0':e(1),
'20.1':e(1,L(P+'8.5','E','Doumergue government with Pétain')),
'20.2':e(1,L(P+'17.1','E','Pétain asked for armistice')),
'20.3':e(1,L(P+'35.2','H','trial and sentence of Pétain','l')),
'20.4':e(1,L(P+'20.0','E','victor of Verdun')),
'20.5':e(1,L(P+'26.b','H','collaboration')),
'21.b':e(1),
'21.0':e(1,L(P+'14.5','H','de Gaulle armoured warfare book')),
'21.1':e(1,L(P+'16.1','H','Reynaud government, 1940')),
'21.2':e(1,L(P+'31.0','H','18 June appeal'),L(P+'18.2','H','Vichy regime')),
'21.3':e(1,L(P+'21.2','H','Provisional Government')),
'21.4':e(1,L(P+'33.5','H','Resistance as a minority','l')),
'22.b':e(1,L(P+'9.2','H','Popular Front government of 1936')),
'22.0':e(1,L(P+'0.6','H','the Socialists'),L(P+'9.2','H','Blum as Prime Minister')),
'22.1':e(1,L(P+'9.4','H','first Socialist, Jewish PM'),L(P+'9.5','H','beaten up in 1936')),
'22.2':e(1,L(P+'25.3','H','the Riom trial'),L(P+'16.0','H','Gamelin','l')),
'22.3':e(1),
'23.b':e(1,L(P+'6.4','H','Laval as Third Republic PM')),
'23.0':e(1,L(P+'6.4','H','Laval as PM 1935-36')),
'23.1':e(1,L(P+'6.4','E','1935 decree-laws')),
'23.2':e(1,L(P+'26.1','E','Laval dismissed, Darlan in power')),
'23.3':e(1,L(P+'26.2','H','Laval return in 1942'),L(P+'35.2','H','Laval executed','l')),
'24.b':e(1,L(P+'18.2','H','Pétain as Head of State')),
'24.0':e(1,L(P+'18.2','H','Pétain given full powers')),
'24.1':e(1,L(P+'17.3','E','occupied and unoccupied zones'),L(P+'18.0','H','government settled at Vichy')),
'24.2':e(1),
'24.3':e(1,L(P+'24.b','H','National Revolution')),
'24.4':e(1,L(P+'24.b','H','National Revolution'),L(P+'9.2','H','the Popular Front')),
'24.5':e(1),
'24.6':e(1,L(P+'24.b','H','National Revolution')),
'25.b':e(1,L(P+'24.b','H','Vichy regime and aims')),
'25.0':e(1,L(P+'10.3','E','union rights won in 1936'),L(P+'10.4','H','1936 social laws')),
'25.1':e(1),
'25.2':e(1,L(P+'31.0','H','de Gaulle 18 June appeal')),
'25.3':e(1,L(P+'22.2','H','Riom trial')),
'26.b':e(1,L(P+'28.b','H','collaborationism')),
'26.0':e(1),
'26.1':e(1,L(P+'23.0','H','Laval as Prime Minister')),
'26.2':e(1,L(P+'23.0','H','Laval as head of government')),
'26.3':e(1,L(P+'17.5','H','fleet kept by France')),
'26.4':e(2,L(P+'17.6','H','prisoners of war in Germany'),L(P+'24.b','H','National Revolution')),
'26.5':e(1,L(P+'26.4','H','Vichy motives for collaboration')),
'27.b':e(1),
'27.0':e(1,L(P+'17.4','E','occupation costs of 400 million francs')),
'27.1':e(1),
'27.2':e(1,L(P+'17.6','H','prisoners taken in 1940')),
'27.3':e(1,L(P+'17.6','H','release of prisoners','l')),
'27.4':e(1,L(P+'17.3','E','the southern unoccupied zone')),
'27.5':e(1,L(P+'17.5','E','fleet kept by France'),L(P+'27.4','H','German occupation of the south')),
'28.b':e(1,L(P+'26.b','H','collaboration versus collaborationism')),
'28.0':e(1,L(P+'26.b','H','Vichy collaboration')),
'28.1':e(1,L(P+'0.6','H','the Communist party (PCF)')),
'28.2':e(1),
'28.3':e(1),
'29.b':e(1),
'29.0':e(1),
'29.1':e(2,L(P+'29.0','H','first Statute on Jews')),
'29.2':e(1,L(P+'17.3','H','the two zones')),
'29.3':e(1,L(P+'29.2','H','police arrests of Jews')),
'29.4':e(1,L(P+'29.3','E','Vel d Hiv round-up')),
'29.5':e(1,L(P+'29.2','H','deportations of Jews')),
'30.b':e(1),
'30.0':e(1,L(P+'33.0','H','the maquis')),
'30.1':e(1,L(P+'30.0','E','the Milice')),
'30.2':e(1,L(P+'27.3','E','the failed relève')),
'30.3':e(1,L(P+'33.0','H','the maquis'),L(P+'30.2','E','the STO')),
'30.4':e(1,L(P+'29.2','H','police arrests and deportations')),
'30.5':e(1,L(P+'26.5','E','Vichy as a shield')),
'31.b':e(1),
'31.0':e(1,L(P+'21.1','H','de Gaulle in Reynaud government')),
'31.1':e(1,L(P+'31.0','E','de Gaulle and the Free French')),
'31.2':e(1,L(P+'31.1','H','Free French')),
'31.3':e(1,L(P+'31.2','H','Free French leadership')),
'31.4':e(1,L(P+'31.3','H','Giraud rivalry','l')),
'32.b':e(1),
'32.0':e(1),
'32.1':e(2,L(P+'32.0','H','early resistance groups')),
'32.2':e(1,L(P+'0.6','H','the Communists')),
'32.3':e(1),
'32.4':e(1,L(P+'31.0','H','Gaullists'),L(P+'32.2','H','Communist resistance')),
'32.5':e(1,L(P+'31.0','H','de Gaulle as leader')),
'32.6':e(1,L(P+'32.5','E','Jean Moulin and the Council')),
'33.b':e(1),
'33.0':e(1,L(P+'30.2','E','the STO')),
'33.1':e(1,L(P+'34.0','H','Normandy landings'),L(P+'33.0','H','the maquis')),
'33.2':e(1,L(P+'30.0','H','the Milice')),
'33.3':e(2),
'33.4':e(1),
'33.5':e(1,L(P+'26.b','H','collaboration','l')),
'34.b':e(1),
'34.0':e(1),
'34.1':e(1,L(P+'31.1','H','Free French forces')),
'34.2':e(1,L(P+'31.4','E','Provisional Government')),
'34.3':e(1,L(P+'31.4','E','Provisional Government'),L(P+'32.4','H','Gaullists and Communists')),
'35.b':e(1),
'35.0':e(1,L(P+'26.b','H','collaborators')),
'35.1':e(1,L(P+'35.0','H','the épuration')),
'35.2':e(1,L(P+'20.3','H','Pétain tried'),L(P+'23.3','H','Laval executed')),
'35.3':e(1,L(P+'0.1','H','women had no vote')),
'35.4':e(1,L(P+'31.4','H','Provisional Government')),
'36.b':e(1,L(P+'21.4','H','Gaullist myth')),
'36.0':e(1,L(P+'26.5','E','shield argument')),
'36.1':e(1,L(P+'30.5','E','Paxton on active collaboration'),L(P+'29.0','H','home-grown anti-Jewish laws')),
'36.2':e(1,L(P+'21.4','E','Gaullist myth of resistance'),L(P+'36.1','H','Paxton')),
'36.3':e(1,L(P+'36.2','H','myth and memory of Vichy')),
'36.4':e(1,L(P+'29.3','E','Vel d Hiv round-up')),
'37.b':e(1),
'37.0':e(2,L(P+'4.3','E','Poincaré stabilised franc'),L(P+'8.4','H','6 February 1934 riot'),L(P+'6.b','H','French Depression','l')),
'37.1':e(2,L(P+'5.2','H','frequent government changes'),L(P+'6.3','H','slow Depression response'),L(P+'14.4','H','army doctrine')),
'37.2':e(1,L(P+'10.4','E','paid holidays and 40-hour week')),
'37.3':e(2,L(P+'13.3','E','40-hour week undone'),L(P+'12.2','E','Spanish Civil War split')),
'37.4':e(1,L(P+'26.5','E','Pétain as shield'),L(P+'17.2','H','the armistice')),
'37.5':e(1,L(P+'29.0','E','anti-Jewish statute beyond German demands'),L(P+'30.5','H','active collaboration')),
'37.6':e(1,L(P+'34.3','H','Republic restored in 1944')),
'37.7':e(2,L(P+'4.3','H','financial stabilisation'),L(P+'10.4','H','social reform'),L(P+'5.2','H','instability'),L(P+'14.4','H','defence failures')),
}
ids2=[P+k for k in p2]
out2={P+k:{"cost":c,"needs":l} for k,(c,l) in p2.items()}
for pk,ids,out,fn in [('t1g3',ids1,out1,'hist-eur3-s6.t1g3'),('t2g1',list(ids2),out2,'hist-eur3-s6.t2g1')]:
    txt=open(B+f'packs/{fn}.txt').read()
    pk_ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tgt=set(re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M))
    assert set(out)==tgt and len(out)==len(tgt),(set(out)^tgt)
    assert list(out)==ids
    links=0;low=0;c2=0
    for k,v in out.items():
        for n in v['needs']:
            assert n['id'] in pk_ids and n['id']!=k,(k,n)
            links+=1; low+=n['confidence']=='low'
        c2+= v.get('cost')==2
    json.dump(out,open(B+f'point-links/{fn}.json','w'),indent=1,ensure_ascii=False)
    json.load(open(B+f'point-links/{fn}.json'))
    print(fn,len(out),links,c2,low)
