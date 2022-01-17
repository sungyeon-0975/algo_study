# import sys
# input = sys.stdin.readline

# 30864KB / 252ms

def dfs(arr, M):
    global visited
    if len(arr) == M:
        print(*arr)
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            dfs(arr+[i], M)
            visited[i] = 0


N, M = map(int, input().split())
num = list(range(1, N))

for i in range(1, N+1):
    visited = [0] * (N+1)
    visited[i] = 1
    dfs([i], M)
