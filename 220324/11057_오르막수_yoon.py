# import sys
# input = sys.stdin.readline

N = int(input())
dp = [1] * 10
for i in range(N-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]
print(sum(dp)%10007)