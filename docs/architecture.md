# Architecture

## Goal

Build a narrow, credible GitHub-facing agent that improves repository documentation quality and public technical signal.

The system should favor usefulness and trust over maximum automation.

## Design principles

- small surface area first
- approval before non-trivial execution
- public artifacts matter as much as internal logic
- prefer explainable heuristics before opaque complexity
- keep the architecture easy to inspect in a README and PR

## System overview

```text
scheduler.py
  -> observer/
  -> planner/
  -> executor/
  -> memory/
  -> social/
  -> policies/
```

## Components

### observer/
Collects repository facts and change opportunities.

Planned responsibilities:
- scan repo structure
- detect stale references between code and docs
- detect missing setup instructions
- detect missing architecture explanation
- summarize CI and issue context when available

Implemented in v0.1 slice:
- detect `README.md`
- detect `docs/` presence
- count Markdown and Python files
- detect missing public docs for repo storytelling and trust artifacts
- score README quality using lightweight section heuristics

### planner/
Turns observations into ranked, bounded work items.

Planned responsibilities:
- estimate usefulness
- estimate blast radius
- estimate reviewability
- estimate narrative value
- choose the next small change worth proposing

Implemented in v0.1 slice:
- prioritize missing public docs as a low-risk, high-reviewability task

### executor/
Creates and validates small candidate changes.

Planned responsibilities:
- draft documentation patches
- run lightweight validation
- assemble diff summaries
- stop when confidence drops

### memory/
Stores durable repository context.

Planned responsibilities:
- repo profile snapshots
- cooldowns for repeated suggestions
- previously accepted vs rejected proposal notes
- maintainability metadata

### social/
Creates public-facing explanation artifacts.

Planned responsibilities:
- PR body drafts
- changelog entries
- lessons learned notes
- failure analysis notes
- devlog snippets

Implemented in v0.1.1 slice:
- render a Markdown observer report for async summaries and future cron delivery

### policies/
Holds explicit taste and safety rules.

## Proposed execution loop

1. observe repository state
2. identify top documentation or clarity gaps
3. rank candidate actions
4. propose one small change
5. wait for approval if write scope is meaningful
6. execute and validate
7. publish rationale and lessons

## Non-goals for v1

- broad codebase refactors
- unattended merges
- large-scale issue farming
- generalized coding-agent behavior
- high-complexity multi-repo orchestration

## Why this narrowness matters

A specialized, trustworthy system is easier to understand, easier to demo, and easier for other developers to believe in.
That is better for reputation than a broader but noisier autonomy claim.
