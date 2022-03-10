
from bisect import bisect_left

N = int(input())
lst = list(map(int, input().split()))
dp = [lst[0]]

for n in lst:
    if n > dp[-1]:
        dp.append(n)
    else:
        dp[bisect_left(dp, n)] = n

print(len(dp))
