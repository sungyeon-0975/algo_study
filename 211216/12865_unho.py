""" 냅색 알고리즘 """
import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
li = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = li[i][0]
        value = li[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[N][K])



"""
DFS 이용한 탐색 (시간초과)
"""
# def dfs(idx, weight, ans):
#     global answer

#     if idx >= N or not weight:
#         if answer < ans:
#             answer = ans
#         return
#     elif weight < 0:
#         return
    
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = 1
#             dfs(idx+1, weight-li[i][0], ans+li[i][1])
#             visited[i] = 0

# N, K = map(int, sys.stdin.readline().split())
# li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# answer = 0
# visited = [0] * N

# dfs(0, K, 0)

# print(answer)