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
            if 0 <= nx < N and 0<=ny<N


N = int(input())
data = list(list(map(int,input().split())) for _ in range(N))
