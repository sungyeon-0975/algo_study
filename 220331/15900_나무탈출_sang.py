import sys


def dfs(node, cnt):
    global leaf
    visited[node] = 1

    if node != 1 and len(tr[node]) == 1:
        leaf += cnt

    for i in tr[node]:
        if not visited[i]:
            dfs(i, cnt + 1)


sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
tr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tr[a].append(b)
    tr[b].append(a)

visited = [0] * (n + 1)
leaf = 0
dfs(1, 0)

ans = "Yes" if leaf % 2 else "No"
print(ans)
