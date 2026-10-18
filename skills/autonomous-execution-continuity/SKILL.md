---
name: autonomous-execution-continuity
description: Preserve productive progress in an authorized multi-task autonomous session when a workstream is blocked by approval, dependency, tooling, or environment failure. Classify blocker scope, checkpoint evidence, switch only to independently authorized tasks, and stop for global safety issues or when no safe work remains.
license: MIT
metadata:
  version: "0.1.0"
---

# Autonomous Execution Continuity

## Purpose

Finish the greatest amount of **validated, authorized work** within an execution budget without diluting safety, research integrity, or approval requirements. A skill is guidance, not a permission grant or a runtime scheduler.

## Preconditions

- There is a user-approved goal, task list or bounded objective, plus an execution budget or stop rule.
- Applicable authority, tool permissions, privacy boundaries, and required approvals are known.
- The agent can preserve a durable checkpoint or clearly explain why it cannot.

If these are unknown, request only the missing authorization or stop rather than assuming consent.

## On encountering a blocker

1. **Classify scope.** Distinguish a *local workstream blocker* (specific approval, dependency, failed tool) from a *global stop* (explicit user stop, compromised security boundary, invalid authorization, systemic data-integrity failure, or uncertainty about whether other work is safe). See [blocker policy](references/blocker-policy.md).
2. **Checkpoint before switching.** Preserve the exact task, version/commit, actions attempted, observed errors, artifacts, current state, and a concise decision request. Never rewrite failed observations into successes.
3. **Respect the blocked boundary.** Do not rerun a frozen experiment, change a locked evaluator/methodology, add permissions, use a paid fallback, or retry a denied action unless separately authorized. An unresolved approval remains unresolved.
4. **Find independent work.** From the *existing authorized queue* select a task with no causal dependency on the blocked decision and no exposure to prohibited resources. Prioritize critical-path work with objective acceptance criteria.
5. **Continue only if safe.** Execute, verify, checkpoint, and repeat. Do not repeatedly ask the same unanswered question during one session. Do not create speculative tasks merely to fill time.
6. **Revisit only on change.** Resume a blocked stream only with evidence that approval or the dependency changed. Never infer approval from silence or elapsed time.
7. **End deliberately.** Stop on an applicable global stop, exhausted authorized work, expired execution budget, or explicit stop request. Provide a decision/evidence handoff, including unverified and incomplete work.

## Scheduling and concurrency

Work may be parallelized only where tasks, environments, resources, and state are isolated. One local blocker must not cause unrelated work to wait. Enforce the user's resource, model-call, time, and cost ceilings; avoid conflicting writes and surprise paid operations. Where timers or background execution are unavailable, report that limitation instead of claiming enforcement.

## Completion standard

For each stream report one of: **verified complete**, **blocked**, **failed with evidence**, or **not started**. Record evidence links, any decision needed, and the highest-priority safe next step. Only the authorized evaluation procedure may declare a research gate passed.

## Non-negotiable precedence

Higher-priority instructions, legal/security controls, the user's explicit limits, and experiment-specific protocols take precedence over this skill. A global safety stop is never bypassed by switching streams.

Use [blocker policy](references/blocker-policy.md) for detailed decision rules and [scenario checklist](https://github.com/AjaneeI/agent-skills/blob/main/tests/scenarios.md) for behavioral verification.