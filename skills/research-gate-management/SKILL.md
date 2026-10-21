---
name: research-gate-management
description: Use when an experiment, evaluation, integration, or release depends on prerequisite evidence or decisions, especially after protocol changes, unclear gate status, or pressure to advance prematurely.
license: MIT
metadata:
  version: "0.1.0"
---

# Research Gate Management

Track whether a specific downstream action has satisfied its existing prerequisites. Do not invent approval layers or replace the project owner's research protocol. A completed document, green unit suite, or deadline does not satisfy an unrelated evidence gate.

## Procedure

1. **Read the controlling contract.** Retrieve the approved objective, acceptance rules, owners, allowed actions, budget, frozen methodology, and current records. Distinguish a scientific evidence prerequisite, technical readiness check, and explicit human permission. None substitutes for another.
2. **Map only necessary dependencies.** For each gated action, record its prerequisite gates, observable acceptance, authoritative evidence source, version binding, decision owner, and permitted next action. Reuse existing gate identifiers and trackers. Resolve missing or cyclic dependencies as a planning defect without starting the affected experiment.
3. **Bind applicability.** Identify relevant data, scorer, model, prompts, configuration, source revision, environment, and invocation limits. Mark genuinely inapplicable fields with reasons. Changed inputs or rules require an impact assessment; invalidate only dependent conclusions. Preserve prior acceptance as historical or superseded rather than rewriting the record.
4. **Assess evidence and authority separately.** Use `evidence-based-verification` for claim adjudication when available. Ready evidence is not accepted evidence if an independent review or owner decision is required. Existing valid approval need not be requested again. An acceptance can carry forward only when its scope and bindings still apply, with that applicability recorded.
5. **Record the state precisely.** Distinguish `proposed`, `ready_for_review`, `accepted`, `blocked`, `failed`, and `superseded`. A blocked prerequisite blocks only dependent actions. Missing data, ambiguous invocation state, or uncertain authority remains unknown; it is not a failed scientific hypothesis or a passed gate. Preserve the actual result separately from readiness.
6. **Advance within the contract.** Proceed automatically through already-authorized gates whose required evidence and decisions are satisfied. Keep independent permitted work moving. Before bounded experimental execution, apply `one-shot-experiment-control`; an uncertain prior invocation cannot be treated as an unused attempt. Do not inspect protected held-out outcomes, change a scorer, replace a failed trial, or expand budget to make a gate pass.
7. **Checkpoint and resolve exceptions.** Record the exact unresolved prerequisite, observed evidence, affected action, smallest decision or authorized diagnostic, and resume condition. Escalate only new authority or material changes using `approval-boundary-management`. Do not repeat unchanged approval requests or silently waive required checks. Reconcile actual state before resuming; a message saying "continue" does not erase version or invocation limits.

## Output and boundaries

Use the [gate record](references/gate-record.md) in the existing source of truth. Return accepted gates with evidence, blocked dependent actions, and independent work still permitted. No new schedule, worker, trial, installation, publication, or approval is created by this skill. Evidence preservation, evaluator validity, statistical freezing, and experiment execution keep their separate roles.
