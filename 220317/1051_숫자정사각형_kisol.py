import sys
import math

# KB / 76ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_1051.txt')


def square():
    global res
    min_l = 1

    for i in range(N):
        for j in range(M):
            max_l = min(N - i, M - j)
            for l in range(min_l, max_l):
                if arr[i][j] == arr[i + l][j] == arr[i][j + l] == arr[i + l][j + l]:
                    res = l + 1
                    min_l = l + 1
                    if res == limit_l:
                        return


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())  # 행, 열 길이
    arr = [list(input()) for _ in range(N)]
    limit_l = min(N, M)
    res = 1

    if limit_l > 1:
        square()

    print(res ** 2)