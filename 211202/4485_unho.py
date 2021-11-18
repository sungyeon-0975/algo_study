"""
Python
    Memory - 31 MB
    Time - 0.168 s
"""


import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():                     # 다익스트라
    heap = [(cave[0][0], 0, 0)]     # 현재 위치의 잃는 금액 / 현재 위치

    while heap:
        node = heapq.heappop(heap)
        distance[node[1]][node[2]] = node[0]        # 현재 위치까지 오는데 잃는 최소 비용
        
        for k in range(4):          # 상하좌우
            r = node[1] + dr[k]     # 새로운 좌표
            c = node[2] + dc[k]

            if 0 <= r < N and 0 <= c < N and not visited[r][c]:     # 범위내이고 아직 방문하지 않았으면
                weight = cave[r][c] + distance[node[1]][node[2]]    # 현재 위치에서 다음칸으로 이동했을때 잃는 금액
                visited[r][c] = 1                                   # 방문처리
                heapq.heappush(heap, (weight, r, c))                # 최소힙에 추가
    return


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

case = 0                                # 테스트 케이스
while True:                             # 테스트 케이스 종료될때까지 반복
    N = int(sys.stdin.readline())       # 동굴의 크기
    if not N:                           # 테스트 케이스 종료인 경우
        break
    
    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]     # 동굴 정보
    distance = [[0]*N for _ in range(N)]                                        # 동굴의 각 위치별 소요되는 비용
    visited = [[0]*N for _ in range(N)]                                         # 동굴의 각 위치 방문 여부
    case += 1                                                                   # 케이스 번호 증가

    dijkstra()      # 다익스트라

    print(f'Problem {case}: {distance[N-1][N-1]}')      # 출력