import sys
input = sys.stdin.readline

# 가로 C, 세로 R
C, R = map(int, input().split())
K = int(input())

arr = [[0] * C for _ in range(R)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

i, j, w = R, 0, 0
num = 1

if K > C * R:
    print(0)
else:
    while num <= K: # 달팽이 채워주기
        ni = i + di[w]
        nj = j + dj[w]

        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0:
            arr[ni][nj] = num
            num += 1
            i, j = ni, nj
        else:
            w = (w+1) % 4

    print(j+1, R-i)