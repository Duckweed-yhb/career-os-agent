# CareerOS

![CareerOS banner](assets/careeros-banner.jpg)

> An operating system for your career growth.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.6.0-blue.svg)](CHANGELOG.md)
[![Last Commit](https://img.shields.io/github/last-commit/Duckweed-yhb/career-os-skill)](https://github.com/Duckweed-yhb/career-os-skill)

**[English](README.en.md) | [简体中文](README.md)**

---

## Overview

**CareerOS** is a skill for AI assistants that turns career growth into an executable path. Give it your background and goals, and it works out a route: lock in a target role, compare that role's requirements against your current skills, then close the gap by building a real project — the project gets split into Markdown lessons you work through one by one, and you end up with a portfolio you can actually show.

The whole flow adapts to your domain, experience level, and how much time you can spend each week — it won't hand you something far above or below where you are.

## Installation

1. **Clone the repository** (or download and extract it):

   ```bash
   git clone https://github.com/Duckweed-yhb/career-os-skill.git
   ```

2. **Locate your AI assistant's skills directory:**

   | Assistant | Skills directory |
   |---|---|
   | Claude Code | `~/.claude/skills/` |
   | Doubao Agent | `<workspace>/.skills/` |
   | Other assistants | See your assistant's documentation for the skills directory |

3. **Put the Skill inside a `career-os/` folder** in that directory — copy the whole repo, not just SKILL.md, because the course templates and examples live alongside it:

   ```bash
   # example (Claude Code): clone the whole repo into your skills directory
   git clone https://github.com/Duckweed-yhb/career-os-skill.git ~/.claude/skills/career-os
   ```

   The repo ships with both `SKILL.md` (English) and `SKILL.zh-CN.md` (Simplified Chinese) — your assistant loads whichever version fits your language; no manual file picking needed.

4. **Restart your assistant session** and verify:

   ```text
   /CareerOS init
   ```

   If you see the init welcome message, you are all set.

## Core Modules

Just like an operating system manages hardware resources, CareerOS manages your career resources:

### 1. Target Identification
- Parse your interests and background to lock in a high-potential target role.
- Generate a capability radar for that role.

### 2. Skill Gap Analysis
- Compare your current resume/skills against the target role requirements.
- Identify the critical missing links.

### 3. Project Generator
- **No toy projects.** Generate real-world project ideas with industrial-level complexity.
- Includes tech stack recommendations, difficulty predictions, and acceptance criteria.

### 4. Course Builder
- Turn any chosen project into a step-by-step **learning-by-doing** course.
- Generates the tech-stack learning route and the project development route, then splits the project into Markdown lessons — each with hands-on tasks and acceptance criteria.

### 5. Portfolio Builder
- Turn your projects into interview highlights.
- Resume bullet optimization and GitHub README writing guidance included.

### 6. Resume Review
- Scores your resume across 6 dimensions: scannability, results over duties, target-role fit, project & tech description, differentiation, and polish.
- Lists issues by priority (must-fix / should-fix / nice-to-have), with rewrite examples for the top issues.

### 7. Mock Interview & Written Test
- **Mock interview**: one question at a time, feedback after each answer, a summary of strengths and gaps at the end.
- **Mock written test**: timed questions for the target role, scored with concrete improvement notes after you answer.

## How to Use

Load the `CareerOS` Skill in your AI assistant, then try:

```text
/CareerOS init
/CareerOS analyze [your resume or current skill list]
/CareerOS generate project --focus=[specific tech, e.g. Redis/microservices]
/CareerOS generate course [project]  # turn a chosen project into learning-by-doing lessons
/CareerOS review resume [resume]     # evaluate your resume and find what to improve
/CareerOS mock interview [role]      # one-question-at-a-time interview practice with feedback
/CareerOS mock test [role]           # timed written-test practice with scoring
```

For a complete walkthrough, see [examples/frontend-to-fullstack.md](examples/frontend-to-fullstack.md). Have questions? See the [FAQ](FAQ.md).

## Why CareerOS?

- **Action-Oriented** — Switch from input mode to output mode.
- **Context-Aware** — Understands your level; never recommends something too easy or too hard.
- **Result-Driven** — Everything leads to one thing: a project you can put on your resume.

## License

[MIT License](LICENSE)

---

Made with ❤️ by Duckweed-yhb
