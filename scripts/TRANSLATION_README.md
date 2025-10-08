# Automatic Translation for .po Files

## Overview

This script automatically translates `.po` files using various translation services.

## Supported Services

1. **Google Translate** (via deep-translator) - Free, fast, good quality
2. **LibreTranslate** - Free, open-source, self-hostable
3. **Argos Translate** - Offline, completely free

## Installation

### Option 1: Google Translate (Recommended)

```bash
pip install deep-translator
```

### Option 2: LibreTranslate

```bash
pip install deep-translator
```

Use free public server or self-host.

### Option 3: Argos Translate (Offline)

```bash
pip install argostranslate
```

Downloads language models on first use.

## Usage

### Basic Usage

Translate a single file:

```bash
python3 scripts/auto-translate.py docs/locale/uk/LC_MESSAGES/contributing.po
```

Translate all files in a directory:

```bash
python3 scripts/auto-translate.py docs/locale/uk/LC_MESSAGES/
```

### Options

**Choose language:**
```bash
# Ukrainian (default)
python3 scripts/auto-translate.py -l uk file.po

# Russian
python3 scripts/auto-translate.py -l ru file.po
```

**Choose translation service:**
```bash
# Google Translate (default, fastest)
python3 scripts/auto-translate.py -s google file.po

# LibreTranslate (open-source)
python3 scripts/auto-translate.py -s libre file.po

# Argos Translate (offline)
python3 scripts/auto-translate.py -s argos file.po
```

**Custom LibreTranslate server:**
```bash
python3 scripts/auto-translate.py -s libre --libre-url http://localhost:5000 file.po
```

**Dry run (preview without saving):**
```bash
python3 scripts/auto-translate.py --dry-run file.po
```

**Retranslate everything (including existing translations):**
```bash
python3 scripts/auto-translate.py --no-skip file.po
```

## Complete Workflow

### 1. Extract translatable strings

```bash
make gettext
```

### 2. Update translation catalogs

```bash
make update
```

### 3. Install translation tool

```bash
pip install deep-translator
```

### 4. Auto-translate

**Translate all Ukrainian files:**
```bash
python3 scripts/auto-translate.py -l uk docs/locale/uk/LC_MESSAGES/
```

**Translate all Russian files:**
```bash
python3 scripts/auto-translate.py -l ru docs/locale/ru/LC_MESSAGES/
```

**Translate specific file:**
```bash
python3 scripts/auto-translate.py docs/locale/uk/LC_MESSAGES/contributing.po
```

### 5. Review and edit translations

Open files in Poedit or text editor to review and improve translations:

```bash
poedit docs/locale/uk/LC_MESSAGES/contributing.po
```

### 6. Compile translations

```bash
make translate
```

### 7. Build translated docs

```bash
# Ukrainian
make html-uk

# Russian
make html-ru

# All languages
make html-all
```

## Translation Quality

### Automatic translations are good for:
- ✅ Simple sentences
- ✅ Technical documentation
- ✅ Consistent terminology
- ✅ Speed (bulk translation)

### Manual review needed for:
- ⚠️ Complex sentences
- ⚠️ Context-dependent terms
- ⚠️ Cultural references
- ⚠️ Marketing copy

### Best Practice:
1. Use automatic translation for initial translation
2. Review and edit important pages manually
3. Ask native speakers to review
4. Update translations as needed

## Features

### Smart Translation
- Skips already translated strings (by default)
- Preserves formatting (`**bold**`, `*italic*`, ````code````)
- Skips code blocks and URLs
- Handles multi-line strings

### Safety
- Creates backup before overwriting
- Dry-run mode to preview
- UTF-8 encoding support

## Examples

### Translate contributing.po

```bash
# Preview first
python3 scripts/auto-translate.py --dry-run docs/locale/uk/LC_MESSAGES/contributing.po

# Translate
python3 scripts/auto-translate.py docs/locale/uk/LC_MESSAGES/contributing.po

# Review
poedit docs/locale/uk/LC_MESSAGES/contributing.po
```

### Batch translate all files

```bash
# Translate all Ukrainian files
for lang in uk ru; do
    echo "Translating to $lang..."
    python3 scripts/auto-translate.py -l $lang docs/locale/$lang/LC_MESSAGES/
done
```

### Translate only new strings

```bash
# Only translate empty msgstr entries
python3 scripts/auto-translate.py docs/locale/uk/LC_MESSAGES/contributing.po
```

## Troubleshooting

### ImportError: deep-translator not installed

```bash
pip install deep-translator
```

### Rate limiting / blocked

Google Translate may rate limit. Solutions:
- Use LibreTranslate instead: `-s libre`
- Use Argos Translate (offline): `-s argos`
- Add delays between translations

### LibreTranslate server errors

Use public instance or self-host:
```bash
# Use different public server
python3 scripts/auto-translate.py -s libre --libre-url https://translate.argosopentech.com
```

### Argos Translate - Models not found

First run downloads models:
```bash
python3 scripts/auto-translate.py -s argos docs/locale/uk/LC_MESSAGES/contributing.po
# Wait for model download...
```

## Advanced Usage

### Integrate with Makefile

Add to `Makefile`:

```makefile
auto-translate-uk:
	python3 scripts/auto-translate.py -l uk docs/locale/uk/LC_MESSAGES/

auto-translate-ru:
	python3 scripts/auto-translate.py -l ru docs/locale/ru/LC_MESSAGES/

auto-translate-all: auto-translate-uk auto-translate-ru
	@echo "All translations completed"
```

Then run:
```bash
make auto-translate-all
```

### Customize for your project

Edit `auto-translate.py` to:
- Add custom terminology
- Skip specific strings
- Use custom API keys
- Implement caching

## Comparison of Services

| Service | Speed | Quality | Cost | Offline | Setup |
|---------|-------|---------|------|---------|-------|
| Google | ⚡⚡⚡ | ⭐⭐⭐⭐ | Free* | No | Easy |
| LibreTranslate | ⚡⚡ | ⭐⭐⭐ | Free | Optional | Medium |
| Argos | ⚡ | ⭐⭐ | Free | Yes | Easy |

*Free tier may have rate limits

## Recommended Workflow

For **quick initial translation**:
```bash
pip install deep-translator
python3 scripts/auto-translate.py -l uk docs/locale/uk/LC_MESSAGES/
```

For **best quality**:
```bash
# 1. Auto-translate
python3 scripts/auto-translate.py -l uk docs/locale/uk/LC_MESSAGES/

# 2. Manual review in Poedit
poedit docs/locale/uk/LC_MESSAGES/contributing.po

# 3. Build and test
make html-uk
xdg-open docs/_build/html/uk/index.html
```

For **offline/privacy**:
```bash
pip install argostranslate
python3 scripts/auto-translate.py -s argos -l uk docs/locale/uk/LC_MESSAGES/
```

## Support

For issues or questions:
- Open GitHub Issue with tag `translation`
- Contact `@vergilium`

---

**Happy translating! 🌍**

