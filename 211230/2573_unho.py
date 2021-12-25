"""
Python
    Memory - 32 MB
    Time - 3.504 s
"""

import sys
sys.stdin = open('input.txt')


def DFS(y, x, num):                                     # 좌표, 빙산 덩어리 번호
    stack = [(y, x)]                                    # 스택에 시작 좌표 추가

    while stack:                                        # 이어진 빙산이 있으면
        node = stack.pop()                              
        if not visited[node[0]][node[1]]:               # 현재 좌표가 아직 방문하지 않은 빙산인 경우
            visited[node[0]][node[1]] = num             # 빙산에 번호를 매김 (방문 처리)
            minus = 0                                   # 현재 위치 주변에 바다의 개수 카운트 위한 변수 
            for k in range(4):                          # 동서남북 탐색
                r = node[0] + dr[k]
                c = node[1] + dc[k]
                
                if not visited[r][c]:                   # 주변 좌표가 아직 방문하지 않았으면
                    if board[r][c] <= 0:                # 바다라면 바다 개수 증가
                        minus += 1
                    elif board[r][c]:                   # 빙산이면, 다음 탐색을 위해 스택에 추가
                        stack.append((r, c))

            board[node[0]][node[1]] -= minus            # 현재 빙산이 주변 바다 개수만큼 녹음
            if board[node[0]][node[1]] <= 0:            # 녹아서 바다가 됬으면, 빙산 좌표가 있는 딕셔너리 변수에서 녹은걸로 표시
                coordinates[(node[0], node[1])] = 0


dr = [-1, 0, 1, 0]                  # 델타 탐색
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())                                   # 행의 개수, 열의 개수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]        # 빙산의 정보들
coordinates = {}                                                                # 좌표값들 저장하는 딕셔너리 변수 (Key-좌표 값, Value-빙산 존재 유무)
year = 0                                                                        # 년도

for i in range(1, N-1):                         # 초기에 2차원 배열을 한번 탐색하여 빙산이 존재하는 좌표 값 구함
    for j in range(1, M-1):                     # 추후 빙산이 있는 좌표 반복문의 횟수를 줄이기 위함
        if board[i][j]:
            coordinates[(i, j)] = 1


while sum(coordinates.values()) > 0:            # 빙산이 하나라도 존재하면 반복
    visited = [[0] * M for _ in range(N)]       # 빙산이 녹은걸 계산했는지 좌표 값 (좌표 방문 여부)
    num = 1                                     # 빙산 덩어리 번호

    for k, v in coordinates.items():            # 빙산이 있는 좌표 값만 반복
        if v and not visited[k[0]][k[1]]:       # 빙산이 있고, 아직 확인하지 않은 빙산일때
            if num == 2:                        # 만약에 빙산 덩어리가 2번 이면, 빙산이 두개 이상으로 분리 되었으므로 종료
                print(year)
                break
            DFS(k[0], k[1], num)                # DFS 탐색
            num += 1                            # 빙산 덩어리 하나 찾았으니, 빙산 번호 증가

    else:                                       # 빙산 덩어리가 하나이면
        year += 1                               # 시간 증가 및 다음 진행
        continue
    break                                       # 빙산 덩어리가 두개 이상으로 종료 되었으면, 전체 반복문도 종료

else:                                           # 빙산이 두개 이상으로 나누어지지 않으면 0 반환
    print(0)