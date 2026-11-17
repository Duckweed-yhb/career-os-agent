# What Comes Next

> Observed 2026-11-17. This document says what to build next, why, and what "done" means. It promises no dates.
> Every item is labelled **carrying layer** (needed whatever the model can do — keep thickening it) or **compensation layer** (covering for today's model — expect to delete it).

## 1. Where comparable projects already are

| Project | Scale | What it solves | Relation to us |
|---|---|---|---|
| `career-ops-hq/career-ops` | 70k+ stars | Turns Claude Code / Codex into a job-search command centre: scan portals → score listings A–F as 1–5 → tailor the CV → track applications | Our closest neighbour. It is an orchestration layer on someone else's CLI; we are a skill with our own methodology. It wins on scan/score/track; we win on targeting, gaps and courses |
| `srbhr/Resume-Matcher` | ~29k stars, Apache-2.0 | Paste a job description and it rewrites your master resume with local Ollama or your own model; the matching logic is open and readable | We can lay out a resume; we cannot match to a JD. That is our largest gap |
| `Reactive Resume` (rxresu.me) | MIT, 17–18 templates | Resume editor: template gallery, type/density/margins, PDF / DOCX / MD / JSON export, ATS check, self-hosting | We have two editions, PDF only (via print), no sharing. Its parameterised templates and our size/line-height/margin controls are the same idea |
| `JSON Resume` | Open standard, draft-07 schema | One JSON for a resume: 14 optional sections plus a `custom` escape hatch; themes and validators exist | Our resume JSON is private and imports nowhere. Aligning to it buys interoperability |
| `JobSpy` | Python scraping library on PyPI | Concurrent scraping of LinkedIn / Indeed / Glassdoor and more into a DataFrame | We do not scrape, and should not start. Hand it to JobSpy or the browser |

Conclusion: **scanning plus JD tailoring is where the field competes and where we are empty; layout and export are acceptable; targeting, gap analysis and courses are what we uniquely have.**

## 2. Priorities

### P0 — foundation; nothing else pays off without it

1. **A minimal eval set** (carrying layer)
   - Create `evals/scenarios.md`: 10–20 realistic scenarios ("electrical engineering undergrad switching to backend, 10 h/week, plan a year"; "resume only has coursework projects, aiming at QA").
   - Each scenario lists checkable points: invents experience or not, gives one executable next step, re-asks known facts, lands difficulty on the user's self-rating.
   - **Bare run comparison**: same scenario, once with the full SKILL, once with only the persona and command names; compare by hand.
   - Done when: ≥15 scenarios are recorded, and at least one rule has been deleted because the bare run did not lose.
   - Why first: without evals, no rule can be judged worthy of keeping — deleting becomes a gamble.

2. **Align the resume JSON with JSON Resume** (carrying layer)
   - Export `basics / work / education / skills / projects / languages`, with the Chinese and English editions in `custom` or as two files.
   - The editor imports and exports that shape without breaking local storage.
   - Done when: an exported file passes the official JSON Resume validator.

3. **Trim the README** (compensation layer)
   - README states only what works today; all forward-looking material moves into this document.
   - Done when: README no longer contains stage tables or "not started" wording.

### P1 — make it usable for a real job hunt

4. **Tailor to a job description** (carrying layer)
   - Input: a JD (text or link). Output: extracted keywords → mapping against the profile and resume → one version per role → match score (0–100) plus what is missing.
   - Rule: reorder real material only; never invent experience because a keyword missed (see the methodology's resume generation rules).
   - Done when: the same profile yields three explainable variants for three JDs, each able to justify its ordering.

5. **Upgrade the ATS check** (carrying layer)
   - The current nine checks are structural; add keyword coverage: JD requirements against resume hits, listing misses by priority.
   - Done when: coverage is reproducible (identical input, identical result) and does not depend on model sampling.

6. **Application tracking** (carrying layer)
   - One `applications.json` or Markdown table: company / role / stage / dates / next step / JD link / which resume version.
   - Stages reuse the pipeline names (apply → screening → test → interview → outcome) but record reality, not a simulation.
   - Done when: it can answer "how many processes am I in and where is each stuck".

### P2 — agent-ification, following the always-on trio

7. **Triggers and a router** (carrying layer)
   - Triggers: schedule (cron), email, calendar, group mentions — all normalised into one message stream.
   - Router: dedupe, merge bursts, priority by source (what you say directly comes first), and a decision on whether to disturb you.
   - Deterministic ceilings: daily cap, per-object cooldown, quiet hours; by default report only "done" and "needs your call".
   - Done when: a week of running produces ≤2 false alarms and one config switch turns it off.

8. **Persistent workflows and a cost ceiling** (carrying layer)
   - Tasks split into resumable steps that survive a crash; token and cache-hit accounting per turn.
   - Done when: recovery does not redo finished steps, and monthly cost is bounded and inspectable.

9. **Collapse the tools** (compensation layer)
   - Nine modules collapse to four tools: role targeting, gap analysis, project generation, course generation.
   - Company intel and pipeline simulation drop to the escalation ladder (search → browser → ask the user) instead of dedicated tools.
   - Done when: the removed tools show no measurable loss in the eval set.

### Deliberately not doing

| Not doing | Why |
|---|---|
| Accounts, cloud storage, public share links | Conflicts with "data stays local and exportable", and needs a server |
| DOCX generation | Printing to PDF is enough; add the `docx` library only when someone actually needs it |
| Our own job scraper | Compliance and maintenance cost; use JobSpy or a browser |
| A template gallery | Layout differences matter far less than content; revisit when there are real users |

## 3. Layer and exit conditions

| Item | Layer | When to delete or replace |
|---|---|---|
| Five-stage hard workflow, per-answer feedback format | Compensation | A bare run shows the model orders the stages sensibly on its own |
| Domain templates (web-fullstack etc.) | Compensation | The model no longer needs a skeleton to decompose a role |
| Nine tools → four | Compensation | Call logs show a tool below 5% of usage |
| Methodology rules (radar / anchors / six dimensions) | Carrying | Never delete; update alongside any rule change |
| Eval set, application records, resume JSON | Carrying | Never delete; keep thickening |
| Triggers, router, cost ceiling | Carrying | Never delete |

## 4. Licence note

`career-ops` and `Resume-Matcher` carry different licence terms (Resume-Matcher is Apache-2.0). This project borrows **ideas, dimensions and field structures** only, never their code, and cites sources with the observation date. `JSON Resume` is an open schema — implement it directly.

## 5. Order of work

One item at a time:

1. Stand up `evals/` with 15 scenarios
2. Align resume export with JSON Resume
3. Trim the README
4. JD tailoring plus ATS keyword coverage
5. Application tracking
6. Always-on trio (triggers, router, persistence and cost)
7. Collapse nine tools into four
