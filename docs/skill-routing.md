# Engineering skill routing

This catalog contains 15 instruction-only skills in this candidate. Load the smallest relevant set, not every skill for every task. Availability in GitHub is not installation, permission, observed behavior, or a merged release. See [activation](skill-activation.md) and [verification status](verification-status.md).

## One role per skill

| Situation | Skill | Distinct deliverable |
| --- | --- | --- |
| Define a bounded objective and non-goals | [constraints-first-execution](../skills/constraints-first-execution/SKILL.md) | Authorized requirements and acceptance contract |
| Choose infrastructure or a major dependency | [reuse-before-build](../skills/reuse-before-build/SKILL.md) | Evidence-backed comparison and reuse/custom decision |
| Remove unjustified implementation complexity | [code-bloat-triage](../skills/code-bloat-triage/SKILL.md) | Tested simplification rationale |
| Assign independently executable work | [safe-parallel-delegation](../skills/safe-parallel-delegation/SKILL.md) | Isolated work contracts and integration evidence |
| Bound a tool's capabilities | [least-privilege-tool-boundaries](../skills/least-privilege-tool-boundaries/SKILL.md) | Capability and enforcement checks |
| An action crosses an actual approval boundary | [approval-boundary-management](../skills/approval-boundary-management/SKILL.md) | One specific decision packet |
| An existing evidence/decision prerequisite controls advancement | [research-gate-management](../skills/research-gate-management/SKILL.md) | Version-bound gate status and permitted next work |
| Check that a grader measures the intended behavior | [evaluator-validity-audit](../skills/evaluator-validity-audit/SKILL.md) | Evaluator controls and validity findings |
| Freeze statistical methods before held-out results | [statistical-calibration-freeze](../skills/statistical-calibration-freeze/SKILL.md) | Prespecified analysis and calibration record |
| Run an explicitly attempt-limited experiment | [one-shot-experiment-control](../skills/one-shot-experiment-control/SKILL.md) | Invocation accounting and immutable outcomes |
| Capture and retain what actually happened | [evidence-preservation](../skills/evidence-preservation/SKILL.md) | Artifact manifest and preserved failures |
| Decide whether evidence supports a particular claim | [evidence-based-verification](../skills/evidence-based-verification/SKILL.md) | Scoped verdict, provenance, and unknowns |
| A workstream is blocked but others may proceed | [autonomous-execution-continuity](../skills/autonomous-execution-continuity/SKILL.md) | Checkpoint and independently authorized next task |
| Reconcile repository and project records | [verified-status-reconciliation](../skills/verified-status-reconciliation/SKILL.md) | Minimal updates backed by authoritative evidence |
| Prepare a public artifact or skill | [safe-publication-review](../skills/safe-publication-review/SKILL.md) | Reviewed disclosure candidate and permission boundary |

## Composition and precedence

Higher-priority instructions and the actual project contract govern every skill. A skill cannot grant another skill permission. Specific frozen protocols, publication restrictions and protected resources remain in force. When directions conflict, stop only the affected action, retain evidence, and resolve the conflict with its owner. Do not invent a new approval for an action already permitted.

A normal implementation may use constraints, reuse selection when warranted, bounded delegation, evidence capture and verification. An experiment additionally needs its applicable evaluator, statistical and prerequisite gates before invocation. Synchronization and public publication are subsequent actions with their own evidence and authority.

**Keep the evidence stages distinct:** preservation stores artifacts; verification decides which claim they support; research gates decide whether prerequisites permit the next step; reconciliation propagates supported status. None is a substitute for actual runtime enforcement or a separate reviewer where required.

## Scope of this catalog completion

The original eleven skills and the two governance additions already cover the other named engineering workflows. The two new completion skills fill claim-adjudication and prerequisite-management gaps; they do not introduce another orchestration system. Generic repair, delivery and cross-project work should compose these existing roles rather than accumulate synonymous skills.

Personal application, meeting, timesheet or study configuration is not part of this public engineering catalog. No private workflow was migrated. A future generalized skill needs a distinct reusable purpose and the same publication review.
