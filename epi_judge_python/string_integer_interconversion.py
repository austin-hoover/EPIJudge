from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:

    negative = x < 0
    x = abs(x)

    s = ''
    while True:
        s = ''.join([chr(ord('0') + x % 10), s])
        x = x // 10
        if x == 0:
            break

    if negative:
        s = ''.join(['-', s])
    return s


def string_to_int(s: str) -> int:

    x, sign = 0, +1
    str_to_int_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                       '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    if s[0] not in str_to_int_dict:
        sign = 1 - 2*(s[0] == '-')
        s = s[1:]
    for i, char in enumerate(reversed(s)):
        x += (10**i) * str_to_int_dict[char]
    return sign * x


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
