from itertools import combinations
from collections import deque
from copy import deepcopy

import sys
sys.stdin = open('17141_input.txt')
# input = sys.stdin.readline


def bfs(c, f):
    global answer

    visited = [[0] * N for _ in range(N)]
    q = deque()
    temp = 0

    for k in c:
        i, j = available[k]
        visited[i][j] = 1
        q.append((i, j))
        f -= 1

    while q:
        i, j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1:
                if visited[i][j] + 1 < visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
                elif not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
                    f -= 1
        if len(q) == 0:
            temp = visited[i][j] - 1

    if not f and temp < answer:
        answer = temp


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
available = []
answer = 1e9
fill = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            fill += 1
        elif arr[i][j] == 2:
            available.append((i, j))
            fill += 1

comb = list(combinations(range(len(available)), M))

for c in comb:
    f = fill
    bfs(c, f)

if answer == 1e9:
    answer = -1

print(answer)