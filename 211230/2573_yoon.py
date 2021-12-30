import sys
sys.stdin = open('2573_input.txt')
# input = sys.stdin.readline

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(r, c):
    cnt = 0 # 한 판 끝나고 melt 할 칸 세기
    for k in range(4):
        ci = r + dir[k][0]
        cj = c + dir[k][1]
        if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 0:
            cnt += 1
    melt[r][c] = cnt

    for l in range(4):
        ni = r + dir[l][0]
        nj = c + dir[l][1]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and melt[ni][nj] == 0:
            dfs(ni, nj)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
melt = [[0] * M for _ in range(N)]
answer = 0

ice = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and melt[i][j] == 0:
            dfs(i, j)
            ice += 1

while ice == 1:
    for i in range(N):
        for j in range(M):
            if arr[i][j] > melt[i][j]:
                arr[i][j] -= melt[i][j]
            else:
                arr[i][j] = 0

    melt = [[0] * M for _ in range(N)]
    ice = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and melt[i][j] == 0:
                dfs(i, j)
                ice += 1