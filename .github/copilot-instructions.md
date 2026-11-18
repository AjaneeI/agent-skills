# Copilot repository instructions

This repository is the canonical, agent-agnostic source for the Agent Skills library. Follow [the human-and-agent-readable standard](../docs/human-agent-readable-standard.md) when editing any instruction, skill, prompt, or Markdown policy.

- Read only the skill(s) relevant to the current request from `skills/<name>/SKILL.md`; do not indiscriminately load the whole catalog.
- Before consequential changes, establish the requested outcome, source of truth, authority, stop conditions, and observable acceptance criteria. Do not treat an instruction file as a permission grant.
- Prefer dedicated connectors/tools. Low-risk, already-authorized, non-sensitive read-only browser/computer fallback is permissible when needed; sensitive account access or consequential actions require explicit scoped approval. Never route around explicit denials. See [routing policy](../docs/work-plugin-routing-policy.md).
- Preserve source provenance, uncertainty, and evidence. Never call a simulated trace a live agent result or an instruction an enforced runtime guard.
- For repository changes, use a reviewable pull request, report tests actually executed, and never merge without explicit approval.
- Maintain existing automation pilots and external account permissions unchanged unless separately approved.
- For a task matching an available Copilot bridge skill in `.github/skills/`, read its canonical linked skill and apply it; the bridge is an index, not a replacement.
