# Verification status — skill catalog

## Format
- Original `autonomous-execution-continuity` skill: official `skills-ref` validator and repository unit checks passed on 2026-10-17. [CI evidence](https://github.com/AjaneeI/agent-skills/actions/runs/39088158136).
- Ten additional `v0.1.0` skills: **format validation required on this commit**. CI validates every `skills/*/SKILL.md` using official `skills-ref`; check the latest action result before declaring pass.
- All skills are instruction-only; no scripts or provider tokens.

## Behavior
- The [ten continuity scenarios](../tests/scenarios.md) and the [new skill smoke cases](../tests/new-skill-smoke-cases.md) are test specifications, **not executed behavioral test results**.
- Codex, Claude Code, Gemini CLI and OpenCode: local installation/discovery **not confirmed**; behavioral acceptance **not run** against each agent.
- A passing reference validator or static catalog unit test does **not** prove adherence during live autonomous execution.

## Promotion gate
1. Official structural validation passes for all skill folders.
2. Owner inspects instructions for ambiguous or excessive permissions.
3. Install the skill on a chosen client, prove that the agent discovers/loads the correct commit.
4. Run at least the negative and positive scenarios with observed traces; record results and environment.
5. Repeat for each client before describing the skill as behaviorally verified across agents.

Never invent installation success, agent evaluations, or autonomous safety guarantees.