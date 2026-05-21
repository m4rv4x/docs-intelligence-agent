# Project Context

This repository is a public flagship project. Optimize for visible usefulness, technical credibility, and coherent long-term narrative.

## Project wedge
This repo is a **Docs Intelligence Agent**.
It should help repositories become easier to understand, safer to adopt, and easier to maintain.

Do not drift into a vague general-purpose autonomous engineer positioning unless the user explicitly asks for it.

## Working style
- Small PRs only
- Prefer reversible changes
- Avoid speculative abstractions
- Tests before refactors when practical
- Docs with every meaningful feature
- Prefer one strong improvement over many noisy edits
- Stop when confidence drops

## Public artifact expectations
For meaningful changes, update or consider updating:
- `README.md`
- `docs/architecture.md`
- `docs/lessons-learned.md`
- `docs/failure-analysis.md`
- `ROADMAP.md`
- `CHANGELOG.md`

## PR standard
When drafting PRs, include when relevant:
- What changed
- Why this change
- Alternatives considered
- Risk assessment
- Tradeoffs
- Validation

## Task selection filter
Prefer work that is:
- clearly useful
- publicly visible
- coherent with the repo's positioning
- low blast radius
- easy for a maintainer to review

Deprioritize:
- cosmetic churn
- generic autonomy demos
- noisy refactors
- low-value commit farming
- broad rewrites without proof of need

## Architecture rules
- `src/observer/` discovers state, drift, and opportunities
- `src/planner/` ranks and scopes work
- `src/executor/` drafts patches and validates them
- `src/memory/` stores repo profiles, cooldowns, and prior observations
- `src/social/` generates PR narratives, changelogs, and public reasoning
- `policies/` defines durable engineering and safety rules

## File conventions
- Public-facing docs should usually be written in English
- Keep modules small and easy to review
- Prefer plain JSON or dataclasses over premature framework choices
- If a feature is not validated yet, mark it explicitly as planned or experimental

## Commands
Current lightweight validation commands:
- `python -m compileall src`
- `python -m json.tool policies/engineering_rules.json > /dev/null`
- `python -m json.tool policies/safety_rules.json > /dev/null`

When tests exist, prefer:
- `pytest -q`

## Safety
- Do not open, merge, or push public-facing changes without explicit approval unless the user has clearly authorized that scope
- Keep scope tight and validation inspectable
- Prefer draft artifacts and proposals before high-confidence automation
