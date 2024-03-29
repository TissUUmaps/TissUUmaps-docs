# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'TissUUmaps'
copyright = '2023, The TissUUmaps Team'
author = 'Nicolas Pielawski, Axel Andersson, Christophe Avenel, Andrea Behanova, Eduard Chelebian, Anna Klemm, Fredrik Nysjö, Leslie Solorzano, Carolina Wählby'

# The full version, including alpha/beta/rc tags
release = '3.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_panels',
    'sphinx.ext.autosectionlabel',
    'sphinx_search.extension',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx-jsonschema'
]
source_suffix = [
    '.rst', '.md'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['./css']

html_css_files = [
    'custom.css'
]

html_theme_options = {
    'style_nav_header_background': '#a31a25'
}

html_logo = 'docs/images/logo.png'

html_favicon = 'docs/images/favicon.ico'

html_context = {
  'display_github': True,
  'github_user': 'TissUUmaps',
  'github_repo': 'TissUUmaps-docs',
  'github_version': 'master/',
}

autodoc_member_order = 'bysource'

master_doc = 'index'

latex_documents = [
    (master_doc, 'index.tex', project,
     author.replace(', ', '\\and ').replace(' and ', '\\and and '),
     'manual'),
]

latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

latex_domain_indices = False
latex_use_modindex = False

# -- Copy the modules documentation ------------------------------------------
try:
    from urllib.request import urlretrieve

    urlretrieve (
        "https://raw.githubusercontent.com/TissUUmaps/TissUUmaps/master/CHANGELOG.md",
        "docs/intro/versions.md"
    )
except:
    print ("No internet connection, continuing without updating CHANGELOG.md")
