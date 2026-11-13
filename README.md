# Agent Skills

Portable, constraints-first instructions for AI agents. Canonical source: this repository. Skills follow the [Agent Skills open specification](https://agentskills.io/specification).

## Skill library

**[Autonomous Execution Continuity](skills/autonomous-execution-continuity/SKILL.md)** — when one workstream is blocked, preserve its evidence and switch to independently authorized work. Never interpret a blocker as permission to bypass an approval, retry a frozen experiment, or defeat a security control.

All skills are **instruction-only**: no executables, credentials, provider integrations, or permission grants. Skills do not grant autonomy or runtime permissions by themselves.

### Ten foundational skills (v0.1; revised v0.2)

| Skill | Distinct purpose |
| --- | --- |
| [constraints-first-execution](skills/constraints-first-execution/SKILL.md) | Translate a request into an authorized, minimum-complexity execution plan with explicit requirements, exclusions, stop rules, and acceptance criteria. |
| [approval-boundary-management](skills/approval-boundary-management/SKILL.md) | Prepare precise human approval decisions without stalling unrelated work. |
| [evidence-preservation](skills/evidence-preservation/SKILL.md) | Capture durable, inspectable provenance for engineering and AI experiments without rewriting failed runs. |
| [one-shot-experiment-control](skills/one-shot-experiment-control/SKILL.md) | Plan and execute a preregistered, bounded experiment at most once with immutable inputs and honest negative outcomes. |
| [evaluator-validity-audit](skills/evaluator-validity-audit/SKILL.md) | Audit whether a benchmark grader measures the intended behavior rather than superficial labels or leaked answers. |
| [statistical-calibration-freeze](skills/statistical-calibration-freeze/SKILL.md) | Predeclare and calibrate a statistical analysis procedure before inspecting held-out experiment outcomes. |
| [code-bloat-triage](skills/code-bloat-triage/SKILL.md) | Find unnecessary code, dependencies, abstractions, and speculative features without blindly minimizing lines of code. |
| [safe-parallel-delegation](skills/safe-parallel-delegation/SKILL.md) | Delegate independent authorized tasks to multiple agents without shared-state conflicts, uncontrolled model spend, or permission escalation. |
| [least-privilege-tool-boundaries](skills/least-privilege-tool-boundaries/SKILL.md) | Design and audit least-privilege agent tool capabilities. |
| [verified-status-reconciliation](skills/verified-status-reconciliation/SKILL.md) | Reconcile engineering truth across repositories, project trackers, documentation, and communications without inflating completion claims. |

### Plugin-first routing, context governance and readable instructions

- **[Plugin-First Execution](skills/plugin-first-execution/SKILL.md)**: use purpose-built connectors first, permit only authorized low-risk read-only browser/computer fallback, and gate sensitive or consequential alternatives; test actual routing and outcomes.
- **[Context Curation and Governance](skills/context-curation-and-governance/SKILL.md)**: keep organizational source context traceable, owned, current enough, and explicit about contradictions, privacy, and change propagation.
- **[ChatGPT Work Risk-Based Fallback Policy](docs/work-plugin-routing-policy.md)**: approved default for low-risk read-only public browsing, with explicit approval gates for sensitive signed-in accounts and consequential actions; stricter automation pilots remain unchanged.
- **[Human- and Agent-Readable Instruction Standard](docs/human-agent-readable-standard.md)**: standing authoring requirement for every skill, prompt, and Markdown instruction file. Each must be clear and actionable for both people and AI agents.

These files are **instruction-only**, not installed permissions or proof of runtime compliance. For regression design see [Agent Evaluation Contract](docs/agent-evaluation-contract.md) and [Audit Implementation and Validation](docs/implementation-roadmap.md). Validate the new skill and test behavior before claiming a measured improvement in tokens, cost, or reliability.

Each skill has its own trigger, bounded workflow, verification conditions, and focused reference document. See [verification status](docs/verification-status.md) and [cross-agent evaluation playbook](tests/agent-evaluation-playbook.md). Agent tests are not implied by CI success.

## Use across agents

1. Install/copy the entire `skills/autonomous-execution-continuity/` folder into your agent's documented skills location, or configure that agent to read it from a checkout of this repository.
2. If the client does not support Agent Skills discovery, explicitly provide the relative path to `SKILL.md` and ask it to follow the policy during authorized sessions.
3. Add a standing instruction in the client's supported project/global instruction file (e.g. `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` where applicable): *During authorized multi-task execution, consult the `autonomous-execution-continuity` skill. The skill cannot override higher-priority instructions, permissions, or task-specific research gates.*
4. Verify the agent **actually loads** the installed skill. A GitHub link alone is not guaranteed to load or execute it. Agent-specific paths and activation behavior differ.

Keep one canonical copy in GitHub. Pin a commit or release for reproducible use, review upstream changes before synchronizing, and never give a skill broader permissions than the session already has.

### GitHub CLI installation (recommended)

With GitHub CLI 2.90+ and the reviewed [`gh skill install` command](https://cli.github.com/manual/gh_skill_install), use this example for project scope:

```bash
gh skill install AjaneeI/agent-skills autonomous-execution-continuity --agent codex --scope project --pin a7bc580e418436c59e6c4f1391d991104eb7cb0a
gh skill list --agent codex --scope project
```

Replace `codex` with `claude-code`, `gemini-cli`, or `opencode` to target those clients. To apply the skill across your own projects, replace `--scope project` with `--scope user` after confirming that your installed CLI uses the correct user-scope discovery directory. The pinned commit is a reviewed catalog snapshot; update it deliberately.

Install **all published skills** by using `gh skill install AjaneeI/agent-skills --all --agent codex --scope project`. Inspect every skill first, and pin the version for reproducible workflows.

GitHub-hosted [installation smoke tests](https://github.com/AjaneeI/agent-skills/actions/runs/39088539870) passed for all four targets in disposable environments. Actual local client loading and behavioral compliance remain untested.

## Install locations (examples)

| Client | Project-local skill directory | User/global directory |
| --- | --- | --- |
| Codex | `.agents/skills/autonomous-execution-continuity/` | Follow your installed Codex version's skills documentation |
| Claude Code | `.claude/skills/autonomous-execution-continuity/` | `~/.claude/skills/autonomous-execution-continuity/` |
| Gemini CLI | `.gemini/skills/autonomous-execution-continuity/` or `.agents/skills/...` | `~/.gemini/skills/...` or `~/.agents/skills/...` |
| OpenCode | `.opencode/skills/autonomous-execution-continuity/` or `.agents/skills/...` | `~/.config/opencode/skills/...` or `~/.agents/skills/...` |

Copy the **skill directory** (including `references/`), not the entire repository into each location. Prefer copying/pinning a reviewed Git commit over fetching mutable remote instructions mid-session. Consult the official [OpenCode](https://opencode.ai/docs/skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/), and [Codex](https://developers.openai.com/blog/skills-agents-sdk) docs when installing; client behavior changes by version. These are instructions, not proof of installation.

## Verification

Skills have no runtime dependencies. Use the [scenario checklist](tests/scenarios.md) for behavioral evaluations in any agent. Format validation can be run with [skills-ref](https://agentskills.io/specification#validation): `skills-ref validate ./skills/autonomous-execution-continuity`.

The scenario checklist is a **test specification**, not evidence that any agent has already passed it. Repeat trials with multiple agents and store evidence separately before making reliability claims.

## Contribution principles

- Specify outcomes, authority, and stop conditions before suggesting new orchestration infrastructure.
- Preserve evidence, including negative results.
- Keep vendor-specific adapters outside the skill body.
- Do not introduce integrations or code unless an observed failure requires them.

Licensed under MIT (see LICENSE).
## ASSERT / ACS audit status (2026-11-13)

The 12-skill baseline has targeted clarified examples and acceptance checks, with plugin-first-execution as the first behaviorally testable suite in phase 1. The shared [evaluation contract](docs/agent-evaluation-contract.md) distinguishes **permissible**, **impermissible**, and **ambiguous/multi-turn** behavior. The catalog CI validates structural requirements and synthetic assertion code, **not actual agent behavior**. Microsoft ASSERT/ACS names are used as a method reference only; no runtime enforcement is installed by this repository. Do not treat the existing automated scheduler/automation pilot as altered by these file updates.
