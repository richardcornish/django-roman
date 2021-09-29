.. _usage:

Usage
*****

Load the template tags.

.. code-block:: django

   {% load roman_tags %}

Filter
======

Convert Arabic numerals to Roman numerals with the ``roman`` template filter.

.. code-block:: django

   {{ "Party like it's 1999."|roman }}

Result:

.. code-block:: html

   Party like it's <span class="numerals numerals-roman">MCMXCIX</span>.

Convert Roman numerals to Arabic numerals with the ``arabic`` template filter.

.. code-block:: django

   {{ "Where did the princes go, Richard III of England?"|arabic }}

Result:

.. code-block:: html

   Where did the princes go, Richard <span class="numerals numerals-arabic">3</span> of England?
