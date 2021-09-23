import sys

# 133696KB / 404ms
# input = sys.stdin.readline
sys.stdin = open('input_11725.txt')
sys.setrecursionlimit(10**6)

def dfs(start):
    global parents
    visited[start] = 1
    for w in G[start]:
        if not visited[w]:
            parents[w] = start
            dfs(w)

T = int(input())

for t in range(T):
    N = int(input())
    G = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    parents = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    dfs(1)
    for i in range(2, N + 1):
        print(parents[i])
