# Blocker handling and recovery policy

## Decision table

| Blocker | Classification | Permitted response |
| --- | --- | --- |
| Human approval needed to change a frozen research scorer in workstream A | Local if B is truly independent | Freeze A, record exact decision and evidence; continue model-free B within existing authorization |
| Local model or database unavailable for experiment A | Local if other work does not depend on it | Record environment diagnostic, continue independent offline validation |
| Pull request blocked by review | Local | Leave draft intact; work on unrelated approved task |
| Denied access or request to override permissions | Global for affected operation; assess whether it affects whole session | Do not circumvent or seek alternate channels for the denied action |
| Credential exposure, unauthorized data access, suspected compromised workspace | Global | Stop affected actions, safeguard evidence, request human guidance |
| Frozen experiment failed after one authorized attempt | Local failure, not an automatic retry opportunity | Preserve failure; do not repeat; other independent authorized tasks may continue |
| User asks to stop | Global | Stop promptly and report |
| Budget exceeded or safe task queue empty | Global session stop | Stop and summarize |

## Checkpoint record

Record: task ID, objective, authorization and limits, blocker type, evidence/provenance links, exact approval question, whether a run was attempted, blocked dependencies, permissible independent tasks, and last known state. Avoid secrets or raw sensitive traces in shared locations.

## Avoid repeated approval loops

- Ask once per *distinct* decision with a specific proposed action and risks.
- Mark the workstream `blocked` until explicit authorization or an observable change occurs.
- Never reframe the same decision to induce automatic approval.
- When there is no independent authorized work, end with the decision request instead of spinning.
- Do not claim completion merely because work was preserved.

## Research-specific caution

Do not contaminate held-out data. Distinguish model-free preparatory work from live experiments. Treat changes to model-visible tool context, observed evidence derivation, benchmarks, scorers, or statistical methods as potentially versioned methodology changes requiring their existing approval gates. Historical failed runs remain immutable.