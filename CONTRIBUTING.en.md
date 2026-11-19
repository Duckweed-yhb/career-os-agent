# Contributing to ArmilGrid

First off, thanks for taking the time to contribute! 🎉

## What you can contribute

- **Skill prompt improvements** — make the `/armil` commands smarter, add new sub-commands, or refine the decision logic.
- **Project recommendation rules** — new templates for target roles, tech stacks, difficulty calibration, or acceptance criteria.
- **Examples** — real conversation walkthroughs under `examples/`. A good example shows the full flow from `init` to a project recommendation.
- **Documentation** — fix typos, clarify wording, or improve the README.
- **Translations** — maintain or add localized docs (currently English and Simplified Chinese).

## Getting started

1. **Fork** the repository and clone it locally.
2. **Create a branch** with a descriptive name:

   ```bash
   git checkout -b feat/your-feature
   ```

3. **Make your changes.** Keep them focused on one topic per pull request.
4. **Commit** with a clear message:

   ```bash
   git commit -m "feat: add X"        # new capability
   git commit -m "fix: correct Y"     # bug fix
   git commit -m "docs: update Z"     # documentation only
   ```

5. **Push** and open a **Pull Request** against `main`.

## Conventions

- **One language per file.** English and Simplified Chinese content must not be mixed in the same file. Use `README.md` (Simplified Chinese) / `README.en.md` (English) as the reference pattern.
- **Keep examples reproducible.** Example conversations must match the current command set documented in the README.
- **Update the CHANGELOG.** Add an entry under `[Unreleased]` → `Added` / `Changed` / `Fixed` for every user-visible change.

## Adding a domain template

`templates/` holds one file per domain, used as the starting skeleton when generating projects or courses (currently `web-fullstack.md`).

1. Create `<domain>.md`, e.g. `ai-data.md` or `devops.md`.
2. Each template covers five parts: domain and typical roles, the canonical stack (with common alternatives), 3–5 project archetypes, the usual M1/M2/M3 milestones, and how the course is split.
3. Keep it lean — a template is a skeleton, not a full course.
4. When no template matches, the skill falls back to its general rules, so templates are always optional and a missing one never blocks generation.

## Pull request checklist

- [ ] The change addresses a single clear purpose.
- [ ] Language is consistent within each touched file.
- [ ] CHANGELOG.md is updated if the change is user-visible.
- [ ] The PR description explains *what* changed and *why*.

## Getting help

If you have questions or an idea you are unsure about, open an issue first — discussion before code saves everyone time.
