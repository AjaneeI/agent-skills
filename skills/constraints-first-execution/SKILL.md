---
name: constraints-first-execution
description: Translate a request into an authorized, minimum-complexity execution plan with explicit requirements, exclusions, stop rules, and acceptance criteria. Use before implementing a multi-step task or proposing new agent infrastructure.
license: MIT
metadata:
  version: "0.1.0"
---

# Constraints-First Execution

## When to use
Use at the beginning of a new implementation, automation, or research workflow, especially when an agent could overbuild or assume unstated permissions.

## Required inputs
Goal, owner-authorized actions, prohibited actions, existing system capabilities, success evidence, resource budget, and any external approval boundaries. Unknown authority is not implicit permission.

## Procedure
1. Write a short **contract**: objective, in-scope deliverable, non-goals, reversible actions, immutable constraints, and verified completion evidence.
2. Question whether each requirement is actually necessary for the user's goal. Do not silently delete explicit user requirements.
3. Remove optional work that does not improve the named acceptance criteria. Keep required safety and quality controls.
4. Simplify the proposed architecture before optimizing it. Prefer existing tools and direct workflows over new frameworks.
5. Order remaining tasks by dependency and evidence gates. Identify the next smallest reversible unit that proves progress.
6. Only after this sequence consider acceleration, parallelization, or automation. Estimate cost and complexity of each addition.
7. Make approval questions explicit and bounded. If authorization is unclear for a material change, preserve a proposal instead of executing it.

## Stop or escalate
Stop before access escalation, paid commitments outside budget, irreversible effects, frozen methodology changes, or actions outside explicit permission. Never treat speed goals as overriding safeguards.

## Deliverable
A brief requirements-to-actions table with **must**, **may**, **must-not**, owners, dependencies, and evidence needed to call each unit complete. Use [the contract template](references/contract-template.md) when traceability matters.

## Acceptance
Every proposed task has a named reason and an evidence condition; no new dependency or abstraction is justified solely by possible future needs.
