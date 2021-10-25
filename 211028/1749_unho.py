import sys
from pprint import pprint
sys.stdin = open('input.txt')


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
accumulate_sum = [[0] * (M+1) for _ in range(N+1)]
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        accumulate_sum[i][j] = board[i-1][j-1] + accumulate_sum[i-1][j] + accumulate_sum[i][j-1] - accumulate_sum[i-1][j-1]

answer = accumulate_sum[1][1]

for i in range(1, N+1):
    for j in range(1, M+1):
        if answer < accumulate_sum[i][j]:
            answer = accumulate_sum[i][j]

print(answer)

"""
pypy3
Memory - 125892 kb
Time - 4364 ms
"""

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# accumulate_sum = [[0] * (M+1) for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, M+1):
#         accumulate_sum[i][j] = board[i-1][j-1] + accumulate_sum[i-1][j] + accumulate_sum[i][j-1] - accumulate_sum[i-1][j-1]

# answer = accumulate_sum[1][1]

# for i in range(1, N+1):
#     for j in range(1, M+1):
#         for r in range(i, N+1):
#             for c in range(j, N+1):
#                 tmp = accumulate_sum[i-1][j-1] + accumulate_sum[r][c] - accumulate_sum[r][j-1] - accumulate_sum[i-1][c]
#                 if tmp > answer:
#                     answer = tmp

# print(answer)