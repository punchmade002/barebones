// Home Economics Content — chapter notes, plus flashcard keyTerms injected from FLASHCARDS_DB.
// Requires: data.js (COURSE_DATA) and home-economics-flashcards.js (FLASHCARDS_DB) to be loaded first.
//
// Notes cover the Leaving Certificate Home Economics (Social & Scientific) core: food science
// and nutrition, resource management and consumer studies, and social studies.
(function () {
  if (typeof COURSE_DATA === 'undefined') return;
  var DB = window.FLASHCARDS_DB || {};
  var chapters = COURSE_DATA.chapters;

  var NOTES = {

    // ── 1. Carbohydrates and Dietary Fibre ─────────────────────────────────
    'hom-carbohydrates': [
      {
        h: "Composition and classification",
        b: "Carbohydrates contain carbon, hydrogen and oxygen, with hydrogen and oxygen in the same 2:1 ratio as water. They are classified by the number of sugar units: monosaccharides (one), disaccharides (two) and polysaccharides (many). Plants make them by photosynthesis, so almost all dietary carbohydrate is of plant origin — the one significant exception being lactose in milk."
      },
      {
        h: "Monosaccharides and disaccharides",
        b: "The monosaccharides are glucose (fruit, honey, the form carried in blood), fructose (the sweetest sugar, in fruit and honey) and galactose (found only combined in lactose). The disaccharides are sucrose (glucose + fructose — table sugar), lactose (glucose + galactose — milk sugar) and maltose (glucose + glucose — in germinating grain and malt)."
      },
      {
        h: "Polysaccharides",
        b: "Starch is the plant storage polysaccharide, found in cereals, potatoes and pulses, and is the main energy source in most diets. Glycogen is the animal equivalent, stored in liver and muscle. Dextrin forms when starch is broken down by dry heat. Cellulose and pectin are structural polysaccharides that humans cannot digest, and form part of dietary fibre."
      },
      {
        h: "Biological functions",
        b: "Carbohydrate's primary role is to supply energy — 1 g yields 4 kcal (17 kJ) — and it is the only fuel the brain and red blood cells use under normal conditions. Adequate carbohydrate spares protein for growth and repair rather than energy. Excess is converted to glycogen and, once those stores are full, to adipose fat. Lactose also aids calcium absorption."
      },
      {
        h: "Dietary fibre: soluble and insoluble",
        b: "Dietary fibre, or non-starch polysaccharide, is plant material that resists digestion. Insoluble fibre — cellulose in wheat bran, wholegrain cereals and vegetable skins — absorbs water, adds bulk and speeds transit, preventing constipation, diverticulitis and haemorrhoids. Soluble fibre — pectin and gums in oats, barley, fruit and pulses — forms gels that lower LDL cholesterol and slow glucose absorption."
      },
      {
        h: "Gelatinisation",
        b: "When starch is heated in liquid above about 60°C the granules absorb water and swell; at around 80°C they rupture and release starch, thickening the liquid. On cooling the mixture sets to a gel. This is the basis of sauces, custards, soups and gravies. Constant stirring prevents lumps, and excess acid or sugar weakens the gel."
      },
      {
        h: "Dextrinisation and caramelisation",
        b: "Dextrinisation is the breakdown of starch to dextrins by dry heat, producing the brown colour and flavour of toast, bread crust and grilled foods. Caramelisation occurs when sugar is heated above about 160°C: it melts, darkens and develops a distinctive flavour. Both reactions contribute appearance and taste but destroy some heat-sensitive nutrients at the surface."
      },
      {
        h: "Other properties",
        b: "Sugar is hygroscopic (attracts water), which keeps cakes moist and, in high concentration, preserves jams by making water unavailable to microorganisms. Hydrolysis splits disaccharides and polysaccharides into simple sugars using water, catalysed by enzymes or by acid and heat. Starch is insoluble in cold water, which is why sauces must be blended before heating."
      },
      {
        h: "Sugar in the diet and dental health",
        b: "Free sugars — those added to food plus those in honey, syrups and fruit juice — are recommended to be limited to under 10% of energy intake, and ideally under 5%. Frequent consumption feeds oral bacteria that produce acid and demineralise enamel, causing dental caries. High intakes also displace nutrient-dense foods and contribute to obesity and type 2 diabetes."
      },
      {
        h: "Recommended intake and sources",
        b: "Carbohydrate should supply roughly half of total energy, with the emphasis on wholegrain cereals, potatoes, pulses, fruit and vegetables rather than refined sugars. Adult fibre intake should be about 25-30 g per day, achieved by choosing wholemeal bread and wholegrain cereals, eating fruit and vegetables with skins on, and including pulses — with adequate fluid, since fibre needs water to work."
      }
    ],

    // ── 2. Proteins and Amino Acids ────────────────────────────────────────
    'hom-proteins': [
      {
        h: "Composition and structure",
        b: "Proteins contain carbon, hydrogen, oxygen and nitrogen, and many also contain sulphur and phosphorus. Nitrogen is what distinguishes them from carbohydrates and fats. They are built from amino acids joined by peptide bonds into long chains, which then fold into precise three-dimensional shapes. There are about twenty amino acids in food proteins."
      },
      {
        h: "Essential and non-essential amino acids",
        b: "Essential (indispensable) amino acids cannot be made by the body and must come from food — there are eight for adults, with histidine additionally essential for infants. Non-essential amino acids can be synthesised from other amino acids. It is the essential ones that determine a protein's nutritional value."
      },
      {
        h: "Biological value",
        b: "High biological value proteins contain all the essential amino acids in the proportions the body needs: meat, poultry, fish, eggs, milk, cheese and soya. Low biological value proteins are deficient in one or more: cereals, pulses, nuts and seeds. Egg and human milk protein are the reference standards against which others are measured."
      },
      {
        h: "Complementary value",
        b: "Two low biological value proteins eaten together can supply the full range of essential amino acids, because the amino acid missing from one is present in the other. Cereals are low in lysine and pulses are low in methionine, so beans on toast, lentil soup with bread, or hummus with pitta provide complete protein. This principle underpins well-planned vegetarian and vegan diets."
      },
      {
        h: "Protein structure",
        b: "Primary structure is the sequence of amino acids in the chain. Secondary structure is the coiling or pleating of that chain into helices or sheets held by hydrogen bonds. Tertiary structure is the further folding into a compact globular or fibrous shape. Fibrous proteins such as collagen and keratin are structural; globular proteins such as albumen and enzymes are functional."
      },
      {
        h: "Denaturation and coagulation",
        b: "Denaturation is the unfolding of a protein's structure without breaking peptide bonds, caused by heat, acid, alkali, mechanical action or heavy metal salts. It is irreversible and changes texture, appearance and digestibility. Coagulation follows: the denatured chains link together and set, as when egg white turns opaque and firm from about 60°C or milk curdles with lemon juice."
      },
      {
        h: "Foam formation and elasticity",
        b: "Whisking egg white denatures the protein and traps air in a foam, which sets on heating — the basis of meringue, soufflé and whisked sponge. Over-beating makes the foam dry and liable to collapse. Gluten, formed when the wheat proteins gliadin and glutenin are mixed with water and kneaded, is elastic and extensible, trapping gas so that bread rises and holds its shape."
      },
      {
        h: "The Maillard reaction and gel formation",
        b: "The Maillard reaction is non-enzymic browning between amino acids and reducing sugars under dry heat, producing the colour and aroma of roast meat, bread crust, and browned pastry. Gel formation occurs when denatured protein traps liquid in a three-dimensional mesh, as gelatine does in jellies and mousses. Both are exploited constantly in cooking."
      },
      {
        h: "Functions in the body",
        b: "Protein's primary roles are growth and the repair of body tissue, and the manufacture of enzymes, hormones, antibodies, haemoglobin and other functional molecules. It also supplies energy at 4 kcal (17 kJ) per gram, though this is a wasteful use of an expensive nutrient. Deficiency causes poor growth, delayed healing, muscle wasting, oedema and lowered immunity."
      },
      {
        h: "Requirements and sources",
        b: "Adults need roughly 0.75-0.8 g of protein per kilogram of body weight per day, with increased needs during growth, pregnancy, lactation, and recovery from illness or surgery. Around 10-15% of energy intake from protein is typical. Excess is not stored: the nitrogen is removed by deamination in the liver, excreted as urea, and the remainder is used for energy or stored as fat."
      }
    ],

    // ── 3. Lipids and Fats ─────────────────────────────────────────────────
    'hom-lipids': [
      {
        h: "Composition and structure",
        b: "Lipids contain carbon, hydrogen and oxygen, but with far less oxygen in proportion than carbohydrates, which is why they yield more than twice the energy. Most dietary fat is triglyceride: one molecule of glycerol joined to three fatty acids. The nature of those fatty acids determines whether the fat is solid or liquid and how it behaves in the body."
      },
      {
        h: "Saturated fatty acids",
        b: "Saturated fatty acids have no double bonds between carbon atoms — every bond is filled with hydrogen. They are straight-chained, pack closely, and are therefore solid at room temperature. Sources are mainly animal: butter, lard, suet, the fat on meat, and full-fat dairy, plus the tropical oils coconut and palm. High intakes raise LDL cholesterol and the risk of coronary heart disease."
      },
      {
        h: "Unsaturated fatty acids",
        b: "Monounsaturated fatty acids have one double bond — olive oil, rapeseed oil, avocados, peanuts — and help maintain HDL cholesterol. Polyunsaturated fatty acids have two or more double bonds and are liquid even when chilled: sunflower and corn oil, oily fish, nuts and seeds. Double bonds create kinks that prevent close packing, which is why these fats are oils."
      },
      {
        h: "Essential fatty acids",
        b: "Linoleic acid (omega-6) and alpha-linolenic acid (omega-3) cannot be synthesised by the body and must be supplied by the diet. They are needed for cell membranes, brain and nervous tissue, and the production of hormone-like regulators. The long-chain omega-3 fatty acids EPA and DHA in oily fish support heart and brain function; two portions of fish a week, one oily, is the usual recommendation."
      },
      {
        h: "Hydrogenation and trans fats",
        b: "Hydrogenation adds hydrogen across the double bonds of a liquid oil in the presence of a nickel catalyst, converting it to a solid or semi-solid fat for margarines and shortenings. Partial hydrogenation produces trans fatty acids, which behave like saturated fats but are worse: they raise LDL and lower HDL cholesterol. Their use has been heavily restricted, and manufacturers now use alternative processes."
      },
      {
        h: "Cholesterol",
        b: "Cholesterol is a sterol needed for cell membranes, bile salts, vitamin D and steroid hormones, and most of it is made by the liver rather than eaten. It is carried in the blood by lipoproteins: LDL deposits cholesterol in artery walls and is the 'bad' carrier, while HDL removes it to the liver. Saturated and trans fat intake influences blood cholesterol far more than dietary cholesterol itself."
      },
      {
        h: "Emulsions and emulsifiers",
        b: "Oil and water do not mix, but an emulsifier — a molecule with a water-loving head and a fat-loving tail — holds them together. Lecithin in egg yolk stabilises mayonnaise and hollandaise; milk is a natural oil-in-water emulsion; butter and margarine are water-in-oil. Commercial emulsifiers and stabilisers keep sauces, ice cream and low-fat spreads from separating."
      },
      {
        h: "Plasticity, shortening and aeration",
        b: "Plasticity is a fat's ability to be spread or creamed over a range of temperatures, which depends on its mix of fatty acids. Shortening happens when fat coats flour particles and prevents gluten development, giving pastry and shortbread their crumbly texture. Aeration is the trapping of air when fat and sugar are creamed, giving cakes their light structure."
      },
      {
        h: "Rancidity and smoke point",
        b: "Oxidative rancidity occurs when oxygen attacks the double bonds of unsaturated fats, producing off-flavours and odours; it is accelerated by light, heat and metal traces and slowed by antioxidants and airtight, cool, dark storage. Hydrolytic rancidity splits fatty acids from glycerol in the presence of moisture and enzymes. The smoke point is the temperature at which a fat breaks down and smokes, and should not be exceeded in frying."
      },
      {
        h: "Functions, requirements and health",
        b: "Fat supplies concentrated energy at 9 kcal (37 kJ) per gram, carries the fat-soluble vitamins A, D, E and K, insulates the body, protects organs, and gives food flavour, texture and satiety. Fat should provide no more than about 35% of energy, with saturated fat under 10%. Excess intake is linked to obesity, cardiovascular disease and some cancers."
      }
    ],

    // ── 4. Vitamins and Minerals ───────────────────────────────────────────
    'hom-vitamins-minerals': [
      {
        h: "What vitamins are",
        b: "Vitamins are organic substances needed in very small amounts to regulate body processes. They supply no energy and are not building materials, but without them metabolism fails. They divide into fat-soluble (A, D, E and K), which are stored in the liver and adipose tissue and can accumulate to toxic levels, and water-soluble (the B group and C), which are not stored and must be supplied regularly."
      },
      {
        h: "Vitamin A",
        b: "Vitamin A occurs as retinol in liver, oily fish, egg yolk, butter and fortified margarine, and as beta-carotene in carrots, sweet potato and dark green leafy vegetables. It is needed for rhodopsin in the retina, for healthy epithelial tissue and for immune function. Deficiency causes night blindness and, in severe cases, xerophthalmia; excess in pregnancy is teratogenic, so liver is avoided."
      },
      {
        h: "Vitamin D",
        b: "Vitamin D is unusual in being synthesised in the skin on exposure to UVB sunlight, with dietary sources limited to oily fish, egg yolk, liver and fortified foods. It controls the absorption of calcium and phosphorus and their deposition in bone. Deficiency causes rickets in children and osteomalacia in adults, and is common at Irish latitudes in winter, so supplementation is widely advised."
      },
      {
        h: "Vitamins E and K",
        b: "Vitamin E is an antioxidant that protects cell membranes and polyunsaturated fats from oxidation, and is found in vegetable oils, nuts, seeds and wheatgerm. Vitamin K is required for the synthesis of prothrombin and therefore for blood clotting, and also for bone protein. It comes from green leafy vegetables and is made by bacteria in the large intestine; newborns are given a supplement."
      },
      {
        h: "The B group",
        b: "The B vitamins act mainly as coenzymes in energy metabolism. Thiamine (B1) is needed for carbohydrate metabolism; deficiency causes beriberi. Riboflavin (B2) and niacin (B3) release energy from food, and niacin deficiency causes pellagra. B6 is involved in protein metabolism, and B12, found only in animal foods, is needed with folate for red blood cell formation — deficiency causes pernicious anaemia."
      },
      {
        h: "Folate",
        b: "Folate is essential for cell division and the formation of DNA and red blood cells. Its best-known role is the prevention of neural tube defects such as spina bifida: because the neural tube closes in the first four weeks, women capable of becoming pregnant are advised to take 400 µg of folic acid daily before conception and through the first trimester. Sources include green leafy vegetables, pulses, liver and fortified cereals."
      },
      {
        h: "Vitamin C",
        b: "Ascorbic acid is needed for the synthesis of collagen, for wound healing, as an antioxidant, and for the absorption of non-haem iron from plant foods. Sources are citrus fruit, blackcurrants, kiwi, peppers, broccoli and potatoes. Deficiency causes scurvy — bleeding gums, poor healing, weakened connective tissue. It is the most easily destroyed vitamin, lost to heat, light, air, alkali and water."
      },
      {
        h: "Calcium and phosphorus",
        b: "About 99% of body calcium is in the bones and teeth, with the remainder essential for blood clotting, nerve transmission and muscle contraction. Absorption requires vitamin D and is hindered by phytates and oxalates. Milk, cheese, yogurt, tinned fish with bones, and fortified products are the main sources. Phosphorus works with calcium in bone and is part of ATP and DNA."
      },
      {
        h: "Iron",
        b: "Iron is a component of haemoglobin, which carries oxygen in the blood, and of myoglobin in muscle. Haem iron from meat, offal and fish is well absorbed; non-haem iron from pulses, dark green vegetables, dried fruit and fortified cereals is absorbed far less well, though vitamin C taken with the meal improves uptake while tea and coffee hinder it. Deficiency causes anaemia, with fatigue, pallor and breathlessness."
      },
      {
        h: "Other minerals and trace elements",
        b: "Sodium and potassium control fluid balance and nerve transmission; excess sodium raises blood pressure, and salt intake should stay under 6 g a day. Iodine is needed to make thyroxine, and deficiency causes goitre. Fluorine strengthens tooth enamel against decay. Zinc supports immunity, healing and growth. Most trace elements are amply supplied by a varied diet."
      },
      {
        h: "Minimising nutrient losses",
        b: "Water-soluble vitamins leach into cooking water and are destroyed by prolonged heat, so vegetables should be prepared just before cooking, cut coarsely, cooked in a minimum of boiling water for the shortest time — or steamed or microwaved — and served promptly. Keeping vegetables cool and dark, avoiding bicarbonate of soda, and reusing cooking liquid in sauces and soups all reduce losses."
      }
    ],

    // ── 5. Digestion and Metabolism ────────────────────────────────────────
    'hom-digestion-metabolism': [
      {
        h: "Purpose of digestion",
        b: "Digestion breaks food down physically and chemically into molecules small enough to be absorbed into the bloodstream. Carbohydrates are reduced to monosaccharides, proteins to amino acids, and fats to fatty acids and glycerol. Mechanical digestion — chewing, churning, emulsification — increases surface area so that enzymes, which are chemical catalysts, can work efficiently."
      },
      {
        h: "The mouth and oesophagus",
        b: "Teeth cut and grind food while saliva moistens it and binds it into a bolus. Salivary amylase (ptyalin) begins the breakdown of cooked starch to maltose in the slightly alkaline mouth. Swallowing pushes the bolus into the oesophagus, where waves of muscular contraction called peristalsis carry it to the stomach; the epiglottis closes the trachea to prevent choking."
      },
      {
        h: "The stomach",
        b: "The stomach churns food into a semi-liquid chyme and secretes gastric juice containing hydrochloric acid, pepsinogen and mucus. The acid provides the pH of about 2 needed to activate pepsinogen into pepsin, which begins protein digestion, and it also kills most ingested bacteria. Rennin coagulates milk protein in infants. Mucus protects the stomach lining from self-digestion."
      },
      {
        h: "The small intestine: duodenum",
        b: "Chyme entering the duodenum is neutralised by alkaline secretions. Bile, made in the liver and stored in the gall bladder, contains no enzymes but emulsifies fat into tiny droplets, greatly increasing the surface area for lipase. Pancreatic juice supplies amylase for starch, trypsin for protein and lipase for fat. Intestinal juice completes digestion with maltase, sucrase, lactase and peptidases."
      },
      {
        h: "Absorption in the ileum",
        b: "The ileum is adapted for absorption: it is long, and its lining is folded into millions of finger-like villi, each covered in microvilli, giving an enormous surface area. Each villus has a thin single-cell wall, a network of capillaries and a lacteal. Glucose and amino acids pass into the capillaries and travel to the liver via the hepatic portal vein; fatty acids and glycerol enter the lacteals and the lymphatic system."
      },
      {
        h: "The large intestine",
        b: "Undigested material, mainly dietary fibre, passes into the colon, where water and mineral salts are reabsorbed and the residue is compacted into faeces for elimination through the rectum and anus. Resident gut bacteria ferment some fibre, synthesise vitamin K and some B vitamins, and contribute to immune function. Adequate fibre and fluid keep transit time short and the stool soft."
      },
      {
        h: "The liver",
        b: "The liver is the body's chemical processing centre. It regulates blood glucose by converting excess to glycogen and releasing it as needed; deaminates surplus amino acids, converting the nitrogen to urea for excretion by the kidneys; stores iron and the fat-soluble vitamins; makes bile and plasma proteins; and detoxifies alcohol, drugs and other harmful substances."
      },
      {
        h: "Metabolism: anabolism and catabolism",
        b: "Metabolism is the sum of all chemical reactions in the body. Catabolism breaks larger molecules into smaller ones and releases energy, as in the oxidation of glucose to carbon dioxide, water and ATP. Anabolism builds larger molecules from smaller ones and uses energy, as in the synthesis of body protein from amino acids. Enzymes control both, and hormones such as insulin regulate the balance."
      },
      {
        h: "Basal metabolic rate",
        b: "Basal metabolic rate is the energy needed to maintain essential functions — breathing, circulation, cell repair, body temperature — at complete rest. It accounts for most of daily energy expenditure and is raised by a large body size, a high proportion of lean muscle, youth, growth, pregnancy, fever and an overactive thyroid, and lowered by ageing, a low muscle mass and prolonged undereating."
      },
      {
        h: "Factors affecting digestion",
        b: "Thorough chewing, relaxed eating and regular meals aid digestion, as does adequate fluid and fibre. Digestion is hindered by eating too quickly, stress, very fatty meals, which slow stomach emptying, and excess alcohol. Cooking generally improves digestibility by softening fibre and gelatinising starch, but overcooked protein becomes tough and harder to break down."
      }
    ],

    // ── 6. Energy Balance and Nutritional Needs ────────────────────────────
    'hom-energy-nutrition': [
      {
        h: "Measuring food energy",
        b: "Food energy is measured in kilocalories (kcal) or kilojoules (kJ), where 1 kcal equals 4.2 kJ. The energy value of each macronutrient is fixed: carbohydrate and protein each supply 4 kcal (17 kJ) per gram, fat 9 kcal (37 kJ) per gram, and alcohol 7 kcal (29 kJ) per gram. Vitamins, minerals, water and fibre supply none."
      },
      {
        h: "Energy balance",
        b: "Body weight is stable when energy intake equals energy expenditure. A sustained surplus is stored as adipose fat and weight rises; a sustained deficit draws on those stores and weight falls. Because roughly 7,000 kcal is stored per kilogram of body fat, small daily imbalances produce large changes over months — which is why gradual, sustainable change works better than crash dieting."
      },
      {
        h: "Components of energy expenditure",
        b: "Total energy expenditure has three parts: basal metabolic rate, which is much the largest; physical activity, which is the most variable and the part a person can change; and the thermic effect of food, the energy used to digest and absorb a meal, which is around 10% of intake. Physical activity level (PAL) is applied to BMR to estimate total needs."
      },
      {
        h: "Factors affecting energy requirements",
        b: "Requirements rise with body size and lean muscle mass, with growth in childhood and adolescence, with pregnancy and lactation, with occupational and leisure activity, and in cold conditions or during illness and recovery. They are lower in older adults as muscle mass and activity decline. Men generally need more than women of the same age because of greater lean mass."
      },
      {
        h: "Dietary reference values",
        b: "Dietary reference values estimate the nutrient needs of population groups, not individuals. The Recommended Daily Allowance is set high enough to meet the needs of almost everyone in a group and is used on food labels and in menu planning. Estimated Average Requirement is the mid-point of need. These figures guide planning, but individual needs vary."
      },
      {
        h: "The food pyramid and balanced eating",
        b: "The food pyramid arranges food groups by the proportion they should occupy in the diet: vegetables, salad and fruit and the starchy foods group at the base; milk, yogurt and cheese and the meat, fish and alternatives group in the middle; fats, spreads and oils in small amounts; and foods high in fat, sugar and salt outside the pyramid, not needed for health. A balanced diet supplies all nutrients in appropriate proportions."
      },
      {
        h: "Nutritional needs across the life cycle",
        b: "Infants need energy- and nutrient-dense feeding, ideally breast milk, for rapid growth. Children and adolescents need protein, calcium and iron for growth and bone development, with adolescent girls particularly at risk of iron deficiency. Adults need a maintenance diet with attention to fat, salt and fibre. Older adults need fewer calories but the same or more vitamin D, calcium, protein and fibre."
      },
      {
        h: "Pregnancy and lactation",
        b: "Energy needs rise modestly in later pregnancy, but nutrient needs rise more sharply: folic acid before conception and in early pregnancy to prevent neural tube defects; iron for expanded blood volume; calcium and vitamin D for fetal skeleton; and protein for tissue growth. Alcohol, liver, raw eggs, unpasteurised cheese and pâté are avoided. Lactation increases energy and fluid needs further."
      },
      {
        h: "Obesity and underweight",
        b: "Body mass index — weight in kilograms divided by height in metres squared — classifies adults as underweight below 18.5, healthy from 18.5 to 24.9, overweight from 25 to 29.9 and obese at 30 or over, though it does not distinguish muscle from fat. Obesity raises the risk of type 2 diabetes, cardiovascular disease, some cancers and joint problems; underweight risks nutrient deficiency, poor immunity and reduced bone density."
      },
      {
        h: "Diet and chronic disease",
        b: "Diet is a modifiable factor in the main non-communicable diseases. Reducing saturated and trans fat and salt lowers cardiovascular risk; limiting free sugars and excess energy lowers the risk of type 2 diabetes and obesity; adequate fibre, fruit and vegetables are protective against bowel cancer; and adequate calcium and vitamin D with weight-bearing exercise protects against osteoporosis."
      }
    ],

    // ── 7. Meat: Selection, Properties and Cooking ─────────────────────────
    'hom-meat-preparation': [
      {
        h: "Structure of meat",
        b: "Meat is animal muscle, made of bundles of long muscle fibres held together by connective tissue and enclosed in sheaths. The thickness of the fibres and the amount of connective tissue determine tenderness: hard-working muscles such as shin and neck have coarse fibres and abundant connective tissue, while little-used muscles such as fillet are fine-grained and tender."
      },
      {
        h: "Connective tissue",
        b: "Connective tissue contains two proteins. Collagen is white and converts to soluble gelatine when cooked slowly in moist heat, which is why tough cuts become tender in a stew or casserole. Elastin is yellow, and does not break down in cooking, so it must be trimmed away. Older animals have more and tougher connective tissue than young ones."
      },
      {
        h: "Nutritional value",
        b: "Meat supplies high biological value protein, well-absorbed haem iron, zinc and the B vitamins, particularly B12, which is found only in animal foods. Liver and other offal are exceptionally rich in iron and vitamin A. Meat contains no carbohydrate and no vitamin C. Fat content varies widely with the cut and with trimming, and the fat is mainly saturated."
      },
      {
        h: "Selecting and buying",
        b: "Fresh meat should be firm and slightly moist rather than wet or slimy, with a fresh smell and colour appropriate to the type — bright red in beef after exposure to air, pale pink in pork, light in poultry. Fat should be firm and creamy. Check the use-by date, the Bord Bia quality mark and country of origin, and buy from a clean, refrigerated display."
      },
      {
        h: "Storage and safety",
        b: "Raw meat is stored covered on the bottom shelf of the refrigerator at 0-5°C so that it cannot drip onto ready-to-eat foods, and used within two to three days or frozen at -18°C. Frozen meat is thawed thoroughly in the refrigerator, never at room temperature, and never refrozen once thawed. Separate boards and knives for raw meat prevent cross-contamination."
      },
      {
        h: "Tenderising",
        b: "Meat is tenderised mechanically by mincing, pounding or scoring across the grain; chemically by marinades containing acid such as wine, vinegar or lemon juice, which swell the protein; enzymically by papain from papaya or bromelain from pineapple; and by hanging, in which the animal's own enzymes break down muscle protein over days in controlled chilled conditions."
      },
      {
        h: "Effects of cooking",
        b: "Protein coagulates from about 60°C, and the fibres shrink and expel water, so overcooking makes meat dry and tough. Collagen converts to gelatine above about 70°C given enough time and moisture. Myoglobin changes from red to brown. Fat melts, carrying flavour. Dry heat produces Maillard browning on the surface, and connective tissue in tough cuts needs long, slow, moist cooking."
      },
      {
        h: "Choosing a cooking method for the cut",
        b: "Tender cuts with little connective tissue — fillet, sirloin, loin chops — suit quick dry methods such as grilling, frying and roasting. Tough cuts with much connective tissue — shin, brisket, shoulder, neck — need long slow moist methods such as stewing, casseroling, braising and pot-roasting, which convert collagen to gelatine and produce a rich sauce."
      },
      {
        h: "Poultry and food safety",
        b: "Poultry is more perishable than red meat and is frequently contaminated with Salmonella and Campylobacter, so it must be cooked right through until the juices run clear and the core temperature reaches 75°C. It should not be washed before cooking, as that splashes bacteria around the kitchen. Stuffing is safest cooked separately, since it slows heat penetration to the centre of the bird."
      },
      {
        h: "Meat products and alternatives",
        b: "Processed meats such as bacon, ham, sausages and salami are preserved with salt, nitrites and smoking; they are high in salt and saturated fat, and processed meat intake is linked to bowel cancer, so consumption should be limited. Alternatives to meat include fish, eggs, pulses, tofu, textured vegetable protein and mycoprotein, which supply protein with little or no saturated fat."
      }
    ],

    // ── 8. Fish and Seafood ────────────────────────────────────────────────
    'hom-fish-seafood': [
      {
        h: "Classification of fish",
        b: "White fish store oil in the liver rather than the flesh, so the flesh is very low in fat — cod, haddock, whiting, plaice, sole. Oily fish store oil throughout the flesh — mackerel, herring, salmon, trout, sardines. Shellfish divide into crustaceans with jointed shells, such as prawns, crab and lobster, and molluscs with hinged or single shells, such as mussels, oysters and scallops."
      },
      {
        h: "Structure and why fish cooks quickly",
        b: "Fish muscle is arranged in short blocks of fibre separated by very thin sheets of connective tissue, with almost no elastin. That connective tissue converts to gelatine at a much lower temperature and in far less time than in meat, so fish is naturally tender, cooks in minutes, and flakes easily. It also means fish overcooks quickly, becoming dry and falling apart."
      },
      {
        h: "Nutritional value",
        b: "All fish supply high biological value protein — around 16-20% — with B vitamins, iodine and, where small bones are eaten as in tinned sardines and salmon, calcium and phosphorus. Oily fish are the outstanding dietary source of long-chain omega-3 fatty acids EPA and DHA, and of the fat-soluble vitamins A and D. White fish is very low in fat and useful in low-calorie and low-cholesterol diets."
      },
      {
        h: "Omega-3 and health",
        b: "The omega-3 fatty acids in oily fish reduce blood triglycerides, discourage clot formation, help maintain a regular heart rhythm and have anti-inflammatory effects, lowering the risk of coronary heart disease. They are also important for brain and retinal development in the foetus and infant. The general recommendation is two portions of fish a week, at least one of them oily."
      },
      {
        h: "Signs of freshness",
        b: "Fresh whole fish has bright, full, clear eyes rather than sunken and cloudy ones; bright red gills; firm flesh that springs back when pressed; shiny, close-fitting scales; a moist appearance and a clean sea smell rather than a strong fishy or ammoniac odour. Fillets should look moist and translucent with no discolouration or gaping. Shellfish must be alive, with closed shells, before cooking."
      },
      {
        h: "Storage",
        b: "Fish is highly perishable because its enzymes and bacteria remain active at low temperatures and its fat oxidises readily. It should be bought last, kept cold on the way home, stored covered in the coldest part of the refrigerator and used the same day or the next. For freezing, fish must be very fresh; oily fish keeps about three months and white fish about six."
      },
      {
        h: "Cooking methods",
        b: "Suitable methods are poaching, steaming, grilling, baking, shallow and deep frying, and en papillote. Moist gentle methods suit delicate white fish; oily fish grill and bake well because their own fat bastes them. Fish is cooked when the flesh turns opaque and flakes easily from the bone, and the protein has coagulated — typically only a few minutes per side."
      },
      {
        h: "Effects of cooking",
        b: "Protein coagulates and the flesh turns from translucent to opaque; connective tissue converts rapidly to gelatine; the fibres shrink and lose moisture. Overcooking makes fish dry, tough and crumbly. Some B vitamins and, in poached fish, water-soluble nutrients leach into the liquid, which is why the cooking liquor is often used in the accompanying sauce."
      },
      {
        h: "Fish products and processing",
        b: "Fish is preserved by freezing, canning in oil or brine, smoking (cold-smoked salmon and kippers, hot-smoked mackerel), salting, drying and pickling. Processed products include fish fingers, fish cakes and breaded portions, which are convenient but often high in added fat and salt. Surimi is fish protein restructured to imitate shellfish."
      },
      {
        h: "Sustainability and safety",
        b: "Overfishing has depleted many stocks, so certification schemes such as the Marine Stewardship Council and quota systems aim to keep fishing within sustainable limits, and aquaculture now supplies a large share of the market. Large predatory fish can accumulate methylmercury, so pregnant women limit shark, swordfish and marlin. Shellfish must be sourced from clean waters and cooked thoroughly to avoid food poisoning."
      }
    ],

    // ── 9. Dairy Products and Eggs ─────────────────────────────────────────
    'hom-dairy-eggs': [
      {
        h: "Composition of milk",
        b: "Whole cow's milk is about 87% water, 3.9% fat, 3.5% protein, 4.6% lactose, with calcium, phosphorus, and vitamins A, D and the B group, particularly riboflavin and B12. Its proteins are caseinogen, which forms the curd, and the whey proteins lactalbumin and lactoglobulin. Milk is a nearly complete food, its main deficiencies being iron, vitamin C and fibre."
      },
      {
        h: "Heat treatment of milk",
        b: "Pasteurisation by the HTST method heats milk to 72°C for 15 seconds then cools it rapidly, destroying pathogens and most spoilage organisms while barely affecting flavour or nutrients. Sterilisation heats bottled milk to about 110°C for 30 minutes, giving long life but a cooked flavour. UHT heats to 135°C for 1-3 seconds and packs aseptically, keeping for months unopened."
      },
      {
        h: "Homogenisation and milk products",
        b: "Homogenisation forces milk through fine apertures so that the fat globules are broken up and distributed evenly, preventing a cream layer forming. Milk is processed into cream, butter, buttermilk, yogurt, cheese, evaporated and condensed milk, and dried milk powder. Skimmed and low-fat milks have fat removed but retain protein, calcium and lactose, though fat-soluble vitamins are reduced."
      },
      {
        h: "Yogurt",
        b: "Yogurt is made by inoculating heat-treated milk with Lactobacillus bulgaricus and Streptococcus thermophilus and incubating at about 40°C. The bacteria ferment lactose to lactic acid, which lowers the pH and coagulates the caseinogen into a soft set, giving the characteristic tang and thick texture. Live yogurt retains active cultures; probiotic yogurts add strains intended to benefit gut flora."
      },
      {
        h: "Cheese making",
        b: "Milk is pasteurised, a starter culture is added to produce lactic acid, and rennet — containing the enzyme rennin — coagulates the caseinogen into curds, leaving liquid whey. The curds are cut, heated, drained, milled, salted, pressed into moulds and ripened. Variations in milk, culture, cutting, pressing and ripening time produce the whole range from soft fresh cheese to hard mature varieties."
      },
      {
        h: "Nutritional value of dairy",
        b: "Dairy foods are the main dietary source of calcium in Ireland and supply high biological value protein, riboflavin, B12, and vitamin A in the full-fat forms. Their fat is largely saturated, so lower-fat versions are recommended for adults, though not for children under two. Three servings a day are recommended, rising to five for teenagers and for women during pregnancy and lactation."
      },
      {
        h: "Structure of an egg",
        b: "The shell is porous calcium carbonate, lined by two membranes that separate at the blunt end to form an air space that enlarges as the egg ages. Inside is the albumen — thick and thin layers of mainly water and protein — and the yolk, held centrally by twisted protein strands called chalazae. The yolk carries the fat, fat-soluble vitamins, iron and lecithin, and bears the germinal disc."
      },
      {
        h: "Nutritional value of eggs",
        b: "Eggs supply high biological value protein — ovalbumin in the white, with the whole egg used as the reference standard for protein quality — plus vitamins A, D, E and B12, iron, phosphorus and lecithin. They contain no carbohydrate and no vitamin C. Dietary cholesterol in the yolk has far less effect on blood cholesterol than saturated fat intake does."
      },
      {
        h: "Culinary properties of eggs",
        b: "Eggs coagulate on heating, setting custards, quiches and baked goods; whites trap air when whisked to form foams for meringue and soufflé; yolk lecithin emulsifies oil and water in mayonnaise; eggs bind ingredients in burgers and stuffings, coat foods for frying, glaze pastry, thicken sauces, enrich mixtures and act as a raising agent through trapped air."
      },
      {
        h: "Egg quality, storage and safety",
        b: "A fresh egg sinks and lies flat in water, while a stale one floats because its air space has enlarged; broken out, a fresh egg has a domed yolk and thick albumen. Eggs are stored pointed end down, away from strong-smelling foods, and used by the best-before date. Because of the risk of Salmonella, raw and lightly cooked egg dishes are avoided by pregnant women, infants, older people and the immunocompromised, unless the eggs carry an assured-quality mark."
      }
    ],

    // ── 10. Cereals and Grains ─────────────────────────────────────────────
    'hom-cereals-grains': [
      {
        h: "Structure of a cereal grain",
        b: "A grain has three parts. The bran is the tough multi-layered outer coat, rich in insoluble fibre, B vitamins and minerals. The endosperm is the bulk of the grain, almost entirely starch with some protein, and is the only part retained in white flour. The germ is the embryo, containing fat, protein, vitamin E and B vitamins, and is removed from white flour because its fat shortens shelf life."
      },
      {
        h: "Nutritional value",
        b: "Cereals are the world's main source of dietary energy, supplying starch, low biological value protein, B vitamins, iron and, in wholegrain form, substantial fibre. They are low in fat and contain no vitamin C, vitamin A or vitamin B12, and their protein is deficient in lysine, so they are complemented by pulses or by animal protein. Wholegrain versions retain far more fibre, vitamins and minerals than refined."
      },
      {
        h: "Wheat and flour",
        b: "Wheat is the most important cereal in the Irish diet because it alone forms gluten. Strong flour from hard wheat has a high protein content and suits bread and puff pastry; soft or plain flour suits cakes, biscuits and shortcrust. Extraction rate is the percentage of the grain retained: wholemeal is 100%, brown around 85%, and white about 70-72%. White and brown flour are fortified by law with calcium, iron, thiamine and niacin."
      },
      {
        h: "Gluten",
        b: "When the wheat proteins gliadin and glutenin are moistened and worked they combine to form gluten, an elastic and extensible network. Kneading develops it; it traps the carbon dioxide produced by yeast or chemical raising agents so the dough rises, then sets on baking to hold the risen structure. Fat, sugar and acid weaken gluten, which is why pastry is handled lightly and kept cool."
      },
      {
        h: "Other cereals",
        b: "Rice is the staple of much of the world and is gluten-free; brown rice retains the bran and germ. Oats are high in soluble beta-glucan fibre, which lowers cholesterol, and are used in porridge, oatcakes and baking. Maize supplies cornflour, polenta and breakfast cereals. Barley is used in soups, stews and malting. Rye makes dense dark breads."
      },
      {
        h: "Effects of cooking",
        b: "Moist heat gelatinises starch: the granules absorb water, swell and rupture, thickening liquids and making the starch digestible. Dry heat causes dextrinisation, giving toast and bread crust their colour and flavour. Cooking softens cellulose in bran, improving palatability. Some thiamine is lost to heat, and water-soluble B vitamins leach into cooking water."
      },
      {
        h: "Bread making",
        b: "Yeast bread relies on fermentation: yeast ferments sugars to carbon dioxide and alcohol, the gas is trapped by the gluten network, and the dough rises. Kneading develops gluten, proving allows the rise, and baking kills the yeast, sets the gluten, gelatinises starch and browns the crust. Soda bread instead uses bicarbonate of soda reacting with the acid in buttermilk, and needs no proving."
      },
      {
        h: "Breakfast cereals and processing",
        b: "Breakfast cereals are made by flaking, puffing, extruding or shredding grain, usually with added sugar and salt, and are commonly fortified with iron, folate and B vitamins. Nutritional value varies enormously: wholegrain, low-sugar, low-salt options with good fibre content are far preferable to heavily sweetened products, and labels should be compared per 100 g."
      },
      {
        h: "Coeliac disease",
        b: "Coeliac disease is an autoimmune condition in which gluten from wheat, barley and rye triggers an immune reaction that damages the villi of the small intestine, reducing absorption and causing weight loss, fatigue, anaemia and gastrointestinal symptoms. The only treatment is a lifelong strict gluten-free diet using rice, maize, potato, buckwheat, quinoa and certified gluten-free oats."
      },
      {
        h: "Storage",
        b: "Flour, rice and pasta are stored in cool, dry, airtight containers to keep out moisture, pests and odours, and stock is rotated so that older supplies are used first. Wholemeal flour and wheatgerm have a shorter shelf life because the fat in the germ turns rancid, so they are bought in smaller quantities and may be refrigerated."
      }
    ],

    // ── 11. Cooking Methods and Heat Transfer ──────────────────────────────
    'hom-cooking-methods': [
      {
        h: "Why food is cooked",
        b: "Cooking destroys pathogenic bacteria and parasites, making food safe. It makes food more digestible by gelatinising starch, softening fibre and connective tissue, and coagulating protein. It improves palatability through changes in colour, texture, flavour and aroma. It extends keeping quality by destroying enzymes and microorganisms, and provides variety in the diet."
      },
      {
        h: "Conduction",
        b: "Conduction is the transfer of heat through direct contact, as vibrating molecules pass energy to their neighbours. It heats the base of a saucepan on a hotplate, the frying pan and the food touching it, and moves heat inwards through a solid piece of food. Metals, particularly copper and aluminium, are good conductors; glass, ceramic and wood are poor, which is why handles are made from them."
      },
      {
        h: "Convection",
        b: "Convection transfers heat through the movement of currents in a liquid or gas. Heated fluid expands, becomes less dense and rises, while cooler fluid sinks to take its place, setting up a circulating current. It is the main mechanism in boiling water, deep-fat frying and conventional ovens, and fan ovens speed it by forcing the circulation, giving faster and more even cooking."
      },
      {
        h: "Radiation and microwaves",
        b: "Radiation transfers heat as infrared waves travelling in straight lines from a source without needing a medium, as under a grill, in a toaster or over a barbecue, and it cooks only the surface facing it. Microwaves are a different form of electromagnetic radiation: they penetrate the outer few centimetres and make water molecules vibrate rapidly, generating heat within the food itself, which is then conducted inwards."
      },
      {
        h: "Moist methods: boiling, simmering and poaching",
        b: "Boiling cooks food in liquid at 100°C and suits vegetables, pasta, rice and tough meat, but agitates delicate foods and leaches water-soluble vitamins and minerals. Simmering holds the liquid just below boiling with occasional bubbles, and is gentler. Poaching cooks in barely trembling liquid at around 80°C and suits eggs, fish and fruit. All three add no fat."
      },
      {
        h: "Steaming, stewing and braising",
        b: "Steaming cooks food in the vapour above boiling water, so nutrients are not leached into the liquid and texture and colour are well preserved. Stewing cooks small pieces of food slowly in a measured amount of liquid, all of which is served, so nothing is lost and tough cuts become tender. Braising combines the two: food is browned, then cooked slowly on a bed of vegetables with a little liquid in a covered dish."
      },
      {
        h: "Dry methods: grilling, roasting and baking",
        b: "Grilling uses radiant heat for quick cooking of tender cuts, and allows fat to drain away. Roasting cooks food in an oven with added fat, giving a browned surface and a moist interior. Baking cooks in dry oven heat without added fat and is used for bread, cakes, pastry and gratins. All three produce Maillard browning and dextrinisation, developing colour and flavour."
      },
      {
        h: "Frying",
        b: "Shallow frying cooks food in a small amount of hot fat in a pan; deep frying immerses it in fat at about 180°C, sealing the surface quickly so that little fat is absorbed if the temperature is correct. Fat that is too cool is absorbed and makes food greasy; fat that is too hot exceeds its smoke point and breaks down. Frying is quick and flavourful but raises the fat and energy content substantially."
      },
      {
        h: "Effect of cooking on nutrients",
        b: "Vitamin C and the B group are the most vulnerable, being destroyed by heat and leached into cooking water; steaming, microwaving and short cooking times minimise the loss. Protein coagulates and, if overcooked, becomes tough and less digestible. Starch gelatinises and becomes digestible. Minerals are heat-stable but can be lost into cooking liquid, so that liquid is best used in sauces and soups."
      },
      {
        h: "Choosing a method",
        b: "The method should suit the food, the nutritional aim and the occasion. Tender cuts and delicate foods take quick or gentle methods; tough cuts need long moist cooking. Steaming, grilling, poaching and baking add no fat and suit weight-reducing and low-cholesterol diets, while frying and roasting in fat add considerable energy. Time, cost, equipment and the number to be served all influence the choice."
      }
    ],

    // ── 12. Food Preservation and Storage ──────────────────────────────────
    'hom-food-preservation': [
      {
        h: "Why food spoils",
        b: "Food deteriorates through the action of bacteria, yeasts and moulds, through the food's own enzymes, and through chemical changes such as the oxidation of fats. Microorganisms need warmth, moisture, food and time, and most also need a near-neutral pH. Preservation works by removing one or more of these conditions, or by destroying the organisms and enzymes outright."
      },
      {
        h: "Principles of preservation",
        b: "There are five basic approaches: apply high temperature to destroy microorganisms and enzymes; apply low temperature to slow or stop their activity; remove water so they cannot function; increase acidity beyond their tolerance; and exclude air or add chemicals that inhibit them. Most commercial methods combine several — for instance heating and then sealing in an airtight can."
      },
      {
        h: "Freezing",
        b: "Freezing at -18°C or below stops microbial growth and greatly slows enzyme and chemical activity, though it does not kill bacteria, which revive on thawing. Fast freezing forms small ice crystals that do minimal damage to cell walls, so texture is better preserved than with slow freezing. Vegetables are blanched first to destroy enzymes that would otherwise cause loss of colour, flavour and vitamin C."
      },
      {
        h: "Chilling and controlled atmosphere",
        b: "Refrigeration at 0-5°C slows microbial growth and enzyme activity without stopping them, so it extends life by days rather than months. Modified atmosphere packaging replaces the air in a pack with a mixture low in oxygen and higher in carbon dioxide and nitrogen, slowing oxidation and the growth of aerobic spoilage organisms — widely used for meat, fish, salads and baked goods."
      },
      {
        h: "Heat treatment: canning and bottling",
        b: "Canning fills food into a container, seals it and heats it under pressure to a temperature high enough to destroy microorganisms and their spores, including Clostridium botulinum in low-acid foods. The sealed container prevents recontamination, giving a shelf life of years. Bottling applies the same principle domestically, most safely with high-acid foods such as fruit. Damaged, blown or rusted cans should never be used."
      },
      {
        h: "Dehydration",
        b: "Removing water leaves too little available moisture for microorganisms to grow. Traditional sun drying is used for fruit; modern methods include hot-air, spray and roller drying. Accelerated freeze drying freezes the food and then removes the ice directly as vapour under vacuum, giving a light, porous product that rehydrates rapidly with excellent retention of flavour, colour and nutrients — used for coffee and convenience meals."
      },
      {
        h: "Sugar and jam making",
        b: "A high sugar concentration binds water and makes it unavailable to microorganisms. A successful jam needs three things in balance: pectin to set the gel, acid to help release the pectin and prevent crystallisation, and sugar at about 60% of the final weight. Under-ripe fruit is higher in pectin and acid; low-pectin fruit is combined with lemon juice or commercial pectin."
      },
      {
        h: "Salting, smoking and pickling",
        b: "Salt draws water out of food and out of microbial cells by osmosis, and is used in curing bacon, ham and fish. Smoking dries the surface and deposits antimicrobial phenols and other compounds, and is usually combined with salting. Pickling in vinegar lowers the pH below the level at which most spoilage organisms can grow, and is used for vegetables, eggs and fish."
      },
      {
        h: "Chemical preservatives and irradiation",
        b: "Permitted chemical preservatives include sulphur dioxide and sulphites in dried fruit and wine, benzoates in soft drinks, nitrites in cured meats, and sorbates in baked goods; all are strictly regulated and must be declared on the label. Irradiation exposes food to controlled ionising radiation to kill microorganisms and inhibit sprouting; it is tightly regulated in the EU and must be labelled."
      },
      {
        h: "Home storage",
        b: "Perishables go into the refrigerator at 0-5°C with raw meat on the bottom shelf and cooked foods above; the freezer runs at -18°C. Dry goods are kept in cool, dry, airtight containers away from light, and stock is rotated so older items are used first. Date marks must be understood: use-by relates to safety and must be observed, while best-before relates to quality."
      }
    ],

    // ── 13. Food Safety and Microorganisms ─────────────────────────────────
    'hom-food-safety': [
      {
        h: "Conditions bacteria need",
        b: "Bacteria multiply when they have warmth, moisture, food and time, and most food-poisoning organisms also prefer a near-neutral pH and, in many cases, oxygen. The danger zone is 5-63°C, with the fastest growth around body temperature. Given ideal conditions a single bacterium can divide every ten to twenty minutes, so a small initial contamination becomes dangerous within hours."
      },
      {
        h: "High-risk foods",
        b: "High-risk foods are moist, high in protein and ready to eat without further cooking: cooked meat and poultry, gravies and stocks, dairy products, eggs and egg dishes, shellfish, cooked rice, pâté and prepared salads. These must be kept out of the danger zone, handled with scrupulous hygiene and used within their use-by date."
      },
      {
        h: "Salmonella and Campylobacter",
        b: "Salmonella is carried in raw poultry, eggs and meat, and causes fever, abdominal pain, vomiting and diarrhoea within 6-72 hours. Campylobacter is the most commonly reported cause of bacterial food poisoning in Ireland, associated mainly with raw poultry and unpasteurised milk, with a longer onset of two to five days. Both are destroyed by thorough cooking to a core temperature of 75°C."
      },
      {
        h: "Listeria and E. coli O157",
        b: "Listeria monocytogenes is unusual in growing at refrigeration temperatures, and is found in soft mould-ripened cheese, pâté, smoked fish and prepared salads; it is particularly dangerous in pregnancy, causing miscarriage and stillbirth. E. coli O157 comes from cattle and is associated with undercooked minced beef and unpasteurised milk; it produces toxins that can cause kidney failure, and the infectious dose is extremely small."
      },
      {
        h: "Toxin-producing bacteria",
        b: "Staphylococcus aureus lives in the nose, throat and on skin and infected cuts, and produces a heat-stable toxin that cooking will not destroy, causing rapid-onset vomiting. Clostridium perfringens forms spores that survive cooking and germinate in food left to cool slowly. Bacillus cereus is associated with cooked rice held warm. Clostridium botulinum grows in improperly canned low-acid foods and produces an often fatal neurotoxin."
      },
      {
        h: "Moulds, yeasts and enzymes",
        b: "Moulds are multicellular fungi that grow visibly on the surface of bread, cheese and fruit, spread by airborne spores, and some produce harmful mycotoxins, so mouldy food is discarded rather than trimmed. Yeasts ferment sugars and spoil fruit juices, jams and syrups. The food's own enzymes continue to act after harvest, causing ripening, softening and the enzymic browning of cut apples and potatoes."
      },
      {
        h: "Cross-contamination",
        b: "Cross-contamination is the transfer of harmful bacteria from raw food to ready-to-eat food, directly through contact or drips, or indirectly via hands, cloths, knives, boards and work surfaces. It is prevented by storing raw meat covered on the bottom shelf, using separate colour-coded boards and utensils, washing hands between tasks, and cleaning and sanitising surfaces and equipment."
      },
      {
        h: "Temperature control",
        b: "Cook food thoroughly to a core temperature of at least 75°C, and reheat only once to the same temperature. Keep hot food above 63°C until served. Cool leftovers quickly, within 90 minutes, in shallow containers, and refrigerate. Thaw frozen food fully in the refrigerator before cooking, and never refreeze thawed food. A probe thermometer is the only reliable check on core temperature."
      },
      {
        h: "Personal and kitchen hygiene",
        b: "Wash hands thoroughly with soap and warm water before handling food, after handling raw meat, after using the toilet, and after touching bins, pets or the face. Tie back hair, wear a clean apron, cover cuts with a waterproof dressing, and stay away from food preparation when suffering from vomiting or diarrhoea. Keep surfaces, equipment, cloths and bins clean, and control pests."
      },
      {
        h: "HACCP and food law",
        b: "Hazard Analysis and Critical Control Point is a preventive system, required of food businesses, that identifies hazards at each stage, determines the critical control points, sets limits and monitoring procedures, specifies corrective action and keeps records. The Food Safety Authority of Ireland enforces food law, coordinates official inspection, issues closure orders and food alerts, and provides guidance to consumers and industry."
      }
    ],

    // ── 14. Meal Planning and Special Diets ────────────────────────────────
    'hom-meal-planning': [
      {
        h: "Factors affecting meal planning",
        b: "Meals must meet the nutritional needs of those eating them, and be planned around the money available, the time and skill of the cook, the equipment and fuel to hand, the season and availability of foods, personal likes and dislikes, cultural and religious requirements, medical needs, and the occasion. Good planning also reduces waste and shopping costs."
      },
      {
        h: "Principles of a well-planned meal",
        b: "A well-planned meal is nutritionally balanced across the food groups, and offers variety in colour, texture, flavour, shape and cooking method so that it is appetising as well as adequate. Courses should complement rather than repeat one another — a rich main course follows a light starter — and the meal should suit the time of day, the weather and the appetite of those eating."
      },
      {
        h: "Planning for infants and young children",
        b: "Breast milk or infant formula is the sole food for the first six months, after which weaning introduces smooth, single-ingredient purées, progressing to lumpier textures and finger foods. Salt, sugar, honey before one year, whole nuts and low-fat products are avoided. Toddlers need small frequent nutrient-dense meals, full-fat milk to age two, and iron- and calcium-rich foods for rapid growth."
      },
      {
        h: "Planning for adolescents and adults",
        b: "Adolescents have high energy, protein, calcium and iron needs during the growth spurt, and girls need extra iron once menstruation begins; regular meals and healthy snacks matter, as this is when lifelong habits form. Adults need a maintenance diet with attention to portion size, saturated fat, salt, free sugars and fibre, and enough calcium and vitamin D to preserve bone density."
      },
      {
        h: "Planning for older adults",
        b: "Energy needs fall with reduced activity and muscle mass, but requirements for protein, calcium, vitamin D, vitamin B12, iron and fibre remain high or rise, so foods must be nutrient-dense. Appetite, dentition, taste, mobility, isolation and a limited budget can all restrict intake. Small frequent meals, easy-to-chew textures, adequate fluid and vitamin D supplementation are commonly needed."
      },
      {
        h: "Coeliac disease and lactose intolerance",
        b: "Coeliac disease requires the lifelong exclusion of wheat, barley and rye, replacing them with rice, maize, potato, buckwheat and certified gluten-free oats, and checking labels for hidden gluten in sauces, soups and processed foods. Lactose intolerance results from insufficient lactase; it is managed with lactose-free or plant-based milks, hard cheeses and live yogurt, which are better tolerated, while ensuring calcium intake is maintained."
      },
      {
        h: "Diabetes",
        b: "In type 1 diabetes the pancreas produces no insulin and treatment is by injection matched to carbohydrate intake; in type 2 the body becomes resistant to insulin, and it is strongly associated with overweight and inactivity. Dietary management centres on regular meals, high-fibre low-glycaemic carbohydrates, limited free sugars and saturated fat, weight control and physical activity."
      },
      {
        h: "Coronary heart disease and hypertension",
        b: "A cardio-protective diet reduces saturated and trans fat, replacing them with monounsaturated and polyunsaturated fats; increases oily fish, fruit, vegetables and soluble fibre from oats and pulses; and limits salt to under 6 g a day to control blood pressure. Grilling, steaming and baking replace frying, and weight control, exercise and stopping smoking are equally important."
      },
      {
        h: "Vegetarian and vegan diets",
        b: "Lacto-ovo vegetarians exclude meat and fish but eat dairy and eggs; vegans exclude all animal products. Both need careful planning for protein, using complementary combinations of cereals and pulses, and for iron and zinc, which are less well absorbed from plants — vitamin C at the meal improves uptake. Vegans additionally need reliable sources of vitamin B12, calcium, vitamin D and omega-3, usually from fortified foods or supplements."
      },
      {
        h: "Food allergy and intolerance",
        b: "A food allergy is an immune response that can be immediate and severe, up to anaphylaxis, while an intolerance is a non-immune reaction that is unpleasant but not life-threatening. EU law requires fourteen named allergens — including peanuts, tree nuts, milk, eggs, fish, crustaceans, molluscs, soya, cereals containing gluten, celery, mustard, sesame, lupin and sulphites — to be emphasised on labels and declared on unpackaged food."
      }
    ],

    // ── 15. Food Additives and Processing ──────────────────────────────────
    'hom-food-additives': [
      {
        h: "What additives are and why they are used",
        b: "A food additive is a substance added intentionally to food to perform a technological function — to preserve it, to improve or maintain its colour, flavour, texture or appearance, or to help it be processed. Additives are not used to disguise faulty ingredients or poor processing, and their use is permitted only where a genuine technological need is demonstrated."
      },
      {
        h: "Regulation and E numbers",
        b: "An additive may only be used if it has been assessed as safe by the European Food Safety Authority and authorised for that food at that level. Authorised additives are given an E number, which shows they have passed EU safety evaluation. Labels must list additives by function and then by name or E number, and acceptable daily intakes are set with a wide safety margin."
      },
      {
        h: "Colourings",
        b: "Colourings restore colour lost in processing, reinforce colour already present, or add colour to products such as soft drinks and confectionery. They may be natural, such as caramel, beta-carotene and beetroot red, or synthetic. Certain azo dyes must carry a warning that they may have an adverse effect on activity and attention in children, which has driven a move to natural alternatives."
      },
      {
        h: "Flavourings and flavour enhancers",
        b: "Flavourings restore or add flavour and may be natural, nature-identical or artificial. Flavour enhancers have little taste of their own but intensify the existing flavour of a food; the best known is monosodium glutamate, used in savoury products, soups and snacks. Sweeteners such as aspartame, saccharin and sucralose provide sweetness with negligible energy and are used in reduced-sugar products."
      },
      {
        h: "Preservatives and antioxidants",
        b: "Preservatives inhibit the growth of microorganisms and extend shelf life — nitrites in cured meats, which also fix the pink colour and inhibit Clostridium botulinum; sulphur dioxide in dried fruit and wine; benzoates in soft drinks. Antioxidants delay the oxidation of fats that causes rancidity and of cut surfaces that causes browning; ascorbic acid, tocopherols, BHA and BHT are common examples."
      },
      {
        h: "Emulsifiers, stabilisers and thickeners",
        b: "Emulsifiers allow oil and water to mix and remain mixed, as lecithin does in chocolate, margarine and mayonnaise. Stabilisers maintain that mixture over time and prevent separation. Thickeners and gelling agents such as pectin, carrageenan, guar gum and modified starch give body and set to sauces, desserts, yogurts and low-fat spreads."
      },
      {
        h: "Other functional additives",
        b: "Anti-caking agents keep powders such as salt and dried milk free-flowing. Humectants retain moisture in cakes and confectionery. Raising agents produce gas to aerate baked goods. Acids and acidity regulators control pH for safety, set and flavour. Glazing agents give a shiny protective coating to confectionery and fruit."
      },
      {
        h: "Advantages and disadvantages",
        b: "Additives extend shelf life and so reduce food waste, improve safety, allow a wide year-round variety of convenience foods, and can maintain or improve nutritional value through fortification. Against that, they may be used to make highly processed products more attractive than their nutritional value merits, a minority of people react adversely to particular additives, and long-term effects of combinations are hard to assess."
      },
      {
        h: "Levels of food processing",
        b: "Primary processing converts a raw commodity into an edible ingredient — milling wheat into flour, pasteurising milk, butchering a carcass. Secondary processing turns those ingredients into products such as bread, cheese or ready meals. Minimally processed foods retain most of their original nutritional character, while ultra-processed products typically carry more added fat, sugar, salt and additives and less fibre."
      },
      {
        h: "Effects of processing on nutritional value",
        b: "Processing can reduce nutrients — milling removes bran and germ, heat destroys vitamin C and thiamine, and water-soluble vitamins leach into cooking and canning liquid. It can also improve them, by fortifying flour with calcium, iron, thiamine and niacin, adding vitamin D to spreads, and making some nutrients more available. Careful choice of processed foods, using labels, matters more than avoiding them altogether."
      }
    ],

    // ── 16. Consumer Rights and Protection ─────────────────────────────────
    'hom-consumer-rights': [
      {
        h: "Who a consumer is",
        b: "A consumer is a person who buys goods or services for their own personal use rather than for resale or for use in a business. That status is what brings the protection of consumer law: a person buying in the course of a business generally has fewer statutory rights, since the law assumes greater bargaining power and expertise."
      },
      {
        h: "Consumer rights and responsibilities",
        b: "Consumers have the right to safety, to honest information, to choice, to value for money, to be heard and to redress when something goes wrong. With those come responsibilities: to be informed before buying, to compare price and quality, to read and follow instructions and care labels, to use goods for their intended purpose, to keep receipts, and to complain promptly and reasonably."
      },
      {
        h: "The Sale of Goods and Supply of Services Act 1980",
        b: "This is the central piece of Irish consumer legislation. Goods must be of merchantable quality, fit for the purpose intended, as described, and must match any sample or model shown. Services must be supplied by a person with the necessary skill, with proper care and diligence, using materials that are sound and goods that are of merchantable quality. These conditions cannot be signed away by the seller."
      },
      {
        h: "Redress and the seller's liability",
        b: "Where goods are faulty the consumer's contract is with the retailer, not the manufacturer, so it is the retailer who must provide redress — repair, replacement or refund. Signs such as 'no refunds' or 'no exchanges' are void where the goods are faulty. A consumer who simply changes their mind has no automatic legal right to a refund, though many shops offer one as a matter of policy."
      },
      {
        h: "Consumer information and protection legislation",
        b: "The Consumer Information Act 1978 made it an offence to give false or misleading descriptions of goods, services or prices. The Consumer Protection Act 2007 replaced and extended it, prohibiting misleading and aggressive commercial practices and establishing the National Consumer Agency. The Consumer Credit Act 1995 regulates credit agreements, requiring clear disclosure of the APR and the total cost of credit."
      },
      {
        h: "The CCPC",
        b: "The Competition and Consumer Protection Commission enforces consumer law and competition law in Ireland. It investigates breaches and can prosecute, provides independent information on personal finance and consumer rights, runs price comparison and awareness campaigns, and advises government on consumer policy. It does not, however, resolve individual disputes on a consumer's behalf."
      },
      {
        h: "Making a complaint",
        b: "The consumer should act promptly, return to the place of purchase with proof of purchase, state clearly what is wrong and what redress is sought, and remain calm and factual. If the shop assistant cannot resolve it, the matter goes to the manager, then in writing to head office, keeping copies of all correspondence. Only then are outside bodies approached."
      },
      {
        h: "The Small Claims procedure",
        b: "The Small Claims procedure offers a cheap, quick and informal way to pursue consumer claims up to €2,000 without a solicitor. The consumer applies through the District Court office for a modest fee, and the Registrar attempts to negotiate a settlement; if none is reached, the case is heard by a judge. It covers faulty goods, poor services and minor property damage, but not debt or personal injury."
      },
      {
        h: "Ombudsman schemes and regulators",
        b: "Where a complaint concerns a body with its own scheme, an ombudsman may investigate free of charge: the Financial Services and Pensions Ombudsman for banks, insurers and pension providers, the Ombudsman for public bodies, and ComReg for telecommunications. The Advertising Standards Authority for Ireland handles complaints that advertising is not legal, decent, honest and truthful."
      },
      {
        h: "Labelling and buying online",
        b: "Food labels must state the name, ingredients in descending order of weight with allergens emphasised, quantity, date mark, storage and use instructions, name and address of the manufacturer or seller, country of origin where required, and nutrition information. When buying online from an EU trader, consumers generally have a fourteen-day cooling-off period to cancel and return goods, with certain exceptions such as personalised items and perishables."
      }
    ],

    // ── 17. Personal Finance and Budgeting ─────────────────────────────────
    'hom-personal-finance': [
      {
        h: "Income: gross and net",
        b: "Gross income is total earnings before any deductions; net or take-home pay is what remains after them. Statutory deductions are PAYE income tax, Universal Social Charge and PRSI. Voluntary deductions may include pension contributions, health insurance, union subscriptions and savings. A payslip must show gross pay, each deduction and net pay, and should be checked and kept."
      },
      {
        h: "Income tax and credits",
        b: "PAYE operates by deducting tax at source. Income up to the standard rate cut-off point is taxed at the standard rate and the balance at the higher rate. Tax credits are then subtracted directly from the tax due, reducing the bill euro for euro — the personal credit and the employee credit being the most common. PRSI builds entitlement to social insurance benefits such as illness, jobseeker's and state pension."
      },
      {
        h: "Household budgeting",
        b: "A budget is a plan that matches expected income to planned spending over a period. It begins by recording net income, then listing fixed expenditure such as rent or mortgage, insurance and loan repayments; irregular expenditure such as electricity, heating and school costs; and discretionary spending. Planned saving is treated as a commitment, not a leftover, and the budget is reviewed against actual spending."
      },
      {
        h: "Why budgets fail",
        b: "Common causes are underestimating irregular bills, forgetting annual costs such as insurance or car tax, impulse buying, using credit to bridge shortfalls, and having no contingency for emergencies. Remedies include keeping a spending diary, setting realistic targets, paying large bills by monthly direct debit, building an emergency fund of a few months' expenditure, and reviewing the budget regularly."
      },
      {
        h: "Saving and investment",
        b: "Saving sets money aside for short-term goals and emergencies, with security and easy access the priority — deposit accounts, credit union shares, and State Savings products. Investment aims at longer-term growth and accepts more risk in exchange for potentially higher return — shares, funds, property, pensions. The key considerations are risk, return, liquidity, term and the effect of inflation and of DIRT on interest."
      },
      {
        h: "Sources of credit",
        b: "Credit union loans are generally low-cost, with interest charged on the reducing balance and no penalty for early repayment. Bank personal loans suit larger fixed purchases. Overdrafts cover short-term shortfalls but are expensive if used continuously. Hire purchase spreads the cost of goods but ownership passes only with the final payment. Credit cards and moneylenders carry the highest rates."
      },
      {
        h: "Understanding the cost of credit",
        b: "The Annual Percentage Rate expresses the full cost of borrowing over a year, including interest and compulsory charges, and is the only reliable basis for comparing offers. The total cost of credit is the difference between the amount borrowed and the total repaid. Longer terms lower the monthly repayment but raise the total cost. Borrowers should check for arrangement fees, penalties and payment protection insurance."
      },
      {
        h: "Mortgages",
        b: "A mortgage is a long-term loan secured on the property, so the lender can repossess if repayments are not met. Lending is limited by loan-to-value and loan-to-income rules, with a deposit required. Repayment mortgages clear capital and interest over the term; interest-only mortgages do not reduce the capital. Fixed rates give certainty, variable rates move with the market, and a tracker follows the ECB rate."
      },
      {
        h: "Insurance",
        b: "Insurance transfers risk to an insurer in return for a premium, and operates on the principle of indemnity — restoring the insured to their previous position, not providing profit. Common types are home buildings and contents, motor, which is compulsory at least to third-party level, health, travel, life assurance and income protection. Non-disclosure of material facts can invalidate a policy."
      },
      {
        h: "Financial services and consumer protection",
        b: "Current accounts, debit cards, direct debits and standing orders, online and mobile banking handle day-to-day money management. Providers are regulated by the Central Bank of Ireland and must follow the Consumer Protection Code. The Financial Services and Pensions Ombudsman investigates unresolved complaints free of charge, and MABS provides free, confidential money advice to people in debt."
      }
    ],

    // ── 18. Housing and Accommodation ──────────────────────────────────────
    'hom-housing': [
      {
        h: "Functions of the home and housing needs",
        b: "A home provides shelter and security, a setting for family life and the rearing of children, privacy, rest and recreation, a base for work and storage of possessions, and a means of expressing identity. Housing needs change over the life cycle, from single-person or shared accommodation, to family housing with space and access to schools, to smaller, accessible, low-maintenance homes in later life."
      },
      {
        h: "Types of accommodation and tenure",
        b: "Housing types include detached, semi-detached and terraced houses, bungalows, dormer bungalows, apartments and duplexes. Tenure may be owner-occupied, whether purchased outright or by mortgage; private rented, governed by a tenancy agreement and registered with the Residential Tenancies Board; local authority or social housing; approved housing body accommodation; or shared-ownership and affordable purchase schemes."
      },
      {
        h: "Choosing a location",
        b: "Location is assessed on proximity to work, schools, shops, healthcare, public transport and recreation; the character, safety and services of the neighbourhood; aspect and orientation for daylight and solar gain; the risk of flooding, noise or pollution; the cost of the site and of local property; and future development plans for the area, which can be checked in the local authority development plan."
      },
      {
        h: "Planning permission",
        b: "Planning permission must be obtained from the local authority before building a new house, making significant alterations or changing the use of a building. The application includes site location and layout maps, detailed plans and elevations, and is publicly notified by newspaper notice and site notice so that observations can be made. Decisions may be appealed to An Bord Pleanála. Certain minor works are exempted development."
      },
      {
        h: "Building regulations and standards",
        b: "The Building Regulations set minimum standards for the design and construction of buildings, covering structural stability, fire safety, means of escape, ventilation, drainage, heating, conservation of fuel and energy, sound insulation and access for people with disabilities. Compliance is certified by the designer and builder, and works are subject to inspection."
      },
      {
        h: "Buying a home",
        b: "The process runs from establishing a budget and obtaining mortgage approval in principle, through searching and viewing, making an offer, paying a booking deposit, commissioning a structural survey and a valuation, engaging a solicitor to check title and carry out searches, signing contracts and paying the contract deposit, to drawdown of the loan and closing. Costs include stamp duty, legal and survey fees and mortgage protection insurance."
      },
      {
        h: "Renting",
        b: "A tenancy should be set out in a written agreement stating rent, term, deposit, notice periods and responsibility for bills and repairs. Landlords must register the tenancy with the Residential Tenancies Board, provide a rent book and a BER certificate, maintain the structure and appliances, and observe minimum standards. Tenants must pay rent, avoid damage beyond fair wear and tear and give proper notice. Disputes go to the RTB."
      },
      {
        h: "Energy efficiency and the BER",
        b: "The Building Energy Rating certificate grades a home from A to G on its energy performance and must be provided when a property is sold or let. Efficiency is improved by attic and wall insulation, draught-proofing, double or triple glazing, an efficient boiler or heat pump, zoned heating with thermostats and timers, LED lighting, and solar thermal or photovoltaic panels. SEAI administers grants for many of these measures."
      },
      {
        h: "Heating and services",
        b: "Heating systems include gas, oil and solid fuel central heating, electric storage heating, heat pumps and solid fuel stoves, distributed by radiators or underfloor pipes. A home also requires a safe electrical installation, a water supply from the mains or a well, wastewater treatment by mains sewer or septic tank, and adequate ventilation to control condensation and indoor air quality."
      },
      {
        h: "Home safety and security",
        b: "Common hazards are falls, fire, burns and scalds, poisoning and electrical accidents, with young children and older people most at risk. Precautions include smoke and carbon monoxide alarms, a fire blanket and extinguisher, an escape plan, stair gates, secure storage of medicines and chemicals, RCD protection on electrical circuits, and good lighting. Security measures include quality locks, alarms, exterior lighting and neighbourhood watch."
      }
    ],

    // ── 19. Textiles and Fabric Properties ─────────────────────────────────
    'hom-textiles-fibres': [
      {
        h: "Classification of fibres",
        b: "Fibres are either natural or manufactured. Natural fibres come from plants (cellulosic — cotton, linen) or animals (protein — wool, silk). Manufactured fibres divide into regenerated fibres, made by chemically treating natural cellulose (viscose, modal, acetate, lyocell), and synthetic fibres, built from petrochemicals (polyester, polyamide, acrylic, elastane)."
      },
      {
        h: "Cotton and linen",
        b: "Cotton comes from the seed boll of the cotton plant. It is absorbent, cool, strong when wet, hard-wearing, washes and boils well and takes dye readily, but creases badly, shrinks and burns easily. Linen comes from the flax stem; it is the strongest natural fibre, highly absorbent, cool and lint-free with a characteristic lustre, but creases severely and is expensive."
      },
      {
        h: "Wool and silk",
        b: "Wool fibres are crimped and covered in overlapping scales, trapping air so that wool is warm, resilient and crease-resistant, absorbent without feeling wet, and naturally flame-resistant. It felts and shrinks with heat, moisture and agitation, and is weakened when wet. Silk, from the cocoon of the silkworm, is the strongest natural fibre, smooth, lustrous, absorbent and drapes beautifully, but is damaged by sunlight and perspiration."
      },
      {
        h: "Regenerated fibres",
        b: "Viscose is made from wood pulp; it is soft, absorbent, drapes well and dyes easily, but is weak when wet and creases. Modal is a stronger, more stable version. Lyocell is produced in a closed-loop solvent process with much lower environmental impact, and is strong, absorbent and biodegradable. Acetate is lustrous and drapes well but is heat-sensitive and weak."
      },
      {
        h: "Synthetic fibres",
        b: "Polyester is strong, crease-resistant, quick-drying, dimensionally stable and cheap, but non-absorbent, prone to static and pilling, and it melts. Polyamide (nylon) is exceptionally strong, elastic and abrasion-resistant. Acrylic is soft, bulky and warm, a wool substitute. Elastane (Lycra) has extraordinary stretch and recovery and is blended in small proportions for fit and comfort."
      },
      {
        h: "Fibre properties",
        b: "The properties that matter in selection are absorbency, which governs comfort and dyeing; strength, both dry and wet; elasticity and resilience, which determine crease recovery and fit; thermal insulation; abrasion resistance and durability; dimensional stability and shrink resistance; flammability; and reaction to sunlight, perspiration, moths and micro-organisms."
      },
      {
        h: "Yarns and blends",
        b: "Fibres are spun into yarns, either from short staple fibres or from continuous filament. Blending combines fibres to obtain the best of each and offset weaknesses: polycotton adds the crease resistance, strength and quick drying of polyester to the absorbency and comfort of cotton; wool blended with polyamide gains abrasion resistance; elastane adds stretch to almost anything."
      },
      {
        h: "Weaving",
        b: "Woven fabric is made by interlacing warp yarns running the length of the fabric with weft yarns running across it. Plain weave, a simple over-and-under, is firm, hard-wearing and cheap. Twill weave produces a diagonal rib and is strong and drapes well, as in denim. Satin weave floats long yarns on the surface for lustre and smoothness but snags easily."
      },
      {
        h: "Knitting and non-wovens",
        b: "Knitted fabric is made from interlocking loops, which gives it natural stretch, softness and crease resistance, but also a tendency to lose shape and to ladder; weft knits unravel across, warp knits are more stable. Non-woven fabrics are made by bonding or felting fibres together without spinning or weaving, and are used for interfacings, wipes and disposable items."
      },
      {
        h: "Finishes",
        b: "Finishes are applied to improve appearance or performance: mercerising for lustre and dye uptake in cotton; sanforising to prevent shrinkage; crease-resist and easy-care finishes; water-repellent and waterproof coatings; flame-retardant treatments, required for children's nightwear; stain-resistant and antistatic finishes; and moth-proofing and antibacterial treatments. Some finishes wash out over time."
      }
    ],

    // ── 20. Clothing Selection and Care ────────────────────────────────────
    'hom-clothing-selection': [
      {
        h: "Factors in choosing clothing",
        b: "Clothing is chosen for its purpose and the activity it must suit; for comfort, fit and freedom of movement; for the climate and season; for durability and ease of care; for cost and value for money; for the wearer's age, occupation, colouring and body shape; and for personal taste and current fashion. Safety matters where the wearer is a child or the setting is hazardous."
      },
      {
        h: "Fibre choice for purpose",
        b: "Sportswear needs elastane for stretch and polyester or polyamide to wick moisture and dry quickly. Underwear and summer clothing need absorbent, cool cotton. Winter outerwear needs wool or insulated synthetics with a water-repellent finish. Workwear needs abrasion resistance and easy care. Children's nightwear must meet flammability standards. Knowing fibre properties is what makes selection rational rather than guesswork."
      },
      {
        h: "Quality indicators",
        b: "Well-made garments have generous seam allowances that are neatened, even stitching with secure ends, seams and hems that lie flat, matched patterns at seams, smooth-lying zips, securely attached buttons with well-finished buttonholes, appropriate interfacing at collars and cuffs, and grain lines that hang straight. Linings, reinforced stress points and spare buttons indicate care in manufacture."
      },
      {
        h: "Care labelling",
        b: "Care labels use international symbols: a wash tub with a temperature or a hand for washing, with a bar underneath indicating a reduced or delicate action and a cross meaning do not wash; a triangle for bleaching; a square with a circle for tumble drying, dots indicating heat; an iron with dots for ironing temperature; and a circle with a letter for professional dry cleaning. A cross through any symbol prohibits that treatment."
      },
      {
        h: "Sorting and preparing the wash",
        b: "Garments are sorted by colour to prevent dye transfer, by fabric type and care instruction, and by degree of soiling. Pockets are emptied, zips closed, delicate items placed in mesh bags, and heavy soiling and stains treated first. Loads are not overpacked, since fabrics need room to move for detergent and water to circulate."
      },
      {
        h: "Detergents and how they work",
        b: "Detergents contain surfactants, whose molecules have a water-loving head and an oil-loving tail; they lower surface tension, lift grease from fibres and hold it suspended in the water until it is rinsed away. Builders soften water so the surfactant can work; enzymes break down protein, starch and fat stains at low temperatures; optical brighteners and bleaches improve whiteness; fabric conditioners coat fibres to soften and reduce static."
      },
      {
        h: "Washing and drying",
        b: "Water temperature is chosen for the fabric and the soiling: cool for wool, silk and bright colours, warm for synthetics and most coloureds, hot for heavily soiled cottons and household linen. Lower temperatures save energy and protect colour and shape. Drying flat suits knitwear that would stretch; line drying is cheap and freshens fabric; tumble drying is convenient but uses energy and can shrink or damage fibres."
      },
      {
        h: "Stain removal",
        b: "Stains are treated as soon as possible, working from the back of the fabric outwards to avoid spreading, and testing any treatment on a hidden area first. Protein stains such as blood, egg and milk are sponged with cold water first, as heat sets them. Grease responds to detergent or solvent, tannin stains such as tea and wine to prompt flushing with cold water, and dye stains often need specialist treatment."
      },
      {
        h: "Ironing, storage and repair",
        b: "Ironing temperature must match the fibre, testing on a seam or hidden area, and using a damp cloth for wool and a cool iron on synthetics, which melt. Clothes are stored clean and dry, hung on suitable hangers or folded to avoid stretching, in a cool, dry, well-ventilated space, with wool protected from moths. Prompt repair of loose buttons, small tears and hems extends garment life considerably."
      },
      {
        h: "Sustainable clothing choices",
        b: "Fast fashion generates large volumes of textile waste, high water and chemical use, and microplastic shedding from synthetics. More sustainable practice means buying fewer, better-made garments, choosing durable and repairable items, favouring organic, recycled or certified fibres, washing at lower temperatures and less often, repairing and altering, and passing on or recycling clothing rather than sending it to landfill."
      }
    ],

    // ── 21. Environmental Issues and Sustainability ────────────────────────
    'hom-environmental-issues': [
      {
        h: "Sustainable development",
        b: "Sustainable development meets the needs of the present without compromising the ability of future generations to meet their own needs. It balances three dimensions — environmental protection, economic viability and social equity — and applies at household level through the choices made about energy, water, food, transport, purchasing and waste."
      },
      {
        h: "The waste hierarchy",
        b: "The waste hierarchy ranks actions by preference: prevent waste arising in the first place; reduce the quantity used; reuse items for the same or another purpose; recycle materials into new products; recover energy from what remains; and dispose to landfill only as a last resort. Prevention and reduction deliver by far the greatest environmental benefit, since they avoid the resource use entirely."
      },
      {
        h: "Household waste management in Ireland",
        b: "Domestic waste is separated at source into three streams: a general waste bin for residual material, a mixed dry recyclables bin for clean, dry paper, cardboard, rigid plastics, and metal cans and tins, and a brown bin for food and garden waste. Contamination of the recycling bin can cause a whole load to be rejected, so items must be clean, dry and loose."
      },
      {
        h: "Composting and food waste",
        b: "Composting converts food and garden waste into a soil conditioner through the action of microorganisms, worms and insects, needing a balance of green nitrogen-rich material and brown carbon-rich material, along with air and moisture. It diverts waste from landfill, where it would generate methane, and returns nutrients to the soil. Reducing food waste through planning, correct storage and using leftovers is more effective still."
      },
      {
        h: "Energy conservation in the home",
        b: "Energy use is reduced by insulating the attic and walls, draught-proofing, upgrading glazing, and installing an efficient boiler or heat pump; by zoning and timing heating and setting thermostats a degree or two lower; by using LED lighting; by choosing appliances with a high energy label rating and running full loads at low temperatures; and by switching off standby. This cuts both bills and carbon emissions."
      },
      {
        h: "Water conservation",
        b: "Treating and pumping water uses significant energy, and supply is not unlimited. Consumption is reduced by fixing dripping taps and leaks promptly, taking shorter showers rather than baths, installing dual-flush cisterns and low-flow showerheads and taps, running washing machines and dishwashers only when full, and collecting rainwater in a butt for the garden."
      },
      {
        h: "Climate change and the carbon footprint",
        b: "Greenhouse gases, principally carbon dioxide and methane, trap heat in the atmosphere, and their concentration has risen sharply through the burning of fossil fuels, intensive agriculture and land-use change. A carbon footprint is the total greenhouse gas emissions attributable to a person or activity. Household emissions are dominated by home heating, private car use, and diet, particularly the consumption of ruminant meat and dairy."
      },
      {
        h: "Food miles and sustainable eating",
        b: "Food miles measure the distance food travels from producer to consumer; long-distance air-freighted produce carries a high transport footprint. But transport is only part of the picture, and production method often matters more than distance. Sustainable eating means choosing seasonal and local produce where sensible, reducing meat and dairy, avoiding overfished species, minimising packaging and, above all, wasting less."
      },
      {
        h: "Packaging and plastics",
        b: "Packaging protects food, extends shelf life and carries legally required information, but generates large volumes of waste. Plastics persist in the environment for centuries and break down into microplastics that enter food chains. Measures include producer responsibility schemes such as Repak, deposit and return schemes for containers, levies on single-use items, and choosing loose produce, refills and reusable containers and bags."
      },
      {
        h: "Pollution and its control",
        b: "Air pollution comes from vehicle exhausts, solid fuel burning and industry, and causes respiratory disease; smoky fuel restrictions and cleaner transport address it. Water pollution arises from sewage, agricultural run-off of nitrates and phosphates, which causes eutrophication, and industrial discharge. Noise and light pollution affect wellbeing and wildlife. The Environmental Protection Agency licenses and monitors major emissions in Ireland."
      }
    ],

    // ── 22. Household Appliances and Equipment ─────────────────────────────
    'hom-appliances-equipment': [
      {
        h: "Choosing an appliance",
        b: "Selection considers the needs of the household and how often the appliance will be used; the purchase price against running costs over its lifetime; energy and water efficiency; capacity and the space available, including door clearance and services; ease of use, cleaning and maintenance; safety marks and standards; the guarantee and availability of servicing and spare parts; and the reputation of the brand and retailer."
      },
      {
        h: "The EU energy label",
        b: "The energy label rates appliances on a scale from A to G, with A the most efficient, and states annual energy consumption in kilowatt hours along with capacity, water use, noise level and other model-specific information. Because running costs accumulate over many years, a more efficient model often costs less overall despite a higher purchase price. The label allows models to be compared directly."
      },
      {
        h: "The refrigerator",
        b: "A refrigerator removes heat from its interior by circulating a refrigerant that evaporates and absorbs heat inside, then is compressed and condenses, releasing heat at the rear coils. It should run at 0-5°C, be sited away from cookers and direct sunlight with space for air to circulate, never be overloaded, and have warm food cooled before storing. Regular defrosting and cleaning maintain efficiency."
      },
      {
        h: "The freezer",
        b: "A freezer operates at -18°C or below, at which microbial growth stops. Star ratings indicate storage capability, with four stars denoting the ability to freeze fresh food as well as store frozen food. Chest freezers are more efficient because cold air does not spill out when opened; upright models are easier to organise. Food is labelled and dated, stock rotated, and the appliance kept reasonably full for efficiency."
      },
      {
        h: "Cookers and hobs",
        b: "Gas hobs give instant, visible and responsive heat. Electric radiant and solid plates are slower to respond. Ceramic hobs are easy to clean but retain heat. Induction hobs generate heat directly in ferrous cookware by electromagnetism, making them the fastest, most controllable and most efficient, with a cool surface, though they require compatible pans. Ovens may be conventional, fan-assisted or multifunction."
      },
      {
        h: "The microwave oven",
        b: "A magnetron generates microwaves that are distributed within the cavity and absorbed by water, fat and sugar molecules in the food, making them vibrate and generate heat directly, with conduction carrying it further in. It is fast, energy-efficient and retains water-soluble vitamins well, but does not brown food unless combined with a grill, and heats unevenly, so food must be stirred, turned and allowed to stand."
      },
      {
        h: "The washing machine",
        b: "An automatic washing machine fills to a set level, heats water to the selected temperature, and rotates the drum so that clothes are lifted and dropped through the detergent solution. It then rinses several times and spins at high speed to extract water by centrifugal force. Efficiency is improved by washing full loads at lower temperatures, dosing detergent correctly and cleaning the filter and detergent drawer."
      },
      {
        h: "The dishwasher",
        b: "A dishwasher sprays heated detergent solution from rotating arms onto the load, then rinses and dries using residual heat or a fan. It generally uses less water than washing the same load by hand, provided it is run full and on an eco programme. Salt maintains the water softener and rinse aid prevents streaking. Items are loaded so that soiled surfaces face the spray and nothing blocks the arms."
      },
      {
        h: "Small appliances and kitchen equipment",
        b: "Small electrical appliances — kettle, toaster, food processor, blender, hand mixer, slow cooker, air fryer — save time and effort for specific tasks, but take storage space and add cost, so they are worth buying only if genuinely used. Basic equipment includes good knives, chopping boards, weighing scales, measuring jugs, saucepans with heavy bases, and ovenproof dishes."
      },
      {
        h: "Safety, maintenance and consumer rights",
        b: "Appliances should carry a recognised safety mark, be installed according to instructions by a competent person where wiring, gas or plumbing is involved, and be kept away from water. Flexes are checked for damage, appliances are not overloaded on adaptors, and instructions are followed and kept. Regular cleaning and servicing extend life. Faulty appliances are covered by the Sale of Goods and Supply of Services Act 1980, and the guarantee is additional to those statutory rights, not a replacement for them."
      }
    ]
  };

  [
    'hom-carbohydrates', 'hom-proteins', 'hom-lipids', 'hom-vitamins-minerals',
    'hom-digestion-metabolism', 'hom-energy-nutrition', 'hom-meat-preparation',
    'hom-fish-seafood', 'hom-dairy-eggs', 'hom-cereals-grains', 'hom-cooking-methods',
    'hom-food-preservation', 'hom-food-safety', 'hom-meal-planning', 'hom-food-additives',
    'hom-consumer-rights', 'hom-personal-finance', 'hom-housing', 'hom-textiles-fibres',
    'hom-clothing-selection', 'hom-environmental-issues', 'hom-appliances-equipment',
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
