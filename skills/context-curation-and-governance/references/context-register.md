# Context Register — Human/Agent Template

Use only fields needed for the task. Do not paste personal, restricted, or secret source contents into a public repository.

## Problem and owner

- Problem / affected workflow:
- Intended "so that" outcome:
- Problem Owner (verified authority or unknown):
- Context Curator (verified authority or unknown):
- Technical implementer / consumer:
- Context version and date:
- Next review **trigger** (not a compulsory cadence):

## Source inventory

| Source reference | Source owner | Effective date | Last verified | Authority/reliability | Sensitivity | Status | Refresh trigger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (link or private internal ref) | (verified or unknown) | (date/unknown) | (date/unknown) | (reason) | public/internal/restricted | verified/stale/conflicting/unverified | (event) |

## Conflict and decision record

| Conflict / exception | Evidence on both sides | Decision owner | Status | Resolution and source |
| --- | --- | --- | --- | --- |
| (issue) | (references) | (role) | open / decided | (dated approval or unknown) |

## Propagation and validation

- Downstream skills / systems affected:
- Changes actually made:
- Changes proposed but **not** made:
- Legitimate success example:
- Prohibited behavior example:
- Ambiguous / multi-turn case:
- Observed test/trace URL (or **not run**):
- Current disposition: verified / partial / blocked / unverified

**Good:** An approved owner updates an effective policy, its context block is versioned, and consumers are tested for correct handling of old/new policy.

**Bad:** A model silently resolves contradictory policies, changes production actions, and reports success with no source check.
