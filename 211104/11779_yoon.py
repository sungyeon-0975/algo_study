import sys
sys.stdin = open('11779_input.txt')
# input = sys.stdin.readline
import heapq

# 54760KB / 388ms

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        for next, cost in arr[now]:
            temp = d + cost
            if temp < dist[next]:
                dist[next] = temp
                path[next].clear()
                for j in path[now]:
                    path[next].append(j)
                path[next].append(next)
                heapq.heappush(q, (temp, next))

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
dist = [987654321] * (n+1)
path = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, b = map(int, input().split())
    arr[s].append((e, b))
depart, arrive = map(int, input().split())

dist[depart] = 0
path[depart].append(depart)
dijkstra(depart)

print(dist[arrive])
print(len(path[arrive]))
print(' '.join(map(str, path[arrive])))