import sys
from collections import deque
sys.stdin = open('input.txt')

def solution():
    q = deque([(0, 0)])             # 시작
    visited[0][0] = 0               # 시작 방문처리

    while q:
        node = q.popleft()
        for k in range(4):
            r = node[0] + dr[k]     # 새로운 좌표
            c = node[1] + dc[k]

            if 0 <= r < N and 0 <= c < N and visited[node[0]][node[1]] < visited[r][c]:     # 다음에 움직일 좌표가 현재 좌표보다 더 많은 방을 바꾸었을 때
                visited[r][c] = visited[node[0]][node[1]]                                   # 다음 좌표는 현재 좌표의 값으로 갱신
                if not board[r][c]:                            # 검은 방이면 바꾸는 횟수 1 증가
                    visited[r][c] += 1
                q.append((r, c))                               # 다음 탐색
                

dr = [-1, 0, 1, 0]                  # 상 우 하 좌
dc = [0, 1, 0, -1]

N = int(sys.stdin.readline())       # 배열의 크기
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]        # 배열 입력
visited = [[1e10] * N for _ in range(N)]                                        # 방문 처리 및 검은방을 몇번 바꿔야하는지 카운트

solution()                      # 탐색

print(visited[N-1][N-1])        # 정답 출력