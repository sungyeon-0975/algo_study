import sys
input = sys.stdin.readline

"""
4중 완전 탐색 까지는 좋았으나, 누적합에 대해 아직 잘 모르는 기분 ...
구글링을 해서 대충 이해는 했지만, 혼자 하라면 생각 못 할 알고리즘과 계산식
"""

def dfs(x, n, y, m):
    global result
    cnt = 0
    for i in range(x, N - n):
        for j in range(y, M - m):
            cnt += N_list[i][j]
    if result < cnt:
        result = cnt

N, M = map(int, input().split())
N_list = [list(map(int,input().split())) for _ in range(N)]
result = N_list[0][0]
for n in range(N):
    for m in range(M):
        for x in range(N - n):
            for y in range(M - m):
                dfs(x, n, y, m)
print(result)