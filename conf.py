# -*- coding: utf-8 -*-
"""Sphinx configuration file."""

import os
import sys

from setuptools_scm import get_version

# -- Project information -----------------------------------------------------
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AvengineersWebPage'

version = get_version(root='.', relative_to=__file__)
release = version

author = 'Alexander Mann-Wahrenberg, Alexandru Maxiniuc, Jochen Maletschek, Karsten Günther, Matthias Eggert'
copyright = f"2022, {author}"


# -- General configuration ---------------------------------------------------
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# @see https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html

sys.path.append(os.path.abspath("./_ext"))

extensions = [
    'sphinx.ext.githubpages',       # @see https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
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

html_baseurl = 'https://avengineers.github.io/'

# -- Options for XXXXXXXXXXXXXXXXX ------------------------------------------
# @see 

#EOF
