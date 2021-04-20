from django import template


register = template.Library()

numerals_set = (
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
)

@register.filter(is_safe=True)
@register.simple_tag
def roman(value):
    try:
        n = int(value)
    except ValueError:
        return value
    if 0 < n < 4000:
        result = ''
        for integer, numeral in numerals_set:
            while n >= integer:
                result += numeral
                n -= integer
        return result
    return n
