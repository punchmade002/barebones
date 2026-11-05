// Exam-style written questions for PE pipeline outcomes without enough relevant
// authored coverage.
// Requires pe-pipeline-content.js to be loaded first.
(function () {
  if (typeof COURSE_DATA === "undefined") return;

  function q(marks, prompt, model) {
    return { type: "short", marks: marks, prompt: prompt, model: model };
  }

  function promptKey(prompt) {
    return String(prompt || "").trim().toLowerCase().replace(/\s+/g, " ");
  }

  var QUESTIONS = {
    "pe-ethics-fair-play-core": [
      q(10, "Evaluate how a school sports programme can protect fair play while still encouraging competitive performance.", "Set and teach clear rules, apply sanctions consistently, model respect for opponents and officials, and reward ethical decisions as well as results. Coaches should challenge cheating, intimidation and unsafe play immediately while giving performers a fair process to explain incidents. Competition remains meaningful when all participants face the same standards and welfare is not sacrificed for winning."),
    ],
    "pe-promoting-physical-activity-core": [
      q(12, "Design a school-based intervention to increase physical-activity participation among teenage girls, justifying four features of your plan.", "Begin with participation records, a questionnaire and a focus group so barriers are evidenced rather than assumed. Offer a choice of social and competitive activities, visible female leaders, affordable access and a timetable shaped by the group. Choice supports autonomy, friends support belonging, role models challenge stereotypes and practical changes remove cost or transport barriers."),
      q(10, "Explain how the COM-B model could be applied to improve physical activity in a sedentary adult population.", "Capability may be developed through beginner instruction and gradual progression; opportunity through safe local facilities, convenient sessions and social support; motivation through personally meaningful goals, feedback and enjoyable choice. An intervention should address the diagnosed barrier rather than use promotion alone. Attendance, retention and activity levels should be compared with a baseline."),
      q(10, "Evaluate two methods of measuring whether a physical-activity promotion programme has been successful.", "Attendance records objectively show reach and retention but do not reveal activity intensity or experience. Wearable or fitness data can quantify movement but may be costly and change behaviour while monitored. Questionnaires capture motivation and perceived barriers but are vulnerable to recall and social-desirability bias, so a mixed-method evaluation is strongest."),
    ],
    "pe-gender-physical-activity-core": [
      q(12, "Account for gender differences in physical-activity participation without relying on biological explanations.", "Family and peer socialisation, school activity choices, body image, kit, harassment, facility allocation, media visibility and access to leaders shape whether participation feels possible and valued. Hegemonic expectations may pressure boys away from activities labelled feminine and girls away from spaces coded masculine. These interacting social and institutional factors produce patterns that can change."),
      q(10, "Evaluate four strategies a sports organisation could use to improve gender equity in participation and leadership.", "Provide equal facility time and funding, varied activity choices, safe reporting procedures and transparent leadership pathways. Representative coaches and officials, inclusive kit and balanced media content strengthen belonging. Success should be measured through retention, experience and leadership representation as well as initial enrolment, otherwise a campaign may improve visibility without lasting access."),
      q(10, "Explain how media representation and body image may influence a young person's relationship with physical activity.", "Repeated emphasis on appearance, sexualisation or narrow athletic body types can increase self-consciousness and make activity feel like judgement rather than enjoyment. Visible diverse performers and coverage of skill, effort and health can broaden perceived possibility. Coaches should use inclusive language and avoid weight-based praise, while teaching critical media literacy."),
    ],
    "pe-business-enterprise-sport-core": [
      q(12, "Compare sponsorship, endorsement and merchandising and assess one risk associated with each.", "Sponsorship exchanges money or resources for association and exposure; a sponsor may pressure scheduling or damage reputation. Endorsement pays an athlete to promote a product, creating authenticity and conflict-of-interest risks. Merchandising sells branded goods and generates income but high prices, counterfeiting or poor labour conditions can undermine supporters and organisational values."),
      q(12, "Develop a brief enterprise plan for a community sport event, covering target market, value proposition, revenue, costs and risk.", "Identify a specific participant need and target group, then state why the event is more useful or attractive than alternatives. Revenue may include entry fees, sponsorship and concessions; costs include venue, insurance, officials, equipment, marketing and safety. Address demand, weather, safeguarding and financial risk, and evaluate success using participation, satisfaction, local benefit and surplus rather than revenue alone."),
      q(10, "Evaluate the effects of hosting a major sporting event on a local community.", "Benefits may include visitor spending, employment, facilities, civic pride and future participation. Costs include public subsidy, congestion, environmental pressure, security and facilities with little later use; revenue may leave through external firms. A sound judgement separates direct event income from wider impact and asks whether benefits remain local and continue after the event."),
    ],
  };

  Object.keys(QUESTIONS).forEach(function (outcomeId) {
    COURSE_DATA.chapters.some(function (chapter) {
      var outcome = (chapter.learningOutcomes || []).find(function (item) { return item.id === outcomeId; });
      if (!outcome) return false;
      var questions = outcome.questions || [];
      var seen = new Set(questions.map(function (question) { return promptKey(question.prompt); }));
      outcome.questions = questions.concat(QUESTIONS[outcomeId].filter(function (question) {
        var key = promptKey(question.prompt);
        if (!key || seen.has(key)) return false;
        seen.add(key);
        return true;
      }));
      return true;
    });
  });
})();
