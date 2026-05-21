---
name: Repo improvement
description: Propose a small, reviewable repository improvement with visible public value.
title: "improve: "
labels: [enhancement]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem
      description: What is weak, missing, confusing, or stale?
    validations:
      required: true
  - type: textarea
    id: evidence
    attributes:
      label: Evidence
      description: Point to files, screenshots, CI output, or concrete examples.
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed direction
      description: What small, reviewable improvement should be made?
    validations:
      required: true
  - type: dropdown
    id: risk
    attributes:
      label: Risk level
      options:
        - low
        - medium
        - high
    validations:
      required: true
  - type: textarea
    id: tradeoffs
    attributes:
      label: Tradeoffs
      description: What are we choosing not to do, or what downside comes with this change?
  - type: textarea
    id: validation
    attributes:
      label: Validation plan
      description: How should this be checked once implemented?
