"""
Python
    Memory - 40 MB
    Time - 2.932 ~ 3.944 s

PyPy3
    Memory - 130 MB
    Time - 0.288 s
"""


import sys
sys.stdin = open('input.txt')


dr = [-1, 0, 1, 0]          # 상 / 우 / 하 / 좌
dc = [0, 1, 0, -1]

SAND = {                    # 모래 이동 관련
    (-1, 1, 0): 0.01,       # 키 - 진행방향 기준 오른쪽 왼쪽 구분, 곱하는 횟수, 진행하는 방향의 곱하는 횟수
    (1, 1, 0): 0.01,        # 값 - 각 비율
    (-1, 1, 1): 0.07,
    (1, 1, 1): 0.07,
    (-1, 1, 2): 0.1,
    (1, 1, 2): 0.1,
    (-1, 2, 1): 0.02,
    (1, 2, 1): 0.02,
    (0, 0, 3): 0.05,
}

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
direction = 3                           # 진행방향
answer = 0                              # 격자 밖으로 나간 모래들

y = N//2                                # 시작 좌표
x = N//2
visited[y][x] = 1                       # 시작 좌표 방문처리

while y != 0 or x != 0:                 # 토네이도가 0,0 에 도달하면 종료
    r = y + dr[direction]               # 토네이도가 새로 이동하는 좌표 및 방문처리
    c = x + dc[direction]
    visited[r][c] = 1
    remove_sand = 0                     # 날아가는 모래의 양

    for k, v in SAND.items():                                                   # 딕셔너리
        nr = y + (dr[(direction+k[0])%4] * k[1]) + (dr[direction] * k[2])       # 모래가 흩어지는 상대적 위치들 계산
        nc = x + (dc[(direction+k[0])%4] * k[1]) + (dc[direction] * k[2])
        

        remove_sand += int(board[r][c] * v)                                     # 비율대로 흩어지는 양들 합산
        if 0 <= nr < N and 0 <= nc < N:                                         # 격자 내부이면 새로운 위치에 합산
            board[nr][nc] += int(board[r][c] * v)
        else:                                                                   # 격자 밖으로 나가면 모래 카운트
            answer += int(board[r][c] * v)
    
    nr = y + dr[direction]*2                                # 알파값 좌표
    nc = x + dc[direction]*2
    if 0 <= nr < N and 0 <= nc < N:
        board[nr][nc] += (board[r][c] - remove_sand)        # 날아가고 남은 모래들이 이동됨
    else:
        answer += (board[r][c] - remove_sand)               # 격자 밖이면 정답에 합산

    if not visited[r+dr[(direction-1)%4]][c+dc[(direction-1)%4]]:       # 토네이도의 현재 위치의 왼쪽 좌표를 방문하지 않았으면 왼쪽으로 방향 전환
        direction = (direction-1) % 4
    y = r
    x = c

print(answer)