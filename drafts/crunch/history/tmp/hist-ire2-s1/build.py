import sys,re
src=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/tmp/hist-ire3-s11/build.py').read().split("s11='''")[0]
exec(src)
s1='''0.b 2|
0.0 1|
0.1 1|
0.2 2|
0.3 1|0.2:e:H:Gladstone's 1870 Land Act
0.4 1|0.0:h:H:O'Connell's agitation
0.5 1|
1.b 1|0.b:h:H:Home Rule as moderate alternative
1.0 1|
1.1 1|0.0:h:L:Young Ireland and O'Connell
1.2 1|
1.3 1|
1.4 1|1.2:h:H:Home Rule movement
1.5 1|
1.6 1|1.2:h:H:Home Government Association
1.7 1|
2.b 1|1.6:h:H:the Home Rule League
2.0 2|1.6:e:H:Home Rule League and party
2.1 1|2.0:h:H:the 1874 Home Rule MPs;1.6:h:H:the League
2.2 1|1.3:h:H:Butt's Home Rule programme
2.3 1|
2.4 1|
2.5 1|3.1:h:H:Biggar and obstruction
2.6 1|3.b:h:H:obstructionists
3.b 1|
3.0 1|
3.1 1|3.0:e:H:obstruction
3.2 1|3.1:h:H:Biggar's obstruction
3.3 1|1.7:h:H:Butt's caution;0.1:h:H:Fenians and executions
3.4 1|1.6:h:L:Home Rule organisation
3.5 2|3.0:e:H:obstruction
3.6 1|3.0:h:H:obstruction
4.b 2|0.1:h:H:Fenians
4.0 1|
4.1 2|0.1:h:H:Fenian rising and prisoners
4.2 2|4.1:e:H:Davitt and Devoy
4.3 1|4.2:e:H:the Devoy offer
4.4 1|4.3:e:H:the New Departure
4.5 1|4.3:h:H:the New Departure
4.6 2|4.3:e:H:the New Departure
5.b 1|4.b:h:H:the New Departure forces
5.0 1|4.5:h:H:land question and national politics
5.1 1|5.0:h:H:Land League
5.2 1|3.2:h:H:Parnell's career
5.3 1|1.6:h:L:the Home Rule party
5.4 1|5.0:h:L:the movement's press
5.5 1|5.0:e:H:the suppressed Land League
5.6 1|2.1:h:H:no pledge among MPs
5.7 1|
5.8 1|5.5:e:H:National League
6.b 1|
6.0 1|
6.1 2|5.0:e:H:the Land League
6.2 2|6.1:e:H:Parnell's imprisonment
6.3 1|6.2:e:H:the Kilmainham settlement
6.4 1|6.0:h:H:Forster's coercion
6.5 2|6.4:e:H:Cavendish's appointment;6.2:h:H:the Kilmainham settlement
6.6 1|6.5:e:H:the Phoenix Park murders
6.7 1|6.5:e:H:the Invincibles' murders
6.8 1|5.5:h:H:National League
7.b 1|
7.0 1|
7.1 1|
7.2 1|3.2:h:H:Meath election and obstruction;5.0:h:H:Land League presidency
7.3 1|7.2:h:H:Parnell's career
7.4 1|5.0:h:H:Land League tenants
7.5 1|
7.6 2|
8.b 1|
8.0 2|2.0:h:H:Butt's 1874 seats
8.1 2|5.6:h:H:pledge and conventions
8.2 1|0.2:h:H:the 1870 Act
8.3 1|3.0:h:H:disruption by obstruction
8.4 1|
8.5 1|
8.6 1|6.2:e:H:the Kilmainham settlement'''
build('hist-ire2-s1.t1g1.txt','hist-ire2-s1.t1g1.json','hist-ire2-s1.',s1,1)
