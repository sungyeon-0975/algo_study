import sys
sys.stdin = open('18352_input.txt')
# input = sys.stdin.readline
import heapq

# 105900KB / 2660ms

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    while q:
        d, idx = heapq.heappop(q)
        if d > dist[idx]:
            continue
        for i in arr[idx]:
            c = d + 1
            if c < dist[i]:
                dist[i] = c
                heapq.heappush(q, (c, i))

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
dist = [N] * (N+1)
dist[X] = 0
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
res = dijkstra(X)
if K not in dist:
    print(-1)
else:
    for i in range(1, N+1):
        if dist[i] == K:
            print(i)