n = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(2, n+1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[-1])

