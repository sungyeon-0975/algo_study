from collections import defaultdict, deque
from copy import deepcopy
# 에라토스테네스의 체
chk = [True]*10000
for i in range(2, 101):
    if chk[i] == True:
        for j in range(i+i, 10000, i):
            chk[j] = False

lst = [i for i in range(1000, 10000) if chk[i]]
l = len(lst)

# 그래프


gh = {i: i for i in lst}


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return


def find(n):
    p = n
    while gh[p] != p:
        p = gh[p]
    while n != p:
        gh[n], n = p, gh[p]
    return p


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    if a == b:
        print(0)
        break

    print(bfs(a, b))
