#!/usr/bin/env python3

import argparse
import os
import sys
import time
import yaml
from pathlib import Path

import polib
from google import genai
from google.genai import types
from pydantic import BaseModel, Field


# ============================================================================
# Sphinx Documentation Translation Script via Gemini API
# ============================================================================
# 
# This script translates Sphinx gettext PO files to multiple target languages
# using the Gemini API. Each language has its own rule file (rule_ua.md, rule_ru.md, etc.)
# that defines translation guidelines and system prompts.
#
# Usage:
#   python translate_po.py path/to/file.po                  # Translate to Ukrainian (default)
#   python translate_po.py path/to/file.po --language uk    # Explicit Ukrainian
#   python translate_po.py path/to/file.po --language ru    # Russian translation
#   python translate_po.py path/to/file.po --language uk --dry-run --batch-size 10
#
# To add a new language:
#   1. Create a new file: rule_xx.md (where xx is language code)
#   2. Use YAML frontmatter for metadata: name, target_language
#   3. Add translation system prompt after frontmatter
#   4. No script modification needed!
#
# Rule file format (rule_ua.md):
#   ---
#   name: Ukrainian
#   target_language: Ukrainian
#   ---
#   
#   You are a professional technical translator...
#
# Environment:
#   Set GEMINI_API_KEY environment variable before running
# ============================================================================


def get_rules_dir() -> Path:
    """Get the directory containing rule files."""
    return Path(__file__).parent


def parse_rule_file(rule_path: Path) -> dict:
    """
    Parse a rule markdown file with YAML frontmatter.
    
    Returns a dict with:
        - name: Language name
        - target_language: Target language for prompts
        - system_prompt: Full system prompt from file content
    """
    content = rule_path.read_text(encoding="utf-8")
    
    # Split frontmatter and content
    if not content.startswith("---"):
        raise ValueError(f"Rule file must start with YAML frontmatter: {rule_path}")
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"Invalid rule file format: {rule_path}")
    
    frontmatter_text = parts[1]
    prompt_text = parts[2].strip()
    
    # Parse YAML frontmatter
    try:
        metadata = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in {rule_path}: {e}")
    
    if not isinstance(metadata, dict):
        raise ValueError(f"Rule file frontmatter must be a YAML object: {rule_path}")
    
    required_fields = {"name", "target_language"}
    missing_fields = required_fields - set(metadata.keys())
    if missing_fields:
        raise ValueError(
            f"Rule file missing required fields: {missing_fields} in {rule_path}"
        )
    
    return {
        "name": metadata["name"],
        "target_language": metadata["target_language"],
        "system_prompt": prompt_text,
    }


def load_available_rules() -> dict:
    """
    Load all available translation rules from rule_*.md files.
    
    Returns dict: {language_code: {name, target_language, system_prompt}}
    """
    rules_dir = get_rules_dir()
    rules = {}
    
    for rule_file in sorted(rules_dir.glob("rule_*.md")):
        language_code = rule_file.stem.replace("rule_", "")
        
        try:
            rule = parse_rule_file(rule_file)
            rules[language_code] = rule
        except Exception as e:
            print(f"Warning: Failed to load {rule_file}: {e}", file=sys.stderr)
    
    if not rules:
        print(
            "No translation rules found. Create rule_*.md files in the scripts directory.",
            file=sys.stderr,
        )
        sys.exit(1)
    
    return rules


class Translation(BaseModel):
    id: int = Field(description="The unchanged numeric ID of the source item")
    translation: str = Field(description="Target language translation")


class TranslationBatch(BaseModel):
    translations: list[Translation]


def parse_args():
    # Load available rules to populate choices
    available_rules = load_available_rules()
    available_languages = sorted(available_rules.keys())
    
    parser = argparse.ArgumentParser(
        description="Translate a Sphinx gettext PO file using Gemini."
    )

    parser.add_argument(
        "file",
        type=Path,
        help="Path to the .po file",
    )

    parser.add_argument(
        "--language",
        default="uk",
        choices=available_languages,
        help=f"Target language (default: uk). Available: {', '.join(available_languages)}",
    )

    parser.add_argument(
        "--model",
        default="gemini-3.1-flash-lite",
        help="Gemini model name",
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=30,
        help="Number of PO entries per API request",
    )

    parser.add_argument(
        "--fuzzy",
        action="store_true",
        help="Also review and translate fuzzy entries",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not modify the PO file",
    )

    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum API retries per batch",
    )

    return parser.parse_args()


def get_entries(po: polib.POFile, include_fuzzy: bool):
    entries = []

    for entry in po:
        if entry.obsolete:
            continue

        is_fuzzy = "fuzzy" in entry.flags

        if not entry.msgstr:
            entries.append(entry)
        elif include_fuzzy and is_fuzzy:
            entries.append(entry)

    return entries


def build_batch(entries):
    items = []

    for index, entry in enumerate(entries):
        item = {
            "id": index,
            "source": entry.msgid,
        }

        if entry.msgctxt:
            item["context"] = entry.msgctxt

        if entry.msgstr:
            item["existing_translation"] = entry.msgstr

        if entry.occurrences:
            item["source_references"] = [
                f"{file}:{line}"
                for file, line in entry.occurrences
            ]

        items.append(item)

    return items


def translate_batch(
    client,
    model: str,
    entries,
    max_retries: int,
    system_prompt: str,
    target_language: str,
):
    batch = build_batch(entries)

    prompt = f"""
Translate the following entries into {target_language}.

The `id` field is an immutable identifier. Return the same IDs.

Input entries:

{batch}
"""

    for attempt in range(1, max_retries + 1):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0.1,
                    response_mime_type="application/json",
                    response_schema=TranslationBatch,
                ),
            )

            result = response.parsed

            if result is None:
                raise RuntimeError(
                    f"Gemini returned no parsed response: {response.text}"
                )

            translations = {
                item.id: item.translation
                for item in result.translations
            }

            expected_ids = set(range(len(entries)))
            received_ids = set(translations.keys())

            if expected_ids != received_ids:
                raise RuntimeError(
                    "Response IDs do not match input IDs. "
                    f"Expected: {expected_ids}, received: {received_ids}"
                )

            return translations

        except Exception as error:
            print(
                f"API error, attempt {attempt}/{max_retries}: {error}",
                file=sys.stderr,
            )

            if attempt == max_retries:
                raise

            time.sleep(2 ** attempt)


def main():
    args = parse_args()

    if not args.file.exists():
        print(f"File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # Load all available rules and validate language
    available_rules = load_available_rules()
    
    if args.language not in available_rules:
        print(
            f"Unknown language: {args.language}\n"
            f"Available: {', '.join(sorted(available_rules.keys()))}",
            file=sys.stderr,
        )
        sys.exit(1)

    rule = available_rules[args.language]

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print(
            "GEMINI_API_KEY environment variable is not set.",
            file=sys.stderr,
        )
        sys.exit(1)

    po = polib.pofile(str(args.file))

    entries = get_entries(
        po,
        include_fuzzy=args.fuzzy,
    )

    if not entries:
        print("Nothing to translate.")
        return

    print(f"File: {args.file}")
    print(f"Language: {rule['name']} ({args.language})")
    print(f"Model: {args.model}")
    print(f"Entries: {len(entries)}")
    print(f"Batch size: {args.batch_size}")

    if args.dry_run:
        print("\nDry run — entries that would be translated:\n")

        for entry in entries:
            print(f"- {entry.msgid[:120]}")

        return

    client = genai.Client(api_key=api_key)

    translated_count = 0

    for start in range(0, len(entries), args.batch_size):
        batch_entries = entries[start:start + args.batch_size]

        batch_number = start // args.batch_size + 1
        total_batches = (
            len(entries) + args.batch_size - 1
        ) // args.batch_size

        print(
            f"\nTranslating batch "
            f"{batch_number}/{total_batches} "
            f"({len(batch_entries)} entries)..."
        )

        translations = translate_batch(
            client=client,
            model=args.model,
            entries=batch_entries,
            max_retries=args.max_retries,
            system_prompt=rule["system_prompt"],
            target_language=rule["target_language"],
        )

        for index, entry in enumerate(batch_entries):
            entry.msgstr = translations[index]

            if "fuzzy" in entry.flags:
                entry.flags.remove("fuzzy")

            translated_count += 1

        # Save after every successful batch.
        # If a later API request fails, completed work is preserved.
        po.save(str(args.file))

        print(
            f"Saved. Total translated: "
            f"{translated_count}/{len(entries)}"
        )

    print("\nTranslation completed.")
    print(f"Translated entries: {translated_count}")
    print(f"Saved to: {args.file}")


if __name__ == "__main__":
    main()