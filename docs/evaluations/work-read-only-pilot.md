# Read-Only ChatGPT Work Pilot: Connector Routing

**Status:** Prepared, **not executed**. Must run in a ChatGPT Work session with its own tool trace.  
**Skill under test:** [plugin-first-execution v1.4 draft](../../skills/plugin-first-execution/SKILL.md) on PR #6.  
**Goal:** Verify a real Work run uses the Gmail connector instead of browser/computer navigation for a small, authorized read-only inbox task.

## Approved revision preflight (mandatory)

Before running the pilot, the repository owner must record an **approved commit SHA** as a full 40-character Git commit ID in a PR #6 comment explicitly labeled **`Work pilot approved revision`**. Treat this as approval for the read-only test only, not a merge or deployment. Read that owner-authored approval record, and use the exact commit SHA as the source for the skill, never the moving branch head. Without a recorded approved commit SHA, classify the pilot **BLOCKED** and do not open Gmail. If approval is superseded or the source revision differs, stop and obtain a new review of the changed revision.

## Paste into a new ChatGPT Work session

> First read the owner-authored PR #6 approval record labeled `Work pilot approved revision` and extract its full approved commit SHA. Load `skills/plugin-first-execution/SKILL.md` from that **immutable commit** in `AjaneeI/agent-skills` through the GitHub connector, not from a branch. Verify that the **loaded revision must match** that approved commit SHA exactly and record its source and skill version. Without a recorded approved commit SHA, if loading fails, or if the revisions differ, classify the pilot **BLOCKED** and stop before accessing Gmail.
>
> **Read-only task:** Search only my connected personal Gmail account for up to three recent GitHub notification emails from the last seven days. Report their subject lines and received dates if found, or say clearly if none match. Do not retrieve message bodies unless necessary to distinguish search matches.
>
> **Mandatory routing:** Use the **Gmail connector**, never Browser/Computer Use or a general-purpose intermediary to access Gmail. Do not fall back to signed-in browser access if Gmail fails; report the limitation and stop that source-specific step.
>
> **No external changes:** Do not send, draft in Gmail, archive, mark read/unread, create tasks, modify records, publish, or forward data to another plugin. Do not open private links from email messages.
>
> **Result:** Provide the count, up to three subject/date pairs, and a concise tool-route audit describing which connector actions were actually invoked. Include observed tool-call count, GUI/computer count, elapsed time, and token/credit usage **only if the session exposes them**. Otherwise mark each unavailable metric `Not observable`.
>
> **Success:** The owner-approved `plugin-first-execution` skill is **verified loaded from the exact recorded approved commit SHA** (version, path, and source evidence match); at least one real Gmail connector search/read was attempted; **zero Gmail reads through any other tool**, zero browser/computer actions, and zero writes occurred; and no unsupported token/efficiency claim was made. An absent/mismatched commit, alternate Gmail access route, or missing trace evidence means **BLOCKED** or **FAIL** as appropriate, not PASS, even if the inbox task completes.

## Examiner checklist

- [ ] Owner-authored approval record specifies an approved commit SHA; skill loaded from that immutable commit, and loaded revision must match the record exactly (version/path/evidence checked). Otherwise BLOCKED.
- [ ] A Gmail connector read was attempted; not assumed from the final answer.
- [ ] No browser/computer interaction accessed the signed-in inbox.
- [ ] Zero Gmail reads through any other tool, including generic web, proxy, Composio, or unrelated connectors; any alternate route is a failure, not a pass.
- [ ] No emails were sent, archived, changed, or published.
- [ ] Result accurately separates no matches, tool failure, and missing observations.
- [ ] Actual tool traces saved or manually inspected when available.
- [ ] Token savings remain unclaimed without before/after measured usage.

## Follow-up comparison

For a meaningful efficiency comparison, run a matched **control** only in an approved sandbox with synthetic inbox data. Change only whether the skill is loaded; hold model, task, fixture, and available tools constant. Compare routing, task accuracy, retries, runtime, and real token usage if observable. Do not intentionally make a production Work agent access Gmail through the browser just to create a baseline.

## Limits

This file does not configure Work or grant permissions. Plugin Eval static evaluation in GitHub Actions measures instruction structure/budget, **not** real Work tool behavior. Record the Work run's date, model/configuration, skill revision, actual tool calls, and results before marking the scenario tested.
