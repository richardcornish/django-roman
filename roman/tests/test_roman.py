from django.template import Context, Template
from django.test import TestCase


class RomanTestCase(TestCase):
    """Roman test cases."""

    def test_roman_text(self):
        out = Template("{% load roman_tags %}" "{{ '1999'|roman }}").render(Context())
        self.assertEqual(out, '<span class="numerals numerals-roman">MCMXCIX</span>')

    def test_roman_integer(self):
        out = Template("{% load roman_tags %}" "{{ 1999|roman }}").render(Context())
        self.assertEqual(out, '<span class="numerals numerals-roman">MCMXCIX</span>')

    def test_roman_text_context(self):
        out = Template("{% load roman_tags %}" "{{ year|roman }}").render(
            Context(
                {
                    "year": "1999",
                }
            )
        )
        self.assertEqual(out, '<span class="numerals numerals-roman">MCMXCIX</span>')

    def test_roman_integer_context(self):
        out = Template("{% load roman_tags %}" "{{ year|roman }}").render(
            Context(
                {
                    "year": 1999,
                }
            )
        )
        self.assertEqual(out, '<span class="numerals numerals-roman">MCMXCIX</span>')

    def test_roman_words(self):
        out = Template(
            "{% load roman_tags %}"
            "{{ 'Party like it is 1999. Or maybe 2001?'|roman }}"
        ).render(Context())
        self.assertEqual(
            out,
            'Party like it is <span class="numerals numerals-roman">MCMXCIX</span>. Or maybe <span class="numerals numerals-roman">MMI</span>?',
        )

    def test_roman_words_context(self):
        out = Template("{% load roman_tags %}" "{{ words|roman }}").render(
            Context({"words": "Party like it is 1999. Or maybe 2001?"})
        )
        self.assertEqual(
            out,
            'Party like it is <span class="numerals numerals-roman">MCMXCIX</span>. Or maybe <span class="numerals numerals-roman">MMI</span>?',
        )

    def test_roman_now(self):
        out = Template(
            "{% load roman_tags %}" "{% filter roman %}{% now 'Y' %}{% endfilter %}."
        ).render(Context())
        self.assertEqual(out, '<span class="numerals numerals-roman">MMXXI</span>.')

    def test_arabic_text(self):
        out = Template("{% load roman_tags %}" "{{ 'MCMXCIX'|arabic }}").render(
            Context()
        )
        self.assertEqual(out, '<span class="numerals numerals-arabic">1999</span>')

    def test_arabic_text_context(self):
        out = Template("{% load roman_tags %}" "{{ year|arabic }}").render(
            Context(
                {
                    "year": "MCMXCIX",
                }
            )
        )
        self.assertEqual(out, '<span class="numerals numerals-arabic">1999</span>')

    def test_arabic_words(self):
        out = Template(
            "{% load roman_tags %}"
            "{{ 'Party like it is MCMXCIX. Or maybe MMI?'|arabic }}"
        ).render(Context())
        self.assertEqual(
            out,
            'Party like it is <span class="numerals numerals-arabic">1999</span>. Or maybe <span class="numerals numerals-arabic">2001</span>?',
        )

    def test_arabic_words_context(self):
        out = Template("{% load roman_tags %}" "{{ words|arabic }}").render(
            Context({"words": "Party like it is MCMXCIX. Or maybe MMI?"})
        )
        self.assertEqual(
            out,
            'Party like it is <span class="numerals numerals-arabic">1999</span>. Or maybe <span class="numerals numerals-arabic">2001</span>?',
        )

    def test_arabic_richard(self):
        out = Template(
            "{% load roman_tags %}"
            "{{ 'Where did the princes go, Richard III of England?'|arabic }}"
        ).render(Context())
        self.assertEqual(
            out,
            'Where did the princes go, Richard <span class="numerals numerals-arabic">3</span> of England?',
        )
