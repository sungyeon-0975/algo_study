from itertools import combinations
from collections import deque


def bfs(start, cnt):
    global ans
    dq = deque(start)
    for r, c in start:
        tmp_mp[r][c] = 0

    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if tmp_mp[nr][nc] == '-' and mp[nr][nc] != 1:
                    tmp_mp[nr][nc] = tmp_mp[r][c] + 1
                    cnt -= 1
                    dq.append((nr, nc))

    if not cnt:
        ans = min(ans, tmp_mp[r][c])


n, m = map(int, input().split())
mp, virus = [], []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = n**2
ans = 10**10

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            cnt -= 1
        if line[j] == 2:
            virus.append((i, j))
    mp.append(line)

for start in combinations(virus, m):
    tmp_mp = [['-'] * n for _ in range(n)]
    bfs(start, cnt - m)

print(-1 if ans == 10**10 else ans)
