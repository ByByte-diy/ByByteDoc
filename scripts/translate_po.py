#!/usr/bin/env python3

import argparse
import os
import sys
import time
from pathlib import Path

import polib
from google import genai
from google.genai import types
from pydantic import BaseModel, Field


SYSTEM_PROMPT = """
You are a professional technical translator for the ByByte-DIY robotics
education project.

Translate English Sphinx documentation into natural, technically accurate
Ukrainian.

Rules:
- Preserve the complete meaning.
- Use natural Ukrainian suitable for educational technical documentation.
- Preserve all Sphinx/reStructuredText markup.
- Preserve placeholders exactly.
- Preserve URLs, reference targets, code, commands, file paths, API names,
  function names, variable names, hardware model numbers, and product names.
- Do not translate: ByByte-DIY, ByByte Nano, ByByte Mega, ByByte NanoBoy,
  Arduino, ESP32, ESP32-CAM, GitHub, Discord, YouTube.
- Do not add explanations or information absent from the source.
- Return exactly one translation for every input item.
"""


class Translation(BaseModel):
    id: int = Field(description="The unchanged numeric ID of the source item")
    translation: str = Field(description="Ukrainian translation")


class TranslationBatch(BaseModel):
    translations: list[Translation]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Translate a Sphinx gettext PO file using Gemini."
    )

    parser.add_argument(
        "file",
        type=Path,
        help="Path to the .po file",
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
):
    batch = build_batch(entries)

    prompt = f"""
Translate the following entries into Ukrainian.

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
                    system_instruction=SYSTEM_PROMPT,
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