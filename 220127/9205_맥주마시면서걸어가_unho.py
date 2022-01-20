import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())       # 테스트케이스 개수

for _ in range(T):
    N = int(sys.stdin.readline())   # 편의점의 개수

    start = list(map(int, sys.stdin.readline().split()))                                # 집의 좌표
    coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(N+1)]    # 편의점, 목적지 좌표

    visited = [0] * (N+1)               # 편의점과 목적지를 방문했는지 여부
    can_move = set()                    # 맥주 마시며 갈수 있는 장소들 집합

    q = deque([start])
    while q:
        node = q.pop()
        can_move.add(tuple(node))       # 현재 위치를 갈 수 있는 집합에 추가 

        for i in range(N+1):
            if not visited[i] and abs(coordinates[i][0] - node[0]) + abs(coordinates[i][1] - node[1]) <= 1000:      # 아직 확인하지 않은 장소이고, 맥주 20병으로 갈 수 있는 거리인 경우
                visited[i] = 1                      # 확인 체크
                q.append(coordinates[i])            # 다음 확인을 위해 추가

    if tuple(coordinates[-1]) in can_move:      # 목적지에 갈 수 있으면 happy 출력
        print('happy')
    else:
        print('sad')