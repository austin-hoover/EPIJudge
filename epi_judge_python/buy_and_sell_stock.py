from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    n = len(prices)
    max_profit = 0
    lo = 0
    while lo < n-1:
        # Move lo to valley as starting point
        while prices[lo+1] <= prices[lo]:
            lo += 1
            if lo == n-1:
                return max_profit
        # Move hi to highest peak
        hi = lo+1
        for i in range(lo+1, n):
            if prices[i] > prices[hi]:
                hi = i
        # Move lo to lowest valley before hi
        for i in range(lo+1, hi):
            if prices[i] < prices[lo]:
                lo = i
        # Record elevation gain
        local_profit = prices[hi] - prices[lo]
        max_profit = max(max_profit, local_profit)
        # Check next sub-array
        lo = hi + 1
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
