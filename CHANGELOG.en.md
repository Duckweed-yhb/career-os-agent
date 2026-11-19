# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.8.0] - 2026-11-19

### Changed

- Repository renamed to **ArmilGrid**, previously `career-os-agent`; the skill id `career-os` becomes `armilgrid`
- Command prefix `/CareerOS` becomes `/armil` (`/armil init`, `/armil generate course`, ...)
- Old names replaced across both languages, badges and examples; historical entries left untouched
## [Unreleased]

### Changed

- New `docs/ROADMAP.md` / `ROADMAP.en.md`: a survey of comparable projects (career-ops, Resume-Matcher, Reactive Resume, JSON Resume, JobSpy) turned into next steps, priorities and exit conditions; README gains a pointer
- `preview/` removed: the board page and its screenshot are gone, leaving only skill docs, examples and the resume tool
- README drops the "design preview" section and the board screenshot; the board HTML stays in `preview/`
- New standalone module "resume generation" and the `/CareerOS build resume` command: drafts from profile, projects and course sign-offs, one version per role, emitting structured JSON
- New `tools/resume-builder/index.html`: offline single-file resume builder with Chinese and English editions sharing one dataset, live A4 preview, local autosave, JSON import/export, print-to-PDF and nine ATS checks
- `references/methodology.md` gains resume generation rules; the tool entry in `docs/agent/DESIGN.md` becomes "resume generation and review"
- Dropped the decorative images: repository banner, social preview, the mobile screenshot and the board review report are gone; only one full-page screenshot remains (and the README header banner with it)
- Merged fragments: the template rules from `templates/README.md` now live in CONTRIBUTING's "Adding a domain template" section
- English twins added for the main docs: `docs/agent/DESIGN.en.md` and `references/methodology.en.md`, and the CI pair check now covers both
- Dropped the six derived screenshot slices in `preview/_shots`, keeping the full desktop and mobile shots
- Repo renamed from `career-os-skill` to `career-os-agent` (the old URL redirects): the skill layer stays at the root, agent design docs go under `docs/agent/`, and the tech-stack preview sits in `preview/`
- Added `docs/agent/DESIGN.md`: capabilities, architecture and Python prerequisites merged into one design doc
- `README.md` / `README.en.md` rewritten as a two-layer front page: skill install and usage on top, what the agent will do below
- Removed `SKILL.zh-CN.md` (merged into the Chinese main doc `SKILL.md`)
- Docs are now **Chinese-first**: `SKILL.md` becomes the Chinese main doc, the English original moved to `SKILL.en.md`, and `SKILL.zh-CN.md` was removed (assistants still load `SKILL.md`, so installation is unchanged)
- `FAQ` / `CONTRIBUTING` / `CODE_OF_CONDUCT` / `CHANGELOG` rewritten in Chinese, with English copies kept as `*.en.md`
- `templates/` docs and domain template, plus `.github/ISSUE_TEMPLATE/` forms, rewritten in Chinese
- Verification script and unit tests now check `SKILL.md` / `SKILL.en.md` and the Chinese/English doc pairs

## [0.7.1] - 2026-09-26

### Added

- Interaction Guidelines: Mindset Support — treats "too late to start" / "why didn't I start earlier" emotions as real signals: acknowledge, reframe ("you will never be younger than today"), judge regret by the replay test, convert anxiety into the smallest next action, never flatter
- Phase 5: Anti-probe checklist — every project must survive five deep questions (why this stack, extreme cases, personal contribution boundary, what you'd redo, the one proof number); true AND expandable, never coaching fabrication
- Mock written test: per-question mode labels (core-code / ACM), prep strategy split by time budget (modular problem list vs. high-frequency sets like LeetCode Hot 100 / CodeTop, labeled as community resources), and the three-pass spaced-repetition method
- Mock interview: delivery note (pacing, answer-first structure, fluency under follow-ups) added to per-answer feedback
- Phase 3: four-dimension tech-stack choice framework (job pool size, transferability, competition & learning cost, community & longevity), labeled as general-experience inference
- Phase 4: explicit Act → Sense → Reflect → Adjust learning loop
- Company Intelligence: design principle "research the company before applying — close the information gap first"

### Changed

- references/methodology.md: tech-stack selection dimensions, written-test prep strategy, anti-probe standard, mindset-support rules

## [0.7.0] - 2026-09-19

### Added

- New capability: Company Intelligence — research a specific company's interview flow, written-test style, and salary from public sources, with a hard rule to leave fields blank (never infer) when no public data exists
- New capability: Full Pipeline Simulation — run the whole recruiting pipeline (submit resume → screening → written test → interview → outcome) with the Skill playing the hiring side and hard gates between stages
- New commands: `/CareerOS company`, `/CareerOS simulate` (with natural-language triggers)
- SKILL.md / SKILL.zh-CN.md: Company Intelligence and Full Pipeline Simulation sections + Command Reference rows
- references/methodology.md: company-intel data discipline and pipeline scoring rules

## [0.6.0] - 2026-09-18

### Added

- Evidence, Defaults & Limitations section in SKILL.md / SKILL.zh-CN.md: recommendations are labeled as based on general experience (not official job data), fact vs. inference is separated, no job-offer promises, explicit handling of low-information domains
- Default profile rules: when the user declines to give background, proceed with an explicitly labeled default (zero-to-beginner, 8 hours/week, explore-first) instead of silently assuming
- New `references/methodology.md`: calculation rules for the capability radar, proficiency anchors, gap scoring, difficulty calibration, course granularity, resume review dimensions, mock interview feedback, and limitations

### Changed

- README is now Simplified Chinese by default; the English version moved to the new `README.en.md`; `README.zh-CN.md` removed (both READMEs link to each other)
- README: rewrite the intro in plainer language (remove template-style phrasing), fix the installation step to clone the whole repo (templates and examples are referenced by the Skill), and add Resume Review and Mock Interview & Written Test to the Core Modules list
- CONTRIBUTING.md: language-pattern reference updated to README.md / README.en.md

## [0.5.0] - 2026-09-17

### Added

- New capability: Mock Interview & Written Test — timed written tests (default 5 questions, rubric-scored after answering) and one-question-at-a-time interview practice (technical / behavioral / system design / HR rounds) with per-answer feedback and an end-of-session summary that feeds strengths and gaps back into the career profile
- New commands: `/CareerOS mock interview`, `/CareerOS mock test` (with natural-language triggers)
- SKILL.md / SKILL.zh-CN.md: Mock Interview & Written Test section and Command Reference rows

## [0.4.0] - 2026-09-17

### Added

- New capability: Resume Review — evaluate a resume across 6 dimensions (scannability, results over duties, target-role fit, project & tech description, differentiation, polish), output score + prioritized issues + rewrite examples, and link findings into the career profile and gap analysis
- New command: `/CareerOS review resume` (with natural-language triggers)
- SKILL.md / SKILL.zh-CN.md: Resume Review section and Command Reference row

## [0.3.0] - 2026-09-08

### Added

- Zero-base course example ([`examples/course-zero/`](examples/course-zero/00-course-overview.md)): overview + first two lessons, showing how the course adapts to a complete beginner
- Study schedule generation: weekly time budget → week-by-week lesson plan in the course overview

### Changed

- SKILL.md / SKILL.zh-CN.md: standard six-axis capability radar dimensions (Language & Frameworks, Data & Storage, Engineering Practice, Architecture & Design, Domain Knowledge, Soft Skills)
- SKILL.md / SKILL.zh-CN.md: proficiency anchors for beginner / intermediate / advanced assessment
- SKILL.md / SKILL.zh-CN.md: growth path planning — a 3-project serial path (Foundation → Capability → Showcase) per target role
- SKILL.md / SKILL.zh-CN.md: Phase 4 course schedule step (version 0.3.0)
- CI: version consistency check (SKILL ↔ README badge ↔ CHANGELOG)

## [0.2.0] - 2026-09-08

### Added

- YAML front matter (name, description, version)
- Phase 4 Course Builder — learning-by-doing Markdown courses
- Command Reference, Debug Protocol, Domain Templates sections
- Difficulty calibration bands and milestone feedback loop
- State persistence via `career-profile.md` and course progress
- Domain template library ([`templates/`](templates/README.md))
- Course example ([`examples/course/`](examples/course/00-course-overview.md))
- FAQ ([`FAQ.md`](FAQ.md))
- CI workflow verifying front matter, links, and changelog
- Code of Conduct, issue templates, repository banner, social preview assets
- Contribution guide ([`CONTRIBUTING.md`](CONTRIBUTING.md))
- Bilingual README with banner, badges, installation guide, and new commands

## [0.1.0] - 2026-09-08

### Added

- Initial project scaffold: repository, README description, MIT LICENSE
