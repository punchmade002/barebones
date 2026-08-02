// Geography HL Content — notes, concept points and flashcards for all chapters.
// Past-paper exam questions live in exam-questions-db.js.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  function ch(id) { return COURSE_DATA.chapters.find(function (c) { return c.id === id; }); }

  // ── geo1: Plate Tectonics ─────────────────────────────────────────────────
  (function () {
    var c = ch("geo1");
    // 1.1 — Theory of Plate Tectonics
    c.learningOutcomes[0].notes = [
      {
        h: "Continental Drift (Wegener)",
        b: "Alfred Wegener proposed Earth's crust is divided into large moving plates. Evidence 1: matching plant and animal fossils on opposite continents. Evidence 2: matching fold mountains (Appalachians and Caledonian Mountains). Evidence 3: continental fit — South America and Africa fit together like a jigsaw."
      },
      {
        h: "Sea Floor Spreading & Mantle Convection",
        b: "Harry Hess (1960): new ocean floor forms at mid-ocean ridges as plates diverge. Sea floor rocks are older the further they are from divergent boundaries. Arthur Holmes (1928): mantle convection — heat from the inner core causes hot rock to rise, driving plate movement."
      },
      {
        h: "Driving Forces",
        b: "Convection currents: heat from inner core pushes hot rock up, cooler rock circulates, moving plates. Slab pull: subducting plate edge drags the rest of the plate with it. Ridge push: tension at divergent boundaries causes plates to swell and push apart. Plates move at 2–15 cm per year."
      },
      {
        h: "Plate Boundaries",
        b: "Divergent: plates separate — e.g. Mid-Atlantic Ridge, forming Iceland. Convergent (destructive): plates collide — forms trenches, fold mountains, volcanoes. Transform: plates slide past each other — e.g. San Andreas Fault; crust is neither created nor destroyed."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the inner core?",
        definition: "Solid ball of ~90% iron with nickel and sulphur, ~1,220 km thick; temperature ~5,500°C — as hot as the surface of the sun.",
        section: "1.1"
      },
      {
        term: "What is the outer core?",
        definition: "Fluid layer of iron and nickel above the inner core, ~2,400 km thick; temperature 3,000–4,000°C.",
        section: "1.1"
      },
      {
        term: "What is the mantle?",
        definition: "Layer of rock between the crust and outer core, ~2,900 km thick; mostly solid but behaves as a viscous fluid under long timescales.",
        section: "1.1"
      },
      {
        term: "What is the asthenosphere?",
        definition: "Soft, ductile layer of the upper mantle on which tectonic plates float and move.",
        section: "1.1"
      },
      {
        term: "What is the lithosphere?",
        definition: "Rigid outer layer of Earth comprising the crust and upper mantle; divided into tectonic plates.",
        section: "1.1"
      },
      {
        term: "What are tectonic plates?",
        definition: "Large segments of Earth's crust and upper mantle that move above the asthenosphere; seven major plates cover ~95% of Earth's surface.",
        section: "1.1"
      },
      {
        term: "What is continental drift?",
        definition: "Wegener's theory that all continents were once a single landmass called Pangaea that broke apart and drifted to their current positions.",
        section: "1.2"
      },
      {
        term: "What is Pangaea?",
        definition: "Wegener's proposed supercontinent from which all present continents separated; supported by matching fossils, rock folds and continental fit.",
        section: "1.2"
      },
      {
        term: "What is mantle convection?",
        definition: "Arthur Holmes' 1928 theory that heat-driven circulation of magma in the mantle drives plate movement.",
        section: "1.2"
      },
      {
        term: "How does seafloor spreading work?",
        definition: "Process introduced by Harry Hess (1960) at divergent boundaries: magma rises as plates separate, new oceanic crust forms and cools symmetrically on both sides of the ridge.",
        section: "1.3"
      },
      {
        term: "What is slab-pull?",
        definition: "Primary mechanism of plate movement (~90%); denser oceanic plate sinks into the mantle due to negative buoyancy, pulling the rest of the plate with it.",
        section: "1.4"
      },
      {
        term: "What is ridge-push?",
        definition: "Secondary mechanism of plate movement (~10%); upwelling mantle rock at mid-ocean ridges creates positive buoyancy that pushes plates apart.",
        section: "1.4"
      },
      {
        term: "What are mantle plumes?",
        definition: "Large columns of hot rock rising through the mantle with positive buoyancy; form volcanic hotspots and are a driving force of mantle convection.",
        section: "1.4"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Discuss the theory of plate tectonics.",
        model: "Continental Drift: Alfred Wegener proposed that Earth's crust is divided into large moving plates. Evidence included matching plant and animal fossils found on opposite sides of the Atlantic. Matching fold mountains — the Appalachians and the Caledonian Mountains — suggested the continents were once joined. The continental fit of South America and Africa, fitting together like a jigsaw, provided further supporting evidence. Sea Floor Spreading: Harry Hess (1960) proposed that new ocean floor forms at mid-ocean ridges as plates diverge. Sea floor rocks are progressively older the further they are from divergent plate boundaries. Arthur Holmes (1928) argued that mantle convection currents are the mechanism driving plate movement. Heat from the inner core causes hot rock to rise, circulate and drag the plates above it. Driving Forces: Convection currents — hot mantle rock rises, cooler rock sinks, creating a circulation cell that moves plates. Slab pull — the dense subducting plate edge drags the rest of the plate down into the mantle. Ridge push — tension at divergent boundaries causes plates to swell upward and push apart. Plates move at approximately 2–15 cm per year, comparable to the rate of human fingernail growth. Plate Boundaries: Divergent boundaries — plates separate, forming new oceanic crust, e.g. Mid-Atlantic Ridge, with Iceland as a surface example. Convergent (destructive) boundaries — plates collide, forming ocean trenches, fold mountains and volcanoes. Transform boundaries — plates slide laterally past each other, e.g. San Andreas Fault, California; crust is neither created nor destroyed at these boundaries."
      }
    ];
    // 1.2 — Destructive (Convergent) Plate Boundaries
    c.learningOutcomes[1].notes = [
      {
        h: "Oceanic–Oceanic",
        b: "The older, denser plate subducts beneath the other into the mantle. A deep ocean trench forms at the subduction zone (up to 8 km deep). Rock and sediment build up an accretionary wedge at the boundary. As the descending plate melts, magma rises — forming island arc volcanoes (e.g. Japan)."
      },
      {
        h: "Oceanic–Continental",
        b: "The denser oceanic plate subducts under the lighter continental plate. Compression forces thrust the coastal edge of the continental plate upward. Fold mountains form through orogeny — e.g. The Andes (Nazca and South American plates). Melting of the subducting plate produces magma chambers and explosive stratovolcanoes along the continental margin."
      },
      {
        h: "Continental–Continental",
        b: "Neither plate subducts as both are composed of light continental crust. Huge compression forces fold and thrust sedimentary rock upward. Major fold mountain ranges form — e.g. The Himalayas (Indian and Eurasian plates, colliding ~50 mya). No volcanic activity typically occurs; earthquakes are common due to compression stress."
      }
    ];
    c.learningOutcomes[1].keyTerms = [
      {
        term: "What is a convergent plate boundary?",
        definition: "Plate boundary where two tectonic plates collide; also called a destructive plate boundary. Three types: oceanic-oceanic, oceanic-continental, continental-continental.",
        section: "1.2"
      },
      {
        term: "What happens during subduction?",
        definition: "Process at convergent boundaries where a denser oceanic plate sinks beneath a less dense plate into the asthenosphere and melts at approximately 100 km depth.",
        section: "1.2"
      },
      {
        term: "What is an ocean trench?",
        definition: "Deep, narrow depression in the ocean floor formed where a plate subducts; typically 50–100 km wide and ~8 km deep.",
        section: "1.2"
      },
      {
        term: "What is orogeny?",
        definition: "Mountain-building process driven by compression forces and collision between two tectonic plates at convergent boundaries.",
        section: "1.2"
      },
      {
        term: "What is an accretionary wedge?",
        definition: "Build-up of sediment scraped from the ocean floor and compressed against the continental plate edge as an oceanic plate subducts.",
        section: "1.2"
      },
      {
        term: "What is an oceanic-continental boundary?",
        definition: "Convergent boundary where dense oceanic plate subducts beneath lighter continental plate; forms fold mountains, ocean trenches and volcanoes. Example: Nazca and South American plates → Andes.",
        section: "1.2"
      },
      {
        term: "What is a continental-continental boundary?",
        definition: "Convergent boundary where two continental plates collide; neither subducts so rock is forced upward into fold mountains. Example: Indian and Eurasian plates → Himalayas.",
        section: "1.2"
      },
      {
        term: "What is an oceanic-oceanic boundary?",
        definition: "Convergent boundary between two oceanic plates; older, denser plate subducts, forming a deep trench and island arc of volcanoes. Example: Pacific and Philippine plates.",
        section: "1.2"
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Describe and explain destructive (convergent) plate boundaries.",
        model: "Oceanic–Oceanic: The older, denser oceanic plate subducts beneath the younger, less dense plate and sinks into the mantle. A deep ocean trench forms at the subduction zone, reaching depths of up to 8 km. Rock and sediment scraped off the descending plate build up an accretionary wedge at the boundary. As the descending plate melts in the mantle, magma rises through the overlying crust. Island arc volcanoes form above the subduction zone — for example, Japan and the Philippine island chain. Oceanic–Continental: The denser oceanic plate subducts beneath the lighter continental plate due to the density difference. Compression forces thrust the coastal edge of the continental plate upward through orogeny. Fold mountains form along the continental margin — for example, the Andes, formed by the Nazca and South American plates. Explosive stratovolcanoes form above the subduction zone along the continental margin. Continental–Continental: Neither plate subducts as both are composed of relatively light continental crust. Huge compression forces fold and thrust sedimentary rock layers upward through intense orogeny. Major fold mountain ranges form — for example, the Himalayas, formed by the Indian and Eurasian plates colliding approximately 50 million years ago. Mount Everest (8,848 m) is still rising as the plates continue to converge. No volcanic activity typically occurs at continental-continental boundaries as no plate melts. Earthquakes are common and powerful due to the immense compression stress between the colliding plates."
      }
    ];
    // 1.3 — Constructive (Divergent) Plate Boundaries
    c.learningOutcomes[2].notes = [
      {
        h: "What Happens at Divergent Boundaries",
        b: "Plates move apart driven by ridge push and mantle convection currents. Fissures form in the thinning crust as plates separate. Magma rises through the fissures — creating new oceanic crust. New crust forms symmetrically on both sides of the ridge."
      },
      {
        h: "Mid-Ocean Ridges",
        b: "Continuous chains of underwater mountains and volcanoes — make up 90% of all mountains on Earth. The Mid-Atlantic Ridge runs from north to south beneath the Atlantic Ocean. Iceland sits on the Mid-Atlantic Ridge — a visible example of a divergent boundary above sea level. Basic (low-silica) lava is produced — runny, non-explosive, forms gently sloping shield volcanoes."
      },
      {
        h: "Continental Rift Zones",
        b: "When divergent forces act on continental crust, rift valleys form. The East African Rift Valley is a current example — eastern Africa is slowly pulling away from the rest of the continent. Eventually the rift widens, sea water floods in, and a new ocean forms — the Red Sea is an early stage of this process. Earthquakes along divergent boundaries are shallow (less than 30 km) and relatively moderate in magnitude."
      }
    ];
    c.learningOutcomes[2].keyTerms = [
      {
        term: "What is a divergent plate boundary?",
        definition: "Plate boundary where tectonic plates move apart; also called a constructive plate boundary. New crust is created as magma fills the gap.",
        section: "1.3"
      },
      {
        term: "What is a continental rift zone?",
        definition: "Divergent boundary on continental crust where plates separate; the crust thins, drops below sea level and may eventually form a mid-ocean ridge.",
        section: "1.3"
      },
      {
        term: "What is a mid-ocean ridge?",
        definition: "Extensive underwater mountain chain at divergent boundaries where new basalt crust is created; stretches ~65,000 km globally and makes up 90% of mountain ranges on Earth.",
        section: "1.3"
      },
      {
        term: "What is basic lava?",
        definition: "Hot, runny lava low in silica content that erupts at mid-ocean ridges and divergent boundaries; cools to form basalt.",
        section: "1.3"
      },
      {
        term: "What is a transform plate boundary?",
        definition: "Boundary where plates slide past each other laterally; Earth's crust is neither created nor destroyed. Creates fault lines and shallow earthquakes. Example: San Andreas Fault.",
        section: "1.3"
      },
      {
        term: "What is a fault line?",
        definition: "Fracture in Earth's crust where rocks are displaced by compression, tension or shearing forces.",
        section: "1.3"
      },
      {
        term: "Ireland's Tectonic Journey",
        definition: "Ireland's geology shaped by closure of the Iapetus Ocean (Caledonian folding, ~400 Ma), Armorican folding (~300 Ma), and Atlantic divergence (~65 Ma) creating the Antrim-Derry basalt plateau.",
        section: "1.4"
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Describe and explain constructive (divergent) plate boundaries.",
        model: "Plates move apart driven by ridge push and mantle convection currents beneath the lithosphere. Fissures form in the thinning crust as the plates separate along divergent boundaries. Magma rises through the fissures from the mantle below, reaching the surface. New oceanic crust is formed symmetrically on both sides of the ridge as the magma solidifies. Mid-Ocean Ridges: Mid-ocean ridges are continuous chains of underwater mountains and volcanoes formed by divergent activity. They make up approximately 90% of all mountains on Earth when measured by length. The Mid-Atlantic Ridge runs from north to south beneath the entire Atlantic Ocean. Iceland sits on the Mid-Atlantic Ridge, making it a visible surface example of a divergent plate boundary above sea level. Basic (low-silica) lava is produced at divergent boundaries — runny and non-explosive, forming gently sloping shield volcanoes. Earthquakes at mid-ocean ridges are shallow (less than 30 km deep) and relatively moderate in magnitude. Continental Rift Zones: When divergent forces act on continental crust rather than oceanic crust, rift valleys form. The East African Rift Valley is a current active example — eastern Africa is slowly pulling away from the rest of the continent. As the rift widens further, sea water floods in and a new ocean basin begins to form. The Red Sea is an early stage of this process — a narrow sea formed by continued rifting between the African and Arabian plates. Eventually, over millions of years, a full ocean can develop — as the Atlantic did when Pangaea split apart."
      }
    ];
    c.examQuestions = [
      {
        id: "geo1-eq-1",
        source: "LC Geography — Sample 2019",
        parts: [
          {
            label: "Q1.",
            question: "Discuss the theory of plate tectonics.",
            marks: 30,
            model: "Continental Drift: Alfred Wegener proposed that Earth's crust is divided into large moving plates. Evidence included matching plant and animal fossils found on opposite sides of the Atlantic. Matching fold mountains — the Appalachians and the Caledonian Mountains — suggested the continents were once joined. The continental fit of South America and Africa, fitting together like a jigsaw, provided further supporting evidence. Sea Floor Spreading: Harry Hess (1960) proposed that new ocean floor forms at mid-ocean ridges as plates diverge. Sea floor rocks are progressively older the further they are from divergent plate boundaries. Arthur Holmes (1928) argued that mantle convection currents are the mechanism driving plate movement. Heat from the inner core causes hot rock to rise, circulate and drag the plates above it. Driving Forces: Convection currents — hot mantle rock rises, cooler rock sinks, creating a circulation cell that moves plates. Slab pull — the dense subducting plate edge drags the rest of the plate down into the mantle. Ridge push — tension at divergent boundaries causes plates to swell upward and push apart. Plates move at approximately 2–15 cm per year, comparable to the rate of human fingernail growth. Plate Boundaries: Divergent boundaries — plates separate, forming new oceanic crust, e.g. Mid-Atlantic Ridge, with Iceland as a surface example. Convergent (destructive) boundaries — plates collide, forming ocean trenches, fold mountains and volcanoes. Transform boundaries — plates slide laterally past each other, e.g. San Andreas Fault, California; crust is neither created nor destroyed at these boundaries.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo1-eq-2",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q2.",
            question: "Describe and explain destructive (convergent) plate boundaries.",
            marks: 30,
            model: "Oceanic–Oceanic: The older, denser oceanic plate subducts beneath the younger, less dense plate and sinks into the mantle. A deep ocean trench forms at the subduction zone, reaching depths of up to 8 km. Rock and sediment scraped off the descending plate build up an accretionary wedge at the boundary. As the descending plate melts in the mantle, magma rises through the overlying crust. Island arc volcanoes form above the subduction zone — for example, Japan and the Philippine island chain. Oceanic–Continental: The denser oceanic plate subducts beneath the lighter continental plate due to the density difference. Compression forces thrust the coastal edge of the continental plate upward through orogeny. Fold mountains form along the continental margin — for example, the Andes, formed by the Nazca and South American plates. Explosive stratovolcanoes form above the subduction zone along the continental margin. Continental–Continental: Neither plate subducts as both are composed of relatively light continental crust. Huge compression forces fold and thrust sedimentary rock layers upward through intense orogeny. Major fold mountain ranges form — for example, the Himalayas, formed by the Indian and Eurasian plates colliding approximately 50 million years ago. Mount Everest (8,848 m) is still rising as the plates continue to converge. No volcanic activity typically occurs at continental-continental boundaries as no plate melts. Earthquakes are common and powerful due to the immense compression stress between the colliding plates.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo1-eq-3",
        source: "LC Geography — Sample 2020",
        parts: [
          {
            label: "Q3.",
            question: "Describe and explain constructive (divergent) plate boundaries.",
            marks: 30,
            model: "Plates move apart driven by ridge push and mantle convection currents beneath the lithosphere. Fissures form in the thinning crust as the plates separate along divergent boundaries. Magma rises through the fissures from the mantle below, reaching the surface. New oceanic crust is formed symmetrically on both sides of the ridge as the magma solidifies. Mid-Ocean Ridges: Mid-ocean ridges are continuous chains of underwater mountains and volcanoes formed by divergent activity. They make up approximately 90% of all mountains on Earth when measured by length. The Mid-Atlantic Ridge runs from north to south beneath the entire Atlantic Ocean. Iceland sits on the Mid-Atlantic Ridge, making it a visible surface example of a divergent plate boundary above sea level. Basic (low-silica) lava is produced at divergent boundaries — runny and non-explosive, forming gently sloping shield volcanoes. Earthquakes at mid-ocean ridges are shallow (less than 30 km deep) and relatively moderate in magnitude. Continental Rift Zones: When divergent forces act on continental crust rather than oceanic crust, rift valleys form. The East African Rift Valley is a current active example — eastern Africa is slowly pulling away from the rest of the continent. As the rift widens further, sea water floods in and a new ocean basin begins to form. The Red Sea is an early stage of this process — a narrow sea formed by continued rifting between the African and Arabian plates. Eventually, over millions of years, a full ocean can develop — as the Atlantic did when Pangaea split apart.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── geo2: Volcanoes & Earthquakes ─────────────────────────────────────────
  (function () {
    var c = ch("geo2");
    // 2.1 — Positive Impacts of Volcanoes
    c.learningOutcomes[0].notes = [
      {
        h: "Fertile Soils",
        b: "Volcanic ash (tephra) is rich in minerals such as potassium and phosphorus — breaks down into highly fertile soils over time. The slopes of Mount Etna (Sicily) support intensive viticulture and citrus farming due to volcanic soils. Java, Indonesia — one of the world's most densely farmed islands due to fertile volcanic soils from nearby active volcanoes."
      },
      {
        h: "Geothermal Energy",
        b: "Volcanic regions have geothermal energy potential — magma heats underground water, harnessed for electricity and heating. Iceland generates almost 100% of its heating and ~30% of its electricity from geothermal energy — derived from its position on the Mid-Atlantic Ridge. Geothermal energy is clean, renewable, and reduces dependence on fossil fuels."
      },
      {
        h: "Tourism & Mineral Wealth",
        b: "Volcanic landscapes attract significant tourism — e.g. Hawaii's shield volcanoes, the Canary Islands, Iceland's geysers and lava fields. Volcanic regions are associated with mineral deposits — gold, silver, copper and diamonds found near igneous rock formations. The Antrim-Derry Lava Plateau (Giant's Causeway) is a UNESCO World Heritage Site attracting 600,000+ visitors per year to Ireland."
      },
      {
        h: "Land Creation",
        b: "Successive lava flows build up new land above sea level — the Hawaiian Islands were entirely formed by hotspot volcanic activity. The island of Surtsey (Iceland) emerged from the ocean in 1963 through underwater volcanic eruptions. The Antrim-Derry Plateau was built up over 2 million years of fissure eruptions, forming a lava landscape up to 1,800 m thick."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is geothermal energy?",
        definition: "Energy harnessed from heat stored in Earth's crust; converted to electricity and heating. Exploited in volcanic regions like Iceland and Hawaii.",
        section: "2.1"
      },
      {
        term: "What are fertile volcanic soils?",
        definition: "Mineral-rich soils (magnesium, potassium) produced by volcanic eruptions; highly porous and productive for agriculture.",
        section: "2.1"
      },
      {
        term: "What is volcanic tourism?",
        definition: "Tourism centred on visiting active, dormant or extinct volcanic landscapes; includes geotourism and ecotourism. Pompeii is a famous example.",
        section: "2.1"
      },
      {
        term: "What is an active volcano?",
        definition: "Volcano that has erupted in the past 10,000 years.",
        section: "2.1"
      },
      {
        term: "What is a dormant volcano?",
        definition: "Volcano that has not erupted in 10,000+ years but is expected to erupt again in the future.",
        section: "2.1"
      },
      {
        term: "What is an extinct volcano?",
        definition: "Volcano that has not erupted in human history and is never expected to erupt again.",
        section: "2.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Discuss the positive impacts of volcanoes.",
        model: "Fertile Soils: Volcanic ash (tephra) is rich in minerals such as potassium and phosphorus, which break down into highly fertile soils over time. The slopes of Mount Etna in Sicily support intensive viticulture and citrus farming due to these volcanic soils. Java, Indonesia is one of the world's most densely farmed islands due to the highly fertile volcanic soils from nearby active volcanoes. Farmers continue to live near active volcanoes because the agricultural productivity outweighs the risk. Geothermal Energy: Volcanic regions have significant geothermal energy potential — magma heats underground water, which is harnessed for electricity generation and heating. Iceland generates almost 100% of its space heating and approximately 30% of its electricity from geothermal energy. Iceland's geothermal advantage stems from its position on the Mid-Atlantic Ridge, where volcanic activity is especially intense. Geothermal energy is clean, renewable and reduces dependence on fossil fuels, lowering carbon emissions. Tourism and Mineral Wealth: Volcanic landscapes attract significant tourism — Hawaii's shield volcanoes, the Canary Islands and Iceland's geysers and lava fields are globally renowned. Volcanic regions are associated with mineral deposits including gold, silver, copper and diamonds near igneous rock formations. The Giant's Causeway on the Antrim-Derry Plateau is a UNESCO World Heritage Site attracting over 600,000 visitors per year to Ireland. Land Creation: Successive lava flows build up new land above sea level — the Hawaiian Islands were entirely formed by hotspot volcanic activity over millions of years. The island of Surtsey off Iceland emerged from the ocean in 1963 through underwater volcanic eruptions. The Antrim-Derry Plateau in northeast Ireland was built up over approximately 2 million years of fissure eruptions. The plateau reaches up to 1,800 m in thickness and constitutes one of Europe's largest and best-preserved lava plateau landscapes."
      }
    ];
    // 2.2 — Global Distribution of Volcanoes
    c.learningOutcomes[1].notes = [
      {
        h: "Divergent Boundaries",
        b: "At divergent boundaries, plates separate and fissures allow magma to rise — creating volcanoes along mid-ocean ridges. Basic lava (low silica) rises at these boundaries — non-explosive, forming shield volcanoes. Iceland sits on the Mid-Atlantic Ridge — a surface example of divergent boundary volcanism."
      },
      {
        h: "Convergent Boundaries",
        b: "The heavier plate subducts and melts — magma rises to form a magma chamber in the overlying crust. High silica content makes this magma viscous and volatile — produces explosive composite (strato) volcanoes. Volcanoes form along the continental margin or as island arcs — e.g. the Andes (Nazca/South American) and Japan."
      },
      {
        h: "Hotspots",
        b: "Over 40 global hotspots exist, many away from plate boundaries — explained by plumes of magma (diapirs) rising from the mantle. The hotspot burns through the oceanic plate — successive volcanic islands form as the plate moves over it. Example: Hawaiian island chain — oldest islands furthest from the current hotspot, youngest still forming over it."
      },
      {
        h: "Ring of Fire",
        b: "~75% of all volcanoes are located in the Ring of Fire — the boundary of the Pacific Plate — explained by multiple convergent subduction zones. Plate tectonics explains why volcanoes cluster at plate boundaries rather than being randomly distributed. Intraplate volcanoes (hotspots) are the exception — explained by mantle plumes rather than plate boundary processes."
      }
    ];
    c.learningOutcomes[1].keyTerms = [
      {
        term: "What is the Ring of Fire?",
        definition: "Horseshoe-shaped zone around the Pacific Ocean with the world's highest concentration of volcanic and seismic activity; located along convergent plate boundaries.",
        section: "2.2"
      },
      {
        term: "What is a hotspot?",
        definition: "Isolated volcanic area not at a plate boundary, caused by a mantle plume burning through thin oceanic plate. Forms chains of volcanic islands as the plate moves. Example: Hawaii.",
        section: "2.2"
      },
      {
        term: "What is a composite cone (stratovolcano)?",
        definition: "Steep cone-shaped volcano built from alternating layers of lava and pyroclastic material; forms at convergent boundaries; characterised by explosive eruptions.",
        section: "2.2"
      },
      {
        term: "What is a shield volcano?",
        definition: "Broad, low-profile volcano formed from basic lava that flows easily; typically at hotspots or divergent boundaries; non-explosive eruptions.",
        section: "2.2"
      },
      {
        term: "What is a cinder cone?",
        definition: "Smallest, most common volcanic landform; steep-sided with a wide crater; forms from explosive eruptions of pyroclastic material; generally erupts only once.",
        section: "2.2"
      },
      {
        term: "What is a pyroclastic flow?",
        definition: "Fast-moving mixture of hot rock fragments, gases and ash that rushes down a volcano's slopes after an explosive eruption.",
        section: "2.2"
      },
      {
        term: "What is a caldera?",
        definition: "Large depression formed when a volcano's magma chamber empties and the surface collapses; can fill with rainwater to form a caldera lake.",
        section: "2.2"
      },
      {
        term: "What is a lava plateau?",
        definition: "Flat landform built up by repeated fissure eruptions of basic lava solidifying over a large area in successive layers.",
        section: "2.2"
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Explain how the study of plate tectonics has helped us to understand the global distribution of volcanoes.",
        model: "Divergent Boundaries: At divergent plate boundaries, plates separate and fissures allow magma to rise from the mantle below. New oceanic crust forms at mid-ocean ridges, and volcanic activity is continuous along these boundaries. Basic lava with low silica content rises at divergent boundaries — it is runny and non-explosive, forming gently sloping shield volcanoes. Iceland sits on the Mid-Atlantic Ridge and is the most prominent surface example of divergent boundary volcanism above sea level. Convergent Boundaries: At convergent boundaries, the heavier oceanic plate subducts beneath the lighter plate and melts in the mantle. Magma rises through the overlying crust and collects in a magma chamber — eventually erupting at the surface. High silica content makes this magma viscous and volatile — it produces explosive composite stratovolcanoes with violent eruptions. Volcanoes form along the continental margin or as island arcs — e.g. the Andes (Nazca and South American plates) and Japan's island arc chain. Hotspots: Over 40 global hotspots exist, many located far from plate boundaries — explained by plumes of magma rising from deep in the mantle. The hotspot burns through the oceanic plate above it as the plate moves — successive volcanic islands form in a chain. The Hawaiian island chain is the classic example — the oldest islands are furthest from the current hotspot, the youngest are still forming directly over it. Ring of Fire: Approximately 75% of all the world's volcanoes are located in the Ring of Fire around the boundary of the Pacific Plate. This concentration is explained by the multiple convergent subduction zones encircling the Pacific. Plate tectonics explains why volcanoes cluster at plate boundaries rather than being randomly distributed across Earth's surface. Intraplate volcanoes at hotspots are the exception — explained by mantle plumes rising through the interior of a plate rather than at its boundary."
      }
    ];
    // 2.3 — Global Distribution of Fold Mountains
    c.learningOutcomes[2].notes = [
      {
        h: "Caledonian Orogeny (~400 mya)",
        b: "North American and Eurasian plates collided — continental-continental convergence forced overlying rock upward. Formed the oldest mountains in Ireland — e.g. Sugarloaf, Co. Wicklow. Also formed the Scottish Highlands and Scandinavian Mountains — evidence of the same orogeny across separated landmasses."
      },
      {
        h: "Armorican Orogeny (~250 mya)",
        b: "African and Eurasian plates collided — compression forces produced 3,000 km of mountains across Europe. Formed the Munster Ridge and Valley — e.g. Macgillycuddy's Reeks, stretching across Ireland, Portugal, England and Germany. Associated rock types: quartzite, shale and marble — formed under high pressure and heat."
      },
      {
        h: "Alpine Orogeny (~60 mya — ongoing)",
        b: "Indo-Australian and Eurasian plates collided — forming the Himalayas. Mount Everest (8,848 m) — world's highest peak, still rising as subduction continues. Nazca and South American plates — forming the Andes (~50 mya), the world's longest mountain range. Fold mountains cluster at convergent plate boundaries worldwide — entirely explained by plate tectonics."
      }
    ];
    c.learningOutcomes[2].keyTerms = [
      {
        term: "What are fold mountains?",
        definition: "Mountain ranges formed by compression and folding of rock at convergent plate boundaries; among the world's most dramatic landscapes.",
        section: "2.3"
      },
      {
        term: "What is an anticline?",
        definition: "Upward arch in folded rock created by compression forces at convergent plate boundaries.",
        section: "2.3"
      },
      {
        term: "What is a syncline?",
        definition: "Downward fold in rock created by compression forces at convergent plate boundaries.",
        section: "2.3"
      },
      {
        term: "What is the Caledonian orogeny?",
        definition: "Mountain-building period ~400 million years ago caused by North American and Eurasian plate collision; formed ranges in Ireland, Wales, Scotland and Norway.",
        section: "2.3"
      },
      {
        term: "What is the Armorican orogeny?",
        definition: "Mountain-building period ~250 million years ago caused by Eurasian-African plate collision; formed ranges across western Europe and uplifted limestone in southern Ireland.",
        section: "2.3"
      },
      {
        term: "What is the Alpine orogeny?",
        definition: "Ongoing mountain-building period beginning ~60 million years ago; responsible for the Alps stretching across France, Italy, Germany, Austria, Switzerland and Slovenia.",
        section: "2.3"
      },
      {
        term: "What is compression?",
        definition: "Squeezing force applied to rocks at convergent plate boundaries causing folding or faulting; rock becomes heated and ductile under this stress.",
        section: "2.3"
      },
      {
        term: "What is metamorphism?",
        definition: "Change in mineral composition and texture of pre-existing rocks due to heat and pressure; occurs at convergent plate boundaries alongside fold mountain formation.",
        section: "2.3"
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine how the tectonic cycle helps to explain the global distribution of fold mountains.",
        model: "Caledonian Orogeny (~400 mya): The North American and Eurasian plates collided in a continental-continental convergence approximately 400 million years ago. Huge compression forces folded and thrust sedimentary rock layers upward, forming mountain ranges across the region. This orogeny formed the oldest mountains in Ireland, including the Wicklow Mountains and Great Sugarloaf, Co. Wicklow. The Scottish Highlands and Scandinavian Mountains were formed by the same orogeny — evidence linking these now-separated landmasses. The NE-SW trend of these mountains in Ireland reflects the direction of the original collision force. Armorican Orogeny (~250 mya): The African and Eurasian plates collided approximately 250 million years ago in another continental-continental convergence. Compression forces produced approximately 3,000 km of mountain ranges across western Europe from Ireland to Germany. In Ireland, this orogeny formed the Munster Ridge and Valley — including Macgillycuddy's Reeks, Cork's ridges and the Kerry Mountains. The associated rock types — quartzite, shale and marble — were formed under the intense heat and pressure of the collision. Alpine Orogeny (~60 mya — ongoing): The Indo-Australian and Eurasian plates collided approximately 60 million years ago, forming the Himalayas. Mount Everest (8,848 m) is still rising as the plates continue to converge today. The collision of the Nazca and South American plates formed the Andes — the world's longest mountain range at approximately 7,000 km. Fold mountains cluster exclusively at convergent plate boundaries worldwide — this distribution is entirely explained by plate tectonics. The ongoing Alpine Orogeny shows that fold mountain formation is a continuous, present-day process."
      }
    ];
    // 2.4 — Earthquake Prediction and Mitigation
    c.learningOutcomes[3].notes = [
      {
        h: "Prediction Methods",
        b: "Rock stress: strainmeters placed along fault lines measure pressure buildup — help indicate when a fault is close to snapping. Radon gas: deformation of rock at fault lines releases radon — networks of radon detectors act as early warning systems. Foreshocks: minor tremors before major earthquakes — used to evacuate Haicheng, China, in 1975. Animal behaviour: animals reported to act erratically before earthquakes — not scientifically reliable."
      },
      {
        h: "Monitoring Technology",
        b: "Seismographs installed globally in a seismographic network — detect and measure ground motion continuously. Tsunameters: pressure sensors on the seafloor detect tsunami waves and relay data via satellite buoy to monitoring centres. GPS satellites monitor ground deformation along fault lines — detect plate movement in real time."
      },
      {
        h: "Reducing Effects",
        b: "Earthquake-resistant building design — flexible steel frames, base isolators, and counterweights absorb seismic energy. Japan uses strict building codes — buildings in Tokyo engineered to survive magnitude 7+ earthquakes. Early warning systems give seconds to minutes of advance notice — enough to stop trains, alert hospitals, and warn the public. Public education and earthquake drills (e.g. Japan's annual Disaster Prevention Day) reduce casualties. Emergency response planning — stockpiles, trained rescue teams, and designated evacuation zones limit secondary deaths."
      }
    ];
    c.learningOutcomes[3].keyTerms = [
      {
        term: "What is a seismograph?",
        definition: "Instrument used to record ground motion during an earthquake; part of a global seismographic network.",
        section: "2.4"
      },
      {
        term: "What is the Richter scale?",
        definition: "Logarithmic scale created in 1935 measuring earthquake magnitude; each step represents a tenfold increase in magnitude.",
        section: "2.4"
      },
      {
        term: "What is the Modified Mercalli scale (MMI)?",
        definition: "Scale measuring earthquake intensity based on observable damage and human experience; twelve grades.",
        section: "2.4"
      },
      {
        term: "Explain Elastic Rebound Theory.",
        definition: "Theory explaining earthquakes: stress builds in rocks at fault lines until it exceeds rock strength, causing sudden fracturing and release of seismic waves.",
        section: "2.4"
      },
      {
        term: "What are foreshocks?",
        definition: "Minor tremors preceding a major earthquake; used as indicators to issue warnings and trigger safety measures.",
        section: "2.4"
      },
      {
        term: "What is a strainmeter?",
        definition: "Instrument placed at fault lines to measure rock stress; monitors pressure build-up to predict when rock will fracture.",
        section: "2.4"
      },
      {
        term: "What is a tsunami?",
        definition: "Series of large waves caused by underwater displacement of water from an earthquake; can travel at 800 km/hr and inundate 5 km inland.",
        section: "2.4"
      },
      {
        term: "What is liquefaction?",
        definition: "Process where saturated soil loses strength and behaves like a liquid during an earthquake due to seismic waves; causes buildings to tilt, settle and collapse.",
        section: "2.4"
      },
      {
        term: "What are earthquake-resistant buildings?",
        definition: "Structures with flexible foundations, vibrational control devices and reinforced materials designed to counteract seismic wave forces.",
        section: "2.4"
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Explain how the occurrence of earthquakes can be predicted and their effects reduced.",
        model: "Prediction Methods: Rock stress monitoring uses strainmeters placed along fault lines to measure pressure buildup — these help indicate when a fault is approaching failure. Radon gas detection is another method — deformation of rock near fault lines releases radon gas, and detector networks can act as early warning systems. Foreshocks are minor tremors that sometimes precede a major earthquake — they were used to successfully evacuate Haicheng, China, in 1975, saving many lives. Animal behaviour — animals reported to behave erratically before earthquakes — has been observed but remains scientifically unreliable as a prediction tool. Monitoring Technology: Seismographs are installed globally in a seismographic network and detect and measure ground motion continuously, day and night. Tsunameters are pressure sensors placed on the seafloor that detect tsunami waves and relay data via satellite buoy to monitoring centres. GPS satellites monitor ground deformation along fault lines and can detect plate movement in real time with millimetre precision. Reducing Effects: Earthquake-resistant building design uses flexible steel frames, base isolators and counterweights to absorb and dissipate seismic energy. Japan enforces strict building codes — buildings in Tokyo are engineered to survive earthquakes of magnitude 7 or greater. Early warning systems give seconds to several minutes of advance notice — enough time to stop trains, alert hospitals and warn the public via phone alerts. Public education programmes and regular earthquake drills, such as Japan's annual Disaster Prevention Day, significantly reduce casualty numbers. Emergency response planning — including stockpiles of food and medicine, trained rescue teams and designated evacuation zones — limits secondary deaths. Seismic hazard zoning maps identify high-risk areas, allowing planning authorities to restrict construction in the most vulnerable locations. International cooperation through organisations such as the USGS shares real-time seismic data globally. Despite advances, predicting the exact time and location of an earthquake remains scientifically impossible."
      }
    ];
    // 2.5 — Volcanic Activity and Ireland's Landscape
    c.learningOutcomes[4].notes = [
      {
        h: "Intrusive Features — The Leinster Batholith",
        b: "A batholith is a large body of igneous (granite) rock formed when magma rose into the crust and cooled slowly underground. The Leinster Batholith has a surface area of ~1,500 km² — formed ~400 mya during the Caledonian Orogeny. Slow cooling underground produced large crystals visible to the naked eye — characteristic coarse-grained granite. Exposed at the surface through denudation (removal of overlying rock) — forms upland areas such as the Wicklow Mountains."
      },
      {
        h: "Intrusive Features — Dykes and Sills",
        b: "Dykes form when magma forces vertically through sedimentary rock layers and solidifies — creates near-perpendicular rock intrusions. Sills form when magma forces horizontally between sedimentary layers — can be exposed through erosion as resistant ridges. Both are visible in various parts of the Irish landscape, particularly in the northeast where igneous activity was most recent."
      },
      {
        h: "Extrusive Features — Antrim-Derry Plateau",
        b: "Fissure eruptions of basic lava occurred over ~2 million years — building up a lava plateau up to 1,800 m thick. Lava cooled more quickly at the surface — forming the characteristic hexagonal basalt columns of the Giant's Causeway. The Giant's Causeway is a UNESCO World Heritage Site — ~40,000 interlocking basalt columns formed by rapid, uniform cooling. The Antrim plateau covers much of northeast Ireland — one of Europe's largest and best-preserved lava plateau landscapes."
      }
    ];
    c.learningOutcomes[4].keyTerms = [
      {
        term: "What is Leinster Batholith?",
        definition: "Large body of granite covering ~1,500 km² in Ireland; formed 400+ million years ago when the Eurasian and North American plates collided during the Caledonian orogeny.",
        section: "2.5"
      },
      {
        term: "What is a batholith?",
        definition: "Large body of intrusive igneous rock (usually granite) that cools slowly deep in the crust; revealed at the surface through denudation.",
        section: "2.5"
      },
      {
        term: "What is granite?",
        definition: "Coarse-grained intrusive igneous rock composed mainly of quartz and feldspar; pink to white to grey colour; large crystals due to slow cooling.",
        section: "2.5"
      },
      {
        term: "What is basalt?",
        definition: "Dark, fine-grained extrusive igneous rock low in silica and high in iron and magnesium; formed by rapid cooling of basic lava outside the crust.",
        section: "2.5"
      },
      {
        term: "What is the Antrim-Derry Plateau?",
        definition: "Basalt landscape (~4,000 km²) in north-east Ireland formed ~65 million years ago by fissure eruptions as the North American and Eurasian plates began separating; home to the Giant's Causeway.",
        section: "2.5"
      },
      {
        term: "Giant's Causeway",
        definition: "World Heritage Site in County Antrim; ~40,000 interlocking hexagonal basalt columns formed by rapid cooling and contraction of basic lava from fissure eruptions.",
        section: "2.5"
      },
      {
        term: "What is denudation?",
        definition: "The combined processes of weathering and erosion that break down and remove rock material from Earth's surface, exposing intrusive features like batholiths.",
        section: "2.5"
      }
    ];
    c.learningOutcomes[4].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine the influence of volcanic activity on the development of the Irish landscape — intrusive and extrusive features.",
        model: "Intrusive — Leinster Batholith: A batholith is a large body of igneous (granite) rock formed when magma rose into the crust and cooled slowly underground. The Leinster Batholith has a surface area of approximately 1,500 km² and formed around 400 million years ago during the Caledonian Orogeny. Slow cooling deep underground produced large interlocking crystals visible to the naked eye, giving the characteristic coarse-grained granite texture. The overlying rock has been removed through millions of years of denudation — exposing the batholith at the surface as the Wicklow Mountains. Intrusive — Dykes and Sills: Dykes form when magma is forced vertically upward through existing sedimentary rock layers and solidifies in place. Sills form when magma is forced horizontally between existing sedimentary layers and solidifies, creating flat-lying igneous intrusions. Both dykes and sills can be exposed through erosion, forming resistant ridges that stand out in the landscape. Multiple dykes are visible across Ireland, particularly in the northeast where igneous activity was most recent. The Fair Head sill in north Antrim is a prominent example of a sill exposed by coastal erosion. Extrusive — Antrim-Derry Plateau: Fissure eruptions of basic lava occurred repeatedly over approximately 2 million years, building up a lava plateau up to 1,800 m thick. The lava cooled more quickly at the surface than deeper down — this uniform, rapid cooling produced the characteristic hexagonal basalt columns. The Giant's Causeway contains approximately 40,000 interlocking hexagonal basalt columns, formed by the uniform cooling pattern. The Giant's Causeway is a UNESCO World Heritage Site, attracting hundreds of thousands of visitors annually and contributing significantly to the local economy. The Antrim plateau covers much of northeast Ireland and is one of Europe's largest and best-preserved lava plateau landscapes. This volcanic activity, occurring approximately 60 million years ago, fundamentally shaped the physical landscape of northeast Ireland that we see today."
      }
    ];
    c.examQuestions = [
      {
        id: "geo2-eq-1",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q1.",
            question: "Discuss the positive impacts of volcanoes.",
            marks: 30,
            model: "Fertile Soils: Volcanic ash (tephra) is rich in minerals such as potassium and phosphorus, which break down into highly fertile soils over time. The slopes of Mount Etna in Sicily support intensive viticulture and citrus farming due to these volcanic soils. Java, Indonesia is one of the world's most densely farmed islands due to the highly fertile volcanic soils from nearby active volcanoes. Farmers continue to live near active volcanoes because the agricultural productivity outweighs the risk. Geothermal Energy: Volcanic regions have significant geothermal energy potential — magma heats underground water, which is harnessed for electricity generation and heating. Iceland generates almost 100% of its space heating and approximately 30% of its electricity from geothermal energy. Iceland's geothermal advantage stems from its position on the Mid-Atlantic Ridge, where volcanic activity is especially intense. Geothermal energy is clean, renewable and reduces dependence on fossil fuels, lowering carbon emissions. Tourism and Mineral Wealth: Volcanic landscapes attract significant tourism — Hawaii's shield volcanoes, the Canary Islands and Iceland's geysers and lava fields are globally renowned. Volcanic regions are associated with mineral deposits including gold, silver, copper and diamonds near igneous rock formations. The Giant's Causeway on the Antrim-Derry Plateau is a UNESCO World Heritage Site attracting over 600,000 visitors per year to Ireland. Land Creation: Successive lava flows build up new land above sea level — the Hawaiian Islands were entirely formed by hotspot volcanic activity over millions of years. The island of Surtsey off Iceland emerged from the ocean in 1963 through underwater volcanic eruptions. The Antrim-Derry Plateau in northeast Ireland was built up over approximately 2 million years of fissure eruptions. The plateau reaches up to 1,800 m in thickness and constitutes one of Europe's largest and best-preserved lava plateau landscapes.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo2-eq-2",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q2.",
            question: "Explain how the study of plate tectonics has helped us to understand the global distribution of volcanoes.",
            marks: 30,
            model: "Divergent Boundaries: At divergent plate boundaries, plates separate and fissures allow magma to rise from the mantle below. New oceanic crust forms at mid-ocean ridges, and volcanic activity is continuous along these boundaries. Basic lava with low silica content rises at divergent boundaries — it is runny and non-explosive, forming gently sloping shield volcanoes. Iceland sits on the Mid-Atlantic Ridge and is the most prominent surface example of divergent boundary volcanism above sea level. Convergent Boundaries: At convergent boundaries, the heavier oceanic plate subducts beneath the lighter plate and melts in the mantle. Magma rises through the overlying crust and collects in a magma chamber — eventually erupting at the surface. High silica content makes this magma viscous and volatile — it produces explosive composite stratovolcanoes with violent eruptions. Volcanoes form along the continental margin or as island arcs — e.g. the Andes (Nazca and South American plates) and Japan's island arc chain. Hotspots: Over 40 global hotspots exist, many located far from plate boundaries — explained by plumes of magma rising from deep in the mantle. The hotspot burns through the oceanic plate above it as the plate moves — successive volcanic islands form in a chain. The Hawaiian island chain is the classic example — the oldest islands are furthest from the current hotspot, the youngest are still forming directly over it. Ring of Fire: Approximately 75% of all the world's volcanoes are located in the Ring of Fire around the boundary of the Pacific Plate. This concentration is explained by the multiple convergent subduction zones encircling the Pacific. Plate tectonics explains why volcanoes cluster at plate boundaries rather than being randomly distributed across Earth's surface. Intraplate volcanoes at hotspots are the exception — explained by mantle plumes rising through the interior of a plate rather than at its boundary.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo2-eq-3",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q3.",
            question: "Examine how the tectonic cycle helps to explain the global distribution of fold mountains.",
            marks: 30,
            model: "Caledonian Orogeny (~400 mya): The North American and Eurasian plates collided in a continental-continental convergence approximately 400 million years ago. Huge compression forces folded and thrust sedimentary rock layers upward, forming mountain ranges across the region. This orogeny formed the oldest mountains in Ireland, including the Wicklow Mountains and Great Sugarloaf, Co. Wicklow. The Scottish Highlands and Scandinavian Mountains were formed by the same orogeny — evidence linking these now-separated landmasses. The NE-SW trend of these mountains in Ireland reflects the direction of the original collision force. Armorican Orogeny (~250 mya): The African and Eurasian plates collided approximately 250 million years ago in another continental-continental convergence. Compression forces produced approximately 3,000 km of mountain ranges across western Europe from Ireland to Germany. In Ireland, this orogeny formed the Munster Ridge and Valley — including Macgillycuddy's Reeks, Cork's ridges and the Kerry Mountains. The associated rock types — quartzite, shale and marble — were formed under the intense heat and pressure of the collision. Alpine Orogeny (~60 mya — ongoing): The Indo-Australian and Eurasian plates collided approximately 60 million years ago, forming the Himalayas. Mount Everest (8,848 m) is still rising as the plates continue to converge today. The collision of the Nazca and South American plates formed the Andes — the world's longest mountain range at approximately 7,000 km. Fold mountains cluster exclusively at convergent plate boundaries worldwide — this distribution is entirely explained by plate tectonics. The ongoing Alpine Orogeny shows that fold mountain formation is a continuous, present-day process.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo2-eq-4",
        source: "LC Geography — Sample 2021",
        parts: [
          {
            label: "Q4.",
            question: "Explain how the occurrence of earthquakes can be predicted and their effects reduced.",
            marks: 30,
            model: "Prediction Methods: Rock stress monitoring uses strainmeters placed along fault lines to measure pressure buildup — these help indicate when a fault is approaching failure. Radon gas detection is another method — deformation of rock near fault lines releases radon gas, and detector networks can act as early warning systems. Foreshocks are minor tremors that sometimes precede a major earthquake — they were used to successfully evacuate Haicheng, China, in 1975, saving many lives. Animal behaviour — animals reported to behave erratically before earthquakes — has been observed but remains scientifically unreliable as a prediction tool. Monitoring Technology: Seismographs are installed globally in a seismographic network and detect and measure ground motion continuously, day and night. Tsunameters are pressure sensors placed on the seafloor that detect tsunami waves and relay data via satellite buoy to monitoring centres. GPS satellites monitor ground deformation along fault lines and can detect plate movement in real time with millimetre precision. Reducing Effects: Earthquake-resistant building design uses flexible steel frames, base isolators and counterweights to absorb and dissipate seismic energy. Japan enforces strict building codes — buildings in Tokyo are engineered to survive earthquakes of magnitude 7 or greater. Early warning systems give seconds to several minutes of advance notice — enough time to stop trains, alert hospitals and warn the public via phone alerts. Public education programmes and regular earthquake drills, such as Japan's annual Disaster Prevention Day, significantly reduce casualty numbers. Emergency response planning — including stockpiles of food and medicine, trained rescue teams and designated evacuation zones — limits secondary deaths. Seismic hazard zoning maps identify high-risk areas, allowing planning authorities to restrict construction in the most vulnerable locations. International cooperation through organisations such as the USGS shares real-time seismic data globally. Despite advances, predicting the exact time and location of an earthquake remains scientifically impossible.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo2-eq-5",
        source: "LC Geography — Sample 2019",
        parts: [
          {
            label: "Q5.",
            question: "Examine the influence of volcanic activity on the development of the Irish landscape — intrusive and extrusive features.",
            marks: 30,
            model: "Intrusive — Leinster Batholith: A batholith is a large body of igneous (granite) rock formed when magma rose into the crust and cooled slowly underground. The Leinster Batholith has a surface area of approximately 1,500 km² and formed around 400 million years ago during the Caledonian Orogeny. Slow cooling deep underground produced large interlocking crystals visible to the naked eye, giving the characteristic coarse-grained granite texture. The overlying rock has been removed through millions of years of denudation — exposing the batholith at the surface as the Wicklow Mountains. Intrusive — Dykes and Sills: Dykes form when magma is forced vertically upward through existing sedimentary rock layers and solidifies in place. Sills form when magma is forced horizontally between existing sedimentary layers and solidifies, creating flat-lying igneous intrusions. Both dykes and sills can be exposed through erosion, forming resistant ridges that stand out in the landscape. Multiple dykes are visible across Ireland, particularly in the northeast where igneous activity was most recent. The Fair Head sill in north Antrim is a prominent example of a sill exposed by coastal erosion. Extrusive — Antrim-Derry Plateau: Fissure eruptions of basic lava occurred repeatedly over approximately 2 million years, building up a lava plateau up to 1,800 m thick. The lava cooled more quickly at the surface than deeper down — this uniform, rapid cooling produced the characteristic hexagonal basalt columns. The Giant's Causeway contains approximately 40,000 interlocking hexagonal basalt columns, formed by the uniform cooling pattern. The Giant's Causeway is a UNESCO World Heritage Site, attracting hundreds of thousands of visitors annually and contributing significantly to the local economy. The Antrim plateau covers much of northeast Ireland and is one of Europe's largest and best-preserved lava plateau landscapes. This volcanic activity, occurring approximately 60 million years ago, fundamentally shaped the physical landscape of northeast Ireland that we see today.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── geo3: Tectonic Activity / Folding & Faulting ──────────────────────────
  (function () {
    var c = ch("geo3");
    // 3.1 — Impact of Tectonic Activity on Ireland's Landscape
    c.learningOutcomes[0].notes = [
      {
        h: "Fold Mountains",
        b: "Three orogenies shaped Ireland's upland landscape. Caledonian (~400 mya): formed NE-SW trending mountains in Leinster — e.g. Wicklow Mountains (Sugarloaf). Armorican (~250 mya): formed E-W trending ridges of Munster — e.g. Macgillycuddy's Reeks, Cork ridges and valleys. Between orogenies, Ireland's surface was worn flat by erosion."
      },
      {
        h: "Rock Types",
        b: "Caledonian orogeny produced the Leinster Batholith (granite) through intrusive igneous activity during continental collision. Quartzite formed under high pressure and heat — e.g. Great Sugarloaf, Co. Wicklow. Limestone (Carboniferous, ~320 mya) formed in warm, shallow tropical seas — covers the Central Lowlands and the Burren, Co. Clare."
      },
      {
        h: "Faulting",
        b: "Normal faulting at divergent boundaries and tension zones produced rift valleys and block mountain structures in Ireland. The Shannon Estuary follows a fault line — the river exploited a zone of crustal weakness created by tectonic faulting. Much of Ireland's drainage pattern (rivers following valleys) is structurally controlled — rivers exploit fault lines and weaker rock."
      },
      {
        h: "Volcanic Activity",
        b: "Fissure eruptions of basic lava ~60 mya formed the Antrim-Derry Plateau — up to 1,800 m thick, covering northeast Ireland. The Giant's Causeway formed as lava cooled uniformly, producing ~40,000 hexagonal basalt columns — now a UNESCO World Heritage Site. The Fair Head sill (north Antrim) and multiple dykes across Ireland are further evidence of past igneous intrusive activity."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the Iapetus Ocean?",
        definition: "Ancient ocean that ~850 million years ago separated the landmasses that would become Ireland; its closure drove the Caledonian orogeny.",
        section: "3.1"
      },
      {
        term: "What is Caledonian folding?",
        definition: "Intense period of folding ~400 million years ago as North American and Eurasian plates collided; formed the Caledonian mountain range across Ireland, Scotland and Norway.",
        section: "3.1"
      },
      {
        term: "What is Armorican folding?",
        definition: "Collision of Eurasian and African plates ~300 million years ago that folded the southern half of Ireland, creating the Munster Ridge Valley and exposing the Burren limestone.",
        section: "3.1"
      },
      {
        term: "What is the Munster Ridge valley?",
        definition: "Distinctive ridges-and-valleys landscape of south-west Ireland (including Macgillycuddy's Reeks) formed by Armorican folding of sandstone and limestone strata.",
        section: "3.1"
      },
      {
        term: "What is the Burren limestone pavement?",
        definition: "Limestone landscape in County Clare exposed by Armorican folding and glaciation; formed when Ireland was submerged in a shallow tropical sea ~320 million years ago.",
        section: "3.1"
      },
      {
        term: "What is Atlantic divergence?",
        definition: "Separation of North American and Eurasian plates ~65 million years ago that formed the North Atlantic and caused fissure eruptions creating the Antrim-Derry basalt plateau.",
        section: "3.1"
      },
      {
        term: "What is Old Red Sandstone?",
        definition: "Sedimentary rock formed ~380–320 million years ago in the Munster region when Ireland had a desert climate; characterises south-west Irish landscape.",
        section: "3.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine the impact of tectonic activity on the landscape of Ireland.",
        model: "Fold Mountains: Three separate orogenies shaped Ireland's upland landscape over hundreds of millions of years. The Caledonian Orogeny (~400 mya) involved the collision of the North American and Eurasian plates, creating NE-SW trending mountains in Leinster — including the Wicklow Mountains and the Great Sugarloaf. Between the orogenies, Ireland's surface was worn flat by millions of years of erosion, removing the original mountain heights. The Armorican Orogeny (~250 mya) formed the E-W trending ridge and valley landscape of Munster — including Macgillycuddy's Reeks, Ireland's highest mountain range. Rock Types: The Leinster Batholith — a large body of granite — formed through intrusive igneous activity during the Caledonian Orogeny, as magma cooled slowly underground. Quartzite was formed under the intense heat and pressure of orogeny — the Great Sugarloaf, Co. Wicklow, is composed of resistant quartzite rock. Carboniferous Limestone (~320 mya) formed in warm, shallow tropical seas when Ireland lay near the equator — it now covers the Central Lowlands and the Burren, Co. Clare. The Burren's limestone pavement is a UNESCO-designated area, shaped by carbonation weathering over thousands of years. Faulting: Normal faulting in tension zones produced rift valleys and block mountain structures across Ireland. The Shannon Estuary follows a major fault line — the river has exploited a zone of crustal weakness created by tectonic faulting. Much of Ireland's drainage pattern is structurally controlled — rivers exploit fault lines and zones of weaker rock in their courses. Volcanic Activity: Fissure eruptions of basic lava approximately 60 million years ago formed the Antrim-Derry Plateau, which is up to 1,800 m thick. Rapid, uniform cooling of the surface lava produced the approximately 40,000 hexagonal basalt columns of the Giant's Causeway. The Giant's Causeway is designated a UNESCO World Heritage Site and attracts over 600,000 visitors annually. The Fair Head sill in north Antrim and multiple dykes across Ireland provide further evidence of past intrusive volcanic activity."
      }
    ];
    // 3.2 — Folding and Faulting Landforms
    c.learningOutcomes[1].notes = [
      {
        h: "Folding — Process",
        b: "Folding occurs when compressional forces at convergent plate boundaries cause layers of sedimentary rock to buckle and deform. Rocks in the lower lithosphere are ductile (plastic) — bend without breaking under sustained pressure. Anticlines form where rock is folded upward; synclines form where rock is folded downward."
      },
      {
        h: "Folding — Landforms",
        b: "Fold mountains form through orogeny — e.g. the Himalayas (Indo-Australian and Eurasian plates) and the Andes (Nazca and South American). In Ireland, the Armorican Orogeny (~250 mya) created the Munster Ridge and Valley landscape — alternating anticlines and synclines. Monoclines: tilted strata folded and faulted under compression — e.g. Ben Bulben, Co. Sligo. Domes: bowl-like upward structures from rising magma pressure — e.g. Slieve Bloom Mountains."
      },
      {
        h: "Faulting — Process",
        b: "Faulting occurs when brittle rocks in the upper lithosphere fracture under tension or compression forces. Normal fault: tension forces (divergent boundaries) — hanging wall drops relative to footwall; e.g. East African Rift Valley. Reverse fault: compression forces (convergent boundaries) — hanging wall rises above footwall. Strike-slip fault: shearing forces (transform boundaries) — walls move laterally past each other; e.g. San Andreas Fault, California."
      },
      {
        h: "Faulting — Landforms",
        b: "Graben: block of land dropped between two normal faults — forms rift valleys; e.g. East African Rift Valley. Horst: elevated block between two grabens — forms block mountains. Fault scarps: small but visible offsets where one side of a fault has moved vertically — common in Ireland."
      }
    ];
    c.learningOutcomes[1].keyTerms = [
      {
        term: "What is a normal fault?",
        definition: "Fault formed under tension forces as plates separate; the hanging wall drops relative to the footwall. Creates rift valleys. Example: East African Rift Valley.",
        section: "3.2"
      },
      {
        term: "What is a reverse fault?",
        definition: "Fault formed under compression forces as plates collide; the hanging wall rises relative to the footwall. Found at convergent plate boundaries.",
        section: "3.2"
      },
      {
        term: "What is a strike-slip fault?",
        definition: "Fault where plates slide past each other laterally; fault plane is vertical, with no hanging wall or footwall. Also called a transform fault. Example: San Andreas Fault.",
        section: "3.2"
      },
      {
        term: "What is a hanging wall?",
        definition: "Block of rock above a fault line; rises in a reverse fault and drops in a normal fault.",
        section: "3.2"
      },
      {
        term: "What is a footwall?",
        definition: "Block of rock below a fault line.",
        section: "3.2"
      },
      {
        term: "What is a rift valley?",
        definition: "Valley formed where tension forces pull the crust apart and a central block drops between two normal faults. Example: East African Rift Valley.",
        section: "3.2"
      },
      {
        term: "What is a monocline?",
        definition: "Plateau-like upland structure of sedimentary rock formed by compression folding and faulting. Example: Ben Bulben, County Sligo.",
        section: "3.2"
      },
      {
        term: "What is an overthrust fold?",
        definition: "Fold type where compressional forces cause one limb to fracture and be pushed on top of the other; indicates intense plate collision.",
        section: "3.2"
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Explain how folding and faulting influence the development of landforms.",
        model: "Folding Process: Folding occurs when compressional forces at convergent plate boundaries cause layers of sedimentary rock to buckle and permanently deform. Rocks in the lower lithosphere are ductile (plastic) and bend without breaking under sustained pressure over millions of years. Anticlines form where rock layers are folded upward into an arch shape; synclines form where rock layers are folded downward into a trough shape. Folding Landforms: Fold mountains form through orogeny at convergent boundaries — the Himalayas (Indo-Australian and Eurasian plates) and the Andes (Nazca and South American plates) are the largest examples. In Ireland, the Armorican Orogeny (~250 mya) created the Munster Ridge and Valley landscape — alternating anticlines and synclines running east to west. Monoclines are tilted rock strata folded and faulted under compression — Ben Bulben, Co. Sligo, is a notable Irish example. Domes are bowl-shaped upward structures formed by rising magma pressure from below — the Slieve Bloom Mountains are an Irish example of a dome structure. Faulting Process: Faulting occurs when brittle rocks in the upper lithosphere fracture under tension or compression forces rather than bending. Normal faults result from tension forces at divergent boundaries — the hanging wall drops relative to the footwall, e.g. the East African Rift Valley. Reverse faults result from compression forces at convergent boundaries — the hanging wall is pushed up above the footwall. Strike-slip faults result from shearing forces at transform boundaries — the rock walls move laterally past each other, e.g. San Andreas Fault, California. Faulting Landforms: A graben is a block of land that has dropped between two normal faults — it forms a rift valley, e.g. the East African Rift Valley. A horst is an elevated block of land between two grabens — forms block mountains that stand above the surrounding lowered terrain. Fault scarps are small but visible vertical offsets at the surface where one side of a fault has moved — common landforms in Ireland. Tectonic faults have also influenced Ireland's drainage pattern — rivers exploit zones of crustal weakness along fault lines in their courses."
      }
    ];
    c.examQuestions = [
      {
        id: "geo3-eq-1",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q1.",
            question: "Examine the impact of tectonic activity on the landscape of Ireland.",
            marks: 30,
            model: "Fold Mountains: Three separate orogenies shaped Ireland's upland landscape over hundreds of millions of years. The Caledonian Orogeny (~400 mya) involved the collision of the North American and Eurasian plates, creating NE-SW trending mountains in Leinster — including the Wicklow Mountains and the Great Sugarloaf. Between the orogenies, Ireland's surface was worn flat by millions of years of erosion, removing the original mountain heights. The Armorican Orogeny (~250 mya) formed the E-W trending ridge and valley landscape of Munster — including Macgillycuddy's Reeks, Ireland's highest mountain range. Rock Types: The Leinster Batholith — a large body of granite — formed through intrusive igneous activity during the Caledonian Orogeny, as magma cooled slowly underground. Quartzite was formed under the intense heat and pressure of orogeny — the Great Sugarloaf, Co. Wicklow, is composed of resistant quartzite rock. Carboniferous Limestone (~320 mya) formed in warm, shallow tropical seas when Ireland lay near the equator — it now covers the Central Lowlands and the Burren, Co. Clare. The Burren's limestone pavement is a UNESCO-designated area, shaped by carbonation weathering over thousands of years. Faulting: Normal faulting in tension zones produced rift valleys and block mountain structures across Ireland. The Shannon Estuary follows a major fault line — the river has exploited a zone of crustal weakness created by tectonic faulting. Much of Ireland's drainage pattern is structurally controlled — rivers exploit fault lines and zones of weaker rock in their courses. Volcanic Activity: Fissure eruptions of basic lava approximately 60 million years ago formed the Antrim-Derry Plateau, which is up to 1,800 m thick. Rapid, uniform cooling of the surface lava produced the approximately 40,000 hexagonal basalt columns of the Giant's Causeway. The Giant's Causeway is designated a UNESCO World Heritage Site and attracts over 600,000 visitors annually. The Fair Head sill in north Antrim and multiple dykes across Ireland provide further evidence of past intrusive volcanic activity.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo3-eq-2",
        source: "LC Geography — Long Question (2007 & 2012)",
        parts: [
          {
            label: "Q2.",
            question: "Explain how folding and faulting influence the development of landforms.",
            marks: 30,
            model: "Folding Process: Folding occurs when compressional forces at convergent plate boundaries cause layers of sedimentary rock to buckle and permanently deform. Rocks in the lower lithosphere are ductile (plastic) and bend without breaking under sustained pressure over millions of years. Anticlines form where rock layers are folded upward into an arch shape; synclines form where rock layers are folded downward into a trough shape. Folding Landforms: Fold mountains form through orogeny at convergent boundaries — the Himalayas (Indo-Australian and Eurasian plates) and the Andes (Nazca and South American plates) are the largest examples. In Ireland, the Armorican Orogeny (~250 mya) created the Munster Ridge and Valley landscape — alternating anticlines and synclines running east to west. Monoclines are tilted rock strata folded and faulted under compression — Ben Bulben, Co. Sligo, is a notable Irish example. Domes are bowl-shaped upward structures formed by rising magma pressure from below — the Slieve Bloom Mountains are an Irish example of a dome structure. Faulting Process: Faulting occurs when brittle rocks in the upper lithosphere fracture under tension or compression forces rather than bending. Normal faults result from tension forces at divergent boundaries — the hanging wall drops relative to the footwall, e.g. the East African Rift Valley. Reverse faults result from compression forces at convergent boundaries — the hanging wall is pushed up above the footwall. Strike-slip faults result from shearing forces at transform boundaries — the rock walls move laterally past each other, e.g. San Andreas Fault, California. Faulting Landforms: A graben is a block of land that has dropped between two normal faults — it forms a rift valley, e.g. the East African Rift Valley. A horst is an elevated block of land between two grabens — forms block mountains that stand above the surrounding lowered terrain. Fault scarps are small but visible vertical offsets at the surface where one side of a fault has moved — common landforms in Ireland. Tectonic faults have also influenced Ireland's drainage pattern — rivers exploit zones of crustal weakness along fault lines in their courses.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── geo4: Weathering ──────────────────────────────────────────────────────
  (function () {
    var c = ch("geo4");
    // 4.1 — Physical Weathering — Role of Temperature
    c.learningOutcomes[0].notes = [
      {
        h: "Freeze-Thaw (Frost Shattering)",
        b: "Most common type of physical weathering in Ireland. Three conditions required: adequate water, temperatures that fluctuate above and below 0°C, and pre-existing fractures in the rock. Water enters cracks; as it freezes it expands by ~9% — exerts pressure on the surrounding rock. Repeated freeze-thaw cycles progressively widen cracks until rock fragments break away — called scree. Example: Great Sugarloaf, Co. Wicklow — scree slopes on its flanks are evidence of freeze-thaw action."
      },
      {
        h: "Haloclasty (Salt Weathering)",
        b: "Salt water seeps into pores of coastal rocks; water evaporates leaving salt crystals behind. Salt crystals expand when heated — repeated expansion exerts pressure, forming micro-fractures over time. Three conditions required: saline supply, porous rock, hot/sunny/windy climate for evaporation. Example: Killiney Beach, Co. Dublin — coastal rock faces show evidence of salt weathering."
      },
      {
        h: "Thermal Expansion",
        b: "In regions with extreme diurnal temperature ranges (e.g. deserts), rocks expand when heated and contract when cooled. The outer surface of rock heats and cools faster than the interior — differential expansion causes the outer layers to peel away (exfoliation/onion-skin weathering). Dark-coloured rocks absorb more heat and are more susceptible to this process than light-coloured rocks."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is weathering?",
        definition: "Breaking down and decaying of rocks and minerals on Earth's surface due to water, ice, acids, salts, plants, animals or temperature changes; no movement of material.",
        section: "4.1"
      },
      {
        term: "What is erosion?",
        definition: "Breakdown and transport of rock material from its original position to another location by water, wind or ice.",
        section: "4.1"
      },
      {
        term: "What is physical (mechanical) weathering?",
        definition: "Breakdown of rock into smaller pieces without changing its chemical composition; most common in areas with little vegetation and extreme climates.",
        section: "4.1"
      },
      {
        term: "What is freeze-thaw action?",
        definition: "Most common physical weathering in Ireland; water fills rock joints, freezes and expands, exerting hydraulic pressure up to 1,800 kg/cm²; repeated cycles shatter rock.",
        section: "4.1"
      },
      {
        term: "What is scree?",
        definition: "Rock fragments produced by freeze-thaw action that accumulate at the base of a steep slope due to gravity.",
        section: "4.1"
      },
      {
        term: "What is haloclasty?",
        definition: "Physical weathering by salt crystal growth in porous rocks; salt crystals expand up to three times in size when heated, fracturing the rock. Most common in coastal areas.",
        section: "4.2"
      },
      {
        term: "What is exfoliation?",
        definition: "Physical weathering where temperature extremes cause rock to expand and contract, peeling away outer layers like an onion. Most common in deserts.",
        section: "4.2"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Explain the role of temperature in the process of physical weathering.",
        model: "Freeze-Thaw (most common in Ireland): Three conditions are required for freeze-thaw weathering — adequate water, temperatures that fluctuate above and below 0°C, and pre-existing fractures in the rock. Water seeps into cracks and joints in the rock and, as temperatures drop below freezing, it freezes and expands by approximately 9%. This expansion exerts enormous pressure on the surrounding rock from within, gradually widening the fractures over repeated cycles. As temperatures rise above 0°C, the ice melts and the process repeats — each cycle widens the crack further. Eventually fragments of rock break away from the exposed surface — these accumulate at the base of the slope as scree deposits. Great Sugarloaf, Co. Wicklow, shows extensive scree slopes on its flanks that are direct evidence of freeze-thaw action. Haloclasty (Salt Weathering): Salt water seeps into the pores and small cracks of coastal rocks — this can occur through sea spray or groundwater. When the water evaporates, salt crystals are left behind in the pores of the rock. When the salt crystals are heated they expand, and repeated expansion exerts sufficient pressure to form micro-fractures in the rock. Three conditions are required: a saline water supply, porous rock, and a hot, sunny or windy climate to drive evaporation. Killiney Beach, Co. Dublin, shows evidence of salt weathering on exposed coastal rock faces. Thermal Expansion: In regions with extreme diurnal temperature ranges, such as deserts, rocks expand significantly when heated and contract when cooled at night. The outer surface of the rock heats and cools much faster than the interior — this differential expansion and contraction causes the outer layers to peel away. This process is called exfoliation or onion-skin weathering and it produces characteristic rounded boulders and layered rock surfaces. Dark-coloured rocks absorb more solar radiation and are more susceptible to thermal expansion than light-coloured rocks."
      }
    ];
    // 4.2 — Physical and Chemical Weathering
    c.learningOutcomes[1].notes = [
      {
        h: "Physical Weathering — Freeze-Thaw",
        b: "Requires: fluctuating temperatures, water, and pre-existing fractures. Water enters cracks; freezes and expands by ~9%, widening fractures. Repeated cycles cause rock to break — fragments called scree accumulate at the base of slopes. Most common in Ireland — example: Great Sugarloaf, Co. Wicklow."
      },
      {
        h: "Chemical Weathering — Carbonation",
        b: "Also called carbonate dissolution — calcium carbonate in limestone dissolves when exposed to carbonic acid (rainwater + CO₂). Three conditions required: rainfall, CO₂ in the atmosphere, and calcium carbonate rock (limestone). Cold water absorbs more CO₂ — carbonation is more effective in cold, wet climates. Water percolates through natural joints, dissolving rock and widening cracks into grikes; remaining rock surfaces form clints. Example: The Burren, Co. Clare — limestone pavement formed by carbonation over thousands of years."
      },
      {
        h: "Chemical Weathering — Hydrolysis",
        b: "Occurs when minerals in rocks react with acidic water — part of the mineral dissolves, the rest transforms into a new substance (e.g. clay). Differs from carbonation — minerals are not fully washed away but changed into weaker materials. Feldspar minerals break down into kaolin (clay) — weakens the rock structure from within. Common in humid temperate climates — Ireland's rainfall makes hydrolysis a widespread weathering process."
      }
    ];
    c.learningOutcomes[1].keyTerms = [
      {
        term: "What is chemical weathering?",
        definition: "Breakdown and change in chemical composition of rock through reactions with agents such as acids; requires warmth and moisture.",
        section: "4.2"
      },
      {
        term: "What is carbonation?",
        definition: "Chemical weathering where carbonic acid (rainwater + CO₂) dissolves calcium carbonate in limestone; most common in cool, wet climates with limestone bedrock.",
        section: "4.3"
      },
      {
        term: "What is carbonic acid?",
        definition: "Weak acid (pH 3.7) formed when rainwater absorbs atmospheric CO₂; the primary agent of carbonation in limestone landscapes.",
        section: "4.3"
      },
      {
        term: "What is calcium bicarbonate?",
        definition: "Soluble product formed when carbonic acid reacts with calcium carbonate in limestone; dissolved and removed from rock through solution.",
        section: "4.3"
      },
      {
        term: "What is hydrolysis?",
        definition: "Most common chemical weathering; minerals in igneous rocks (e.g. feldspar) react with acidic water and are transformed into new solids (e.g. kaolin/clay) or washed away.",
        section: "4.4"
      },
      {
        term: "What is oxidation?",
        definition: "Chemical weathering where iron in rocks reacts with oxygen to form rust; rust expands, weakening and breaking apart the rock.",
        section: "4.4"
      },
      {
        term: "What is solution weathering?",
        definition: "Chemical weathering process where water dissolves and removes soluble minerals from rock; occurs in carbonation and hydrolysis reactions.",
        section: "4.3"
      },
      {
        term: "What is biological weathering?",
        definition: "Weathering caused by living organisms; plant roots widen rock cracks and burrowing animals loosen soil and rock.",
        section: "4.1"
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Explain one process of physical weathering and one process of chemical weathering.",
        model: "Physical — Freeze-Thaw: Three conditions are required: fluctuating temperatures above and below 0°C, adequate water, and pre-existing fractures in the rock. Water enters cracks in the rock surface and freezes — expanding by approximately 9% and exerting intense pressure on the surrounding rock. Repeated freeze-thaw cycles progressively widen the fractures until fragments of rock break away from the surface. These rock fragments accumulate at the base of the slope as scree deposits — Great Sugarloaf, Co. Wicklow, shows prominent scree slopes as evidence. Chemical — Carbonation: Carbonation occurs when rainwater absorbs CO₂ from the atmosphere, forming a weak carbonic acid. The carbonic acid reacts with calcium carbonate in the limestone rock, dissolving it in a process called carbonation or carbonate dissolution. Three conditions are required: adequate rainfall, CO₂ in the atmosphere, and calcium carbonate (limestone) rock. Cold water absorbs more CO₂ than warm water — making carbonation most effective in cold, wet climates such as Ireland's. Water percolates downward through natural joints in the limestone, dissolving and widening the cracks. The dissolved joints become grikes — the remaining raised rock surfaces between them are called clints. This creates the limestone pavement characteristic of karst landscapes — the Burren, Co. Clare, is Ireland's finest example. Chemical — Hydrolysis: Hydrolysis occurs when minerals in rocks react chemically with acidic water — part of the mineral dissolves and the rest is transformed into a new, weaker substance. Feldspar minerals in granite, for example, break down through hydrolysis into kaolin (clay) — this weakens the rock structure from within, making it more susceptible to further erosion. Hydrolysis differs from carbonation in that the minerals are not fully washed away but chemically changed into weaker materials. Ireland's high rainfall and humid temperate climate make hydrolysis a widespread and significant weathering process across the country."
      }
    ];
    c.examQuestions = [
      {
        id: "geo4-eq-1",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q1.",
            question: "Explain the role of temperature in the process of physical weathering.",
            marks: 30,
            model: "Freeze-Thaw (most common in Ireland): Three conditions are required for freeze-thaw weathering — adequate water, temperatures that fluctuate above and below 0°C, and pre-existing fractures in the rock. Water seeps into cracks and joints in the rock and, as temperatures drop below freezing, it freezes and expands by approximately 9%. This expansion exerts enormous pressure on the surrounding rock from within, gradually widening the fractures over repeated cycles. As temperatures rise above 0°C, the ice melts and the process repeats — each cycle widens the crack further. Eventually fragments of rock break away from the exposed surface — these accumulate at the base of the slope as scree deposits. Great Sugarloaf, Co. Wicklow, shows extensive scree slopes on its flanks that are direct evidence of freeze-thaw action. Haloclasty (Salt Weathering): Salt water seeps into the pores and small cracks of coastal rocks — this can occur through sea spray or groundwater. When the water evaporates, salt crystals are left behind in the pores of the rock. When the salt crystals are heated they expand, and repeated expansion exerts sufficient pressure to form micro-fractures in the rock. Three conditions are required: a saline water supply, porous rock, and a hot, sunny or windy climate to drive evaporation. Killiney Beach, Co. Dublin, shows evidence of salt weathering on exposed coastal rock faces. Thermal Expansion: In regions with extreme diurnal temperature ranges, such as deserts, rocks expand significantly when heated and contract when cooled at night. The outer surface of the rock heats and cools much faster than the interior — this differential expansion and contraction causes the outer layers to peel away. This process is called exfoliation or onion-skin weathering and it produces characteristic rounded boulders and layered rock surfaces. Dark-coloured rocks absorb more solar radiation and are more susceptible to thermal expansion than light-coloured rocks.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo4-eq-2",
        source: "LC Geography — Sample 2020",
        parts: [
          {
            label: "Q2.",
            question: "Explain one process of physical weathering and one process of chemical weathering.",
            marks: 30,
            model: "Physical — Freeze-Thaw: Three conditions are required: fluctuating temperatures above and below 0°C, adequate water, and pre-existing fractures in the rock. Water enters cracks in the rock surface and freezes — expanding by approximately 9% and exerting intense pressure on the surrounding rock. Repeated freeze-thaw cycles progressively widen the fractures until fragments of rock break away from the surface. These rock fragments accumulate at the base of the slope as scree deposits — Great Sugarloaf, Co. Wicklow, shows prominent scree slopes as evidence. Chemical — Carbonation: Carbonation occurs when rainwater absorbs CO₂ from the atmosphere, forming a weak carbonic acid. The carbonic acid reacts with calcium carbonate in the limestone rock, dissolving it in a process called carbonation or carbonate dissolution. Three conditions are required: adequate rainfall, CO₂ in the atmosphere, and calcium carbonate (limestone) rock. Cold water absorbs more CO₂ than warm water — making carbonation most effective in cold, wet climates such as Ireland's. Water percolates downward through natural joints in the limestone, dissolving and widening the cracks. The dissolved joints become grikes — the remaining raised rock surfaces between them are called clints. This creates the limestone pavement characteristic of karst landscapes — the Burren, Co. Clare, is Ireland's finest example. Chemical — Hydrolysis: Hydrolysis occurs when minerals in rocks react chemically with acidic water — part of the mineral dissolves and the rest is transformed into a new, weaker substance. Feldspar minerals in granite, for example, break down through hydrolysis into kaolin (clay) — this weakens the rock structure from within, making it more susceptible to further erosion. Hydrolysis differs from carbonation in that the minerals are not fully washed away but chemically changed into weaker materials. Ireland's high rainfall and humid temperate climate make hydrolysis a widespread and significant weathering process across the country.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── geo5: Karst Regions / Limestone Landscapes ────────────────────────────
  (function () {
    var c = ch("geo5");
    // 5.1 — Limestone Pavement Formation
    c.learningOutcomes[0].notes = [
      {
        h: "Formation of Limestone Pavement",
        b: "Limestone is a stratified sedimentary rock — contains joints, bedding planes and fissures that allow water to percolate through. Glaciers removed the soil cover — exposing bare limestone to exogenic (surface) forces. Limestone is permeable — water passes through it, dissolving the calcium carbonate through carbonation."
      },
      {
        h: "Carbonation Process on the Pavement",
        b: "Rainwater absorbs CO₂ from the atmosphere to form weak carbonic acid. Acid reacts with calcium carbonate in the limestone — dissolving the rock along joints and bedding planes. Joints are widened by dissolution into grikes — the remaining raised blocks are called clints. Carbonation continues on the surface of clints — forming shallow channels called karrens; as water runs off the edge it creates flutings."
      },
      {
        h: "Dolines",
        b: "Solution doline: water runs across a joint and progressively dissolves the rock — forming a funnel-shaped pit that deepens over time. Collapse doline: underlying cavity grows until the roof collapses — forms steep-walled circular hollows; common in Ireland. Both features are characteristic surface landforms of karst landscapes."
      },
      {
        h: "Swallow Holes & Caves",
        b: "Swallow holes (sinkholes): funnel-shaped surface features where a river disappears underground into the cave system. Cave systems form as water flows from swallow holes through the rock — carbonation, solution and hydraulic action carve out large caverns. Stalactites form on cave ceilings — calcite deposited as mineral-rich water evaporates, building downward slowly over thousands of years. Stalagmites form on cave floors — calcite drips down and accumulates upward; pillars form when both join."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a karst landscape?",
        definition: "Exposed landscape of soluble limestone rock characterised by surface and underground features shaped by carbonation, freeze-thaw and glacial erosion; ~13% of the world's land surface.",
        section: "5.1"
      },
      {
        term: "What is an aquifer?",
        definition: "Body of rock capable of holding groundwater; karst landscapes function as natural aquifers.",
        section: "5.1"
      },
      {
        term: "What is a limestone pavement?",
        definition: "Large area of exposed, flat limestone from which soil has been removed by glaciation; the surface is patterned by clints and grikes through carbonation.",
        section: "5.2"
      },
      {
        term: "What are clints?",
        definition: "Flat-topped segments of limestone on a pavement separated from each other by grikes.",
        section: "5.2"
      },
      {
        term: "What are grikes?",
        definition: "Gaps or fissures in a limestone pavement formed when carbonation progressively widens the natural joints between clints.",
        section: "5.2"
      },
      {
        term: "What are karren?",
        definition: "Small hollows dissolved into the upper surface of clints by carbonic acid pooling on them.",
        section: "5.2"
      },
      {
        term: "What is a doline (sinkhole)?",
        definition: "Enclosed depression in a limestone landscape formed by slow solution or sudden collapse of rock; funnels surface water underground.",
        section: "5.2"
      },
      {
        term: "What is a swallow hole?",
        definition: "Funnel-shaped surface opening in a karst landscape into which a river flows and disappears underground; entrance to cave systems.",
        section: "5.2"
      },
      {
        term: "What is The Burren?",
        definition: "Ireland's most famous limestone pavement in County Clare; formed ~320 million years ago when Ireland was submerged under a shallow tropical sea; UNESCO Global Geopark.",
        section: "5.2"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Explain how chemical weathering has shaped the limestone pavement in a karst region.",
        model: "Formation of Limestone Pavement: Limestone is a stratified sedimentary rock containing joints, bedding planes and fissures that allow water to percolate through the rock. Glaciers during the last ice age removed the soil cover from the limestone, exposing the bare rock surface to exogenic (surface) forces. Limestone is permeable — water passes directly through it, dissolving calcium carbonate through the process of carbonation. The exposed limestone surface is progressively lowered and shaped by carbonation into a distinctive flat pavement landscape. Carbonation Process: Rainwater absorbs CO₂ from the atmosphere and soil to form a weak carbonic acid solution. This carbonic acid reacts with the calcium carbonate in the limestone, dissolving the rock along its natural joints and bedding planes. The joints are progressively widened by dissolution into deep vertical channels called grikes — the remaining raised limestone blocks between grikes are called clints. Karrens (shallow channels) form on the upper surfaces of clints as acidic water flows across them. Flutings form on the edges of clints where water runs off the sides, creating vertical grooved channels. Dolines: A solution doline forms where water runs across a joint and progressively dissolves the rock from the surface downward, forming a funnel-shaped pit. A collapse doline forms when an underground cavity grows large enough that its roof collapses inward, creating steep-walled circular hollows. Collapse dolines are common in Ireland, particularly in the Burren region of Co. Clare. Swallow Holes and Caves: Swallow holes (sinkholes) are funnel-shaped surface features where a surface river disappears underground into the cave system below. Cave systems form as water flows from swallow holes through the rock — carbonation, solution and hydraulic action together carve out large caverns over thousands of years. Stalactites form on cave ceilings as mineral-rich water evaporates, depositing calcite; stalagmites build up from the cave floor where the water drips — when both meet, they form a pillar."
      }
    ];
    // 5.2 — Underground Karst Landforms
    c.learningOutcomes[1].notes = [
      {
        h: "How Cave Systems Form",
        b: "Swallow holes provide an entry point for surface water into the limestone bedrock. Carbonation dissolves the calcium carbonate along joints and bedding planes — gradually enlarging passages into cave systems. Hydraulic action of flowing water erodes the cave floor and walls — increasing the volume of the cave over time. Most karst caves form below the water table (zone of saturation) — the greater the water volume, the faster the cave develops."
      },
      {
        h: "Stalactites",
        b: "Mineral-rich (calcium carbonate) water seeps through the cave ceiling. Water evaporates — leaving a tiny deposit of calcite behind. Repeated over thousands of years — calcite builds up into a spike hanging from the ceiling (stalactite). Growth is extremely slow — ~1 cm per 100 years in most cases."
      },
      {
        h: "Stalagmites and Pillars",
        b: "Calcium carbonate-rich water drips to the cave floor and evaporates — building a column upward (stalagmite). Curtains form when water runs in a thin sheet along a sloping ceiling — depositing a thin wavy sheet of calcite. When a stalactite and stalagmite meet they form a pillar — a complete calcite column from floor to ceiling. Aillwee Cave, Co. Clare — one of Ireland's oldest known cave systems, formed in the Burren limestone; open to tourists; shows all these features."
      }
    ];
    c.learningOutcomes[1].keyTerms = [
      {
        term: "What is a karst cave system?",
        definition: "Underground passage carved by carbonation, erosion and solution from a swallow hole; forms below the water table along joints and bedding planes of limestone.",
        section: "5.3"
      },
      {
        term: "What is a stalactite?",
        definition: "Downward-growing calcite formation hanging from a cave ceiling; forms as mineral-rich water drips slowly and deposits calcite.",
        section: "5.3"
      },
      {
        term: "What is a stalagmite?",
        definition: "Upward-growing calcite formation on a cave floor; forms directly below a stalactite from dripping mineral-rich water.",
        section: "5.3"
      },
      {
        term: "What is a pillar?",
        definition: "Cave formation created when a stalactite and stalagmite grow together and join.",
        section: "5.3"
      },
      {
        term: "What are speleothems?",
        definition: "General term for all calcite formations (dripstone features) inside limestone caves; rate of growth depends on temperature and precipitation.",
        section: "5.3"
      },
      {
        term: "What is the zone of saturation?",
        definition: "Area below the water table where all rock spaces are filled with water; most karst cave systems form here.",
        section: "5.3"
      },
      {
        term: "What is a karst life cycle?",
        definition: "Three stages of karst development: youthful (surface features form), mature (underground drainage develops), old (limestone removed, caves collapse, rivers flow over impermeable bedrock).",
        section: "5.4"
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "With reference to the Irish landscape, examine the processes which have influenced the development of an underground landform in a karst region.",
        model: "Cave Formation: Swallow holes provide an entry point for surface water to enter the limestone bedrock and begin forming cave systems. Carbonation dissolves the calcium carbonate along joints and bedding planes — gradually enlarging passages and caverns over thousands of years. Hydraulic action of the flowing water erodes the cave floor and walls further — increasing the volume of the cave system over time. Most karst caves form below the water table in the zone of saturation — the greater the water volume, the faster the cave develops. As the water table drops over geological time, the cave passages become air-filled and speleothem features begin to form. Stalactites: Mineral-rich (calcium carbonate) water seeps slowly through the cave ceiling from the rock above. The water evaporates on the ceiling surface, leaving a tiny deposit of calcite behind. This process is repeated over thousands of years, and the calcite deposits build into a spike hanging downward from the ceiling — a stalactite. Stalactite growth is extremely slow — approximately 1 cm per 100 years in most cave environments. Stalagmites and Pillars: Calcium carbonate-rich water drips from the ceiling to the cave floor, where it evaporates and deposits calcite — building a column upward over time, forming a stalagmite. Curtains form when water runs in a thin sheet along a sloping ceiling — depositing a thin, wavy curtain of calcite hanging downward. When a stalactite and a stalagmite grow toward each other and eventually meet, they form a pillar — a complete calcite column from floor to ceiling. Aillwee Cave, Co. Clare, is one of Ireland's oldest known cave systems, formed in the Burren limestone over hundreds of thousands of years. It is open to tourists and contains examples of stalactites, stalagmites, pillars and other cave features. The Burren's underground drainage system is one of the most extensive karst cave networks in Ireland."
      }
    ];
    c.examQuestions = [
      {
        id: "geo5-eq-1",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q1.",
            question: "Explain how chemical weathering has shaped the limestone pavement in a karst region.",
            marks: 30,
            model: "Formation of Limestone Pavement: Limestone is a stratified sedimentary rock containing joints, bedding planes and fissures that allow water to percolate through the rock. Glaciers during the last ice age removed the soil cover from the limestone, exposing the bare rock surface to exogenic (surface) forces. Limestone is permeable — water passes directly through it, dissolving calcium carbonate through the process of carbonation. The exposed limestone surface is progressively lowered and shaped by carbonation into a distinctive flat pavement landscape. Carbonation Process: Rainwater absorbs CO₂ from the atmosphere and soil to form a weak carbonic acid solution. This carbonic acid reacts with the calcium carbonate in the limestone, dissolving the rock along its natural joints and bedding planes. The joints are progressively widened by dissolution into deep vertical channels called grikes — the remaining raised limestone blocks between grikes are called clints. Karrens (shallow channels) form on the upper surfaces of clints as acidic water flows across them. Flutings form on the edges of clints where water runs off the sides, creating vertical grooved channels. Dolines: A solution doline forms where water runs across a joint and progressively dissolves the rock from the surface downward, forming a funnel-shaped pit. A collapse doline forms when an underground cavity grows large enough that its roof collapses inward, creating steep-walled circular hollows. Collapse dolines are common in Ireland, particularly in the Burren region of Co. Clare. Swallow Holes and Caves: Swallow holes (sinkholes) are funnel-shaped surface features where a surface river disappears underground into the cave system below. Cave systems form as water flows from swallow holes through the rock — carbonation, solution and hydraulic action together carve out large caverns over thousands of years. Stalactites form on cave ceilings as mineral-rich water evaporates, depositing calcite; stalagmites build up from the cave floor where the water drips — when both meet, they form a pillar.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo5-eq-2",
        source: "LC Geography — Sample 2010",
        parts: [
          {
            label: "Q2.",
            question: "With reference to the Irish landscape, examine the processes which have influenced the development of an underground landform in a karst region.",
            marks: 30,
            model: "Cave Formation: Swallow holes provide an entry point for surface water to enter the limestone bedrock and begin forming cave systems. Carbonation dissolves the calcium carbonate along joints and bedding planes — gradually enlarging passages and caverns over thousands of years. Hydraulic action of the flowing water erodes the cave floor and walls further — increasing the volume of the cave system over time. Most karst caves form below the water table in the zone of saturation — the greater the water volume, the faster the cave develops. As the water table drops over geological time, the cave passages become air-filled and speleothem features begin to form. Stalactites: Mineral-rich (calcium carbonate) water seeps slowly through the cave ceiling from the rock above. The water evaporates on the ceiling surface, leaving a tiny deposit of calcite behind. This process is repeated over thousands of years, and the calcite deposits build into a spike hanging downward from the ceiling — a stalactite. Stalactite growth is extremely slow — approximately 1 cm per 100 years in most cave environments. Stalagmites and Pillars: Calcium carbonate-rich water drips from the ceiling to the cave floor, where it evaporates and deposits calcite — building a column upward over time, forming a stalagmite. Curtains form when water runs in a thin sheet along a sloping ceiling — depositing a thin, wavy curtain of calcite hanging downward. When a stalactite and a stalagmite grow toward each other and eventually meet, they form a pillar — a complete calcite column from floor to ceiling. Aillwee Cave, Co. Clare, is one of Ireland's oldest known cave systems, formed in the Burren limestone over hundreds of thousands of years. It is open to tourists and contains examples of stalactites, stalagmites, pillars and other cave features. The Burren's underground drainage system is one of the most extensive karst cave networks in Ireland.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── geo6: Surface Processes — Rivers, Coasts & Mass Movement ──────────────
  (function () {
    var c = ch("geo6");
    // 6.1 — Erosion — Meander Formation
    c.learningOutcomes[0].notes = [
      {
        h: "River Erosion Processes",
        b: "Hydraulic action: force of moving water dislodges loose material from the river bed and banks. Abrasion: sediment carried by the river scrapes and wears down the bed and banks like sandpaper. Solution: slightly acidic river water dissolves soluble minerals (e.g. limestone) from the river bed. Attrition: sediment particles collide with each other, becoming smaller and more rounded as they travel downstream."
      },
      {
        h: "Meander Formation",
        b: "In the middle course of a river, lateral (sideways) erosion dominates over vertical (downward) erosion. The thalweg (fastest current) swings to the outer bank of any slight bend — erosion cuts a steep river cliff here. On the inner bank, velocity is lower — deposition of sediment forms a gentle slip-off slope (point bar). The bend is progressively accentuated — a meander develops, widening the river valley laterally."
      },
      {
        h: "Oxbow Lake Formation",
        b: "Continued erosion of the outer banks of adjacent meanders narrows the neck of land between them. During a flood, the river cuts through the neck — taking the straighter, shorter course. The abandoned meander loop is cut off — sealed by deposition to form an oxbow lake. Example: River Lee, Cork — shows meander features in its middle course through the Lee Valley."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a meander?",
        definition: "Curving loop or bend in a river's middle to lower course formed by differential erosion and deposition; outer bank erodes while inner bank deposits sediment.",
        section: "6.1"
      },
      {
        term: "What is hydraulic action?",
        definition: "River erosion caused by the force of water hitting rock surfaces; most powerful on the outside of meander bends.",
        section: "6.1"
      },
      {
        term: "What is abrasion?",
        definition: "River erosion where transported rocks scrape and wear away the bed and banks through friction.",
        section: "6.1"
      },
      {
        term: "What is attrition?",
        definition: "River erosion where rocks carried by the river collide with each other, becoming smaller and smoother over time.",
        section: "6.1"
      },
      {
        term: "What is lateral erosion?",
        definition: "Widening of a river channel; dominant in the middle and lower course; responsible for meander formation.",
        section: "6.1"
      },
      {
        term: "What is vertical erosion?",
        definition: "Deepening of a river channel; dominant in the upper course; creates V-shaped valleys.",
        section: "6.1"
      },
      {
        term: "What is an oxbow lake?",
        definition: "Crescent-shaped lake formed when a river cuts through a meander neck, isolating the loop and shortening its course.",
        section: "6.2"
      },
      {
        term: "What is a floodplain?",
        definition: "Wide, flat river valley floor that floods during heavy rainfall; built up by alluvium deposits from repeated flooding.",
        section: "6.2"
      },
      {
        term: "What are interlocking spurs?",
        definition: "Ridges of land alternating on either side of an upper course valley as the river winds around obstacles of hard rock.",
        section: "6.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine the role of erosion on the formation of a fluvial landform.",
        model: "River Erosion Processes: Hydraulic action is the force of moving water dislodging loose material from the river bed and banks — powerful in fast-flowing reaches. Abrasion occurs when sediment carried by the river scrapes and wears down the bed and banks like sandpaper — most effective when coarse material is transported. Solution is the chemical weathering process by which slightly acidic river water dissolves soluble minerals such as limestone from the river bed. Attrition occurs when sediment particles collide with each other during transport — they become progressively smaller and more rounded as they travel downstream. Meander Formation: In the middle course of a river, the gradient decreases and lateral (sideways) erosion dominates over vertical (downward) erosion. The thalweg — the line of fastest current — swings to the outer bank of any slight bend in the channel. On the outer bank, higher velocity erosion undercuts the bank, creating a steep river cliff (a river bluff). On the inner bank, water velocity is lower — deposition of sediment forms a gentle slip-off slope called a point bar. The bend is progressively accentuated as outer bank erosion and inner bank deposition continue — a meander loop develops. As meanders develop, they migrate downstream and widen the valley laterally, forming a broad floodplain. Oxbow Lake Formation: Continued erosion of the outer banks of adjacent meanders progressively narrows the neck of land between them. During a flood event, the river cuts through the narrow neck — taking the shorter, straighter course. The abandoned meander loop is cut off from the main channel and sealed by deposition at both ends. The isolated water body forms an oxbow lake — it gradually silts up and may become a marshy area over time. The River Lee in Cork shows classic meander features in its middle course through the Lee Valley."
      }
    ];
    // 6.2 — Deposition — Beach and Spit Formation
    c.learningOutcomes[1].notes = [
      {
        h: "Coastal Deposition Processes",
        b: "Longshore drift: waves approach the shore at an angle (driven by prevailing wind) — swash carries sediment up the beach at the same angle. Backwash returns directly down the slope under gravity — net movement of sediment along the coast. When energy is reduced (sheltered bay, change in coastal direction), sediment is deposited."
      },
      {
        h: "Beach Formation",
        b: "Beaches form in sheltered bays where wave energy is low enough for deposition to exceed erosion. Constructive waves (low frequency, strong swash) build beaches up by depositing sand and shingle. Beach material is graded — coarser material near the back of the beach, finer material at the waterline. Storm beaches form ridges of coarser material above the normal high tide line — deposited by high-energy storm waves."
      },
      {
        h: "Spit Formation",
        b: "Where the coastline changes direction abruptly, longshore drift continues to carry sediment in the original direction. Sediment is deposited in open water — extending as a narrow ridge of sand or shingle called a spit. Waves refract around the tip of the spit — causing it to curve into a hooked or recurved end. Sheltered water behind the spit allows mud and vegetation to accumulate — eventually forming a salt marsh. Example: Inch Spit, Co. Kerry — formed by longshore drift extending into Dingle Bay."
      }
    ];
    c.learningOutcomes[1].keyTerms = [
      {
        term: "What is longshore drift?",
        definition: "Movement of sediment along a coastline caused by waves approaching at an angle from the prevailing wind; swash moves sediment diagonally, backwash pulls it straight back.",
        section: "6.2"
      },
      {
        term: "What is a constructive wave?",
        definition: "Low-height, long-wavelength wave with a strong swash relative to backwash; deposits sediment and builds beaches.",
        section: "6.2"
      },
      {
        term: "What is a destructive wave?",
        definition: "High-height, short-wavelength wave with a strong backwash; produced in large oceans with large fetch; erodes the coastline.",
        section: "6.2"
      },
      {
        term: "What is a spit?",
        definition: "Long, narrow ridge of sand and shingle projecting from the coastline into the sea; formed by longshore drift depositing sediment beyond a bend in the coastline.",
        section: "6.2"
      },
      {
        term: "What is a tombolo?",
        definition: "Sand spit that has extended to connect the mainland to an offshore island.",
        section: "6.2"
      },
      {
        term: "What is a bay mouth bar?",
        definition: "Sand spit that grows across the mouth of a bay, creating a lagoon behind it.",
        section: "6.2"
      },
      {
        term: "What is wave refraction?",
        definition: "Process where waves bend as they approach the coastline due to differences in water depth; concentrates erosion energy on resistant headlands.",
        section: "6.1"
      },
      {
        term: "What is a headland?",
        definition: "Resistant rock mass projecting into the sea at a discordant coastline; formed when softer rock between bands of hard rock is eroded faster.",
        section: "6.2"
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine the role of deposition on the formation of a coastal landform.",
        model: "Coastal Deposition Processes: Longshore drift is the primary mechanism of sediment transport along coastlines — waves approach the shore at an angle driven by the prevailing wind, and the swash carries sediment up the beach at that angle. The backwash returns directly down the slope under gravity, carrying some sediment with it — the net result is the gradual movement of sediment along the coast in the direction of the prevailing wind. When wave energy is reduced by a sheltered bay or a change in coastal direction, the carrying capacity drops and sediment is deposited. Beach Formation: Beaches form in sheltered bays where wave energy is low enough for deposition to consistently exceed erosion. Constructive waves — characterised by low frequency and a strong swash — build beaches up by depositing sand and shingle on the shore. Beach material is graded along the profile — coarser, heavier material (shingle) accumulates near the back of the beach, while finer sand settles near the waterline. Storm beaches form ridges of coarser material well above the normal high tide line — deposited by the exceptional energy of storm waves. Spit Formation: Where the coastline changes direction abruptly, longshore drift continues to carry sediment in its original direction beyond the change in coastline. Sediment is deposited in the open water beyond the coastline — extending as a narrow ridge of sand or shingle called a spit. The spit grows progressively longer as longshore drift continues to add material to its seaward end. Waves refract (bend) around the tip of the spit — causing the end to curve inward, forming a characteristic hooked or recurved end. The water behind the spit is sheltered from wave energy — sediment settles and mud accumulates; salt-tolerant vegetation colonises the area, eventually forming a salt marsh. Salt marshes provide important coastal habitats and act as natural buffers against storm surge and coastal flooding. Inch Spit in Co. Kerry is a classic Irish example — formed by longshore drift extending southwestward into Dingle Bay."
      }
    ];
    // 6.3 — Human Activity — Flood Control on Rivers
    c.learningOutcomes[2].notes = [
      {
        h: "Why Rivers Flood",
        b: "Natural flooding occurs when precipitation exceeds the river's capacity — occurs in lower course where the floodplain is wide. Urbanisation increases impermeable surfaces — rainwater runs off faster into rivers, increasing flood risk. Deforestation reduces interception and infiltration — more water reaches the river channel more quickly."
      },
      {
        h: "Hard Engineering — Channel Modifications and Dams",
        b: "Channelisation (straightening and deepening) increases flow velocity — moves floodwater downstream more rapidly. Artificial levees (embankments) raise the bank height — contain higher water volumes within the channel. Flood walls in urban areas (e.g. Dublin City Quays) protect property — but increase risk downstream by concentrating flow. Dams hold back excess water in reservoirs — releasing it gradually to prevent flooding. Poulaphouca Reservoir, Co. Wicklow, built on the River Liffey — reduces flood risk to downstream areas including Dublin. Dams trap sediment — downstream channel is sediment-starved, increasing erosion (channel incision)."
      },
      {
        h: "Soft Engineering",
        b: "Flood plain zoning: kept as open land — allows natural storage of floodwater. Wetland restoration and tree planting in catchment areas slow runoff — reducing peak discharge. Sustainable urban drainage systems (SUDS): permeable paving and retention ponds — mimic natural drainage patterns."
      }
    ];
    c.learningOutcomes[2].keyTerms = [
      {
        term: "What is a drainage basin?",
        definition: "Area of land where all precipitation collects and drains into a common body of water such as a river, lake or sea.",
        section: "6.3"
      },
      {
        term: "What is hard engineering?",
        definition: "Flood or coastal management using artificial structures (dams, sea walls, levees, groynes) to control natural processes.",
        section: "6.3"
      },
      {
        term: "What is soft engineering?",
        definition: "Sustainable flood or coastal management that works with natural processes (beach nourishment, managed retreat, floodplain zoning) rather than building structures.",
        section: "6.3"
      },
      {
        term: "What is a natural levee?",
        definition: "Ridge that builds up along river banks through repeated alluvium deposits when a river floods and then drops sediment as it spreads across the floodplain.",
        section: "6.2"
      },
      {
        term: "What is urbanisation?",
        definition: "Growth of urban settlement; increases surface run-off by replacing permeable vegetation with impermeable concrete, raising flood risk.",
        section: "6.3"
      },
      {
        term: "What is deposition in rivers?",
        definition: "Process where a river drops transported material as it loses energy; dominant in the lower course; produces floodplains, natural levees and deltas.",
        section: "6.2"
      },
      {
        term: "What is a river delta?",
        definition: "Landform at a river's mouth where deposition creates new land as sediment accumulates; types include arcuate, bird's foot and estuarine.",
        section: "6.2"
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine the impacts of flood control on river processes.",
        model: "Why Rivers Flood: Natural flooding occurs when precipitation exceeds the river's capacity to contain the water — most common in the lower course where the floodplain is wide and flat. Urbanisation significantly increases impermeable surfaces such as roads, car parks and rooftops — rainwater runs off into rivers much faster than it would through natural vegetation, increasing flood peaks. Deforestation reduces interception (water caught by leaves) and infiltration (water soaking into the soil) — more water reaches the river channel more quickly, raising flood risk. Hard Engineering — Channel Modifications: Channelisation involves straightening and deepening the river channel — this increases flow velocity and moves floodwater downstream more rapidly, reducing local flood risk. Artificial levees (embankments) raise the height of the river bank above natural levels — containing higher volumes of water within the channel during flood events. Flood walls in urban areas, such as those along Dublin City Quays, protect property from flooding — but can increase flood risk downstream by concentrating flow. Dams and Reservoirs: Dams are built across rivers to hold back excess water in an upstream reservoir during periods of high rainfall. Water is released gradually and in a controlled manner to prevent downstream flooding. Poulaphouca Reservoir, Co. Wicklow, was built on the River Liffey — it significantly reduces flood risk to downstream areas including Dublin city. One drawback of dams is that they trap sediment — the downstream channel becomes sediment-starved, which can increase channel erosion (incision). Soft Engineering: Flood plain zoning keeps river floodplains as open agricultural land or parks — allowing natural temporary storage of floodwater without property damage. Wetland restoration and strategic tree planting in the river's catchment area slow the rate of surface runoff — reducing the peak discharge that reaches the channel. Sustainable Urban Drainage Systems (SUDS) — including permeable paving and retention ponds — mimic natural drainage patterns and reduce flash flood risk. Soft engineering approaches are more environmentally sustainable and less disruptive to river ecosystems than hard engineering. A combined approach using both hard and soft engineering is now recommended by hydrologists and the Office of Public Works (OPW) in Ireland."
      }
    ];
    // 6.4 — Mass Movement — Landslides
    c.learningOutcomes[3].notes = [
      {
        h: "What is mass movement?",
        b: "Mass movement is the downslope movement of rock, soil or debris under the influence of gravity — no water or ice needed as a transport medium. The trigger can be natural (heavy rain, earthquakes) or human-induced (deforestation, construction, vibration from machinery)."
      },
      {
        h: "Factors Governing Landslides",
        b: "Slope angle: steeper slopes increase gravitational stress on material — material more likely to fail above a critical angle. Water saturation: heavy rainfall adds weight to slope material and reduces friction between particles — known as pore water pressure. Rock/soil type: weak, impermeable rock (e.g. clay) becomes unstable when wet — impermeable layer below saturated soil acts as a slip plane. Vegetation removal: tree roots bind soil; deforestation removes this anchorage — greatly increases landslide risk."
      },
      {
        h: "Human Factors and Consequences",
        b: "Road and building construction on steep slopes undercuts the natural support of the hillside — removes material from the base (toe) of the slope, triggering failure. Agricultural overgrazing strips vegetation — increases surface runoff and destabilises slope material. Example: Connemara and West Mayo — increased landslide frequency linked to overgrazing on blanket bog and peat soils. Primary consequences: direct burial of buildings, roads and infrastructure. Secondary: disruption to transport networks, contamination of water supplies."
      }
    ];
    c.learningOutcomes[3].keyTerms = [
      {
        term: "What is mass movement?",
        definition: "Movement of regolith downslope under the influence of gravity; classified by type of failure, material, motion and rate of movement.",
        section: "6.4"
      },
      {
        term: "What is regolith?",
        definition: "Layer of loose rock, soil, mud and dust sitting on bedrock; easily mobilised by gravity, water or seismic activity.",
        section: "6.4"
      },
      {
        term: "What is soil creep?",
        definition: "Slowest form of mass movement; gradual downslope movement of soil driven by gravity, wetting-drying cycles and freeze-thaw action; evidence includes terracettes and tilting poles.",
        section: "6.4"
      },
      {
        term: "What is solifluction?",
        definition: "Slow downslope flow of saturated soil over permafrost; occurs in upland and polar areas where frozen ground prevents drainage.",
        section: "6.4"
      },
      {
        term: "What is a rockslide?",
        definition: "Fast downslope movement of large areas of solid bedrock triggered when gravitational force exceeds the slope's resistance; common in mountain and coastal areas.",
        section: "6.4"
      },
      {
        term: "What is slumping?",
        definition: "Rotational sliding of loose regolith along a curved surface; triggered when the base of a slope is removed by river erosion or wave action.",
        section: "6.4"
      },
      {
        term: "What is a mudflow?",
        definition: "Fast-moving flow of extremely saturated loose soil down a slope; most common in high mountainous areas with thin vegetation.",
        section: "6.4"
      },
      {
        term: "What is a lahar?",
        definition: "Volcanic mudflow composed of pyroclastic material; triggered when volcanic eruptions melt snow or glaciers.",
        section: "6.4"
      },
      {
        term: "What is a bogburst?",
        definition: "Sudden movement of saturated peatland or blanket bog downslope; triggered by heavy rainfall; a hazard in western Ireland.",
        section: "6.4"
      },
      {
        term: "What is permafrost?",
        definition: "Ground frozen for two or more years; makes overlying soil impermeable, causing waterlogging and increasing susceptibility to solifluction.",
        section: "6.4"
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Describe and explain the factors governing the operation of one mass movement process.",
        model: "Mass Movement: Mass movement is the downslope movement of rock, soil or debris under the direct influence of gravity — no water or ice is needed as a transport medium. Landslides are a form of rapid mass movement in which large volumes of material slide suddenly downslope along a failure plane. The trigger for a landslide can be natural — such as heavy prolonged rainfall or an earthquake — or human-induced, such as deforestation, construction or the vibration of heavy machinery. Factors Governing Landslides: Slope angle is a fundamental factor — steeper slopes increase the gravitational stress on slope material, making failure more likely above a critical angle. Water saturation is a key trigger — heavy rainfall adds significant weight to slope material and reduces friction between particles through pore water pressure. Saturated material loses its internal cohesion and shear strength — the slope material fails and flows downslope. Rock and soil type is critical — weak, impermeable rock such as clay becomes highly unstable when saturated with water. An impermeable layer of rock or clay beneath saturated soil acts as a slip plane — the overlying material slides across it during a failure event. Vegetation removal is highly significant — tree roots bind soil particles together and absorb water; deforestation removes this anchorage and greatly increases landslide risk. Human Factors: Road and building construction on steep slopes undercuts the natural toe support of the hillside — removing material from the base of the slope destabilises the slope above. Agricultural overgrazing strips the protective vegetation from slopes — increasing surface runoff and destabilising the slope material below. Connemara and West Mayo have experienced increased landslide frequency in recent decades, linked to overgrazing on blanket bog and peat soils. Consequences: Primary consequences include the direct burial of buildings, roads and infrastructure by displaced material. Secondary consequences include prolonged disruption to transport networks and contamination of water supplies. Recovery is costly and slow — landslide-prone areas require long-term engineering stabilisation and land management reform."
      }
    ];
    c.examQuestions = [
      {
        id: "geo6-eq-1",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q1.",
            question: "Examine the role of erosion on the formation of a fluvial landform.",
            marks: 30,
            model: "River Erosion Processes: Hydraulic action is the force of moving water dislodging loose material from the river bed and banks — powerful in fast-flowing reaches. Abrasion occurs when sediment carried by the river scrapes and wears down the bed and banks like sandpaper — most effective when coarse material is transported. Solution is the chemical weathering process by which slightly acidic river water dissolves soluble minerals such as limestone from the river bed. Attrition occurs when sediment particles collide with each other during transport — they become progressively smaller and more rounded as they travel downstream. Meander Formation: In the middle course of a river, the gradient decreases and lateral (sideways) erosion dominates over vertical (downward) erosion. The thalweg — the line of fastest current — swings to the outer bank of any slight bend in the channel. On the outer bank, higher velocity erosion undercuts the bank, creating a steep river cliff (a river bluff). On the inner bank, water velocity is lower — deposition of sediment forms a gentle slip-off slope called a point bar. The bend is progressively accentuated as outer bank erosion and inner bank deposition continue — a meander loop develops. As meanders develop, they migrate downstream and widen the valley laterally, forming a broad floodplain. Oxbow Lake Formation: Continued erosion of the outer banks of adjacent meanders progressively narrows the neck of land between them. During a flood event, the river cuts through the narrow neck — taking the shorter, straighter course. The abandoned meander loop is cut off from the main channel and sealed by deposition at both ends. The isolated water body forms an oxbow lake — it gradually silts up and may become a marshy area over time. The River Lee in Cork shows classic meander features in its middle course through the Lee Valley.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo6-eq-2",
        source: "LC Geography — Long Question (Sample 2021)",
        parts: [
          {
            label: "Q2.",
            question: "Examine the role of deposition on the formation of a coastal landform.",
            marks: 30,
            model: "Coastal Deposition Processes: Longshore drift is the primary mechanism of sediment transport along coastlines — waves approach the shore at an angle driven by the prevailing wind, and the swash carries sediment up the beach at that angle. The backwash returns directly down the slope under gravity, carrying some sediment with it — the net result is the gradual movement of sediment along the coast in the direction of the prevailing wind. When wave energy is reduced by a sheltered bay or a change in coastal direction, the carrying capacity drops and sediment is deposited. Beach Formation: Beaches form in sheltered bays where wave energy is low enough for deposition to consistently exceed erosion. Constructive waves — characterised by low frequency and a strong swash — build beaches up by depositing sand and shingle on the shore. Beach material is graded along the profile — coarser, heavier material (shingle) accumulates near the back of the beach, while finer sand settles near the waterline. Storm beaches form ridges of coarser material well above the normal high tide line — deposited by the exceptional energy of storm waves. Spit Formation: Where the coastline changes direction abruptly, longshore drift continues to carry sediment in its original direction beyond the change in coastline. Sediment is deposited in the open water beyond the coastline — extending as a narrow ridge of sand or shingle called a spit. The spit grows progressively longer as longshore drift continues to add material to its seaward end. Waves refract (bend) around the tip of the spit — causing the end to curve inward, forming a characteristic hooked or recurved end. The water behind the spit is sheltered from wave energy — sediment settles and mud accumulates; salt-tolerant vegetation colonises the area, eventually forming a salt marsh. Salt marshes provide important coastal habitats and act as natural buffers against storm surge and coastal flooding. Inch Spit in Co. Kerry is a classic Irish example — formed by longshore drift extending southwestward into Dingle Bay.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo6-eq-3",
        source: "LC Geography — Sample 2019",
        parts: [
          {
            label: "Q3.",
            question: "Examine the impacts of flood control on river processes.",
            marks: 30,
            model: "Why Rivers Flood: Natural flooding occurs when precipitation exceeds the river's capacity to contain the water — most common in the lower course where the floodplain is wide and flat. Urbanisation significantly increases impermeable surfaces such as roads, car parks and rooftops — rainwater runs off into rivers much faster than it would through natural vegetation, increasing flood peaks. Deforestation reduces interception (water caught by leaves) and infiltration (water soaking into the soil) — more water reaches the river channel more quickly, raising flood risk. Hard Engineering — Channel Modifications: Channelisation involves straightening and deepening the river channel — this increases flow velocity and moves floodwater downstream more rapidly, reducing local flood risk. Artificial levees (embankments) raise the height of the river bank above natural levels — containing higher volumes of water within the channel during flood events. Flood walls in urban areas, such as those along Dublin City Quays, protect property from flooding — but can increase flood risk downstream by concentrating flow. Dams and Reservoirs: Dams are built across rivers to hold back excess water in an upstream reservoir during periods of high rainfall. Water is released gradually and in a controlled manner to prevent downstream flooding. Poulaphouca Reservoir, Co. Wicklow, was built on the River Liffey — it significantly reduces flood risk to downstream areas including Dublin city. One drawback of dams is that they trap sediment — the downstream channel becomes sediment-starved, which can increase channel erosion (incision). Soft Engineering: Flood plain zoning keeps river floodplains as open agricultural land or parks — allowing natural temporary storage of floodwater without property damage. Wetland restoration and strategic tree planting in the river's catchment area slow the rate of surface runoff — reducing the peak discharge that reaches the channel. Sustainable Urban Drainage Systems (SUDS) — including permeable paving and retention ponds — mimic natural drainage patterns and reduce flash flood risk. Soft engineering approaches are more environmentally sustainable and less disruptive to river ecosystems than hard engineering. A combined approach using both hard and soft engineering is now recommended by hydrologists and the Office of Public Works (OPW) in Ireland.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo6-eq-4",
        source: "LC Geography — Sample 2022",
        parts: [
          {
            label: "Q4.",
            question: "Describe and explain the factors governing the operation of one mass movement process.",
            marks: 30,
            model: "Mass Movement: Mass movement is the downslope movement of rock, soil or debris under the direct influence of gravity — no water or ice is needed as a transport medium. Landslides are a form of rapid mass movement in which large volumes of material slide suddenly downslope along a failure plane. The trigger for a landslide can be natural — such as heavy prolonged rainfall or an earthquake — or human-induced, such as deforestation, construction or the vibration of heavy machinery. Factors Governing Landslides: Slope angle is a fundamental factor — steeper slopes increase the gravitational stress on slope material, making failure more likely above a critical angle. Water saturation is a key trigger — heavy rainfall adds significant weight to slope material and reduces friction between particles through pore water pressure. Saturated material loses its internal cohesion and shear strength — the slope material fails and flows downslope. Rock and soil type is critical — weak, impermeable rock such as clay becomes highly unstable when saturated with water. An impermeable layer of rock or clay beneath saturated soil acts as a slip plane — the overlying material slides across it during a failure event. Vegetation removal is highly significant — tree roots bind soil particles together and absorb water; deforestation removes this anchorage and greatly increases landslide risk. Human Factors: Road and building construction on steep slopes undercuts the natural toe support of the hillside — removing material from the base of the slope destabilises the slope above. Agricultural overgrazing strips the protective vegetation from slopes — increasing surface runoff and destabilising the slope material below. Connemara and West Mayo have experienced increased landslide frequency in recent decades, linked to overgrazing on blanket bog and peat soils. Consequences: Primary consequences include the direct burial of buildings, roads and infrastructure by displaced material. Secondary consequences include prolonged disruption to transport networks and contamination of water supplies. Recovery is costly and slow — landslide-prone areas require long-term engineering stabilisation and land management reform.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── geo7: Concept of a Region / Regional Geography ────────────────────────
  (function () {
    var c = ch("geo7");
    // 7.1 — Defining a Climatic Region
    c.learningOutcomes[0].notes = [
      {
        h: "Defining a Climatic Region",
        b: "A climatic region is defined by average weather conditions recorded over a long period of time. Ireland has a cool temperate oceanic climate — shaped primarily by the Atlantic Ocean and its proximity to it."
      },
      {
        h: "Ireland's Climate — Main Influences",
        b: "The Atlantic Ocean regulates temperature — preventing the extremes of heat and cold experienced at similar latitudes inland. The North Atlantic Drift carries warm water from the Gulf of Mexico — makes Irish winters milder than those of continental Europe. Prevailing winds come from the southwest — blow over the warm Atlantic, carrying heat and moisture; Ireland's damp climate results from this."
      },
      {
        h: "Variation Within Ireland and France",
        b: "The west of Ireland receives significantly more precipitation than the east — Atlantic moisture released as relief rain when air rises over western mountains. Ireland sits on a polar front — frontal depressions bring heavy rainfall nationally. East coast: drier, sunnier — Dublin averages ~700 mm rainfall per year vs. 1,200+ mm in Connacht. Paris Basin: two sub-climatic regions — cool temperate oceanic (west) and cool temperate continental (east). Continental areas have colder winters, warmer summers and convectional rainfall — ideal for wheat and maize."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is a region?",
        definition: "Any area with distinctive characteristics that distinguish it from surrounding areas; defined by borders and studied to identify patterns of change over time.",
        section: "7.1"
      },
      {
        term: "What is climate?",
        definition: "Average weather conditions (temperature, humidity, pressure, wind, precipitation) over an area measured over 30+ years.",
        section: "7.2"
      },
      {
        term: "What is a cool temperate oceanic climate?",
        definition: "Ireland's climate type; characterised by mild winters, cool summers and moderate year-round rainfall; influenced by the Atlantic Ocean and North Atlantic Drift.",
        section: "7.2"
      },
      {
        term: "What is the North Atlantic Drift?",
        definition: "Warm ocean current flowing from the equator towards Ireland; moderates Ireland's temperature so it doesn't experience continental extremes.",
        section: "7.2"
      },
      {
        term: "What is the Polar Front?",
        definition: "Zone of transition between warm and cold air masses that influences Ireland's weather patterns and precipitation.",
        section: "7.2"
      },
      {
        term: "What are the seven global climates?",
        definition: "Major global climate types: Polar, Temperate, Continental, Arid, Tropical, Mediterranean and Mountain.",
        section: "7.2"
      },
      {
        term: "What is a core region?",
        definition: "Central, well-connected region with high population density, developed infrastructure and concentrated economic power; typically holds high political capital.",
        section: "7.4"
      },
      {
        term: "What is a peripheral region?",
        definition: "Region on the outskirts of a country or continent with poor infrastructure, low population density and limited economic development.",
        section: "7.4"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine how climate can be used to define regions, with reference to examples.",
        model: "Defining a Climatic Region: A climatic region is defined by average weather conditions — temperature, precipitation, wind and humidity — recorded over a long period of time, typically 30 years. Ireland has a cool temperate oceanic climate, shaped primarily by its proximity to the Atlantic Ocean and its position on the western fringe of Europe. Ireland's Climate Influences: The Atlantic Ocean acts as a temperature regulator — its thermal mass prevents the extremes of heat and cold experienced at similar latitudes further inland. The North Atlantic Drift, a warm ocean current originating in the Gulf of Mexico, flows along Ireland's western coast — making Irish winters significantly milder than those of continental Europe at the same latitude. Prevailing winds blow from the southwest over the warm Atlantic Ocean — carrying heat and moisture and bringing Ireland its characteristically damp, mild climate. Ireland's position on the polar front means it is regularly crossed by frontal depressions — these low-pressure systems bring heavy, prolonged rainfall particularly in autumn and winter. Variation Within Ireland: The west of Ireland receives significantly more precipitation than the east — Atlantic moisture is released as relief rainfall when air rises over the western mountain ranges. Connacht and parts of Munster receive over 1,200 mm of rainfall annually, while Dublin on the east coast averages approximately 700 mm per year. The east coast is drier and sunnier than the west — Dublin experiences more settled, continental-influenced weather due to the rain shadow effect of the western mountains. Comparison — France (Paris Basin): The Paris Basin also sits within the cool temperate oceanic climate zone but experiences greater continentality due to its distance from the Atlantic. The western Paris Basin has a cool temperate oceanic climate — mild, wet and windy — while the eastern Paris Basin has a cool temperate continental climate. Continental areas experience colder winters, warmer summers and convectional rainfall in summer — conditions ideal for growing wheat and maize. The transition between the oceanic west and continental east of France creates a distinct intermediate climatic zone in the middle of the Paris Basin. France's climatic variation means two very different agricultural systems can operate within the same country — pastoral farming in the west, arable farming in the east."
      }
    ];
    // 7.2 — Defining a Language/Cultural Region
    c.learningOutcomes[1].notes = [
      {
        h: "Defining a Language Region",
        b: "A language region is an area defined by its dominant spoken or written language — can exist within or across national borders. Language regions reflect historical, political and cultural forces rather than physical geography."
      },
      {
        h: "The Gaeltacht — Ireland",
        b: "Gaeltacht regions are officially recognised areas where Irish is the primary spoken language — first designated by the Irish Free State in the 1920s. The language declined due to British plantation policies and the Great Famine — a million died, a million emigrated; most Irish speakers were in the west. English is more economically valuable internationally — Irish continues to decline despite government revival policies. The government funds TG4, Irish-medium schools (Gaelscoileanna) and Údarás na Gaeltachta to support language regions."
      },
      {
        h: "Belgium — Language Regions",
        b: "Belgium is divided into four language communities: Flanders (Dutch), Wallonia (French), Ostbelgien (German) and Brussels (bilingual). Dutch, French and German are co-equal official languages written into law — creating distinct cultural and administrative regions. Historical economic divide: Wallonia was wealthier (coal-based industry) but declined in the 20th century as world shifted to oil — Flanders became wealthier; economic division deepens cultural tension. Belgium became a federal state to reduce tensions — national parliament handles foreign policy; regional parliaments handle education, policing and local affairs."
      }
    ];
    c.learningOutcomes[1].keyTerms = [
      {
        term: "What is a cultural region?",
        definition: "Area inhabited by people sharing one or more cultural traits such as language or religion; borders are difficult to define as cultures naturally overlap.",
        section: "7.6"
      },
      {
        term: "What is the Gaeltacht?",
        definition: "Region in Ireland where Irish is the predominant spoken language; seven areas in Cork, Donegal, Galway, Kerry, Meath, Mayo and Waterford; 63,664 daily Irish speakers.",
        section: "7.6"
      },
      {
        term: "What is Gaelic Revival?",
        definition: "Irish government policy from the 1920s to promote the Irish language and restore Gaeltacht areas; Gaeltacht regions have declined significantly over the past 100 years.",
        section: "7.6"
      },
      {
        term: "What are Belgium's language communities?",
        definition: "Belgium has four language communities: Flemish (north), French/Walloon (south), German (east) and bilingual Brussels; language regions have legal geographical boundaries.",
        section: "7.6"
      },
      {
        term: "What is an administrative region?",
        definition: "Geographical area defined by governmental borders responsible for specific governmental or political functions.",
        section: "7.5"
      },
      {
        term: "What is a regional assembly?",
        definition: "Tier of Irish government (3 assemblies: Eastern & Midland, Northern & Western, Southern) co-ordinating strategic planning and sustainable regional development.",
        section: "7.5"
      },
      {
        term: "What is the Northern Ireland religious divide?",
        definition: "Region where Protestant (Unionist) and Catholic (Nationalist) communities have experienced conflict since English plantations 400 years ago; shaped by the Government of Ireland Act (1920) and the Good Friday Agreement.",
        section: "7.7"
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine how language can be used to define cultural regions.",
        model: "Defining a Language Region: A language region is an area defined by its dominant spoken or written language — it can exist within a single country or span across national borders. Language regions are shaped by historical, political and cultural forces rather than by physical geography — they change over time as societies change. The Gaeltacht — Ireland: Gaeltacht regions are officially recognised areas of Ireland where Irish Gaelic is the primary spoken language of the community. They were first designated by the Irish Free State government in the 1920s, primarily located along the western seaboard. The Irish language declined dramatically due to British plantation policies in the 16th and 17th centuries — English was imposed as the language of administration, law and commerce. The Great Famine (1845–1852) devastated the Irish-speaking population of the west — approximately one million people died and another million emigrated, most of whom were Irish speakers. English has greater economic value in international trade and employment than Irish — this economic reality continues to drive language shift away from Irish. The Irish government funds TG4 (Irish-language television), Irish-medium schools (Gaelscoileanna) and Údarás na Gaeltachta (the Gaeltacht development agency) to support the survival of the language. Belgium — Language Regions: Belgium is divided into four official language communities: Flanders in the north (Dutch-speaking), Wallonia in the south (French-speaking), Ostbelgien in the east (German-speaking) and Brussels-Capital (officially bilingual). Dutch, French and German are co-equal official languages enshrined in law — creating distinct cultural, educational and administrative regions with their own governments. Historically, Wallonia was the wealthier region — its coal-based heavy industry drove the Belgian economy through the 19th and early 20th centuries. In the mid-20th century, world energy shifted from coal to oil — Wallonia's industry declined sharply while Flanders, with newer light industry and service sectors, became the wealthier region. This economic reversal deepened cultural and political tensions between the Dutch-speaking Flemish and the French-speaking Walloons. Belgium restructured as a federal state to manage these tensions — the national parliament handles foreign policy and defence, while regional parliaments handle education, policing and local economic affairs. The Belgian model demonstrates how language differences, reinforced by economic inequality, can produce complex, legally defined regional structures within a small country."
      }
    ];
    // 7.3 — Defining a Geomorphological Region
    c.learningOutcomes[2].notes = [
      {
        h: "Defining a Geomorphological Region",
        b: "A geomorphological region is defined by shared physical landform characteristics — rock type, relief, soils, and drainage pattern. Tectonic history and erosion/deposition processes determine these features over millions of years."
      },
      {
        h: "Paris Basin — Geomorphology",
        b: "The Paris Basin is a large synclinal structure — layers of sedimentary rock (limestone, chalk) formed when the area was submerged under a shallow sea. The basin shape results from compaction and slight folding — rock layers dip toward the centre from all sides. Around the basin edges, denudation exposed tilted sedimentary rocks — forming steep-faced escarpments (e.g. the Champagne chalk escarpments). The gently sloping terrain of the basin interior defines it as an arable farming region — mechanisation possible on flat lowlands."
      },
      {
        h: "West of Ireland — Geomorphology",
        b: "The western seaboard is characterised by mountainous terrain — upland areas formed during the Caledonian and Armorican orogenies. The eastern part of the region is flatter and lower-lying — divided from the west by the uplands. Glacial processes removed upper soil layers and deposited peat, gley and podzol soils — defining a region of poor drainage and low agricultural productivity. The coastline is highly indented with bays, headlands and drumlins — a geomorphological fingerprint of glacial deposition and Atlantic wave erosion."
      }
    ];
    c.learningOutcomes[2].keyTerms = [
      {
        term: "What is geomorphology?",
        definition: "Study of distinctive surface landforms and the physical, chemical and biological processes that created them.",
        section: "7.3"
      },
      {
        term: "What is a geomorphological region?",
        definition: "Region characterised by unique relief, drainage patterns, rock types and ecosystems that make it distinctively different from surrounding areas.",
        section: "7.3"
      },
      {
        term: "What is the Burren (as a region)?",
        definition: "Karst geomorphological region in County Clare awarded UNESCO Global Geopark status for its unique limestone landscape including pavements, dolines and cave systems.",
        section: "7.3"
      },
      {
        term: "What is industrial decline?",
        definition: "Reduction in industrial activity in a region, often affecting heavy industries (coal, steel); caused by exhaustion of raw materials, changing demand or cheaper competition.",
        section: "7.4"
      },
      {
        term: "What is primary economic activity?",
        definition: "Activity involving extraction of raw materials from the Earth (farming, fishing, mining).",
        section: "7.4"
      },
      {
        term: "What is secondary economic activity?",
        definition: "Activity involving processing raw materials into finished goods (manufacturing, construction).",
        section: "7.4"
      },
      {
        term: "What is tertiary economic activity?",
        definition: "Activity providing services in an economy (education, healthcare, retail, tourism, transport).",
        section: "7.4"
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine how geomorphology can be used to define regions.",
        model: "Defining a Geomorphological Region: A geomorphological region is defined by shared physical landform characteristics — including rock type, relief, soils and drainage pattern. Tectonic history and the processes of erosion and deposition over millions of years determine these physical characteristics. Regions with similar geomorphological characteristics tend to share similar land uses and economic activities. Paris Basin: The Paris Basin is a large synclinal geological structure — layers of sedimentary rock including limestone and chalk were deposited when the area was submerged under a shallow sea during the Cretaceous period. The basin shape results from compaction and slight downward folding of the rock layers — they dip from the outer edges toward the centre of the basin like a shallow bowl. Around the basin edges, long-term denudation has exposed tilted sedimentary rocks — forming steep-faced escarpments, particularly the Champagne chalk escarpments to the east of Paris. The gently sloping, fertile terrain of the basin interior defines it as a major arable farming region — large-scale mechanisation is possible on the extensive flat lowlands. The Seine and its tributaries have carved out valleys through the basin's sedimentary layers — providing flat floodplain land used for settlement and agriculture. West of Ireland: The western seaboard of Ireland is characterised by mountainous terrain — upland areas formed during the Caledonian and Armorican orogenies hundreds of millions of years ago. The eastern part of the western region is flatter and lower-lying, separated from the mountainous west by the uplands — this internal variation defines distinct sub-regions within the west. Glacial processes during the last ice age removed upper soil layers across most of the west, depositing peat, gley and podzol soils — defining a region with characteristically poor drainage and low agricultural productivity. The coastline of the west is highly indented with bays, headlands, sea stacks and offshore islands — a geomorphological fingerprint of glacial deposition, Atlantic wave erosion and coastal drowning. Drumlins — elongated hills of glacial till — are clustered in parts of the west, particularly around Clew Bay in Co. Mayo, creating a distinctive drumlin landscape. This combination of mountainous relief, poor soils, indented coastline and glacial landforms defines the West of Ireland as a geomorphological region fundamentally different from any other part of the country."
      }
    ];
    // 7.4 — Causes and Impacts of Industrial Decline
    c.learningOutcomes[3].notes = [
      {
        h: "Causes of Decline — Belfast",
        b: "Belfast developed during the Industrial Revolution — linen and shipbuilding industries (e.g. Harland and Wolff) dominated the economy. Post-WW1: unemployment rose to 23% — global demand for ships fell, hitting Belfast's core industry. Post-WW2 decline compounded by The Troubles (1960s–1990s) — political instability deterred foreign investment and destroyed consumer confidence. Globalisation shifted manufacturing to lower-cost economies — Belfast's traditional industries could not compete."
      },
      {
        h: "Causes of Decline — West of Ireland",
        b: "The West is a peripheral region with poor transport infrastructure — mountainous terrain made road and rail construction expensive. The small labour force and low population density made it unattractive for foreign direct investment (FDI). Brain drain: educated young people leave for the GDA or abroad — reducing the skilled workforce. Legacy industries (food processing, timber) dominate — limited high-value manufacturing due to lack of raw materials."
      },
      {
        h: "Impacts of Industrial Decline",
        b: "Unemployment rises — increased dependence on social welfare; poverty and social deprivation in affected areas. Outward migration — working-age population leaves; ageing population remains; declining tax base reduces public services investment. Urban dereliction — abandoned factory sites, vacant town centres, deteriorating housing. Recovery possible: Belfast's Titanic Quarter redeveloped as a tourism and education hub; West supported by EU funds and IDA initiatives attracting companies such as Boston Scientific and Pfizer."
      }
    ];
    c.learningOutcomes[3].keyTerms = [
      {
        term: "What is the Mezzogiorno?",
        definition: "Peripheral socio-economic region in southern Italy characterised by mountainous terrain, poor infrastructure, high unemployment (double the northern rate) and slow economic development.",
        section: "7.4"
      },
      {
        term: "What is the Cassa scheme?",
        definition: "Italian government intervention from the 1950s to stimulate economic growth in the Mezzogiorno by redistributing land, building infrastructure and attracting FDI; ended 1984.",
        section: "7.4"
      },
      {
        term: "What is Vanoni Plan?",
        definition: "Part of the Cassa Scheme; aimed to attract multinational corporations to the Mezzogiorno by establishing industrial growth poles.",
        section: "7.4"
      },
      {
        term: "What is brain drain?",
        definition: "Loss of educated, skilled workers from a region through outward migration in search of better education and employment opportunities; affects both the Mezzogiorno and the west of Ireland.",
        section: "7.4"
      },
      {
        term: "What is foreign direct investment (FDI)?",
        definition: "Investment by foreign companies in a region's economy; attracted by low corporation tax, skilled workforce and government incentives.",
        section: "7.4"
      },
      {
        term: "What is the ERDF (European Regional Development Funds)?",
        definition: "EU funds that replaced the Cassa Scheme in 1984; support peripheral regions in developing infrastructure and economic activity.",
        section: "7.4"
      },
      {
        term: "What is the 2030 plan for southern Italy?",
        definition: "Italian government initiative announced in 2020 pledging €33 billion to develop transport and economic infrastructure in the Mezzogiorno.",
        section: "7.4"
      },
      {
        term: "What is the Sirocco wind?",
        definition: "Hot, dry prevailing wind in the Mezzogiorno blowing northward from the Sahara Desert; reduces summer rainfall and makes agriculture challenging.",
        section: "7.4"
      }
    ];
    c.learningOutcomes[3].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine the causes and impacts of industrial decline with reference to any region that you have studied.",
        model: "Causes — Belfast: Belfast developed as an industrial city during the Industrial Revolution — the linen textile industry and shipbuilding (centred on Harland and Wolff) dominated the city's economy. After World War One, global demand for ships fell sharply — Belfast's shipbuilding industry contracted and unemployment rose to approximately 23% of the workforce. The Troubles (1960s–1990s) created prolonged political instability and civil unrest in Belfast — this severely deterred foreign direct investment and destroyed consumer confidence in the city. Globalisation shifted manufacturing to lower-cost economies in Asia and Eastern Europe — Belfast's traditional industries could no longer compete on price. Causes — West of Ireland: The West of Ireland is a peripheral region with historically poor transport infrastructure — mountainous terrain made road and rail construction very expensive, limiting connectivity. The small resident labour force and low population density made the West unattractive for foreign direct investment (FDI) compared to the Greater Dublin Area. Brain drain is a persistent problem — educated young people leave the West for the Greater Dublin Area or abroad, reducing the local skilled workforce available to employers. Legacy industries such as food processing and timber dominate in the West — there is limited high-value manufacturing due to the lack of raw materials and poor connectivity. Impacts of Industrial Decline: Unemployment rises sharply in areas of industrial decline — this increases dependence on social welfare and creates widespread poverty and social deprivation. Outward migration of working-age people follows — the remaining population ages, the tax base shrinks and investment in public services declines. Urban dereliction becomes a visible symptom — abandoned factory sites, vacant town centres and deteriorating housing reduce quality of life and further deter new investment. Recovery Strategies: Belfast's Titanic Quarter has been successfully redeveloped as a major tourism, education and creative industries hub — the Titanic Belfast museum alone attracts over 800,000 visitors per year. The West of Ireland has been supported by EU Structural Funds and the IDA — attracting significant companies such as Boston Scientific and Pfizer to the region. These recovery efforts demonstrate that decline is not inevitable — targeted investment and rebranding can transform former industrial regions into competitive modern economies."
      }
    ];
    c.examQuestions = [
      {
        id: "geo7-eq-1",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q1.",
            question: "Examine how climate can be used to define regions, with reference to examples.",
            marks: 30,
            model: "Defining a Climatic Region: A climatic region is defined by average weather conditions — temperature, precipitation, wind and humidity — recorded over a long period of time, typically 30 years. Ireland has a cool temperate oceanic climate, shaped primarily by its proximity to the Atlantic Ocean and its position on the western fringe of Europe. Ireland's Climate Influences: The Atlantic Ocean acts as a temperature regulator — its thermal mass prevents the extremes of heat and cold experienced at similar latitudes further inland. The North Atlantic Drift, a warm ocean current originating in the Gulf of Mexico, flows along Ireland's western coast — making Irish winters significantly milder than those of continental Europe at the same latitude. Prevailing winds blow from the southwest over the warm Atlantic Ocean — carrying heat and moisture and bringing Ireland its characteristically damp, mild climate. Ireland's position on the polar front means it is regularly crossed by frontal depressions — these low-pressure systems bring heavy, prolonged rainfall particularly in autumn and winter. Variation Within Ireland: The west of Ireland receives significantly more precipitation than the east — Atlantic moisture is released as relief rainfall when air rises over the western mountain ranges. Connacht and parts of Munster receive over 1,200 mm of rainfall annually, while Dublin on the east coast averages approximately 700 mm per year. The east coast is drier and sunnier than the west — Dublin experiences more settled, continental-influenced weather due to the rain shadow effect of the western mountains. Comparison — France (Paris Basin): The Paris Basin also sits within the cool temperate oceanic climate zone but experiences greater continentality due to its distance from the Atlantic. The western Paris Basin has a cool temperate oceanic climate — mild, wet and windy — while the eastern Paris Basin has a cool temperate continental climate. Continental areas experience colder winters, warmer summers and convectional rainfall in summer — conditions ideal for growing wheat and maize. The transition between the oceanic west and continental east of France creates a distinct intermediate climatic zone in the middle of the Paris Basin. France's climatic variation means two very different agricultural systems can operate within the same country — pastoral farming in the west, arable farming in the east.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo7-eq-2",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q2.",
            question: "Examine how language can be used to define cultural regions.",
            marks: 30,
            model: "Defining a Language Region: A language region is an area defined by its dominant spoken or written language — it can exist within a single country or span across national borders. Language regions are shaped by historical, political and cultural forces rather than by physical geography — they change over time as societies change. The Gaeltacht — Ireland: Gaeltacht regions are officially recognised areas of Ireland where Irish Gaelic is the primary spoken language of the community. They were first designated by the Irish Free State government in the 1920s, primarily located along the western seaboard. The Irish language declined dramatically due to British plantation policies in the 16th and 17th centuries — English was imposed as the language of administration, law and commerce. The Great Famine (1845–1852) devastated the Irish-speaking population of the west — approximately one million people died and another million emigrated, most of whom were Irish speakers. English has greater economic value in international trade and employment than Irish — this economic reality continues to drive language shift away from Irish. The Irish government funds TG4 (Irish-language television), Irish-medium schools (Gaelscoileanna) and Údarás na Gaeltachta (the Gaeltacht development agency) to support the survival of the language. Belgium — Language Regions: Belgium is divided into four official language communities: Flanders in the north (Dutch-speaking), Wallonia in the south (French-speaking), Ostbelgien in the east (German-speaking) and Brussels-Capital (officially bilingual). Dutch, French and German are co-equal official languages enshrined in law — creating distinct cultural, educational and administrative regions with their own governments. Historically, Wallonia was the wealthier region — its coal-based heavy industry drove the Belgian economy through the 19th and early 20th centuries. In the mid-20th century, world energy shifted from coal to oil — Wallonia's industry declined sharply while Flanders, with newer light industry and service sectors, became the wealthier region. This economic reversal deepened cultural and political tensions between the Dutch-speaking Flemish and the French-speaking Walloons. Belgium restructured as a federal state to manage these tensions — the national parliament handles foreign policy and defence, while regional parliaments handle education, policing and local economic affairs. The Belgian model demonstrates how language differences, reinforced by economic inequality, can produce complex, legally defined regional structures within a small country.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo7-eq-3",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q3.",
            question: "Examine how geomorphology can be used to define regions.",
            marks: 30,
            model: "Defining a Geomorphological Region: A geomorphological region is defined by shared physical landform characteristics — including rock type, relief, soils and drainage pattern. Tectonic history and the processes of erosion and deposition over millions of years determine these physical characteristics. Regions with similar geomorphological characteristics tend to share similar land uses and economic activities. Paris Basin: The Paris Basin is a large synclinal geological structure — layers of sedimentary rock including limestone and chalk were deposited when the area was submerged under a shallow sea during the Cretaceous period. The basin shape results from compaction and slight downward folding of the rock layers — they dip from the outer edges toward the centre of the basin like a shallow bowl. Around the basin edges, long-term denudation has exposed tilted sedimentary rocks — forming steep-faced escarpments, particularly the Champagne chalk escarpments to the east of Paris. The gently sloping, fertile terrain of the basin interior defines it as a major arable farming region — large-scale mechanisation is possible on the extensive flat lowlands. The Seine and its tributaries have carved out valleys through the basin's sedimentary layers — providing flat floodplain land used for settlement and agriculture. West of Ireland: The western seaboard of Ireland is characterised by mountainous terrain — upland areas formed during the Caledonian and Armorican orogenies hundreds of millions of years ago. The eastern part of the western region is flatter and lower-lying, separated from the mountainous west by the uplands — this internal variation defines distinct sub-regions within the west. Glacial processes during the last ice age removed upper soil layers across most of the west, depositing peat, gley and podzol soils — defining a region with characteristically poor drainage and low agricultural productivity. The coastline of the west is highly indented with bays, headlands, sea stacks and offshore islands — a geomorphological fingerprint of glacial deposition, Atlantic wave erosion and coastal drowning. Drumlins — elongated hills of glacial till — are clustered in parts of the west, particularly around Clew Bay in Co. Mayo, creating a distinctive drumlin landscape. This combination of mountainous relief, poor soils, indented coastline and glacial landforms defines the West of Ireland as a geomorphological region fundamentally different from any other part of the country.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo7-eq-4",
        source: "LC Geography — Sample 2015",
        parts: [
          {
            label: "Q4.",
            question: "Examine the causes and impacts of industrial decline with reference to any region that you have studied.",
            marks: 30,
            model: "Causes — Belfast: Belfast developed as an industrial city during the Industrial Revolution — the linen textile industry and shipbuilding (centred on Harland and Wolff) dominated the city's economy. After World War One, global demand for ships fell sharply — Belfast's shipbuilding industry contracted and unemployment rose to approximately 23% of the workforce. The Troubles (1960s–1990s) created prolonged political instability and civil unrest in Belfast — this severely deterred foreign direct investment and destroyed consumer confidence in the city. Globalisation shifted manufacturing to lower-cost economies in Asia and Eastern Europe — Belfast's traditional industries could no longer compete on price. Causes — West of Ireland: The West of Ireland is a peripheral region with historically poor transport infrastructure — mountainous terrain made road and rail construction very expensive, limiting connectivity. The small resident labour force and low population density made the West unattractive for foreign direct investment (FDI) compared to the Greater Dublin Area. Brain drain is a persistent problem — educated young people leave the West for the Greater Dublin Area or abroad, reducing the local skilled workforce available to employers. Legacy industries such as food processing and timber dominate in the West — there is limited high-value manufacturing due to the lack of raw materials and poor connectivity. Impacts of Industrial Decline: Unemployment rises sharply in areas of industrial decline — this increases dependence on social welfare and creates widespread poverty and social deprivation. Outward migration of working-age people follows — the remaining population ages, the tax base shrinks and investment in public services declines. Urban dereliction becomes a visible symptom — abandoned factory sites, vacant town centres and deteriorating housing reduce quality of life and further deter new investment. Recovery Strategies: Belfast's Titanic Quarter has been successfully redeveloped as a major tourism, education and creative industries hub — the Titanic Belfast museum alone attracts over 800,000 visitors per year. The West of Ireland has been supported by EU Structural Funds and the IDA — attracting significant companies such as Boston Scientific and Pfizer to the region. These recovery efforts demonstrate that decline is not inevitable — targeted investment and rebranding can transform former industrial regions into competitive modern economies.",
            diagram: ""
          }
        ]
      }
    ];
  })();

  // ── geo8: Economic Activity & Social-Economic Regions ─────────────────────
  (function () {
    var c = ch("geo8");
    // 8.1 — Tourism in Irish Regions — GDA and West of Ireland
    c.learningOutcomes[0].notes = [
      {
        h: "Tourist Attractions — GDA",
        b: "GDA: 11 million visitors per year; earns ~€6 billion annually — Dublin Castle, Guinness Storehouse, Trinity College attract year-round visitors (not weather-dependent). Benefits from events tourism — concerts, sports, conferences; also strong retail tourism (~€1 billion per year). 250,000 people in the GDA are employed in tourism-related industries."
      },
      {
        h: "Tourist Attractions — West of Ireland",
        b: "Wild Atlantic Way (founded 2014) is one of the world's longest defined coastal routes — attracted almost €2 billion in tourist spending in 2019. The Gaeltacht attracts 30,000 Irish language students per year — a unique cultural tourism asset."
      },
      {
        h: "Transport Infrastructure — GDA and West",
        b: "GDA: Dublin Airport is the primary international gateway — brings in the vast majority of overseas tourists; Luas and DART expanded to serve tourism. The M50 was upgraded — NDP (2006) drove major infrastructure development in the GDA. West of Ireland: transport is underdeveloped — mainly car-dependent; limited railway; mountainous terrain makes road construction expensive. Knock Airport has no freight services; only one motorway (M6). Despite this, Galway City is the most visited part of the West — Airbnb market has expanded significantly."
      }
    ];
    c.learningOutcomes[0].keyTerms = [
      {
        term: "What is the GDA (Greater Dublin Area)?",
        definition: "Core socio-economic region in eastern Ireland comprising counties Dublin, Meath, Kildare and Wicklow; contributes ~50% of Ireland's GDP and houses 40.5% of the population.",
        section: "8.1"
      },
      {
        term: "What is the western region?",
        definition: "Peripheral socio-economic region comprising counties Galway, Mayo and Roscommon; occupies 21.4% of Ireland's land area but only 9.5% of the population.",
        section: "8.1"
      },
      {
        term: "What is Wild Atlantic Way?",
        definition: "Tourism initiative launched in 2014 by Fáilte Ireland highlighting the scenic coastal route of the west of Ireland; boosted seasonal tourism in the Western region.",
        section: "8.1"
      },
      {
        term: "What is year-round tourism (GDA)?",
        definition: "GDA tourism is not reliant on seasonal patterns; 6.6 million overseas tourists in 2019 driven by historical, cultural, retail and events-based attractions.",
        section: "8.1"
      },
      {
        term: "What is seasonal tourism (west)?",
        definition: "West of Ireland tourism is heavily dependent on summer visitors; lack of year-round demand limits economic returns compared with the GDA.",
        section: "8.1"
      },
      {
        term: "What is the Celtic Tiger?",
        definition: "Period of rapid Irish economic growth in the 1990s–early 2000s; drove GDA population growth, urban sprawl and commuter town development.",
        section: "8.1"
      },
      {
        term: "What is urban sprawl?",
        definition: "Expansion of urban settlement into surrounding rural land, driven by housing demand; characteristic of the GDA during the Celtic Tiger period.",
        section: "8.1"
      }
    ];
    c.learningOutcomes[0].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine two factors that have influenced the development of tourism in an Irish region.",
        model: "Factor 1 — Tourist Attractions: The Greater Dublin Area (GDA) attracts approximately 11 million visitors per year and earns approximately €6 billion annually from tourism. Major cultural and heritage attractions — Dublin Castle, the Guinness Storehouse and Trinity College — attract large numbers of year-round visitors regardless of weather conditions. Events tourism is a major strength of the GDA — concerts, international sports events and major conferences bring significant visitor numbers and spend. Retail tourism generates approximately €1 billion per year for the GDA — international visitors make Dublin a major shopping destination. Approximately 250,000 people in the GDA are directly employed in tourism-related industries, making it a critical part of the regional economy. The West of Ireland's primary tourism asset is the Wild Atlantic Way — founded in 2014, it is one of the world's longest defined coastal touring routes at approximately 2,500 km. The Wild Atlantic Way generated approximately €2 billion in tourist spending in 2019 alone, before the disruption of the pandemic. The Gaeltacht attracts approximately 30,000 Irish language students per year — a unique form of cultural and educational tourism that benefits remote western communities. Factor 2 — Transport Infrastructure: Dublin Airport is the primary international gateway for Ireland, connecting the country to over 180 destinations worldwide and delivering the vast majority of overseas tourists. The Luas light rail network and DART suburban rail have been expanded — improving access from the airport and port to Dublin's major tourist attractions. The M50 orbital motorway was upgraded — NDP investment (2006 onwards) drove major transport infrastructure development in the GDA. The West of Ireland's transport infrastructure is significantly underdeveloped by comparison — the region is mainly car-dependent with a limited rail network. Knock Airport provides only limited connectivity with no freight services, and the West has only one motorway (M6) connecting it to Dublin. Galway City is the most visited destination in the West despite infrastructure deficits — the growth of Airbnb and short-term rental accommodation has expanded tourism capacity significantly. Improved road and air connectivity would be critical to further developing the West's tourism potential in the coming decades."
      }
    ];
    // 8.2 — Core vs Peripheral Regions — GDA and West of Ireland
    c.learningOutcomes[1].notes = [
      {
        h: "Primary Activity — GDA (Core) vs West (Peripheral)",
        b: "GDA: fertile brown earth soils, gently rolling lowlands, 700 mm annual rainfall — ideal for commercial arable farming. Farms large, mechanised, commercially profitable. Co. Kildare's horse breeding industry globally competitive — well-drained limestone soils. West: peat, gley and podzol soils — poor drainage, prone to waterlogging. Mountainous terrain prevents mechanisation — small, semi-subsistence farms; ~50% rely on income outside farming. Average farmer income in the West is €20,000 less than in the GDA — heavily dependent on EU farm grants."
      },
      {
        h: "Secondary Activity — Core vs Peripheral",
        b: "GDA: attracts vast majority of Ireland's FDI — 19 of world's 20 largest pharmaceutical companies have a presence in Ireland, most based in the GDA; Ireland exports €100+ billion in pharma annually. GDA has highly educated workforce (multiple universities), well-developed transport (M50, Dublin Airport, port) and population of 2.1 million — attractive to multinationals. West: industrial job growth 20% per year in Galway — above national average — but from a low base. West struggles: poor transport (one motorway), small labour force, brain drain of graduates."
      },
      {
        h: "Tertiary Activity — Core vs Peripheral",
        b: "GDA: 11 million tourists/year, €6 billion revenue, 250,000 employed in tourism — well-developed hospitality, retail and financial services. West: tourism growing (Wild Atlantic Way) but employment in services limited by low population density and poor infrastructure. Core regions benefit from agglomeration — services cluster together, reducing costs and attracting further business; peripheral regions lack this self-reinforcing economic dynamic."
      }
    ];
    c.learningOutcomes[1].keyTerms = [
      {
        term: "Why is the GDA a core region?",
        definition: "GDA has favourable physical conditions (fertile soils, mild climate, flat terrain), excellent infrastructure, large skilled labour force and high economic output; contributes ~50% of Ireland's GDP.",
        section: "8.2"
      },
      {
        term: "Why is the West a peripheral region?",
        definition: "Western region has mountainous terrain, infertile soils, high rainfall, poor infrastructure and small labour force; low population density and limited FDI.",
        section: "8.2"
      },
      {
        term: "What is IDA Ireland?",
        definition: "Industrial Development Agency; government body that promotes and supports foreign direct investment in Ireland; key driver of pharmaceutical and tech industries in both regions.",
        section: "8.2"
      },
      {
        term: "What is corporation tax?",
        definition: "Ireland's 12.5% tax rate on company profits; key incentive attracting multinational corporations (e.g. pharmaceuticals, tech) to locate in Ireland.",
        section: "8.2"
      },
      {
        term: "What is the Common Agricultural Policy (CAP)?",
        definition: "EU policy providing farm subsidies; essential to western Irish farmers who cannot compete profitably without support; Brexit has threatened CAP benefits.",
        section: "8.2"
      },
      {
        term: "What is rural depopulation?",
        definition: "Decline in rural population due to outward migration; particularly affecting the west of Ireland; driven by lack of employment and educational opportunities.",
        section: "8.2"
      },
      {
        term: "What are commuter towns?",
        definition: "Towns beyond a city whose residents travel daily to work in the city; a result of urban sprawl in the GDA during the Celtic Tiger period.",
        section: "8.2"
      }
    ];
    c.learningOutcomes[1].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Economic activity in core regions differs from those in peripheral regions. Examine this statement with reference to examples.",
        model: "Primary Activity — GDA (Core): The GDA has fertile brown earth soils, gently rolling lowlands and approximately 700 mm of annual rainfall — conditions ideal for commercial arable farming. GDA farms are large, highly mechanised and commercially profitable — using modern equipment to grow grain, potatoes, and horticulture products at scale. Co. Kildare's horse breeding industry is globally competitive — the region's well-drained limestone soils and flat terrain make it ideal for thoroughbred production and training. Primary Activity — West (Peripheral): The West has peat, gley and podzol soils with characteristically poor drainage, prone to waterlogging and flooding — unsuitable for most arable crops. Mountainous terrain prevents mechanisation on most western farms — small, often semi-subsistence farms persist where combine harvesters cannot operate. Approximately 50% of western farmers rely on income from outside farming to survive — EU farm grants are essential to the viability of farming in the region. The average farmer income in the West is approximately €20,000 per year less than in the GDA — reflecting the fundamental physical disadvantages of the western landscape. Secondary Activity — GDA (Core): The GDA attracts the vast majority of Ireland's foreign direct investment (FDI) — 19 of the world's 20 largest pharmaceutical companies have a presence in Ireland, most based in the GDA. Ireland exports over €100 billion in pharmaceutical products annually — the GDA is the primary driver of this globally significant export sector. The GDA offers multinationals a highly educated workforce, well-developed transport infrastructure (M50, Dublin Port, Dublin Airport) and a population of 2.1 million. Secondary Activity — West (Peripheral): Industrial job growth in Galway has been approximately 20% per year — above the national average — but this growth is from a very low starting base. The West struggles to attract investment due to poor transport (only one motorway), a small labour force and the brain drain of graduates to the GDA. Tertiary Activity: The GDA generates €6 billion annually from tourism, employs 250,000 in tourism-related work and hosts well-developed financial, retail and hospitality services. Tourism is growing in the West (particularly through the Wild Atlantic Way) but employment in services remains limited by low population density and poor infrastructure. Core regions benefit from agglomeration economies — services cluster together, reducing costs and attracting further business investment; peripheral regions lack this self-reinforcing economic dynamic."
      }
    ];
    // 8.3 — Agriculture in Contrasting Irish Regions
    c.learningOutcomes[2].notes = [
      {
        h: "Physical Factors — GDA and West",
        b: "GDA: gently rolling lowlands — ideal for mechanisation; fertile brown earth soils with low leaching risk — high calcium content supports grain, potato and horticulture. Cool temperate oceanic climate — 700 mm rainfall, mild winters, warm summers; good growing season. West: mountainous terrain — steep slopes prevent machinery; peat, gley and podzol soils — poor drainage, prone to waterlogging. Higher rainfall (1,200+ mm) — soils become saturated; leaching removes minerals, reducing fertility."
      },
      {
        h: "Socio-Economic Factors — GDA and West",
        b: "GDA: population of 2.1 million — largest internal market; average disposable income 17% above national average. Majority of GDA farms profitable; younger farmers adopting modern practices; larger farm sizes allow machinery investment. Excellent road, rail and port networks — produce reaches markets quickly. West: peripheral location — distant from major markets; low population density; Galway Harbour only port but poorly positioned for European trade. Average income €20,000 below GDA farmers; most rely on EU grants; labour unattractive to young people. Underdeveloped roads — one motorway (M6); mountainous terrain makes construction expensive."
      }
    ];
    c.learningOutcomes[2].keyTerms = [
      {
        term: "What is intensive agriculture (GDA)?",
        definition: "Large-scale, mechanised, commercialised farming on fertile brown-earth soils; highly profitable; farms in the GDA are on average 41.3% larger than western farms.",
        section: "8.3"
      },
      {
        term: "What is commercialised farming?",
        definition: "Farming where crops are grown for sale to return a profit using modern technology and machinery; dominant in the GDA.",
        section: "8.3"
      },
      {
        term: "What are brown-earth soils?",
        definition: "Fertile soils of the GDA formed under deciduous woodland on limestone bedrock; ideal for horticulture and arable farming; high calcium content.",
        section: "8.3"
      },
      {
        term: "What is leaching?",
        definition: "Process where rainfall washes nutrients and minerals downward through the soil profile; more pronounced in the west due to higher annual rainfall (1,200+ mm) compared to the GDA.",
        section: "8.3"
      },
      {
        term: "What is semi-subsistence farming (west)?",
        definition: "Small-scale farming in the west of Ireland where most output is for household consumption; relies on off-farm income and EU CAP subsidies to survive.",
        section: "8.3"
      },
      {
        term: "What are peat soils?",
        definition: "Waterlogged, infertile soils covering most of Connemara and west Mayo; formed from accumulating organic matter; unsuitable for arable farming.",
        section: "8.3"
      },
      {
        term: "What are gley soils?",
        definition: "Poorly drained, frequently waterlogged soils common in drumlin lowlands of County Mayo; limits agricultural productivity.",
        section: "8.3"
      },
      {
        term: "What is the impact of Brexit on western farming?",
        definition: "UK's exit from the EU has reduced demand for Irish cattle exports; economists estimate up to 70% of western farmers face significant financial challenges.",
        section: "8.3"
      }
    ];
    c.learningOutcomes[2].questions = [
      {
        type: "short",
        marks: 30,
        prompt: "Examine the factors that influence the development of agriculture in two contrasting Irish regions.",
        model: "Physical Factors — GDA: The GDA's gently rolling lowland relief is ideal for mechanisation — combine harvesters, tractors and precision agricultural equipment can be used effectively across most of the region. The GDA has fertile brown earth soils with low leaching risk and high calcium content — supporting the production of grain, potatoes, vegetables and horticulture. The cool temperate oceanic climate of the GDA provides approximately 700 mm of rainfall annually, mild winters and warm summers — a good growing season for a wide range of crops. Physical Factors — West: The West's mountainous terrain — with steep, often rocky slopes — prevents the use of large agricultural machinery on most upland farms. The West has peat, gley and podzol soils — these have poor drainage, are prone to waterlogging and flooding, and are unsuitable for most arable crops. Annual rainfall in the West exceeds 1,200 mm in many areas — soils become saturated for extended periods; leaching removes essential minerals, further reducing soil fertility. The harsher climate in the West, with more exposure to wind and lower temperatures, shortens the growing season and limits the range of viable crops. Socio-Economic — GDA: The GDA has a population of approximately 2.1 million — providing the largest internal market for agricultural produce in Ireland, close to where it is grown. Average disposable income in the GDA is 17% above the national average — residents spend more on quality food products, supporting premium agricultural markets. The majority of GDA farms are commercially profitable — younger farmers are adopting modern precision farming practices, and larger farm sizes allow significant capital investment. Excellent road, rail and port networks in the GDA mean produce can reach domestic and European markets quickly and cost-effectively. Socio-Economic — West: The West's peripheral location — distant from major population centres and European markets — increases transport costs and reduces the competitiveness of western agricultural produce. Galway Harbour is the only significant port in the West but is poorly positioned for direct European trade compared to Dublin or Cork. Average farming income in the West is approximately €20,000 below the GDA — most western farmers depend on EU Common Agricultural Policy (CAP) grants to remain viable. Roads in the West are underdeveloped — the M6 is the only motorway, and mountainous terrain makes road construction extremely expensive. Labour in the agricultural sector is increasingly difficult to attract in the West — young people leave for urban employment opportunities, creating an ageing farming community with limited capacity for change."
      }
    ];
    c.examQuestions = [
      {
        id: "geo8-eq-1",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q1.",
            question: "Examine two factors that have influenced the development of tourism in an Irish region.",
            marks: 30,
            model: "Factor 1 — Tourist Attractions: The Greater Dublin Area (GDA) attracts approximately 11 million visitors per year and earns approximately €6 billion annually from tourism. Major cultural and heritage attractions — Dublin Castle, the Guinness Storehouse and Trinity College — attract large numbers of year-round visitors regardless of weather conditions. Events tourism is a major strength of the GDA — concerts, international sports events and major conferences bring significant visitor numbers and spend. Retail tourism generates approximately €1 billion per year for the GDA — international visitors make Dublin a major shopping destination. Approximately 250,000 people in the GDA are directly employed in tourism-related industries, making it a critical part of the regional economy. The West of Ireland's primary tourism asset is the Wild Atlantic Way — founded in 2014, it is one of the world's longest defined coastal touring routes at approximately 2,500 km. The Wild Atlantic Way generated approximately €2 billion in tourist spending in 2019 alone, before the disruption of the pandemic. The Gaeltacht attracts approximately 30,000 Irish language students per year — a unique form of cultural and educational tourism that benefits remote western communities. Factor 2 — Transport Infrastructure: Dublin Airport is the primary international gateway for Ireland, connecting the country to over 180 destinations worldwide and delivering the vast majority of overseas tourists. The Luas light rail network and DART suburban rail have been expanded — improving access from the airport and port to Dublin's major tourist attractions. The M50 orbital motorway was upgraded — NDP investment (2006 onwards) drove major transport infrastructure development in the GDA. The West of Ireland's transport infrastructure is significantly underdeveloped by comparison — the region is mainly car-dependent with a limited rail network. Knock Airport provides only limited connectivity with no freight services, and the West has only one motorway (M6) connecting it to Dublin. Galway City is the most visited destination in the West despite infrastructure deficits — the growth of Airbnb and short-term rental accommodation has expanded tourism capacity significantly. Improved road and air connectivity would be critical to further developing the West's tourism potential in the coming decades.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo8-eq-2",
        source: "LC Geography — Long Question",
        parts: [
          {
            label: "Q2.",
            question: "Economic activity in core regions differs from those in peripheral regions. Examine this statement with reference to examples.",
            marks: 30,
            model: "Primary Activity — GDA (Core): The GDA has fertile brown earth soils, gently rolling lowlands and approximately 700 mm of annual rainfall — conditions ideal for commercial arable farming. GDA farms are large, highly mechanised and commercially profitable — using modern equipment to grow grain, potatoes, and horticulture products at scale. Co. Kildare's horse breeding industry is globally competitive — the region's well-drained limestone soils and flat terrain make it ideal for thoroughbred production and training. Primary Activity — West (Peripheral): The West has peat, gley and podzol soils with characteristically poor drainage, prone to waterlogging and flooding — unsuitable for most arable crops. Mountainous terrain prevents mechanisation on most western farms — small, often semi-subsistence farms persist where combine harvesters cannot operate. Approximately 50% of western farmers rely on income from outside farming to survive — EU farm grants are essential to the viability of farming in the region. The average farmer income in the West is approximately €20,000 per year less than in the GDA — reflecting the fundamental physical disadvantages of the western landscape. Secondary Activity — GDA (Core): The GDA attracts the vast majority of Ireland's foreign direct investment (FDI) — 19 of the world's 20 largest pharmaceutical companies have a presence in Ireland, most based in the GDA. Ireland exports over €100 billion in pharmaceutical products annually — the GDA is the primary driver of this globally significant export sector. The GDA offers multinationals a highly educated workforce, well-developed transport infrastructure (M50, Dublin Port, Dublin Airport) and a population of 2.1 million. Secondary Activity — West (Peripheral): Industrial job growth in Galway has been approximately 20% per year — above the national average — but this growth is from a very low starting base. The West struggles to attract investment due to poor transport (only one motorway), a small labour force and the brain drain of graduates to the GDA. Tertiary Activity: The GDA generates €6 billion annually from tourism, employs 250,000 in tourism-related work and hosts well-developed financial, retail and hospitality services. Tourism is growing in the West (particularly through the Wild Atlantic Way) but employment in services remains limited by low population density and poor infrastructure. Core regions benefit from agglomeration economies — services cluster together, reducing costs and attracting further business investment; peripheral regions lack this self-reinforcing economic dynamic.",
            diagram: ""
          }
        ]
      },
      {
        id: "geo8-eq-3",
        source: "LC Geography — Sample 2018",
        parts: [
          {
            label: "Q3.",
            question: "Examine the factors that influence the development of agriculture in two contrasting Irish regions.",
            marks: 30,
            model: "Physical Factors — GDA: The GDA's gently rolling lowland relief is ideal for mechanisation — combine harvesters, tractors and precision agricultural equipment can be used effectively across most of the region. The GDA has fertile brown earth soils with low leaching risk and high calcium content — supporting the production of grain, potatoes, vegetables and horticulture. The cool temperate oceanic climate of the GDA provides approximately 700 mm of rainfall annually, mild winters and warm summers — a good growing season for a wide range of crops. Physical Factors — West: The West's mountainous terrain — with steep, often rocky slopes — prevents the use of large agricultural machinery on most upland farms. The West has peat, gley and podzol soils — these have poor drainage, are prone to waterlogging and flooding, and are unsuitable for most arable crops. Annual rainfall in the West exceeds 1,200 mm in many areas — soils become saturated for extended periods; leaching removes essential minerals, further reducing soil fertility. The harsher climate in the West, with more exposure to wind and lower temperatures, shortens the growing season and limits the range of viable crops. Socio-Economic — GDA: The GDA has a population of approximately 2.1 million — providing the largest internal market for agricultural produce in Ireland, close to where it is grown. Average disposable income in the GDA is 17% above the national average — residents spend more on quality food products, supporting premium agricultural markets. The majority of GDA farms are commercially profitable — younger farmers are adopting modern precision farming practices, and larger farm sizes allow significant capital investment. Excellent road, rail and port networks in the GDA mean produce can reach domestic and European markets quickly and cost-effectively. Socio-Economic — West: The West's peripheral location — distant from major population centres and European markets — increases transport costs and reduces the competitiveness of western agricultural produce. Galway Harbour is the only significant port in the West but is poorly positioned for direct European trade compared to Dublin or Cork. Average farming income in the West is approximately €20,000 below the GDA — most western farmers depend on EU Common Agricultural Policy (CAP) grants to remain viable. Roads in the West are underdeveloped — the M6 is the only motorway, and mountainous terrain makes road construction extremely expensive. Labour in the agricultural sector is increasingly difficult to attract in the West — young people leave for urban employment opportunities, creating an ageing farming community with limited capacity for change.",
            diagram: ""
          }
        ]
      }
    ];
  })();

})();