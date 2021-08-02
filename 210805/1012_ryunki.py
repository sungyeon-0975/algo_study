import sys
from collections import deque
sys.setrecursionlimit(10000)

# DFS
def DFS(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for _ in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<N and 0<=ny<M:
            if Map[nx][ny] == 1:
                Map[nx][ny] = 0
                DFS(nx,ny)

T = int(sys.stdin.readline())
for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    Map = [[0]*M for _ in range(N)]

    warm = 0

    for i in range(K):
        m,n = map(int,sys.stdin.readline().split())
        Map[n][m] = 1
    
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 1:
                DFS(i,j)
                warm += 1
    
    print(warm)