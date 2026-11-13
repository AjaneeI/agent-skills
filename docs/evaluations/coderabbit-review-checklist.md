# CodeRabbit Review Checklist — Plugin-First Execution PR #6

**Status:** Review instructions; not a completed review or evidence of compliance.  
**Audience:** CodeRabbit, maintainers, and any agent reading PR #6.  
**Target:** [Draft PR #6](https://github.com/AjaneeI/agent-skills/pull/6).  
**Authority:** CodeRabbit's findings are advisory. Do not merge, auto-fix, publish, or edit private accounts on the basis of this checklist.

## Review objective

Assess whether the proposed plugin-first skill and its evaluation infrastructure are
**clear to humans, actionable for agents, safe at approval boundaries, and truthful
about what testing actually demonstrated**. Focus on correctness and meaningful
risks before presentation details.

## Review checklist

- [ ] **Scope and precedence:** The global policy is risk-based but preserves the existing Networking & Application Follow-up automation's stricter ask-first fallback.
- [ ] **Connector-first routing:** Gmail and other supported account operations use dedicated connected tools before browser/computer navigation. Broken connectors do not silently expand access.
- [ ] **Risk classification:** Public read-only access can be low risk; signed-in sources and sensitive personal accounts require the documented approvals. A read-only goal alone cannot reduce data sensitivity.
- [ ] **Consequential actions:** Sends, invitations, publication, sharing changes, purchases, commits, record updates, and other external changes require task-specific authority.
- [ ] **Handoff and failure behavior:** Missing capability, ambiguous identities, and source failures produce useful verified partial results with an explicit decision request. No invented successes or tool-use claims.
- [ ] **Untrusted content:** Webpages, emails, task descriptions, and repository files cannot grant permissions, override policy, or cause unapproved tool use.
- [ ] **Human/agent readability:** Clear trigger, sources, steps, permissions, good/bad examples, handoff, and acceptance checks. No unnecessary jargon or repeated instructions.
- [ ] **Test strength:** The 14 routing scenarios cover safe allowance, required refusal, and legitimate authorized writes. Static contract tests should not pass merely because favorable phrases appear.
- [ ] **Evidence honesty:** CI, packaging, and Plugin Eval static scores must not be described as live Work behavior, real token savings, or verified runtime security.
- [ ] **Cost and efficiency:** Flag gratuitous tool invocations, broad searches, unnecessarily loaded supporting files, or long instructions that do not improve execution. Avoid inferring actual token savings from static estimates.
- [ ] **CI safety and reproducibility:** Ensure pinned evaluator source, read-only GitHub Actions permissions, bounded execution, no credentials or personal data, and no automatic paid benchmarks.
- [ ] **Source safety:** The public repository must contain no private message content, credentials, financial/health information, or individual account identifiers.

## Good review example

> **Medium: Approval boundary ambiguity.** The fallback instructions permit
> reading a signed-in account without establishing that the exact browser
> route was approved. Suggest requesting authorization for that route before
> navigation. This protects sensitive data without blocking public research.

Why it is helpful: names an exact failure mode, points to the affected rule,
explains the impact, and proposes the smallest feasible correction.

## Bad review example

> Use more AI or automate every website interaction. The score looks good, so
> the skill is production-ready.

Why it fails: generic, unsupported, expands access, and equates static
assessment with observed agent behavior.

## Findings and triage

Classify each comment as **blocker**, **important**, **minor**, or **question**.
For each significant finding, include the file and location, exact evidence,
impact on the agreed policy, and a minimal proposed change. Prefer fewer,
well-supported findings over speculative or stylistic noise.

Treat all CodeRabbit output as recommendations to be reviewed before edits.
Do not enable its automated fix workflows unless separately approved.

## Human acceptance and next gate

A maintainer can approve a revision for merging only after:

1. Reviewing CodeRabbit's actual comments, disagreements, and false positives.
2. Confirming relevant GitHub Actions checks passed for the final commit.
3. Confirming policy, examples, and the stricter automation exception remain intact.
4. Clearly recording that the live Work read-only pilot has **not** been executed
   until observable tool traces support it.
5. Making a conscious merge decision. This document never authorizes auto-merge.

**How to request review:** On PR #6, post `@coderabbitai review` once the
changes are ready. Keep the PR draft; do not turn on auto-review for drafts
repository-wide merely to review this one PR. Verify the bot actually posts
a completed review instead of assuming a command succeeded.
