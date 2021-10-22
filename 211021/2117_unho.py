"""
최소한 이득을 봐야함 - 모든 
"""
import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(y, x):                      # BFS 팀색
    global tc_answer

    q = deque([(y, x)])
    k = 2                           # 최소한 크기가 2가 되야 함
    home_cost = 0                   # 집이 지불하는 비용 (초기에 0)
    visited[y][x] = 1               # 현재 시작점은 방문처리

    if home_coor.get((y, x)):       # 만약에 현재 시작점에도 집이 있으면, 집 지불비용 플러스
        home_cost += M

    while q:    
        node = q.popleft()
        for a in range(4):
            r = node[0] + dr[a]     
            c = node[1] + dc[a]

            if 0 <= r < N and 0 <= c < N and not visited[r][c]:
                if visited[node[0]][node[1]] + 1 == k:              # 한단계 레벨을 모두 방문하면
                    tmp = home_cost - ((k-1)**2 + (k-2)**2)         # 집지불비용 - 방범비용
                    if 0 <= tmp and tc_answer <= home_cost:         # 이득을 보고, 현재 저장된 집 수익보다 크면 새로 저장
                        tc_answer = home_cost
                        
                    k += 1              # 다음단계
                
                if home_coor.get((r, c)):   # 확인하는 좌표에 집이 있으면
                    home_cost += M          # 집 지불 비용 추가

                visited[r][c] = visited[node[0]][node[1]] + 1       # 방문처리
                q.append((r, c))
    
    tmp = home_cost - ((k-1)**2 + (k-2)**2)                         # while 문 종료되고 마지막 단계도 확인을 해줘야함
    if 0 <= tmp and tc_answer <= home_cost:
        tc_answer = home_cost
    



dr = [-1, 0 ,1 ,0]      # 델타 탐색을 위한 할당
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N, M = map(int, input().split())                                    # length of array / cost each home
    village = [list(map(int, input().split())) for _ in range(N)]       # 마을의 정보
    home_coor = {}                                                      # 집 위치
    
    min_cost = 1e10             # 최소 비용 (임의의 큰 값)
    tc_answer = 0               # 홈방범 서비스를 제공하는 집들의 개수

    for i in range(N):                  # 2차원 배열을 순회하여 집들의 좌표값을 키로 하는 딕셔너리 변수에 저장
        for j in range(N):              # 해당 좌표에 집의 유무를 나태내기 위함
            if village[i][j]:
                home_coor[(i, j)] = 1


    for i in range(N):                              # 2차원 배열의 모든 좌표를 돌면서 경우의 수 탐색
        for j in range(N):                          # 방문 여부를 담는 변수 매번 초기화
            visited = [[0] * N for _ in range(N)]
            bfs(i, j)

    answer.append('#{} {}'.format(tc, tc_answer//M))
print(*answer, sep='\n')