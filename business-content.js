// Business HL Content — notes, concept points and flashcards for all chapters.
// Past-paper exam questions live in exam-questions-db.js.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  function ch(id) { return COURSE_DATA.chapters.find(function (c) { return c.id === id; }); }

  // ── ch1: Key Stakeholders in Business ─────────────────────────────────────
  (function () {
    var c = ch("ch1");
    // 1.1 — Internal & external stakeholders and their importance
    c.learningOutcomes[0].notes = [
      {
        h: "Distinguish between internal and external stakeholders.",
        b: "Internal stakeholders are individuals or groups directly involved in running the business (Owner/Entrepreneur, Managers, Employees, Investors). External stakeholders are not directly involved but are affected by the business's activities (Consumers, Local Community, Suppliers, Government, Interest Groups)."
      },
      {
        h: "Distinguish between Owner and Entrepreneur (Internal).", b: "Role: Identifies opportunities, secures funding, takes personal/financial risks. Importance: Provides leadership, vision and shoulders early risk. Needs/Wants: Financial success, recognition, independence and control. Example: Shane Curran raised €3m+ for cybersecurity start-up Evervault."
      },
      {
        h: "What is the role of Managers?",
        b: "Role: Set objectives based on the entrepreneur's vision and organise resources. Importance: Coordinate daily operations, motivate staff, keep business focused. Needs/Wants: Resources, recognition, career progression. Example: Anne O'Leary became Head of Meta Ireland in 2023."
      },
      {
        h: "What is the role of Employees?",
        b: "Role: Follow manager's instructions, share ideas, use skills daily. Importance: Provide time, experience and qualifications to keep the business productive. Needs/Wants: Fair pay, good conditions, respect, more responsibility over time."
      },
      {
        h: "What is the role of Investors (Internal)?", b: "Role: Provide funding for equity (ownership) or debt (banks, repayments + interest). Importance: Help the business grow; may bring contacts, experience, advice. Needs/Wants: Early-stage — accept higher risk, lower dividends; later — return through dividends, less risk. Example: Act Venture Capital, Enterprise Ireland."
      },
      {
        h: "What is the role of Consumers (External)?", b: "Role: Purchase goods/services, give feedback, advocate for the business. Importance: Drive revenue, shape brand reputation. Needs/Wants: Quality, value for money, good service, ethical/sustainable practices. Example: Patagonia commands premium prices because customers value its ethics."
      },
      {
        h: "What is the role of Local Community (External)?", b: "Role: People and area surrounding the business. Importance: Goodwill provides a base of customers and employees. Needs/Wants: Local jobs, access to goods/services, environmental and ethical responsibility."
      },
      {
        h: "What is the role of Suppliers?",
        b: "Role: Provide raw materials, products or services the business uses. Importance: Reliable supply allows consistent production and quality. Needs/Wants: To be paid on time, longer-term contracts. Example: McDonald's sources 100% Irish beef."
      },
      {
        h: "What is the role of Government (External)?", b: "Role: Regulates business activity, provides grants/incentives, supports start-ups via LEOs and Enterprise Ireland. Importance: Funding, training, mentoring, infrastructure, lower taxes create a positive business climate. Needs/Wants: Compliance with laws, payment of tax, social responsibility, exports, job creation."
      },
      {
        h: "What is the role of Interest Groups (External)?", b: "Also called pressure or lobby groups. Role: Represent shared objectives of a group. Importance: Negotiate with and inform other stakeholders. Methods: Lobbying, media campaigns, protests, boycotts, legal action. Example: Small Firms Association (SFA) lobbied Government in 2024."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline two internal stakeholders and explain their importance in the business environment.",
        model: "**Owner/Entrepreneur**: Identifies market opportunities, secures funding and takes the risks involved in starting the business. They are crucial because they transform business ideas into viable operations and provide leadership and strategic vision.\n\n**Employees**: Use their skills to complete daily tasks set by management. They are essential as they bring experience, ideas and qualifications that keep the business productive and able to deliver to customers."
      },
      {
        type: "short",
        marks: 10,
        prompt: "Demonstrate the importance of a business's relationship with its (i) suppliers and (ii) government. (2 @ 5m: 3m relationship explained + 2m reasoning/application)",
        model: "**(i) Suppliers**: Suppliers provide the raw materials, products or services a business needs to produce its own goods. A strong relationship ensures consistent supply of quality inputs delivered on time, allowing the business to meet customer demand efficiently and avoid costly production delays.\n\n**(ii) Government**: Through bodies like the Local Enterprise Office (LEO) and Enterprise Ireland, the government provides funding, training, mentoring and grants. A good relationship with government gives the business access to expert advice and financial support that can improve its chances of early success and expansion."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Outline how the needs and wants of an investor may change at different stages of business development.",
        model: "At the **start-up stage**, the investor may accept more risk and prioritise long-term growth, focusing on brand development and market entry; they may accept lower or no dividends.\n\nAt **maturity**, as the business becomes more stable, they want to see consistent profits and seek a return through dividends or expansion opportunities. Their focus shifts from growth potential to performance and steady returns."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "Which of the following is NOT an internal stakeholder?",
        model: "Suppliers are external stakeholders — they are not directly involved in running the business but are affected by its activities.",
        options: [
          "Manager",
          "Employee",
          "Supplier",
          "Investor"
        ],
        correct: 2
      },
      {
        type: "tf",
        marks: 2,
        prompt: "Banks providing a loan to a business are considered internal investors who take ownership in the business.",
        model: "False. A bank providing a loan supplies debt (repaid with interest) and does not take ownership. Investors who buy shares (equity) take ownership; lenders do not.",
        correct: false
      },
      {
        type: "short",
        marks: 6,
        prompt: "List three external stakeholders and briefly state the role of each in a business.",
        model: "1. **Consumers** — Purchase goods/services and give feedback that shapes the brand.\n2. **Suppliers** — Provide raw materials and inputs needed to produce the business's goods/services.\n3. **Government** — Regulates business activity and provides supports such as grants and training through LEOs and Enterprise Ireland."
      }
    ];
    // 1.2 — How stakeholders interact and potential conflicts
    c.learningOutcomes[1].notes = [
      {
        h: "What is a co-operative stakeholder relationship?", b: "Both stakeholders mutually benefit from working towards a common goal. Examples: Employer & Employee — training boosts employee skills and business productivity. Investor & Owner — funding allows growth and profit for both. Producer & Producer — local producers share promotional costs (e.g. cheese festival)."
      },
      {
        h: "What is a competitive stakeholder relationship?", b: "Conflict arises when needs of stakeholders are mutually exclusive — one gains, the other loses. Examples: Employer wants to cut pay vs Employee wants a pay rise. Investor wants high dividends vs Manager wants to reinvest profits. Supplier wants quick payment vs Manager wants to delay payment to manage cash flow. Producer vs Producer — competing for the same customers."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Demonstrate how stakeholders can interact in (i) a co-operative way and (ii) a competitive way. Use one example for each.",
        model: "**(i) Co-operative**: An employer invests in staff training. The employees gain skills that allow them to earn promotion or pay rises, while the business benefits from more productive, capable workers. Both sides win.\n\n**(ii) Competitive**: An investor wants higher dividend payments from the business's profits, while the manager wants to reinvest those profits back into the business to fund expansion. If one side gets what it wants, the other loses out — it is a win-lose situation."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Identify a potential conflict that might arise between an entrepreneur and (i) consumers and (ii) employees. (2 @ 4m)",
        model: "**(i) Consumers**: Consumers may want low prices and good value, but if the entrepreneur uses high-quality, ethical or sustainable inputs, costs are higher and the product becomes more expensive. This creates tension over pricing.\n\n**(ii) Employees**: Employees might want job security and predictable hours, but as a small start-up the entrepreneur may need flexibility, offer only part-time roles, or be unable to guarantee consistent work — leading to conflict over job security."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "Which of the following best describes a co-operative stakeholder relationship?",
        model: "A co-operative relationship is win-win, where both parties benefit. Agreed payment terms suit both supplier and manager.",
        options: [
          "Employer cuts pay while employees demand a rise",
          "Investor demands dividends while manager reinvests profits",
          "Supplier and manager agree on payment terms that suit both",
          "Two competing producers fight for the same customers"
        ],
        correct: 2
      }
    ];
    // 1.3 — Avoiding and resolving conflict between stakeholders
    c.learningOutcomes[2].notes = [
      {
        h: "What strategies can a business use to avoid stakeholder conflict?", b: "**1. Open communication**: Honest, regular contact with stakeholders helps spot concerns early (e.g. fairly handling customer complaints). **2. Corporate Social Responsibility (CSR)**: Ethical decisions that balance profit with societal good (e.g. avoid unfair price hikes on loyal customers). **3. Stakeholder Involvement**: Include stakeholders in decisions (e.g. builders consulting local communities before major projects)."
      },
      {
        h: "What are the main methods for resolving stakeholder conflicts?", b: "**1. Meet & Talk**: Direct discussion (e.g. supplier and manager agree a realistic payment timeline). **2. Negotiation/Bargaining**: Both sides give and take (e.g. employee wants a 4-day week, owner wants output maintained — agree a trial with targets). **3. Mediation**: A neutral third party helps both sides reach their own agreement (e.g. local community and developer with a mediator). **4. Conciliation**: A third party suggests a possible solution that the parties may accept (e.g. phased dividend increase). **5. Arbitration**: Independent arbitrator hears both sides, reviews evidence, and makes a binding recommendation that both parties have agreed in advance to accept (e.g. unfair dismissal claim)."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Outline two strategies a business can use to avoid stakeholder conflict.",
        model: "**1. Open Communication**: Maintain honest, regular contact with stakeholders. By understanding concerns early — for example, by handling customer complaints fairly — small issues can be resolved before they grow into major disputes.\n\n**2. Stakeholder Involvement**: Include stakeholders in decision-making. For example, a building company consulting the local community before starting a major project reduces resistance and builds trust."
      },
      {
        type: "short",
        marks: 10,
        prompt: "Should a conflict arise with investors over the use of profits in a business, suggest two ways of resolving the conflict between an entrepreneur and their investors. (2 @ 5m: 2m method + 2m solution + 1m how it would work)",
        model: "**1. Negotiation/Bargaining**: The entrepreneur and investor meet directly and each makes compromises. For example, they could agree that 60% of profits are paid as dividends and 40% reinvested into the business. This works because both sides feel they have made gains — the investor receives a return, while the business still has funds to grow.\n\n**2. Conciliation**: A neutral third party listens to both sides and suggests a possible compromise, such as a phased increase in dividends over three years as profits grow. The conciliator helps both parties move closer to agreement themselves rather than imposing a binding decision."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Distinguish between mediation and arbitration as methods of resolving stakeholder conflict.",
        model: "**Mediation**: A neutral third party (the mediator) helps both sides reach their own agreement by improving communication. The mediator does not make a decision — the parties find their own solution.\n\n**Arbitration**: An independent arbitrator hears both sides and reviews the evidence, then issues a recommendation. Both parties agree in advance to accept the arbitrator's decision, which is binding."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "In which conflict resolution method is the third party's decision binding on both sides?",
        model: "Arbitration produces a binding recommendation that both parties have agreed in advance to accept.",
        options: [
          "Mediation",
          "Conciliation",
          "Arbitration",
          "Negotiation"
        ],
        correct: 2
      }
    ];
    // 1.4 — Stakeholder mapping and prioritising stakeholder interests
    c.learningOutcomes[3].notes = [
      {
        h: "Describe the process of stakeholder mapping and its purpose.", b: "A business measures the **interest** (how affected they are) and **influence/power** (how much they can change a decision) of each stakeholder, to decide who to prioritise when making decisions."
      },
      {
        h: "What are the key steps involved in conducting stakeholder mapping?", b: "**1. Identify stakeholders** — list all groups affected, internal and external. **2. Analyse power and interest** — judge the level of influence and interest of each group. **3. Map to a Power–Interest grid** — High/Low Power on one axis, High/Low Interest on the other. **4. Allocate resources & plan engagement** — focus most attention on stakeholders with both high power and high interest."
      },
      {
        h: "What is the importance of stakeholder mapping?", b: "**1. Improves decision-making quality**: Helps a business consider all viewpoints before deciding (e.g. a bank may delay branch closures after mapping shows high impact on older customers). **2. Supports strategic planning**: Helps plan long-term actions and avoid surprises (e.g. during expansion, a company maps which stakeholders to engage early — local councils, investors)."
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "A bakery is planning a major expansion. Conduct stakeholder mapping to identify and prioritise four stakeholders affected by this decision. (4 @ 3m)",
        model: "**1. Employees — High Interest, High Power**: Their hours and roles will change directly, and as a unionised group they can resist or support the change. **Priority: Manage closely** — consult and involve them.\n\n**2. Customers — High Interest, Low Power**: Affected by changes to product range/prices but limited influence individually. **Priority: Keep informed** with clear communication.\n\n**3. Local Community — Low Interest, Low Power**: May notice change but unlikely to act. **Priority: Monitor** with minimal engagement.\n\n**4. Investors — High Interest, High Power**: They have funded the expansion and have a direct say in major decisions. **Priority: Manage closely** — frequent updates, involvement in key decisions."
      },
      {
        type: "short",
        marks: 10,
        prompt: "Explain the importance of prioritising different stakeholder interests when making decisions in a business.",
        model: "**1. Improves decision-making quality**: Mapping forces the business to look at all viewpoints before making a decision. This means choices balance the needs, concerns and power of different groups, leading to fewer disputes and better outcomes. For example, a bank may delay a rural branch closure after mapping shows older customers with low digital access would be heavily impacted.\n\n**2. Supports strategic planning**: Stakeholder mapping helps plan long-term actions by clarifying who to engage and when, reducing surprises. For example, during expansion a company maps which stakeholders — such as local councils or investors — to involve early to smooth the path."
      },
      {
        type: "tf",
        marks: 2,
        prompt: "On a Power–Interest grid, stakeholders with high power and high interest should receive minimal attention from management.",
        model: "False. Stakeholders with high power and high interest should be 'managed closely' — they are the most important group and require frequent communication and involvement in decisions.",
        correct: false
      }
    ];
  })();

  // ── ch6: Enterprise in Action ─────────────────────────────────────────────
  (function () {
    var c = ch("ch6");
    // 6.1 — Innovation, intrapreneurship & entrepreneurship — and importance of innovation
    c.learningOutcomes[0].notes = [
      {
        h: "Distinguish between innovation, entrepreneurship, and intrapreneurship.", b: "**Innovation**: Coming up with something new or better — a product, service, process, way of selling, or way of earning revenue. **Intrapreneur**: An employee who brings new ideas to life within an existing business; takes no personal financial risk but acts creatively. **Entrepreneurship**: When someone takes personal/financial risk to create or grow a business or social enterprise."
      },
      {
        h: "Provide examples of an entrepreneur, an intrapreneur, and an innovation.",
        b: "**Entrepreneur**: Hannah Joyce setting up Flexera (home pilates equipment). **Intrapreneur**: A SuperValu deli team member proposing a 'grab & go breakfast box' that gets rolled out. **Innovation**: Netflix moving from DVDs to streaming."
      },
      {
        h: "What are the different motives for starting an enterprise?", b: "**Personal motives**: Be your own boss, need for achievement, redundancy. **Financial motive**: Earn more income. **Societal motive**: Solve a social problem (e.g. We Make Good)."
      },
      {
        h: "What is the importance of innovation for businesses?", b: "1. **Gain competitive advantage** — stand out with better/cheaper/unique products. 2. **Expand into new markets** — digital tools reach global customers. 3. **Improve efficiency** — AI/automation reduce costs and speed up delivery."
      },
      {
        h: "What is the importance of innovation for the economy?", b: "1. **Drives economic growth** — more productivity, GDP, tax revenue. 2. **Creates jobs** — new industries (green tech, digital health), regional employment. 3. **Boosts exports** — Irish solutions to global problems (e.g. LetsGetChecked)."
      },
      {
        h: "What is the importance of innovation for society?", b: "1. **Solves social challenges** — homelessness, addiction, digital exclusion. 2. **Supports environmental goals** — circular packaging, sustainable production. 3. **Empowers communities** — provides tools, funding, support to solve local problems."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "mcq",
        marks: 4,
        prompt: "An engineer at Sony, Ken Kutaragi, met initial resistance for his idea to create a console to rival Nintendo. He convinced Sony to fund it and the PlayStation launched in 1994. This is an example of:",
        model: "Intrapreneurship — Kutaragi was an employee who developed a new idea inside an existing business, without taking personal financial risk.",
        options: [
          "Entrepreneurship",
          "A circular economy",
          "Intrapreneurship",
          "A franchise"
        ],
        correct: 2
      },
      {
        type: "short",
        marks: 6,
        prompt: "Distinguish between innovation, entrepreneurship and intrapreneurship, with one example of each.",
        model: "**Innovation** is coming up with something new or better — a product, service or process. *Example*: Netflix switching from DVD rental to streaming.\n\n**Entrepreneurship** is when someone takes personal or financial risk to create or grow a business. *Example*: Hannah Joyce setting up Flexera, a pilates equipment business.\n\n**Intrapreneurship** is when an employee brings new ideas to life within an existing business, without taking personal financial risk. *Example*: A SuperValu deli employee proposing the 'grab & go breakfast box' that was rolled out across stores."
      },
      {
        type: "short",
        marks: 9,
        prompt: "Outline three benefits of innovation for the Irish economy.",
        model: "**1. Drives economic growth**: Innovation increases business productivity and GDP, generating more tax revenue that funds public services like healthcare and education.\n\n**2. Creates jobs**: New industries such as green tech and digital health offer future-proof careers and regional employment, reducing reliance on traditional sectors.\n\n**3. Boosts exports**: Irish innovations can solve global problems and earn foreign income — for example, LetsGetChecked exports its at-home diagnostic services internationally, strengthening Ireland's global business reputation."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Outline two reasons, other than financial motives, why someone might start their own enterprise.",
        model: "**1. To be their own boss**: They want control, independence and the ability to make all decisions about how the business is run.\n\n**2. To solve a social problem**: They want to tackle inequality, support sustainability or create ethical products — for example, We Make Good employs vulnerable groups in Dublin."
      }
    ];
    // 6.2 — Competencies of innovators
    c.learningOutcomes[1].notes = [
      {
        h: "What are competencies?", b: "Competencies are the integration of knowledge, skills, values and dispositions that support and foster innovation."
      },
      {
        h: "What are key competencies?",
        b: "**Risk-Taker** — takes personal and financial risks. **Creative** — thinks outside the box, generates new ideas, spots gaps. **Decision-making** — analyses data, consults others, makes good choices under pressure. **Proactive** — uses initiative to seize opportunities, doesn't wait. **Realistic** — sees situations as they are without bias. **Resilient** — determined to overcome failure. **Human Relations** — communicates well, builds networks. **Independent** — confident making decisions without constant reassurance. **Flexible** — adapts to change and feedback. **Time Management** — prioritises tasks and uses resources efficiently."
      },
      {
        h: "How do competencies differ in importance between the start-up and expansion phases of a business?", b: "**Risk-taking** is essential when entering uncertain markets. **Creative thinking** helps develop unique products. **Resilience** keeps the entrepreneur going through early failures. **Flexibility** is vital in fast-changing markets during growth. **Time management** matters when juggling responsibilities in early-stage businesses."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 4,
        prompt: "Identify four key competencies that innovators such as a successful Irish entrepreneur possess.",
        model: "**1. Risk-Taker** — willing to take personal and financial risks to pursue an idea.\n**2. Creative** — thinks differently, generates new ideas, sees gaps in the market.\n**3. Decision-making** — analyses data, consults the right people and makes good choices under pressure.\n**4. Proactive** — uses initiative to seize opportunities and does not wait to respond."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Identify one competency of innovators and outline its importance when starting or expanding a business.",
        model: "**Resilience**: Resilient innovators don't give up easily and are determined to overcome setbacks.\n\nThis competency is vital when starting or expanding a business because new and growing businesses face many early failures — products may not sell, funding may be refused, or customers may be slow to commit. A resilient entrepreneur keeps adjusting their approach and pushing forward instead of giving up, which gives the business the best chance of long-term success."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "Which competency best describes someone who builds strong networks and communicates effectively to gain support and funding?",
        model: "Human Relations is the competency of building networks and communicating well — this supports funding, loyalty and team-building.",
        options: [
          "Independent",
          "Human Relations",
          "Time Management",
          "Realistic"
        ],
        correct: 1
      }
    ];
    // 6.3 — Role of government in supporting enterprise
    c.learningOutcomes[2].notes = [
      {
        h: "How does government create a positive business climate?", b: "**Planning**: Stable budgets and wage agreements encourage investment. **Capital Expenditure**: Spending on infrastructure (roads, schools) creates jobs and demand. **Current Expenditure**: Increases in public sector pay and welfare boost disposable income and sales. **Taxation/Funding**: Low corporation tax, tax breaks and grants. **Education & Training**: Investment in SOLAS and free third-level education builds skilled labour."
      },
      {
        h: "What are Local Enterprise Offices (LEOs) and what support do they provide?", b: "Promote entrepreneurship locally and support start-ups/small businesses. Services: **Training** (online and in-person, e.g. Start Your Own Business), **Mentoring** (1-on-1 with experienced mentors), **Financial support** (Feasibility and Expansion grants; loans up to €50,000 via Microfinance Ireland), **Networking** events."
      },
      {
        h: "What are the other local supports available to entrepreneurs in Ireland?", b: "**Microfinance Ireland**: Loans of €2,000–€50,000 for businesses unable to get bank funding. **Leader**: Funds rural job-creation and sustainability projects. **SOLAS**: Training and education for the labour market. **Area Partnership Companies (APCs)**: Support local entrepreneurs solving community problems."
      },
      {
        h: "What is Enterprise Ireland and what support does it provide to growing businesses?", b: "Government agency for Irish-owned businesses aiming to grow internationally (10+ employees, exporting/scaling). Services: **Funding** (grants and equity); **30+ International Offices**; **R&D support**; **Market Research Centres**; **Trade fairs and missions abroad**."
      },
      {
        h: "What is National Enterprise Hub?", b: "Launched in 2024. One-stop shop centralising 180+ supports from 19+ state bodies. Personalised help via web, phone or live chat."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Discuss three ways the Irish government can support businesses such as a tech start-up. (3 @ 4m)",
        model: "**1. Local Enterprise Offices (LEOs)**: LEOs offer training, mentoring and grants to start-ups and small businesses. A tech start-up could access the 'Start Your Own Business' programme and apply for a Feasibility Grant to test whether their idea is viable.\n\n**2. Enterprise Ireland**: Once the start-up grows, EI provides equity investment, R&D supports and access to over 30 international offices. This helps the start-up scale into export markets and connect with overseas buyers.\n\n**3. Microfinance Ireland**: For businesses that cannot access traditional bank loans, Microfinance Ireland provides loans of between €2,000 and €50,000. This is especially useful for tech start-ups that have limited assets to use as collateral."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Describe two supports the Irish government can provide to a new entrepreneur.",
        model: "**1. Mentoring through the LEO**: The Local Enterprise Office matches the entrepreneur with an experienced mentor for one-on-one support in business planning, strategy, finance and market research, helping them avoid common early mistakes.\n\n**2. Feasibility Grants**: The LEO provides Feasibility Grants to help the entrepreneur research and test whether their idea is viable before investing significant amounts of their own money — this reduces risk and improves chances of success."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Name one state agency, other than Enterprise Ireland, that supports business and enterprise in Ireland and explain how it supports new business start-ups.",
        model: "**Microfinance Ireland**: Supported by the Irish government, it assists businesses struggling to secure a loan from a traditional lender. It offers loans of between €2,000 and €50,000 to new and expanding businesses that cannot access bank funding. This investment supports start-ups by providing the working capital they need to launch — for things like buying stock, equipment or marketing — improving their cashflow and chances of survival in the early stages."
      },
      {
        type: "tf",
        marks: 2,
        prompt: "Enterprise Ireland focuses primarily on supporting Irish-owned businesses that are looking to expand internationally.",
        model: "True. Enterprise Ireland supports Irish-owned businesses with 10+ employees that are looking to expand exports, scale operations and innovate for long-term success.",
        correct: true
      }
    ];
  })();

  // ── ch7: Idea Development ─────────────────────────────────────────────────
  (function () {
    var c = ch("ch7");
    // 7.1 — Factors impacting idea development
    c.learningOutcomes[0].notes = [
      {
        h: "What are internal sources of business ideas?",
        b: "**Hobbies & Interests** (Dyson founder created bagless vacuum from frustration). **Skills & Experience**. **Invention & R&D**. **Brainstorming** (no idea off limits). **Intrapreneurship** (Sony's Ken Kutaragi developing PlayStation)."
      },
      {
        h: "What are the external sources of business ideas?", b: "**Customers** — asking what people want. **Competitors** — improving or localising what works elsewhere. **Market Research** — surveys, interviews, social listening. **Import Substitution** — homegrown alternative to imported product."
      },
      {
        h: "What factors influence idea development?",
        b: "**Organisational Culture** — leadership shapes willingness to share ideas (Steve Jobs, Apple). **Availability of Resources** — time/funding/skills (Google's 20% time). **Market Trends & Consumer Behaviour** (move from plastic → eco-friendly products). **Technological Advancements** (smartphones enabled Deliveroo, Just Eat). **Legal Requirements** — outdated laws can block ideas (modular homes need legal change)."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Determine four factors that impact on the development of business ideas.",
        model: "**1. Organisational Culture**: A leadership style that encourages risk-taking and creativity (e.g. Apple under Steve Jobs) helps new ideas emerge from within the business.\n\n**2. Availability of Resources**: Without time, funding or skilled people, ideas struggle to develop. Google encourages innovation by giving employees 20% of their time to work on new concepts.\n\n**3. Market Trends and Consumer Behaviour**: Shifts in customer habits create opportunities — for example, the move away from single-use plastic opened the market for eco-friendly products like paper straws.\n\n**4. Technological Advancements**: New technology unlocks entire industries — smartphones enabled app-based services like Deliveroo and Just Eat that simply weren't profitable before."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Outline two internal sources from which a business idea may come.",
        model: "**1. Hobbies and Interests**: Ideas can emerge from personal passion or solving problems the entrepreneur has experienced. Dyson's founder invented the bagless vacuum out of frustration with his own vacuum cleaner.\n\n**2. Brainstorming**: Team-based idea generation where no idea is off-limits. This combines different perspectives within the business and can spark innovative ideas."
      }
    ];
    // 7.2 — Design thinking — iterative, person- and solution-centred
    c.learningOutcomes[1].notes = [
      {
        h: "What is design thinking?", b: "An innovative, non-linear approach to developing products and services that focuses on solutions for the end user."
      },
      {
        h: "What are the three key characteristics of design thinking?",
        b: "**Person-centred**: Understands the user's real problems and empathises before designing solutions. **Solution-centred**: Defines the problem clearly and explores creative ways to solve it, beginning with the desired outcome. **Iterative**: Repeated cycles of prototyping, testing, refining and retesting until a practical, user-approved solution emerges."
      },
      {
        h: "What are the four phases of the design thinking process?",
        b: "**1. Clarify** — gain a deep understanding of the current problem from the user's perspective (surveys, observation, research). **2. Ideate** — creative brainstorming sessions to explore multiple potential solutions. **3. Develop** — turn top ideas into early prototypes (sketches or first working models) to test functionality. **4. Implement** — test prototypes with real users, gather feedback, refine repeatedly."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Outline how a business can use each of the four phases of design thinking to successfully develop a new product. (4 @ 3m)",
        model: "**1. Clarify**: The business gains a deep understanding of the user's problem through surveys, observation and interviews — for example, asking parents what frustrates them about existing kids' products.\n\n**2. Ideate**: Hold creative brainstorming sessions to explore multiple solutions, with no idea ruled out at this stage.\n\n**3. Develop**: Turn the strongest ideas into early prototypes — sketches or basic working models — to test how they look and function.\n\n**4. Implement**: Test prototypes with real users, gather feedback and refine repeatedly until the product meets users' needs and is ready to launch."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain what is meant by design thinking being 'person-centred', 'solution-centred' and 'iterative'.",
        model: "**Person-centred**: It focuses on understanding the real problems of the end user and empathising with them before generating solutions, so the design genuinely meets user needs.\n\n**Solution-centred**: The process clearly outlines the problem the product or service will solve from the start and explores creative ways to deliver the desired outcome.\n\n**Iterative**: The process uses repeated cycles of prototyping, testing, refining and retesting — re-visiting earlier steps again and again until a user-approved solution emerges."
      }
    ];
    // 7.3 — Conducting a feasibility study
    c.learningOutcomes[2].notes = [
      {
        h: "What is a feasibility study?",
        b: "A check on whether an idea is workable, profitable and sustainable before investing time and money. Doing this early saves resources and helps avoid launching something that won't succeed."
      },
      {
        h: "What are the key areas of feasibility to assess when evaluating a business idea?", b: "**Financial**: Cost to start/run vs expected income; break-even, startup costs. *Can it make a profit?* **Market**: Is there demand? Surveys, interviews assess market size. *Will customers want it?* **Production**: Can it be built/delivered with available resources, skills, equipment? *Can we make it?* **Legal**: Does it meet current laws/regulations? *Are there any legal obstacles?* **Environmental**: Impact on environment, sustainability, materials, emissions, waste. *Will it meet environmental standards?*"
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 5,
        prompt: "Explain one function of a feasibility study when developing a new business idea.",
        model: "**Tests financial feasibility**: A feasibility study estimates the start-up costs, ongoing costs and expected income, and calculates whether the business can reach a break-even point and earn a profit. This allows the entrepreneur to know whether the idea is financially viable before committing significant time and money — saving resources if the idea cannot make money, or strengthening the case for funding if it can."
      },
      {
        type: "short",
        marks: 12,
        prompt: "Outline four areas a business should assess when conducting a feasibility study on a new product idea. (4 @ 3m)",
        model: "**1. Market Feasibility**: Researches whether customers actually want the product through surveys and interviews, and assesses market size and competitors. Key question: Is there real demand?\n\n**2. Financial Feasibility**: Compares the cost to start and run the business with expected income, calculating break-even and required cash. Key question: Can it make a profit?\n\n**3. Production Feasibility**: Assesses whether the product can actually be built or delivered with available skills, equipment and technology. Key question: Can we make it?\n\n**4. Legal Feasibility**: Checks if the idea meets current laws and regulations or if there are planning, safety or industry rules that would block it. Key question: Are there any legal obstacles?"
      },
      {
        type: "tf",
        marks: 2,
        prompt: "Environmental feasibility looks at whether a business idea aligns with sustainability goals and meets environmental standards.",
        model: "True. Environmental feasibility assesses the potential impact on the environment — including materials, emissions, energy use and waste — and whether the idea aligns with sustainability expectations.",
        correct: true
      }
    ];
  })();

  // ── ch8: Business Planning ────────────────────────────────────────────────
  (function () {
    var c = ch("ch8");
    // 8.1 — Importance and key functions of a business plan
    c.learningOutcomes[0].notes = [
      {
        h: "What is a business plan?", b: "A written document that outlines what a business wants to achieve and how it will achieve it. It clarifies the idea, sets goals, attracts funding, assesses market size, and identifies risks."
      },
      {
        h: "What are the sections of a business plan?", b: "**1. Executive Summary** — short persuasive overview of the business, why it will succeed, key financials. **2. Market Analysis** — trends, competitors, target market. **3. Sales & Marketing** — how the business will reach the target market and drive sales. **4. Financial Plan** — projected income, costs (fixed/variable), cash flow forecasts, profit. **5. Production Plan** — how goods/services will be produced, machinery, timelines. **6. Operational Plan** — daily operations, staffing, stock, working hours. **7. Business Model Canvas** — one-page summary of how value is created and delivered (9 boxes)."
      },
      {
        h: "What is the importance of business plans at different stages?", b: "**Start-up**: Clarifies idea and value proposition, secures early funding. Key sections: Executive Summary, Market Analysis, BMC, Financial Plan. **Growth/Expansion**: Guides expansion decisions, shows growth potential. Key sections: Sales & Marketing, Financial Plan (revised). **Maturity**: Supports day-to-day efficiency and long-term planning. Key sections: Operational Plan, Production Plan, Financial Plan."
      },
      {
        h: "What is a value proposition?",
        b: "A short, clear statement explaining what a product/service is, who it is for, and the range of benefits that make it better than alternatives. Example (All Real Nutrition): 'A bar high in protein and made from real, natural ingredients while supporting Irish suppliers and sustainability, with zero plastic packaging.'"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline four key functions of a business plan.",
        model: "**1. Clarifies the business idea** — Forces the entrepreneur to think through how the business will work, including its value proposition.\n\n**2. Helps secure funding** — Banks, investors and the LEO use the plan to assess whether to lend or invest.\n\n**3. Sets goals and benchmarks** — Sales, profit and growth targets allow the business to measure performance.\n\n**4. Identifies risks and challenges** — The planning process forces the business to think about competitors, costs and potential threats so they can prepare contingency plans."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Explain how a business plan can contribute to the success of a new business.",
        model: "A business plan contributes to success in several connected ways. First, it forces the entrepreneur to clarify the value proposition and confirm that customers want the product, reducing the risk of launching an unviable idea. Second, the financial plan within it (with projected costs, sales and cashflow) is essential to securing finance from banks, investors or the LEO. Finally, it provides clear goals against which the business can benchmark performance — for example, monthly sales targets — allowing it to spot problems early and make timely adjustments."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "Which section of the business plan provides a short persuasive overview, including key financial highlights and reasons the business will succeed?",
        model: "The Executive Summary is the short, persuasive overview at the start of the plan.",
        options: [
          "Market Analysis",
          "Operational Plan",
          "Executive Summary",
          "Production Plan"
        ],
        correct: 2
      }
    ];
    // 8.2 — Ethics and sustainability in business planning
    c.learningOutcomes[1].notes = [
      {
        h: "Why do ethics and sustainability matter in business planning?", b: "**1. Builds trust and brand loyalty** — customers value businesses that stand for more than profit (highlighted in Executive Summary and Sales & Marketing sections). **2. Helps attract investment** — many investors apply ESG criteria (Environmental, Social, Governance). Businesses that demonstrate responsible practice in the Financial Plan and Risk sections are more likely to secure funding. **3. Avoids legal and reputational risks** — planning compliance into the Operations and Production Plans reduces the risk of fines, scandals and reputation damage. **4. Supports long-term profitability** — businesses with ethics built into their Financial Plan are more resilient and adaptable to changing regulations and customer expectations."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Outline three benefits to a business of incorporating ethics and sustainability into its business planning. (3 @ 4m)",
        model: "**1. Builds Trust and Brand Loyalty**: When ethical values and sustainability goals are highlighted in the Executive Summary and Sales & Marketing sections, customers see the business stands for more than profit. This builds long-term loyalty and brand advocacy.\n\n**2. Helps Attract Investment**: Modern investors often apply ESG (Environmental, Social, Governance) criteria. Businesses showing responsible practices in their Financial Plan and Risk sections are more likely to secure funding and long-term backing.\n\n**3. Supports Long-Term Profitability**: Sustainable businesses are more resilient to changing regulations, resource constraints and customer expectations — helping them stay competitive over the long run."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Outline how sustainability planning can reduce risks for a business.",
        model: "Building sustainability into the Operations Plan and Production Plan reduces the chance that the business will breach environmental laws, face fines or be linked to unethical behaviour. For example, sourcing from certified suppliers ensures compliance with regulations and protects against scandals that could be costly to recover from. By planning compliance from the outset, the business reduces both legal risk and reputational damage."
      }
    ];
    // 8.3 — What a business model is and its role in the business plan
    c.learningOutcomes[2].notes = [
      {
        h: "Define Definition.", b: "A business model is an element within the business plan that outlines how a company will operate, create, deliver and capture value."
      },
      {
        h: "What is the role of the business model in explaining how a business operates?", b: "It explains how a business will: **1. Create value** — the product/service that solves a problem. **2. Deliver value** — how it reaches and serves customers. **3. Earn revenue** — one-off, subscription, ads, etc. Example: Spotify creates value through music streaming, delivers it via an easy-to-use app, and earns revenue through subscriptions and ads."
      },
      {
        h: "What are examples of business models?",
        b: "Retail (Penneys, Zara), Marketplace (Airbnb, DoneDeal), Franchise (Supermac's, McDonald's), Subscription (Netflix, Spotify, Adobe)."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 5,
        prompt: "Explain what is meant by a 'business model' and describe its role within a business plan.",
        model: "A **business model** outlines how a company will operate, create, deliver and capture value. Within the business plan, it explains the three core questions: how the business creates value (the product or service that solves a customer problem), how it delivers value (how it reaches and serves the customer), and how it earns revenue (one-off sales, subscription, advertising, commission, etc.). For example, Spotify creates value through music streaming, delivers it via its easy-to-use app, and earns revenue through subscriptions and ads. The business model gives investors and the entrepreneur a clear understanding of how the business will make money."
      }
    ];
    // 8.4 — Business Model Canvas (BMC)
    c.learningOutcomes[3].notes = [
      {
        h: "What is this tool?", b: "A one-page tool used to map out a business model on 9 connected building blocks."
      },
      {
        h: "What are the 9 elements?",
        b: "**1. Key Partners** — suppliers, software providers, couriers, producers. **2. Key Activities** — design, marketing, customer service. **3. Key Resources** — IP, patents, key staff, premises. **4. Value Proposition** — the 'why' a customer would choose this product/service. **5. Customer Relationships** — managing interactions (social media, in-store). **6. Customer Segments** — target market and other groups served. **7. Customer Channels** — how the customer is reached (online, store, email). **8. Revenue Streams** — how income is earned (sales, subscription, ads). **9. Cost Structure** — fixed and variable costs of running the business."
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 9,
        prompt: "Identify three key elements of the Business Model Canvas and explain the role of each.",
        model: "**1. Value Proposition**: The bundle of benefits a product or service offers customers — the 'why' a customer would choose this business over alternatives. It is the heart of the BMC, with all other elements supporting it.\n\n**2. Revenue Streams**: How the business generates income — direct sales, recurring subscriptions, advertising, commission, etc. This shows how the business will sustain itself financially.\n\n**3. Key Partners**: External organisations the business relies on — suppliers, software providers, logistics firms. These ensure the business can deliver its value proposition smoothly to customers."
      },
      {
        type: "tf",
        marks: 2,
        prompt: "The Business Model Canvas summarises the business model on a single page across nine sections including Key Partners, Value Proposition and Revenue Streams.",
        model: "True. The BMC is a one-page summary across 9 building blocks.",
        correct: true
      }
    ];
    // 8.5 — Common business models
    c.learningOutcomes[4].notes = [
      {
        h: "What is the retail business model and how does it create value?", b: "Buys at wholesale prices and sells higher to consumers, online or in-store (Dunnes, Lifestyle Sports). Value: convenience, choice, loyalty rewards (Tesco Clubcard)."
      },
      {
        h: "What is the manufacturing business model and what value does it create?", b: "Makes goods from raw materials and sells to retailers (B2B — Intel) or directly to consumers (B2C — Nike.com). Value: innovation, efficiency through cost-effective production."
      },
      {
        h: "What is the subscription business model and what value does it provide to customers?", b: "Recurring payments — monthly or annual (Sky TV, Virgin broadband). Value: continuous access, customisation, flexibility to cancel."
      },
      {
        h: "What is a franchise?",
        b: "Franchisor licenses brand, logo, systems, products to franchisees in exchange for fees and a % of revenue/profits (McDonald's, Insomnia Coffee). Value: brand consistency, increased availability across locations."
      },
      {
        h: "What is the affiliate business model and how do affiliates generate revenue?", b: "Affiliates earn commission when their content drives a sale (TikTok influencers promoting Gymshark, Amazon links). Value: leverages influencer trust and targeted marketing."
      }
    ];
    c.learningOutcomes[4].questions = [
      {
        type: "short",
        marks: 5,
        prompt: "Describe the franchise business model.",
        model: "In a **franchise**, the franchisor grants a licence to a franchisee to operate branches under the franchisor's brand, logo, systems and products. The franchisee pays an upfront fee plus an ongoing percentage of revenue or profits. *Example: McDonald's, Insomnia Coffee*. Value is created through brand consistency — customers receive a familiar product across all locations — and through increased availability, as the brand can scale quickly through the franchisees' investment."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Compare the retailer and manufacturer business models, referring to how each generates revenue.",
        model: "**Retailers** buy products at wholesale prices from suppliers/manufacturers and sell them at a higher price (markup) to consumers, either online or in-store (e.g. Dunnes Stores). Their revenue comes from the margin between buying and selling price, and they create value through convenience, choice and loyalty schemes.\n\n**Manufacturers** make goods from raw materials and sell them at a profit, either to retailers (B2B — e.g. Intel selling chips to Dell) or directly to consumers (B2C — e.g. Nike.com). Their revenue comes from converting cheaper inputs into higher-value finished goods. They create value through innovation and efficient production allowing competitive pricing."
      }
    ];
    // 8.6 — Digital technology as a driver of change
    c.learningOutcomes[5].notes = [
      {
        h: "What are the internal change drivers that digital technology creates for businesses?", b: "**1. Innovation & Product Development** — apps and social media for personalised shopping (ASOS). **2. Efficiency & Automation** — robots and inventory systems (Amazon). **3. Data-Driven Decisions** — Netflix uses AI to track viewing and choose new shows. **4. Employee Collaboration** — Slack, Notion enable global teamwork."
      },
      {
        h: "What are the external change drivers that digital technology creates for businesses?", b: "**5. Changing Consumer Behaviour** — convenience, personalisation, speed (Gymshark uses TikTok feedback). **6. Competitive Pressure** — digital-first disruptors (Uber forced taxi firms to launch apps). **7. Globalisation** — Shein uses digital payments and translation tools. **8. Brand Image and Public Engagement** — Ryanair shapes brand using humour and social trends."
      }
    ];
    c.learningOutcomes[5].questions = [
      {
        type: "short",
        marks: 9,
        prompt: "Outline three ways digital technology drives change in business.",
        model: "**1. Efficiency and Automation**: Businesses automate processes using AI and robotics to save time, cut costs and reduce errors. Amazon uses warehouse robots and automated inventory systems to fulfil orders much faster than manual workers could.\n\n**2. Data-Driven Decisions**: Businesses can collect and analyse huge amounts of customer data in real time. Netflix uses AI to track viewing habits and decide which new shows to produce and recommend, increasing both engagement and retention.\n\n**3. Changing Consumer Behaviour**: Digital platforms have raised customer expectations for speed, personalisation and convenience. Gymshark uses TikTok to get rapid feedback on products and adjust quickly — businesses that don't adapt risk losing customers to digital-first rivals."
      }
    ];
    // 8.7 — Technology-driven business models
    c.learningOutcomes[6].notes = [
      {
        h: "What is the marketplace business model and how does it generate revenue?", b: "**Revenue**: Charges fees or commission on transactions between buyers and sellers. **Access/Cost**: Usually free for users; sellers may pay listing fees. **Scalability**: Highly scalable — no need to own stock/property; grows as users join. **Engagement**: Reviews, ratings, personalised suggestions build trust."
      },
      {
        h: "What is the subscription-based technology business model?", b: "**Revenue**: Recurring monthly or annual payments; some offer ad-supported tiers. **Access/Cost**: Customers pay for continued access; freemium offers limited free access with paid upgrades. **Scalability**: Highly scalable globally without major infrastructure costs. **Engagement**: Personalised content (Spotify playlists, Netflix recommendations) and exclusive features keep users subscribed."
      },
      {
        h: "What is the crowdfunding business model and how does it support new ventures?", b: "**Revenue**: Many small contributions raised online before product launch. **Access/Cost**: Free to browse; backers contribute in return for rewards or early access. **Scalability**: Campaigns can go viral globally without big budgets; low overhead. **Engagement**: Updates, reward tiers and storytelling build community support."
      },
      {
        h: "What is the advertising-supported business model?", b: "**Revenue**: Advertisers pay based on views, clicks or impressions; premium ad-free options (YouTube Premium). **Access/Cost**: Free for consumers; revenue earned indirectly through ads. **Scalability**: Extremely scalable — more users means more ad reach. **Engagement**: Algorithms personalise content to maximise time on platform and ad exposure."
      },
      {
        h: "How do technology-driven business models differ from traditional non-digital models?", b: "Tech-driven models bring 24/7 access, easier cancellation, personalisation, lower scaling costs, global reach and direct funding from public — without needing physical stores or big advertising budgets."
      }
    ];
    c.learningOutcomes[6].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Explain two key characteristics of each of the following technology-driven business models: (i) Subscription and (ii) Advertising-supported.",
        model: "**(i) Subscription** (e.g. Netflix, Spotify):\n• **Recurring revenue** — Customers pay regular monthly or annual fees, providing predictable, ongoing income for the business.\n• **High scalability** — Digital delivery means new users can be added globally at very little extra cost compared to traditional services.\n\n**(ii) Advertising-supported** (e.g. TikTok, YouTube):\n• **Indirect revenue** — Consumers access content for free; revenue comes from advertisers paying for views, clicks or impressions.\n• **Algorithm-driven engagement** — Personalised content keeps users on the platform for longer, increasing the value of advertising space."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Explain the term 'crowdfunding'.",
        model: "**Crowdfunding** is a technology-driven business model where a business raises small amounts of money from a large number of individuals online, typically before a product or service is launched. Backers may contribute in exchange for rewards, early access to the product, or equity. Platforms like Kickstarter and Fundit.ie allow campaigns to go viral and reach a global audience without large marketing budgets, while also building an early community of customers."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Compare a subscription service with another technology-driven business model under the headings (i) Revenue Generation and (ii) Scalability.",
        model: "**(i) Revenue Generation**:\n• Subscription (Spotify) — earns recurring monthly or annual fees from users for continuous access.\n• Marketplace (Vinted) — charges a fee or commission on each transaction between buyers and sellers; revenue depends on transaction volume rather than fixed payments.\n\n**(ii) Scalability**:\n• Subscription — Highly scalable as digital delivery means more users add little extra cost; can grow globally quickly.\n• Marketplace — Also highly scalable as platforms grow as more users join; no need to own additional stock or property, but it relies on attracting a critical mass of both buyers and sellers."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "Match the following: 'A platform earns commission on transactions between buyers and sellers without holding inventory'.",
        model: "Marketplace — connects buyers and sellers and earns a commission per transaction.",
        options: [
          "Subscription",
          "Marketplace",
          "Crowdfunding",
          "Advertising-supported"
        ],
        correct: 1
      }
    ];
  })();

  // ── ch9: The Target Market ────────────────────────────────────────────────
  (function () {
    var c = ch("ch9");
    // 9.1 — Importance of market research and identifying the target market
    c.learningOutcomes[0].notes = [
      {
        h: "What is meant by target market?", b: "The specific segment or group of customers a business is trying to sell to, defined by characteristics like age, gender, income, location, lifestyle and interests."
      },
      {
        h: "Why is identifying the target market important for a business?", b: "**1. Stronger brand identity** — name, logo and tone match customer preferences (Mooju → 16–24 year-old males). **2. Better product design** — tailored to needs (Nobó dairy-free ice cream). **3. Smarter marketing choices** — best platforms and messages (Chupi uses Instagram for fashion-conscious customers). **4. Improved customer loyalty** — meeting expectations builds trust (SuperValu adapts ranges to local communities)."
      },
      {
        h: "What are the main types of market segmentation?", b: "Dividing a market into smaller groups with common characteristics. Types: **Demographic** (age, gender, income, family size); **Geographical** (county, region, country); **Behavioural** (attitudes, usage habits — impulse buying, value seekers); **Psychological** (lifestyle/personality — health-conscious, ethical, sustainable)."
      },
      {
        h: "What are the key reasons a business should conduct market research?", b: "1. **Estimate market size and trends**. 2. **Analyse competitors**. 3. **Shape the marketing mix** (price, promotion, etc.). 4. **Test and improve products** to reduce launch risk."
      },
      {
        h: "What is field research and what are its advantages and disadvantages?", b: "First-hand info collected directly. Methods: **Surveys** (questions to customers), **Observation** (watching behaviour), **Customer Feedback** (smiley buttons, ratings), **Focus Groups** (small in-depth discussions). *Advantages*: most up-to-date, highly specific. *Disadvantages*: expensive, time-consuming."
      },
      {
        h: "What is desk research and what are its sources, advantages and disadvantages?",
        b: "Existing information collected by others. Sources: **Internal Reports** (past sales, customer records), **Government Publications** (CSO data), **Online Sources** (websites, social media, reviews), **Industry Reports**. *Advantages*: quick, low-cost, accessible, useful for trend analysis. *Disadvantages*: may be outdated, not specific to the business, doesn't always show 'why'."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Discuss two types of market research a business may use before expanding.",
        model: "**1. Field Research (Primary)**: The business collects new, first-hand information from customers using methods like surveys, focus groups and observation. For expansion, this is highly relevant — for example, surveying potential customers in a new region tells the business if there is genuine demand for its product. The data is up-to-date and tailored, though it can be expensive and time-consuming.\n\n**2. Desk Research (Secondary)**: The business uses existing information already collected by others — internal sales records, CSO population/income data, online reviews, or industry reports. This is fast and cheap and is useful for spotting broad trends and comparing markets. However, the data may be outdated or not specific to the business's exact needs."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Outline four reasons why a business should carry out market research.",
        model: "**1. Estimate market size and trends** — to understand if a market is growing and what its key characteristics are.\n\n**2. Analyse competitors** — to reveal rivals' strengths and weaknesses and improve competitive positioning.\n\n**3. Shape the marketing mix** — to guide decisions on product design, pricing, promotion and sales strategy.\n\n**4. Test and improve products** — to find out what customers value, reducing the risk of launching a product that fails."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Identify the intended target market for a heavily branded, high-protein bar with bold packaging and explain how you would justify your choice based on the marketing mix.",
        model: "**Target market**: Health-conscious adults aged 18–35, particularly those interested in fitness, the gym or sport.\n\n**Justification using the marketing mix**: The bold, branded packaging and use of macros/protein content as a key claim signals **Product/Promotion** is aimed at fitness-oriented customers who care about nutritional information. The premium pricing typical of these products signals **Pricing** aimed at adults with disposable income rather than children or budget-conscious shoppers. The likely **Place** — health food shops, gyms, supermarket protein aisles — also confirms it is positioned for active, wellness-aware customers."
      }
    ];
    // 9.2 — The 7 P's of the marketing mix
    c.learningOutcomes[1].notes = [
      {
        h: "What are the seven P's of the marketing mix?",
        b: "Product, Price, Promotion, People, Packaging, Process, Place. Each is adjusted to match the target market."
      },
      {
        h: "Product/Service",
        b: "**USP** — the differentiating feature. **Branding** — name, design, logo, slogan ('Just Do It'). **Product Design** — core features, branding, target appeal, quality, sustainability. **Product Life Cycle** — Introduction → Growth → Maturity → Decline. Extend life cycle by adjusting the 7 P's (Pringles: new flavours, bundle deals, expand to airports, influencer campaigns)."
      },
      {
        h: "What factors influence pricing decisions?", b: "Target market (income), Cost of production, Competitor prices, Economic conditions."
      },
      {
        h: "Pricing strategies",
        b: "**Penetration** — low to enter market and gain share (HelloFresh discounts). **Price Skimming** — high then drop (PlayStation launches). **Premium** — high signals luxury (Lululemon). **Cost-Plus** — total cost + markup. **Bundle** — discount when bought together (McDonald's meals). **Tiered** — multiple versions at different prices (Spotify Free/Premium/Family). **Price Discrimination** — different groups (student/senior). **Predatory** — low to eliminate rivals (Amazon underpricing books). **Loss Leader** — sold below cost to attract customers (IKEA hot dogs). **Dynamic** — based on demand/time (Oasis tickets, FIFA World Cup)."
      },
      {
        h: "What are the different types of promotion?", b: "**Advertising**: Informative, Persuasive, Generic, Competitive. Regulated by **ASAI** (Advertising Standards Authority of Ireland). **Public Relations**: press releases, sponsorships, community initiatives, crisis response. **Sales Promotions**: discounts, BOGOF, loyalty cards, competitions. **Direct Marketing**: email, SMS, push notifications, A/B testing. **Digital Marketing**: influencers, viral content. **Personal Selling**: face-to-face/online sales help; AI chatbots (Dell)."
      },
      {
        h: "People",
        b: "Everyone delivering the product/service — staff, drivers, online support. Target market influences who is hired and how they're trained: a youth fashion brand hires TikTok-savvy staff; a luxury hotel trains formal, discreet staff."
      },
      {
        h: "What are the functions of packaging, and how does physical evidence apply to services?", b: "Functions: **Protection** (childproof lids), **Information** (use-by, allergens), **Point of Differentiation** (Pringles tube), **Ethics & Sustainability** (Ballygowan recycled bottles). For services, physical evidence builds trust (restaurant interior, spotless taxi)."
      },
      {
        h: "Process",
        b: "Every step from first contact to after-sales (e.g. Browse → Cart → Checkout → Payment → Delivery → Returns). Smooth process builds trust and repeat purchases. Influenced by target market — e.g. McDonald's kiosks for speed; clear return labels for less tech-savvy customers."
      },
      {
        h: "What is the place element of the marketing mix and what factors influence distribution decisions?", b: "How product/service reaches the customer. Factors: **Cost** (each intermediary takes markup), **Nature of product** (perishable vs luxury), **Market reach** (small brands sell direct online, big brands need retailers). Selling direct: higher margins, lower overheads, full control, customer data — but limited reach. Selling via retailer: large reach, no own store needed — but lower margins and risk of own-brand copies."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 10,
        prompt: "Outline the seven elements of the marketing mix and briefly explain the role of each.",
        model: "**1. Product/Service** — what the business sells; must meet target market needs and have a clear USP.\n**2. Price** — what customers pay; chosen using strategies such as penetration, premium or cost-plus.\n**3. Promotion** — how the product is communicated to customers (advertising, PR, sales promotions, direct/digital marketing, personal selling).\n**4. People** — staff who deliver the product or service and shape the customer experience.\n**5. Packaging** — physical packaging for goods, or physical evidence (e.g. interior design) for services; protects, informs and differentiates.\n**6. Process** — the customer journey from first contact through to after-sales support; should be smooth and convenient.\n**7. Place** — how the product reaches customers (direct, retailer, marketplace, online or offline)."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Outline two ways the target market for a product or service might influence the promotion element of the marketing mix.",
        model: "**1. Choice of platform**: Businesses select where to advertise based on where the target market spends time. A skincare brand targeting Gen Z might use Snapchat ads and short-form TikTok video tutorials, whereas a brand targeting older customers might use radio or print to reach them effectively.\n\n**2. Tone and content of message**: The format of the message is tailored to audience preferences. A retirement investment firm may post brochures with formal language to older adults, while a fashion brand targets young adults via stylised email and Instagram campaigns featuring influencers."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Explain four pricing strategies a business may use, with an example of each.",
        model: "**1. Penetration Pricing** — Low price to enter a market and quickly gain share. *Example*: HelloFresh offered deep discounts to attract first-time users.\n\n**2. Price Skimming** — High initial price to target early adopters, then dropped. *Example*: Sony PlayStation consoles launch at a premium before later cuts.\n\n**3. Premium Pricing** — High price to signal status or quality. *Example*: Lululemon for activewear, Rolex for watches.\n\n**4. Bundle Pricing** — Discount when items are bought together. *Example*: McDonald's meal deals cost less than buying items separately."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Outline four functions of packaging in the marketing mix.",
        model: "**1. Protection** — Protects the product during delivery and storage. *Example*: childproof lids on medicine bottles.\n\n**2. Information** — Includes essential details such as use-by dates, allergens or caffeine content. *Example*: energy drinks display caffeine content clearly.\n\n**3. Point of Differentiation** — Helps the product stand out and be recognisable. *Example*: Pringles' distinctive tube.\n\n**4. Ethics and Sustainability** — Recyclable or ethically sourced packaging boosts appeal to eco-conscious customers. *Example*: Ballygowan bottles made from 100% recycled plastic."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "An online shopping experience taking the customer through Browse → Cart → Checkout → Payment → Delivery is an example of which 'P' in the marketing mix?",
        model: "Process — every step the customer goes through from first contact to after-sales.",
        options: [
          "Place",
          "Process",
          "Packaging",
          "Promotion"
        ],
        correct: 1
      },
      {
        type: "tf",
        marks: 2,
        prompt: "Predatory pricing involves charging temporarily low prices in order to drive competitors out of the market.",
        model: "True. Predatory pricing is a temporary low-price strategy used to eliminate rivals from a market.",
        correct: true
      }
    ];
    // 9.3 — USP analysis for a product/service
    c.learningOutcomes[2].notes = [
      {
        h: "What a USP analysis is",
        b: "It identifies and highlights the unique benefits a business offers that customers desire and competitors don't deliver as well. A business should clarify: 1. What it does well, 2. What customers want, 3. What competitors do well — and build the marketing mix to focus on the overlap of (its strengths + customer wants) that competitors don't offer."
      },
      {
        h: "Worked example — Netflix vs Disney+",
        b: "**Focus on these (Netflix's USP)**: Strong global original content (Squid Game, The Crown, Stranger Things), binge-watching releases, sophisticated recommendation algorithm, broad teen/adult appeal. **Don't bother differentiating on**: HD/4K streaming, offline downloads, profiles — both do these. **Avoid competing on**: exclusive Disney franchises (Marvel, Star Wars, Pixar) where Disney+ is stronger."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Conduct a USP analysis for a product or service of your choice and explain how the marketing mix should focus on the USP identified.",
        model: "**Service example: Spotify vs Apple Music**\n\n**What Spotify does well + what customers want + Apple Music doesn't do as well**:\n• Sophisticated discovery algorithms and personalised playlists like Discover Weekly.\n• Strong free, ad-supported tier as a route into the paid product.\n• Cross-platform availability (works seamlessly on Android, Windows, smart speakers, etc.).\n\n**Implications for the marketing mix**: Spotify should focus its **Promotion** on personalised discovery (e.g. Spotify Wrapped campaigns showcasing year-end personalisation). **Product** should keep investing in algorithms and playlist curation. **Pricing** should retain the freemium tier as a USP. Spotify should avoid promoting features that Apple Music does as well (e.g. high audio quality), and avoid marketing in areas where Apple Music dominates (deep iOS integration)."
      }
    ];
    // 9.4 — Evaluating and improving an existing marketing mix
    c.learningOutcomes[3].notes = [
      {
        h: "How to evaluate",
        b: "Don't just say what to change — explain why. Support suggestions with evidence (customer feedback, trends, competitor moves). Always link back to target market and brand USP. Suggestions should: show clear understanding of the target market, link to current trends (high-protein, sustainability), be realistic for the brand's image and resources, and explain how the change will increase sales/loyalty/reputation."
      },
      {
        h: "Worked example — McDonald's",
        b: "**Evaluation**: Heavy focus on indulgent, high-calorie meals. Promotions centre on value and family deals. Strong McDelivery. **Gap**: nothing for the growing health/protein-conscious segment. **Improvements**: 1. **Product** — Introduce 'MacroChicken Wrap' (35g+ protein, <500 kcal). 2. **Promotion** — Influencer Instagram/TikTok campaigns. 3. **Packaging** — Clean, eco-friendly with QR code linking to nutrition info."
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Evaluate the marketing mix of a business of your choice and recommend two ways it could be improved. (4m evaluation + 4m for each recommendation)",
        model: "**Business: McDonald's Ireland**\n\n**Evaluation**: McDonald's product range is heavily focused on indulgent, high-calorie meals, with limited options for health-conscious customers. Promotions centre on value meals and family-friendly deals rather than wellness trends. The McDelivery service is strong but the menu lacks targeted offerings for the growing market of consumers seeking high-protein, lower-calorie options.\n\n**Recommendation 1 — Product**: Introduce a new 'MacroChicken Wrap' — a grilled chicken wrap with 35g+ protein, added fibre and under 500 calories. This appeals to fitness-conscious Gen Z and millennial customers who currently choose competitors like Subway or coffee shop wraps, expanding McDonald's reach into a profitable segment.\n\n**Recommendation 2 — Promotion**: Run targeted Instagram and TikTok campaigns featuring fitness influencers trialling the MacroChicken Wrap and posting macro breakdowns. This positions the new product as credible to health-aware audiences and reaches them where they spend time, increasing trial rates and shifting brand perception away from purely indulgent food."
      }
    ];
    // 9.5 — Disruptive impact of digital technology on market research and marketing
    c.learningOutcomes[4].notes = [
      {
        h: "What is an Impact on market research?", b: "**Real-time feedback** — online polls, social listening allow instant feedback. **Big Data & AI** — tools analyse vast volumes of search/review/behaviour data faster than traditional research. **More affordable tools** — Google Analytics, Meta Suite open detailed data to small firms, closing the gap with large businesses."
      },
      {
        h: "What is an Impact on marketing?", b: "**More targeted campaigns** — TikTok and Google Ads target by age/interest/habits. **Measurable results** — clicks, sales and views are tracked; A/B testing compares versions. **Creative low-cost options** — memes, influencer content and viral videos let small brands reach huge audiences cheaply, challenging big-budget advertising."
      }
    ];
    c.learningOutcomes[4].questions = [
      {
        type: "short",
        marks: 9,
        prompt: "Demonstrate three ways digital technology has disrupted marketing for businesses.",
        model: "**1. More targeted campaigns**: Platforms like TikTok and Google Ads allow precise targeting by age, interests and behaviour, making marketing more personal and cost-effective than traditional broadcast advertising.\n\n**2. Measurable results**: Digital tools show exact ad performance — clicks, sales, views — and A/B testing compares versions to find what works. This means businesses can refine campaigns in real time based on hard data instead of guessing.\n\n**3. Creative, low-cost options**: Memes, influencer content and viral videos let small brands reach huge audiences on tiny budgets, challenging the dominance of traditional big-budget advertising and giving start-ups a route to market."
      }
    ];
    // 9.6 — Influence of ethics and sustainability on marketing
    c.learningOutcomes[5].notes = [
      {
        h: "Positive influence",
        b: "**Builds trust and loyalty** — Tony's Chocolonely championing fair trade. **Creates powerful marketing stories** — SuperValu's TidyTowns support. **Competitive advantage** — Ballygowan's recycled bottles win eco-conscious customers."
      },
      {
        h: "Challenges",
        b: "**Increased costs** — sustainable materials and ethical sourcing reduce margins. **Risk of greenwashing** — overstating eco-claims without action damages trust (fast fashion brands criticised for 'green' lines while remaining unsustainable). Evaluation: ethics and sustainability build loyalty only when authentic — businesses must align marketing with real action."
      }
    ];
    c.learningOutcomes[5].questions = [
      {
        type: "short",
        marks: 9,
        prompt: "Outline three ways ethics is an important consideration when designing a marketing strategy.",
        model: "**1. Builds trust and customer loyalty**: Customers increasingly support brands that reflect their values. Ethical positioning — like Tony's Chocolonely championing fair trade cocoa — builds a loyal following willing to pay a premium and recommend the brand.\n\n**2. Avoids reputational damage from greenwashing**: Overstating environmental claims without genuine action damages trust quickly when exposed. Marketing must align with real practice, otherwise consumers and regulators (e.g. ASAI) will call out misleading claims.\n\n**3. Creates a competitive advantage**: Genuine ethical and sustainable practice can differentiate a brand. Ballygowan promotes its 100% recycled plastic bottles to win eco-conscious customers in a crowded market — this is a marketing point rivals can't easily copy."
      }
    ];
    // 9.7 — Power-interest grid for customers
    c.learningOutcomes[6].notes = [
      {
        h: "What is the power-interest grid and how can it be used to inform marketing decisions?", b: "A business uses a power-interest grid to decide how to treat different customer segments, based on **power** (their influence on the business) and **interest** (how much they care about the business). The marketing mix is then adjusted to focus most attention on customers in the high-power/high-interest quadrant."
      }
    ];
    c.learningOutcomes[6].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Explain how a business can use a power-interest grid to inform its marketing mix.",
        model: "A business plots its customer segments on a power-interest grid using the axes Power (influence on the business) and Interest (how much they care about it). Customers in the **high-power, high-interest** quadrant are the priority — for example, a clothing brand's loyal repeat customers — and the marketing mix should focus on retaining them with loyalty schemes (Pricing), personalised messaging (Promotion), and excellent in-store and online service (People, Process). **Low-interest, low-power** segments such as occasional shoppers receive minimal effort. This allows the business to allocate marketing spend efficiently and protect the customers who matter most."
      }
    ];
    // 9.8 — STEEPLE analysis
    c.learningOutcomes[7].notes = [
      {
        h: "What is the STEEPLE analysis tool and why is it useful?", b: "A tool to understand the wider external environment a business operates in. Identifies opportunities and threats so the business can plan, decide and adapt to stay competitive and compliant."
      },
      {
        h: "STEEPLE factors",
        b: "**Social** — lifestyle/values changes (vegan/low-cal options for Gen Z). **Technological** — automation, platforms (apps for younger customers). **Economic** — inflation, interest rates, consumer confidence (subscription cancellations during downturns). **Environmental** — climate, sustainability (water company's plastic bottles). **Political** — government policy, trade relations, taxes (US tariffs on Irish exporters). **Legal** — employment, GDPR, advertising law (gym data). **Ethical** — values, treatment of people/animals/environment (clothing brand's factory exposé)."
      }
    ];
    c.learningOutcomes[7].questions = [
      {
        type: "short",
        marks: 14,
        prompt: "Conduct a STEEPLE analysis on a business operating in Ireland today, identifying one factor under each of seven headings.",
        model: "**Social**: Growing demand for plant-based and low-calorie food has pushed fast-food chains to add vegan or wellness options to keep Gen Z customers.\n\n**Technological**: Adoption of AI-driven customer service (chatbots, recommendation engines) is now standard — businesses without it lose customers to competitors with smoother digital experiences.\n\n**Economic**: Persistent inflation and high interest rates have reduced disposable income, leading consumers to switch to cheaper alternatives or cancel subscriptions.\n\n**Environmental**: Growing public concern over packaging waste means consumers expect recyclable or refillable options — Ballygowan's recycled plastic bottles is one response.\n\n**Political**: New US tariffs during the Trump administration increased export costs for Irish firms selling into the US market, forcing pricing reviews.\n\n**Legal**: GDPR compliance is mandatory for any business collecting personal data — fines of up to 4% of global turnover make legal compliance a top priority.\n\n**Ethical**: Cultural insensitivity in marketing (e.g. tone-deaf US ad campaigns) can quickly damage a brand's reputation — businesses must check campaigns carefully before launch."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "A clothing company collecting customer data and ensuring it complies with privacy law is responding to which STEEPLE factor?",
        model: "Legal — GDPR is a legal regulation that governs personal data collection.",
        options: [
          "Social",
          "Economic",
          "Legal",
          "Ethical"
        ],
        correct: 2
      }
    ];
  })();

  // ── ch10: Operations and Finance ──────────────────────────────────────────
  (function () {
    var c = ch("ch10");
    // 10.1 — Operational model — Key Partners, Activities & Resources
    c.learningOutcomes[0].notes = [
      {
        h: "What are the three core elements of a business's operational model?", b: "Three core building blocks from the BMC explain how a business runs day-to-day: Key Partners, Key Activities, Key Resources."
      },
      {
        h: "Key Partners",
        b: "External people/organisations a business depends on. **Suppliers** (bakery's wholesaler), **Distributors** (An Post, DPD), **Outsourcing/Service Providers** (payroll, web management), **Strategic Alliances** (Spotify & Uber), **Joint Ventures** (Sony Ericsson), **Licensing** (Penneys licensing Disney/Marvel). Change over time as: business grows, expands abroad, undergoes digital transformation, ethical sourcing pressure, or legal compliance changes."
      },
      {
        h: "What is Key Activities?", b: "Essential tasks needed to deliver the value proposition. **Product Design & Development** (Apple R&D), **Manufacturing** (small-batch chocolatier), **Marketing & Branding** (Gymshark), **Distribution & Logistics** (UPS for online bookstore), **Customer Experience & Support** (24/7 mobile provider support), **App & Website Development**. Change as: business grows, technology evolves, customer needs shift, business model changes (e.g. subscription needs onboarding/retention)."
      },
      {
        h: "Key Resources",
        b: "Essential assets needed to operate. **Physical** (Fastway's vans/depots), **Human Capital** (developers at a start-up), **Financial** (loans/crowdfunding for new business), **Intangible** (Disney's brand/IP, Vinted's user base, Airbnb app/data). Change as: physical assets depreciate, human capital evolves with training/turnover, financial resources shift (start-ups rely on external funding, mature firms reinvest profits), intangibles strengthen or weaken with reputation."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 10,
        prompt: "Outline the three main elements key to the operational model of a business and explain why each may change over time.",
        model: "**1. Key Partners** — external people/organisations the business depends on (suppliers, distributors, outsourced service providers). They change as the business grows: a local supplier may not be enough as the business scales, and exporting requires logistics partners or customs agents.\n\n**2. Key Activities** — the most important day-to-day tasks (manufacturing, marketing, customer support, app development). They change with digital transformation — AI and platforms can automate tasks — and with new business models, where a switch to subscription requires new onboarding and retention activities.\n\n**3. Key Resources** — essential assets (physical, human, financial, intangible). They change because physical assets depreciate and need replacement, human capital evolves as staff gain experience or leave, financial resources shift from start-up funding to retained earnings, and intangibles like brand value can grow or be damaged by events."
      }
    ];
    // 10.2 — Costs, sources of finance, revenue streams across the lifecycle
    c.learningOutcomes[1].notes = [
      {
        h: "What are variable costs and how do they change with output?", b: "Linked to output — rise as output rises. *Examples*: wages, stock, light/heat. As output grows, variable cost per unit usually falls due to economies of scale."
      },
      {
        h: "What are the main short-term sources of finance available to businesses?", b: "**Bank Overdraft** — withdraw more than account balance up to limit. **Accrued Expenses** — delaying payment of bills temporarily. **Trade Credit** — receive goods now, pay 30–60 days later. **Factoring** — sell unpaid invoices to a factoring company for immediate cash; they keep a fee."
      },
      {
        h: "Fixed costs",
        b: "Same each month regardless of output. *Examples*: rent, manager's salary, lease payments. Can change at renewal but stay consistent within agreed period."
      },
      {
        h: "What are the main medium-term sources of finance?", b: "**Leasing** — rent an asset; never own it. **Term Loan** — bank loan repaid in instalments over 1–5 years. **Hire Purchase** — buy via deposit + instalments; ownership after final payment."
      },
      {
        h: "Long-term finance (over 5 years)",
        b: "**Long-term Loan** — instalments over 5+ years. **Debenture** — secured against assets, repaid 10–15 years, annual interest. **Equity/Share Capital** — sell shares; investors become part-owners. **Venture Capital** — invested in high-potential, high-risk start-ups. **Retained Earnings** — reinvest past profits. **Grants** — government/EU money that doesn't need to be repaid (strict criteria)."
      },
      {
        h: "What factors should a business consider when choosing a source of finance?", b: "**Cost** — compare APR. **Purpose** — match source to use (van → medium-term). **Amount** — capital limits. **Control** — equity dilutes voting rights. **Collateral** — risk of losing the asset used as security."
      },
      {
        h: "What are the different types of revenue streams a business can use?", b: "**Product Sales** (bakery), **Service Fees** (gym class), **Subscription** (Netflix), **Advertising** (YouTube), **Commission** (DoneDeal), **Licensing/Franchise Fees**, **Renting/Leasing Assets**."
      },
      {
        h: "Why do revenue streams change over time?", b: "Customer behaviour shifts (gym moves from pay-per-visit to membership), digital transformation, need for predictable income (veg box subscription), competitive diversification (café renting space)."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 5,
        prompt: "Identify a suitable source of finance for a business looking to purchase a delivery van and give a reason for your choice.",
        model: "**Hire Purchase** is suitable. The business pays an initial deposit followed by regular monthly instalments over a 1–5 year period (medium-term, matching the useful life of the van). After the final payment the business owns the van, allowing it to use it long-term and resell when no longer needed. This avoids the large upfront cost of buying outright and the lack of ownership in leasing."
      },
      {
        type: "mcq",
        marks: 6,
        prompt: "Identify whether each of the following costs is variable or fixed: (1) Monthly rent for the bakery space, (2) Cost of ingredients, (3) Lease payments for equipment.",
        model: "Rent is fixed — same each month. Ingredients are variable — rise with production. Lease payments are fixed — same agreed amount each period.",
        options: [
          "1) Variable, 2) Fixed, 3) Variable",
          "1) Fixed, 2) Variable, 3) Fixed",
          "1) Fixed, 2) Variable, 3) Variable",
          "1) Variable, 2) Fixed, 3) Fixed"
        ],
        correct: 1
      },
      {
        type: "short",
        marks: 8,
        prompt: "Outline four short-term sources of finance a business could use to cover variable costs.",
        model: "**1. Bank Overdraft** — Allows the business to withdraw more than is in its current account up to an agreed limit. Useful for short cashflow gaps.\n\n**2. Trade Credit** — The business receives goods now and pays the supplier in 30–60 days, freeing cash to be spent elsewhere in the meantime.\n\n**3. Accrued Expenses** — Delaying the payment of bills for a short time to use that money for another short-term purpose.\n\n**4. Factoring** — Selling unpaid customer invoices to a factoring company in exchange for immediate cash; the factor takes a percentage as its fee."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Outline two factors a business considers when choosing a source of finance.",
        model: "**1. Cost (APR)**: The business compares the Annual Percentage Rate of different options, including interest, fees and charges, to choose the cheapest option that fits its needs.\n\n**2. Control**: If the business issues ordinary shares (equity), the new investors gain voting rights and a say in decision-making. The owner may prefer debt to keep control of the business."
      }
    ];
    // 10.3 — Cashflow analysis
    c.learningOutcomes[2].notes = [
      {
        h: "What is a cashflow forecast and why is it important?", b: "Plans the money coming in (receipts) and going out (payments) over a future period. Helps ensure the business has enough cash for day-to-day operations — without it, employees, suppliers and utility providers go unpaid."
      },
      {
        h: "What are the key reasons a business should prepare a cashflow forecast?", b: "**1. Avoid deficits** — see in advance when a shortage may occur. **2. Improved financial control** — compare actual vs planned cashflow. **3. Raise finance** — required by banks and investors as part of a business plan. **4. Plan for surpluses** — what to do with extra cash (deposit, equipment, expansion)."
      },
      {
        h: "What is Limitations?", b: "**Based on estimates** — predicted figures may be inaccurate. **Unexpected events** — energy price rises, bad debts, economic shocks."
      },
      {
        h: "Analysing the forecast",
        b: "**Closing Cash Surplus** — positive closing balance. **Closing Cash Deficit** — negative closing balance, business won't have enough cash to cover payments."
      },
      {
        h: "What are the main actions a business can take to address cashflow problems?", b: "**1. Spread payments** — lease or pay off in monthly instalments instead of one-off. **2. Increase cash receipts** — short-term promotion for quick cash. **3. Reduce cash payments** — cut unnecessary spending, find cheaper suppliers, restructure loans. **4. Use short-term finance** — overdraft or short-term loan."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline four reasons why a business prepares a cashflow forecast.",
        model: "**1. To help avoid cash deficits** — A forecast highlights months when cash will run short, allowing the business to arrange short-term finance like an overdraft in advance.\n\n**2. Improved financial control** — It allows the business to compare actual cashflow to planned figures, spot variances, and operate within its means.\n\n**3. To raise finance** — Banks, investors and the LEO usually require a cashflow forecast as part of the business plan before agreeing to provide funding.\n\n**4. To plan for surpluses** — When months show excess cash, the business can plan how to use it productively, e.g. placing it on deposit, investing in equipment or funding expansion."
      },
      {
        type: "short",
        marks: 8,
        prompt: "A business has identified a closing cash deficit of €25,000 in December. Recommend a suitable course of action to address this issue.",
        model: "The business could combine several actions:\n\n**1. Avail of a short-term source of finance** — Arrange a bank overdraft to cover the shortfall temporarily until receipts pick up. This is often the quickest solution.\n\n**2. Increase cash receipts** — Run a December promotion such as a 10% discount or 'buy one get one free' to bring forward sales and increase cash inflows.\n\n**3. Reduce cash payments** — Cut non-essential spending, source cheaper suppliers, and ask the bank to restructure existing loan repayments to spread payments over a longer period at smaller monthly amounts.\n\n**4. Spread payments over time** — For any large one-off purchase planned for December, choose to lease or pay over instalments instead of paying upfront."
      },
      {
        type: "tf",
        marks: 2,
        prompt: "A cashflow forecast is based on actual figures from past months and therefore is fully accurate.",
        model: "False. Cashflow forecasts are based on estimated/predicted figures, which may not be accurate. Unexpected events such as energy price rises or bad debts can also affect outcomes.",
        correct: false
      }
    ];
  })();

  // ── ch11: Growth, Development and Expansion ───────────────────────────────
  (function () {
    var c = ch("ch11");
    // 11.1 — Importance of identifying competition
    c.learningOutcomes[0].notes = [
      {
        h: "How do direct competitors differ from indirect competitors?", b: "**Direct competitors** — same/similar products to the same target market (a bakery vs another bakery). **Indirect competitors** — different products satisfying the same need (supermarket selling bread)."
      },
      {
        h: "Why is it important for a business to analyse its competition?", b: "**1. Understand who direct/indirect competitors are**. **2. Insight into what strategies have worked or failed** for rivals — avoid mistakes, build on proven ideas. **3. Reveals current consumer preferences** — adapt to what customers value (gluten-free range)."
      },
      {
        h: "Capitalising on competitive advantage",
        b: "**1. Helps create a clear USP** — a differentiating feature, service or experience. **2. Builds loyal customer base** — customers return for what they can't easily find elsewhere (Ryanair's low fares). **3. Improves the marketing mix** — communicate USP through advertising, in-store, packaging, staff. **4. Develops the advantage** — invest in what you're best at; advantages are not permanent. Examples of advantages: lower prices, free returns, higher quality, location, customer service, technology, next-day delivery, latest designs."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Demonstrate the importance of identifying competition in the market for a business.",
        model: "Identifying competition allows a business to understand both **direct competitors** (same product to same market — e.g. another local bakery) and **indirect competitors** (different products meeting the same need — e.g. a supermarket selling bread). This is important because it provides insights into strategies that have worked or failed for rivals — letting the business avoid expensive mistakes and copy proven approaches. It also reveals current consumer preferences, helping the business adapt — for example, a bakery noticing gluten-free products selling well at competitors might launch its own gluten-free range. Without this analysis the business risks irrelevance."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Identify a potential competitive advantage for a business of your choice and recommend an appropriate strategy for launching a new product to the market.",
        model: "**Business**: A small Irish skincare brand with a competitive advantage in **organic, locally-sourced ingredients**.\n\n**Recommended strategy**: Build the entire marketing mix around this USP. **Product**: highlight the natural, plant-based formula on packaging with clear ingredient transparency. **Pricing**: position as premium, justified by ethical sourcing. **Promotion**: use Instagram and TikTok influencers in the wellness/eco space to demonstrate the products and tell the supplier story. **Place**: launch direct-to-consumer through the brand website to maintain margin and customer data, plus stock in select health shops. This way, every part of the marketing mix reinforces the competitive advantage rather than competing on price with mass-market brands."
      }
    ];
    // 11.2 — Porter's Five Forces
    c.learningOutcomes[1].notes = [
      {
        h: "What is Porter's Five Forces model and what does it help a business understand?", b: "A model with five competitive forces driving the division of economic value among stakeholders. It helps a business identify strengths, risks and competitive advantage."
      },
      {
        h: "1. Threat of New Entrants",
        b: "How easy it is for new businesses to enter the market. **Low threat** = high barriers (McDonald's needs huge capital, branding, supply networks). **High threat** = anyone can enter (a barber shop)."
      },
      {
        h: "2. Bargaining Power of Suppliers",
        b: "Power suppliers have over the business. **Low** = many alternatives (Supermac's sourcing potatoes from many Irish farms). **High** = relies on key supplier (small Irish cake maker selling most of its output to Aldi)."
      },
      {
        h: "3. Bargaining Power of Buyers",
        b: "Power customers have. **Low** = loyal, can't switch easily (Apple iPhone). **High** = customers can switch instantly (taxi customers can use Uber, FreeNow)."
      },
      {
        h: "What does the threat of substitutes mean in Porter's Five Forces?", b: "Alternative ways to meet the same need. **Low** = few alternatives (electricity supply). **High** = many options (Spotify vs YouTube, Apple Music, radio, podcasts)."
      },
      {
        h: "What does competitive rivalry mean in Porter's Five Forces model?", b: "Intensity of competition. **Low** = limited rivals (Irish Rail intercity routes). **High** = price wars, heavy promotion (Circle K vs Applegreen forecourt sector)."
      },
      {
        h: "How can a business use Porter's Five Forces to inform strategic decisions?", b: "Low new-entrant threat + strong loyalty → scope to raise prices/expand. High rivalry/new entrants → delay expansion, invest in marketing/innovation to protect the business."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 25,
        prompt: "Analyse the competitive forces in the market for an Irish supermarket like Dunnes Stores using Porter's Five Forces Model. (5 @ 5m: 2m explain force + 3m apply to business)",
        model: "**1. Threat of New Entrants — Low**: Setting up a nationwide supermarket chain requires massive investment in stores, logistics, distribution centres and branding. Few new players could match Dunnes' established footprint, so the threat is low.\n\n**2. Bargaining Power of Suppliers — Low**: Dunnes has scale and a wide network of Irish and international suppliers, allowing it to negotiate favourable prices and reduce supplier power over its margins.\n\n**3. Bargaining Power of Customers — High**: Irish customers can easily switch between Dunnes, Tesco, Aldi, Lidl and SuperValu. This forces Dunnes to use loyalty schemes like the well-known €10 off €50 spend to keep customers returning.\n\n**4. Threat of Substitutes — Medium**: Customers could shop at convenience stores, farmers' markets or use meal delivery services like HelloFresh, but supermarkets remain the most convenient single option for the weekly shop.\n\n**5. Competitive Rivalry — High**: Rivalry is fierce among the big five retailers. Dunnes competes through promotions, in-house brands like Simply Better, and a unique mix of groceries with clothing and homeware that is harder for pure grocers like Aldi to copy."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Name the two forces missing from Porter's Five Forces Model from the list: 1. Threat of New Entrants; 2. _____; 3. _____; 4. Threat of Substitutes; 5. Competitive Rivalry.",
        model: "**2. Bargaining Power of Suppliers**\n**3. Bargaining Power of Buyers (Customers)**"
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "A business with strong customer loyalty and a low threat of new entrants is in a good position to:",
        model: "A business with these conditions has scope to raise prices or expand because its position is well protected.",
        options: [
          "Lower prices to defend market share",
          "Raise prices or expand the business",
          "Reduce its marketing budget",
          "Sell to a competitor"
        ],
        correct: 1
      }
    ];
    // 11.3 — Strategies to adapt or expand
    c.learningOutcomes[2].notes = [
      {
        h: "Adaptation strategies",
        b: "**Updating products/services** (McDonald's vegan burgers). **Targeting new segments** (gym launches low-impact programme for older adults). **Reducing costs through automation/AI** (hotel chatbot for bookings). **Diversifying** to remove risk (soft drinks company adds sparkling water). **Investing in staff development** (training in digital tools). **Improving sustainability/branding** (clothing brand switches to organic cotton)."
      },
      {
        h: "What is organic expansion and what are its benefits and challenges?", b: "**Increasing product range / entering new markets** — spreads risk, opens revenue. **E-commerce expansion** — reach more customers without physical sites (All Real Nutrition into US). **Franchising** — franchisor grants licence to franchisees in return for fees. *Benefits*: rapid expansion, lower costs (franchisees fund their own outlets), local knowledge. *Challenges*: quality varies, loss of control, brand reputation risk."
      },
      {
        h: "What is a takeover/acquisition and what are its benefits and challenges?",
        b: "Acquiring 50%+ of another business's shares. *Hostile* if directors recommend rejection. *Benefits*: rapid market access, eliminates competition, gains assets/IP. *Challenges*: high capital, hostility with stakeholders, regulatory issues. Example: Meta took over Instagram and WhatsApp."
      },
      {
        h: "What is a merger and what are its benefits and challenges?", b: "Voluntary amalgamation of two firms into one new legal entity (Kraft + Heinz → KraftHeinz). *Benefits*: shared resources, economies of scale, stronger market position. *Challenges*: culture clashes, redundancies, complex integration."
      },
      {
        h: "What is a strategic alliance and what are its benefits and challenges?", b: "Two+ businesses pool resources/expertise for a project or period while keeping separate identities (Uber + Spotify in-car streaming). *Benefits*: shared expertise, market access, lower risk. *Challenges*: unequal contribution, loss of control, conflicting objectives."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Outline three strategies a small Irish online clothing business could use to expand. (3 @ 4m)",
        model: "**1. E-commerce expansion into new geographic markets**: The business could expand its website to ship internationally — for example targeting the UK and US — with localised pricing and shipping. This allows growth without the cost of physical stores. *Example*: All Real Nutrition expanded into the US through Shopify.\n\n**2. Strategic Alliance with a larger retailer or marketplace**: The business could agree to stock a curated range on a larger platform such as ASOS Marketplace or a high-street retailer's website. This gives instant access to a much bigger customer base while keeping the brand identity separate.\n\n**3. Diversifying into new product lines**: The business could expand into adjacent categories such as accessories or athleisure to spread risk across multiple revenue streams and increase the average order value of existing customers."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Distinguish between a takeover and a merger as expansion strategies, giving one example of each.",
        model: "**Takeover (Acquisition)**: One business takes control of another by buying over 50% of its shares. The target business may continue under its own name as a subsidiary. *Example*: Meta took over Instagram. It can be hostile if the target company's directors recommend rejecting the offer.\n\n**Merger**: A voluntary amalgamation of two or more firms into a single new legal entity, with no business in control of the other. Both shareholder groups must approve. *Example*: Kraft and Heinz merged to form KraftHeinz."
      },
      {
        type: "short",
        marks: 10,
        prompt: "Discuss two benefits and two challenges of franchising as an expansion strategy.",
        model: "**Benefits**:\n**1. Rapid expansion at lower cost** — Franchisees fund and manage their own outlets, allowing the franchisor to grow quickly without huge capital outlay.\n**2. Local knowledge and motivation** — Franchisees often understand their local market well and are highly motivated as owners, helping the business succeed in different regions.\n\n**Challenges**:\n**1. Loss of control and inconsistent quality** — Decisions are shared with many independent franchisees and customer experience can vary if franchisees do not follow standards.\n**2. Brand reputation risk** — One franchisee delivering poor service or facing negative publicity can damage the entire brand's reputation across all locations."
      }
    ];
    // 11.4 — Technology supporting adaptation and expansion
    c.learningOutcomes[3].notes = [
      {
        h: "How does technology support business adaptation and expansion?", b: "**Meeting expectations for speed/convenience** — apps, online ordering. **Expanding reach** — Shopify, WooCommerce e-commerce platforms. **Understanding customer behaviour** — Google Analytics, in-app tracking to personalise offers. **Reducing costs/increasing efficiency** — automation, AI, chatbots. **Building brand awareness** — Instagram, TikTok and content tools. **Accessing finance online** — crowdfunding (Kickstarter, Fundit, GoFundMe)."
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Describe two forms of technology that support adaptation or expansion for a business.",
        model: "**1. E-commerce platforms (Shopify, WooCommerce)**: These allow a business to set up an online store quickly and sell nationally or internationally without the cost of physical premises. This expands reach to new markets — for example, a small Irish brand can sell to UK and US customers from day one.\n\n**2. Data analytics tools (Google Analytics)**: By tracking what customers view, click and buy, businesses can understand behaviour and personalise offers. This allows the business to refine its marketing and product range based on real evidence rather than guesswork, supporting smart expansion decisions."
      }
    ];
    // 11.5 — Cost-Benefit Analysis (CBA) of expansion
    c.learningOutcomes[4].notes = [
      {
        h: "Why is cost-benefit analysis important when evaluating expansion?", b: "When considering expansion, the business weighs short- and long-term benefits against costs to ensure a **net benefit**. Helps make decisions strategic, sustainable, and realistic."
      },
      {
        h: "What are the potential benefits of business expansion?", b: "**Increased Revenue (profit)** — reach new markets (All Real Nutrition into US via Shopify). **Economies of Scale (lower costs)** — fixed costs spread over larger output (Ryanair). **Stronger Market Presence (lowers risk)** — bigger market share reduces rival influence (Aldi forced Tesco/Dunnes to price-match). **Access to new skills/products (diversification)** — new tech, IP, audience (Facebook bought Instagram for younger audience)."
      },
      {
        h: "Potential costs",
        b: "**High Capital Investment** — large outlay for property, equipment, staff (Tesco's failed Fresh & Easy US expansion cost £1bn+). **Regulatory Risks** — extra scrutiny, possible blocks (Facebook's WhatsApp acquisition faced investigation). **Culture Clashes/Poor Integration** — different systems and cultures (AOL–Time Warner). **Loss of Focus/Quality** — distraction from core business (Nokia's late smartphone move)."
      }
    ];
    c.learningOutcomes[4].questions = [
      {
        type: "short",
        marks: 16,
        prompt: "Conduct a cost-benefit analysis of a proposed takeover by one large Irish business of another. (4 benefits @ 2m + 4 costs @ 2m)",
        model: "**Scenario**: Tesco proposed takeover of Musgrave Group (SuperValu/Centra).\n\n**Benefits**:\n**1. Rapid Market Access** — Instant access to 220+ SuperValu outlets and Musgrave's strong supplier relationships, vastly increasing Tesco's reach in Ireland.\n**2. Eliminates Competition** — Removes a major rival from the market and gives Tesco a far stronger position against Aldi and Lidl.\n**3. Economies of Scale** — Combined purchasing power reduces unit costs and increases bargaining power with suppliers, improving margins.\n**4. New Assets and Customer Base** — Gains the Centra/SuperValu brands, retail technology and a loyal local customer base that would take years to build from scratch.\n\n**Costs**:\n**1. High Capital Investment** — Acquiring Musgrave at a premium price would cost a huge amount and put pressure on Tesco's cash flow and balance sheet.\n**2. Regulatory Risks** — The Competition and Consumer Protection Commission (CCPC) could block or restrict the deal due to concerns about reduced competition in Irish grocery.\n**3. Community/Reputation Backlash** — The loss of an Irish-owned brand could lead to public anger and customer boycotts, damaging Tesco's reputation in Ireland.\n**4. Integration Challenges** — Merging two large retail systems, store formats and workforces is complex and may distract management from core operations.\n\n**Conclusion**: The financial and reputational risks are significant, but the strategic benefits of dominating the Irish grocery market may outweigh them — provided the CCPC approves the deal and Tesco manages the integration carefully."
      }
    ];
    // 11.6 — Adapting marketing mix or business model
    c.learningOutcomes[5].notes = [
      {
        h: "Customer demographics",
        b: "**Marketing Mix**: Ben & Jerry's introduced non-dairy ice cream for vegan/lactose-intolerant customers, changing product, promotion, packaging. **Business Model**: All Real Nutrition added an online subscription for recurring convenience and steady revenue."
      },
      {
        h: "Competition",
        b: "**Marketing Mix**: Burger King launched a flame-grilled plant-based Whopper to match McDonald's vegan offering. **Business Model**: Disney created Disney+ to stream directly to customers, ending licensing to Netflix and creating a subscription revenue stream."
      },
      {
        h: "What is an Economic factors?", b: "**Marketing Mix**: Lidl Plus loyalty app with digital coupons targets cost-conscious shoppers. **Business Model**: Irish gyms moved to hybrid memberships (in-person + online classes) during COVID, creating a blended revenue model."
      }
    ];
    c.learningOutcomes[5].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Outline how a business could adapt its marketing mix or its business model to respond to changing competition in the market.",
        model: "**Marketing Mix Example — Burger King**: Faced with McDonald's vegan launch, Burger King introduced its flame-grilled plant-based Whopper. This adapts the **Product** by adding a vegan option, and adapts **Promotion** by emphasising the flame-grilled cooking method that differentiates it from McDonald's, allowing Burger King to defend market share against changing competition.\n\n**Business Model Example — Disney**: As Netflix grew, Disney shifted from licensing its content to competitors and instead launched Disney+, a subscription streaming service. This change in business model gave Disney direct control over distribution and a new recurring revenue stream, allowing it to compete head-on with Netflix in a way the old licensing model couldn't."
      }
    ];
  })();

  // ── ch12: Managing Risk ───────────────────────────────────────────────────
  (function () {
    var c = ch("ch12");
    // 12.1 — Challenges and risks of enterprise
    c.learningOutcomes[0].notes = [
      {
        h: "What are the main challenges facing entrepreneurs?", b: "**Raising finance** — equity, debt, crowdfunding (Kickstarter). **Production methods** — keeping costs low while meeting demand. **Choosing ownership type** — sole trader (cheap, easy) vs Ltd (limited liability, lower corporation tax). **Marketing/market penetration** — costly initial advertising, need clear USP. **Availability of location/staff** — high rents, skilled labour shortages."
      },
      {
        h: "What are the different types of risks that entrepreneurs face?", b: "**Personal & Financial Risk** — savings, assets, credit rating, reputation. **Operational Risk** — poor staffing/logistics/admin causes lost sales. **Economic Risk** — inflation, interest rates, tariffs. **Competitor & Market Risk** — new entrants, aggressive rivals (Revolut/N26 challenging Irish banks). **Compliance Risk** — failing legal obligations (tax, H&S). **Technological Risk** — cyberattacks, breaches (Ardagh Group 2021). **Ethical & Environmental Risk** — unethical sourcing damages reputation (Boohoo paid workers £3.50/hr in Leicester)."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Outline three challenges, apart from inflation, facing entrepreneurs in Ireland. (3 @ 4m)",
        model: "**1. Raising Finance**: Many entrepreneurs lack the capital to start or grow. Banks require strong business plans, and equity investors take ownership in return for funding. Crowdfunding through platforms like Kickstarter is an option but requires building trust quickly.\n\n**2. Availability of Location and Staff**: High rents — especially in Dublin city centre — make finding affordable premises difficult, hurting footfall and margins. Hiring skilled staff is also harder due to high cost of living and labour shortages in sectors like hospitality and tech.\n\n**3. Marketing and Market Penetration**: Standing out is expensive when initial sales are slow. Entrepreneurs must invest in marketing, identify the right channels (digital, social, in-store) and build a clear USP to compete with established rivals."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Discuss two risks facing entrepreneurs and explain how each could affect the business.",
        model: "**1. Technological & Cyber Risk**: A cyberattack or data breach can disrupt operations, expose customer data and damage reputation. *Example*: Ardagh Group experienced a cyberattack in 2021 that disrupted operations. This can lead to loss of customer trust, fines under GDPR, and immediate financial damage from system downtime.\n\n**2. Ethical & Environmental Risk**: Unethical sourcing or environmental harm can damage brand reputation. *Example*: Boohoo faced backlash when an investigation revealed Leicester factory workers being paid below minimum wage. This kind of risk leads to consumer boycotts, regulator scrutiny, and falling sales — even when the financials look strong otherwise."
      }
    ];
    // 12.2 — Importance of assessing and managing risks
    c.learningOutcomes[1].notes = [
      {
        h: "What is risk management?", b: "Identification of all possible risks/losses (fire, employer negligence, personal injury, legal liability) and taking action to avoid risks or minimise their impact."
      },
      {
        h: "What are the main steps in the risk management process?", b: "**1. Identify the risk** — spot threats through audits (injury, theft). **2. Assess its impact** — likelihood × severity to prioritise. **3. Take action to reduce risk** — train staff, diversify, insure, avoid. **4. Monitor and review** — update plans for new risks."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Explain two reasons why it is important for a business to manage risks.",
        model: "**1. Avoids costly mistakes**: By identifying risks in advance, a business can prevent legal, financial or reputational harm before it happens. For example, training staff in machinery safety and conducting regular checks prevents workplace accidents that would cause downtime and compensation claims.\n\n**2. Improves financial sustainability**: Businesses that manage risk are more resilient to disruptions and market shifts. By spreading risk through diversification — for example, a food brand expanding into both retail and online — the business protects revenue if one channel suffers, helping it survive long-term."
      },
      {
        type: "short",
        marks: 4,
        prompt: "Outline the four steps involved in risk management.",
        model: "**1. Identify the risk** — Spot potential threats through audits and reviews (e.g. injury, theft, cyberattack).\n**2. Assess its impact** — Judge likelihood and severity of each risk to prioritise action.\n**3. Take action to reduce risk** — Train staff, diversify, insure, or avoid high-risk activities.\n**4. Monitor and review** — Update plans regularly as new risks emerge."
      }
    ];
    // 12.3 — Risk management strategies and types of insurance
    c.learningOutcomes[2].notes = [
      {
        h: "Strategy 1 — Avoidance",
        b: "Not engaging in an activity that presents significant or unmanageable risk. *Example*: festival cancelled due to weather warnings; food start-up avoids allergen products if it can't guarantee safety."
      },
      {
        h: "What is the spread or diversification risk management strategy?", b: "Diversifying products, suppliers, markets, channels. *Example*: farm sells locally and via online delivery; Netflix produces international content (Squid Game) to reduce US reliance."
      },
      {
        h: "What is the prevention risk management strategy?", b: "Proactive steps to reduce likelihood. *Example*: hotel installs sprinklers and trains staff in fire safety; Apple performs rigorous battery testing."
      },
      {
        h: "What is the insurance risk management strategy?", b: "Transfers financial cost of a risk to an insurer for a premium. *Example*: tech start-up takes out cyber insurance; construction firm insures equipment and workers."
      },
      {
        h: "What are the main types of business insurance?", b: "**Public Liability** — injury/damage to customers/property (slip in shop). **Employer Liability** — staff injury at work. **Product Liability** — injury from faulty products. **Buildings & Contents** — premises and stock (fire, flood, theft). **Motor** — company vehicles (legally required). **Key Person** — loss of vital staff. **Fidelity Guarantee** — internal theft/fraud by staff. **Goods in Transit** — damage during transport. **Cyber** — cyberattacks, breaches. **Professional Indemnity** — claims of poor advice. **Business Interruption** — income loss during closures (fire, flood, pandemic)."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 16,
        prompt: "Discuss four risk management strategies that can be used by businesses to respond to potential risk. (4 @ 4m)",
        model: "**1. Avoidance**: Not engaging in an activity that presents significant or unmanageable risk. *Example*: A festival organiser cancels an outdoor event due to weather warnings, avoiding reputational and financial loss. A food start-up may avoid expanding into allergen-sensitive products if it cannot guarantee safety.\n\n**2. Spread (Diversification)**: Diversifying products, suppliers, markets or channels to reduce overreliance on one area. *Example*: Netflix produces international content like Squid Game to reduce reliance on the US market and audience.\n\n**3. Prevention**: Proactive steps to reduce the likelihood of risks occurring. *Example*: A hotel trains staff in fire safety and installs sprinklers; Apple performs rigorous battery testing to prevent product malfunctions.\n\n**4. Insurance**: Transferring the financial cost of a risk to an insurer in exchange for a premium. *Example*: A tech start-up takes out cyber insurance to cover recovery costs from a data breach. Insurance does not prevent the risk but ensures the business can recover financially."
      },
      {
        type: "short",
        marks: 12,
        prompt: "Outline three types of insurance a small bakery café should consider, with reasons for each. (3 @ 4m)",
        model: "**1. Public Liability Insurance**: Covers injury or damage to customers on the premises. Essential for a café where customers may slip on a wet floor or be injured by faulty furniture — protects against expensive legal claims.\n\n**2. Buildings & Contents Insurance**: Covers premises and stock against fire, flood and theft. *Example*: an electrical fault damaging a fridge full of stock — this insurance allows quick recovery without severe financial loss.\n\n**3. Motor Insurance**: Legally required for company vehicles. The bakery uses its van for cake deliveries, so motor insurance ensures compensation if there is an accident during a delivery and protects the business from claims."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "A construction company insuring its equipment and workers in case of site accidents is using which risk management strategy?",
        model: "Insurance — transferring the financial cost of a risk to an insurer in exchange for a premium.",
        options: [
          "Avoidance",
          "Spread",
          "Prevention",
          "Insurance"
        ],
        correct: 3
      }
    ];
  })();

  // ── ch16: The Rationale for Planning ──────────────────────────────────────
  (function () {
    var c = ch("ch16");
    // 16.1 — Internal and external changes facing organisations
    c.learningOutcomes[0].notes = [
      {
        h: "What are the main types of internal changes an organisation might face?", b: "**Leadership changes** — new vision and management style. **Adoption of technology** — new systems require staff training. **Restructuring/downsizing** — merging teams, layoffs to remain sustainable. **Change in business model/strategy** — new products, new markets. **Cultural/organisational development** — autonomy, remote working."
      },
      {
        h: "What are the main types of external changes an organisation might face?",
        b: "**Market trends and consumer expectations** — ethical, digital-first preferences. **Economic trends** — inflation, interest rates, minimum wage. **Legal and regulatory changes** — GDPR. **Digital disruption and transformation** — invest in new systems/skills. **Competitors' innovations** — innovate to stay relevant."
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 10,
        prompt: "Outline three internal changes and two external changes an organisation might encounter through its lifetime.",
        model: "**Internal**:\n**1. Leadership changes** — A new CEO can bring different priorities, management style and vision, leading to changes in culture and strategy.\n**2. Adoption of technology** — Introducing new software or automation forces process and training changes for staff.\n**3. Restructuring or downsizing** — Economic pressure may lead to merging teams, redundancies or layoffs to keep the business sustainable.\n\n**External**:\n**1. Legal and regulatory changes** — New laws like GDPR force businesses to update systems and processes, with significant fines for non-compliance.\n**2. Digital disruption** — New technology and digital-first competitors push existing businesses to invest in new systems and skills to stay relevant."
      }
    ];
    // 16.2 — Reasons for resistance to change
    c.learningOutcomes[1].notes = [
      {
        h: "What are the main reasons employees resist change in an organisation?",
        b: "**Fear of job losses** — new tech or outsourcing may reduce/replace roles. **Fear of failure** — doubt about adapting to new systems. **No clear benefit communicated** — staff see change as unnecessary or risky. **Inertia** — preference for familiar routines, 'the way things have always been done'."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 16,
        prompt: "Analyse four reasons for resistance to change in an organisation. (4 @ 4m)",
        model: "**1. Fear of Job Losses**: When new technology or outsourcing is introduced, employees may worry their roles will be cut or replaced. This fear grows if management doesn't communicate openly that change supports growth rather than redundancies. The result is low engagement and active opposition to the change.\n\n**2. Fear of Failure**: Employees can doubt their ability to adapt to new systems or responsibilities. Without proper training and reassurance, they resist change to avoid making mistakes or being judged in front of colleagues.\n\n**3. No Clear Benefit Communicated**: Staff are more likely to support change when they understand how it helps them or the organisation. If management doesn't explain the benefits clearly, employees view the change as unnecessary or risky and resist it.\n\n**4. Inertia**: Many people prefer familiar routines and resist moving away from 'the way things have always been done'. Leaders need to create a clear vision of why change matters and how it will improve the workplace to overcome this."
      }
    ];
    // 16.3 — Practices that promote innovation and intrapreneurial thinking
    c.learningOutcomes[2].notes = [
      {
        h: "What practices help organisations promote innovation and intrapreneurial thinking?", b: "**1. Leadership Culture that Encourages Risk-Taking** — make it safe to take smart risks and learn from mistakes. **2. Provide Training and Resources to Staff** — invest time, funding and skills development. **3. Use of Teamwork and Collaboration** — across departments to share perspectives. **4. Recognition and Rewards for Innovation** — praise, bonuses, opportunities to motivate creative contributions."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Identify three practices that promote innovation and intrapreneurial thinking in an organisation. (3 @ 4m)",
        model: "**1. Leadership Culture that Encourages Risk-Taking**: Leaders should promote an environment where employees feel safe to take smart risks and learn from mistakes. This builds the confidence needed for staff to come forward with creative ideas without fear of being penalised.\n\n**2. Provide Training and Resources**: Businesses should invest in time, funding and skills development so employees can explore new ideas. *Example*: Google's 20% time policy gives staff space to work on new concepts.\n\n**3. Recognition and Rewards for Innovation**: Acknowledging staff for creative contributions through praise, bonuses or career opportunities motivates continued innovation. People are far more likely to share new ideas when they see them recognised and acted on."
      }
    ];
    // 16.4 — Overcoming resistance to change
    c.learningOutcomes[3].notes = [
      {
        h: "What approaches can help an organisation overcome resistance to change?", b: "**Lead by Example** — leaders model the behaviour expected. **Open Communication and Consultation** — explain the why and involve staff. **Training and Resource Support** — tools and guidance reduce anxiety. **Employee Empowerment** — give ownership over their role in change. **Rewarding Staff** — recognise those who embrace change. **Use of Teamwork and Collaboration** — peer support reduces isolation."
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline two ways an organisation can overcome resistance to change.",
        model: "**1. Open Communication and Consultation**: Explaining why the change is happening and involving staff in decisions reduces fear and rumours. When employees feel informed and consulted — for example through Q&A sessions and feedback surveys — they are far more likely to support the change.\n\n**2. Training and Resource Support**: Providing the right tools, training and guidance helps employees feel prepared. *Example*: when introducing new software, dedicated training time and easy-to-access support reduces anxiety about new responsibilities and avoids the fear of failure that often drives resistance."
      }
    ];
    // 16.5 — Strategic planning as an ongoing process
    c.learningOutcomes[4].notes = [
      {
        h: "What is strategic planning and why is it important?", b: "The ongoing process of setting long-term goals and deciding how the business will achieve them. Acts as a roadmap, sets a clear vision, aligns people and resources."
      },
      {
        h: "What are the main steps in the strategic planning process?", b: "**1. Define vision through Mission Statement** — values, purpose, long-term ambition. **2. Analyse internal and external environment** — SWOT and STEEPLE. **3. Set long-term plan** — 5–10 year goals using SMART objectives. **4. Tactical Plans** — break into 1–2 year smaller chunks for departments. **5. Operational Plans** — implement day-to-day."
      },
      {
        h: "Why is strategic planning an ongoing process?", b: "Regular reviews track progress and adjust goals; changing markets require updates; identifies new risks early; supports continuous improvement."
      }
    ];
    c.learningOutcomes[4].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Outline what is meant by strategic planning and explain why it is an ongoing process.",
        model: "**Strategic planning** is the ongoing process of setting long-term goals (typically 5–10 years) and deciding how the business will achieve them. It begins with a mission statement, uses tools like SWOT and STEEPLE to analyse the internal and external environment, sets SMART long-term goals, and breaks them down into tactical and operational plans.\n\nIt is **ongoing** because the business environment is constantly changing — new competitors emerge, customer expectations shift, technology evolves, and laws change. Regular reviews allow the business to track progress, adjust goals where needed and identify new risks early. A static plan would quickly become out of date, leaving the business unable to adapt."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Outline the steps involved in the strategic planning process.",
        model: "**1. Define the vision through the mission statement** — outlining values, purpose and long-term ambition.\n**2. Analyse the internal and external environment** using tools like SWOT and STEEPLE.\n**3. Set the long-term plan** — 5–10 year SMART goals.\n**4. Break long-term plans into tactical plans** — 1–2 year chunks for departments.\n**5. Implement through operational plans** — day-to-day running of the business."
      }
    ];
    // 16.6 — Benefits of strategic planning
    c.learningOutcomes[5].notes = [
      {
        h: "What are the main benefits of strategic planning?", b: "**1. Increased clarity and direction** — clear long-term goal, consistent decisions across departments. **2. Increased ability to manage change** — respond without losing focus, adjust plans as environment changes. **3. Increased resource efficiency** — allocate staff, money and time to top priorities. **4. Increased competitive advantage** — regular SWOT review supports innovation, differentiation and early opportunities."
      }
    ];
    c.learningOutcomes[5].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Describe three benefits of strategic planning for an organisation.",
        model: "**1. Increased Clarity and Direction**: A strategic plan gives the business a clear long-term goal, helping leaders and departments make consistent decisions and avoid being distracted by short-term issues.\n\n**2. Increased Resource Efficiency**: It helps the business allocate staff, money and time to the priorities that matter most for long-term success, reducing wasted effort on low-value activities.\n\n**3. Increased Competitive Advantage**: Regular review of strengths, weaknesses, opportunities and threats helps the business stay ahead. It supports innovation, differentiation and early identification of opportunities — for example, spotting an emerging customer trend before competitors react."
      }
    ];
    // 16.7 — Force-Field Analysis
    c.learningOutcomes[6].notes = [
      {
        h: "What is Force-Field Analysis and what does it help identify?", b: "An approach to identify and analyse forces that drive and inhibit change. Forces can be internal or external."
      },
      {
        h: "What are the key steps in conducting a Force-Field Analysis?", b: "**1. Define the strategic change clearly** (e.g. moving back to office). **2. Identify driving and restraining forces** — internal (employee morale, skills, culture) and external (laws, technology, customer expectations). **3. Assign a score/weight (1–5)** based on strength of influence. **4. Analyse the results** — if restraining > driving: strengthen drivers, reduce restrainers, delay/cancel, or revise strategy and re-run analysis."
      },
      {
        h: "Can you provide an example of Force-Field Analysis for a hybrid-to-office change?", b: "Driving forces (collaboration, oversight, culture) totalled 11. Restraining forces (commuting time, retention risk, work-life balance) totalled 17. Restraining > driving → reconsider; alternative: 3-day office week to reduce restrainers."
      }
    ];
    c.learningOutcomes[6].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Use a Force Field Analysis to examine the potential effects of a decision to move all staff back to the office full-time.",
        model: "**Driving Forces (favouring the change)**:\n• Improved face-to-face collaboration and culture (score: 4)\n• Easier supervision and management oversight (score: 3)\n• Stronger company culture and onboarding for new staff (score: 4)\n**Total Driving = 11**\n\n**Restraining Forces (against the change)**:\n• Reduced staff satisfaction and work-life balance (score: 5)\n• Increased risk of staff turnover, especially senior talent (score: 5)\n• Higher commuting and childcare costs for staff (score: 4)\n• Reduced ability to attract talent who want flexibility (score: 3)\n**Total Restraining = 17**\n\n**Analysis**: Restraining forces (17) clearly outweigh driving forces (11). The proposed change risks staff dissatisfaction, retention problems and reduced ability to hire. The business should consider an alternative such as a three-day office / two-day remote hybrid, which preserves the collaboration benefits while reducing the strongest restraining forces."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Indicate whether each of the following statements relating to a hybrid working model is a driving force or a restraining force: (1) may result in employees feeling isolated, (2) would help fulfil the wellness programme, (3) may lead to difficulty in monitoring productivity, (4) may bring about a higher likelihood of confidentiality breaches.",
        model: "**1. Restraining force** — isolation undermines collaboration and morale.\n**2. Driving force** — supports the wellness programme objective.\n**3. Restraining force** — harder oversight makes the change less attractive.\n**4. Restraining force** — confidentiality risk argues against hybrid working."
      }
    ];
    // 16.8 — Contingency planning for crisis management
    c.learningOutcomes[7].notes = [
      {
        h: "What is contingency planning?", b: "A backup plan prepared in advance for unexpected events that could disrupt operations. Outlines steps to protect staff, customers, finances and reputation."
      },
      {
        h: "Why is contingency planning important for crisis management?", b: "Allows business to: **respond quickly** to reduce panic; **protect staff and assets**; **maintain operations** or restore them quickly; **minimise damage** to finances, brand or supply chains."
      }
    ];
    c.learningOutcomes[7].questions = [
      {
        type: "short",
        marks: 5,
        prompt: "Explain the term 'contingency planning'.",
        model: "**Contingency planning** is the process of preparing a backup plan in advance to deal with unexpected events or emergencies that could disrupt business operations — for example, a fire, cyberattack, supply chain failure or pandemic. It outlines the steps the business will take if something goes wrong, helping to protect staff, customers, finances and reputation. It allows the business to respond quickly, reducing panic and confusion, maintain operations where possible, and minimise damage to the business if a crisis occurs."
      }
    ];
    // 16.9 — Factors to consider when developing a contingency plan
    c.learningOutcomes[8].notes = [
      {
        h: "What factors should a business consider when developing a contingency plan?", b: "**Cost** — spending on training, backup systems, alternative suppliers — must be weighed against larger damage if no plan exists. **Timing** — some risks need immediate response, others allow more preparation. Acting quickly prevents small disruptions becoming major crises. **Risk** — not all risks are equally likely or severe. Prioritise high-impact, high-probability risks. **Communication** — clear communication during a crisis reduces confusion, identifies who needs to be contacted and how, and protects reputation."
      }
    ];
    c.learningOutcomes[8].questions = [
      {
        type: "short",
        marks: 8,
        prompt: "Discuss two factors that should be considered when developing a contingency plan.",
        model: "**1. Risk**: Not every risk is equally likely or equally severe. Businesses must prioritise the most serious threats — those with high probability and high impact — and assign more detailed planning to them. Focusing resources on the biggest risks makes the plan more effective and prevents wasted time on low-impact events.\n\n**2. Communication**: Clear communication during a crisis reduces confusion and helps the business respond faster. The plan should outline who needs to be contacted (e.g. emergency services, key staff, customers, regulators), how messages will be delivered (email, social media, phone tree), and who is responsible for issuing updates. Strong communication prevents mistakes, protects the business's reputation and supports a faster recovery."
      },
      {
        type: "mcq",
        marks: 2,
        prompt: "When developing a contingency plan, which factor relates to deciding how quickly the business must respond to a particular type of risk?",
        model: "Timing — matching the urgency of the threat to the response speed in the plan.",
        options: [
          "Cost",
          "Timing",
          "Risk",
          "Communication"
        ],
        correct: 1
      }
    ];
  })();

  // ── ch17: Making Informed Decisions as a Consumer ─────────────────────────
  (function () {
    var c = ch("ch17");
    // 17.1 — Consumer rights and responsibilities under current legislation
    c.learningOutcomes[0].notes = [
      {
        h: "What is the role and function of the Competition and Consumer Protection Commission (CCPC)?", b: "Independent statutory body that promotes consumer rights and fair competition. **Functions**: Advise/inform consumers (ccpc.ie), educate (financial calculators, comparison tools), advise government on policy, enforce consumer law (investigate, on-the-spot fines), publish Consumer Protection List of breaches/convictions, promote fair competition (prevent monopolies)."
      },
      {
        h: "Consumer Rights Act 2022 — buying products",
        b: "**Faulty within 30 days**: full refund (must be issued within 14 days). **Fault after 30 days but within 12 months**: free repair or replacement; if serious or repair fails, full/partial refund. **First 12 months**: assumed faulty at time of purchase unless seller proves otherwise (burden of proof on retailer). Same rights apply to sale items, reduced-price items, and second-hand goods bought from a business. Does **not** apply to wear and tear, accidental damage, or where the consumer didn't install a required update."
      },
      {
        h: "What is Right to Cancel a Distance Contract?", b: "When buying online, by phone, mail order or doorstep — consumers have **14 days from receipt** to cancel without giving a reason."
      },
      {
        h: "What is Consumer Rights Act 2022 — services?", b: "Seller must give name, address, phone, full details, total price (incl. VAT) or how price will be calculated. **Redress**: No supply → cancel and refund; Problem with service → refund or price reduction; Damage caused → claim compensation; **Cooling-off**: 14 days to cancel many services."
      },
      {
        h: "What is Digital content & services?", b: "Right to refund if not supplied as agreed; price reduction or refund for serious issues. *Example*: Netflix, Spotify, TikTok (services); games, music, e-books (content)."
      },
      {
        h: "Other points",
        b: "Guarantees/warranties **add to** legal rights, never replace them. **Change of mind** in-store: no automatic right to refund/exchange unless faulty. **Gift vouchers**: don't have to spend full amount at once, can combine, minimum 5-year expiry. **Sale items**: same rights as full price. **Unfair contract terms**: businesses cannot exclude liability for negligence."
      },
      {
        h: "Consumer Protection Act 2007",
        b: "Protects consumers from misleading, false, aggressive practices. Applies to businesses and influencers. **Pricing**: clear/inclusive of taxes; if advertising a sale, the 'prior price' must be the lowest price in the 30 days before. **Influencer marketing**: paid promotions and gifted items must be clearly labelled. CCPC can issue compliance notices, on-the-spot fines (€300) and publish Consumer Protection List."
      },
      {
        h: "What is an Enforcing rights?", b: "**1. Direct Resolution** — contact retailer first, cheapest and quickest. **2. Alternative Dispute Resolution (ADR)** — third party helps without going to court. **3. Small Claims Procedure** — €25 fee, up to €2,000, no solicitor needed, response in 2 weeks. **4. Ombudsman** — last resort for public services; recommendations only (not legally binding)."
      },
      {
        h: "How do consumer protections differ when shopping in the EU versus non-EU countries?", b: "**EU**: Same consumer rights apply across EU; **European Small Claims Procedure** for cross-border disputes up to €5,000 (€25 fee). **Non-EU**: Limited legal protections, more difficult to enforce rights."
      },
      {
        h: "What are the key responsibilities of a consumer?", b: "**Be informed** — research before buying. **Keep records** — receipts, contracts, warranties. **Use products correctly** — as intended. **Choose ethical/sustainable** options."
      },
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "tf",
        marks: 8,
        prompt: "Mark each TRUE or FALSE: (1) Consumers always have a 14-day cooling-off period for purchases made in physical shops. (2) Digital services bought from EU-based businesses must include the most up-to-date version. (3) Buying from non-EU websites gives consumers the same legal protections as buying from EU retailers. (4) Consumers are only entitled to a repair if a product is faulty within 30 days.",
        model: "**1. FALSE** — The 14-day cooling-off period applies to distance contracts (online, phone, mail, doorstep), not in-store purchases.\n**2. TRUE** — Under the Consumer Rights Act 2022, digital services from EU sellers must include up-to-date versions.\n**3. FALSE** — Non-EU purchases have far weaker protection and are harder to enforce.\n**4. FALSE** — Within 30 days, a consumer is entitled to a full refund. After 30 days but within 12 months they are entitled to a repair or replacement (and refund if these fail).",
        correct: false
      },
      {
        type: "short",
        marks: 8,
        prompt: "Outline two rights a consumer has when they are using a service.",
        model: "**1. Right to a service carried out with due skill, care and diligence**: The provider must complete the work to the standard expected of a competent professional in that field — for example, a mechanic must repair a car correctly using appropriate tools and methods.\n\n**2. Right that the service matches what was agreed or described**: If the business promises certain work, materials or a particular level of service, they must deliver as stated. *Example*: a cleaning service that agreed to clean every room must do so."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Outline two forms of redress available to a consumer for a service that is not carried out appropriately.",
        model: "**1. Refund / Cancellation**: If the service is not provided at all or is not delivered on the agreed date, the consumer can cancel the contract and receive a refund within 14 days of agreement.\n\n**2. Price Reduction or Compensation**: If the service is carried out but not done properly, the consumer may be entitled to a price reduction. If the service caused additional financial loss or damage — for example, a plumber causing flooding — the consumer can claim compensation."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Based on current consumer legislation, explain two forms of redress available for a faulty good.",
        model: "**1. Refund**: If a product is faulty within 30 days of purchase, the consumer is entitled to a full refund. The seller must issue this within 14 days of receiving the returned item.\n\n**2. Repair or Replacement**: If the fault appears after 30 days but within 12 months, the consumer is entitled to a free repair or replacement within a reasonable time and without major inconvenience. If the fault is serious, repair fails, replacement isn't offered, or the cost is excessive, the consumer can request a full or partial refund."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Outline three main functions of the Competition and Consumer Protection Commission (CCPC).",
        model: "**1. Advise and Inform Consumers** — Provides clear information through ccpc.ie and social media to help consumers understand their rights, including simplified explanations of laws like the Consumer Rights Act 2022.\n\n**2. Enforce Consumer Law** — Has legal powers to investigate breaches of consumer legislation, enter premises, and issue on-the-spot fines of €300 where laws are broken.\n\n**3. Publish the Consumer Protection List** — Names businesses that have received compliance notices, been fined or been convicted of consumer offences, helping consumers make informed choices."
      }
    ];
    // 17.2 — Ethics, sustainability and the circular economy
    c.learningOutcomes[1].notes = [
      {
        h: "What are the main ethical concerns consumers should consider?", b: "**Fair treatment of workers** — choosing Fairtrade or ethically sourced products. **Animal welfare** — cruelty-free or vegan (Leaping Bunny logo). **Data protection and online privacy** — limiting data shared, reading privacy policies. **Supporting local businesses** — choosing Irish even at slightly higher prices."
      },
      {
        h: "What are the main sustainability concerns consumers should consider?", b: "**Packaging waste** — choosing recyclable or minimal packaging. **Carbon footprint and transport** — buying locally to reduce emissions. **Overproduction and waste** — avoiding fast fashion, choosing durable goods. **Energy efficiency and resource use** — energy-efficient appliances, LED lighting."
      },
      {
        h: "What is the shadow economy and what are its consequences?", b: "Transactions outside the formal economy, unrecorded by Revenue (tax evasion, undeclared wages, counterfeit goods, dodgy boxes). **Consequences**: For **consumers** — unsafe, unregulated, no legal protection or refund. For **businesses** — legitimate firms undercut by illegal traders. For **government** — loss of tax revenue (VAT, income tax, corporation tax), higher enforcement costs."
      },
      {
        h: "What is the circular economy and how can consumers contribute?", b: "Model of production/consumption that extends product life cycles, reduces waste and creates value. Focuses on re-using, recycling and re-purposing instead of single-use throwaway. **How consumers contribute**: 1. **Buying second-hand** (Depop, Vinted, charity shops, refurbished electronics). 2. **Recycling products** (WEEE recycling for electronics; donating clothing). 3. **Improving consumption habits** (using devices longer, repairing clothes). 4. **Choosing sustainable brands** (energy-efficient appliances, Fairtrade, organic clothing)."
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Describe four ways a consumer purchasing food products can actively contribute to the circular economy. (4 @ 3m)",
        model: "**1. Buying loose/unpackaged products**: Choosing fruit, vegetables and grains sold loose or in bulk reduces single-use packaging waste sent to landfill.\n\n**2. Choosing local and seasonal foods**: Buying locally produced, in-season food reduces the carbon footprint from long-distance transport and supports Irish producers.\n\n**3. Reducing food waste through better habits**: Planning meals, freezing leftovers, and composting peelings extends the life of food and reduces what goes to landfill.\n\n**4. Choosing reusable packaging and refill stations**: Bringing reusable containers to refill shops or buying products in returnable glass containers (e.g. milk in glass bottles) keeps packaging in circulation rather than throwing it away after one use."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Outline two consequences of participation in the shadow economy: (i) for the consumer, (ii) for the economy.",
        model: "**(i) For the consumer**:\n**1. No legal protection** — Goods bought through the shadow economy are unregulated, so the consumer has no right to a refund, repair or replacement if something goes wrong.\n**2. Unsafe products** — Items like 'dodgy boxes' or counterfeit electronics may not meet safety standards, putting the consumer at risk of fire, electric shock or other harm.\n\n**(ii) For the economy**:\n**1. Loss of tax revenue** — VAT, income tax and corporation tax are not paid on shadow transactions, reducing funds available for public services like health and education.\n**2. Higher enforcement costs** — The government must spend more on inspections, Revenue investigations and prosecution to tackle illegal trading, putting further strain on public finances."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Explain the term 'circular economy' and describe two ethical concerns of Irish consumers when purchasing from online retailers.",
        model: "**Circular economy**: A model of production and consumption that extends the life cycle of products, reduces waste and creates further value. It focuses on reusing, recycling and re-purposing items rather than single-use disposal — moving away from 'buy, use once, throw away'.\n\n**Ethical concerns when buying online**:\n**1. Fair treatment of workers** — Consumers may be concerned that fast fashion or cheap imports rely on unfair wages or poor conditions; many now check whether brands publish information on factory conditions before buying.\n**2. Data protection and online privacy** — Consumers worry about how online retailers collect and use their personal data, including tracking, cookies and targeted ads, and may avoid retailers with poor privacy practices."
      }
    ];
    // 17.3 — Impact of digital technology on consumer behaviour
    c.learningOutcomes[2].notes = [
      {
        h: "What are the positive impacts of digital technology on consumer behaviour?", b: "**Increased convenience** — Amazon one-click, mobile banking. **Better access to information** — comparison tools (Bonkers.ie, ccpc.ie). **Greater choice** — wider product range from Irish/international sellers. **Price transparency**, **customer reviews/ratings** (Trustpilot), **improved accessibility** (rural areas, mobility issues)."
      },
      {
        h: "What are the negative impacts of digital technology on consumer behaviour?", b: "**Impulse buying and overconsumption** — shopping apps, targeted ads, influencer marketing. **Reduced social interaction** — physical stores closing. **Increased screen time and digital addiction** — TikTok/Instagram driving spending. **Information overload (paradox of choice)**, greater exposure to scams/fraud, reduced privacy (tracking, cookies)."
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Analyse three ways digital technology can influence consumer behaviour. (3 @ 4m)",
        model: "**1. Increased Convenience**: Online platforms like Amazon offer one-click purchasing and next-day delivery, while mobile banking apps allow instant transfers without visiting a branch. Consumers now expect speed and ease as a baseline, and are likely to abandon retailers whose websites or checkouts are clunky.\n\n**2. Better-informed Decisions**: Consumers can compare prices, features and reviews before buying — for example using Bonkers.ie for broadband or Trustpilot for product reviews. This shifts power towards consumers, making them more price-sensitive and more likely to choose based on objective evidence rather than advertising.\n\n**3. Impulse Buying and Overconsumption**: Constant access to shopping apps, targeted ads and influencer marketing leads to unplanned purchases. Social media platforms allow direct purchases through influencer posts, encouraging spending that consumers might otherwise have considered more carefully — leading to financial strain and overconsumption."
      },
      {
        type: "short",
        marks: 6,
        prompt: "Evaluate two negative impacts of digital technology on consumer behaviour.",
        model: "**1. Impulse buying and overconsumption** has been amplified by 24/7 access to shopping apps and targeted advertising. Consumers may regret unplanned purchases and accumulate debt. While technology offers convenience, it also makes it harder for consumers to control spending, especially when influencer marketing and limited-time offers create urgency.\n\n**2. Reduced privacy** is a serious concern, as websites track behaviour through cookies and apps collect personal data for resale or targeted ads. Consumers often share data without realising the extent. The balance is therefore mixed — digital technology empowers consumers with information, but it can also exploit them. Effective regulation (like GDPR) and consumer education are essential to manage these risks."
      }
    ];
    // 17.4 — Personal data protection — GDPR
    c.learningOutcomes[3].notes = [
      {
        h: "What is GDPR and what does it cover?", b: "EU regulation across all member states including Ireland. Sets out: rights of data subjects, responsibilities of data controllers, role of Data Protection Commissioner (DPC)."
      },
      {
        h: "What is a data subject under GDPR?", b: "The individual whose data is collected. Personal data = anything that can identify them (name, passport, financial records, address, employment details)."
      },
      {
        h: "Rights of data subjects",
        b: "**1. Right not to be subject to automated decision-making** — important decisions (creditworthiness, performance ratings) cannot be made solely by AI without consent. **2. Right to complain** to the DPC. **3. Right of access, correction, and erasure** ('right to be forgotten') — request a copy, correct inaccuracies, delete data (e.g. TikTok account)."
      },
      {
        h: "What are the responsibilities of data controllers (businesses) under GDPR?", b: "**1. Report data breaches** to DPC within 72 hours (e.g. bank notifies DPC and customers). **2. Keep data safe and secure** with encryption, restricted access (e.g. healthcare patient records)."
      },
      {
        h: "What are the functions and powers of the Data Protection Commissioner?", b: "Investigates complaints, informs people of rights, conducts investigations (Meta, Google, Apple, WhatsApp, LinkedIn), promotes compliance, identifies risks. **Penalties**: up to €20 million or 4% of global annual turnover, whichever is higher. *Example*: 2023 — Meta fined €1.2 billion for unlawful EU→US data transfers."
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 6,
        prompt: "Based on current EU law, outline two rights consumers have in relation to protection of their personal data.",
        model: "**1. Right of Access, Correction and Erasure**: Individuals can request a copy of the data a business holds about them, ask for inaccurate data to be corrected, and ask for their data to be erased — known as the 'right to be forgotten'. *Example*: a TikTok user can request that their account and all associated data be deleted.\n\n**2. Right not to be subject to automated decision-making**: Important decisions, such as creditworthiness or job application screening, cannot be made solely by automated systems without the individual's consent. Consumers have the right to a human being involved in decisions that significantly affect them."
      },
      {
        type: "short",
        marks: 8,
        prompt: "Identify two responsibilities of data controllers under GDPR.",
        model: "**1. Report data breaches within 72 hours**: Businesses must notify the Data Protection Commissioner of any personal data breach within 72 hours of becoming aware of it, and inform affected customers if there is a high risk to their rights. *Example*: a bank must inform the DPC and customers if customer data is hacked.\n\n**2. Keep data safe and secure**: Businesses must implement appropriate technical and organisational security measures to protect personal data, such as encryption, restricted access and secure storage. *Example*: healthcare organisations using encryption and limited access for patient records."
      },
      {
        type: "short",
        marks: 5,
        prompt: "Evaluate the role of the Data Protection Commissioner (DPC).",
        model: "The DPC plays a critical role in enforcing GDPR in Ireland. **Strengths**: It has strong penalty powers — fines up to €20 million or 4% of global turnover — and has used them, fining Meta €1.2 billion in 2023 for unlawful EU-to-US data transfers. It investigates complaints, conducts independent investigations into giants like Google, Apple and LinkedIn, and educates the public on their rights. **Limitations**: As Ireland hosts the EU HQ of many big tech firms, the DPC handles a vast caseload that can lead to delays. Some campaigners have criticised the speed of its enforcement. **Overall**: the DPC is essential to GDPR enforcement and creates a strong incentive for businesses to handle data correctly, but its effectiveness depends on resourcing and case turnaround."
      }
    ];
    // 17.5 — Importance of making informed consumer decisions
    c.learningOutcomes[4].notes = [
      {
        h: "What is meant by being an informed consumer?", b: "Having the knowledge and understanding of the impact of your decisions, and the skills to make choices in your best interest around price, value, quality and ethics."
      },
      {
        h: "Why is making informed consumer decisions important?", b: "**Improves financial wellbeing** — comparing prices, quality and long-term costs avoids unnecessary spending. **Improves safety** — buying from legitimate, certified providers reduces risk of unsafe products. **Improves legal protection** — knowing rights increases the chance of refund/repair (buying from registered businesses, not the shadow economy). **Positive social and environmental impact** — supports ethical brands and reduces environmental harm (Fairtrade, locally produced)."
      }
    ];
    c.learningOutcomes[4].questions = [
      {
        type: "short",
        marks: 12,
        prompt: "Discuss three reasons why making informed consumer decisions is important. (3 @ 4m)",
        model: "**1. Improves Financial Wellbeing**: By comparing prices, quality and long-term costs, consumers avoid unnecessary spending. *Example*: comparing total mortgage repayments between lenders before signing can save thousands of euro over the life of the loan.\n\n**2. Improves Legal Protection**: Knowing your consumer rights increases the chance of receiving a refund, repair or replacement if something goes wrong. Buying from registered Irish businesses rather than the shadow economy means you have legal recourse through the CCPC, Small Claims Court and Consumer Rights Act 2022.\n\n**3. Positive Social and Environmental Impact**: Informed consumers can support ethical brands and reduce environmental harm. *Example*: choosing Fairtrade chocolate or locally produced food lowers carbon impact and supports fair worker treatment, encouraging more businesses to adopt sustainable practices."
      }
    ];
  })();

})();