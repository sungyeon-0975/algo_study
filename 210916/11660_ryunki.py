"""
70592kb , 1052ms

"""

import sys

# sys.stdin = open('input_11660.txt')
from itertools import accumulate

input = sys.stdin.readline

N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

# 누적합 가로
for i in range(N):
    data[i] = list(accumulate(data[i]))
# 누적합 세로
for i in range(1, N):
    for j in range(N):
        data[i][j] += data[i - 1][j]
for _ in range(M):
    x1, y1, x2, y2 = map(lambda x: x - 1, map(int, input().split()))
    answer = data[x2][y2]
    if y1 != 0:
        answer -= data[x2][y1 - 1]

    if x1 != 0:
        answer -= data[x1 - 1][y2]
    if y1 !=0 and x1 !=0:
        answer += data[x1 - 1][y1 - 1]
    print(answer)