#!/usr/bin/env python3
"""
Automatic translation for .po files using various translation services.

Supports:
- Google Translate (via deep-translator)
- LibreTranslate (free, self-hosted)
- Argos Translate (offline)
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional

# Try importing translation libraries
TRANSLATORS = {}

try:
    from deep_translator import GoogleTranslator
    TRANSLATORS['google'] = True
except ImportError:
    TRANSLATORS['google'] = False

try:
    import argostranslate.package
    import argostranslate.translate
    TRANSLATORS['argos'] = True
except ImportError:
    TRANSLATORS['argos'] = False

try:
    from deep_translator import LibreTranslator
    TRANSLATORS['libre'] = True
except ImportError:
    TRANSLATORS['libre'] = False


class PoTranslator:
    """Translates .po files automatically."""
    
    def __init__(self, source_lang='en', target_lang='uk', service='google', libre_url=None):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.service = service
        self.libre_url = libre_url or 'https://libretranslate.de'
        
        # Initialize translator
        self.translator = self._init_translator()
    
    def _init_translator(self):
        """Initialize the translation service."""
        if self.service == 'google':
            if not TRANSLATORS['google']:
                raise ImportError("deep-translator not installed. Run: pip install deep-translator")
            
            # Map language codes
            lang_map = {'uk': 'uk', 'ru': 'ru', 'en': 'en'}
            target = lang_map.get(self.target_lang, self.target_lang)
            
            return GoogleTranslator(source='en', target=target)
        
        elif self.service == 'libre':
            if not TRANSLATORS['libre']:
                raise ImportError("deep-translator not installed. Run: pip install deep-translator")
            
            return LibreTranslator(
                source='en',
                target=self.target_lang,
                base_url=self.libre_url
            )
        
        elif self.service == 'argos':
            if not TRANSLATORS['argos']:
                raise ImportError("argostranslate not installed. Run: pip install argostranslate")
            
            # Download packages if needed
            argostranslate.package.update_package_index()
            available_packages = argostranslate.package.get_available_packages()
            
            package_to_install = next(
                (pkg for pkg in available_packages 
                 if pkg.from_code == 'en' and pkg.to_code == self.target_lang),
                None
            )
            
            if package_to_install:
                argostranslate.package.install_from_path(package_to_install.download())
            
            return None  # Argos uses different API
        
        else:
            raise ValueError(f"Unknown service: {self.service}")
    
    def translate_text(self, text: str) -> str:
        """Translate a single text string."""
        if not text or text.strip() == '':
            return text
        
        # Skip if text contains only code or special characters
        if self._is_code_only(text):
            return text
        
        try:
            if self.service == 'argos':
                return argostranslate.translate.translate(text, 'en', self.target_lang)
            else:
                return self.translator.translate(text)
        except Exception as e:
            print(f"  ⚠ Translation error: {e}", file=sys.stderr)
            return text
    
    def _is_code_only(self, text: str) -> bool:
        """Check if text is code/markup only."""
        # Don't translate if mostly code
        code_patterns = [
            r'^[`\[\]{}()<>]+$',  # Only brackets/backticks
            r'^\$\w+',  # Environment variables
            r'^https?://',  # URLs
            r'^\w+\(\)',  # Function calls
        ]
        
        for pattern in code_patterns:
            if re.match(pattern, text.strip()):
                return True
        
        return False
    
    def _preserve_formatting(self, text: str, translation: str) -> str:
        """Preserve RST formatting in translation."""
        # Preserve bold/italic markers
        if text.startswith('**') and text.endswith('**'):
            if not (translation.startswith('**') and translation.endswith('**')):
                translation = f"**{translation.strip('* ')}**"
        
        if text.startswith('*') and text.endswith('*') and not text.startswith('**'):
            if not (translation.startswith('*') and translation.endswith('*')):
                translation = f"*{translation.strip('* ')}*"
        
        # Preserve code markers
        if '``' in text:
            # Try to preserve inline code
            parts = re.split(r'(``[^`]+``)', text)
            trans_parts = re.split(r'(``[^`]+``)', translation)
            # This is complex, just return translation for now
        
        return translation
    
    def translate_po_file(self, po_file: Path, output_file: Optional[Path] = None, 
                          skip_translated: bool = True, dry_run: bool = False):
        """Translate a .po file."""
        if not po_file.exists():
            raise FileNotFoundError(f"File not found: {po_file}")
        
        print(f"📖 Reading: {po_file}")
        
        with open(po_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        translated_lines = []
        
        i = 0
        msgid = None
        msgstr = None
        msgid_lines = []
        in_msgid = False
        in_msgstr = False
        translated_count = 0
        skipped_count = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Detect msgid
            if line.startswith('msgid '):
                in_msgid = True
                in_msgstr = False
                msgid_lines = [line[7:].strip('"')]
                translated_lines.append(line)
            
            # Detect msgstr
            elif line.startswith('msgstr '):
                in_msgid = False
                in_msgstr = True
                msgstr = line[8:].strip('"')
                
                # Join multi-line msgid
                msgid = ' '.join(msgid_lines).strip()
                
                # Translate if msgstr is empty and msgid is not empty
                if msgstr == '' and msgid != '':
                    print(f"  🔄 Translating: {msgid[:50]}...")
                    translation = self.translate_text(msgid)
                    translation = self._preserve_formatting(msgid, translation)
                    
                    if not dry_run:
                        translated_lines.append(f'msgstr "{translation}"')
                        translated_count += 1
                    else:
                        translated_lines.append(line)
                        print(f"     → {translation[:50]}...")
                elif msgstr != '' and skip_translated:
                    translated_lines.append(line)
                    skipped_count += 1
                elif msgstr != '' and not skip_translated:
                    # Retranslate existing
                    print(f"  🔄 Re-translating: {msgid[:50]}...")
                    translation = self.translate_text(msgid)
                    translation = self._preserve_formatting(msgid, translation)
                    
                    if not dry_run:
                        translated_lines.append(f'msgstr "{translation}"')
                        translated_count += 1
                    else:
                        translated_lines.append(line)
                        print(f"     → {translation[:50]}...")
                else:
                    translated_lines.append(line)
                
                msgid_lines = []
            
            # Continue multi-line msgid
            elif in_msgid and line.startswith('"'):
                msgid_lines.append(line.strip('"'))
                translated_lines.append(line)
            
            # Regular line
            else:
                translated_lines.append(line)
                in_msgid = False
                in_msgstr = False
            
            i += 1
        
        if not dry_run:
            output = output_file or po_file
            with open(output, 'w', encoding='utf-8') as f:
                f.write('\n'.join(translated_lines))
            
            print(f"✅ Saved: {output}")
        
        print(f"📊 Translated: {translated_count}, Skipped: {skipped_count}")
        
        return translated_count


def main():
    parser = argparse.ArgumentParser(description='Automatically translate .po files')
    parser.add_argument('input', help='Input .po file or directory')
    parser.add_argument('-l', '--lang', default='uk', help='Target language (uk, ru)')
    parser.add_argument('-s', '--service', default='google', 
                       choices=['google', 'libre', 'argos'],
                       help='Translation service to use')
    parser.add_argument('-o', '--output', help='Output file (default: overwrite input)')
    parser.add_argument('--libre-url', help='LibreTranslate server URL')
    parser.add_argument('--no-skip', action='store_true', 
                       help='Translate even if msgstr is not empty')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show translations without saving')
    
    args = parser.parse_args()
    
    # Check if service is available
    if args.service not in TRANSLATORS or not TRANSLATORS[args.service]:
        print(f"❌ Service '{args.service}' not available.", file=sys.stderr)
        print(f"\nInstall required package:", file=sys.stderr)
        if args.service == 'google' or args.service == 'libre':
            print(f"  pip install deep-translator", file=sys.stderr)
        elif args.service == 'argos':
            print(f"  pip install argostranslate", file=sys.stderr)
        sys.exit(1)
    
    # Initialize translator
    translator = PoTranslator(
        source_lang='en',
        target_lang=args.lang,
        service=args.service,
        libre_url=args.libre_url
    )
    
    # Process file(s)
    input_path = Path(args.input)
    
    if input_path.is_file():
        # Single file
        output_path = Path(args.output) if args.output else None
        translator.translate_po_file(
            input_path,
            output_path,
            skip_translated=not args.no_skip,
            dry_run=args.dry_run
        )
    
    elif input_path.is_dir():
        # Directory - process all .po files
        po_files = list(input_path.glob('**/*.po'))
        print(f"📁 Found {len(po_files)} .po files")
        
        for po_file in po_files:
            print(f"\n{'='*60}")
            try:
                translator.translate_po_file(
                    po_file,
                    skip_translated=not args.no_skip,
                    dry_run=args.dry_run
                )
            except Exception as e:
                print(f"❌ Error: {e}", file=sys.stderr)
    
    else:
        print(f"❌ Path not found: {input_path}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

