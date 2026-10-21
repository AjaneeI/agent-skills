---
name: evidence-based-verification
description: Use when deciding whether a task, test, agent action, review, or delivery claim is supported, especially with stale evidence, incomplete traces, denied operations, or uncertain effects.
license: MIT
metadata:
  version: "0.1.0"
---

# Evidence-Based Verification

Decide what the evidence supports before calling work complete. This skill evaluates a claim; `evidence-preservation` retains its artifacts, and `verified-status-reconciliation` updates authoritative records afterward. It does not create another tracker or grant execution permission.

## Procedure

1. **Bind the claim.** Name the exact requested outcome, acceptance criterion, task, candidate commit/tree or artifact revision, configuration, environment, and observation window. Separate local correctness, live integration, publication, merge, deployment, and end-to-end acceptance. Evidence for one stage does not establish another.
2. **Inspect actual sources.** Read the relevant checks, command results, expected and observed effects, provider state, and reviewer findings. Distinguish direct observation, source-reported evidence, independent reproduction, and an agent self-report. A summary or test count without applicable evidence is insufficient.
3. **Check applicability.** Match identity, scope, versions, inputs, timestamps, and environment to the claim. A changed source, configuration, or acceptance rule invalidates affected conclusions until rechecked. Retain superseded results as historical evidence; do not relabel them as current. Hash agreement supports byte consistency, not authenticity, completeness, or correctness by itself.
4. **Check meaningful behavior.** Inspect both intended success and relevant negative cases using an observable oracle outside the completion narrative. Distinguish assertion failures from setup failures, skipped checks, missing logs, and interrupted runs. Preserve failures and denominators. A missing required observation is unknown, not a pass; no observed log is not proof of no action.
5. **Classify separate dimensions.** Record execution/effect state, acceptance-check result, business-task success, safety-test result, authority status, and review provenance. A safely denied forbidden action can pass its safety test while the business task remains incomplete. `needs_approval` is not permission to execute. A timeout after dispatch leaves the effect unknown until authoritative reconciliation; do not blindly retry.
6. **Assign a verdict.** Use `verified` only for the specifically bound claim whose required checks and evidence are satisfied. Use `failed` for observed nonconformance and `unverified` for insufficient, conflicting, or inapplicable evidence. Keep `denied` and `needs_approval` as distinct execution/authority states rather than disguising them as successful task completion. Identify exact limitations and any unrun checks.
7. **Take the smallest authorized next action.** Recheck only affected, repeatable validations within scope. A verification request cannot authorize a frozen experiment rerun, external write, purchase, or security change. Obtain a genuinely separate reviewer when required; label model-assisted, human, self-review, and independently rerun checks accurately. Update conclusions after changed evidence, preserving the previous record.

## Output

Use the [claim record](references/claim-record.md): scoped verdict, bindings, evidence, outcome dimensions, limitations, and next action. Return a supported conclusion or the precise missing observation. Do not manufacture confidence percentages or a universal reliability score.
