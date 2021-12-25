import sys
sys.stdin = open('14503_input.txt')
# input = sys.stdin.readline

di = [-1, 0, 1, 0] # 상 좌 하 우
dj = [0, -1, 0, 1]

def solve(i, j, d):
    global answer
    for k in range(1, 5): # d + 1
        nd = (d + k) % 4
        ni = i + di[nd]
        nj = j + dj[nd]
        if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
            answer += 1
            arr[ni][nj] = 'c'
            solve(ni, nj, nd)
            break
    else:
        ni = i - di[d]
        nj = j - dj[d]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
            solve(ni, nj, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 1

arr[r][c] = 'c'
solve(r, c, d)

print(answer)