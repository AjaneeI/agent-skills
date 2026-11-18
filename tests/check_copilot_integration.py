"""Static checks for GitHub Copilot skill discovery layout and canonical links.

This checks files, not that a running Copilot agent discovered or obeyed skills.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PILOT = (
    "plugin-first-execution",
    "approval-boundary-management",
    "constraints-first-execution",
)


def validate():
    instructions = ROOT / ".github" / "copilot-instructions.md"
    assert instructions.is_file(), "Missing Copilot repository instructions"
    assert "never merge without explicit approval" in instructions.read_text().lower()

    for name in PILOT:
        bridge = ROOT / ".github" / "skills" / name / "SKILL.md"
        canonical = ROOT / "skills" / name / "SKILL.md"
        assert bridge.is_file(), f"Missing Copilot skill: {name}"
        assert canonical.is_file(), f"Missing canonical skill: {name}"
        body = bridge.read_text(encoding="utf-8")
        assert body.startswith("---\n"), f"Missing frontmatter: {name}"
        assert re.search(r"(?m)^name:\s*" + re.escape(name) + r"\s*$", body)
        assert re.search(r"(?m)^description:\s*\S+", body)
        assert "canonical" in body.lower(), f"Missing canonical reference: {name}"
        assert "acceptance" in body.lower(), f"Missing acceptance condition: {name}"

        links = re.findall(r"\]\(([^)]+)\)", body)
        assert links, f"No Markdown links: {name}"
        for link in links:
            target = link.split("#", 1)[0]
            if not target or "://" in target:
                continue
            resolved = (bridge.parent / target).resolve()
            assert resolved.is_file(), f"Broken link in {name}: {link}"
            assert resolved.is_relative_to(ROOT.resolve()), f"Link escapes repository: {link}"
        assert canonical.resolve() == (bridge.parent / "../../../skills" / name / "SKILL.md").resolve()

    print(f"PASS: Copilot repository instructions and {len(PILOT)} pilot skills validated (static only)")


if __name__ == "__main__":
    validate()
