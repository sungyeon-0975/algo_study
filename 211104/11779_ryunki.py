import sys
sys.stdin = open('11779_input.txt')
"""
다익스트라 적용하기 위해 구글링... 이해가 안되네
"""
import heapq

def sol(start,end):
    dist = [1e9 for _ in range(N)]
    dist[start]=0
    path = [-1]*N
    q=[]
    heapq.heappush(q,[0,start])
    while q:
        cost, point = heapq.heappop(q)
        for x,y in graph[point]:
            y+=cost
            if y< dist[x]:
                dist[x]=y
                path[x]=point
                heapq.heappush(q,[y,x])
    return dist[end],path

N = int(input())
M = int(input())

graph = [[] for _ in range(N)]
for _ in range(M):
    S,E,C = map(int,input().split())
    graph[S-1].append([E-1,C])

start,end = map(int,input().split())

cost, point = sol(start-1,end-1)
path = [end-1]
temp = end-1
while point[temp] != -1:
    path.append(point[temp])
    temp = point[temp]

print(cost)
print(len(path))
for i in path[::-1]:
    print(i+1,end = ' ')