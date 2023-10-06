# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MaturityModel'
copyright = ''
author = ''

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',  # Falls Sie Graphviz verwenden
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

smartquotes = False

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'logo_nfdi4ing_cmyk_hoch.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    }

# -- Options for EPUB output
epub_show_urls = 'footnote'
