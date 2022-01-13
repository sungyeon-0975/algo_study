from itertools import combinations
from collections import deque
from copy import deepcopy

import sys
sys.stdin = open('17141_input.txt')
# input = sys.stdin.readline


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(c):
    global visited, answer

    q = deque()
    temp = 1
    for k in range(len(c)):
        i, j = available[k]
        q.append([i, j, 1])             # 숫자 기록 1부터 시작, 나중에 1 빼주기
    while q:
        i, j, num = q.popleft()
        visited[i][j] = num
        temp = num
        if temp-1 > answer:
            return
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                q.append((ni, nj, num+1))
    print(visited)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                return
    else:
        if temp-1 < answer:
            answer = temp-1


N, M = map(int, input().split())
arr, available = [], []
answer = 1e9

for i in range(N):
    row = list(map(int, input().split()))
    new_row = [0] * N
    for j in range(N):
        if row[j] == 1:                 # 벽 위치 -1로 재표시
            new_row[j] = -1
        elif row[j] == 2:               # 바이러스 놓을 수 있는 자리 따로 리스트화, arr에는 0으로 표시
            available.append((i, j))
            new_row[j] = 0
    arr.append(new_row)

comb = list(combinations(range(len(available)), M))

for c in comb:
    visited = deepcopy(arr)
    bfs(c)

if answer == 1e9:
    answer = -1

print(answer)