"""
Python
    Memory - 29 MB
    Time - 0.068 s
"""
import sys
sys.stdin = open('input.txt')


def DFS(y, x, direction):                                       # 좌표, 바라보는 방향
    global answer

    for k in range(1, 5):                                       # 왼쪽 방향을 4번 확인 해야 하므로 4번 반복
        new_direction = (direction - k) % 4                     # 새로운 방향은 현재 방향에서 (델타값 - 1)을 4로 나눈 나머지 값
        r = y + dr[new_direction]                               # 새로운 좌표 (행, 열)
        c = x + dc[new_direction]

        if 0 <= r < N and 0 <= c < M and not board[r][c]:       # 사각형 범위 내이고, 다른 방향의 앞에 청소가 되어 있지 않으면
            board[r][c] = 2                                     # 다음 위치 청소 및 청소한 구역 카운트 1 증가
            answer += 1
            DFS(r, c, new_direction)                            # 다음 위치 및 바라보는 방향으로 재귀 호출하여 탐색
            break

    else:                                                       # 네 방향 모두 청소가 되어 있거나, 벽인 경우 (break를 만나지 않으면 실행)
        r = y + dr[(direction+2) % 4]                           # 뒤로 이동하는 새로운 좌표 (행, 열)
        c = x + dc[(direction+2) % 4]
        
        if 0 <= r < N and 0 <= c < M and board[r][c] != 1:      # 후진하는 좌표가 범위 내이고, 벽이 아니면
            DFS(r, c, direction)                                # 진행 방향은 유지한채로 1칸 후진


N, M = map(int, sys.stdin.readline().split())                               # 세로, 가로
R, C, D = map(int, sys.stdin.readline().split())                            # x 좌표, y 좌표, 방향 (0-북, 1-동, 2-남, 3-서)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 지도 (0-빈칸, 1-벽)
answer = 1                                                                  # 청소한 구역을 저장하는 변수 (초기에 시작하자마자 현재 위치를 청소하므로 1로 초기화)

dr = [-1, 0, 1, 0]          # 델타 탐색을 위한 네가지 방향 설정 (북, 동, 남, 서)
dc = [0, 1, 0, -1]

board[R][C] = 2             # 초기 위치 청소 시작
DFS(R, C, D)                # DFS 탐색

print(answer)               # 정답 출력