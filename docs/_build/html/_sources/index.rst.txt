.. documentation for refineryframe package master file, created by
   sphinx-quickstart on Sun Aug 13 21:07:03 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to documentation for refineryframe package!
===================================================================

.. role:: raw-html-m2r(raw)
   :format: html



.. image:: https://github.com/Kiril-Mordan/refineryframe/workflows/Tests/badge.svg
   :target: https://github.com/Kiril-Mordan/refineryframe/actions/
   :alt: Build status


.. image:: https://static.pepy.tech/badge/refineryframe
   :target: https://pepy.tech/project/refineryframe
   :alt: Downloads


.. image:: https://img.shields.io/pypi/v/refineryframe
   :target: https://pypi.org/project/refineryframe/
   :alt: PyPiVersion


.. image:: https://img.shields.io/github/license/Kiril-Mordan/refineryframe
   :target: https://github.com/Kiril-Mordan/refineryframe/blob/main/LICENSE
   :alt: License


.. image:: https://img.shields.io/pypi/pyversions/refineryframe
   :target:
   :alt: PyVersions


.. image:: https://codecov.io/gh/Kiril-Mordan/refineryframe/branch/main/graph/badge.svg
   :target: https://app.codecov.io/gh/Kiril-Mordan/refineryframe?branch=main
   :alt: Codecov


refineryframe
=============

.. image:: _static/logo.png

The goal of the package is to simplify life for data scientists, that have to deal with imperfect raw data. The package suppose to detect and clean unexpected values, while doubling as safeguard in production code based on predifined conditions that arise from business assumptions or any other source. The package is well suited to be an initial preprocessing step in ml pipelines situated between data gathering and training/scoring steps.

Developed by Kyrylo Mordan (c) 2023

Installation
------------

Install ``refineryframe`` via pip with

.. code-block:: bash

   pip install refineryframe


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
