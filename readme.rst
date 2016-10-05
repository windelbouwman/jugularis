
Welcome to the jugularis compiler project!
==========================================

This project contains a compiler for various languages written in python.
The first language targets will be a simple toy language, and ada83.


Installation
============

Create a virtual env.

.. code:: bash

    $ clone jugularis
    $ virtualenv myenv
    $ source myenv/bin/activate
    $ pip install -r requirements

- textx, for the frontend
- ppci, for the backend

Ada compatibility
-----------------

To check the compiler, the following test suite can be used:

http://www.ada-auth.org/acats.html


.. image:: https://travis-ci.org/windelbouwman/jugularis.svg?branch=master
    :target: https://travis-ci.org/windelbouwman/jugularis

