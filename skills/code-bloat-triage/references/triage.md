# Bloat triage register

| Candidate | Why suspicious | Required behavior | Evidence | Change and tests | Decision |
|---|---|---|---|---|---|
| duplicate validation wrapper | repeated rules | reject unsafe SQL | tests/trace | targeted consolidation | pending |

Beware Goodhart's law: smaller files or lower LOC can correlate poorly with better maintenance. Prefer measurable review cost and error reduction.