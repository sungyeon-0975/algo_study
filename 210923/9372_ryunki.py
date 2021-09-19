"""
30704KB / 256ms
"""

import sys
# input = sys.stdin.readline
sys.stdin = open('input_9372.txt')


def DFS(key, cnt):
    visit[key] = 1

    for i in tree[key]:
        if visit[i] == 0:
            cnt = DFS(i, cnt + 1)
    return cnt


for test in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    tree = {x : [] for x in range(N + 1)}
    for i in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    visit = [0] * (N + 1)
    print(DFS(1, 0))
