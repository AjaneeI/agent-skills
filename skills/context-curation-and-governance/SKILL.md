---
name: context-curation-and-governance
description: Govern the source context an agent relies on. Use when policies, operating procedures, knowledge bases, instructions, or role-specific source material have multiple owners, versions, contradictions, freshness requirements, or privacy boundaries.
license: MIT
metadata:
  version: "0.1.0"
---

# Context Curation and Governance

## Purpose and trigger

Ensure that information used by people and agents is **relevant, traceable, current enough, authorized, and maintained**. This is a narrow knowledge-governance skill, not a general data warehouse proposal and not permission to access source systems.

Use when context comes from multiple documents, teams, tools, or policy versions; when answers depend on changing organizational rules; or when a skill must be updated after underlying process changes. Skip a formal register for simple, stable, single-source tasks.

## Accountable roles

- **Problem Owner:** defines the user/business problem, accepts tradeoffs, and resolves decisions within their actual authority.
- **Context Curator:** maintains the source register, checks contradictions and freshness, proposes version updates, and seeks authorized decisions where needed.
- **Technical implementer/agent:** retrieves only permitted context, builds the smallest useful capability, and validates observed behavior. It does not inherit the decision rights of either human role.

A person may hold multiple roles if independently authorized. Never infer authority from a job title.

## Inputs

Define the use case and its observable "so that" outcome, affected users and workflows, permitted source systems, known owners, access classification, relevant dates or policy versions, and the context update trigger. If a key owner or source cannot be confirmed, label it **unknown**.

## Procedure

1. **Start with the problem.** Ask what decision or workflow the context enables. Do not collect everything merely because it is available.
2. **Inventory narrowly.** For each material source, capture location/reference, source type, owner, collection date, effective date if applicable, last verification, reliability/authority, access sensitivity, and expiry or review trigger.
3. **Reconcile meaning.** Compare definitions, exceptions, local practices, written policies, and conflicting accounts. Distinguish a newer edit from a higher-authority or currently effective rule.
4. **Assign disposition.** Mark context as verified, valid with caveat, conflicting, stale, unverified, or out of scope. Do not silently promote unverified source text into policy.
5. **Package minimally.** Provide a concise context block containing purpose, source links, applicable rules, exceptions, boundaries, version and owner. Keep private data outside public instructions.
6. **Route decisions.** Where interpretation affects permissions, compensation, legal/compliance duties, sensitive records, or external commitments, request the appropriate owner decision before activating a change.
7. **Version and test.** Record the change, affected skills and downstream consumers, and a small set of permissible/impermissible/ambiguous regression cases. Validate new behavior with observed traces when a runtime agent is available.
8. **Maintain.** Revisit on source revision, owner change, expiration, incident, user correction, or a known behavioral failure. Do not impose arbitrary recurring reviews on truly static context.

## Source conflicts and precedence

Higher-priority current instructions, actual organizational requirements, privacy limits, and authorization controls prevail. In an operational source conflict, preserve both facts and ask the accountable owner; do not let the agent fabricate consensus or automatically trust the newest timestamp.

**Good:** Two onboarding documents give different expense-approval thresholds. Record both versions and effective dates, confirm the authorized policy owner, prevent consequential reimbursements until resolved, and update only the permitted context block after approval.

**Bad:** Feed both documents to the agent, tell it to follow whichever looks recent, and declare the policy resolved without evidence.

**Ambiguous:** A personal working note conflicts with current policy. Preserve the note as historical context; verify applicability and authority rather than treating personal preference as employer policy.

## Handoff and output

Return a compact [context register](references/context-register.md), contradiction/decision log, change impact, next review trigger, and exact unknowns. For a blocked source, return partial verified context and the smallest decision needed. Never fabricate access, ownership, or freshness metadata.

## Acceptance checks

- [ ] Context supports a defined problem and outcome; no indiscriminate bulk collection.
- [ ] Every consequential context claim has a source or is labeled unverified.
- [ ] Owners, effective dates, restrictions, and refresh triggers are stated where relevant.
- [ ] Contradictions and uncertain authority are visible and not silently resolved.
- [ ] No personal or confidential data was published to this public skills repository.
- [ ] Relevant downstream skills/evaluations are identified for regression testing.
- [ ] Actual agent behavior is not called verified without execution traces.

## Boundaries

This skill is **instruction-only**. It cannot grant permissions, establish organizational policy, replace human ownership, or implement ACS runtime enforcement. Kendall Project workshop themes motivate the structure; the procedure and templates here are an engineering adaptation, not a verbatim official standard.
