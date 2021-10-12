import sys
sys.stdin = open('input.txt')


N = int(sys.stdin.readline())
li = [0]                        # 인덱스 편의를 위함

for _ in range(N):
    li.append(int(sys.stdin.readline()))

dp = [0] * (N+1)

dp[1] = li[1]               # 첫번째는 하나만
if N >= 2:                  # 두번째는 첫번째 + 두번째
    dp[2] = dp[1] + li[2]

for idx in range(3, N+1):       # 현재 인덱스를 포함하지 않는 경우 / 현재 인덱스 하나만 포함하는 경우 / 현재 인덱스와 바로 앞에 인덱스 (2개) 포함하는 경우
    dp[idx] = max(dp[idx-1], dp[idx-2] + li[idx], dp[idx-3] + li[idx] + li[idx-1])
    

print(max(dp))