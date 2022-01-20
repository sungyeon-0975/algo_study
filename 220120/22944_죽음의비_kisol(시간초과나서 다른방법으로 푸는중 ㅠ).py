import sys
sys.setrecursionlimit(10**6)
# KB / 864ms
# input = sys.stdin.readline
'''
출력 초과 => strip() 
시간 초과 => 각 문자가 어느 위치에 사용됐었는지 판단
'''

sys.stdin = open('input_22944.txt')

def bfs(r, c):
    global min_move

    Q = [(r, c)]

    

    if move == min_move:
        return

    if arr[r][c] == 'E':
        min_move = move
        return

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and move < visited[nr][nc]:
            visited[nr][nc] = move + 1
            if arr[nr][nc] == 'U':
                dfs(nr, nc, move + 1, hp, D)
            elif umbrella:
                dfs(nr, nc, move + 1, hp, umbrella - 1)
            elif hp > 1:
                dfs(nr, nc, move + 1, hp - 1, umbrella)


T = int(input())

for _ in range(T):
    N, H, D = map(int, input().split())  # N: 한변의 길이, H: 현재 체력, D: 우산 내구도
    arr = [list(input()) for _ in range(N)]  # S: 시작, U: 우산, E: 도착
    visited = [[N * N] * N for _ in range(N)]
    min_move = 987654321
    dr = [0, 1, 0, -1] # 우하좌상
    dc = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'S':
                visited[i][j] = 0
                dfs(i, j, 0, H, 0)
                break

    if min_move == 987654321:
        print(-1)
    else:
        print(min_move)


# def dfs(r, c, move, hp, umbrella):
#     global min_move
#
#     if move == min_move:
#         return
#
#     if arr[r][c] == 'E':
#         min_move = move
#         return
#
#     for d in range(4):
#         nr, nc = r + dr[d], c + dc[d]
#         if 0 <= nr < N and 0 <= nc < N and move < visited[nr][nc]:
#             visited[nr][nc] = move + 1
#             if arr[nr][nc] == 'U':
#                 dfs(nr, nc, move + 1, hp, D)
#             elif umbrella:
#                 dfs(nr, nc, move + 1, hp, umbrella - 1)
#             elif hp > 1:
#                 dfs(nr, nc, move + 1, hp - 1, umbrella)
#
#
# T = int(input())
#
# for _ in range(T):
#     N, H, D = map(int, input().split())  # N: 한변의 길이, H: 현재 체력, D: 우산 내구도
#     arr = [list(input()) for _ in range(N)]  # S: 시작, U: 우산, E: 도착
#     visited = [[N * N] * N for _ in range(N)]
#     min_move = 987654321
#     dr = [0, 1, 0, -1] # 우하좌상
#     dc = [1, 0, -1, 0]
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'S':
#                 visited[i][j] = 0
#                 dfs(i, j, 0, H, 0)
#                 break
#
#     if min_move == 987654321:
#         print(-1)
#     else:
#         print(min_move)