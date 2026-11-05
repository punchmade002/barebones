// Answer marker — marks a written answer against its model answer, entirely in
// the browser. The model answer is split into marking points (one per bullet,
// numbered item or sentence, the way SEC schemes award marks), and each point
// counts as made when the student's answer uses enough of its key terms close
// together. Spelling slips, word forms ("respire" / "respiration") and common
// synonyms ("rises" / "increases") are forgiven; restating the question is not
// rewarded. Pure logic, no DOM.
(function (root) {
  // Function words and exam instructions: never a reason to award a mark.
  const STOPWORDS = new Set(`
    a about above across after again against all almost along also although always am among an and another any anything
    are around as at away be because been before being below between both but by can cannot could did do does doing done
    down during each either else etc even ever every few for from further get gets getting give given gives go goes going
    got had has have having he her here hers him his how however i if in into is it its itself just least less like made
    make makes many may me might more most much must my near need needs neither no nor not now of off often on once one
    only onto or other others otherwise our out over own per perhaps quite rather really same shall she should since so
    some something such than that the their them themselves then there therefore these they thing things this those though
    through thus to too toward towards under unless until up upon us very via was way ways we well were what whatever when
    where whereas whether which while who whom whose why will with within without would yes yet you your
    answer answers question questions part parts explain explains describe describes state states name names identify
    outline discuss evaluate suggest list mention give example examples e g eg ie i e called known term terms also
    shown show shows above below following use used uses using mark marks award awarded expect
  `.trim().split(/\s+/));

  // Words a student may use in place of the scheme's word.
  const SYNONYM_GROUPS = [
    "increase increases increased increasing rise rises risen rising rose raise raises raised higher more greater grow grows growth up",
    "decrease decreases decreased decreasing decline declines declined fall falls fell falling lower less reduce reduces reduced reducing reduction drop drops dropped fewer down",
    "large larger largest big bigger biggest huge",
    "small smaller smallest little tiny",
    "fast faster quick quicker quickly rapid rapidly",
    "stop stops stopped prevent prevents prevented block blocks blocked inhibit inhibits inhibited",
    "produce produces produced production make makes made form forms formed create creates created synthesise synthesises synthesised synthesize",
    "kill kills killed destroy destroys destroyed",
    "help helps helped aid aids assist assists",
    "need needs needed require requires required",
    "begin begins began start starts started",
    "get gets obtain obtains obtained gain gains gained receive receives received",
    "change changes changed alter alters altered",
    "cause causes caused lead leads led",
    "remove removes removed eliminate eliminates eliminated",
    "store stores stored storage",
    "join joins joined bond bonds bonded",
    "break breaks broke broken split splits",
    "heat heats heated warm warms warmed hot",
    "cold colder cool cools cooled",
    "effect effects affect affects affected impact impacts influence influences",
    "easy easier easily simple simpler",
    "cheap cheaper inexpensive",
    "expensive dear costly",
  ];
  const SYNONYMS = new Map();
  SYNONYM_GROUPS.forEach((group, index) => {
    group.split(/\s+/).forEach((word) => SYNONYMS.set(word, `~${index}`));
  });

  // Phrases written several ways.
  const PHRASES = [
    [/\bcarbon dioxide\b/g, "co2"],
    [/\bdeoxyribonucleic acid\b/g, "dna"],
    [/\bribonucleic acid\b/g, "rna"],
    [/\badenosine triphosphate\b/g, "atp"],
    [/\bh2o\b/g, "water"],
    [/\bo2\b/g, "oxygen"],
  ];

  const NEGATIONS = new Set(["not", "no", "never", "cannot", "cant", "dont", "doesnt", "didnt", "isnt", "arent", "wasnt", "werent", "wont", "without", "none", "neither", "nor"]);

  const SUBSCRIPTS = { "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9", "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-" };

  function normaliseText(text) {
    let out = String(text || "")
      .replace(/[₀-₉⁰-⁹⁻¹²³]/g, (c) => SUBSCRIPTS[c] || c)
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .replace(/[’‘]/g, "'")
      .toLowerCase();
    // 2.49 × 10-3 -> 0.00249, so either way of writing a number matches.
    out = out.replace(/(\d+(?:\.\d+)?)\s*[x×*]\s*10\s*\^?\s*(-?\d+)/g, (_, mantissa, power) => {
      const value = Number(mantissa) * Math.pow(10, Number(power));
      return Number.isFinite(value) ? String(Number(value.toPrecision(6))) : _;
    });
    PHRASES.forEach(([re, to]) => {
      out = out.replace(re, to);
    });
    return out;
  }

  const WORD_RE = /\d+(?:[.,]\d+)*|[a-z][a-z0-9']*(?:-[a-z0-9]+)*/g;

  function stemWord(word) {
    let w = word.replace(/'s$|'$/, "").replace(/'/g, "");
    if (w.length <= 3) return w;
    if (/ies$/.test(w) && w.length > 4) w = w.slice(0, -3) + "y";
    else if (/iest?$|ier$/.test(w) && w.length > 5) w = w.replace(/iest?$|ier$/, "y");
    else if (/sses$/.test(w)) w = w.slice(0, -2);
    else if (/[^su]s$/.test(w)) w = w.slice(0, -1);
    if (/(?:ing|ed)$/.test(w)) {
      const base = w.replace(/(?:ing|ed)$/, "");
      if (base.length >= 4) w = /([b-df-hj-np-tv-z])\1$/.test(base) && !/(?:ll|ss)$/.test(base) ? base.slice(0, -1) : base;
    }
    if (/ly$/.test(w) && w.length > 6) w = w.slice(0, -2);
    if (/e$/.test(w) && w.length > 4) w = w.slice(0, -1);
    return w;
  }

  function canonical(word) {
    return SYNONYMS.get(word) || stemWord(word);
  }

  function editDistance(a, b, limit) {
    if (Math.abs(a.length - b.length) > limit) return limit + 1;
    const row = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) {
      let prev = row[0];
      row[0] = i;
      let best = row[0];
      for (let j = 1; j <= b.length; j++) {
        const tmp = row[j];
        row[j] = Math.min(row[j] + 1, row[j - 1] + 1, prev + (a[i - 1] === b[j - 1] ? 0 : 1));
        prev = tmp;
        best = Math.min(best, row[j]);
      }
      if (best > limit) return limit + 1;
    }
    return row[b.length];
  }

  function isNumber(word) {
    return /^\d/.test(word);
  }

  function numberValue(word) {
    return Number(word.replace(/,(?=\d{3}\b)/g, "").replace(",", "."));
  }

  // Do two words count as the same term? Same root, a shared long prefix
  // ("photosynthesis" / "photosynthetic"), or a small spelling slip.
  function termsMatch(term, token) {
    if (term.canon === token.canon) return true;
    if (term.number || token.number) {
      if (!(term.number && token.number)) return false;
      const a = term.value;
      const b = token.value;
      return Number.isFinite(a) && Number.isFinite(b) && Math.abs(a - b) <= Math.max(Math.abs(a) * 0.02, 1e-9);
    }
    if (term.canon.startsWith("~") || token.canon.startsWith("~")) return false;
    const a = term.stem;
    const b = token.stem;
    const shorter = Math.min(a.length, b.length);
    if (shorter >= 5) {
      let prefix = 0;
      while (prefix < shorter && a[prefix] === b[prefix]) prefix++;
      if (prefix >= Math.max(5, Math.ceil(shorter * 0.75))) return true;
    }
    const w = term.word;
    const v = token.word;
    if (w.length < 5 || v.slice(0, 2) !== w.slice(0, 2)) return false;
    return editDistance(w, v, w.length >= 9 ? 2 : 1) <= (w.length >= 9 ? 2 : 1);
  }

  function makeToken(word) {
    const number = isNumber(word);
    const stem = number ? word : stemWord(word);
    return { word, stem, canon: number ? word : canonical(word), number, value: number ? numberValue(word) : NaN };
  }

  function contentTokens(text) {
    return (normaliseText(text).match(WORD_RE) || [])
      .filter((word) => isNumber(word) || (word.length >= 2 && !STOPWORDS.has(word.replace(/'s$/, ""))))
      .map(makeToken);
  }

  // ── Marking points ─────────────────────────────────────────

  function stripLead(text) {
    return text
      .replace(/^\s*(?:[-–—*•·▪◦●‣\uF0B7\uF0A7]+|\(?(?:[ivx]{1,4}|[a-h]|\d{1,2})[.)](?=\s))\s*/i, "")
      // A short heading such as "Calculation:" or "Advantages" labels the points after it.
      .replace(/^\s*(?:[A-Z][A-Za-z ]{0,40}):\s+/, "")
      .trim();
  }

  // SEC schemes annotate their answers: "3 points @ 4 marks each", "[any two]",
  // "(6 + 3)", "2 × 3". The annotation is about marking, not content.
  const SCHEME_COUNT_RE = /\b(\d+|one|two|three|four|five|six)\s+(?:points?|factors?|reasons?|ways?|examples?|features?|effects?|benefits?)\s*@\s*\d+\s*marks?(?:\s*each)?/i;
  const WORD_NUMBERS = { one: 1, two: 2, three: 3, four: 4, five: 5, six: 6 };

  function schemeCount(model) {
    const m = String(model || "").match(SCHEME_COUNT_RE);
    if (!m) return 0;
    return Number(m[1]) || WORD_NUMBERS[m[1].toLowerCase()] || 0;
  }

  function stripScheme(model) {
    return String(model || "")
      .replace(/\*\*/g, "")
      .replace(/\r/g, "")
      .replace(/\(?\s*(?:expect\s+)?\b(?:\d+|one|two|three|four|five|six)\s+(?:points?|factors?|reasons?|ways?|examples?|features?|effects?|benefits?)\s*@\s*\d+\s*marks?(?:\s*each)?\s*\)?/gi, " ")
      .replace(/\[[^\]]*\]/g, " ")
      .replace(/\(\s*\d+\s*(?:[+×x]\s*\d+\s*)+\)/gi, " ")
      .replace(/\(\s*\d+\s*marks?\s*\)/gi, " ")
      .replace(/(?:^|\s)\d+\s*×\s*\d+(?=\s|$|[.;,)])/g, " ");
  }

  // One point per line, bullet, numbered item or sentence ("//" in a scheme).
  // With `lists`, a run of short comma-separated items ("Upbringing, Education,
  // Social class, Ambition") is one point per item, as a scheme asking for
  // several points would mark it.
  function splitPoints(model, options = {}) {
    const text = stripScheme(model);
    const pieces = [];
    const add = (piece) => {
      const clean = stripLead(piece).replace(/\s+/g, " ").replace(/^[.,;:\s]+/, "").trim();
      if (!clean || /^etc\.?$/i.test(clean)) return;
      pieces.push(clean);
    };
    text
      .split(/\n+|\s*\/\/\s*|\s*[•·▪◦●‣\uF0B7\uF0A7]\s*|;\s+|\s(?=\((?:i{1,3}|iv|v|vi{1,3}|ix|x)\)\s)/i)
      .forEach((line) => {
        line.split(/(?<=[.!?])\s+(?=[A-Z0-9"“(])/).forEach((sentence) => {
          const items = sentence.replace(/[.\s]+$/, "").split(/,\s+(?:and\s+|or\s+)?/);
          const isList = options.lists && items.length >= 3 && items.every((item) => item.trim().split(/\s+/).length <= 5);
          if (isList) {
            items.forEach(add);
            return;
          }
          // "kill bacteria and have no effect on viruses" is two marking points.
          const clauses = sentence.split(/,?\s+and\s+(?![^()]*\))/);
          const substantial = clauses.length <= 3 && clauses.every((clause) => contentTokens(clause).length >= 2);
          if (clauses.length > 1 && substantial) clauses.forEach(add);
          else add(sentence);
        });
      });
    return pieces.filter((piece) => contentTokens(piece).length > 0);
  }

  // A point's key terms. Words in brackets are alternatives or extras: they can
  // stand in for a missed term but are not required. "x, or y" gives choices.
  function analysePoint(text, questionTokens) {
    const choices = text
      .split(/(?:,?\s+or\s+(?=[a-z])|\s+\/\s+|(?<=[A-Za-z)]{2})\/(?=[A-Za-z(]{2}))(?![^()]*\))/i)
      .filter((choice) => contentTokens(choice).length > 0);
    const options = (choices.length > 1 ? choices : [text]).map((choice) => {
      const required = [];
      const extra = [];
      const seen = new Set();
      let depth = 0;
      choice.split(/([()])/).forEach((chunk) => {
        if (chunk === "(") depth += 1;
        else if (chunk === ")") depth = Math.max(0, depth - 1);
        else {
          contentTokens(chunk).forEach((token) => {
            if (seen.has(token.canon)) return;
            seen.add(token.canon);
            const restates = questionTokens.some((q) => termsMatch(q, token));
            token.weight = (token.number ? 1.5 : token.word.length >= 8 ? 1.3 : 1) * (restates ? 0.35 : 1);
            (depth > 0 ? extra : required).push(token);
          });
        }
      });
      const negates = (normaliseText(choice).match(WORD_RE) || []).some((w) => NEGATIONS.has(w.replace(/'/g, "")));
      // A point that is all brackets ("(any two)") still needs something to match.
      return required.length ? { required, extra, negates } : { required: extra, extra: [], negates };
    });
    // In a short answer, brackets give another name: "Fallopian tube (oviduct)".
    options.slice().forEach((option) => {
      if (option.required.length <= 3 && option.extra.length && option.extra.length <= 3) {
        options.push({ required: option.extra, extra: [], negates: option.negates });
      }
    });
    return options;
  }

  // ── Student answer ─────────────────────────────────────────

  function studentSentences(answer) {
    return String(answer || "")
      .split(/\n+|(?<=[.!?;])\s+/)
      .map((sentence) => sentence.trim())
      .filter(Boolean);
  }

  function prepareAnswer(answer) {
    const sentences = studentSentences(answer);
    const tokens = [];
    sentences.forEach((sentence, s) => {
      const words = normaliseText(sentence).match(WORD_RE) || [];
      words.forEach((word, position) => {
        const token = makeToken(word);
        token.sentence = s;
        token.position = position;
        token.negation = NEGATIONS.has(word.replace(/'/g, ""));
        token.content = isNumber(word) || (word.length >= 2 && !STOPWORDS.has(word.replace(/'s$/, "")));
        tokens.push(token);
      });
    });
    return { sentences, tokens };
  }

  function isNegated(prepared, start, option, matched) {
    const near = prepared.tokens.filter((t) => t.sentence === start || t.sentence === start + 1);
    return near.some((t, i) => t.negation && near.slice(i + 1, i + 4).some((n) =>
      n.sentence === t.sentence && n.content
      && option.required.some((term) => matched.has(term.canon) && termsMatch(term, n))));
  }

  // Best coverage of one option over windows of two adjacent sentences, so a
  // point's terms must appear together, not scattered across the answer.
  function scoreOption(option, prepared) {
    const totalWeight = option.required.reduce((sum, t) => sum + t.weight, 0) || 1;
    const hitsBySentence = (term) => {
      const sentences = new Set();
      prepared.tokens.forEach((token) => {
        if (token.content && termsMatch(term, token)) sentences.add(token.sentence);
      });
      return sentences;
    };
    const requiredHits = option.required.map(hitsBySentence);
    const extraHits = option.extra.map(hitsBySentence);
    const windows = Math.max(1, prepared.sentences.length);
    let best = { coverage: 0, weight: 0, window: -1, matched: new Set() };
    for (let start = 0; start < windows; start++) {
      const inWindow = (set) => set.has(start) || set.has(start + 1);
      let weight = 0;
      const matched = new Set();
      option.required.forEach((term, i) => {
        if (inWindow(requiredHits[i])) {
          weight += term.weight;
          matched.add(term.canon);
        }
      });
      let bonus = 0;
      option.extra.forEach((term, i) => {
        if (inWindow(extraHits[i])) {
          bonus += term.weight;
          matched.add(term.canon);
        }
      });
      let coverage = Math.min(1, (weight + bonus) / totalWeight);
      // "does not contain" is not "contains": a negation the point lacks, just
      // before a matched term in the same sentence, halves the credit.
      if (coverage > 0 && !option.negates && isNegated(prepared, start, option, matched)) coverage *= 0.5;
      // ...and "has no effect" is not answered by a sentence with no negative in it.
      if (coverage > 0 && option.negates && !prepared.tokens.some((t) => t.negation && (t.sentence === start || t.sentence === start + 1))) coverage *= 0.6;
      if (coverage > best.coverage) best = { coverage, weight: weight + bonus, window: start, matched };
    }
    return best;
  }

  // The point's own text split into words and gaps, flagged for highlighting.
  function pointParts(text, options, matched) {
    const parts = [];
    let last = 0;
    const re = /\d+(?:[.,]\d+)*|[A-Za-zÀ-ɏ][A-Za-zÀ-ɏ0-9'’]*(?:-[A-Za-z0-9]+)*/g;
    let m;
    const terms = options.flatMap((option) => option.required.concat(option.extra));
    while ((m = re.exec(text))) {
      if (m.index > last) parts.push({ text: text.slice(last, m.index) });
      const token = makeToken(normaliseText(m[0]));
      const term = terms.find((t) => t.canon === token.canon || t.stem === token.stem);
      parts.push({ text: m[0], key: Boolean(term), matched: Boolean(term && matched.has(term.canon)) });
      last = m.index + m[0].length;
    }
    if (last < text.length) parts.push({ text: text.slice(last) });
    return parts;
  }

  // A long point has more key terms than anyone repeats word for word, so
  // several matched terms together also earn it.
  function creditFor(coverage, weight) {
    if (coverage >= 0.6 || (coverage >= 0.4 && weight >= 3.5)) return 1;
    if (coverage >= 0.34 || (coverage >= 0.2 && weight >= 2.5)) return 0.5;
    return 0;
  }

  // "Controls what enters and leaves the cell: A / Storage: B": the answer is a
  // letter from a diagram, which words cannot be matched against.
  function isLabelKey(model) {
    const lines = String(model || "").split(/\n+/).map((line) => line.trim()).filter(Boolean);
    const labels = lines.filter((line) => /[:=]\s*\(?[A-Z]\)?\.?$/.test(line) || /^[A-Z]\.?$/.test(line));
    return lines.length > 0 && labels.length >= Math.ceil(lines.length / 2);
  }

  /**
   * markAnswer({ answer, model, marks, schemePoints, question }) ->
   *   { earned, marks, needed, confidence: "high" | "low", points: [{ text, credit, coverage, parts }] }
   */
  function markAnswer(input) {
    const marks = Math.max(0, Number(input.marks) || 0);
    const scheme = Number(input.schemePoints) || schemeCount(input.model);
    const pointTexts = isLabelKey(input.model) ? [] : splitPoints(input.model, { lists: scheme > 1 });
    const questionTokens = contentTokens(input.question || "");
    const prepared = prepareAnswer(input.answer);
    const answered = prepared.tokens.some((t) => t.content);

    const points = pointTexts.map((text) => {
      const options = analysePoint(text, questionTokens);
      let best = { coverage: 0, weight: 0, matched: new Set(), option: options[0] };
      const matchedAny = new Set();
      if (answered) {
        options.forEach((option) => {
          const result = scoreOption(option, prepared);
          result.matched.forEach((canon) => matchedAny.add(canon));
          if (result.coverage > best.coverage) best = { ...result, option };
        });
      }
      return {
        text,
        coverage: Math.round(best.coverage * 100) / 100,
        credit: creditFor(best.coverage, best.weight),
        parts: pointParts(text, options, matchedAny),
      };
    });

    if (!points.length || !marks) {
      return { earned: 0, marks, needed: 0, confidence: "low", points };
    }

    let earned;
    let needed;
    if (points.length === 1) {
      // A single-point answer (a definition, a one-line fact) earns in proportion.
      needed = 1;
      // Short answers ("Fallopian tube") are right or wrong; longer ones earn in proportion.
      const shortAnswer = contentTokens(pointTexts[0]).length <= 3;
      const share = Math.min(1, points[0].coverage / 0.7);
      earned = marks === 1 || shortAnswer
        ? (points[0].coverage >= 0.55 ? marks : 0)
        : Math.floor(marks * share + 0.35);
    } else {
      const sp = scheme;
      needed = sp >= 1 && sp <= points.length
        ? sp
        : points.length <= 3 ? points.length : Math.max(3, Math.ceil(points.length * 0.55));
      needed = Math.max(1, Math.min(needed, marks));
      const credit = points
        .map((p) => p.credit)
        .sort((a, b) => b - a)
        .slice(0, needed)
        .reduce((sum, c) => sum + c, 0);
      earned = Math.floor(marks * Math.min(1, credit / needed) + 0.35);
    }
    earned = Math.max(0, Math.min(marks, earned));

    // Long model answers are samples: a good answer can make points the sample
    // does not, so a low score on a substantial answer is worth a second look.
    const answerWords = prepared.tokens.filter((t) => t.content).length;
    const confidence = !answered
      ? "high"
      : (points.length > 8 && earned < marks) || (answerWords >= 25 && earned < marks * 0.5)
        ? "low"
        : "high";

    return { earned, marks, needed, confidence, points };
  }

  root.AnswerMarker = { markAnswer, splitPoints, termsMatch: (a, b) => termsMatch(makeToken(normaliseText(a)), makeToken(normaliseText(b))) };
})(typeof window !== "undefined" ? window : globalThis);
