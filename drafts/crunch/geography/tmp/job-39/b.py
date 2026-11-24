import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S3='geo-option-atmosphere-ocean-s3.'
c2={'1.0','2.5','6.3','8.0','12.0','12.2','13.0','13.3','14.2','14.3','20.1','21.0','21.2','24.0','26.4','28.5','31.0','31.2','31.6','34.1'}
# (id, [(target, strength, why, conf)]) ; target 's1.x'/'s2.x' full-qualified with geo-option-atmosphere-ocean-, or 'N.n' for s3
L1={'0.2':[('0.0','helpful','stores and flows drawn','high')],
'2.1':[('2.0','helpful','evapotranspiration includes evaporation','high')],
'3.0':[('2.0','helpful','evaporation as the source flow','low')],
'3.1':[('3.0','essential','surplus follows evaporation exceeding rain','high')],
'4.0':[('4.b','essential','residence time definition','high')],
'4.1':[('4.0','essential','uses the residence times','high')],
'5.0':[('s1.13.0','helpful','evaporation over rain raises salinity','high')],
'5.2':[('2.1','essential','uses evapotranspiration','high')],
'1.0':[('s1.11.0','helpful','oceans hold 97% of water','low')],
'6.1':[('6.0','essential','builds on humidity','high')],
'6.2':[('6.1','helpful','capacity at a temperature','high')],
'6.3':[('6.1','essential','relative humidity','high'),('6.2','essential','warm air holds more vapour','high')],
'6.4':[('6.1','essential','uses saturated air','high')],
'7.0':[('8.2','helpful','evaporation slow in humid air','high')],
'7.1':[('8.2','helpful','dry air allows rapid evaporation','high')],
'8.0':[('2.0','helpful','evaporation vapour concept','low')],
'8.1':[('8.0','helpful','energy for evaporation','high')],
'8.2':[('6.1','essential','uses relative humidity','high')],
'9.1':[('2.1','essential','uses evapotranspiration','high')],
'10.0':[('6.4','essential','uses dew point','high')],
'10.1':[('s1.3.1','helpful','aerosols act as condensation nuclei','low')],
'11.0':[('12.0','helpful','why rising air cools','high')],
'12.0':[('s1.5.1','essential','pressure falls with altitude','high')],
'12.1':[('12.0','essential','adiabatic cooling of rising air','high')],
'12.2':[('12.1','essential','compares with dry rate','high'),('8.0','helpful','latent heat released on condensation','high')],
'12.3':[('10.0','helpful','condensation at dew point','high')],
'13.0':[('12.1','essential','rising air cooling rate','high'),('s1.7.1','helpful','environmental lapse rate','high')],
'13.1':[('13.0','essential','contrasts with unstable air','high')],
'13.2':[('13.1','essential','stability idea','high')],
'13.3':[('13.0','essential','environmental lapse rate','high'),('12.1','essential','adiabatic lapse rate','high')],
'14.0':[('6.4','essential','uses dew point','high')],
'14.1':[('14.0','helpful','dew below freezing','high')],
'14.2':[('11.1','essential','contact cooling at night','high')],
'14.3':[('11.2','essential','advection cooling','high')],
'14.4':[('14.3','essential','same advection fog process','high')],
'14.5':[('15.2','helpful','forced uplift over high ground','low')],
'15.0':[('6.4','helpful','cooling below dew point','high')],
'17.0':[('16.1','helpful','meaning of cirrus','high')],
'18.b':[('16.2','helpful','meaning of alto-','high')],
'20.1':[('s1.7.3','helpful','tropopause defined','high')],
'21.0':[('17.0','helpful','cirrus description','low'),('19.2','helpful','nimbostratus description','low')],
'21.1':[('20.1','essential','cumulonimbus described','high')],
'21.2':[('16.3','helpful','ten cloud types','high')],
'24.1':[('24.0','essential','the process named','high')],
'24.0':[('23.0','helpful','droplets must grow','high')],
'25.0':[('23.0','helpful','droplets must grow','high')],
'26.0':[('19.2','helpful','nimbostratus rain','high')],
'26.1':[('19.0','helpful','stratus drizzle','high')],
'26.3':[('26.2','helpful','melting snow','low')],
'26.4':[('20.1','essential','hail forms in cumulonimbus','high')],
'27.1':[('11.0','essential','adiabatic cooling','high')],
'27.5':[('27.1','helpful','rising air steps','low')],
'28.1':[('28.0','essential','follows forced rise','high')],
'28.2':[('12.0','essential','descending air compresses and warms','high')],
'28.3':[('28.2','helpful','lee-side descent','high')],
'28.4':[('28.1','helpful','relief rain process','high')],
'28.5':[('28.1','helpful','windward rain process','high')],
'28.6':[('28.2','essential','rain shadow explanation','high')],
'29.0':[('15.3','helpful','frontal uplift','high')],
'29.1':[('29.0','helpful','follows warm front','high')],
'30.0':[('15.4','essential','convergence uplift','high')],
'31.0':[('15.4','helpful','ITCZ convergence','high'),('27.b','helpful','convection','low')],
'31.1':[('15.4','helpful','ITCZ moving over','high')],
'31.2':[('12.0','helpful','sinking air warms','high')],
'31.3':[('31.2','helpful','Atacama desert context','low'),('32.3','helpful','cold current fog','high')],
'31.4':[('29.2','helpful','depressions bring frontal rain','high')],
'31.6':[('31.0','helpful','rainfall belts to draw','high')],
'32.0':[('28.2','essential','rain shadow explained','high')],
'32.3':[('14.3','helpful','advection fog on cold currents','high')],
'32.4':[('31.b','helpful','pressure belts','high')],
'33.0':[('31.0','helpful','equatorial rain','high')],
'33.1':[('31.1','helpful','wet and dry season','high')],
'33.3':[('15.1','helpful','convection','high')],
'33.4':[('29.2','helpful','frontal rain from depressions','high')],
'34.3':[('29.2','helpful','Atlantic depressions','high'),('28.4','helpful','relief uplift','high')],
'35.0':[('15.4','helpful','ITCZ moves north','low')],
'35.1':[('35.0','essential','refers to Sahel rainfall','high')],
'36.0':[('27.b','helpful','convectional rain','high')],
'36.1':[('33.1','helpful','monsoon regime','high')],
'36.2':[('31.3','essential','Atacama and Namib fog','high')],
'36.3':[('34.0','helpful','wet west of Ireland','low')],
'36.5':[('5.3','essential','warming intensifies cycle','high')],
}
L2={'8.0':[('s2.1.1','helpful','latent heat','high')],
'9.0':[('s2.20.1','helpful','trade winds','high'),('s2.23.2','helpful','Gulf Stream','high')],
'12.2':[('s2.1.1','helpful','latent heat release','high')],
'14.3':[('s2.23.2','helpful','Gulf Stream','high'),('s2.23.1','helpful','Labrador Current','high')],
'14.4':[('s2.23.1','helpful','California Current','high')],
'15.4':[('s2.20.0','helpful','ITCZ','high')],
'22.0':[('s2.0.1','essential','long-wave radiation','high'),('s2.3.0','helpful','reflecting sunlight (albedo)','low')],
'27.0':[('s2.4.2','helpful','surface heats the air','low')],
'30.0':[('s2.20.0','helpful','ITCZ','high')],
'31.b':[('s2.20.b','helpful','three-cell circulation','low')],
'31.0':[('s2.20.0','helpful','ITCZ','high')],
'31.2':[('s2.20.1','essential','air sinks at 30 degrees','high')],
'31.4':[('s2.21.0','helpful','Ferrel cell westerlies','low')],
'31.5':[('s2.21.1','helpful','polar high','high')],
'31.6':[('s2.20.3','essential','three-cell model','high')],
'32.3':[('s2.23.1','helpful','cold currents','high')],
'32.4':[('s2.9.1','essential','overhead sun movement','high')],
'33.0':[('s2.9.1','helpful','equinoxes','low')],
'5.1':[('s2.21.0','helpful','westerlies belt','low')],
'35.0':[('s2.9.1','helpful','ITCZ follows sun','low')],
'36.2':[('s2.23.1','helpful','cold-current coasts','high')],
'36.3':[('s2.13.0','essential','North Atlantic Drift','high')],
}
def build(pack,out,L,mode):
    txt=open(P+'packs/'+pack).read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[(\S+?)\]',tgt,re.M)
    allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
    suf=[i[len(S3):] for i in ids]
    assert all(k in suf for k in L),[k for k in L if k not in suf]
    res={};nl=nc=nlow=0
    for s in suf:
        needs=[]
        for t,st,w,c in L.get(s,[]):
            tid=S3+t if re.match(r'^\d',t) else 'geo-option-atmosphere-ocean-'+t
            assert tid in allids and tid!=S3+s,tid
            needs.append({'id':tid,'strength':st,'why':w,'confidence':c}); nlow+=c=='low'
        e={'needs':needs}
        if mode=='c': e={'cost':2 if s in c2 else 1,**e}; nc+=s in c2
        res[S3+s]=e; nl+=len(needs)
    json.dump(res,open(P+'point-links/'+out,'w'),indent=0)
    chk=json.load(open(P+'point-links/'+out)); assert list(chk)==ids
    print(out,len(ids),nl,nc,nlow)
build('geo-option-atmosphere-ocean-s3.t1g1.txt','geo-option-atmosphere-ocean-s3.t1g1.json',L1,'c')
build('geo-option-atmosphere-ocean-s3.t1g2.txt','geo-option-atmosphere-ocean-s3.t1g2.json',L2,'l')
