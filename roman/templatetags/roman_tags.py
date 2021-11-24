import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from ..roman import (
    arabic as _arabic,
    arabic_pattern,
    roman as _roman,
    roman_pattern,
)

register = template.Library()


def roman_repl(match_obj):
    if match_obj and match_obj.group():
        html = '<span class="numerals numerals-roman">%s</span>'
        return html % _roman(match_obj.group())
    return ""


def arabic_repl(match_obj):
    if match_obj and match_obj.group():
        html = '<span class="numerals numerals-arabic">%s</span>'
        return html % _arabic(match_obj.group())
    return ""


@register.filter(name="roman", is_safe=True, needs_autoescape=True)
@stringfilter
def roman_filter(value, autoescape=True):
    if autoescape:
        value = conditional_escape(value)
    return mark_safe(arabic_pattern.sub(roman_repl, value))


@register.filter(name="arabic", is_safe=True, needs_autoescape=True)
@stringfilter
def arabic_filter(value, autoescape=True):
    if autoescape:
        value = conditional_escape(value)
    return mark_safe(roman_pattern.sub(arabic_repl, value))
