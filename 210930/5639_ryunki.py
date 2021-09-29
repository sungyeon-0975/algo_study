import sys

sys.stdin = open('input_5639.txt')
sys.setrecursionlimit(10 ** 9)
def match(start,end):
    if start>end:
        return

    right = end+1

    for i in range(start+1,end+1):
        if tree[start]<tree[i]:
            right = i
            break

    match(start+1,right-1) # 왼쪽 트리
    match(right,end) # 오른쪽 트리
    print(tree[start])

tree = [*map(int,sys.stdin.read().split())]

match(0,len(tree)-1)
#
# M = 9 ** 9
# a = [*map(int, sys.stdin.read().split()),M]
# print(a)
#
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
