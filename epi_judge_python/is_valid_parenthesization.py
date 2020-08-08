from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    pairs = {'[':']', '{':'}', '(':')'}
    left = []
    for c in s:
        if c in pairs:
            left.append(c)
        elif not left or c != pairs[left.pop()]:
            return False
    return not left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
