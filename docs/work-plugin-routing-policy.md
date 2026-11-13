# ChatGPT Work: Plugin-First, Risk-Based Fallback Policy

**Status:** User-approved proposed Work-wide policy (2026-11-13). Not automatically installed in Work.  
**Skill:** [Plugin-First Execution](../skills/plugin-first-execution/SKILL.md) v1.4.0 (draft, pending review).  
**Exception:** The existing Networking & Application Follow-up automation retains its stricter **always ask first** rule.

## Objective

Use the most direct authorized tool for each task, minimizing unnecessary browser/computer steps without sacrificing correctness, privacy, or security.

## Required process

1. Identify the goal, source of truth, permitted actions, and sensitivity.
2. Use the purpose-built connector first for supported operations (for example, Gmail for Gmail).
3. If it fails or lacks the needed action, classify the **source and action** using the table below.
4. Apply the fallback rule before opening a browser/computer session. Never silently bypass a failed connector.
5. Verify the outcome; request approval before a consequential external action.
6. Report partial completion, blocked access, and observed metrics accurately.

## Risk and authority

| Tier | Examples | Browser/computer fallback |
| --- | --- | --- |
| Low | Public documentation and event pages; specifically preapproved non-sensitive read-only sources | **MAY**, read-only when necessary and already permitted |
| Medium | Signed-in Notion, Asana, HubSpot, Google Calendar/Drive, private project data | **ASK** before authenticated fallback unless this exact route was preapproved |
| High | Personal Gmail, medical/health, finances, credentials, security settings | **ASK** before authenticated fallback; otherwise return verified partial work |

**All tiers:** No unapproved sending, publishing, invitations, purchases, record edits, permission changes, or other consequential actions. Read-only intent does not make state-changing clicks acceptable. Do not classify sensitive account access as low-risk.

## Good and bad examples

**Good:** A public conference agenda is missing from search snippets. Read the public page in a browser, cite it, and stop before any RSVP or account login.

**Good handoff:** The Gmail connector cannot read a private attachment. Summarize verified messages and ask before opening signed-in Gmail via computer use. Send nothing.

**Bad:** Open Gmail in a browser while the functioning Gmail connector can retrieve the same message; silently switch to the signed-in interface after a connector error.

## Completion check

- [ ] Correct connector used first.
- [ ] Browser fallback justified by risk tier and actual need.
- [ ] Sensitive-account and consequential actions had required approvals.
- [ ] Evidence was verified; proposals were not described as completed actions.
- [ ] Tool-call, time, and token savings are claimed only when observed.

**Authority:** The current task, platform/tool access controls, and stricter task-specific rules take precedence. This Markdown file documents a policy; it does not enforce Work-wide settings on its own.
