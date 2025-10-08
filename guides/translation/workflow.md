# Translation Workflow Guide
# Посібник з робочого процесу перекладу
# Руководство по рабочему процессу перевода

## Overview / Огляд / Обзор

This guide explains how to translate **ALL content** (not just headers) using the gettext/po system.

Цей посібник пояснює, як перекладати **ВЕСЬ контент** (не тільки заголовки) використовуючи систему gettext/po.

Это руководство объясняет, как переводить **ВЕСЬ контент** (не только заголовки) используя систему gettext/po.

---

## How It Works / Як це працює / Как это работает

### 1. Source Files (English) / Вихідні файли / Исходные файлы

Write documentation in English (`.rst` files):

```rst
Installation
============

This guide will help you install ByByte.

Requirements
------------

* Arduino IDE
* Python 3.x
```

### 2. Extract Messages / Витяг повідомлень / Извлечение сообщений

Run command:

```bash
make gettext
```

This creates `.pot` template files in `docs/_build/gettext/`:

```pot
msgid "Installation"
msgstr ""

msgid "This guide will help you install ByByte."
msgstr ""

msgid "Requirements"
msgstr ""

msgid "Arduino IDE"
msgstr ""

msgid "Python 3.x"
msgstr ""
```

### 3. Update Translation Catalogs / Оновити каталоги / Обновить каталоги

```bash
make update
```

This updates all `.po` files in `docs/locale/{uk,ru}/LC_MESSAGES/`.

**Every paragraph, every sentence becomes a translatable string!**

**Кожен абзац, кожне речення стає рядком для перекладу!**

**Каждый абзац, каждое предложение становится переводимой строкой!**

### 4. Translate ALL Content / Перекласти ВСЕ / Перевести ВСЁ

Edit `.po` files - translate EVERYTHING:

**English original:**
```po
#: ../../installation.rst:1
msgid "Installation"
msgstr ""

#: ../../installation.rst:4
msgid "This guide will help you install ByByte."
msgstr ""
```

**Ukrainian translation:**
```po
#: ../../installation.rst:1
msgid "Installation"
msgstr "Встановлення"

#: ../../installation.rst:4
msgid "This guide will help you install ByByte."
msgstr "Цей посібник допоможе вам встановити ByByte."
```

**Russian translation:**
```po
#: ../../installation.rst:1
msgid "Installation"
msgstr "Установка"

#: ../../installation.rst:4
msgid "This guide will help you install ByByte."
msgstr "Это руководство поможет вам установить ByByte."
```

---

## Best Practices / Найкращі практики / Лучшие практики

### 1. Use Translation Tools / Використовуйте інструменти / Используйте инструменты

**Poedit** (Recommended / Рекомендовано / Рекомендуется):

```bash
# Install on Ubuntu/Debian
sudo apt install poedit

# Open translation file
poedit docs/locale/uk/LC_MESSAGES/installation.po
```

**Benefits of Poedit:**
- ✅ Visual interface / Візуальний інтерфейс / Визуальный интерфейс
- ✅ Shows original and translation side-by-side / Показує оригінал і переклад поруч
- ✅ Translation memory / Пам'ять перекладів / Память переводов
- ✅ Spell check / Перевірка орфографії / Проверка орфографии
- ✅ Auto-save / Автозбереження / Автосохранение

**Alternative tools:**
- **Lokalize** - KDE translation tool
- **GTranslator** - GNOME tool
- **Virtaal** - Cross-platform
- **OmegaT** - Professional CAT tool

### 2. Translate in Context / Перекладайте в контексті / Переводите в контексте

`.po` files show the source file and line number:

```po
#: ../../installation.rst:10
msgid "Install dependencies:"
msgstr "Встановіть залежності:"
```

This helps understand context! / Це допомагає зрозуміти контекст! / Это помогает понять контекст!

### 3. Keep Formatting / Зберігайте форматування / Сохраняйте форматирование

**RST markup must be preserved:**

❌ **WRONG / НЕПРАВИЛЬНО:**
```po
msgid "**bold** and *italic*"
msgstr "жирний і курсив"
```

✅ **CORRECT / ПРАВИЛЬНО:**
```po
msgid "**bold** and *italic*"
msgstr "**жирний** і *курсив*"
```

**Common RST elements to preserve:**

```rst
**bold**          → **жирний**
*italic*          → *курсив*
`code`            → `код`
:ref:`link`       → :ref:`link` (don't translate ref targets!)
.. note::         → .. note:: (keep directives in English)
.. code-block::   → .. code-block::
```

### 4. Don't Translate Code / Не перекладайте код / Не переводите код

❌ **WRONG:**
```po
msgid "pip install sphinx"
msgstr "піп інсталл сфінкс"
```

✅ **CORRECT:**
```po
msgid "pip install sphinx"
msgstr "pip install sphinx"
```

**But DO translate code comments in examples if they're part of the documentation!**

---

## Complete Workflow Example / Повний приклад / Полный пример

### Step 1: Write English Documentation

`docs/quickstart.rst`:
```rst
Quick Start Guide
=================

Get started with ByByte in 5 minutes.

Installation
------------

Install the package:

.. code-block:: bash

   pip install bybyte

First Example
-------------

Here's your first program:

.. code-block:: python

   import bybyte
   device = bybyte.connect('/dev/ttyACM0')
   print(device.status())
```

### Step 2: Extract & Update

```bash
make gettext
make update
```

### Step 3: Translate in Poedit

Open `docs/locale/uk/LC_MESSAGES/quickstart.po`:

```po
# Ukrainian translation
msgid "Quick Start Guide"
msgstr "Посібник швидкого старту"

msgid "Get started with ByByte in 5 minutes."
msgstr "Почніть роботу з ByByte за 5 хвилин."

msgid "Installation"
msgstr "Встановлення"

msgid "Install the package:"
msgstr "Встановіть пакет:"

# Code blocks are NOT translated - they stay as-is!
msgid "pip install bybyte"
msgstr "pip install bybyte"

msgid "First Example"
msgstr "Перший приклад"

msgid "Here's your first program:"
msgstr "Ось ваша перша програма:"

# Python code example - keep as-is!
msgid "import bybyte\ndevice = bybyte.connect('/dev/ttyACM0')\nprint(device.status())"
msgstr "import bybyte\ndevice = bybyte.connect('/dev/ttyACM0')\nprint(device.status())"
```

### Step 4: Build & Test

```bash
# Build Ukrainian version
make html-uk

# View result
xdg-open docs/_build/html/uk/quickstart.html
```

---

## Translation Strategy / Стратегія перекладу / Стратегия перевода

### Priority Order / Порядок пріоритету / Порядок приоритета

1. **High Priority / Високий пріоритет / Высокий приоритет:**
   - `index.po` - Main page / Головна сторінка / Главная страница ✅
   - `installation.po` - Installation guide
   - `quickstart.po` - Quick start

2. **Medium Priority / Середній пріоритет / Средний приоритет:**
   - `usage.po` - Usage guide
   - `api.po` - API reference

3. **Low Priority / Низький пріоритет / Низкий приоритет:**
   - `contributing.po` - Contributing guide
   - `changelog.po` - Changelog

### Batch Translation / Масовий переклад / Массовый перевод

```bash
# Translate one file at a time
poedit docs/locale/uk/LC_MESSAGES/installation.po
make html-uk
# Check result, fix issues
# Move to next file
poedit docs/locale/uk/LC_MESSAGES/quickstart.po
```

---

## Tips for Large Texts / Поради для великих текстів / Советы для больших текстов

### 1. Use Translation Memory

Poedit automatically remembers previous translations.

If you translate "installation" once, it will suggest it everywhere!

### 2. Break Large Paragraphs

**In source .rst files:**

Instead of:
```rst
This is a very long paragraph with lots of text that goes on and on and explains many things in great detail which makes it hard to translate as one big block.
```

Better:
```rst
This is a clear introduction.

This is the first point explained.

This is the second point explained.
```

Sphinx will extract these as separate translatable strings!

### 3. Use Comments in .po Files

```po
# Translation note: "device" refers to Arduino hardware
msgid "Connect the device"
msgstr "Підключіть пристрій"
```

### 4. Consistent Terminology

Create a glossary:

| English | Ukrainian | Russian |
|---------|-----------|---------|
| device | пристрій | устройство |
| connect | підключити | подключить |
| install | встановити | установить |
| build | зібрати | собрать |

---

## Automation & Tools / Автоматизація / Автоматизация

### Pre-translate with Machine Translation

**Use DeepL or Google Translate for first pass:**

```bash
# Example with DeepL API (if you have it)
# This is just an example - not included by default

for po in docs/locale/uk/LC_MESSAGES/*.po; do
    # Extract untranslated strings
    # Translate with API
    # Update .po file
done
```

**Then manually review and fix!**

### Online Translation Platforms

**Weblate** - Free for open source:
- Upload `.po` files
- Translators work in web interface
- Download translated files
- Supports translation memory, suggestions

**Transifex**, **Crowdin** - Similar services

---

## Checking Translation Quality / Перевірка якості / Проверка качества

### 1. Check Syntax

```bash
# Check for errors in .po files
msgfmt -c -v docs/locale/uk/LC_MESSAGES/*.po
```

### 2. Build and Review

```bash
# Build with warnings
make html-uk SPHINXOPTS="-W"

# Visual check
xdg-open docs/_build/html/uk/index.html
```

### 3. Check for Untranslated Strings

```bash
# Find empty translations
grep -B 1 'msgstr ""' docs/locale/uk/LC_MESSAGES/*.po | grep msgid

# Or use our script
./scripts/check-translations.sh
```

### 4. Compare with Original

Open side-by-side:
```bash
# English
xdg-open docs/_build/html/installation.html

# Ukrainian  
xdg-open docs/_build/html/uk/installation.html
```

---

## Maintaining Translations / Підтримка перекладів / Поддержка переводов

### When Source Changes / Коли джерело змінюється / Когда источник изменяется

1. **Update English .rst files**
2. **Extract new messages:**
   ```bash
   make gettext
   ```
3. **Update translations:**
   ```bash
   make update
   ```
4. **Sphinx-intl marks changes:**
   - New strings: empty `msgstr ""`
   - Changed strings: marked as `#, fuzzy`
   - Deleted strings: commented out

5. **Update fuzzy translations:**
   ```po
   #, fuzzy
   msgid "New improved text"
   msgstr "Old translation"  # Update this!
   ```

6. **Rebuild:**
   ```bash
   make html-all
   ```

---

## Summary / Підсумок / Итог

✅ **Write** .rst files in English  
✅ **Extract** with `make gettext`  
✅ **Update** catalogs with `make update`  
✅ **Translate** ALL `msgstr` in .po files (use Poedit!)  
✅ **Build** with `make html-uk` or `make html-all`  
✅ **Review** in browser  
✅ **Repeat** for all files  

**This approach scales to ANY size documentation!**

**Цей підхід масштабується на БУДЬ-ЯКИЙ розмір документації!**

**Этот подход масштабируется на ЛЮБОЙ размер документации!**

---

## Quick Commands Reference

```bash
# Start translation workflow
make gettext              # Extract translatable strings
make update               # Update .po files

# Translate files
poedit docs/locale/uk/LC_MESSAGES/installation.po
poedit docs/locale/uk/LC_MESSAGES/quickstart.po
# ... translate all files ...

# Build and test
make html-uk              # Build Ukrainian version
make html-ru              # Build Russian version
make html-all             # Build all versions

# Check progress
./scripts/check-translations.sh

# Validate
msgfmt -c docs/locale/uk/LC_MESSAGES/*.po
```

---

## Need Help? / Потрібна допомога? / Нужна помощь?

- 📖 [Sphinx i18n Documentation](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- 📖 [Poedit Tutorial](https://poedit.net/trac/wiki/Doc)
- 📖 [GNU gettext Manual](https://www.gnu.org/software/gettext/manual/)

---

**Remember:** One source (English .rst), many translations (.po files)!

**Пам'ятайте:** Одне джерело (англійська .rst), багато перекладів (.po файли)!

**Помните:** Один источник (английский .rst), много переводов (.po файлы)!

