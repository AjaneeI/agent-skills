---
name: one-shot-experiment-control
description: Plan and execute a preregistered, bounded experiment at most once with immutable inputs and honest negative outcomes. Use for frozen AI benchmarks, one-attempt tool evaluations, and controlled comparisons where retries contaminate evidence.
license: MIT
metadata:
  version: "0.1.0"
---

# One-Shot Experiment Control

## Trigger
Use whenever an experimental protocol restricts invocation counts, controls, prompt changes, or retries.

## Preflight (no experimental calls)
1. Name the exact authorized hypothesis, task IDs, configuration, commit, model, tools, data, reference/scorer version, allowed invocations, and measured outcomes.
2. Verify the run is permitted by the owner **and** any prerequisite research gates. A proposed configuration or passing unit tests is not permission to run it.
3. Check resources, environment reachability, private data and tool restrictions without invoking the frozen test input.
4. Record hashes and a planned evidence destination; require that captured errors can be preserved as observed.
5. Classify preflight as ready, blocked, or failed. Never label preflight passing as scientific success.

## Execute
6. Execute the approved number of attempts once. Preserve raw errors, timeouts, and unknown or unscored results without repair.
7. Immediately freeze and hash evidence, including start/end configuration and any observable resource metadata.
8. Compare the result only under the original scorer and interpretation rules. A repaired runtime or different tool description becomes a new versioned experimental condition; it cannot silently replace the failed run.

## Following a failure
Do not retry, re-prompt, loosen guards, change expected answers or claim success. Diagnose using offline records if allowed; propose changes under a separately approved configuration and invocation.

## Output
A run manifest with explicit **attempts consumed**, **attempts remaining**, evidence hashes, and a stop/continuation decision. See [preflight checklist](references/preflight.md).

## Scientific boundary
A standalone qualification run cannot establish cross-architecture superiority or generalized model reliability.
