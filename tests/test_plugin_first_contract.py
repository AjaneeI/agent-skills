"""Static contract checks for Plugin-First Execution.

These tests validate documentation structure only, not agent behavior.
Real routing compliance needs observed tool traces and pressure scenarios.
"""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "skills" / "plugin-first-execution" / "SKILL.md"
POLICY_PATH = ROOT / "docs" / "work-plugin-routing-policy.md"
SCENARIO_PATH = ROOT / "tests" / "plugin-first-routing-scenarios.md"


class PluginFirstContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL_PATH.read_text(encoding="utf-8")
        cls.policy = POLICY_PATH.read_text(encoding="utf-8")
        cls.scenarios = SCENARIO_PATH.read_text(encoding="utf-8")

    def test_skill_frontmatter_matches_directory(self):
        self.assertTrue(self.skill.startswith("---\n"))
        self.assertIn("\nname: plugin-first-execution\n", self.skill)
        self.assertIn("\ndescription:", self.skill)
        self.assertIn('version: "1.1.0"', self.skill)

    def test_related_markdown_paths_resolve(self):
        for ref in re.findall(r"\]\(([^)]+\.md)\)", self.skill):
            if "://" in ref:
                continue
            target = (SKILL_PATH.parent / ref).resolve()
            self.assertTrue(target.is_file(), f"Missing linked reference: {ref}")

    def test_human_and_agent_readable_sections(self):
        sections = (
            "## Purpose and trigger",
            "## Before using tools",
            "## Tool routing",
            "## Required workflow",
            "## Permission boundary",
            "## Browser and computer fallback",
            "## Good output",
            "## Bad output",
            "## Handoff and failure response",
            "## Acceptance checklist",
            "## Evaluation",
        )
        for section in sections:
            with self.subTest(section=section):
                self.assertIn(section, self.skill)

    def test_risk_tiers_and_approval_boundaries(self):
        for tier in ("**Low**", "**Medium**", "**High**"):
            self.assertIn(tier, self.skill)
        for phrase in (
            "explicit authorization",
            "read-only",
            "Gmail connector",
            "This is an instruction policy",
            "Existing pilot exception",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_policy_does_not_override_stricter_pilot(self):
        self.assertIn("Networking & Application Follow-up", self.policy)
        self.assertIn("stricter", self.policy)
        self.assertIn("risk", self.policy.lower())

    def test_positive_and_negative_scenarios_documented(self):
        ids = re.findall(r"\bPFR-(\d{2})\b", self.scenarios)
        unique = set(ids)
        self.assertGreaterEqual(len(unique), 12)
        self.assertIn("PFR-01", self.scenarios)
        self.assertIn("PFR-02", self.scenarios)
        self.assertIn("PFR-11", self.scenarios)
        self.assertIn("PFR-14", self.scenarios)
        self.assertIn("No agent runs", self.scenarios)
        self.assertIn("Not measured", self.scenarios)

    def test_no_placeholder_success_claims(self):
        self.assertNotIn("all benchmark scenarios passed", self.scenarios.lower())
        self.assertIn("not proof", self.scenarios.lower())


if __name__ == "__main__":
    unittest.main()
