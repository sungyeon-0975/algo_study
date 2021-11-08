import sys
sys.stdin = open('11659_input.txt')
# input = sys.stdin.readline

# 39468KB / 328ms

N, M = map(int, input().split())
num = list(map(int, input().split()))
for k in range(1, N):
    num[k] = num[k] + num[k-1]
# print(num)
for _ in range(M):
    i, j = map(int, input().split())
    if i - 1 == 0:
        print(num[j-1])
    elif i == j:
        print(num[i-1] - num[i-2])
    else:
        print(num[j-1] - num[i-2])