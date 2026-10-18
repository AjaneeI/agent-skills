---
name: statistical-calibration-freeze
description: Predeclare and calibrate a statistical analysis procedure before inspecting held-out experiment outcomes. Use for repeated-measures benchmarks, confidence intervals, uncertainty reporting, practical thresholds, and confirmatory comparisons.
license: MIT
metadata:
  version: "0.1.0"
---

# Statistical Calibration and Freeze

## Trigger
Use when designing inferential comparisons that could be biased by post-hoc analysis choices, nested repeats, small task banks, or uncalibrated uncertainty intervals.

## Inputs
Primary outcome and estimand, experimental unit, pairing structure, strata/families, randomization, missingness, repeat counts, and intended generalization population.

## Procedure
1. Specify estimand and task-level aggregation explicitly. Do not mistake repeated observations on the same task for independent task samples.
2. Identify all sources of dependence: tasks, task families, model configurations, repeated runs, and shared runtime conditions.
3. Design plausible **model-free simulations** spanning task difficulty, treatment heterogeneity, run-to-run variability, missing data, and unequal samples.
4. Evaluate proposed uncertainty method against coverage, false positives, bias and interval width. Record parameter grid, seeds, and test code.
5. Compare sensitivity methods only as preregistered; a plausible method is not automatically calibrated.
6. Freeze the chosen estimator/interval plus missing-data, exclusions, timeouts, failed harness runs, multiplicity, and practical decision thresholds **before** held-out exposure.
7. If a method cannot satisfy validity checks, report failure and seek methodology approval rather than searching until significance appears.

## Output
Versioned statistical analysis plan, simulation evidence, limitations, and clearly delineated confirmatory vs exploratory claims. Use [analysis plan checklist](references/plan-checklist.md).

## Prohibited
No outcome-dependent interval choice, pseudo-replication, retroactive exclusions, or interpreting a development pilot as confirmatory proof.
