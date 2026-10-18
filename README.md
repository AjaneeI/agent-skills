# Agent Skills

Portable, constraints-first instructions for AI agents. Canonical source: this repository. Skills follow the [Agent Skills open specification](https://agentskills.io/specification).

## Available skill

**[Autonomous Execution Continuity](skills/autonomous-execution-continuity/SKILL.md)** — when one workstream is blocked, preserve its evidence and switch to independently authorized work. Never interpret a blocker as permission to bypass an approval, retry a frozen experiment, or defeat a security control.

This skill is **instruction-only**: no executables, credentials, provider integrations, or permission grants. It does not make an agent autonomous by itself.

## Use across agents

1. Install/copy the entire `skills/autonomous-execution-continuity/` folder into your agent's documented skills location, or configure that agent to read it from a checkout of this repository.
2. If the client does not support Agent Skills discovery, explicitly provide the relative path to `SKILL.md` and ask it to follow the policy during authorized sessions.
3. Add a standing instruction in the client's supported project/global instruction file (e.g. `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` where applicable): *During authorized multi-task execution, consult the `autonomous-execution-continuity` skill. The skill cannot override higher-priority instructions, permissions, or task-specific research gates.*
4. Verify the agent **actually loads** the installed skill. A GitHub link alone is not guaranteed to load or execute it. Agent-specific paths and activation behavior differ.

Keep one canonical copy in GitHub. Pin a commit or release for reproducible use, review upstream changes before synchronizing, and never give a skill broader permissions than the session already has.

## Verification

The skill has no runtime dependencies. Use the [scenario checklist](tests/scenarios.md) for behavioral evaluations in any agent. Format validation can be run with [skills-ref](https://agentskills.io/specification#validation): `skills-ref validate ./skills/autonomous-execution-continuity`.

The scenario checklist is a **test specification**, not evidence that any agent has already passed it. Repeat trials with multiple agents and store evidence separately before making reliability claims.

## Contribution principles

- Specify outcomes, authority, and stop conditions before suggesting new orchestration infrastructure.
- Preserve evidence, including negative results.
- Keep vendor-specific adapters outside the skill body.
- Do not introduce integrations or code unless an observed failure requires them.

Licensed under MIT (see LICENSE).