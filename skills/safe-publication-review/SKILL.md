---
name: safe-publication-review
description: Use when preparing a skill, document, code change, example, log, or attachment for a public repository, pull request, release, or catalog, especially when source context may be private.
license: MIT
metadata:
  version: "0.1.0"
---

# Safe Publication Review

Review **before** the first public upload, not merely before merge. A public branch or draft PR is already publication. Publish generalized engineering assets without exposing private context or inventing evidence.

## Procedure

1. Define the exact candidate files, commit range, destination/visibility, publication authority, and required reviews. Implementation, publication, merge, and activation are separate permissions. Apply existing approval only to its actual scope.
2. Keep personal circumstances, private correspondence, confidential material, identifiable case histories, and account configuration outside the candidate. Write a generalized method with synthetic examples. Changing names may leave identifying context. Do not send private inputs to public scanners, search queries, issues, or external services merely to sanitize them.
3. Inspect the entire new surface: files, every new commit and reachable new history, messages, author/committer email, branch names, PR text, logs, examples, screenshots, links, filenames, and embedded metadata. Check sensitive identifiers, credentials, personal paths, and contextual disclosure. Use approved public attribution or a verified noreply identity. Noreply addresses do not guarantee anonymity; review names and other identity-bearing metadata too. A clean final diff does not clean earlier commits.
4. Verify provenance and license rights for code, text, examples, data, and media. Preserve required notices and attribution. Unknown or incompatible rights block affected material; public availability is not permission to redistribute.
5. Require focused triggers, portable instructions, valid references, evidence, limitations, and neutral professional language. Exclude personal grievances and judgments about identifiable people. Retain material technical limitations and failed evidence; never invent completed tests, adoption, endorsement, performance, or security guarantees.
6. Freeze the candidate and complete the [publication review record](references/publication-review.md). Obtain the independent review required by the owning project. Label self-review, automated checks, and model-assisted review accurately, including their scope. If a required reviewer is unavailable, retain the candidate privately and report that gate.
7. Resolve blocking findings before publication. Recheck changed content after review. Publish only the reviewed candidate within authorization and read back its files and metadata. Raw private evidence stays private; public summaries must also pass review.

## Verdict

Return **ready for authorized publication**, **needs revision**, or **blocked**, with exact unresolved items. Unknown privacy, provenance, license, or authority is not a pass. Mechanical checks complement contextual review; neither guarantees that all sensitive information has been found.

For a suspected exposure, stop further disclosure and notify its owner privately. Follow the authorized incident process. Deleting a file or closing a PR does not prove that history, clones, or caches are clean. Incident-response changes require their relevant authority.
