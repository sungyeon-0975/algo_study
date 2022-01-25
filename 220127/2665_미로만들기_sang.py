from collections import deque


def bfs(r, c):
    dq = deque([(r, c)])

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:

                if mp[nr][nc]:
                    if v[r][c] < v[nr][nc]:
                        v[nr][nc] = v[r][c]
                        dq.append((nr, nc))
                else:
                    if v[r][c] + 1 < v[nr][nc]:
                        v[nr][nc] = v[r][c] + 1
                        dq.append((nr, nc))


n = int(input())
mp = [list(map(int, list(input()))) for _ in range(n)]
v = [[n**2]*n for _ in range(n)]
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

v[0][0] = 0
bfs(0, 0)
print(v[-1][-1])
