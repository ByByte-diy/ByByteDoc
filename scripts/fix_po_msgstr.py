#!/usr/bin/env python3
"""
Fix multi-line msgstr entries in PO files by collapsing them into single lines.
Usage: python3 scripts/fix_po_msgstr.py
"""
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS = PROJECT_ROOT / "docs"


def fix_po_file(po_path: Path) -> bool:
    """Fix multi-line msgstr entries in a PO file."""
    if not po_path.exists():
        return False
    
    content = po_path.read_text(encoding="utf-8")
    original_content = content
    
    # Pattern to match multi-line msgstr entries
    pattern = r'(msgstr ""\n)((?:"[^"]*"\n?)+)'
    
    def replace_msgstr(match):
        msgstr_start = match.group(1)
        multi_line_content = match.group(2)
        
        # Extract all quoted strings and join them
        quoted_strings = re.findall(r'"([^"]*)"', multi_line_content)
        joined_content = ''.join(quoted_strings)
        
        # Escape quotes and create single-line msgstr
        escaped_content = joined_content.replace('\\', '\\\\').replace('"', '\\"')
        return f'msgstr "{escaped_content}"\n'
    
    # Apply the fix
    content = re.sub(pattern, replace_msgstr, content, flags=re.MULTILINE)
    
    # Only write if content changed
    if content != original_content:
        po_path.write_text(content, encoding="utf-8")
        return True
    
    return False


def main():
    """Fix all PO files in the locale directory."""
    fixed_count = 0
    
    # Find all PO files
    for po_file in DOCS.rglob("*.po"):
        if fix_po_file(po_file):
            print(f"Fixed: {po_file.relative_to(DOCS)}")
            fixed_count += 1
    
    print(f"Fixed {fixed_count} PO files")


if __name__ == "__main__":
    main()
