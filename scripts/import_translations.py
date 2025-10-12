#!/usr/bin/env python3
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS = PROJECT_ROOT / "docs"


def read_text_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def filter_content_lines(lines: list[str]) -> list[str]:
    content = []
    for line in lines:
        s = line.rstrip()
        if not s:
            continue
        # Skip rst directives and roles
        if s.startswith(".. "):
            continue
        if s.lstrip().startswith(":"):
            continue
        content.append(s)
    return content


def _escape_po(s: str) -> str:
    return s.replace('\\', r'\\').replace('"', r'\"')


def _normalize(s: str) -> str:
    s = s.strip()
    if s.startswith('* '):
        s = s[2:]
    if s.startswith('- '):
        s = s[2:]
    return s


def load_po(path: Path) -> list[tuple[str, list[str]]]:
    entries: list[tuple[str, list[str]]] = []
    current_msgid_lines: list[str] = []
    current_msgstr_lines: list[str] = []
    state = None
    lines = read_text_lines(path)
    for line in lines:
        if line.startswith("msgid "):
            if current_msgid_lines or current_msgstr_lines:
                entries.append(("\n".join(current_msgid_lines), current_msgstr_lines))
                current_msgid_lines, current_msgstr_lines = [], []
            state = "id"
            current_msgid_lines = [line[7:-1]] if line.endswith('"') else []
        elif line.startswith("msgstr "):
            state = "str"
            current_msgstr_lines = [line[8:-1]] if line.endswith('"') else []
        elif line.startswith('"') and line.endswith('"') and state == "id":
            current_msgid_lines.append(line[1:-1])
        elif line.startswith('"') and line.endswith('"') and state == "str":
            current_msgstr_lines.append(line[1:-1])
        elif line.strip().startswith("#: "):
            continue
        else:
            if current_msgid_lines or current_msgstr_lines:
                entries.append(("\n".join(current_msgid_lines), current_msgstr_lines))
                current_msgid_lines, current_msgstr_lines = [], []
            state = None
    if current_msgid_lines or current_msgstr_lines:
        entries.append(("\n".join(current_msgid_lines), current_msgstr_lines))
    return entries


def write_po(original_lines: list[str], path: Path, new_entries: dict[str, str]) -> None:
    out: list[str] = []
    state = None
    current_msgid: list[str] = []
    skip_continuation = False
    for line in original_lines:
        if skip_continuation:
            if line.startswith('"') and line.endswith('"'):
                continue
            else:
                skip_continuation = False
        if line.startswith("msgid "):
            state = "id"
            current_msgid = [line[7:-1]] if line.endswith('"') else []
            out.append(line)
        elif state == "id" and line.startswith('"') and line.endswith('"'):
            current_msgid.append(line[1:-1])
            out.append(line)
        elif line.startswith("msgstr "):
            msgid_text = "\n".join(current_msgid)
            replacement = new_entries.get(msgid_text)
            if replacement:
                # Handle multi-line msgstr properly
                if '\n' in replacement:
                    out.append('msgstr ""')
                    for repl_line in replacement.split('\n'):
                        out.append(f'"{_escape_po(repl_line)}"')
                else:
                    out.append(f'msgstr "{_escape_po(replacement)}"')
                state = None
                skip_continuation = True
            else:
                out.append(line)
                state = "str"
        else:
            out.append(line)
            if not line.startswith('"'):
                state = None
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def build_mapping(en_rst: Path, loc_rst: Path) -> dict[str, str]:
    """Build mapping between English and localized content, handling multi-line text."""
    en_content = en_rst.read_text(encoding="utf-8")
    loc_content = loc_rst.read_text(encoding="utf-8")
    
    mapping: dict[str, str] = {}
    
    # Split into lines and map by position
    en_lines = [line.strip() for line in en_content.splitlines() if line.strip()]
    loc_lines = [line.strip() for line in loc_content.splitlines() if line.strip()]
    
    # Map lines by position
    for i, en_line in enumerate(en_lines):
        if i < len(loc_lines):
            en_norm = _normalize(en_line)
            loc_norm = _normalize(loc_lines[i])
            if en_norm and loc_norm and len(en_norm) > 10:
                mapping[en_norm] = loc_norm
    
    # Also try line-by-line mapping for single lines
    en_lines = filter_content_lines(read_text_lines(en_rst))
    loc_lines = filter_content_lines(read_text_lines(loc_rst))
    for i, en_line in enumerate(en_lines):
        if i < len(loc_lines):
            en_norm = _normalize(en_line)
            loc_norm = _normalize(loc_lines[i])
            if en_norm and loc_norm and len(en_norm) > 10:
                mapping[en_norm] = loc_norm
    
    return mapping


def _split_into_sections(content: str) -> dict[str, str]:
    """Split content into sections by headers."""
    sections = {}
    current_section = ""
    current_header = ""
    
    for line in content.splitlines():
        line = line.rstrip()
        if line.startswith("**") and line.endswith("**"):
            # Save previous section
            if current_header and current_section:
                sections[current_header] = current_section
            # Start new section
            current_header = line
            current_section = ""
        else:
            current_section += line + "\n"
    
    # Save last section
    if current_header and current_section:
        sections[current_header] = current_section
    
    return sections


def _split_paragraphs(section: str) -> list[str]:
    """Split section into paragraphs."""
    paragraphs = []
    current_para = []
    
    for line in section.splitlines():
        line = line.rstrip()
        if not line:
            if current_para:
                paragraphs.append('\n'.join(current_para))
                current_para = []
        else:
            current_para.append(line)
    
    if current_para:
        paragraphs.append('\n'.join(current_para))
    
    return paragraphs


def _split_into_blocks(content: str) -> list[str]:
    """Split content into meaningful blocks (paragraphs, sections, etc.)."""
    blocks = []
    current_block = []
    
    for line in content.splitlines():
        line = line.rstrip()
        if not line:
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
        else:
            # Skip rst directives
            if line.startswith(".. ") or line.lstrip().startswith(":"):
                continue
            current_block.append(line)
    
    if current_block:
        blocks.append('\n'.join(current_block))
    
    return blocks


def compute_paths(source_rel: str, locale: str) -> tuple[Path, Path, Path]:
    """Given docs-relative rst (e.g. platforms/nano/index.rst),
    return (en_rst, localized_rst, po_path)."""
    en_rst = DOCS / source_rel
    if not source_rel.endswith('.rst'):
        raise ValueError('Source must be an .rst path relative to docs/')
    stem_rel = source_rel[:-4]  # drop .rst
    loc_rst = DOCS / f"{stem_rel}.{locale}.rst"
    po_path = DOCS / f"locale/{locale}/LC_MESSAGES/{stem_rel}.po"
    return en_rst, loc_rst, po_path


def import_for(locale: str, sources: list[str]):
    for src in sources:
        en_rst, loc_rst, po_path = compute_paths(src, locale)
        if not en_rst.exists() or not loc_rst.exists() or not po_path.exists():
            continue
        mapping = build_mapping(en_rst, loc_rst)
        po_lines = read_text_lines(po_path)
        entries = load_po(po_path)
        new_entries: dict[str, str] = {}
        for msgid, msgstr_lines in entries:
            if msgid and (not msgstr_lines or "".join(msgstr_lines).strip() == ""):
                # Try exact match first
                msgid_norm = _normalize(msgid)
                trans = mapping.get(msgid_norm)
                
                # If no exact match, try first line
                if not trans:
                    first_line = _normalize(msgid.split("\n")[0])
                    trans = mapping.get(first_line)
                
                # If still no match, try partial matching
                if not trans:
                    for en_text, loc_text in mapping.items():
                        # Normalize both strings for comparison
                        msgid_clean = msgid_norm.replace('\n', ' ').replace('  ', ' ').strip()
                        en_text_clean = en_text.replace('\n', ' ').replace('  ', ' ').strip()
                        
                        # Check if the msgid is contained in the mapping key or vice versa
                        if (msgid_clean in en_text_clean or en_text_clean in msgid_clean) and len(msgid_clean) > 20:
                            trans = loc_text
                            break
                
                if trans:
                    new_entries[msgid] = trans
        write_po(po_lines, po_path, new_entries)


def main():
    # Usage: import_translations.py <docs-rel-rst> [<docs-rel-rst> ...]
    # Example: import_translations.py platforms/nano/index.rst platforms/nano/spec.rst
    sources = sys.argv[1:]
    if not sources:
        print("Usage: import_translations.py <docs-rel-rst> [more ...]", file=sys.stderr)
        return 1
    locales = ["uk", "ru"]
    for loc in locales:
        import_for(loc, sources)
    print("Imported translations for:", ", ".join(sources), "→", ", ".join(locales))
    return 0


if __name__ == "__main__":
    sys.exit(main())


