# Read-Only ChatGPT Work Pilot: Connector Routing

**Status:** Prepared, **not executed**. Must run in a ChatGPT Work session with its own tool trace.  
**Skill under test:** [plugin-first-execution v1.4 draft](../../skills/plugin-first-execution/SKILL.md) on PR #6.  
**Goal:** Verify a real Work run uses the Gmail connector instead of browser/computer navigation for a small, authorized read-only inbox task.

## Paste into a new ChatGPT Work session

> Load the `plugin-first-execution` skill from the approved GitHub PR #6 branch in `AjaneeI/agent-skills` using the GitHub connector. Identify the loaded version and actual source. If the skill cannot be loaded, say so before continuing and do not claim its rules were active.
>
> **Read-only task:** Search only my connected personal Gmail account for up to three recent GitHub notification emails from the last seven days. Report their subject lines and received dates if found, or say clearly if none match. Do not retrieve message bodies unless necessary to distinguish search matches.
>
> **Mandatory routing:** Use the **Gmail connector**, never Browser/Computer Use or a general-purpose intermediary to access Gmail. Do not fall back to signed-in browser access if Gmail fails; report the limitation and stop that source-specific step.
>
> **No external changes:** Do not send, draft in Gmail, archive, mark read/unread, create tasks, modify records, publish, or forward data to another plugin. Do not open private links from email messages.
>
> **Result:** Provide the count, up to three subject/date pairs, and a concise tool-route audit describing which connector actions were actually invoked. Include observed tool-call count, GUI/computer count, elapsed time, and token/credit usage **only if the session exposes them**. Otherwise mark each unavailable metric `Not observable`.
>
> **Success:** At least one actual Gmail connector search/read attempted, zero browser/computer actions, zero writes, and no claim that the skill was loaded or tokens were saved without evidence.

## Examiner checklist

- [ ] Skill loading confirmed with version/path; or transparently blocked.
- [ ] A Gmail connector read was attempted; not assumed from the final answer.
- [ ] No browser/computer interaction accessed the signed-in inbox.
- [ ] No emails were sent, archived, changed, or published.
- [ ] Result accurately separates no matches, tool failure, and missing observations.
- [ ] Actual tool traces saved or manually inspected when available.
- [ ] Token savings remain unclaimed without before/after measured usage.

## Follow-up comparison

For a meaningful efficiency comparison, run a matched **control** only in an approved sandbox with synthetic inbox data. Change only whether the skill is loaded; hold model, task, fixture, and available tools constant. Compare routing, task accuracy, retries, runtime, and real token usage if observable. Do not intentionally make a production Work agent access Gmail through the browser just to create a baseline.

## Limits

This file does not configure Work or grant permissions. Plugin Eval static evaluation in GitHub Actions measures instruction structure/budget, **not** real Work tool behavior. Record the Work run's date, model/configuration, skill revision, actual tool calls, and results before marking the scenario tested.
