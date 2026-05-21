# Docs Intelligence Agent

[![CI](https://github.com/m4rv4x/docs-intelligence-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/m4rv4x/docs-intelligence-agent/actions/workflows/ci.yml)

A taste-driven GitHub maintenance system focused on one public wedge: **making repositories easier to understand, trust, and adopt**.

This project is not trying to be a magical "autonomous software engineer".
It is trying to be a **credible, useful, reviewable docs-and-maintenance agent** that helps builders and maintainers ship clearer repositories with better architectural signal.

## Positioning

**Docs Intelligence Agent** helps with high-signal repository maintenance:
- detect documentation drift
- propose architecture notes and examples
- improve README clarity
- surface failure modes and lessons learned
- draft small, reviewable PRs with rationale

The goal is visible value, not autonomy theater.

## Why this project exists

Most AI coding agents optimize for:
- more autonomy
- more commits
- more task completion theater

This project optimizes for:
- **visible usefulness**
- **technical credibility**
- **maintainer trust**
- **coherent public narrative**
- **small, reviewable improvements**

## Core workflow

The default operating loop is:

1. **Observe** repository state
2. **Rank** opportunities by usefulness, risk, and public value
3. **Propose** one small, high-value change
4. **Wait for approval** when write scope matters
5. **Execute** the change with validation
6. **Publish** rationale, tradeoffs, and lessons learned

In short:

`observe -> propose -> approve -> execute -> publish`

## What this repo should produce publicly

This repository is designed to generate public artifacts that people actually care about:
- good README upgrades
- architecture notes
- examples and onboarding docs
- failure analysis
- lessons learned
- benchmark notes
- clean PR bodies with clear reasoning

The project should look like a serious engineering system, not an AI gimmick.

## Scope for v1

Version 1 is intentionally narrow.

It focuses on a single wedge:

**Repository documentation intelligence**

That means:
- detecting stale or missing docs
- identifying unclear setup steps
- drafting architecture documentation
- generating reviewable improvement proposals
- keeping a coherent changelog and roadmap

## Repository structure

```text
src/
  observer/    repo scanning and doc-drift detection
  planner/     task selection and risk analysis
  executor/    patch drafting and validation
  memory/      local repo profiles and cooldowns
  social/      PR bodies, changelogs, devlogs
policies/      engineering and safety rules
docs/          public technical narrative
```

## Public engineering principles

- prefer simplicity
- avoid abstractions early
- small PRs only
- docs with every meaningful feature
- explain tradeoffs on important changes
- prefer reversible changes
- stop when confidence drops

## Near-term roadmap

- build repository profile format
- implement docs-drift scanner
- add README quality checks
- generate architecture note drafts
- create PR-body templates with rationale sections
- add approval-first GitHub workflow

See [ROADMAP.md](./ROADMAP.md) for the detailed sequence.

## Key docs

- [docs/architecture.md](./docs/architecture.md)
- [docs/example-observer-report.md](./docs/example-observer-report.md)
- [docs/lessons-learned.md](./docs/lessons-learned.md)
- [docs/failure-analysis.md](./docs/failure-analysis.md)
- [ROADMAP.md](./ROADMAP.md)
- [CHANGELOG.md](./CHANGELOG.md)
- [AGENTS.md](./AGENTS.md)

## Current status

The repo now includes a first real vertical slice:

- repository scanning for docs signal
- missing public-doc detection
- a planner that proposes the next small docs-oriented action
- unit tests for the observer/planner loop

### Current v1 behavior

The observer currently reports:
- whether a repo has a `README.md`
- whether a `docs/` directory exists
- Python and Markdown file counts
- a lightweight README quality score
- whether these public docs are missing:
  - `CHANGELOG.md`
  - `ROADMAP.md`
  - `docs/architecture.md`
  - `docs/lessons-learned.md`
  - `docs/failure-analysis.md`

The planner currently turns that into a bounded proposal:
- if key public docs are missing -> propose `add_missing_public_docs`
- otherwise -> emit a no-op / no-small-gap result

The social layer now also renders a Markdown observer report with:
- repo signal summary
- missing or weak public artifacts
- best next task
- risk and reviewability summary

### Validation

Current baseline validation commands:

```bash
python -m compileall src
python -m json.tool policies/engineering_rules.json > /dev/null
python -m json.tool policies/safety_rules.json > /dev/null
python -m unittest discover -s tests -v
```

These same checks now run in GitHub Actions on pushes to `main` and on pull requests.

## GitHub workflow defaults

The repository now includes:
- a pull request template with rationale, risk, tradeoffs, and validation
- an issue template for small, reviewable repo improvements
- a baseline GitHub Actions CI workflow that runs compile, policy, and unit-test checks
