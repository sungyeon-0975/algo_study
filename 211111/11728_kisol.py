import sys

# 343344KB / 1636ms pypy3
# 184088KB / 2352ms
# input = sys.stdin.readline
'''

'''
sys.stdin = open('input_11728.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    i = j = 0  # A, B idx
    while i < N and j < M:
        if A[i] < B[j]:
            print(A[i], end=' ')
            i += 1
        else:
            print(B[j], end=' ')
            j += 1

    if i < N:
        print(*A[i:])
    else:
        print(*B[j:])