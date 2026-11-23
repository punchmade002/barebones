import json,re
B='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(B+'points/bio22-s2.txt').read()
tg=txt.split('CANDIDATES')[0]
targets=re.findall(r'^\[(\S+?)\]',tg,re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
P='bio22-s2.'
# id suffix: (cost, [(need, E/H, why, H/L)])
S={
'1.4':(1,[('1.3','E','mucus trapping microorganisms','h')]),
'2.3':(1,[('s1.0.1','H','harmless microorganisms','l')]),
'3.1':(1,[('3.0','H','phagocytes defined','h')]),
'3.2':(1,[('3.0','E','phagocyte engulfs pathogens','h')]),
'3.5':(1,[('3.4','E','vesicle','h')]),
'3.7':(2,[('3.4','H','vesicle stage','h')]),
'4.0':(2,[]),'4.1':(1,[('4.0','E','histamine effects on vessels','h')]),
'4.2':(1,[('3.0','H','phagocytes','h')]),'4.3':(2,[]),
'4.4':(1,[('4.3','H','raised body temperature','h')]),
'5.0':(1,[('3.0','H','phagocytes engulf','h')]),
'5.1':(1,[('s1.4.b','H','viruses','l')]),
'5.2':(1,[('s5.2.0','H','natural killer cells','h')]),
'6.0':(1,[('0.1','H','self vs foreign markers','h')]),
'6.1':(1,[('6.0','E','antigen','h')]),'6.2':(1,[('6.0','E','antigen','h')]),
'7.0':(1,[('6.0','E','antigen','h')]),'7.1':(1,[('7.0','E','antibody structure','h')]),
'7.2':(2,[('7.1','E','chains of antibody','h')]),
'7.3':(2,[('7.2','E','antigen-binding site','h')]),
'7.4':(2,[('7.2','E','antibody regions','h')]),
'8.0':(1,[('7.2','E','two binding sites','h')]),
'8.1':(1,[('7.3','H','antibody specificity','l')]),
'8.2':(1,[('3.0','E','phagocytes','h'),('7.2','H','constant region','l')]),
'8.3':(1,[('5.0','E','complement','h')]),
'9.1':(1,[('7.0','E','antibodies','h')]),
'9.2':(1,[('9.0','H','lymphocytes','h')]),
'9.3':(2,[('9.1','E','B cells make antibodies','h')]),
'9.4':(2,[('9.3','E','B cell receptors','h')]),
'9.5':(1,[('9.4','E','clone of selected B cells','h')]),
'9.6':(1,[('9.5','E','plasma cells','h')]),'9.7':(1,[('9.5','E','memory B cells','h')]),
'10.0':(2,[('9.4','E','clonal selection','h')]),
'10.1':(1,[('10.0','E','delay in primary response','h')]),
'10.2':(2,[('9.7','E','memory cells','h')]),
'10.3':(1,[('10.2','E','secondary response','h')]),
'10.4':(2,[('10.2','E','primary vs secondary','h')]),
'11.0':(1,[('9.2','H','T cells','h')]),
'11.1':(1,[('11.0','H','cell-mediated response','h')]),
'11.2':(1,[('11.0','H','cell-mediated response','h')]),
'11.3':(2,[('0.1','E','self-marker proteins','h')]),
'11.4':(1,[('11.3','E','antigen presentation','h'),('3.0','H','engulfing pathogen','l')]),
'11.5':(1,[('11.3','E','antigen presentation','h')]),
'12.0':(2,[('11.3','E','antigen presentation','h')]),
'12.1':(1,[('12.0','H','helper T cells','h')]),
'12.2':(1,[('12.1','E','cytokines','h')]),
'12.3':(1,[('9.5','H','plasma and memory cells','h')]),
'12.4':(1,[('3.1','H','macrophages','l')]),
'12.5':(1,[('12.1','H','cytokine signalling','l')]),
'13.0':(1,[('12.2','H','killer T cell cloning','l')]),
'13.1':(1,[('13.0','H','killer T cells','l')]),
'13.2':(1,[('s5.6.3','H','memory T cells','l')]),
'13.3':(1,[('11.4','E','antigen-presenting cells','h')]),
'13.4':(1,[('8.2','H','marking for destruction','l')]),
'13.5':(2,[('12.0','H','helper T cell activation','l')]),
'14.0':(1,[('0.2','H','innate present from birth','h')]),
'14.1':(1,[('0.3','H','adaptive specific','h')]),
'14.2':(1,[('0.4','H','immune memory','h')]),
'14.3':(1,[('0.4','H','adaptive speed','h')]),
'14.4':(2,[('3.0','H','phagocytes','l')]),
'14.5':(1,[('0.5','H','distribution of defences','h')]),
'14.6':(1,[('11.4','E','antigen presentation by macrophages','h')]),
}
out={}
for t in targets:
    k=t[len('bio22-s2.'):]
    c,n=S.get(k,(1,[]))
    out[t]={'cost':c,'needs':[{'id':(i if i.startswith('s') else 'bio22-s2.'+i) if not i.startswith('s') else 'bio22-'+i,'strength':'essential' if s=='E' else 'helpful','why':w,'confidence':'high' if f=='h' else 'low'} for i,s,w,f in n]}
for t in ('0.0','7.1','0.1'):
    pass
out['bio22-s2.0.0']['cost']=2
json.dump(out,open(B+'point-links/bio22-s2.json','w'),indent=0)
d=json.load(open(B+'point-links/bio22-s2.json'))
assert list(d)==targets and len(set(targets))==len(targets)
L=[x for v in d.values() for x in v['needs']]
assert all(x['id'] in allids for x in L),[x['id'] for x in L if x['id'] not in allids]
assert all(x['id']!=k for k,v in d.items() for x in v['needs'])
print(len(d),len(L),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for x in L))
