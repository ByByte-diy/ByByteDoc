# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SPHINXINTL    ?= sphinx-intl
SOURCEDIR     = .
BUILDDIR      = _build
LANGUAGES     = uk ru

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "Internationalization targets:"
	@echo "  gettext    - extract translatable messages from source files"
	@echo "  update     - update translation catalogs (.po files)"
	@echo "  translate  - compile translation catalogs (.mo files)"
	@echo "  html-uk    - build Ukrainian HTML documentation"
	@echo "  html-ru    - build Russian HTML documentation"
	@echo "  html-all   - build documentation for all languages"

.PHONY: help Makefile gettext update translate html-uk html-ru html-all

# Extract translatable messages
gettext:
	@$(SPHINXBUILD) -b gettext $(SOURCEDIR) $(BUILDDIR)/gettext
	@echo "Translatable messages extracted to $(BUILDDIR)/gettext"

# Update translation catalogs
update: gettext
	@$(SPHINXINTL) update -p $(BUILDDIR)/gettext -l uk -l ru
	@echo "Translation catalogs updated in locale/"

# Compile translation catalogs
translate:
	@$(SPHINXINTL) build
	@echo "Translation catalogs compiled"

# Build Ukrainian documentation
html-uk:
	@$(SPHINXBUILD) -b html -D language=uk $(SOURCEDIR) $(BUILDDIR)/html/uk $(SPHINXOPTS)
	@echo "Ukrainian documentation built in $(BUILDDIR)/html/uk"

# Build Russian documentation
html-ru:
	@$(SPHINXBUILD) -b html -D language=ru $(SOURCEDIR) $(BUILDDIR)/html/ru $(SPHINXOPTS)
	@echo "Russian documentation built in $(BUILDDIR)/html/ru"

# Build documentation for all languages
html-all: html html-uk html-ru
	@echo "Documentation built for all languages"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

