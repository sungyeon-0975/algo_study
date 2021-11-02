"""
python
    Memory - 29 mb
    Time - 68 ms
"""

import sys
sys.stdin = open('input.txt')


IDX_CHANGE = {                  # 주사위가 움직이는 방향에 따라 주사위 리스트 자리 바꿀 인덱스
    0: [3, 1, 0, 5, 4, 2],      # 예) 주사위 오른쪽 이동시 (방향 0) -> 이동 전 바닥면(0)은 오른쪽면(3)이 된다
    1: [2, 1, 5, 0, 4, 3],      #                             -> 이동 전 앞면(1)은 앞면(1) 유지
    2: [1, 5, 2, 3, 0, 4],      #                             -> 이동 전 오른쪽면(2)은 아랫면(0)이 된다
    3: [4, 0, 2, 3, 5, 1],      #                             -> 이동 전 왼쪽면(3)은 윗면(5)이 된다......
}

dr = [0, 0, -1, 1]          # 오른쪽 / 왼쪽 / 위 / 아래
dc = [1, -1, 0, 0]

N, M, y, x, K = map(int, sys.stdin.readline().split())                      # 행 / 열 / 행좌표 / 열좌표 / 이동 개수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 초기 지도
move = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))          # 이동

now = [y, x]                                # 현재 주사위의 위치
dice = [0] * 6                              # 0-bottom / 1-front / 2-right / 3-left / 4-back / 5-top
dice_idx = {x:x for x in range(6)}          # 0-bottom / 1-front / 2-right / 3-left / 4-back / 5-top

answer = []
for e in move:                      # 이동 하나씩 순회
    r = now[0] + dr[e]              # 새로운 좌표
    c = now[1] + dc[e]
    
    if 0 <= r < N and 0 <= c < M:   # 새로운 좌표가 범위 내
        now[0], now[1] = r, c       # 주사위 현재 위치 갱신

        # 주사위 각면에 맞게 값 재배치
        dice[IDX_CHANGE[e][0]], dice[IDX_CHANGE[e][1]], dice[IDX_CHANGE[e][2]], dice[IDX_CHANGE[e][3]], dice[IDX_CHANGE[e][4]], dice[IDX_CHANGE[e][5]] = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

        if not board[r][c]:         # 지도에 값이 0이면
            board[r][c] = dice[0]   # 주사위 아랫면의 값이 지도로 복사
        else:                       # 지도에 값이 0 보다 크면
            dice[0] = board[r][c]   # 주사위 아랫면에 지도의 값 복사
            board[r][c] = 0         # 지도는 값이 0이 됨

        answer.append(dice[5])      # 윗면의 값 정답 리스트에 추가

for e in answer:        # 출력
    print(e)