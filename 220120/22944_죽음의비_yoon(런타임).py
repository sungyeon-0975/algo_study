import sys
# sys.setrecursionlimit(10000)
sys.stdin = open('22944_input.txt')
# input = sys.stdin.readline


def dfs(r, c, h, d, move):
    global ans, visited
    if arr[r][c] == 'E':
        if move < ans:
            ans = move
        return
    # if h == 0:
    #     return
    if arr[r][c] == 'U':
        d = D
    for k in range(4):
        ni = r + dir[k][0]
        nj = c + dir[k][1]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            visited[ni][nj] = 1
            # if arr[ni][nj] == 'U':
            #     d = D
            if d != 0:
                dfs(ni, nj, h, d-1, move+1)
            elif d == 0 and h > 0:
                dfs(ni, nj, h-1, d, move+1)
            else:
                continue
            visited[ni][nj] = 0


N, H, D = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
si, sj = 0, 0
ans = 10e9
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            si, sj = i, j
visited[si][sj] = 1
dfs(si, sj, H, 0, 0)
if ans == 10e9:
    ans = -1
print(ans)