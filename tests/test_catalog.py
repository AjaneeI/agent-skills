"""Offline catalog and authoring invariants; NOT a live agent-behavior evaluation."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


class CatalogChecks(unittest.TestCase):
    def test_every_skill_has_authoring_contract_and_safe_files(self):
        names = set()
        folders = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        self.assertGreaterEqual(len(folders), 13)
        for folder in folders:
            entry = folder / "SKILL.md"
            self.assertTrue(entry.is_file(), f"{entry} missing")
            body = entry.read_text(encoding="utf-8")
            self.assertTrue(body.startswith("---\n"), str(entry))
            self.assertIn(f"name: {folder.name}\n", body)
            self.assertRegex(body, r"(?im)^description:\s*\S+")
            self.assertGreater(len(body), 700)
            self.assertNotIn(folder.name, names)
            names.add(folder.name)

            # Enforces human/agent-readable markers, not semantic compliance.
            self.assertRegex(body.lower(), r"(\*\*good\b|^## good\b|\*\*permissible\b)")
            self.assertRegex(body.lower(), r"(\*\*bad\b|^## bad\b|\*\*impermissible\b)")
            self.assertRegex(body.lower(), r"(acceptance|definition of done|pass criteria|success criteria|verification)")
            self.assertRegex(body.lower(), r"(permission|authoriz|approval|must not|prohibit)")
            self.assertRegex(body.lower(), r"(handoff|stop|blocked|escalat)")

            # Relative Markdown file links must resolve; web links are excluded.
            for relative in re.findall(r"\]\(([^)]+)\)", body):
                target = relative.split("#", 1)[0]
                if not target or "://" in target or target.startswith("#") or not target.endswith(".md"):
                    continue
                self.assertTrue((folder / target).resolve().is_file(),
                                f"{entry}: broken link {relative}")
            for path in folder.rglob("*"):
                if path.is_file():
                    self.assertEqual(path.suffix, ".md", f"Unexpected non-Markdown skill file: {path}")

    def test_catalog_documentation_and_test_fixture(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        verification = (ROOT / "docs" / "verification-status.md").read_text(encoding="utf-8")
        self.assertIn("all 13 skills", readme.lower())
        self.assertIn("13 skill directories", verification.lower())
        self.assertIn("NOT RUN", verification)
        self.assertTrue((ROOT / "docs" / "agent-evaluation-contract.md").is_file())
        cases = json.loads((ROOT / "tests" / "fixtures" / "plugin-first-cases.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 9)

    def test_scenarios_are_not_claimed_as_executed(self):
        scenarios = (ROOT / "tests" / "scenarios.md").read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^\d+\. \*\*", scenarios, re.M)), 10)
        self.assertIn("not executed test results", scenarios)
        plugin_cases = (ROOT / "tests" / "new-skill-smoke-cases.md").read_text(encoding="utf-8")
        self.assertIn("unexecuted specifications", plugin_cases)


if __name__ == "__main__":
    unittest.main()
