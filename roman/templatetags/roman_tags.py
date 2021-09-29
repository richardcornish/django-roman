from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from ..utils.roman import from_roman as _from_roman, to_roman as _to_roman

register = template.Library()


@register.filter(name="to_roman", is_safe=True)
@stringfilter
def to_roman_filter(value):
    return mark_safe(_to_roman(value))


@register.filter(name="from_roman", is_safe=True)
@stringfilter
def from_roman_filter(value):
    return mark_safe(_from_roman(value))


class RomanNode(template.Node):
    def __init__(self, nodelist, func):
        self.nodelist = nodelist
        self.func = func

    def render(self, context):
        output = self.nodelist.render(context)
        return mark_safe(self.func(output))


@register.tag(name="to_roman")
def to_roman_tag(parser, token):
    nodelist = parser.parse(("endto_roman",))
    parser.delete_first_token()
    return RomanNode(nodelist, _to_roman)


@register.tag(name="from_roman")
def to_roman_tag(parser, token):
    nodelist = parser.parse(("endfrom_roman",))
    parser.delete_first_token()
    return RomanNode(nodelist, _from_roman)
