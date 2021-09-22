# 972ms, 46612KB
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
visited = set()
for _ in range(Q):
    result = 0
    i = int(input())
    temp = i
    while i > 1:
        if i in visited:
            result = i
        i //= 2
    visited.add(temp)
    print(result)