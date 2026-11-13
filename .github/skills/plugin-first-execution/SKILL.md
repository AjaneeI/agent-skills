---
name: plugin-first-execution
description: Route tasks to connected tools before browser or computer fallback, and enforce risk-based approval and denied-access boundaries. Use when choosing tools, evaluating fallbacks, or auditing tool traces.
---

# Plugin-first execution (Copilot bridge)

**Canonical instructions:** [../../../../skills/plugin-first-execution/SKILL.md](../../../../skills/plugin-first-execution/SKILL.md)

1. Read and follow the entire canonical skill before taking action. This bridge contains no independent or superseding policy.
2. Apply the risk-based fallback rule from [the policy](../../../../docs/work-plugin-routing-policy.md). A denied access decision cannot be bypassed.
3. For evaluation, use [the frozen scenarios](../../../../tests/fixtures/plugin-first-cases.json) and [evaluation contract](../../../../docs/agent-evaluation-contract.md). Record actual observed calls and results, not inferred behavior.
4. Stop or request scoped approval when an action crosses an unapproved boundary.

**Acceptance:** The correct authorized route is observed; unauthorized or denied routes are absent; source and outcome are reported.
