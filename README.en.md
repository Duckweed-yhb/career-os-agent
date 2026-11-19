# ArmilGrid

> An operating system for your career growth. The skill is the recipe; the agent is the cook who can light the stove.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.8.0-blue.svg)](CHANGELOG.md)
[![Last Commit](https://img.shields.io/github/last-commit/Duckweed-yhb/ArmilGrid)](https://github.com/Duckweed-yhb/ArmilGrid)

**English | [简体中文](README.md)**

---

## What this is

ArmilGrid gives you a route, not a course list: lock a target role → find the skill gaps against that role → close them with one real project → split the project into Markdown lessons you build through → end up with something you can put on a resume.

The repository holds two layers:

| Layer | What it is | Status |
|---|---|---|
| **Skill layer** | A single `SKILL.md` instruction with nine modules, loaded by your AI assistant | Available (v0.8.0) |
| **Agent layer** | The nine modules turned into tools, plus a runtime, long-term memory, proactive follow-up and a dashboard | Design stage — documents only |

How they divide the work: the skill settles the methodology, module boundaries and data discipline; the agent grows orchestration on top of that foundation, moving from "you type a command, it answers once" to "it knows what the next step is".

## Skill layer: install and use

1. Clone the repository (or download and extract it):

   ```bash
   git clone https://github.com/Duckweed-yhb/ArmilGrid.git
   ```

2. Locate your AI assistant's skills directory:

   | Assistant | Skills directory |
   |---|---|
   | Claude Code | `~/.claude/skills/` |
   | Doubao Agent | `<workspace>/.skills/` |
   | Other assistants | See your assistant's documentation |

3. Put the whole repository inside a `armilgrid/` folder there — `templates/` and `examples/` are referenced by the skill automatically, so don't copy `SKILL.md` alone:

   ```bash
   # example (Claude Code)
   git clone https://github.com/Duckweed-yhb/ArmilGrid.git ~/.claude/skills/armilgrid
   ```

   The assistant loads only `SKILL.md`, which is the Chinese core instruction. For English instructions, rename `SKILL.en.md` over it.

4. Restart your assistant session and verify:

   ```text
   /armil init
   ```

   If you see the init welcome message, you are set.

## The nine modules

| # | Module | In one line |
|---|---|---|
| 1 | Target identification | Locks interests and background into 1–3 target roles, with a six-axis capability radar |
| 2 | Skill gaps | Role requirements against your self-assessment, ranked by impact × urgency |
| 3 | Project generator | Industrial-level projects aimed at the gaps; no toy projects |
| 4 | Course builder | The project split into learning-by-doing Markdown lessons, each with checkable acceptance criteria |
| 5 | Portfolio | Project → README guide + resume bullets + interview talking points |
| 6 | Resume review | Six-dimension scoring, issues tiered must-fix / should-fix / nice-to-have, with before → after rewrites |
| 7 | Mock test & interview | Timed questions scored one by one; interviews run one question at a time with feedback after each answer |
| 8 | Company intelligence | Interview flow, written-test style and pay, each fact carrying a source and a date; blanks stay blank |
| 9 | Full pipeline simulation | Apply → screening → written test → interview → outcome, with hard gates between stages |

Two modules need the network: `company` (company intelligence) and `simulate` (pipeline simulation). Offline they explicitly report "未查到公开信息" or fall back to generic role requirements — they never fabricate data.

## Common commands

```text
/armil init
/armil analyze [your resume or current skill list]
/armil generate project --focus=[specific tech, e.g. Redis/microservices]
/armil generate course [project]   # turn a chosen project into learning-by-doing lessons
/armil build resume [role]         # draft a resume from your profile, Chinese and English editions
/armil review resume [resume]      # review your resume and find what to improve
/armil mock interview [role]       # interview drill, one question at a time, with feedback
/armil mock test [role]            # timed written-test practice with scoring
/armil company [company] [role]    # research interview flow, test style and pay
/armil simulate [company] [role]   # run the full pipeline: apply → screening → test → interview
```

For a full walkthrough see [examples/frontend-to-fullstack.md](examples/frontend-to-fullstack.md); for questions see the [FAQ](FAQ.en.md).

## Agent layer: what exists today

Design documents only, no code — deliberately, so the boundaries and trade-offs are settled before any implementation.

| Document | Content |
|---|---|
| [docs/agent/DESIGN.en.md](docs/agent/DESIGN.en.md) | Design doc: capability list, the four layers and one typical data flow, stack options, roadmap, and the Python prerequisites for building it yourself |

Five-stage roadmap:

| Stage | Goal | Status |
|---|---|---|
| 1 · Foundation | Runtime + intent parsing + unified contract + profile persistence | Not started |
| 2 · Port the tools | Positioning / gaps / projects / courses ported to tools, minimal loop working | Not started |
| 3 · Job-hunt loop | Resume review / mock test & interview / portfolio | Not started |
| 4 · Network & proactive | Company intel / pipeline simulation / cross-session memory / review prompts | Not started |
| 5 · Dashboard | Capability radar, learning progress, roadmap | Not started |

## Repository structure

```
ArmilGrid/
├── SKILL.md / SKILL.en.md        # Skill core instructions (Chinese / English)
├── README.md / README.en.md      # This document (Chinese / English)
├── FAQ.md / FAQ.en.md            # FAQ
├── CONTRIBUTING.md / *.en.md     # Contribution guide
├── CODE_OF_CONDUCT.md / *.en.md  # Code of conduct
├── CHANGELOG.md / CHANGELOG.en.md
├── references/methodology.md / *.en.md  # Every scoring rule and data discipline
├── templates/                    # Domain templates: starting skeletons for projects and courses
├── examples/                     # Full conversation walkthrough + sample courses
├── docs/agent/DESIGN.md / DESIGN.en.md  # Design doc: capabilities, architecture, Python prerequisites
├── docs/ROADMAP.md / ROADMAP.en.md      # What comes next: peers, priorities, exit conditions
├── tools/resume-builder/index.html  # offline resume builder (form left, A4 right, zh + en, prints to PDF)
└── .github/                      # CI verification script and issue templates
```

Docs are Chinese-first: every main doc is Chinese with an English twin using an `.en.md` suffix. Never mix two languages in one file. `examples/` and `templates/` are reusable content skeletons and ship in Chinese only.

## Resume builder

`tools/resume-builder/index.html` is a single offline file: double-click it, no setup, no network.

- **One dataset, two editions**: a Chinese edition with education first and an optional photo, and an English edition with experience first. Switching changes the layout only
- **Form left, A4 right**: the right pane is exactly what prints; font size, line height, margins and accent colour are adjustable
- **Autosave**: content lives in browser local storage
- **JSON import / export**: for backups or moving machines; Markdown export for handing content back to the AI
- **Print to PDF**: choose "Print / Save as PDF", margins None, and enable background graphics to keep the accent colour
- **Nine ATS checks**: name, contact, summary length, bullet count, 40% quantified, consistent date format, 5–15 skills, and whether it fits one page — every failing item is listed on the spot

Where the content comes from: `/armil build resume` drafts it from the profile and projects, paste it into the editor for layout and PDF, then `/armil review resume` to score and iterate.

## What comes next

Anything not built yet lives in [docs/ROADMAP.en.md](docs/ROADMAP.en.md): where comparable projects already are, the priority order, and when each item should be deleted. The README only covers what works today.
## Repo history

This repo used to be called `armilgrid-skill`; it is now `ArmilGrid`. The skill layer was already here, and the agent layer grows straight out of its nine modules. The old URL redirects, so existing clones keep working without touching their remote.

## License

[MIT License](LICENSE)

---

Made with ❤️ by Duckweed-yhb
