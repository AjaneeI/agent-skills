# Gate record

Store this beside the existing protocol or tracking issue. Do not create a duplicate database. Examples are synthetic.

## Gate

Record gate ID, purpose, downstream action, gate type (evidence, technical readiness, human permission), contract revision, owner, and state. States: proposed, ready_for_review, accepted, blocked, failed, superseded.

## Dependencies

List prerequisite IDs and their applicable evidence or decisions. Each prerequisite needs an observable acceptance condition. Identify independent authorized work explicitly. Detect missing or cyclic dependencies before advancing the affected action.

## Version binding

Bind applicable source, data, scorer, model, prompts, configuration, environment, and invocation/budget limits. An evidence gate accepted for D1/S1 does not automatically cover D2/S2. Use exact known identifiers; absent information is unknown, not a fabricated value.

## Evidence

Link observed results, test commands, artifacts, exact revisions and reviewer scope. Distinguish builder results, separate review, and independent reproduction. Passing local tests does not complete a live experiment or authorize its invocation.

## Decision

Record who or what may accept the gate under the existing contract, the actual decision, its scope and evidence reference, and any unresolved item. "Ready for review" is not "accepted." A routine automated gate may advance when already authorized; do not manufacture a human decision requirement.

## Invalidation

Document the change, affected dependencies, applicability assessment, historical acceptance retained, and exact recheck needed. Do not silently broaden criteria or relabel old evidence. Reopening one gate does not invalidate unrelated accepted work.

## Permitted next action

Example: evaluator review is unresolved, so the confirmatory run is blocked; permitted unit tests and documentation continue. Name the exact missing decision once and a resume condition. If a prior frozen invocation may have executed, preserve uncertainty and reconcile the receipt; do not count it as a free retry.

Keep hypotheses, setup failures, permission decisions, and statistical conclusions distinct. Update only the existing authoritative record after checking actual state.
