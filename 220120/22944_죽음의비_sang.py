from collections import deque


def bfs(start):
    dq = deque([start])

    while dq:
        r, c, h, d, cnt = dq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if mp[nr][nc] == "E":
                    return cnt + 1

                nh, nd = h, d

                if mp[nr][nc] == "U":
                    nd = D

                if nd:
                    nd -= 1
                else:
                    nh -= 1

                if nh and nh+nd > check[nr][nc]:
                    check[nr][nc] = nh+nd
                    dq.append((nr, nc, nh, nd, cnt + 1))

    return -1


N, H, D = map(int, input().split())
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

mp = []
check = [[0]*N for _ in range(N)]  # 최대 이동가능 거리

for i in range(N):
    lst = list(input())
    for j in range(N):
        if lst[j] == "S":
            start = (i, j, H, 0, 0)
            check[i][j] = H
    mp.append(lst)

check[start[0]][start[1]] = H
print(bfs(start))
