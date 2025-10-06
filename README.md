# ByByte Documentation

[![Documentation Status](https://readthedocs.org/projects/bybyte/badge/?version=latest)](https://bybyte.readthedocs.io/en/latest/?badge=latest)

This repository contains the complete documentation for the ByByte project, an Arduino-based system.

## 📖 Documentation

The documentation is automatically built and published on **ReadTheDocs**:

🔗 **[Read the Docs](https://bybyte.readthedocs.io/)**

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
   make html
   ```

3. **View documentation:**
   ```bash
   xdg-open docs/_build/html/index.html
   ```

### Available Make Commands

Run these commands from the project root directory:

| Command | Description |
|---------|-------------|
| `make html` | Build HTML documentation |
| `make clean` | Remove all build artifacts |
| `make latexpdf` | Build PDF documentation (requires LaTeX) |
| `make epub` | Build EPUB documentation |
| `make help` | Show all available commands |

## 📂 Documentation Structure

```
ByByteDoc/
├── .readthedocs.yaml    # ReadTheDocs configuration
├── .gitignore           # Git ignore patterns
├── Makefile             # Root makefile for building docs
├── README.md            # This file
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
    └── _static/         # Static files (images, CSS, etc.)
```

## ✏️ Contributing to Documentation

We welcome contributions! To contribute:

1. **Fork this repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ByByteDoc.git
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

