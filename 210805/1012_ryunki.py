import sys
from collections import deque
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

T = int(input())

def BFS(mymap,a,b):
    quen = deque()
    quen.append((a,b))
    mymap[a][b] = 0

    while quen:
        x,y = quen.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mymap[nx][ny] == 1:
                mymap[nx][ny] = 0
                quen.append((nx,ny))
    return

for i in range(T):
    warm = 0
    M,N,K = map(int,input().split())
    mymap = [[0]*M for _ in range(N)]

    for j in range(K):
        n,m = map(int,input().split())
        mymap[m][n] = 1
    
    for a in range(N):
        for b in range(M):
            if mymap[a][b] == 1:
                BFS(mymap,a,b)
                warm += 1
    print(warm)
    
# # DFS
# def DFS(x,y):
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]

#     for _ in range(4):
#         if x<0 or x>=N or y<0 or y>=M:
#             return False
#         nx = x+dx[i]
#         ny = y+dy[i]

#         if 0<=nx<N and 0<=ny<M:
#             if Map[nx][ny] == 1:
#                 Map[nx][ny] = 0
#                 DFS(nx,ny)
#                 return True
#     return False

# T = int(sys.stdin.readline())
# for _ in range(T):
#     M,N,K = mymap(int,sys.stdin.readline().split())
#     Map = [[0]*M for _ in range(N)]

#     warm = 0

#     for i in range(K):
#         m,n = mymap(int,sys.stdin.readline().split())
#         Map[n][m] = 1
    
#     for i in range(N):
#         for j in range(M):
#             if Map[i][j] == True:
#                 DFS(i,j)
#                 warm += 1
    
#     print(warm)