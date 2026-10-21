# Activate the standing engineering rules

GitHub is the canonical source. Publication does **not automatically** install skills, change account-wide memory, update another repository, or make every chat load them.

## In this repository

[AGENTS.md](../AGENTS.md) routes relevant work to `reuse-before-build` and `safe-publication-review`. Both use the existing `skills/` catalog convention. Neither is a runtime permission control.

## In another project or engineering lead

1. Review a specific commit containing both skills and record its full SHA. A reviewed PR branch is not a merged release.
2. Copy each complete skill directory, including `references/`, into the client's documented discovery location or configure a pinned checkout. Reconcile same-name local skills rather than overwriting them. Keep private configuration separate.
3. Merge the directive below into the environment's supported project or standing instruction file; preserve existing instructions:

> Before substantial infrastructure work, load `reuse-before-build` from the installed, pinned catalog. Before any public skill or related artifact leaves the private workspace, load `safe-publication-review`. Newly authored reusable non-personal skills have their canonical source in the approved GitHub skill repository; personal context remains private. Existing task scope, publication authority, and merge permissions remain in force.

4. In a fresh session, request the resolved skill paths and revision, then have the client actually read the skills and references. Save a loading receipt. Merely repeating the skill names is not discovery evidence.
5. Exercise the [governance scenarios](../tests/governance-scenarios.md) with synthetic data, bounded permissions and observable tool actions. Record client/model version and outcomes. Do not alter frozen evaluations, global configuration or provider budgets without relevant authority.

## Activation receipt

Keep the client/version, pinned SHA, installed file hashes, read evidence, scenario outcomes and limitations in the consuming project's private records. Do not publish personal device paths. Global activation remains unverified until observations support it.

Consult current official client documentation: [OpenAI skill authoring](https://learn.chatgpt.com/docs/build-skills) and [AGENTS.md configuration](https://learn.chatgpt.com/docs/agent-configuration/agents-md). This guide does not assert a local installation.
