from django.template import Context, Template
from django.test import TestCase


class RomanTestCase(TestCase):
    """Roman test cases."""

    def test_filter_to_roman(self):
        out = Template("{% load roman_tags %}" "{{ '1999'|to_roman }}").render(
            Context()
        )
        self.assertEqual(out, "MCMXCIX")

    def test_filter_from_roman(self):
        out = Template("{% load roman_tags %}" "{{ 'MCMXCIX'|from_roman }}").render(
            Context()
        )
        self.assertEqual(out, "1999")

    def test_tag_to_roman(self):
        out = Template(
            "{% load roman_tags %}" "{% to_roman %}1999{% endto_roman %}"
        ).render(Context())
        self.assertEqual(out, "MCMXCIX")

    def test_tag_from_roman(self):
        out = Template(
            "{% load roman_tags %}" "{% from_roman %}MCMXCIX{% endfrom_roman %}"
        ).render(Context())
        self.assertEqual(out, "1999")
