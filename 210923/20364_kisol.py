import sys
import math

# 39764KB / 2092ms
# input = sys.stdin.readline
sys.stdin = open('input_20364.txt')

def dfs(t, land, n):
    if t <= N:
        if not visited[t]:
            if t == land:
                visited[t] = 1
                print(0)
                return
            dfs(land // (2 ** (n - 1)), land, n - 1)
        else:
            print(t)
            return


N, Q = map(int, input().split())
visited = [0] * (N + 1)

for _ in range(Q):
    land = int(input())
    dfs(1, land, int(math.log2(land)))
