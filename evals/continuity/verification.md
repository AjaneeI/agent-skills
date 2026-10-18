# Pilot implementation verification

## What exists

The approved first iteration adds a Continuity v0.1.1 candidate with explicit precedence, six synthetic pilot scenarios, an offline trace scorer and 34 scorer regression tests. All other ten skill definitions remain unchanged. The candidate is not merged or installed by this change.

## Local development evidence

The initial 26 tests were observed failing before the scorer existed, then passing after implementation. Adding comparison controls exposed two failures: repeated native captures could be counted twice, and different skill versions could be pooled. After repair all 34 scorer tests passed in Python 3.13. These are scripted fixtures, not observations of an agent. The source published on GitHub also receives the repository CI checks; exact published-head CI, not a local file count, governs integration readiness.

## What is not verified

- Live Codex baseline or skill-enabled behavior: not run.
- Successful skill discovery/installation on the owner's Mac: not observed.
- A native collector and independently reviewed trace mapping: not implemented or exercised.
- ACS policies, runtime enforcement or Microsoft ASSERT execution: not implemented.
- Statistical superiority, safety guarantees or production readiness: not established.

The current chat runtime has no local Codex executable or Mac runtime access. No substitute model was invoked and no paid fallback was used to fabricate a behavioral comparison. Work continued on the independent authorized scoring and precedence tasks.

## Remaining gate

Collect complete native traces in isolated Codex contexts using the protocol in README.md, independently review their normalization, then use the frozen scorer to report matched outcomes, resource costs, missing data and limitations. This is unfinished approved evaluation work, not a request to approve the same scope again. Changes to runtime permissions, paid providers, experimental conditions or research claims still require their own applicable authorization.
