# 432ms, 138540KB
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(idx, tree, parents):
    for i in tree[idx]:
        if parents[i] == 0:
            parents[i] = idx
            DFS(i, tree, parents)

N = int(input())
tree = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

DFS(1, tree, parents)

for i in range(2, N + 1):
    print(parents[i])