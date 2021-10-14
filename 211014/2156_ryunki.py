import sys
sys.stdin = open('input_2156.txt')
"""
29708KB, 488ms
"""
n = int(input())
data = [0] + list(int(input()) for _ in range(n))

dp = [0,data[1]]

if n > 1:
    dp.append(data[1] + data[2])
for i in range(3, n + 1):
    dp.append((max(dp[i - 1], dp[i - 2] + data[i] , dp[i - 3] + data[i - 1] + data[i]))) # 규칙찾기....
print(dp[n])
