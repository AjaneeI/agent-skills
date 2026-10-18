# Evaluator control matrix

| Case ID | Construct | Control type | Expected | Observed | Evidence | Defect / approval |
|---|---|---|---|---|---|---|
| example-positive | scope | known-good | accept | pending | link | none |
| example-negative | evidence | spoofed value | reject | pending | link | none |
| example-alternative | execution | equivalent allowed SQL | accept | pending | link | none |

Record task-template lineage and whether a control used live tools, test doubles or historical artifacts. Never treat test doubles as live system confirmation.