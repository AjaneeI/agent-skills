# Plugin-first-execution evaluation status (phase 1)

## Environment snapshot

- Repository: `AjaneeI/agent-skills`
- Pinned commit for this snapshot: `1c7774dbf668278c16b654f0c178eadab00a37ad`
- Runtime: `Python 3.12.3`
- Client/model for live behavior: `NOT_RUN` (no connected runner executed in this phase)
- Synthetic fixture revision: `tests/fixtures/plugin-first-cases.json`

## Plugin Eval CLI availability probe (reproducible)

Coordination scope note: PR #6 (`eval/plugin-first-routing-2026-11-13`) already carries pinned Plugin Eval static CI, a 14-scenario static suite, and a v1.4 candidate skill draft. This phase-1 artifact in PR #8 is intentionally limited to unmet gaps: reproducible local CLI availability evidence (`BLOCKED` here), deterministic fixture/harness checks, and explicit `NOT_RUN` live-behavior status until trace-backed execution is possible.

Executed in this repository checkout:

```bash
plugin-eval --help
plugin-eval start --help
plugin-eval analyze --help
plugin-eval init-benchmark --help
plugin-eval benchmark --help
```

Observed output in this environment:

```text
/bin/bash: plugin-eval: command not found
```

Status: `BLOCKED` for Plugin Eval CLI execution until a real `plugin-eval` binary is installed in the Copilot environment. After installation, rerun the exact commands above, confirm command schema from `--help`, and only then run `plugin-eval start`, `plugin-eval analyze`, `plugin-eval init-benchmark`, and `plugin-eval benchmark --dry-run`.

## Evidence-backed state register

| Scope | Status | Evidence |
| --- | --- | --- |
| Catalog/static CI checks (structure + links + fixture schema tests) | `BLOCKED` | Latest PR #8 workflow runs are `action_required`: https://github.com/AjaneeI/agent-skills/actions/runs/43522516956 and https://github.com/AjaneeI/agent-skills/actions/runs/43522244244 |
| Deterministic harness unit tests (`tests/test_trace_evaluator.py`) | `PASS` | Local command and output: `python -m unittest discover -s tests -p 'test_trace_evaluator.py' -v` |
| Plugin Eval CLI static report (`plugin-eval *`) | `BLOCKED` | `command not found` outputs above |
| Real agent behavioral execution for PF-01..PF-12 | `NOT_RUN` | No live agent traces captured in this phase |

CI blocker detail: the `action_required` runs did not start jobs (`total_jobs: 0`, `failed_jobs: 0`) and therefore are treated as approval/permission blockers, not passing tests.

## Trace-ready behavioral case results template

| Case ID | Expected outcome | Status (`PASS`,`FAIL`,`BLOCKED`,`NOT_RUN`) | Agent/client | Model | Trace link | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| PF-01 .. PF-12 | See fixture | `NOT_RUN` | (pending) | (pending) | (pending) | Fill only from observed traces |

## Guardrails

- Do **not** mark behavioral cases `PASS` from prose-only claims, markdown quality, or green static CI.
- Any cost/token savings claim must include observed instrumentation evidence; estimates must be labeled as estimated.
- Cases requiring connector-failure/approval provenance are machine-checked through explicit `trace_flags` (for example PF-03/PF-04/PF-11), not inferred from empty `handoff` outcomes.
- Self-reported approval or metric claims are non-authoritative for deterministic checks.
- Keep the existing Networking & Application Follow-up automation pilot unchanged (stricter always-ask-first behavior).
