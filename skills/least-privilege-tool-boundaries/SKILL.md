---
name: least-privilege-tool-boundaries
description: Design and audit least-privilege agent tool capabilities. Use when connecting AI workers to local services, APIs, files, databases, production systems, or delegated execution tools with differing trust boundaries.
license: MIT
metadata:
  version: "0.1.0"
---

# Least-Privilege Tool Boundaries

## Purpose
Grant only the capabilities needed for a specific approved task and prove that failure or routing mistakes cannot broaden authority.

## Workflow
1. Enumerate the task's requested outcomes, allowed evidence sources, forbidden operations and trust boundaries. Identify which tool calls actually need write permissions.
2. Compute effective capabilities from the **intersection** of user authorization, task policy, runtime/tool availability, and worker role. Missing authorization means no access.
3. Enforce capabilities at the actual execution boundary, not merely through natural-language prompts.
4. Separate read-only inspection from mutations, approvals, purchases, publishing, and external communications. Demand distinct grants for higher-impact actions.
5. Test rejection paths: unknown tool, unapproved path/table, nested delegation, tool-call overflow, spoofed observation, secret-bearing output, and access denied.
6. Log actual tool invocations, not model-authored descriptions of what it claims to have done. Redact or securely store sensitive evidence.
7. Disable fallback routes that can silently reach a broader provider or spend money unless separately authorized.
8. Review new plugins and integrations as new trust boundaries, never as harmless extensions.

## Guardrails
No instruction-only assertion substitutes for runtime enforcement. Do not bypass external authorization, branch protection, SQL guards, or read-only database limits.

## Output
[Capability matrix](references/capability-matrix.md), proof of enforced rejection, and residual risks.

## Verification
Demonstrate that routing errors, malicious model output, or missing permissions still fail closed without access expansion.
