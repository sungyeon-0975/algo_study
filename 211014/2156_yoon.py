import sys
# input = sys.stdin.readline
sys.stdin = open('input_2156.txt')

# 29078KB / 84ms

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
dp = [0] * n
dp[0] = wine[0]
try:
    dp[1] = dp[0] + wine[1]
    dp[2] = max(wine[1] + wine[2], wine[0] + wine[2], dp[1])
    for i in range(3, n):
        # 0+2+3, 1+3, 1+2
        dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i], dp[i - 1])
except:
    pass

print(dp[n-1])