Django Roman
************

|PyPI version|_ |Build status|_ |Documentation status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-roman.svg
.. _PyPI version: https://pypi.org/project/django-roman/

.. |Build status| image::
   https://github.com/richardcornish/django-roman/actions/workflows/main.yml/badge.svg
.. _Build status: https://github.com/richardcornish/django-roman/actions/workflows/main.yml

.. |Documentation status| image::
   https://readthedocs.org/projects/django-roman/badge/?version=latest
.. _Documentation status: https://django-roman.readthedocs.io/en/latest/?badge=latest

**Django Roman** is a `Django <https://www.djangoproject.com/>`_ `template tag <https://docs.djangoproject.com/en/dev/howto/custom-template-tags/>`_ application to convert `Arabic numerals <https://en.wikipedia.org/wiki/Arabic_numerals>`_ into `Roman numerals <https://en.wikipedia.org/wiki/Roman_numerals>`_.

Original Roman numeral conversion code `adapted <https://diveintopython3.net/refactoring.html>`_ from `Dive Into Python 3 <https://diveintopython3.net/>`_ by Mark Pilgrim.

* `Package <https://pypi.org/project/django-roman/>`_
* `Source <https://github.com/richardcornish/django-roman>`_
* `Documentation <https://django-roman.readthedocs.io/>`_
* `Tests <https://github.com/richardcornish/django-roman/actions/workflows/main.yml>`_

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

Convert Arabic numerals to Roman numerals with the ``roman`` template filter.

.. code-block:: django

   {% load roman_tags %}

   {{ "Party like it's 1999."|roman }}

Result:

.. code-block:: html

   Party like it's <span class="numerals numerals-roman">MCMXCIX</span>.

Can also be imported as a standalone Python module:

.. code-block:: python

   >>> from roman import roman
   >>> roman(1999)
   'MCMXCIX'
   >>> roman("1999")
   'MCMXCIX'
   >>> from roman import arabic
   >>> arabic("MCMXCIX")
   1999
