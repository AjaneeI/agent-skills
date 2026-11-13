# Plugin-First Execution: Baseline Static Evaluation

**Date:** 2026-11-13  
**Skill:** `skills/plugin-first-execution/SKILL.md` v1.1.0 (main at evaluation start)  
**Evaluator:** OpenAI Plugin Eval CLI, run in GitHub Actions  
**Source run:** [Evaluate Plugin-First Skill, run 43518464416](https://github.com/AjaneeI/agent-skills/actions/runs/43518464416)  
**Status:** Actual static evaluation; **no live Work or Codex behavior** has been tested.

## At a glance

| Metric | Baseline result |
| --- | --- |
| Plugin Eval score | 81/100 (grade C) |
| Evaluator risk | High |
| Checks | 1 fail, 1 warning, 2 informational |
| Estimated activation/trigger tokens | 76 |
| Estimated skill invocation tokens | 2,388 |
| Estimated total active tokens | 2,464 |
| Deferred tokens | 0 |
| Observed token usage | Not provided |

## Why the evaluator flagged it

1. **High active-context cost (failure):** A 2,388-token skill body is expensive relative to Plugin Eval's baseline. Reduce duplicated guidance and move optional detail to documentation loaded only when needed.
2. **Weak activation trigger (warning):** The frontmatter description does not begin with a clear `Use when ...` condition.

**Score caveat:** These are CLI static estimates, not measured token use inside ChatGPT Work. The exact impact on Work depends on whether, when, and how the skill is loaded by that environment.

## Positive signals in the current skill

- Read-only default and explicit send/write approval boundaries.
- Dedicated connector routing for supported account operations.
- Risk tiering for public, signed-in, and sensitive sources.
- Stricter task-specific automation rules take precedence.
- Explicit examples of acceptable and prohibited behavior.
- Honest statement that instruction files are not runtime access controls.

## Proposed experiment

Run Plugin Eval again against a **compact v1.2 draft on a non-default branch** with the same evaluator. Keep all essential permission gates in the active skill, while moving reference details to the existing policy document.

Success would mean **reduced static context cost without weakening any contractual behavior**. A higher static score alone does not establish better real-world behavior. Run the 14 positive and negative scenarios with trace evidence before claiming that.

## Current limits

This GitHub Actions workflow does not execute Codex agent sessions, access private user accounts, load ChatGPT Work, or record actual Work tool-call traces. The accompanying [scenario suite](../../tests/plugin-first-routing-scenarios.md) is an unexecuted specification. No measured savings or behavioral pass rates are reported.
