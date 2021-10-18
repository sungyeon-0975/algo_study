import sys
sys.stdin = open('input_9251.txt')
"""
29200KB, 280ms
누적합으로 풀이 가능
"""
N = input()
M = input()
n, m = len(N), len(M)

dp = [0] * m

for i in range(n):
    temp = 0
    for j in range(m):
        if temp < dp[j]:
            temp = dp[j]
        elif N[i] == M[j]:
            dp[j] = temp + 1
        print(dp)

print(max(dp))
