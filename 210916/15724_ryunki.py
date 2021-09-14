"""
70560KB 844ms
"""
import sys

from itertools import accumulate

sys.stdin = open('input_15724.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    data[i] = list(accumulate(data[i]))

for i in range(1, N):
    for j in range(M):
        data[i][j] += data[i - 1][j]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(lambda x: x - 1, map(int, input().split()))
    answer = data[x2][y2]
    if y1 != 0:
        answer -= data[x2][y1 - 1]
    if x1 != 0:
        answer -= data[x1 - 1][y2]

    if x1 != 0 and y1 != 0:
        answer += data[x1 - 1][y1 - 1]

    print(answer)
