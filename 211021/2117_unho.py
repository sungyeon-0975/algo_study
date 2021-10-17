"""
최소한 이득을 봐야함 - 모든 
"""
import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(y, x):
    global tc_answer

    q = deque([(y, x)])
    k = 2
    home_cost = 0
    visited[y][x] = 1

    if home_coor.get((y, x)):
        home_cost += M

    while q:
        node = q.popleft()
        for a in range(4):
            r = node[0] + dr[a]
            c = node[1] + dc[a]

            if 0 <= r < N and 0 <= c < N and not visited[r][c]:
                if visited[node[0]][node[1]] + 1 == k:              # 한단계 레벨을 모두 방문하면
                    tmp = home_cost - ((k-1)**2 + (k-2)**2)
                    if 0 <= tmp and tc_answer <= home_cost:
                        tc_answer = home_cost
                        
                    k += 1
                
                if home_coor.get((r, c)):
                    home_cost += M

                visited[r][c] = visited[node[0]][node[1]] + 1
                q.append((r, c))
    
    tmp = home_cost - ((k-1)**2 + (k-2)**2)
    if 0 <= tmp and tc_answer <= home_cost:
        tc_answer = home_cost
    



dr = [-1, 0 ,1 ,0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N, M = map(int, input().split())        # length of array / cost each home
    village = [list(map(int, input().split())) for _ in range(N)]
    home_coor = {}                              # 집 위치
    
    min_cost = 1e10
    tc_answer = 0

    for i in range(N):
        for j in range(N):
            if village[i][j]:
                home_coor[(i, j)] = 1


    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            bfs(i, j)

    answer.append('#{} {}'.format(tc, tc_answer//M))
print(*answer, sep='\n')