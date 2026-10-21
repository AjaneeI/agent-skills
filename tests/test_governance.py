"""Static governance checks, not runtime agent behavior or a privacy guarantee."""
from pathlib import Path
import re
import unittest
ROOT = Path(__file__).resolve().parents[1]
NAMES = ("reuse-before-build", "safe-publication-review")

class GovernanceChecks(unittest.TestCase):
    def read_required(self, relative):
        path = ROOT / relative
        self.assertTrue(path.is_file(), f"Missing required artifact: {relative}")
        return path.read_text(encoding="utf-8")

    def test_new_skills_have_bounded_trigger_and_mit_metadata(self):
        for name in NAMES:
            with self.subTest(name=name):
                text = self.read_required(f"skills/{name}/SKILL.md")
                front = text.split("---", 2)[1]
                self.assertRegex(front, rf"(?m)^name: {name}$")
                self.assertRegex(front, r"(?m)^description: Use when .+")
                self.assertIn("license: MIT", front)
                self.assertIn('version: "0.1.0"', front)
                self.assertLess(len(text.splitlines()), 150)
                self.assertNotIn("allowed-tools:", front)

    def test_reuse_decision_requires_evidence_not_popularity(self):
        text = self.read_required("skills/reuse-before-build/SKILL.md")
        for term in ("at least three", "maintenance", "security", "licens", "integration", "compatibility", "ownership", "exception", "unknown", "small"):
            self.assertIn(term, text.lower())
        record = self.read_required("skills/reuse-before-build/references/technology-evaluation.md")
        for heading in ("Requirements", "Candidates", "Decision", "Custom-build exception", "Verification"):
            self.assertIn(heading, record)

    def test_publication_covers_history_metadata_and_truth(self):
        text = self.read_required("skills/safe-publication-review/SKILL.md").lower()
        for term in ("before", "public", "draft", "history", "metadata", "private", "license", "independent", "unknown", "limitations"):
            self.assertIn(term, text)
        review = self.read_required("skills/safe-publication-review/references/publication-review.md")
        for heading in ("Candidate", "Privacy", "Provenance", "Quality", "Verdict"):
            self.assertIn(heading, review)

    def test_standing_policy_and_activation_are_linked(self):
        policy = self.read_required("AGENTS.md")
        contrib = self.read_required("CONTRIBUTING.md")
        activation = self.read_required("docs/skill-activation.md")
        for name in NAMES:
            self.assertIn(name, policy)
            self.assertIn(name, self.read_required("README.md"))
            self.assertIn(name, activation)
        self.assertIn("non-personal", contrib)
        self.assertIn("not automatically", activation)
        self.read_required("SECURITY.md")
        self.read_required(".github/pull_request_template.md")

    def test_governance_scenarios_have_expected_and_prohibited_actions(self):
        text = self.read_required("tests/governance-scenarios.md")
        for identifier in ("R1", "R2", "R3", "P1", "P2", "P3"):
            self.assertIn(identifier, text)
        self.assertIn("not executed runtime results", text)
        self.assertGreaterEqual(text.count("Expected:"), 6)
        self.assertGreaterEqual(text.count("Prohibited:"), 6)

    def test_new_relative_markdown_links_resolve_within_repository(self):
        docs = [ROOT/"AGENTS.md", ROOT/"CONTRIBUTING.md", ROOT/"SECURITY.md", ROOT/"docs/skill-activation.md", ROOT/".github/pull_request_template.md"]
        for name in NAMES:
            folder = ROOT/"skills"/name
            self.assertTrue(folder.is_dir(), str(folder))
            docs.extend(folder.rglob("*.md"))
        for path in docs:
            self.assertTrue(path.is_file(), str(path))
            for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if re.match(r"[a-z]+://|mailto:|#", link): continue
                target = (path.parent/link.split("#",1)[0]).resolve()
                self.assertTrue(target.is_relative_to(ROOT.resolve()), str(target))
                self.assertTrue(target.exists(), f"{path}: {link}")

if __name__ == "__main__":
    unittest.main()
