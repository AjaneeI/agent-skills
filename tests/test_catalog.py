"""Offline catalog invariants. This is not an agent-behavior evaluation."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

class CatalogChecks(unittest.TestCase):
    def test_every_skill_is_instruction_only_and_has_references(self):
        names = set()
        entries = list(sorted(SKILLS.iterdir()))
        self.assertTrue(entries)
        for folder in entries:
            if not folder.is_dir():
                continue
            entry = folder / "SKILL.md"
            self.assertTrue(entry.is_file(), f"{entry} missing")
            body = entry.read_text(encoding="utf-8")
            self.assertTrue(body.startswith("---\n"), str(entry))
            self.assertIn(f"name: {folder.name}\n", body)
            self.assertGreater(len(body), 700)
            self.assertNotIn(folder.name, names)
            names.add(folder.name)
            for relative in re.findall(r"\]\((references/[^)]+)\)", body):
                self.assertTrue((folder / relative).is_file(), f"{entry}: {relative}")
            for path in folder.rglob("*"):
                if path.is_file():
                    self.assertEqual(path.suffix, ".md", f"Unexpected executable or binary: {path}")

    def test_scenarios_are_not_claimed_as_executed(self):
        scenarios = (ROOT / "tests" / "scenarios.md").read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^\d+\. \*\*", scenarios, re.M)), 10)
        self.assertIn("not executed test results", scenarios)

if __name__ == "__main__":
    unittest.main()
