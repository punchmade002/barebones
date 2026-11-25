import re,json
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio33-s2.txt'
O='/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio33-s2.json'
txt=open(P).read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=[]
for l in txt.split('CANDIDATES')[0].splitlines():
    m=re.match(r'\[([^\]]+)\]',l)
    if m: tgt.append(m.group(1))
def X(i):
    return {'S':'bio33-s2.','1':'bio33-s1.','B':'bio2-s2.','T':'bio25-s1.'}[i[0]]+i[1:] if i[0] in 'S1BT' and i[1]=='.' or i[0] in 'S1BT' and False else i
def ex(i):
    p={'S':'bio33-s2.','L':'bio33-s1.','B':'bio2-s2.','T':'bio25-s1.'}[i[0]]
    return p+i[1:]
C2=set('1.5 3.0 5.6 5.7 6.0 6.3 6.5 7.5 8.1 9.2 10.2 12.3 12.4 14.1 16.1 16.3 17.0 17.2 18.1 18.6 18.7 19.4 20.0 20.1'.split())
# key: (id, e/h, why[, L])
N={
'0.1':[('S4.0','h','solid medium: agar')],
'0.2':[('S0.1','h','colony definition','L')],
'0.3':[('S0.1','e','colony')],
'0.4':[('S0.3','h','plate measuring methods')],
'0.5':[('S4.2','h','broth culture')],
'0.6':[('L9.0','h','yeast cells')],
'1.1':[('S1.0','e','aseptic technique')],
'1.2':[('L0.1','h','pathogen definition')],
'1.3':[('S1.0','h','aseptic technique')],
'1.4':[('S1.2','h','cultures as possible pathogens')],
'1.5':[('L5.4','h','bacterial endospores')],
'1.6':[('S1.5','h','sterilising equipment')],
'2.0':[('S1.0','h','aseptic technique')],
'2.1':[('S2.0','e','flaming the loop')],
'2.2':[('S1.0','h','keeping airborne microbes out')],
'2.3':[('S1.0','h','avoiding contamination')],
'2.4':[('S2.3','h','opening culture bottles')],
'2.5':[('S1.0','h','avoiding contamination')],
'3.0':[('L7.6','h','anaerobic bacteria','L'),('S0.7','h','oxygen as growth factor')],
'3.3':[('S1.2','h','pathogens')],
'3.4':[('S1.2','h','pathogens')],
'3.5':[('S1.5','h','autoclave conditions')],
'4.2':[('S4.0','e','nutrient agar')],
'4.3':[('S4.0','h','agar types')],
'4.4':[('L10.0','h','Rhizopus mould')],
'4.5':[('S1.2','h','pathogen risk')],
'5.0':[('S4.0','h','sterile agar')],
'5.1':[('S5.0','e','melted agar')],
'5.2':[('S2.4','h','flaming bottle neck')],
'5.3':[('S2.5','h','opening dish slightly')],
'5.4':[('S5.3','h','pouring agar')],
'5.5':[('S2.0','e','flamed inoculating loop')],
'5.6':[('S3.7','h','sterile glass spreader')],
'5.7':[('S3.2','h','upside-down incubation')],
'6.0':[('B0.1','e','independent variable'),('B0.2','e','dependent variable')],
'6.1':[('B0.3','e','controlled variables')],
'6.2':[('B0.3','e','controlled variables')],
'6.3':[('B2.1','h','control experiment')],
'6.4':[('B2.1','e','control for comparison')],
'6.5':[('B5.1','e','replicates')],
'6.6':[('B0.2','h','dependent variable on y-axis','L')],
'6.7':[('S21.0','h','secondary data')],
'7.0':[('B1.4','h','optimum')],
'7.1':[('B0.1','e','independent variable')],
'7.2':[('S3.b','h','inoculating')] ,
'7.3':[('S6.1','h','same incubation time')],
'7.4':[('S0.3','e','colony measurement')],
'7.5':[('S7.1','h','temperature values tested')],
'7.6':[('S7.5','e','heat-treated cultures')],
'8.0':[('S7.0','h','temperature hypothesis')],
'8.2':[('S8.1','h','slow reactions when cold')],
'8.3':[('S8.1','h','enzyme-controlled reactions')],
'8.4':[('L5.6','e','endospores')],
'9.1':[('B0.1','e','independent variable')],
'9.2':[('B1.0','h','buffer holds pH')],
'9.3':[('S6.1','h','same inoculum volume')],
'9.4':[('S6.1','h','same incubation conditions')],
'9.5':[('S0.3','h','measuring growth')],
'10.0':[('S9.0','h','pH hypothesis')],
'10.1':[('S10.0','h','compare with bacteria')],
'10.2':[('S8.3','h','denaturation')],
'10.3':[('S10.0','h','low pH limits growth')],
'10.4':[('S10.3','h','acid preserves food')],
'11.1':[('B0.1','e','independent variable')],
'11.2':[('S4.0','e','nutrient agar')],
'11.3':[('S6.1','h','same inoculum volume')],
'11.4':[('S6.1','h','same incubation conditions')],
'11.5':[('S0.3','h','colony count, percentage cover')],
'12.0':[('S11.2','h','plain agar no nutrients')],
'12.1':[('S11.0','h','nutrient hypothesis','L')],
'12.2':[('S16.1','h','solute lowers growth by osmosis')],
'12.3':[('S0.7','h','nutrients as growth factor')],
'12.4':[('L12.2','h','amylase digests starch')],
'12.5':[('S12.4','e','starch digestion')],
'13.1':[('B0.1','e','independent variable')],
'13.2':[('B0.3','h','controlled variables')],
'13.3':[('L10.1','h','airborne spores')],
'13.4':[('S14.3','h','sealed bags safety','L')],
'13.5':[('S6.1','h','same conditions')],
'13.6':[('S0.4','e','percentage cover grid')],
'13.7':[('S14.3','h','spore safety')],
'14.0':[('S13.0','h','moisture hypothesis')],
'14.1':[('L12.1','h','extracellular digestion')],
'14.2':[('S14.1','e','water needed')],
'14.3':[('L8.6','h','spores')],
'15.1':[('B0.1','e','independent variable')],
'15.2':[('S4.0','h','nutrient agar')],
'15.3':[('S6.1','h','same inoculum volume')],
'15.4':[('S6.1','h','same incubation')],
'15.5':[('S0.3','h','colony count or diameter')],
'16.0':[('S15.0','h','solute hypothesis')],
'16.1':[('T2.0','e','osmosis')],
'16.2':[('S16.1','e','water loss by osmosis')],
'16.3':[('L1.3','h','cell wall stops bursting')],
'16.4':[('S16.1','e','osmosis in cells')],
'17.1':[('S17.0','h','antibacterial chemicals')],
'17.2':[('L14.2','h','antibiotic targets bacteria')],
'17.3':[('S17.0','h','antibacterial chemicals')],
'17.4':[('B0.1','h','independent variable'),('B0.2','h','dependent variable')],
'18.0':[('S5.6','e','lawn')],
'18.1':[('S2.0','h','flaming tools')],
'18.2':[('S6.4','h','control disc')],
'18.3':[('S3.0','h','taping plates')],
'18.4':[('S3.2','h','upside-down incubation')],
'18.5':[('S17.4','h','clear zone diameter')],
'18.6':[('S18.0','h','lawn plate')],
'18.7':[('S19.0','h','zone of inhibition')],
'19.0':[('S18.5','h','clear zone measured')],
'19.1':[('S18.2','e','water control disc')],
'19.2':[('S19.0','e','zone of inhibition')],
'19.3':[('S18.6','e','yeast lawn antifungal')],
'19.4':[('T1.0','e','diffusion down gradient')],
'19.5':[('S19.4','e','diffusion of chemical')],
'19.6':[('S19.0','h','zone of inhibition')],
'19.7':[('S19.6','h','resistance')],
'20.0':[('S19.0','h','clear zone diameter')],
'20.1':[('S20.0','e','zone area')],
'20.2':[('S20.0','h','area calculation')],
'21.1':[('S21.0','e','secondary data')],
'21.2':[('S21.1','h','published findings')],
'22.0':[('S8.2','h','cold slows growth')],
'22.1':[('S8.0','h','heat kills')],
'22.2':[('S1.5','h','sterilisation')],
'22.3':[('S14.1','e','water needed by enzymes')],
'22.4':[('S16.1','e','water loss by osmosis')],
'22.5':[('S10.3','e','low pH preserves')],
'23.1':[('L7.5','h','aerobic need oxygen')],
'23.2':[('S1.0','h','aseptic technique')],
'23.3':[('S7.0','h','optimum conditions')],
'24.0':[('S6.3','e','uninoculated control')],
'24.1':[('S6.1','h','equal inoculum')],
'24.2':[('S0.4','h','percentage cover alternative')],
'24.3':[('S9.2','h','pH meter and buffers')],
'24.4':[('S6.2','h','constant temperature')],
'24.5':[('S18.1','h','disc soaking')],
'24.6':[('S6.5','e','replicates and means')],
}
def full(i):
    if i[0]=='S':
        r=i[1:]
        # allow forms like 'S3.b' meaning bio33-s2.3.b ; 'S2.0' means s2.2.0
        return 'bio33-s2.'+r
    return ex(i)
out={}
for t in tgt:
    k=t.split('bio33-s2.')[1]
    cost=2 if k in C2 else 1
    needs=[]
    for n in N.get(k,[]):
        i=full(n[0]); 
        # fix S2.2.0 -> bio33-s2.2.0 handled; S2.3.b -> bio33-s2.3.b
        needs.append({'id':i,'strength':'essential' if n[1]=='e' else 'helpful','why':n[2],'confidence':'low' if len(n)>3 else 'high'})
    out[t]={'cost':cost,'needs':needs}
for t,v in out.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id']!=t,(t,n['id'])
        assert len(n['why'].split())<=8
assert list(out)==tgt and len(set(tgt))==len(tgt)
json.dump(out,open(O,'w'),indent=1)
json.load(open(O))
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
