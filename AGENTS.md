# Repository instructions

This repository is the canonical GitHub source for newly authored, reusable **non-personal skills**. Maintain them as open-source assets under the existing license after publication review. Personal workflows and private configuration stay outside this public repository.

## Standing rules

- Before substantial infrastructure work, load [reuse-before-build](skills/reuse-before-build/SKILL.md). Compare at least three credible existing implementations and document evidence, ownership cost, and custom-build exceptions. Use proportionate review for small routine changes.
- Before the first public push, PR, issue, release, or attachment, load [safe-publication-review](skills/safe-publication-review/SKILL.md). A public draft PR is publication; review all new disclosure surfaces, including history and metadata.
- Keep personal context, private correspondence, credentials, confidential material, and identifiable private case histories out of public artifacts. Use synthetic examples while retaining relevant technical limitations.
- Reuse existing evidence, approval, and status skills rather than duplicating them. Skills do not grant permissions or override higher-priority instructions or task-specific approvals.
- Preserve unrelated branches and active evaluations. Merge, global activation, license changes, and security-setting changes require their relevant authorization.

Run `python -m unittest discover -s tests -p 'test_*.py' -v`. Existing CI separately runs the official format validator. Distinguish static checks, text-only probes, independent review, actual client activation, and observed tool behavior.

See [contribution policy](CONTRIBUTING.md), [security handling](SECURITY.md), and [activation instructions](docs/skill-activation.md). These repository instructions do not automatically apply to other projects or chats.
