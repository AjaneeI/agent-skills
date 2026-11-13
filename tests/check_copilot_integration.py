"""Static Copilot bridge validation; not a live agent test."""

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
        assert bridge.is_file(), f"Missing Copilot bridge: {name}"
        assert canonical.is_file(), f"Missing canonical skill: {name}"
        text = bridge.read_text()
        assert re.search(r"(?m)^name:\s*" + re.escape(name) + r"\s*$", text)
        assert re.search(r"(?m)^description:\s*\S+", text)
        target = (bridge.parent / "../../../../skills" / name / "SKILL.md").resolve()
        assert target == canonical.resolve() and target.is_file(), f"Broken bridge: {name}"
    print(f"PASS: Copilot instructions and {len(PILOT)} canonical skill bridges (static only)")


if __name__ == "__main__":
    validate()
