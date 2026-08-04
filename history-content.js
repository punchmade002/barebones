// History HL Content — chapter notes, plus flashcard keyTerms injected from FLASHCARDS_DB.
// Requires: data.js (COURSE_DATA) and history-flashcards.js (FLASHCARDS_DB) to be loaded first.
//
// Notes are organised by the Leaving Certificate History perspectives — politics and
// administration; society and economy; culture, religion and science — and cover the key
// personalities and the major case-study material for each topic.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  var DB = window.FLASHCARDS_DB || {};
  var chapters = COURSE_DATA.chapters;

  var NOTES = {

    // ── Ireland Topic 1 — Ireland and the Union, 1815-1870 ──────────────────
    'hist-ire1': [
      {
        h: "Ireland under the Union",
        b: "The Act of Union (1801) abolished the Irish Parliament and governed Ireland directly from Westminster, with 100 Irish MPs in the Commons. Executive power rested with the Lord Lieutenant and Chief Secretary in Dublin Castle. Catholics, roughly three-quarters of the population, could vote on the same terms as Protestants but could not sit in Parliament or hold senior office — the grievance that dominated the first half of the period."
      },
      {
        h: "The Catholic Association and the Catholic Rent",
        b: "Daniel O'Connell founded the Catholic Association in 1823. Its innovation was the Catholic Rent — a subscription of one penny a month, collected through the parishes by priests and wardens — which brought the mass of tenant farmers into politics for the first time and gave the movement a large, independent income. It became the first modern mass political movement in Europe."
      },
      {
        h: "The Waterford election (1826) and the Clare election (1828)",
        b: "In 1826 the Association backed Villiers-Stuart against the Beresford family in Waterford, proving that 40-shilling freeholders would defy their landlords. In 1828 O'Connell himself stood in Co. Clare against William Vesey Fitzgerald and won, even though as a Catholic he could not take his seat. The government faced a choice between concession and civil unrest."
      },
      {
        h: "Catholic Emancipation (1829)",
        b: "Wellington and Peel carried the Catholic Relief Act in 1829, allowing Catholics to sit in Parliament and hold most public offices. The price was steep: the franchise qualification was raised from 40 shillings to £10, disenfranchising the very smallholders who had won the campaign. O'Connell became 'The Liberator', but Emancipation benefited the Catholic middle class far more than the rural poor."
      },
      {
        h: "The Tithe War (1830-36)",
        b: "Tithes were a compulsory payment of roughly one-tenth of produce to the Church of Ireland, the church of a small Protestant minority. Widespread refusal to pay led to violent confrontations with police and army, notably at Carrickshock and Rathcormac. The Tithe Rentcharge Act (1838) defused the issue by converting the tithe into a reduced rent charge payable by the landlord, who passed it on in rent."
      },
      {
        h: "The Repeal campaign and the monster meetings",
        b: "O'Connell founded the Repeal Association in 1840 to restore an Irish parliament under the Crown. He declared 1843 'Repeal Year' and held monster meetings — vast open-air gatherings, with perhaps 750,000 at Tara. When the government banned the meeting planned for Clontarf in October 1843, O'Connell cancelled it rather than risk bloodshed. He was imprisoned in 1844 and the campaign never recovered its momentum."
      },
      {
        h: "Young Ireland and The Nation",
        b: "Thomas Davis, Charles Gavan Duffy and John Blake Dillon founded The Nation in 1842. It promoted a cultural, non-sectarian nationalism built on Irish history, language, ballads and identity, and reached a readership far larger than its circulation through public readings. Young Ireland split from O'Connell in 1846 over his refusal to countenance physical force under any circumstances."
      },
      {
        h: "The 1848 Rising",
        b: "Inspired by the European revolutions of 1848 and radicalised by the Famine, Young Ireland attempted a rising led by William Smith O'Brien. It collapsed almost immediately at Ballingarry, Co. Tipperary, in a skirmish at Widow McCormack's house. Its significance is symbolic rather than military: it kept the separatist tradition alive, and its survivors seeded later movements at home and in exile."
      },
      {
        h: "The Great Famine: causes and course",
        b: "The blight Phytophthora infestans destroyed the potato crop from 1845, catastrophically in 1846 and 1848. Roughly one-third of the population depended on the potato almost exclusively, farming tiny subdivided holdings. Around one million people died of starvation and of the diseases that followed — typhus, dysentery, relapsing fever — and around one million emigrated. Population fell from about 8.2 million in 1841 to 6.5 million in 1851."
      },
      {
        h: "Government response to the Famine",
        b: "Peel imported Indian corn (maize) in 1845-46 and repealed the Corn Laws. Russell's Whig government relied on public works, which paid too little and exhausted starving labourers. The Soup Kitchen Act (1847) fed three million a day at its peak but was wound up within months. The Poor Law Extension Act (1847) shifted the cost onto Irish rates and included the Gregory Quarter-Acre Clause, which denied relief to anyone holding more than a quarter-acre and so drove mass evictions."
      },
      {
        h: "Charles Trevelyan and laissez-faire",
        b: "As Assistant Secretary to the Treasury, Trevelyan controlled relief spending. A committed believer in laissez-faire and in Providence, he opposed interference with the grain trade and regarded the Famine as a judgement on Irish overpopulation and on landlord neglect. His outlook shaped the wind-down of relief in 1847, when the crisis was far from over, and made him the enduring symbol of official indifference."
      },
      {
        h: "Private and voluntary relief",
        b: "The Society of Friends (Quakers) set up soup kitchens and supplied boilers, seed and clothing, and their honest reporting shaped opinion abroad. The British Relief Association raised large sums, including a donation from Queen Victoria. Individuals such as the American missionary Asenath Nicholson walked the country distributing food and Bibles. Voluntary relief was significant but far too small for a crisis of this scale."
      },
      {
        h: "Skibbereen and the local experience",
        b: "West Cork, and Skibbereen in particular, became the international image of the Famine. Reports by Nicholas Cummins and the sketches published in the Illustrated London News described whole families dying in cabins, mass graves, and workhouses overwhelmed far beyond capacity. Studying one locality shows how unevenly the Famine fell: the west and south-west suffered catastrophically while parts of the east were barely touched."
      },
      {
        h: "Fenianism and the IRB",
        b: "James Stephens founded the Irish Republican Brotherhood in Dublin on 17 March 1858; John O'Mahony founded the Fenian Brotherhood in America. Organised in secret cells and funded by the diaspora, it published the Irish People (1863) and rejected constitutional politics entirely. The 1867 rising failed, but the Manchester Martyrs and the Clerkenwell explosion that year created a potent tradition of republican martyrdom."
      },
      {
        h: "The devotional revolution: Cullen and the Synod of Thurles",
        b: "Paul Cullen, Archbishop of Armagh from 1849 and of Dublin from 1852, convened the Synod of Thurles in 1850 — the first national synod since the twelfth century. It imposed uniform discipline on the clergy, moved worship out of homes and into churches, and suppressed folk religious practice in favour of Roman devotions. Mass attendance rose sharply after the Famine. Cullen became Ireland's first cardinal in 1866."
      },
      {
        h: "Economy, transport and industry",
        b: "William Dargan built much of Ireland's railway network and financed the Great Industrial Exhibition of 1853 in Dublin. Industrialisation, however, concentrated in the north-east around Belfast linen and shipbuilding, while the rest of the country remained agricultural and, after the Famine, shifted decisively from tillage to pasture as holdings were consolidated and subdivision ended."
      },
      {
        h: "Culture and society",
        b: "William Carleton's Traits and Stories of the Irish Peasantry gave the most detailed portrait of pre-Famine rural life. Mother Mary Aikenhead founded the Irish Sisters of Charity, part of a wider expansion of religious orders into education and poor relief. The Irish language, already retreating before the Famine, collapsed in the decades after it, since the worst-hit districts were precisely the Irish-speaking ones."
      }
    ],

    // ── Ireland Topic 2 — Movements for reform, 1870-1914 ───────────────────
    'hist-ire2': [
      {
        h: "Isaac Butt and the birth of Home Rule",
        b: "Isaac Butt, a Protestant barrister who had defended Young Irelanders and Fenians, founded the Home Government Association in 1870 and the Home Rule League in 1873. He sought a subordinate Irish parliament for domestic affairs within the Union. Fifty-nine Home Rule MPs were returned in 1874, but Butt's courteous parliamentary style achieved little and frustrated younger members."
      },
      {
        h: "Parnell, obstruction and the leadership of the Party",
        b: "Charles Stewart Parnell, elected in 1875, adopted obstructionism — using parliamentary procedure to paralyse Commons business until Ireland was attended to. It made him famous and won Fenian respect. He became president of the Land League in 1879 and leader of the Irish Parliamentary Party in 1880, welding constitutional, agrarian and revolutionary strands into the 'New Departure'."
      },
      {
        h: "The Land War, 1879-82",
        b: "Bad harvests and falling prices from 1877 revived the threat of famine and eviction. Michael Davitt founded the Irish National Land League in 1879 with Parnell as president, demanding the 'three Fs' — fair rent, fixity of tenure, free sale. Its central weapon was ostracism, named after Captain Charles Boycott, the Mayo land agent shunned by an entire community in 1880."
      },
      {
        h: "Land legislation and the Kilmainham Treaty",
        b: "Gladstone's Land Act of 1881 conceded the three Fs and established land courts to fix fair rents, but excluded tenants in arrears. Parnell was imprisoned in Kilmainham; the resulting 'Kilmainham Treaty' of 1882 released him in return for cooperation, with arrears dealt with. Days later the Phoenix Park Murders of Lord Frederick Cavendish and T.H. Burke by the Invincibles nearly destroyed the settlement."
      },
      {
        h: "The Home Rule Bills of 1886 and 1893",
        b: "After the 1885 election the Irish Party held the balance of power and Gladstone converted to Home Rule. The First Home Rule Bill (1886) was defeated in the Commons and split the Liberal Party. The Second (1893) passed the Commons but was thrown out by the Lords. Both showed that Home Rule was achievable in principle and that the Lords' veto was the decisive obstacle."
      },
      {
        h: "The Parnell split",
        b: "In 1890 Parnell was named in Captain O'Shea's divorce petition over his long relationship with Katharine O'Shea. Gladstone made Parnell's retirement the condition of the Liberal alliance, and the Catholic hierarchy turned against him. The Party split in Committee Room 15. Parnell fought on, married Katharine, and died in 1891 aged 45. The split poisoned nationalist politics for a decade."
      },
      {
        h: "Land purchase and the end of landlordism",
        b: "A series of Acts moved from rent control to outright purchase. The Ashbourne Act (1885) advanced the full purchase price; the Wyndham Act (1903) offered landlords a cash bonus to sell entire estates and made purchase overwhelmingly attractive. Within a generation Ireland was transformed from a country of tenants into one of owner-occupying farmers — arguably the greatest social change of the period."
      },
      {
        h: "The GAA and the cultural revival",
        b: "Michael Cusack and Maurice Davin founded the Gaelic Athletic Association in Thurles in 1884, with Archbishop Croke as patron. It codified hurling and Gaelic football, organised them on a parish and county basis, and banned members from playing or attending 'foreign games'. It spread with extraordinary speed and was quickly infiltrated by the IRB, becoming a nursery of advanced nationalism."
      },
      {
        h: "The Gaelic League and the literary revival",
        b: "Douglas Hyde and Eoin MacNeill founded the Gaelic League in 1893 after Hyde's lecture 'The Necessity for De-Anglicising Ireland'. It aimed to revive the spoken language and was explicitly non-political — though Pearse and many later revolutionaries came through it. In parallel, W.B. Yeats, Lady Gregory and J.M. Synge built an Irish literary theatre, opening the Abbey in 1904."
      },
      {
        h: "Labour, Larkin and the 1913 Lockout",
        b: "James Larkin founded the Irish Transport and General Workers' Union in 1909 and used the sympathetic strike to organise unskilled labour. In August 1913 William Martin Murphy and some 400 Dublin employers locked out any worker who would not renounce the ITGWU. Around 20,000 workers held out for six months in a city with Europe's worst slums before hunger forced a return to work. James Connolly formed the Irish Citizen Army to defend strikers."
      },
      {
        h: "Women, suffrage and social reform",
        b: "Hanna Sheehy Skeffington and Margaret Cousins founded the Irish Women's Franchise League in 1908, adopting militant tactics and enduring imprisonment and hunger strikes. Countess Markievicz founded Fianna Éireann in 1909. Women's organisations divided over whether suffrage or national independence came first — a tension that ran through the following decade."
      },
      {
        h: "Ulster unionism and resistance to Home Rule",
        b: "The Ulster Unionist Council was formed in 1905. When the Parliament Act of 1911 removed the Lords' veto and made the Third Home Rule Bill (1912) unstoppable, Edward Carson and James Craig organised resistance: the Ulster Solemn League and Covenant was signed by nearly 250,000 men in September 1912, and the Ulster Volunteer Force was formed in 1913 and armed at Larne in April 1914."
      },
      {
        h: "The Irish Volunteers and the drift to arms",
        b: "Eoin MacNeill's Irish Volunteers were founded in November 1913 in response to the UVF and quickly reached some 180,000 members. The Curragh incident of March 1914 showed that British officers might refuse to coerce Ulster. The Howth gun-running in July 1914 armed the Volunteers, and troops fired on a crowd at Bachelor's Walk. Home Rule reached the statute book in September 1914 but was suspended for the duration of the war."
      },
      {
        h: "Cooperation and rural improvement",
        b: "Horace Plunkett founded the Irish Agricultural Organisation Society in 1894, promoting cooperative creameries, credit societies and agricultural education on the principle of 'better farming, better business, better living'. The Congested Districts Board (1891) tackled poverty along the western seaboard by consolidating holdings and supporting fishing and cottage industry."
      }
    ],

    // ── Ireland Topic 3 — Sovereignty and partition, 1912-1949 ──────────────
    'hist-ire3': [
      {
        h: "The Home Rule crisis and the outbreak of war",
        b: "The Third Home Rule Bill (1912) could no longer be vetoed by the Lords, so Ulster unionists organised extra-parliamentary resistance through the Covenant and the UVF, and nationalists answered with the Irish Volunteers. By mid-1914 partition in some form was already being discussed. The outbreak of war suspended the Act; Redmond's call at Woodenbridge for Volunteers to serve in the British army split the movement, leaving a small separatist minority."
      },
      {
        h: "The 1916 Rising",
        b: "A secret IRB military council planned a rising for Easter 1916. MacNeill's countermanding order and the loss of the Aud's German arms confined it largely to Dublin. Pearse read the Proclamation of the Irish Republic outside the GPO on Easter Monday; about 1,600 held out for six days against artillery. Some 450 died, much of the city centre was destroyed, and initial public reaction was hostile."
      },
      {
        h: "The executions and the transformation of opinion",
        b: "Between 3 and 12 May 1916 fifteen leaders were executed at Kilmainham, including the badly wounded Connolly, who was shot tied to a chair. Thousands were interned. The drawn-out executions, martial law and the threat of conscription in 1918 turned public sympathy decisively towards separatism — the outcome the Rising's planners had hoped for but could not have engineered."
      },
      {
        h: "Sinn Féin and the 1918 election",
        b: "Reorganised under de Valera in 1917 as an abstentionist republican party, Sinn Féin won by-elections and then swept the December 1918 general election, taking 73 of 105 seats. The Irish Parliamentary Party was reduced to six. Sinn Féin refused to attend Westminster and instead convened the First Dáil in the Mansion House on 21 January 1919, issuing a Declaration of Independence and a Democratic Programme."
      },
      {
        h: "The War of Independence, 1919-21",
        b: "Fighting began at Soloheadbeg on the day the Dáil first met. Michael Collins, as Director of Intelligence and Minister for Finance, ran a spy network inside Dublin Castle and raised the National Loan. The IRA fought a guerrilla campaign of ambushes and flying columns. Britain deployed the Black and Tans and Auxiliaries, whose reprisals — the burning of Cork, Bloody Sunday in November 1920 — lost the government the propaganda war."
      },
      {
        h: "Partition and the Government of Ireland Act",
        b: "The Government of Ireland Act (1920) created two parliaments: six counties as Northern Ireland and twenty-six as Southern Ireland. Only the northern parliament functioned, opening in June 1921 with James Craig as Prime Minister. The six counties were chosen as the largest area with a secure unionist majority — nine-county Ulster would not have delivered one. Partition was therefore in place before the Treaty was negotiated."
      },
      {
        h: "The Treaty negotiations, October-December 1921",
        b: "After the July 1921 truce, de Valera stayed in Dublin and sent Griffith and Collins as plenipotentiaries against Lloyd George, Churchill and Birkenhead. The delegates signed on 6 December under threat of 'immediate and terrible war', without referring back to the cabinet. The Treaty gave dominion status as the Irish Free State, an oath of fidelity to the Crown, retention of three Treaty Ports, and a Boundary Commission on the border."
      },
      {
        h: "The Treaty split and the Civil War",
        b: "The Dáil approved the Treaty by 64 to 57 in January 1922 and de Valera resigned. Collins argued it gave 'the freedom to achieve freedom'; opponents rejected the oath and the abandonment of the Republic. Anti-Treaty forces occupied the Four Courts, and shelling began in June 1922. The Civil War lasted until May 1923, killed Collins at Béal na mBláth and Griffith by stroke, and left a bitterness that defined party politics for generations."
      },
      {
        h: "Cumann na nGaedheal in power, 1923-32",
        b: "W.T. Cosgrave's government prioritised stability: an unarmed Garda Síochána, an independent judiciary, and the reduction of the army after the Army Mutiny of 1924. The Boundary Commission collapsed in 1925 when its report proposed only minor changes, and the border was confirmed unaltered. The Shannon hydroelectric scheme at Ardnacrusha and the Electricity Supply Board were its outstanding achievements."
      },
      {
        h: "De Valera, Fianna Fáil and the Economic War",
        b: "De Valera founded Fianna Fáil in 1926, entered the Dáil in 1927 and took power in 1932 — with Cumann na nGaedheal handing over peacefully, a crucial democratic precedent. He withheld the land annuities; Britain retaliated with tariffs on Irish cattle, and the Economic War (1932-38) hit farmers hard while protectionism built up native industry. It was settled in 1938, with the Treaty Ports returned."
      },
      {
        h: "The 1937 Constitution",
        b: "Bunreacht na hÉireann replaced the Free State constitution in 1937. It named the state Éire, created the office of President and a Taoiseach with strengthened powers, and claimed jurisdiction over the whole island in Articles 2 and 3. Article 41 recognised the family and referred to women's 'life within the home'; Article 44 acknowledged the 'special position' of the Catholic Church while guaranteeing other denominations."
      },
      {
        h: "Northern Ireland under unionist rule",
        b: "Craig's government at Stormont governed as 'a Protestant parliament for a Protestant people'. Proportional representation was abolished for local elections in 1922 and Stormont elections in 1929; constituency boundaries were drawn to secure unionist control even where nationalists were a majority, most notoriously in Derry. The Special Powers Act (1922) and the largely Protestant B Specials underpinned security policy."
      },
      {
        h: "The Emergency and neutrality",
        b: "Ireland remained neutral in the Second World War — 'the Emergency' — as an assertion of the sovereignty won in 1938. Censorship was strict, supplies scarce, and the army expanded. Neutrality was nonetheless benevolent towards the Allies: Allied airmen were returned across the border while German ones were interned. Belfast, by contrast, was heavily bombed in April and May 1941, and Dublin fire brigades crossed the border to help."
      },
      {
        h: "The Republic of Ireland, 1948-49",
        b: "The 1948 inter-party government under John A. Costello, which ended Fianna Fáil's sixteen-year run, passed the Republic of Ireland Act, repealing the External Relations Act and taking the state out of the Commonwealth on Easter Monday 1949. Britain's Ireland Act (1949) responded by guaranteeing that Northern Ireland would remain in the United Kingdom unless its own parliament consented — hardening partition."
      }
    ],

    // ── Ireland Topic 4 — The Irish diaspora, 1840-1966 ─────────────────────
    'hist-ire4': [
      {
        h: "Emigration before and after the Famine",
        b: "Emigration was already substantial before 1845, drawing mainly Ulster Presbyterians and better-off Catholics who could pay their passage. The Famine changed its character utterly: between 1845 and 1855 around two million left, now overwhelmingly poor, Catholic and from the west and south. Emigration then became structural — a normal expectation of Irish life for over a century rather than a crisis response."
      },
      {
        h: "The crossing and the coffin ships",
        b: "The cheapest route was the timber trade to British North America, on vessels that became known as coffin ships for their mortality. On the worst crossings of 1847 a fifth or more of passengers died of typhus and dysentery in overcrowded holds. Grosse Île in the St Lawrence, the quarantine station for Quebec, received thousands of the dying; over 5,000 are buried there."
      },
      {
        h: "Chain migration, remittances and the American wake",
        b: "Emigration was self-sustaining: those who went sent money home, and that money paid the next passage. Remittances from North America financed a large share of all subsequent departures and supported families left behind. The American wake — a night of music, dancing and lament before departure — treated emigration as a form of death, since the emigrant was rarely expected to return."
      },
      {
        h: "The Irish in Britain",
        b: "Britain was the cheapest and therefore the commonest destination. Liverpool, Glasgow, Manchester and London developed large Irish quarters where migrants worked as navvies on canals, railways and docks, and women in domestic service and textiles. They met intense hostility on grounds of religion, poverty and disease, and sectarian rioting was recurrent in Liverpool and Glasgow."
      },
      {
        h: "The Irish in the United States",
        b: "Arriving without capital, the Irish concentrated in the eastern cities — Boston, New York, Philadelphia — in the worst housing and hardest labour. They faced nativist hostility from the Know-Nothing movement and 'No Irish Need Apply' notices. Advancement came through numbers and organisation rather than wealth: the Church, the trade unions, the police and fire departments, and above all city politics."
      },
      {
        h: "Political machines and Tammany Hall",
        b: "Irish-Americans mastered urban machine politics, exchanging jobs, coal, food and legal help for reliable votes at ward level. Tammany Hall in New York was the model, and by the later nineteenth century the Irish controlled the Democratic organisation in many major cities. The trajectory ran from ward boss to mayor, and eventually to the presidency with John F. Kennedy in 1960."
      },
      {
        h: "The Church as an institution of emigration",
        b: "The Catholic Church followed the emigrants and became the central institution of Irish communities abroad, supplying parishes, schools, hospitals and orphanages, and a steady supply of Irish priests, nuns and bishops. It preserved identity and respectability but also drew accusations of clannishness, and Irish clerical dominance caused friction with later German, Italian and Polish Catholic immigrants."
      },
      {
        h: "Australia and the wider diaspora",
        b: "Around 40,000 Irish convicts were transported to Australia, followed by assisted emigrants and the gold rushes of the 1850s. The Irish made up a far larger share of the Australian population than of the American, and shaped its Catholic Church under Archbishop Daniel Mannix and its labour politics. Ned Kelly, son of an Irish convict, became a folk symbol of Irish-Australian resistance to authority."
      },
      {
        h: "The diaspora and Irish nationalism",
        b: "Exiles funded and armed Irish separatism. The Fenian Brotherhood was founded in New York in 1858 and Clan na Gael in 1867, and John Devoy sustained links between American money and Irish revolutionaries for fifty years, from the New Departure to the 1916 Rising. De Valera's American tour of 1919-20 raised over five million dollars for the Dáil and made the Irish case an issue in US politics."
      },
      {
        h: "Emigration in the independent state",
        b: "Independence did not stop emigration. The 1950s were worse than any decade since the Famine: over 400,000 left, most for Britain's post-war building sites, factories and hospitals, and net emigration in some years exceeded the natural increase, so the population actually fell. It was the clearest indictment of the economic policies that Whitaker and Lemass set out to reverse from 1958."
      },
      {
        h: "Identity, assimilation and return",
        b: "By the twentieth century Irish-America had moved into the middle class and into national life, while retaining a strong symbolic ethnicity expressed through St Patrick's Day parades, county associations, sport and continued interest in Irish affairs. Kennedy's visit to Ireland in June 1963, four months before his assassination, was the emotional high point of the relationship between the state and its diaspora."
      }
    ],

    // ── Ireland Topic 5 — Northern Ireland, 1949-1993 ───────────────────────
    'hist-ire5': [
      {
        h: "The unionist state at mid-century",
        b: "Northern Ireland had a devolved parliament at Stormont, controlled without interruption by the Ulster Unionist Party from 1921. Westminster convention prevented debate of Northern Ireland affairs. The Ireland Act (1949) guaranteed that the North would not leave the UK without Stormont's consent, confirming unionist security just as the South declared a republic."
      },
      {
        h: "Discrimination and grievance",
        b: "Nationalist grievances centred on three areas: electoral boundaries drawn to produce unionist councils in nationalist-majority areas, most flagrantly in Derry; the allocation of council housing, which controlled the local government franchise since it was tied to householders; and employment, both in the public sector and in major private firms. The Special Powers Act and the B Specials made security policy a further grievance."
      },
      {
        h: "The IRA Border Campaign, 1956-62",
        b: "Operation Harvest attacked customs posts, barracks and infrastructure along the border. It won little support from northern nationalists, was contained by internment on both sides of the border, and was called off in 1962 with a statement blaming the indifference of the people. Its failure discredited physical force and encouraged a turn towards civil rights agitation."
      },
      {
        h: "O'Neill's reformism and its limits",
        b: "Terence O'Neill became Prime Minister in 1963 promising economic modernisation and better community relations, and met Seán Lemass at Stormont in 1965 — the first such meeting since partition. But symbolic gestures outran substance. Decisions such as siting the new university in Protestant Coleraine rather than in Derry, and the new city of Craigavon, convinced nationalists that nothing structural would change, while alarming unionists led by Ian Paisley."
      },
      {
        h: "The civil rights movement",
        b: "The Northern Ireland Civil Rights Association was founded in 1967, demanding one man one vote, fair housing allocation, an end to gerrymandering, repeal of the Special Powers Act and disbandment of the B Specials — reform within the UK, not unity. The Derry march of 5 October 1968 was baton-charged by the RUC in front of television cameras, and the images turned the movement into an international story."
      },
      {
        h: "From Burntollet to the deployment of troops",
        b: "People's Democracy's Belfast-to-Derry march was ambushed at Burntollet Bridge in January 1969 with police complicity. Rioting escalated through the summer, culminating in the Battle of the Bogside in August when residents held off the RUC for two days. British troops were deployed on 14 August 1969, welcomed at first by Catholics as protection from the police and loyalist mobs."
      },
      {
        h: "The Provisional IRA, internment and Bloody Sunday",
        b: "The IRA split in December 1969, the Provisionals emerging committed to armed defence and an offensive campaign. Internment without trial was introduced on 9 August 1971 and applied almost entirely to nationalists, driving recruitment sharply upward. On 30 January 1972 paratroopers shot dead thirteen unarmed civil rights marchers in Derry — Bloody Sunday. Stormont was prorogued in March 1972 and direct rule imposed."
      },
      {
        h: "Sunningdale and the power-sharing executive",
        b: "The 1973 Sunningdale Agreement established a power-sharing executive of unionists, the SDLP and Alliance under Brian Faulkner, together with a Council of Ireland giving Dublin a consultative role. The Council was the sticking point. The loyalist Ulster Workers' Council strike in May 1974 shut down power and industry, and the executive collapsed after five months — a template its supporters would return to twenty-four years later."
      },
      {
        h: "The hunger strikes, 1980-81",
        b: "The removal of special category status led republican prisoners in the Maze to the blanket and dirty protests and then to hunger strike. Bobby Sands died on 5 May 1981 after 66 days, having been elected MP for Fermanagh-South Tyrone while dying; nine others followed. Thatcher refused to concede. The strikes cost lives and international standing but delivered Sinn Féin an electoral mandate and the 'Armalite and ballot box' strategy."
      },
      {
        h: "The Anglo-Irish Agreement, 1985",
        b: "Signed at Hillsborough by Thatcher and FitzGerald, it gave the Irish government a formal consultative role in Northern Ireland affairs through an intergovernmental conference, while affirming that constitutional change required majority consent. Unionists were enraged — 'Ulster Says No', mass rallies, resignations of MPs — but the Agreement held, demonstrating that a unionist veto could no longer stop London and Dublin acting together."
      },
      {
        h: "Towards a settlement: Hume, Adams and Downing Street",
        b: "John Hume of the SDLP argued that the conflict could only be resolved by including republicans, and opened talks with Gerry Adams in 1988 and again from 1993 at considerable political cost. The Downing Street Declaration of December 1993, agreed by Albert Reynolds and John Major, accepted Irish self-determination on the basis of consent and offered Sinn Féin a route into negotiations after a cessation of violence."
      },
      {
        h: "Economy and society",
        b: "The traditional industries that had underpinned the northern economy — Harland and Wolff shipbuilding, linen, Short Brothers — declined steeply from the 1960s, and the Troubles deterred investment while inflating public sector employment. Segregation deepened as families moved for safety, producing interface areas and peace walls, and separate schooling reinforced division across two generations."
      }
    ],

    // ── Ireland Topic 6 — Government, economy and society, 1949-1989 ────────
    'hist-ire6': [
      {
        h: "The stagnant fifties",
        b: "The 1950s were the worst decade of independence economically: protectionism had exhausted its possibilities, industry was small and inefficient, balance of payments crises forced deflationary budgets in 1952 and 1956, and over 400,000 people emigrated. Population fell to its lowest recorded level in 1961. The failure was severe enough to force a fundamental rethink of economic policy."
      },
      {
        h: "The Mother and Child Scheme, 1951",
        b: "Health Minister Noël Browne proposed free maternity care and free healthcare for children under sixteen, without a means test. The Catholic hierarchy under Archbishop McQuaid objected that it usurped the rights of the family and the Church in matters of moral instruction, and the medical profession opposed it on income grounds. Browne was forced to resign and the coalition fell — the clearest demonstration of Church power over the state."
      },
      {
        h: "Whitaker, Lemass and economic expansion",
        b: "T.K. Whitaker's Economic Development (1958) argued for abandoning protectionism in favour of free trade, foreign investment and productive rather than social capital spending. It became the First Programme for Economic Expansion under Seán Lemass, who succeeded de Valera as Taoiseach in 1959. Grants and tax concessions through the IDA attracted foreign firms; growth averaged around 4% a year in the 1960s and emigration fell sharply."
      },
      {
        h: "Free secondary education",
        b: "Donogh O'Malley announced free secondary education and free school transport in 1966, to take effect in 1967, reportedly without full cabinet sanction. Participation rose dramatically, and the creation of regional technical colleges and the expansion of third level followed. It is generally regarded as the most consequential social reform of the period and a precondition of later economic success."
      },
      {
        h: "Television and the Late Late Show",
        b: "Telefís Éireann began broadcasting on 31 December 1961. The Late Late Show, presented by Gay Byrne from 1962, brought subjects previously undiscussed in public — sex, contraception, clerical authority, illegitimacy, emigration — into Irish living rooms every week, provoking repeated clashes with bishops and politicians. Lemass observed that television could be a dangerous instrument; it was certainly a solvent of deference."
      },
      {
        h: "Entry to the EEC, 1973",
        b: "Ireland joined the European Economic Community with Britain and Denmark on 1 January 1973 after a referendum carried by 83%. The Common Agricultural Policy transformed farm incomes, structural funds financed infrastructure, and access to a continental market reduced dependence on Britain from about three-quarters of exports to under a third. Membership also provided external leverage for social and equality legislation."
      },
      {
        h: "The Arms Crisis, 1970",
        b: "The outbreak of the Troubles forced the Republic to define its northern policy. In May 1970 Jack Lynch dismissed ministers Charles Haughey and Neil Blaney over an alleged plot to import arms for northern nationalists. Both were acquitted, but the crisis established that the state would not support the Provisional IRA, and it shaped Fianna Fáil's internal politics for the next twenty years."
      },
      {
        h: "The economic crisis of the late 1970s and 1980s",
        b: "The oil shocks of 1973 and 1979 ended the long boom. Fianna Fáil's expansionary 1977 manifesto — abolishing rates and car tax while borrowing heavily — left a debt burden that dominated the following decade. By the mid-1980s unemployment approached 18%, the national debt exceeded GNP, taxation on employment was punishing, and net emigration resumed on a large scale."
      },
      {
        h: "The women's movement",
        b: "The Irish Women's Liberation Movement was founded in 1970 and staged the contraceptive train from Belfast in 1971. The marriage bar requiring women to resign from public service jobs on marriage was removed in 1973. The McGee case (1973) established a right to marital privacy in relation to contraception, though the 1979 Act still restricted it to bona fide family planning purposes by prescription."
      },
      {
        h: "Referendums and the contested moral order",
        b: "The 1983 referendum inserted the Eighth Amendment recognising the equal right to life of the unborn, carried by two to one after a bitter campaign. The 1986 referendum on removing the constitutional ban on divorce was defeated by a similar margin. Both showed the continuing influence of Catholic teaching, but also a substantial, growing and largely urban minority prepared to vote against it."
      },
      {
        h: "The changing position of the Church",
        b: "Church influence remained formidable through the period — in education, health and legislation — and the Papal visit of 1979 drew over a million people to the Phoenix Park. But vocations were falling, television and education had eroded deference, and the confidence of the 1950s was gone. The institutional crisis of the 1990s had its roots in the social changes of these decades."
      }
    ],

    // ── Europe Topic 1 — Nationalism and state formation, 1815-1871 ─────────
    'hist-eur1': [
      {
        h: "The Congress of Vienna, 1815",
        b: "Metternich, Castlereagh, Talleyrand and Tsar Alexander I redrew Europe after Napoleon on three principles: legitimacy (restoring rightful dynasties), compensation (rewarding the victors with territory) and the balance of power (preventing any state dominating again). France was ringed with strengthened neighbours. Nationalism and liberalism were treated as threats to be suppressed, not forces to be accommodated."
      },
      {
        h: "Metternich and the Concert of Europe",
        b: "The Austrian chancellor dominated European diplomacy until 1848. The Concert of Europe committed the great powers to consult and to intervene against revolution — at Troppau, Laibach and Verona. Within the German Confederation the Carlsbad Decrees (1819) censored the press, policed the universities and banned student societies. Austria's multinational empire made Metternich the natural enemy of national self-determination."
      },
      {
        h: "The revolutions of 1848",
        b: "Beginning in Palermo and Paris, revolution spread to Vienna, Berlin, Budapest, Prague, Milan and Rome. Metternich fled. Liberals demanded constitutions, nationalists demanded unification or independence, and workers demanded relief from unemployment and food prices. Within eighteen months almost all had been reversed, because the middle-class liberals feared social revolution more than reaction and the national movements divided against each other."
      },
      {
        h: "The Frankfurt Parliament",
        b: "Elected in May 1848, it debated German unity for a year, splitting over the Grossdeutsch solution including Austria and the Kleindeutsch solution excluding it. It finally offered the imperial crown to Frederick William IV of Prussia in 1849, who refused to accept 'a crown from the gutter'. Its failure taught the lesson Bismarck would apply: German unity would come from Prussian power, not liberal assemblies."
      },
      {
        h: "Mazzini, Cavour and the Italian question",
        b: "Giuseppe Mazzini's Young Italy preached a democratic republic achieved by popular insurrection, and inspired a generation without ever succeeding. Count Camillo Cavour, Prime Minister of Piedmont from 1852, took the opposite approach: modernise the state, gain diplomatic standing by joining the Crimean War, and secure a great-power ally. At Plombières in 1858 he obtained Napoleon III's support against Austria."
      },
      {
        h: "Garibaldi and the Expedition of the Thousand",
        b: "In May 1860 Garibaldi sailed from Genoa with about a thousand red-shirted volunteers, landed at Marsala, defeated far larger Neapolitan forces at Calatafimi and Palermo, crossed to the mainland and entered Naples. Cavour, alarmed that Garibaldi would march on Rome and provoke France, sent Piedmontese troops south. Garibaldi handed his conquests to Victor Emmanuel II at Teano and retired to Caprera."
      },
      {
        h: "The Kingdom of Italy",
        b: "Victor Emmanuel II was proclaimed King of Italy in March 1861. Venetia was gained in 1866 as a by-product of the Austro-Prussian War, and Rome was taken in 1870 when French troops withdrew for the Franco-Prussian War. Unification left deep problems: a poor, resentful south under northern administration, an alienated papacy refusing to recognise the state, and a tiny electorate."
      },
      {
        h: "Bismarck and Realpolitik",
        b: "Appointed Minister-President of Prussia in 1862, Bismarck governed without a budget and declared that the great questions would be settled 'by blood and iron'. He was a Prussian conservative rather than a German nationalist, using national feeling to extend Hohenzollern power. His method was to isolate each opponent diplomatically before fighting, and to stop as soon as the objective was achieved."
      },
      {
        h: "The three wars of German unification",
        b: "The Danish War (1864), fought alongside Austria over Schleswig and Holstein, created the joint administration Bismarck then used to provoke the Austro-Prussian War (1866). Victory at Sadowa in seven weeks excluded Austria from Germany and produced the North German Confederation. The Ems telegram provoked France into declaring war in 1870; after Sedan and the siege of Paris, the German Empire was proclaimed in the Hall of Mirrors at Versailles in January 1871."
      },
      {
        h: "Napoleon III and the Second Empire",
        b: "Elected president in 1848 and emperor after the 1851 coup, Napoleon III combined authoritarian rule with plebiscites, economic modernisation, investment banking and free trade. His foreign policy — Crimea, Italy, Mexico — sought prestige and often produced the opposite. Defeat and capture at Sedan in 1870 ended the empire and produced the Third Republic and the Paris Commune."
      },
      {
        h: "The Paris of Baron Haussmann",
        b: "As Prefect of the Seine from 1853, Haussmann drove wide boulevards through medieval Paris, built the sewer and water systems, laid out parks, railway stations and the Opéra, and imposed uniform building frontages. The work modernised the city, employed tens of thousands and made barricade-building far harder. It also demolished working-class districts and pushed the poor to the periphery, and its cost brought him down in 1870."
      },
      {
        h: "Industry, railways and the Great Exhibition",
        b: "Railways, steam power, iron and later steel transformed the European economy and were essential to state formation — the Zollverein customs union of 1834 knit Germany economically long before politically, and railways made rapid mobilisation possible. The Great Exhibition of 1851 in Joseph Paxton's Crystal Palace displayed the products of a hundred thousand exhibits to six million visitors, advertising British industrial supremacy."
      }
    ],

    // ── Europe Topic 2 — Nation states and international tensions ───────────
    'hist-eur2': [
      {
        h: "Bismarck's alliance system",
        b: "After 1871 Bismarck's aim was to keep France isolated and to prevent an Austro-Russian collision in the Balkans dragging Germany in. He built the Dual Alliance with Austria-Hungary (1879), added Italy to make the Triple Alliance (1882), and kept a separate Reinsurance Treaty with Russia (1887). The system was intricate, defensive and dependent on one man's judgement."
      },
      {
        h: "Wilhelm II and Weltpolitik",
        b: "Wilhelm II dismissed Bismarck in 1890 and let the Reinsurance Treaty lapse, freeing Russia to ally with France in 1894 — the two-front position Bismarck had spent twenty years avoiding. Weltpolitik demanded colonies, influence and above all a battle fleet. Tirpitz's Navy Laws from 1898 were aimed unmistakably at Britain and converted a natural friend into a determined opponent."
      },
      {
        h: "The formation of the Triple Entente",
        b: "Britain abandoned splendid isolation, allying with Japan in 1902 and settling colonial disputes with France in the Entente Cordiale of 1904 and with Russia in 1907. None of these were binding military alliances, but Anglo-French naval and staff conversations created strong expectations. Europe had divided into two armed camps, each convinced the other was the aggressor."
      },
      {
        h: "The Moroccan and Balkan crises",
        b: "Germany challenged French primacy in Morocco in 1905 and again at Agadir in 1911, and on each occasion succeeded only in tightening the Entente. In the Balkans, Austria's annexation of Bosnia-Herzegovina in 1908 humiliated Russia and enraged Serbia, and the Balkan Wars of 1912-13 doubled Serbian territory. Austria concluded that Serbia had to be destroyed."
      },
      {
        h: "The Dreyfus Case",
        b: "Captain Alfred Dreyfus, an Alsatian Jew, was convicted of treason in 1894 on forged evidence and sent to Devil's Island. When Colonel Picquart identified Esterhazy as the real spy the army closed ranks. Émile Zola's open letter 'J'accuse' in 1898 split France between Dreyfusards defending the individual against the state and anti-Dreyfusards defending the army, Church and nation. Dreyfus was pardoned in 1899 and exonerated in 1906."
      },
      {
        h: "July 1914",
        b: "Franz Ferdinand and his wife were assassinated in Sarajevo on 28 June 1914 by Gavrilo Princip. Austria secured Germany's 'blank cheque' and issued an ultimatum designed to be rejected. Russia mobilised in support of Serbia; German war planning allowed no pause, since the Schlieffen Plan required knocking out France in six weeks before turning east. Britain entered on 4 August over the invasion of neutral Belgium."
      },
      {
        h: "Stalemate and the Western Front",
        b: "The Schlieffen Plan failed at the Marne in September 1914 and both sides dug in from the Channel to Switzerland. Machine guns, quick-firing artillery and barbed wire gave the defence overwhelming advantage. Attacks gained metres for enormous casualties, and the war became one of attrition, industry and blockade rather than manoeuvre."
      },
      {
        h: "Verdun and the Somme",
        b: "At Verdun from February 1916 Falkenhayn sought to 'bleed France white'; the ten-month battle cost around 700,000 casualties on both sides. The Somme, launched on 1 July 1916 partly to relieve Verdun, cost the British nearly 60,000 casualties on the first day alone — the worst in the army's history — and about a million overall by November for an advance of a few miles. Tanks appeared for the first time in September."
      },
      {
        h: "Total war and the home front",
        b: "States took control of industry, food, labour and information. Conscription became near-universal; women entered munitions, transport and agriculture in unprecedented numbers, strengthening the case for the vote. Propaganda and censorship shaped opinion, and the British naval blockade produced severe malnutrition in Germany by the 'turnip winter' of 1916-17. Civilian morale became a strategic factor."
      },
      {
        h: "1917: revolution and American entry",
        b: "Unrestricted submarine warfare and the Zimmermann Telegram brought the United States into the war in April 1917, promising decisive resources. In Russia the February Revolution toppled the Tsar and the Bolsheviks seized power in October, making peace at Brest-Litovsk in March 1918. Germany's resulting last offensive in spring 1918 exhausted itself, and the Allied counter-attack forced an armistice on 11 November."
      },
      {
        h: "The Paris Peace Conference",
        b: "Wilson, Lloyd George and Clemenceau dominated proceedings in 1919; Germany and Russia were excluded. Wilson's Fourteen Points and self-determination collided with French demands for security and with British and Italian territorial claims. The settlement created new states across central and eastern Europe, but self-determination could not be applied cleanly to a region of mixed populations, leaving large minorities everywhere."
      },
      {
        h: "The Treaty of Versailles and the League",
        b: "Germany lost Alsace-Lorraine, the Polish Corridor and all colonies, was limited to a 100,000-man army with no air force, tanks or submarines, and had the Rhineland demilitarised. Article 231 assigned responsibility for the war and grounded a reparations bill fixed at £6,600 million in 1921. The League of Nations was founded to arbitrate disputes, but the United States never joined and it had no armed force."
      }
    ],

    // ── Europe Topic 3 — Dictatorship and democracy, 1920-1945 ──────────────
    'hist-eur3': [
      {
        h: "The Weimar Republic and its weaknesses",
        b: "The 1919 constitution was democratic in design but flawed in practice: proportional representation produced unstable coalitions, and Article 48 allowed the President to rule by decree. The Republic was born of defeat and burdened with the 'stab in the back' myth and the odium of Versailles. It faced the Kapp Putsch from the right and the Spartacist rising from the left within its first eighteen months."
      },
      {
        h: "Hyperinflation and recovery",
        b: "When Germany defaulted on reparations, France and Belgium occupied the Ruhr in 1923. Passive resistance was funded by printing money and the currency collapsed — a loaf reaching hundreds of billions of marks — wiping out middle-class savings. Stresemann introduced the Rentenmark, ended resistance, and negotiated the Dawes Plan (1924) and Young Plan (1929), which brought American loans and five years of relative stability."
      },
      {
        h: "Mussolini and Italian Fascism",
        b: "Post-war Italy had a 'mutilated victory', inflation, unemployment and factory occupations. Mussolini's blackshirt squads attacked socialists with tacit official approval, and after the March on Rome in October 1922 the King appointed him Prime Minister. The Acerbo Law and the murder of Matteotti in 1924 completed the transition to dictatorship, and the Lateran Treaty of 1929 reconciled the state with the papacy."
      },
      {
        h: "Hitler's rise to power",
        b: "The Munich Putsch of 1923 failed and earned Hitler a short sentence in which he wrote Mein Kampf and resolved to take power legally. The Depression was decisive: Nazi seats rose from 12 in 1928 to 230 in July 1932 as unemployment passed six million. Papen and Hindenburg, believing they could control him, appointed Hitler Chancellor on 30 January 1933."
      },
      {
        h: "The consolidation of Nazi power",
        b: "The Reichstag Fire of February 1933 justified an emergency decree suspending civil liberties. The Enabling Act in March gave Hitler power to legislate without parliament. Trade unions and other parties were abolished by July. The Night of the Long Knives in June 1934 destroyed the SA leadership and reassured the army, and on Hindenburg's death that August Hitler merged the offices of Chancellor and President."
      },
      {
        h: "The Nuremberg Rallies",
        b: "The annual party rallies at Nuremberg, staged by Albert Speer with searchlight 'cathedrals of light', massed ranks and standards, were the fullest expression of Nazi propaganda. Leni Riefenstahl's Triumph of the Will (1935) filmed the 1934 rally and defined the regime's image internationally. The rallies produced no policy; their function was to submerge the individual in the mass and to display power."
      },
      {
        h: "Racial policy and the Holocaust",
        b: "The Nuremberg Laws (1935) stripped Jews of citizenship and outlawed marriage with 'Aryans'. Kristallnacht in November 1938 destroyed synagogues and businesses and sent 30,000 men to camps. War brought ghettoisation, the Einsatzgruppen shootings in the east, and from the Wannsee Conference of January 1942 the systematic extermination of European Jewry in death camps, in which around six million people were murdered."
      },
      {
        h: "Stalin's economic revolution",
        b: "The Five-Year Plans from 1928 drove crash industrialisation with vast targets, showpiece projects such as Magnitogorsk and Dnieprostroi, and severe labour discipline. Collectivisation forced peasants into kolkhozes and destroyed the kulaks as a class. Resistance and grain requisitioning produced famine, most catastrophically in Ukraine in 1932-33, where millions died."
      },
      {
        h: "The Purges and the Show Trials",
        b: "The murder of Kirov in 1934 launched the Great Terror. The Moscow Show Trials of 1936-38 saw Old Bolsheviks — Zinoviev, Kamenev, Bukharin — confess publicly to fantastic charges of treason and sabotage after torture and threats to their families, then be shot. The officer corps was decimated and millions were sent to the Gulag. The trials were staged as public theatre to make the regime's version of reality unchallengeable."
      },
      {
        h: "Depression and democracy: the Jarrow March",
        b: "In Britain the Depression bore hardest on the old industrial regions. When Palmer's shipyard closed, male unemployment in Jarrow reached about 70%. In October 1936 two hundred men marched 300 miles to London with a petition, disciplined and non-political, accompanied by their MP Ellen Wilkinson. They were received without action, but the march became the enduring image of the 1930s and of democracy's failure to answer mass unemployment."
      },
      {
        h: "The Spanish Civil War",
        b: "Franco's nationalist rising against the Republic in July 1936 became a European conflict by proxy. Germany and Italy supplied aircraft and troops — Guernica was bombed by the Condor Legion in 1937 — while the USSR aided the Republic and the International Brigades drew volunteers from across the world. Britain and France pursued non-intervention. Franco won in 1939, and the war exposed the weakness of the democracies."
      },
      {
        h: "Appeasement and the road to war",
        b: "Hitler reintroduced conscription in 1935, remilitarised the Rhineland in 1936, and achieved Anschluss with Austria in March 1938, each time unopposed. At Munich in September 1938 Chamberlain and Daladier conceded the Sudetenland for 'peace for our time'; Hitler took the rest of Czechoslovakia in March 1939. The Nazi-Soviet Pact of August 1939 secured his eastern flank, and Germany invaded Poland on 1 September."
      },
      {
        h: "The Second World War in Europe",
        b: "Blitzkrieg overwhelmed Poland, Denmark, Norway, the Low Countries and France by June 1940. Britain survived the Battle of Britain and the Blitz. Operation Barbarossa in June 1941 opened the decisive front; the German surrender at Stalingrad in February 1943 and defeat at Kursk turned the war. D-Day in June 1944 opened the west, and with Soviet forces in Berlin Hitler killed himself on 30 April 1945."
      }
    ],

    // ── Europe Topic 4 — Division and realignment, 1945-1992 ────────────────
    'hist-eur4': [
      {
        h: "Yalta, Potsdam and the division of Germany",
        b: "At Yalta in February 1945 Roosevelt, Churchill and Stalin agreed to divide Germany into occupation zones and to hold free elections in liberated Europe. By Potsdam in July the personnel had changed to Truman and Attlee, the atomic bomb had been tested, and mutual suspicion was open. Germany and Berlin were divided into four zones, and 'free elections' in the east never materialised."
      },
      {
        h: "The origins of the Cold War",
        b: "Churchill described an 'iron curtain' descending across Europe in March 1946. The Truman Doctrine (1947) pledged support to peoples resisting subjugation, beginning with Greece and Turkey. The Marshall Plan offered around $13 billion for European recovery; Stalin forbade the eastern states to accept it and answered with Cominform and Comecon. Europe was divided economically as well as politically."
      },
      {
        h: "The Berlin Blockade and NATO",
        b: "When the western powers introduced a new currency in their zones, Stalin cut all land access to West Berlin in June 1948. The Allies supplied over two million people entirely by air for eleven months, at peak landing a plane every few minutes, until the blockade was lifted in May 1949. The crisis produced NATO in April 1949, the two German states that year, and the Warsaw Pact in 1955."
      },
      {
        h: "De-Stalinisation and Hungary, 1956",
        b: "Khrushchev denounced Stalin's crimes in a secret speech to the Twentieth Party Congress in 1956, raising hopes across the bloc. In Hungary, Imre Nagy's government announced withdrawal from the Warsaw Pact and multi-party elections. Soviet tanks crushed the rising in November; around 2,500 Hungarians died, 200,000 fled, and Nagy was executed. The West protested but did not intervene."
      },
      {
        h: "The Berlin Wall",
        b: "Around 2.7 million people left East Germany through Berlin between 1949 and 1961, disproportionately the young and skilled. On 13 August 1961 the border was sealed overnight with wire and then concrete. The Wall stopped the haemorrhage and stabilised the GDR, and it became the visual definition of the Cold War — Kennedy's 'Ich bin ein Berliner' in 1963 and Reagan's 'tear down this wall' in 1987."
      },
      {
        h: "The Prague Spring and the Brezhnev Doctrine",
        b: "Alexander Dubček's reforms from January 1968 promised 'socialism with a human face' — press freedom, rehabilitation of purge victims, economic decentralisation. Warsaw Pact forces invaded in August. The Brezhnev Doctrine asserted the right to intervene wherever socialism was threatened, and it defined the limits of change in the bloc until Gorbachev explicitly repudiated it."
      },
      {
        h: "Western European integration",
        b: "The Schuman Plan produced the European Coal and Steel Community in 1951, binding French and German heavy industry so that war between them became impracticable. The Treaty of Rome (1957) created the EEC of six, with a customs union and the Common Agricultural Policy. De Gaulle twice vetoed British entry; Britain, Ireland and Denmark joined in 1973, and the Community expanded southwards in the 1980s."
      },
      {
        h: "Ostpolitik and détente",
        b: "Willy Brandt as Chancellor from 1969 pursued reconciliation with the east, recognising the Oder-Neisse line and the existence of the GDR, and kneeling at the Warsaw Ghetto memorial in 1970. Détente produced the SALT agreements and the Helsinki Final Act of 1975, in which the West accepted existing borders in exchange for human rights commitments that dissident groups then used against their own governments."
      },
      {
        h: "Solidarity in Poland",
        b: "Strikes at the Lenin Shipyard in Gdańsk in August 1980 under Lech Wałęsa produced Solidarity, the first independent trade union in the bloc, which reached nearly ten million members. Martial law under General Jaruzelski suppressed it in December 1981, but it survived underground with support from the Church and from the Polish Pope John Paul II, and it returned to negotiate the transition in 1989."
      },
      {
        h: "Gorbachev: glasnost and perestroika",
        b: "Gorbachev took power in 1985 facing economic stagnation and an unsustainable arms burden. Perestroika restructured the economy and glasnost opened public discussion, accelerated by the Chernobyl disaster of 1986. He negotiated arms reductions with Reagan and, crucially, made clear that Soviet troops would not prop up the satellite regimes — removing the guarantee on which they depended."
      },
      {
        h: "1989 and the collapse of communism",
        b: "Hungary opened its border with Austria in May 1989, Poland held partly free elections in June, and the Berlin Wall opened on 9 November. Czechoslovakia's Velvet Revolution followed and Ceaușescu was overthrown and executed in Romania. Germany reunified in October 1990. An attempted coup against Gorbachev in August 1991 hastened the dissolution of the Soviet Union that December."
      },
      {
        h: "Maastricht and the new Europe",
        b: "The Maastricht Treaty of 1992 created the European Union, established the framework for a single currency, and added common foreign and security policy and justice cooperation to the existing economic community. It also set the terms on which the former communist states of central Europe would eventually seek membership, redrawing the continent's alignment for the following two decades."
      }
    ],

    // ── Europe Topic 5 — Retreat from empire, 1945-1990 ─────────────────────
    'hist-eur5': [
      {
        h: "Why empires ended after 1945",
        b: "The war exhausted the imperial powers financially and militarily, and the fall of Singapore and the Japanese occupation of South-East Asia destroyed the myth of European invincibility. Colonial troops who had fought for freedom abroad demanded it at home. Both superpowers were rhetorically anti-colonial, the UN Charter endorsed self-determination, and educated nationalist elites were ready to lead."
      },
      {
        h: "India and partition, 1947",
        b: "Gandhi's mass non-violent campaigns and Nehru's Congress had made British rule unsustainable, while Jinnah's Muslim League demanded a separate state. Mountbatten advanced independence to August 1947 and the subcontinent was partitioned into India and Pakistan on lines drawn in weeks. Around 12 million people were displaced and up to a million killed in communal violence; Gandhi was assassinated in January 1948."
      },
      {
        h: "France in Indochina",
        b: "France attempted to restore control after 1945 against Ho Chi Minh's Viet Minh. Defeat at Dien Bien Phu in May 1954, where a French garrison was besieged and overwhelmed by Giap's artillery in the surrounding hills, ended the war. The Geneva Accords divided Vietnam at the 17th parallel pending elections that were never held — opening the way to American involvement."
      },
      {
        h: "The Algerian War, 1954-62",
        b: "Algeria was constitutionally part of France with a million European settlers, which made withdrawal far harder than elsewhere. The FLN's guerrilla and urban campaign, met by the systematic use of torture in the Battle of Algiers, tore French politics apart, brought down the Fourth Republic and returned de Gaulle in 1958. He concluded the Evian Accords in 1962; independence followed, and nearly all the pieds-noirs left."
      },
      {
        h: "Ghana and the 'wind of change'",
        b: "Kwame Nkrumah's Convention People's Party won elections from prison, and the Gold Coast became Ghana in 1957, the first sub-Saharan colony to gain independence. Macmillan told the South African parliament in February 1960 that 'the wind of change is blowing through this continent'. Some seventeen African states became independent in 1960 alone."
      },
      {
        h: "The Congo crisis, 1960-65",
        b: "Belgium withdrew in June 1960 having done almost nothing to prepare a Congolese administration. Within weeks the army mutinied, Katanga seceded under Tshombe with Belgian mining backing, and the state collapsed. The UN deployed a large force in which Irish troops served, suffering losses at Niemba and fighting at Jadotville. Secretary-General Hammarskjöld died in an air crash in 1961, Lumumba was murdered, and Mobutu eventually seized power."
      },
      {
        h: "Kenya and the Mau Mau",
        b: "Settler control of the White Highlands and land hunger among the Kikuyu produced the Mau Mau insurgency from 1952. Britain declared an emergency and interned over 100,000 people in camps where abuse was systematic; the Hola camp deaths in 1959 caused a scandal at Westminster. Kenya became independent in 1963 under Jomo Kenyatta, who had been imprisoned as an alleged Mau Mau leader."
      },
      {
        h: "The Portuguese empire and Rhodesia",
        b: "Portugal fought long wars in Angola, Mozambique and Guinea-Bissau until the Carnation Revolution of April 1974 overthrew the Lisbon dictatorship, after which independence came rapidly and was followed by civil war. In Rhodesia, Ian Smith's white minority declared independence unilaterally in 1965; sanctions and a guerrilla war led to the Lancaster House settlement and majority-rule Zimbabwe in 1980."
      },
      {
        h: "Apartheid in South Africa",
        b: "The National Party took power in 1948 and legislated comprehensive racial separation: population registration, the Group Areas Act, pass laws and Bantu education. Opposition by the ANC met increasing repression, and the shooting of 69 protesters at Sharpeville in March 1960 led to the banning of the ANC and the turn to armed struggle. Mandela was imprisoned from 1962 and sentenced to life at the Rivonia Trial in 1964."
      },
      {
        h: "Soweto, sanctions and the end of apartheid",
        b: "The Soweto uprising of June 1976, triggered by compulsory instruction in Afrikaans, was met with gunfire and produced hundreds of deaths and a new generation of activists. International sports boycotts, disinvestment and sanctions tightened through the 1980s while the townships became ungovernable. De Klerk unbanned the ANC and released Mandela in February 1990, opening negotiations that ended apartheid."
      },
      {
        h: "The aftermath of empire",
        b: "New states inherited arbitrary borders, economies geared to exporting raw materials, and few trained administrators, and many slid into one-party rule or military government amid Cold War competition for allies. Critics described the resulting economic dependence as neo-colonialism. In Europe, decolonisation produced substantial migration from former colonies and reshaped the societies of Britain, France and the Netherlands."
      }
    ],

    // ── Europe Topic 6 — The United States and the world, 1945-1989 ─────────
    'hist-eur6': [
      {
        h: "Containment and the Truman Doctrine",
        b: "George Kennan's Long Telegram argued that Soviet hostility was inherent and should be met by patient containment. Truman applied it in March 1947, pledging support to Greece and Turkey, and then through the Marshall Plan, which was both humanitarian and strategic since prosperous democracies were thought unlikely to turn communist. NATO in 1949 committed the United States to Europe in peacetime for the first time."
      },
      {
        h: "The Korean War, 1950-53",
        b: "North Korea invaded the South in June 1950 and the UN, with the USSR boycotting the Security Council, authorised a response led by MacArthur. His landing at Inchon reversed the war, but the advance to the Yalu brought massive Chinese intervention. MacArthur was dismissed in 1951 for publicly urging escalation. The armistice of 1953 restored roughly the original line, at a cost of some three million lives."
      },
      {
        h: "McCarthyism and the Red Scare",
        b: "Fear of internal subversion, sharpened by the Soviet bomb, the fall of China and the Hiss and Rosenberg cases, produced the House Un-American Activities Committee hearings and blacklists in Hollywood. Senator Joseph McCarthy's unsubstantiated claims of communists in government dominated 1950-54 until the televised Army hearings exposed his methods and the Senate censured him."
      },
      {
        h: "Brinkmanship and the arms race",
        b: "Eisenhower and Dulles relied on massive retaliation and the readiness to go to the brink, which was cheaper than large conventional forces. Both sides tested hydrogen bombs and built intercontinental missiles, and the Soviet launch of Sputnik in 1957 caused alarm about a 'missile gap'. The shooting down of Gary Powers's U-2 over the USSR in 1960 wrecked the Paris summit."
      },
      {
        h: "Cuba: the Bay of Pigs and the Missile Crisis",
        b: "The CIA-backed invasion by Cuban exiles at the Bay of Pigs in April 1961 failed humiliatingly. In October 1962 U-2 photographs revealed Soviet medium-range missiles in Cuba. Kennedy imposed a naval quarantine and, after thirteen days that brought the world closer to nuclear war than at any other point, Khrushchev withdrew the missiles in exchange for a pledge not to invade Cuba and the quiet removal of US missiles from Turkey."
      },
      {
        h: "The civil rights movement to 1963",
        b: "Brown v. Board of Education (1954) ruled school segregation unconstitutional. Rosa Parks's arrest triggered the Montgomery bus boycott of 1955-56, in which the city's black population walked and car-pooled for 381 days until the Supreme Court struck down bus segregation — and which made Martin Luther King a national figure. Eisenhower sent troops to Little Rock in 1957, and the 1963 March on Washington drew 250,000 to hear King's 'I Have a Dream'."
      },
      {
        h: "Legislation, radicalism and division",
        b: "Johnson used his mastery of Congress and the shock of Kennedy's assassination to pass the Civil Rights Act (1964) outlawing segregation and the Voting Rights Act (1965) after the Selma marches. But northern ghettos gained little; riots swept Watts, Newark and Detroit. Malcolm X and later the Black Panthers rejected integration and non-violence, and King's murder in April 1968 was followed by rioting in over a hundred cities."
      },
      {
        h: "The Great Society",
        b: "Johnson's domestic programme declared war on poverty and produced Medicare and Medicaid, federal aid to education, Head Start, housing and immigration reform. It reduced poverty substantially, particularly among the elderly. Its funding, however, competed directly with the escalating cost of Vietnam, and Johnson's refusal to choose between guns and butter fuelled inflation and undermined both."
      },
      {
        h: "Vietnam",
        b: "The Gulf of Tonkin Resolution in 1964 gave Johnson effectively unlimited authority, and US strength rose above half a million by 1968 alongside the Rolling Thunder bombing campaign. The Tet Offensive in January 1968 was a military defeat for the communists but destroyed American confidence that the war was being won. Johnson declined to seek re-election; Nixon's Vietnamisation and the 1973 Paris accords preceded the fall of Saigon in 1975."
      },
      {
        h: "Protest and counterculture",
        b: "Opposition to the draft and the war radicalised campuses, from Berkeley's free speech movement to the shooting of four students at Kent State in 1970. The counterculture rejected consumer conformity through music, drugs and communal living, and the period also produced second-wave feminism, the environmental movement and, after Stonewall in 1969, gay liberation."
      },
      {
        h: "The Moon Landing",
        b: "Kennedy committed the United States in May 1961 to landing a man on the Moon before the decade ended, after the shock of Sputnik and Gagarin's flight. Apollo 11 landed on 20 July 1969, and Armstrong and Aldrin's moonwalk was watched by an estimated 600 million people. It was a Cold War victory as much as a scientific one, and the resulting technologies and images of the whole Earth had wide cultural effects."
      },
      {
        h: "Nixon, détente and Watergate",
        b: "Nixon and Kissinger opened relations with China in 1972, exploiting the Sino-Soviet split, and signed SALT I with Moscow. The break-in at the Democratic headquarters in the Watergate building in 1972 and the cover-up that followed were exposed by congressional hearings and the White House tapes, and Nixon resigned in August 1974 — the first president to do so, leaving lasting public distrust of government."
      },
      {
        h: "Reagan and the end of the Cold War",
        b: "Reagan denounced the USSR as an 'evil empire', launched a large military build-up and proposed the Strategic Defense Initiative in 1983, straining an already failing Soviet economy. From 1985 he and Gorbachev met repeatedly, and the INF Treaty of 1987 eliminated an entire class of missiles. By the time Reagan left office in 1989 the Cold War was ending, though its formal close came under his successor."
      }
    ]
  };

  [
    'hist-ire1', 'hist-ire2', 'hist-ire3', 'hist-ire4', 'hist-ire5', 'hist-ire6',
    'hist-eur1', 'hist-eur2', 'hist-eur3', 'hist-eur4', 'hist-eur5', 'hist-eur6',
  ].forEach(function (id) {
    var ch = chapters.find(function (c) { return c.id === id; });
    if (!ch || !ch.learningOutcomes.length) return;
    if (DB[id]) {
      ch.learningOutcomes[0].keyTerms = DB[id].map(function (card) {
        // `prompt` is the authored question the app shows; without it the app falls back to
        // rendering the bare term as the question. This map is a whitelist, so a field
        // omitted here is dropped no matter what the pipeline generated.
        return { term: card.term, prompt: card.prompt || '', definition: card.definition,
                 section: id, type: card.type || 'concept' };
      });
    }
    if (NOTES[id]) ch.learningOutcomes[0].notes = NOTES[id];
  });
})();
