import sys
# input = sys.stdin.readline
sys.stdin = open('input_11811.txt')

'''
37028KB / 464ms
'''

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = [0] * N

    for i in range(N):
        for j in range(N):
            if i != j and arr[i][j]:
                num[i] = num[i] | arr[i][j]

    print(*num)