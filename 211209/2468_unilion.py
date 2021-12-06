#	31880KB	1596ms

import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, safe):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N:
                if N_list[nr][nc] > safe and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
N_list_min = min(map(min, N_list))
N_list_max = max(map(max, N_list))

result = N_list_min
for safe in range(N_list_min, N_list_max + 1):
    visited = [[0] * N for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            if N_list[i][j] > safe and visited[i][j] == 0:
                bfs(i, j, safe)
                temp += 1
    if temp > result:
        result = temp
print(result)