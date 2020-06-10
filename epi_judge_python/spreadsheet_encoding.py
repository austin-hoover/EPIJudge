from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    n = 0
    for i, letter in enumerate(reversed(col)):
        n += (26**i) * (ord(letter) - ord('A') + 1)
    return n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
