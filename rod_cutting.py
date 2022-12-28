# rod_cutting.py
# By yohannes dawit

import functools
memoize = functools.lru_cache(maxsize = None)

import sys
sys.setrecursionlimit(10000)

class RodCutting:

    def  __init__(self, values):
        self.values = list(values)
        self.F = memoize(self.F)

    def F(self, n, length):

        if n == -1 or length == -1:
            return 0

        else:
            li, vi = self.values[n]

            if length - li < 0:
                return self.F(n - 1, length)

            else:
                return max(self.F(n - 1, length), vi + self.F(n - 1, length - li))


    def solution(self, n, length):
        optimal_val = self.F(n, length)
        optimal_cuts = []

        while n >= 0 and length >= 0:

            if self.F(n, length) > self.F(n - 1, length):
                l, val = self.values[n]
                optimal_cuts.append(l)
                length -= l

            n -= 1

        return optimal_val, optimal_cuts


def main():
    print("Implementing the Rod Cuting Algorithm")
    print("rc = RodCuttingg([(2, 10), (1, 15), (3, 5), (4,  20)])")
    rc = RodCutting([(2, 10), (1, 15), (3, 5), (4,  20)])
    print("rc.solution(3, 7)")
    print(rc.solution(3, 7))


if __name__ == "__main__":
    main()
