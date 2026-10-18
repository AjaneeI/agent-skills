# Capability matrix

| Actor / workstream | Operation | Resource | Authorization source | Enforced where | Evidence | Status |
|---|---|---|---|---|---|---|
| analyst worker | SELECT | synthetic development table | task policy | SQL validator + read-only identity | test / trace | pending |
| analyst worker | DELETE | any table | none | guard | rejection case | denied |

For each capability distinguish model-visible tool description from runtime implementation. A prompt saying 'read only' is not an enforcement boundary.