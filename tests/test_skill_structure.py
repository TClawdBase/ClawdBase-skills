"""Offline checks for the published skill's structure and key safeguards."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "agent-trust-assessment"


class SkillStructureTests(unittest.TestCase):
    def test_frontmatter_and_directory_name(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        parts = text.split("\n---\n", 1)
        self.assertEqual(len(parts), 2)
        fields = dict(re.findall(r"^([a-z-]+):\s*(.+)$", parts[0], re.MULTILINE))
        name = fields["name"]
        self.assertEqual(name, SKILL_DIR.name)
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertTrue(1 <= len(fields["description"]) <= 1024)
        self.assertTrue(parts[1].strip())

    def test_referenced_files_exist(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        references = re.findall(r"\]\((references/[^)]+)\)", text)
        self.assertTrue(references)
        for reference in references:
            with self.subTest(reference=reference):
                self.assertTrue((SKILL_DIR / reference).is_file())

    def test_safety_rules_are_present(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8").lower()
        for term in ("idempotency", "fresh", "snapshot", "credits", "sandbox", "secret"):
            with self.subTest(term=term):
                self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
