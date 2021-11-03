"""
python
    Memory - 57 mb
    Time - 0.4 s
"""

import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    heap = [(0, start, start)]              # 초기에 비용 0, 출발과 도착지를 같게 하여 초기에 세팅을 위함

    while heap:
        node = heapq.heappop(heap)          # 버스 정보 가져옴 (비용 / 출발 도시 / 도착 도시)
        if not visited[node[2]]:            # 도착하려는 도시를 아직 방문하지 않았으면 (아직 최소 비용을 구하지 못하였다면)
            visited[node[2]] = 1            # 방문 표시 및 현재 도시에서 출발하는게 해당 도착지로 가는 최소 비용이므로, 해당 도시로 가는 최소 비용 저장
            distance[node[2]] = node[0]
            route[node[2]] = route[node[1]][:] + [node[2]]      # 경로에 추가 
                                                                # 인덱스 도시까지 가는 최소 비용의 버스 노선 저장
            # print(f'----- CASE -----')
            # print(f'출발지 {node[1]} - 도착지 {node[2]} => 누적된 비용 {node[0]}')
            # for i in range(1, len(route)):
            #     if visited[i]:
            #         print(f'* {i}번 도시로 가는 최소 비용 {distance[i]} / 경로 {route[i]}')

            for e in bus[node[2]]:          # 도착 도시에서 다음으로 탑승 가능한 버스 찾아봄
                if not visited[e[2]]:       # 도착 도시에서 출발하여 그 다음 도착지로 가는게, 아직 안가본 도시만 힙에 추가
                    heapq.heappush(heap, (distance[node[2]]+e[0], e[1], e[2]))


N = int(sys.stdin.readline())           # 도시의 개수
M = int(sys.stdin.readline())           # 버스의 개수

bus = [[] for _ in range(N+1)]          # 버스 관계
distance = [1e10] * (N+1)               # 시작 도시에서 해당 도시로의 최소 거리
visited = [0] * (N+1)                   # 해당 도시로 가는 최소 비용 구했는지 여부
route = [[] for _ in range(N+1)]        # 해당 도시로 가는 최소 경로 담아두는 2차원 배열 (DP 개념 적용)

for _ in range(M):                                              # 버스 정보 리스트에 추가
    start, end, pay = map(int, sys.stdin.readline().split())
    bus[start].append((pay, start, end))                        # 출발 도시의 리스트에 (비용, 출발 도시, 도착 도시)

start, end = map(int, sys.stdin.readline().split())             # 문제에서 요구하는 출발 도시, 도착 도시

dijkstra()              # 다익스트라

print(distance[end])    # 출력
print(len(route[end]))
print(*route[end])