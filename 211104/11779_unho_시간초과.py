"""
1. dijkstra 이용하면 내가 어디를 방문했는지 알수없는데, 이걸 어떻게 처리할것인가
    -> 우선 출발지에서 도착지로 최소 비용을 구함
    -> MST ? 

2. BFS 이용하여 탐색
"""


"""
python, pypy3
시간 초과
"""
import sys
sys.stdin = open('input.txt')


def dijkstra():
    for _ in range(N):
        min_idx = -1
        min_distance = 1e10

        for i in range(1, N+1):
            if not visited[i] and min_distance > distance[i]:
                min_idx = i
                min_distance = distance[i]
        visited[min_idx] = 1

        for e in bus.get(min_idx, []):
            if not visited[e[2]] and distance[e[2]] > distance[min_idx] + e[0]:
                distance[e[2]] = distance[min_idx] + e[0]
                route[e[2]].clear()
                route[e[2]] = route[e[1]][:] + [e[2]]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = {}
distance = [1e10] * (N+1)
visited = [0] * (N+1)
route = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, pay = map(int, sys.stdin.readline().split())
    bus[start] = bus.get(start, []) + [(pay, start, end)]

start, end = map(int, sys.stdin.readline().split())

distance[start] = 0
route[start] = [start]
dijkstra()
print(distance[end])
print(len(route[end]))
print(*route[end])



"""
dijkstra_heap
시간, 메모리 초과
"""
# import sys
# import heapq
# sys.stdin = open('input.txt')


# def dijkstra_heap():
#     global answer

#     heap = [(0, start, start)]
#     dp[start] = [0, [start]]

#     while heap:
#         node = heapq.heappop(heap)
#         if not dp[node[2]]:
#             dp[node[2]] = [dp[node[1]][0] + node[0], dp[node[1]][1][:] + [node[2]]]         # 도착지 dp = 출발지 최소거리 + 현재 최소거리 , 출발지까지 경로 + 현재 도착지
#         elif dp[node[2]][0] > dp[node[1]][0] + node[0]:
#             dp[node[2]] = [dp[node[1]][0] + node[0], dp[node[1]][1][:] + [node[2]]]

#         if bus:
#             for e in bus.get(node[2], []):
#                 heapq.heappush(heap, (e[0], e[1], e[2]))
#             if bus.get(node[2], []):
#                 bus.pop(node[2])
#         else:
#             for e in bus2.get(node[2], []):
#                 heapq.heappush(heap, (e[0], e[1], e[2]))
#             if bus2.get(node[2], []):
#                 bus2.pop(node[2])


# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())

# bus = {}
# bus2 = {}
# visited = [0] * (N+1)
# dp = [[] for _ in range(N+1)]

# route = []

# for _ in range(M):
#     start, end, pay = map(int, sys.stdin.readline().split())
#     bus[start] = bus.get(start, []) + [(pay, start, end)]
#     bus2[start] = bus2.get(start, []) + [(pay, start, end)]

# start, end = map(int, sys.stdin.readline().split())


# dijkstra_heap()
# print(dp[end][0])
# print(len(dp[end][1]))
# print(*dp[end][1])