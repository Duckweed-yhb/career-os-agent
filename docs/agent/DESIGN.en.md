# ArmilGrid Agent · Design

> Version: v0.1 (draft, pending review)
> Status: planning stage — no development yet
> One document answers three things: what this agent can do, how it is put together, and how far your Python has to go before building it yourself.
> Related: [README.en.md](../../README.en.md) (front page) · skill layer [SKILL.en.md](../../SKILL.en.md) (capability source) · [methodology.en.md](../../references/methodology.en.md) (decision rules and data discipline)

---

## Contents

- [Part I — Capabilities](#part-i--capabilities)
- [Part II — Architecture](#part-ii--architecture)
- [Part III — Python prerequisites](#part-iii--python-prerequisites)
- [Appendix — Mapping to the skill layer](#appendix--mapping-to-the-skill-layer)

---

## Part I — Capabilities

> **In one line**: ArmilGrid Agent is the agent-side upgrade of this repository's skill layer — it keeps the nine career modules and adds three new layers (proactive orchestration, cross-session memory, a visual dashboard), turning "you ask, it answers" into a career coach that runs on its own.
> **Status legend**: ⚪ to confirm / 🟢 settled / 🔵 in progress

### 1.1 Capability overview

```
ArmilGrid Agent (three layers)
├── Agent runtime (kernel, required)
│   ├── Intent parsing      goals, background, emotions → tasks
│   ├── Planning            multi-step flow (role → gaps → project → course)
│   ├── Tool calls          the nine career modules as tools
│   ├── Reflection          write-back, difficulty calibration, re-routing
│   └── Follow-up           cross-session resume, reminders, reviews (opt-in)
│
├── Tool layer (nine modules, pluggable)
│   ├── Role radar          ├── Gap analysis
│   ├── Project generator   ├── Course builder
│   ├── Portfolio           ├── Resume gen & review
│   ├── Mock test + interview ├── Company intel
│   └── Full pipeline simulation
│
└── Memory and data layer
    ├── Session memory      context of the current conversation
    ├── Long-term profile   career-profile (profile, goals, projects, difficulty)
    ├── Vector index (RAG)  resumes / courses / reviews, searchable
    └── Progress            lesson checkmarks, milestones

Cross-cutting: dashboard (radar / progress / roadmap) · local data ownership · exportable
```

### 1.2 Runtime (kernel) capabilities

| Capability | What it does | Status |
|------|------|:---:|
| Intent parsing | Reads target role, experience level, time budget and emotional signals from natural language | ⚪ |
| Planning | Drives the multi-stage flow (role → gaps → project → course) automatically | ⚪ |
| Tool calls | Wraps the nine modules as tools, calls them on demand, parses results | ⚪ |
| Reflection | Writes back after each stage, shifts difficulty on user feedback, re-routes | ⚪ |
| Follow-up | Resumes last progress across sessions, reminds at milestones, stage reviews (opt-in) | ⚪ |
| Unified contract | One schema for tool input/output — auditable, rollback-able | ⚪ |

### 1.3 Tool layer (the nine career modules)

> All inherited from the skill layer, upgraded from "a flow inside a prompt" to "structured tool interfaces".

#### 1.3.1 Role targeting and capability radar

- Reads interests and background, locks 1–3 target roles, and produces a six-axis radar (language & frameworks / data & storage / engineering practice / architecture / domain knowledge / soft skills).

#### 1.3.2 Skill gap analysis

- Compares the current level against the role's requirements, ranks gaps by impact × urgency, and attacks the critical 20% first.

#### 1.3.3 Project generator

- Generates industrial-complexity project ideas aimed at the gaps — stack, predicted difficulties, acceptance criteria; no toy projects.

#### 1.3.4 Course builder

- Splits a chosen project into learning-by-doing Markdown lessons; each lesson carries a knowledge increment plus a project increment, with checkable acceptance criteria.

#### 1.3.5 Portfolio builder

- Turns projects into resume highlights: bullet rewrites plus a GitHub README guide.

#### 1.3.6 Resume generation and review

- Generation: drafts a version from the profile, projects and course sign-offs, one per role, and emits structured JSON for the local editor (`tools/resume-builder/index.html`).
- Review: scores across six dimensions (scannability / results over duties / role fit / project description / differentiation / polish) and lists issues as must-fix, should-fix, nice-to-have.

#### 1.3.7 Mock written test and interview

- Test: timed questions, scored one by one. Interview: one question at a time, feedback after each answer, strengths and gaps written back at the end.

#### 1.3.8 Company intelligence

- Verifies interview flow, written-test style and pay — every fact with a source and a date; fields without public data stay empty, never invented.

#### 1.3.9 Full pipeline simulation

- Apply → screening → written test → interview → outcome, with hard gates between stages and "simulated verdict" kept separate from "real advice".

### 1.4 Capabilities the agent adds (not in the skill)

| Capability | What it does | Status |
|------|------|:---:|
| Proactive follow-up | No need to retype commands each time; resumes last progress, reviews at milestones | ⚪ |
| Cross-session memory | Profile plus vector index, so the next session remembers your goals and progress | ⚪ |
| Task orchestration | One instruction drives a whole pipeline instead of one call per step | ⚪ |
| Visual dashboard | Capability radar, learning progress and roadmap rendered visually | ⚪ |
| Data ownership and export | Everything stays local; exportable as Markdown / JSON | ⚪ |

### 1.5 Capability tiers (suggested build order)

| Tier | Meaning | Capabilities |
|------|------|-----------|
| **P0 · Foundation** | Runtime and memory first | Intent parsing, tool calls, unified contract, profile persistence |
| **P1 · Core tools** | Straight port from the skill | Role targeting, gap analysis, project generation, course generation |
| **P2 · Job-hunt loop** | For real applications | Resume review, mock test and interview, portfolio |
| **P3 · Network and proactivity** | Needs the network and scheduling | Company intel, pipeline simulation, follow-up, dashboard |

> Suggestion: stand up the P0 skeleton and port the P1 tools to get the "role → project → course" minimal loop working; then add the job-hunt loop and the proactive layer.

### 1.6 Boundaries and trade-offs

| Trade-off | Why |
|------|------|
| Not a general assistant | Stays on career growth; does not compete with general-purpose AI |
| No invented company data | Inherits the skill's data discipline: unknown stays blank |
| The user's profile is authoritative | No guessing; self-assessment outranks inference |
| Follow-up is off by default | Respects the user; opt-in only |
| Sensitive data stays off the network | Profiles are local and exportable |

### 1.7 Open decisions

| # | Decision | My suggestion | Your call |
|---|---------|---------|---------|
| 1 | Runtime choice | An existing LLM framework (e.g. LangGraph) or a lightweight in-house orchestrator | ⚪ |
| 2 | Memory shape | Profile files + vector store (RAG) — files first, vectors later | ⚪ |
| 3 | Integration form | Standalone service / embedded in the assistant / both | ⚪ |
| 4 | Build a web dashboard | Yes, later; a visual panel is worth it | ⚪ |
| 5 | Relationship to Crafts-Island | Can join Crafts-Island as a "career growth islander" | ⚪ |

---

## Part II — Architecture

### 2.1 Positioning

Upgrade the skill layer from "an instruction file your assistant reads" to "a career growth agent that runs on its own":

- **Kernel (agent runtime)**: intent → planning → tool calls → reflection → follow-up
- **Tool layer**: the nine career modules wrapped as tools (a direct deposit from the skill)
- **Memory layer**: session memory + long-term profile + vector index RAG
- **Cross-cutting**: visual dashboard, data ownership and export

### 2.2 Architecture at a glance

```
Entry layer      chat (inside your assistant) · web dashboard · CLI / API
      ↓ natural language / intent
Agent runtime    intent → planning → tool calls → reflection → follow-up
                 (parse goals)  (multi-step)  (invoke tools)  (write back)  (resume)
      ↓ calls (unified schema)
Tool layer       role radar · gap analysis · project generator · course builder ·
                 portfolio · resume review · mock test & interview ·
                 company intel · full pipeline simulation
      ↓ read / write
Memory layer     session memory · long-term profile career-profile ·
                 vector index (RAG) · learning progress
```

### 2.3 Layers

#### 2.3.1 Agent runtime (kernel)

| Component | Responsibility |
|------|------|
| Intent parsing | Reads target role, experience level, time budget, emotional signals |
| Planning and orchestration | Multi-stage flow (role → gaps → project → course → job hunt), skippable and re-enterable |
| Tool calls | Calls the nine modules through a tool registry with a unified input/output schema |
| Reflection | Writes back after each stage, shifts difficulty on feedback, re-routes |
| Follow-up | Cross-session resume, milestone reminders, stage reviews (user can turn off) |

#### 2.3.2 Tool layer

Each career module is one tool with `name / description / input_schema / output_schema`. Rules:

- All inherit the skill's methodology (`references/methodology.md`)
- Results separate "inferred from general experience" from "verifiable facts"
- Sensitive data (e.g. real resume details) is processed locally only

#### 2.3.3 Memory and data layer

- Long-term profile: `career-profile.md` (profile, target roles, capability matrix, projects, difficulty preference) — the user's profile is authoritative
- Vector index: embeddings over resumes, courses and reviews, enabling RAG retrieval
- Progress: lesson checkmarks and milestones, read by the follow-up layer

### 2.4 One typical data flow

```
User: "I want to move from electrical engineering to backend, 10 hours a week, plan a year for me"
  ↓ intent: goal=backend · start=electrical · budget=10h/week · horizon=1 year
  ↓ planning: role → gaps → project → course
  ↓ tool calls: role radar (six-axis picture) → gap analysis (ranked) → project generator (2-3) → course builder
  ↓ reflection: calibrate difficulty to the time budget, write it into career-profile
  ↓ returns: route + first project + first lesson; marks "resume from here next time"
  ↓ (with follow-up on) next week it reviews lesson one and nudges you forward
```

### 2.5 From skill to agent

```
skill layer (today: SKILL.md instruction file)
   │  nine modules = candidates for tools
   │  methodology  = decision rules
   │  profile      = memory prototype
   ▼
ArmilGrid Agent (this project, the goal)
   │  tool layer: nine modules → tools (ported almost unchanged)
   │  kernel: new runtime (orchestration / reflection / follow-up / memory)
   ▼
A career growth agent that runs on its own
```

> Key insight: the module boundaries and methodology discipline accumulated in the skill stage are exactly the natural skeleton for tool-ification — the smoothest path for "a skill that later grows into an agent".

### 2.6 Stack options

| Layer | Candidates | Lean |
|----|------|------|
| Agent runtime | LangGraph / lightweight in-house state machine / reuse the host assistant | In-house lightweight first (simple, auditable) |
| LLM access | An existing model API | Same as the host |
| Vector index | Local vector store / keyword search to start | Keywords first, vectors later |
| Profile storage | Markdown / JSON | Markdown (continues the skill, user can take it away) |
| Visualisation | ECharts / HTML panel | Web dashboard later |

> These are suggestions and a planning direction, not a settled stack; to be finalised after review.

### 2.7 Roadmap

| Stage | Goal | Key actions | Status |
|------|------|---------|:---:|
| **Stage 1 · Foundation** | Agent skeleton | Runtime + intent parsing + unified contract + profile persistence | ⚪ |
| **Stage 2 · Port the tools** | Minimal loop | Role / gaps / project / course ported to tools; "role → project → course" works | ⚪ |
| **Stage 3 · Job-hunt loop** | Real applications | Resume review / mock test and interview / portfolio | ⚪ |
| **Stage 4 · Network and proactivity** | Smart follow-up | Company intel / pipeline simulation / cross-session memory / proactive reviews | ⚪ |
| **Stage 5 · Dashboard** | Visualisation | Capability radar, progress, roadmap | ⚪ |

### 2.8 Current state and next steps

#### 2.8.1 Repository layout

```
ArmilGrid/
├── README.md / README.en.md      front page (positioning)
├── SKILL.md / SKILL.en.md        skill layer core instructions (capability source)
├── references/methodology.md / *.en.md  scoring rules and data discipline
├── docs/agent/DESIGN.md / DESIGN.en.md  this document (capabilities + architecture + prerequisites)
└── preview/                      tech-stack board (single HTML page)
```

#### 2.8.2 Open questions

- [ ] Runtime choice (in-house lightweight vs. LangGraph)
- [ ] Memory shape (pace from profile files to a vector store)
- [ ] Integration form (standalone service / embedded / both)
- [ ] Whether to join Crafts-Island as a "career growth islander"
- [ ] Finalise the stack

#### 2.8.3 Next steps

1. Review this design and settle the open decisions in §1.7
2. Do stage one first: agent runtime skeleton + profile persistence
3. In stage two, port the four skill modules and get the minimal loop running

---

## Part III — Python prerequisites

> Answers one question: **to build this project, how far into `python-100-days` do you have to go?**
> Written 2026-10-18 · based on §2.6 stack options plus the structural kinship with hello-agents
> Conclusion: **`Day22`** (= the 20 lessons of "01 Python language basics" plus the first 2 of "02 Python in practice")

### 3.1 In one line

**`Day22` is enough to start**; add the **asyncio lesson in `Day31`**.

Why: this project has the same shape as hello-agents (agent runtime + tool set + memory), so **its Python bar is hello-agents' bar**.

`Day22` = `02-Python语言应用\Day22.对象的序列化和反序列化.md` (JSON / pickle)

### 3.2 Two premises to see first

1. **The project is still in the "planning stage"** ([README.en.md](../../README.en.md): "design stage — documents only") → **today's Python bar is lower than the final one**.
2. **The stack is not settled yet** (§2.6 is still a suggestion table, ending with "planning direction, not a settled stack") → this part follows the **current direction**; update it once the stack is finalised.

### 3.3 Acceptance criteria

| # | Ability | How to verify |
|---|---|---|
| 1 | Write functions and classes (a tool set is just a class's methods) | Write a class with two methods without references |
| 2 | File reads/writes + `try/except` (the "long-term profile + memory" live in files) | Read and write a `career-profile.json` |
| 3 | **JSON serialisation/deserialisation** | Save the nine modules' output as JSON and read it back |
| 4 | Read `typing` (`List/Dict/Optional/Any`) | Follow hello-agents chapter 4 without stalling |
| 5 | venv + pip + `.env` | Set up the environment yourself and run hello-agents ch1 |
| 6 | (Only needed for stage five) a data interface for the dashboard | Aggregate chart data with pandas |

**Lower bound**: run hello-agents' `code\chapter1\FirstAgentTest.py` (matches §2.2 and §2.3.1).
**Upper bound**: write a minimal agent of your own with tool calling plus memory files.

### 3.4 Mapping: which 100-days lessons go where

| 100-days | Content | Where it is used here |
|---|---|---|
| Day01–17 | Syntax → functions | Tool functions for the nine modules |
| Day18–20 | Object orientation | Agent runtime, tool set, dashboard data model |
| Day21 | File IO and exceptions | Profile, course files, review records ("data ownership") |
| **Day22** | **JSON serialisation** | The single exchange format for profile/courses/dashboard is Markdown/JSON (§2.2, last line) |
| Day31 (asyncio lesson) | Async | Proactive orchestration / concurrent tool calls |
| Day72–75 (as needed) | pandas | Dashboard data aggregation |

### 3.5 Skip for now

Django (Day46–60) · web scraping (Day61–65) · Excel/PDF/image/email (Day23–29) · machine learning (Day81–90)

> Databases (Day36–45) **depend on the choice**: if "memory shape" ends up as a vector store or a database, bring Day36–44 forward.

### 3.6 Gaps: not taught by python-100-days, but used here

| Gap | Note | How to fill it |
|---|---|---|
| **venv + pip, in earnest** | Needed on day one | One read-through of the commands (100-days mentions it only in passing) |
| **`.env` environment variables** | API key handling | `python-dotenv` |
| **Type hints (`typing`)** | Tool signatures, state machine definitions | Learn as you go |
| **pydantic** | Structured output/validation (the schema relies on it) | Learn as you go |
| **Vector index / embedding retrieval** | Required by §2.3.3 (keywords first, vectors later) | 100-days only has NumPy (Day66–68); pick a vector store separately |
| **Agent orchestration framework** | §2.6 candidates: LangGraph / lightweight in-house state machine | Learn as you go (in-house first, as this document suggests) |
| **Dashboard front end** | §2.6: ECharts / HTML panel | "Day32-33 web front-end intro" is not enough; add on top |

### 3.7 Current progress

Python position: **Day04 done** (2026-10-18) → **18 lessons to go** before Day22 (one per day).

- Progress file: `12-知识库\02-职业与发展\02-技术栈笔记\02-编程语言\Python\学习进度.md`
- Related plan: `12-知识库\00-成长系统\04-项目模式\01-ArmilGrid-agent化方案.md` (paths checked 2026-10-18; the old number 10 is now 01)

---

## Appendix — Mapping to the skill layer

```
nine modules of the skill layer   ──→  ArmilGrid Agent's tool layer (tools)
references/methodology.md         ──→  the agent's rule book (scoring / calibration / discipline)
career-profile.md                 ──→  the agent's long-term profile (upgraded to searchable memory)
courses / acceptance criteria     ──→  learning progress tracking (the follow-up layer's data source)
```
