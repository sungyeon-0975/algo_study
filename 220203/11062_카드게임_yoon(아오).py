import sys
sys.stdin = open('11062_input.txt')
# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [0] * N
    i, j = 0, N - 1

    for k in range(N):
        if cards[i] > cards[j]:
            temp = cards[i]
            i += 1
        else:
            temp = cards[j]
            j -= 1
        if k < 2:
            dp[k] = temp
        else:
            dp[k] = dp[k-2] + temp

    print(dp)
    if N % 2:
        print(dp[-1])
    else:
        print(dp[-2])