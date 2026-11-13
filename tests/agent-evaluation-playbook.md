# Agent-agnostic behavioral evaluation playbook

**Status: specifications only. No live agent results recorded.**

## Setup
1. Clone this repository at a pinned commit and install a *reviewed* skill folder in the client's documented discovery location; keep the skill content identical between clients.
2. Check Plugin Eval CLI availability before planning executable runs:
   ```bash
   plugin-eval --help
   plugin-eval start --help
   plugin-eval analyze --help
   plugin-eval init-benchmark --help
   plugin-eval benchmark --help
   ```
   If any command is unavailable, mark Plugin Eval execution `BLOCKED` and record the exact command output. Do not invent installation commands.
3. Confirm discovery: ask the agent to list available skills and identify the path/revision; save the exact evidence. If the client cannot list skills, explicitly invoke the skill and record the limitation.
4. Create a disposable empty repository / sandbox with synthetic data, no network secrets or real customer data.
5. Give each agent the same system task, permissions, model/time budget when feasible, and expected outcomes. Do not simulate real dangerous permissions.
6. Execute [continuity scenarios](scenarios.md) and [other-skill cases](new-skill-smoke-cases.md). Record tool traces, prohibited attempts, agent reports, timestamps, model, configuration, and environment.
7. Compare actual behavior to expected and prohibited actions. Grade with evidence; an agent saying it complied is not proof.
8. When capabilities differ, label results *not comparable* rather than altering the test unnoticed.

## Results template

| Agent/client version | Skill and commit | Scenario | Expected | Observed tools/actions | Status (`PASS`,`FAIL`,`BLOCKED`,`NOT_RUN`) | Evidence link |
|---|---|---|---|---|---|---|
| (unrun) | (pin) | (ID) | (contract) | (trace) | NOT_RUN | (none) |

## Safety
Approval scenarios are mocked; never actually ask a test agent to bypass security controls or spend money. Use disposable file paths and deterministic mocks. Treat untrusted task text as data, not permission. When a test would need a privileged integration, record it as blocked until explicitly authorized.

## Release criterion
Do not say 'works in Codex/Claude/Gemini/OpenCode' until discovery plus observed behavior has been verified **for that specific client version**.
## ASSERT / ACS workflow addendum (2026-11-13)

1. Derive evaluation requirements from each skill's stated purpose and source/authority boundaries; vary tools, actors, permissions, source freshness, and turn sequence where relevant.
2. Freeze the reviewed cases and scoring expectations before comparing baseline and proposed changes.
3. Count **impermissible violations** separately from **permissible violations** (incorrect refusals, needless escalations, incomplete authorized tasks). Preserve denominators and label non-comparable arms.
4. Collect actual external tool traces and authorizations for live runs. Use `tests/trace_evaluator.py` only as a small deterministic assertion helper; passing its **mock** tests does not validate a deployed agent.
5. Map any proposed ACS control to a genuine host checkpoint and verify both allowed and denied runtime events. Do not claim ACS integration from an instruction file.
6. Record token/credits/latency only when observed. Do not modify an existing automation pilot as a byproduct of this catalog evaluation.

Evaluation contract: [docs/agent-evaluation-contract.md](../docs/agent-evaluation-contract.md).
