"""
Python
    Memory - 29 MB
    Time - 1.796 s
"""
import sys
sys.stdin = open('2468_input.txt')


def dfs(y, x, h):                           # 좌표, 현재 물에 잠기는 높이
    stack = [(y, x)]                        # DFS 스택

    while stack:                            
        node = stack.pop()                  # 현재 좌표값
        if not visited[node[0]][node[1]]:   # 방문하지 않은곳이면
            visited[node[0]][node[1]] = 1   # 방문 처리

            for a in range(4):              # 상하좌우 이동
                r = node[0] + dr[a]
                c = node[1] + dc[a]

                if 0 <= r < N and 0 <= c < N and not visited[r][c] and board[r][c] > h:     # 새로운 좌표가 사각형 범위 안이고, 방문하지 않았고, 잠기는 높이보다 높을때만
                    stack.append((r, c))                                                    # DFS 스택에 추가


dr = [-1, 0, 1, 0]          # 델타이동 (상하좌우) 
dc = [0, 1, 0, -1]

N = int(sys.stdin.readline())                                               # 사각형의 크기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 사각형의 높이 값들

min_height = 101            # 최소 높이를 저장할 변수 (임의의 값)
max_height = 0              # 최대 높이를 저장할 변수 (임의의 값)
answer = 1                  # 정답 변수 (한군데도 물에 잠기지 않는 경우 안전한 구역은 무조건 1개)

for i in range(N):                          # 가장 높은 높이와 가장 낮은 높이를 각각 구함
    for j in range(N):
        if board[i][j] > max_height:
            max_height = board[i][j]
        elif board[i][j] < min_height:
            min_height = board[i][j]

for h in range(min_height, max_height+1):   # 가장 낮은 높이부터 잠기는 경우 ~ 가장 높은 높이가 잠기는 경우
    visited = [[0]*N for _ in range(N)]     # 방문 변수, 매번 새로운 높이가 잠기는 경우마다 새로 초기화
    tmp_answer = 0                          # 현재 높이가 잠기는 경우에 안전한 구역의 개수

    for i in range(N):                                   
        for j in range(N):
            if board[i][j] > h and not visited[i][j]:       # 현재 위치가 방문하지 않았고, 안전한 구역인 경우 DFS 탐색하여 인접한 안전한 구역을 이어줌
                tmp_answer += 1                             # 안전한 구역의 개수 카운트
                dfs(i, j, h)                                # DFS 함수 호출
    
    if answer < tmp_answer:                 # 현재 높이가 잠길때 가장 많은 안전한 구역이라면 새로 정답 갱신
        answer = tmp_answer

print(answer)