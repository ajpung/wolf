.. WOLF documentation master file, created by
   sphinx-quickstart on Mon Nov 6 15:19:08 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the WOLF documentation!
==================================

**WOLF** (Waveform Operation and Layering Framework) is a Python library aimed at ingesting, processing, and modifying sound files.

.. warning::

   This project is under active development


Installation
------------
.. note::

   If running on a Mac, first ensure you have developer tools installed by running
   ``xcode-select --install``


.. code::

   python -m pip install --upgrade pip setuptools wheel numpy
   python -m pip install wolf



.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Development

   development/contributing/workflow
   development/contributing/internals
   development/changelog


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: API Reference

   modules/analysis
   modules/data
   modules/physics
   modules/utils




Indices and tables
==================

* :ref:`genindex`
* :ref:`search`