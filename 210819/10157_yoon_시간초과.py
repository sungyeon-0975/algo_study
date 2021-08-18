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
        valid = 0 <= ni < C and 0 <= nj < R
        if valid and arr[ni][nj] == 0:
            arr[ni][nj] = num
            num += 1
            i, j = ni, nj
        else:
            w = (w+1) % 4

    if arr[i][j] == K:
        #print(i, j) # 행, 열 값이 각각 위치 바뀌고 기존 열+1, 행은 R-i
        print(j+1, R-i)

# 시간초과남... 제법 성질나요