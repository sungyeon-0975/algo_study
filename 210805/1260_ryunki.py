import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().split())

matrix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    x,y = list(map(int,sys.stdin.readline().split()))
    matrix[x][y]=matrix[y][x]=1

def BFS(V):
    found = [V]
    queue = deque()
    queue.append(V)

    while queue:
        v = queue.popleft()
        print(v, end=' ')
    
        for i in range(len(matrix[V])):
           if matrix[v][i] == 1 and (i not in found):
             found.append(i)
             queue.append(i)

def DFS(V, found = []):
    
    found.append(V)
    print(V, end=' ')

    for i in range(len(matrix[V])):
        if matrix[V][i] == 1 and (i not in found):
            DFS(i,found)

DFS(V)
print()
BFS(V)

