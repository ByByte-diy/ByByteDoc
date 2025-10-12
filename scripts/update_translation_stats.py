#!/usr/bin/env python3
"""
Update translation statistics in README.md based on actual PO file completion.
Usage: python3 scripts/update_translation_stats.py
"""
import re
from pathlib import Path
from typing import Dict, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS = PROJECT_ROOT / "docs"
README_PATH = PROJECT_ROOT / "guides/translation/README.md"


def count_po_stats(po_path: Path) -> Tuple[int, int]:
    """Count translated and untranslated entries in a PO file."""
    if not po_path.exists():
        return 0, 0
    
    content = po_path.read_text(encoding="utf-8")
    translated = 0
    untranslated = 0
    
    # Count msgstr entries
    lines = content.split('\n')
    in_msgstr = False
    current_msgstr = ""
    
    for line in lines:
        if line.startswith("msgstr "):
            in_msgstr = True
            current_msgstr = line[7:]  # Remove "msgstr "
        elif line.startswith('"') and in_msgstr:
            current_msgstr += line[1:-1]  # Remove quotes
        elif line.startswith("msgid ") or line.startswith("#"):
            if in_msgstr:
                # Process the complete msgstr
                msgstr_content = current_msgstr.strip()
                if msgstr_content and msgstr_content != '""':
                    translated += 1
                else:
                    untranslated += 1
                in_msgstr = False
                current_msgstr = ""
        else:
            if in_msgstr:
                current_msgstr += line
    
    # Handle last entry
    if in_msgstr:
        msgstr_content = current_msgstr.strip()
        if msgstr_content and msgstr_content != '""':
            translated += 1
        else:
            untranslated += 1
    
    return translated, untranslated


def get_language_stats(locale: str) -> Dict[str, Tuple[int, int]]:
    """Get translation stats for a language."""
    stats = {}
    locale_dir = DOCS / f"locale/{locale}/LC_MESSAGES"
    
    if not locale_dir.exists():
        return stats
    
    # Find all PO files
    for po_file in locale_dir.rglob("*.po"):
        relative_path = po_file.relative_to(locale_dir)
        key = str(relative_path).replace("/", "_").replace(".po", "")
        
        translated, untranslated = count_po_stats(po_file)
        stats[key] = (translated, untranslated)
    
    return stats


def calculate_percentage(translated: int, untranslated: int) -> int:
    """Calculate completion percentage."""
    total = translated + untranslated
    if total == 0:
        return 0
    return int((translated / total) * 100)


def update_readme_stats():
    """Update translation statistics in README.md."""
    if not README_PATH.exists():
        print(f"README not found: {README_PATH}")
        return
    
    content = README_PATH.read_text(encoding="utf-8")
    
    # Get stats for both languages
    uk_stats = get_language_stats("uk")
    ru_stats = get_language_stats("ru")
    
    # Calculate overall percentages
    uk_total_translated = sum(t for t, u in uk_stats.values())
    uk_total_untranslated = sum(u for t, u in uk_stats.values())
    uk_percentage = calculate_percentage(uk_total_translated, uk_total_untranslated)
    
    ru_total_translated = sum(t for t, u in ru_stats.values())
    ru_total_untranslated = sum(u for t, u in ru_stats.values())
    ru_percentage = calculate_percentage(ru_total_translated, ru_total_untranslated)
    
    # Update the status table
    status_pattern = r'(\|\s*🇺🇦\s+Ukrainian\s+\|\s*`uk`\s+\|\s*🔄\s+)\d+%(\s+\|\s*-\s+\|)'
    new_uk_status = f'| 🇺🇦 Ukrainian | `uk` | 🔄 {uk_percentage}% | - |'
    content = re.sub(status_pattern, lambda m: m.group(1) + f'{uk_percentage}%' + m.group(2), content)
    
    status_pattern = r'(\|\s*🇷🇺\s+Russian\s+\|\s*`ru`\s+\|\s*🔄\s+)\d+%(\s+\|\s*-\s+\|)'
    new_ru_status = f'| 🇷🇺 Russian | `ru` | 🔄 {ru_percentage}% | - |'
    content = re.sub(status_pattern, lambda m: m.group(1) + f'{ru_percentage}%' + m.group(2), content)
    
    # Update progress section if it exists
    progress_pattern = r'(\*\*📈 Progress:\s+)\d+%'
    content = re.sub(progress_pattern, f'\\g<1>{uk_percentage}%', content)
    
    # Write back
    README_PATH.write_text(content, encoding="utf-8")
    
    print(f"Updated translation stats:")
    print(f"  Ukrainian: {uk_percentage}% ({uk_total_translated} translated, {uk_total_untranslated} untranslated)")
    print(f"  Russian: {ru_percentage}% ({ru_total_translated} translated, {ru_total_untranslated} untranslated)")


if __name__ == "__main__":
    update_readme_stats()
