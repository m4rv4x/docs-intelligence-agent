# Failure Analysis

This document records failures, false starts, and anti-patterns.

## Known failure modes to avoid

### 1. Autonomy theater
Symptoms:
- impressive sounding claims
- unclear real utility
- noisy activity without user-visible value

Countermeasure:
- require visible artifacts and concrete validation

### 2. Generic agent positioning
Symptoms:
- project can do "everything"
- no memorable specialization
- weak public story

Countermeasure:
- keep the docs-intelligence wedge explicit

### 3. Maintainer-hostile PRs
Symptoms:
- too large
- too many unrelated changes
- no rationale
- no validation

Countermeasure:
- small diffs, explicit tradeoffs, easy review path

### 4. Cosmetic churn
Symptoms:
- renamed files without value
- formatting-only churn
- micro-refactors with no narrative benefit

Countermeasure:
- enforce a visible-value filter before changes

### 5. Trust decay through overclaiming
Symptoms:
- acting more certain than warranted
- calling proposals "fixed" too early
- overstating benchmark or impact results

Countermeasure:
- separate facts, assumptions, risks, and recommendations
