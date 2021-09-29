.. _usage:

Usage
*****

Load the template tags.

.. code-block:: django

   {% load roman_tags %}

Filter
======

Use the ``to_roman`` template filter to convert from Arabic to Roman numerals.

.. code-block:: django

   {{ post.body|to_roman }}

Result:

.. code-block:: html

   Party like it's MCMXCIX.

Or use the ``from_roman`` template filter to convert from Roman to Arabic numerals.

.. code-block:: django

   {{ post.body|from_roman }}

Result:

.. code-block:: html

   Party like it's 1999.

Tag
===

Use the ``{% to_roman %}`` template tag to convert from Arabic to Roman numerals.

.. code-block:: django

   {% to_roman %}1999{% endto_roman %}

Result:

.. code-block:: html

   MCMXCIX

Or use the ``{% from_roman %}`` template tag to convert from Roman to Arabic numerals.

.. code-block:: django

   {% from_roman %}MCMXCIX{% endfrom_roman %}

Result:

.. code-block:: html

   1999
