# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXAUTOGEN = sphinx-autogen
BUILDDIR      = _build

# Internal variables.
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees  $(SPHINXOPTS) .

PYTHON_VERSION = $(shell python -c "import sys; v=sys.version_info.major; sys.stdout.write(str(v))")
PORT = 8010
ifeq ($(PYTHON_VERSION), 2)
	HTTP_SERVER = "SimpleHTTPServer"
else
	HTTP_SERVER = "http.server"
endif

.PHONY: help clean html linkcheck doctest api

all: html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  all        generate the complete webpage"
	@echo "  html       make only the HTML files from the existing rst sources"
	@echo "  linkcheck  check all external links for integrity"
	@echo "  doctest    run all doctests embedded in the documentation (if enabled)"

clean:
	rm -rf $(BUILDDIR)/html/*
	rm -rf $(BUILDDIR)/doctrees
	rm -rf $(BUILDDIR)/linkcheck
	rm -rf modules
	rm -rf api/wavefd*.rst
	rm -rf api/generated
	rm -rf .ipynb_checkpoints

html: api
	@echo
	@echo "Building HTML files."
	@echo
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

api:
	@echo
	@echo "Building API docs."
	@echo
	$(SPHINXAUTOGEN) -i -t _templates -o api/ api/_generate_api.rst


linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

serve:
	cd $(BUILDDIR)/html && python -m $(HTTP_SERVER) $(PORT)
