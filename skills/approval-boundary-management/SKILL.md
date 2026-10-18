---
name: approval-boundary-management
description: Prepare precise human approval decisions without stalling unrelated work. Use when an agent encounters changes to authority, methodology, data access, budget, deployment, or any other explicitly reserved decision.
license: MIT
metadata:
  version: "0.1.0"
---

# Approval Boundary Management

## Trigger
Use when a requested action crosses an explicit human decision boundary; do not use to create new unnecessary checkpoints.

## Procedure
1. Determine the exact proposed action, who owns the decision, and which rule or authorization requires approval. Distinguish new approval from already-granted approval.
2. Capture a versioned proposal and a **decision packet**: current behavior, proposed delta, purpose, affected resources, risks, reversible/irreversible effects, alternative of doing nothing, and precise authorization requested.
3. Name the boundary: implementation, experiment invocation, production activation, publication, spending, or data/security. Approval for one is not approval for the others.
4. Ask for the decision once, with a concrete yes/no or bounded set of options. Avoid presenting a broad blanket consent as the only option.
5. Mark affected work **blocked awaiting decision**. Do not repeatedly request the same approval, reinterpret silence, or retry blocked operations.
6. If independent work remains authorized, hand its queue to the autonomous execution continuity process. A project-wide safety incident is not a local blocker.
7. Upon explicit response, preserve the decision record, scope, timestamp and reference; verify proposed actions still match it before executing.

## Anti-patterns
Never silently alter a scorer, unlock a guard, change billing, publish privately sourced artifacts, or widen agent tool permissions because it seems technically reasonable.

## Output
An auditable decision record with exact permitted next actions and separate not-authorized actions. See [approval record](references/decision-record.md).

## Definition of done
The owner can approve or reject an unambiguous versioned change without reverse-engineering a long debugging transcript.
