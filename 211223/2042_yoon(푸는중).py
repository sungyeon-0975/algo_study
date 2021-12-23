import sys
sys.stdin = open('2042_input.txt')
# input = sys.stdin.readline

N, M, K = map(int, input().split())
num = [0] * (N+1)
for i in range(1, N+1):
    num[i] = num[i-1] + int(input())
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        for j in range(b, N+1):
            num[j] = num[j] - b + c
    else:
        print(num[c] - num[b-1])