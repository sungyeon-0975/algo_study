from collections import deque
from pprint import pprint


def bfs():
    dq = deque([(0, 0)])
    visited = [[0]*n for _ in range(m)]
    melted_cheeze = set()
    visited[0][0] = 1

    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = 1
                if mp[nr][nc]:
                    melted_cheeze.add((nr, nc))
                else:
                    dq.append((nr, nc))

    for r, c in melted_cheeze:
        mp[r][c] = 0

    return melted_cheeze


m, n = map(int, input().split())
mp, cheeze = list(), set()
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


for i in range(m):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            cheeze.add((i, j))
    mp.append(line)

ans = [0, len(cheeze)]

while True:
    ans[0] += 1
    melted_cheeze = bfs()
    cheeze = cheeze - melted_cheeze

    if not cheeze:
        break

    ans[1] = len(cheeze)

print(ans[0])
print(ans[1])
