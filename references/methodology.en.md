# CareerOS Recommendation Methodology

This document records the rules behind every judgement CareerOS makes: the capability radar, level assessment, gap ranking, difficulty calibration, course granularity, resume scoring, mock-interview feedback, company intelligence and full pipeline simulation. It makes each recommendation reviewable and auditable. **These are heuristics based on general industry experience — not an official standard, and not the hiring bar of any specific company.**

## Six-axis capability radar

- The six axes are fixed: language & frameworks, data & storage, engineering practice, architecture & design, domain knowledge, soft skills.
- Each axis scores 0–10, expressing how strongly the target role demands that capability, inferred from general role requirements and labelled "inferred from general experience" when shown.
- The radar describes the role, not the user. User levels go through the anchors below instead.

## Level anchors

- **Beginner**: can follow a tutorial but cannot start from a blank page; needs step-by-step guidance.
- **Junior**: can build independently, looks things up occasionally; stalls on debugging and design decisions.
- **Intermediate**: develops, debugs and explains trade-offs independently; can guide others.

Every assessment asks the user to self-rate by skill category. Never guess from a resume — the user's self-rating is the authoritative source for current level.

## Gap scoring and ranking

- Gap = role requirement strength × the user's shortfall at that level.
- Ranking uses impact × urgency: attack the 20% of gaps that deliver the largest gain, never a flat list.
- Evidence priority: user self-rating > course acceptance results > resume evidence; a resume is a reference, not a verdict.

## Difficulty calibration

- Average gap 1–2 → difficulty 1 (gentle); 3–4 → difficulty 2 (stretch); 5+ → difficulty 3 (challenge).
- Always offer both "current tier" and "one tier up" project options.
- Ask how the difficulty felt after each milestone; if the user says "too easy" or "too hard", shift everything one tier and record it in the profile.
- Difficulty is not the AI's call — the user's rating is.

## Stack selection dimensions

- When recommending or comparing stacks, assess four dimensions: job volume, transferability, competition and learning cost, community and lifecycle.
- Label conclusions "inferred from general experience", never official data; never quote specific market percentages.
- Give direction and trade-offs; the decision is the user's.

## Course granularity

- 1–3 hours per lesson; 6–20 lessons per course depending on project size.
- Every lesson must contain both a knowledge increment and a project increment; acceptance criteria must be runnable and demonstrable.
- Beginners get smaller lessons and more scaffolding; experienced users get denser lessons that land directly on the first real gap.

## Resume generation rules

- Real material only: profile, finished projects, course sign-offs, the user's own words. Mark gaps "to fill"; never invent companies, dates or numbers.
- One version per role: pick the 3–5 most relevant bullets for the target role from the same facts, each leading with a result and a number.
- One page first: 1–2 pages for Chinese, one page for English; cut secondary bullets rather than shrinking type.
- ATS-safe: single column, standard section headings, one date format, no text baked into images, no nested tables.
- Same facts across editions: wording may differ, but numbers, dates and titles must not.
## Resume review dimensions

Six dimensions, 0–10 each: scannability, results over duties, role fit, project and technical description, differentiation, polish. Total is the average. Issues are tiered must-fix / should-fix / nice-to-have, ordered by "fix this first for the biggest gain".

## Mock test and interview feedback rules

- Each test question is labelled by mode: core-code (fill a function body, LeetCode style) or ACM (import your own packages, handle your own IO); practise both, real tests use both.
- Test prep splits by time budget: with time to build foundations, work a modular problem list (archetype → variants); close to the interview, prioritise high-frequency sets (e.g. LeetCode Hot 100 / CodeTop, labelled as community resources). Grinding hards close to an interview is poor value.
- Three-pass spaced repetition: first pass builds recognition (read the solution if stuck for 3 minutes), second pass the next day rebuilds the structure and fills in code, third pass solves it independently on day three; the core habit is volume in one sitting plus a daily routine.
- Interviews run one question at a time; each answer gets one strength, one improvement, one reference answer structure, plus one delivery note (pacing, conclusion first, fluency under follow-ups).
- One round defaults to 8 questions (~30–40 minutes); it closes with an overall impression, top 3 strengths, top 3 gaps, written back to the gap list.
- When the user is stuck, hint first, reference answer second.

## Anti-probe standard for projects

- Every project must survive five questions: why this technical approach (alternatives and trade-offs), what breaks at the extremes, the boundary of personal contribution, what you would redo, and which number proves it works.
- Goal: every line on the resume is true and expandable; never help a user dress up experience they do not have.

## Company intelligence data discipline

- Source priority: official careers page > established recruiting platforms > interview write-ups / salary leaks.
- Every fact carries a source and a date; no source, no fact.
- Fields without public information stay empty and say "no public information found"; never fill them with general experience or inference.
- Salary ranges: report only when at least two independent sources agree; mark single-source findings as single-source; always state city, level and year; a posted range is not an offer.
- Interview flow and question direction: report only what public material actually says, with its freshness noted.

## Full pipeline simulation rules

- Stage verdicts: pass / hold / fail; hold and fail end the pipeline — improve and re-apply.
- Resume screening is the screener's view (fit, keywords, red flags), not the six-dimension resume review.
- Test and interview questions align with company intelligence first; when there is no public data, use generic role requirements and say so.
- Every piece of feedback separates "simulated verdict" from "real advice"; a simulation promises nothing about the real outcome.
- Behavioural questions avoid protected characteristics.

## Mindset support rules

- Treat "too late to start" / "why didn't I start earlier" / "I'm not good enough" as real signals: acknowledge the feeling, reframe ("you will never be younger than today"), judge regret by the replay test (would the outcome change? then let it go), and convert anxiety into the smallest next action in the current plan.
- Encouragement is perspective, not flattery: do not flatter, do not gloss over gaps; the honesty standard does not move.

## Limitations

- Role requirements and skill popularity come from general industry experience, not official job data, and change with the market; finishing a course promises no offer.
- Recommendations are learning vehicles; whether the output is recognised depends on the user's actual performance.
- Niche domains or thin samples are labelled as such; never manufacture certainty with percentages.
- This document governs every scoring rule; when a rule changes, update this document in the same change.
