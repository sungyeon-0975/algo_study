import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                           # 필요한 카드의 개수
price = list(map(int, sys.stdin.readline().split()))    # 입력으로 주어지는 카드팩별 금액

dp = [0] * (N+1)                        # 카드의 개수별 최고 금액

for i in range(1, N+1):                 # 카드 N개까지 인덱스 반복
    cases = {price[i-1]}                # 카드 i개가 들어있는 팩을 하나 샀을 경우
    for j in range(1, i):               # 이전에 구한 카드 최대 개수들 조합
        cases.add(dp[j] + dp[i-j])      # ex. 5개 => 1 + 4, 2 + 3
    
    dp[i] = max(cases)                  # 최대 비용을 dp에 저장

print(dp[N])