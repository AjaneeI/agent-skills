---
name: code-bloat-triage
description: Find unnecessary code, dependencies, abstractions, and speculative features without blindly minimizing lines of code. Use during refactor reviews, AI-generated code audits, performance-focused cleanups, or pre-merge maintainability checks.
license: MIT
metadata:
  version: "0.1.0"
---

# Code Bloat Triage

## Objective
Reduce unjustified complexity **without sacrificing** correctness, necessary fault handling, accessibility, security, evidence, or maintainability.

## Triage workflow
1. Identify the actual user-facing or research requirement and its supported tests. Treat functionality and safety as constraints.
2. Inventory candidate bloat: duplicate logic, dead branches, unused dependencies, unnecessary layers, speculative configuration, redundant wrappers, and oversized generated files.
3. Measure only what is meaningful: cognitive complexity, dependencies introduced, code churn, duplicate coverage, review burden, and stability. Lines of code alone are not a quality metric.
4. For each candidate, ask: *What requirement or failure does this support?* Trace to evidence; retain it if necessary, even if verbose.
5. Order changes **delete unused**, **consolidate duplicate**, **simplify abstractions**, then **optimize hot paths**. Avoid a sweeping rewrite when one local fix suffices.
6. Make the smallest reversible change under tests; perform positive and regression checks. Preserve behavior and externally observed contracts.
7. Report benefits and tradeoffs. If removal weakens coverage or obscures behavior, do not merge the simplification.

## Guardrails
No deleting research provenance, validations, approval boundaries, security checks, or known failure examples merely to reduce file count. No unjustified new libraries for small features. Do not alter frozen benchmark semantics under a refactoring label.

## Output
[Decision register](references/triage.md) with candidates, reason, proof, change risk, and retained safeguards.

## Success criteria
A reviewer can justify each removal and confirm that supported behavior and trust boundaries are unchanged.
