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
