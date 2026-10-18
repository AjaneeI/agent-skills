---
name: evaluator-validity-audit
description: Audit whether a benchmark grader measures the intended behavior rather than superficial labels or leaked answers. Use before freezing evaluations, accepting model comparisons, or interpreting task-success claims.
license: MIT
metadata:
  version: "0.1.0"
---

# Evaluator Validity Audit

## Scope
Use on deterministic or model-assisted evaluators where grading defects can make incorrect answers look correct or legitimate alternatives fail.

## Procedure
1. Name the **construct** being measured: answer correctness, evidence grounding, required tool action, authority boundary, population scope, etc. Separate these dimensions.
2. Map each task to reference solutions, input assumptions, evaluator logic, accepted alternative behaviors, and explicit failure codes.
3. Test positive controls (genuinely correct), negative controls (wrong values, missing evidence, spoofed tool outcomes, impermissible actions), and valid alternatives (equivalent SQL, evidence paths or reasoning dispositions).
4. Verify that observation fields are derived from actual runtime evidence, not model-authored labels or untrusted result metadata.
5. Run controls without exposing held-out instances to the development agent. Preserve counterexamples and their original evidence.
6. Classify defects as **false acceptance**, **false rejection**, **ambiguous task contract**, or **unsupported but valid alternative**. Distinguish scorer defects from model or runtime failures.
7. Propose versioned changes with expected behavioral deltas; do not silently tune the grader after seeing confirmatory outcomes.
8. Freeze only when the stated validity gate passes, or explicitly report outstanding limitations and withhold claims.

## Output
An [audited case matrix](references/control-matrix.md) showing reference, adversarial, and alternative cases, expected vs observed reason codes, and unclosed defects.

## Stop conditions
Pause confirmatory interpretation for unresolved defects that materially alter measured success. Tests passing alone do not establish validity if important counterexamples are missing.
