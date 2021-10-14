import sys

# 29200KB / 316ms
# input = sys.stdin.readline
'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
1) X가 3으로 나누어 떨어지면, 3으로 나눈다.
2) X가 2로 나누어 떨어지면, 2로 나눈다.
3) 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력
'''
sys.stdin = open('input_1463.txt')


def dfs(N):
    if N == 1:
        return 0
    if DP[N]:
        return DP[N]
    DP[N] = dfs(N - 1) + 1
    if N % 3 == 0:
        DP[N] = min(DP[N], dfs(N // 3) + 1)
    if N % 2 == 0:
        DP[N] = min(DP[N], dfs(N // 2) + 1)
    return DP[N]

T = int(input())

for _ in range(T):
    N = int(input())

    DP = [0] * (N + 1)
    print(dfs(N))
