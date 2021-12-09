"""
31880kb, 1724ms
"""
from collections import deque
import sys
input = sys.stdin.readline
sys.stdin = open('2468_input.txt')

dx = [-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,cnt):
    queu = deque()
    queu.append((x,y))
    visited[x][y]=1

    while queu:
        x,y=queu.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < N and 0<=ny<N:
                if data[nx][ny] >= cnt and visited[nx][ny] ==0:
                    visited[nx][ny]=1
                    queu.append((nx,ny))


N = int(input())
data = list(list(map(int,input().split())) for _ in range(N))


answer = min(map(min,data)) 

for x in range(min(map(min,data)), max(map(max,data))+1):
    visited = [[0]*N for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            if data[i][j]>=x and visited[i][j] == 0:
                bfs(i,j,x)
                temp += 1
    if temp > answer:
        answer = temp
print(answer)