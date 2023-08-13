# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'refineryframe package'
copyright = '2023, Kyrylo Mordan'
author = 'Kyrylo Mordan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo",
              "sphinx.ext.viewcode",
              "sphinx.ext.autodoc"]  # Add the m2r2 extension for Markdown support

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','setup.py']
autodoc_mock_imports = ['setup']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']



# # -- Include the content of README.md ----------------------------------------
# # Include the content of README.md using the m2r2 extension
# from m2r2 import convert

# with open('README_base.md', 'r') as f:
#     readme_md_content = f.read()

# readme_rst_content = convert(readme_md_content)

# with open('readme.rst', 'w') as f:
#     f.write(readme_rst_content)
