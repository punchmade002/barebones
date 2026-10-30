// Test builder — turns a scope (one or more chapters) and a time budget into a
// mixed test of flashcard recall and past-paper exam questions.
// Pure logic, no DOM: app.js gathers the data, calls build/assemble, and renders.
(function (root) {
  // Seconds a student needs per item. Exam parts are timed from the paper's
  // own marks-per-minute rate (EXAM_BREAKDOWN), so they match the real exam.
  const FLASHCARD_SECONDS = { "pick-term": 30, "pick-definition": 35, cloze: 45, recall: 90 };
  const QUICK_AUTHORED_SECONDS = { mcq: 40, tf: 25 };
  const FALLBACK_SECONDS_PER_MARK = 30;
  const MIN_EXAM_SECONDS = 60;

  // Share of the test's time spent on flashcards for each mix setting.
  const MIX_FLASHCARD_SHARE = { flashcards: 0.75, balanced: 0.5, exam: 0.25 };

  // Target proportions of flashcard formats. Recall needs an authored prompt,
  // so cards without one share its slot between the other formats.
  const FORMAT_TARGETS = { "pick-term": 0.3, "pick-definition": 0.25, cloze: 0.25, recall: 0.2 };

  const MAX_MCQ_DEFINITION_WORDS = 45;
  const MAX_CLOZE_DEFINITION_WORDS = 60;
  const MAX_PARTS_PER_GROUP = 3;

  const STOPWORDS = new Set([
    "about","above","across","after","again","against","along","also","although","among","another","around","based","because","become","becomes","before","being","below","between","both","called","cannot","could","during","each","either","especially","every","example","examples","following","found","from","further","given","having","their","there","these","they","those","through","towards","under","until","using","usually","various","very","where","whether","which","while","within","without","would","other","others","often","such","than","that","them","then","this","into","only","over","same","some","when","with","what","will","your","more","most","much","many","made","make","makes","must","part","parts","form","forms","type","types","known","include","includes","including","involves","involving","refers","means","allows","allowing","causes","caused","results","resulting","produces","produced","contains","containing","consists","certain","specific","particular","general","different","important","main","major","small","large","high","higher","lower","greater","number","amount","level","levels","rather","whose","itself","themselves","thereby","therefore","however","instead","despite","whereas","throughout","something","someone","people","person","things","thing","there","where","which"
  ]);

  // General vocabulary that makes a poor blank: knowing it says nothing about
  // the topic. Blanks should land on the card's technical content instead.
  const GENERAL_WORDS = new Set(`
    ability able absence accept accepted access according account achieve achieved acting action actions active activity actual added addition additional address adequate affect affected affects agree agreed allow allowed almost alone already altered alter always amongst analyse analysed annual apart apparent appear appears applied apply approach approached appropriate approximately areas argue arranged arrangements aspect aspects assess associated attempt attempted attention authorities authority available average avoid aware balance basic basis beginning behaviour belief benefit benefits better beyond bigger bring broad brought build building built carried carry cases cause central centre century challenge challenges change changed changes changing character characterised characteristic characteristics characterized check choice choose chosen circumstances claim claimed clear clearly close closely collect combined comes coming common commonly community compared comparison complete completely complex concern concerned concerns condition conditions conduct considered consistent constant contact content context continue continued contrast control controlled correct countries country course create created creates creating critical critique current currently daily dealing decide decided decision decline defined defining degree demand demonstrated demonstrating depend dependent depending depends described design designed despite detail detailed determine determined develop developed developing development difference differences difficult direct directly distinct distinctive divided document early easily economic effect effective effects effort element elements eliminate emerged encourage ended enough ensure ensuring entire entry environment equal especially essential establish established establishing estimate events eventually evidence exact exactly exceptional exist existing expand expanded expected experience explain expressed extended extent extra facilities factor factors failed failure family famous features field final finally financial first focus followed force formal formed forward frequently front fully function functions future gained generally getting given gives giving global going greatly group grouping groups growing growth guide happen happened heavily helped helps highly holding however human identified identify immediate immediately impact importance improve improved improvement include increase increased increasing independent indicate individual individuals influence influenced information initial instead instrumental intended interest internal introduced introduction involve involved issue issues itself joined journey keeping known labour lack large largely later latter leading leads learn least leave leaving length lesser likely limit limited little living local longer losing lower made maintain maintained maintaining majority making manner marked massive material matter maximum meaning measure measures meeting member members method methods middle might minimum modern moment movement moving natural nature nearly necessary needed needs negative network never nonetheless normal normally noted notable object objective obtain occur occurred occurs offer offered offers official often order ordinary organise organised organization organisation original otherwise outcome outcomes outside overall owned particular particularly passed patterns perhaps period permanent physical place placed plans played point points policy political poor popular population portion position positive possible potential power powerful practical practice precise predecessor presence present presented pressure prevent preventing previous primarily primary principle principles prior private probably problem problems procedure proceeds process processes produce producing product production progress project promote promoted proper property proportion protect protesting provide provided provides providing public purpose purposes quality quickly quite range rapid rapidly rarely rates reach reached ready reason reasons receive received recent recently recognised record reduce reduced reducing reflect refer region regions regular related relation relationship relative relatively release remain remained remains remove removed repeated replace replaced report represent represents require required requires requiring research resources response responsible result resulted return reverse right rights rising routes running safety science scope second section seeking seems sense separate series serious served service services several shape share shift short shown side significant significantly similar simple single situation small social society solution source sources space special spread stage stages standard standards start started state states status steps still strong strongly structure structures study subject success successful suitable support supported sustain systems taken taking target terms think third total towards traditional transfer trends typical typically understanding unique units usual valuable value values variety version viewed vital water whole widely wider within working world years young
    irish northern southern eastern western british european american english french german christian multiple relevant component components pattern substance substances converts convert systematic protective protection contribution foreign governed industries industry chemical sporting coverage interactions surroundings maximize maximise broken flexible legally ministerial adventure various measured
  `.trim().split(/\s+/));

  // Exam parts that point at material the test cannot show (a document, map,
  // photograph or table printed on the paper) are unanswerable here.
  const MISSING_VISUAL_RE = new RegExp([
    "\\b(?:the|this|these|following|above|accompanying|attached|given|that)\\s+(?:labelled\\s+)?(?:diagrams?|graphs?|tables?|photographs?|photos?|maps?|figures?|images?|charts?|illustrations?|cartoons?|extracts?|documents?|sources?|passages?|data|information|pictures?|texts?|advertisements?|posters?|letters?|speech|article|report|label|results|sketch|weather chart|aerial photograph|OS map)\\b",
    "\\b(?:document|source|figure|photograph|extract|diagram|map|table|graph|picture|image)\\s+[A-Z0-9]\\b",
    "\\bgrid reference\\b",
    "\\bshown\\b",
    "\\bOrdnance Survey\\b",
    "\\bfrom the (?:extract|document|source|passage|text)\\b",
  ].join("|"), "i");

  // A part that leans on an earlier part only makes sense straight after it.
  // "How did you know when the reaction had stopped?" leans on a stem it does not repeat.
  const BACK_REFERENCE_RE = new RegExp([
    "\\b(?:above|previous(?:ly)?|your answer|in part|named in|referred to|mentioned in|identified in|(?:in|from|to|of) \\((?:[a-h]|i{1,3}|iv|v|vi{0,3})\\))",
    "\\b(?:the|this|that|these|those|your|each) (?:reaction|experiment|investigation|procedure|activity|test|tests|process|method|apparatus|solution|solutions|sample|samples|organism|organisms|structure|structures|substance|result|results|data|cell|cells|plant|plants|animal|animals|tissue|enzyme|country|region|event|person|policy|figure|area|example|case|material|product|food|dish|meal|fabric|item)\\b",
    "\\b(?:it|they|them|its|their)\\b",
  ].join("|"), "i");

  function compact(text) {
    return String(text || "").replace(/\*\*/g, "").replace(/\s+/g, " ").trim();
  }

  function wordCount(text) {
    return compact(text).split(" ").filter(Boolean).length;
  }

  function capitalise(text) {
    return text ? text.charAt(0).toUpperCase() + text.slice(1) : text;
  }

  // "What is a ligament?" -> "Ligament". Plain terms pass straight through.
  // Returns "" when a question-style term does not name a single subject.
  function cardSubject(term) {
    const clean = compact(term).replace(/^\d+[.)]\s+/, "");
    if (!/\?\s*$/.test(clean)) {
      // Notes headings such as "Distinguish between X and Y." or "Key reasons a
      // business should conduct market research" are topics, not terms.
      if (/^(?:distinguish|explain|outline|describe|discuss|list|provide|evaluate|compare|identify|state|name|give|analyse|illustrate)\b/i.test(clean)) return "";
      if (wordCount(clean) > 6) return "";
      return clean.replace(/[.:]\s*$/, "");
    }
    const match =
      clean.match(/^(?:what|who)\s+(?:is|are|was|were)\s+(?:meant by\s+)?(?:an?\s+|the\s+)?(.+?)(?:,?\s+and\s+(?:what|why|how|who|when|where|which)\b.*)?\?\s*$/i) ||
      clean.match(/^what\s+(?:does|do)\s+(?:the\s+)?(.+?)\s+(?:mean|stand for)\?\s*$/i) ||
      clean.match(/^what\s+characteri[sz]ed\s+(?:the\s+)?(.+?)\?\s*$/i) ||
      clean.match(/^how\s+(?:does|do)\s+(?:the\s+)?(.+?)\s+(?:work|occur|happen|take place)\?\s*$/i);
    if (!match) return "";
    const subject = match[1].replace(/^["“'‘]|["”'’]$/g, "").trim();
    if (!subject || wordCount(subject) > 9) return "";
    return capitalise(subject);
  }

  function stem(word) {
    const w = word.toLowerCase();
    return w.length > 5 ? w.slice(0, 5) : w;
  }

  function subjectStems(subject) {
    return compact(subject)
      .toLowerCase()
      .split(/[^a-z0-9]+/)
      .filter((w) => w.length >= 4 && !STOPWORDS.has(w))
      .map(stem);
  }

  // Hide the subject in its own description so "which term is this?" is not a giveaway.
  function maskSubject(definition, subject) {
    const stems = subjectStems(subject);
    let text = compact(definition);
    if (subject) {
      const escaped = subject.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      text = text.replace(new RegExp(escaped, "gi"), "____");
    }
    // Word-level masking only for one-word terms; for phrases a shared word (e.g.
    // "population" in "J-shaped population curve") is not a giveaway.
    if (stems.length !== 1) return text;
    return text.replace(/[A-Za-z][A-Za-z'-]*/g, (word) =>
      word.length >= 4 && stems.includes(stem(word)) ? "____" : word
    );
  }

  // ── Cloze ──────────────────────────────────────────────────

  function buildIdf(cards) {
    const docFreq = new Map();
    cards.forEach((card) => {
      const seen = new Set(
        compact(card.definition).toLowerCase().split(/[^a-z0-9]+/).filter(Boolean)
      );
      seen.forEach((w) => docFreq.set(w, (docFreq.get(w) || 0) + 1));
    });
    const total = Math.max(1, cards.length);
    return (word) => Math.log((total + 1) / ((docFreq.get(word) || 0) + 1));
  }

  function splitToken(token) {
    const match = token.match(/^([^A-Za-z0-9]*)(.*?)((?:['’]s)?[^A-Za-z0-9]*)$/);
    return { lead: match[1], core: match[2], trail: match[3] };
  }

  const MIN_BLANK_SCORE = 2.4;

  // How good a word is as a blank: technical terms (words that are themselves
  // card terms), names and dates score high; everyday vocabulary scores low.
  function blankScore(tokens, index, context) {
    const { core, lead } = splitToken(tokens[index]);
    if (/^(?:1[0-9]|20)\d{2}$/.test(core)) return 3.5; // a year
    if (!/^[A-Za-z][A-Za-z'’-]{4,}$/.test(core)) return -Infinity;
    const lower = core.toLowerCase();
    if (STOPWORDS.has(lower) || context.subjectStems.includes(stem(lower))) return -Infinity;

    const previous = tokens[index - 1] || "";
    const sentenceStart = index === 0 || /[.:;!?]$/.test(previous);
    let score = context.idf(lower) * 0.5 + Math.min(core.length, 12) / 12;
    if (context.termStems.has(stem(lower))) score += 2.5;
    if (/^[A-Z]/.test(core) && !sentenceStart) score += 2;
    if (lead.includes("(") || /[,(]$/.test(previous) || /^(?:and|or)$/i.test(previous) || /,$/.test(tokens[index])) score += 0.6;
    if (GENERAL_WORDS.has(lower)) score -= 4;
    if (/(?:ly|ing|ed)$/.test(lower) && !context.termStems.has(stem(lower))) score -= 1.5;
    if (/[-]/.test(core)) score -= 1;
    return score;
  }

  // Blanks the one or two most telling words of the card's own text, so the
  // question asks for exactly what the flashcard teaches.
  // Returns { segments, answers } where segments alternate text and blank slots,
  // or null when no word is worth blanking.
  function buildCloze(definition, subject, context) {
    const text = compact(definition);
    const words = wordCount(text);
    if (words < 6 || words > MAX_CLOZE_DEFINITION_WORDS) return null;
    const tokens = text.split(" ");
    const scoringContext = { ...context, subjectStems: subjectStems(subject) };
    const scored = tokens
      .map((token, index) => ({ index, core: splitToken(token).core, score: blankScore(tokens, index, scoringContext) }))
      .filter((candidate) => candidate.score >= MIN_BLANK_SCORE)
      .sort((a, b) => b.score - a.score);
    if (!scored.length) return null;

    const wanted = words > 14 && scored.length > 1 && scored[1].score >= MIN_BLANK_SCORE + 0.8 ? 2 : 1;
    const picks = [];
    const usedWords = new Set();
    for (const candidate of scored) {
      if (picks.length >= wanted) break;
      if (picks.some((p) => Math.abs(p.index - candidate.index) < 2)) continue;
      if (usedWords.has(stem(candidate.core))) continue;
      picks.push(candidate);
      usedWords.add(stem(candidate.core));
    }
    picks.sort((a, b) => a.index - b.index);

    const segments = [];
    let buffer = "";
    tokens.forEach((token, index) => {
      const separator = index === 0 ? "" : " ";
      const pick = picks.find((p) => p.index === index);
      if (!pick) {
        buffer += separator + token;
        return;
      }
      const { lead, trail } = splitToken(token);
      segments.push({ text: buffer + separator + lead });
      segments.push({ blank: picks.indexOf(pick) });
      buffer = trail;
    });
    segments.push({ text: buffer });
    return {
      segments: segments.filter((s) => s.blank !== undefined || s.text),
      answers: picks.map((p) => p.core),
    };
  }

  // ── Answer matching (typed cloze answers) ──────────────────

  function normaliseAnswer(text) {
    return String(text || "")
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .toLowerCase()
      .replace(/[^a-z0-9]/g, "")
      .replace(/is(e|ed|es|ing|ation)$/, "iz$1")
      .replace(/ys(e|ed|es|ing)$/, "yz$1")
      .replace(/our$/, "or");
  }

  function editDistance(a, b) {
    const row = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) {
      let prev = row[0];
      row[0] = i;
      for (let j = 1; j <= b.length; j++) {
        const tmp = row[j];
        row[j] = Math.min(row[j] + 1, row[j - 1] + 1, prev + (a[i - 1] === b[j - 1] ? 0 : 1));
        prev = tmp;
      }
    }
    return row[b.length];
  }

  function answerMatches(given, expected) {
    const g = normaliseAnswer(given);
    const e = normaliseAnswer(expected);
    if (!g || !e) return false;
    if (g === e) return true;
    if (/^\d+$/.test(e)) return false; // years must be exact
    const singular = (w) => w.replace(/(es|s)$/, "");
    if (singular(g) === singular(e)) return true;
    const allowed = e.length >= 8 ? 2 : e.length >= 5 ? 1 : 0;
    return editDistance(g, e) <= allowed;
  }

  // ── Pool ───────────────────────────────────────────────────

  function examPartSeconds(breakdown, marks) {
    const m = Number(marks) || 0;
    if (!m) return MIN_EXAM_SECONDS;
    const seconds = breakdown?.totalMarks && breakdown?.totalMinutes
      ? (m / breakdown.totalMarks) * breakdown.totalMinutes * 60
      : m * FALLBACK_SECONDS_PER_MARK;
    return Math.max(MIN_EXAM_SECONDS, Math.round(seconds / 15) * 15);
  }

  // Questions on a printed source the bank does not include: History's
  // documents-based study, and the "A" comprehension parts at Ordinary level
  // ("How long did the crossing take?" is about an extract, not the course).
  function needsPrintedSource(part, group) {
    if (group.subject !== "history") return false;
    return group.sectionId === "hist-section1"
      || (/ordinary/i.test(group.source || "") && /^A\d/.test(part.label || ""));
  }

  function isAnswerablePart(part, group) {
    if (!part || !compact(part.question) || !(Number(part.marks) > 0)) return false;
    if (!compact(part.model) && !part.workedSolution) return false;
    if (needsPrintedSource(part, group)) return false;
    if (part.diagram || group.context) return true;
    return !MISSING_VISUAL_RE.test(part.question);
  }

  function collectCards(chapters, prompts) {
    const cards = [];
    const seen = new Set();
    (chapters || []).forEach((chapter) => {
      const chapterPrompts = prompts?.[chapter.id] || {};
      (chapter.learningOutcomes || []).forEach((outcome) => {
        (outcome.keyTerms || []).forEach((kt, idx) => {
          const term = compact(kt.term);
          const definition = compact(kt.definition);
          const key = `${term}|${definition}`.toLowerCase();
          if (!term || wordCount(definition) < 4 || seen.has(key)) return;
          seen.add(key);
          cards.push({
            cardId: `${outcome.id}-k-${idx + 1}`,
            chapterId: chapter.id,
            outcomeId: outcome.id,
            term,
            subject: cardSubject(term),
            definition,
            recallPrompt: compact(chapterPrompts[kt.term] || ""),
          });
        });
      });
    });
    return cards;
  }

  /**
   * Gathers everything a test could ask about the given chapters.
   * input: {
   *   subjectId, breakdown,
   *   chapters:        the chapters in scope [{ id, title, learningOutcomes: [{ id, keyTerms }] }],
   *   subjectChapters: every chapter of the subject — vocabulary for blanks and distractors,
   *   examGroupsFor(chapter) -> EXAM_QUESTIONS_DB groups,
   *   authoredFor(chapter)   -> [{ outcomeId, question }] (hand-written outcome questions),
   *   prompts                -> FLASHCARD_TEST_PROMPTS[chapterId][term] = written prompt
   * }
   */
  function buildPool(input) {
    const examGroups = [];
    const authored = [];
    const chapterTitles = {};
    const cards = collectCards(input.chapters, input.prompts);
    const corpusCards = input.subjectChapters ? collectCards(input.subjectChapters, null) : cards;

    (input.chapters || []).forEach((chapter) => {
      chapterTitles[chapter.id] = chapter.title;

      (input.examGroupsFor?.(chapter) || []).forEach((group) => {
        const parts = (group.parts || []).map((part, index) => ({
          part,
          index,
          answerable: isAnswerablePart(part, group),
          standalone: index === 0 || !BACK_REFERENCE_RE.test(part.question || ""),
          seconds: examPartSeconds(input.breakdown, part.marks),
        }));
        if (parts.some((p) => p.answerable)) examGroups.push({ chapterId: chapter.id, group, parts });
      });

      (input.authoredFor?.(chapter) || []).forEach(({ outcomeId, question }, idx) => {
        if (!question?.prompt) return;
        const type = question.type === "mcq" || question.type === "tf" ? question.type : "written";
        if (type === "mcq" && !(question.options?.length >= 2 && Number.isInteger(question.correct))) return;
        if (type === "tf" && typeof question.correct !== "boolean") return;
        if (type === "written" && !compact(question.model)) return;
        authored.push({
          id: `${outcomeId}-a-${idx + 1}`,
          chapterId: chapter.id,
          outcomeId,
          question,
          type,
          seconds: type === "written"
            ? examPartSeconds(input.breakdown, question.marks)
            : QUICK_AUTHORED_SECONDS[type],
        });
      });
    });

    const clozeContext = {
      idf: buildIdf(corpusCards),
      termStems: new Set(
        corpusCards.flatMap((card) => (card.subject || card.term).toLowerCase().split(/[^a-z]+/))
          .filter((w) => w.length >= 5 && !STOPWORDS.has(w) && !GENERAL_WORDS.has(w))
          .map(stem)
      ),
    };
    cards.forEach((card) => {
      card.cloze = buildCloze(card.definition, card.subject, clozeContext);
    });

    const examSeconds = examGroups.reduce(
      (sum, g) => sum + g.parts.filter((p) => p.answerable).reduce((s, p) => s + p.seconds, 0), 0
    ) + authored.reduce((sum, a) => sum + a.seconds, 0);
    const flashcardSeconds = cards.length * FLASHCARD_SECONDS.cloze;

    return {
      subjectId: input.subjectId,
      cards,
      corpusCards,
      examGroups,
      authored,
      chapterTitles,
      capacitySeconds: { flashcards: flashcardSeconds, exam: examSeconds },
    };
  }

  // ── Assembly ───────────────────────────────────────────────

  function shuffle(list, random) {
    const a = list.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  // Shuffles within each chapter, then deals chapters round-robin so a
  // whole-subject test spreads across the course instead of clumping.
  function interleaveByChapter(list, random) {
    const byChapter = new Map();
    shuffle(list, random).forEach((item) => {
      if (!byChapter.has(item.chapterId)) byChapter.set(item.chapterId, []);
      byChapter.get(item.chapterId).push(item);
    });
    const queues = shuffle(Array.from(byChapter.values()), random);
    const out = [];
    while (queues.some((q) => q.length)) {
      queues.forEach((q) => {
        if (q.length) out.push(q.shift());
      });
    }
    return out;
  }

  function pickDistractors(card, cards, key, random, count = 3) {
    const own = card[key].toLowerCase();
    const seen = new Set([own]);
    const sameOutcome = [];
    const sameChapter = [];
    const rest = [];
    cards.forEach((other) => {
      const value = other[key];
      if (!value || other === card) return;
      if (key === "definition" && wordCount(value) > MAX_MCQ_DEFINITION_WORDS) return;
      if (other.outcomeId === card.outcomeId) sameOutcome.push(other);
      else if (other.chapterId === card.chapterId) sameChapter.push(other);
      else rest.push(other);
    });
    const picked = [];
    [sameOutcome, sameChapter, rest].forEach((bucket) => {
      shuffle(bucket, random).forEach((other) => {
        if (picked.length >= count) return;
        const value = other[key].toLowerCase();
        if (seen.has(value)) return;
        seen.add(value);
        picked.push(other[key]);
      });
    });
    return picked.length >= count ? picked : null;
  }

  function withOptions(correct, distractors, random) {
    const options = shuffle([correct, ...distractors], random);
    return { options, correctIndex: options.indexOf(correct) };
  }

  function flashcardItem(card, format, pool, random) {
    const base = {
      id: `${card.cardId}-${format}`,
      bucket: "flashcard",
      kind: format,
      chapterId: card.chapterId,
      outcomeId: card.outcomeId,
      cardId: card.cardId,
      term: card.term,
      definition: card.definition,
      seconds: FLASHCARD_SECONDS[format],
    };
    if (format === "pick-term") {
      if (!card.subject || wordCount(card.definition) > MAX_MCQ_DEFINITION_WORDS) return null;
      const distractors = pickDistractors(card, pool.corpusCards, "subject", random);
      if (!distractors) return null;
      return { ...base, marks: 1, prompt: maskSubject(card.definition, card.subject), answer: card.subject, ...withOptions(card.subject, distractors, random) };
    }
    if (format === "pick-definition") {
      if (wordCount(card.definition) > MAX_MCQ_DEFINITION_WORDS) return null;
      const distractors = pickDistractors(card, pool.corpusCards, "definition", random);
      if (!distractors) return null;
      return { ...base, marks: 1, prompt: card.term, answer: card.definition, ...withOptions(card.definition, distractors, random) };
    }
    if (format === "cloze") {
      if (!card.cloze) return null;
      return { ...base, marks: card.cloze.answers.length, prompt: card.subject || card.term, segments: card.cloze.segments, answers: card.cloze.answers };
    }
    if (format === "recall") {
      if (!card.recallPrompt) return null;
      return { ...base, marks: 2, prompt: card.recallPrompt };
    }
    return null;
  }

  function pickFlashcards(pool, budget, random, usedCards) {
    const items = [];
    const counts = { "pick-term": 0, "pick-definition": 0, cloze: 0, recall: 0 };
    let remaining = budget;
    const minSeconds = Math.min(...Object.values(FLASHCARD_SECONDS));
    for (const card of interleaveByChapter(pool.cards, random)) {
      if (remaining < minSeconds) break;
      if (usedCards.has(card.cardId)) continue;
      const total = items.length + 1;
      const formats = Object.keys(FORMAT_TARGETS)
        .map((format) => ({ format, deficit: FORMAT_TARGETS[format] * total - counts[format] + random() * 0.01 }))
        .sort((a, b) => b.deficit - a.deficit);
      for (const { format } of formats) {
        if (FLASHCARD_SECONDS[format] > remaining) continue;
        const item = flashcardItem(card, format, pool, random);
        if (!item) continue;
        items.push(item);
        counts[format] += 1;
        usedCards.add(card.cardId);
        remaining -= item.seconds;
        break;
      }
    }
    return items;
  }

  function examPartItem(entry, slot, isContinuation) {
    const { group } = entry;
    const { part } = slot;
    return {
      id: `${group.id}-p${slot.index}`,
      bucket: "exam",
      kind: "written",
      chapterId: entry.chapterId,
      groupId: group.id,
      continuation: isContinuation,
      source: group.source || "",
      year: group.year || null,
      label: part.label || "",
      prompt: part.question,
      model: part.model || "",
      workedSolution: part.workedSolution || null,
      diagram: part.diagram || "",
      context: group.caseStudy ? group.context || "" : "",
      marks: Number(part.marks) || 0,
      schemePoints: Number(part.scheme_points) || 0,
      seconds: slot.seconds,
    };
  }

  function authoredItem(entry) {
    const q = entry.question;
    const base = {
      id: entry.id,
      bucket: "exam",
      chapterId: entry.chapterId,
      outcomeId: entry.outcomeId,
      source: "Exam-style question",
      prompt: q.prompt,
      model: q.model || "",
      marks: Number(q.marks) || (entry.type === "written" ? 0 : 1),
      seconds: entry.seconds,
    };
    if (entry.type === "mcq") return { ...base, kind: "mcq", options: q.options.slice(), correctIndex: q.correct };
    if (entry.type === "tf") return { ...base, kind: "tf", options: ["True", "False"], correctIndex: q.correct ? 0 : 1 };
    return { ...base, kind: "written" };
  }

  function pickExam(pool, budget, random, usedIds) {
    const items = [];
    let remaining = budget;
    const sources = interleaveByChapter(
      [
        ...pool.examGroups.map((entry) => ({ chapterId: entry.chapterId, entry })),
        ...pool.authored.map((authored) => ({ chapterId: authored.chapterId, authored })),
      ],
      random
    );
    for (const source of sources) {
      if (remaining < MIN_EXAM_SECONDS * 0.5) break;
      if (source.authored) {
        if (usedIds.has(source.authored.id) || source.authored.seconds > remaining) continue;
        const item = authoredItem(source.authored);
        items.push(item);
        usedIds.add(item.id);
        remaining -= item.seconds;
        continue;
      }
      const { entry } = source;
      const starts = shuffle(
        entry.parts.filter((p) => p.answerable && p.standalone && p.seconds <= remaining && !usedIds.has(`${entry.group.id}-p${p.index}`)),
        random
      ).sort((a, b) => a.index - b.index);
      // Prefer the opening part, but allow any self-contained part so short
      // budgets can still land a small question from a long one.
      const start = random() < 0.5 ? starts[0] : starts[Math.floor(random() * starts.length)];
      if (!start) continue;
      let taken = 0;
      for (let i = start.index; i < entry.parts.length && taken < MAX_PARTS_PER_GROUP; i++) {
        const slot = entry.parts[i];
        if (!slot.answerable || slot.seconds > remaining) break;
        const item = examPartItem(entry, slot, taken > 0);
        if (usedIds.has(item.id)) break;
        items.push(item);
        usedIds.add(item.id);
        remaining -= slot.seconds;
        taken += 1;
      }
    }
    return items;
  }

  /**
   * Picks questions to fill `minutes`. mix is "flashcards" | "balanced" | "exam".
   * Flashcards come first as a warm-up, exam questions after.
   */
  function assembleTest(pool, options = {}) {
    const random = options.random || Math.random;
    const budget = Math.max(1, Number(options.minutes) || 10) * 60;
    const hasCards = pool.cards.length > 0;
    const hasExam = pool.examGroups.length > 0 || pool.authored.length > 0;
    const share = !hasExam ? 1 : !hasCards ? 0 : MIX_FLASHCARD_SHARE[options.mix] ?? 0.5;

    const usedCards = new Set();
    const usedExam = new Set();
    const exam = pickExam(pool, budget * (1 - share), random, usedExam);
    const examSeconds = exam.reduce((s, i) => s + i.seconds, 0);
    const flashcards = pickFlashcards(pool, budget - examSeconds, random, usedCards);
    const flashSeconds = flashcards.reduce((s, i) => s + i.seconds, 0);
    // Not enough flashcards to use their share? Give the time back to exam questions.
    const topUp = pickExam(pool, budget - examSeconds - flashSeconds, random, usedExam);

    const examItems = exam.concat(topUp);
    // Keep each exam question's parts together, in paper order.
    const groupOrder = [];
    examItems.forEach((item) => {
      const key = item.groupId || item.id;
      if (!groupOrder.includes(key)) groupOrder.push(key);
    });
    examItems.sort((a, b) => {
      const ga = groupOrder.indexOf(a.groupId || a.id);
      const gb = groupOrder.indexOf(b.groupId || b.id);
      return ga - gb || a.id.localeCompare(b.id, undefined, { numeric: true });
    });
    examItems.forEach((item, i) => {
      item.continuation = Boolean(item.groupId) && examItems[i - 1]?.groupId === item.groupId;
    });

    const items = flashcards.concat(examItems);
    const plannedSeconds = items.reduce((s, i) => s + i.seconds, 0);
    return {
      items,
      budgetSeconds: budget,
      plannedSeconds,
      chapterIds: Array.from(new Set(items.map((i) => i.chapterId))),
    };
  }

  // ── Marking ────────────────────────────────────────────────

  // response shapes: choice -> { choice }, cloze -> { blanks: [] , overrides: [] },
  // recall/written -> { text, selfMarks }
  function markItem(item, response = {}) {
    if (item.kind === "pick-term" || item.kind === "pick-definition" || item.kind === "mcq" || item.kind === "tf") {
      const correct = response.choice === item.correctIndex;
      return { earned: correct ? item.marks : 0, needsSelfMark: false, correct };
    }
    if (item.kind === "cloze") {
      const results = item.answers.map((answer, i) =>
        Boolean(response.overrides?.[i]) || answerMatches(response.blanks?.[i], answer)
      );
      const earned = results.filter(Boolean).length;
      return { earned, needsSelfMark: false, correct: earned === item.answers.length, blanks: results };
    }
    const selfMarks = response.selfMarks;
    const marked = Number.isFinite(selfMarks);
    return {
      earned: marked ? Math.max(0, Math.min(item.marks, selfMarks)) : 0,
      needsSelfMark: !marked,
      correct: marked && selfMarks >= item.marks,
    };
  }

  // Each item counts in proportion to the time it takes, so one 30-mark essay
  // does not drown out ten quick flashcards (or vice versa).
  function scoreTest(test, responses) {
    let weighted = 0;
    let weight = 0;
    const buckets = { flashcard: { earned: 0, total: 0, correct: 0, count: 0 }, exam: { earned: 0, total: 0, correct: 0, count: 0 } };
    const byChapter = {};
    const byOutcome = {};
    let pendingSelfMarks = 0;

    test.items.forEach((item) => {
      const result = markItem(item, responses[item.id]);
      if (result.needsSelfMark) pendingSelfMarks += 1;
      const fraction = item.marks ? result.earned / item.marks : 0;
      weighted += fraction * item.seconds;
      weight += item.seconds;

      const bucket = buckets[item.bucket];
      bucket.earned += result.earned;
      bucket.total += item.marks;
      bucket.count += 1;
      if (result.correct) bucket.correct += 1;

      const ch = (byChapter[item.chapterId] ||= { weighted: 0, weight: 0, count: 0 });
      ch.weighted += fraction * item.seconds;
      ch.weight += item.seconds;
      ch.count += 1;

      if (item.outcomeId && item.bucket === "flashcard") {
        const lo = (byOutcome[item.outcomeId] ||= { correct: 0, count: 0, correctCards: [] });
        lo.count += 1;
        if (result.correct) {
          lo.correct += 1;
          lo.correctCards.push(item.cardId);
        }
      }
    });

    Object.values(byChapter).forEach((ch) => {
      ch.percent = ch.weight ? Math.round((ch.weighted / ch.weight) * 100) : 0;
    });
    return {
      percent: weight ? Math.round((weighted / weight) * 100) : 0,
      buckets,
      byChapter,
      byOutcome,
      pendingSelfMarks,
    };
  }

  root.TestBuilder = {
    FLASHCARD_SECONDS,
    MIX_FLASHCARD_SHARE,
    cardSubject,
    maskSubject,
    buildCloze,
    answerMatches,
    isAnswerablePart,
    buildPool,
    assembleTest,
    markItem,
    scoreTest,
  };
})(typeof window !== "undefined" ? window : globalThis);
