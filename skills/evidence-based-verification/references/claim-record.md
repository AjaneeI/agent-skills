# Claim record

Use this in the existing issue or evidence store. It is a record shape, not a new service. All examples below are synthetic.

## Claim

State one observable assertion, acceptance criterion, and requested stage. Example: "Candidate B passes the specified offline regression suite." This is not the assertion "Candidate B is deployed."

## Bindings

Record task and scope revision; source commit/tree or artifact digest; configuration and input/suite revision; environment; relevant time; and verifier version when available. Mark absent fields unknown or not applicable with a reason.

## Evidence

| Required observation | Actual source and revision | Observed result | Provenance | Applicable to claim? |
| --- | --- | --- | --- | --- |
| Protected regression suite on B | Only a log for A is available | Historical pass for A | Builder log; not rerun | No |

Include actual commands and exit codes when executed, provider readback for remote effects, and reviewer scope. Record assertions separately from observations. Do not fill in plausible commands as executed evidence.

## Outcome dimensions

| Dimension | Synthetic example |
| --- | --- |
| Execution/effect | Denied; independent fixture check saw no write |
| Safety test | Passed for that forbidden-write fixture |
| Business task | Not completed |
| Authority | Write remained prohibited |
| Claim verification | Verified only for the denial/no-effect assertion |
| Review | Not supplied; required review remains outstanding |

A timed-out publication is a different case: effect unknown, task success unknown, and completion unverified until provider reconciliation. Retrying is not verification.

## Verdict

Choose verified, failed, or unverified for the exact claim. State limits, required but missing checks, historical/superseded evidence, and contradictions. Record denial and approval-needed states separately. Byte integrity does not authenticate authorship or establish correctness.

## Next action

Identify the smallest permitted observation or correction, its owner, and the evidence that would resolve the gap. Link to existing authority or a specific unresolved boundary. Preserve raw evidence in authorized storage; separately review anything intended for public release.
