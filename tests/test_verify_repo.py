"""Unit tests for .github/scripts/verify_repo.py.

Each test builds a fake repository under a temp dir, points the module's ROOT
at it, runs the relevant checks, and asserts on the collected errors.
"""

import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / ".github" / "scripts"))

import verify_repo  # noqa: E402

SKILL_TMPL = """---
name: {name}
description: "test skill"
version: {version}
---

# Test
"""

README_TMPL = """# Test

[![Version](https://img.shields.io/badge/version-{version}-blue.svg)](CHANGELOG.md)

[ok](docs/guide.md)
"""

CHANGELOG_TMPL = """# Changelog

## [Unreleased]

## [{version}] - 2026-01-01
"""

CMD_REF_TMPL = """
| `/CareerOS {cmd}` | trigger | — | out |
"""


class VerifyRepoTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._old_root = verify_repo.ROOT
        verify_repo.ROOT = self.root

    def tearDown(self):
        verify_repo.ROOT = self._old_root
        verify_repo.errors.clear()
        self._tmp.cleanup()

    def _run_all(self):
        verify_repo.errors.clear()
        verify_repo.check_skill_frontmatter()
        verify_repo.check_relative_links()
        verify_repo.check_changelog()
        verify_repo.check_doc_pairs()
        verify_repo.check_version_consistency()
        verify_repo.check_examples_commands()
        return list(verify_repo.errors)

    def _write(self, rel: str, content: str) -> Path:
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return p

    def _build_healthy_repo(self):
        self._write("SKILL.md", SKILL_TMPL.format(name="career-os", version="0.1.0"))
        self._write("SKILL.en.md", SKILL_TMPL.format(name="career-os-en", version="0.1.0"))
        self._write("README.md", README_TMPL.format(version="0.1.0"))
        self._write("README.en.md", README_TMPL.format(version="0.1.0"))
        self._write("FAQ.md", "# FAQ\n")
        self._write("FAQ.en.md", "# FAQ\n")
        self._write("CONTRIBUTING.md", "# 贡献指南\n")
        self._write("CONTRIBUTING.en.md", "# Contributing\n")
        self._write("CODE_OF_CONDUCT.md", "# 行为准则\n")
        self._write("CODE_OF_CONDUCT.en.md", "# Code of Conduct\n")
        self._write("CHANGELOG.md", CHANGELOG_TMPL.format(version="0.1.0"))
        self._write("CHANGELOG.en.md", CHANGELOG_TMPL.format(version="0.1.0"))
        self._write("docs/guide.md", "guide")
        self._write("docs/agent/DESIGN.md", "# 设计方案\n")
        self._write("docs/agent/DESIGN.en.md", "# Design\n")
        self._write("references/methodology.md", "# 方法论\n")
        self._write("references/methodology.en.md", "# Methodology\n")
        self._write("docs/ROADMAP.md", "# 路线\n")
        self._write("docs/ROADMAP.en.md", "# Roadmap\n")
        self._write("examples/demo.md", "用户: /CareerOS init")
        self._write("SKILL.md", SKILL_TMPL.format(name="career-os", version="0.1.0") + CMD_REF_TMPL.format(cmd="init"))

    def test_healthy_repo_passes(self):
        self._build_healthy_repo()
        self.assertEqual(self._run_all(), [])

    def test_missing_skill_frontmatter_fails(self):
        self._build_healthy_repo()
        self._write("SKILL.md", "no front matter here")
        errs = self._run_all()
        self.assertTrue(any("[frontmatter]" in e for e in errs))

    def test_broken_relative_link_fails(self):
        self._build_healthy_repo()
        self._write("README.md", README_TMPL.format(version="0.1.0") + "\n[broken](missing.md)")
        errs = self._run_all()
        self.assertTrue(any("[link]" in e for e in errs))

    def test_missing_unreleased_section_fails(self):
        self._build_healthy_repo()
        self._write("CHANGELOG.md", "## [0.1.0] - 2026-01-01\n")
        errs = self._run_all()
        self.assertTrue(any("[changelog]" in e for e in errs))

    def test_version_mismatch_fails(self):
        self._build_healthy_repo()
        self._write("README.md", README_TMPL.format(version="9.9.9"))
        errs = self._run_all()
        self.assertTrue(any("[version]" in e for e in errs))

    def test_unknown_example_command_fails(self):
        self._build_healthy_repo()
        self._write("examples/demo.md", "用户: /CareerOS notacommand")
        errs = self._run_all()
        self.assertTrue(any("[examples]" in e for e in errs))

    def test_missing_english_twin_fails(self):
        self._build_healthy_repo()
        (self.root / "FAQ.en.md").unlink()
        errs = self._run_all()
        self.assertTrue(any("[docs]" in e for e in errs))

    def test_bad_encoding_does_not_crash(self):
        self._build_healthy_repo()
        (self.root / "README.md").write_bytes(b"\xff\xfe\x00bad")
        errs = self._run_all()
        self.assertTrue(any("[read]" in e for e in errs))


if __name__ == "__main__":
    unittest.main()
