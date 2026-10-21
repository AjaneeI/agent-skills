# Verification status — agent skill catalog

## Historical eleven-skill format validation: PASSED
- The original `autonomous-execution-continuity` skill passed the official reference validator on 2026-10-17: [initial CI run](https://github.com/AjaneeI/agent-skills/actions/runs/39088158136).
- **All 11 skills** passed the official `skills-ref validate` CLI and the repository's two structural checks: [catalog CI run](https://github.com/AjaneeI/agent-skills/actions/runs/39088424759). Job log: `Validated 11 skill directories`.
- The skill library is instruction-only: no scripts, credentials or provider-specific permissions. This is a formatting and internal consistency check, **not a behavioral safety certification**.

## Historical original-skill installation packaging: PASSED IN EPHEMERAL CI
- [Install smoke matrix](https://github.com/AjaneeI/agent-skills/actions/runs/39088539870) passed four jobs: `codex`, `claude-code`, `gemini-cli`, and `opencode`.
- The GitHub CLI installed `autonomous-execution-continuity` in each **disposable project**; each job verified a skill entry, referenced blocker policy and a client-scoped skill listing.
- This does **not** establish successful installation or activation on the owner's Mac, nor runtime behavioral compliance. Other ten skills passed format but were not individually installed in the cross-client smoke matrix.

## Existing runtime behavior evaluation: NOT YET EXECUTED
- [Ten continuity scenarios](../tests/scenarios.md) and [ten new-skill scenarios](../tests/new-skill-smoke-cases.md) remain written specifications, **not empirical agent outcomes**.
- Local discovery and actual execution in Codex, Claude Code, Gemini CLI and OpenCode are **not confirmed**.
- A passing reference validator or GitHub CLI installation does not prove that an agent obeys the rules under pressure.

## Historical catalog promotion checklist
1. ✅ Reference validation for all 11 skills and static checks.
2. ✅ GitHub-hosted packaging/distribution smoke for original skill in four agent targets.
3. ☐ User reviews sensitive/ambiguous scope before activating skills on a real project.
4. ☐ Install at a pinned commit in each real agent environment; capture `gh skill list` or an equivalent actual discovery result.
5. ☐ Execute observed positive and negative behavioral scenarios in disposable environments with tool traces and budgets.
6. ☐ Independently review all decisions and failures before calling a skill behaviorally verified across agents.

Follow the [cross-agent behavioral evaluation playbook](../tests/agent-evaluation-playbook.md). Do not turn unexecuted scenarios into claimed pass rates.

## Governance additions: 2026-10-21

`reuse-before-build` and `safe-publication-review` are new instruction-only skills. Their candidate adds repository instructions, publication policy, security guidance, activation instructions, a PR checklist and six static governance tests.

Read the exact candidate PR for current tests and review evidence. The historical CI links above cover the previous catalog, not these additions. The new skills' official-validator status must be read from their own checks.

Four synthetic text-only baseline planning probes were captured before authoring and repeated with the skill context after authoring. These are wording-development exercises through a model helper, not installed-client runtime trials. No actual publication, tool behavior, model identity guarantee or productivity measurement is established. The baseline already rejected unsafe publication; no safety improvement is claimed. R1 omitted explicit license and security assessment, motivating the structured comparison requirements. See [governance scenarios](../tests/governance-scenarios.md).

A repository commit does not install these skills on a device. Global memory settings, schedules, active evaluation branches and merge authority are unchanged. Self-review, separate model-assisted document review, human approval and native-client behavior tests are distinct forms of evidence.

## Completion additions: 2026-10-21

`evidence-based-verification` and `research-gate-management` add distinct claim-adjudication and prerequisite-management roles, plus a catalog routing guide, six static document-contract tests, and six synthetic scenario specifications. Existing skill bodies, frozen evaluation artifacts, and CI configuration are not changed.

Read the exact candidate PR and its final verification receipt for current checks, document review, and publication readback. Earlier commits' validation does not establish the new candidate's results. The current catalog contains 15 instruction-only skills; publication and actual client activation remain separate.

Four synthetic text-only baseline probes were captured before authoring and repeated with the skill text and reference afterward. Both conditions declined unsupported completion and premature experiments. These observations do not demonstrate a new safety benefit, live tool behavior, or a pass rate. The added records make scope/version binding, outcome separation, dependency ownership, and applicability explicit. [Scenario specifications](../tests/completion-scenarios.md) are not runtime results. Raw probe output remains outside the public candidate.
