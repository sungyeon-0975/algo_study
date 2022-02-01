import sys
sys.stdin = open('11062_input.txt')
# input = sys.stdin.readline

# https://deveun.tistory.com/entry/Python%EB%B0%B1%EC%A4%80-11062%EC%B9%B4%EB%93%9C%EA%B2%8C%EC%9E%84
# 이해 덜 됨

T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    turn = True if N % 2 else False
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N-i):
            if i == 0:
                if turn:
                    dp[j][i+j] = cards[j]
            elif turn:
                dp[j][i+j] = max(dp[j+1][i+j] + cards[j], dp[j][i+j-1] + cards[i+j])
            else:
                dp[j][i+j] = min(dp[j+1][i+j], dp[j][i+j-1])
        turn = not turn

    print(dp[0][N-1])
