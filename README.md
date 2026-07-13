# ByByte Documentation

[![Documentation Status](https://readthedocs.org/projects/bybyte/badge/?version=latest)](https://bybyte.readthedocs.io/en/latest/?badge=latest)

This repository contains the complete documentation for the ByByte project, an Arduino-based system.

## 📖 Documentation

The documentation is automatically built and published on **ReadTheDocs**:

🔗 **[Read the Docs](https://bybyte.readthedocs.io/)**

## 🚀 Building Documentation Locally

### Cloning the Repository

This project pulls content from external repositories via **git submodules** in the
`shared/` directory:

| Submodule path | Repository | Contents |
|----------------|------------|----------|
| `shared/github/` | [`ByByte-diy/.github`](https://github.com/ByByte-diy/.github) | Organization profile, mission, policies |
| `shared/bybyte-nano/` | [`ByByte-diy/ByByteNano`](https://github.com/ByByte-diy/ByByteNano) | BOM, hardware images, schematics |

Clone with submodules in one step:

```bash
git clone --recurse-submodules https://github.com/vergilium/ByByteDoc.git
```

If you already cloned the repository without submodules, initialize them once:

```bash
git submodule update --init --recursive
```

To pull the latest changes of the shared content later:

```bash
git submodule update --remote --recursive
```

### Including content from submodules

Markdown files from `shared/` are included with the standard ``.. include::``
directive. Paths are **relative to the current** ``.rst`` file and must use
``:parser: myst_parser.sphinx_`` for ``.md`` sources:

```rst
# docs/home/about.rst
.. include:: ../../shared/github/profile/README.md
   :parser: myst_parser.sphinx_

# docs/platforms/bybyte-nano-bill-of-materials.rst
.. include:: ../../shared/bybyte-nano/BOM.md
   :parser: myst_parser.sphinx_
   :start-line: 2
```

The ``shared_include`` extension (``docs/_ext/shared_include/``) overrides
Sphinx's built-in ``include`` directive. When a file under ``shared/`` is read,
**relative** Markdown links and ``<img src="…">`` paths are rewritten to
absolute GitHub URLs. Submodule metadata (owner, repo, branch) is discovered
automatically from ``.gitmodules`` and each submodule's ``git remote`` — no
hardcoded repository URLs in ``conf.py``. Native ``.rst`` files and includes
outside ``shared/`` are not modified.

| Path from ``.rst`` | Resolves to |
|--------------------|-------------|
| ``../../shared/github/…`` | ``shared/github/`` submodule (org docs) |
| ``../../shared/bybyte-nano/…`` | ``shared/bybyte-nano/`` submodule (hardware) |

This approach is compatible with **Esbonio** and RST linters: they see a normal
``include`` directive and a file path that exists on disk. Link rewriting runs
only during ``sphinx-build`` (live preview may still show relative image paths
from the source Markdown).

### Prerequisites

- Python 3.x
- pip
- GNU Make

On **Linux/macOS** `make` is usually preinstalled. On **Windows** it is not available by default — install it once:

```powershell
winget install GnuWin32.Make
```

Then add its folder `C:\Program Files (x86)\GnuWin32\bin` to your `PATH` and restart the terminal.

> **No-install alternative for Windows:** instead of installing GNU Make, replace `make` with `docs\make.bat` in every command below (e.g. `docs\make.bat html`). It is bundled with the repository and works out of the box.

### Installation & Build

Run all commands from the **project root**.

1. **Install dependencies:**
   ```bash
   pip install -r docs/requirements.txt
   ```

2. **Build HTML documentation:**
   ```bash
   make html
   ```

3. **View documentation** by opening `docs/_build/html/index.html` in your browser:
   - Linux: `xdg-open docs/_build/html/index.html`
   - macOS: `open docs/_build/html/index.html`
   - Windows: `Invoke-Item docs\_build\html\index.html`

### Available Make Commands

Run these commands from the project root directory (on Windows, use `docs\make.bat` instead of `make` if you did not install GNU Make):

| Command | Description |
|---------|-------------|
| `make html` | Build HTML documentation |
| `make clean` | Remove all build artifacts |
| `make latexpdf` | Build PDF documentation (requires LaTeX) |
| `make epub` | Build EPUB documentation |
| `make help` | Show all available commands |

### Building for a Specific Locale (i18n)

The documentation is written in English (`en`) and can be translated into other
locales using [`sphinx-intl`](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html).
Translation catalogs live in `docs/locale/<lang>/LC_MESSAGES/`.

#### Manual Translation Setup

Run all commands from the **project root**. Replace `uk` with your target locale code
(e.g. `de`, `fr`, `es`).

1. **Extract translatable strings** (generates `.pot` templates):
   ```bash
   sphinx-build -b gettext docs docs/_build/gettext
   ```

2. **Create/update the translation catalogs** for a locale:
   ```bash
   sphinx-intl update -p docs/_build/gettext -d docs/locale -l uk
   ```

3. **Translate** the generated `.po` files in `docs/locale/uk/LC_MESSAGES/` manually or use the automatic translation script below.

4. **Build the HTML for that locale** into its own output folder:
   ```bash
   sphinx-build -b html -D language=uk docs docs/_build/html/uk
   ```

#### Automatic Translation with AI (Gemini)

For fast and consistent translations, use the `translate_po.py` script to automatically
translate `.po` files using the Google Gemini API. First, create the `.po` files using
the manual setup steps above (steps 1–2).

**Prerequisites:**

1. Set the `GEMINI_API_KEY` environment variable with your Google Gemini API key:

   **Linux/macOS:**
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

   **Windows (PowerShell):**
   ```powershell
   $env:GEMINI_API_KEY = "your-api-key-here"
   ```

   **Windows (Command Prompt):**
   ```cmd
   set GEMINI_API_KEY=your-api-key-here
   ```

2. Install Python dependencies:
   ```bash
   pip install -r docs/requirements.txt pyyaml google-genai
   ```

**Usage:**

Translate a `.po` file to Ukrainian (default):
```bash
python scripts/translate_po.py docs/locale/uk/LC_MESSAGES/index.po
```

Translate to a specific language:
```bash
python scripts/translate_po.py docs/locale/uk/LC_MESSAGES/index.po --language uk
python scripts/translate_po.py docs/locale/ru/LC_MESSAGES/index.po --language ru
```

See available languages and options:
```bash
python scripts/translate_po.py --help
```

**Adding a New Language:**

1. Create a rule file `scripts/rule_xx.md` (where `xx` is the language code):

```markdown
---
name: German
target_language: German
---

You are a professional technical translator for the ByByte-DIY robotics
education project.

Translate English Sphinx documentation into natural, technically accurate
German.

Rules:
- Preserve the complete meaning.
- Use natural German suitable for educational technical documentation.
- Preserve all Sphinx/reStructuredText markup.
- Preserve placeholders exactly.
- ...
```

2. The script automatically discovers the new language. No code changes needed!

#### Paths to open a built locale

Each locale is built into a separate subfolder, so open the matching `index.html`:

| Locale | Path |
|--------|------|
| English (default) | `docs/_build/html/index.html` |
| Ukrainian (`uk`) | `docs/_build/html/uk/index.html` |
| `<lang>` | `docs/_build/html/<lang>/index.html` |

Open it in your browser:

- Linux: `xdg-open docs/_build/html/uk/index.html`
- macOS: `open docs/_build/html/uk/index.html`
- Windows: `Invoke-Item docs\_build\html\uk\index.html`

## 📂 Documentation Structure

```
ByByteDoc/
├── .readthedocs.yaml    # ReadTheDocs configuration
├── .gitignore           # Git ignore patterns
├── Makefile             # Root makefile for building docs
├── README.md            # This file
├── .gitmodules          # Git submodule definitions
├── shared/              # External content (git submodules)
│   ├── github/          #   ByByte-diy/.github — org docs & policies
│   └── bybyte-nano/     #   ByByte-diy/ByByteNano — BOM & hardware assets
└── docs/
   ├── index.rst            # Main documentation page
   ├── contributing.rst     # Contributing guidelines
   ├── changelog.rst        # Version changelog
   ├── home/
   │   ├── about.rst        # About section
   │   ├── mission.rst      # Mission section
   │   ├── quick-start.rst  # Quick start section
   │   └── organization-documents.rst  # Organization documents section
   │
   ├── platforms/           # Platforms documentation files
   │
   ├── conf.py              # Sphinx configuration
   ├── requirements.txt     # Python dependencies
   ├── Makefile             # Sphinx makefile (Linux/macOS)
   ├── make.bat             # Sphinx build script (Windows)
   ├── _ext/                # Custom Sphinx extensions
   │   └── shared_include/  # Rewrites links in shared/ includes
   ├── _static/             # Static files (images, CSS, etc.)
   └── locale/              # Translation catalogs (.po) per locale
```

## ✏️ Contributing to Documentation

We welcome contributions! To contribute:

1. **Fork this repository**
2. **Clone your fork** (with submodules):
   ```bash
   git clone --recurse-submodules https://github.com/YOUR_USERNAME/ByByteDoc.git
   cd ByByteDoc
   ```

3. **Create a new branch:**
   ```bash
   git checkout -b improve-docs
   ```

4. **Edit documentation files** in the `docs/` directory
   - Documentation is written in reStructuredText (`.rst`)
   - See [Sphinx documentation](https://www.sphinx-doc.org/) for syntax

5. **Build and test locally:**
   ```bash
   make clean && make html
   xdg-open docs/_build/html/index.html
   ```

6. **Commit and push:**
   ```bash
   git add .
   git commit -m "Improve documentation"
   git push origin improve-docs
   ```

7. **Create a Pull Request** on GitHub

### Documentation Guidelines

- Write in clear, concise English
- Use proper reStructuredText formatting
- Include code examples where appropriate
- Add cross-references to related sections
- Test all code examples before committing
- Build documentation locally to check for errors

## 🔧 ReadTheDocs Configuration

The project is configured for ReadTheDocs with:

- **Python 3.13** on Ubuntu 24.04
- **Sphinx RTD Theme** for beautiful documentation
- **Multiple output formats**: HTML, PDF, EPUB
- **Automatic builds** on every push to main branch
- **Version management** support
- **Search functionality** enabled

### Features

✅ Automatic documentation builds  
✅ Multiple output formats (HTML, PDF, EPUB)  
✅ Search functionality  
✅ Version control support  
✅ GitHub integration  
✅ Mobile-friendly theme  
✅ Code syntax highlighting  
✅ Cross-referencing  
✅ API documentation generation

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

