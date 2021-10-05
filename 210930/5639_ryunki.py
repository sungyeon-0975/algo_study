"""

38708KB, 3912ms
40776KB, 88ms

"""

import sys
from bisect import bisect

sys.stdin = open('input_5639.txt')
sys.setrecursionlimit(10 ** 9)


def match(start, end):

    if start >= end:
        return
    d = tree[start]
    idx = bisect(tree, d, start, end)
    print('idx : {}'.format(idx))
    match(start + 1, idx)
    match(idx, end)
    print(d)


tree = [*map(int, sys.stdin.read().split())]
print(tree)

match(0, len(tree))

#
# M = 9 ** 9
# a = [*map(int, sys.stdin.read().split()),M]
# print(a)
# def f(i, u):
#     p = a[i]
#     i += 1
#     i += p > a[i] and f(i, min(u, p)) - i
#     i += u > a[i] and f(i, u) - i
#     print(p)
#     return i
#
#
# f(0, M)
