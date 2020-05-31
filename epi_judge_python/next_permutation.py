from typing import List

from test_framework import generic_test

                                                                     #
def next_permutation(perm: List[int]) -> List[int]:

    # Check for array of length 1
    n = len(perm)
    if n < 2:
        return []

    # Try to swap last two elements
    if perm[-1] > perm[-2]:
        perm[-1], perm[-2] = perm[-2], perm[-1]
    else:
        # Travel backwards until we find perm[i] < perm[i+1]
        i = n - 2
        while perm[i] >= perm[i + 1]:
            i -= 1
            if i < 0:  # last permutation
                return []
        # Travel backwards from end of array to find smallest
        # element in perm[i+1:] larger than perm[i], then swap
        # it with perm[i].
        for j in reversed(range(i+1, n)):
            if perm[j] > perm[i]:
                perm[j], perm[i] = perm[i], perm[j]
                break
        # perm[i+1:] is already sorted in descending order,
        # but it now needs to be in ascending order.
        perm[i+1:] = reversed(perm[i+1:])
    return perm

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
