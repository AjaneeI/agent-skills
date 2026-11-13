# GitHub Copilot integration and behavioral evaluation

**Status:** Repository integration prepared; no live Copilot behavioral run claimed.

## Architecture

- Canonical skill definitions live in `skills/<name>/SKILL.md`.
- `.github/copilot-instructions.md` contains short repository-wide rules.
- Three discoverable Copilot pilot skills live in `.github/skills/`. They are thin bridges to canonical skills, not independent forks.
- Copilot's skill discovery and actual skill selection must be verified in the intended client. Other ten canonical skills are **not yet** bridged into Copilot's native directory.
- No runtime ACS enforcement, user permissions, account access, or scheduled automations are modified.

Official reference: https://code.visualstudio.com/docs/agent-customization/agent-skills

## Manual live-agent evaluation protocol

1. Open this repository in VS Code with the **Copilot** harness. Confirm the three pilot skills appear in the skill picker or slash-command menu. Also test GitHub's cloud agent separately if available.
2. Record client, model, version, repository commit, tool availability, and permission state. Use synthetic/mock data only; do not send real emails or access private accounts for a test.
3. For each scenario in `tests/fixtures/plugin-first-cases.json`, freeze the setup, prompt, allowed tools, and scoring before running. Start with PF-01, PF-02, PF-03, PF-04, PF-06, PF-09; extend to all ten when the harness supports safe simulation.
4. Capture **actual** tool invocation order, arguments (redacted), return statuses, final output, and whether the skill was loaded. A text-only claim of using a tool is not evidence.
5. Save traces in a local untracked location or sanitized review artifact. Score with `tests/trace_evaluator.py` where its schema applies. A mock trace validates the scorer, **not** Copilot.
6. Repeat the same cases in Codex with the same allowed capabilities. Report each client's legitimate-completion rate, boundary-violation count, false refusals, and unknown/unscored cases. Measure cost only when instrumented.
7. Report observed limitations and propose a new PR for any corrections. Do not merge based solely on static validation.

## Local checks

Run `python -m unittest discover -s tests -v` and `python tests/check_copilot_integration.py`. These validate static repository structure and bridge references, **not** live Copilot behavior.

## Stop conditions

Stop if the test harness cannot isolate consequential actions, if an account is sensitive without specific authorization, or if actual traces cannot be collected. Mark cases blocked or unscored rather than passed.
