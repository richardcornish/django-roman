.. _tests:

Tests
*****

`Continuous integration test results <https://app.travis-ci.com/github/richardcornish/django-roman>`_ are available online.

However, you can also test the source code.

.. code-block:: bash

   $ workon myvenv
   (myvenv)$ django-admin test roman.tests --settings="roman.tests.settings"
   Creating test database for alias 'default'...
   System check identified no issues (0 silenced).
   ............
   ----------------------------------------------------------------------
   Ran 12 tests in 0.085s
   
   OK
   Destroying test database for alias 'default'...

A bundled settings file allows you to test the code without even creating a Django project.
