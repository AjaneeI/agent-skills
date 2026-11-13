# Plugin-First Routing: Static Evaluation Comparison

**Date:** 2026-11-13  
**Evaluator:** OpenAI Plugin Eval CLI through GitHub Actions  
**Scope:** Static skill assessment only, **not** a live ChatGPT Work or Codex behavioral benchmark.

## Verified Plugin Eval results

| Revision | Score / grade | Risk | Trigger tokens (estimate) | Invocation tokens (estimate) | Deferred tokens (estimate) | Total estimate |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| v1.1 baseline | 81 / C | High | 76 | 2,388 | 0 | 2,464 |
| v1.2 compact | 86 / B | High | 61 | 1,478 | 0 | 1,539 |
| v1.3 deferred-reference experiment | 72 / C | High | 55 | 1,130 | 1,332 | 2,517 |
| v1.4 final draft | 86 / B | High | 48 | 1,032 | 0 | 1,080 |

**Change in estimated total active skill tokens, v1.1 to v1.4:** 2,464 → 1,080, a **56.2% reduction**. This is **not a measured ChatGPT Work token saving** and may not correspond directly to an individual user session's cost.

**Why v1.3 was rejected:** Plugin Eval treated the added reference as 1,332 deferred tokens, producing a second budget failure and a lower score. v1.4 retains a short, self-contained routing and approval contract; longer explanations remain in the separately maintained Work policy document rather than a skill-bundled supporting file.

## What Plugin Eval still flags

- v1.4 keeps an **invocation-token budget failure** despite the smaller skill. The CLI estimates 1,032 invocation tokens and labels it excessive against its own reference baseline.
- The evaluator's risk remains **High** because of this static budget check, **not because it observed a privacy or permission violation**.
- Live token usage, first-tool selection, unnecessary GUI calls, task accuracy, and refusal/approval behavior are **not measured** by these runs.

## Verified automated checks

- [Plugin Eval static run for v1.4](https://github.com/AjaneeI/agent-skills/actions/runs/43519668516): completed successfully; report/budget artifacts uploaded.
- [Agent Skills structural validation and repository tests](https://github.com/AjaneeI/agent-skills/actions/runs/43519668409): passed.
- [Cross-client installation smoke tests](https://github.com/AjaneeI/agent-skills/actions/runs/43519668430): passed in disposable CI for Codex, Claude Code, Gemini CLI and OpenCode.
- [Baseline static run](https://github.com/AjaneeI/agent-skills/actions/runs/43518464416): genuine initial score, 81/100. That run's custom test step initially failed due a test-assertion wording mismatch and was repaired in later commits.

**Scope of CI passing:** Skill format, packaging, static documentation checks, and Plugin Eval reporting. Not a proof of runtime tool selection or security enforcement.

## Behavioral test protocol

The [14-scenario suite](../../tests/plugin-first-routing-scenarios.md) defines positive, negative and legitimate authorized operations. The [Work read-only pilot](work-read-only-pilot.md) supplies a minimal, specific task to run in an actual Work conversation, with Gmail connector routing required and no browser/computer fallback.

**Next gate:** Observe a real Work run with the exact approved skill loaded. Capture actual first tool, full route, GUI calls, approval decisions, and task result. Record usage only if Work exposes token/credit metrics. A Codex benchmark cannot establish Work behavior on its own.

## Release recommendation

Keep [PR #6](https://github.com/AjaneeI/agent-skills/pull/6) **in draft** until a human reviews the compacted wording and at least one observed read-only behavior run is available. Do not merge or globally activate a policy based only on static scores.
