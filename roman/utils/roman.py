"""
Convert to and from Roman numerals
This program is part of 'Dive Into Python 3', a free Python book for
experienced programmers. Visit http://diveintopython3.org/ for the latest
version.

https://github.com/kennethreitz/dive-into-python3/blob/master/examples/roman7.py
"""


import re


class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


class InvalidRomanNumeralError(ValueError):
    pass


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

roman_numeral_pattern = re.compile(
    """
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """,
    re.VERBOSE,
)


def to_roman(n):
    """Convert integer to Roman numeral"""
    try:
        n = int(n)
    except ValueError:
        raise NotIntegerError("Non-integers cannot be converted")
    if not (0 < n < 4000):
        raise OutOfRangeError("Number is out of range. Number must be from 1 to 3999.")

    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result


def from_roman(s):
    """Convert Roman numeral to integer"""
    if not isinstance(s, str):
        raise InvalidRomanNumeralError("Input must be a string")
    if not roman_numeral_pattern.search(s):
        raise InvalidRomanNumeralError("Invalid Roman numeral: %s" % s)

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index : index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
