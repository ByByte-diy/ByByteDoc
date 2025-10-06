# Makefile for ByByte documentation
# This delegates all commands to docs/Makefile

.PHONY: help html clean latexpdf

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

# Catch-all target: route all unknown targets to docs/Makefile
%:
	@$(MAKE) -C docs $@

