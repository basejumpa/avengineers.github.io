# -*- coding: utf-8 -*-
"""Sphinx configuration file."""

from setuptools_scm import get_version

# -- Project information -----------------------------------------------------
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Avengineers'

version = get_version(root='.', relative_to=__file__)
release = version

author = 'Alexander Mann-Wahrenberg, Alexandru Maxiniuc, Jochen Maletschek, Karsten Günther, Matthias Eggert'
copyright = f"2022, {author}"


# -- General configuration ---------------------------------------------------
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# @see https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html

extensions = [
    'sphinx.ext.githubpages',       # @see https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
]

exclude_patterns = [
    'README.rst',
    'LICENSE.rst',
]

# Figure references shall have numbers
numfig = True

# -- Options for HTML output with theme "sphinx_material" -------------------
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# @see https://bashtage.github.io/sphinx-material/customization.html

html_title = f"Avengineers {version}" 
html_logo  = '_figures/logo.svg'

# Hide hyper link which leeds to the source of page displayed
html_show_sourcelink = False

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_theme = 'sphinx_material'

html_theme_options = {
    'nav_title'    : f"Avengineers",
    'base_url'     : 'https://avengineers.github.io/',
    
    'repo_url'     : 'https://github.com/avengineers/avengineers.github.io',
    'repo_name'    : 'avengineers.github.io',
    
    'color_primary': 'teal',
    'color_accent' : 'yellow',
    
    'globaltoc_depth'        : 3,
    'globaltoc_collapse'     : 'true',
    'globaltoc_includehidden': 'true',
}

# -- Options for XXXXXXXXXXXXXXXXX ------------------------------------------
# @see 

#EOF
