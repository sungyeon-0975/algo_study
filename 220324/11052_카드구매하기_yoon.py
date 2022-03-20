import sys
sys.stdin = open('11052_input.txt')
# input = sys.stdin.readline

#

N = int(input())
packs = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = packs[1]
for i in range(2, N+1):
    pos = [packs[i]]
    for j in range(1, i):
        pos.append(dp[j] + dp[i-j])
    dp[i] = max(pos)
print(dp[N])