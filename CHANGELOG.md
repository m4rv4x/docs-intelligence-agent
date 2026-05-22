# Changelog

## Unreleased

### Changed
- README quality heuristics now parse actual Markdown headings, ignore fenced code blocks, and accept common heading-level and capitalization variations

### Added
- Initial flagship repository skeleton
- Public manifesto README
- Repo-local AGENTS.md with public-builder rules
- Architecture, lessons-learned, and failure-analysis docs
- Initial policy files for engineering and safety guidance
- Repository observer that reports docs signal and missing public docs
- Planner that proposes a small docs-oriented next action
- Unit tests for the observer/planner slice
- README quality heuristics
- Markdown observer report rendering
- Example observer report artifact in docs
- Issue template for small repo improvements
- Pull request template with rationale, risk, tradeoffs, and validation
- Baseline GitHub Actions CI for compile, policy, and unit-test validation
