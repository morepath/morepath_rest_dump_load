.. image:: https://github.com/morepath/morepath_rest_dump_load/workflows/CI/badge.svg?branch=master
   :target: https://github.com/morepath/morepath_rest_dump_load/actions?workflow=CI
   :alt: CI Status

.. image:: https://img.shields.io/pypi/v/morepath_rest_dump_load.svg
  :target: https://pypi.org/project/morepath_rest_dump_load/

.. image:: https://img.shields.io/pypi/pyversions/morepath_static.svg
  :target: https://pypi.org/project/morepath_rest_dump_load/


Morepath RESTful HTTP API demo
==============================

Show how to create a RESTful API server with Morepath using
``dump_json`` and ``load_json``.

More information:

http://blog.startifact.com/posts/better-rest-with-morepath-08.html

Installation
------------

You can use pip in a virtual env::

  $ virtualenv env
  $ source env/bin/activate
  $ env/bin/pip install -e .

Then to run the web server::

  $ env/bin/morepath_rest

You can now access the application through http://localhost:5000
