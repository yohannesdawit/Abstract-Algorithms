# Knapsack.py
# yohannes dawit

import functools
memoize = functools.lru_cache(maxsize = None)

import sys
sys.setrecursionlimit(10000)

class Knapsack:

    def  __init__(self, items):
        self.items = list(items)
        self.F = memoize(self.F)

    def F(self, i, j):

        if i == -1 or j == -1:
            return 0

        else:
            wi, vi = self.items[i]

            if j - wi < 0:
                return self.F(i - 1, j)

            else:
                return max(self.F(i - 1, j), vi + self.F(i - 1, j - wi))

    def solution(self, i, j):
        optimal_val = self.F(i, j)
        optimal_items = []

        while i >= 0 and j >= 0:

            if self.F(i, j) > self.F(i - 1, j):
                weight, val = self.items[i]
                optimal_items.append(val)
                j -= weight

            i -= 1

        return optimal_val, optimal_items
                


            
if __name__ == "__main__":
    main()
