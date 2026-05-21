# Roadmap

## Phase 0 — Positioning and scaffolding
- [x] Create flagship repo skeleton
- [x] Write README manifesto
- [x] Add AGENTS.md rules
- [x] Add architecture, lessons, and failure-analysis docs
- [x] Add policy files for engineering and safety principles

## Phase 1 — Repository profiling
- [ ] Define a repo profile schema
- [ ] Store local metadata for usefulness, reviewability, and risk
- [ ] Add cooldown support for repeated suggestions

## Phase 2 — Observation layer
- [x] Implement repo scanner
- [x] Implement baseline README quality checks
- [x] Implement baseline public-doc gap detection
- [ ] Implement missing-architecture-note detection
- [ ] Implement setup-step clarity heuristics
- [ ] Implement docs/code reference drift checks

## Phase 3 — Planning layer
- [x] Rank a first candidate task based on missing public docs
- [x] Emit one small proposed task at a time
- [ ] Add explicit approval checkpoints

## Phase 4 — Execution layer
- [ ] Draft docs patches
- [ ] Run lightweight validation
- [ ] Generate diff summaries
- [ ] Add self-review before proposing a PR

## Phase 4.5 — Reporting and GitHub hygiene
- [x] Render markdown observer reports
- [x] Add PR template
- [x] Add issue template
- [ ] Publish issue labels and contribution conventions
- [x] Add example observer report artifact to docs

## Phase 5 — Social layer
- [ ] Generate PR bodies with rationale sections
- [ ] Draft changelog entries
- [ ] Draft lessons learned and failure-analysis updates

## Phase 6 — Hermes integration
- [x] Point the `public-builder` profile at this repo by default
- [ ] Add safe cron jobs for observation and reporting
- [ ] Add a reusable repo-local workflow for propose/approve/execute

## v1.1 target
- [x] README heuristics
- [x] observer report markdown
- [x] issue template / PR template
- [x] stronger public roadmap
