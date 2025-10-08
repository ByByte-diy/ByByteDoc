# Makefile for ByByte documentation
# This delegates all commands to docs/Makefile

.PHONY: help html clean latexpdf gettext update translate html-uk html-ru html-all

help:
	@$(MAKE) -C docs help

html:
	@$(MAKE) -C docs html
	@echo ""
	@echo "Build finished. Open file://$(CURDIR)/docs/_build/html/index.html in your browser."

clean:
	@$(MAKE) -C docs clean

latexpdf:
	@$(MAKE) -C docs latexpdf

# Internationalization targets
gettext:
	@$(MAKE) -C docs gettext

update:
	@$(MAKE) -C docs update

translate:
	@$(MAKE) -C docs translate

html-uk:
	@$(MAKE) -C docs html-uk
	@echo ""
	@echo "Ukrainian docs: file://$(CURDIR)/docs/_build/html/uk/index.html"

html-ru:
	@$(MAKE) -C docs html-ru
	@echo ""
	@echo "Russian docs: file://$(CURDIR)/docs/_build/html/ru/index.html"

html-all:
	@$(MAKE) -C docs html-all
	@echo ""
	@echo "English: file://$(CURDIR)/docs/_build/html/index.html"
	@echo "Ukrainian: file://$(CURDIR)/docs/_build/html/uk/index.html"
	@echo "Russian: file://$(CURDIR)/docs/_build/html/ru/index.html"

# Catch-all target: route all unknown targets to docs/Makefile
%:
	@$(MAKE) -C docs $@

