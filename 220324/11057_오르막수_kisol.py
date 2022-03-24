import sys

# KB / 72ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_11057.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [[0] * 10 for _ in range(N)]

    for i in range(1, N):
        dp[i][0] = 1

    for j in range(10):
        dp[0][j] = j + 1

    for i in range(1, N):
        for j in range(1, 10):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    print(dp[N - 1][9] % 10007)