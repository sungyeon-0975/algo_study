import sys
# input = sys.stdin.readline
sys.stdin = open('input_13458.txt')

'''
143644KB / 884ms 뭐야 왜 이렇게 거대해?
143644KB / 788ms
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    supervisor = 0

    for i in range(N):
        temp = A[i] - B # 변수로 받아줘서 최대한 줄여보려 함
        if temp <= 0:
            supervisor += 1
        else:
            if temp % C:
                supervisor += (temp // C) + 2
            else:
                supervisor += (temp // C) + 1

    print(supervisor)