---
name: constraints-first-execution
description: Translate a request into an authorized, minimum-complexity execution plan with explicit requirements, exclusions, stop rules, and acceptance criteria. Use before implementing a multi-step task or proposing new agent infrastructure.
license: MIT
metadata:
  version: "0.2.0"
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

## Problem-first context contract (Kendall-derived)

Before choosing an AI tool or implementation, record: **who** encounters the problem, **when/where** it appears, **what** currently fails, **why** it matters, existing workarounds, and a measurable **so that** outcome. Use a short user story if useful: "As a [role], when [situation], I need [capability] so that [outcome]."

Identify the **Problem Owner** (accountable for the business problem and decisions), the **Context Curator** where ongoing source maintenance matters, and the implementing agent's delegated scope. A title or agent instruction does not confer organizational authority. Gather contradictory perspectives when material; do not silently pick one account.

**Good:** A team reports inconsistent internal answers; first identify conflicting source policies, affected employees, decision owner, and a success criterion, then propose the smallest authorized context-validation pilot.

**Bad:** "Deploy an enterprise chatbot and connect all systems" before identifying a problem, source owner, or access boundary.

**Stop / handoff:** If the business problem or authority is too uncertain for a consequential action, return the smallest discovery question and independently safe preparatory work rather than selecting an irreversible solution.

**Acceptance:** The proposed implementation traces to a real problem, source ownership, scope, and observable user outcome; no speculative infrastructure is introduced.
