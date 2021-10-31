from heapq import heappop, heappush
# 구글링해서 공부하면서 쳤는데, 왜 그 사람 코드는 통과하고 나는 시간 초과..?
def dijkstra(x):
    heappush(heap, [x, 0])
    dist[x] = 0
    while heap:
        n, w = heappop(heap)
        for num, wei in G[n]:
            new_wei = wei + w
            if new_wei < dist[num]:
                dist[num] = new_wei
                heappush(heap, [num, new_wei])

N, M, K, X = map(int, input().split())
G = [[] for _ in range(N + 1)]
dist = [1e6] * (N + 1)
heap = []
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append([b, 1])

dijkstra(X)
result = []
for i in range(1, N + 1):
    if dist[i] == K:
        result.append(i)

if result:
    for r in result:
        print(r)
else:
    print(-1)


# BFS 통과
# import sys
# input = sys.stdin.readline
# from collections import deque
# # 266616KB, 7456ms bfs로 풀기...
# def bfs(x, K):
#     global result
#     stack = deque()
#     stack.append((x, 0))
#     while stack:
#         y, cnt = stack.popleft()
#         for j in range(1, N + 1):
#             if not visited[j] and j in temp_list[y]:
#                 cnt2 = cnt
#                 visited[j] = 1
#                 cnt2 += 1
#                 if cnt2 > K:
#                     return
#                 if cnt2 == K:
#                     result.add(j)
#                 stack.append((j,cnt2))
#
# N, M, K, X = map(int, input().split())
# N_list = [list(map(int, input().split())) for _ in range(M)]
# temp_list = [[] for _ in range(N + 1)]
# result = set()
# for i in range(M):
#     temp_list[N_list[i][0]].append(N_list[i][1])
# visited = [0] * (N + 1)
# visited[X] = 1
# bfs(X, K)
# if not result:
#     print(-1)
# else:
#     temp = []
#     for r in result:
#         temp.append(r)
#     temp.sort()
#     for t in temp:
#         print(t)