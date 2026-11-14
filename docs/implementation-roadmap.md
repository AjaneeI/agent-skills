# Audit Implementation and Remaining Validation

**Date:** 2026-11-13  
**Scope:** 12 existing skills, one narrowly scoped context-curation skill, authoring/tests/CI, and the approved risk-based fallback policy.

## Completed in this PR (subject to review and CI)

- Updated all 12 existing skills with targeted behavioral examples, source/authority handling, and regression expectations.
- Added `context-curation-and-governance`, including accountable roles, provenance, contradictions, and refresh triggers.
- Preserved instruction-only skills. No runtime permission grant, ACS installation, production deployment, secret, or external account access is bundled.
- Improved catalog assertions, test-case specification, mock trace evaluator, CI coverage, and count/version documentation.
- Updated the general plugin-first policy to distinguish low-risk read-only fallback from sensitive/consequential actions. **No scheduled automation is modified.**

## Not yet established by a GitHub PR

| Work | Required evidence |
| --- | --- |
| Actual agent skill activation in Codex / Claude / Gemini / OpenCode | Local discovery/loading evidence for each exact client and pinned revision |
| ASSERT-driven behavioral pass/fail rates | Frozen case set, live agent execution, trace-grounded scoring, comparison arms |
| ACS enforcement | Real host integration, executable policy, observed allow/deny checkpoints |
| Token/credit improvement | Captured provider metrics or a defensible measured proxy |
| Validity across accounts | Approved synthetic/sandbox cases; never live private data as a convenient benchmark |
| Production readiness | Human approval plus project-specific organizational controls |

## Suggested first live pilot, preserving current automations

Use the `plugin-first-execution` scenarios in a **disposable synthetic** email/event environment. Hold the case set constant for baseline and revised agents. Test working connector, low-risk public read fallback, unavailable sensitive connector, access-denied, explicit send approval, and multi-turn escalation. Collect actual tool order, outputs, source evidence, and permissible/impermissible metrics separately. Do **not** modify or repurpose the active automation pilot.

## Promotion decision

This PR may be merged after format/static/mock CI succeeds and its wording is reviewed. **Behavioral compliance remains unverified until actual independent agent runs occur.** Keep these two milestones separate.
