# import sys
# from collections import deque


# def bfs(r, c):
#     d = [-1, 0, 1]
#     dq = deque([(r, c)])
#     mp[r][c] = 0

#     while dq:
#         r, c = dq.popleft()
#         for dr in d:
#             for dc in d:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < h and 0 <= nc < w and mp[nr][nc]:
#                     mp[nr][nc] = 0
#                     dq.append((nr, nc))


# while True:
#     w, h = map(int, input().split())

#     if not w and not h:
#         break

#     mp = [list(map(int, input().split())) for _ in range(h)]
#     ans = 0

#     for i in range(h):
#         for j in range(w):
#             if mp[i][j]:
#                 ans += 1
#                 bfs(i, j)

#     print(ans)

import sys
sys.setrecursionlimit(int(1e8))


def dfs(r, c):
    mp[r][c] = 0
    for dr in d:
        for dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and mp[nr][nc]:
                dfs(nr, nc)


while True:
    w, h = map(int, input().split())

    if not w and not h:
        break

    mp = [list(map(int, input().split())) for _ in range(h)]
    d = [-1, 0, 1]
    ans = 0

    for i in range(h):
        for j in range(w):
            if mp[i][j]:
                ans += 1
                dfs(i, j)

    print(ans)
