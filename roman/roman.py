"""
Convert to and from Roman numerals
This program is part of 'Dive Into Python 3', a free Python book for
experienced programmers. Visit http://diveintopython3.org/ for the latest
version.

https://github.com/kennethreitz/dive-into-python3/blob/master/examples/roman7.py
"""


import re


roman_numeral_map = (
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)

arabic_pattern = re.compile(r"(\d+)")

roman_pattern = re.compile(
    """
    M{0,3}              # thousands - 0 to 3 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    """,
    re.VERBOSE,
)


def roman(n):
    """Convert integer to Roman numeral"""
    try:
        n = int(n)
    except ValueError:
        return n
    if not (0 < n < 4000):
        return n
    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result


def arabic(s):
    """Convert Roman numeral to integer"""
    if not s:
        return s
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index : index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
