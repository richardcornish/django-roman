Django Roman
************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-roman.svg
.. _PyPI version: https://pypi.org/project/django-roman/

.. |Build status| image::
   https://api.travis-ci.com/richardcornish/django-roman.svg?branch=main
.. _Build status: https://app.travis-ci.com/github/richardcornish/django-roman

**Django Roman** is a `Django <https://www.djangoproject.com/>`_ `template tag <https://docs.djangoproject.com/en/dev/howto/custom-template-tags/>`_ application to convert `Arabic numerals <https://en.wikipedia.org/wiki/Arabic_numerals>`_ into `Roman numerals <https://en.wikipedia.org/wiki/Roman_numerals>`_.

* `Package <https://pypi.org/project/django-roman/>`_
* `Source <https://github.com/richardcornish/django-roman>`_
* `Documentation <https://django-roman.readthedocs.io/>`_
* `Tests <https://app.travis-ci.com/github/richardcornish/django-roman>`_

Install
=======

.. code-block:: bash

   $ pip install django-roman

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'roman',
   ]

Usage
=====

Use as a template tag.

.. code-block:: django

   {% load roman_tags %}

   {% to_roman %}Party like it's 1999.{% endto_roman %}

Or as a template filter.

.. code-block:: django

   {{ post.body|to_roman }}

Result:

.. code-block:: html

   Party like it's MCMXCIX.
