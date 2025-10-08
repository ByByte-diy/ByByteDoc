# ByByte Documentation

[![Documentation Status](https://readthedocs.org/projects/bybyte/badge/?version=latest)](https://bybyte.readthedocs.io/en/latest/?badge=latest)

This repository contains the complete documentation for the ByByte project, an Arduino-based system.

## 📖 Documentation

The documentation is automatically built and published on **ReadTheDocs**:

🔗 **[Read the Docs](https://bybyte.readthedocs.io/)**

## 🌍 Multilingual Support

The documentation is available in **3 languages**:

- **🇬🇧 English** (en) - Default
- **🇺🇦 Ukrainian** (uk) - Українська
- **🇷🇺 Russian** (ru) - Русский

### Building Multilingual Documentation

```bash
# Build all languages at once
make html-all

# Build specific language
make html       # English
make html-uk    # Ukrainian  
make html-ru    # Russian
```

### Working with Translations

```bash
# Extract translatable strings
make gettext

# Update translation catalogs
make update

# Edit translations in: docs/locale/{uk,ru}/LC_MESSAGES/*.po
```

📖 **See [LOCALIZATION.md](LOCALIZATION.md) for detailed translation guide**

## 🚀 Building Documentation Locally

### Prerequisites

- Python 3.x
- pip

### Installation & Build

1. **Install dependencies:**
   ```bash
   pip install -r docs/requirements.txt
   ```

2. **Build HTML documentation:**
   ```bash
   make html       # English only
   make html-all   # All languages
   ```

3. **View documentation:**
   ```bash
   # English
   xdg-open docs/_build/html/index.html
   
   # Ukrainian
   xdg-open docs/_build/html/uk/index.html
   
   # Russian
   xdg-open docs/_build/html/ru/index.html
   ```

### Available Make Commands

Run these commands from the project root directory:

| Command | Description |
|---------|-------------|
| `make html` | Build English HTML documentation |
| `make html-uk` | Build Ukrainian HTML documentation |
| `make html-ru` | Build Russian HTML documentation |
| `make html-all` | Build documentation for all languages |
| `make clean` | Remove all build artifacts |
| `make gettext` | Extract translatable strings |
| `make update` | Update translation catalogs (.po files) |
| `make latexpdf` | Build PDF documentation (requires LaTeX) |
| `make epub` | Build EPUB documentation |
| `make help` | Show all available commands |

## 📂 Documentation Structure

```
ByByteDoc/
├── .readthedocs.yaml    # ReadTheDocs configuration
├── .gitignore           # Git ignore patterns
├── .github/
│   └── workflows/
│       └── docs.yml     # GitHub Actions CI
├── Makefile             # Root makefile for building docs
├── README.md            # This file
├── LOCALIZATION.md      # Translation guide
└── docs/
    ├── conf.py          # Sphinx configuration
    ├── index.rst        # Main documentation page
    ├── installation.rst # Installation guide
    ├── quickstart.rst   # Quick start guide
    ├── usage.rst        # Usage guide
    ├── api.rst          # API reference
    ├── changelog.rst    # Version changelog
    ├── contributing.rst # Contributing guidelines
    ├── requirements.txt # Python dependencies
    ├── Makefile         # Sphinx makefile
    ├── _static/         # Static files (images, CSS, etc.)
    ├── locale/          # Translations
    │   ├── uk/          # Ukrainian translations
    │   │   └── LC_MESSAGES/
    │   │       ├── index.po
    │   │       ├── installation.po
    │   │       └── ...
    │   └── ru/          # Russian translations
    │       └── LC_MESSAGES/
    │           ├── index.po
    │           └── ...
    └── _build/          # Build output (generated)
        └── html/
            ├── index.html    # English docs
            ├── uk/           # Ukrainian docs
            └── ru/           # Russian docs
```

## ✏️ Contributing to Documentation

We welcome contributions! See **[Contributing Guide](guides/CONTRIBUTING.md)** for detailed instructions.

Ми вітаємо внески! Дивіться **[Посібник контриб'ютора](guides/CONTRIBUTING.md)** для детальних інструкцій.

### ⚠️ Important / Важливо

**Before contributing, please discuss your plans with maintainers!** Open a [GitHub Discussion](https://github.com/vergilium/ByByteDoc/discussions) or [Issue](https://github.com/vergilium/ByByteDoc/issues) first.

**Перед внеском, будь ласка, обговоріть ваші плани з мейнтейнерами!** Відкрийте [GitHub Discussion](https://github.com/vergilium/ByByteDoc/discussions) або [Issue](https://github.com/vergilium/ByByteDoc/issues) спочатку.

This ensures your efforts are valuable and aligned with project goals.

Це гарантує, що ваші зусилля будуть цінними та відповідають цілям проекту.

---

### Quick Start / Швидкий старт

1. **Fork this repository / Зробіть форк репозиторію**
2. **Clone your fork / Клонуйте ваш форк:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ByByteDoc.git
   cd ByByteDoc
   ```

3. **Create a new branch / Створіть нову гілку:**
   ```bash
   git checkout -b improve-docs
   ```

4. **Edit documentation files / Редагуйте файли документації** in the `docs/` directory
   - Documentation is written in reStructuredText (`.rst`)
   - See [Sphinx documentation](https://www.sphinx-doc.org/) for syntax

5. **Build and test locally / Зберіть та протестуйте локально:**
   ```bash
   make clean && make html
   xdg-open docs/_build/html/index.html
   ```

6. **Commit and push / Закомітьте та запуште:**
   ```bash
   git add .
   git commit -m "Improve documentation"
   git push origin improve-docs
   ```

7. **Create a Pull Request on GitHub / Створіть Pull Request на GitHub**

### 📚 Developer Documentation / Документація розробників

**New contributors / Новим контриб'юторам:**
- 📖 [Developer Guide](guides/README.md) - Complete developer documentation / Повна документація розробників
- 🚀 [Setup Guide](guides/development/setup.md) - Environment setup / Налаштування середовища
- 🏗️ [Project Structure](guides/development/structure.md) - Understanding the codebase / Розуміння кодової бази

**For translators / Для перекладачів:**
- 🌍 [Translation Overview](guides/translation/README.md) - Translation system / Система перекладів
- 📝 [Translation Workflow](guides/translation/workflow.md) - Step-by-step guide / Покроковий посібник
- 🛠️ [Translation Tools](guides/translation/tools.md) - Tools for translators / Інструменти для перекладачів

### Documentation Guidelines

- Write in clear, concise English
- Use proper reStructuredText formatting
- Include code examples where appropriate
- Add cross-references to related sections
- Test all code examples before committing
- Build documentation locally to check for errors

### Contributing Translations

We welcome translations! Here's how:

1. **Extract messages:**
   ```bash
   make gettext
   ```

2. **Update translation catalogs:**
   ```bash
   make update
   ```

3. **Edit `.po` files** in `docs/locale/{uk,ru}/LC_MESSAGES/`
   - Use tools like [Poedit](https://poedit.net/) or edit manually
   - Translate `msgstr` fields, keep `msgid` unchanged

4. **Test your translation:**
   ```bash
   make html-uk  # or html-ru
   xdg-open docs/_build/html/uk/index.html
   ```

5. **Submit a pull request**

📖 **Full translation guide:** [LOCALIZATION.md](LOCALIZATION.md)

## 🔧 ReadTheDocs Configuration

The project is configured for ReadTheDocs with:

- **Python 3.13** on Ubuntu 24.04
- **Sphinx RTD Theme** for beautiful documentation
- **Multiple output formats**: HTML, PDF, EPUB
- **Automatic builds** on every push to main branch
- **Version management** support
- **Search functionality** enabled

### Features

✅ **Multilingual support** - English, Ukrainian, Russian  
✅ **Automatic documentation builds** on every commit  
✅ **Multiple output formats** - HTML, PDF, EPUB  
✅ **Full-text search** functionality  
✅ **Version control** support  
✅ **GitHub integration** with badges and links  
✅ **Mobile-friendly** responsive theme  
✅ **Code syntax highlighting** for multiple languages  
✅ **Cross-referencing** between pages  
✅ **API documentation** generation  
✅ **Internationalization (i18n)** with sphinx-intl  
✅ **CI/CD integration** with GitHub Actions

## 📝 Syntax Reference

Documentation uses reStructuredText. Quick reference:

```rst
Headers
=======

Subheader
---------

**bold** and *italic*

`inline code`

.. code-block:: python

   # Code block
   print("Hello, World!")

.. note::
   This is a note

.. warning::
   This is a warning

:doc:`link-to-other-page`

External link: `ReadTheDocs <https://readthedocs.org/>`_
```

## 🐛 Reporting Issues

Found an issue in the documentation?

1. Check if it's already reported in [Issues](https://github.com/vergilium/ByByteDoc/issues)
2. If not, create a new issue with:
   - Clear description of the problem
   - Page/section where the issue occurs
   - Suggested fix (if any)

## 📄 License

This documentation is part of the ByByte project.

## 🔗 Links

- **Documentation**: https://bybyte.readthedocs.io/
- **GitHub Repository**: https://github.com/vergilium/ByByteDoc
- **Issue Tracker**: https://github.com/vergilium/ByByteDoc/issues

---

Built with ❤️ using [Sphinx](https://www.sphinx-doc.org/) and [ReadTheDocs](https://readthedocs.org/)

