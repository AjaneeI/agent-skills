---
name: safe-parallel-delegation
description: Delegate independent authorized tasks to multiple agents without shared-state conflicts, uncontrolled model spend, or permission escalation. Use when parallel engineering, reviews, simulations, or evidence collection may accelerate a bounded session.
license: MIT
metadata:
  version: "0.1.0"
---

# Safe Parallel Delegation

## When to use
Use only when two or more tasks are demonstrably independent and execution environments can enforce bounded resources and permissions.

## Procedure
1. List authorized tasks and dependency edges. Separate critical-path gates from work that can be prepared offline.
2. Identify tasks that are independent in **state, permissions, inputs and scientific validity**. If a task depends on an unresolved methodological change, it is not independent.
3. Define one worker contract per task: inputs, allowed tools, explicit prohibited paths, output artifact, acceptance checks, resource/time budget, and stop conditions.
4. Assign isolated working directories, branches or worktrees. Reserve shared write targets for a single integrator. Do not launch multiple writers against the same mutable file.
5. Set maximum concurrent workers based on memory, runtime, provider limits and user-approved budget. Sequentialize local model inference if resource pressure is uncertain.
6. Each worker independently logs evidence. Treat self-reported success as unverified until checked.
7. Integrate by evidence: validate outputs, compare commit bases, resolve overlaps and run appropriate checks. A passing worker task does not automatically advance an entire research phase.
8. On a blocked worker, preserve its results and switch only if unaffected by the root cause.

## Stop conditions
Global safety incident, corrupted shared state, unauthorized tool request, resource ceiling exceeded, contaminated held-out data or conflicting irreversible actions.

## Deliverable
A [delegation manifest](references/work-contract.md) plus distinct work products and independent integration decisions.

## Principle
Parallelism is justified by *independent useful throughput*, not agent count.
