import sys
sys.setrecursionlimit(10000)
sys.stdin = open('4963_input.txt')
# input = sys.stdin.readline


# 33152KB / 88ms


def dfs(r, c):
    for k in range(8):
        ni = r + di[k]
        nj = c + dj[k]
        if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj)


# 상 하 좌 우 좌상 좌하 우상 우하
di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [0, 0, -1, 1, -1, -1, 1, 1]
while True:
    w, h = map(int, input().split())
    ans = 0
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                dfs(i, j)
                ans += 1
    print(ans)
