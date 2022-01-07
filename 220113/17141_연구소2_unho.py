import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')


def BFS(starts):                            # 너비 우선 탐색
    global remain_empty

    visited = [[0] * N for _ in range(N)]   # 좌표 방문 여부 체크 리스트
    q = deque(starts)
    
    for n in q:                             # 첫 시작점 방문 체크
        visited[n[0]][n[1]] = 1

    while q:
        node = q.popleft()
        for k in range(4):    
            r = node[0] + dr[k]             # 상하좌우 새로운 좌표
            c = node[1] + dc[k]

            if 0 <= r < N and 0 <= c < N and not visited[r][c] and board[r][c] != 1:    # 범위가 보드 안에 있고, 벽이 아니라면
                visited[r][c] = visited[node[0]][node[1]] + 1                           # 방문처리 및 거리 증가
                remain_empty -= 1                                                       # 비어있는 공간 카운트 마이너스
                q.append((r, c))                                                        # 다음 탐색을 위한 추가
    
    return visited[node[0]][node[1]] - 1        # 모든 칸을 채우는데 필요한 시간 반환


dr = [-1, 0, 1, 0]      # 상 우 하 좌
dc = [0, 1, 0, -1]


N, M = map(int, sys.stdin.readline().split())                               # 연구소의 크기, 놓을 수 있는 바이러스의 개수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 연구소의 상태

start_coordinates = []                                  # 바이러스 시작 가능한 좌표
empty_cnt = 0                                           # 비어있는 공간
answer = 1e10                                           # 정답 (최소 시간)

for i in range(N):                                      # 연구소 한번 전체 반복하여
    for j in range(N):                                  # 바이러스 놓을 수 있는 공간과
        if board[i][j] == 2:                            # 빈 공간 + 바이러스 공간 개수 확인하기
            start_coordinates.append((i, j))
            empty_cnt += 1
        elif board[i][j] == 0:
            empty_cnt += 1

for element in combinations(start_coordinates, M):      # 시작 좌표들 조합 구하기
    remain_empty = empty_cnt - M                        # 남은 빈 공간은 (빈 + 바이러스 놓을 수 있는 공간) - 바이러스 놓는 공간
    tmp = BFS(element)                                  # 모든 칸에 바이러스를 놓는데 소요 되는 시간

    if tmp < answer and not remain_empty:               # 최소 시간이 갱신되고, 남은 빈 공간이 없으면 정답 갱신
        answer = tmp

if answer == 1e10:      # 정답이 임의의 최댓값이면 빈 공간이 계속 남았으므로 -1 출력
    print(-1)
else:                   # 정답 출력
    print(answer)