# Human- and Agent-Readable Instruction Standard

**Status:** User-approved authoring standard  
**Version:** 1.0.0  
**Established:** 2026-11-13  
**Applies to:** Skills, prompts, Markdown instructions, agent policies, and automation playbooks authored for this workflow.

## Purpose

Every instruction artifact must be **easy for a person to read** and **unambiguous for an AI agent to execute**. Clarity, reliability, and safety take priority over clever wording or compactness alone.

**Quick rule:** A new reader should understand *what, why, how, with which tools, under whose authority, and what counts as done* without needing to reverse-engineer the author's intent.

## Required authoring rules

1. **Lead with the purpose.** State who the instruction is for, when to use it, and what it produces.
2. **Use descriptive headings.** Prefer short sections, numbered workflows, plain-language explanations, and Markdown that renders well on GitHub.
3. **Make directions executable.** Use explicit verbs such as *read*, *compare*, *draft*, *verify*, *stop*, or *request approval*. Separate **MUST**, **MAY**, and **MUST NOT**.
4. **Define the inputs and source of truth.** Name the relevant documents, systems, authority, and freshness requirements. Do not assume the reader can access an unstated system.
5. **Route tools deliberately.** Say which connector/tool handles each source and action; distinguish preferred tools from permitted fallbacks.
6. **State boundaries.** Define which reads and writes are authorized, what may be shared or published, and which actions require confirmation.
7. **Describe the handoff.** Specify exactly when to ask a human, stop, return partial results, or escalate.
8. **Show good and bad examples.** Demonstrate both a successful output and a concrete failure. Explain the distinction.
9. **Make success testable.** Include acceptance checks, evidence expectations, and honest failure states. Never assert unobserved tool compliance.
10. **Keep the source safe to publish.** Never embed passwords, secrets, private identifiers, confidential messages, or unnecessary personal data in a public skill or Markdown file.
11. **Avoid needless verbosity.** Keep the main file scannable; move optional background, extended examples, and specialized reference material into linked Markdown files when warranted.
12. **Preserve portability.** Instructions may guide behavior, but cannot grant credentials, runtime permissions, or guarantee that a particular client automatically loads the file.

## Suggested document structure

Use these sections when applicable; omit only those that are genuinely irrelevant to the task.

| Section | Question it answers |
| --- | --- |
| Purpose / when to use | Why does this exist and what triggers it? |
| Inputs / sources | What evidence or access is required? |
| Tool routing | Which tool must handle which information or action? |
| Procedure | What are the steps, in order? |
| Permissions | What can and cannot be done? |
| Handoff / failure | When do we stop, ask, or deliver partial results? |
| Good output | What does a successful result look like? |
| Bad output | Which tempting behavior is incorrect? |
| Acceptance tests | What observations prove the result? |

## Example: good instruction

> **Goal:** Summarize relevant application replies from the last seven days.  
> **Source:** Search the connected Gmail account with the Gmail connector; read only matching threads.  
> **Allowed:** Read and summarize; draft suggested replies in the answer.  
> **Not allowed:** Send emails, change CRM records, or open Gmail through GUI browsing.  
> **Handoff:** If Gmail access fails, report the missing source instead of silently switching to Computer Use.  
> **Done:** Every proposed follow-up identifies a fresh source, a reason to act, and whether a message was sent (normally, no).

This is readable aloud, scannable in Markdown, and specific enough for an agent to follow and evaluate.

## Example: bad instruction

> Check my stuff, use whatever tools you need, finish everything, and tell me when done.

**Why it fails:** No named source, time window, authority, tooling preference, scope, definition of completion, approval gate, or handling of failed access.

## Review checklist

- [ ] A human can identify the purpose and expected output in under a minute.
- [ ] An agent can determine exact inputs, ordered steps, and tool choices.
- [ ] Rules separate authorized actions from forbidden actions.
- [ ] The document has at least one realistic good and bad example when behavior is consequential.
- [ ] Handoff and fallback behavior cannot silently expand authority.
- [ ] Completion evidence is observable; unexecuted tests are labeled as unexecuted.
- [ ] Links are supportive, not essential to understanding core instructions.
- [ ] No confidential data or credentials are included.

## Authority and limits

This is an **authoring standard**, not a permission grant or an enforcement mechanism. Current user instructions, actual tool/runtime permissions, organizational requirements, and applicable law take precedence. Evaluate behavioral compliance using real execution traces, not merely the presence of this document.

**Companion skill:** [Plugin-First Execution](../skills/plugin-first-execution/SKILL.md).
