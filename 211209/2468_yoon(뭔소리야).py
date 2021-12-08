import sys
sys.setrecursionlimit(10000)
sys.stdin = open('2468_input.txt')
# input = sys.stdin.readline

# 37780KB / 1748ms


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(i, j, s):
    global visited
    for k in range(4):
        ni = i + dir[k][0]
        nj = j + dir[k][1]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > s and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, s)


N = int(input())
arr = []
visited = [[0 for _ in range(N)] for _ in range(N)]
min_h, max_h = 100, 0
for _ in range(N):
   line = list(map(int, input().split()))
   min_h = min(min_h, min(line))
   max_h = max(max_h, max(line))
   arr.append(line)

max_cnt = 1
for s in range(min_h, max_h):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > s and not visited[i][j]:
                visited[i][j] = 1
                cnt += 1
                dfs(i, j, s)
    max_cnt = max(max_cnt, cnt)
    visited = [[0 for _ in range(N)] for _ in range(N)]

print(max_cnt)