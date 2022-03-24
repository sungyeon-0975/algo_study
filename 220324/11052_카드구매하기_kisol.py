import sys

# KB / 260ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_11052.txt')


T = int(input())

for _ in range(T):
    N = int(input())
    P = [0] + list(map(int, input().split()))
    dp = P[:]

    for i in range(1, N + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], dp[i - j] + P[j])

    print(dp[N])