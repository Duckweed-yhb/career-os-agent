import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []


def _read_text(path):
    """Read a UTF-8 text file defensively; on failure record an error and return ''."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        errors.append(f"[read] {path.name}: {exc}")
        return ""


def check_skill_frontmatter():
    """SKILL.md must start with valid front matter (name + description)."""
    for skill in ["SKILL.md", "SKILL.en.md"]:
        path = ROOT / skill
        if not path.exists():
            errors.append(f"[frontmatter] missing file: {skill}")
            continue
        text = _read_text(path)
        if not text.startswith("---\n"):
            errors.append(f"[frontmatter] {skill} must start with `---` YAML front matter")
            continue
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not m:
            errors.append(f"[frontmatter] {skill} has unclosed front matter block")
            continue
        for field in ("name:", "description:"):
            if field not in m.group(1):
                errors.append(f"[frontmatter] {skill} missing `{field}`")


def check_relative_links():
    """Every relative link in README*/FAQ* must point to an existing file."""
    for md in [
        ROOT / "README.md",
        ROOT / "README.en.md",
        ROOT / "FAQ.md",
        ROOT / "FAQ.en.md",
    ]:
        if not md.exists():
            continue
        text = _read_text(md)
        for target in re.findall(r"\]\(([^)#]+?)(?:#[^)]*)?\)", text):
            if target.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            if target.startswith("assets/"):
                continue  # binary assets; presence not enforced here
            if (ROOT / target).exists():
                continue
            errors.append(f"[link] {md.name}: broken relative link -> {target}")


def check_changelog():
    path = ROOT / "CHANGELOG.md"
    if not path.exists():
        errors.append("[changelog] CHANGELOG.md missing")
        return
    text = _read_text(path)
    if not any(m in text for m in ("## [Unreleased]", "## [未发布]")):
        errors.append("[changelog] CHANGELOG.md must contain an [Unreleased] / [未发布] section")


def check_version_consistency():
    """SKILL front-matter version, README badge, and latest CHANGELOG version must match."""
    skill_text = _read_text(ROOT / "SKILL.md")
    m = re.search(r"^version:\s*([\d.]+)", skill_text, re.MULTILINE)
    if not m:
        errors.append("[version] SKILL.md missing `version:` in front matter")
        return
    skill_version = m.group(1)

    readme_text = _read_text(ROOT / "README.md")
    m = re.search(r"badge/version-([\d.]+)-blue", readme_text)
    if not m:
        errors.append("[version] README.md missing shields.io version badge")
        return
    badge_version = m.group(1)

    changelog_text = _read_text(ROOT / "CHANGELOG.md")
    m = re.search(r"^## \[([\d.]+)\]", changelog_text, re.MULTILINE)
    if not m:
        errors.append("[version] CHANGELOG.md missing a released version section")
        return
    changelog_version = m.group(1)

    versions = {
        "SKILL": skill_version,
        "README badge": badge_version,
        "CHANGELOG": changelog_version,
    }
    if len(set(versions.values())) != 1:
        errors.append(f"[version] version mismatch: {versions}")


def check_examples_commands():
    """Every /CareerOS command used under examples/ must exist in the Command Reference."""
    known = set()
    skill_text = _read_text(ROOT / "SKILL.md")
    for row in re.findall(r"\| `/CareerOS ([^`]+)` \|", skill_text):
        known.add(row.split()[0])
    if not known:
        errors.append("[examples] no /CareerOS commands found in SKILL.md Command Reference")
        return
    examples_dir = ROOT / "examples"
    if not examples_dir.exists():
        return
    for md in sorted(examples_dir.rglob("*.md")):
        text = _read_text(md)
        for cmd in re.findall(r"/CareerOS ([a-z]+)", text):
            if cmd not in known:
                errors.append(f"[examples] {md.relative_to(ROOT)}: unknown command /CareerOS {cmd}")


def check_doc_pairs():
    """Main docs are Chinese; each must ship an English twin (`*.en.md`)."""
    pairs = [
        ("SKILL.md", "SKILL.en.md"),
        ("README.md", "README.en.md"),
        ("FAQ.md", "FAQ.en.md"),
        ("CONTRIBUTING.md", "CONTRIBUTING.en.md"),
        ("CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT.en.md"),
        ("CHANGELOG.md", "CHANGELOG.en.md"),
        ("docs/agent/DESIGN.md", "docs/agent/DESIGN.en.md"),
        ("references/methodology.md", "references/methodology.en.md"),
    ]
    for main, en in pairs:
        if not (ROOT / main).exists():
            errors.append(f"[docs] missing Chinese main doc: {main}")
        if not (ROOT / en).exists():
            errors.append(f"[docs] missing English doc: {en}")


def main():
    check_skill_frontmatter()
    check_relative_links()
    check_changelog()
    check_doc_pairs()
    check_version_consistency()
    check_examples_commands()
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: verified {ROOT} — front matter, links, changelog, version consistency all valid.")


if __name__ == "__main__":
    main()
