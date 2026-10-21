# Contributing and public-skill policy

## Destination and boundaries

All newly authored, reusable **non-personal skills** belong in this GitHub repository as open-source assets after review. Keep one canonical version and synchronize reviewed, pinned copies into consuming environments. A conversation or local installation must not be the only authoritative copy.

Personal workflows, credentials, account configuration, private identifiers, confidential sources, and relationship or workplace context stay private. For a mixed workflow, author a separate generalized skill with synthetic examples. Changing names in copied private material is not adequate by itself.

Existing personal skills are not automatically approved for migration. Publication authority covers only its actual scope and reviewed candidate; it never authorizes confidential disclosure. Preserve the MIT license and required attribution. Do not relabel incompatible third-party material as MIT.

## Workflow

1. Inspect the catalog for an equivalent skill. Extend suitable work or record the new skill's distinct purpose.
2. Define trigger, outcome, authority boundaries, expected behavior and negative cases. Apply `reuse-before-build` before substantial infrastructure choices.
3. Author concise `skills/<name>/SKILL.md` instructions and focused Markdown references. This catalog remains instruction-only. Keep client installation details in documentation.
4. Write tests before the change, run the complete repository suite, and validate format. Record exactly what ran. Static checks and text-only probes are not runtime compliance evidence or privacy guarantees.
5. Apply `safe-publication-review` before any public upload. Review files, every new commit, metadata, messages, PR text, images and attachments. Obtain the independent review required by the project; label review methods and limitations truthfully.
6. Resolve blocking findings privately. Reuse existing approvals within their scope without asking for the same approval repeatedly. Unresolved privacy, provenance, licensing or authority keeps the affected candidate private.
7. Publish the reviewed candidate on a scoped branch and PR when authorized. Read back exact provider state. A public draft is already disclosed. Merge and installation remain separate actions.

## Professional quality

Use neutral engineering language, portable paths, and fabricated examples. Preserve material technical constraints, failed cases and unrun checks accurately without exposing personal narratives or judgments about identifiable people. Do not invent adoption, endorsement, performance, security or cross-client compatibility claims.

Combine mechanical checks with contextual review. No finite scan guarantees the absence of sensitive information.

## Verification

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Existing CI runs `skills-ref` over the catalog. See [verification status](docs/verification-status.md), [governance scenarios](tests/governance-scenarios.md), and the [cross-agent playbook](tests/agent-evaluation-playbook.md). A test specification is not a completed evaluation.
