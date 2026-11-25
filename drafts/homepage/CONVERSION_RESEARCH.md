# Study-app conversion research (for barebones.ie homepage)

Researched 2026-11-24 via web search and live page fetches. Rule applied: every number has a source link; anything else is marked unverified. **Headline finding: almost no study site publishes sign-up conversion rates.** What exists is user counts, a few A/B results (mostly Duolingo), and tactics visible on live pages.

## 1. Public numbers

| Claim | Source | Quality |
|---|---|---|
| Duolingo: moving the sign-up screen back a few steps (lesson first) gave about +20% DAU. Later soft/hard wall refinements added +8.2% DAU about three years on. | [First Round Review, Duolingo A/B tenets](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker.md) (also repeated by [Taplytics](https://taplytics.com/blog/duolingo-ab-test-onboarding)) | Primary interview, company-reported. Strongest sign-up-timing evidence found. |
| Duolingo: current-user retention +21% over 4 years; 7+ day streak share of DAU up almost 3x to over half; leaderboards raised learning time 17%; referral (free month) added only 3% new users. | [Lenny's Newsletter](https://lennysnewsletter.com/p/how-duolingo-reignited-user-growth) | Insider write-up. Retention, not sign-up. |
| Knowt: 519% TikTok growth H1 to H2; grew from 13,000 users on organic posts, then spent a reported six figures a month on TikTok ads. Site claims 50% of AP students use it. | [TikTok Academy case](https://omg.tiktokacademy.com/student/page/3649444-how-knowt-used-tiktok-to-grow-519-in-a-single-year), [knowt.com](https://knowt.com/) | Platform marketing page; brand-reported. Knowt's own site shows conflicting user counts (about 9.1M vs 5M). |
| Gizmo: over 13M users in 120+ countries, up from 300K+ in 2023; uses streaks, leaderboards, limited lives. | [TechCrunch, Apr 2026](https://techcrunch.com/2026/04/15/ai-learning-app-gizmo-levels-up-with-13m-users-and-a-22m-investment/) | Press. Article does not name channels or conversion. |
| Seneca: claims 14M+ users, 800+ free courses; hero now says 15M students. | [Seneca about](https://senecalearning.com/en-GB/about/), [live homepage](https://senecalearning.com/en-GB/) | Company claim. |
| Save My Exams: "over 3 million people every month". | [Publift/SME pages via search](https://www.savemyexams.com/learning-hub/sme-articles/how-many-people-use-save-my-exams/) | Company claim; conflicting figures (2.5M vs 3M). Revenue estimates online are modelled, unverified. |
| Studyclix: claims 250,000+ students and 90% of teachers (LinkedIn); earlier profile said 136,000 unique visitors a year and 3,000+ daily users. | [Silicon Republic](https://siliconrepublic.com/start-ups/tech-start-up-of-the-week-studyclix-ie) | Self-reported and dated. |
| Examinaite (Irish): 1,000+ users, grew by teacher word of mouth; free tier, then EUR 2.99 and 6.99 a month. | [Irish Times, Dec 2025](https://www.irishtimes.com/business/innovation/2025/12/04/teacher-quit-job-to-build-personalised-ai-revision-platform-for-leaving-cert/) | Founder quote. |
| Signup wall: roughly 20% bounce at a forced-signup wall on first launch (Phiture); one indie tool went from 3% to 30% by removing it. | [Phiture](https://phiture.com/?p=82267), [Indie Hackers](https://www.indiehackers.com/post/i-built-a-saas-for-photographers-and-watched-everyone-leave-before-signing-up-heres-what-i-changed-f27e646ece) | Consultancy claim and one anecdote. Directional only. |

**Not found (do not cite anything for these):** sign-up conversion rates for Quizlet, Seneca, Save My Exams, Studyclix, Brainly, Chegg, Khan, Photomath, Atom, Sparx, Revisely, Memrise, PMT. Quizlet's and Duolingo's live pages could not be fetched (403 / empty), so their current hero copy is unverified. Studyclix's homepage fetch returned nothing.

## 2. Observed homepage and onboarding tactics

- **Seneca** (live): headline "Learn 2x faster for free"; subhead "join 15 million students"; CTA "Get started for free"; level picker (GCSE, A Level, KS3...) then subject then "Start learning"; app ratings (2000+ App Store, 1500+ Google Play); free is unlimited, Premium is optional. [Source](https://senecalearning.com/en-GB/)
- **Save My Exams** (live): "Revision Notes, Past Papers & Exam Questions"; single CTA "Join now for free"; navigation organised by qualification, subject and exam board. No numbers near the top of the fetched text. [Source](https://www.savemyexams.com/)
- **Knowt** (live): "Every AI Study Tool You Need for a 4.0"; app-store badges plus "Continue on the Website" (no forced sign-up wording); proof is exam-season stats (700,000 of 1.3M AP students); explicitly "doesn't paywall" unlike Quizlet; "#1 free Quizlet alternative" in the page title. [Source](https://knowt.com/)
- **Photomath**: camera is the first screen, no tutorial, core step-by-step solutions stay free. [Google support](https://support.google.com/photomath/answer/14328660?hl=en)
- **Duolingo**: lesson before account; streaks and leaderboards as retention loops (sources above).
- **Gizmo**: streaks, limited daily lives, friend challenges.

## 3. Recurring patterns, ranked by evidence

1. **Value before account.** Strongest evidence (Duolingo +20% DAU, Photomath, Knowt's "Continue on the Website", Phiture and indie anecdotes). Ask for sign-up after the first meaningful action, ideally a moment that saves progress.
2. **Pick-your-exam first step.** Seneca (level, then subject, then start) and SME (nav by exam board) route the visitor to their own content in two taps. No A/B data, but universal across winners.
3. **"Free" as the headline claim, with a stated no-paywall promise.** Seneca ("for free"), SME ("Join now for free"), Knowt (free vs Quizlet paywall). Consistent, no conversion data.
4. **Specific, verifiable social proof.** Big user counts (Seneca 15M), store ratings, and exam-season usage share (Knowt). Treat numbers as company claims; use real ones only.
5. **Streaks and short loops for retention.** Duolingo data (7+ day streak share of DAU up almost 3x, 10-day streak lowers drop-off, with selection-bias caveat). Gizmo copies it. Retention, not sign-up.
6. **Short-form video as the engine, with a product built to be shown in a clip.** Knowt: organic first, paid later. Quizlet also partnered with TikTok creators ([Marketing Brew](https://www.marketingbrew.com/stories/2021/01/29/quizlet-partners-tiktok-education-integration)).
7. **Teacher and word-of-mouth distribution** (Examinaite, Studyclix's "90% of teachers" claim). Anecdotal.
8. **Referral bonuses are weak** (Duolingo +3%).

## 4. Fit for barebones (free, Leaving Cert, mobile, TikTok)

**Applies**
- Let a visitor answer a real past-paper question on the homepage, see it marked against the scheme, then prompt "save your progress" (pattern 1). This is barebones's strongest differentiator and costs no trust.
- Two-tap picker: subject, then level (Higher/Ordinary) or year, then straight into a question (pattern 2). Use Leaving Cert language: subject names, "2025 paper", marking scheme.
- Hero says plainly: free, real exam questions, marked against the official scheme. One CTA, thumb-reachable, wording like "Try a question" before "Sign up".
- Honest proof only: counts of questions and papers in the bank, years covered, any real usage figure. Avoid invented user numbers.
- A streak or "questions done" counter after sign-up for return visits.
- Landing-page-per-TikTok: link each video to the exact subject/question it showed (matches Knowt's creator-first approach).

**Does not apply**
- Paid ad scaling (Knowt's six-figure spend), app-store badges, leaderboards at scale, lives/limits (conflicts with free and open), referral discounts, enterprise or school-sales pages.
- SEO nav megamenus (SME) are for desktop search traffic, not TikTok phones.

## Caveats
Nearly all figures are company-reported. Duolingo's lift is DAU, not a sign-up rate. Test your own funnel: measure visit to first-question-answered, then answered to account created, as separate numbers.
