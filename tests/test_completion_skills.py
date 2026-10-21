"""Static document contract checks; these do not evaluate live agent compliance."""
from pathlib import Path
import re
import unittest
ROOT = Path(__file__).resolve().parents[1]
NAMES = ("evidence-based-verification", "research-gate-management")

class CompletionSkillChecks(unittest.TestCase):
    def required(self, relative):
        path = ROOT / relative
        self.assertTrue(path.is_file(), f"Missing required artifact: {relative}")
        return path.read_text(encoding="utf-8")

    def test_manifests_and_instruction_only_references(self):
        for name in NAMES:
            with self.subTest(name=name):
                text = self.required(f"skills/{name}/SKILL.md")
                self.assertTrue(text.startswith("---\n"))
                front = text.split("---", 2)[1]
                self.assertIn(f"name: {name}\n", front)
                self.assertRegex(front, r"(?m)^description: Use when .+")
                self.assertIn("license: MIT", front)
                self.assertNotIn("allowed-tools:", front)
                self.assertLess(len(text.splitlines()), 150)
                refs = list((ROOT/"skills"/name/"references").glob("*.md"))
                self.assertTrue(refs)
                for file in (ROOT/"skills"/name).rglob("*"):
                    if file.is_file(): self.assertEqual(file.suffix, ".md")

    def test_verification_record_separates_claims_and_outcomes(self):
        text = self.required("skills/evidence-based-verification/references/claim-record.md")
        for heading in ("Claim", "Bindings", "Evidence", "Outcome dimensions", "Verdict", "Next action"):
            self.assertIn(heading, text)
        body = self.required("skills/evidence-based-verification/SKILL.md").lower()
        for term in ("unverified", "denied", "needs_approval", "failed", "verified", "authenticity", "self-report", "independent", "timeout", "supersed"):
            self.assertIn(term, body)

    def test_research_record_has_versioned_dependencies_and_stop_rules(self):
        text = self.required("skills/research-gate-management/references/gate-record.md")
        for heading in ("Gate", "Dependencies", "Version binding", "Evidence", "Decision", "Invalidation", "Permitted next action"):
            self.assertIn(heading, text)
        body = self.required("skills/research-gate-management/SKILL.md").lower()
        for term in ("existing", "prerequisite", "blocked", "supersed", "budget", "independent", "unknown", "one-shot-experiment-control"):
            self.assertIn(term, body)

    def test_routing_map_covers_catalog_without_duplicate_entries(self):
        text = self.required("docs/skill-routing.md")
        links = re.findall(r"\]\(../skills/([^/]+)/SKILL.md\)", text)
        actual = {p.parent.name for p in (ROOT/"skills").glob("*/SKILL.md")}
        self.assertEqual(set(links), actual)
        self.assertEqual(len(links), len(set(links)))
        for name in NAMES:
            self.assertIn(name, self.required("README.md"))
            self.assertIn(name, self.required("AGENTS.md"))
            self.assertIn(name, self.required("docs/skill-activation.md"))

    def test_scenarios_have_observable_expected_and_prohibited_actions(self):
        text = self.required("tests/completion-scenarios.md")
        for key in ("EV1", "EV2", "EV3", "RG1", "RG2", "RG3"):
            self.assertIn(key, text)
        self.assertGreaterEqual(text.count("Expected:"), 6)
        self.assertGreaterEqual(text.count("Prohibited:"), 6)
        self.assertIn("not executed runtime results", text)

    def test_new_links_resolve_without_leaving_repository(self):
        paths = [ROOT/"docs/skill-routing.md", ROOT/"tests/completion-scenarios.md"]
        for name in NAMES:
            folder = ROOT/"skills"/name
            self.assertTrue(folder.is_dir(), str(folder))
            paths.extend(folder.rglob("*.md"))
        for path in paths:
            self.assertTrue(path.is_file(), str(path))
            for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if re.match(r"[a-z]+://|mailto:|#", link): continue
                target = (path.parent/link.split("#", 1)[0]).resolve()
                self.assertTrue(target.is_relative_to(ROOT.resolve()), str(target))
                self.assertTrue(target.is_file(), f"{path}: {link}")

if __name__ == "__main__":
    unittest.main()
