import sys
sys.stdin = open('11779_input.txt')
# input = sys.stdin.readline
import heapq

# 리스트로 다시 풀어보기

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, idx = heapq.heappop(q)
        if d > dist[idx]:
            continue
        for i in range(1, n+1):
            if arr[idx][i] != 987654321:
                temp = d + arr[idx][i]
                if temp < dist[i]:
                    dist[i] = temp
                    path[i] = []
                    for j in path[idx]:
                        path[i].append(j)
                    path[i].append(i)
                    heapq.heappush(q, (temp, i))

n = int(input())
m = int(input())
arr = [[987654321] * (n+1) for _ in range(n+1)]
dist = [987654321] * (n+1)
path = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, b = map(int, input().split())
    arr[s][e] = b
depart, arrive = map(int, input().split())
dist[depart] = 0
path[depart].append(depart)
dijkstra(depart)
print(dist[arrive])
print(len(path[arrive]))
print(' '.join(map(str, path[arrive])))