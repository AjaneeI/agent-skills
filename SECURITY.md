# Security and sensitive-information handling

These skills are instructions, not a sandbox, access-control system, or security certification. Review them before installation and enforce runtime permissions separately.

Use [safe-publication-review](skills/safe-publication-review/SKILL.md) before any public disclosure. Branches, draft PRs, issues, attachments, metadata and build logs can all expose information. Review the new history, not only the final tree.

## Reporting

Do not paste credentials, personal information, confidential evidence or exploit details into public issues. Use GitHub private vulnerability reporting only if it is actually enabled. Otherwise arrange an authorized private channel with the maintainer without posting the sensitive payload. This document does not assert that private reporting is configured or promise a response time.

## Suspected exposure

Stop further publication and notify the authorized owner privately. Preserve restricted evidence. For credentials, coordinate owner-authorized revocation or rotation rather than relying on deletion alone. Removing a file or closing a PR does not establish removal from history, clones, or caches. Changes to shared history, credentials or security settings require appropriate authority.

Reference: [GitHub sensitive-data guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
