---
name: evidence-preservation
description: Capture durable, inspectable provenance for engineering and AI experiments without rewriting failed runs. Use before and after experiments, evaluations, incidents, code changes, or other work whose results require independent verification.
license: MIT
metadata:
  version: "0.2.0"
---

# Evidence Preservation

## Purpose
Preserve enough evidence for another engineer to reconstruct what occurred without trusting an agent's narrative or storing unnecessary sensitive material.

## Inputs
Task version, environment, authorized tools, provenance requirements, permitted evidence destination, and privacy limits.

## Workflow
1. **Before execution:** snapshot the relevant commit/configuration, inputs, fingerprints, tool/model identities, budgets, run order, and expected observable outcomes.
2. **During execution:** collect original timestamps, tool calls, errors, return codes, outputs, scoring records, resource consumption, and user interventions to the extent actually observable. Distinguish traces from agent self-reports.
3. **After execution:** calculate stable hashes for preserved artifacts where feasible, record the result (pass, fail, blocked, unscored), and index files by source and version.
4. If diagnostic interpretation changes, create a dated **addendum** linked to the raw record. Do not edit the original run or overwrite failures.
5. Remove or redact credentials, private data, and secrets **only in a separately labeled publishable copy**. Keep any permitted originals in authorized secure storage; never commit secrets to a public repository.
6. Re-run deterministic checks only when the experiment's protocol permits them, and clearly separate diagnostic checks from fresh experiments.
7. Produce a concise manifest showing what is independently verified, what is inferred, and what remains unknown.

## Stop conditions
Stop evidence collection on unauthorized access or compromised storage. Do not invent missing provenance or claim no model calls merely because logs are absent.

## Output
[Evidence manifest](references/manifest-template.md) plus immutable source artifacts and a separate analysis note.

## Pass criteria
Every reported claim points to an artifact or is explicitly marked as interpretation, estimate, or unverified.

## Context provenance and example controls

For any context-dependent agent workflow, also record the **source owner**, origin, last verification date, applicable version or policy effective date, reliability, permitted sharing scope, and a clear refresh trigger. Where source claims conflict, preserve the disagreement and route the decision to the authorized Problem Owner/Context Curator; never blend them into a fictitious consensus.

**Good:** Keep the original failed run secure and immutable, write a dated explanatory addendum, and publish only a separately redacted summary with source hashes.

**Bad:** Modify a failed test record to show success, commit personal Gmail content to this public repository, or treat stale notes as a newer policy.

**Acceptance:** A reviewer can establish what was observed, which source or tool produced it, whether the evidence was authorized for storage, and what remains unknown. Missing metadata is reported rather than invented.
