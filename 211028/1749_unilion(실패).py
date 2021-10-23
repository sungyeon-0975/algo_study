import sys
input = sys.stdin.readline

"""
4중 완전 탐색 까지는 좋았으나, 누적합에 대해 아직 잘 모르는 기분 ...
구글링을 해서 대충 이해는 했지만, 혼자 하라면 생각 못 할 알고리즘과 계산식
https://hbj0209.tistory.com/142
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
N_list = [list(map(int, input().split())) for _ in range(N)]
result = N_list[0][0]
for n in range(N):
    for m in range(M):
        for x in range(N - n):
            for y in range(M - m):
                dfs(x, n, y, m)
print(result)

"""
# 구글링 코드
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
nums = [list(map(int,input().split())) for _ in range(N)]

# 일반식을 통한 prefix_sum 채우기
prefix_sum = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + nums[i - 1][j - 1] - prefix_sum[i - 1][j - 1]

# ans의 최솟값은 200x200칸에 모두 -10000이 들어 있는 경우인 -4억이다
# x1, y1, x2, y2를 증가시켜가며 4중 for문으로 완전탐색
# 부분행렬 구하는 것도 공식을 통해..
ans = -400000001
for x1 in range(1, N+1):
    for y1 in range(1, M+1):
        for x2 in range(x1, N+1):
            for y2 in range(y1, M+1):
                ans = max(ans, prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][y1 - 1])
print(ans)
"""