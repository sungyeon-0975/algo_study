import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input.txt')


def bfs(node):
    global answer

    q = deque([node])
    visited[node[0]][node[1]] = 1                   # 시작점도 1번 이동으로 포함

    while q:
        node = q.popleft()
        answer += 1                                 # 이동 가능한 칸의 갯수 증가
        for k in START[tunnel[node[0]][node[1]]]:   # 현재 위치에서 이동 가능한 방향으로만 탐색
            y = node[0] + dr[k]
            x = node[1] + dc[k]

            if 0 <= y < N and 0 <= x < M and not visited[y][x] and tunnel[y][x] in DIRECTION[k]:    # 다음 좌표가 범위 안, 방문한적 없고, 다음 파이프가 연결되는 경우
                visited[y][x] = visited[node[0]][node[1]] + 1
                if visited[y][x] == L+1:            # 이동 가능한 거리 넘어서게 되면 종료
                    answer += len(q)                # 스택에 남아 있는 칸들도 모두 이동 가능하므로 모두 카운트
                    return
                q.append((y, x))                    # 이동 가능한 거리 안넘어가면 계속 추가하여 반복
                

START = {               # 현재 위치에 파이프의 종류에 따라 이동 가능한 방향
    1: [0, 1, 2, 3],    # 현재 위치가 1번 파이프면 0,1,2,3 방향 이동 가능
    2: [0, 2],          # 2번 파이프면 0,2 방향 이동 가능
    3: [1, 3],          # 3번 파이프면 1,3 방향 이동 가능
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [0, 3],
}

DIRECTION = {           # 이동할 칸에서 어떤 파이프가 있으면 움직일수 있는지 리스트
    0: [1, 2, 5, 6],    # 위쪽 칸에서 1,2,5,6 파이프가 있으면 이동 가능
    1: [1, 3, 6, 7],    # 오른쪽 칸에서 1,3,6,7 파이프가 있으면 이동 가능
    2: [1, 2, 4, 7],
    3: [1, 3, 4, 5],
}

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    answer = 0

    bfs((R, C))                         # start coordinate
    
    print('#{} {}'.format(tc, answer))