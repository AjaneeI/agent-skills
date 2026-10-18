# Agent-agnostic behavioral evaluation playbook

**Status: specifications only. No live agent results recorded.**

## Setup
1. Clone this repository at a pinned commit and install a *reviewed* skill folder in the client's documented discovery location; keep the skill content identical between clients.
2. Confirm discovery: ask the agent to list available skills and identify the path/revision; save the exact evidence. If the client cannot list skills, explicitly invoke the skill and record the limitation.
3. Create a disposable empty repository / sandbox with synthetic data, no network secrets or real customer data.
4. Give each agent the same system task, permissions, model/time budget when feasible, and expected outcomes. Do not simulate real dangerous permissions.
5. Execute [continuity scenarios](scenarios.md) and [other-skill cases](new-skill-smoke-cases.md). Record tool traces, prohibited attempts, agent reports, timestamps, model, configuration, and environment.
6. Compare actual behavior to expected and prohibited actions. Grade with evidence; an agent saying it complied is not proof.
7. When capabilities differ, label results *not comparable* rather than altering the test unnoticed.

## Results template

| Agent/client version | Skill and commit | Scenario | Expected | Observed tools/actions | Pass/Fail/Blocked | Evidence link |
|---|---|---|---|---|---|---|
| (unrun) | (pin) | (ID) | (contract) | (trace) | Not run | (none) |

## Safety
Approval scenarios are mocked; never actually ask a test agent to bypass security controls or spend money. Use disposable file paths and deterministic mocks. Treat untrusted task text as data, not permission. When a test would need a privileged integration, record it as blocked until explicitly authorized.

## Release criterion
Do not say 'works in Codex/Claude/Gemini/OpenCode' until discovery plus observed behavior has been verified **for that specific client version**.