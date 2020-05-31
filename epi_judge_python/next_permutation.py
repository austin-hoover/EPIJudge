from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # Check for short arrays
    n = len(perm)
    if n < 2:
        return []
    # Try to swap last two elements
    if perm[-1] > perm[-2]:
        perm[-1], perm[-2] = perm[-2], perm[-1]
    else:
        # Go back until we find an index to be incremented
        i = n - 2
        while perm[i] >= perm[i + 1]:
            i -= 1
            if i < 0: # Last dictionary sorted permutation
                return []
        # Find smallest element in perm[i+1] which is larger than perm[i]
        i_next_largest = i + 1
        for j in range(i + 2, n):
            if perm[j] > perm[i] and perm[j] < perm[i_next_largest]:
                i_next_largest = j
        # Move that element and sort the remaining array
        perm[i], perm[i_next_largest] = perm[i_next_largest], perm[i]
        perm[i+1:] = sorted(perm[i+1:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
