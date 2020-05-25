from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    min_so_far, max_so_far = float('inf'), float('-inf')
    n = len(prices)
    L, R = [0] * n, [0] * n
    for i in range(1, n):
        j = n-1-i
        min_so_far = min(min_so_far, prices[i-1])
        max_so_far = max(max_so_far, prices[j+1])
        L[i] = max(L[i-1], prices[i] - min_so_far)
        R[j] = max(R[j+1], max_so_far - prices[j])
    return max([sell+buy for sell,buy in zip(L, R)])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
