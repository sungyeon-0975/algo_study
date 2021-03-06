from collections import deque


def bfs(r, c):
    counter = []
    visited[r][c] = 1
    dq = deque([(r, c)])

    while dq:
        r, c = dq.popleft()
        w = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < n and 0 <= nc < m:  # 이동가능
                if mp[nr][nc]:  # 연결가능
                    if not visited[nr][nc]:
                        visited[nr][nc] = 1
                        dq.append((nr, nc))
                else:  # 물
                    w += 1

        counter.append((r, c, w))

    for r, c, w in counter:
        mp[r][c] = mp[r][c] - w if mp[r][c] > w else 0


n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
ans = 0

# 시작지점 초기화
start = []
for i in range(n):
    for j in range(m):
        if mp[i][j]:
            start.append((i, j))


while True:
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    brk = False
    for i, j in start:
        if mp[i][j] and not visited[i][j]:
            if cnt:  # 덩어리가 두개
                brk = True
                break
            else:
                cnt += 1
                bfs(i, j)

        if brk:
            break

    if brk:
        break

    if cnt == 0:  # 덩어리가 없는 경우
        ans = 0
        break
    ans += 1


print(ans)
