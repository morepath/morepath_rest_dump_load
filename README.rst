Morepath RESTful HTTP API demo
==============================

Show how to create a RESTful API server with Morepath using
``dump_json`` and ``load_json``.

More information:

http://blog.startifact.com/posts/better-rest-with-morepath-08.html

Installation
------------

Firstly you have to install virtualenv by this command in the terminal

  $ pip install virtualenv 
Then type this command
  $ virtualenv env
After then you Have to activate the virtual environment by this command.
  $ source env/bin/activate
Then use this.
  $ env/bin/pip install -e .

Then to run the web server::

  $ env/bin/morepath_rest

You can now access the application through http://localhost:5000
