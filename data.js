// LC Business Higher Level — Back In Business
// Notes & Exam-Style Questions, organised by Chapter & Learning Outcome

const COURSE_DATA = {
  meta: {
    course: "Leaving Certificate Business — Higher Level",
    textbook: "Back In Business",
    subtitle: "Chapter notes and exam practice"
  },
  chapters: [
    /* =================== CHAPTER 1 =================== */
    {
      id: "ch1",
      number: 1,
      strand: 1,
      title: "Key Stakeholders in Business",
      learningOutcomes: [
        {
          id: "lo1-1",
          code: "1.1",
          title: "Internal & external stakeholders and their importance",
          notes: [
            { h: "Definitions", b: "Internal stakeholders are individuals or groups directly involved in running the business (Owner/Entrepreneur, Managers, Employees, Investors). External stakeholders are not directly involved but are affected by the business's activities (Consumers, Local Community, Suppliers, Government, Interest Groups)." },
            { h: "Owner/Entrepreneur (Internal)", b: "Role: Identifies opportunities, secures funding, takes personal/financial risks. Importance: Provides leadership, vision and shoulders early risk. Needs/Wants: Financial success, recognition, independence and control. Example: Shane Curran raised €3m+ for cybersecurity start-up Evervault." },
            { h: "Managers (Internal)", b: "Role: Set objectives based on the entrepreneur's vision and organise resources. Importance: Coordinate daily operations, motivate staff, keep business focused. Needs/Wants: Resources, recognition, career progression. Example: Anne O'Leary became Head of Meta Ireland in 2023." },
            { h: "Employees (Internal)", b: "Role: Follow manager's instructions, share ideas, use skills daily. Importance: Provide time, experience and qualifications to keep the business productive. Needs/Wants: Fair pay, good conditions, respect, more responsibility over time." },
            { h: "Investors (Internal)", b: "Role: Provide funding for equity (ownership) or debt (banks, repayments + interest). Importance: Help the business grow; may bring contacts, experience, advice. Needs/Wants: Early-stage — accept higher risk, lower dividends; later — return through dividends, less risk. Example: Act Venture Capital, Enterprise Ireland." },
            { h: "Consumers (External)", b: "Role: Purchase goods/services, give feedback, advocate for the business. Importance: Drive revenue, shape brand reputation. Needs/Wants: Quality, value for money, good service, ethical/sustainable practices. Example: Patagonia commands premium prices because customers value its ethics." },
            { h: "Local Community (External)", b: "Role: People and area surrounding the business. Importance: Goodwill provides a base of customers and employees. Needs/Wants: Local jobs, access to goods/services, environmental and ethical responsibility." },
            { h: "Suppliers (External)", b: "Role: Provide raw materials, products or services the business uses. Importance: Reliable supply allows consistent production and quality. Needs/Wants: To be paid on time, longer-term contracts. Example: McDonald's sources 100% Irish beef." },
            { h: "Government (External)", b: "Role: Regulates business activity, provides grants/incentives, supports start-ups via LEOs and Enterprise Ireland. Importance: Funding, training, mentoring, infrastructure, lower taxes create a positive business climate. Needs/Wants: Compliance with laws, payment of tax, social responsibility, exports, job creation." },
            { h: "Interest Groups (External)", b: "Also called pressure or lobby groups. Role: Represent shared objectives of a group. Importance: Negotiate with and inform other stakeholders. Methods: Lobbying, media campaigns, protests, boycotts, legal action. Example: Small Firms Association (SFA) lobbied Government in 2024." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline two internal stakeholders and explain their importance in the business environment.", model: "**Owner/Entrepreneur**: Identifies market opportunities, secures funding and takes the risks involved in starting the business. They are crucial because they transform business ideas into viable operations and provide leadership and strategic vision.\n\n**Employees**: Use their skills to complete daily tasks set by management. They are essential as they bring experience, ideas and qualifications that keep the business productive and able to deliver to customers." },
            { type: "short", marks: 10, prompt: "Demonstrate the importance of a business's relationship with its (i) suppliers and (ii) government. (2 @ 5m: 3m relationship explained + 2m reasoning/application)", model: "**(i) Suppliers**: Suppliers provide the raw materials, products or services a business needs to produce its own goods. A strong relationship ensures consistent supply of quality inputs delivered on time, allowing the business to meet customer demand efficiently and avoid costly production delays.\n\n**(ii) Government**: Through bodies like the Local Enterprise Office (LEO) and Enterprise Ireland, the government provides funding, training, mentoring and grants. A good relationship with government gives the business access to expert advice and financial support that can improve its chances of early success and expansion." },
            { type: "short", marks: 4, prompt: "Outline how the needs and wants of an investor may change at different stages of business development.", model: "At the **start-up stage**, the investor may accept more risk and prioritise long-term growth, focusing on brand development and market entry; they may accept lower or no dividends.\n\nAt **maturity**, as the business becomes more stable, they want to see consistent profits and seek a return through dividends or expansion opportunities. Their focus shifts from growth potential to performance and steady returns." },
            { type: "mcq", marks: 2, prompt: "Which of the following is NOT an internal stakeholder?", options: ["Manager", "Employee", "Supplier", "Investor"], correct: 2, model: "Suppliers are external stakeholders — they are not directly involved in running the business but are affected by its activities." },
            { type: "tf", marks: 2, prompt: "Banks providing a loan to a business are considered internal investors who take ownership in the business.", correct: false, model: "False. A bank providing a loan supplies debt (repaid with interest) and does not take ownership. Investors who buy shares (equity) take ownership; lenders do not." },
            { type: "short", marks: 6, prompt: "List three external stakeholders and briefly state the role of each in a business.", model: "1. **Consumers** — Purchase goods/services and give feedback that shapes the brand.\n2. **Suppliers** — Provide raw materials and inputs needed to produce the business's goods/services.\n3. **Government** — Regulates business activity and provides supports such as grants and training through LEOs and Enterprise Ireland." }
          ]
        },
        {
          id: "lo1-2",
          code: "1.2",
          title: "How stakeholders interact and potential conflicts",
          notes: [
            { h: "Co-operative relationships (win–win)", b: "Both stakeholders mutually benefit from working towards a common goal. Examples: Employer & Employee — training boosts employee skills and business productivity. Investor & Owner — funding allows growth and profit for both. Producer & Producer — local producers share promotional costs (e.g. cheese festival)." },
            { h: "Competitive relationships (win–lose)", b: "Conflict arises when needs of stakeholders are mutually exclusive — one gains, the other loses. Examples: Employer wants to cut pay vs Employee wants a pay rise. Investor wants high dividends vs Manager wants to reinvest profits. Supplier wants quick payment vs Manager wants to delay payment to manage cash flow. Producer vs Producer — competing for the same customers." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Demonstrate how stakeholders can interact in (i) a co-operative way and (ii) a competitive way. Use one example for each.", model: "**(i) Co-operative**: An employer invests in staff training. The employees gain skills that allow them to earn promotion or pay rises, while the business benefits from more productive, capable workers. Both sides win.\n\n**(ii) Competitive**: An investor wants higher dividend payments from the business's profits, while the manager wants to reinvest those profits back into the business to fund expansion. If one side gets what it wants, the other loses out — it is a win-lose situation." },
            { type: "short", marks: 8, prompt: "Identify a potential conflict that might arise between an entrepreneur and (i) consumers and (ii) employees. (2 @ 4m)", model: "**(i) Consumers**: Consumers may want low prices and good value, but if the entrepreneur uses high-quality, ethical or sustainable inputs, costs are higher and the product becomes more expensive. This creates tension over pricing.\n\n**(ii) Employees**: Employees might want job security and predictable hours, but as a small start-up the entrepreneur may need flexibility, offer only part-time roles, or be unable to guarantee consistent work — leading to conflict over job security." },
            { type: "mcq", marks: 2, prompt: "Which of the following best describes a co-operative stakeholder relationship?", options: ["Employer cuts pay while employees demand a rise", "Investor demands dividends while manager reinvests profits", "Supplier and manager agree on payment terms that suit both", "Two competing producers fight for the same customers"], correct: 2, model: "A co-operative relationship is win-win, where both parties benefit. Agreed payment terms suit both supplier and manager." }
          ]
        },
        {
          id: "lo1-3",
          code: "1.3",
          title: "Avoiding and resolving conflict between stakeholders",
          notes: [
            { h: "Avoiding conflict", b: "**1. Open communication**: Honest, regular contact with stakeholders helps spot concerns early (e.g. fairly handling customer complaints). **2. Corporate Social Responsibility (CSR)**: Ethical decisions that balance profit with societal good (e.g. avoid unfair price hikes on loyal customers). **3. Stakeholder Involvement**: Include stakeholders in decisions (e.g. builders consulting local communities before major projects)." },
            { h: "Resolving conflict — methods", b: "**1. Meet & Talk**: Direct discussion (e.g. supplier and manager agree a realistic payment timeline). **2. Negotiation/Bargaining**: Both sides give and take (e.g. employee wants a 4-day week, owner wants output maintained — agree a trial with targets). **3. Mediation**: A neutral third party helps both sides reach their own agreement (e.g. local community and developer with a mediator). **4. Conciliation**: A third party suggests a possible solution that the parties may accept (e.g. phased dividend increase). **5. Arbitration**: Independent arbitrator hears both sides, reviews evidence, and makes a binding recommendation that both parties have agreed in advance to accept (e.g. unfair dismissal claim)." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Outline two strategies a business can use to avoid stakeholder conflict.", model: "**1. Open Communication**: Maintain honest, regular contact with stakeholders. By understanding concerns early — for example, by handling customer complaints fairly — small issues can be resolved before they grow into major disputes.\n\n**2. Stakeholder Involvement**: Include stakeholders in decision-making. For example, a building company consulting the local community before starting a major project reduces resistance and builds trust." },
            { type: "short", marks: 10, prompt: "Should a conflict arise with investors over the use of profits in a business, suggest two ways of resolving the conflict between an entrepreneur and their investors. (2 @ 5m: 2m method + 2m solution + 1m how it would work)", model: "**1. Negotiation/Bargaining**: The entrepreneur and investor meet directly and each makes compromises. For example, they could agree that 60% of profits are paid as dividends and 40% reinvested into the business. This works because both sides feel they have made gains — the investor receives a return, while the business still has funds to grow.\n\n**2. Conciliation**: A neutral third party listens to both sides and suggests a possible compromise, such as a phased increase in dividends over three years as profits grow. The conciliator helps both parties move closer to agreement themselves rather than imposing a binding decision." },
            { type: "short", marks: 5, prompt: "Distinguish between mediation and arbitration as methods of resolving stakeholder conflict.", model: "**Mediation**: A neutral third party (the mediator) helps both sides reach their own agreement by improving communication. The mediator does not make a decision — the parties find their own solution.\n\n**Arbitration**: An independent arbitrator hears both sides and reviews the evidence, then issues a recommendation. Both parties agree in advance to accept the arbitrator's decision, which is binding." },
            { type: "mcq", marks: 2, prompt: "In which conflict resolution method is the third party's decision binding on both sides?", options: ["Mediation", "Conciliation", "Arbitration", "Negotiation"], correct: 2, model: "Arbitration produces a binding recommendation that both parties have agreed in advance to accept." }
          ]
        },
        {
          id: "lo1-4",
          code: "1.4",
          title: "Stakeholder mapping and prioritising stakeholder interests",
          notes: [
            { h: "What stakeholder mapping is", b: "A business measures the **interest** (how affected they are) and **influence/power** (how much they can change a decision) of each stakeholder, to decide who to prioritise when making decisions." },
            { h: "Steps in stakeholder mapping", b: "**1. Identify stakeholders** — list all groups affected, internal and external. **2. Analyse power and interest** — judge the level of influence and interest of each group. **3. Map to a Power–Interest grid** — High/Low Power on one axis, High/Low Interest on the other. **4. Allocate resources & plan engagement** — focus most attention on stakeholders with both high power and high interest." },
            { h: "Importance of stakeholder mapping", b: "**1. Improves decision-making quality**: Helps a business consider all viewpoints before deciding (e.g. a bank may delay branch closures after mapping shows high impact on older customers). **2. Supports strategic planning**: Helps plan long-term actions and avoid surprises (e.g. during expansion, a company maps which stakeholders to engage early — local councils, investors)." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "A bakery is planning a major expansion. Conduct stakeholder mapping to identify and prioritise four stakeholders affected by this decision. (4 @ 3m)", model: "**1. Employees — High Interest, High Power**: Their hours and roles will change directly, and as a unionised group they can resist or support the change. **Priority: Manage closely** — consult and involve them.\n\n**2. Customers — High Interest, Low Power**: Affected by changes to product range/prices but limited influence individually. **Priority: Keep informed** with clear communication.\n\n**3. Local Community — Low Interest, Low Power**: May notice change but unlikely to act. **Priority: Monitor** with minimal engagement.\n\n**4. Investors — High Interest, High Power**: They have funded the expansion and have a direct say in major decisions. **Priority: Manage closely** — frequent updates, involvement in key decisions." },
            { type: "short", marks: 10, prompt: "Explain the importance of prioritising different stakeholder interests when making decisions in a business.", model: "**1. Improves decision-making quality**: Mapping forces the business to look at all viewpoints before making a decision. This means choices balance the needs, concerns and power of different groups, leading to fewer disputes and better outcomes. For example, a bank may delay a rural branch closure after mapping shows older customers with low digital access would be heavily impacted.\n\n**2. Supports strategic planning**: Stakeholder mapping helps plan long-term actions by clarifying who to engage and when, reducing surprises. For example, during expansion a company maps which stakeholders — such as local councils or investors — to involve early to smooth the path." },
            { type: "tf", marks: 2, prompt: "On a Power–Interest grid, stakeholders with high power and high interest should receive minimal attention from management.", correct: false, model: "False. Stakeholders with high power and high interest should be 'managed closely' — they are the most important group and require frequent communication and involvement in decisions." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 6 =================== */
    {
      id: "ch6",
      number: 6,
      strand: 2,
      title: "Enterprise in Action",
      learningOutcomes: [
        {
          id: "lo6-1",
          code: "6.1",
          title: "Innovation, intrapreneurship & entrepreneurship — and importance of innovation",
          notes: [
            { h: "Definitions", b: "**Innovation**: Coming up with something new or better — a product, service, process, way of selling, or way of earning revenue. **Intrapreneur**: An employee who brings new ideas to life within an existing business; takes no personal financial risk but acts creatively. **Entrepreneurship**: When someone takes personal/financial risk to create or grow a business or social enterprise." },
            { h: "Examples", b: "**Entrepreneur**: Hannah Joyce setting up Flexera (home pilates equipment). **Intrapreneur**: A SuperValu deli team member proposing a 'grab & go breakfast box' that gets rolled out. **Innovation**: Netflix moving from DVDs to streaming." },
            { h: "Reasons for starting an enterprise", b: "**Personal motives**: Be your own boss, need for achievement, redundancy. **Financial motive**: Earn more income. **Societal motive**: Solve a social problem (e.g. We Make Good)." },
            { h: "Importance of innovation for business", b: "1. **Gain competitive advantage** — stand out with better/cheaper/unique products. 2. **Expand into new markets** — digital tools reach global customers. 3. **Improve efficiency** — AI/automation reduce costs and speed up delivery." },
            { h: "Importance for the economy", b: "1. **Drives economic growth** — more productivity, GDP, tax revenue. 2. **Creates jobs** — new industries (green tech, digital health), regional employment. 3. **Boosts exports** — Irish solutions to global problems (e.g. LetsGetChecked)." },
            { h: "Importance for society", b: "1. **Solves social challenges** — homelessness, addiction, digital exclusion. 2. **Supports environmental goals** — circular packaging, sustainable production. 3. **Empowers communities** — provides tools, funding, support to solve local problems." }
          ],
          questions: [
            { type: "mcq", marks: 4, prompt: "An engineer at Sony, Ken Kutaragi, met initial resistance for his idea to create a console to rival Nintendo. He convinced Sony to fund it and the PlayStation launched in 1994. This is an example of:", options: ["Entrepreneurship", "A circular economy", "Intrapreneurship", "A franchise"], correct: 2, model: "Intrapreneurship — Kutaragi was an employee who developed a new idea inside an existing business, without taking personal financial risk." },
            { type: "short", marks: 6, prompt: "Distinguish between innovation, entrepreneurship and intrapreneurship, with one example of each.", model: "**Innovation** is coming up with something new or better — a product, service or process. *Example*: Netflix switching from DVD rental to streaming.\n\n**Entrepreneurship** is when someone takes personal or financial risk to create or grow a business. *Example*: Hannah Joyce setting up Flexera, a pilates equipment business.\n\n**Intrapreneurship** is when an employee brings new ideas to life within an existing business, without taking personal financial risk. *Example*: A SuperValu deli employee proposing the 'grab & go breakfast box' that was rolled out across stores." },
            { type: "short", marks: 9, prompt: "Outline three benefits of innovation for the Irish economy.", model: "**1. Drives economic growth**: Innovation increases business productivity and GDP, generating more tax revenue that funds public services like healthcare and education.\n\n**2. Creates jobs**: New industries such as green tech and digital health offer future-proof careers and regional employment, reducing reliance on traditional sectors.\n\n**3. Boosts exports**: Irish innovations can solve global problems and earn foreign income — for example, LetsGetChecked exports its at-home diagnostic services internationally, strengthening Ireland's global business reputation." },
            { type: "short", marks: 4, prompt: "Outline two reasons, other than financial motives, why someone might start their own enterprise.", model: "**1. To be their own boss**: They want control, independence and the ability to make all decisions about how the business is run.\n\n**2. To solve a social problem**: They want to tackle inequality, support sustainability or create ethical products — for example, We Make Good employs vulnerable groups in Dublin." }
          ]
        },
        {
          id: "lo6-2",
          code: "6.2",
          title: "Competencies of innovators",
          notes: [
            { h: "What are competencies?", b: "Competencies are the integration of knowledge, skills, values and dispositions that support and foster innovation." },
            { h: "Key competencies", b: "**Risk-Taker** — takes personal and financial risks. **Creative** — thinks outside the box, generates new ideas, spots gaps. **Decision-making** — analyses data, consults others, makes good choices under pressure. **Proactive** — uses initiative to seize opportunities, doesn't wait. **Realistic** — sees situations as they are without bias. **Resilient** — determined to overcome failure. **Human Relations** — communicates well, builds networks. **Independent** — confident making decisions without constant reassurance. **Flexible** — adapts to change and feedback. **Time Management** — prioritises tasks and uses resources efficiently." },
            { h: "Why competencies matter when starting/expanding", b: "**Risk-taking** is essential when entering uncertain markets. **Creative thinking** helps develop unique products. **Resilience** keeps the entrepreneur going through early failures. **Flexibility** is vital in fast-changing markets during growth. **Time management** matters when juggling responsibilities in early-stage businesses." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Identify four key competencies that innovators such as a successful Irish entrepreneur possess.", model: "**1. Risk-Taker** — willing to take personal and financial risks to pursue an idea.\n**2. Creative** — thinks differently, generates new ideas, sees gaps in the market.\n**3. Decision-making** — analyses data, consults the right people and makes good choices under pressure.\n**4. Proactive** — uses initiative to seize opportunities and does not wait to respond." },
            { type: "short", marks: 5, prompt: "Identify one competency of innovators and outline its importance when starting or expanding a business.", model: "**Resilience**: Resilient innovators don't give up easily and are determined to overcome setbacks.\n\nThis competency is vital when starting or expanding a business because new and growing businesses face many early failures — products may not sell, funding may be refused, or customers may be slow to commit. A resilient entrepreneur keeps adjusting their approach and pushing forward instead of giving up, which gives the business the best chance of long-term success." },
            { type: "mcq", marks: 2, prompt: "Which competency best describes someone who builds strong networks and communicates effectively to gain support and funding?", options: ["Independent", "Human Relations", "Time Management", "Realistic"], correct: 1, model: "Human Relations is the competency of building networks and communicating well — this supports funding, loyalty and team-building." }
          ]
        },
        {
          id: "lo6-3",
          code: "6.3",
          title: "Role of government in supporting enterprise",
          notes: [
            { h: "How government creates a positive business climate", b: "**Planning**: Stable budgets and wage agreements encourage investment. **Capital Expenditure**: Spending on infrastructure (roads, schools) creates jobs and demand. **Current Expenditure**: Increases in public sector pay and welfare boost disposable income and sales. **Taxation/Funding**: Low corporation tax, tax breaks and grants. **Education & Training**: Investment in SOLAS and free third-level education builds skilled labour." },
            { h: "Local Enterprise Offices (LEOs)", b: "Promote entrepreneurship locally and support start-ups/small businesses. Services: **Training** (online and in-person, e.g. Start Your Own Business), **Mentoring** (1-on-1 with experienced mentors), **Financial support** (Feasibility and Expansion grants; loans up to €50,000 via Microfinance Ireland), **Networking** events." },
            { h: "Other local supports", b: "**Microfinance Ireland**: Loans of €2,000–€50,000 for businesses unable to get bank funding. **Leader**: Funds rural job-creation and sustainability projects. **SOLAS**: Training and education for the labour market. **Area Partnership Companies (APCs)**: Support local entrepreneurs solving community problems." },
            { h: "Enterprise Ireland (national level)", b: "Government agency for Irish-owned businesses aiming to grow internationally (10+ employees, exporting/scaling). Services: **Funding** (grants and equity); **30+ International Offices**; **R&D support**; **Market Research Centres**; **Trade fairs and missions abroad**." },
            { h: "National Enterprise Hub", b: "Launched in 2024. One-stop shop centralising 180+ supports from 19+ state bodies. Personalised help via web, phone or live chat." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Discuss three ways the Irish government can support businesses such as a tech start-up. (3 @ 4m)", model: "**1. Local Enterprise Offices (LEOs)**: LEOs offer training, mentoring and grants to start-ups and small businesses. A tech start-up could access the 'Start Your Own Business' programme and apply for a Feasibility Grant to test whether their idea is viable.\n\n**2. Enterprise Ireland**: Once the start-up grows, EI provides equity investment, R&D supports and access to over 30 international offices. This helps the start-up scale into export markets and connect with overseas buyers.\n\n**3. Microfinance Ireland**: For businesses that cannot access traditional bank loans, Microfinance Ireland provides loans of between €2,000 and €50,000. This is especially useful for tech start-ups that have limited assets to use as collateral." },
            { type: "short", marks: 6, prompt: "Describe two supports the Irish government can provide to a new entrepreneur.", model: "**1. Mentoring through the LEO**: The Local Enterprise Office matches the entrepreneur with an experienced mentor for one-on-one support in business planning, strategy, finance and market research, helping them avoid common early mistakes.\n\n**2. Feasibility Grants**: The LEO provides Feasibility Grants to help the entrepreneur research and test whether their idea is viable before investing significant amounts of their own money — this reduces risk and improves chances of success." },
            { type: "short", marks: 5, prompt: "Name one state agency, other than Enterprise Ireland, that supports business and enterprise in Ireland and explain how it supports new business start-ups.", model: "**Microfinance Ireland**: Supported by the Irish government, it assists businesses struggling to secure a loan from a traditional lender. It offers loans of between €2,000 and €50,000 to new and expanding businesses that cannot access bank funding. This investment supports start-ups by providing the working capital they need to launch — for things like buying stock, equipment or marketing — improving their cashflow and chances of survival in the early stages." },
            { type: "tf", marks: 2, prompt: "Enterprise Ireland focuses primarily on supporting Irish-owned businesses that are looking to expand internationally.", correct: true, model: "True. Enterprise Ireland supports Irish-owned businesses with 10+ employees that are looking to expand exports, scale operations and innovate for long-term success." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 7 =================== */
    {
      id: "ch7",
      number: 7,
      strand: 2,
      title: "Idea Development",
      learningOutcomes: [
        {
          id: "lo7-1",
          code: "7.1",
          title: "Factors impacting idea development",
          notes: [
            { h: "Internal sources of business ideas", b: "**Hobbies & Interests** (Dyson founder created bagless vacuum from frustration). **Skills & Experience**. **Invention & R&D**. **Brainstorming** (no idea off limits). **Intrapreneurship** (Sony's Ken Kutaragi developing PlayStation)." },
            { h: "External sources of business ideas", b: "**Customers** — asking what people want. **Competitors** — improving or localising what works elsewhere. **Market Research** — surveys, interviews, social listening. **Import Substitution** — homegrown alternative to imported product." },
            { h: "Factors influencing idea development", b: "**Organisational Culture** — leadership shapes willingness to share ideas (Steve Jobs, Apple). **Availability of Resources** — time/funding/skills (Google's 20% time). **Market Trends & Consumer Behaviour** (move from plastic → eco-friendly products). **Technological Advancements** (smartphones enabled Deliveroo, Just Eat). **Legal Requirements** — outdated laws can block ideas (modular homes need legal change)." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Determine four factors that impact on the development of business ideas.", model: "**1. Organisational Culture**: A leadership style that encourages risk-taking and creativity (e.g. Apple under Steve Jobs) helps new ideas emerge from within the business.\n\n**2. Availability of Resources**: Without time, funding or skilled people, ideas struggle to develop. Google encourages innovation by giving employees 20% of their time to work on new concepts.\n\n**3. Market Trends and Consumer Behaviour**: Shifts in customer habits create opportunities — for example, the move away from single-use plastic opened the market for eco-friendly products like paper straws.\n\n**4. Technological Advancements**: New technology unlocks entire industries — smartphones enabled app-based services like Deliveroo and Just Eat that simply weren't profitable before." },
            { type: "short", marks: 4, prompt: "Outline two internal sources from which a business idea may come.", model: "**1. Hobbies and Interests**: Ideas can emerge from personal passion or solving problems the entrepreneur has experienced. Dyson's founder invented the bagless vacuum out of frustration with his own vacuum cleaner.\n\n**2. Brainstorming**: Team-based idea generation where no idea is off-limits. This combines different perspectives within the business and can spark innovative ideas." }
          ]
        },
        {
          id: "lo7-2",
          code: "7.2",
          title: "Design thinking — iterative, person- and solution-centred",
          notes: [
            { h: "What is design thinking?", b: "An innovative, non-linear approach to developing products and services that focuses on solutions for the end user." },
            { h: "Three characteristics", b: "**Person-centred**: Understands the user's real problems and empathises before designing solutions. **Solution-centred**: Defines the problem clearly and explores creative ways to solve it, beginning with the desired outcome. **Iterative**: Repeated cycles of prototyping, testing, refining and retesting until a practical, user-approved solution emerges." },
            { h: "The four phases", b: "**1. Clarify** — gain a deep understanding of the current problem from the user's perspective (surveys, observation, research). **2. Ideate** — creative brainstorming sessions to explore multiple potential solutions. **3. Develop** — turn top ideas into early prototypes (sketches or first working models) to test functionality. **4. Implement** — test prototypes with real users, gather feedback, refine repeatedly." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Outline how a business can use each of the four phases of design thinking to successfully develop a new product. (4 @ 3m)", model: "**1. Clarify**: The business gains a deep understanding of the user's problem through surveys, observation and interviews — for example, asking parents what frustrates them about existing kids' products.\n\n**2. Ideate**: Hold creative brainstorming sessions to explore multiple solutions, with no idea ruled out at this stage.\n\n**3. Develop**: Turn the strongest ideas into early prototypes — sketches or basic working models — to test how they look and function.\n\n**4. Implement**: Test prototypes with real users, gather feedback and refine repeatedly until the product meets users' needs and is ready to launch." },
            { type: "short", marks: 6, prompt: "Explain what is meant by design thinking being 'person-centred', 'solution-centred' and 'iterative'.", model: "**Person-centred**: It focuses on understanding the real problems of the end user and empathising with them before generating solutions, so the design genuinely meets user needs.\n\n**Solution-centred**: The process clearly outlines the problem the product or service will solve from the start and explores creative ways to deliver the desired outcome.\n\n**Iterative**: The process uses repeated cycles of prototyping, testing, refining and retesting — re-visiting earlier steps again and again until a user-approved solution emerges." }
          ]
        },
        {
          id: "lo7-3",
          code: "7.3",
          title: "Conducting a feasibility study",
          notes: [
            { h: "What is a feasibility study?", b: "A check on whether an idea is workable, profitable and sustainable before investing time and money. Doing this early saves resources and helps avoid launching something that won't succeed." },
            { h: "Areas of feasibility", b: "**Financial**: Cost to start/run vs expected income; break-even, startup costs. *Can it make a profit?* **Market**: Is there demand? Surveys, interviews assess market size. *Will customers want it?* **Production**: Can it be built/delivered with available resources, skills, equipment? *Can we make it?* **Legal**: Does it meet current laws/regulations? *Are there any legal obstacles?* **Environmental**: Impact on environment, sustainability, materials, emissions, waste. *Will it meet environmental standards?*" }
          ],
          questions: [
            { type: "short", marks: 5, prompt: "Explain one function of a feasibility study when developing a new business idea.", model: "**Tests financial feasibility**: A feasibility study estimates the start-up costs, ongoing costs and expected income, and calculates whether the business can reach a break-even point and earn a profit. This allows the entrepreneur to know whether the idea is financially viable before committing significant time and money — saving resources if the idea cannot make money, or strengthening the case for funding if it can." },
            { type: "short", marks: 12, prompt: "Outline four areas a business should assess when conducting a feasibility study on a new product idea. (4 @ 3m)", model: "**1. Market Feasibility**: Researches whether customers actually want the product through surveys and interviews, and assesses market size and competitors. Key question: Is there real demand?\n\n**2. Financial Feasibility**: Compares the cost to start and run the business with expected income, calculating break-even and required cash. Key question: Can it make a profit?\n\n**3. Production Feasibility**: Assesses whether the product can actually be built or delivered with available skills, equipment and technology. Key question: Can we make it?\n\n**4. Legal Feasibility**: Checks if the idea meets current laws and regulations or if there are planning, safety or industry rules that would block it. Key question: Are there any legal obstacles?" },
            { type: "tf", marks: 2, prompt: "Environmental feasibility looks at whether a business idea aligns with sustainability goals and meets environmental standards.", correct: true, model: "True. Environmental feasibility assesses the potential impact on the environment — including materials, emissions, energy use and waste — and whether the idea aligns with sustainability expectations." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 8 =================== */
    {
      id: "ch8",
      number: 8,
      strand: 2,
      title: "Business Planning",
      learningOutcomes: [
        {
          id: "lo8-1",
          code: "8.1",
          title: "Importance and key functions of a business plan",
          notes: [
            { h: "What is a business plan?", b: "A written document that outlines what a business wants to achieve and how it will achieve it. It clarifies the idea, sets goals, attracts funding, assesses market size, and identifies risks." },
            { h: "Sections of a business plan", b: "**1. Executive Summary** — short persuasive overview of the business, why it will succeed, key financials. **2. Market Analysis** — trends, competitors, target market. **3. Sales & Marketing** — how the business will reach the target market and drive sales. **4. Financial Plan** — projected income, costs (fixed/variable), cash flow forecasts, profit. **5. Production Plan** — how goods/services will be produced, machinery, timelines. **6. Operational Plan** — daily operations, staffing, stock, working hours. **7. Business Model Canvas** — one-page summary of how value is created and delivered (9 boxes)." },
            { h: "Importance at different stages", b: "**Start-up**: Clarifies idea and value proposition, secures early funding. Key sections: Executive Summary, Market Analysis, BMC, Financial Plan. **Growth/Expansion**: Guides expansion decisions, shows growth potential. Key sections: Sales & Marketing, Financial Plan (revised). **Maturity**: Supports day-to-day efficiency and long-term planning. Key sections: Operational Plan, Production Plan, Financial Plan." },
            { h: "Value Proposition", b: "A short, clear statement explaining what a product/service is, who it is for, and the range of benefits that make it better than alternatives. Example (All Real Nutrition): 'A bar high in protein and made from real, natural ingredients while supporting Irish suppliers and sustainability, with zero plastic packaging.'" }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline four key functions of a business plan.", model: "**1. Clarifies the business idea** — Forces the entrepreneur to think through how the business will work, including its value proposition.\n\n**2. Helps secure funding** — Banks, investors and the LEO use the plan to assess whether to lend or invest.\n\n**3. Sets goals and benchmarks** — Sales, profit and growth targets allow the business to measure performance.\n\n**4. Identifies risks and challenges** — The planning process forces the business to think about competitors, costs and potential threats so they can prepare contingency plans." },
            { type: "short", marks: 5, prompt: "Explain how a business plan can contribute to the success of a new business.", model: "A business plan contributes to success in several connected ways. First, it forces the entrepreneur to clarify the value proposition and confirm that customers want the product, reducing the risk of launching an unviable idea. Second, the financial plan within it (with projected costs, sales and cashflow) is essential to securing finance from banks, investors or the LEO. Finally, it provides clear goals against which the business can benchmark performance — for example, monthly sales targets — allowing it to spot problems early and make timely adjustments." },
            { type: "mcq", marks: 2, prompt: "Which section of the business plan provides a short persuasive overview, including key financial highlights and reasons the business will succeed?", options: ["Market Analysis", "Operational Plan", "Executive Summary", "Production Plan"], correct: 2, model: "The Executive Summary is the short, persuasive overview at the start of the plan." }
          ]
        },
        {
          id: "lo8-2",
          code: "8.2",
          title: "Ethics and sustainability in business planning",
          notes: [
            { h: "Why ethics & sustainability matter in planning", b: "**1. Builds trust and brand loyalty** — customers value businesses that stand for more than profit (highlighted in Executive Summary and Sales & Marketing sections). **2. Helps attract investment** — many investors apply ESG criteria (Environmental, Social, Governance). Businesses that demonstrate responsible practice in the Financial Plan and Risk sections are more likely to secure funding. **3. Avoids legal and reputational risks** — planning compliance into the Operations and Production Plans reduces the risk of fines, scandals and reputation damage. **4. Supports long-term profitability** — businesses with ethics built into their Financial Plan are more resilient and adaptable to changing regulations and customer expectations." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Outline three benefits to a business of incorporating ethics and sustainability into its business planning. (3 @ 4m)", model: "**1. Builds Trust and Brand Loyalty**: When ethical values and sustainability goals are highlighted in the Executive Summary and Sales & Marketing sections, customers see the business stands for more than profit. This builds long-term loyalty and brand advocacy.\n\n**2. Helps Attract Investment**: Modern investors often apply ESG (Environmental, Social, Governance) criteria. Businesses showing responsible practices in their Financial Plan and Risk sections are more likely to secure funding and long-term backing.\n\n**3. Supports Long-Term Profitability**: Sustainable businesses are more resilient to changing regulations, resource constraints and customer expectations — helping them stay competitive over the long run." },
            { type: "short", marks: 5, prompt: "Outline how sustainability planning can reduce risks for a business.", model: "Building sustainability into the Operations Plan and Production Plan reduces the chance that the business will breach environmental laws, face fines or be linked to unethical behaviour. For example, sourcing from certified suppliers ensures compliance with regulations and protects against scandals that could be costly to recover from. By planning compliance from the outset, the business reduces both legal risk and reputational damage." }
          ]
        },
        {
          id: "lo8-3",
          code: "8.3",
          title: "What a business model is and its role in the business plan",
          notes: [
            { h: "Definition", b: "A business model is an element within the business plan that outlines how a company will operate, create, deliver and capture value." },
            { h: "Role of business model", b: "It explains how a business will: **1. Create value** — the product/service that solves a problem. **2. Deliver value** — how it reaches and serves customers. **3. Earn revenue** — one-off, subscription, ads, etc. Example: Spotify creates value through music streaming, delivers it via an easy-to-use app, and earns revenue through subscriptions and ads." },
            { h: "Examples of business models", b: "Retail (Penneys, Zara), Marketplace (Airbnb, DoneDeal), Franchise (Supermac's, McDonald's), Subscription (Netflix, Spotify, Adobe)." }
          ],
          questions: [
            { type: "short", marks: 5, prompt: "Explain what is meant by a 'business model' and describe its role within a business plan.", model: "A **business model** outlines how a company will operate, create, deliver and capture value. Within the business plan, it explains the three core questions: how the business creates value (the product or service that solves a customer problem), how it delivers value (how it reaches and serves the customer), and how it earns revenue (one-off sales, subscription, advertising, commission, etc.). For example, Spotify creates value through music streaming, delivers it via its easy-to-use app, and earns revenue through subscriptions and ads. The business model gives investors and the entrepreneur a clear understanding of how the business will make money." }
          ]
        },
        {
          id: "lo8-4",
          code: "8.4",
          title: "Business Model Canvas (BMC)",
          notes: [
            { h: "What it is", b: "A one-page tool used to map out a business model on 9 connected building blocks." },
            { h: "The 9 elements", b: "**1. Key Partners** — suppliers, software providers, couriers, producers. **2. Key Activities** — design, marketing, customer service. **3. Key Resources** — IP, patents, key staff, premises. **4. Value Proposition** — the 'why' a customer would choose this product/service. **5. Customer Relationships** — managing interactions (social media, in-store). **6. Customer Segments** — target market and other groups served. **7. Customer Channels** — how the customer is reached (online, store, email). **8. Revenue Streams** — how income is earned (sales, subscription, ads). **9. Cost Structure** — fixed and variable costs of running the business." }
          ],
          questions: [
            { type: "short", marks: 9, prompt: "Identify three key elements of the Business Model Canvas and explain the role of each.", model: "**1. Value Proposition**: The bundle of benefits a product or service offers customers — the 'why' a customer would choose this business over alternatives. It is the heart of the BMC, with all other elements supporting it.\n\n**2. Revenue Streams**: How the business generates income — direct sales, recurring subscriptions, advertising, commission, etc. This shows how the business will sustain itself financially.\n\n**3. Key Partners**: External organisations the business relies on — suppliers, software providers, logistics firms. These ensure the business can deliver its value proposition smoothly to customers." },
            { type: "tf", marks: 2, prompt: "The Business Model Canvas summarises the business model on a single page across nine sections including Key Partners, Value Proposition and Revenue Streams.", correct: true, model: "True. The BMC is a one-page summary across 9 building blocks." }
          ]
        },
        {
          id: "lo8-5",
          code: "8.5",
          title: "Common business models",
          notes: [
            { h: "Retailer", b: "Buys at wholesale prices and sells higher to consumers, online or in-store (Dunnes, Lifestyle Sports). Value: convenience, choice, loyalty rewards (Tesco Clubcard)." },
            { h: "Manufacturer", b: "Makes goods from raw materials and sells to retailers (B2B — Intel) or directly to consumers (B2C — Nike.com). Value: innovation, efficiency through cost-effective production." },
            { h: "Subscription", b: "Recurring payments — monthly or annual (Sky TV, Virgin broadband). Value: continuous access, customisation, flexibility to cancel." },
            { h: "Franchise", b: "Franchisor licenses brand, logo, systems, products to franchisees in exchange for fees and a % of revenue/profits (McDonald's, Insomnia Coffee). Value: brand consistency, increased availability across locations." },
            { h: "Affiliate", b: "Affiliates earn commission when their content drives a sale (TikTok influencers promoting Gymshark, Amazon links). Value: leverages influencer trust and targeted marketing." }
          ],
          questions: [
            { type: "short", marks: 5, prompt: "Describe the franchise business model.", model: "In a **franchise**, the franchisor grants a licence to a franchisee to operate branches under the franchisor's brand, logo, systems and products. The franchisee pays an upfront fee plus an ongoing percentage of revenue or profits. *Example: McDonald's, Insomnia Coffee*. Value is created through brand consistency — customers receive a familiar product across all locations — and through increased availability, as the brand can scale quickly through the franchisees' investment." },
            { type: "short", marks: 6, prompt: "Compare the retailer and manufacturer business models, referring to how each generates revenue.", model: "**Retailers** buy products at wholesale prices from suppliers/manufacturers and sell them at a higher price (markup) to consumers, either online or in-store (e.g. Dunnes Stores). Their revenue comes from the margin between buying and selling price, and they create value through convenience, choice and loyalty schemes.\n\n**Manufacturers** make goods from raw materials and sell them at a profit, either to retailers (B2B — e.g. Intel selling chips to Dell) or directly to consumers (B2C — e.g. Nike.com). Their revenue comes from converting cheaper inputs into higher-value finished goods. They create value through innovation and efficient production allowing competitive pricing." }
          ]
        },
        {
          id: "lo8-6",
          code: "8.6",
          title: "Digital technology as a driver of change",
          notes: [
            { h: "Internal change drivers", b: "**1. Innovation & Product Development** — apps and social media for personalised shopping (ASOS). **2. Efficiency & Automation** — robots and inventory systems (Amazon). **3. Data-Driven Decisions** — Netflix uses AI to track viewing and choose new shows. **4. Employee Collaboration** — Slack, Notion enable global teamwork." },
            { h: "External change drivers", b: "**5. Changing Consumer Behaviour** — convenience, personalisation, speed (Gymshark uses TikTok feedback). **6. Competitive Pressure** — digital-first disruptors (Uber forced taxi firms to launch apps). **7. Globalisation** — Shein uses digital payments and translation tools. **8. Brand Image and Public Engagement** — Ryanair shapes brand using humour and social trends." }
          ],
          questions: [
            { type: "short", marks: 9, prompt: "Outline three ways digital technology drives change in business.", model: "**1. Efficiency and Automation**: Businesses automate processes using AI and robotics to save time, cut costs and reduce errors. Amazon uses warehouse robots and automated inventory systems to fulfil orders much faster than manual workers could.\n\n**2. Data-Driven Decisions**: Businesses can collect and analyse huge amounts of customer data in real time. Netflix uses AI to track viewing habits and decide which new shows to produce and recommend, increasing both engagement and retention.\n\n**3. Changing Consumer Behaviour**: Digital platforms have raised customer expectations for speed, personalisation and convenience. Gymshark uses TikTok to get rapid feedback on products and adjust quickly — businesses that don't adapt risk losing customers to digital-first rivals." }
          ]
        },
        {
          id: "lo8-7",
          code: "8.7",
          title: "Technology-driven business models",
          notes: [
            { h: "Marketplace (Vinted, Deliveroo, DoneDeal, Airbnb)", b: "**Revenue**: Charges fees or commission on transactions between buyers and sellers. **Access/Cost**: Usually free for users; sellers may pay listing fees. **Scalability**: Highly scalable — no need to own stock/property; grows as users join. **Engagement**: Reviews, ratings, personalised suggestions build trust." },
            { h: "Subscription (Netflix, Spotify, Strava)", b: "**Revenue**: Recurring monthly or annual payments; some offer ad-supported tiers. **Access/Cost**: Customers pay for continued access; freemium offers limited free access with paid upgrades. **Scalability**: Highly scalable globally without major infrastructure costs. **Engagement**: Personalised content (Spotify playlists, Netflix recommendations) and exclusive features keep users subscribed." },
            { h: "Crowdfunding (Kickstarter, GoFundMe, Fundit.ie)", b: "**Revenue**: Many small contributions raised online before product launch. **Access/Cost**: Free to browse; backers contribute in return for rewards or early access. **Scalability**: Campaigns can go viral globally without big budgets; low overhead. **Engagement**: Updates, reward tiers and storytelling build community support." },
            { h: "Advertising-supported (TikTok, Facebook, YouTube)", b: "**Revenue**: Advertisers pay based on views, clicks or impressions; premium ad-free options (YouTube Premium). **Access/Cost**: Free for consumers; revenue earned indirectly through ads. **Scalability**: Extremely scalable — more users means more ad reach. **Engagement**: Algorithms personalise content to maximise time on platform and ad exposure." },
            { h: "Compared to non-digital", b: "Tech-driven models bring 24/7 access, easier cancellation, personalisation, lower scaling costs, global reach and direct funding from public — without needing physical stores or big advertising budgets." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Explain two key characteristics of each of the following technology-driven business models: (i) Subscription and (ii) Advertising-supported.", model: "**(i) Subscription** (e.g. Netflix, Spotify):\n• **Recurring revenue** — Customers pay regular monthly or annual fees, providing predictable, ongoing income for the business.\n• **High scalability** — Digital delivery means new users can be added globally at very little extra cost compared to traditional services.\n\n**(ii) Advertising-supported** (e.g. TikTok, YouTube):\n• **Indirect revenue** — Consumers access content for free; revenue comes from advertisers paying for views, clicks or impressions.\n• **Algorithm-driven engagement** — Personalised content keeps users on the platform for longer, increasing the value of advertising space." },
            { type: "short", marks: 5, prompt: "Explain the term 'crowdfunding'.", model: "**Crowdfunding** is a technology-driven business model where a business raises small amounts of money from a large number of individuals online, typically before a product or service is launched. Backers may contribute in exchange for rewards, early access to the product, or equity. Platforms like Kickstarter and Fundit.ie allow campaigns to go viral and reach a global audience without large marketing budgets, while also building an early community of customers." },
            { type: "short", marks: 8, prompt: "Compare a subscription service with another technology-driven business model under the headings (i) Revenue Generation and (ii) Scalability.", model: "**(i) Revenue Generation**:\n• Subscription (Spotify) — earns recurring monthly or annual fees from users for continuous access.\n• Marketplace (Vinted) — charges a fee or commission on each transaction between buyers and sellers; revenue depends on transaction volume rather than fixed payments.\n\n**(ii) Scalability**:\n• Subscription — Highly scalable as digital delivery means more users add little extra cost; can grow globally quickly.\n• Marketplace — Also highly scalable as platforms grow as more users join; no need to own additional stock or property, but it relies on attracting a critical mass of both buyers and sellers." },
            { type: "mcq", marks: 2, prompt: "Match the following: 'A platform earns commission on transactions between buyers and sellers without holding inventory'.", options: ["Subscription", "Marketplace", "Crowdfunding", "Advertising-supported"], correct: 1, model: "Marketplace — connects buyers and sellers and earns a commission per transaction." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 9 =================== */
    {
      id: "ch9",
      number: 9,
      strand: 2,
      title: "The Target Market",
      learningOutcomes: [
        {
          id: "lo9-1",
          code: "9.1",
          title: "Importance of market research and identifying the target market",
          notes: [
            { h: "Target market", b: "The specific segment or group of customers a business is trying to sell to, defined by characteristics like age, gender, income, location, lifestyle and interests." },
            { h: "Importance of identifying the target market", b: "**1. Stronger brand identity** — name, logo and tone match customer preferences (Mooju → 16–24 year-old males). **2. Better product design** — tailored to needs (Nobó dairy-free ice cream). **3. Smarter marketing choices** — best platforms and messages (Chupi uses Instagram for fashion-conscious customers). **4. Improved customer loyalty** — meeting expectations builds trust (SuperValu adapts ranges to local communities)." },
            { h: "Market segmentation", b: "Dividing a market into smaller groups with common characteristics. Types: **Demographic** (age, gender, income, family size); **Geographical** (county, region, country); **Behavioural** (attitudes, usage habits — impulse buying, value seekers); **Psychological** (lifestyle/personality — health-conscious, ethical, sustainable)." },
            { h: "Reasons for market research", b: "1. **Estimate market size and trends**. 2. **Analyse competitors**. 3. **Shape the marketing mix** (price, promotion, etc.). 4. **Test and improve products** to reduce launch risk." },
            { h: "Field research (primary)", b: "First-hand info collected directly. Methods: **Surveys** (questions to customers), **Observation** (watching behaviour), **Customer Feedback** (smiley buttons, ratings), **Focus Groups** (small in-depth discussions). *Advantages*: most up-to-date, highly specific. *Disadvantages*: expensive, time-consuming." },
            { h: "Desk research (secondary)", b: "Existing information collected by others. Sources: **Internal Reports** (past sales, customer records), **Government Publications** (CSO data), **Online Sources** (websites, social media, reviews), **Industry Reports**. *Advantages*: quick, low-cost, accessible, useful for trend analysis. *Disadvantages*: may be outdated, not specific to the business, doesn't always show 'why'." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Discuss two types of market research a business may use before expanding.", model: "**1. Field Research (Primary)**: The business collects new, first-hand information from customers using methods like surveys, focus groups and observation. For expansion, this is highly relevant — for example, surveying potential customers in a new region tells the business if there is genuine demand for its product. The data is up-to-date and tailored, though it can be expensive and time-consuming.\n\n**2. Desk Research (Secondary)**: The business uses existing information already collected by others — internal sales records, CSO population/income data, online reviews, or industry reports. This is fast and cheap and is useful for spotting broad trends and comparing markets. However, the data may be outdated or not specific to the business's exact needs." },
            { type: "short", marks: 8, prompt: "Outline four reasons why a business should carry out market research.", model: "**1. Estimate market size and trends** — to understand if a market is growing and what its key characteristics are.\n\n**2. Analyse competitors** — to reveal rivals' strengths and weaknesses and improve competitive positioning.\n\n**3. Shape the marketing mix** — to guide decisions on product design, pricing, promotion and sales strategy.\n\n**4. Test and improve products** — to find out what customers value, reducing the risk of launching a product that fails." },
            { type: "short", marks: 5, prompt: "Identify the intended target market for a heavily branded, high-protein bar with bold packaging and explain how you would justify your choice based on the marketing mix.", model: "**Target market**: Health-conscious adults aged 18–35, particularly those interested in fitness, the gym or sport.\n\n**Justification using the marketing mix**: The bold, branded packaging and use of macros/protein content as a key claim signals **Product/Promotion** is aimed at fitness-oriented customers who care about nutritional information. The premium pricing typical of these products signals **Pricing** aimed at adults with disposable income rather than children or budget-conscious shoppers. The likely **Place** — health food shops, gyms, supermarket protein aisles — also confirms it is positioned for active, wellness-aware customers." }
          ]
        },
        {
          id: "lo9-2",
          code: "9.2",
          title: "The 7 P's of the marketing mix",
          notes: [
            { h: "The 7 P's", b: "Product, Price, Promotion, People, Packaging, Process, Place. Each is adjusted to match the target market." },
            { h: "Product/Service", b: "**USP** — the differentiating feature. **Branding** — name, design, logo, slogan ('Just Do It'). **Product Design** — core features, branding, target appeal, quality, sustainability. **Product Life Cycle** — Introduction → Growth → Maturity → Decline. Extend life cycle by adjusting the 7 P's (Pringles: new flavours, bundle deals, expand to airports, influencer campaigns)." },
            { h: "Price — factors", b: "Target market (income), Cost of production, Competitor prices, Economic conditions." },
            { h: "Pricing strategies", b: "**Penetration** — low to enter market and gain share (HelloFresh discounts). **Price Skimming** — high then drop (PlayStation launches). **Premium** — high signals luxury (Lululemon). **Cost-Plus** — total cost + markup. **Bundle** — discount when bought together (McDonald's meals). **Tiered** — multiple versions at different prices (Spotify Free/Premium/Family). **Price Discrimination** — different groups (student/senior). **Predatory** — low to eliminate rivals (Amazon underpricing books). **Loss Leader** — sold below cost to attract customers (IKEA hot dogs). **Dynamic** — based on demand/time (Oasis tickets, FIFA World Cup)." },
            { h: "Promotion — types", b: "**Advertising**: Informative, Persuasive, Generic, Competitive. Regulated by **ASAI** (Advertising Standards Authority of Ireland). **Public Relations**: press releases, sponsorships, community initiatives, crisis response. **Sales Promotions**: discounts, BOGOF, loyalty cards, competitions. **Direct Marketing**: email, SMS, push notifications, A/B testing. **Digital Marketing**: influencers, viral content. **Personal Selling**: face-to-face/online sales help; AI chatbots (Dell)." },
            { h: "People", b: "Everyone delivering the product/service — staff, drivers, online support. Target market influences who is hired and how they're trained: a youth fashion brand hires TikTok-savvy staff; a luxury hotel trains formal, discreet staff." },
            { h: "Packaging / Physical Evidence", b: "Functions: **Protection** (childproof lids), **Information** (use-by, allergens), **Point of Differentiation** (Pringles tube), **Ethics & Sustainability** (Ballygowan recycled bottles). For services, physical evidence builds trust (restaurant interior, spotless taxi)." },
            { h: "Process", b: "Every step from first contact to after-sales (e.g. Browse → Cart → Checkout → Payment → Delivery → Returns). Smooth process builds trust and repeat purchases. Influenced by target market — e.g. McDonald's kiosks for speed; clear return labels for less tech-savvy customers." },
            { h: "Place", b: "How product/service reaches the customer. Factors: **Cost** (each intermediary takes markup), **Nature of product** (perishable vs luxury), **Market reach** (small brands sell direct online, big brands need retailers). Selling direct: higher margins, lower overheads, full control, customer data — but limited reach. Selling via retailer: large reach, no own store needed — but lower margins and risk of own-brand copies." }
          ],
          questions: [
            { type: "short", marks: 10, prompt: "Outline the seven elements of the marketing mix and briefly explain the role of each.", model: "**1. Product/Service** — what the business sells; must meet target market needs and have a clear USP.\n**2. Price** — what customers pay; chosen using strategies such as penetration, premium or cost-plus.\n**3. Promotion** — how the product is communicated to customers (advertising, PR, sales promotions, direct/digital marketing, personal selling).\n**4. People** — staff who deliver the product or service and shape the customer experience.\n**5. Packaging** — physical packaging for goods, or physical evidence (e.g. interior design) for services; protects, informs and differentiates.\n**6. Process** — the customer journey from first contact through to after-sales support; should be smooth and convenient.\n**7. Place** — how the product reaches customers (direct, retailer, marketplace, online or offline)." },
            { type: "short", marks: 8, prompt: "Outline two ways the target market for a product or service might influence the promotion element of the marketing mix.", model: "**1. Choice of platform**: Businesses select where to advertise based on where the target market spends time. A skincare brand targeting Gen Z might use Snapchat ads and short-form TikTok video tutorials, whereas a brand targeting older customers might use radio or print to reach them effectively.\n\n**2. Tone and content of message**: The format of the message is tailored to audience preferences. A retirement investment firm may post brochures with formal language to older adults, while a fashion brand targets young adults via stylised email and Instagram campaigns featuring influencers." },
            { type: "short", marks: 8, prompt: "Explain four pricing strategies a business may use, with an example of each.", model: "**1. Penetration Pricing** — Low price to enter a market and quickly gain share. *Example*: HelloFresh offered deep discounts to attract first-time users.\n\n**2. Price Skimming** — High initial price to target early adopters, then dropped. *Example*: Sony PlayStation consoles launch at a premium before later cuts.\n\n**3. Premium Pricing** — High price to signal status or quality. *Example*: Lululemon for activewear, Rolex for watches.\n\n**4. Bundle Pricing** — Discount when items are bought together. *Example*: McDonald's meal deals cost less than buying items separately." },
            { type: "short", marks: 8, prompt: "Outline four functions of packaging in the marketing mix.", model: "**1. Protection** — Protects the product during delivery and storage. *Example*: childproof lids on medicine bottles.\n\n**2. Information** — Includes essential details such as use-by dates, allergens or caffeine content. *Example*: energy drinks display caffeine content clearly.\n\n**3. Point of Differentiation** — Helps the product stand out and be recognisable. *Example*: Pringles' distinctive tube.\n\n**4. Ethics and Sustainability** — Recyclable or ethically sourced packaging boosts appeal to eco-conscious customers. *Example*: Ballygowan bottles made from 100% recycled plastic." },
            { type: "mcq", marks: 2, prompt: "An online shopping experience taking the customer through Browse → Cart → Checkout → Payment → Delivery is an example of which 'P' in the marketing mix?", options: ["Place", "Process", "Packaging", "Promotion"], correct: 1, model: "Process — every step the customer goes through from first contact to after-sales." },
            { type: "tf", marks: 2, prompt: "Predatory pricing involves charging temporarily low prices in order to drive competitors out of the market.", correct: true, model: "True. Predatory pricing is a temporary low-price strategy used to eliminate rivals from a market." }
          ]
        },
        {
          id: "lo9-3",
          code: "9.3",
          title: "USP analysis for a product/service",
          notes: [
            { h: "What a USP analysis is", b: "It identifies and highlights the unique benefits a business offers that customers desire and competitors don't deliver as well. A business should clarify: 1. What it does well, 2. What customers want, 3. What competitors do well — and build the marketing mix to focus on the overlap of (its strengths + customer wants) that competitors don't offer." },
            { h: "Worked example — Netflix vs Disney+", b: "**Focus on these (Netflix's USP)**: Strong global original content (Squid Game, The Crown, Stranger Things), binge-watching releases, sophisticated recommendation algorithm, broad teen/adult appeal. **Don't bother differentiating on**: HD/4K streaming, offline downloads, profiles — both do these. **Avoid competing on**: exclusive Disney franchises (Marvel, Star Wars, Pixar) where Disney+ is stronger." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Conduct a USP analysis for a product or service of your choice and explain how the marketing mix should focus on the USP identified.", model: "**Service example: Spotify vs Apple Music**\n\n**What Spotify does well + what customers want + Apple Music doesn't do as well**:\n• Sophisticated discovery algorithms and personalised playlists like Discover Weekly.\n• Strong free, ad-supported tier as a route into the paid product.\n• Cross-platform availability (works seamlessly on Android, Windows, smart speakers, etc.).\n\n**Implications for the marketing mix**: Spotify should focus its **Promotion** on personalised discovery (e.g. Spotify Wrapped campaigns showcasing year-end personalisation). **Product** should keep investing in algorithms and playlist curation. **Pricing** should retain the freemium tier as a USP. Spotify should avoid promoting features that Apple Music does as well (e.g. high audio quality), and avoid marketing in areas where Apple Music dominates (deep iOS integration)." }
          ]
        },
        {
          id: "lo9-4",
          code: "9.4",
          title: "Evaluating and improving an existing marketing mix",
          notes: [
            { h: "How to evaluate", b: "Don't just say what to change — explain why. Support suggestions with evidence (customer feedback, trends, competitor moves). Always link back to target market and brand USP. Suggestions should: show clear understanding of the target market, link to current trends (high-protein, sustainability), be realistic for the brand's image and resources, and explain how the change will increase sales/loyalty/reputation." },
            { h: "Worked example — McDonald's", b: "**Evaluation**: Heavy focus on indulgent, high-calorie meals. Promotions centre on value and family deals. Strong McDelivery. **Gap**: nothing for the growing health/protein-conscious segment. **Improvements**: 1. **Product** — Introduce 'MacroChicken Wrap' (35g+ protein, <500 kcal). 2. **Promotion** — Influencer Instagram/TikTok campaigns. 3. **Packaging** — Clean, eco-friendly with QR code linking to nutrition info." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Evaluate the marketing mix of a business of your choice and recommend two ways it could be improved. (4m evaluation + 4m for each recommendation)", model: "**Business: McDonald's Ireland**\n\n**Evaluation**: McDonald's product range is heavily focused on indulgent, high-calorie meals, with limited options for health-conscious customers. Promotions centre on value meals and family-friendly deals rather than wellness trends. The McDelivery service is strong but the menu lacks targeted offerings for the growing market of consumers seeking high-protein, lower-calorie options.\n\n**Recommendation 1 — Product**: Introduce a new 'MacroChicken Wrap' — a grilled chicken wrap with 35g+ protein, added fibre and under 500 calories. This appeals to fitness-conscious Gen Z and millennial customers who currently choose competitors like Subway or coffee shop wraps, expanding McDonald's reach into a profitable segment.\n\n**Recommendation 2 — Promotion**: Run targeted Instagram and TikTok campaigns featuring fitness influencers trialling the MacroChicken Wrap and posting macro breakdowns. This positions the new product as credible to health-aware audiences and reaches them where they spend time, increasing trial rates and shifting brand perception away from purely indulgent food." }
          ]
        },
        {
          id: "lo9-5",
          code: "9.5",
          title: "Disruptive impact of digital technology on market research and marketing",
          notes: [
            { h: "Impact on market research", b: "**Real-time feedback** — online polls, social listening allow instant feedback. **Big Data & AI** — tools analyse vast volumes of search/review/behaviour data faster than traditional research. **More affordable tools** — Google Analytics, Meta Suite open detailed data to small firms, closing the gap with large businesses." },
            { h: "Impact on marketing", b: "**More targeted campaigns** — TikTok and Google Ads target by age/interest/habits. **Measurable results** — clicks, sales and views are tracked; A/B testing compares versions. **Creative low-cost options** — memes, influencer content and viral videos let small brands reach huge audiences cheaply, challenging big-budget advertising." }
          ],
          questions: [
            { type: "short", marks: 9, prompt: "Demonstrate three ways digital technology has disrupted marketing for businesses.", model: "**1. More targeted campaigns**: Platforms like TikTok and Google Ads allow precise targeting by age, interests and behaviour, making marketing more personal and cost-effective than traditional broadcast advertising.\n\n**2. Measurable results**: Digital tools show exact ad performance — clicks, sales, views — and A/B testing compares versions to find what works. This means businesses can refine campaigns in real time based on hard data instead of guessing.\n\n**3. Creative, low-cost options**: Memes, influencer content and viral videos let small brands reach huge audiences on tiny budgets, challenging the dominance of traditional big-budget advertising and giving start-ups a route to market." }
          ]
        },
        {
          id: "lo9-6",
          code: "9.6",
          title: "Influence of ethics and sustainability on marketing",
          notes: [
            { h: "Positive influence", b: "**Builds trust and loyalty** — Tony's Chocolonely championing fair trade. **Creates powerful marketing stories** — SuperValu's TidyTowns support. **Competitive advantage** — Ballygowan's recycled bottles win eco-conscious customers." },
            { h: "Challenges", b: "**Increased costs** — sustainable materials and ethical sourcing reduce margins. **Risk of greenwashing** — overstating eco-claims without action damages trust (fast fashion brands criticised for 'green' lines while remaining unsustainable). Evaluation: ethics and sustainability build loyalty only when authentic — businesses must align marketing with real action." }
          ],
          questions: [
            { type: "short", marks: 9, prompt: "Outline three ways ethics is an important consideration when designing a marketing strategy.", model: "**1. Builds trust and customer loyalty**: Customers increasingly support brands that reflect their values. Ethical positioning — like Tony's Chocolonely championing fair trade cocoa — builds a loyal following willing to pay a premium and recommend the brand.\n\n**2. Avoids reputational damage from greenwashing**: Overstating environmental claims without genuine action damages trust quickly when exposed. Marketing must align with real practice, otherwise consumers and regulators (e.g. ASAI) will call out misleading claims.\n\n**3. Creates a competitive advantage**: Genuine ethical and sustainable practice can differentiate a brand. Ballygowan promotes its 100% recycled plastic bottles to win eco-conscious customers in a crowded market — this is a marketing point rivals can't easily copy." }
          ]
        },
        {
          id: "lo9-7",
          code: "9.7",
          title: "Power-interest grid for customers",
          notes: [
            { h: "What it does", b: "A business uses a power-interest grid to decide how to treat different customer segments, based on **power** (their influence on the business) and **interest** (how much they care about the business). The marketing mix is then adjusted to focus most attention on customers in the high-power/high-interest quadrant." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Explain how a business can use a power-interest grid to inform its marketing mix.", model: "A business plots its customer segments on a power-interest grid using the axes Power (influence on the business) and Interest (how much they care about it). Customers in the **high-power, high-interest** quadrant are the priority — for example, a clothing brand's loyal repeat customers — and the marketing mix should focus on retaining them with loyalty schemes (Pricing), personalised messaging (Promotion), and excellent in-store and online service (People, Process). **Low-interest, low-power** segments such as occasional shoppers receive minimal effort. This allows the business to allocate marketing spend efficiently and protect the customers who matter most." }
          ]
        },
        {
          id: "lo9-8",
          code: "9.8",
          title: "STEEPLE analysis",
          notes: [
            { h: "What it is", b: "A tool to understand the wider external environment a business operates in. Identifies opportunities and threats so the business can plan, decide and adapt to stay competitive and compliant." },
            { h: "STEEPLE factors", b: "**Social** — lifestyle/values changes (vegan/low-cal options for Gen Z). **Technological** — automation, platforms (apps for younger customers). **Economic** — inflation, interest rates, consumer confidence (subscription cancellations during downturns). **Environmental** — climate, sustainability (water company's plastic bottles). **Political** — government policy, trade relations, taxes (US tariffs on Irish exporters). **Legal** — employment, GDPR, advertising law (gym data). **Ethical** — values, treatment of people/animals/environment (clothing brand's factory exposé)." }
          ],
          questions: [
            { type: "short", marks: 14, prompt: "Conduct a STEEPLE analysis on a business operating in Ireland today, identifying one factor under each of seven headings.", model: "**Social**: Growing demand for plant-based and low-calorie food has pushed fast-food chains to add vegan or wellness options to keep Gen Z customers.\n\n**Technological**: Adoption of AI-driven customer service (chatbots, recommendation engines) is now standard — businesses without it lose customers to competitors with smoother digital experiences.\n\n**Economic**: Persistent inflation and high interest rates have reduced disposable income, leading consumers to switch to cheaper alternatives or cancel subscriptions.\n\n**Environmental**: Growing public concern over packaging waste means consumers expect recyclable or refillable options — Ballygowan's recycled plastic bottles is one response.\n\n**Political**: New US tariffs during the Trump administration increased export costs for Irish firms selling into the US market, forcing pricing reviews.\n\n**Legal**: GDPR compliance is mandatory for any business collecting personal data — fines of up to 4% of global turnover make legal compliance a top priority.\n\n**Ethical**: Cultural insensitivity in marketing (e.g. tone-deaf US ad campaigns) can quickly damage a brand's reputation — businesses must check campaigns carefully before launch." },
            { type: "mcq", marks: 2, prompt: "A clothing company collecting customer data and ensuring it complies with privacy law is responding to which STEEPLE factor?", options: ["Social", "Economic", "Legal", "Ethical"], correct: 2, model: "Legal — GDPR is a legal regulation that governs personal data collection." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 10 =================== */
    {
      id: "ch10",
      number: 10,
      strand: 2,
      title: "Operations and Finance",
      learningOutcomes: [
        {
          id: "lo10-1",
          code: "10.1",
          title: "Operational model — Key Partners, Activities & Resources",
          notes: [
            { h: "What the operational model is", b: "Three core building blocks from the BMC explain how a business runs day-to-day: Key Partners, Key Activities, Key Resources." },
            { h: "Key Partners", b: "External people/organisations a business depends on. **Suppliers** (bakery's wholesaler), **Distributors** (An Post, DPD), **Outsourcing/Service Providers** (payroll, web management), **Strategic Alliances** (Spotify & Uber), **Joint Ventures** (Sony Ericsson), **Licensing** (Penneys licensing Disney/Marvel). Change over time as: business grows, expands abroad, undergoes digital transformation, ethical sourcing pressure, or legal compliance changes." },
            { h: "Key Activities", b: "Essential tasks needed to deliver the value proposition. **Product Design & Development** (Apple R&D), **Manufacturing** (small-batch chocolatier), **Marketing & Branding** (Gymshark), **Distribution & Logistics** (UPS for online bookstore), **Customer Experience & Support** (24/7 mobile provider support), **App & Website Development**. Change as: business grows, technology evolves, customer needs shift, business model changes (e.g. subscription needs onboarding/retention)." },
            { h: "Key Resources", b: "Essential assets needed to operate. **Physical** (Fastway's vans/depots), **Human Capital** (developers at a start-up), **Financial** (loans/crowdfunding for new business), **Intangible** (Disney's brand/IP, Vinted's user base, Airbnb app/data). Change as: physical assets depreciate, human capital evolves with training/turnover, financial resources shift (start-ups rely on external funding, mature firms reinvest profits), intangibles strengthen or weaken with reputation." }
          ],
          questions: [
            { type: "short", marks: 10, prompt: "Outline the three main elements key to the operational model of a business and explain why each may change over time.", model: "**1. Key Partners** — external people/organisations the business depends on (suppliers, distributors, outsourced service providers). They change as the business grows: a local supplier may not be enough as the business scales, and exporting requires logistics partners or customs agents.\n\n**2. Key Activities** — the most important day-to-day tasks (manufacturing, marketing, customer support, app development). They change with digital transformation — AI and platforms can automate tasks — and with new business models, where a switch to subscription requires new onboarding and retention activities.\n\n**3. Key Resources** — essential assets (physical, human, financial, intangible). They change because physical assets depreciate and need replacement, human capital evolves as staff gain experience or leave, financial resources shift from start-up funding to retained earnings, and intangibles like brand value can grow or be damaged by events." }
          ]
        },
        {
          id: "lo10-2",
          code: "10.2",
          title: "Costs, sources of finance, revenue streams across the lifecycle",
          notes: [
            { h: "Variable costs", b: "Linked to output — rise as output rises. *Examples*: wages, stock, light/heat. As output grows, variable cost per unit usually falls due to economies of scale." },
            { h: "Short-term finance (under 1 year, for variable costs)", b: "**Bank Overdraft** — withdraw more than account balance up to limit. **Accrued Expenses** — delaying payment of bills temporarily. **Trade Credit** — receive goods now, pay 30–60 days later. **Factoring** — sell unpaid invoices to a factoring company for immediate cash; they keep a fee." },
            { h: "Fixed costs", b: "Same each month regardless of output. *Examples*: rent, manager's salary, lease payments. Can change at renewal but stay consistent within agreed period." },
            { h: "Medium-term finance (1–5 years, fixed costs)", b: "**Leasing** — rent an asset; never own it. **Term Loan** — bank loan repaid in instalments over 1–5 years. **Hire Purchase** — buy via deposit + instalments; ownership after final payment." },
            { h: "Long-term finance (over 5 years)", b: "**Long-term Loan** — instalments over 5+ years. **Debenture** — secured against assets, repaid 10–15 years, annual interest. **Equity/Share Capital** — sell shares; investors become part-owners. **Venture Capital** — invested in high-potential, high-risk start-ups. **Retained Earnings** — reinvest past profits. **Grants** — government/EU money that doesn't need to be repaid (strict criteria)." },
            { h: "Factors when choosing finance", b: "**Cost** — compare APR. **Purpose** — match source to use (van → medium-term). **Amount** — capital limits. **Control** — equity dilutes voting rights. **Collateral** — risk of losing the asset used as security." },
            { h: "Revenue streams", b: "**Product Sales** (bakery), **Service Fees** (gym class), **Subscription** (Netflix), **Advertising** (YouTube), **Commission** (DoneDeal), **Licensing/Franchise Fees**, **Renting/Leasing Assets**." },
            { h: "Why revenue streams change", b: "Customer behaviour shifts (gym moves from pay-per-visit to membership), digital transformation, need for predictable income (veg box subscription), competitive diversification (café renting space)." }
          ],
          questions: [
            { type: "short", marks: 5, prompt: "Identify a suitable source of finance for a business looking to purchase a delivery van and give a reason for your choice.", model: "**Hire Purchase** is suitable. The business pays an initial deposit followed by regular monthly instalments over a 1–5 year period (medium-term, matching the useful life of the van). After the final payment the business owns the van, allowing it to use it long-term and resell when no longer needed. This avoids the large upfront cost of buying outright and the lack of ownership in leasing." },
            { type: "mcq", marks: 6, prompt: "Identify whether each of the following costs is variable or fixed: (1) Monthly rent for the bakery space, (2) Cost of ingredients, (3) Lease payments for equipment.", options: ["1) Variable, 2) Fixed, 3) Variable", "1) Fixed, 2) Variable, 3) Fixed", "1) Fixed, 2) Variable, 3) Variable", "1) Variable, 2) Fixed, 3) Fixed"], correct: 1, model: "Rent is fixed — same each month. Ingredients are variable — rise with production. Lease payments are fixed — same agreed amount each period." },
            { type: "short", marks: 8, prompt: "Outline four short-term sources of finance a business could use to cover variable costs.", model: "**1. Bank Overdraft** — Allows the business to withdraw more than is in its current account up to an agreed limit. Useful for short cashflow gaps.\n\n**2. Trade Credit** — The business receives goods now and pays the supplier in 30–60 days, freeing cash to be spent elsewhere in the meantime.\n\n**3. Accrued Expenses** — Delaying the payment of bills for a short time to use that money for another short-term purpose.\n\n**4. Factoring** — Selling unpaid customer invoices to a factoring company in exchange for immediate cash; the factor takes a percentage as its fee." },
            { type: "short", marks: 5, prompt: "Outline two factors a business considers when choosing a source of finance.", model: "**1. Cost (APR)**: The business compares the Annual Percentage Rate of different options, including interest, fees and charges, to choose the cheapest option that fits its needs.\n\n**2. Control**: If the business issues ordinary shares (equity), the new investors gain voting rights and a say in decision-making. The owner may prefer debt to keep control of the business." }
          ]
        },
        {
          id: "lo10-3",
          code: "10.3",
          title: "Cashflow analysis",
          notes: [
            { h: "What is a cashflow forecast?", b: "Plans the money coming in (receipts) and going out (payments) over a future period. Helps ensure the business has enough cash for day-to-day operations — without it, employees, suppliers and utility providers go unpaid." },
            { h: "Reasons for preparing a cashflow forecast", b: "**1. Avoid deficits** — see in advance when a shortage may occur. **2. Improved financial control** — compare actual vs planned cashflow. **3. Raise finance** — required by banks and investors as part of a business plan. **4. Plan for surpluses** — what to do with extra cash (deposit, equipment, expansion)." },
            { h: "Limitations", b: "**Based on estimates** — predicted figures may be inaccurate. **Unexpected events** — energy price rises, bad debts, economic shocks." },
            { h: "Analysing the forecast", b: "**Closing Cash Surplus** — positive closing balance. **Closing Cash Deficit** — negative closing balance, business won't have enough cash to cover payments." },
            { h: "Actions to address cashflow problems", b: "**1. Spread payments** — lease or pay off in monthly instalments instead of one-off. **2. Increase cash receipts** — short-term promotion for quick cash. **3. Reduce cash payments** — cut unnecessary spending, find cheaper suppliers, restructure loans. **4. Use short-term finance** — overdraft or short-term loan." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline four reasons why a business prepares a cashflow forecast.", model: "**1. To help avoid cash deficits** — A forecast highlights months when cash will run short, allowing the business to arrange short-term finance like an overdraft in advance.\n\n**2. Improved financial control** — It allows the business to compare actual cashflow to planned figures, spot variances, and operate within its means.\n\n**3. To raise finance** — Banks, investors and the LEO usually require a cashflow forecast as part of the business plan before agreeing to provide funding.\n\n**4. To plan for surpluses** — When months show excess cash, the business can plan how to use it productively, e.g. placing it on deposit, investing in equipment or funding expansion." },
            { type: "short", marks: 8, prompt: "A business has identified a closing cash deficit of €25,000 in December. Recommend a suitable course of action to address this issue.", model: "The business could combine several actions:\n\n**1. Avail of a short-term source of finance** — Arrange a bank overdraft to cover the shortfall temporarily until receipts pick up. This is often the quickest solution.\n\n**2. Increase cash receipts** — Run a December promotion such as a 10% discount or 'buy one get one free' to bring forward sales and increase cash inflows.\n\n**3. Reduce cash payments** — Cut non-essential spending, source cheaper suppliers, and ask the bank to restructure existing loan repayments to spread payments over a longer period at smaller monthly amounts.\n\n**4. Spread payments over time** — For any large one-off purchase planned for December, choose to lease or pay over instalments instead of paying upfront." },
            { type: "tf", marks: 2, prompt: "A cashflow forecast is based on actual figures from past months and therefore is fully accurate.", correct: false, model: "False. Cashflow forecasts are based on estimated/predicted figures, which may not be accurate. Unexpected events such as energy price rises or bad debts can also affect outcomes." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 11 =================== */
    {
      id: "ch11",
      number: 11,
      strand: 2,
      title: "Growth, Development and Expansion",
      learningOutcomes: [
        {
          id: "lo11-1",
          code: "11.1",
          title: "Importance of identifying competition",
          notes: [
            { h: "Direct vs indirect competition", b: "**Direct competitors** — same/similar products to the same target market (a bakery vs another bakery). **Indirect competitors** — different products satisfying the same need (supermarket selling bread)." },
            { h: "Why analyse competition?", b: "**1. Understand who direct/indirect competitors are**. **2. Insight into what strategies have worked or failed** for rivals — avoid mistakes, build on proven ideas. **3. Reveals current consumer preferences** — adapt to what customers value (gluten-free range)." },
            { h: "Capitalising on competitive advantage", b: "**1. Helps create a clear USP** — a differentiating feature, service or experience. **2. Builds loyal customer base** — customers return for what they can't easily find elsewhere (Ryanair's low fares). **3. Improves the marketing mix** — communicate USP through advertising, in-store, packaging, staff. **4. Develops the advantage** — invest in what you're best at; advantages are not permanent. Examples of advantages: lower prices, free returns, higher quality, location, customer service, technology, next-day delivery, latest designs." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Demonstrate the importance of identifying competition in the market for a business.", model: "Identifying competition allows a business to understand both **direct competitors** (same product to same market — e.g. another local bakery) and **indirect competitors** (different products meeting the same need — e.g. a supermarket selling bread). This is important because it provides insights into strategies that have worked or failed for rivals — letting the business avoid expensive mistakes and copy proven approaches. It also reveals current consumer preferences, helping the business adapt — for example, a bakery noticing gluten-free products selling well at competitors might launch its own gluten-free range. Without this analysis the business risks irrelevance." },
            { type: "short", marks: 8, prompt: "Identify a potential competitive advantage for a business of your choice and recommend an appropriate strategy for launching a new product to the market.", model: "**Business**: A small Irish skincare brand with a competitive advantage in **organic, locally-sourced ingredients**.\n\n**Recommended strategy**: Build the entire marketing mix around this USP. **Product**: highlight the natural, plant-based formula on packaging with clear ingredient transparency. **Pricing**: position as premium, justified by ethical sourcing. **Promotion**: use Instagram and TikTok influencers in the wellness/eco space to demonstrate the products and tell the supplier story. **Place**: launch direct-to-consumer through the brand website to maintain margin and customer data, plus stock in select health shops. This way, every part of the marketing mix reinforces the competitive advantage rather than competing on price with mass-market brands." }
          ]
        },
        {
          id: "lo11-2",
          code: "11.2",
          title: "Porter's Five Forces",
          notes: [
            { h: "What it is", b: "A model with five competitive forces driving the division of economic value among stakeholders. It helps a business identify strengths, risks and competitive advantage." },
            { h: "1. Threat of New Entrants", b: "How easy it is for new businesses to enter the market. **Low threat** = high barriers (McDonald's needs huge capital, branding, supply networks). **High threat** = anyone can enter (a barber shop)." },
            { h: "2. Bargaining Power of Suppliers", b: "Power suppliers have over the business. **Low** = many alternatives (Supermac's sourcing potatoes from many Irish farms). **High** = relies on key supplier (small Irish cake maker selling most of its output to Aldi)." },
            { h: "3. Bargaining Power of Buyers", b: "Power customers have. **Low** = loyal, can't switch easily (Apple iPhone). **High** = customers can switch instantly (taxi customers can use Uber, FreeNow)." },
            { h: "4. Threat of Substitutes", b: "Alternative ways to meet the same need. **Low** = few alternatives (electricity supply). **High** = many options (Spotify vs YouTube, Apple Music, radio, podcasts)." },
            { h: "5. Competitive Rivalry", b: "Intensity of competition. **Low** = limited rivals (Irish Rail intercity routes). **High** = price wars, heavy promotion (Circle K vs Applegreen forecourt sector)." },
            { h: "How a business uses the model", b: "Low new-entrant threat + strong loyalty → scope to raise prices/expand. High rivalry/new entrants → delay expansion, invest in marketing/innovation to protect the business." }
          ],
          questions: [
            { type: "short", marks: 25, prompt: "Analyse the competitive forces in the market for an Irish supermarket like Dunnes Stores using Porter's Five Forces Model. (5 @ 5m: 2m explain force + 3m apply to business)", model: "**1. Threat of New Entrants — Low**: Setting up a nationwide supermarket chain requires massive investment in stores, logistics, distribution centres and branding. Few new players could match Dunnes' established footprint, so the threat is low.\n\n**2. Bargaining Power of Suppliers — Low**: Dunnes has scale and a wide network of Irish and international suppliers, allowing it to negotiate favourable prices and reduce supplier power over its margins.\n\n**3. Bargaining Power of Customers — High**: Irish customers can easily switch between Dunnes, Tesco, Aldi, Lidl and SuperValu. This forces Dunnes to use loyalty schemes like the well-known €10 off €50 spend to keep customers returning.\n\n**4. Threat of Substitutes — Medium**: Customers could shop at convenience stores, farmers' markets or use meal delivery services like HelloFresh, but supermarkets remain the most convenient single option for the weekly shop.\n\n**5. Competitive Rivalry — High**: Rivalry is fierce among the big five retailers. Dunnes competes through promotions, in-house brands like Simply Better, and a unique mix of groceries with clothing and homeware that is harder for pure grocers like Aldi to copy." },
            { type: "short", marks: 4, prompt: "Name the two forces missing from Porter's Five Forces Model from the list: 1. Threat of New Entrants; 2. _____; 3. _____; 4. Threat of Substitutes; 5. Competitive Rivalry.", model: "**2. Bargaining Power of Suppliers**\n**3. Bargaining Power of Buyers (Customers)**" },
            { type: "mcq", marks: 2, prompt: "A business with strong customer loyalty and a low threat of new entrants is in a good position to:", options: ["Lower prices to defend market share", "Raise prices or expand the business", "Reduce its marketing budget", "Sell to a competitor"], correct: 1, model: "A business with these conditions has scope to raise prices or expand because its position is well protected." }
          ]
        },
        {
          id: "lo11-3",
          code: "11.3",
          title: "Strategies to adapt or expand",
          notes: [
            { h: "Adaptation strategies", b: "**Updating products/services** (McDonald's vegan burgers). **Targeting new segments** (gym launches low-impact programme for older adults). **Reducing costs through automation/AI** (hotel chatbot for bookings). **Diversifying** to remove risk (soft drinks company adds sparkling water). **Investing in staff development** (training in digital tools). **Improving sustainability/branding** (clothing brand switches to organic cotton)." },
            { h: "Organic expansion", b: "**Increasing product range / entering new markets** — spreads risk, opens revenue. **E-commerce expansion** — reach more customers without physical sites (All Real Nutrition into US). **Franchising** — franchisor grants licence to franchisees in return for fees. *Benefits*: rapid expansion, lower costs (franchisees fund their own outlets), local knowledge. *Challenges*: quality varies, loss of control, brand reputation risk." },
            { h: "Inorganic expansion — Takeover/Acquisition", b: "Acquiring 50%+ of another business's shares. *Hostile* if directors recommend rejection. *Benefits*: rapid market access, eliminates competition, gains assets/IP. *Challenges*: high capital, hostility with stakeholders, regulatory issues. Example: Meta took over Instagram and WhatsApp." },
            { h: "Inorganic expansion — Mergers", b: "Voluntary amalgamation of two firms into one new legal entity (Kraft + Heinz → KraftHeinz). *Benefits*: shared resources, economies of scale, stronger market position. *Challenges*: culture clashes, redundancies, complex integration." },
            { h: "Inorganic expansion — Strategic Alliances", b: "Two+ businesses pool resources/expertise for a project or period while keeping separate identities (Uber + Spotify in-car streaming). *Benefits*: shared expertise, market access, lower risk. *Challenges*: unequal contribution, loss of control, conflicting objectives." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Outline three strategies a small Irish online clothing business could use to expand. (3 @ 4m)", model: "**1. E-commerce expansion into new geographic markets**: The business could expand its website to ship internationally — for example targeting the UK and US — with localised pricing and shipping. This allows growth without the cost of physical stores. *Example*: All Real Nutrition expanded into the US through Shopify.\n\n**2. Strategic Alliance with a larger retailer or marketplace**: The business could agree to stock a curated range on a larger platform such as ASOS Marketplace or a high-street retailer's website. This gives instant access to a much bigger customer base while keeping the brand identity separate.\n\n**3. Diversifying into new product lines**: The business could expand into adjacent categories such as accessories or athleisure to spread risk across multiple revenue streams and increase the average order value of existing customers." },
            { type: "short", marks: 8, prompt: "Distinguish between a takeover and a merger as expansion strategies, giving one example of each.", model: "**Takeover (Acquisition)**: One business takes control of another by buying over 50% of its shares. The target business may continue under its own name as a subsidiary. *Example*: Meta took over Instagram. It can be hostile if the target company's directors recommend rejecting the offer.\n\n**Merger**: A voluntary amalgamation of two or more firms into a single new legal entity, with no business in control of the other. Both shareholder groups must approve. *Example*: Kraft and Heinz merged to form KraftHeinz." },
            { type: "short", marks: 10, prompt: "Discuss two benefits and two challenges of franchising as an expansion strategy.", model: "**Benefits**:\n**1. Rapid expansion at lower cost** — Franchisees fund and manage their own outlets, allowing the franchisor to grow quickly without huge capital outlay.\n**2. Local knowledge and motivation** — Franchisees often understand their local market well and are highly motivated as owners, helping the business succeed in different regions.\n\n**Challenges**:\n**1. Loss of control and inconsistent quality** — Decisions are shared with many independent franchisees and customer experience can vary if franchisees do not follow standards.\n**2. Brand reputation risk** — One franchisee delivering poor service or facing negative publicity can damage the entire brand's reputation across all locations." }
          ]
        },
        {
          id: "lo11-4",
          code: "11.4",
          title: "Technology supporting adaptation and expansion",
          notes: [
            { h: "How technology supports growth", b: "**Meeting expectations for speed/convenience** — apps, online ordering. **Expanding reach** — Shopify, WooCommerce e-commerce platforms. **Understanding customer behaviour** — Google Analytics, in-app tracking to personalise offers. **Reducing costs/increasing efficiency** — automation, AI, chatbots. **Building brand awareness** — Instagram, TikTok and content tools. **Accessing finance online** — crowdfunding (Kickstarter, Fundit, GoFundMe)." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Describe two forms of technology that support adaptation or expansion for a business.", model: "**1. E-commerce platforms (Shopify, WooCommerce)**: These allow a business to set up an online store quickly and sell nationally or internationally without the cost of physical premises. This expands reach to new markets — for example, a small Irish brand can sell to UK and US customers from day one.\n\n**2. Data analytics tools (Google Analytics)**: By tracking what customers view, click and buy, businesses can understand behaviour and personalise offers. This allows the business to refine its marketing and product range based on real evidence rather than guesswork, supporting smart expansion decisions." }
          ]
        },
        {
          id: "lo11-5",
          code: "11.5",
          title: "Cost-Benefit Analysis (CBA) of expansion",
          notes: [
            { h: "Why CBA matters", b: "When considering expansion, the business weighs short- and long-term benefits against costs to ensure a **net benefit**. Helps make decisions strategic, sustainable, and realistic." },
            { h: "Potential benefits", b: "**Increased Revenue (profit)** — reach new markets (All Real Nutrition into US via Shopify). **Economies of Scale (lower costs)** — fixed costs spread over larger output (Ryanair). **Stronger Market Presence (lowers risk)** — bigger market share reduces rival influence (Aldi forced Tesco/Dunnes to price-match). **Access to new skills/products (diversification)** — new tech, IP, audience (Facebook bought Instagram for younger audience)." },
            { h: "Potential costs", b: "**High Capital Investment** — large outlay for property, equipment, staff (Tesco's failed Fresh & Easy US expansion cost £1bn+). **Regulatory Risks** — extra scrutiny, possible blocks (Facebook's WhatsApp acquisition faced investigation). **Culture Clashes/Poor Integration** — different systems and cultures (AOL–Time Warner). **Loss of Focus/Quality** — distraction from core business (Nokia's late smartphone move)." }
          ],
          questions: [
            { type: "short", marks: 16, prompt: "Conduct a cost-benefit analysis of a proposed takeover by one large Irish business of another. (4 benefits @ 2m + 4 costs @ 2m)", model: "**Scenario**: Tesco proposed takeover of Musgrave Group (SuperValu/Centra).\n\n**Benefits**:\n**1. Rapid Market Access** — Instant access to 220+ SuperValu outlets and Musgrave's strong supplier relationships, vastly increasing Tesco's reach in Ireland.\n**2. Eliminates Competition** — Removes a major rival from the market and gives Tesco a far stronger position against Aldi and Lidl.\n**3. Economies of Scale** — Combined purchasing power reduces unit costs and increases bargaining power with suppliers, improving margins.\n**4. New Assets and Customer Base** — Gains the Centra/SuperValu brands, retail technology and a loyal local customer base that would take years to build from scratch.\n\n**Costs**:\n**1. High Capital Investment** — Acquiring Musgrave at a premium price would cost a huge amount and put pressure on Tesco's cash flow and balance sheet.\n**2. Regulatory Risks** — The Competition and Consumer Protection Commission (CCPC) could block or restrict the deal due to concerns about reduced competition in Irish grocery.\n**3. Community/Reputation Backlash** — The loss of an Irish-owned brand could lead to public anger and customer boycotts, damaging Tesco's reputation in Ireland.\n**4. Integration Challenges** — Merging two large retail systems, store formats and workforces is complex and may distract management from core operations.\n\n**Conclusion**: The financial and reputational risks are significant, but the strategic benefits of dominating the Irish grocery market may outweigh them — provided the CCPC approves the deal and Tesco manages the integration carefully." }
          ]
        },
        {
          id: "lo11-6",
          code: "11.6",
          title: "Adapting marketing mix or business model",
          notes: [
            { h: "Customer demographics", b: "**Marketing Mix**: Ben & Jerry's introduced non-dairy ice cream for vegan/lactose-intolerant customers, changing product, promotion, packaging. **Business Model**: All Real Nutrition added an online subscription for recurring convenience and steady revenue." },
            { h: "Competition", b: "**Marketing Mix**: Burger King launched a flame-grilled plant-based Whopper to match McDonald's vegan offering. **Business Model**: Disney created Disney+ to stream directly to customers, ending licensing to Netflix and creating a subscription revenue stream." },
            { h: "Economic factors", b: "**Marketing Mix**: Lidl Plus loyalty app with digital coupons targets cost-conscious shoppers. **Business Model**: Irish gyms moved to hybrid memberships (in-person + online classes) during COVID, creating a blended revenue model." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Outline how a business could adapt its marketing mix or its business model to respond to changing competition in the market.", model: "**Marketing Mix Example — Burger King**: Faced with McDonald's vegan launch, Burger King introduced its flame-grilled plant-based Whopper. This adapts the **Product** by adding a vegan option, and adapts **Promotion** by emphasising the flame-grilled cooking method that differentiates it from McDonald's, allowing Burger King to defend market share against changing competition.\n\n**Business Model Example — Disney**: As Netflix grew, Disney shifted from licensing its content to competitors and instead launched Disney+, a subscription streaming service. This change in business model gave Disney direct control over distribution and a new recurring revenue stream, allowing it to compete head-on with Netflix in a way the old licensing model couldn't." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 12 =================== */
    {
      id: "ch12",
      number: 12,
      strand: 2,
      title: "Managing Risk",
      learningOutcomes: [
        {
          id: "lo12-1",
          code: "12.1",
          title: "Challenges and risks of enterprise",
          notes: [
            { h: "Challenges", b: "**Raising finance** — equity, debt, crowdfunding (Kickstarter). **Production methods** — keeping costs low while meeting demand. **Choosing ownership type** — sole trader (cheap, easy) vs Ltd (limited liability, lower corporation tax). **Marketing/market penetration** — costly initial advertising, need clear USP. **Availability of location/staff** — high rents, skilled labour shortages." },
            { h: "Risks", b: "**Personal & Financial Risk** — savings, assets, credit rating, reputation. **Operational Risk** — poor staffing/logistics/admin causes lost sales. **Economic Risk** — inflation, interest rates, tariffs. **Competitor & Market Risk** — new entrants, aggressive rivals (Revolut/N26 challenging Irish banks). **Compliance Risk** — failing legal obligations (tax, H&S). **Technological Risk** — cyberattacks, breaches (Ardagh Group 2021). **Ethical & Environmental Risk** — unethical sourcing damages reputation (Boohoo paid workers £3.50/hr in Leicester)." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Outline three challenges, apart from inflation, facing entrepreneurs in Ireland. (3 @ 4m)", model: "**1. Raising Finance**: Many entrepreneurs lack the capital to start or grow. Banks require strong business plans, and equity investors take ownership in return for funding. Crowdfunding through platforms like Kickstarter is an option but requires building trust quickly.\n\n**2. Availability of Location and Staff**: High rents — especially in Dublin city centre — make finding affordable premises difficult, hurting footfall and margins. Hiring skilled staff is also harder due to high cost of living and labour shortages in sectors like hospitality and tech.\n\n**3. Marketing and Market Penetration**: Standing out is expensive when initial sales are slow. Entrepreneurs must invest in marketing, identify the right channels (digital, social, in-store) and build a clear USP to compete with established rivals." },
            { type: "short", marks: 8, prompt: "Discuss two risks facing entrepreneurs and explain how each could affect the business.", model: "**1. Technological & Cyber Risk**: A cyberattack or data breach can disrupt operations, expose customer data and damage reputation. *Example*: Ardagh Group experienced a cyberattack in 2021 that disrupted operations. This can lead to loss of customer trust, fines under GDPR, and immediate financial damage from system downtime.\n\n**2. Ethical & Environmental Risk**: Unethical sourcing or environmental harm can damage brand reputation. *Example*: Boohoo faced backlash when an investigation revealed Leicester factory workers being paid below minimum wage. This kind of risk leads to consumer boycotts, regulator scrutiny, and falling sales — even when the financials look strong otherwise." }
          ]
        },
        {
          id: "lo12-2",
          code: "12.2",
          title: "Importance of assessing and managing risks",
          notes: [
            { h: "Risk management defined", b: "Identification of all possible risks/losses (fire, employer negligence, personal injury, legal liability) and taking action to avoid risks or minimise their impact." },
            { h: "Steps in risk management", b: "**1. Identify the risk** — spot threats through audits (injury, theft). **2. Assess its impact** — likelihood × severity to prioritise. **3. Take action to reduce risk** — train staff, diversify, insure, avoid. **4. Monitor and review** — update plans for new risks." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Explain two reasons why it is important for a business to manage risks.", model: "**1. Avoids costly mistakes**: By identifying risks in advance, a business can prevent legal, financial or reputational harm before it happens. For example, training staff in machinery safety and conducting regular checks prevents workplace accidents that would cause downtime and compensation claims.\n\n**2. Improves financial sustainability**: Businesses that manage risk are more resilient to disruptions and market shifts. By spreading risk through diversification — for example, a food brand expanding into both retail and online — the business protects revenue if one channel suffers, helping it survive long-term." },
            { type: "short", marks: 4, prompt: "Outline the four steps involved in risk management.", model: "**1. Identify the risk** — Spot potential threats through audits and reviews (e.g. injury, theft, cyberattack).\n**2. Assess its impact** — Judge likelihood and severity of each risk to prioritise action.\n**3. Take action to reduce risk** — Train staff, diversify, insure, or avoid high-risk activities.\n**4. Monitor and review** — Update plans regularly as new risks emerge." }
          ]
        },
        {
          id: "lo12-3",
          code: "12.3",
          title: "Risk management strategies and types of insurance",
          notes: [
            { h: "Strategy 1 — Avoidance", b: "Not engaging in an activity that presents significant or unmanageable risk. *Example*: festival cancelled due to weather warnings; food start-up avoids allergen products if it can't guarantee safety." },
            { h: "Strategy 2 — Spread (Diversification)", b: "Diversifying products, suppliers, markets, channels. *Example*: farm sells locally and via online delivery; Netflix produces international content (Squid Game) to reduce US reliance." },
            { h: "Strategy 3 — Prevention", b: "Proactive steps to reduce likelihood. *Example*: hotel installs sprinklers and trains staff in fire safety; Apple performs rigorous battery testing." },
            { h: "Strategy 4 — Insurance", b: "Transfers financial cost of a risk to an insurer for a premium. *Example*: tech start-up takes out cyber insurance; construction firm insures equipment and workers." },
            { h: "Types of business insurance", b: "**Public Liability** — injury/damage to customers/property (slip in shop). **Employer Liability** — staff injury at work. **Product Liability** — injury from faulty products. **Buildings & Contents** — premises and stock (fire, flood, theft). **Motor** — company vehicles (legally required). **Key Person** — loss of vital staff. **Fidelity Guarantee** — internal theft/fraud by staff. **Goods in Transit** — damage during transport. **Cyber** — cyberattacks, breaches. **Professional Indemnity** — claims of poor advice. **Business Interruption** — income loss during closures (fire, flood, pandemic)." }
          ],
          questions: [
            { type: "short", marks: 16, prompt: "Discuss four risk management strategies that can be used by businesses to respond to potential risk. (4 @ 4m)", model: "**1. Avoidance**: Not engaging in an activity that presents significant or unmanageable risk. *Example*: A festival organiser cancels an outdoor event due to weather warnings, avoiding reputational and financial loss. A food start-up may avoid expanding into allergen-sensitive products if it cannot guarantee safety.\n\n**2. Spread (Diversification)**: Diversifying products, suppliers, markets or channels to reduce overreliance on one area. *Example*: Netflix produces international content like Squid Game to reduce reliance on the US market and audience.\n\n**3. Prevention**: Proactive steps to reduce the likelihood of risks occurring. *Example*: A hotel trains staff in fire safety and installs sprinklers; Apple performs rigorous battery testing to prevent product malfunctions.\n\n**4. Insurance**: Transferring the financial cost of a risk to an insurer in exchange for a premium. *Example*: A tech start-up takes out cyber insurance to cover recovery costs from a data breach. Insurance does not prevent the risk but ensures the business can recover financially." },
            { type: "short", marks: 12, prompt: "Outline three types of insurance a small bakery café should consider, with reasons for each. (3 @ 4m)", model: "**1. Public Liability Insurance**: Covers injury or damage to customers on the premises. Essential for a café where customers may slip on a wet floor or be injured by faulty furniture — protects against expensive legal claims.\n\n**2. Buildings & Contents Insurance**: Covers premises and stock against fire, flood and theft. *Example*: an electrical fault damaging a fridge full of stock — this insurance allows quick recovery without severe financial loss.\n\n**3. Motor Insurance**: Legally required for company vehicles. The bakery uses its van for cake deliveries, so motor insurance ensures compensation if there is an accident during a delivery and protects the business from claims." },
            { type: "mcq", marks: 2, prompt: "A construction company insuring its equipment and workers in case of site accidents is using which risk management strategy?", options: ["Avoidance", "Spread", "Prevention", "Insurance"], correct: 3, model: "Insurance — transferring the financial cost of a risk to an insurer in exchange for a premium." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 16 =================== */
    {
      id: "ch16",
      number: 16,
      strand: 3,
      title: "The Rationale for Planning",
      learningOutcomes: [
        {
          id: "lo16-1",
          code: "16.1",
          title: "Internal and external changes facing organisations",
          notes: [
            { h: "Internal changes", b: "**Leadership changes** — new vision and management style. **Adoption of technology** — new systems require staff training. **Restructuring/downsizing** — merging teams, layoffs to remain sustainable. **Change in business model/strategy** — new products, new markets. **Cultural/organisational development** — autonomy, remote working." },
            { h: "External changes", b: "**Market trends and consumer expectations** — ethical, digital-first preferences. **Economic trends** — inflation, interest rates, minimum wage. **Legal and regulatory changes** — GDPR. **Digital disruption and transformation** — invest in new systems/skills. **Competitors' innovations** — innovate to stay relevant." }
          ],
          questions: [
            { type: "short", marks: 10, prompt: "Outline three internal changes and two external changes an organisation might encounter through its lifetime.", model: "**Internal**:\n**1. Leadership changes** — A new CEO can bring different priorities, management style and vision, leading to changes in culture and strategy.\n**2. Adoption of technology** — Introducing new software or automation forces process and training changes for staff.\n**3. Restructuring or downsizing** — Economic pressure may lead to merging teams, redundancies or layoffs to keep the business sustainable.\n\n**External**:\n**1. Legal and regulatory changes** — New laws like GDPR force businesses to update systems and processes, with significant fines for non-compliance.\n**2. Digital disruption** — New technology and digital-first competitors push existing businesses to invest in new systems and skills to stay relevant." }
          ]
        },
        {
          id: "lo16-2",
          code: "16.2",
          title: "Reasons for resistance to change",
          notes: [
            { h: "Reasons for resistance", b: "**Fear of job losses** — new tech or outsourcing may reduce/replace roles. **Fear of failure** — doubt about adapting to new systems. **No clear benefit communicated** — staff see change as unnecessary or risky. **Inertia** — preference for familiar routines, 'the way things have always been done'." }
          ],
          questions: [
            { type: "short", marks: 16, prompt: "Analyse four reasons for resistance to change in an organisation. (4 @ 4m)", model: "**1. Fear of Job Losses**: When new technology or outsourcing is introduced, employees may worry their roles will be cut or replaced. This fear grows if management doesn't communicate openly that change supports growth rather than redundancies. The result is low engagement and active opposition to the change.\n\n**2. Fear of Failure**: Employees can doubt their ability to adapt to new systems or responsibilities. Without proper training and reassurance, they resist change to avoid making mistakes or being judged in front of colleagues.\n\n**3. No Clear Benefit Communicated**: Staff are more likely to support change when they understand how it helps them or the organisation. If management doesn't explain the benefits clearly, employees view the change as unnecessary or risky and resist it.\n\n**4. Inertia**: Many people prefer familiar routines and resist moving away from 'the way things have always been done'. Leaders need to create a clear vision of why change matters and how it will improve the workplace to overcome this." }
          ]
        },
        {
          id: "lo16-3",
          code: "16.3",
          title: "Practices that promote innovation and intrapreneurial thinking",
          notes: [
            { h: "Practices to support new ideas", b: "**1. Leadership Culture that Encourages Risk-Taking** — make it safe to take smart risks and learn from mistakes. **2. Provide Training and Resources to Staff** — invest time, funding and skills development. **3. Use of Teamwork and Collaboration** — across departments to share perspectives. **4. Recognition and Rewards for Innovation** — praise, bonuses, opportunities to motivate creative contributions." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Identify three practices that promote innovation and intrapreneurial thinking in an organisation. (3 @ 4m)", model: "**1. Leadership Culture that Encourages Risk-Taking**: Leaders should promote an environment where employees feel safe to take smart risks and learn from mistakes. This builds the confidence needed for staff to come forward with creative ideas without fear of being penalised.\n\n**2. Provide Training and Resources**: Businesses should invest in time, funding and skills development so employees can explore new ideas. *Example*: Google's 20% time policy gives staff space to work on new concepts.\n\n**3. Recognition and Rewards for Innovation**: Acknowledging staff for creative contributions through praise, bonuses or career opportunities motivates continued innovation. People are far more likely to share new ideas when they see them recognised and acted on." }
          ]
        },
        {
          id: "lo16-4",
          code: "16.4",
          title: "Overcoming resistance to change",
          notes: [
            { h: "Approaches", b: "**Lead by Example** — leaders model the behaviour expected. **Open Communication and Consultation** — explain the why and involve staff. **Training and Resource Support** — tools and guidance reduce anxiety. **Employee Empowerment** — give ownership over their role in change. **Rewarding Staff** — recognise those who embrace change. **Use of Teamwork and Collaboration** — peer support reduces isolation." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline two ways an organisation can overcome resistance to change.", model: "**1. Open Communication and Consultation**: Explaining why the change is happening and involving staff in decisions reduces fear and rumours. When employees feel informed and consulted — for example through Q&A sessions and feedback surveys — they are far more likely to support the change.\n\n**2. Training and Resource Support**: Providing the right tools, training and guidance helps employees feel prepared. *Example*: when introducing new software, dedicated training time and easy-to-access support reduces anxiety about new responsibilities and avoids the fear of failure that often drives resistance." }
          ]
        },
        {
          id: "lo16-5",
          code: "16.5",
          title: "Strategic planning as an ongoing process",
          notes: [
            { h: "What strategic planning is", b: "The ongoing process of setting long-term goals and deciding how the business will achieve them. Acts as a roadmap, sets a clear vision, aligns people and resources." },
            { h: "Steps in strategic planning", b: "**1. Define vision through Mission Statement** — values, purpose, long-term ambition. **2. Analyse internal and external environment** — SWOT and STEEPLE. **3. Set long-term plan** — 5–10 year goals using SMART objectives. **4. Tactical Plans** — break into 1–2 year smaller chunks for departments. **5. Operational Plans** — implement day-to-day." },
            { h: "Why ongoing", b: "Regular reviews track progress and adjust goals; changing markets require updates; identifies new risks early; supports continuous improvement." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline what is meant by strategic planning and explain why it is an ongoing process.", model: "**Strategic planning** is the ongoing process of setting long-term goals (typically 5–10 years) and deciding how the business will achieve them. It begins with a mission statement, uses tools like SWOT and STEEPLE to analyse the internal and external environment, sets SMART long-term goals, and breaks them down into tactical and operational plans.\n\nIt is **ongoing** because the business environment is constantly changing — new competitors emerge, customer expectations shift, technology evolves, and laws change. Regular reviews allow the business to track progress, adjust goals where needed and identify new risks early. A static plan would quickly become out of date, leaving the business unable to adapt." },
            { type: "short", marks: 5, prompt: "Outline the steps involved in the strategic planning process.", model: "**1. Define the vision through the mission statement** — outlining values, purpose and long-term ambition.\n**2. Analyse the internal and external environment** using tools like SWOT and STEEPLE.\n**3. Set the long-term plan** — 5–10 year SMART goals.\n**4. Break long-term plans into tactical plans** — 1–2 year chunks for departments.\n**5. Implement through operational plans** — day-to-day running of the business." }
          ]
        },
        {
          id: "lo16-6",
          code: "16.6",
          title: "Benefits of strategic planning",
          notes: [
            { h: "Benefits", b: "**1. Increased clarity and direction** — clear long-term goal, consistent decisions across departments. **2. Increased ability to manage change** — respond without losing focus, adjust plans as environment changes. **3. Increased resource efficiency** — allocate staff, money and time to top priorities. **4. Increased competitive advantage** — regular SWOT review supports innovation, differentiation and early opportunities." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Describe three benefits of strategic planning for an organisation.", model: "**1. Increased Clarity and Direction**: A strategic plan gives the business a clear long-term goal, helping leaders and departments make consistent decisions and avoid being distracted by short-term issues.\n\n**2. Increased Resource Efficiency**: It helps the business allocate staff, money and time to the priorities that matter most for long-term success, reducing wasted effort on low-value activities.\n\n**3. Increased Competitive Advantage**: Regular review of strengths, weaknesses, opportunities and threats helps the business stay ahead. It supports innovation, differentiation and early identification of opportunities — for example, spotting an emerging customer trend before competitors react." }
          ]
        },
        {
          id: "lo16-7",
          code: "16.7",
          title: "Force-Field Analysis",
          notes: [
            { h: "What it is", b: "An approach to identify and analyse forces that drive and inhibit change. Forces can be internal or external." },
            { h: "Steps", b: "**1. Define the strategic change clearly** (e.g. moving back to office). **2. Identify driving and restraining forces** — internal (employee morale, skills, culture) and external (laws, technology, customer expectations). **3. Assign a score/weight (1–5)** based on strength of influence. **4. Analyse the results** — if restraining > driving: strengthen drivers, reduce restrainers, delay/cancel, or revise strategy and re-run analysis." },
            { h: "Worked example — Hybrid back to full-time office", b: "Driving forces (collaboration, oversight, culture) totalled 11. Restraining forces (commuting time, retention risk, work-life balance) totalled 17. Restraining > driving → reconsider; alternative: 3-day office week to reduce restrainers." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Use a Force Field Analysis to examine the potential effects of a decision to move all staff back to the office full-time.", model: "**Driving Forces (favouring the change)**:\n• Improved face-to-face collaboration and culture (score: 4)\n• Easier supervision and management oversight (score: 3)\n• Stronger company culture and onboarding for new staff (score: 4)\n**Total Driving = 11**\n\n**Restraining Forces (against the change)**:\n• Reduced staff satisfaction and work-life balance (score: 5)\n• Increased risk of staff turnover, especially senior talent (score: 5)\n• Higher commuting and childcare costs for staff (score: 4)\n• Reduced ability to attract talent who want flexibility (score: 3)\n**Total Restraining = 17**\n\n**Analysis**: Restraining forces (17) clearly outweigh driving forces (11). The proposed change risks staff dissatisfaction, retention problems and reduced ability to hire. The business should consider an alternative such as a three-day office / two-day remote hybrid, which preserves the collaboration benefits while reducing the strongest restraining forces." },
            { type: "short", marks: 8, prompt: "Indicate whether each of the following statements relating to a hybrid working model is a driving force or a restraining force: (1) may result in employees feeling isolated, (2) would help fulfil the wellness programme, (3) may lead to difficulty in monitoring productivity, (4) may bring about a higher likelihood of confidentiality breaches.", model: "**1. Restraining force** — isolation undermines collaboration and morale.\n**2. Driving force** — supports the wellness programme objective.\n**3. Restraining force** — harder oversight makes the change less attractive.\n**4. Restraining force** — confidentiality risk argues against hybrid working." }
          ]
        },
        {
          id: "lo16-8",
          code: "16.8",
          title: "Contingency planning for crisis management",
          notes: [
            { h: "What is contingency planning?", b: "A backup plan prepared in advance for unexpected events that could disrupt operations. Outlines steps to protect staff, customers, finances and reputation." },
            { h: "Importance for crisis management", b: "Allows business to: **respond quickly** to reduce panic; **protect staff and assets**; **maintain operations** or restore them quickly; **minimise damage** to finances, brand or supply chains." }
          ],
          questions: [
            { type: "short", marks: 5, prompt: "Explain the term 'contingency planning'.", model: "**Contingency planning** is the process of preparing a backup plan in advance to deal with unexpected events or emergencies that could disrupt business operations — for example, a fire, cyberattack, supply chain failure or pandemic. It outlines the steps the business will take if something goes wrong, helping to protect staff, customers, finances and reputation. It allows the business to respond quickly, reducing panic and confusion, maintain operations where possible, and minimise damage to the business if a crisis occurs." }
          ]
        },
        {
          id: "lo16-9",
          code: "16.9",
          title: "Factors to consider when developing a contingency plan",
          notes: [
            { h: "Factors", b: "**Cost** — spending on training, backup systems, alternative suppliers — must be weighed against larger damage if no plan exists. **Timing** — some risks need immediate response, others allow more preparation. Acting quickly prevents small disruptions becoming major crises. **Risk** — not all risks are equally likely or severe. Prioritise high-impact, high-probability risks. **Communication** — clear communication during a crisis reduces confusion, identifies who needs to be contacted and how, and protects reputation." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Discuss two factors that should be considered when developing a contingency plan.", model: "**1. Risk**: Not every risk is equally likely or equally severe. Businesses must prioritise the most serious threats — those with high probability and high impact — and assign more detailed planning to them. Focusing resources on the biggest risks makes the plan more effective and prevents wasted time on low-impact events.\n\n**2. Communication**: Clear communication during a crisis reduces confusion and helps the business respond faster. The plan should outline who needs to be contacted (e.g. emergency services, key staff, customers, regulators), how messages will be delivered (email, social media, phone tree), and who is responsible for issuing updates. Strong communication prevents mistakes, protects the business's reputation and supports a faster recovery." },
            { type: "mcq", marks: 2, prompt: "When developing a contingency plan, which factor relates to deciding how quickly the business must respond to a particular type of risk?", options: ["Cost", "Timing", "Risk", "Communication"], correct: 1, model: "Timing — matching the urgency of the threat to the response speed in the plan." }
          ]
        }
      ]
    },

    /* =================== CHAPTER 17 =================== */
    {
      id: "ch17",
      number: 17,
      strand: 4,
      title: "Making Informed Decisions as a Consumer",
      learningOutcomes: [
        {
          id: "lo17-1",
          code: "17.1",
          title: "Consumer rights and responsibilities under current legislation",
          notes: [
            { h: "Competition and Consumer Protection Commission (CCPC)", b: "Independent statutory body that promotes consumer rights and fair competition. **Functions**: Advise/inform consumers (ccpc.ie), educate (financial calculators, comparison tools), advise government on policy, enforce consumer law (investigate, on-the-spot fines), publish Consumer Protection List of breaches/convictions, promote fair competition (prevent monopolies)." },
            { h: "Consumer Rights Act 2022 — buying products", b: "**Faulty within 30 days**: full refund (must be issued within 14 days). **Fault after 30 days but within 12 months**: free repair or replacement; if serious or repair fails, full/partial refund. **First 12 months**: assumed faulty at time of purchase unless seller proves otherwise (burden of proof on retailer). Same rights apply to sale items, reduced-price items, and second-hand goods bought from a business. Does **not** apply to wear and tear, accidental damage, or where the consumer didn't install a required update." },
            { h: "Right to Cancel a Distance Contract", b: "When buying online, by phone, mail order or doorstep — consumers have **14 days from receipt** to cancel without giving a reason." },
            { h: "Consumer Rights Act 2022 — services", b: "Seller must give name, address, phone, full details, total price (incl. VAT) or how price will be calculated. **Redress**: No supply → cancel and refund; Problem with service → refund or price reduction; Damage caused → claim compensation; **Cooling-off**: 14 days to cancel many services." },
            { h: "Digital content & services", b: "Right to refund if not supplied as agreed; price reduction or refund for serious issues. *Example*: Netflix, Spotify, TikTok (services); games, music, e-books (content)." },
            { h: "Other points", b: "Guarantees/warranties **add to** legal rights, never replace them. **Change of mind** in-store: no automatic right to refund/exchange unless faulty. **Gift vouchers**: don't have to spend full amount at once, can combine, minimum 5-year expiry. **Sale items**: same rights as full price. **Unfair contract terms**: businesses cannot exclude liability for negligence." },
            { h: "Consumer Protection Act 2007", b: "Protects consumers from misleading, false, aggressive practices. Applies to businesses and influencers. **Pricing**: clear/inclusive of taxes; if advertising a sale, the 'prior price' must be the lowest price in the 30 days before. **Influencer marketing**: paid promotions and gifted items must be clearly labelled. CCPC can issue compliance notices, on-the-spot fines (€300) and publish Consumer Protection List." },
            { h: "Enforcing rights", b: "**1. Direct Resolution** — contact retailer first, cheapest and quickest. **2. Alternative Dispute Resolution (ADR)** — third party helps without going to court. **3. Small Claims Procedure** — €25 fee, up to €2,000, no solicitor needed, response in 2 weeks. **4. Ombudsman** — last resort for public services; recommendations only (not legally binding)." },
            { h: "Shopping in EU vs non-EU", b: "**EU**: Same consumer rights apply across EU; **European Small Claims Procedure** for cross-border disputes up to €5,000 (€25 fee). **Non-EU**: Limited legal protections, more difficult to enforce rights." },
            { h: "Consumer responsibilities", b: "**Be informed** — research before buying. **Keep records** — receipts, contracts, warranties. **Use products correctly** — as intended. **Choose ethical/sustainable** options." }
          ],
          questions: [
            { type: "tf", marks: 8, prompt: "Mark each TRUE or FALSE: (1) Consumers always have a 14-day cooling-off period for purchases made in physical shops. (2) Digital services bought from EU-based businesses must include the most up-to-date version. (3) Buying from non-EU websites gives consumers the same legal protections as buying from EU retailers. (4) Consumers are only entitled to a repair if a product is faulty within 30 days.", correct: false, model: "**1. FALSE** — The 14-day cooling-off period applies to distance contracts (online, phone, mail, doorstep), not in-store purchases.\n**2. TRUE** — Under the Consumer Rights Act 2022, digital services from EU sellers must include up-to-date versions.\n**3. FALSE** — Non-EU purchases have far weaker protection and are harder to enforce.\n**4. FALSE** — Within 30 days, a consumer is entitled to a full refund. After 30 days but within 12 months they are entitled to a repair or replacement (and refund if these fail)." },
            { type: "short", marks: 8, prompt: "Outline two rights a consumer has when they are using a service.", model: "**1. Right to a service carried out with due skill, care and diligence**: The provider must complete the work to the standard expected of a competent professional in that field — for example, a mechanic must repair a car correctly using appropriate tools and methods.\n\n**2. Right that the service matches what was agreed or described**: If the business promises certain work, materials or a particular level of service, they must deliver as stated. *Example*: a cleaning service that agreed to clean every room must do so." },
            { type: "short", marks: 8, prompt: "Outline two forms of redress available to a consumer for a service that is not carried out appropriately.", model: "**1. Refund / Cancellation**: If the service is not provided at all or is not delivered on the agreed date, the consumer can cancel the contract and receive a refund within 14 days of agreement.\n\n**2. Price Reduction or Compensation**: If the service is carried out but not done properly, the consumer may be entitled to a price reduction. If the service caused additional financial loss or damage — for example, a plumber causing flooding — the consumer can claim compensation." },
            { type: "short", marks: 8, prompt: "Based on current consumer legislation, explain two forms of redress available for a faulty good.", model: "**1. Refund**: If a product is faulty within 30 days of purchase, the consumer is entitled to a full refund. The seller must issue this within 14 days of receiving the returned item.\n\n**2. Repair or Replacement**: If the fault appears after 30 days but within 12 months, the consumer is entitled to a free repair or replacement within a reasonable time and without major inconvenience. If the fault is serious, repair fails, replacement isn't offered, or the cost is excessive, the consumer can request a full or partial refund." },
            { type: "short", marks: 6, prompt: "Outline three main functions of the Competition and Consumer Protection Commission (CCPC).", model: "**1. Advise and Inform Consumers** — Provides clear information through ccpc.ie and social media to help consumers understand their rights, including simplified explanations of laws like the Consumer Rights Act 2022.\n\n**2. Enforce Consumer Law** — Has legal powers to investigate breaches of consumer legislation, enter premises, and issue on-the-spot fines of €300 where laws are broken.\n\n**3. Publish the Consumer Protection List** — Names businesses that have received compliance notices, been fined or been convicted of consumer offences, helping consumers make informed choices." }
          ]
        },
        {
          id: "lo17-2",
          code: "17.2",
          title: "Ethics, sustainability and the circular economy",
          notes: [
            { h: "Ethical concerns", b: "**Fair treatment of workers** — choosing Fairtrade or ethically sourced products. **Animal welfare** — cruelty-free or vegan (Leaping Bunny logo). **Data protection and online privacy** — limiting data shared, reading privacy policies. **Supporting local businesses** — choosing Irish even at slightly higher prices." },
            { h: "Sustainability concerns", b: "**Packaging waste** — choosing recyclable or minimal packaging. **Carbon footprint and transport** — buying locally to reduce emissions. **Overproduction and waste** — avoiding fast fashion, choosing durable goods. **Energy efficiency and resource use** — energy-efficient appliances, LED lighting." },
            { h: "Shadow economy", b: "Transactions outside the formal economy, unrecorded by Revenue (tax evasion, undeclared wages, counterfeit goods, dodgy boxes). **Consequences**: For **consumers** — unsafe, unregulated, no legal protection or refund. For **businesses** — legitimate firms undercut by illegal traders. For **government** — loss of tax revenue (VAT, income tax, corporation tax), higher enforcement costs." },
            { h: "Circular economy", b: "Model of production/consumption that extends product life cycles, reduces waste and creates value. Focuses on re-using, recycling and re-purposing instead of single-use throwaway. **How consumers contribute**: 1. **Buying second-hand** (Depop, Vinted, charity shops, refurbished electronics). 2. **Recycling products** (WEEE recycling for electronics; donating clothing). 3. **Improving consumption habits** (using devices longer, repairing clothes). 4. **Choosing sustainable brands** (energy-efficient appliances, Fairtrade, organic clothing)." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Describe four ways a consumer purchasing food products can actively contribute to the circular economy. (4 @ 3m)", model: "**1. Buying loose/unpackaged products**: Choosing fruit, vegetables and grains sold loose or in bulk reduces single-use packaging waste sent to landfill.\n\n**2. Choosing local and seasonal foods**: Buying locally produced, in-season food reduces the carbon footprint from long-distance transport and supports Irish producers.\n\n**3. Reducing food waste through better habits**: Planning meals, freezing leftovers, and composting peelings extends the life of food and reduces what goes to landfill.\n\n**4. Choosing reusable packaging and refill stations**: Bringing reusable containers to refill shops or buying products in returnable glass containers (e.g. milk in glass bottles) keeps packaging in circulation rather than throwing it away after one use." },
            { type: "short", marks: 8, prompt: "Outline two consequences of participation in the shadow economy: (i) for the consumer, (ii) for the economy.", model: "**(i) For the consumer**:\n**1. No legal protection** — Goods bought through the shadow economy are unregulated, so the consumer has no right to a refund, repair or replacement if something goes wrong.\n**2. Unsafe products** — Items like 'dodgy boxes' or counterfeit electronics may not meet safety standards, putting the consumer at risk of fire, electric shock or other harm.\n\n**(ii) For the economy**:\n**1. Loss of tax revenue** — VAT, income tax and corporation tax are not paid on shadow transactions, reducing funds available for public services like health and education.\n**2. Higher enforcement costs** — The government must spend more on inspections, Revenue investigations and prosecution to tackle illegal trading, putting further strain on public finances." },
            { type: "short", marks: 6, prompt: "Explain the term 'circular economy' and describe two ethical concerns of Irish consumers when purchasing from online retailers.", model: "**Circular economy**: A model of production and consumption that extends the life cycle of products, reduces waste and creates further value. It focuses on reusing, recycling and re-purposing items rather than single-use disposal — moving away from 'buy, use once, throw away'.\n\n**Ethical concerns when buying online**:\n**1. Fair treatment of workers** — Consumers may be concerned that fast fashion or cheap imports rely on unfair wages or poor conditions; many now check whether brands publish information on factory conditions before buying.\n**2. Data protection and online privacy** — Consumers worry about how online retailers collect and use their personal data, including tracking, cookies and targeted ads, and may avoid retailers with poor privacy practices." }
          ]
        },
        {
          id: "lo17-3",
          code: "17.3",
          title: "Impact of digital technology on consumer behaviour",
          notes: [
            { h: "Positive impacts", b: "**Increased convenience** — Amazon one-click, mobile banking. **Better access to information** — comparison tools (Bonkers.ie, ccpc.ie). **Greater choice** — wider product range from Irish/international sellers. **Price transparency**, **customer reviews/ratings** (Trustpilot), **improved accessibility** (rural areas, mobility issues)." },
            { h: "Negative impacts", b: "**Impulse buying and overconsumption** — shopping apps, targeted ads, influencer marketing. **Reduced social interaction** — physical stores closing. **Increased screen time and digital addiction** — TikTok/Instagram driving spending. **Information overload (paradox of choice)**, greater exposure to scams/fraud, reduced privacy (tracking, cookies)." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Analyse three ways digital technology can influence consumer behaviour. (3 @ 4m)", model: "**1. Increased Convenience**: Online platforms like Amazon offer one-click purchasing and next-day delivery, while mobile banking apps allow instant transfers without visiting a branch. Consumers now expect speed and ease as a baseline, and are likely to abandon retailers whose websites or checkouts are clunky.\n\n**2. Better-informed Decisions**: Consumers can compare prices, features and reviews before buying — for example using Bonkers.ie for broadband or Trustpilot for product reviews. This shifts power towards consumers, making them more price-sensitive and more likely to choose based on objective evidence rather than advertising.\n\n**3. Impulse Buying and Overconsumption**: Constant access to shopping apps, targeted ads and influencer marketing leads to unplanned purchases. Social media platforms allow direct purchases through influencer posts, encouraging spending that consumers might otherwise have considered more carefully — leading to financial strain and overconsumption." },
            { type: "short", marks: 6, prompt: "Evaluate two negative impacts of digital technology on consumer behaviour.", model: "**1. Impulse buying and overconsumption** has been amplified by 24/7 access to shopping apps and targeted advertising. Consumers may regret unplanned purchases and accumulate debt. While technology offers convenience, it also makes it harder for consumers to control spending, especially when influencer marketing and limited-time offers create urgency.\n\n**2. Reduced privacy** is a serious concern, as websites track behaviour through cookies and apps collect personal data for resale or targeted ads. Consumers often share data without realising the extent. The balance is therefore mixed — digital technology empowers consumers with information, but it can also exploit them. Effective regulation (like GDPR) and consumer education are essential to manage these risks." }
          ]
        },
        {
          id: "lo17-4",
          code: "17.4",
          title: "Personal data protection — GDPR",
          notes: [
            { h: "GDPR overview", b: "EU regulation across all member states including Ireland. Sets out: rights of data subjects, responsibilities of data controllers, role of Data Protection Commissioner (DPC)." },
            { h: "Data Subject", b: "The individual whose data is collected. Personal data = anything that can identify them (name, passport, financial records, address, employment details)." },
            { h: "Rights of data subjects", b: "**1. Right not to be subject to automated decision-making** — important decisions (creditworthiness, performance ratings) cannot be made solely by AI without consent. **2. Right to complain** to the DPC. **3. Right of access, correction, and erasure** ('right to be forgotten') — request a copy, correct inaccuracies, delete data (e.g. TikTok account)." },
            { h: "Responsibilities of Data Controllers (businesses)", b: "**1. Report data breaches** to DPC within 72 hours (e.g. bank notifies DPC and customers). **2. Keep data safe and secure** with encryption, restricted access (e.g. healthcare patient records)." },
            { h: "Functions of the DPC", b: "Investigates complaints, informs people of rights, conducts investigations (Meta, Google, Apple, WhatsApp, LinkedIn), promotes compliance, identifies risks. **Penalties**: up to €20 million or 4% of global annual turnover, whichever is higher. *Example*: 2023 — Meta fined €1.2 billion for unlawful EU→US data transfers." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Based on current EU law, outline two rights consumers have in relation to protection of their personal data.", model: "**1. Right of Access, Correction and Erasure**: Individuals can request a copy of the data a business holds about them, ask for inaccurate data to be corrected, and ask for their data to be erased — known as the 'right to be forgotten'. *Example*: a TikTok user can request that their account and all associated data be deleted.\n\n**2. Right not to be subject to automated decision-making**: Important decisions, such as creditworthiness or job application screening, cannot be made solely by automated systems without the individual's consent. Consumers have the right to a human being involved in decisions that significantly affect them." },
            { type: "short", marks: 8, prompt: "Identify two responsibilities of data controllers under GDPR.", model: "**1. Report data breaches within 72 hours**: Businesses must notify the Data Protection Commissioner of any personal data breach within 72 hours of becoming aware of it, and inform affected customers if there is a high risk to their rights. *Example*: a bank must inform the DPC and customers if customer data is hacked.\n\n**2. Keep data safe and secure**: Businesses must implement appropriate technical and organisational security measures to protect personal data, such as encryption, restricted access and secure storage. *Example*: healthcare organisations using encryption and limited access for patient records." },
            { type: "short", marks: 5, prompt: "Evaluate the role of the Data Protection Commissioner (DPC).", model: "The DPC plays a critical role in enforcing GDPR in Ireland. **Strengths**: It has strong penalty powers — fines up to €20 million or 4% of global turnover — and has used them, fining Meta €1.2 billion in 2023 for unlawful EU-to-US data transfers. It investigates complaints, conducts independent investigations into giants like Google, Apple and LinkedIn, and educates the public on their rights. **Limitations**: As Ireland hosts the EU HQ of many big tech firms, the DPC handles a vast caseload that can lead to delays. Some campaigners have criticised the speed of its enforcement. **Overall**: the DPC is essential to GDPR enforcement and creates a strong incentive for businesses to handle data correctly, but its effectiveness depends on resourcing and case turnaround." }
          ]
        },
        {
          id: "lo17-5",
          code: "17.5",
          title: "Importance of making informed consumer decisions",
          notes: [
            { h: "What being an informed consumer means", b: "Having the knowledge and understanding of the impact of your decisions, and the skills to make choices in your best interest around price, value, quality and ethics." },
            { h: "Importance", b: "**Improves financial wellbeing** — comparing prices, quality and long-term costs avoids unnecessary spending. **Improves safety** — buying from legitimate, certified providers reduces risk of unsafe products. **Improves legal protection** — knowing rights increases the chance of refund/repair (buying from registered businesses, not the shadow economy). **Positive social and environmental impact** — supports ethical brands and reduces environmental harm (Fairtrade, locally produced)." }
          ],
          questions: [
            { type: "short", marks: 12, prompt: "Discuss three reasons why making informed consumer decisions is important. (3 @ 4m)", model: "**1. Improves Financial Wellbeing**: By comparing prices, quality and long-term costs, consumers avoid unnecessary spending. *Example*: comparing total mortgage repayments between lenders before signing can save thousands of euro over the life of the loan.\n\n**2. Improves Legal Protection**: Knowing your consumer rights increases the chance of receiving a refund, repair or replacement if something goes wrong. Buying from registered Irish businesses rather than the shadow economy means you have legal recourse through the CCPC, Small Claims Court and Consumer Rights Act 2022.\n\n**3. Positive Social and Environmental Impact**: Informed consumers can support ethical brands and reduce environmental harm. *Example*: choosing Fairtrade chocolate or locally produced food lowers carbon impact and supports fair worker treatment, encouraging more businesses to adopt sustainable practices." }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 1 =================== */
    {
      id: "pe1",
      number: 1,
      subject: "pe",
      title: "Physical Demands of Performance",
      learningOutcomes: [
        {
          id: "pe1-1",
          code: "1.1",
          title: "Health, fitness, components and fitness testing",
          notes: [
            { h: "Health, Fitness, Well-being", b: "Health (WHO): state of complete physical, mental and social well-being, not merely absence of disease. Fitness: ability to carry out everyday tasks without becoming overly tired. Well-being: combination of mental and social elements that contribute to fulfilment. Regular exercise reduces risk of heart disease, obesity, high blood pressure, adult-onset diabetes, osteoporosis and stroke." },
            { h: "Two categories of fitness", b: "Health-related fitness — 5 components essential for health (mnemonic: Cows Make Milk For Bones). Performance-related (skill-related) fitness — 6 components that enhance performance (mnemonic: All Big Cats Pounce Really Softly)." },
            { h: "Health-related components (5)", b: "1. Cardiorespiratory endurance — delivering oxygen and nutrients to muscles over a sustained period. 2. Muscular endurance — ability of a muscle/muscle group to generate force repetitively without fatiguing. 3. Muscular strength — maximal force a muscle can produce. 4. Flexibility — range of motion at a joint. 5. Body composition — percentage of body fat vs non-fat mass." },
            { h: "Body composition and somatotypes", b: "Measured by body fat % or BMI (mass kg / height m squared; high muscle mass can give a false high BMI). Ectomorph: long, lean, low body fat, low musculature, fast metabolism (high jumper, long-distance runner). Mesomorph: broad shoulders, narrow hips, high musculature, moderate fat, gains muscle easily (sprinter, swimmer). Endomorph: apple-shaped, high body fat, slow metabolism, gains fat and muscle easily (sumo wrestler, prop forward)." },
            { h: "Performance-related components (6)", b: "1. Agility — change direction and speed quickly and efficiently. 2. Balance — maintain equilibrium (static = stationary, dynamic = moving). 3. Coordination — move two or more body parts in a controlled, smooth way. 4. Power — exert maximal force in as short a time as possible (Power = force x time). 5. Reaction time — how quickly the brain initiates a response to a stimulus. 6. Speed — how fast a body is moving." },
            { h: "Needs analysis", b: "Process of determining the qualities necessary for a sport, an athlete, or a combination. Allows a training programme to target sport-specific fitness based on the demands of the sport, position and role." },
            { h: "Fitness testing", b: "Form of assessment for performer needs and optimum performance. Identifies strengths and weaknesses to set realistic goals. Test battery: collection of tests specific to the sport. Field tests are practical and school-friendly; lab tests are more accurate." },
            { h: "Key fitness tests", b: "Cardiorespiratory endurance: Cooper 12-minute run (estimates VO2 max) or multistage 20m bleep test. Muscular endurance: push-up test, sit-up test. Muscular strength: standing broad jump (lower), seated medicine ball throw (upper), 1RM/3RM, hand grip dynamometer. Flexibility: sit-and-reach. Body composition: BMI, body fat callipers, BODPOD, DEXA scan. Agility: Illinois Agility Test, T-drill. Balance: stork balance test. Coordination: alternative hand wall toss. Power: vertical jump. Reaction time: ruler drop test. Speed: 30m sprint." },
            { h: "Factors affecting assessment", b: "Standardised test: same protocol every time. Valid: measures what it claims to measure. Reliable: produces consistent results when repeated. Normative data: results compared against population norms." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline the five health-related components of fitness and briefly explain why each is important for general health.", model: "Cardiorespiratory endurance allows the heart and lungs to deliver oxygen to working muscles for sustained activity. Muscular endurance lets muscles work repeatedly without fatigue. Muscular strength is the maximal force a muscle can produce, important for lifting and pushing tasks. Flexibility provides pain-free range of motion at the joints. Body composition (lower body fat, higher lean mass) reduces the risk of obesity-related disease." },
            { type: "short", marks: 6, prompt: "Compare the three somatotypes and give a sporting example of each.", model: "Ectomorphs are tall and lean with low muscle mass and a fast metabolism, suited to long-distance running or high jump. Mesomorphs have broad shoulders, narrow hips and gain muscle easily, suiting sprinting and swimming. Endomorphs are short and rounded with higher body fat and slow metabolism, suited to sumo wrestling or prop forward in rugby." },
            { type: "short", marks: 6, prompt: "Describe two fitness tests, identifying the component each measures and one strength of each test.", model: "The Cooper 12-minute run measures cardiorespiratory endurance by recording distance covered in 12 minutes; it is cheap, simple and estimates VO2 max. The sit-and-reach test measures hamstring and lower-back flexibility; it is standardised and provides reliable, normative data for comparison." },
            { type: "short", marks: 5, prompt: "Explain the difference between a valid and a reliable fitness test.", model: "A valid test measures what it claims to measure — for example, the vertical jump genuinely measures leg power. A reliable test produces consistent results when repeated under the same conditions. A test can be reliable without being valid; a good test battery should be both." }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 2 =================== */
    {
      id: "pe2",
      number: 2,
      subject: "pe",
      title: "Training Methods and Fitness Plans",
      learningOutcomes: [
        {
          id: "pe2-1",
          code: "2.1",
          title: "Principles, methods, recovery and periodisation",
          notes: [
            { h: "Principles of training (SPORRT)", b: "Specificity — training must match the activity and goals (energy systems, muscles, components, intensity, time). Progressive overload — gradually increase Frequency, Intensity, Time or Type. Recovery — time for the body to repair and adapt. Reversibility — training effects diminish without progression (use it or lose it). Tedium — vary training to avoid boredom and keep performers motivated." },
            { h: "FITT formula", b: "Frequency (how often), Intensity (how hard), Time (how long), Type (what kind). Used to apply progressive overload." },
            { h: "Diminishing returns", b: "Rate of fitness improvement decreases over time as fitness approaches its potential. Fitter performers gain less from each training session." },
            { h: "Continuous training", b: "Exercising continuously without rest. Low intensity, minimum 20 minutes in the aerobic zone (70-80% MHR). Develops cardiorespiratory endurance." },
            { h: "Fartlek training", b: "Swedish 'speed play' — continuous training with varied speed and terrain. Develops aerobic AND anaerobic systems, lactate threshold and recovery times." },
            { h: "Interval training", b: "Periods of intense work followed by timed rest or cardiac-readiness rest. Structured in sets and reps; intensity expressed as % HR. Improves cardiorespiratory endurance, muscular endurance, speed and recovery." },
            { h: "Circuit training", b: "Series of 8-10 stations performed one after another, working different muscle groups. Types: aerobic, local muscular endurance, anaerobic, strength, flexibility, skill-related." },
            { h: "Weight training", b: "Uses external weights. Strength = high weight, low reps. Endurance = low weight, high reps. Power = moderate weight, explosive reps." },
            { h: "Plyometric training", b: "Uses speed and force to build muscle power: bounding, hopping, jumping, box jumps. Eccentric contraction (landing) followed quickly by concentric contraction (jumping)." },
            { h: "Flexibility training", b: "Deliberate programme to permanently increase range of motion. Static (hold at resistance), active (partner-assisted), ballistic (momentum, bouncing), PNF (stretch + contract — most effective): stretch to resistance, contract 5-6 sec, relax, hold 20-30 sec, recover 30 sec, repeat 2-4 times." },
            { h: "Adaptation and recovery", b: "Adaptation is the body getting accustomed to training through repeated exposure. Without rest, performance decreases and overtraining occurs. Strategies: passive recovery (complete rest), active recovery (low-intensity activity, improves blood flow), sleep (7-8 hours; non-REM releases growth hormones), nutrition, cryotherapy, foam rolling (self-myofascial release for DOMS), compression garments." },
            { h: "Periodisation", b: "Division of a training plan (usually yearly) into cycles. Macrocycle: full long-term cycle (yearly or 4-year Olympic plan) with preparation, competition and transition phases. Mesocycle: weeks emphasising the same type of adaptation. Microcycle: a small number of training sessions, often a daily breakdown." },
            { h: "Overtraining, peaking and tapering", b: "Overtraining: imbalance between load and recovery, causing performance to fall. Peaking: performer in best physical, emotional and mental condition for the most important competition. Tapering: reduction in training VOLUME (intensity maintained) before competition to be fresh for peak performance." }
          ],
          questions: [
            { type: "short", marks: 10, prompt: "Outline the principles of training using the acronym SPORRT.", model: "Specificity: training matches the demands of the activity (energy systems, muscles, components). Progressive overload: gradually increase frequency, intensity, time or type. Recovery: schedule rest for the body to repair and adapt. Reversibility: gains are lost if training stops or fails to progress. Tedium: vary sessions to maintain motivation and prevent boredom." },
            { type: "short", marks: 6, prompt: "Explain how the FITT formula is used to apply progressive overload in a training plan.", model: "The coach increases one variable at a time to keep stressing the body. Frequency raises the number of sessions per week; Intensity increases the difficulty (e.g. heavier weight or higher % MHR); Time lengthens session duration; Type introduces a new training method (e.g. switching from continuous to fartlek) to keep adaptations occurring." },
            { type: "short", marks: 8, prompt: "Compare continuous training and interval training, including one fitness component each develops best.", model: "Continuous training is steady-state exercise at low-to-moderate intensity for at least 20 minutes, primarily developing cardiorespiratory endurance through the aerobic system. Interval training alternates intense work with timed rest, building both aerobic and anaerobic capacity, lactate tolerance and speed. Continuous is suited to marathon runners; interval is suited to team-sport athletes who repeat sprints." },
            { type: "short", marks: 6, prompt: "Describe two recovery strategies and explain how each promotes adaptation.", model: "Active recovery (easy jog or gentle cycle) keeps blood flowing through muscles, removing waste products and reducing soreness. Sleep — particularly non-REM deep sleep — releases growth hormone and allows tissue repair; 7-8 hours per night maximises adaptation gained from training." },
            { type: "short", marks: 5, prompt: "Distinguish between a macrocycle, mesocycle and microcycle in periodisation.", model: "A macrocycle is the full long-term plan, usually a season or four-year Olympic cycle, divided into preparation, competition and transition phases. A mesocycle is a block of weeks focused on one adaptation (e.g. strength). A microcycle is the smallest unit, typically a week of training broken down session by session." }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 3 =================== */
    {
      id: "pe3",
      number: 3,
      subject: "pe",
      title: "Psychological Demands of Performance",
      learningOutcomes: [
        {
          id: "pe3-1",
          code: "3.1",
          title: "Confidence, anxiety, arousal, motivation and mental strategies",
          notes: [
            { h: "Psychological preparedness", b: "Forming the mental functions, processes and personality traits required to solve problems during training and competition." },
            { h: "Confidence and self-efficacy", b: "Self-confidence: belief in one's skills and ability. Self-efficacy: self-belief that enables better performance in a specific task. Trait confidence: confident in many situations. State confidence: confident only in specific situations. Extroverts tend to have high self-confidence." },
            { h: "Bandura's model of self-efficacy", b: "Self-efficacy is formed and changed through four information sources: enactive mastery (past success), vicarious experiences (seeing others succeed), verbal persuasion (encouragement) and physiological arousal (how the body feels). High self-efficacy pursues challenges and persists; low self-efficacy avoids challenges and gives up." },
            { h: "Anxiety", b: "Feeling of unease, worry or fear, ranging from mild to severe. Trait anxiety is part of personality across life areas. State anxiety is temporary, in specific situations. Cognitive anxiety: mental worries and expectations. Somatic anxiety: physical effects such as sweaty palms, raised HR and butterflies. SCAT (Sports Competition Anxiety Test, 1990) measures anxiety level." },
            { h: "Arousal and the Inverted-U", b: "Arousal is a state of physical and mental readiness on a continuum from low to high. Inverted-U theory: performance improves with arousal up to an optimal point, then worsens. Low arousal = boredom; medium arousal = the 'zone'; high arousal = over-arousal and panic. Extroverts need higher arousal; introverts perform better at lower arousal." },
            { h: "Motivation", b: "Level of enthusiasm or desire to train and compete. Intrinsic motivation comes from within (satisfaction, pride). Extrinsic motivation comes from outside: tangible rewards (medals, money — use sparingly with young athletes) and intangible rewards (praise, recognition — use regularly). Amotivation: lack of motivation; performer likely to quit." },
            { h: "Mental strategies — before performance", b: "Positive self-talk: encouragement (I can, I will) maintains self-confidence and regulates thoughts. Mental rehearsal: imagining successful performance. Visualisation/imagery: like mental rehearsal but uses all five senses to recreate or create a successful experience. Pre-performance ritual: routine to focus the mind and combat anxiety. Music: matching rhythm to movement and uplifting lyrics energise the performer." },
            { h: "Mental strategies — during performance", b: "Accept anxiety as part of sport; reduce it when overwhelming. Manage emotions: accept and use them. Concentration: focus on the moment, resist distractions, regain focus when lost. Breathing control: slow, deep diaphragmatic breaths reduce anxiety and control arousal." },
            { h: "Reframing and after performance", b: "Reframing: putting a new, growth-mindset frame on a setback to build confidence. WWW technique — 'What Will Work?' before and 'What Went Well?' after. After performance: breathing control, music, speak with coach/mentor, reframing and goal-setting." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Using Bandura's model, outline how a coach can build self-efficacy in a young athlete.", model: "The coach uses the four information sources. Enactive mastery: set achievable tasks so the athlete experiences success. Vicarious experiences: show video of similar athletes performing well. Verbal persuasion: give specific, sincere encouragement. Physiological arousal: teach breathing and warm-up routines so the athlete reads their body's signals as readiness rather than fear." },
            { type: "short", marks: 6, prompt: "Use the Inverted-U theory to explain how arousal affects performance.", model: "Performance improves as arousal rises from a low, bored state to an optimal mid-range 'zone', where focus and physical readiness are at their best. Beyond this peak, further arousal causes muscle tension, narrow attention and poor decision-making, so performance drops. Different personalities and skills require different optimal points — introverts and fine-skill performers usually need lower arousal." },
            { type: "short", marks: 6, prompt: "Distinguish between cognitive and somatic anxiety with a sporting example of each.", model: "Cognitive anxiety is mental — negative thoughts, worry and self-doubt — such as a footballer obsessing over missing a penalty before taking it. Somatic anxiety is physical — sweaty palms, raised heart rate, butterflies — such as a sprinter's hands shaking on the blocks. Cognitive anxiety responds to mental strategies like reframing; somatic anxiety responds to physical strategies like breathing control." },
            { type: "short", marks: 5, prompt: "Explain two strategies a performer can use before competition to enhance psychological preparation.", model: "Visualisation: the athlete uses all five senses to imagine a successful performance, building confidence and rehearsing the motor programme without physical fatigue. Pre-performance ritual: a consistent routine (kit, warm-up, music) quiets the mind, reduces anxiety and signals readiness to compete." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "pe3-eq-1",
          source: "LC Physical Education Past Paper — Q4",
          parts: [
            { label: "Q4. (a)", question: "Define the following types of goals related to physical activity: (i) Short term goal and (ii) Performance goal.", marks: 6, model: "Short term goal: A specific target set to be achieved in the near future (days or weeks), designed to provide motivation and measurable progress towards a longer-term aim. Example: I will improve my 100m sprint time by 0.3 seconds within the next two weeks. Performance goal: A goal focused on achieving a specific quality or level of performance based on the athlete's own previous standard, independent of comparison with others. It is entirely within the athlete's control. Example: I will successfully complete 80% of my set shots from the free-throw line during this week's training sessions." },
            { label: "Q4. (b)", question: "Write a short term performance goal.", marks: 4, model: "Example: By the end of this week's training, I will maintain a plank position for 60 seconds without breaking form. This is a short term performance goal because it is specific, time-bound, measurable, and entirely based on my own personal performance standard rather than comparing myself to others. (Use the SMART framework: Specific, Measurable, Achievable, Relevant, Time-bound.)" }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 4 =================== */
    {
      id: "pe4",
      number: 4,
      subject: "pe",
      title: "Diet and Nutrition",
      learningOutcomes: [
        {
          id: "pe4-1",
          code: "4.1",
          title: "Macronutrients, micronutrients, energy systems and supplements",
          notes: [
            { h: "Balanced diet", b: "Variety of foods providing adequate nutrients for good health. The food pyramid: bottom five levels eaten daily in varying amounts; top level limited. Ensures correct macronutrients, micronutrients, fibre and water." },
            { h: "Carbohydrates", b: "Main energy source. Stored as glycogen in muscles and liver, broken down to glucose during exercise. 1g = 4 calories; 50-60% of total daily calories. Daily intake: 5-7g/kg moderate, 7-10g/kg endurance, 10-12g/kg extreme. Complex (slow release: brown pasta, potatoes). Simple (quick release: juice, sweets)." },
            { h: "Glycogen / carb loading", b: "Used by endurance athletes. 1 week pre-competition: 2-3 days high-protein/fat with intense exercise to deplete glycogen, then 3 days high-carb plus tapering. Supercompensates glycogen stores up to 2x normal, delaying fatigue." },
            { h: "Protein", b: "Provides amino acids for muscle growth and repair, immune function and hormones. 1.7-2g/kg/day for performers. 1g = 4 calories." },
            { h: "Fats", b: "Most concentrated energy source; primary fuel for endurance; aids brain/cell function; insulates organs; absorbs fat-soluble vitamins. 1g = 9 calories. Saturated (limit): butter, fatty meat. Unsaturated (aim for): nuts, seeds, vegetable oils." },
            { h: "Fibre and micronutrients", b: "Fibre: indigestible, helps absorb vitamins, removes waste, creates fullness. Vitamins: fat-soluble (A, D, E, K) stored in fatty tissue; water-soluble (B, C) must be replenished daily. Minerals: calcium, potassium, iron." },
            { h: "Hydration and dehydration", b: "Water transports oxygen, nutrients and hormones; lost through sweat which also removes salts. 2% body-weight fluid loss reduces performance; 3%+ risks heat exhaustion. Athletes can sweat 6-10% body weight in competition." },
            { h: "Energy systems (ATP)", b: "All produce ATP for muscle contraction. ATP-PCr system: immediate, max intensity, 8-10 sec, recovers in 2-3 min (100m sprint, powerlifting). Anaerobic glycolysis: uses glycogen without oxygen, up to 1-2 min, produces lactic acid (800m, circuit training); lactate clears in ~8 min. Aerobic glycolysis: uses oxygen with fats and carbs, 2 min to hours, recovery hours-3 days (marathon, long-distance cycling). The energy continuum describes how all three contribute together." },
            { h: "Supplements and sports drinks", b: "WADA and Sport Ireland do not endorse supplements; performers must check the prohibited list. Sports drinks: water + electrolytes + 6-8% carbohydrates, no stimulants. Energy drinks: contain stimulants (caffeine, guarana). Key supplements: protein (muscle repair), creatine (extends ATP-PCr), caffeine (CNS stimulant, fat metabolism), nitrates (oxygen uptake)." },
            { h: "Metabolism and BMR", b: "Metabolism converts food into energy. BMR (Basal Metabolic Rate): calories required at rest. Affected by gender, weight, height, age, body composition, genetics. Males have a 10-15% higher BMR; BMR falls 2-3% per decade after age 18." },
            { h: "Nutrition planning", b: "Targets: =55% carbs, =30% fat, 15% protein. Before (fuel up): carb-rich; avoid high fat. During: usually no food if <2 hours. After (3 Rs): refuel glycogen, repair muscle, rehydrate." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline the three macronutrients and the role of each in an athlete's diet.", model: "Carbohydrates are the primary fuel for exercise, stored as glycogen and broken into glucose to power high-intensity work; they should provide 50-60% of calories. Proteins supply amino acids for muscle growth and repair, immune function and hormone production; athletes need 1.7-2g/kg/day. Fats are the most concentrated energy source (9 cal/g), fuel endurance work, insulate organs and carry fat-soluble vitamins; unsaturated sources should be prioritised." },
            { type: "short", marks: 8, prompt: "Describe the three energy systems and give a sporting example of each.", model: "ATP-PCr: produces ATP rapidly for 8-10 seconds of max effort (100m sprint, powerlifting); recovers in 2-3 minutes. Anaerobic glycolysis: breaks down glycogen without oxygen for 1-2 minutes of high intensity (800m, circuit training), producing lactic acid that causes fatigue. Aerobic system: uses oxygen with fats and carbs to make large amounts of ATP for endurance work lasting 2 minutes to several hours (marathon, road cycling)." },
            { type: "short", marks: 6, prompt: "Explain the process of carbohydrate loading and the benefit to an endurance athlete.", model: "About a week before competition the athlete spends 2-3 days on high-protein, high-fat, low-carb intake with intense training to deplete glycogen, then switches to 3 days of high-carb intake while tapering. The body supercompensates by storing up to twice the normal level of glycogen, which delays fatigue and helps the athlete maintain pace during long races such as a marathon." },
            { type: "short", marks: 5, prompt: "Discuss the risks of dehydration on sporting performance.", model: "A 2% fluid loss already reduces performance: muscles cannot use fat effectively, glycogen burns faster, and the brain shows reduced concentration, alertness and mood. At 3%+ the risk of heat exhaustion and heatstroke rises sharply. Since athletes can sweat 6-10% of body weight, planned pre-, during- and post-exercise hydration with electrolytes is essential." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "pe4-eq-1",
          source: "LC Physical Education Past Paper — Q5",
          parts: [
            { label: "Q5.", question: "Describe two categories of performance-enhancing drugs. You are not permitted to use anabolic steroids as one of your answers.", marks: 8, model: "1. Beta-blockers: Drugs that block adrenaline receptors, reducing heart rate, lowering anxiety and steadying fine motor control. Used in precision sports such as archery, shooting and golf to reduce tremors and improve accuracy. Example: propranolol. Health risks: low blood pressure, fatigue, depression, reduced exercise capacity. 2. Stimulants: Drugs that stimulate the central nervous system, increasing alertness, reducing perceived fatigue and elevating aggression or confidence. Used by athletes in endurance and power sports to mask tiredness. Examples: amphetamines, cocaine, ephedrine. Health risks: cardiovascular damage, addiction, aggression, hyperthermia. (Other valid categories: Diuretics — used to rapidly lose weight or mask other drugs; Erythropoietin (EPO) / blood doping — increases red blood cell count and oxygen delivery.)" }
          ]
        },
        {
          id: "pe4-eq-2",
          source: "LC Physical Education Past Paper — Q10",
          parts: [
            { label: "Q10. (a)", question: "Outline two benefits of sports drinks for performers.", marks: 6, model: "1. Rehydration: Sports drinks contain water and electrolytes (sodium, potassium, magnesium) that replace the fluids and salts lost through sweat during exercise. Maintaining fluid balance prevents dehydration, sustaining muscular function and cognitive performance. 2. Energy provision: Sports drinks contain carbohydrates (glucose, maltodextrin) that provide a rapid and sustained energy source during prolonged exercise. This maintains blood glucose levels, spares muscle glycogen and delays the onset of fatigue." },
            { label: "Q10. (b)", question: "Name a sports supplement used by athletes and justify why athletes might use this supplement.", marks: 6, model: "Supplement: Creatine (creatine monohydrate). Justification: Creatine is stored in muscle as phosphocreatine (PCr), which rapidly regenerates ATP during short, maximal-intensity efforts (e.g. sprinting, weightlifting, jumping). Supplementing with creatine increases the PCr stores in muscle, enabling athletes to perform more repetitions at high intensity before fatigue, potentially increasing muscle mass and strength over time through a greater training volume. It is most beneficial in repeated short-burst sports." }
          ]
        },
        {
          id: "pe4-eq-3",
          source: "LC Physical Education Past Paper — Q12",
          parts: [
            { label: "Q12. (a)", question: "Identify three ways in which Irish anti-doping rules are enforced.", marks: 6, model: "1. In-competition testing: Athletes selected (randomly or by targeting) must provide urine or blood samples immediately following competition. 2. Out-of-competition testing: Athletes may be tested at any time, without prior notice — at training venues, their home or anywhere — to catch athletes who time drug use to avoid detection during competition. 3. Whereabouts programme: Elite athletes must register their current location with Sport Ireland Anti-Doping on a quarterly basis so testers can locate them for unannounced out-of-competition tests (missing three tests in 12 months is treated as a doping violation)." },
            { label: "Q12. (b)", question: "Under what circumstance can an athlete compete with banned substances in their system?", marks: 4, model: "Under a Therapeutic Use Exemption (TUE). If an athlete has a legitimate diagnosed medical condition that requires treatment with a substance that appears on the prohibited list (e.g. asthma requiring corticosteroids, ADHD requiring stimulants, or testosterone deficiency requiring replacement therapy), they may apply to Sport Ireland Anti-Doping for a TUE before competition. If granted, the athlete may use the medication without committing a doping violation, provided it is used solely for therapeutic medical purposes at the prescribed dose." }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 5 =================== */
    {
      id: "pe5",
      number: 5,
      subject: "pe",
      title: "Skill, Ability and Skilled Performance",
      learningOutcomes: [
        {
          id: "pe5-1",
          code: "5.1",
          title: "Classification, learning, guidance, feedback and practice",
          notes: [
            { h: "Skill", b: "A sequence of movements performed effectively and efficiently to achieve a predetermined goal." },
            { h: "Characteristics of skilful movement (ACE FACE)", b: "Aesthetic (looks good), Coordinated, Efficient, Fluent, Accurate, Controlled/Consistent, Economical." },
            { h: "Qualities of a skilled performer (TACK)", b: "Technique: correct practical procedure. Anticipation: reading and predicting opponents' movements. Consistency: repeating quality movement under various conditions. Kinaesthetic sense (muscle memory): awareness of own movement during execution, enabling error correction." },
            { h: "Skill vs ability", b: "Skills are LEARNED through practice and produce permanent behaviour change. Abilities are INHERITED, INNATE and enduring traits that make tasks possible (coordination, flexibility, balance, power, endurance, speed)." },
            { h: "Domains of skill", b: "Psychomotor (the 'do' — physical movement, hand-eye, foot-eye). Cognitive (the 'think' — selecting skills, tactics, rules). Perceptual (the 'feel' — senses interpret the situation)." },
            { h: "Skill classification continua", b: "Gross-Fine (muscle size). Open-Closed (environmental influence — open is externally paced and unpredictable; closed is self-paced and fixed). Simple-Complex (cognitive demand). Externally paced-Self-paced (timing). Discrete-Serial-Continuous (defined start/end). Individual-Coactive-Interactive (athlete interaction)." },
            { h: "Information-processing model", b: "Four stages: 1. Perceiving (input via senses), 2. Decision-making (short-term memory ~30 sec and long-term memory store motor programmes), 3. Acting (output), 4. Evaluating (feedback adapts performance)." },
            { h: "Fitts and Posner stages of learning (1967)", b: "Cognitive: inconsistent, trial and error, relies on coach cues, 2-3/10 success. Associative: motor memories forming, internal feedback developing, 5-7/10 success. Autonomous: skill is automatic and motor programmes are in long-term memory, focus shifts to tactics, 9/10 success — must keep practising to retain. Learning plateau: performance levels off temporarily or at the limit of ability." },
            { h: "Types of guidance (VVMM)", b: "Visual: demonstrations, diagrams, videos (early stages, builds a model). Verbal: brief, focused explanation of key cues. Manual: physical support from coach (complex or dangerous skills). Mechanical: equipment assists or guides the movement." },
            { h: "Feedback", b: "Intrinsic: internal information from proprioception during execution. Extrinsic: from external sources (coach, video, results). Concurrent: during the action. Terminal: after the action. Knowledge of performance: feedback on the QUALITY of execution. Knowledge of results: feedback on the SUCCESS or final outcome." },
            { h: "Practice types and organisation", b: "Fixed (drill): repeated practice of one skill — suits closed skills. Variable: same skill in many contexts — suits open skills. Massed: no breaks; for fit, experienced performers. Distributed: rest breaks; for beginners or low fitness. Whole: skill in entirety (simple skills). Part: one element at a time (complex skills). Progressive-part: chain sub-routines together. Whole-part-whole: whole, isolate weakness, whole again. Effective practice (GAP VAT): Goal-orientated, Appropriate, Progressive, Varied, Adaptable, Time-bound." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Distinguish between skill and ability and give a sporting example of each.", model: "An ability is innate and enduring — for example, natural reaction speed that a sprinter is born with. A skill is learned and produces a permanent change in behaviour through practice — for example, the smooth start out of the blocks the sprinter develops over years of training. Abilities are the raw material; skills are the polished movement built on top." },
            { type: "short", marks: 8, prompt: "Outline Fitts and Posner's three stages of motor-skill learning.", model: "Cognitive stage: the learner is inconsistent, makes many errors and relies on external cues from the coach; success is low (2-3/10). Associative stage: motor memories form, simple parts become fluent and the performer begins self-correcting using kinaesthetic feedback; success rises to 5-7/10. Autonomous stage: the skill is automatic, attention can switch to tactics and opponents, and success is around 9/10 — but practice must continue to retain the level." },
            { type: "short", marks: 6, prompt: "Compare knowledge of performance and knowledge of results as types of feedback.", model: "Knowledge of performance focuses on the QUALITY of the technique — for example, a coach noting that a golfer's hip rotation was incomplete. Knowledge of results focuses on the OUTCOME — for example, the ball landing 10 metres short of the green. Knowledge of performance helps refine the skill, while knowledge of results confirms whether the action achieved its goal." },
            { type: "short", marks: 6, prompt: "Explain two methods of practice a coach could use to teach a complex skill.", model: "Part practice breaks a complex skill into its sub-routines so the performer can perfect one element at a time, e.g. practising only the toss in a tennis serve. Progressive-part practice then chains those sub-routines together — toss, then toss + swing, then full serve — building the skill up while keeping cognitive load manageable." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "pe5-eq-1",
          source: "LC Physical Education Past Paper — Q2",
          parts: [
            { label: "Q2.", question: "Outline four types of feedback that can be beneficial to athlete performance.", marks: 8, model: "1. Intrinsic (internal) feedback: Sensory information received from within the performer's own body during or after movement — proprioceptive sensations of balance, muscle tension and joint position. Example: a gymnast feeling whether their body alignment is correct during a handstand. 2. Extrinsic (augmented/external) feedback: Information received from an outside source — coach instruction, video analysis, score or performance data — that the athlete could not obtain unaided. 3. Knowledge of Results (KR): Feedback about the outcome or end result of a performance. Example: 'You scored 7 out of 10 free throws.' It motivates athletes and informs them whether they are achieving goals. 4. Knowledge of Performance (KP): Feedback about the movement pattern or technique used rather than the result. Example: 'Your release point was too early in the throw.' Helps the performer refine technique." }
          ]
        },
        {
          id: "pe5-eq-2",
          source: "LC Physical Education Past Paper — Q6",
          parts: [
            { label: "Q6. (a)", question: "Outline two principles of effective practice.", marks: 6, model: "1. Specificity of practice: Practice should closely replicate the conditions, movements and demands of actual performance so that the skill transfers effectively. A sprinter should practise start technique from blocks in race-like conditions, not just jog. 2. Variability of practice: Exposing the learner to slightly varied practice conditions (different speeds, distances, opponents) develops a more adaptable motor programme, improving the performer's ability to adapt the skill to changing game situations." },
            { label: "Q6. (b)", question: "How would you use one of the principles outlined in Q6(a) to develop skill in a practice session?", marks: 6, model: "Applying Specificity of practice — Example: Basketball free throw. Initially I have the athlete practise uncontested free throws to groove the basic technique. I then progressively make the practice more specific: simulate game fatigue by having the athlete complete a sprint before each throw, add the crowd noise and pressure of a decisive final-minute scenario, and introduce a real defender making noise nearby. Each stage more closely replicates the specific physical and psychological conditions of an actual game, ensuring the skill transfers from training to competition." }
          ]
        },
        {
          id: "pe5-eq-3",
          source: "LC Physical Education Past Paper — Q8",
          parts: [
            { label: "Q8. (a)", question: "As part of your studies in LC Physical Education you compared your personal performance to that of a more skilled/model performer. Describe how you conducted this analysis.", marks: 6, model: "I selected my physical activity (e.g. 100m sprint). I recorded a video of my own performance from a consistent camera angle and distance. I also sourced a video of a skilled/model performer (e.g. a national or international sprinter) performing the same skill from an equivalent angle. I created a structured observation checklist of key technical components: drive phase mechanics, arm action, knee lift, body lean and stride frequency. I watched both videos multiple times and compared each component against the checklist, identifying where my technique differed from the model. For example: my arm action crossed the midline of my body, whereas the model performer drove their arms straight forward and back, which is more efficient. I then prioritised these differences and set goals to address the most significant technical weaknesses." },
            { label: "Q8. (b)", question: "Outline two aesthetic/artistic criteria of performance in a named physical activity of your choice.", marks: 6, model: "Physical activity: Contemporary Dance. 1. Fluency and continuity: Movements flow seamlessly from one to the next without abrupt stops or jarring transitions. A skilled dancer connects each movement phrase smoothly, creating a continuous stream of motion that gives the impression of effortless control. 2. Expression and interpretation: The performer communicates emotion, narrative or the intent of the choreography through dynamic variation (contrast between powerful and gentle movements), facial expression and spatial awareness. A skilled dancer makes the audience feel the intended mood of the piece rather than simply executing correct technical positions." }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 6 =================== */
    {
      id: "pe6",
      number: 6,
      subject: "pe",
      title: "Biomechanics",
      learningOutcomes: [
        {
          id: "pe6-1",
          code: "6.1",
          title: "Planes, axes, levers, motion and economy of movement",
          notes: [
            { h: "Biomechanics", b: "The study of structure, function and movement of a living body. Used to increase performance (speed, power, technique, economy) and reduce injury risk (lessen joint impact, fix technique, address imbalances)." },
            { h: "Planes (3)", b: "Sagittal plane — divides body LEFT/RIGHT; movements are flexion/extension, forward/backward (running, squatting). Frontal plane — divides FRONT/BACK; movements are abduction/adduction. Transverse plane — horizontal, divides UPPER/LOWER; movements are rotation (360 twist)." },
            { h: "Axes (3)", b: "Sagittal axis: runs horizontally back-to-front. Vertical axis: runs vertically top-to-bottom. Frontal (transverse) axis: runs horizontally left-to-right." },
            { h: "Planes and axes paired", b: "Frontal plane rotates around the sagittal axis (FP/SA). Transverse plane rotates around the vertical axis (TP/VA). Sagittal plane rotates around the frontal axis (SP/FA)." },
            { h: "Levers", b: "A lever is a rigid body moving around a fulcrum. In the body: bones are the lever, joints are the fulcrum, muscles supply the effort, body parts or weights are the load." },
            { h: "Three classes of levers", b: "1st class — fulcrum in the middle (neck nodding). 2nd class — load in the middle (standing on tiptoe; gastrocnemius is the effort, body weight is the load, ball of foot is fulcrum). 3rd class — effort in the middle (biceps curl); most common in the human body." },
            { h: "Mechanical advantage/disadvantage", b: "Load arm: load to fulcrum. Effort arm: effort to fulcrum. Mechanical advantage: effort arm longer than load arm — lifts large loads with small effort. 2nd class always has mechanical advantage; 3rd class always has mechanical disadvantage." },
            { h: "Quantities and units", b: "Scalar = magnitude only (time, length, mass, speed, temperature). Vector = magnitude + direction (force, weight, velocity, acceleration, displacement). Force/weight in Newtons (N), acceleration m/s2, velocity m/s, displacement m, mass kg." },
            { h: "Distance vs displacement", b: "Distance is the scalar interval covered along the path. Displacement is the shortest straight-line vector from start to finish. A 400m runner finishing in the same lane has covered 400m distance but 0m displacement." },
            { h: "Speed, velocity, acceleration", b: "Speed = distance / time. Velocity = displacement / time (vector). Acceleration = rate of change of velocity (vector); deceleration is negative acceleration. Mass = amount of matter (kg); Weight = mass x gravity (N)." },
            { h: "Newton's laws", b: "1st (Inertia): a body stays at rest or in uniform motion unless acted on by an external force — a ball stays still until kicked. 2nd (Acceleration): F = MA; a tennis smash applies more force than a drop shot, producing greater acceleration. 3rd (Counterforce): every action has an equal and opposite reaction — a runner pushes into the ground, the ground pushes back." },
            { h: "Economy of movement", b: "Energy efficiency of the body. Internal factors (controlled by performer): technique, coordination, mobility, stability. External factors: gravity, friction (a weightlifter uses chalk to increase grip), wind, weather. Creative application of skill is performing a skill in a new, high-risk, high-reward way." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Outline the three planes of motion and give one example of movement in each.", model: "The sagittal plane divides the body into left and right and allows flexion/extension movements such as squatting or running. The frontal plane divides front from back and allows abduction/adduction such as a jumping jack. The transverse plane is horizontal, divides upper from lower and allows rotation such as a 360-degree twist in gymnastics." },
            { type: "short", marks: 8, prompt: "Describe the three classes of levers, giving a body example of each.", model: "First-class levers have the fulcrum in the middle (e.g. neck nodding — neck joint is fulcrum, head is load, neck muscles provide effort). Second-class levers have the load in the middle (standing on tiptoe — ball of foot is fulcrum, body weight is load, calf muscle provides effort); they always give mechanical advantage. Third-class levers have the effort in the middle (biceps curl — elbow is fulcrum, hand is load, biceps is effort); they are most common in the body and always have mechanical disadvantage." },
            { type: "short", marks: 6, prompt: "Explain Newton's three laws of motion using sporting examples.", model: "1st (Inertia): a hockey ball stays still until struck and continues until stopped by another force. 2nd (F = MA): the same hurler applies more force on a long puck than a short pass, producing greater acceleration of the sliotar. 3rd (Counterforce): a sprinter pushes back into the blocks and the blocks push the sprinter forward with equal force." },
            { type: "short", marks: 5, prompt: "Distinguish between a scalar and a vector quantity and provide two examples of each.", model: "Scalar quantities have magnitude only — examples include speed and mass. Vector quantities have magnitude AND direction — examples include velocity and displacement. The difference matters in biomechanics because a 400m runner has speed throughout the lap but ends with zero displacement." }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 7 =================== */
    {
      id: "pe7",
      number: 7,
      subject: "pe",
      title: "Structures and Strategies",
      learningOutcomes: [
        {
          id: "pe7-1",
          code: "7.1",
          title: "Compositional elements, team structures and strategies",
          notes: [
            { h: "Composition", b: "Arrangement of a series of movements or skills in a desired manner to achieve a performance goal." },
            { h: "Compositional elements (5)", b: "1. Shape — element of space: low (on ground), medium (standing), high (in air); symmetry vs asymmetry. 2. Space — path and pattern (straight, zigzag, circular, curved). 3. Timing — tempo (steady or varied) and rhythm. 4. Dynamics — variation in energy/effort (slow, sustained, powerful, explosive). 5. Relationships — connections with space, objects and people (lifts, passes, ribbons)." },
            { h: "Structures", b: "Set-up of an activity, competition format, or team formation. Examples: soccer 4-4-2, GAA backs/midfield/forwards, cycling stage races. A team is more than two people in an organised set-up where players take on positions, roles and responsibilities." },
            { h: "Strategies (tactics)", b: "Game plans pre-arranged and rehearsed to maximise the chance of success. Performers must adapt during performance through problem-solving and decision-making (who does what, use of space, on/off-ball action)." },
            { h: "Modifying structures and strategies (ACT)", b: "Anticipate (read the opponent), Correct (adjust the plan), Timing (act at the right moment). Used to exploit opponent weaknesses or recover from setbacks." },
            { h: "Demands of performance / qualities of a performer", b: "Physical qualities: health- and performance-related components. Personal qualities: personality and character. Technical qualities: execution of skill." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline the five compositional elements and apply each to a chosen sport or dance performance.", model: "Shape: the body or team adopts different levels and symmetry — e.g. a gymnast holding a high asymmetric balance. Space: paths through the area — e.g. a basketball point guard cutting on a curved drive. Timing: tempo and rhythm — e.g. a dancer matching steps to musical beat. Dynamics: explosive vs sustained effort — e.g. a hurler changing pace before a side-step. Relationships: connections with people/objects — e.g. a rugby lift in a line-out." },
            { type: "short", marks: 6, prompt: "Explain how a coach can modify team structures and strategies during a game using the ACT model.", model: "Anticipate: read patterns in the opponent's play (e.g. they target the left wing). Correct: adjust the structure to counter — drop a midfielder into that channel. Timing: pick the right moment to make the change, e.g. at the start of the second half before the opponent commits to its plan, so the team gains an advantage without giving the opponent time to react." },
            { type: "short", marks: 5, prompt: "Distinguish between a structure and a strategy in team performance.", model: "A structure is the physical set-up — formation, positions and roles (e.g. a soccer 4-4-2). A strategy is the plan of action within that structure — the tactics for using space, on- and off-ball movement, and exploiting the opposition. The structure is the framework; the strategy is how the team plays inside it." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "pe7-eq-1",
          source: "LC Physical Education Past Paper — Q11",
          parts: [
            { label: "Q11.", question: "Explain two structures OR two strategies that can help an athlete or team succeed. Support your answer with physical activity examples.", marks: 8, model: "STRUCTURES: 1. Periodisation: The systematic division of the training year into phases (macrocycles, mesocycles, microcycles) so the athlete peaks physically at the right time, avoids overtraining and systematically develops fitness, technique and tactical skills. Example: A 1500m runner builds an aerobic base in the off-season (general preparation), transitions to speed work in pre-competition, then tapers in the final two weeks before the national championships to ensure peak form on race day. 2. Support staff structure: A clearly defined coaching team — head coach, assistant coaches, sports scientist, physiotherapist, nutritionist — ensures every aspect of an athlete's preparation is covered by a specialist, reducing gaps and maximising performance. Example: An elite rugby team with a dedicated lineout and set-piece specialist coach enables the team to gain a significant tactical advantage at restarts. STRATEGIES: 1. High press (soccer): A collective tactical strategy in which all outfield players immediately press the ball-carrier high up the pitch after losing possession, reducing the opposition's time and space and forcing errors or long balls. Example: Liverpool FC's gegenpressing under Klopp. 2. Zone defence (basketball): Players each guard a designated area rather than a specific opponent, protecting the key, reducing the opposition's ability to drive to the basket, and forcing difficult perimeter shots." }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 8 =================== */
    {
      id: "pe8",
      number: 8,
      subject: "pe",
      title: "Safe Practice in Sport and PA",
      learningOutcomes: [
        {
          id: "pe8-1",
          code: "8.1",
          title: "Safety, injuries, first aid, overtraining and load management",
          notes: [
            { h: "Safe practice", b: "Procedures to ensure safety of all stakeholders: safe facilities, fit equipment, correct attire, warm-up/cool-down and first-aid knowledge." },
            { h: "Clothing and protective equipment", b: "Compression clothing aids muscle recovery; base layers regulate temperature; supports and braces protect joints. Protective equipment (helmets, mouth guards, padding) must be maintained in good condition." },
            { h: "Injury prevention", b: "Warm-up increases body temperature, blood flow, flexibility and range of motion. Cool-down removes lactic acid, prevents DOMS and blood pooling, and returns HR gradually to rest." },
            { h: "Risk factors", b: "Intrinsic: personal to the performer (previous injury, age, fitness). Extrinsic: external (surface, weather, equipment)." },
            { h: "Common injuries", b: "Ankle sprain, pulled groin, hamstring strain, shin splints, ACL tear, patellofemoral knee syndrome, tennis elbow (epicondylitis), head injury." },
            { h: "Types of injuries", b: "Acute injuries (specific impact): hard tissue acute = dislocations, fractures; soft tissue acute = tears, strains, sprains. Chronic injuries (overuse): hard tissue chronic = stress fractures; soft tissue chronic = shin splints, tendinosis. Sprain grades: 1 = overstretched ligament, 2 = partial tear, 3 = full tear with popping sound." },
            { h: "Concussion", b: "Acute injury from head trauma. Symptoms: headache, dizziness, balance issues, nausea, possible loss of consciousness. Managed with the 6 Rs: Recognise, Remove, Refer, Rest, Recover, Return." },
            { h: "First aid — SALTAPS", b: "Stop the play, Ask about the injury, Look (bleeding, swelling), Touch with consent (pain/sensation), Active movement (can athlete move it?), Passive movement (full range?), Strength test (walk/run/jump?)." },
            { h: "PRICE protocol", b: "Treats sprains, strains and closed fractures. Protection (stop activity), Rest (2-3 days), Ice (15-20 min several times a day), Compression (bandage to limit swelling), Elevation (above heart level)." },
            { h: "Overtraining, fatigue and supercompensation", b: "Overtraining is an imbalance between training load and recovery and causes performance to fall. Overreaching is a temporary, recoverable version. Fatigue is lack of energy. Supercompensation: after training and adequate recovery, the body adapts BEYOND pre-training levels — repeated cycles produce steady improvement." },
            { h: "Monitoring load", b: "Borg RPE: subjective rating of how hard exercise feels (1-10). Daily wellness parameters: sleep, mood, soreness, motivation, nutrition. Training load = duration x intensity (training units = RPE x session time). External exertion is measurable (kg lifted); internal exertion is perceived. Performance management: set goals, monitor load, evaluate and re-evaluate." },
            { h: "BREAKS checklist", b: "Body, Rules, Equipment, Ability, Kit, Surface — used before participation to ensure safe practice." }
          ],
          questions: [
            { type: "short", marks: 6, prompt: "Outline the steps of the SALTAPS protocol for assessing injury.", model: "Stop the play to prevent further damage. Ask the athlete where it hurts and what happened. Look at the area for swelling, bleeding or bruising. Touch the site (with consent) to check for pain and sensation. Active movement — ask the athlete to move it themselves. Passive movement — gently test the full range of motion. Strength — see if the athlete can walk, run or jump on it before deciding whether they can return." },
            { type: "short", marks: 5, prompt: "Describe how the PRICE protocol is used to treat a Grade 1 ankle sprain.", model: "Protection: stop the activity immediately. Rest the ankle for 2-3 days before reintroducing movement. Ice the area for 15-20 minutes several times a day to reduce swelling. Compression with a bandage limits further swelling and supports the joint. Elevation of the ankle above heart level draws fluid away from the injury and reduces inflammation." },
            { type: "short", marks: 6, prompt: "Distinguish between acute and chronic injuries with one example of each.", model: "Acute injuries are caused by a specific impact or traumatic event — for example, an ankle sprain when landing awkwardly from a jump. Chronic injuries develop slowly from overuse and insufficient recovery — for example, shin splints in a runner who has increased mileage too quickly. Acute injuries need immediate first aid; chronic injuries need load management and addressing underlying causes." },
            { type: "short", marks: 5, prompt: "Explain supercompensation and how it leads to fitness improvements.", model: "After a training session the body is temporarily fatigued and performance dips, but during recovery it adapts and rebuilds BEYOND the previous baseline — this is supercompensation. If the next training stimulus is timed during this raised state and rest is adequate, fitness climbs in a stepwise pattern. Insufficient recovery results in overtraining instead of compensation." }
          ]
        }
      ]
    },

    /* =================== LC PE CHAPTER 9 =================== */
    {
      id: "pe9",
      number: 9,
      subject: "pe",
      title: "Rules, Rituals, Coach and Officials",
      learningOutcomes: [
        {
          id: "pe9-1",
          code: "9.1",
          title: "Roles of the coach and the official, communication and reflection",
          notes: [
            { h: "Rules, roles, rituals", b: "Rules: agreed-upon principles governing a sport — for safety, sportsmanship and fair competition. Roles: playing (defender, captain) and non-playing (referee, coach). Rituals: behaviours believed to have a specific purpose or power (e.g. the Haka). Superstition: belief in supernatural good/bad luck attached to actions. Pre-performance rituals are task-relevant routines that prepare mind and body. Conventions (etiquette): unwritten rules such as the coin flip in soccer or glove touch in boxing." },
            { h: "Role of the coach", b: "Ensures each athlete or team reaches full potential. Duties: skill and strategy practice, line-ups, leadership, communication and support, working with the manager, considering both physical and psychological elements." },
            { h: "Effective coach roles", b: "Facilitator of learning, problem-solver, time manager, innovator, aware of health and safety, good role model, motivator and inspiration." },
            { h: "Coaching qualities", b: "Emotional intelligence: understanding and managing one's emotions positively to relieve stress, empathise and defuse conflict. Interpersonal skills: communicating with others. Intrapersonal skills: managing one's own emotions, self-awareness, self-control." },
            { h: "Motivational strategies (coach)", b: "Communicate effectively and openly. Create a positive training environment and healthy competition. Use praise appropriately. Avoid punishment to eliminate mistakes. Use SMARTER goal-setting (Specific, Measurable, Achievable, Realistic, Time-bound, Evaluated, Reviewed). Share a vision for success." },
            { h: "Communication", b: "Non-verbal: gestures, facial expressions, tone, eye contact, body language, posture. Verbal: positive feedback and constructive criticism. A coach must be aware of their own non-verbal cues and read the performer's." },
            { h: "Performance analysis and reflection", b: "Notational analysis: factual recording of events (tactics, technique, work rate). Video analysis: immediate feedback, highlights strengths/weaknesses. Sports analytics: statistical principles for competitive advantage. Reflection — concurrent ('in' action, during) and terminal ('on' action, after); self-, peer- or coach-reflection. Sport Ireland Coaching Development Programme: 50+ NGBs, 25,000 coaches per year, 130 awards." },
            { h: "Role of the official", b: "Ensure competition is safe and fair, implement rules, protect player safety, guided by codes of conduct. Roles: athlete, rule enforcer, decision-maker, timekeeper, conflict manager, record-keeper. Characteristics: knowledge of rules, fitness, calmness, moral courage, safety awareness." },
            { h: "Scoring and recording", b: "Officials record goals, fouls and cards. In aesthetic sports (gymnastics, dance) judges rate performance against criteria; in outcome sports the result decides the winner." },
            { h: "Psychological readiness (3 Cs)", b: "Concentration: task-oriented focus on rules and events. Coping: handle the conditions using techniques. Confidence: belief in own knowledge and decisions." },
            { h: "Mental tools (4 Ms)", b: "Moves: pre-performance routine to get into the zone. Maps: reflect on performance, set goals, use self-talk. Mood: control and monitor mood (relaxation, deep breathing). Movies: mental imagery of performing the role." },
            { h: "Managing conflict (official)", b: "Recognise causes early, be respectful, stay calm, step back if needed, avoid raising the voice, keep hand movements slow and open, be assertive not aggressive, ask for help from other officials, communicate with the captain, breathe deeply, self-talk ('Relax'), be proactive not reactive." }
          ],
          questions: [
            { type: "short", marks: 8, prompt: "Outline four qualities of an effective coach and the impact each has on a team.", model: "Effective communication keeps players informed of expectations and tactics, reducing confusion and conflict. Emotional intelligence allows the coach to read mood, empathise and defuse tension, building trust. Knowledge of the sport and of training methods means sessions are well planned and progressive. Being a good role model — punctual, fair, calm — sets the standard players model themselves on." },
            { type: "short", marks: 6, prompt: "Describe two motivational strategies a coach can use, including one practical example of each.", model: "SMARTER goal-setting: agree a Specific, Measurable, Achievable, Realistic, Time-bound goal that is Evaluated and Reviewed — e.g. 'improve free-throw success from 60% to 75% by April'. Creating a positive training environment: praise effort, allow mistakes and use healthy internal competition — e.g. small-sided games with rotating teams so players are challenged but not embarrassed." },
            { type: "short", marks: 6, prompt: "Explain how an official can manage on-pitch conflict.", model: "The official recognises early warning signs, remains calm and respectful, and communicates assertively with the captain rather than confronting every player. Body language is open, hand movements slow, and the official may take a step back, breathe deeply and use self-talk to control mood. If needed they consult fellow officials and apply cards in line with the rules, staying proactive rather than reactive." },
            { type: "short", marks: 5, prompt: "Distinguish between concurrent reflection and terminal reflection.", model: "Concurrent reflection happens DURING the event ('reflection in action') — for example, a midfielder noticing the press is too high and dropping deeper. Terminal reflection happens AFTER the event ('reflection on action') — for example, reviewing match video the next day to identify what worked. Both feed into future performance, but concurrent reflection adjusts in the moment while terminal reflection adjusts the plan." }
          ]
        }
      ]
    },

    /* =================== LC PE CASE STUDY =================== */
    {
      id: "pe-casestudy",
      number: 13,
      subject: "pe",
      isCaseStudy: true,
      title: "Case Study",
      learningOutcomes: [
        {
          id: "pe-cs-1",
          code: "CS.1",
          title: "Case study practice",
          notes: [
            { h: "What is the Case Study?", b: "Question 13 in the LC PE exam is a 50-mark Case Study. A text (with images, tables and figures) is provided in the exam paper and all sub-questions refer to that text. Sub-questions draw on multiple chapters — biomechanics, skill learning, fitness, nutrition, ethics." },
            { h: "How to Prepare", b: "Practise applying concepts from multiple chapters to unseen scenarios. Read the case study carefully before answering, underlining key facts. Structure answers using specific PE terminology and physical activity examples." }
          ],
          questions: [
            { type: "short", marks: 5, prompt: "List the key concepts likely to appear in a PE Case Study question.", model: "Concepts of physical activity (play, sport, physical education), FMS (locomotor, body control, manipulative), fitness components, skill learning and practice methods, biomechanical principles (levers, planes of movement), nutrition/supplementation, ethical practice in sport." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "pe-cs-eq-1",
          source: "LC Physical Education Past Paper — Q13 (Case Study: Throwing — 50 marks)",
          caseStudy: true,
          context: "Throwing\n\nThrowing can be a fun, open-ended activity that provides opportunities for children to explore, experiment and learn through play.\n\nFundamental movement skills (FMS) are believed to be the building blocks from which many other sporting movements are developed. FMS are grouped into three different categories: locomotor or movement skills such as running and jumping; body control or stability skills such as catching and throwing; or manipulative skills such as catching and throwing. When you examine Figure 6 you can understand how FMS like throwing can be viewed as the building block for skills in different sports.\n\nAthlete note (Figure 6): Volleyball — Spike; Badminton — Smash; Netball — Overhead pass; Baseball — Pitch; Javelin — Release; Tennis — Serve.\n\nThe javelin can be described simply as: a straight run of approximately 10-15 steps, during which the athlete continues running but the body turns to position to throw the javelin. The athlete must then ensure they stay within the throwing zone after releasing the javelin.\n\nFigure 9 shows a training plan for a javelin thrower during their competitive phase. The plan includes: Technique/throwing specifics, Full throw, Strength, Speed, Competition, Rest — distributed across M/T/W/T/F/S.\n\nInterestingly, many throwing coaches now advocate for throwing both light and heavy implements in training. It is believed that these training approaches can help develop different components of fitness relevant to the javelin.\n\nUnfortunately, some javelin throwers looking to gain an edge over competitors turn to unethical practices. DP Manu tested positive for the anabolic steroid methyltestosterone in 2024 and missed the Olympic Games as a result.",
          parts: [
            { label: "13. (a) (i)", question: "Identify and define two concepts of physical activity named in the case study.", marks: 8, model: "Concept 1: Play — a free, intrinsically motivated, open-ended and enjoyable physical activity undertaken for its own sake, without defined rules or outcomes. The case study states throwing can be a fun, open-ended activity for children to explore and learn through play. Concept 2: Sport — a structured, rule-governed physical activity involving competition, with defined objectives and outcomes. The case study identifies javelin as part of Athletics Ireland's track and field programme, with athletes competing according to rules (throwing zone, step count)." },
            { label: "13. (a) (ii)", question: "Discuss the personal and social benefits, mentioned in the case study, for children engaging in throwing activities.", marks: 8, model: "Personal benefits: 1. Development of Fundamental Movement Skills — throwing develops body control/stability and manipulative FMS, which are the building blocks for more complex sporting skills later in life. 2. Physical development and coordination — practising throwing improves hand-eye coordination, upper-body strength and kinaesthetic awareness. Social benefits: 1. Transferable participation — by developing throwing as an FMS, children gain the competence to participate in multiple sports (volleyball, badminton, netball, baseball, javelin, tennis as shown in Figure 6), expanding their opportunities for social inclusion through sport. 2. Shared enjoyment — the open-ended, playful nature of throwing creates an inclusive, low-pressure social environment in which children can experiment, collaborate and experience enjoyment together." },
            { label: "13. (b)", question: "Name a skill that uses a 3rd class lever from a named physical activity of your choice. Justify why this skill is an example of a 3rd class lever.", marks: 10, model: "Physical activity: Athletics (Javelin). Skill: The javelin throwing action. A 3rd class lever has the effort (muscular force) applied between the fulcrum (joint/pivot) and the load (resistance/implement). In the javelin throw: the shoulder joint acts as the fulcrum; muscle force (deltoid, triceps, rotator cuff) is applied to the upper arm close to the shoulder, between the shoulder joint and the javelin held in the hand (the load). Because the effort arm is shorter than the load arm, this arrangement sacrifices force advantage in exchange for a large range of motion and high velocity at the end of the lever (hand). This generates the high release speed required to throw the javelin as far as possible. (Alternatively: bicep curl — elbow joint = fulcrum; bicep muscle force = effort applied between elbow and hand; load = weight held in hand.)" },
            { label: "13. (c) (i)", question: "Based on the description of javelin in the case study, name a skill practice method appropriate for developing the skill of a javelin thrower.", marks: 4, model: "Part practice (also called progressive part practice or segmentation). The javelin throw is a complex, multi-phase closed skill (run-up, cross-step, body rotation, release, follow-through/recovery within the throwing zone). Breaking it into component parts allows the learner to master each sub-routine before recombining them." },
            { label: "13. (c) (ii)", question: "Explain how you would apply the practice method you named in 13(c)(i) to improve the skill of a javelin thrower.", marks: 8, model: "Applying Part practice to the javelin throw: Phase 1 — Grip and release: practise the correct grip and wrist-flick release action from a standing position, focusing on a clean, controlled release point. Phase 2 — Throwing action: add the shoulder rotation and arm drive from a standing position only, without the run-up. Phase 3 — Cross-step: practise the penultimate cross-steps (the body rotation phase) without throwing, developing rhythm and balance. Phase 4 — Combine cross-step + throw: integrate the rotation with the release. Phase 5 — Run-up: add the straight run-up and practise the full approach. Phase 6 — Full skill (Whole): combine all phases continuously at full speed, including a controlled recovery within the throwing zone. The coach provides KP feedback after each phase to correct errors in technique before moving to the next." },
            { label: "13. (c) (iii)", question: "Hammer throwers mainly move in which plane of movement?", marks: 4, model: "The transverse (horizontal) plane. The hammer thrower rotates their entire body horizontally around a vertical axis during the spinning turns. All rotational movement — the turning of the trunk, hips and arms — occurs in the transverse plane." },
            { label: "13. (d) (i)", question: "Use Figure 9 (the training plan) to suggest which component of fitness might be developed by throwing light implements. Justify your answer.", marks: 6, model: "Component of fitness: Speed (or speed-strength/power — speed component). Justification: Throwing a lighter implement allows the athlete to accelerate and release the implement at a much higher velocity than they can with a standard or heavy implement. By repeatedly practising this high-velocity movement, the athlete overloads the speed dimension of the power equation (Power = Force x Velocity), training the neuromuscular system to fire muscle fibres at a faster rate and improving the speed of the throwing action. This transfers to a faster release speed when throwing the standard implement." },
            { label: "13. (d) (ii)", question: "Use Figure 9 (the training plan) to suggest which component of fitness might be developed by throwing heavy implements. Justify your answer.", marks: 6, model: "Component of fitness: Muscular Strength (or power — strength component). Justification: A heavier implement requires the athlete to generate significantly greater muscular force to accelerate it through the throwing motion. This overloads the strength component of the movement. Over time, repeatedly applying maximal or near-maximal force against a heavier load stimulates the muscles, tendons and neural pathways to adapt, increasing muscle cross-sectional area (hypertrophy) and improving motor unit recruitment. This strength gain transfers to greater force production when throwing the standard implement." },
            { label: "13. (e) (i)", question: "Suggest two effects that anabolic steroids can have on athlete performance.", marks: 8, model: "1. Increased muscle mass and strength: Anabolic steroids (synthetic testosterone) accelerate protein synthesis in muscle cells and increase nitrogen retention, leading to greater muscle hypertrophy. The athlete gains more lean muscle mass and can produce greater force, improving performance in power and strength events such as javelin throwing. 2. Faster recovery: Anabolic steroids reduce muscle protein breakdown and inflammatory responses after intense training sessions. This allows athletes to train more frequently and at higher intensity without accumulating fatigue, enabling greater training volumes and faster adaptation. (Additional valid effects: increased aggression/assertiveness which may improve competitive drive; increased red blood cell production in some cases.)" },
            { label: "13. (e) (ii)", question: "Explain how DP Manu did NOT adhere to the principles of ethical practice when he took methyltestosterone. You must refer to at least two principles of ethical practice.", marks: 8, model: "1. Fair Play: By taking methyltestosterone (an anabolic steroid banned by the World Anti-Doping Code), DP Manu artificially enhanced his throwing performance beyond what was achievable through natural talent, training and dedication. This violated the principle of fair play, which requires all athletes to compete on an equal basis using only legally permitted means. Other competitors who trained drug-free were at an unfair disadvantage. 2. Integrity/Honesty: By using a prohibited substance while competing, Manu misrepresented his true, naturally achievable capabilities to his fellow competitors, officials and the public. He deliberately circumvented the rules of his sport, showing a disregard for the honesty and transparency that are fundamental to ethical competition. His actions undermined trust in athletics and resulted in his disqualification from the 2024 Olympic Games." }
          ]
        }
      ]
    },

        /* =================== LC PE ACRONYMS =================== */
    {
      id: "pe-acronyms",
      number: 10,
      subject: "pe",
      title: "Acronyms and Mnemonics",
      learningOutcomes: [
        {
          id: "pe-acronyms-1",
          code: "A.1",
          title: "Acronyms and mnemonics to learn",
          notes: [
            { h: "SPORRT", b: "Principles of training: Specificity, Progressive overload, Recovery, Reversibility, Tedium." },
            { h: "FITT", b: "Progressive overload formula: Frequency, Intensity, Time, Type." },
            { h: "Cows Make Milk For Bones", b: "Five health-related components of fitness: Cardiorespiratory endurance, Muscular endurance, Muscular strength, Flexibility, Body composition." },
            { h: "All Big Cats Pounce Really Softly", b: "Six performance-related components: Agility, Balance, Coordination, Power, Reaction time, Speed." },
            { h: "ACE FACE", b: "Characteristics of skilful movement: Aesthetic, Coordinated, Efficient, Fluent, Accurate, Controlled, Economical." },
            { h: "TACK", b: "Qualities of a skilled performance: Technique, Anticipation, Consistency, Kinaesthetic sense." },
            { h: "VVMM", b: "Types of guidance: Visual, Verbal, Manual, Mechanical." },
            { h: "GAP VAT", b: "Effective practice design: Goal-orientated, Appropriate, Progressive, Varied, Adaptable, Time-bound." },
            { h: "SCAT", b: "Sports Competition Anxiety Test (1990) — measures level of anxiety with a points system." },
            { h: "WWW", b: "Reframing technique: What Will Work? (before performance) and What Went Well? (after performance)." },
            { h: "SMARTER", b: "Goal-setting framework: Specific, Measurable, Achievable, Realistic, Time-bound, Evaluated, Reviewed." },
            { h: "ACT", b: "Modifying structures and strategies: Anticipate, Correct, Timing." },
            { h: "SALTAPS", b: "Injury assessment: Stop, Ask, Look, Touch, Active movement, Passive movement, Strength test." },
            { h: "PRICE", b: "Injury treatment: Protection, Rest, Ice, Compression, Elevation." },
            { h: "BREAKS", b: "Safe practice checklist: Body, Rules, Equipment, Ability, Kit, Surface." },
            { h: "6 Rs", b: "Concussion management: Recognise, Remove, Refer, Rest, Recover, Return." },
            { h: "RPE", b: "Rating of Perceived Exertion (Borg scale) — measures intensity by how hard the performer feels they are working." },
            { h: "3 Cs", b: "Psychological readiness of officials: Concentration, Coping, Confidence." },
            { h: "4 Ms", b: "Mental tools for officials: Moves, Maps, Mood, Movies." },
            { h: "F = MA", b: "Newton's 2nd Law: Force = Mass x Acceleration." },
            { h: "Plane-Axis pairs", b: "FP/SA: Frontal plane rotates around sagittal axis. TP/VA: Transverse plane rotates around vertical axis. SP/FA: Sagittal plane rotates around frontal axis." },
            { h: "Energy and testing acronyms", b: "ATP: Adenosine Triphosphate. ATP-PCr: Adenosine Triphosphate-Phosphocreatine system. BMI: Body Mass Index. BMR: Basal Metabolic Rate. VO2 max: maximum oxygen consumption. DOMS: Delayed Onset Muscle Soreness. LME: Local Muscular Endurance. PNF: Proprioceptive Neuromuscular Facilitation. HIIT: High Intensity Interval Training. MHR: Maximum Heart Rate. 1RM/3RM: One/Three Repetition Maximum. DEXA: Dual-Energy X-ray Absorptiometry." },
            { h: "Governance and bodies", b: "WHO: World Health Organization. WADA: World Anti-Doping Agency. NGB: National Governing Body. GAA: Gaelic Athletic Association. FAI: Football Association of Ireland. FIFA: Federation Internationale de Football Association. RSA: Road Safety Authority." },
            { h: "Periodisation cycles", b: "Macrocycle: full long-term plan (year+). Mesocycle: weeks emphasising one type of adaptation. Microcycle: small number of sessions, often a week or day plan." }
          ],
          questions: [
            { type: "short", marks: 5, prompt: "State what each letter of SPORRT stands for and give a one-line meaning for each.", model: "Specificity — training matches the activity. Progressive overload — gradually increase the demand. Recovery — schedule rest to allow adaptation. Reversibility — gains fade without progression. Tedium — vary training to keep performers motivated." },
            { type: "short", marks: 6, prompt: "Explain the SALTAPS and PRICE acronyms and when each is used.", model: "SALTAPS (Stop, Ask, Look, Touch, Active, Passive, Strength) is used pitch-side immediately after an injury to ASSESS severity and decide if the athlete can continue. PRICE (Protection, Rest, Ice, Compression, Elevation) is then used to TREAT soft-tissue injuries like sprains and strains in the hours and days afterwards." },
            { type: "short", marks: 6, prompt: "List the four parts of the FITT formula and apply each to a 4-week running plan.", model: "Frequency: progress from 3 runs/week to 4. Intensity: lift average pace from 70% MHR to 80% MHR for a portion of the run. Time: increase long-run duration from 30 to 45 minutes. Type: introduce one fartlek session per week alongside continuous running to vary the stimulus and avoid plateau." },
            { type: "short", marks: 5, prompt: "State the SMARTER goal-setting acronym and write one SMARTER goal for a club hurler.", model: "Specific, Measurable, Achievable, Realistic, Time-bound, Evaluated, Reviewed. Example goal: 'Raise free-taking success rate from 65% to 80% over the next 8 weeks by completing 50 frees per training session, reviewed weekly with the coach using video.'" }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 1 =================== */
    {
      id: "bio1",
      number: 1,
      subject: "biology",
      title: "Scientific Knowledge",
      learningOutcomes: [
        {
          id: "bio1-1",
          code: "1.1",
          title: "Scientific knowledge, method and publishing",
          notes: [
            { h: "Science", b: "A systematic way of building knowledge about the natural world through observation, testing and reasoning, producing explanations supported by repeatable evidence." },
            { h: "Scientific Method", b: "Steps: Observation -> Question -> Hypothesis -> Prediction -> Experiment -> Data collection -> Analysis -> Conclusion -> Publish/repeat." },
            { h: "Hypothesis", b: "A testable, provisional explanation for an observation (e.g. 'plants grow taller with more sunlight'). Early stage and can be rejected." },
            { h: "Theory", b: "A well-supported explanation built from many tested hypotheses (e.g. cell theory, evolution). Stronger than a hypothesis." },
            { h: "Principle/Law", b: "A concise statement of a consistently observed relationship in nature, often expressed mathematically (e.g. law of conservation of mass)." },
            { h: "Primary vs Secondary Data", b: "Primary data: collected first-hand by the experimenter. Secondary data: obtained from existing sources such as papers or databases." },
            { h: "Peer Review", b: "Independent scientists in the same field check the work for flaws before publication. Prevents fraud, errors and duplication." },
            { h: "Reproducibility", b: "Other scientists must be able to repeat the experiment and get similar results, confirming reliability." },
            { h: "Bias", b: "A preference or assumption that distorts results. Sources: poor sampling, funding interests, researcher expectations. Reduced by blind/double-blind methods, large samples and peer review." },
            { h: "Limits of Science", b: "Cannot address morality, beauty or faith. Always provisional — new evidence can revise conclusions. Limited by technology, ethics and complexity of natural systems." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "List the steps of the scientific method in order.", model: "Observation, Question, Hypothesis, Prediction, Experiment, Data collection, Analysis, Conclusion, Publish/repeat." },
            { type: "short", marks: 4, prompt: "Distinguish between a hypothesis and a theory.", model: "A hypothesis is a provisional, testable explanation based on limited evidence. A theory is a well-supported explanation built from many tested hypotheses over time; it is much stronger evidence but still subject to revision." },
            { type: "short", marks: 4, prompt: "Explain what peer review is and why it is important.", model: "Peer review is the process where independent experts in the same field scrutinise a study before publication. It catches errors and fraud, ensures methods are sound and allows findings to be trusted and built upon by the wider scientific community." },
            { type: "short", marks: 4, prompt: "What is bias in science and give two ways it can be reduced?", model: "Bias is a preference or assumption that distorts results (e.g. funding source influencing conclusions). It can be reduced by using blind or double-blind trials so researchers don't know which group is which, and by using large random samples to avoid skewed data." },
            { type: "short", marks: 3, prompt: "Give two limitations of the scientific method.", model: "Science cannot address questions of morality or faith. All conclusions are provisional and can be overturned by new evidence. It is also limited by available technology and ethical constraints on experimentation." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio1-eq-1",
          source: "LC Biology Past Paper — Q7",
          parts: [
            { label: "7. (a)", question: "In the scientific method, a testable statement is known as a ___. Write the missing word.", marks: 3, model: "Hypothesis — a testable, provisional explanation for an observation that can be supported or rejected by experiment." },
            { label: "7. (b)", question: "How can this statement be tested?", marks: 3, model: "By designing a controlled experiment in which all variables are kept constant except the independent variable being investigated; the outcome (dependent variable) is measured and compared to a control." },
            { label: "7. (c)", question: "What is the function of a scientific control?", marks: 3, model: "A control is an identical experimental setup in which the variable being tested is absent (or at a standard value). It provides a baseline for comparison, ensuring any observed change is caused by the variable under investigation and not by other factors." },
            { label: "7. (d)", question: "Give two limitations of the scientific method.", marks: 4, model: "1. Science cannot address moral, ethical or faith-based questions — these lie outside its scope. 2. All scientific conclusions are provisional and can be overturned or revised when new evidence becomes available." },
            { label: "7. (e)", question: "Where does a biologist normally publish their results?", marks: 3, model: "In a peer-reviewed scientific journal, where independent experts in the same field evaluate the methodology and conclusions before publication." },
            { label: "7. (f)", question: "What is meant by the term theory?", marks: 3, model: "A theory is a well-supported explanation for a body of observations, built from many tested and confirmed hypotheses. It is backed by substantial evidence from repeated experiments and peer review, but remains open to revision if new evidence emerges." }
          ]
        },
        {
          id: "bio1-eq-2",
          source: "LC Biology Past Paper — Q2 (Scientific Method)",
          parts: [
            { label: "2. (a)", question: "After making an observation, a biologist often develops a hypothesis. What is a hypothesis?", marks: 4, model: "A hypothesis is a testable, provisional explanation proposed to account for an observation. It must be stated in a way that allows it to be supported or rejected through experimental evidence. Example: If soil pH increases above 7, the germination rate of grass seeds will decrease." },
            { label: "2. (b)", question: "A biologist tests their hypothesis by designing an experiment. State two principles of good experimentation.", marks: 4, model: "1. Control: include an identical setup with the variable being tested absent, to provide a standard of comparison. 2. Repetition/reproducibility: conduct multiple trials to ensure results are consistent and not due to chance or experimental error." },
            { label: "2. (c)", question: "Outline the steps of the scientific method that follow the design of an experiment.", marks: 5, model: "1. Conduct the experiment and collect data carefully. 2. Analyse the data using tables, graphs or statistical methods. 3. Draw a conclusion — does the evidence support or contradict the hypothesis? 4. Publish findings in a peer-reviewed journal. 5. Allow other scientists to repeat the experiment to verify reproducibility." },
            { label: "2. (d)", question: "The scientific method also has limitations. State any one limitation of the scientific method.", marks: 3, model: "Science cannot answer questions of morality, ethics or faith — these lie outside its scope. Alternatively: all scientific conclusions are provisional and subject to revision when new evidence is found." }
          ]
        },
        {
          id: "bio1-eq-3",
          source: "LC Biology Past Paper — Q2 (Germination Investigation)",
          parts: [
            { label: "2. (a)", question: "Draw a vertical line on the graph to indicate the pH most suitable for germination of grass seeds.", marks: 3, diagram: "images/germination-graph.png", model: "Draw the line at approximately pH 6 — this corresponds to the peak of the germination curve where the highest percentage of grass seeds germinate according to the graph." },
            { label: "2. (b)", question: "Explain the term hypothesis.", marks: 3, model: "A hypothesis is a testable, provisional statement proposed to explain an observation; it can be supported or rejected by experimental evidence." },
            { label: "2. (c)", question: "State one variable from the investigation described above.", marks: 2, model: "Independent variable: soil pH (the variable changed by the investigator). Dependent variable: percentage germination of grass seeds (the outcome measured)." },
            { label: "2. (d)", question: "Controls are often used in investigations. What is the function of a control?", marks: 3, model: "A control is an experimental setup identical to the test except that the independent variable (soil pH) is kept at a standard or natural value. It allows results to be compared against a baseline, ensuring differences in germination rate are due to pH change alone." },
            { label: "2. (e)", question: "Where might the horticulturist first publish the results of their research?", marks: 2, model: "In a peer-reviewed scientific journal, where independent scientists evaluate the methodology and findings before publication." },
            { label: "2. (f)", question: "Give two limitations of the scientific method.", marks: 3, model: "1. Science cannot answer moral, ethical or faith-based questions. 2. All scientific conclusions are provisional and may be revised or overturned as new evidence emerges." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 5 =================== */
    {
      id: "bio5",
      number: 5,
      subject: "biology",
      title: "Characteristics of Life",
      learningOutcomes: [
        {
          id: "bio5-1",
          code: "5.1",
          title: "Characteristics of life and levels of organisation",
          notes: [
            { h: "Levels of Organisation", b: "Unicellular -> Multicellular -> Tissue -> Organ -> Organ system -> Organism. Each level is built from the previous." },
            { h: "Tissue", b: "A group of similar cells with a shared function. Human: muscle, nervous, epithelial, connective. Plant: dermal, vascular, ground." },
            { h: "Organ", b: "Structure of several tissues performing a specific function. Human: heart, lung, kidney. Plant: roots, stems, leaves." },
            { h: "Response", b: "Detecting and reacting to a stimulus. Animals: fast via nervous system. Plants: slower growth responses called tropisms (phototropism = toward light; geotropism = toward gravity)." },
            { h: "Aerobic Respiration", b: "Uses oxygen; occurs mainly in mitochondria; breaks glucose down to produce ~38 ATP, CO2 and water." },
            { h: "Anaerobic Respiration", b: "Without oxygen; occurs in cytoplasm; only ~2 ATP. Produces lactic acid (animals) or ethanol + CO2 (yeast/plants)." },
            { h: "Nutrition", b: "Autotrophic: makes own food via photosynthesis (plants, algae). Heterotrophic: takes in ready-made food (animals, fungi)." },
            { h: "Excretion", b: "Removal of metabolic waste. Plants: O2 and CO2 through stomata. Humans: CO2 via lungs; urea via kidneys; water/salts via skin." },
            { h: "Reproduction", b: "Asexual: one parent, genetically identical offspring (e.g. binary fission). Sexual: two parents, gametes fuse, genetically varied offspring." },
            { h: "Metabolism", b: "Sum of all chemical reactions. Anabolic: build complex from simple (require energy, e.g. photosynthesis). Catabolic: break complex down (release energy, e.g. respiration)." },
            { h: "Homeostasis", b: "Maintenance of stable internal conditions. Human examples: body temperature (sweating/shivering), blood glucose (insulin/glucagon), water balance (ADH)." },
            { h: "Heredity and Mutation", b: "Heredity: passing genetic information via DNA. Mutation: change in DNA sequence. Most are neutral/harmful; rare beneficial ones drive evolution (e.g. antibiotic resistance)." },
            { h: "Cell Size and Measurement", b: "Cells measured in micrometres (um). Bacteria: 1-10 um; animal/plant cells: 10-100 um. Actual size = Image size / Magnification." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Name the seven characteristics of life.", model: "Response, Respiration, Nutrition, Excretion, Reproduction, Growth/Metabolism, Homeostasis. A common mnemonic is MRS GREN: Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, Nutrition." },
            { type: "short", marks: 4, prompt: "Distinguish between aerobic and anaerobic respiration.", model: "Aerobic respiration uses oxygen and occurs mainly in mitochondria, producing ~38 ATP plus CO2 and water. Anaerobic respiration occurs without oxygen in the cytoplasm, producing only ~2 ATP; it yields lactic acid in animals or ethanol + CO2 in yeast." },
            { type: "short", marks: 4, prompt: "What is homeostasis? Give two examples in humans.", model: "Homeostasis is the maintenance of stable internal conditions. Examples: (1) body temperature — sweating cools, shivering warms; (2) blood glucose — insulin lowers it when high, glucagon raises it when low." },
            { type: "short", marks: 3, prompt: "Distinguish between autotrophic and heterotrophic nutrition.", model: "Autotrophic organisms make their own food using light energy (photosynthesis), e.g. plants and algae. Heterotrophic organisms must consume ready-made organic food, e.g. animals and fungi." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 6 =================== */
    {
      id: "bio6",
      number: 6,
      subject: "biology",
      title: "Viruses, Classification and Domains of Life",
      learningOutcomes: [
        {
          id: "bio6-1",
          code: "6.1",
          title: "Viruses, classification and the three domains",
          notes: [
            { h: "Virus Structure", b: "Non-cellular. Protein coat (capsid) surrounding genetic material (DNA or RNA). Some have a lipid envelope. Not alive — no cells, no respiration, no independent reproduction." },
            { h: "Virus Shapes", b: "Helical (TMV), icosahedral (adenovirus), complex (bacteriophages), enveloped (influenza, HIV)." },
            { h: "Viral Diseases", b: "Human: influenza, measles, HIV/AIDS, COVID-19. Plant: Tobacco Mosaic Virus, Potato Leaf Roll Virus. Animal: foot-and-mouth, rabies, bird flu." },
            { h: "Beneficial Uses of Viruses", b: "Bacteriophage therapy targets antibiotic-resistant bacteria. Biological control (e.g. myxomatosis). Gene therapy and vaccine production use modified viruses." },
            { h: "Classification", b: "Grouping organisms by shared features. Taxonomy: science of classifying and naming. Importance: organises diversity, allows prediction of features, supports communication." },
            { h: "Binomial System (Linnaeus)", b: "Every species has a two-word Latin name: Genus species (e.g. Homo sapiens). Genus capitalised; species lowercase; both italicised or underlined." },
            { h: "Prokaryotes vs Eukaryotes", b: "Prokaryotes: no membrane-bound nucleus, circular DNA, small ribosomes. Eukaryotes: true nucleus, membrane-bound organelles, linear DNA, larger ribosomes." },
            { h: "Three Domains (Carl Woese, 1990)", b: "Bacteria, Archaea, Eukarya. Archaea are prokaryotic extremophiles differing in cell wall chemistry and rRNA sequences." },
            { h: "Phylogeny", b: "Study of evolutionary relationships. DNA sequencing compares base order; more similar = more recent common ancestor. Shown as a phylogenetic tree with branch points (nodes) = common ancestors." },
            { h: "Dichotomous Key", b: "An identification tool giving two contrasting choices at each step to lead to the correct identification of an unknown organism." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Why are viruses considered non-living?", model: "Viruses lack cells, cannot carry out respiration, do not grow independently, and cannot reproduce outside a host cell. They have no homeostasis. They are considered non-living because they fail to meet the cell-based criteria for life." },
            { type: "short", marks: 4, prompt: "Explain the binomial naming system and give one example.", model: "The binomial system (Linnaeus) gives each species a two-part Latin name: Genus species. The genus is capitalised, species is lowercase, and both are italicised (e.g. Homo sapiens for humans). It allows scientists worldwide to identify organisms unambiguously." },
            { type: "short", marks: 4, prompt: "Name the three domains of life and state which organisms belong to each.", model: "Bacteria: prokaryotic microorganisms such as E. coli. Archaea: prokaryotic extremophiles found in hot springs and salt lakes. Eukarya: all eukaryotic organisms including animals, plants, fungi and protists." },
            { type: "short", marks: 4, prompt: "How is DNA sequencing used to determine evolutionary relationships?", model: "Scientists compare the order of DNA bases between species. The more similar two sequences are, the more recently those species shared a common ancestor. Results are displayed on a phylogenetic tree where branch points show divergence events." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio6-eq-1",
          source: "LC Biology Past Paper — Q5 (Bacterial Cell)",
          parts: [
            { label: "5. (a)", question: "The diagram shows a transmission electron microscope (TEM) image of a bacterial cell. There are three types of bacterial shape. Which type is shown in the picture?", marks: 2, diagram: "images/bacteria-tem.png", model: "Rod-shaped (bacillus). The three bacterial shapes are: coccus (spherical), bacillus (rod/cylinder-shaped) and spirillum (spiral-shaped)." },
            { label: "5. (b)", question: "On the diagram, draw an arrow from the letter X to show the location of the bacterial cell wall.", marks: 2, diagram: "images/bacteria-tem.png", model: "The bacterial cell wall is the dense layer surrounding and just outside the cell membrane — it appears as the outermost rigid boundary of the cell in the TEM image. Arrow should point to this outer layer." },
            { label: "5. (c)", question: "The bacterium is reproducing asexually. What term describes how bacteria reproduce asexually?", marks: 2, model: "Binary fission. The bacterium replicates its circular DNA, elongates, then divides symmetrically into two genetically identical daughter cells." },
            { label: "5. (d)", question: "Give any one factor that affects the growth of bacteria.", marks: 2, model: "Temperature: bacteria grow best at their optimal temperature (e.g. ~37 C for human pathogens); temperatures too high or too low slow growth or kill the bacteria. Other valid answers: pH, nutrient availability, oxygen level, presence of antibiotics." },
            { label: "5. (e)", question: "Name any one harmful bacterium.", marks: 2, model: "Salmonella (food poisoning), Mycobacterium tuberculosis (tuberculosis), Helicobacter pylori (gastric ulcers), Staphylococcus aureus (MRSA/skin infections) or Clostridium tetani (tetanus)." },
            { label: "5. (f) (i)", question: "The partially drawn graph represents the microorganism growth curve. By drawing on the graph, complete the first part of the curve.", marks: 3, diagram: "images/bacteria-growth.png", model: "The complete growth curve has four phases: (1) Lag phase — flat section at the start as cells adapt to the environment. (2) Log (exponential) phase — steep upward curve as population doubles at a constant rate. (3) Stationary phase — the line levels off (birth rate = death rate). (4) Death/decline phase — downward curve as nutrients deplete and waste builds up. Draw the lag and early log phases to complete the curve." },
            { label: "5. (f) (ii)", question: "Name the stage indicated by the letter Z.", marks: 2, model: "Stationary phase — the rate of cell division equals the death rate so population size remains constant. Nutrients are being used up and waste products are accumulating." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 7 =================== */
    {
      id: "bio7",
      number: 7,
      subject: "biology",
      title: "The Unit of Life — The Cell",
      learningOutcomes: [
        {
          id: "bio7-1",
          code: "7.1",
          title: "Cell theory, microscopy and organelles",
          notes: [
            { h: "Cell Theory (3 points)", b: "1. All living things are made of one or more cells. 2. The cell is the basic unit of structure and function. 3. All cells come from pre-existing cells." },
            { h: "Light vs Electron Microscope", b: "Light: visible light + lenses, up to ~1500x, views living cells. Electron: beams of electrons, up to ~500,000x, dead specimens only. TEM = 2D ultrastructure; SEM = 3D surface." },
            { h: "Magnification Calculation", b: "Magnification = Image size / Actual size. Rearrange for any unknown. Total magnification = eyepiece x objective lens." },
            { h: "Nucleus", b: "Control centre; contains chromosomes (DNA + histone proteins); nuclear pores allow mRNA and ribosomes in/out." },
            { h: "Mitochondria", b: "Site of aerobic respiration (ATP). Bean-shaped, double membrane; inner membrane (cristae) folded to maximise surface area for the electron transport chain." },
            { h: "Mitochondria Abundance", b: "High: muscle, liver, sperm, kidney tubules, root meristems. Low: skin cells, red blood cells." },
            { h: "Ribosomes", b: "Site of protein synthesis. Free in cytoplasm or on rough ER. Example product: haemoglobin." },
            { h: "Chloroplasts", b: "Site of photosynthesis. Thylakoids (stacked into grana) hold chlorophyll; stroma contains enzymes for the dark stage." },
            { h: "Rough ER and Golgi", b: "Rough ER: ribosome-studded; processes/folds proteins. Golgi: modifies, packages and ships proteins/lipids in vesicles." },
            { h: "Plant vs Animal Cells", b: "Plant only: cellulose cell wall, large central vacuole, chloroplasts, regular box shape. Animal only: no wall, no chloroplasts, irregular shape, small vacuoles." },
            { h: "Microscope Practical", b: "Cheek cells: scrape, smear, add methylene blue stain, coverslip. Onion cells: peel, place, add iodine stain, coverslip. Lower coverslip at angle to avoid air bubbles." }
          ],
          questions: [
            { type: "short", marks: 3, prompt: "State the three points of cell theory.", model: "1. All living things are made of one or more cells. 2. The cell is the basic unit of structure and function in living organisms. 3. All cells arise from pre-existing cells." },
            { type: "short", marks: 4, prompt: "Compare the light microscope and electron microscope.", model: "Light microscope uses visible light and glass lenses; maximum magnification ~1500x; can view living specimens; cheaper. Electron microscope uses electron beams; magnification up to ~500,000x; only dead, prepared specimens; reveals ultrastructure (organelles like ribosomes)." },
            { type: "short", marks: 4, prompt: "Explain why mitochondria have a folded inner membrane.", model: "The inner membrane is folded into cristae to greatly increase surface area. This provides more space for the electron transport chain enzymes and ATP synthase, maximising the rate of ATP production during aerobic respiration." },
            { type: "short", marks: 4, prompt: "List three structures found in plant cells but not in animal cells and give the function of each.", model: "Cell wall (cellulose): provides structural support and prevents bursting. Large central vacuole: stores water, maintains turgor pressure. Chloroplasts: carry out photosynthesis to make glucose from CO2 and water using light energy." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio7-eq-1",
          source: "LC Biology Past Paper — Q4 (Cell Membrane)",
          parts: [
            { label: "4. (a)", question: "The diagram shows the ultrastructure of a cell membrane with parts labelled X and Y. Name the parts labelled X and Y.", marks: 4, diagram: "images/cell-membrane.png", model: "X: Protein molecule (integral membrane protein) — spans or sits within the phospholipid bilayer; functions in transport, cell signalling and recognition. Y: Phospholipid molecule — has a hydrophilic phosphate head (faces the watery exterior/interior) and hydrophobic fatty-acid tails (pointing inward), forming the bilayer." },
            { label: "4. (b)", question: "Give a function of the cell membrane.", marks: 3, model: "The cell membrane controls what enters and leaves the cell (selective permeability), maintaining a stable internal environment. It also provides receptor sites for hormones and signalling molecules, and facilitates cell-to-cell communication." },
            { label: "4. (c) (i)", question: "What term describes cells without membrane-bound organelles?", marks: 2, model: "Prokaryotic (prokaryotes). Examples: bacteria and archaea. They lack a true nucleus and membrane-bound organelles." },
            { label: "4. (c) (ii)", question: "What term describes cells with membrane-bound organelles?", marks: 2, model: "Eukaryotic (eukaryotes). Examples: animal, plant, fungal and protist cells. They have a membrane-bound nucleus and organelles." },
            { label: "4. (d) (i)", question: "Plant cells have a cell wall in addition to a cell membrane. Sketch the basic structure of a plant cell, clearly labelling the cell membrane and the cell wall.", marks: 5, model: "Sketch a rectangular box-shaped cell showing: outer cell wall (thick, cellulose layer), inner cell membrane (thin layer just inside the wall), large central vacuole, chloroplasts in the cytoplasm, and a nucleus. Label both the cell wall (outermost) and cell membrane (inside the wall)." },
            { label: "4. (d) (ii)", question: "Give one function of a plant cell wall.", marks: 2, model: "The cellulose cell wall provides structural support and rigidity to the plant cell. It prevents the cell from bursting when it becomes turgid (after water enters by osmosis), giving non-woody plants their firmness." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 8 =================== */
    {
      id: "bio8",
      number: 8,
      subject: "biology",
      title: "Biomolecules — The Chemicals of Life",
      learningOutcomes: [
        {
          id: "bio8-1",
          code: "8.1",
          title: "Biomolecules, food tests and nutritional roles",
          notes: [
            { h: "Carbohydrates", b: "Elements: C, H, O (H:O ratio 2:1). Monosaccharides (glucose, fructose) -> disaccharides (sucrose, lactose) -> polysaccharides (starch, glycogen, cellulose). Main fuel; storage; structural (cellulose)." },
            { h: "Lipids", b: "Elements: C, H, O (less O than carbs). Glycerol + fatty acids. Triglyceride = 1 glycerol + 3 fatty acids (storage). Phospholipid = 1 glycerol + 2 fatty acids + phosphate = basis of all membranes." },
            { h: "Phospholipid Bilayer", b: "Hydrophilic head (phosphate) faces water; hydrophobic tails (fatty acids) face inward. Forms the cell membrane." },
            { h: "Proteins", b: "Elements: C, H, O, N (sometimes S). Basic unit: amino acid (20 types). Fibrous: long, strong, insoluble (keratin, collagen). Globular: rounded, soluble, functional (enzymes, haemoglobin, antibodies, insulin)." },
            { h: "Minerals", b: "Calcium (bones/teeth — dairy), iron (haemoglobin — red meat/leafy greens), iodine (thyroid hormone — fish/salt)." },
            { h: "Vitamins", b: "Fat-soluble: A, D, E, K (stored in fat). Water-soluble: B-group, C (not stored, needed daily). Vitamin C deficiency = scurvy. Vitamin D deficiency = rickets (children), osteomalacia (adults)." },
            { h: "Water Roles", b: "Solvent for reactions, transport medium, temperature regulation, lubrication, raw material in photosynthesis, removes wastes." },
            { h: "Food Test: Starch", b: "Reagent: iodine solution. Positive result: blue-black colour." },
            { h: "Food Test: Reducing Sugar", b: "Reagent: Benedict's solution + heat. Positive: brick-red precipitate." },
            { h: "Food Test: Protein", b: "Reagent: biuret (NaOH + CuSO4). Positive: purple/violet colour." },
            { h: "Food Test: Lipids", b: "Rub on filter paper: positive = translucent grease spot. Or ethanol emulsion test: cloudy white suspension." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Describe the food test for starch and protein.", model: "Starch: add iodine solution to the sample; a positive result gives a blue-black colour. Protein: add biuret reagent (NaOH then CuSO4) to the sample; a positive result gives a purple/violet colour." },
            { type: "short", marks: 4, prompt: "What is the difference between a triglyceride and a phospholipid?", model: "A triglyceride has one glycerol molecule joined to three fatty acids; it is a storage molecule. A phospholipid has one glycerol, two fatty acids and one phosphate group; the phosphate head is hydrophilic and the fatty acid tails are hydrophobic, so phospholipids form the bilayer of cell membranes." },
            { type: "short", marks: 4, prompt: "Distinguish between fibrous and globular proteins, giving one example of each.", model: "Fibrous proteins are long, strong and insoluble, serving structural roles (e.g. collagen in tendons and skin). Globular proteins are rounded, soluble and carry out functional roles (e.g. haemoglobin transporting oxygen, or enzymes catalysing reactions)." },
            { type: "short", marks: 4, prompt: "Give two symptoms of vitamin C deficiency and explain why they occur.", model: "Vitamin C is needed for collagen synthesis. Deficiency (scurvy) causes bleeding gums (collagen in blood vessel walls breaks down) and poor wound healing (collagen is needed to form scar tissue). Regular intake of citrus fruit, peppers or broccoli prevents this." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio8-eq-1",
          source: "LC Biology Past Paper — Q1 (Carbohydrates & Proteins)",
          parts: [
            { label: "1. (a)", question: "Write the general formula for carbohydrates.", marks: 3, model: "CH2O (or (CH2O)n / Cn(H2O)n). The ratio of hydrogen to oxygen in carbohydrates is always 2:1, the same as in water." },
            { label: "1. (b)", question: "Give the four chemical elements found in all proteins.", marks: 4, model: "Carbon (C), Hydrogen (H), Oxygen (O) and Nitrogen (N). Some proteins also contain Sulfur (S), but C, H, O, N are present in ALL proteins." },
            { label: "1. (c)", question: "State one structural role of proteins in the body.", marks: 3, model: "Collagen: the most abundant structural protein in the body; forms tendons, ligaments, cartilage, bone matrix and skin, providing tensile strength. Alternatively: Keratin forms hair, nails and the outer layer of skin." },
            { label: "1. (d)", question: "Name the small subunits that make protein.", marks: 2, model: "Amino acids. There are 20 different amino acids joined by peptide bonds to form polypeptide chains, which fold into functional proteins." },
            { label: "1. (e)", question: "Name one water-soluble vitamin.", marks: 2, model: "Vitamin C (ascorbic acid), or any B-group vitamin (B1 thiamine, B2 riboflavin, B12 cobalamin, etc.). Water-soluble vitamins are not stored in the body and must be consumed regularly." },
            { label: "1. (f)", question: "Give one example of a trace element found in food.", marks: 2, model: "Iron (Fe) — found in red meat, spinach and legumes; required for haemoglobin synthesis. Other valid examples: Iodine (fish/iodised salt, thyroid hormone) or Calcium (dairy, bones/teeth)." }
          ]
        },
        {
          id: "bio8-eq-2",
          source: "LC Biology Past Paper — Q1 (Lipids)",
          parts: [
            { label: "1. (a)", question: "Which three chemical elements are present in all lipids?", marks: 3, model: "Carbon (C), Hydrogen (H) and Oxygen (O). Lipids contain significantly less oxygen relative to hydrogen compared to carbohydrates, making them a more concentrated energy store." },
            { label: "1. (b)", question: "How do fats and oils differ at room temperature?", marks: 3, model: "Fats are solid at room temperature (e.g. butter, lard) — typically of animal origin with mainly saturated fatty acids (no C=C double bonds, straight chains that pack tightly). Oils are liquid at room temperature (e.g. olive oil) — typically of plant origin with mainly unsaturated fatty acids (one or more C=C double bonds, kinked chains that cannot pack closely)." },
            { label: "1. (c)", question: "Give one way phospholipids differ from triglycerides.", marks: 3, model: "A phospholipid has two fatty-acid tails instead of three — the third is replaced by a phosphate group. This gives the phospholipid an amphipathic structure (hydrophilic phosphate head + hydrophobic tails), allowing it to form the cell membrane bilayer. Triglycerides are purely hydrophobic storage molecules." },
            { label: "1. (d)", question: "Give one metabolic role of lipids in cells.", marks: 3, model: "Lipids are a concentrated energy store — containing approximately twice as much energy per gram as carbohydrates. Adipose tissue stores triglycerides that can be broken down by lipase for use in cellular respiration when glucose is scarce." },
            { label: "1. (e)", question: "Give one structural role of lipids in cells.", marks: 3, model: "Phospholipids form the phospholipid bilayer of all cell membranes, providing a selectively permeable boundary that controls what enters and leaves the cell." },
            { label: "1. (f)", question: "Name one fat-soluble vitamin.", marks: 2, model: "Vitamin A, D, E or K. These vitamins dissolve in fats and oils, are absorbed with dietary fat from the gut, and can be stored in adipose tissue and the liver." }
          ]
        },
        {
          id: "bio8-eq-3",
          source: "LC Biology Past Paper — Q1 (Carbohydrates — detailed)",
          parts: [
            { label: "1. (a)", question: "Name the three chemical elements present in all carbohydrates.", marks: 3, model: "Carbon (C), Hydrogen (H) and Oxygen (O). The H:O ratio is always 2:1." },
            { label: "1. (b)", question: "Give the general formula for carbohydrates.", marks: 2, model: "CH2O (or (CH2O)n / Cn(H2O)n)." },
            { label: "1. (c)", question: "Name the smallest unit of a carbohydrate.", marks: 2, model: "Monosaccharide (single sugar). Examples: glucose, fructose, galactose (all with formula C6H12O6)." },
            { label: "1. (d)", question: "Name the type of carbohydrate formed when many monosaccharide units bond together.", marks: 2, model: "Polysaccharide. Examples: starch (energy storage in plants), glycogen (energy storage in animals/liver), cellulose (structural in plant cell walls)." },
            { label: "1. (e)", question: "Give one structural role of carbohydrates in living organisms.", marks: 3, model: "Cellulose — a polysaccharide composed of beta-glucose units — forms the rigid cell wall of plant cells, providing mechanical support and preventing the cell from bursting when turgid." },
            { label: "1. (f)", question: "Carbohydrates are an important component of the diet. State one dietary source of carbohydrates.", marks: 2, model: "Bread, pasta, rice, potatoes, cereals, fruit or vegetables — any starch- or sugar-containing food." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 13 =================== */
    {
      id: "bio13",
      number: 13,
      subject: "biology",
      title: "Enzymes",
      learningOutcomes: [
        {
          id: "bio13-1",
          code: "13.1",
          title: "Enzyme structure, action, factors and industrial uses",
          notes: [
            { h: "Enzyme Basics", b: "Globular proteins that act as biological catalysts: speed up reactions without being used up; lower activation energy. Each has a specific active site." },
            { h: "Substrate and Product", b: "Substrate: molecule the enzyme acts on. Product: molecule made. Enzyme specificity: only one substrate fits the active site (lock and key / induced fit)." },
            { h: "Induced Fit Model", b: "Active site changes shape slightly to fit the substrate snugly, like a hand in a glove." },
            { h: "Temperature Effect", b: "Activity rises with temperature up to the optimum (~37 C in humans) then falls sharply as the enzyme denatures (active site shape destroyed — irreversible)." },
            { h: "pH Effect", b: "Activity peaks at the optimum pH (pepsin pH 2, amylase pH 7). Extremes of pH denature the enzyme." },
            { h: "Denaturation", b: "Active site loses its specific shape; substrate can no longer bind. Usually irreversible. Caused by high temperature or extreme pH." },
            { h: "Immobilised Enzymes", b: "Enzyme attached to or trapped in an inert material (e.g. alginate beads). Advantages: reusable (lower cost), product not contaminated, more stable to temperature/pH." },
            { h: "Catalase Experiment", b: "Enzyme: catalase. Substrate: H2O2. Products: water + oxygen. Source: celery, potato or liver. Washing-up liquid traps O2 as foam; foam height measures activity." },
            { h: "Controlling Variables", b: "Change temperature with a water bath; control pH with buffer solutions. Only one variable changed at a time so any effect is attributed to that factor." },
            { h: "Industrial Enzyme Uses", b: "Amylase: bread/beer. Lactase: lactose-free milk. Pectinase: clear fruit juice. Rennin: cheese. Streptokinase: dissolves blood clots. Cellulase/amylase: bioethanol production." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Explain what is meant by enzyme specificity.", model: "Each enzyme has an active site with a unique three-dimensional shape. Only the correct substrate molecule can fit into that active site (induced-fit model — the site adjusts slightly). This means each enzyme catalyses only one specific reaction." },
            { type: "short", marks: 4, prompt: "Describe how temperature affects enzyme activity.", model: "As temperature increases, molecules move faster and collisions between enzyme and substrate are more frequent, so activity rises. At the optimum (~37 C for human enzymes), activity is greatest. Above this, high energy breaks the bonds maintaining the active site's shape — the enzyme denatures and activity falls sharply to zero." },
            { type: "short", marks: 4, prompt: "Give three advantages of using immobilised enzymes in industry.", model: "1. The enzyme can be recovered and reused, lowering production costs. 2. The product is not contaminated with enzyme protein. 3. The immobilised enzyme is more stable to temperature and pH changes than free enzyme." },
            { type: "short", marks: 5, prompt: "Describe the catalase experiment to investigate the effect of temperature on enzyme activity.", model: "Fill test tubes with equal volumes of hydrogen peroxide. Add a fixed amount of catalase source (e.g. equal discs of potato). Place tubes in water baths at different temperatures (e.g. 10, 20, 37, 60 C). Add washing-up liquid to trap O2 as foam. After a set time (e.g. 2 min) measure foam height. Keep the same pH (buffer), same amount of enzyme and substrate. Plot temperature vs foam height. Activity should peak at ~37 C and drop sharply above due to denaturation." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio13-eq-1",
          source: "LC Biology Past Paper — Q9",
          parts: [
            { label: "9. (a) (i)", question: "Briefly explain the term enzyme.", marks: 4, model: "An enzyme is a globular protein that acts as a biological catalyst — it speeds up chemical reactions in living organisms without being consumed. It does this by lowering the activation energy needed to start a reaction. Each enzyme has a uniquely shaped active site that binds only one specific substrate (induced fit model)." },
            { label: "9. (a) (ii)", question: "State one advantage of immobilising enzymes.", marks: 4, model: "The enzyme can be recovered and reused many times, significantly reducing the cost of industrial processes. (Alternatively: the product is not contaminated with enzyme protein, giving a purer product.)" },
            { label: "9. (b) (i)", question: "Name the enzyme or cell you immobilised.", marks: 3, model: "Lactase (enzyme) — used to convert lactose in milk to glucose and galactose, producing lactose-free milk. (Acceptable alternatives: catalase, yeast cells.)" },
            { label: "9. (b) (ii)", question: "Describe the procedure you used to immobilise the enzyme or cell. You may include a labelled diagram if you wish.", marks: 10, model: "1. Dissolve sodium alginate powder in warm distilled water to make a 2% solution. 2. Mix the enzyme (e.g. lactase) thoroughly into the sodium alginate solution. 3. Fill a syringe with the mixture. 4. Drop the mixture dropwise into a beaker of calcium chloride solution — each drop forms a bead immediately as alginate reacts with Ca2+ ions to form an insoluble gel. 5. Leave beads in the CaCl2 solution for a few minutes to harden. 6. Remove beads with a spatula and rinse with distilled water to remove excess calcium chloride. 7. Place beads in a small column or syringe for use." },
            { label: "9. (b) (iii)", question: "Describe how you examined the application of the immobilised enzyme or cell.", marks: 6, model: "Pass a lactose solution (or milk) slowly through the column of immobilised lactase beads. Collect the liquid that drips out from the bottom. Test both the original lactose solution and the collected product using Benedict's solution: heat both samples with Benedict's reagent. The original lactose solution (a non-reducing sugar) gives no colour change. The collected product contains glucose and galactose (reducing sugars) and turns brick-red, confirming the lactase successfully hydrolysed the lactose." }
          ]
        },
        {
          id: "bio13-eq-2",
          source: "LC Biology Past Paper — Q10(b)",
          parts: [
            { label: "10. (b) (i)", question: "During your practical studies you investigated the action of digestive enzymes in germinating seeds using either starch agar or skimmed milk plates. Describe how you set up the apparatus for this investigation.", marks: 10, model: "Starch agar method: 1. Prepare starch agar plates by dissolving starch and agar in boiling water, pouring into petri dishes and allowing to set. 2. Germinate barley or wheat seeds on moist cotton wool for 2–3 days. 3. Crush the germinating seeds in a pestle and mortar with a little distilled water to extract the enzyme. 4. Use a cork borer to cut wells in the starch agar. 5. Pipette a measured volume of the seed extract into the wells. As a control, add distilled water to another well. 6. Incubate at room temperature or 25–30°C for 24–48 hours. 7. Flood the plate with iodine solution and observe for clear (unstained) zones. Skimmed milk plate method: Use the same setup but with skimmed milk agar. After incubation, observe for clear transparent zones (halos) around the wells where protein was digested." },
            { label: "10. (b) (ii)", question: "Explain how you knew digestion had occurred.", marks: 6, model: "On starch agar: the plate was flooded with iodine solution. Iodine turns undigested starch blue-black. A clear (unstained) halo around the seed extract well showed that the enzyme (amylase) in the extract had digested the starch. No clear zone appeared around the control well. On skimmed milk plates: a clear transparent zone (halo) formed around the well containing seed extract, indicating that protease activity had broken down the milk protein (casein). The greater the zone of clearance, the greater the enzyme activity." }
          ]
        },
        {
          id: "bio13-eq-3",
          source: "LC Biology Past Paper — Q5 (Bioreactor)",
          parts: [
            { label: "5. (a)", question: "What is the common name given to this piece of equipment? (large vessel used in food processing with microorganisms/enzymes)", marks: 3, model: "Fermenter (or bioreactor). It is used in industrial biotechnology to grow microorganisms or use enzymes under controlled conditions to produce food products or medicines." },
            { label: "5. (b)", question: "Name two factors controlled by the piece of equipment that could affect the growth of bacteria, other than nutrient availability.", marks: 4, model: "1. Temperature — maintained at the optimum for enzyme activity and microbial growth. 2. pH — kept at the optimum to prevent enzyme denaturation and maintain microbial health. (Other valid: oxygen/aeration level, stirring/mixing speed.)" },
            { label: "5. (c)", question: "Name the two stages X and Y on the population growth curve.", marks: 4, model: "X: Lag phase — microorganisms adapt to their new environment; cells synthesise enzymes and adjust their metabolism; little or no increase in population. Y: Log (exponential) phase — population doubles at a constant rapid rate; nutrients are plentiful and conditions are optimal." },
            { label: "5. (d)", question: "The equipment is keeping the bacteria in steady growth phase Y. Which type of food processing technique is represented?", marks: 3, model: "Continuous culture (continuous fermentation) — fresh nutrient medium is continuously added and products/spent cells are continuously removed, maintaining bacteria in the exponential growth phase at a steady population." },
            { label: "5. (e)", question: "If the bacteria in the equipment were to run out of nutrients, draw on the graph to show how the line would continue.", marks: 3, model: "After nutrient depletion, the curve enters the Stationary phase (levels off — death rate = birth rate) and then the Death/Decline phase (curves downward — death rate exceeds birth rate as toxins accumulate)." }
          ]
        },
        {
          id: "bio13-eq-4",
          source: "LC Biology Past Paper — Q10 (Yeast Investigation)",
          parts: [
            { label: "10. (a) (i)", question: "To which kingdom of living organisms do yeast belong?", marks: 2, model: "Fungi (kingdom Fungi). Yeast are unicellular fungi that reproduce by budding." },
            { label: "10. (a) (ii)", question: "Working with microorganisms often involves sterility. Explain the term sterility.", marks: 4, model: "Sterility is the complete absence of ALL living microorganisms, including spores and non-pathogenic organisms. A sterile environment or piece of equipment contains no viable microorganisms, ensuring that only the intended organism grows in an investigation." },
            { label: "10. (b) (i)", question: "Describe how you set up an investigation to grow leaf yeast. Include one safety precaution. You may include a labelled diagram.", marks: 8, model: "1. Prepare sterile nutrient agar plates (melt agar, pour into petri dishes in a sterile environment, allow to set). 2. Take a leaf and gently wash it in a small volume of sterile distilled water to dislodge surface microorganisms. 3. Using a sterile spreader or loop, spread the leaf-wash onto the agar plate surface. 4. Replace the lid, invert the plate and incubate at approximately 25 C for 48-72 hours. 5. Observe colonies that develop. Control: a plate of agar with sterile distilled water (no leaf-wash) spread on it. Safety precaution: Treat all incubated plates as potential biohazards; do not open plates after incubation; autoclave or disinfect plates before disposal." },
            { label: "10. (b) (ii)", question: "Describe the result of the investigation, assuming the leaf yeast grew successfully.", marks: 4, model: "Colonies of yeast would be visible on the surface of the agar plate — small, round, cream-coloured raised colonies. Each colony grew from a single yeast cell or spore present on the leaf surface. The control plate (no leaf-wash) would show no colonies, confirming that colonies on the experimental plate came from the leaf and not from contamination." }
          ]
        },
        {
          id: "bio13-eq-5",
          source: "LC Biology Past Paper — Q10 (Asepsis and Sterility)",
          parts: [
            { label: "10. (a)", question: "Distinguish between the terms asepsis and sterility as applied to living organisms.", marks: 4, model: "Asepsis: the absence of pathogenic (disease-causing) microorganisms from a specific area, surface or material. It refers to maintaining conditions that prevent infection without necessarily eliminating ALL microorganisms (e.g. aseptic technique in a lab). Sterility: the complete absence of ALL living microorganisms including spores and non-pathogens. Sterility is a more absolute state than asepsis — sterilisation kills every living organism present." },
            { label: "10. (b) (i) 1.", question: "Name a nutrient added to the agar to enable growth of leaf yeast.", marks: 2, model: "Glucose (as a carbon and energy source). Other valid nutrients: peptone or yeast extract (nitrogen source/amino acids), potassium phosphate (minerals)." },
            { label: "10. (b) (i) 2.", question: "Describe the control you used in the investigation of leaf yeast growth.", marks: 3, model: "A sterile agar plate to which sterile distilled water (not the leaf-wash) was added and spread. It was incubated under identical conditions (same temperature, same time period). If the control showed no colonies, this confirmed that any colonies on the experimental plate came from the leaf surface microorganisms and not from airborne contamination or contaminated agar." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 14 =================== */
    {
      id: "bio14",
      number: 14,
      subject: "biology",
      title: "Photosynthesis",
      learningOutcomes: [
        {
          id: "bio14-1",
          code: "14.1",
          title: "Photosynthesis: stages, factors and leaf adaptations",
          notes: [
            { h: "Overview", b: "Anabolic process: plants use light energy to make glucose from CO2 and water. Equation: 6CO2 + 6H2O -> C6H12O6 + 6O2. Chlorophyll captures light." },
            { h: "Carbon Sink", b: "Plants remove CO2 from the atmosphere and lock the carbon into biomass (glucose, starch, cellulose). Vital in regulating atmospheric CO2." },
            { h: "Raw Material Sources", b: "CO2: through stomata from air. Water: root hairs absorb from soil, transported up xylem. Sunlight: captured by chlorophyll." },
            { h: "Light-Dependent Stage", b: "In thylakoid membranes. Light splits water (photolysis): 2H2O -> 4H+ + 4e- + O2. ATP and NADPH produced. O2 is the waste product released." },
            { h: "Light-Independent (Dark) Stage", b: "In stroma (Calvin cycle). CO2 fixed and reduced using ATP and NADPH to form glucose. Enzyme-controlled, so temperature affects this stage strongly." },
            { h: "Chloroplast Adaptations", b: "Thylakoids stacked into grana (large SA for chlorophyll). Stroma contains Calvin cycle enzymes. Double membrane." },
            { h: "Leaf Adaptations", b: "Large flat shape (maximise light). Thin (short diffusion path). Stomata (gas exchange). Chloroplasts in palisade mesophyll (max light absorption). Vascular tissue (transport)." },
            { h: "Factors Affecting Rate", b: "Light intensity, CO2 concentration, temperature. Each can be the limiting factor if too low. Graphs show a rising curve levelling off when another factor becomes limiting." },
            { h: "Investigating Rate (Elodea)", b: "Submerged pondweed; count O2 bubbles per minute. IV = light distance/temperature/CO2 (NaHCO3 conc). DV = bubble rate. Controls = all other factors." },
            { h: "Glucose Uses", b: "Respiration (energy), starch (storage), cellulose (cell walls), proteins, lipids, nucleic acids." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Write the balanced chemical equation for photosynthesis and state where each reactant comes from.", model: "6CO2 + 6H2O -> C6H12O6 + 6O2. CO2 enters through stomata from the air. Water is absorbed by root hairs from the soil and transported up the xylem to leaves. Light energy (from sunlight) drives the reaction via chlorophyll." },
            { type: "short", marks: 4, prompt: "Distinguish between the light-dependent and light-independent stages of photosynthesis.", model: "The light-dependent stage occurs in thylakoid membranes; light splits water (photolysis) releasing O2, and produces ATP and NADPH. The light-independent (dark/Calvin cycle) stage occurs in the stroma; ATP and NADPH are used to fix CO2 into glucose via enzyme-controlled reactions." },
            { type: "short", marks: 4, prompt: "Describe an experiment to investigate the effect of light intensity on photosynthesis.", model: "Place Elodea in a beaker of water with NaHCO3 (CO2 source). Position a lamp at set distances (e.g. 5, 10, 20, 40 cm) and count O2 bubbles per minute at each distance. Keep temperature and CO2 level constant. As light intensity increases, bubble rate increases until another factor (CO2 or temperature) becomes limiting and the graph levels off." },
            { type: "short", marks: 3, prompt: "Explain what is meant by a carbon sink and why plants are important in this role.", model: "A carbon sink removes CO2 from the atmosphere and stores the carbon. Plants fix atmospheric CO2 into glucose during photosynthesis, then store it in biomass as starch, cellulose and other organic molecules. This reduces atmospheric CO2 levels, helping to regulate the greenhouse effect." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio14-eq-1",
          source: "LC Biology Past Paper — Q7 (Photosynthesis)",
          parts: [
            { label: "7. (a) (i)", question: "The graph shows absorption spectra for chlorophyll a and chlorophyll b. Which colour of light is absorbed most by chlorophyll a?", marks: 2, diagram: "images/photosynthesis-spectrum.png", model: "Chlorophyll a has peak absorption in the blue-violet region (~430 nm) and the red region (~680 nm). The strongest peak is in the red region. Answer: Red light (with a secondary peak in blue-violet)." },
            { label: "7. (a) (ii)", question: "Which colour of light is absorbed most by chlorophyll b?", marks: 2, diagram: "images/photosynthesis-spectrum.png", model: "Chlorophyll b absorbs most strongly in the blue region (~460 nm) and in the orange-red region (~640 nm). Answer: Blue light (strongest absorption)." },
            { label: "7. (a) (iii)", question: "What happens to green and yellow light when they strike chlorophyll?", marks: 2, diagram: "images/photosynthesis-spectrum.png", model: "Green and yellow light are mostly reflected (not absorbed) by chlorophyll molecules — this is why plants appear green to our eyes. These wavelengths contribute very little to photosynthesis." },
            { label: "7. (b)", question: "The function of chlorophyll is to absorb sunlight and use this energy to energise electrons. Give two fates of these energised electrons in photosynthesis.", marks: 6, model: "1. Energised electrons are passed along the electron transport chain in the thylakoid membrane, releasing energy that drives ATP synthase to produce ATP from ADP + Pi (photophosphorylation). 2. Energised electrons reduce NADP+ to NADPH by combining with a proton (H+). NADPH acts as a reducing agent in the Calvin cycle, providing hydrogen to reduce CO2 to glucose." },
            { label: "7. (c)", question: "Name another molecule which can provide electrons during photosynthesis.", marks: 2, model: "Water (H2O). During the light-dependent stage, water is split by photolysis: 2H2O -> 4H+ + 4e- + O2. The electrons released replace those lost by chlorophyll, and oxygen is released as a by-product." },
            { label: "7. (d)", question: "Identify a source of the molecule you named in part (c) for photosynthesis in a plant.", marks: 2, model: "Water is absorbed from the soil by root hair cells and transported upward to the leaves through the xylem vessels of the vascular bundles." },
            { label: "7. (e)", question: "Suggest one reason why horticulturists might use carbon dioxide enrichment in a greenhouse.", marks: 3, model: "CO2 is a raw material for the Calvin (light-independent) stage of photosynthesis. Enriching the greenhouse atmosphere with CO2 removes CO2 as a limiting factor, allowing plants to fix more carbon and produce more glucose per unit time, leading to faster growth and higher crop yields." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 15 =================== */
    {
      id: "bio15",
      number: 15,
      subject: "biology",
      title: "Respiration",
      learningOutcomes: [
        {
          id: "bio15-1",
          code: "15.1",
          title: "Aerobic and anaerobic respiration, fermentation",
          notes: [
            { h: "ATP", b: "Adenosine Triphosphate: the cell's energy currency. ATP -> ADP + Pi releases energy used by cells for movement, synthesis, transport and growth." },
            { h: "Aerobic Respiration Overview", b: "Catabolic: glucose + oxygen -> CO2 + water + ~38 ATP. Carbon from glucose is released as CO2; protons end up in water." },
            { h: "Glycolysis", b: "Stage 1. In cytoplasm, no oxygen needed. Glucose (6C) -> 2 pyruvic acid (3C) + 2 ATP + 2 NADH." },
            { h: "Citric Acid (Krebs) Cycle", b: "Stage 2. In mitochondrial matrix. Pyruvic acid -> acetyl CoA -> enters cycle with oxaloacetate -> releases CO2, NADH, FADH2, small ATP." },
            { h: "Electron Transport Chain (ETC)", b: "Stage 3. On inner mitochondrial membrane (cristae). NADH/FADH2 drive ATP synthase via H+ flow -> ~34 ATP. Final electron acceptor: O2 -> water formed." },
            { h: "NAD+ and ATP Synthase", b: "NAD+: coenzyme carrying H+ and electrons (as NADH) to the ETC. ATP synthase: enzyme on cristae that builds ATP as H+ flows through it." },
            { h: "Anaerobic: Lactic Acid", b: "Animal muscle/some bacteria. Glucose -> 2 lactic acid + 2 ATP. Lactic acid removed by liver (converted back to glucose or oxidised). Causes oxygen debt." },
            { h: "Anaerobic: Alcohol Fermentation", b: "Yeast/plants. Glucose -> 2 ethanol + 2 CO2 + 2 ATP. CO2 carbon comes from glucose. Used in bread-making and brewing." },
            { h: "Fermentation Experiment", b: "Anaerobic: seal with oil or fermentation lock. Yeast provides zymase enzymes. Fermentation lock + limewater traps CO2 (turns cloudy). Optimum temp ~30-35 C." },
            { h: "Ethanol Detection", b: "Add acidified potassium dichromate: orange -> green confirms ethanol present." },
            { h: "ATP Yield Comparison", b: "Aerobic: ~38 ATP per glucose. Anaerobic: ~2 ATP per glucose (only glycolysis)." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Name the three stages of aerobic respiration, state where each occurs and give the main products.", model: "1. Glycolysis: cytoplasm -> 2 pyruvic acid + 2 ATP + 2 NADH. 2. Krebs cycle: mitochondrial matrix -> CO2 + NADH + FADH2 + small ATP. 3. Electron transport chain: inner mitochondrial membrane -> ~34 ATP + water." },
            { type: "short", marks: 4, prompt: "Explain how lactic acid is produced and removed during intense exercise.", model: "During intense exercise O2 supply to muscles is insufficient for aerobic respiration; anaerobic respiration in the cytoplasm converts glucose to lactic acid, producing only 2 ATP. Lactic acid builds up causing fatigue. After exercise, extra O2 is consumed (oxygen debt) to allow the liver to convert lactic acid back to glucose or oxidise it to CO2 and water." },
            { type: "short", marks: 5, prompt: "Describe an experiment to demonstrate anaerobic respiration in yeast.", model: "Set up a flask with a glucose-yeast solution and seal with a fermentation lock containing limewater. Boil a second flask of yeast first (kills it) as a control — run the same setup with dead yeast. Leave for 20-30 min at ~30 C. In the live yeast flask, CO2 bubbles through and turns the limewater cloudy. No cloudiness in the control. Test the liquid with acidified potassium dichromate: orange -> green confirms ethanol was produced. Keep temperature constant between flasks." },
            { type: "short", marks: 3, prompt: "What is the role of NAD+ in aerobic respiration?", model: "NAD+ is a coenzyme that picks up hydrogen ions (H+) and electrons from glycolysis and the Krebs cycle to become NADH. NADH then carries these to the electron transport chain where the energy released as electrons pass down the chain powers ATP synthase to make ATP. NAD+ is regenerated and recycled." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio15-eq-1",
          source: "LC Biology Past Paper — Q3 (Aerobic Respiration)",
          parts: [
            { label: "3. (a)", question: "Aerobic respiration is a two-stage process. Stage 2 occurs in the cell organelle shown (diagram of mitochondrion). Name the cell organelle shown.", marks: 2, diagram: "images/mitochondrion.png", model: "Mitochondrion (plural: mitochondria). It is the site of stages 2 and 3 of aerobic respiration — the Krebs cycle (matrix) and the electron transport chain (inner membrane/cristae)." },
            { label: "3. (b)", question: "Name the cycle of reactions that occurs in stage 2 of aerobic respiration.", marks: 2, model: "The Citric Acid Cycle (Krebs Cycle). Occurs in the mitochondrial matrix; pyruvic acid is converted to acetyl CoA, which enters the cycle and is oxidised, releasing CO2 and producing NADH and FADH2." },
            { label: "3. (c)", question: "ATP is produced in large quantities by aerobic respiration. What does ATP stand for?", marks: 2, model: "ATP stands for Adenosine Triphosphate — the cell's main energy currency. Energy is released when the terminal phosphate bond is broken: ATP -> ADP + Pi + energy." },
            { label: "3. (d)", question: "NAD+ is an important molecule in respiration. Give the function of NAD+.", marks: 3, model: "NAD+ (nicotinamide adenine dinucleotide) is a coenzyme that acts as an electron and hydrogen carrier. During glycolysis and the Krebs cycle, NAD+ accepts hydrogen (H+ + electrons) to become NADH. NADH then transports these to the electron transport chain on the inner mitochondrial membrane, where their energy drives ATP synthase to produce large amounts of ATP, and NAD+ is regenerated." },
            { label: "3. (e)", question: "Suggest a condition under which anaerobic respiration might occur.", marks: 2, model: "During intense physical exercise, when the rate of O2 delivery to muscle cells cannot keep pace with the demand for ATP — the cells switch to anaerobic respiration. Alternatively: in a sealed or low-oxygen environment such as a fermentation vessel (e.g. yeast producing ethanol)." },
            { label: "3. (f)", question: "State where anaerobic respiration occurs in a cell.", marks: 2, model: "In the cytoplasm (cytosol). Anaerobic respiration (glycolysis and fermentation) does not require mitochondria and takes place entirely in the cytoplasm." },
            { label: "3. (g)", question: "Name one main product of anaerobic respiration.", marks: 2, model: "In animal cells/bacteria: Lactic acid (lactate). In yeast/plant cells: Ethanol and carbon dioxide. (Both pathways also produce 2 ATP per glucose molecule.)" }
          ]
        },
        {
          id: "bio15-eq-2",
          source: "LC Biology Past Paper — Q9 (Anaerobic Respiration & Yeast Fermentation)",
          parts: [
            { label: "9. (a) (i)", question: "What is meant by the term anaerobic?", marks: 3, model: "Anaerobic means without oxygen. Anaerobic respiration is a form of cellular respiration that takes place in the absence of oxygen. It occurs in the cytoplasm and produces only 2 ATP per glucose molecule (compared to approximately 38 ATP by aerobic respiration)." },
            { label: "9. (a) (ii)", question: "What other substance is produced in animal cells as a result of anaerobic respiration?", marks: 2, model: "Lactic acid (lactate). Glucose -> 2 lactic acid + 2 ATP. Lactic acid accumulates in muscles during intense exercise, contributing to fatigue and muscle soreness." },
            { label: "9. (b) (i)", question: "Draw a labelled diagram showing how you set up the apparatus to prepare alcohol using yeast.", marks: 6, model: "Diagram should show: (1) Conical flask containing glucose solution and yeast. (2) A one-hole bung with a glass delivery tube leading from the flask. (3) The delivery tube leading into limewater (to detect CO2). (4) A fermentation lock or layer of oil sealing the flask to exclude air. Incubate at 30-35 C. Labels: flask, glucose + yeast solution, delivery tube/fermentation lock, limewater/CO2 detector." },
            { label: "9. (b) (ii)", question: "Explain the importance of keeping the yeast cells at an optimum temperature.", marks: 3, model: "Yeast fermentation enzymes (e.g. zymase) have an optimum temperature of approximately 30-35 C. At this temperature, enzyme activity and fermentation rate are maximised. Below the optimum, enzyme activity slows due to reduced molecular kinetic energy. Above the optimum, enzymes are denatured — their active site shape is permanently altered — and fermentation stops." },
            { label: "9. (b) (iii)", question: "Alcohol production eventually stops. Explain why this happens.", marks: 3, model: "Ethanol accumulates to a toxic concentration (typically around 12-15% by volume) that inhibits and kills the yeast cells. Their enzymes are denatured by the high alcohol concentration. Nutrient (glucose) depletion may also contribute to stopping fermentation." },
            { label: "9. (b) (iv)", question: "How did you know when the reaction had stopped?", marks: 2, model: "When the limewater in the delivery tube stopped turning milky/cloudy, indicating that CO2 was no longer being produced. CO2 is a by-product of yeast fermentation; its absence signals the reaction has ceased." },
            { label: "9. (b) (v)", question: "Name a test for alcohol and give the final colour observed if alcohol was present.", marks: 4, model: "Test: Acidified potassium dichromate (add a few drops of acidified K2Cr2O7 to a sample of the fermented liquid). Final colour if alcohol present: Green — the orange dichromate(VI) ion is reduced to green chromium(III) ions by the ethanol (ethanol is oxidised to ethanoic acid)." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 16 =================== */
    {
      id: "bio16",
      number: 16,
      subject: "biology",
      title: "Cell Division and Cancer",
      learningOutcomes: [
        {
          id: "bio16-1",
          code: "16.1",
          title: "Cell cycle, mitosis, meiosis and cancer",
          notes: [
            { h: "Cell Cycle Phases", b: "Interphase (G1, S, G2 — growth + DNA replication), Mitosis (nuclear division), Cytokinesis (cytoplasm divides). Biomolecules formed in interphase: DNA and proteins." },
            { h: "DNA Replication", b: "In S phase. Helix unwinds; DNA polymerase reads each strand and adds complementary nucleotides -> two identical DNA molecules. Essential so each daughter cell gets a full genome." },
            { h: "Haploid and Diploid", b: "Haploid (n = 23): one set of chromosomes; gametes. Diploid (2n = 46): two sets; body cells. Fusion of two haploid gametes at fertilisation restores diploid number." },
            { h: "Mitosis", b: "Produces two genetically identical diploid daughter cells. Role: growth, repair, asexual reproduction. Stages: prophase, metaphase, anaphase, telophase." },
            { h: "Cytokinesis", b: "Animal cells: cleavage furrow pinches inward. Plant cells: cell plate forms between daughters, becoming the new cell wall." },
            { h: "Meiosis", b: "Produces four genetically varied haploid daughter cells (gametes). Two divisions; halves chromosome number; variation from crossing over and independent assortment." },
            { h: "Mitosis vs Meiosis", b: "Mitosis: 1 division -> 2 diploid identical cells (growth/repair). Meiosis: 2 divisions -> 4 haploid varied cells (gametes)." },
            { h: "Cancer", b: "Uncontrolled cell division forming a tumour. Benign: contained, non-spreading. Malignant: invades tissues, metastasis (spreads via blood/lymph), can be fatal." },
            { h: "Cancer Causes", b: "Genetic (inherited mutations, e.g. BRCA1/2), environmental carcinogens (UV, smoking, asbestos), infectious (HPV -> cervical cancer; HepB/C -> liver cancer)." },
            { h: "Cancer Treatments", b: "Surgery (remove tumour), chemotherapy (kill fast-dividing cells), radiation therapy (damage tumour DNA), immunotherapy (stimulate immune system), vaccination (HPV, HepB)." },
            { h: "Risk Factors", b: "Not controllable: age, family history, genetics, gender. Controllable: smoking, alcohol, diet, obesity, sun exposure, exercise, HPV vaccination." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Describe the key events of mitosis.", model: "Prophase: chromosomes condense, spindle forms. Metaphase: chromosomes align at the cell equator attached to spindle fibres. Anaphase: sister chromatids are pulled to opposite poles. Telophase: new nuclear envelopes form around each set of chromosomes. Cytokinesis then divides the cytoplasm to give two identical diploid daughter cells." },
            { type: "short", marks: 4, prompt: "Compare mitosis and meiosis.", model: "Mitosis: one division produces two genetically identical diploid (2n = 46) daughter cells used for growth and repair. Meiosis: two divisions produce four genetically different haploid (n = 23) daughter cells (gametes). Meiosis introduces variation through crossing over (prophase I) and independent assortment." },
            { type: "short", marks: 4, prompt: "Distinguish between benign and malignant tumours.", model: "A benign tumour is a contained mass of cells that does not invade surrounding tissue or spread to other parts of the body; it is often non-fatal. A malignant tumour invades nearby tissues and can metastasise — cancer cells break away and travel via blood or lymph to form secondary tumours elsewhere; it can be fatal." },
            { type: "short", marks: 4, prompt: "List two controllable and two uncontrollable risk factors for cancer.", model: "Controllable: smoking (causes lung/throat cancer), excess UV exposure (skin cancer). Uncontrollable: age (most cancers are more common with age), inherited genetic mutations (e.g. BRCA1 mutation raises breast cancer risk). Controllable risks can be reduced by lifestyle changes; uncontrollable ones can only be monitored." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio16-eq-1",
          source: "LC Biology Past Paper — Q6(d)",
          parts: [
            { label: "6. (d)", question: "Distinguish between the terms haploid and diploid.", marks: 6, model: "Haploid (n): a cell or organism that contains a single set of chromosomes — 23 chromosomes in humans. Haploid cells are the gametes (sperm and egg cells) and are produced by meiosis. Diploid (2n): a cell or organism that contains two complete sets of chromosomes — 46 chromosomes in humans. Diploid cells are all body (somatic) cells and are produced by mitosis. At fertilisation, two haploid gametes fuse to restore the diploid number in the zygote." }
          ]
        },
        {
          id: "bio16-eq-2",
          source: "LC Biology Past Paper — Q6 (f)",
          parts: [
            { label: "6. (f)", question: "Give a brief biological explanation: Meiosis halves the number of chromosomes in cells.", marks: 4, model: "Meiosis is a specialised type of cell division that produces gametes (sex cells — sperm and eggs). Starting from a diploid parent cell (2n = 46 chromosomes in humans), two successive divisions (meiosis I separates homologous chromosomes; meiosis II separates sister chromatids) produce four haploid daughter cells, each with n = 23 chromosomes. Halving the chromosome number is essential so that when two gametes fuse at fertilisation, the normal diploid chromosome number (2n = 46) is restored in the zygote." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 25 =================== */
    {
      id: "bio25",
      number: 25,
      subject: "biology",
      title: "Transport Across Membranes",
      learningOutcomes: [
        {
          id: "bio25-1",
          code: "25.1",
          title: "Diffusion, osmosis, active transport",
          notes: [
            { h: "Diffusion", b: "Movement of particles from high to low concentration. Passive — no ATP required; driven by concentration gradient. Examples: O2 into blood from alveoli; CO2 the reverse." },
            { h: "Selectively Permeable Membrane", b: "Allows some molecules through (small/non-polar) and blocks others (large/charged). Cell membrane, nuclear membrane and organelle membranes are all selectively permeable." },
            { h: "Osmosis", b: "Movement of WATER from high water concentration (low solute) to low water concentration (high solute) across a selectively permeable membrane. Special case of diffusion." },
            { h: "Osmosis vs Diffusion", b: "Osmosis: only water moves, only across a selectively permeable membrane. Diffusion: any dissolved particle, across any barrier." },
            { h: "Isotonic, Hypotonic, Hypertonic", b: "Isotonic: same concentration as cytoplasm — no net movement. Hypotonic outside: water enters — animal swells/bursts (haemolysis); plant becomes turgid. Hypertonic outside: water leaves — animal shrinks (crenation); plant becomes flaccid/plasmolysed." },
            { h: "Turgor Pressure", b: "Pressure of cell contents against the cell wall in plants. Keeps non-woody plants firm. Cellulose wall resists bursting. Loss of turgor = wilting." },
            { h: "Active Transport", b: "Movement of substances AGAINST a concentration gradient using ATP. Examples: mineral uptake by root hairs; sodium-potassium pump in nerve cells; glucose reabsorption in kidney tubules." },
            { h: "Osmosis Experiment (Visking Tubing)", b: "IV = temperature/sucrose concentration/surface area. DV = mass change of tubing. Tubing partially filled so it can expand. Increase in mass = water entered by osmosis." },
            { h: "Osmosis Applications", b: "Salting meat: high salt draws water out of microbes by osmosis, killing them. Plant turgor supports stems. Rehydration therapy replaces water and salts." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Define osmosis and explain how it differs from diffusion.", model: "Osmosis is the movement of water molecules from an area of high water concentration (low solute) to an area of low water concentration (high solute) across a selectively permeable membrane. It differs from diffusion in that only water molecules move, and only across a selectively permeable membrane; diffusion can involve any dissolved substance and does not require a membrane." },
            { type: "short", marks: 4, prompt: "Explain what happens to an animal cell and a plant cell when placed in a hypotonic solution.", model: "In a hypotonic solution (more water outside), water enters both cells by osmosis. The animal cell swells and may burst (haemolysis) because it has no rigid wall. The plant cell also gains water and becomes turgid; the cellulose cell wall resists the swelling pressure, so the plant cell does not burst." },
            { type: "short", marks: 4, prompt: "Describe active transport and give two examples.", model: "Active transport is the movement of substances against their concentration gradient (low to high) using ATP and carrier proteins. Examples: (1) mineral ion uptake by root hair cells from dilute soil water. (2) Glucose reabsorption in kidney tubule cells, pumped back into the blood from dilute filtrate." },
            { type: "short", marks: 4, prompt: "Describe an experiment using Visking tubing to investigate the effect of concentration gradient on the rate of osmosis.", model: "Fill three pieces of Visking tubing with different sucrose concentrations (e.g. 0.1, 0.5, 1.0 M). Weigh each. Place each in beakers of distilled water for 30 min. Reweigh. The increase in mass shows water entered by osmosis. Higher sucrose concentration inside produces a steeper gradient and greater mass increase. Keep temperature, surface area and time constant." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio25-eq-1",
          source: "LC Biology Past Paper — Q9 (Osmosis)",
          parts: [
            { label: "9. (a)", question: "Explain the term osmosis.", marks: 4, model: "Osmosis is the movement of water molecules from a region of high water concentration (low solute concentration) to a region of low water concentration (high solute concentration) across a selectively permeable membrane. It is a passive process — no ATP is required — and is a special case of diffusion involving only water." },
            { label: "9. (b) (i)", question: "Name the tissue or membrane that you used in a laboratory activity to demonstrate osmosis.", marks: 2, model: "Visking tubing (dialysis/cellophane tubing) — a selectively permeable membrane. Alternatively: potato tissue or beetroot tissue, which contain natural selectively permeable membranes." },
            { label: "9. (b) (ii)", question: "Describe how you carried out this activity, including the result. You may include a labelled diagram.", marks: 10, model: "Method using Visking tubing: 1. Soak a piece of Visking tubing in water to make it pliable; tie one end tightly. 2. Fill the tubing with a concentrated sucrose solution (e.g. 1 mol/L); tie the other end, leaving slack for expansion; weigh the tubing. 3. Place the filled tubing in a beaker of distilled water and leave for 20-30 minutes. 4. Remove, dry the outside gently and reweigh. Control: identical tubing filled with distilled water placed in distilled water — no mass change expected. Result: The tubing filled with sucrose solution increases in mass and becomes more turgid, because water moved by osmosis from the distilled water (high water concentration) across the selectively permeable Visking tubing membrane into the sucrose solution (lower water concentration). The control tube shows no change in mass, confirming the result is due to the concentration gradient." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 26 =================== */
    {
      id: "bio26",
      number: 26,
      subject: "biology",
      title: "The Urinary System",
      learningOutcomes: [
        {
          id: "bio26-1",
          code: "26.1",
          title: "Kidney structure, nephron, ADH and osmoregulation",
          notes: [
            { h: "Urinary System Components", b: "Two kidneys, two ureters, one bladder, one urethra. Kidneys flanking the spine at the back of the abdomen." },
            { h: "Kidney Zones", b: "Cortex (outer, filtration), medulla (inner, loops of Henle), pelvis (collects urine -> ureter). Blood in via renal artery, out via renal vein." },
            { h: "Kidney Functions", b: "Excretion of urea and wastes. Osmoregulation (water/salt balance). Blood pH maintenance (~7.4). All via filtration, reabsorption and secretion in nephrons." },
            { h: "Filtration", b: "Glomerulus: high-pressure knot of capillaries forces small molecules into Bowman's capsule. Filtered: water, glucose, salts, urea, amino acids. NOT filtered: red blood cells, plasma proteins, platelets." },
            { h: "Reabsorption", b: "PCT: glucose, amino acids, salts, water, vitamins (active transport — microvilli + many mitochondria). Loop of Henle: water + salts. DCT: fine-tunes salts and pH. Collecting duct: water (ADH-controlled)." },
            { h: "Urine Composition", b: "Normal urine: water (95%), urea, salts, creatinine. Normal urine does NOT contain glucose, protein or blood cells." },
            { h: "Urea Production", b: "Produced in the liver by deamination of excess amino acids. Filtered at glomerulus; not fully reabsorbed; excreted in urine." },
            { h: "ADH (Antidiuretic Hormone)", b: "Released from posterior pituitary. Makes collecting ducts more permeable -> more water reabsorbed -> concentrated urine." },
            { h: "ADH Feedback", b: "Dehydrated (high solute): hypothalamus detects -> pituitary releases ADH -> more reabsorption -> small concentrated urine. Over-hydrated: less ADH -> dilute, plentiful urine." },
            { h: "Diabetes Insipidus", b: "Without ADH: collecting ducts cannot reabsorb water -> large volumes of dilute urine -> severe thirst." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Describe the process of filtration in the nephron.", model: "Blood enters the glomerulus (a knot of capillaries in the Bowman's capsule) at high pressure. This pressure forces small molecules — water, glucose, urea, salts and amino acids — out of the blood into the Bowman's capsule (glomerular filtrate). Large molecules such as plasma proteins and blood cells are too big to cross and remain in the blood." },
            { type: "short", marks: 4, prompt: "Explain the role of ADH in controlling urine volume.", model: "ADH (antidiuretic hormone) is released from the posterior pituitary when blood plasma is too concentrated (e.g. dehydration). ADH makes the collecting ducts more permeable to water, so more water is reabsorbed back into the blood. This produces a small volume of concentrated urine. When fluid intake is high, ADH release is suppressed, less water is reabsorbed and large volumes of dilute urine are produced." },
            { type: "short", marks: 4, prompt: "Name three substances that should NOT normally be found in urine and explain why.", model: "1. Glucose: completely reabsorbed in the PCT by active transport (if present, suggests diabetes mellitus). 2. Plasma proteins: too large to pass through the glomerular filter. 3. Red blood cells: too large to filter (presence indicates kidney damage or infection)." },
            { type: "short", marks: 3, prompt: "Why is urea found in urine?", model: "Urea is a waste product of protein metabolism. Excess amino acids undergo deamination in the liver: the amino group is removed and converted via ammonia to less-toxic urea. Urea enters the blood, is filtered at the glomerulus and is not completely reabsorbed by the tubules, so it is excreted in urine." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio26-eq-1",
          source: "LC Biology Past Paper — Q6 (d)",
          parts: [
            { label: "6. (d)", question: "Give a brief biological explanation: Urine volume will be low if a person does not regularly drink fluids.", marks: 4, model: "When a person is dehydrated, the water content of the blood falls and blood solute concentration rises. The hypothalamus detects this increased osmolarity and signals the posterior pituitary gland to release ADH (antidiuretic hormone). ADH travels in the blood to the kidneys and makes the collecting ducts of the nephrons more permeable to water, causing more water to be reabsorbed back into the bloodstream. The result is a small volume of highly concentrated (dark) urine, reducing further water loss." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 27 =================== */
    {
      id: "bio27",
      number: 27,
      subject: "biology",
      title: "The Digestive System",
      learningOutcomes: [
        {
          id: "bio27-1",
          code: "27.1",
          title: "Digestion, absorption and the liver",
          notes: [
            { h: "Mechanical vs Chemical Digestion", b: "Mechanical: physical breakdown — teeth (mouth) and churning (stomach). Chemical: enzyme breakdown — amylase (mouth), pepsin (stomach), pancreatic/intestinal enzymes (small intestine)." },
            { h: "Peristalsis", b: "Wave-like smooth muscle contractions propelling food along the gut. Dietary fibre adds bulk so muscles have something to push against." },
            { h: "Stomach", b: "HCl: kills microbes, denatures proteins, optimal pH (~2) for pepsin. Pepsin: protease that breaks proteins into polypeptides." },
            { h: "Pancreatic Enzymes", b: "Amylase (starch -> maltose), lipase (lipid -> fatty acids + glycerol), trypsin (peptides -> amino acids). Sodium bicarbonate neutralises acidic chyme from stomach." },
            { h: "Bile", b: "Made in liver from bile salts, bile pigments and cholesterol. Stored in gall bladder. Functions: emulsifies fats (increases SA for lipase), neutralises acidic chyme." },
            { h: "Liver Functions", b: "Makes bile (digestion). Detoxification. Glycogen storage (blood glucose regulation). Plasma protein synthesis. Deamination -> urea production." },
            { h: "Villus Adaptations", b: "Large surface area, one-cell-thick wall, rich capillary network (glucose/amino acids -> blood), lacteal (fats -> lymph as chylomicrons). Maximise absorption rate." },
            { h: "Hepatic Portal System", b: "Hepatic portal vein: nutrient-rich blood from small intestine -> liver. Hepatic artery: O2-rich blood to liver. Hepatic vein: processed blood + urea -> vena cava." },
            { h: "Deamination", b: "Removal of amino group from excess amino acids in the liver. Produces urea (excreted by kidneys) and a carbon residue (used for energy or stored)." },
            { h: "Large Intestine", b: "Reabsorbs water, stores and excretes faeces. Components: caecum, appendix, colon, rectum, anus." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Explain the role of bile in digestion.", model: "Bile is produced by the liver, stored in the gall bladder and released into the duodenum. It does not contain enzymes but: (1) emulsifies fats — bile salts break large fat globules into smaller droplets, increasing surface area for lipase; (2) neutralises acidic chyme from the stomach, creating a neutral/slightly alkaline pH optimal for pancreatic enzymes." },
            { type: "short", marks: 4, prompt: "Describe the adaptations of the villi that make them efficient at absorption.", model: "Villi are finger-like projections lining the ileum. They maximise absorption because: large total surface area; walls only one cell thick (minimal diffusion distance); dense capillary network for rapid uptake of glucose and amino acids; central lacteal absorbs fats as chylomicrons into the lymphatic system." },
            { type: "short", marks: 4, prompt: "Name the three enzymes produced by the pancreas and state what each digests.", model: "Amylase: digests starch into maltose. Lipase: digests lipids into fatty acids and glycerol. Trypsin: digests polypeptides into amino acids." },
            { type: "short", marks: 4, prompt: "Describe the path of a fat molecule from the duodenum to the bloodstream.", model: "In the duodenum, bile emulsifies fat into small droplets. Pancreatic lipase digests these into fatty acids and glycerol. They are absorbed through villus epithelium and reassembled into chylomicrons, which enter the lacteal (lymph vessel). Lymph carries them via the lymphatic system into the bloodstream through the thoracic duct." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio27-eq-1",
          source: "LC Biology Past Paper — Q3 (Alimentary Canal)",
          parts: [
            { label: "3. (a)", question: "The diagram shows the human alimentary canal. Name tube A, organ B and gland C, and give the function of each.", marks: 6, diagram: "images/alimentary-canal.png", model: "Tube A: Oesophagus (gullet) — muscular tube transporting food (as a bolus) from the pharynx to the stomach by peristalsis. Organ B: Stomach — muscular sac where mechanical churning and chemical digestion of proteins occur (HCl + pepsin). Gland C: Pancreas — produces pancreatic juice (amylase, lipase, trypsin, NaHCO3) secreted into the duodenum." },
            { label: "3. (b)", question: "Give one function of tube A.", marks: 2, model: "The oesophagus transports the food bolus from the pharynx (throat) to the stomach by peristalsis — coordinated, wave-like contractions of smooth muscle that propel food downward." },
            { label: "3. (c)", question: "Give one function of organ B.", marks: 2, model: "The stomach mechanically churns food and chemically digests proteins: HCl (hydrochloric acid) lowers gastric pH to approximately 2 (killing microbes and denaturing proteins) and activates pepsin, a protease that hydrolyses proteins into polypeptides." },
            { label: "3. (d)", question: "Give one function of gland C in relation to the digestive system.", marks: 2, model: "The pancreas produces and secretes pancreatic juice into the duodenum via the pancreatic duct. Pancreatic juice contains: amylase (starch to maltose), lipase (fats to fatty acids + glycerol), trypsin (polypeptides to amino acids), and sodium bicarbonate (neutralises acidic chyme from the stomach)." },
            { label: "3. (e)", question: "State one structural feature of the small intestine that enables it to carry out its function.", marks: 3, model: "The inner lining of the small intestine is covered with villi — finger-like projections that increase the surface area for absorption. Each villus is further covered with microvilli (the brush border), further maximising surface area. Each villus has a capillary network and a lacteal for absorbing nutrients into the blood and lymph respectively." },
            { label: "3. (f)", question: "Symbiotic bacteria are present in the alimentary canal. Give two functions of these symbiotic bacteria.", marks: 4, model: "1. Vitamin synthesis: gut bacteria (e.g. E. coli) produce Vitamin K and certain B-group vitamins that the body cannot synthesise in sufficient quantities, supporting blood clotting and metabolism. 2. Competitive exclusion: the resident bacteria occupy niches and consume nutrients, preventing pathogenic bacteria from colonising the gut (colonisation resistance)." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 28 =================== */
    {
      id: "bio28",
      number: 28,
      subject: "biology",
      title: "The Breathing System",
      learningOutcomes: [
        {
          id: "bio28-1",
          code: "28.1",
          title: "Breathing mechanics, gas exchange and lung structure",
          notes: [
            { h: "Why We Breathe", b: "Inhale O2 to supply aerobic respiration in cells; exhale CO2 produced by respiration. Controlled by CO2 levels detected by chemoreceptors in the medulla oblongata." },
            { h: "Airway Pathway", b: "Nose/mouth -> pharynx -> larynx -> trachea -> bronchi -> bronchioles -> alveoli." },
            { h: "Nose Benefits", b: "Warms, moistens and filters inhaled air. Mucus and hairs trap dust and microbes." },
            { h: "Epiglottis and Larynx", b: "Epiglottis: closes trachea during swallowing so food goes into the oesophagus. Larynx: voice box, produces sound. Cartilage rings keep airway open against pressure changes." },
            { h: "Cilia and Mucus", b: "Cilia line trachea/bronchi; sweep mucus + trapped particles upward to the throat to be swallowed or expelled." },
            { h: "Pleural Membranes", b: "Two thin layers surrounding each lung with fluid between them. Reduce friction during breathing; keep lungs attached to thoracic wall." },
            { h: "Alveoli Adaptations", b: "Very large total surface area. Walls one cell thick. Rich capillary network. Moist surface. All maximise O2/CO2 diffusion rate." },
            { h: "Inhalation (Active)", b: "Diaphragm contracts (flattens) + external intercostal muscles contract (ribs up/out) -> thorax volume increases -> pressure drops -> air flows in. Requires ATP." },
            { h: "Exhalation (Passive at Rest)", b: "Diaphragm relaxes (domes up) + intercostal muscles relax (ribs fall) -> thorax volume decreases -> pressure rises -> air flows out. Elastic recoil — no ATP needed at rest." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Describe the mechanism of inhalation.", model: "The diaphragm contracts and flattens. The external intercostal muscles contract, pulling the ribs up and outward. These actions increase the volume of the thoracic cavity. As volume increases, pressure inside the lungs drops below atmospheric pressure, so air flows in. Inhalation is an active process requiring ATP for muscle contraction." },
            { type: "short", marks: 4, prompt: "List four adaptations of the alveoli for efficient gas exchange.", model: "1. Enormous total surface area to maximise diffusion area. 2. Walls only one cell thick to minimise diffusion distance. 3. Rich capillary network maintains a steep concentration gradient. 4. Moist surface allows gases to dissolve before diffusing through." },
            { type: "short", marks: 4, prompt: "Explain why exhalation at rest is described as passive.", model: "At rest, exhalation occurs by elastic recoil — as the diaphragm and intercostal muscles relax, the elastic lung tissue springs back to its resting volume. This decreases thoracic volume and raises internal pressure above atmospheric, pushing air out. No muscle contraction is required so no ATP is used." },
            { type: "short", marks: 3, prompt: "What is the role of the epiglottis and the cilia?", model: "The epiglottis is a flap of cartilage that closes over the trachea during swallowing, directing food into the oesophagus and preventing choking. Cilia are tiny hair-like structures lining the trachea and bronchi; they beat in coordinated waves to sweep mucus containing trapped dust and microbes upward to the throat." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 29 =================== */
    {
      id: "bio29",
      number: 29,
      subject: "biology",
      title: "The Circulatory System and Blood",
      learningOutcomes: [
        {
          id: "bio29-1",
          code: "29.1",
          title: "Heart, blood vessels, blood and circulation",
          notes: [
            { h: "Blood Vessel Types", b: "Arteries: away from heart, high pressure, thick walls, no valves. Veins: to heart, low pressure, valves prevent backflow. Capillaries: one cell thick, site of exchange. Arterioles/venules connect them." },
            { h: "Vessel Wall Layers", b: "Tunica externa (fibrous outer), tunica media (smooth muscle + elastic fibres — vasoconstriction/dilation), tunica intima (smooth inner lining). Lumen = hollow centre." },
            { h: "Heart Structure", b: "In thoracic cavity, behind sternum. Pericardium: protective membrane + fluid to reduce friction. Atria (upper, receive blood), ventricles (lower, pump blood out)." },
            { h: "Heart Valves", b: "Tricuspid (right AV, 3 flaps), bicuspid/mitral (left AV, 2 flaps), semilunar valves (at exits of both ventricles). Prevent backflow. Lub = AV valves closing; dub = semilunar valves closing." },
            { h: "Blood Flow Through Heart", b: "Deoxygenated: vena cava -> right atrium -> tricuspid -> right ventricle -> pulmonary artery -> lungs. Oxygenated: pulmonary vein -> left atrium -> bicuspid -> left ventricle -> aorta -> body." },
            { h: "Double Circulation Benefits", b: "Blood reaches body at high pressure. Oxygenated and deoxygenated blood never mix. More efficient delivery to active tissues." },
            { h: "SA Node and AV Node", b: "SA node: pacemaker in right atrium wall, triggers atrial contraction. AV node: delays and relays impulse to ventricles -> ventricular contraction." },
            { h: "Blood Components", b: "Plasma (~90% water, dissolved proteins/hormones/gases/nutrients), red blood cells (haemoglobin), white blood cells (phagocytes + lymphocytes), platelets (clotting)." },
            { h: "Red Blood Cells", b: "Produced in red bone marrow. No nucleus or mitochondria (maximises haemoglobin). Haemoglobin + O2 -> oxyhaemoglobin in lungs; O2 released in tissues." },
            { h: "Blood Groups and Clotting", b: "ABO system (A, B, AB, O). Incompatible blood -> agglutination (fatal). Rhesus factor: Rh+ has the protein; Rh- does not. Platelets -> clotting factors -> fibrin mesh seals wounds." },
            { h: "Coronary Heart Disease", b: "Coronary arteries supply heart muscle. Blockage -> angina or heart attack. Treatments: stent (keep artery open) or coronary bypass (graft around blockage)." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Trace the path of a deoxygenated red blood cell from the vena cava to the aorta.", model: "Vena cava -> right atrium -> tricuspid valve -> right ventricle -> pulmonary semilunar valve -> pulmonary artery -> lungs (oxygenated) -> pulmonary vein -> left atrium -> bicuspid (mitral) valve -> left ventricle -> aortic semilunar valve -> aorta." },
            { type: "short", marks: 4, prompt: "Explain why the left ventricle has a thicker wall than the right ventricle.", model: "The left ventricle pumps oxygenated blood through the aorta to the entire body (systemic circuit), requiring much higher pressure to overcome the resistance of the long circuit. The right ventricle only pumps to the nearby lungs (pulmonary circuit), which has lower resistance. The left ventricular wall is therefore thicker with more muscle to generate the greater force needed." },
            { type: "short", marks: 4, prompt: "Describe the role of haemoglobin in oxygen transport.", model: "Haemoglobin is an iron-containing globular protein in red blood cells. In the lungs (high O2 partial pressure) it binds up to four O2 molecules to form oxyhaemoglobin. In respiring tissues (low O2) oxyhaemoglobin dissociates and releases O2 to cells. RBCs lack a nucleus and mitochondria to maximise haemoglobin space and avoid consuming the O2 they transport." },
            { type: "short", marks: 4, prompt: "Explain the ABO blood group system and why compatibility matters for transfusions.", model: "ABO groups (A, B, AB, O) are determined by antigens on red blood cells and antibodies in plasma. Transfusing incompatible blood causes the recipient's antibodies to attack donor RBCs, causing agglutination (clumping) which can block vessels and be fatal. Blood must be matched before transfusion." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio29-eq-1",
          source: "LC Biology Past Paper — Q6(e)",
          parts: [
            { label: "6. (e)", question: "Distinguish clearly between systole and diastole.", marks: 6, model: "Systole: the phase of the cardiac cycle during which the heart muscle contracts. Ventricular systole forces blood out of the ventricles — from the right ventricle into the pulmonary artery and from the left ventricle into the aorta. Blood pressure is at its highest point during systole. Diastole: the phase during which the heart muscle relaxes and the chambers refill with blood. The atria and ventricles are filling during diastole. Blood pressure is at its lowest point. The two alternate continuously: one complete systole + diastole = one heartbeat (~0.8 s at rest)." }
          ]
        },
        {
          id: "bio29-eq-2",
          source: "LC Biology Past Paper — Q6 (g)",
          parts: [
            { label: "6. (g)", question: "Give a brief biological explanation: The septum separates the two sides of the human heart.", marks: 4, model: "The septum is a thick muscular wall of cardiac tissue that divides the heart vertically into a right side and a left side. The right side receives deoxygenated blood returning from the body (via the vena cava) and pumps it to the lungs (pulmonary circuit). The left side receives oxygenated blood from the lungs (via pulmonary veins) and pumps it to the body (systemic circuit). The septum ensures that oxygenated and deoxygenated blood never mix, maintaining the efficiency of double circulation." }
          ]
        },
        {
          id: "bio29-eq-3",
          source: "LC Biology Past Paper — Q10 (b) (ii) (Heart Dissection)",
          parts: [
            { label: "10. (b) (ii) 1.", question: "Name one instrument you used to make incisions when dissecting an ox/sheep heart.", marks: 2, model: "Scalpel (or dissection scissors). A scalpel is used to make precise incisions through the muscular walls of the heart to expose the internal chambers, valves and septum." },
            { label: "10. (b) (ii) 2.", question: "Describe one difference between the walls of the right and left ventricles.", marks: 3, model: "The wall of the left ventricle is significantly thicker (approximately 3 times) than the wall of the right ventricle. This is because the left ventricle must generate much higher pressure to pump oxygenated blood through the aorta to the entire body (systemic circuit, high resistance). The right ventricle only needs to pump deoxygenated blood to the nearby lungs (pulmonary circuit, low resistance) and therefore requires less muscular force." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY CHAPTER 30 =================== */
    {
      id: "bio30",
      number: 30,
      subject: "biology",
      title: "Transport in Plants",
      learningOutcomes: [
        {
          id: "bio30-1",
          code: "30.1",
          title: "Xylem, phloem, transpiration and mineral uptake",
          notes: [
            { h: "Plant Tissue Types", b: "Dermal: outer covering, protection/gas exchange (epidermis, cuticle). Vascular: transports water, minerals, sugars (xylem + phloem). Ground: bulk tissue — storage, support, photosynthesis." },
            { h: "Xylem", b: "Dead hollow tubes (tracheids + vessels) with lignified walls. Carries water + minerals upward from roots. Lignin provides strength; no cross-walls allow continuous flow; narrow tubes enable capillary action." },
            { h: "Phloem", b: "Living sieve tube elements (no nucleus) with sieve plates. Companion cells alongside provide energy via plasmodesmata. Transports dissolved sugars (sucrose) in both directions (translocation)." },
            { h: "Xylem vs Phloem", b: "Xylem: dead cells, one direction (up), water + minerals. Phloem: living cells, both directions, dissolved sugars." },
            { h: "Root Hair Cells", b: "High solute concentration so water enters from soil by osmosis. Minerals absorbed by active transport (ATP needed). Long extensions maximise surface area." },
            { h: "Water Path", b: "Soil -> root hair -> cortex -> endodermis -> xylem -> stem xylem -> leaf xylem -> mesophyll cells -> evaporates through stomata (transpiration)." },
            { h: "Cohesion-Tension Model", b: "Water molecules hydrogen-bond to each other (cohesion) and to xylem walls (adhesion). Transpiration creates tension (pull) at the top. Cohesion + tension draws a continuous water column up from roots." },
            { h: "Transpiration Factors", b: "More transpiration with: higher light (stomata open more), higher temperature (faster evaporation), lower humidity (steeper gradient), higher wind (removes water vapour). Measured with a potometer." },
            { h: "Guard Cells and Stomata", b: "Guard cells regulate stomata. Turgid -> stomate opens (light, low CO2). Flaccid -> stomate closes. High CO2 inside -> close; low CO2 -> open." },
            { h: "Reducing Water Loss", b: "Waxy cuticle. Stomata mainly on lower leaf surface. Sunken stomata (xerophytes). Rolled/hairy leaves. Thick cell walls." },
            { h: "Essential Minerals", b: "Nitrogen (proteins, chlorophyll), phosphorus (DNA, ATP, membranes), potassium (enzyme activation, stomata), magnesium (chlorophyll), calcium (cell walls). Absorbed by active transport in root hairs." }
          ],
          questions: [
            { type: "short", marks: 4, prompt: "Compare xylem and phloem.", model: "Xylem: dead, hollow cells with lignified walls; transports water and dissolved minerals upward only from roots to leaves; provides structural support. Phloem: living sieve tube elements with companion cells; transports dissolved sugars (sucrose) in both directions from leaves to all parts of the plant (translocation)." },
            { type: "short", marks: 4, prompt: "Explain the cohesion-tension model of water transport.", model: "As water evaporates through stomata (transpiration), it creates tension (a pulling force) at the top of the xylem column. Water molecules are held together by hydrogen bonds (cohesion) and also adhere to xylem walls. This combination pulls a continuous column of water up from the roots to replace what is lost, without the plant expending ATP." },
            { type: "short", marks: 4, prompt: "Describe how a potometer is used to measure the effect of humidity on transpiration.", model: "Set up a leafy shoot in a water-filled potometer in a sealed system. Mark the position of an air bubble in the capillary tube. In high humidity, record the bubble movement per minute (low = low transpiration rate). Move to low humidity and repeat. The bubble moves faster in low humidity because the water-vapour gradient between leaf and air is steeper, driving faster evaporation." },
            { type: "short", marks: 4, prompt: "How do guard cells regulate stomatal opening?", model: "In light (and when CO2 is low), guard cells absorb K+ ions by active transport, lowering their water potential. Water enters by osmosis making them turgid; their curved shape causes them to bow outward, opening the stoma. In darkness or high CO2 or drought, K+ leaves, guard cells become flaccid and the stoma closes, reducing water loss." }
          ]
        }
      ],
      examQuestions: [
        {
          id: "bio30-eq-1",
          source: "LC Biology Past Paper — Q2 (Plant Root Section)",
          parts: [
            { label: "2. (a)", question: "The diagram shows a longitudinal section through the root of a plant. Name the structure indicated by letter X and give its function.", marks: 4, diagram: "images/root.png", model: "X: Root cap (calyptra). Function: Protects the root apical meristem (the zone of actively dividing cells at the root tip) from mechanical damage as the root pushes through the soil. The outermost cells are continuously shed and replaced." },
            { label: "2. (b)", question: "Name the tissue type indicated by letter Y and give its function.", marks: 4, diagram: "images/root.png", model: "Y: Vascular tissue (xylem and phloem forming the central vascular cylinder). Function: Xylem transports water and dissolved mineral ions from roots upward to shoots and leaves. Phloem transports dissolved sugars (sucrose, products of photosynthesis) from leaves to all living regions of the plant." },
            { label: "2. (c)", question: "Name the tissue indicated by letter Z where rapid mitosis is occurring.", marks: 2, diagram: "images/root.png", model: "Meristematic tissue (root apical meristem / zone of cell division). These are undifferentiated cells that divide rapidly by mitosis, producing new cells that elongate and differentiate into the various root tissues." },
            { label: "2. (d)", question: "Draw and label a transverse section of the root as it would appear if cut at the position of the dashed line.", marks: 5, diagram: "images/root.png", model: "Sketch should show (from outside inward): Epidermis (outermost single layer, some cells extended as root hairs), Cortex (wide zone of large thin-walled parenchyma cells, used for storage), Endodermis (single layer with Casparian strip), Pericycle, and central Vascular cylinder with Xylem (X-shaped, thick walls) in the centre and Phloem located between the arms of the xylem. Label all tissues." }
          ]
        },
        {
          id: "bio30-eq-2",
          source: "LC Biology Past Paper — Q4 (Xylem and Phloem)",
          parts: [
            { label: "4. (a)", question: "The diagram shows a longitudinal view of xylem vessels and phloem. Label any one structure on the diagram.", marks: 2, diagram: "images/xylem-phloem.png", model: "Label either: Xylem vessel — dead, hollow, lignified tube transporting water upward. Phloem sieve tube — living cell with sieve plates transporting sugars. Companion cell — living cell alongside phloem sieve tube, providing metabolic support." },
            { label: "4. (b)", question: "To which type of plant tissue do xylem and phloem belong?", marks: 2, model: "Vascular tissue (vascular bundle). This is one of the three fundamental plant tissue systems, alongside dermal tissue and ground tissue." },
            { label: "4. (c)", question: "Give one function of xylem.", marks: 2, model: "Xylem transports water and dissolved mineral salts (e.g. nitrates, phosphates, potassium) from the roots upward to the leaves and all aerial parts of the plant." },
            { label: "4. (d)", question: "Give one function of phloem.", marks: 2, model: "Phloem transports dissolved organic substances — principally sucrose produced by photosynthesis in the leaves — bidirectionally to all living parts of the plant that need energy and building materials (a process called translocation)." },
            { label: "4. (e) (i)", question: "The image shows the arrangement of xylem and phloem in a transverse section of a stem. Is this stem from a monocot or a dicot? Justify your answer.", marks: 4, model: "This is a monocot stem. In monocotyledonous plants (e.g. maize, grass), vascular bundles are scattered irregularly throughout the ground tissue. In dicotyledonous plants (e.g. sunflower, bean), vascular bundles are arranged in a ring near the periphery of the stem. The scattered pattern of bundles in the image is characteristic of a monocot." },
            { label: "4. (f)", question: "State the location of the tissue containing xylem and phloem in a transverse section of a root.", marks: 2, model: "In the centre of the root, forming the central vascular cylinder (stele). The xylem forms a star/X-shape at the very centre with phloem bundles positioned between the xylem arms. This is surrounded by the pericycle and endodermis." }
          ]
        },
        {
          id: "bio30-eq-3",
          source: "LC Biology Past Paper — Q10 (b) (iv) (Dicot Stem Section)",
          parts: [
            { label: "10. (b) (iv) 1.", question: "Explain the importance of the section being thin when viewing a transverse section of a dicot stem under the light microscope.", marks: 3, model: "A thin section allows sufficient light to pass through the specimen so that a clear image can be formed. If the section were too thick, insufficient light would reach the eyepiece, the image would be too dark to observe detail, and overlapping tissue layers would make identification of individual tissue types impossible." },
            { label: "10. (b) (iv) 2.", question: "Sketch what you observed under the light microscope when viewing a transverse section of a dicot stem.", marks: 5, model: "Sketch (from outside to centre): 1. Epidermis — single outer ring of cells. 2. Cortex — several layers of larger, thin-walled cells (may include collenchyma). 3. Vascular bundles arranged in a ring near the periphery: each bundle has Phloem (outer, smaller living cells) and Xylem (inner, large dead cells with thick walls). 4. Pith — large thin-walled parenchyma cells filling the centre. Label: epidermis, cortex, phloem, xylem, pith." }
          ]
        }
      ]
    },

    /* =================== LC BIOLOGY ACRONYMS =================== */
    {
      id: "bio-acronyms",
      number: 31,
      subject: "biology",
      title: "Biology Acronyms and Key Terms",
      learningOutcomes: [
        {
          id: "bio-acronyms-1",
          code: "A.1",
          title: "Acronyms and key terms to learn",
          notes: [
            { h: "DNA / RNA", b: "DNA: Deoxyribonucleic Acid. RNA: Ribonucleic Acid." },
            { h: "ATP / ADP", b: "ATP: Adenosine Triphosphate (energy currency). ADP: Adenosine Diphosphate (ATP after energy release)." },
            { h: "NAD+ / NADH / NADP+ / NADPH", b: "NAD+: Nicotinamide Adenine Dinucleotide (oxidised). NADH: reduced form, carries electrons to ETC. NADP+/NADPH: phosphorylated version used in photosynthesis." },
            { h: "FAD / FADH2", b: "Flavin Adenine Dinucleotide — coenzyme that carries electrons to the ETC from the Krebs cycle." },
            { h: "ER / TEM / SEM", b: "ER: Endoplasmic Reticulum (smooth = lipids; rough = proteins). TEM: Transmission Electron Microscope (2D). SEM: Scanning Electron Microscope (3D)." },
            { h: "ETC", b: "Electron Transport Chain — on inner mitochondrial membrane; uses NADH/FADH2 to drive ATP synthesis." },
            { h: "SA Node / AV Node", b: "SA node: Sinoatrial node — heart pacemaker in right atrium. AV node: Atrioventricular node — delays and relays impulse to ventricles." },
            { h: "ADH", b: "Antidiuretic Hormone (vasopressin) — released by posterior pituitary; makes collecting ducts more permeable to water." },
            { h: "PCT / DCT", b: "PCT: Proximal Convoluted Tubule (reabsorbs glucose, amino acids, water). DCT: Distal Convoluted Tubule (fine-tunes salts and pH)." },
            { h: "RBC / WBC", b: "RBC: Red Blood Cell — carries haemoglobin. WBC: White Blood Cell — phagocytes (engulf microbes) and lymphocytes (produce antibodies)." },
            { h: "Pulmonary / Systemic Circuit", b: "Pulmonary: heart -> lungs -> heart (gas exchange). Systemic: heart -> body -> heart (delivers O2, collects CO2)." },
            { h: "ABO / Rh", b: "ABO: four main blood groups (A, B, AB, O). Rh: Rhesus factor — Rh+ has the protein, Rh- does not." },
            { h: "Classification Hierarchy", b: "Domain -> Kingdom -> Phylum -> Class -> Order -> Family -> Genus -> Species. Mnemonic: 'Dear King Philip Came Over For Good Soup'." },
            { h: "Three Domains", b: "Bacteria (prokaryotes, e.g. E. coli), Archaea (prokaryotic extremophiles), Eukarya (all eukaryotes)." },
            { h: "Photosynthesis Equation", b: "6CO2 + 6H2O -> C6H12O6 + 6O2 (in light, with chlorophyll)." },
            { h: "Aerobic Respiration Equation", b: "C6H12O6 + 6O2 -> 6CO2 + 6H2O + ~38 ATP." },
            { h: "ATP Yields", b: "Aerobic respiration: ~38 ATP per glucose. Anaerobic respiration: ~2 ATP per glucose (glycolysis only)." },
            { h: "Experiment Variables", b: "IV: Independent Variable (changed by experimenter). DV: Dependent Variable (measured). CV: Control Variables (kept constant)." },
            { h: "Food Tests Summary", b: "Iodine -> blue-black = starch. Benedict's + heat -> brick-red = reducing sugar. Biuret -> purple = protein. Ethanol emulsion -> cloudy white = lipid. Acidified potassium dichromate orange -> green = ethanol." },
            { h: "Limewater", b: "Turns cloudy/milky white in the presence of CO2. Used to confirm CO2 production in respiration experiments." }
          ],
          questions: [
            { type: "short", marks: 5, prompt: "State the classification hierarchy from domain to species and give the mnemonic.", model: "Domain -> Kingdom -> Phylum -> Class -> Order -> Family -> Genus -> Species. Mnemonic: 'Dear King Philip Came Over For Good Soup'." },
            { type: "short", marks: 6, prompt: "Write the equations for photosynthesis and aerobic respiration and state the ATP yield of each.", model: "Photosynthesis: 6CO2 + 6H2O -> C6H12O6 + 6O2 (uses light energy; net producer of glucose and oxygen). Aerobic respiration: C6H12O6 + 6O2 -> 6CO2 + 6H2O + ~38 ATP. Anaerobic respiration yields only ~2 ATP per glucose." },
            { type: "short", marks: 4, prompt: "Name four food tests, the reagent used and a positive result for each.", model: "Starch: iodine -> blue-black. Reducing sugar: Benedict's solution + heat -> brick-red precipitate. Protein: biuret reagent (NaOH + CuSO4) -> purple/violet. Lipid: ethanol emulsion test -> cloudy white suspension." },
            { type: "short", marks: 4, prompt: "Explain the roles of the SA node and ADH.", model: "SA node (sinoatrial node): acts as the heart's pacemaker in the right atrium wall; generates electrical impulses that trigger atrial contraction and set heart rate (~60-80 bpm at rest). ADH (antidiuretic hormone): released from the posterior pituitary when blood is too concentrated; makes collecting ducts more permeable to water so more is reabsorbed, producing concentrated urine and restoring normal blood water content." }
          ]
        }
      ]
    }
  ]
};
