import sys
sys.stdin = open('input_1953.txt')
from collections import deque

# 상0 우1 하2 좌3
tunnel = [
    [],
    [0, 1, 2, 3],
    [0, 2],
    [1, 3],
    [0, 1],
    [1, 2],
    [2, 3],
    [0, 3],
]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs():
    global q, visited

    while q:
        i, j = q.popleft()
        dir = tunnel[arr[i][j]]

        for k in dir:
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < M and (k+2) % 4 in tunnel[arr[ni][nj]] and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] += visited[i][j] + 1


T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((R, C))
    visited[R][C] = 1

    bfs()

    ans = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] < L+1:
                ans += 1

    print('#{} {}'.format(t, ans))