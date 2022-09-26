# -*- coding: utf-8 -*-
"""Sphinx configuration file."""

import os
import sys

from setuptools_scm import get_version

# -- Project information -----------------------------------------------------
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Avengineers'

version = get_version(root='.', relative_to=__file__)
release = version

author = 'MQG/SD-RM - Alexander Mann-Wahrenberg, Alexandru Maxiniuc, Jochen Maletschek, Karsten Günther, Matthias Eggert'
copyright = f"2022, {author}"


# -- General configuration ---------------------------------------------------
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# @see https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html

extensions = [
    'sphinxawesome_theme',          # @see https://sphinxawesome.xyz/
    'sphinxcontrib.plantuml',       # @see https://github.com/sphinx-contrib/plantuml
# Todo: Make sphinxcontrib.umlet ready for usage and use it here. Then replace the generation of the umlet-exports in the makefile by this extension. Why necessary: Without that, umlet-exporting does not work together with sphinx-autobuild and sphinx_multiversion
#    'sphinxcontrib.umlet',          # @see https://pypi.org/project/sphinxcontrib-umlet/
]

templates_path = [
    "_templates",
]
exclude_patterns = [
    'README.rst',
    'LICENSE.rst',
]

numfig = True

# -- Options for HTML output -------------------------------------------------
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# @see https://sphinxawesome.xyz/

#master_doc = "index"

html_theme_path = [
    '_themes'
]

html_css_files = [
    # 'basic.css',  # included through inheritance from the basic theme
    'sphinx13.css',
]
#html_theme = 'sphinx13'

html_theme = 'sphinxawesome_theme'
pygments_style = "friendly"
html_permalinks_icon = '<span>#</span>'

# Usage: cwd == repository root
# $ make html


# -- Options for sphinxcontrib.umlet ----------------------------------------
# @see https://pypi.org/project/sphinxcontrib-umlet/


# -- Options for XXXXXXXXXXXXXXXXX ------------------------------------------
# @see 

#EOF
