import sys
from collections import deque
sys.stdin = open('input.txt')

def solution(y, x):
    global answer

    q = deque([(y, x, H, 0)])                       # 좌표, 남은 체력, 남은 우산 내구도

    while q:
        y, x, h, u = q.popleft()
        for k in range(4):
            r = y + dr[k]                           # 다음 좌표들
            c = x + dc[k]

            if 0 <= r < N and 0 <= c < N:
                tmp_h = h                           # 현재 남은 체력과 우산 내구도를 임시 변수에 저장
                tmp_u = u

                if board[r][c] == 'E':              # 다음 좌표가 도착지점이면
                    answer = visited[y][x]          # 이동 거리 저장하고 종료
                    return
                elif board[r][c] == 'U':            # 다음 좌표가 우산이 있으면
                    tmp_u = D                       # 임시변수에 새로운 우산 내구도 적용

                if tmp_u > 0:                       # 우산 내구도가 남아있으면 우산 사용
                    tmp_u -= 1
                else:                               # 우산 없으면 체력 - 1
                    tmp_h -= 1
                    
                if tmp_h > 0:                       # 체력이 남아있다면
                    tmp = tmp_u + tmp_h             # 남은 체력 + 남은 우산 내구도

                    if dp[r][c] < tmp:                      # 다음 좌표에 기억된 체력 + 내구도 보다 현재 저장하려는 값이 더 큰 경우에만 진행
                        visited[r][c] = visited[y][x] + 1   # 한칸 이동
                        dp[r][c] = tmp                      # 새로운 체력 + 내구도 저장
                        q.append((r, c, tmp_h, tmp_u)) 


dr = [-1, 0, 1, 0]              # 상 우 하 좌
dc = [0, 1, 0, -1]

N, H, D = map(int, sys.stdin.readline().split())                    # 격자 길이, 현재 체력, 우산 내구도
board = [list(sys.stdin.readline().strip()) for _ in range(N)]      # U - 우산, S - 현재위치, E - 안전지대, . - 빈칸

visited = [[0] * N for _ in range(N)]       # 몇번째 이동인지 체크
dp = [[0] * N for _ in range(N)]            # 우산 + 체력이 얼마나 남아있는지 체크
answer = 1e10                               # 정답, 초기 값은 임의의 큰 수
end_flag = False                            # 종료를 알리는 신호 변수

for i in range(N):                          # 2차원 배열을 확인하며 시작점을 찾음
    for j in range(N):
        if board[i][j] == 'S':              # 시작점이면, 방문 처리 및 현재 체력 + 우산한 값을 저장
            visited[i][j] = 1
            dp[i][j] = H
            solution(i, j)
            end_flag = True
            break
    if end_flag:
        break

if answer >= 1e10:          # 도착지에 못가면 -1 반환
    print('-1')
else:                       # 출력
    print(answer)