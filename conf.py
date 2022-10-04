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
    'sphinxawesome_theme',          # @see https://sphinxawesome.xyz/
    'sphinx.ext.githubpages',       # @see https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
    'sphinxcontrib.plantuml',       # @see https://github.com/sphinx-contrib/plantuml
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



# -- Options for PlantUml  --------------------------------------------------
# @see https://github.com/sphinx-contrib/plantuml

conf_location = os.path.realpath(os.path.dirname(__file__))
plantuml = f"java -jar {conf_location}/../utils/plantuml-1.2022.1.jar -config {conf_location}/plantuml.config"
plantuml_output_format = 'svg'
plantuml_latex_output_format = 'eps'


# -- Options for sphinxcontrib.umlet ----------------------------------------
# @see https://pypi.org/project/sphinxcontrib-umlet/


# -- Options for XXXXXXXXXXXXXXXXX ------------------------------------------
# @see 

#EOF
