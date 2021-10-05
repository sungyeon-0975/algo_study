import sys
sys.stdin = open('input_2115.txt')

T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    honey = [[0] * (N-M+1) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            temp = arr[i][j:j+M]

    # 미완