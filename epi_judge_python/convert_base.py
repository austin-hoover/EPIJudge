from test_framework import generic_test
import math

def convert_base(num_as_string: str, b1: int, b2: int) -> str:

    # Strip leading +/- sign
    is_negative = False
    if num_as_string[0] in ['+', '-']:
        is_negative = num_as_string[0] == '-'
        num_as_string = num_as_string[1:]

    # Convert from base b1 to base 10
    X, factor = 0, 1
    for i, char in enumerate(reversed(num_as_string)):
        number = ord(char) - ord('0')
        if number > 9:
            number = (ord(char) - ord('A') + 10)
        X += int(number) * factor
        factor *= b1

    # Convert to X to base b2
    start_index = int(math.log(X, b2)) if X > 0 else 0
    A = [0] * (start_index + 1)
    factor = b2 ** start_index
    for i in range(len(A)):
        A[i] = int(X // factor)
        X %= factor
        factor /= b2
        if X == 0:
            break

    # Change numbers larger than 10 to letters
    for i, number in enumerate(A):
        if number >= 10:
            A[i] = chr(ord('A') - 10 + number)

    # Convert list to string representation
    num_as_string_base_b2 = ''.join([str(c) for c in A])
    if is_negative:
        num_as_string_base_b2 = ''.join(['-', num_as_string_base_b2])
    return num_as_string_base_b2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
