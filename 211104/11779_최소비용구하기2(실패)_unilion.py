import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from collections import deque
from copy import deepcopy
# 뭐가 틀린지 모르겠어유 ...
def dijkstra(start):
    heappush(heap, [start, 0])
    dist[start] = 0
    while heap:
        m, w = heappop(heap)
        if dist[m] < w: # 해당 if 문 구글링
            continue
        for num, wid in G[m]:
            new_w = w + wid
            if new_w < dist[num]:
                temp[num] = deepcopy(temp[m])
                temp[num].append(num)
                dist[num] = new_w
                heappush(heap, [num, new_w])

n = int(input())
m = int(input())
G = [deque() for _ in range(n + 1)]
dist = [1e6] * (n + 1)
heap = []
for _ in range(m):
    a, b, w = map(int, input().split())
    G[a].append([b, w])
start, end = map(int, input().split())
temp = [deque() for _ in range(n + 1)]
temp[start].append(start)
dijkstra(start)
print(dist[end])
print(len(temp[end]))
for i in temp[end]:
    print(i, end=" ")