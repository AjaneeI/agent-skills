---
name: plugin-first-execution
description: Route account and project tasks through purpose-built connectors before browser or computer use. Use for ChatGPT Work, automations, or agent workflows that access external services and need explicit read/write boundaries, handoffs, good and bad examples, and verifiable outcomes.
license: MIT
metadata:
  version: "1.1.0"
---

# Plugin-First Execution

## Purpose and trigger

Use this skill when an agent must read or act across external systems such as email, calendars, tasks, CRM, documents, events, or source code.

**Goal:** Deliver the authorized outcome with reliable sources, the least necessary access, and no avoidable browser/computer navigation. **Tool efficiency never overrides correctness, privacy, or necessary verification.**

Read the companion [Human- and Agent-Readable Instruction Standard](../../docs/human-agent-readable-standard.md) when writing or revising a skill, prompt, or Markdown instruction.

## Before using tools

Establish the task's **objective**, **inputs and sources of truth**, **permitted actions**, **prohibited actions**, **user approval requirements**, **deliverable**, and **evidence needed to declare success**. If a significant permission is unknown, do not infer authorization.

## Tool routing

Use a functioning, dedicated connector for supported operations. Examples below are **preferred routes, not proof that a service is installed, authenticated, or sufficient**.

| Information or action | Prefer | Avoid when connector works |
| --- | --- | --- |
| Personal Gmail messages and threads | Gmail connector | Signing into Gmail through browser/computer |
| Google meetings and availability | Google Calendar connector | Navigating the calendar UI |
| Google Drive files and native Docs/Sheets/Slides | Google Drive connector | GUI downloads or edits |
| Professional context and operating rules | Notion connector | Copying data through browser navigation |
| Tasks and project status | Asana connector | Point-and-click task inspection |
| Contact history and CRM updates | HubSpot connector | Browser-based CRM work |
| Company/contact enrichment | Apollo.io or authorized service connector | Ungrounded guesses or unnecessary scraping |
| GitHub code, issues and pull requests | GitHub connector | Browser navigation for supported repository operations |
| Event registration and management | Luma connector | Browsing an organizer dashboard for supported actions |
| Designs and marketing assets | Canva connector | GUI editing when a supported API action fits |
| Current public facts | Public search | Private account access via search |
| Unsupported UI-only operation | Browser/Computer Use *if authorized* | Pretending a connector can perform it |

**Never use public web search to expose or retrieve personal-account contents.** Do not send private information into an unrelated tool as a workaround.

## Required workflow

1. **Plan:** Determine the smallest authorized route that can satisfy the objective.
2. **Select sources:** Use the source's designated connector before any generic GUI.
3. **Retrieve narrowly:** Search scoped dates/keywords; open full items only when a candidate needs verification.
4. **Reconcile:** Compare current authoritative evidence against stale notes or trackers; avoid repeated retrieval of the same record.
5. **Draft or act within authority:** Clearly distinguish a proposed action from a completed one.
6. **Validate:** Verify material factual claims and check the system-of-record response for any permitted write.
7. **Hand off:** Report results, blockers, pending approvals, and observable efficiency metrics without inventing them.

## Permission boundary

**Default for unspecified tasks: read and analyze only.** Drafting text in the response is not sending it.

- **MAY:** Search relevant authorized records; read, compare, summarize, and draft proposals.
- **MUST request explicit approval before:** Sending messages, submitting applications, inviting people, publishing, changing sharing permissions, modifying records, initiating payment, or making external commitments, unless that specific action is already clearly authorized in the current task.
- **MUST NOT:** Bypass a failed connector using another authenticated access route without approval; broaden access by delegation; fabricate source checks; send personal data to unrelated apps; or claim a tool ran without evidence.
- **MUST respect:** Platform permissions, organizational policy, stronger current instructions, and safety constraints. This skill cannot grant capabilities.

For tasks with explicit authorized writes, use only the named destination and verify the result. Do not create duplicate trackers merely to log progress.

## Browser and computer fallback: risk-based policy

**Global Work default:** Allow low-risk read-only browser/computer fallback when necessary, but require approval before authenticated fallback for sensitive accounts or consequential actions. This does not change stricter task-specific rules.

| Tier | Source examples | Fallback rule |
| --- | --- | --- |
| **Low** | Public documentation, public event pages, or expressly preapproved non-sensitive read-only sources | May use browser/computer when search or the designated connector is insufficient and existing permissions allow it. No login expansion or state changes. |
| **Medium** | Signed-in Notion, Asana, HubSpot, Google Calendar/Drive, private project dashboards | Ask before switching from the connector to an authenticated browser/computer route unless the exact fallback was already approved for this task. |
| **High** | Personal Gmail, health, finances, credentials, sensitive records or security settings | Ask before any authenticated GUI fallback; otherwise return verified partial results. |

**All tiers:** Sending, publishing, changing sharing permissions, submitting applications, making purchases, or modifying external records require explicit authorization for that task. Classify both **information sensitivity** and **action impact**; a public page does not make a send or purchase low-risk. Read-only browser interfaces can have side effects: stop before state-changing clicks.

**Fail closed:** A broken, missing, or insufficient connector does not grant another access method. Use another route only when the tier and existing authorization allow it. Do not silently switch to an authenticated browser/computer session. For public websites, prefer web search first. Keep a human approval handoff for medium/high exceptions.

**Existing pilot exception:** The Networking & Application Follow-up automation retains its stricter ask-first instruction. This global skill neither edits nor weakens that automation.

**Example allowed:** Search fails to show the full agenda of a public AI conference. Read the publicly accessible agenda in a browser, cite the result, and do not sign in or RSVP.

**Example requiring approval:** The Gmail connector cannot access a personal attachment. Do not open signed-in Gmail in a browser. Explain what was verified and ask before switching access methods.

**Example prohibited:** Calling a private financial account “low-risk” merely because only a balance is needed.

This is an instruction policy, not a runtime permission grant or proof that ChatGPT Work has globally loaded it.

## Good output

> Reviewed four relevant Gmail threads using the Gmail connector and checked two associated calendar events through Google Calendar. One recruiter asked for availability by Tuesday. A reply draft is ready for approval. **Nothing was sent or changed.** Source links accompany the finding. Browser/computer actions: zero observed.

## Bad output

> Opened the browser, signed into Gmail, scrolled through the inbox, took screenshots, and sent a follow-up because a task was marked overdue.

**Why it fails:** Unnecessary GUI routing, potential stale-state reasoning, and an unauthorized external send. A polished summary cannot compensate for an incorrect process.

## Handoff and failure response

When action, identity, access, or recipient is ambiguous, state the uncertainty and the smallest decision needed. Never claim full completion from partial evidence. If tool-call traces are unavailable, say actual routing or token savings **cannot be verified**.

## Acceptance checklist

- [ ] Necessary information was retrieved through the designated connector when available.
- [ ] No unnecessary browser/computer route was taken.
- [ ] Evidence was checked for freshness, contradictions, and duplicated actions.
- [ ] No unauthorized writes, sends, or publication occurred.
- [ ] Good/bad behavior and user approval gates were honored.
- [ ] Results distinguish verified facts, recommendations, and incomplete work.
- [ ] Claims about tokens, time, or efficiency are based on observed metrics, not assumptions.

## Evaluation

Test one read-only task first, such as recent inbox triage. Compare **accuracy**, **number of tool calls**, **GUI/browser calls**, **retries**, **elapsed time**, and **tokens/credits only if available**. Record negative outcomes. An instruction-only skill is **not a security enforcement boundary**; independently enforced capabilities and logged tool traces are required for strong guarantees.

**Related skills:** [Constraints-First Execution](../constraints-first-execution/SKILL.md), [Least-Privilege Tool Boundaries](../least-privilege-tool-boundaries/SKILL.md), and [Verified Status Reconciliation](../verified-status-reconciliation/SKILL.md).
