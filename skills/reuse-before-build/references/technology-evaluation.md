# Technology evaluation record

Keep this record with the owning project. A public skill does not make its project-specific decision records public. Use **unknown** when evidence is unavailable.

## Requirements

Decision ID, date, owner, scope revision, authorized budget, required behavior, acceptance checks, non-goals, runtime/interface constraints, data sensitivity, and operational boundaries. Record existing code and dependencies inspected, a simpler configuration/removal alternative, and whether this is a full review or a proportionate small change.

## Candidates

Evaluate at least three credible existing implementations when available. For each, record:

| Dimension | Required evidence |
| --- | --- |
| Identity | Project, primary URL, exact version or commit, retrieval date. |
| Fit | Requirement coverage, gaps, runtime and interface compatibility. |
| Maintenance | Release/support activity, maintainership, issue responsiveness, deprecation signals. Stable software is not automatically abandoned. |
| Security | Advisory search/date, applicable unresolved issues, dependency exposure, update process, relevant controls and unknowns. |
| License | Exact license source/version, redistribution and attribution obligations, compatibility questions. Public availability alone is not a license. |
| Integration | Adapter work, migration, tests, expertise needed, estimates versus measured checks. |
| Ownership | Runtime costs, upgrades, support, operations, migration and exit cost. |
| Verification | Reproducible check and observed outcome, distinguished from documentation-only evidence. |

## Decision

Selected approach; requirement-based reasons; rejected alternatives; unresolved evidence; required authorization; smallest adoption check; exit plan where relevant; review trigger. Do not install a service merely to complete this table.

## Custom-build exception

For custom infrastructure or a genuine candidate shortfall, record searches, excluded candidates and reasons, missing capabilities, why configuration or a thin adapter is insufficient, lifecycle owner/cost, tests, approval scope, and reconsideration trigger. Do not fabricate an option or silently weaken requirements.

## Verification

Link exact commands, artifacts, and versions only when checks actually ran. Preserve negative results. Implementation approval, executed integration, independent review, and deployment are separate states. Apply `safe-publication-review` to public extracts.
