import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:

    # Remove b's
    for i in range(size):
        while s[i] == 'b':
            for j in range(i, size):
                s[j] = s[j + 1]

    # Convert a's to d's
    n_valid = len(s) - s.count('')
    size = n_valid + s.count('a')
    write_idx = size - 1
    for char in reversed(s[:n_valid]):
        if char == 'a':
            s[write_idx] = s[write_idx - 1] = 'd'
            write_idx -= 2
        else:
            s[write_idx] = char
            write_idx -= 1

    return size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
